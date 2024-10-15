# SNMP MIB module (CISCO-CCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:07 2024
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
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCcmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156)
)
ciscoCcmMIB.setRevisions(
        ("2010-07-07 00:00",
         "2009-12-03 00:00",
         "2008-08-21 00:00",
         "2008-02-12 00:00",
         "2005-09-14 00:00",
         "2005-05-09 00:00",
         "2004-08-02 00:00",
         "2003-08-25 00:00",
         "2003-05-08 00:00",
         "2002-01-11 00:00",
         "2000-12-01 00:00",
         "2000-03-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcmIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CcmIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CcmDevFailCauseCode(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("authenticationError", 10),
          ("callManagerReset", 9),
          ("connectivityError", 6),
          ("databaseConfigurationError", 3),
          ("deviceInitiatedReset", 8),
          ("deviceNameUnresolveable", 4),
          ("directoryNumberMismatch", 13),
          ("initializationError", 7),
          ("invalidTLSCipher", 12),
          ("invalidX509NameInCertificate", 11),
          ("malformedRegisterMsg", 14),
          ("maxDevRegReached", 5),
          ("noEntryInDatabase", 2),
          ("noError", 0),
          ("unknown", 1))
    )



class CcmDevRegFailCauseCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              23,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("addressingModeMismatch", 33),
          ("authenticatedDeviceAlreadyExists", 17),
          ("authenticationError", 10),
          ("autoRegisterDBConfigTimeout", 31),
          ("autoRegisterDBError", 29),
          ("callManagerReset", 9),
          ("capabilityResponseTimeout", 27),
          ("connectivityError", 6),
          ("databaseConfigurationError", 3),
          ("databaseTimeout", 23),
          ("dbAccessError", 30),
          ("deviceInitiatedReset", 8),
          ("deviceNameUnresolveable", 4),
          ("deviceNotActive", 16),
          ("deviceTypeMismatch", 32),
          ("directoryNumberMismatch", 13),
          ("initializationError", 7),
          ("invalidCapabilities", 26),
          ("invalidTLSCipher", 12),
          ("invalidX509NameInCertificate", 11),
          ("malformedRegisterMsg", 14),
          ("maxDevRegExceeded", 5),
          ("noEntryInDatabase", 2),
          ("noError", 0),
          ("obsoleteProtocolVersion", 18),
          ("protocolMismatch", 15),
          ("registrationSequenceError", 25),
          ("securityMismatch", 28),
          ("unknown", 1))
    )



class CcmDevUnregCauseCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("callManagerApplyConfig", 17),
          ("callManagerForcedRestart", 22),
          ("callManagerReset", 9),
          ("callManagerRestart", 15),
          ("configurationMismatch", 14),
          ("connectivityError", 6),
          ("databaseConfigurationError", 3),
          ("deviceInitiatedReset", 8),
          ("deviceNameUnresolveable", 4),
          ("deviceNoResponse", 18),
          ("deviceSwitch", 29),
          ("deviceUnregistered", 10),
          ("duplicateRegistration", 16),
          ("emLoginLogout", 19),
          ("emccLoginLogout", 20),
          ("energywisePowerSavePlus", 21),
          ("fallbackInitiated", 28),
          ("initializationError", 7),
          ("invalidCapabilities", 26),
          ("keepAliveTimeout", 13),
          ("malformedRegisterMsg", 11),
          ("maxDevRegExceeded", 5),
          ("noEntryInDatabase", 2),
          ("noError", 0),
          ("registrationSequenceError", 25),
          ("sccpDeviceThrottling", 12),
          ("sourceIPAddrChanged", 23),
          ("sourcePortChanged", 24),
          ("unknown", 1))
    )



class CcmDeviceStatus(Integer32, TextualConvention):
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
        *(("partiallyregistered", 5),
          ("registered", 2),
          ("rejected", 4),
          ("unknown", 1),
          ("unregistered", 3))
    )



class CcmPhoneProtocolType(Integer32, TextualConvention):
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
        *(("sccp", 2),
          ("sip", 3),
          ("unknown", 1))
    )



class CcmDeviceLineStatus(Integer32, TextualConvention):
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
        *(("registered", 2),
          ("rejected", 4),
          ("unknown", 1),
          ("unregistered", 3))
    )



class CcmSIPTransportProtocolType(Integer32, TextualConvention):
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
        *(("tcp", 2),
          ("tcpAndUdp", 4),
          ("tls", 5),
          ("udp", 3),
          ("unknown", 1))
    )



class CcmDeviceProductId(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2,
              3,
              4,
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
              27,
              43,
              44,
              45,
              46,
              47,
              49,
              52,
              55,
              58,
              59,
              62,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              75,
              76,
              77,
              80,
              81,
              90,
              95,
              10001,
              20000,
              20002,
              30004,
              30005,
              30006,
              30007,
              30011,
              30019,
              30020)
        )
    )
    namedValues = NamedValues(
        *(("gwyCisco1751", 30020),
          ("gwyCisco1760", 30019),
          ("gwyCisco269X", 30011),
          ("gwyCisco26XX", 44),
          ("gwyCisco362X", 45),
          ("gwyCisco364X", 46),
          ("gwyCisco366X", 47),
          ("gwyCisco3725", 20002),
          ("gwyCisco3745", 20000),
          ("gwyCiscoAS2", 13),
          ("gwyCiscoAS4", 14),
          ("gwyCiscoAS8", 15),
          ("gwyCiscoAT2", 10),
          ("gwyCiscoAT4", 11),
          ("gwyCiscoAT8", 12),
          ("gwyCiscoATA186", 69),
          ("gwyCiscoCat4000AccessGwyModule", 59),
          ("gwyCiscoCat4224VoiceGwySwitch", 58),
          ("gwyCiscoCat6000AVVIDServModule", 80),
          ("gwyCiscoCat6KE1", 2),
          ("gwyCiscoCat6KFXO", 4),
          ("gwyCiscoCat6KFXS", 3),
          ("gwyCiscoCat6KT1", 1),
          ("gwyCiscoDT24", 9),
          ("gwyCiscoDT24Plus", 7),
          ("gwyCiscoDT30Plus", 8),
          ("gwyCiscoIAD2400", 62),
          ("gwyCiscoICS77XXASI160", 72),
          ("gwyCiscoICS77XXASI81", 71),
          ("gwyCiscoICS77XXMRP2XX", 70),
          ("gwyCiscoICS77XXMRP316FXS", 30006),
          ("gwyCiscoICS77XXMRP38FXOM1", 30007),
          ("gwyCiscoICS77XXMRP38FXS", 30005),
          ("gwyCiscoICS77XXMRP3XX", 30004),
          ("gwyCiscoMGCPBRIPort", 90),
          ("gwyCiscoMGCPE1Port", 55),
          ("gwyCiscoMGCPFXOPort", 18),
          ("gwyCiscoMGCPFXSPort", 19),
          ("gwyCiscoMGCPT1Port", 52),
          ("gwyCiscoSlotVGCPort", 67),
          ("gwyCiscoVG200", 43),
          ("gwyCiscoVG224AndV248", 66),
          ("gwyCiscoVGCBox", 68),
          ("gwyCiscoVGCEndPoint", 65),
          ("gwyCiscoWSSVCCMMMS", 10001),
          ("gwyCiscoWSX6600", 81),
          ("h323AnonymousGatewy", 49),
          ("h323H225GKControlledTrunk", 75),
          ("h323ICTGKControlled", 76),
          ("h323ICTNonGKControlled", 77),
          ("h323Phone", 16),
          ("h323Trunk", 17),
          ("other", -2),
          ("sipTrunk", 95),
          ("unknown", -1),
          ("voiceMailUOnePort", 27))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCcmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCcmMIBObjects = _CiscoCcmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1)
)
_CcmGeneralInfo_ObjectIdentity = ObjectIdentity
ccmGeneralInfo = _CcmGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1)
)
_CcmGroupTable_Object = MibTable
ccmGroupTable = _CcmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccmGroupTable.setStatus("current")
_CcmGroupEntry_Object = MibTableRow
ccmGroupEntry = _CcmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 1, 1)
)
ccmGroupEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmGroupIndex"),
)
if mibBuilder.loadTexts:
    ccmGroupEntry.setStatus("current")
_CcmGroupIndex_Type = CcmIndex
_CcmGroupIndex_Object = MibTableColumn
ccmGroupIndex = _CcmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 1, 1, 1),
    _CcmGroupIndex_Type()
)
ccmGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmGroupIndex.setStatus("current")


class _CcmGroupName_Type(SnmpAdminString):
    """Custom type ccmGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmGroupName_Type.__name__ = "SnmpAdminString"
_CcmGroupName_Object = MibTableColumn
ccmGroupName = _CcmGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 1, 1, 2),
    _CcmGroupName_Type()
)
ccmGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGroupName.setStatus("current")
_CcmGroupTftpDefault_Type = TruthValue
_CcmGroupTftpDefault_Object = MibTableColumn
ccmGroupTftpDefault = _CcmGroupTftpDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 1, 1, 3),
    _CcmGroupTftpDefault_Type()
)
ccmGroupTftpDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGroupTftpDefault.setStatus("current")
_CcmTable_Object = MibTable
ccmTable = _CcmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ccmTable.setStatus("current")
_CcmEntry_Object = MibTableRow
ccmEntry = _CcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1)
)
ccmEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmIndex"),
)
if mibBuilder.loadTexts:
    ccmEntry.setStatus("current")
_CcmIndex_Type = CcmIndex
_CcmIndex_Object = MibTableColumn
ccmIndex = _CcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 1),
    _CcmIndex_Type()
)
ccmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmIndex.setStatus("current")


class _CcmName_Type(SnmpAdminString):
    """Custom type ccmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmName_Type.__name__ = "SnmpAdminString"
_CcmName_Object = MibTableColumn
ccmName = _CcmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 2),
    _CcmName_Type()
)
ccmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmName.setStatus("current")


class _CcmDescription_Type(SnmpAdminString):
    """Custom type ccmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmDescription_Type.__name__ = "SnmpAdminString"
_CcmDescription_Object = MibTableColumn
ccmDescription = _CcmDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 3),
    _CcmDescription_Type()
)
ccmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmDescription.setStatus("current")


class _CcmVersion_Type(SnmpAdminString):
    """Custom type ccmVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CcmVersion_Type.__name__ = "SnmpAdminString"
_CcmVersion_Object = MibTableColumn
ccmVersion = _CcmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 4),
    _CcmVersion_Type()
)
ccmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVersion.setStatus("current")


class _CcmStatus_Type(Integer32):
    """Custom type ccmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_CcmStatus_Type.__name__ = "Integer32"
_CcmStatus_Object = MibTableColumn
ccmStatus = _CcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 5),
    _CcmStatus_Type()
)
ccmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmStatus.setStatus("current")
_CcmInetAddressType_Type = InetAddressType
_CcmInetAddressType_Object = MibTableColumn
ccmInetAddressType = _CcmInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 6),
    _CcmInetAddressType_Type()
)
ccmInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmInetAddressType.setStatus("current")
_CcmInetAddress_Type = InetAddress
_CcmInetAddress_Object = MibTableColumn
ccmInetAddress = _CcmInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 7),
    _CcmInetAddress_Type()
)
ccmInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmInetAddress.setStatus("current")


class _CcmClusterId_Type(SnmpAdminString):
    """Custom type ccmClusterId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmClusterId_Type.__name__ = "SnmpAdminString"
_CcmClusterId_Object = MibTableColumn
ccmClusterId = _CcmClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 8),
    _CcmClusterId_Type()
)
ccmClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmClusterId.setStatus("current")
_CcmInetAddress2Type_Type = InetAddressType
_CcmInetAddress2Type_Object = MibTableColumn
ccmInetAddress2Type = _CcmInetAddress2Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 9),
    _CcmInetAddress2Type_Type()
)
ccmInetAddress2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmInetAddress2Type.setStatus("current")
_CcmInetAddress2_Type = InetAddress
_CcmInetAddress2_Object = MibTableColumn
ccmInetAddress2 = _CcmInetAddress2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 2, 1, 10),
    _CcmInetAddress2_Type()
)
ccmInetAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmInetAddress2.setStatus("current")
_CcmGroupMappingTable_Object = MibTable
ccmGroupMappingTable = _CcmGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ccmGroupMappingTable.setStatus("current")
_CcmGroupMappingEntry_Object = MibTableRow
ccmGroupMappingEntry = _CcmGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 3, 1)
)
ccmGroupMappingEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmGroupIndex"),
    (0, "CISCO-CCM-MIB", "ccmIndex"),
)
if mibBuilder.loadTexts:
    ccmGroupMappingEntry.setStatus("current")
_CcmCMGroupMappingCMPriority_Type = Unsigned32
_CcmCMGroupMappingCMPriority_Object = MibTableColumn
ccmCMGroupMappingCMPriority = _CcmCMGroupMappingCMPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 3, 1, 1),
    _CcmCMGroupMappingCMPriority_Type()
)
ccmCMGroupMappingCMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCMGroupMappingCMPriority.setStatus("current")
_CcmRegionTable_Object = MibTable
ccmRegionTable = _CcmRegionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ccmRegionTable.setStatus("current")
_CcmRegionEntry_Object = MibTableRow
ccmRegionEntry = _CcmRegionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 4, 1)
)
ccmRegionEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmRegionIndex"),
)
if mibBuilder.loadTexts:
    ccmRegionEntry.setStatus("current")
_CcmRegionIndex_Type = CcmIndex
_CcmRegionIndex_Object = MibTableColumn
ccmRegionIndex = _CcmRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 4, 1, 1),
    _CcmRegionIndex_Type()
)
ccmRegionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmRegionIndex.setStatus("current")


class _CcmRegionName_Type(SnmpAdminString):
    """Custom type ccmRegionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmRegionName_Type.__name__ = "SnmpAdminString"
_CcmRegionName_Object = MibTableColumn
ccmRegionName = _CcmRegionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 4, 1, 2),
    _CcmRegionName_Type()
)
ccmRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRegionName.setStatus("current")
_CcmRegionPairTable_Object = MibTable
ccmRegionPairTable = _CcmRegionPairTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ccmRegionPairTable.setStatus("current")
_CcmRegionPairEntry_Object = MibTableRow
ccmRegionPairEntry = _CcmRegionPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 5, 1)
)
ccmRegionPairEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmRegionSrcIndex"),
    (0, "CISCO-CCM-MIB", "ccmRegionDestIndex"),
)
if mibBuilder.loadTexts:
    ccmRegionPairEntry.setStatus("current")
_CcmRegionSrcIndex_Type = CcmIndex
_CcmRegionSrcIndex_Object = MibTableColumn
ccmRegionSrcIndex = _CcmRegionSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 5, 1, 1),
    _CcmRegionSrcIndex_Type()
)
ccmRegionSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmRegionSrcIndex.setStatus("current")
_CcmRegionDestIndex_Type = CcmIndex
_CcmRegionDestIndex_Object = MibTableColumn
ccmRegionDestIndex = _CcmRegionDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 5, 1, 2),
    _CcmRegionDestIndex_Type()
)
ccmRegionDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmRegionDestIndex.setStatus("current")


class _CcmRegionAvailableBandWidth_Type(Integer32):
    """Custom type ccmRegionAvailableBandWidth based on Integer32"""
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
        *(("bwG711", 5),
          ("bwG723", 3),
          ("bwG729", 4),
          ("bwGSM", 6),
          ("bwWideband", 7),
          ("other", 2),
          ("unknown", 1))
    )


_CcmRegionAvailableBandWidth_Type.__name__ = "Integer32"
_CcmRegionAvailableBandWidth_Object = MibTableColumn
ccmRegionAvailableBandWidth = _CcmRegionAvailableBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 5, 1, 3),
    _CcmRegionAvailableBandWidth_Type()
)
ccmRegionAvailableBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRegionAvailableBandWidth.setStatus("current")
_CcmTimeZoneTable_Object = MibTable
ccmTimeZoneTable = _CcmTimeZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ccmTimeZoneTable.setStatus("current")
_CcmTimeZoneEntry_Object = MibTableRow
ccmTimeZoneEntry = _CcmTimeZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 6, 1)
)
ccmTimeZoneEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmTimeZoneIndex"),
)
if mibBuilder.loadTexts:
    ccmTimeZoneEntry.setStatus("current")
_CcmTimeZoneIndex_Type = CcmIndex
_CcmTimeZoneIndex_Object = MibTableColumn
ccmTimeZoneIndex = _CcmTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 6, 1, 1),
    _CcmTimeZoneIndex_Type()
)
ccmTimeZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmTimeZoneIndex.setStatus("current")


class _CcmTimeZoneName_Type(SnmpAdminString):
    """Custom type ccmTimeZoneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmTimeZoneName_Type.__name__ = "SnmpAdminString"
_CcmTimeZoneName_Object = MibTableColumn
ccmTimeZoneName = _CcmTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 6, 1, 2),
    _CcmTimeZoneName_Type()
)
ccmTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmTimeZoneName.setStatus("current")


class _CcmTimeZoneOffset_Type(Integer32):
    """Custom type ccmTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_CcmTimeZoneOffset_Type.__name__ = "Integer32"
_CcmTimeZoneOffset_Object = MibTableColumn
ccmTimeZoneOffset = _CcmTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 6, 1, 3),
    _CcmTimeZoneOffset_Type()
)
ccmTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmTimeZoneOffset.setStatus("obsolete")


class _CcmTimeZoneOffsetHours_Type(Integer32):
    """Custom type ccmTimeZoneOffsetHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_CcmTimeZoneOffsetHours_Type.__name__ = "Integer32"
_CcmTimeZoneOffsetHours_Object = MibTableColumn
ccmTimeZoneOffsetHours = _CcmTimeZoneOffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 6, 1, 4),
    _CcmTimeZoneOffsetHours_Type()
)
ccmTimeZoneOffsetHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmTimeZoneOffsetHours.setStatus("current")


class _CcmTimeZoneOffsetMinutes_Type(Integer32):
    """Custom type ccmTimeZoneOffsetMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-59, 59),
    )


_CcmTimeZoneOffsetMinutes_Type.__name__ = "Integer32"
_CcmTimeZoneOffsetMinutes_Object = MibTableColumn
ccmTimeZoneOffsetMinutes = _CcmTimeZoneOffsetMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 6, 1, 5),
    _CcmTimeZoneOffsetMinutes_Type()
)
ccmTimeZoneOffsetMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmTimeZoneOffsetMinutes.setStatus("current")
_CcmDevicePoolTable_Object = MibTable
ccmDevicePoolTable = _CcmDevicePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ccmDevicePoolTable.setStatus("current")
_CcmDevicePoolEntry_Object = MibTableRow
ccmDevicePoolEntry = _CcmDevicePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 7, 1)
)
ccmDevicePoolEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmDevicePoolIndex"),
)
if mibBuilder.loadTexts:
    ccmDevicePoolEntry.setStatus("current")
_CcmDevicePoolIndex_Type = CcmIndex
_CcmDevicePoolIndex_Object = MibTableColumn
ccmDevicePoolIndex = _CcmDevicePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 7, 1, 1),
    _CcmDevicePoolIndex_Type()
)
ccmDevicePoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmDevicePoolIndex.setStatus("current")


class _CcmDevicePoolName_Type(SnmpAdminString):
    """Custom type ccmDevicePoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmDevicePoolName_Type.__name__ = "SnmpAdminString"
_CcmDevicePoolName_Object = MibTableColumn
ccmDevicePoolName = _CcmDevicePoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 7, 1, 2),
    _CcmDevicePoolName_Type()
)
ccmDevicePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmDevicePoolName.setStatus("current")
_CcmDevicePoolRegionIndex_Type = CcmIndexOrZero
_CcmDevicePoolRegionIndex_Object = MibTableColumn
ccmDevicePoolRegionIndex = _CcmDevicePoolRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 7, 1, 3),
    _CcmDevicePoolRegionIndex_Type()
)
ccmDevicePoolRegionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmDevicePoolRegionIndex.setStatus("current")
_CcmDevicePoolTimeZoneIndex_Type = CcmIndexOrZero
_CcmDevicePoolTimeZoneIndex_Object = MibTableColumn
ccmDevicePoolTimeZoneIndex = _CcmDevicePoolTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 7, 1, 4),
    _CcmDevicePoolTimeZoneIndex_Type()
)
ccmDevicePoolTimeZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmDevicePoolTimeZoneIndex.setStatus("current")
_CcmDevicePoolGroupIndex_Type = CcmIndexOrZero
_CcmDevicePoolGroupIndex_Object = MibTableColumn
ccmDevicePoolGroupIndex = _CcmDevicePoolGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 7, 1, 5),
    _CcmDevicePoolGroupIndex_Type()
)
ccmDevicePoolGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmDevicePoolGroupIndex.setStatus("current")
_CcmProductTypeTable_Object = MibTable
ccmProductTypeTable = _CcmProductTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ccmProductTypeTable.setStatus("current")
_CcmProductTypeEntry_Object = MibTableRow
ccmProductTypeEntry = _CcmProductTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 8, 1)
)
ccmProductTypeEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmProductTypeIndex"),
)
if mibBuilder.loadTexts:
    ccmProductTypeEntry.setStatus("current")
_CcmProductTypeIndex_Type = CcmIndex
_CcmProductTypeIndex_Object = MibTableColumn
ccmProductTypeIndex = _CcmProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 8, 1, 1),
    _CcmProductTypeIndex_Type()
)
ccmProductTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmProductTypeIndex.setStatus("current")
_CcmProductType_Type = Unsigned32
_CcmProductType_Object = MibTableColumn
ccmProductType = _CcmProductType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 8, 1, 2),
    _CcmProductType_Type()
)
ccmProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmProductType.setStatus("current")


class _CcmProductName_Type(SnmpAdminString):
    """Custom type ccmProductName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CcmProductName_Type.__name__ = "SnmpAdminString"
_CcmProductName_Object = MibTableColumn
ccmProductName = _CcmProductName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 8, 1, 3),
    _CcmProductName_Type()
)
ccmProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmProductName.setStatus("current")


class _CcmProductCategory_Type(Integer32):
    """Custom type ccmProductCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
        *(("ctiDevice", 4),
          ("gateway", 2),
          ("h323Device", 3),
          ("huntListDevice", 7),
          ("mediaResourceDevice", 6),
          ("notApplicable", 0),
          ("phone", 1),
          ("sipDevice", 8),
          ("unknown", -1),
          ("voiceMailDevice", 5))
    )


_CcmProductCategory_Type.__name__ = "Integer32"
_CcmProductCategory_Object = MibTableColumn
ccmProductCategory = _CcmProductCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 1, 8, 1, 4),
    _CcmProductCategory_Type()
)
ccmProductCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmProductCategory.setStatus("current")
_CcmPhoneInfo_ObjectIdentity = ObjectIdentity
ccmPhoneInfo = _CcmPhoneInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2)
)
_CcmPhoneTable_Object = MibTable
ccmPhoneTable = _CcmPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccmPhoneTable.setStatus("current")
_CcmPhoneEntry_Object = MibTableRow
ccmPhoneEntry = _CcmPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1)
)
ccmPhoneEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmPhoneIndex"),
)
if mibBuilder.loadTexts:
    ccmPhoneEntry.setStatus("current")
_CcmPhoneIndex_Type = CcmIndex
_CcmPhoneIndex_Object = MibTableColumn
ccmPhoneIndex = _CcmPhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 1),
    _CcmPhoneIndex_Type()
)
ccmPhoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmPhoneIndex.setStatus("current")
_CcmPhonePhysicalAddress_Type = MacAddress
_CcmPhonePhysicalAddress_Object = MibTableColumn
ccmPhonePhysicalAddress = _CcmPhonePhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 2),
    _CcmPhonePhysicalAddress_Type()
)
ccmPhonePhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhonePhysicalAddress.setStatus("current")


class _CcmPhoneType_Type(Integer32):
    """Custom type ccmPhoneType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("cisco12S", 6),
          ("cisco12SP", 5),
          ("cisco12SPplus", 4),
          ("cisco30SPplus", 3),
          ("cisco30VIP", 7),
          ("cisco7902", 13),
          ("cisco7905", 14),
          ("cisco7912", 15),
          ("cisco7970", 16),
          ("ciscoConferencePhone", 12),
          ("ciscoSoftPhone", 11),
          ("ciscoTeleCasterBid", 8),
          ("ciscoTeleCasterBusiness", 10),
          ("ciscoTeleCasterMgr", 9),
          ("other", 2),
          ("unknown", 1))
    )


_CcmPhoneType_Type.__name__ = "Integer32"
_CcmPhoneType_Object = MibTableColumn
ccmPhoneType = _CcmPhoneType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 3),
    _CcmPhoneType_Type()
)
ccmPhoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneType.setStatus("obsolete")


class _CcmPhoneDescription_Type(SnmpAdminString):
    """Custom type ccmPhoneDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmPhoneDescription_Type.__name__ = "SnmpAdminString"
_CcmPhoneDescription_Object = MibTableColumn
ccmPhoneDescription = _CcmPhoneDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 4),
    _CcmPhoneDescription_Type()
)
ccmPhoneDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneDescription.setStatus("current")


class _CcmPhoneUserName_Type(SnmpAdminString):
    """Custom type ccmPhoneUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmPhoneUserName_Type.__name__ = "SnmpAdminString"
_CcmPhoneUserName_Object = MibTableColumn
ccmPhoneUserName = _CcmPhoneUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 5),
    _CcmPhoneUserName_Type()
)
ccmPhoneUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneUserName.setStatus("current")
_CcmPhoneIpAddress_Type = IpAddress
_CcmPhoneIpAddress_Object = MibTableColumn
ccmPhoneIpAddress = _CcmPhoneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 6),
    _CcmPhoneIpAddress_Type()
)
ccmPhoneIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneIpAddress.setStatus("obsolete")
_CcmPhoneStatus_Type = CcmDeviceStatus
_CcmPhoneStatus_Object = MibTableColumn
ccmPhoneStatus = _CcmPhoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 7),
    _CcmPhoneStatus_Type()
)
ccmPhoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatus.setStatus("current")
_CcmPhoneTimeLastRegistered_Type = DateAndTime
_CcmPhoneTimeLastRegistered_Object = MibTableColumn
ccmPhoneTimeLastRegistered = _CcmPhoneTimeLastRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 8),
    _CcmPhoneTimeLastRegistered_Type()
)
ccmPhoneTimeLastRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneTimeLastRegistered.setStatus("current")


class _CcmPhoneE911Location_Type(SnmpAdminString):
    """Custom type ccmPhoneE911Location based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmPhoneE911Location_Type.__name__ = "SnmpAdminString"
_CcmPhoneE911Location_Object = MibTableColumn
ccmPhoneE911Location = _CcmPhoneE911Location_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 9),
    _CcmPhoneE911Location_Type()
)
ccmPhoneE911Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneE911Location.setStatus("current")


class _CcmPhoneLoadID_Type(SnmpAdminString):
    """Custom type ccmPhoneLoadID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmPhoneLoadID_Type.__name__ = "SnmpAdminString"
_CcmPhoneLoadID_Object = MibTableColumn
ccmPhoneLoadID = _CcmPhoneLoadID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 10),
    _CcmPhoneLoadID_Type()
)
ccmPhoneLoadID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneLoadID.setStatus("current")


class _CcmPhoneLastError_Type(Integer32):
    """Custom type ccmPhoneLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CcmPhoneLastError_Type.__name__ = "Integer32"
_CcmPhoneLastError_Object = MibTableColumn
ccmPhoneLastError = _CcmPhoneLastError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 11),
    _CcmPhoneLastError_Type()
)
ccmPhoneLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneLastError.setStatus("obsolete")
_CcmPhoneTimeLastError_Type = DateAndTime
_CcmPhoneTimeLastError_Object = MibTableColumn
ccmPhoneTimeLastError = _CcmPhoneTimeLastError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 12),
    _CcmPhoneTimeLastError_Type()
)
ccmPhoneTimeLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneTimeLastError.setStatus("obsolete")
_CcmPhoneDevicePoolIndex_Type = CcmIndexOrZero
_CcmPhoneDevicePoolIndex_Object = MibTableColumn
ccmPhoneDevicePoolIndex = _CcmPhoneDevicePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 13),
    _CcmPhoneDevicePoolIndex_Type()
)
ccmPhoneDevicePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneDevicePoolIndex.setStatus("current")
_CcmPhoneInetAddressType_Type = InetAddressType
_CcmPhoneInetAddressType_Object = MibTableColumn
ccmPhoneInetAddressType = _CcmPhoneInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 14),
    _CcmPhoneInetAddressType_Type()
)
ccmPhoneInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneInetAddressType.setStatus("deprecated")
_CcmPhoneInetAddress_Type = InetAddress
_CcmPhoneInetAddress_Object = MibTableColumn
ccmPhoneInetAddress = _CcmPhoneInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 15),
    _CcmPhoneInetAddress_Type()
)
ccmPhoneInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneInetAddress.setStatus("deprecated")
_CcmPhoneStatusReason_Type = CcmDevFailCauseCode
_CcmPhoneStatusReason_Object = MibTableColumn
ccmPhoneStatusReason = _CcmPhoneStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 16),
    _CcmPhoneStatusReason_Type()
)
ccmPhoneStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusReason.setStatus("deprecated")
_CcmPhoneTimeLastStatusUpdt_Type = DateAndTime
_CcmPhoneTimeLastStatusUpdt_Object = MibTableColumn
ccmPhoneTimeLastStatusUpdt = _CcmPhoneTimeLastStatusUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 17),
    _CcmPhoneTimeLastStatusUpdt_Type()
)
ccmPhoneTimeLastStatusUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneTimeLastStatusUpdt.setStatus("current")
_CcmPhoneProductTypeIndex_Type = CcmIndexOrZero
_CcmPhoneProductTypeIndex_Object = MibTableColumn
ccmPhoneProductTypeIndex = _CcmPhoneProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 18),
    _CcmPhoneProductTypeIndex_Type()
)
ccmPhoneProductTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneProductTypeIndex.setStatus("current")
_CcmPhoneProtocol_Type = CcmPhoneProtocolType
_CcmPhoneProtocol_Object = MibTableColumn
ccmPhoneProtocol = _CcmPhoneProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 19),
    _CcmPhoneProtocol_Type()
)
ccmPhoneProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneProtocol.setStatus("current")


class _CcmPhoneName_Type(SnmpAdminString):
    """Custom type ccmPhoneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmPhoneName_Type.__name__ = "SnmpAdminString"
_CcmPhoneName_Object = MibTableColumn
ccmPhoneName = _CcmPhoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 20),
    _CcmPhoneName_Type()
)
ccmPhoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneName.setStatus("current")
_CcmPhoneInetAddressIPv4_Type = InetAddressIPv4
_CcmPhoneInetAddressIPv4_Object = MibTableColumn
ccmPhoneInetAddressIPv4 = _CcmPhoneInetAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 21),
    _CcmPhoneInetAddressIPv4_Type()
)
ccmPhoneInetAddressIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneInetAddressIPv4.setStatus("current")
_CcmPhoneInetAddressIPv6_Type = InetAddressIPv6
_CcmPhoneInetAddressIPv6_Object = MibTableColumn
ccmPhoneInetAddressIPv6 = _CcmPhoneInetAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 22),
    _CcmPhoneInetAddressIPv6_Type()
)
ccmPhoneInetAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneInetAddressIPv6.setStatus("current")


class _CcmPhoneIPv4Attribute_Type(Integer32):
    """Custom type ccmPhoneIPv4Attribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminAndControl", 3),
          ("adminOnly", 1),
          ("controlOnly", 2),
          ("unknown", 0))
    )


_CcmPhoneIPv4Attribute_Type.__name__ = "Integer32"
_CcmPhoneIPv4Attribute_Object = MibTableColumn
ccmPhoneIPv4Attribute = _CcmPhoneIPv4Attribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 23),
    _CcmPhoneIPv4Attribute_Type()
)
ccmPhoneIPv4Attribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneIPv4Attribute.setStatus("current")


class _CcmPhoneIPv6Attribute_Type(Integer32):
    """Custom type ccmPhoneIPv6Attribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminAndControl", 3),
          ("adminOnly", 1),
          ("controlOnly", 2),
          ("unknown", 0))
    )


_CcmPhoneIPv6Attribute_Type.__name__ = "Integer32"
_CcmPhoneIPv6Attribute_Object = MibTableColumn
ccmPhoneIPv6Attribute = _CcmPhoneIPv6Attribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 24),
    _CcmPhoneIPv6Attribute_Type()
)
ccmPhoneIPv6Attribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneIPv6Attribute.setStatus("current")
_CcmPhoneActiveLoadID_Type = SnmpAdminString
_CcmPhoneActiveLoadID_Object = MibTableColumn
ccmPhoneActiveLoadID = _CcmPhoneActiveLoadID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 25),
    _CcmPhoneActiveLoadID_Type()
)
ccmPhoneActiveLoadID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneActiveLoadID.setStatus("current")
_CcmPhoneUnregReason_Type = CcmDevUnregCauseCode
_CcmPhoneUnregReason_Object = MibTableColumn
ccmPhoneUnregReason = _CcmPhoneUnregReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 26),
    _CcmPhoneUnregReason_Type()
)
ccmPhoneUnregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneUnregReason.setStatus("current")
_CcmPhoneRegFailReason_Type = CcmDevRegFailCauseCode
_CcmPhoneRegFailReason_Object = MibTableColumn
ccmPhoneRegFailReason = _CcmPhoneRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 1, 1, 27),
    _CcmPhoneRegFailReason_Type()
)
ccmPhoneRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneRegFailReason.setStatus("current")
_CcmPhoneExtensionTable_Object = MibTable
ccmPhoneExtensionTable = _CcmPhoneExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccmPhoneExtensionTable.setStatus("obsolete")
_CcmPhoneExtensionEntry_Object = MibTableRow
ccmPhoneExtensionEntry = _CcmPhoneExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2, 1)
)
ccmPhoneExtensionEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmPhoneExtensionIndex"),
)
if mibBuilder.loadTexts:
    ccmPhoneExtensionEntry.setStatus("obsolete")
_CcmPhoneExtensionIndex_Type = CcmIndex
_CcmPhoneExtensionIndex_Object = MibTableColumn
ccmPhoneExtensionIndex = _CcmPhoneExtensionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2, 1, 1),
    _CcmPhoneExtensionIndex_Type()
)
ccmPhoneExtensionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmPhoneExtensionIndex.setStatus("obsolete")


class _CcmPhoneExtension_Type(SnmpAdminString):
    """Custom type ccmPhoneExtension based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CcmPhoneExtension_Type.__name__ = "SnmpAdminString"
_CcmPhoneExtension_Object = MibTableColumn
ccmPhoneExtension = _CcmPhoneExtension_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2, 1, 2),
    _CcmPhoneExtension_Type()
)
ccmPhoneExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtension.setStatus("obsolete")
_CcmPhoneExtensionIpAddress_Type = IpAddress
_CcmPhoneExtensionIpAddress_Object = MibTableColumn
ccmPhoneExtensionIpAddress = _CcmPhoneExtensionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2, 1, 3),
    _CcmPhoneExtensionIpAddress_Type()
)
ccmPhoneExtensionIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtensionIpAddress.setStatus("obsolete")
_CcmPhoneExtensionMultiLines_Type = Unsigned32
_CcmPhoneExtensionMultiLines_Object = MibTableColumn
ccmPhoneExtensionMultiLines = _CcmPhoneExtensionMultiLines_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2, 1, 4),
    _CcmPhoneExtensionMultiLines_Type()
)
ccmPhoneExtensionMultiLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtensionMultiLines.setStatus("obsolete")
_CcmPhoneExtensionInetAddressType_Type = InetAddressType
_CcmPhoneExtensionInetAddressType_Object = MibTableColumn
ccmPhoneExtensionInetAddressType = _CcmPhoneExtensionInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2, 1, 5),
    _CcmPhoneExtensionInetAddressType_Type()
)
ccmPhoneExtensionInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtensionInetAddressType.setStatus("obsolete")
_CcmPhoneExtensionInetAddress_Type = InetAddress
_CcmPhoneExtensionInetAddress_Object = MibTableColumn
ccmPhoneExtensionInetAddress = _CcmPhoneExtensionInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 2, 1, 6),
    _CcmPhoneExtensionInetAddress_Type()
)
ccmPhoneExtensionInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtensionInetAddress.setStatus("obsolete")
_CcmPhoneFailedTable_Object = MibTable
ccmPhoneFailedTable = _CcmPhoneFailedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ccmPhoneFailedTable.setStatus("current")
_CcmPhoneFailedEntry_Object = MibTableRow
ccmPhoneFailedEntry = _CcmPhoneFailedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1)
)
ccmPhoneFailedEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmPhoneFailedIndex"),
)
if mibBuilder.loadTexts:
    ccmPhoneFailedEntry.setStatus("current")
_CcmPhoneFailedIndex_Type = CcmIndex
_CcmPhoneFailedIndex_Object = MibTableColumn
ccmPhoneFailedIndex = _CcmPhoneFailedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 1),
    _CcmPhoneFailedIndex_Type()
)
ccmPhoneFailedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmPhoneFailedIndex.setStatus("current")
_CcmPhoneFailedTime_Type = DateAndTime
_CcmPhoneFailedTime_Object = MibTableColumn
ccmPhoneFailedTime = _CcmPhoneFailedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 2),
    _CcmPhoneFailedTime_Type()
)
ccmPhoneFailedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedTime.setStatus("current")


class _CcmPhoneFailedName_Type(SnmpAdminString):
    """Custom type ccmPhoneFailedName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmPhoneFailedName_Type.__name__ = "SnmpAdminString"
_CcmPhoneFailedName_Object = MibTableColumn
ccmPhoneFailedName = _CcmPhoneFailedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 3),
    _CcmPhoneFailedName_Type()
)
ccmPhoneFailedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedName.setStatus("obsolete")
_CcmPhoneFailedInetAddressType_Type = InetAddressType
_CcmPhoneFailedInetAddressType_Object = MibTableColumn
ccmPhoneFailedInetAddressType = _CcmPhoneFailedInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 4),
    _CcmPhoneFailedInetAddressType_Type()
)
ccmPhoneFailedInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedInetAddressType.setStatus("deprecated")
_CcmPhoneFailedInetAddress_Type = InetAddress
_CcmPhoneFailedInetAddress_Object = MibTableColumn
ccmPhoneFailedInetAddress = _CcmPhoneFailedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 5),
    _CcmPhoneFailedInetAddress_Type()
)
ccmPhoneFailedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedInetAddress.setStatus("deprecated")
_CcmPhoneFailCauseCode_Type = CcmDevFailCauseCode
_CcmPhoneFailCauseCode_Object = MibTableColumn
ccmPhoneFailCauseCode = _CcmPhoneFailCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 6),
    _CcmPhoneFailCauseCode_Type()
)
ccmPhoneFailCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailCauseCode.setStatus("deprecated")
_CcmPhoneFailedMacAddress_Type = MacAddress
_CcmPhoneFailedMacAddress_Object = MibTableColumn
ccmPhoneFailedMacAddress = _CcmPhoneFailedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 7),
    _CcmPhoneFailedMacAddress_Type()
)
ccmPhoneFailedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedMacAddress.setStatus("current")
_CcmPhoneFailedInetAddressIPv4_Type = InetAddressIPv4
_CcmPhoneFailedInetAddressIPv4_Object = MibTableColumn
ccmPhoneFailedInetAddressIPv4 = _CcmPhoneFailedInetAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 8),
    _CcmPhoneFailedInetAddressIPv4_Type()
)
ccmPhoneFailedInetAddressIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedInetAddressIPv4.setStatus("current")
_CcmPhoneFailedInetAddressIPv6_Type = InetAddressIPv6
_CcmPhoneFailedInetAddressIPv6_Object = MibTableColumn
ccmPhoneFailedInetAddressIPv6 = _CcmPhoneFailedInetAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 9),
    _CcmPhoneFailedInetAddressIPv6_Type()
)
ccmPhoneFailedInetAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedInetAddressIPv6.setStatus("current")


class _CcmPhoneFailedIPv4Attribute_Type(Integer32):
    """Custom type ccmPhoneFailedIPv4Attribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminAndControl", 3),
          ("adminOnly", 1),
          ("controlOnly", 2),
          ("unknown", 0))
    )


_CcmPhoneFailedIPv4Attribute_Type.__name__ = "Integer32"
_CcmPhoneFailedIPv4Attribute_Object = MibTableColumn
ccmPhoneFailedIPv4Attribute = _CcmPhoneFailedIPv4Attribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 10),
    _CcmPhoneFailedIPv4Attribute_Type()
)
ccmPhoneFailedIPv4Attribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedIPv4Attribute.setStatus("current")


class _CcmPhoneFailedIPv6Attribute_Type(Integer32):
    """Custom type ccmPhoneFailedIPv6Attribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminAndControl", 3),
          ("adminOnly", 1),
          ("controlOnly", 2),
          ("unknown", 0))
    )


_CcmPhoneFailedIPv6Attribute_Type.__name__ = "Integer32"
_CcmPhoneFailedIPv6Attribute_Object = MibTableColumn
ccmPhoneFailedIPv6Attribute = _CcmPhoneFailedIPv6Attribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 11),
    _CcmPhoneFailedIPv6Attribute_Type()
)
ccmPhoneFailedIPv6Attribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedIPv6Attribute.setStatus("current")
_CcmPhoneFailedRegFailReason_Type = CcmDevRegFailCauseCode
_CcmPhoneFailedRegFailReason_Object = MibTableColumn
ccmPhoneFailedRegFailReason = _CcmPhoneFailedRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 3, 1, 12),
    _CcmPhoneFailedRegFailReason_Type()
)
ccmPhoneFailedRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneFailedRegFailReason.setStatus("current")
_CcmPhoneStatusUpdateTable_Object = MibTable
ccmPhoneStatusUpdateTable = _CcmPhoneStatusUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateTable.setStatus("current")
_CcmPhoneStatusUpdateEntry_Object = MibTableRow
ccmPhoneStatusUpdateEntry = _CcmPhoneStatusUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1)
)
ccmPhoneStatusUpdateEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmPhoneStatusUpdateIndex"),
)
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateEntry.setStatus("current")
_CcmPhoneStatusUpdateIndex_Type = CcmIndex
_CcmPhoneStatusUpdateIndex_Object = MibTableColumn
ccmPhoneStatusUpdateIndex = _CcmPhoneStatusUpdateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1, 1),
    _CcmPhoneStatusUpdateIndex_Type()
)
ccmPhoneStatusUpdateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateIndex.setStatus("current")
_CcmPhoneStatusPhoneIndex_Type = CcmIndexOrZero
_CcmPhoneStatusPhoneIndex_Object = MibTableColumn
ccmPhoneStatusPhoneIndex = _CcmPhoneStatusPhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1, 2),
    _CcmPhoneStatusPhoneIndex_Type()
)
ccmPhoneStatusPhoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusPhoneIndex.setStatus("current")
_CcmPhoneStatusUpdateTime_Type = DateAndTime
_CcmPhoneStatusUpdateTime_Object = MibTableColumn
ccmPhoneStatusUpdateTime = _CcmPhoneStatusUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1, 3),
    _CcmPhoneStatusUpdateTime_Type()
)
ccmPhoneStatusUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateTime.setStatus("current")


class _CcmPhoneStatusUpdateType_Type(Integer32):
    """Custom type ccmPhoneStatusUpdateType based on Integer32"""
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
        *(("phonePartiallyregistered", 4),
          ("phoneRegistered", 2),
          ("phoneUnregistered", 3),
          ("unknown", 1))
    )


_CcmPhoneStatusUpdateType_Type.__name__ = "Integer32"
_CcmPhoneStatusUpdateType_Object = MibTableColumn
ccmPhoneStatusUpdateType = _CcmPhoneStatusUpdateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1, 4),
    _CcmPhoneStatusUpdateType_Type()
)
ccmPhoneStatusUpdateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateType.setStatus("current")
_CcmPhoneStatusUpdateReason_Type = CcmDevFailCauseCode
_CcmPhoneStatusUpdateReason_Object = MibTableColumn
ccmPhoneStatusUpdateReason = _CcmPhoneStatusUpdateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1, 5),
    _CcmPhoneStatusUpdateReason_Type()
)
ccmPhoneStatusUpdateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateReason.setStatus("deprecated")
_CcmPhoneStatusUnregReason_Type = CcmDevUnregCauseCode
_CcmPhoneStatusUnregReason_Object = MibTableColumn
ccmPhoneStatusUnregReason = _CcmPhoneStatusUnregReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1, 6),
    _CcmPhoneStatusUnregReason_Type()
)
ccmPhoneStatusUnregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusUnregReason.setStatus("current")
_CcmPhoneStatusRegFailReason_Type = CcmDevRegFailCauseCode
_CcmPhoneStatusRegFailReason_Object = MibTableColumn
ccmPhoneStatusRegFailReason = _CcmPhoneStatusRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 4, 1, 7),
    _CcmPhoneStatusRegFailReason_Type()
)
ccmPhoneStatusRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusRegFailReason.setStatus("current")
_CcmPhoneExtnTable_Object = MibTable
ccmPhoneExtnTable = _CcmPhoneExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ccmPhoneExtnTable.setStatus("current")
_CcmPhoneExtnEntry_Object = MibTableRow
ccmPhoneExtnEntry = _CcmPhoneExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5, 1)
)
ccmPhoneExtnEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmPhoneIndex"),
    (0, "CISCO-CCM-MIB", "ccmPhoneExtnIndex"),
)
if mibBuilder.loadTexts:
    ccmPhoneExtnEntry.setStatus("current")
_CcmPhoneExtnIndex_Type = CcmIndex
_CcmPhoneExtnIndex_Object = MibTableColumn
ccmPhoneExtnIndex = _CcmPhoneExtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5, 1, 1),
    _CcmPhoneExtnIndex_Type()
)
ccmPhoneExtnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmPhoneExtnIndex.setStatus("current")


class _CcmPhoneExtn_Type(SnmpAdminString):
    """Custom type ccmPhoneExtn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CcmPhoneExtn_Type.__name__ = "SnmpAdminString"
_CcmPhoneExtn_Object = MibTableColumn
ccmPhoneExtn = _CcmPhoneExtn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5, 1, 2),
    _CcmPhoneExtn_Type()
)
ccmPhoneExtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtn.setStatus("current")
_CcmPhoneExtnMultiLines_Type = Unsigned32
_CcmPhoneExtnMultiLines_Object = MibTableColumn
ccmPhoneExtnMultiLines = _CcmPhoneExtnMultiLines_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5, 1, 3),
    _CcmPhoneExtnMultiLines_Type()
)
ccmPhoneExtnMultiLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtnMultiLines.setStatus("current")
_CcmPhoneExtnInetAddressType_Type = InetAddressType
_CcmPhoneExtnInetAddressType_Object = MibTableColumn
ccmPhoneExtnInetAddressType = _CcmPhoneExtnInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5, 1, 4),
    _CcmPhoneExtnInetAddressType_Type()
)
ccmPhoneExtnInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtnInetAddressType.setStatus("current")
_CcmPhoneExtnInetAddress_Type = InetAddress
_CcmPhoneExtnInetAddress_Object = MibTableColumn
ccmPhoneExtnInetAddress = _CcmPhoneExtnInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5, 1, 5),
    _CcmPhoneExtnInetAddress_Type()
)
ccmPhoneExtnInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtnInetAddress.setStatus("current")
_CcmPhoneExtnStatus_Type = CcmDeviceLineStatus
_CcmPhoneExtnStatus_Object = MibTableColumn
ccmPhoneExtnStatus = _CcmPhoneExtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 2, 5, 1, 6),
    _CcmPhoneExtnStatus_Type()
)
ccmPhoneExtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtnStatus.setStatus("current")
_CcmGatewayInfo_ObjectIdentity = ObjectIdentity
ccmGatewayInfo = _CcmGatewayInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3)
)
_CcmGatewayTable_Object = MibTable
ccmGatewayTable = _CcmGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccmGatewayTable.setStatus("current")
_CcmGatewayEntry_Object = MibTableRow
ccmGatewayEntry = _CcmGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1)
)
ccmGatewayEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmGatewayIndex"),
)
if mibBuilder.loadTexts:
    ccmGatewayEntry.setStatus("current")
_CcmGatewayIndex_Type = CcmIndex
_CcmGatewayIndex_Object = MibTableColumn
ccmGatewayIndex = _CcmGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 1),
    _CcmGatewayIndex_Type()
)
ccmGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmGatewayIndex.setStatus("current")


class _CcmGatewayName_Type(SnmpAdminString):
    """Custom type ccmGatewayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmGatewayName_Type.__name__ = "SnmpAdminString"
_CcmGatewayName_Object = MibTableColumn
ccmGatewayName = _CcmGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 2),
    _CcmGatewayName_Type()
)
ccmGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayName.setStatus("current")


class _CcmGatewayType_Type(Integer32):
    """Custom type ccmGatewayType based on Integer32"""
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
              44)
        )
    )
    namedValues = NamedValues(
        *(("cisco1751", 43),
          ("cisco1760", 42),
          ("cisco269X", 41),
          ("cisco26XX", 17),
          ("cisco362X", 18),
          ("cisco364X", 19),
          ("cisco366X", 20),
          ("cisco3725", 36),
          ("cisco3745", 35),
          ("ciscoATA186", 27),
          ("ciscoAnalogAccess", 3),
          ("ciscoAnalogAccessWSX6612", 14),
          ("ciscoAnalogAccessWSX6624", 9),
          ("ciscoCat4000AccessGatewayModule", 22),
          ("ciscoCat4224VoiceGatewaySwitch", 21),
          ("ciscoCat6000AVVIDServModule", 32),
          ("ciscoDigitalAccessE1Plus", 11),
          ("ciscoDigitalAccessPRI", 4),
          ("ciscoDigitalAccessPRIPlus", 6),
          ("ciscoDigitalAccessT1", 5),
          ("ciscoDigitalAccessT1Plus", 12),
          ("ciscoDigitalAccessWSX6608E1", 7),
          ("ciscoDigitalAccessWSX6608PRI", 13),
          ("ciscoDigitalAccessWSX6608T1", 8),
          ("ciscoIAD2400", 23),
          ("ciscoICS77XXASI160", 30),
          ("ciscoICS77XXASI81", 29),
          ("ciscoICS77XXMRP2XX", 28),
          ("ciscoICS77XXMRP316FXS", 39),
          ("ciscoICS77XXMRP38FXOM1", 40),
          ("ciscoICS77XXMRP38FXS", 38),
          ("ciscoICS77XXMRP3XX", 37),
          ("ciscoMGCPBRIPort", 44),
          ("ciscoMGCPStation", 10),
          ("ciscoMGCPTrunk", 15),
          ("ciscoSlotVGCPort", 31),
          ("ciscoVG200", 16),
          ("ciscoVG224VG248Gateway", 25),
          ("ciscoVGCBox", 26),
          ("ciscoVGCEndPoint", 24),
          ("ciscoWSSVCCMMMS", 34),
          ("ciscoWSX6600", 33),
          ("other", 2),
          ("unknown", 1))
    )


_CcmGatewayType_Type.__name__ = "Integer32"
_CcmGatewayType_Object = MibTableColumn
ccmGatewayType = _CcmGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 3),
    _CcmGatewayType_Type()
)
ccmGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayType.setStatus("obsolete")


class _CcmGatewayDescription_Type(SnmpAdminString):
    """Custom type ccmGatewayDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmGatewayDescription_Type.__name__ = "SnmpAdminString"
_CcmGatewayDescription_Object = MibTableColumn
ccmGatewayDescription = _CcmGatewayDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 4),
    _CcmGatewayDescription_Type()
)
ccmGatewayDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayDescription.setStatus("current")
_CcmGatewayStatus_Type = CcmDeviceStatus
_CcmGatewayStatus_Object = MibTableColumn
ccmGatewayStatus = _CcmGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 5),
    _CcmGatewayStatus_Type()
)
ccmGatewayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayStatus.setStatus("current")
_CcmGatewayDevicePoolIndex_Type = CcmIndexOrZero
_CcmGatewayDevicePoolIndex_Object = MibTableColumn
ccmGatewayDevicePoolIndex = _CcmGatewayDevicePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 6),
    _CcmGatewayDevicePoolIndex_Type()
)
ccmGatewayDevicePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayDevicePoolIndex.setStatus("current")
_CcmGatewayInetAddressType_Type = InetAddressType
_CcmGatewayInetAddressType_Object = MibTableColumn
ccmGatewayInetAddressType = _CcmGatewayInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 7),
    _CcmGatewayInetAddressType_Type()
)
ccmGatewayInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayInetAddressType.setStatus("current")
_CcmGatewayInetAddress_Type = InetAddress
_CcmGatewayInetAddress_Object = MibTableColumn
ccmGatewayInetAddress = _CcmGatewayInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 8),
    _CcmGatewayInetAddress_Type()
)
ccmGatewayInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayInetAddress.setStatus("current")
_CcmGatewayProductId_Type = CcmDeviceProductId
_CcmGatewayProductId_Object = MibTableColumn
ccmGatewayProductId = _CcmGatewayProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 9),
    _CcmGatewayProductId_Type()
)
ccmGatewayProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayProductId.setStatus("obsolete")
_CcmGatewayStatusReason_Type = CcmDevFailCauseCode
_CcmGatewayStatusReason_Object = MibTableColumn
ccmGatewayStatusReason = _CcmGatewayStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 10),
    _CcmGatewayStatusReason_Type()
)
ccmGatewayStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayStatusReason.setStatus("deprecated")
_CcmGatewayTimeLastStatusUpdt_Type = DateAndTime
_CcmGatewayTimeLastStatusUpdt_Object = MibTableColumn
ccmGatewayTimeLastStatusUpdt = _CcmGatewayTimeLastStatusUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 11),
    _CcmGatewayTimeLastStatusUpdt_Type()
)
ccmGatewayTimeLastStatusUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayTimeLastStatusUpdt.setStatus("current")
_CcmGatewayTimeLastRegistered_Type = DateAndTime
_CcmGatewayTimeLastRegistered_Object = MibTableColumn
ccmGatewayTimeLastRegistered = _CcmGatewayTimeLastRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 12),
    _CcmGatewayTimeLastRegistered_Type()
)
ccmGatewayTimeLastRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayTimeLastRegistered.setStatus("current")


class _CcmGatewayDChannelStatus_Type(Integer32):
    """Custom type ccmGatewayDChannelStatus based on Integer32"""
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
        *(("active", 1),
          ("inActive", 2),
          ("notApplicable", 4),
          ("unknown", 3))
    )


_CcmGatewayDChannelStatus_Type.__name__ = "Integer32"
_CcmGatewayDChannelStatus_Object = MibTableColumn
ccmGatewayDChannelStatus = _CcmGatewayDChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 13),
    _CcmGatewayDChannelStatus_Type()
)
ccmGatewayDChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayDChannelStatus.setStatus("current")


class _CcmGatewayDChannelNumber_Type(Integer32):
    """Custom type ccmGatewayDChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 24),
    )


_CcmGatewayDChannelNumber_Type.__name__ = "Integer32"
_CcmGatewayDChannelNumber_Object = MibTableColumn
ccmGatewayDChannelNumber = _CcmGatewayDChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 14),
    _CcmGatewayDChannelNumber_Type()
)
ccmGatewayDChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayDChannelNumber.setStatus("current")
_CcmGatewayProductTypeIndex_Type = CcmIndexOrZero
_CcmGatewayProductTypeIndex_Object = MibTableColumn
ccmGatewayProductTypeIndex = _CcmGatewayProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 15),
    _CcmGatewayProductTypeIndex_Type()
)
ccmGatewayProductTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayProductTypeIndex.setStatus("current")
_CcmGatewayUnregReason_Type = CcmDevUnregCauseCode
_CcmGatewayUnregReason_Object = MibTableColumn
ccmGatewayUnregReason = _CcmGatewayUnregReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 16),
    _CcmGatewayUnregReason_Type()
)
ccmGatewayUnregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayUnregReason.setStatus("current")
_CcmGatewayRegFailReason_Type = CcmDevRegFailCauseCode
_CcmGatewayRegFailReason_Object = MibTableColumn
ccmGatewayRegFailReason = _CcmGatewayRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 3, 1, 1, 17),
    _CcmGatewayRegFailReason_Type()
)
ccmGatewayRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayRegFailReason.setStatus("current")
_CcmGatewayTrunkInfo_ObjectIdentity = ObjectIdentity
ccmGatewayTrunkInfo = _CcmGatewayTrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4)
)
_CcmGatewayTrunkTable_Object = MibTable
ccmGatewayTrunkTable = _CcmGatewayTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ccmGatewayTrunkTable.setStatus("obsolete")
_CcmGatewayTrunkEntry_Object = MibTableRow
ccmGatewayTrunkEntry = _CcmGatewayTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4, 1, 1)
)
ccmGatewayTrunkEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmGatewayTrunkIndex"),
)
if mibBuilder.loadTexts:
    ccmGatewayTrunkEntry.setStatus("obsolete")
_CcmGatewayTrunkIndex_Type = CcmIndex
_CcmGatewayTrunkIndex_Object = MibTableColumn
ccmGatewayTrunkIndex = _CcmGatewayTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4, 1, 1, 1),
    _CcmGatewayTrunkIndex_Type()
)
ccmGatewayTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmGatewayTrunkIndex.setStatus("obsolete")


class _CcmGatewayTrunkType_Type(Integer32):
    """Custom type ccmGatewayTrunkType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("analog", 12),
          ("bri", 14),
          ("other", 2),
          ("pri", 13),
          ("trunkDID", 5),
          ("trunkEM1", 7),
          ("trunkEM2", 8),
          ("trunkEM3", 9),
          ("trunkEM4", 10),
          ("trunkEM5", 11),
          ("trunkGroundStart", 3),
          ("trunkLoopStart", 4),
          ("trunkPOTS", 6),
          ("unknown", 1))
    )


_CcmGatewayTrunkType_Type.__name__ = "Integer32"
_CcmGatewayTrunkType_Object = MibTableColumn
ccmGatewayTrunkType = _CcmGatewayTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4, 1, 1, 2),
    _CcmGatewayTrunkType_Type()
)
ccmGatewayTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayTrunkType.setStatus("obsolete")


class _CcmGatewayTrunkName_Type(SnmpAdminString):
    """Custom type ccmGatewayTrunkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmGatewayTrunkName_Type.__name__ = "SnmpAdminString"
_CcmGatewayTrunkName_Object = MibTableColumn
ccmGatewayTrunkName = _CcmGatewayTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4, 1, 1, 3),
    _CcmGatewayTrunkName_Type()
)
ccmGatewayTrunkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayTrunkName.setStatus("obsolete")
_CcmTrunkGatewayIndex_Type = CcmIndexOrZero
_CcmTrunkGatewayIndex_Object = MibTableColumn
ccmTrunkGatewayIndex = _CcmTrunkGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4, 1, 1, 4),
    _CcmTrunkGatewayIndex_Type()
)
ccmTrunkGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmTrunkGatewayIndex.setStatus("obsolete")


class _CcmGatewayTrunkStatus_Type(Integer32):
    """Custom type ccmGatewayTrunkStatus based on Integer32"""
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
        *(("busy", 3),
          ("down", 4),
          ("unknown", 1),
          ("up", 2))
    )


_CcmGatewayTrunkStatus_Type.__name__ = "Integer32"
_CcmGatewayTrunkStatus_Object = MibTableColumn
ccmGatewayTrunkStatus = _CcmGatewayTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 4, 1, 1, 5),
    _CcmGatewayTrunkStatus_Type()
)
ccmGatewayTrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayTrunkStatus.setStatus("obsolete")
_CcmGlobalInfo_ObjectIdentity = ObjectIdentity
ccmGlobalInfo = _CcmGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5)
)
_CcmActivePhones_Type = Counter32
_CcmActivePhones_Object = MibScalar
ccmActivePhones = _CcmActivePhones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 1),
    _CcmActivePhones_Type()
)
ccmActivePhones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmActivePhones.setStatus("obsolete")
_CcmInActivePhones_Type = Counter32
_CcmInActivePhones_Object = MibScalar
ccmInActivePhones = _CcmInActivePhones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 2),
    _CcmInActivePhones_Type()
)
ccmInActivePhones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmInActivePhones.setStatus("obsolete")
_CcmActiveGateways_Type = Counter32
_CcmActiveGateways_Object = MibScalar
ccmActiveGateways = _CcmActiveGateways_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 3),
    _CcmActiveGateways_Type()
)
ccmActiveGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmActiveGateways.setStatus("obsolete")
_CcmInActiveGateways_Type = Counter32
_CcmInActiveGateways_Object = MibScalar
ccmInActiveGateways = _CcmInActiveGateways_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 4),
    _CcmInActiveGateways_Type()
)
ccmInActiveGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmInActiveGateways.setStatus("obsolete")
_CcmRegisteredPhones_Type = Counter32
_CcmRegisteredPhones_Object = MibScalar
ccmRegisteredPhones = _CcmRegisteredPhones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 5),
    _CcmRegisteredPhones_Type()
)
ccmRegisteredPhones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRegisteredPhones.setStatus("current")
_CcmUnregisteredPhones_Type = Counter32
_CcmUnregisteredPhones_Object = MibScalar
ccmUnregisteredPhones = _CcmUnregisteredPhones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 6),
    _CcmUnregisteredPhones_Type()
)
ccmUnregisteredPhones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmUnregisteredPhones.setStatus("current")
_CcmRejectedPhones_Type = Counter32
_CcmRejectedPhones_Object = MibScalar
ccmRejectedPhones = _CcmRejectedPhones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 7),
    _CcmRejectedPhones_Type()
)
ccmRejectedPhones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRejectedPhones.setStatus("current")
_CcmRegisteredGateways_Type = Counter32
_CcmRegisteredGateways_Object = MibScalar
ccmRegisteredGateways = _CcmRegisteredGateways_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 8),
    _CcmRegisteredGateways_Type()
)
ccmRegisteredGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRegisteredGateways.setStatus("current")
_CcmUnregisteredGateways_Type = Counter32
_CcmUnregisteredGateways_Object = MibScalar
ccmUnregisteredGateways = _CcmUnregisteredGateways_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 9),
    _CcmUnregisteredGateways_Type()
)
ccmUnregisteredGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmUnregisteredGateways.setStatus("current")
_CcmRejectedGateways_Type = Counter32
_CcmRejectedGateways_Object = MibScalar
ccmRejectedGateways = _CcmRejectedGateways_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 10),
    _CcmRejectedGateways_Type()
)
ccmRejectedGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRejectedGateways.setStatus("current")
_CcmRegisteredMediaDevices_Type = Counter32
_CcmRegisteredMediaDevices_Object = MibScalar
ccmRegisteredMediaDevices = _CcmRegisteredMediaDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 11),
    _CcmRegisteredMediaDevices_Type()
)
ccmRegisteredMediaDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRegisteredMediaDevices.setStatus("current")
_CcmUnregisteredMediaDevices_Type = Counter32
_CcmUnregisteredMediaDevices_Object = MibScalar
ccmUnregisteredMediaDevices = _CcmUnregisteredMediaDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 12),
    _CcmUnregisteredMediaDevices_Type()
)
ccmUnregisteredMediaDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmUnregisteredMediaDevices.setStatus("current")
_CcmRejectedMediaDevices_Type = Counter32
_CcmRejectedMediaDevices_Object = MibScalar
ccmRejectedMediaDevices = _CcmRejectedMediaDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 13),
    _CcmRejectedMediaDevices_Type()
)
ccmRejectedMediaDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRejectedMediaDevices.setStatus("current")
_CcmRegisteredCTIDevices_Type = Counter32
_CcmRegisteredCTIDevices_Object = MibScalar
ccmRegisteredCTIDevices = _CcmRegisteredCTIDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 14),
    _CcmRegisteredCTIDevices_Type()
)
ccmRegisteredCTIDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRegisteredCTIDevices.setStatus("current")
_CcmUnregisteredCTIDevices_Type = Counter32
_CcmUnregisteredCTIDevices_Object = MibScalar
ccmUnregisteredCTIDevices = _CcmUnregisteredCTIDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 15),
    _CcmUnregisteredCTIDevices_Type()
)
ccmUnregisteredCTIDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmUnregisteredCTIDevices.setStatus("current")
_CcmRejectedCTIDevices_Type = Counter32
_CcmRejectedCTIDevices_Object = MibScalar
ccmRejectedCTIDevices = _CcmRejectedCTIDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 16),
    _CcmRejectedCTIDevices_Type()
)
ccmRejectedCTIDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRejectedCTIDevices.setStatus("current")
_CcmRegisteredVoiceMailDevices_Type = Counter32
_CcmRegisteredVoiceMailDevices_Object = MibScalar
ccmRegisteredVoiceMailDevices = _CcmRegisteredVoiceMailDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 17),
    _CcmRegisteredVoiceMailDevices_Type()
)
ccmRegisteredVoiceMailDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRegisteredVoiceMailDevices.setStatus("current")
_CcmUnregisteredVoiceMailDevices_Type = Counter32
_CcmUnregisteredVoiceMailDevices_Object = MibScalar
ccmUnregisteredVoiceMailDevices = _CcmUnregisteredVoiceMailDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 18),
    _CcmUnregisteredVoiceMailDevices_Type()
)
ccmUnregisteredVoiceMailDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmUnregisteredVoiceMailDevices.setStatus("current")
_CcmRejectedVoiceMailDevices_Type = Counter32
_CcmRejectedVoiceMailDevices_Object = MibScalar
ccmRejectedVoiceMailDevices = _CcmRejectedVoiceMailDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 19),
    _CcmRejectedVoiceMailDevices_Type()
)
ccmRejectedVoiceMailDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmRejectedVoiceMailDevices.setStatus("current")
_CcmCallManagerStartTime_Type = DateAndTime
_CcmCallManagerStartTime_Object = MibScalar
ccmCallManagerStartTime = _CcmCallManagerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 20),
    _CcmCallManagerStartTime_Type()
)
ccmCallManagerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallManagerStartTime.setStatus("current")


class _CcmPhoneTableStateId_Type(Integer32):
    """Custom type ccmPhoneTableStateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmPhoneTableStateId_Type.__name__ = "Integer32"
_CcmPhoneTableStateId_Object = MibScalar
ccmPhoneTableStateId = _CcmPhoneTableStateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 21),
    _CcmPhoneTableStateId_Type()
)
ccmPhoneTableStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneTableStateId.setStatus("current")


class _CcmPhoneExtensionTableStateId_Type(Integer32):
    """Custom type ccmPhoneExtensionTableStateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmPhoneExtensionTableStateId_Type.__name__ = "Integer32"
_CcmPhoneExtensionTableStateId_Object = MibScalar
ccmPhoneExtensionTableStateId = _CcmPhoneExtensionTableStateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 22),
    _CcmPhoneExtensionTableStateId_Type()
)
ccmPhoneExtensionTableStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneExtensionTableStateId.setStatus("current")


class _CcmPhoneStatusUpdateTableStateId_Type(Integer32):
    """Custom type ccmPhoneStatusUpdateTableStateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmPhoneStatusUpdateTableStateId_Type.__name__ = "Integer32"
_CcmPhoneStatusUpdateTableStateId_Object = MibScalar
ccmPhoneStatusUpdateTableStateId = _CcmPhoneStatusUpdateTableStateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 23),
    _CcmPhoneStatusUpdateTableStateId_Type()
)
ccmPhoneStatusUpdateTableStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateTableStateId.setStatus("current")


class _CcmGatewayTableStateId_Type(Integer32):
    """Custom type ccmGatewayTableStateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmGatewayTableStateId_Type.__name__ = "Integer32"
_CcmGatewayTableStateId_Object = MibScalar
ccmGatewayTableStateId = _CcmGatewayTableStateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 24),
    _CcmGatewayTableStateId_Type()
)
ccmGatewayTableStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatewayTableStateId.setStatus("current")


class _CcmCTIDeviceTableStateId_Type(Integer32):
    """Custom type ccmCTIDeviceTableStateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmCTIDeviceTableStateId_Type.__name__ = "Integer32"
_CcmCTIDeviceTableStateId_Object = MibScalar
ccmCTIDeviceTableStateId = _CcmCTIDeviceTableStateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 25),
    _CcmCTIDeviceTableStateId_Type()
)
ccmCTIDeviceTableStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceTableStateId.setStatus("current")


class _CcmCTIDeviceDirNumTableStateId_Type(Integer32):
    """Custom type ccmCTIDeviceDirNumTableStateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmCTIDeviceDirNumTableStateId_Type.__name__ = "Integer32"
_CcmCTIDeviceDirNumTableStateId_Object = MibScalar
ccmCTIDeviceDirNumTableStateId = _CcmCTIDeviceDirNumTableStateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 26),
    _CcmCTIDeviceDirNumTableStateId_Type()
)
ccmCTIDeviceDirNumTableStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceDirNumTableStateId.setStatus("current")
_CcmPhStatUpdtTblLastAddedIndex_Type = CcmIndexOrZero
_CcmPhStatUpdtTblLastAddedIndex_Object = MibScalar
ccmPhStatUpdtTblLastAddedIndex = _CcmPhStatUpdtTblLastAddedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 27),
    _CcmPhStatUpdtTblLastAddedIndex_Type()
)
ccmPhStatUpdtTblLastAddedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhStatUpdtTblLastAddedIndex.setStatus("current")
_CcmPhFailedTblLastAddedIndex_Type = CcmIndexOrZero
_CcmPhFailedTblLastAddedIndex_Object = MibScalar
ccmPhFailedTblLastAddedIndex = _CcmPhFailedTblLastAddedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 28),
    _CcmPhFailedTblLastAddedIndex_Type()
)
ccmPhFailedTblLastAddedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPhFailedTblLastAddedIndex.setStatus("current")


class _CcmSystemVersion_Type(SnmpAdminString):
    """Custom type ccmSystemVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmSystemVersion_Type.__name__ = "SnmpAdminString"
_CcmSystemVersion_Object = MibScalar
ccmSystemVersion = _CcmSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 29),
    _CcmSystemVersion_Type()
)
ccmSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSystemVersion.setStatus("current")


class _CcmInstallationId_Type(SnmpAdminString):
    """Custom type ccmInstallationId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmInstallationId_Type.__name__ = "SnmpAdminString"
_CcmInstallationId_Object = MibScalar
ccmInstallationId = _CcmInstallationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 30),
    _CcmInstallationId_Type()
)
ccmInstallationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmInstallationId.setStatus("current")
_CcmPartiallyRegisteredPhones_Type = Counter32
_CcmPartiallyRegisteredPhones_Object = MibScalar
ccmPartiallyRegisteredPhones = _CcmPartiallyRegisteredPhones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 31),
    _CcmPartiallyRegisteredPhones_Type()
)
ccmPartiallyRegisteredPhones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmPartiallyRegisteredPhones.setStatus("current")


class _CcmH323TableEntries_Type(Integer32):
    """Custom type ccmH323TableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmH323TableEntries_Type.__name__ = "Integer32"
_CcmH323TableEntries_Object = MibScalar
ccmH323TableEntries = _CcmH323TableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 32),
    _CcmH323TableEntries_Type()
)
ccmH323TableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323TableEntries.setStatus("current")


class _CcmSIPTableEntries_Type(Integer32):
    """Custom type ccmSIPTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmSIPTableEntries_Type.__name__ = "Integer32"
_CcmSIPTableEntries_Object = MibScalar
ccmSIPTableEntries = _CcmSIPTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 5, 33),
    _CcmSIPTableEntries_Type()
)
ccmSIPTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPTableEntries.setStatus("current")
_CcmMediaDeviceInfo_ObjectIdentity = ObjectIdentity
ccmMediaDeviceInfo = _CcmMediaDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6)
)
_CcmMediaDeviceTable_Object = MibTable
ccmMediaDeviceTable = _CcmMediaDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ccmMediaDeviceTable.setStatus("current")
_CcmMediaDeviceEntry_Object = MibTableRow
ccmMediaDeviceEntry = _CcmMediaDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1)
)
ccmMediaDeviceEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmMediaDeviceIndex"),
)
if mibBuilder.loadTexts:
    ccmMediaDeviceEntry.setStatus("current")
_CcmMediaDeviceIndex_Type = CcmIndex
_CcmMediaDeviceIndex_Object = MibTableColumn
ccmMediaDeviceIndex = _CcmMediaDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 1),
    _CcmMediaDeviceIndex_Type()
)
ccmMediaDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmMediaDeviceIndex.setStatus("current")


class _CcmMediaDeviceName_Type(SnmpAdminString):
    """Custom type ccmMediaDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMediaDeviceName_Type.__name__ = "SnmpAdminString"
_CcmMediaDeviceName_Object = MibTableColumn
ccmMediaDeviceName = _CcmMediaDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 2),
    _CcmMediaDeviceName_Type()
)
ccmMediaDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceName.setStatus("current")


class _CcmMediaDeviceType_Type(Integer32):
    """Custom type ccmMediaDeviceType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ciscoConfBridgeWSSVCCMM", 8),
          ("ciscoConfBridgeWSX6608", 3),
          ("ciscoIOSConfBridgeHDV2", 12),
          ("ciscoIOSMTPHDV2", 13),
          ("ciscoIOSSWMTPHDV2", 11),
          ("ciscoMTPWSSVCCMM", 10),
          ("ciscoMediaServerWSSVCCMMMS", 9),
          ("ciscoMediaTerminPointWSX6608", 2),
          ("ciscoMusicOnHold", 6),
          ("ciscoSwConfBridge", 5),
          ("ciscoSwMediaTerminationPoint", 4),
          ("ciscoToneAnnouncementPlayer", 7),
          ("ciscoVCBIPVC35XX", 14),
          ("unknown", 1))
    )


_CcmMediaDeviceType_Type.__name__ = "Integer32"
_CcmMediaDeviceType_Object = MibTableColumn
ccmMediaDeviceType = _CcmMediaDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 3),
    _CcmMediaDeviceType_Type()
)
ccmMediaDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceType.setStatus("obsolete")


class _CcmMediaDeviceDescription_Type(SnmpAdminString):
    """Custom type ccmMediaDeviceDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMediaDeviceDescription_Type.__name__ = "SnmpAdminString"
_CcmMediaDeviceDescription_Object = MibTableColumn
ccmMediaDeviceDescription = _CcmMediaDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 4),
    _CcmMediaDeviceDescription_Type()
)
ccmMediaDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceDescription.setStatus("current")
_CcmMediaDeviceStatus_Type = CcmDeviceStatus
_CcmMediaDeviceStatus_Object = MibTableColumn
ccmMediaDeviceStatus = _CcmMediaDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 5),
    _CcmMediaDeviceStatus_Type()
)
ccmMediaDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceStatus.setStatus("current")
_CcmMediaDeviceDevicePoolIndex_Type = CcmIndexOrZero
_CcmMediaDeviceDevicePoolIndex_Object = MibTableColumn
ccmMediaDeviceDevicePoolIndex = _CcmMediaDeviceDevicePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 6),
    _CcmMediaDeviceDevicePoolIndex_Type()
)
ccmMediaDeviceDevicePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceDevicePoolIndex.setStatus("current")
_CcmMediaDeviceInetAddressType_Type = InetAddressType
_CcmMediaDeviceInetAddressType_Object = MibTableColumn
ccmMediaDeviceInetAddressType = _CcmMediaDeviceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 7),
    _CcmMediaDeviceInetAddressType_Type()
)
ccmMediaDeviceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceInetAddressType.setStatus("deprecated")
_CcmMediaDeviceInetAddress_Type = InetAddress
_CcmMediaDeviceInetAddress_Object = MibTableColumn
ccmMediaDeviceInetAddress = _CcmMediaDeviceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 8),
    _CcmMediaDeviceInetAddress_Type()
)
ccmMediaDeviceInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceInetAddress.setStatus("deprecated")
_CcmMediaDeviceStatusReason_Type = CcmDevFailCauseCode
_CcmMediaDeviceStatusReason_Object = MibTableColumn
ccmMediaDeviceStatusReason = _CcmMediaDeviceStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 9),
    _CcmMediaDeviceStatusReason_Type()
)
ccmMediaDeviceStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceStatusReason.setStatus("deprecated")
_CcmMediaDeviceTimeLastStatusUpdt_Type = DateAndTime
_CcmMediaDeviceTimeLastStatusUpdt_Object = MibTableColumn
ccmMediaDeviceTimeLastStatusUpdt = _CcmMediaDeviceTimeLastStatusUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 10),
    _CcmMediaDeviceTimeLastStatusUpdt_Type()
)
ccmMediaDeviceTimeLastStatusUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceTimeLastStatusUpdt.setStatus("current")
_CcmMediaDeviceTimeLastRegistered_Type = DateAndTime
_CcmMediaDeviceTimeLastRegistered_Object = MibTableColumn
ccmMediaDeviceTimeLastRegistered = _CcmMediaDeviceTimeLastRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 11),
    _CcmMediaDeviceTimeLastRegistered_Type()
)
ccmMediaDeviceTimeLastRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceTimeLastRegistered.setStatus("current")
_CcmMediaDeviceProductTypeIndex_Type = CcmIndexOrZero
_CcmMediaDeviceProductTypeIndex_Object = MibTableColumn
ccmMediaDeviceProductTypeIndex = _CcmMediaDeviceProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 12),
    _CcmMediaDeviceProductTypeIndex_Type()
)
ccmMediaDeviceProductTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceProductTypeIndex.setStatus("current")
_CcmMediaDeviceInetAddressIPv4_Type = InetAddressIPv4
_CcmMediaDeviceInetAddressIPv4_Object = MibTableColumn
ccmMediaDeviceInetAddressIPv4 = _CcmMediaDeviceInetAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 13),
    _CcmMediaDeviceInetAddressIPv4_Type()
)
ccmMediaDeviceInetAddressIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceInetAddressIPv4.setStatus("current")
_CcmMediaDeviceInetAddressIPv6_Type = InetAddressIPv6
_CcmMediaDeviceInetAddressIPv6_Object = MibTableColumn
ccmMediaDeviceInetAddressIPv6 = _CcmMediaDeviceInetAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 14),
    _CcmMediaDeviceInetAddressIPv6_Type()
)
ccmMediaDeviceInetAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceInetAddressIPv6.setStatus("current")
_CcmMediaDeviceUnregReason_Type = CcmDevUnregCauseCode
_CcmMediaDeviceUnregReason_Object = MibTableColumn
ccmMediaDeviceUnregReason = _CcmMediaDeviceUnregReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 15),
    _CcmMediaDeviceUnregReason_Type()
)
ccmMediaDeviceUnregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceUnregReason.setStatus("current")
_CcmMediaDeviceRegFailReason_Type = CcmDevRegFailCauseCode
_CcmMediaDeviceRegFailReason_Object = MibTableColumn
ccmMediaDeviceRegFailReason = _CcmMediaDeviceRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 6, 1, 1, 16),
    _CcmMediaDeviceRegFailReason_Type()
)
ccmMediaDeviceRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMediaDeviceRegFailReason.setStatus("current")
_CcmGatekeeperInfo_ObjectIdentity = ObjectIdentity
ccmGatekeeperInfo = _CcmGatekeeperInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7)
)
_CcmGatekeeperTable_Object = MibTable
ccmGatekeeperTable = _CcmGatekeeperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ccmGatekeeperTable.setStatus("obsolete")
_CcmGatekeeperEntry_Object = MibTableRow
ccmGatekeeperEntry = _CcmGatekeeperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1)
)
ccmGatekeeperEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmGatekeeperIndex"),
)
if mibBuilder.loadTexts:
    ccmGatekeeperEntry.setStatus("obsolete")
_CcmGatekeeperIndex_Type = CcmIndex
_CcmGatekeeperIndex_Object = MibTableColumn
ccmGatekeeperIndex = _CcmGatekeeperIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 1),
    _CcmGatekeeperIndex_Type()
)
ccmGatekeeperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmGatekeeperIndex.setStatus("obsolete")


class _CcmGatekeeperName_Type(SnmpAdminString):
    """Custom type ccmGatekeeperName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmGatekeeperName_Type.__name__ = "SnmpAdminString"
_CcmGatekeeperName_Object = MibTableColumn
ccmGatekeeperName = _CcmGatekeeperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 2),
    _CcmGatekeeperName_Type()
)
ccmGatekeeperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatekeeperName.setStatus("obsolete")


class _CcmGatekeeperType_Type(Integer32):
    """Custom type ccmGatekeeperType based on Integer32"""
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
        *(("gateway", 4),
          ("other", 2),
          ("terminal", 3),
          ("unknown", 1))
    )


_CcmGatekeeperType_Type.__name__ = "Integer32"
_CcmGatekeeperType_Object = MibTableColumn
ccmGatekeeperType = _CcmGatekeeperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 3),
    _CcmGatekeeperType_Type()
)
ccmGatekeeperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatekeeperType.setStatus("obsolete")


class _CcmGatekeeperDescription_Type(SnmpAdminString):
    """Custom type ccmGatekeeperDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmGatekeeperDescription_Type.__name__ = "SnmpAdminString"
_CcmGatekeeperDescription_Object = MibTableColumn
ccmGatekeeperDescription = _CcmGatekeeperDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 4),
    _CcmGatekeeperDescription_Type()
)
ccmGatekeeperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatekeeperDescription.setStatus("obsolete")


class _CcmGatekeeperStatus_Type(Integer32):
    """Custom type ccmGatekeeperStatus based on Integer32"""
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
        *(("registered", 2),
          ("rejected", 4),
          ("unknown", 1),
          ("unregistered", 3))
    )


_CcmGatekeeperStatus_Type.__name__ = "Integer32"
_CcmGatekeeperStatus_Object = MibTableColumn
ccmGatekeeperStatus = _CcmGatekeeperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 5),
    _CcmGatekeeperStatus_Type()
)
ccmGatekeeperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatekeeperStatus.setStatus("obsolete")
_CcmGatekeeperDevicePoolIndex_Type = CcmIndexOrZero
_CcmGatekeeperDevicePoolIndex_Object = MibTableColumn
ccmGatekeeperDevicePoolIndex = _CcmGatekeeperDevicePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 6),
    _CcmGatekeeperDevicePoolIndex_Type()
)
ccmGatekeeperDevicePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatekeeperDevicePoolIndex.setStatus("obsolete")
_CcmGatekeeperInetAddressType_Type = InetAddressType
_CcmGatekeeperInetAddressType_Object = MibTableColumn
ccmGatekeeperInetAddressType = _CcmGatekeeperInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 7),
    _CcmGatekeeperInetAddressType_Type()
)
ccmGatekeeperInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatekeeperInetAddressType.setStatus("obsolete")
_CcmGatekeeperInetAddress_Type = InetAddress
_CcmGatekeeperInetAddress_Object = MibTableColumn
ccmGatekeeperInetAddress = _CcmGatekeeperInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 7, 1, 1, 8),
    _CcmGatekeeperInetAddress_Type()
)
ccmGatekeeperInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmGatekeeperInetAddress.setStatus("obsolete")
_CcmCTIDeviceInfo_ObjectIdentity = ObjectIdentity
ccmCTIDeviceInfo = _CcmCTIDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8)
)
_CcmCTIDeviceTable_Object = MibTable
ccmCTIDeviceTable = _CcmCTIDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ccmCTIDeviceTable.setStatus("current")
_CcmCTIDeviceEntry_Object = MibTableRow
ccmCTIDeviceEntry = _CcmCTIDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1)
)
ccmCTIDeviceEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmCTIDeviceIndex"),
)
if mibBuilder.loadTexts:
    ccmCTIDeviceEntry.setStatus("current")
_CcmCTIDeviceIndex_Type = CcmIndex
_CcmCTIDeviceIndex_Object = MibTableColumn
ccmCTIDeviceIndex = _CcmCTIDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 1),
    _CcmCTIDeviceIndex_Type()
)
ccmCTIDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmCTIDeviceIndex.setStatus("current")


class _CcmCTIDeviceName_Type(SnmpAdminString):
    """Custom type ccmCTIDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmCTIDeviceName_Type.__name__ = "SnmpAdminString"
_CcmCTIDeviceName_Object = MibTableColumn
ccmCTIDeviceName = _CcmCTIDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 2),
    _CcmCTIDeviceName_Type()
)
ccmCTIDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceName.setStatus("current")


class _CcmCTIDeviceType_Type(Integer32):
    """Custom type ccmCTIDeviceType based on Integer32"""
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
        *(("ctiPort", 4),
          ("ctiRoutePoint", 3),
          ("other", 2),
          ("unknown", 1))
    )


_CcmCTIDeviceType_Type.__name__ = "Integer32"
_CcmCTIDeviceType_Object = MibTableColumn
ccmCTIDeviceType = _CcmCTIDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 3),
    _CcmCTIDeviceType_Type()
)
ccmCTIDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceType.setStatus("obsolete")


class _CcmCTIDeviceDescription_Type(SnmpAdminString):
    """Custom type ccmCTIDeviceDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmCTIDeviceDescription_Type.__name__ = "SnmpAdminString"
_CcmCTIDeviceDescription_Object = MibTableColumn
ccmCTIDeviceDescription = _CcmCTIDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 4),
    _CcmCTIDeviceDescription_Type()
)
ccmCTIDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceDescription.setStatus("current")
_CcmCTIDeviceStatus_Type = CcmDeviceStatus
_CcmCTIDeviceStatus_Object = MibTableColumn
ccmCTIDeviceStatus = _CcmCTIDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 5),
    _CcmCTIDeviceStatus_Type()
)
ccmCTIDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceStatus.setStatus("current")
_CcmCTIDevicePoolIndex_Type = CcmIndexOrZero
_CcmCTIDevicePoolIndex_Object = MibTableColumn
ccmCTIDevicePoolIndex = _CcmCTIDevicePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 6),
    _CcmCTIDevicePoolIndex_Type()
)
ccmCTIDevicePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDevicePoolIndex.setStatus("current")
_CcmCTIDeviceInetAddressType_Type = InetAddressType
_CcmCTIDeviceInetAddressType_Object = MibTableColumn
ccmCTIDeviceInetAddressType = _CcmCTIDeviceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 7),
    _CcmCTIDeviceInetAddressType_Type()
)
ccmCTIDeviceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceInetAddressType.setStatus("deprecated")
_CcmCTIDeviceInetAddress_Type = InetAddress
_CcmCTIDeviceInetAddress_Object = MibTableColumn
ccmCTIDeviceInetAddress = _CcmCTIDeviceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 8),
    _CcmCTIDeviceInetAddress_Type()
)
ccmCTIDeviceInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceInetAddress.setStatus("deprecated")


class _CcmCTIDeviceAppInfo_Type(SnmpAdminString):
    """Custom type ccmCTIDeviceAppInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmCTIDeviceAppInfo_Type.__name__ = "SnmpAdminString"
_CcmCTIDeviceAppInfo_Object = MibTableColumn
ccmCTIDeviceAppInfo = _CcmCTIDeviceAppInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 9),
    _CcmCTIDeviceAppInfo_Type()
)
ccmCTIDeviceAppInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceAppInfo.setStatus("obsolete")
_CcmCTIDeviceStatusReason_Type = CcmDevFailCauseCode
_CcmCTIDeviceStatusReason_Object = MibTableColumn
ccmCTIDeviceStatusReason = _CcmCTIDeviceStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 10),
    _CcmCTIDeviceStatusReason_Type()
)
ccmCTIDeviceStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceStatusReason.setStatus("deprecated")
_CcmCTIDeviceTimeLastStatusUpdt_Type = DateAndTime
_CcmCTIDeviceTimeLastStatusUpdt_Object = MibTableColumn
ccmCTIDeviceTimeLastStatusUpdt = _CcmCTIDeviceTimeLastStatusUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 11),
    _CcmCTIDeviceTimeLastStatusUpdt_Type()
)
ccmCTIDeviceTimeLastStatusUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceTimeLastStatusUpdt.setStatus("current")
_CcmCTIDeviceTimeLastRegistered_Type = DateAndTime
_CcmCTIDeviceTimeLastRegistered_Object = MibTableColumn
ccmCTIDeviceTimeLastRegistered = _CcmCTIDeviceTimeLastRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 12),
    _CcmCTIDeviceTimeLastRegistered_Type()
)
ccmCTIDeviceTimeLastRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceTimeLastRegistered.setStatus("current")
_CcmCTIDeviceProductTypeIndex_Type = CcmIndexOrZero
_CcmCTIDeviceProductTypeIndex_Object = MibTableColumn
ccmCTIDeviceProductTypeIndex = _CcmCTIDeviceProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 13),
    _CcmCTIDeviceProductTypeIndex_Type()
)
ccmCTIDeviceProductTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceProductTypeIndex.setStatus("current")
_CcmCTIDeviceInetAddressIPv4_Type = InetAddressIPv4
_CcmCTIDeviceInetAddressIPv4_Object = MibTableColumn
ccmCTIDeviceInetAddressIPv4 = _CcmCTIDeviceInetAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 14),
    _CcmCTIDeviceInetAddressIPv4_Type()
)
ccmCTIDeviceInetAddressIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceInetAddressIPv4.setStatus("current")
_CcmCTIDeviceInetAddressIPv6_Type = InetAddressIPv6
_CcmCTIDeviceInetAddressIPv6_Object = MibTableColumn
ccmCTIDeviceInetAddressIPv6 = _CcmCTIDeviceInetAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 15),
    _CcmCTIDeviceInetAddressIPv6_Type()
)
ccmCTIDeviceInetAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceInetAddressIPv6.setStatus("current")
_CcmCTIDeviceUnregReason_Type = CcmDevUnregCauseCode
_CcmCTIDeviceUnregReason_Object = MibTableColumn
ccmCTIDeviceUnregReason = _CcmCTIDeviceUnregReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 16),
    _CcmCTIDeviceUnregReason_Type()
)
ccmCTIDeviceUnregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceUnregReason.setStatus("current")
_CcmCTIDeviceRegFailReason_Type = CcmDevRegFailCauseCode
_CcmCTIDeviceRegFailReason_Object = MibTableColumn
ccmCTIDeviceRegFailReason = _CcmCTIDeviceRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 1, 1, 17),
    _CcmCTIDeviceRegFailReason_Type()
)
ccmCTIDeviceRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceRegFailReason.setStatus("current")
_CcmCTIDeviceDirNumTable_Object = MibTable
ccmCTIDeviceDirNumTable = _CcmCTIDeviceDirNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ccmCTIDeviceDirNumTable.setStatus("current")
_CcmCTIDeviceDirNumEntry_Object = MibTableRow
ccmCTIDeviceDirNumEntry = _CcmCTIDeviceDirNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 2, 1)
)
ccmCTIDeviceDirNumEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmCTIDeviceIndex"),
    (0, "CISCO-CCM-MIB", "ccmCTIDeviceDirNumIndex"),
)
if mibBuilder.loadTexts:
    ccmCTIDeviceDirNumEntry.setStatus("current")
_CcmCTIDeviceDirNumIndex_Type = CcmIndex
_CcmCTIDeviceDirNumIndex_Object = MibTableColumn
ccmCTIDeviceDirNumIndex = _CcmCTIDeviceDirNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 2, 1, 1),
    _CcmCTIDeviceDirNumIndex_Type()
)
ccmCTIDeviceDirNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmCTIDeviceDirNumIndex.setStatus("current")


class _CcmCTIDeviceDirNum_Type(SnmpAdminString):
    """Custom type ccmCTIDeviceDirNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CcmCTIDeviceDirNum_Type.__name__ = "SnmpAdminString"
_CcmCTIDeviceDirNum_Object = MibTableColumn
ccmCTIDeviceDirNum = _CcmCTIDeviceDirNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 8, 2, 1, 2),
    _CcmCTIDeviceDirNum_Type()
)
ccmCTIDeviceDirNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDeviceDirNum.setStatus("current")
_CcmAlarmConfigInfo_ObjectIdentity = ObjectIdentity
ccmAlarmConfigInfo = _CcmAlarmConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9)
)


class _CcmCallManagerAlarmEnable_Type(TruthValue):
    """Custom type ccmCallManagerAlarmEnable based on TruthValue"""


_CcmCallManagerAlarmEnable_Object = MibScalar
ccmCallManagerAlarmEnable = _CcmCallManagerAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9, 1),
    _CcmCallManagerAlarmEnable_Type()
)
ccmCallManagerAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCallManagerAlarmEnable.setStatus("current")


class _CcmPhoneFailedAlarmInterval_Type(Integer32):
    """Custom type ccmPhoneFailedAlarmInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 3600),
    )


_CcmPhoneFailedAlarmInterval_Type.__name__ = "Integer32"
_CcmPhoneFailedAlarmInterval_Object = MibScalar
ccmPhoneFailedAlarmInterval = _CcmPhoneFailedAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9, 2),
    _CcmPhoneFailedAlarmInterval_Type()
)
ccmPhoneFailedAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPhoneFailedAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccmPhoneFailedAlarmInterval.setUnits("seconds")


class _CcmPhoneFailedStorePeriod_Type(Integer32):
    """Custom type ccmPhoneFailedStorePeriod based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 3600),
    )


_CcmPhoneFailedStorePeriod_Type.__name__ = "Integer32"
_CcmPhoneFailedStorePeriod_Object = MibScalar
ccmPhoneFailedStorePeriod = _CcmPhoneFailedStorePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9, 3),
    _CcmPhoneFailedStorePeriod_Type()
)
ccmPhoneFailedStorePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPhoneFailedStorePeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccmPhoneFailedStorePeriod.setUnits("seconds")


class _CcmPhoneStatusUpdateAlarmInterv_Type(Integer32):
    """Custom type ccmPhoneStatusUpdateAlarmInterv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 3600),
    )


_CcmPhoneStatusUpdateAlarmInterv_Type.__name__ = "Integer32"
_CcmPhoneStatusUpdateAlarmInterv_Object = MibScalar
ccmPhoneStatusUpdateAlarmInterv = _CcmPhoneStatusUpdateAlarmInterv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9, 4),
    _CcmPhoneStatusUpdateAlarmInterv_Type()
)
ccmPhoneStatusUpdateAlarmInterv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateAlarmInterv.setStatus("current")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateAlarmInterv.setUnits("seconds")


class _CcmPhoneStatusUpdateStorePeriod_Type(Integer32):
    """Custom type ccmPhoneStatusUpdateStorePeriod based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 3600),
    )


_CcmPhoneStatusUpdateStorePeriod_Type.__name__ = "Integer32"
_CcmPhoneStatusUpdateStorePeriod_Object = MibScalar
ccmPhoneStatusUpdateStorePeriod = _CcmPhoneStatusUpdateStorePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9, 5),
    _CcmPhoneStatusUpdateStorePeriod_Type()
)
ccmPhoneStatusUpdateStorePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateStorePeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdateStorePeriod.setUnits("seconds")


class _CcmGatewayAlarmEnable_Type(TruthValue):
    """Custom type ccmGatewayAlarmEnable based on TruthValue"""


_CcmGatewayAlarmEnable_Object = MibScalar
ccmGatewayAlarmEnable = _CcmGatewayAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9, 6),
    _CcmGatewayAlarmEnable_Type()
)
ccmGatewayAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmGatewayAlarmEnable.setStatus("current")


class _CcmMaliciousCallAlarmEnable_Type(TruthValue):
    """Custom type ccmMaliciousCallAlarmEnable based on TruthValue"""


_CcmMaliciousCallAlarmEnable_Object = MibScalar
ccmMaliciousCallAlarmEnable = _CcmMaliciousCallAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 9, 7),
    _CcmMaliciousCallAlarmEnable_Type()
)
ccmMaliciousCallAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmMaliciousCallAlarmEnable.setStatus("current")
_CcmNotificationsInfo_ObjectIdentity = ObjectIdentity
ccmNotificationsInfo = _CcmNotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10)
)


class _CcmAlarmSeverity_Type(Integer32):
    """Custom type ccmAlarmSeverity based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("notice", 6),
          ("warning", 5))
    )


_CcmAlarmSeverity_Type.__name__ = "Integer32"
_CcmAlarmSeverity_Object = MibScalar
ccmAlarmSeverity = _CcmAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 1),
    _CcmAlarmSeverity_Type()
)
ccmAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmAlarmSeverity.setStatus("current")


class _CcmFailCauseCode_Type(Integer32):
    """Custom type ccmFailCauseCode based on Integer32"""
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
        *(("callControlInitFailed", 8),
          ("criticalThreadDied", 5),
          ("dbMgrInitFailed", 10),
          ("deviceMgrInitFailed", 6),
          ("digitAnalysisInitFailed", 7),
          ("heartBeatStopped", 2),
          ("linkMgrInitFailed", 9),
          ("msgTranslatorInitFailed", 11),
          ("routerThreadDied", 3),
          ("suppServicesInitFailed", 12),
          ("timerThreadDied", 4),
          ("unknown", 1))
    )


_CcmFailCauseCode_Type.__name__ = "Integer32"
_CcmFailCauseCode_Object = MibScalar
ccmFailCauseCode = _CcmFailCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 2),
    _CcmFailCauseCode_Type()
)
ccmFailCauseCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmFailCauseCode.setStatus("current")
_CcmPhoneFailures_Type = Unsigned32
_CcmPhoneFailures_Object = MibScalar
ccmPhoneFailures = _CcmPhoneFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 3),
    _CcmPhoneFailures_Type()
)
ccmPhoneFailures.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmPhoneFailures.setStatus("current")
_CcmPhoneUpdates_Type = Unsigned32
_CcmPhoneUpdates_Object = MibScalar
ccmPhoneUpdates = _CcmPhoneUpdates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 4),
    _CcmPhoneUpdates_Type()
)
ccmPhoneUpdates.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmPhoneUpdates.setStatus("current")
_CcmGatewayFailCauseCode_Type = CcmDevFailCauseCode
_CcmGatewayFailCauseCode_Object = MibScalar
ccmGatewayFailCauseCode = _CcmGatewayFailCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 5),
    _CcmGatewayFailCauseCode_Type()
)
ccmGatewayFailCauseCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmGatewayFailCauseCode.setStatus("deprecated")


class _CcmMediaResourceType_Type(Integer32):
    """Custom type ccmMediaResourceType based on Integer32"""
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
        *(("conferenceBridge", 4),
          ("mediaTerminationPoint", 2),
          ("musicOnHold", 5),
          ("transcoder", 3),
          ("unknown", 1))
    )


_CcmMediaResourceType_Type.__name__ = "Integer32"
_CcmMediaResourceType_Object = MibScalar
ccmMediaResourceType = _CcmMediaResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 6),
    _CcmMediaResourceType_Type()
)
ccmMediaResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMediaResourceType.setStatus("current")


class _CcmMediaResourceListName_Type(SnmpAdminString):
    """Custom type ccmMediaResourceListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMediaResourceListName_Type.__name__ = "SnmpAdminString"
_CcmMediaResourceListName_Object = MibScalar
ccmMediaResourceListName = _CcmMediaResourceListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 7),
    _CcmMediaResourceListName_Type()
)
ccmMediaResourceListName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMediaResourceListName.setStatus("current")


class _CcmRouteListName_Type(SnmpAdminString):
    """Custom type ccmRouteListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmRouteListName_Type.__name__ = "SnmpAdminString"
_CcmRouteListName_Object = MibScalar
ccmRouteListName = _CcmRouteListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 8),
    _CcmRouteListName_Type()
)
ccmRouteListName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmRouteListName.setStatus("current")


class _CcmGatewayPhysIfIndex_Type(Integer32):
    """Custom type ccmGatewayPhysIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcmGatewayPhysIfIndex_Type.__name__ = "Integer32"
_CcmGatewayPhysIfIndex_Object = MibScalar
ccmGatewayPhysIfIndex = _CcmGatewayPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 9),
    _CcmGatewayPhysIfIndex_Type()
)
ccmGatewayPhysIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmGatewayPhysIfIndex.setStatus("current")


class _CcmGatewayPhysIfL2Status_Type(Integer32):
    """Custom type ccmGatewayPhysIfL2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_CcmGatewayPhysIfL2Status_Type.__name__ = "Integer32"
_CcmGatewayPhysIfL2Status_Object = MibScalar
ccmGatewayPhysIfL2Status = _CcmGatewayPhysIfL2Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 10),
    _CcmGatewayPhysIfL2Status_Type()
)
ccmGatewayPhysIfL2Status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmGatewayPhysIfL2Status.setStatus("current")


class _CcmMaliCallCalledPartyName_Type(SnmpAdminString):
    """Custom type ccmMaliCallCalledPartyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMaliCallCalledPartyName_Type.__name__ = "SnmpAdminString"
_CcmMaliCallCalledPartyName_Object = MibScalar
ccmMaliCallCalledPartyName = _CcmMaliCallCalledPartyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 11),
    _CcmMaliCallCalledPartyName_Type()
)
ccmMaliCallCalledPartyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMaliCallCalledPartyName.setStatus("current")


class _CcmMaliCallCalledPartyNumber_Type(SnmpAdminString):
    """Custom type ccmMaliCallCalledPartyNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMaliCallCalledPartyNumber_Type.__name__ = "SnmpAdminString"
_CcmMaliCallCalledPartyNumber_Object = MibScalar
ccmMaliCallCalledPartyNumber = _CcmMaliCallCalledPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 12),
    _CcmMaliCallCalledPartyNumber_Type()
)
ccmMaliCallCalledPartyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMaliCallCalledPartyNumber.setStatus("current")


class _CcmMaliCallCalledDeviceName_Type(SnmpAdminString):
    """Custom type ccmMaliCallCalledDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMaliCallCalledDeviceName_Type.__name__ = "SnmpAdminString"
_CcmMaliCallCalledDeviceName_Object = MibScalar
ccmMaliCallCalledDeviceName = _CcmMaliCallCalledDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 13),
    _CcmMaliCallCalledDeviceName_Type()
)
ccmMaliCallCalledDeviceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMaliCallCalledDeviceName.setStatus("current")


class _CcmMaliCallCallingPartyName_Type(SnmpAdminString):
    """Custom type ccmMaliCallCallingPartyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMaliCallCallingPartyName_Type.__name__ = "SnmpAdminString"
_CcmMaliCallCallingPartyName_Object = MibScalar
ccmMaliCallCallingPartyName = _CcmMaliCallCallingPartyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 14),
    _CcmMaliCallCallingPartyName_Type()
)
ccmMaliCallCallingPartyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMaliCallCallingPartyName.setStatus("current")


class _CcmMaliCallCallingPartyNumber_Type(SnmpAdminString):
    """Custom type ccmMaliCallCallingPartyNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMaliCallCallingPartyNumber_Type.__name__ = "SnmpAdminString"
_CcmMaliCallCallingPartyNumber_Object = MibScalar
ccmMaliCallCallingPartyNumber = _CcmMaliCallCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 15),
    _CcmMaliCallCallingPartyNumber_Type()
)
ccmMaliCallCallingPartyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMaliCallCallingPartyNumber.setStatus("current")


class _CcmMaliCallCallingDeviceName_Type(SnmpAdminString):
    """Custom type ccmMaliCallCallingDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmMaliCallCallingDeviceName_Type.__name__ = "SnmpAdminString"
_CcmMaliCallCallingDeviceName_Object = MibScalar
ccmMaliCallCallingDeviceName = _CcmMaliCallCallingDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 16),
    _CcmMaliCallCallingDeviceName_Type()
)
ccmMaliCallCallingDeviceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMaliCallCallingDeviceName.setStatus("current")
_CcmMaliCallTime_Type = DateAndTime
_CcmMaliCallTime_Object = MibScalar
ccmMaliCallTime = _CcmMaliCallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 17),
    _CcmMaliCallTime_Type()
)
ccmMaliCallTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmMaliCallTime.setStatus("current")


class _CcmQualityRprtSourceDevName_Type(SnmpAdminString):
    """Custom type ccmQualityRprtSourceDevName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmQualityRprtSourceDevName_Type.__name__ = "SnmpAdminString"
_CcmQualityRprtSourceDevName_Object = MibScalar
ccmQualityRprtSourceDevName = _CcmQualityRprtSourceDevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 18),
    _CcmQualityRprtSourceDevName_Type()
)
ccmQualityRprtSourceDevName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmQualityRprtSourceDevName.setStatus("current")


class _CcmQualityRprtClusterId_Type(SnmpAdminString):
    """Custom type ccmQualityRprtClusterId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmQualityRprtClusterId_Type.__name__ = "SnmpAdminString"
_CcmQualityRprtClusterId_Object = MibScalar
ccmQualityRprtClusterId = _CcmQualityRprtClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 19),
    _CcmQualityRprtClusterId_Type()
)
ccmQualityRprtClusterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmQualityRprtClusterId.setStatus("current")


class _CcmQualityRprtCategory_Type(SnmpAdminString):
    """Custom type ccmQualityRprtCategory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmQualityRprtCategory_Type.__name__ = "SnmpAdminString"
_CcmQualityRprtCategory_Object = MibScalar
ccmQualityRprtCategory = _CcmQualityRprtCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 20),
    _CcmQualityRprtCategory_Type()
)
ccmQualityRprtCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmQualityRprtCategory.setStatus("current")


class _CcmQualityRprtReasonCode_Type(SnmpAdminString):
    """Custom type ccmQualityRprtReasonCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmQualityRprtReasonCode_Type.__name__ = "SnmpAdminString"
_CcmQualityRprtReasonCode_Object = MibScalar
ccmQualityRprtReasonCode = _CcmQualityRprtReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 21),
    _CcmQualityRprtReasonCode_Type()
)
ccmQualityRprtReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmQualityRprtReasonCode.setStatus("current")
_CcmQualityRprtTime_Type = DateAndTime
_CcmQualityRprtTime_Object = MibScalar
ccmQualityRprtTime = _CcmQualityRprtTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 22),
    _CcmQualityRprtTime_Type()
)
ccmQualityRprtTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmQualityRprtTime.setStatus("current")


class _CcmTLSDevName_Type(SnmpAdminString):
    """Custom type ccmTLSDevName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmTLSDevName_Type.__name__ = "SnmpAdminString"
_CcmTLSDevName_Object = MibScalar
ccmTLSDevName = _CcmTLSDevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 23),
    _CcmTLSDevName_Type()
)
ccmTLSDevName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmTLSDevName.setStatus("current")
_CcmTLSDevInetAddressType_Type = InetAddressType
_CcmTLSDevInetAddressType_Object = MibScalar
ccmTLSDevInetAddressType = _CcmTLSDevInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 24),
    _CcmTLSDevInetAddressType_Type()
)
ccmTLSDevInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmTLSDevInetAddressType.setStatus("current")
_CcmTLSDevInetAddress_Type = InetAddress
_CcmTLSDevInetAddress_Object = MibScalar
ccmTLSDevInetAddress = _CcmTLSDevInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 25),
    _CcmTLSDevInetAddress_Type()
)
ccmTLSDevInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmTLSDevInetAddress.setStatus("current")
_CcmTLSConnFailTime_Type = DateAndTime
_CcmTLSConnFailTime_Object = MibScalar
ccmTLSConnFailTime = _CcmTLSConnFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 26),
    _CcmTLSConnFailTime_Type()
)
ccmTLSConnFailTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmTLSConnFailTime.setStatus("current")


class _CcmTLSConnectionFailReasonCode_Type(Integer32):
    """Custom type ccmTLSConnectionFailReasonCode based on Integer32"""
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
        *(("authenticationerror", 2),
          ("invalidtlscipher", 4),
          ("invalidx509nameincertificate", 3),
          ("unknown", 1))
    )


_CcmTLSConnectionFailReasonCode_Type.__name__ = "Integer32"
_CcmTLSConnectionFailReasonCode_Object = MibScalar
ccmTLSConnectionFailReasonCode = _CcmTLSConnectionFailReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 27),
    _CcmTLSConnectionFailReasonCode_Type()
)
ccmTLSConnectionFailReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmTLSConnectionFailReasonCode.setStatus("current")
_CcmGatewayRegFailCauseCode_Type = CcmDevRegFailCauseCode
_CcmGatewayRegFailCauseCode_Object = MibScalar
ccmGatewayRegFailCauseCode = _CcmGatewayRegFailCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 10, 28),
    _CcmGatewayRegFailCauseCode_Type()
)
ccmGatewayRegFailCauseCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmGatewayRegFailCauseCode.setStatus("current")
_CcmH323DeviceInfo_ObjectIdentity = ObjectIdentity
ccmH323DeviceInfo = _CcmH323DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11)
)
_CcmH323DeviceTable_Object = MibTable
ccmH323DeviceTable = _CcmH323DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ccmH323DeviceTable.setStatus("current")
_CcmH323DeviceEntry_Object = MibTableRow
ccmH323DeviceEntry = _CcmH323DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1)
)
ccmH323DeviceEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmH323DevIndex"),
)
if mibBuilder.loadTexts:
    ccmH323DeviceEntry.setStatus("current")
_CcmH323DevIndex_Type = CcmIndex
_CcmH323DevIndex_Object = MibTableColumn
ccmH323DevIndex = _CcmH323DevIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 1),
    _CcmH323DevIndex_Type()
)
ccmH323DevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmH323DevIndex.setStatus("current")


class _CcmH323DevName_Type(SnmpAdminString):
    """Custom type ccmH323DevName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmH323DevName_Type.__name__ = "SnmpAdminString"
_CcmH323DevName_Object = MibTableColumn
ccmH323DevName = _CcmH323DevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 2),
    _CcmH323DevName_Type()
)
ccmH323DevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevName.setStatus("current")
_CcmH323DevProductId_Type = CcmDeviceProductId
_CcmH323DevProductId_Object = MibTableColumn
ccmH323DevProductId = _CcmH323DevProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 3),
    _CcmH323DevProductId_Type()
)
ccmH323DevProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevProductId.setStatus("obsolete")


class _CcmH323DevDescription_Type(SnmpAdminString):
    """Custom type ccmH323DevDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmH323DevDescription_Type.__name__ = "SnmpAdminString"
_CcmH323DevDescription_Object = MibTableColumn
ccmH323DevDescription = _CcmH323DevDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 4),
    _CcmH323DevDescription_Type()
)
ccmH323DevDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevDescription.setStatus("current")
_CcmH323DevInetAddressType_Type = InetAddressType
_CcmH323DevInetAddressType_Object = MibTableColumn
ccmH323DevInetAddressType = _CcmH323DevInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 5),
    _CcmH323DevInetAddressType_Type()
)
ccmH323DevInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevInetAddressType.setStatus("current")
_CcmH323DevInetAddress_Type = InetAddress
_CcmH323DevInetAddress_Object = MibTableColumn
ccmH323DevInetAddress = _CcmH323DevInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 6),
    _CcmH323DevInetAddress_Type()
)
ccmH323DevInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevInetAddress.setStatus("current")
_CcmH323DevCnfgGKInetAddressType_Type = InetAddressType
_CcmH323DevCnfgGKInetAddressType_Object = MibTableColumn
ccmH323DevCnfgGKInetAddressType = _CcmH323DevCnfgGKInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 7),
    _CcmH323DevCnfgGKInetAddressType_Type()
)
ccmH323DevCnfgGKInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevCnfgGKInetAddressType.setStatus("current")
_CcmH323DevCnfgGKInetAddress_Type = InetAddress
_CcmH323DevCnfgGKInetAddress_Object = MibTableColumn
ccmH323DevCnfgGKInetAddress = _CcmH323DevCnfgGKInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 8),
    _CcmH323DevCnfgGKInetAddress_Type()
)
ccmH323DevCnfgGKInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevCnfgGKInetAddress.setStatus("current")
_CcmH323DevAltGK1InetAddressType_Type = InetAddressType
_CcmH323DevAltGK1InetAddressType_Object = MibTableColumn
ccmH323DevAltGK1InetAddressType = _CcmH323DevAltGK1InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 9),
    _CcmH323DevAltGK1InetAddressType_Type()
)
ccmH323DevAltGK1InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK1InetAddressType.setStatus("current")
_CcmH323DevAltGK1InetAddress_Type = InetAddress
_CcmH323DevAltGK1InetAddress_Object = MibTableColumn
ccmH323DevAltGK1InetAddress = _CcmH323DevAltGK1InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 10),
    _CcmH323DevAltGK1InetAddress_Type()
)
ccmH323DevAltGK1InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK1InetAddress.setStatus("current")
_CcmH323DevAltGK2InetAddressType_Type = InetAddressType
_CcmH323DevAltGK2InetAddressType_Object = MibTableColumn
ccmH323DevAltGK2InetAddressType = _CcmH323DevAltGK2InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 11),
    _CcmH323DevAltGK2InetAddressType_Type()
)
ccmH323DevAltGK2InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK2InetAddressType.setStatus("current")
_CcmH323DevAltGK2InetAddress_Type = InetAddress
_CcmH323DevAltGK2InetAddress_Object = MibTableColumn
ccmH323DevAltGK2InetAddress = _CcmH323DevAltGK2InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 12),
    _CcmH323DevAltGK2InetAddress_Type()
)
ccmH323DevAltGK2InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK2InetAddress.setStatus("current")
_CcmH323DevAltGK3InetAddressType_Type = InetAddressType
_CcmH323DevAltGK3InetAddressType_Object = MibTableColumn
ccmH323DevAltGK3InetAddressType = _CcmH323DevAltGK3InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 13),
    _CcmH323DevAltGK3InetAddressType_Type()
)
ccmH323DevAltGK3InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK3InetAddressType.setStatus("current")
_CcmH323DevAltGK3InetAddress_Type = InetAddress
_CcmH323DevAltGK3InetAddress_Object = MibTableColumn
ccmH323DevAltGK3InetAddress = _CcmH323DevAltGK3InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 14),
    _CcmH323DevAltGK3InetAddress_Type()
)
ccmH323DevAltGK3InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK3InetAddress.setStatus("current")
_CcmH323DevAltGK4InetAddressType_Type = InetAddressType
_CcmH323DevAltGK4InetAddressType_Object = MibTableColumn
ccmH323DevAltGK4InetAddressType = _CcmH323DevAltGK4InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 15),
    _CcmH323DevAltGK4InetAddressType_Type()
)
ccmH323DevAltGK4InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK4InetAddressType.setStatus("current")
_CcmH323DevAltGK4InetAddress_Type = InetAddress
_CcmH323DevAltGK4InetAddress_Object = MibTableColumn
ccmH323DevAltGK4InetAddress = _CcmH323DevAltGK4InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 16),
    _CcmH323DevAltGK4InetAddress_Type()
)
ccmH323DevAltGK4InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK4InetAddress.setStatus("current")
_CcmH323DevAltGK5InetAddressType_Type = InetAddressType
_CcmH323DevAltGK5InetAddressType_Object = MibTableColumn
ccmH323DevAltGK5InetAddressType = _CcmH323DevAltGK5InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 17),
    _CcmH323DevAltGK5InetAddressType_Type()
)
ccmH323DevAltGK5InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK5InetAddressType.setStatus("current")
_CcmH323DevAltGK5InetAddress_Type = InetAddress
_CcmH323DevAltGK5InetAddress_Object = MibTableColumn
ccmH323DevAltGK5InetAddress = _CcmH323DevAltGK5InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 18),
    _CcmH323DevAltGK5InetAddress_Type()
)
ccmH323DevAltGK5InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevAltGK5InetAddress.setStatus("current")
_CcmH323DevActGKInetAddressType_Type = InetAddressType
_CcmH323DevActGKInetAddressType_Object = MibTableColumn
ccmH323DevActGKInetAddressType = _CcmH323DevActGKInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 19),
    _CcmH323DevActGKInetAddressType_Type()
)
ccmH323DevActGKInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevActGKInetAddressType.setStatus("current")
_CcmH323DevActGKInetAddress_Type = InetAddress
_CcmH323DevActGKInetAddress_Object = MibTableColumn
ccmH323DevActGKInetAddress = _CcmH323DevActGKInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 20),
    _CcmH323DevActGKInetAddress_Type()
)
ccmH323DevActGKInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevActGKInetAddress.setStatus("current")


class _CcmH323DevStatus_Type(Integer32):
    """Custom type ccmH323DevStatus based on Integer32"""
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
        *(("notApplicable", 0),
          ("registered", 2),
          ("rejected", 4),
          ("unknown", 1),
          ("unregistered", 3))
    )


_CcmH323DevStatus_Type.__name__ = "Integer32"
_CcmH323DevStatus_Object = MibTableColumn
ccmH323DevStatus = _CcmH323DevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 21),
    _CcmH323DevStatus_Type()
)
ccmH323DevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevStatus.setStatus("current")
_CcmH323DevStatusReason_Type = CcmDevFailCauseCode
_CcmH323DevStatusReason_Object = MibTableColumn
ccmH323DevStatusReason = _CcmH323DevStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 22),
    _CcmH323DevStatusReason_Type()
)
ccmH323DevStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevStatusReason.setStatus("deprecated")
_CcmH323DevTimeLastStatusUpdt_Type = DateAndTime
_CcmH323DevTimeLastStatusUpdt_Object = MibTableColumn
ccmH323DevTimeLastStatusUpdt = _CcmH323DevTimeLastStatusUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 23),
    _CcmH323DevTimeLastStatusUpdt_Type()
)
ccmH323DevTimeLastStatusUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevTimeLastStatusUpdt.setStatus("current")
_CcmH323DevTimeLastRegistered_Type = DateAndTime
_CcmH323DevTimeLastRegistered_Object = MibTableColumn
ccmH323DevTimeLastRegistered = _CcmH323DevTimeLastRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 24),
    _CcmH323DevTimeLastRegistered_Type()
)
ccmH323DevTimeLastRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevTimeLastRegistered.setStatus("current")
_CcmH323DevRmtCM1InetAddressType_Type = InetAddressType
_CcmH323DevRmtCM1InetAddressType_Object = MibTableColumn
ccmH323DevRmtCM1InetAddressType = _CcmH323DevRmtCM1InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 25),
    _CcmH323DevRmtCM1InetAddressType_Type()
)
ccmH323DevRmtCM1InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevRmtCM1InetAddressType.setStatus("current")
_CcmH323DevRmtCM1InetAddress_Type = InetAddress
_CcmH323DevRmtCM1InetAddress_Object = MibTableColumn
ccmH323DevRmtCM1InetAddress = _CcmH323DevRmtCM1InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 26),
    _CcmH323DevRmtCM1InetAddress_Type()
)
ccmH323DevRmtCM1InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevRmtCM1InetAddress.setStatus("current")
_CcmH323DevRmtCM2InetAddressType_Type = InetAddressType
_CcmH323DevRmtCM2InetAddressType_Object = MibTableColumn
ccmH323DevRmtCM2InetAddressType = _CcmH323DevRmtCM2InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 27),
    _CcmH323DevRmtCM2InetAddressType_Type()
)
ccmH323DevRmtCM2InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevRmtCM2InetAddressType.setStatus("current")
_CcmH323DevRmtCM2InetAddress_Type = InetAddress
_CcmH323DevRmtCM2InetAddress_Object = MibTableColumn
ccmH323DevRmtCM2InetAddress = _CcmH323DevRmtCM2InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 28),
    _CcmH323DevRmtCM2InetAddress_Type()
)
ccmH323DevRmtCM2InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevRmtCM2InetAddress.setStatus("current")
_CcmH323DevRmtCM3InetAddressType_Type = InetAddressType
_CcmH323DevRmtCM3InetAddressType_Object = MibTableColumn
ccmH323DevRmtCM3InetAddressType = _CcmH323DevRmtCM3InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 29),
    _CcmH323DevRmtCM3InetAddressType_Type()
)
ccmH323DevRmtCM3InetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevRmtCM3InetAddressType.setStatus("current")
_CcmH323DevRmtCM3InetAddress_Type = InetAddress
_CcmH323DevRmtCM3InetAddress_Object = MibTableColumn
ccmH323DevRmtCM3InetAddress = _CcmH323DevRmtCM3InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 30),
    _CcmH323DevRmtCM3InetAddress_Type()
)
ccmH323DevRmtCM3InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevRmtCM3InetAddress.setStatus("current")
_CcmH323DevProductTypeIndex_Type = CcmIndexOrZero
_CcmH323DevProductTypeIndex_Object = MibTableColumn
ccmH323DevProductTypeIndex = _CcmH323DevProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 31),
    _CcmH323DevProductTypeIndex_Type()
)
ccmH323DevProductTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevProductTypeIndex.setStatus("current")
_CcmH323DevUnregReason_Type = CcmDevUnregCauseCode
_CcmH323DevUnregReason_Object = MibTableColumn
ccmH323DevUnregReason = _CcmH323DevUnregReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 32),
    _CcmH323DevUnregReason_Type()
)
ccmH323DevUnregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevUnregReason.setStatus("current")
_CcmH323DevRegFailReason_Type = CcmDevRegFailCauseCode
_CcmH323DevRegFailReason_Object = MibTableColumn
ccmH323DevRegFailReason = _CcmH323DevRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 11, 1, 1, 33),
    _CcmH323DevRegFailReason_Type()
)
ccmH323DevRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmH323DevRegFailReason.setStatus("current")
_CcmVoiceMailDeviceInfo_ObjectIdentity = ObjectIdentity
ccmVoiceMailDeviceInfo = _CcmVoiceMailDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12)
)
_CcmVoiceMailDeviceTable_Object = MibTable
ccmVoiceMailDeviceTable = _CcmVoiceMailDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ccmVoiceMailDeviceTable.setStatus("current")
_CcmVoiceMailDeviceEntry_Object = MibTableRow
ccmVoiceMailDeviceEntry = _CcmVoiceMailDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1)
)
ccmVoiceMailDeviceEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmVMailDevIndex"),
)
if mibBuilder.loadTexts:
    ccmVoiceMailDeviceEntry.setStatus("current")
_CcmVMailDevIndex_Type = CcmIndex
_CcmVMailDevIndex_Object = MibTableColumn
ccmVMailDevIndex = _CcmVMailDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 1),
    _CcmVMailDevIndex_Type()
)
ccmVMailDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmVMailDevIndex.setStatus("current")


class _CcmVMailDevName_Type(SnmpAdminString):
    """Custom type ccmVMailDevName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmVMailDevName_Type.__name__ = "SnmpAdminString"
_CcmVMailDevName_Object = MibTableColumn
ccmVMailDevName = _CcmVMailDevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 2),
    _CcmVMailDevName_Type()
)
ccmVMailDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevName.setStatus("current")
_CcmVMailDevProductId_Type = CcmDeviceProductId
_CcmVMailDevProductId_Object = MibTableColumn
ccmVMailDevProductId = _CcmVMailDevProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 3),
    _CcmVMailDevProductId_Type()
)
ccmVMailDevProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevProductId.setStatus("obsolete")


class _CcmVMailDevDescription_Type(SnmpAdminString):
    """Custom type ccmVMailDevDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmVMailDevDescription_Type.__name__ = "SnmpAdminString"
_CcmVMailDevDescription_Object = MibTableColumn
ccmVMailDevDescription = _CcmVMailDevDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 4),
    _CcmVMailDevDescription_Type()
)
ccmVMailDevDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevDescription.setStatus("current")
_CcmVMailDevStatus_Type = CcmDeviceStatus
_CcmVMailDevStatus_Object = MibTableColumn
ccmVMailDevStatus = _CcmVMailDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 5),
    _CcmVMailDevStatus_Type()
)
ccmVMailDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevStatus.setStatus("current")
_CcmVMailDevInetAddressType_Type = InetAddressType
_CcmVMailDevInetAddressType_Object = MibTableColumn
ccmVMailDevInetAddressType = _CcmVMailDevInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 6),
    _CcmVMailDevInetAddressType_Type()
)
ccmVMailDevInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevInetAddressType.setStatus("current")
_CcmVMailDevInetAddress_Type = InetAddress
_CcmVMailDevInetAddress_Object = MibTableColumn
ccmVMailDevInetAddress = _CcmVMailDevInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 7),
    _CcmVMailDevInetAddress_Type()
)
ccmVMailDevInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevInetAddress.setStatus("current")
_CcmVMailDevStatusReason_Type = CcmDevFailCauseCode
_CcmVMailDevStatusReason_Object = MibTableColumn
ccmVMailDevStatusReason = _CcmVMailDevStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 8),
    _CcmVMailDevStatusReason_Type()
)
ccmVMailDevStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevStatusReason.setStatus("deprecated")
_CcmVMailDevTimeLastStatusUpdt_Type = DateAndTime
_CcmVMailDevTimeLastStatusUpdt_Object = MibTableColumn
ccmVMailDevTimeLastStatusUpdt = _CcmVMailDevTimeLastStatusUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 9),
    _CcmVMailDevTimeLastStatusUpdt_Type()
)
ccmVMailDevTimeLastStatusUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevTimeLastStatusUpdt.setStatus("current")
_CcmVMailDevTimeLastRegistered_Type = DateAndTime
_CcmVMailDevTimeLastRegistered_Object = MibTableColumn
ccmVMailDevTimeLastRegistered = _CcmVMailDevTimeLastRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 10),
    _CcmVMailDevTimeLastRegistered_Type()
)
ccmVMailDevTimeLastRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevTimeLastRegistered.setStatus("current")
_CcmVMailDevProductTypeIndex_Type = CcmIndexOrZero
_CcmVMailDevProductTypeIndex_Object = MibTableColumn
ccmVMailDevProductTypeIndex = _CcmVMailDevProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 11),
    _CcmVMailDevProductTypeIndex_Type()
)
ccmVMailDevProductTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevProductTypeIndex.setStatus("current")
_CcmVMailDevUnregReason_Type = CcmDevUnregCauseCode
_CcmVMailDevUnregReason_Object = MibTableColumn
ccmVMailDevUnregReason = _CcmVMailDevUnregReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 12),
    _CcmVMailDevUnregReason_Type()
)
ccmVMailDevUnregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevUnregReason.setStatus("current")
_CcmVMailDevRegFailReason_Type = CcmDevRegFailCauseCode
_CcmVMailDevRegFailReason_Object = MibTableColumn
ccmVMailDevRegFailReason = _CcmVMailDevRegFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 1, 1, 13),
    _CcmVMailDevRegFailReason_Type()
)
ccmVMailDevRegFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevRegFailReason.setStatus("current")
_CcmVoiceMailDeviceDirNumTable_Object = MibTable
ccmVoiceMailDeviceDirNumTable = _CcmVoiceMailDeviceDirNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 2)
)
if mibBuilder.loadTexts:
    ccmVoiceMailDeviceDirNumTable.setStatus("current")
_CcmVoiceMailDeviceDirNumEntry_Object = MibTableRow
ccmVoiceMailDeviceDirNumEntry = _CcmVoiceMailDeviceDirNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 2, 1)
)
ccmVoiceMailDeviceDirNumEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmVMailDevIndex"),
    (0, "CISCO-CCM-MIB", "ccmVMailDevDirNumIndex"),
)
if mibBuilder.loadTexts:
    ccmVoiceMailDeviceDirNumEntry.setStatus("current")
_CcmVMailDevDirNumIndex_Type = CcmIndex
_CcmVMailDevDirNumIndex_Object = MibTableColumn
ccmVMailDevDirNumIndex = _CcmVMailDevDirNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 2, 1, 1),
    _CcmVMailDevDirNumIndex_Type()
)
ccmVMailDevDirNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmVMailDevDirNumIndex.setStatus("current")


class _CcmVMailDevDirNum_Type(SnmpAdminString):
    """Custom type ccmVMailDevDirNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CcmVMailDevDirNum_Type.__name__ = "SnmpAdminString"
_CcmVMailDevDirNum_Object = MibTableColumn
ccmVMailDevDirNum = _CcmVMailDevDirNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 12, 2, 1, 2),
    _CcmVMailDevDirNum_Type()
)
ccmVMailDevDirNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmVMailDevDirNum.setStatus("current")
_CcmQualityReportAlarmConfigInfo_ObjectIdentity = ObjectIdentity
ccmQualityReportAlarmConfigInfo = _CcmQualityReportAlarmConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 13)
)


class _CcmQualityReportAlarmEnable_Type(TruthValue):
    """Custom type ccmQualityReportAlarmEnable based on TruthValue"""


_CcmQualityReportAlarmEnable_Object = MibScalar
ccmQualityReportAlarmEnable = _CcmQualityReportAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 13, 1),
    _CcmQualityReportAlarmEnable_Type()
)
ccmQualityReportAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmQualityReportAlarmEnable.setStatus("current")
_CcmSIPDeviceInfo_ObjectIdentity = ObjectIdentity
ccmSIPDeviceInfo = _CcmSIPDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14)
)
_CcmSIPDeviceTable_Object = MibTable
ccmSIPDeviceTable = _CcmSIPDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1)
)
if mibBuilder.loadTexts:
    ccmSIPDeviceTable.setStatus("current")
_CcmSIPDeviceEntry_Object = MibTableRow
ccmSIPDeviceEntry = _CcmSIPDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1)
)
ccmSIPDeviceEntry.setIndexNames(
    (0, "CISCO-CCM-MIB", "ccmSIPDevIndex"),
)
if mibBuilder.loadTexts:
    ccmSIPDeviceEntry.setStatus("current")
_CcmSIPDevIndex_Type = CcmIndex
_CcmSIPDevIndex_Object = MibTableColumn
ccmSIPDevIndex = _CcmSIPDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 1),
    _CcmSIPDevIndex_Type()
)
ccmSIPDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmSIPDevIndex.setStatus("current")


class _CcmSIPDevName_Type(SnmpAdminString):
    """Custom type ccmSIPDevName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcmSIPDevName_Type.__name__ = "SnmpAdminString"
_CcmSIPDevName_Object = MibTableColumn
ccmSIPDevName = _CcmSIPDevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 2),
    _CcmSIPDevName_Type()
)
ccmSIPDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPDevName.setStatus("current")
_CcmSIPDevProductTypeIndex_Type = CcmIndexOrZero
_CcmSIPDevProductTypeIndex_Object = MibTableColumn
ccmSIPDevProductTypeIndex = _CcmSIPDevProductTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 3),
    _CcmSIPDevProductTypeIndex_Type()
)
ccmSIPDevProductTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPDevProductTypeIndex.setStatus("current")


class _CcmSIPDevDescription_Type(SnmpAdminString):
    """Custom type ccmSIPDevDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmSIPDevDescription_Type.__name__ = "SnmpAdminString"
_CcmSIPDevDescription_Object = MibTableColumn
ccmSIPDevDescription = _CcmSIPDevDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 4),
    _CcmSIPDevDescription_Type()
)
ccmSIPDevDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPDevDescription.setStatus("current")
_CcmSIPDevInetAddressType_Type = InetAddressType
_CcmSIPDevInetAddressType_Object = MibTableColumn
ccmSIPDevInetAddressType = _CcmSIPDevInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 5),
    _CcmSIPDevInetAddressType_Type()
)
ccmSIPDevInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPDevInetAddressType.setStatus("deprecated")
_CcmSIPDevInetAddress_Type = InetAddress
_CcmSIPDevInetAddress_Object = MibTableColumn
ccmSIPDevInetAddress = _CcmSIPDevInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 6),
    _CcmSIPDevInetAddress_Type()
)
ccmSIPDevInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPDevInetAddress.setStatus("deprecated")
_CcmSIPInTransportProtocolType_Type = CcmSIPTransportProtocolType
_CcmSIPInTransportProtocolType_Object = MibTableColumn
ccmSIPInTransportProtocolType = _CcmSIPInTransportProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 7),
    _CcmSIPInTransportProtocolType_Type()
)
ccmSIPInTransportProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPInTransportProtocolType.setStatus("current")
_CcmSIPInPortNumber_Type = InetPortNumber
_CcmSIPInPortNumber_Object = MibTableColumn
ccmSIPInPortNumber = _CcmSIPInPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 8),
    _CcmSIPInPortNumber_Type()
)
ccmSIPInPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPInPortNumber.setStatus("current")
_CcmSIPOutTransportProtocolType_Type = CcmSIPTransportProtocolType
_CcmSIPOutTransportProtocolType_Object = MibTableColumn
ccmSIPOutTransportProtocolType = _CcmSIPOutTransportProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 9),
    _CcmSIPOutTransportProtocolType_Type()
)
ccmSIPOutTransportProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPOutTransportProtocolType.setStatus("current")
_CcmSIPOutPortNumber_Type = InetPortNumber
_CcmSIPOutPortNumber_Object = MibTableColumn
ccmSIPOutPortNumber = _CcmSIPOutPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 10),
    _CcmSIPOutPortNumber_Type()
)
ccmSIPOutPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPOutPortNumber.setStatus("current")
_CcmSIPDevInetAddressIPv4_Type = InetAddressIPv4
_CcmSIPDevInetAddressIPv4_Object = MibTableColumn
ccmSIPDevInetAddressIPv4 = _CcmSIPDevInetAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 11),
    _CcmSIPDevInetAddressIPv4_Type()
)
ccmSIPDevInetAddressIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPDevInetAddressIPv4.setStatus("current")
_CcmSIPDevInetAddressIPv6_Type = InetAddressIPv6
_CcmSIPDevInetAddressIPv6_Object = MibTableColumn
ccmSIPDevInetAddressIPv6 = _CcmSIPDevInetAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 1, 14, 1, 1, 12),
    _CcmSIPDevInetAddressIPv6_Type()
)
ccmSIPDevInetAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSIPDevInetAddressIPv6.setStatus("current")
_CcmMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ccmMIBNotificationPrefix = _CcmMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2)
)
_CcmMIBNotifications_ObjectIdentity = ObjectIdentity
ccmMIBNotifications = _CcmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0)
)
_CiscoCcmMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCcmMIBConformance = _CiscoCcmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3)
)
_CiscoCcmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCcmMIBCompliances = _CiscoCcmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1)
)
_CiscoCcmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCcmMIBGroups = _CiscoCcmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2)
)

# Managed Objects groups

ccmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 1)
)
ccmInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmGroupName"),
        ("CISCO-CCM-MIB", "ccmGroupTftpDefault"),
        ("CISCO-CCM-MIB", "ccmName"),
        ("CISCO-CCM-MIB", "ccmDescription"),
        ("CISCO-CCM-MIB", "ccmVersion"),
        ("CISCO-CCM-MIB", "ccmStatus"),
        ("CISCO-CCM-MIB", "ccmCMGroupMappingCMPriority"),
        ("CISCO-CCM-MIB", "ccmRegionName"),
        ("CISCO-CCM-MIB", "ccmRegionAvailableBandWidth"),
        ("CISCO-CCM-MIB", "ccmTimeZoneName"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffset"),
        ("CISCO-CCM-MIB", "ccmDevicePoolName"),
        ("CISCO-CCM-MIB", "ccmDevicePoolRegionIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolTimeZoneIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolGroupIndex"))
)
if mibBuilder.loadTexts:
    ccmInfoGroup.setStatus("obsolete")

ccmPhoneInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 2)
)
ccmPhoneInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmPhonePhysicalAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneType"),
        ("CISCO-CCM-MIB", "ccmPhoneDescription"),
        ("CISCO-CCM-MIB", "ccmPhoneUserName"),
        ("CISCO-CCM-MIB", "ccmPhoneIpAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneStatus"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmPhoneE911Location"),
        ("CISCO-CCM-MIB", "ccmPhoneLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneLastError"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastError"),
        ("CISCO-CCM-MIB", "ccmPhoneDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneExtension"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionIpAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionMultiLines"),
        ("CISCO-CCM-MIB", "ccmActivePhones"),
        ("CISCO-CCM-MIB", "ccmInActivePhones"))
)
if mibBuilder.loadTexts:
    ccmPhoneInfoGroup.setStatus("obsolete")

ccmGatewayInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 3)
)
ccmGatewayInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayType"),
        ("CISCO-CCM-MIB", "ccmGatewayDescription"),
        ("CISCO-CCM-MIB", "ccmGatewayStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayTrunkType"),
        ("CISCO-CCM-MIB", "ccmGatewayTrunkName"),
        ("CISCO-CCM-MIB", "ccmTrunkGatewayIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayTrunkStatus"),
        ("CISCO-CCM-MIB", "ccmActiveGateways"),
        ("CISCO-CCM-MIB", "ccmInActiveGateways"))
)
if mibBuilder.loadTexts:
    ccmGatewayInfoGroup.setStatus("obsolete")

ccmInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 4)
)
ccmInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmGroupName"),
        ("CISCO-CCM-MIB", "ccmGroupTftpDefault"),
        ("CISCO-CCM-MIB", "ccmName"),
        ("CISCO-CCM-MIB", "ccmDescription"),
        ("CISCO-CCM-MIB", "ccmVersion"),
        ("CISCO-CCM-MIB", "ccmStatus"),
        ("CISCO-CCM-MIB", "ccmInetAddressType"),
        ("CISCO-CCM-MIB", "ccmInetAddress"),
        ("CISCO-CCM-MIB", "ccmClusterId"),
        ("CISCO-CCM-MIB", "ccmCMGroupMappingCMPriority"),
        ("CISCO-CCM-MIB", "ccmRegionName"),
        ("CISCO-CCM-MIB", "ccmRegionAvailableBandWidth"),
        ("CISCO-CCM-MIB", "ccmTimeZoneName"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffset"),
        ("CISCO-CCM-MIB", "ccmDevicePoolName"),
        ("CISCO-CCM-MIB", "ccmDevicePoolRegionIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolTimeZoneIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolGroupIndex"))
)
if mibBuilder.loadTexts:
    ccmInfoGroupRev1.setStatus("obsolete")

ccmPhoneInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 5)
)
ccmPhoneInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmPhonePhysicalAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneType"),
        ("CISCO-CCM-MIB", "ccmPhoneDescription"),
        ("CISCO-CCM-MIB", "ccmPhoneUserName"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneStatus"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmPhoneE911Location"),
        ("CISCO-CCM-MIB", "ccmPhoneLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneLastError"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastError"),
        ("CISCO-CCM-MIB", "ccmPhoneDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneExtension"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionMultiLines"),
        ("CISCO-CCM-MIB", "ccmActivePhones"),
        ("CISCO-CCM-MIB", "ccmInActivePhones"))
)
if mibBuilder.loadTexts:
    ccmPhoneInfoGroupRev1.setStatus("obsolete")

ccmGatewayInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 6)
)
ccmGatewayInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayType"),
        ("CISCO-CCM-MIB", "ccmGatewayDescription"),
        ("CISCO-CCM-MIB", "ccmGatewayStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddress"),
        ("CISCO-CCM-MIB", "ccmActiveGateways"),
        ("CISCO-CCM-MIB", "ccmInActiveGateways"))
)
if mibBuilder.loadTexts:
    ccmGatewayInfoGroupRev1.setStatus("obsolete")

ccmMediaDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 7)
)
ccmMediaDeviceInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmMediaDeviceName"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceType"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddressType"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddress"))
)
if mibBuilder.loadTexts:
    ccmMediaDeviceInfoGroup.setStatus("obsolete")

ccmGatekeeperInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 8)
)
ccmGatekeeperInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmGatekeeperName"),
        ("CISCO-CCM-MIB", "ccmGatekeeperType"),
        ("CISCO-CCM-MIB", "ccmGatekeeperDescription"),
        ("CISCO-CCM-MIB", "ccmGatekeeperStatus"),
        ("CISCO-CCM-MIB", "ccmGatekeeperDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmGatekeeperInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatekeeperInetAddress"))
)
if mibBuilder.loadTexts:
    ccmGatekeeperInfoGroup.setStatus("obsolete")

ccmCTIDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 9)
)
ccmCTIDeviceInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmCTIDeviceName"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceType"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmCTIDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddressType"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddress"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceAppInfo"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNum"))
)
if mibBuilder.loadTexts:
    ccmCTIDeviceInfoGroup.setStatus("obsolete")

ccmNotificationsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 10)
)
ccmNotificationsInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmCallManagerAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailures"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedTime"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedName"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedAlarmInterval"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhoneUpdates"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusPhoneIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTime"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateType"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateAlarmInterv"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateStorePeriod"),
        ("CISCO-CCM-MIB", "ccmGatewayAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmGatewayFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmMediaResourceType"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListName"),
        ("CISCO-CCM-MIB", "ccmRouteListName"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfL2Status"))
)
if mibBuilder.loadTexts:
    ccmNotificationsInfoGroup.setStatus("obsolete")

ccmInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 12)
)
ccmInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmGroupName"),
        ("CISCO-CCM-MIB", "ccmGroupTftpDefault"),
        ("CISCO-CCM-MIB", "ccmName"),
        ("CISCO-CCM-MIB", "ccmDescription"),
        ("CISCO-CCM-MIB", "ccmVersion"),
        ("CISCO-CCM-MIB", "ccmStatus"),
        ("CISCO-CCM-MIB", "ccmInetAddressType"),
        ("CISCO-CCM-MIB", "ccmInetAddress"),
        ("CISCO-CCM-MIB", "ccmClusterId"),
        ("CISCO-CCM-MIB", "ccmCMGroupMappingCMPriority"),
        ("CISCO-CCM-MIB", "ccmRegionName"),
        ("CISCO-CCM-MIB", "ccmRegionAvailableBandWidth"),
        ("CISCO-CCM-MIB", "ccmTimeZoneName"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffsetHours"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffsetMinutes"),
        ("CISCO-CCM-MIB", "ccmDevicePoolName"),
        ("CISCO-CCM-MIB", "ccmDevicePoolRegionIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolTimeZoneIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolGroupIndex"),
        ("CISCO-CCM-MIB", "ccmCallManagerStartTime"))
)
if mibBuilder.loadTexts:
    ccmInfoGroupRev2.setStatus("obsolete")

ccmPhoneInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 13)
)
ccmPhoneInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmPhonePhysicalAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneType"),
        ("CISCO-CCM-MIB", "ccmPhoneDescription"),
        ("CISCO-CCM-MIB", "ccmPhoneUserName"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneStatus"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmPhoneE911Location"),
        ("CISCO-CCM-MIB", "ccmPhoneLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusReason"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmPhoneExtn"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnMultiLines"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddress"),
        ("CISCO-CCM-MIB", "ccmRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmUnregisteredPhones"),
        ("CISCO-CCM-MIB", "ccmRejectedPhones"),
        ("CISCO-CCM-MIB", "ccmPhoneTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionTableStateId"))
)
if mibBuilder.loadTexts:
    ccmPhoneInfoGroupRev2.setStatus("obsolete")

ccmGatewayInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 14)
)
ccmGatewayInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayType"),
        ("CISCO-CCM-MIB", "ccmGatewayDescription"),
        ("CISCO-CCM-MIB", "ccmGatewayStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddress"),
        ("CISCO-CCM-MIB", "ccmGatewayProductId"),
        ("CISCO-CCM-MIB", "ccmGatewayStatusReason"),
        ("CISCO-CCM-MIB", "ccmGatewayTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmGatewayTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmGatewayDChannelStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDChannelNumber"),
        ("CISCO-CCM-MIB", "ccmRegisteredGateways"),
        ("CISCO-CCM-MIB", "ccmUnregisteredGateways"),
        ("CISCO-CCM-MIB", "ccmRejectedGateways"),
        ("CISCO-CCM-MIB", "ccmGatewayTableStateId"))
)
if mibBuilder.loadTexts:
    ccmGatewayInfoGroupRev2.setStatus("obsolete")

ccmMediaDeviceInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 15)
)
ccmMediaDeviceInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmMediaDeviceName"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceType"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddressType"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddress"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatusReason"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmRegisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedMediaDevices"))
)
if mibBuilder.loadTexts:
    ccmMediaDeviceInfoGroupRev1.setStatus("obsolete")

ccmCTIDeviceInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 16)
)
ccmCTIDeviceInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmCTIDeviceName"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceType"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmCTIDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddressType"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddress"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatusReason"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNum"),
        ("CISCO-CCM-MIB", "ccmRegisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedCTIDevices"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTableStateId"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNumTableStateId"))
)
if mibBuilder.loadTexts:
    ccmCTIDeviceInfoGroupRev1.setStatus("obsolete")

ccmH323DeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 17)
)
ccmH323DeviceInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmH323DevName"),
        ("CISCO-CCM-MIB", "ccmH323DevProductId"),
        ("CISCO-CCM-MIB", "ccmH323DevDescription"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevStatus"),
        ("CISCO-CCM-MIB", "ccmH323DevStatusReason"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddress"))
)
if mibBuilder.loadTexts:
    ccmH323DeviceInfoGroup.setStatus("obsolete")

ccmVoiceMailDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 18)
)
ccmVoiceMailDeviceInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmVMailDevName"),
        ("CISCO-CCM-MIB", "ccmVMailDevProductId"),
        ("CISCO-CCM-MIB", "ccmVMailDevDescription"),
        ("CISCO-CCM-MIB", "ccmVMailDevStatus"),
        ("CISCO-CCM-MIB", "ccmVMailDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmVMailDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmVMailDevStatusReason"),
        ("CISCO-CCM-MIB", "ccmVMailDevTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmVMailDevTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmVMailDevDirNum"),
        ("CISCO-CCM-MIB", "ccmRegisteredVoiceMailDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredVoiceMailDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedVoiceMailDevices"))
)
if mibBuilder.loadTexts:
    ccmVoiceMailDeviceInfoGroup.setStatus("obsolete")

ccmNotificationsInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 19)
)
ccmNotificationsInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmCallManagerAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailures"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedTime"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedMacAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedAlarmInterval"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhFailedTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneUpdates"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusPhoneIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTime"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateType"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateReason"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateAlarmInterv"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhStatUpdtTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmGatewayFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmMediaResourceType"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListName"),
        ("CISCO-CCM-MIB", "ccmRouteListName"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfL2Status"))
)
if mibBuilder.loadTexts:
    ccmNotificationsInfoGroupRev1.setStatus("obsolete")

ccmInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 20)
)
ccmInfoGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmGroupName"),
        ("CISCO-CCM-MIB", "ccmGroupTftpDefault"),
        ("CISCO-CCM-MIB", "ccmName"),
        ("CISCO-CCM-MIB", "ccmDescription"),
        ("CISCO-CCM-MIB", "ccmVersion"),
        ("CISCO-CCM-MIB", "ccmStatus"),
        ("CISCO-CCM-MIB", "ccmInetAddressType"),
        ("CISCO-CCM-MIB", "ccmInetAddress"),
        ("CISCO-CCM-MIB", "ccmClusterId"),
        ("CISCO-CCM-MIB", "ccmCMGroupMappingCMPriority"),
        ("CISCO-CCM-MIB", "ccmRegionName"),
        ("CISCO-CCM-MIB", "ccmRegionAvailableBandWidth"),
        ("CISCO-CCM-MIB", "ccmTimeZoneName"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffsetHours"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffsetMinutes"),
        ("CISCO-CCM-MIB", "ccmDevicePoolName"),
        ("CISCO-CCM-MIB", "ccmDevicePoolRegionIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolTimeZoneIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolGroupIndex"),
        ("CISCO-CCM-MIB", "ccmProductType"),
        ("CISCO-CCM-MIB", "ccmProductName"),
        ("CISCO-CCM-MIB", "ccmProductCategory"),
        ("CISCO-CCM-MIB", "ccmCallManagerStartTime"),
        ("CISCO-CCM-MIB", "ccmSystemVersion"),
        ("CISCO-CCM-MIB", "ccmInstallationId"))
)
if mibBuilder.loadTexts:
    ccmInfoGroupRev3.setStatus("obsolete")

ccmNotificationsInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 21)
)
ccmNotificationsInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmCallManagerAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailures"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedTime"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedMacAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedAlarmInterval"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhFailedTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneUpdates"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusPhoneIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTime"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateType"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateReason"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateAlarmInterv"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhStatUpdtTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmGatewayFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmMediaResourceType"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListName"),
        ("CISCO-CCM-MIB", "ccmRouteListName"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfL2Status"),
        ("CISCO-CCM-MIB", "ccmMaliciousCallAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallTime"),
        ("CISCO-CCM-MIB", "ccmQualityReportAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmQualityRprtSourceDevName"),
        ("CISCO-CCM-MIB", "ccmQualityRprtClusterId"),
        ("CISCO-CCM-MIB", "ccmQualityRprtCategory"),
        ("CISCO-CCM-MIB", "ccmQualityRprtReasonCode"),
        ("CISCO-CCM-MIB", "ccmQualityRprtTime"))
)
if mibBuilder.loadTexts:
    ccmNotificationsInfoGroupRev2.setStatus("obsolete")

ccmSIPDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 23)
)
ccmSIPDeviceInfoGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmSIPDevName"),
        ("CISCO-CCM-MIB", "ccmSIPDevProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmSIPDevDescription"),
        ("CISCO-CCM-MIB", "ccmSIPDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmSIPDevInetAddress"))
)
if mibBuilder.loadTexts:
    ccmSIPDeviceInfoGroup.setStatus("obsolete")

ccmPhoneInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 24)
)
ccmPhoneInfoGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmPhonePhysicalAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneDescription"),
        ("CISCO-CCM-MIB", "ccmPhoneUserName"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneStatus"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmPhoneE911Location"),
        ("CISCO-CCM-MIB", "ccmPhoneLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusReason"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmPhoneProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneExtn"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnMultiLines"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddress"),
        ("CISCO-CCM-MIB", "ccmRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmUnregisteredPhones"),
        ("CISCO-CCM-MIB", "ccmRejectedPhones"),
        ("CISCO-CCM-MIB", "ccmPhoneTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionTableStateId"))
)
if mibBuilder.loadTexts:
    ccmPhoneInfoGroupRev3.setStatus("obsolete")

ccmGatewayInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 25)
)
ccmGatewayInfoGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayDescription"),
        ("CISCO-CCM-MIB", "ccmGatewayStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddress"),
        ("CISCO-CCM-MIB", "ccmGatewayStatusReason"),
        ("CISCO-CCM-MIB", "ccmGatewayTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmGatewayTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmGatewayDChannelStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDChannelNumber"),
        ("CISCO-CCM-MIB", "ccmGatewayProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmRegisteredGateways"),
        ("CISCO-CCM-MIB", "ccmUnregisteredGateways"),
        ("CISCO-CCM-MIB", "ccmRejectedGateways"),
        ("CISCO-CCM-MIB", "ccmGatewayTableStateId"))
)
if mibBuilder.loadTexts:
    ccmGatewayInfoGroupRev3.setStatus("deprecated")

ccmMediaDeviceInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 26)
)
ccmMediaDeviceInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmMediaDeviceName"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddressType"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddress"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatusReason"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmRegisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedMediaDevices"))
)
if mibBuilder.loadTexts:
    ccmMediaDeviceInfoGroupRev2.setStatus("deprecated")

ccmCTIDeviceInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 27)
)
ccmCTIDeviceInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmCTIDeviceName"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmCTIDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddressType"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddress"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatusReason"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNum"),
        ("CISCO-CCM-MIB", "ccmRegisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedCTIDevices"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTableStateId"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNumTableStateId"))
)
if mibBuilder.loadTexts:
    ccmCTIDeviceInfoGroupRev2.setStatus("deprecated")

ccmH323DeviceInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 28)
)
ccmH323DeviceInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmH323DevName"),
        ("CISCO-CCM-MIB", "ccmH323DevDescription"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevStatus"),
        ("CISCO-CCM-MIB", "ccmH323DevStatusReason"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevProductTypeIndex"))
)
if mibBuilder.loadTexts:
    ccmH323DeviceInfoGroupRev1.setStatus("obsolete")

ccmVoiceMailDeviceInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 29)
)
ccmVoiceMailDeviceInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmVMailDevName"),
        ("CISCO-CCM-MIB", "ccmVMailDevDescription"),
        ("CISCO-CCM-MIB", "ccmVMailDevStatus"),
        ("CISCO-CCM-MIB", "ccmVMailDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmVMailDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmVMailDevStatusReason"),
        ("CISCO-CCM-MIB", "ccmVMailDevTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmVMailDevTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmVMailDevProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmVMailDevDirNum"),
        ("CISCO-CCM-MIB", "ccmRegisteredVoiceMailDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredVoiceMailDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedVoiceMailDevices"))
)
if mibBuilder.loadTexts:
    ccmVoiceMailDeviceInfoGroupRev1.setStatus("deprecated")

ccmPhoneInfoGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 30)
)
ccmPhoneInfoGroupRev4.setObjects(
      *(("CISCO-CCM-MIB", "ccmPhonePhysicalAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneDescription"),
        ("CISCO-CCM-MIB", "ccmPhoneUserName"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneStatus"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmPhoneE911Location"),
        ("CISCO-CCM-MIB", "ccmPhoneLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusReason"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmPhoneProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneProtocol"),
        ("CISCO-CCM-MIB", "ccmPhoneName"),
        ("CISCO-CCM-MIB", "ccmPhoneExtn"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnMultiLines"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnStatus"),
        ("CISCO-CCM-MIB", "ccmRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmUnregisteredPhones"),
        ("CISCO-CCM-MIB", "ccmRejectedPhones"),
        ("CISCO-CCM-MIB", "ccmPartiallyRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmPhoneTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionTableStateId"))
)
if mibBuilder.loadTexts:
    ccmPhoneInfoGroupRev4.setStatus("deprecated")

ccmSIPDeviceInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 31)
)
ccmSIPDeviceInfoGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmSIPDevName"),
        ("CISCO-CCM-MIB", "ccmSIPDevProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmSIPDevDescription"),
        ("CISCO-CCM-MIB", "ccmSIPDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmSIPDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmSIPInTransportProtocolType"),
        ("CISCO-CCM-MIB", "ccmSIPInPortNumber"),
        ("CISCO-CCM-MIB", "ccmSIPOutTransportProtocolType"),
        ("CISCO-CCM-MIB", "ccmSIPOutPortNumber"))
)
if mibBuilder.loadTexts:
    ccmSIPDeviceInfoGroupRev1.setStatus("deprecated")

ccmNotificationsInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 32)
)
ccmNotificationsInfoGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmCallManagerAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailures"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedTime"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedMacAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedAlarmInterval"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhFailedTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneUpdates"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusPhoneIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTime"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateType"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateReason"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateAlarmInterv"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhStatUpdtTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmGatewayFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmMediaResourceType"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListName"),
        ("CISCO-CCM-MIB", "ccmRouteListName"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfL2Status"),
        ("CISCO-CCM-MIB", "ccmMaliciousCallAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallTime"),
        ("CISCO-CCM-MIB", "ccmQualityReportAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmQualityRprtSourceDevName"),
        ("CISCO-CCM-MIB", "ccmQualityRprtClusterId"),
        ("CISCO-CCM-MIB", "ccmQualityRprtCategory"),
        ("CISCO-CCM-MIB", "ccmQualityRprtReasonCode"),
        ("CISCO-CCM-MIB", "ccmQualityRprtTime"),
        ("CISCO-CCM-MIB", "ccmTLSDevName"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmTLSConnFailTime"),
        ("CISCO-CCM-MIB", "ccmTLSConnectionFailReasonCode"))
)
if mibBuilder.loadTexts:
    ccmNotificationsInfoGroupRev3.setStatus("deprecated")

ccmInfoGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 34)
)
ccmInfoGroupRev4.setObjects(
      *(("CISCO-CCM-MIB", "ccmGroupName"),
        ("CISCO-CCM-MIB", "ccmGroupTftpDefault"),
        ("CISCO-CCM-MIB", "ccmName"),
        ("CISCO-CCM-MIB", "ccmDescription"),
        ("CISCO-CCM-MIB", "ccmVersion"),
        ("CISCO-CCM-MIB", "ccmStatus"),
        ("CISCO-CCM-MIB", "ccmInetAddressType"),
        ("CISCO-CCM-MIB", "ccmInetAddress"),
        ("CISCO-CCM-MIB", "ccmClusterId"),
        ("CISCO-CCM-MIB", "ccmCMGroupMappingCMPriority"),
        ("CISCO-CCM-MIB", "ccmRegionName"),
        ("CISCO-CCM-MIB", "ccmRegionAvailableBandWidth"),
        ("CISCO-CCM-MIB", "ccmTimeZoneName"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffsetHours"),
        ("CISCO-CCM-MIB", "ccmTimeZoneOffsetMinutes"),
        ("CISCO-CCM-MIB", "ccmDevicePoolName"),
        ("CISCO-CCM-MIB", "ccmDevicePoolRegionIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolTimeZoneIndex"),
        ("CISCO-CCM-MIB", "ccmDevicePoolGroupIndex"),
        ("CISCO-CCM-MIB", "ccmProductType"),
        ("CISCO-CCM-MIB", "ccmProductName"),
        ("CISCO-CCM-MIB", "ccmProductCategory"),
        ("CISCO-CCM-MIB", "ccmCallManagerStartTime"),
        ("CISCO-CCM-MIB", "ccmSystemVersion"),
        ("CISCO-CCM-MIB", "ccmInstallationId"),
        ("CISCO-CCM-MIB", "ccmInetAddress2Type"),
        ("CISCO-CCM-MIB", "ccmInetAddress2"))
)
if mibBuilder.loadTexts:
    ccmInfoGroupRev4.setStatus("current")

ccmPhoneInfoGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 35)
)
ccmPhoneInfoGroupRev5.setObjects(
      *(("CISCO-CCM-MIB", "ccmPhonePhysicalAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneDescription"),
        ("CISCO-CCM-MIB", "ccmPhoneUserName"),
        ("CISCO-CCM-MIB", "ccmPhoneStatus"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmPhoneE911Location"),
        ("CISCO-CCM-MIB", "ccmPhoneLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusReason"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmPhoneProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneProtocol"),
        ("CISCO-CCM-MIB", "ccmPhoneName"),
        ("CISCO-CCM-MIB", "ccmPhoneExtn"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnMultiLines"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnStatus"),
        ("CISCO-CCM-MIB", "ccmRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmUnregisteredPhones"),
        ("CISCO-CCM-MIB", "ccmRejectedPhones"),
        ("CISCO-CCM-MIB", "ccmPartiallyRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmPhoneTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressIPv6"),
        ("CISCO-CCM-MIB", "ccmPhoneIPv4Attribute"),
        ("CISCO-CCM-MIB", "ccmPhoneIPv6Attribute"),
        ("CISCO-CCM-MIB", "ccmPhoneActiveLoadID"))
)
if mibBuilder.loadTexts:
    ccmPhoneInfoGroupRev5.setStatus("deprecated")

ccmMediaDeviceInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 36)
)
ccmMediaDeviceInfoGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmMediaDeviceName"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatusReason"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmRegisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedMediaDevices"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddressIPv6"))
)
if mibBuilder.loadTexts:
    ccmMediaDeviceInfoGroupRev3.setStatus("deprecated")

ccmSIPDeviceInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 37)
)
ccmSIPDeviceInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmSIPDevName"),
        ("CISCO-CCM-MIB", "ccmSIPDevProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmSIPDevDescription"),
        ("CISCO-CCM-MIB", "ccmSIPInTransportProtocolType"),
        ("CISCO-CCM-MIB", "ccmSIPInPortNumber"),
        ("CISCO-CCM-MIB", "ccmSIPOutTransportProtocolType"),
        ("CISCO-CCM-MIB", "ccmSIPOutPortNumber"),
        ("CISCO-CCM-MIB", "ccmSIPDevInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmSIPDevInetAddressIPv6"),
        ("CISCO-CCM-MIB", "ccmSIPTableEntries"))
)
if mibBuilder.loadTexts:
    ccmSIPDeviceInfoGroupRev2.setStatus("current")

ccmNotificationsInfoGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 38)
)
ccmNotificationsInfoGroupRev4.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmCallManagerAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailures"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedTime"),
        ("CISCO-CCM-MIB", "ccmPhoneFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedMacAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedAlarmInterval"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhFailedTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneUpdates"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusPhoneIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTime"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateType"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateReason"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateAlarmInterv"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhStatUpdtTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmGatewayFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmMediaResourceType"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListName"),
        ("CISCO-CCM-MIB", "ccmRouteListName"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfL2Status"),
        ("CISCO-CCM-MIB", "ccmMaliciousCallAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallTime"),
        ("CISCO-CCM-MIB", "ccmQualityReportAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmQualityRprtSourceDevName"),
        ("CISCO-CCM-MIB", "ccmQualityRprtClusterId"),
        ("CISCO-CCM-MIB", "ccmQualityRprtCategory"),
        ("CISCO-CCM-MIB", "ccmQualityRprtReasonCode"),
        ("CISCO-CCM-MIB", "ccmQualityRprtTime"),
        ("CISCO-CCM-MIB", "ccmTLSDevName"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmTLSConnFailTime"),
        ("CISCO-CCM-MIB", "ccmTLSConnectionFailReasonCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressIPv6"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedIPv4Attribute"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedIPv6Attribute"))
)
if mibBuilder.loadTexts:
    ccmNotificationsInfoGroupRev4.setStatus("deprecated")

ccmH323DeviceInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 39)
)
ccmH323DeviceInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmH323DevName"),
        ("CISCO-CCM-MIB", "ccmH323DevDescription"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevStatus"),
        ("CISCO-CCM-MIB", "ccmH323DevStatusReason"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmH323TableEntries"))
)
if mibBuilder.loadTexts:
    ccmH323DeviceInfoGroupRev2.setStatus("deprecated")

ccmCTIDeviceInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 40)
)
ccmCTIDeviceInfoGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmCTIDeviceName"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmCTIDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatusReason"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNum"),
        ("CISCO-CCM-MIB", "ccmRegisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedCTIDevices"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTableStateId"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNumTableStateId"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddressIPv6"))
)
if mibBuilder.loadTexts:
    ccmCTIDeviceInfoGroupRev3.setStatus("deprecated")

ccmPhoneInfoGroupRev6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 41)
)
ccmPhoneInfoGroupRev6.setObjects(
      *(("CISCO-CCM-MIB", "ccmPhonePhysicalAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneDescription"),
        ("CISCO-CCM-MIB", "ccmPhoneUserName"),
        ("CISCO-CCM-MIB", "ccmPhoneStatus"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmPhoneE911Location"),
        ("CISCO-CCM-MIB", "ccmPhoneLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmPhoneProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneProtocol"),
        ("CISCO-CCM-MIB", "ccmPhoneName"),
        ("CISCO-CCM-MIB", "ccmPhoneExtn"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnMultiLines"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddressType"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnInetAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneExtnStatus"),
        ("CISCO-CCM-MIB", "ccmRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmUnregisteredPhones"),
        ("CISCO-CCM-MIB", "ccmRejectedPhones"),
        ("CISCO-CCM-MIB", "ccmPartiallyRegisteredPhones"),
        ("CISCO-CCM-MIB", "ccmPhoneTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhoneExtensionTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmPhoneInetAddressIPv6"),
        ("CISCO-CCM-MIB", "ccmPhoneIPv4Attribute"),
        ("CISCO-CCM-MIB", "ccmPhoneIPv6Attribute"),
        ("CISCO-CCM-MIB", "ccmPhoneActiveLoadID"),
        ("CISCO-CCM-MIB", "ccmPhoneUnregReason"),
        ("CISCO-CCM-MIB", "ccmPhoneRegFailReason"))
)
if mibBuilder.loadTexts:
    ccmPhoneInfoGroupRev6.setStatus("current")

ccmNotificationsInfoGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 42)
)
ccmNotificationsInfoGroupRev5.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmCallManagerAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmFailCauseCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailures"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedTime"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedMacAddress"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedAlarmInterval"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhFailedTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneUpdates"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusPhoneIndex"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTime"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateType"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateAlarmInterv"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateStorePeriod"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdateTableStateId"),
        ("CISCO-CCM-MIB", "ccmPhStatUpdtTblLastAddedIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmMediaResourceType"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListName"),
        ("CISCO-CCM-MIB", "ccmRouteListName"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfL2Status"),
        ("CISCO-CCM-MIB", "ccmMaliciousCallAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallTime"),
        ("CISCO-CCM-MIB", "ccmQualityReportAlarmEnable"),
        ("CISCO-CCM-MIB", "ccmQualityRprtSourceDevName"),
        ("CISCO-CCM-MIB", "ccmQualityRprtClusterId"),
        ("CISCO-CCM-MIB", "ccmQualityRprtCategory"),
        ("CISCO-CCM-MIB", "ccmQualityRprtReasonCode"),
        ("CISCO-CCM-MIB", "ccmQualityRprtTime"),
        ("CISCO-CCM-MIB", "ccmTLSDevName"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmTLSConnFailTime"),
        ("CISCO-CCM-MIB", "ccmTLSConnectionFailReasonCode"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedInetAddressIPv6"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedIPv4Attribute"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedIPv6Attribute"),
        ("CISCO-CCM-MIB", "ccmPhoneFailedRegFailReason"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUnregReason"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusRegFailReason"),
        ("CISCO-CCM-MIB", "ccmGatewayRegFailCauseCode"))
)
if mibBuilder.loadTexts:
    ccmNotificationsInfoGroupRev5.setStatus("current")

ccmGatewayInfoGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 43)
)
ccmGatewayInfoGroupRev4.setObjects(
      *(("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayDescription"),
        ("CISCO-CCM-MIB", "ccmGatewayStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddress"),
        ("CISCO-CCM-MIB", "ccmGatewayTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmGatewayTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmGatewayDChannelStatus"),
        ("CISCO-CCM-MIB", "ccmGatewayDChannelNumber"),
        ("CISCO-CCM-MIB", "ccmGatewayProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmRegisteredGateways"),
        ("CISCO-CCM-MIB", "ccmUnregisteredGateways"),
        ("CISCO-CCM-MIB", "ccmRejectedGateways"),
        ("CISCO-CCM-MIB", "ccmGatewayTableStateId"),
        ("CISCO-CCM-MIB", "ccmGatewayUnregReason"),
        ("CISCO-CCM-MIB", "ccmGatewayRegFailReason"))
)
if mibBuilder.loadTexts:
    ccmGatewayInfoGroupRev4.setStatus("current")

ccmMediaDeviceInfoGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 44)
)
ccmMediaDeviceInfoGroupRev4.setObjects(
      *(("CISCO-CCM-MIB", "ccmMediaDeviceName"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmRegisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredMediaDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedMediaDevices"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceInetAddressIPv6"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceUnregReason"),
        ("CISCO-CCM-MIB", "ccmMediaDeviceRegFailReason"))
)
if mibBuilder.loadTexts:
    ccmMediaDeviceInfoGroupRev4.setStatus("current")

ccmCTIDeviceInfoGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 45)
)
ccmCTIDeviceInfoGroupRev4.setObjects(
      *(("CISCO-CCM-MIB", "ccmCTIDeviceName"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDescription"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceStatus"),
        ("CISCO-CCM-MIB", "ccmCTIDevicePoolIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNum"),
        ("CISCO-CCM-MIB", "ccmRegisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredCTIDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedCTIDevices"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceTableStateId"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceDirNumTableStateId"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddressIPv4"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceInetAddressIPv6"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceUnregReason"),
        ("CISCO-CCM-MIB", "ccmCTIDeviceRegFailReason"))
)
if mibBuilder.loadTexts:
    ccmCTIDeviceInfoGroupRev4.setStatus("current")

ccmH323DeviceInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 46)
)
ccmH323DeviceInfoGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmH323DevName"),
        ("CISCO-CCM-MIB", "ccmH323DevDescription"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevCnfgGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK3InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK4InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevAltGK5InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevActGKInetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevStatus"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmH323DevTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM1InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM2InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddressType"),
        ("CISCO-CCM-MIB", "ccmH323DevRmtCM3InetAddress"),
        ("CISCO-CCM-MIB", "ccmH323DevProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmH323TableEntries"),
        ("CISCO-CCM-MIB", "ccmH323DevUnregReason"),
        ("CISCO-CCM-MIB", "ccmH323DevRegFailReason"))
)
if mibBuilder.loadTexts:
    ccmH323DeviceInfoGroupRev3.setStatus("current")

ccmVoiceMailDeviceInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 47)
)
ccmVoiceMailDeviceInfoGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmVMailDevName"),
        ("CISCO-CCM-MIB", "ccmVMailDevDescription"),
        ("CISCO-CCM-MIB", "ccmVMailDevStatus"),
        ("CISCO-CCM-MIB", "ccmVMailDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmVMailDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmVMailDevTimeLastStatusUpdt"),
        ("CISCO-CCM-MIB", "ccmVMailDevTimeLastRegistered"),
        ("CISCO-CCM-MIB", "ccmVMailDevProductTypeIndex"),
        ("CISCO-CCM-MIB", "ccmVMailDevDirNum"),
        ("CISCO-CCM-MIB", "ccmRegisteredVoiceMailDevices"),
        ("CISCO-CCM-MIB", "ccmUnregisteredVoiceMailDevices"),
        ("CISCO-CCM-MIB", "ccmRejectedVoiceMailDevices"),
        ("CISCO-CCM-MIB", "ccmVMailDevUnregReason"),
        ("CISCO-CCM-MIB", "ccmVMailDevRegFailReason"))
)
if mibBuilder.loadTexts:
    ccmVoiceMailDeviceInfoGroupRev2.setStatus("current")


# Notification objects

ccmCallManagerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 1)
)
ccmCallManagerFailed.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmFailCauseCode"))
)
if mibBuilder.loadTexts:
    ccmCallManagerFailed.setStatus(
        "current"
    )

ccmPhoneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 2)
)
ccmPhoneFailed.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmPhoneFailures"))
)
if mibBuilder.loadTexts:
    ccmPhoneFailed.setStatus(
        "current"
    )

ccmPhoneStatusUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 3)
)
ccmPhoneStatusUpdate.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmPhoneUpdates"))
)
if mibBuilder.loadTexts:
    ccmPhoneStatusUpdate.setStatus(
        "current"
    )

ccmGatewayFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 4)
)
ccmGatewayFailed.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddress"),
        ("CISCO-CCM-MIB", "ccmGatewayFailCauseCode"))
)
if mibBuilder.loadTexts:
    ccmGatewayFailed.setStatus(
        "deprecated"
    )

ccmMediaResourceListExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 5)
)
ccmMediaResourceListExhausted.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmMediaResourceType"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListName"))
)
if mibBuilder.loadTexts:
    ccmMediaResourceListExhausted.setStatus(
        "current"
    )

ccmRouteListExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 6)
)
ccmRouteListExhausted.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmRouteListName"))
)
if mibBuilder.loadTexts:
    ccmRouteListExhausted.setStatus(
        "current"
    )

ccmGatewayLayer2Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 7)
)
ccmGatewayLayer2Change.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddress"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfIndex"),
        ("CISCO-CCM-MIB", "ccmGatewayPhysIfL2Status"))
)
if mibBuilder.loadTexts:
    ccmGatewayLayer2Change.setStatus(
        "current"
    )

ccmMaliciousCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 8)
)
ccmMaliciousCall.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCalledDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyName"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingPartyNumber"),
        ("CISCO-CCM-MIB", "ccmMaliCallCallingDeviceName"),
        ("CISCO-CCM-MIB", "ccmMaliCallTime"))
)
if mibBuilder.loadTexts:
    ccmMaliciousCall.setStatus(
        "current"
    )

ccmQualityReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 9)
)
ccmQualityReport.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmQualityRprtSourceDevName"),
        ("CISCO-CCM-MIB", "ccmQualityRprtClusterId"),
        ("CISCO-CCM-MIB", "ccmQualityRprtCategory"),
        ("CISCO-CCM-MIB", "ccmQualityRprtReasonCode"),
        ("CISCO-CCM-MIB", "ccmQualityRprtTime"))
)
if mibBuilder.loadTexts:
    ccmQualityReport.setStatus(
        "current"
    )

ccmTLSConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 10)
)
ccmTLSConnectionFailure.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmTLSDevName"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddressType"),
        ("CISCO-CCM-MIB", "ccmTLSDevInetAddress"),
        ("CISCO-CCM-MIB", "ccmTLSConnectionFailReasonCode"),
        ("CISCO-CCM-MIB", "ccmTLSConnFailTime"))
)
if mibBuilder.loadTexts:
    ccmTLSConnectionFailure.setStatus(
        "current"
    )

ccmGatewayFailedReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 2, 0, 11)
)
ccmGatewayFailedReason.setObjects(
      *(("CISCO-CCM-MIB", "ccmAlarmSeverity"),
        ("CISCO-CCM-MIB", "ccmGatewayName"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddressType"),
        ("CISCO-CCM-MIB", "ccmGatewayInetAddress"),
        ("CISCO-CCM-MIB", "ccmGatewayRegFailCauseCode"))
)
if mibBuilder.loadTexts:
    ccmGatewayFailedReason.setStatus(
        "current"
    )


# Notifications groups

ccmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 11)
)
ccmNotificationsGroup.setObjects(
      *(("CISCO-CCM-MIB", "ccmCallManagerFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdate"),
        ("CISCO-CCM-MIB", "ccmGatewayFailed"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListExhausted"),
        ("CISCO-CCM-MIB", "ccmRouteListExhausted"),
        ("CISCO-CCM-MIB", "ccmGatewayLayer2Change"))
)
if mibBuilder.loadTexts:
    ccmNotificationsGroup.setStatus(
        "obsolete"
    )

ccmNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 22)
)
ccmNotificationsGroupRev1.setObjects(
      *(("CISCO-CCM-MIB", "ccmCallManagerFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdate"),
        ("CISCO-CCM-MIB", "ccmGatewayFailed"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListExhausted"),
        ("CISCO-CCM-MIB", "ccmRouteListExhausted"),
        ("CISCO-CCM-MIB", "ccmGatewayLayer2Change"),
        ("CISCO-CCM-MIB", "ccmMaliciousCall"),
        ("CISCO-CCM-MIB", "ccmQualityReport"))
)
if mibBuilder.loadTexts:
    ccmNotificationsGroupRev1.setStatus(
        "obsolete"
    )

ccmNotificationsGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 33)
)
ccmNotificationsGroupRev2.setObjects(
      *(("CISCO-CCM-MIB", "ccmCallManagerFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdate"),
        ("CISCO-CCM-MIB", "ccmGatewayFailed"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListExhausted"),
        ("CISCO-CCM-MIB", "ccmRouteListExhausted"),
        ("CISCO-CCM-MIB", "ccmGatewayLayer2Change"),
        ("CISCO-CCM-MIB", "ccmMaliciousCall"),
        ("CISCO-CCM-MIB", "ccmQualityReport"),
        ("CISCO-CCM-MIB", "ccmTLSConnectionFailure"))
)
if mibBuilder.loadTexts:
    ccmNotificationsGroupRev2.setStatus(
        "deprecated"
    )

ccmNotificationsGroupRev3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 2, 48)
)
ccmNotificationsGroupRev3.setObjects(
      *(("CISCO-CCM-MIB", "ccmCallManagerFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneFailed"),
        ("CISCO-CCM-MIB", "ccmPhoneStatusUpdate"),
        ("CISCO-CCM-MIB", "ccmGatewayFailedReason"),
        ("CISCO-CCM-MIB", "ccmMediaResourceListExhausted"),
        ("CISCO-CCM-MIB", "ccmRouteListExhausted"),
        ("CISCO-CCM-MIB", "ccmGatewayLayer2Change"),
        ("CISCO-CCM-MIB", "ccmMaliciousCall"),
        ("CISCO-CCM-MIB", "ccmQualityReport"),
        ("CISCO-CCM-MIB", "ccmTLSConnectionFailure"))
)
if mibBuilder.loadTexts:
    ccmNotificationsGroupRev3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCcmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBCompliance.setStatus(
        "obsolete"
    )

ciscoCcmMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBComplianceRev1.setStatus(
        "obsolete"
    )

ciscoCcmMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBComplianceRev2.setStatus(
        "obsolete"
    )

ciscoCcmMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBComplianceRev3.setStatus(
        "obsolete"
    )

ciscoCcmMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBComplianceRev4.setStatus(
        "obsolete"
    )

ciscoCcmMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoCcmMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoCcmMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 156, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoCcmMIBComplianceRev7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CCM-MIB",
    **{"CcmIndex": CcmIndex,
       "CcmIndexOrZero": CcmIndexOrZero,
       "CcmDevFailCauseCode": CcmDevFailCauseCode,
       "CcmDevRegFailCauseCode": CcmDevRegFailCauseCode,
       "CcmDevUnregCauseCode": CcmDevUnregCauseCode,
       "CcmDeviceStatus": CcmDeviceStatus,
       "CcmPhoneProtocolType": CcmPhoneProtocolType,
       "CcmDeviceLineStatus": CcmDeviceLineStatus,
       "CcmSIPTransportProtocolType": CcmSIPTransportProtocolType,
       "CcmDeviceProductId": CcmDeviceProductId,
       "ciscoCcmMIB": ciscoCcmMIB,
       "ciscoCcmMIBObjects": ciscoCcmMIBObjects,
       "ccmGeneralInfo": ccmGeneralInfo,
       "ccmGroupTable": ccmGroupTable,
       "ccmGroupEntry": ccmGroupEntry,
       "ccmGroupIndex": ccmGroupIndex,
       "ccmGroupName": ccmGroupName,
       "ccmGroupTftpDefault": ccmGroupTftpDefault,
       "ccmTable": ccmTable,
       "ccmEntry": ccmEntry,
       "ccmIndex": ccmIndex,
       "ccmName": ccmName,
       "ccmDescription": ccmDescription,
       "ccmVersion": ccmVersion,
       "ccmStatus": ccmStatus,
       "ccmInetAddressType": ccmInetAddressType,
       "ccmInetAddress": ccmInetAddress,
       "ccmClusterId": ccmClusterId,
       "ccmInetAddress2Type": ccmInetAddress2Type,
       "ccmInetAddress2": ccmInetAddress2,
       "ccmGroupMappingTable": ccmGroupMappingTable,
       "ccmGroupMappingEntry": ccmGroupMappingEntry,
       "ccmCMGroupMappingCMPriority": ccmCMGroupMappingCMPriority,
       "ccmRegionTable": ccmRegionTable,
       "ccmRegionEntry": ccmRegionEntry,
       "ccmRegionIndex": ccmRegionIndex,
       "ccmRegionName": ccmRegionName,
       "ccmRegionPairTable": ccmRegionPairTable,
       "ccmRegionPairEntry": ccmRegionPairEntry,
       "ccmRegionSrcIndex": ccmRegionSrcIndex,
       "ccmRegionDestIndex": ccmRegionDestIndex,
       "ccmRegionAvailableBandWidth": ccmRegionAvailableBandWidth,
       "ccmTimeZoneTable": ccmTimeZoneTable,
       "ccmTimeZoneEntry": ccmTimeZoneEntry,
       "ccmTimeZoneIndex": ccmTimeZoneIndex,
       "ccmTimeZoneName": ccmTimeZoneName,
       "ccmTimeZoneOffset": ccmTimeZoneOffset,
       "ccmTimeZoneOffsetHours": ccmTimeZoneOffsetHours,
       "ccmTimeZoneOffsetMinutes": ccmTimeZoneOffsetMinutes,
       "ccmDevicePoolTable": ccmDevicePoolTable,
       "ccmDevicePoolEntry": ccmDevicePoolEntry,
       "ccmDevicePoolIndex": ccmDevicePoolIndex,
       "ccmDevicePoolName": ccmDevicePoolName,
       "ccmDevicePoolRegionIndex": ccmDevicePoolRegionIndex,
       "ccmDevicePoolTimeZoneIndex": ccmDevicePoolTimeZoneIndex,
       "ccmDevicePoolGroupIndex": ccmDevicePoolGroupIndex,
       "ccmProductTypeTable": ccmProductTypeTable,
       "ccmProductTypeEntry": ccmProductTypeEntry,
       "ccmProductTypeIndex": ccmProductTypeIndex,
       "ccmProductType": ccmProductType,
       "ccmProductName": ccmProductName,
       "ccmProductCategory": ccmProductCategory,
       "ccmPhoneInfo": ccmPhoneInfo,
       "ccmPhoneTable": ccmPhoneTable,
       "ccmPhoneEntry": ccmPhoneEntry,
       "ccmPhoneIndex": ccmPhoneIndex,
       "ccmPhonePhysicalAddress": ccmPhonePhysicalAddress,
       "ccmPhoneType": ccmPhoneType,
       "ccmPhoneDescription": ccmPhoneDescription,
       "ccmPhoneUserName": ccmPhoneUserName,
       "ccmPhoneIpAddress": ccmPhoneIpAddress,
       "ccmPhoneStatus": ccmPhoneStatus,
       "ccmPhoneTimeLastRegistered": ccmPhoneTimeLastRegistered,
       "ccmPhoneE911Location": ccmPhoneE911Location,
       "ccmPhoneLoadID": ccmPhoneLoadID,
       "ccmPhoneLastError": ccmPhoneLastError,
       "ccmPhoneTimeLastError": ccmPhoneTimeLastError,
       "ccmPhoneDevicePoolIndex": ccmPhoneDevicePoolIndex,
       "ccmPhoneInetAddressType": ccmPhoneInetAddressType,
       "ccmPhoneInetAddress": ccmPhoneInetAddress,
       "ccmPhoneStatusReason": ccmPhoneStatusReason,
       "ccmPhoneTimeLastStatusUpdt": ccmPhoneTimeLastStatusUpdt,
       "ccmPhoneProductTypeIndex": ccmPhoneProductTypeIndex,
       "ccmPhoneProtocol": ccmPhoneProtocol,
       "ccmPhoneName": ccmPhoneName,
       "ccmPhoneInetAddressIPv4": ccmPhoneInetAddressIPv4,
       "ccmPhoneInetAddressIPv6": ccmPhoneInetAddressIPv6,
       "ccmPhoneIPv4Attribute": ccmPhoneIPv4Attribute,
       "ccmPhoneIPv6Attribute": ccmPhoneIPv6Attribute,
       "ccmPhoneActiveLoadID": ccmPhoneActiveLoadID,
       "ccmPhoneUnregReason": ccmPhoneUnregReason,
       "ccmPhoneRegFailReason": ccmPhoneRegFailReason,
       "ccmPhoneExtensionTable": ccmPhoneExtensionTable,
       "ccmPhoneExtensionEntry": ccmPhoneExtensionEntry,
       "ccmPhoneExtensionIndex": ccmPhoneExtensionIndex,
       "ccmPhoneExtension": ccmPhoneExtension,
       "ccmPhoneExtensionIpAddress": ccmPhoneExtensionIpAddress,
       "ccmPhoneExtensionMultiLines": ccmPhoneExtensionMultiLines,
       "ccmPhoneExtensionInetAddressType": ccmPhoneExtensionInetAddressType,
       "ccmPhoneExtensionInetAddress": ccmPhoneExtensionInetAddress,
       "ccmPhoneFailedTable": ccmPhoneFailedTable,
       "ccmPhoneFailedEntry": ccmPhoneFailedEntry,
       "ccmPhoneFailedIndex": ccmPhoneFailedIndex,
       "ccmPhoneFailedTime": ccmPhoneFailedTime,
       "ccmPhoneFailedName": ccmPhoneFailedName,
       "ccmPhoneFailedInetAddressType": ccmPhoneFailedInetAddressType,
       "ccmPhoneFailedInetAddress": ccmPhoneFailedInetAddress,
       "ccmPhoneFailCauseCode": ccmPhoneFailCauseCode,
       "ccmPhoneFailedMacAddress": ccmPhoneFailedMacAddress,
       "ccmPhoneFailedInetAddressIPv4": ccmPhoneFailedInetAddressIPv4,
       "ccmPhoneFailedInetAddressIPv6": ccmPhoneFailedInetAddressIPv6,
       "ccmPhoneFailedIPv4Attribute": ccmPhoneFailedIPv4Attribute,
       "ccmPhoneFailedIPv6Attribute": ccmPhoneFailedIPv6Attribute,
       "ccmPhoneFailedRegFailReason": ccmPhoneFailedRegFailReason,
       "ccmPhoneStatusUpdateTable": ccmPhoneStatusUpdateTable,
       "ccmPhoneStatusUpdateEntry": ccmPhoneStatusUpdateEntry,
       "ccmPhoneStatusUpdateIndex": ccmPhoneStatusUpdateIndex,
       "ccmPhoneStatusPhoneIndex": ccmPhoneStatusPhoneIndex,
       "ccmPhoneStatusUpdateTime": ccmPhoneStatusUpdateTime,
       "ccmPhoneStatusUpdateType": ccmPhoneStatusUpdateType,
       "ccmPhoneStatusUpdateReason": ccmPhoneStatusUpdateReason,
       "ccmPhoneStatusUnregReason": ccmPhoneStatusUnregReason,
       "ccmPhoneStatusRegFailReason": ccmPhoneStatusRegFailReason,
       "ccmPhoneExtnTable": ccmPhoneExtnTable,
       "ccmPhoneExtnEntry": ccmPhoneExtnEntry,
       "ccmPhoneExtnIndex": ccmPhoneExtnIndex,
       "ccmPhoneExtn": ccmPhoneExtn,
       "ccmPhoneExtnMultiLines": ccmPhoneExtnMultiLines,
       "ccmPhoneExtnInetAddressType": ccmPhoneExtnInetAddressType,
       "ccmPhoneExtnInetAddress": ccmPhoneExtnInetAddress,
       "ccmPhoneExtnStatus": ccmPhoneExtnStatus,
       "ccmGatewayInfo": ccmGatewayInfo,
       "ccmGatewayTable": ccmGatewayTable,
       "ccmGatewayEntry": ccmGatewayEntry,
       "ccmGatewayIndex": ccmGatewayIndex,
       "ccmGatewayName": ccmGatewayName,
       "ccmGatewayType": ccmGatewayType,
       "ccmGatewayDescription": ccmGatewayDescription,
       "ccmGatewayStatus": ccmGatewayStatus,
       "ccmGatewayDevicePoolIndex": ccmGatewayDevicePoolIndex,
       "ccmGatewayInetAddressType": ccmGatewayInetAddressType,
       "ccmGatewayInetAddress": ccmGatewayInetAddress,
       "ccmGatewayProductId": ccmGatewayProductId,
       "ccmGatewayStatusReason": ccmGatewayStatusReason,
       "ccmGatewayTimeLastStatusUpdt": ccmGatewayTimeLastStatusUpdt,
       "ccmGatewayTimeLastRegistered": ccmGatewayTimeLastRegistered,
       "ccmGatewayDChannelStatus": ccmGatewayDChannelStatus,
       "ccmGatewayDChannelNumber": ccmGatewayDChannelNumber,
       "ccmGatewayProductTypeIndex": ccmGatewayProductTypeIndex,
       "ccmGatewayUnregReason": ccmGatewayUnregReason,
       "ccmGatewayRegFailReason": ccmGatewayRegFailReason,
       "ccmGatewayTrunkInfo": ccmGatewayTrunkInfo,
       "ccmGatewayTrunkTable": ccmGatewayTrunkTable,
       "ccmGatewayTrunkEntry": ccmGatewayTrunkEntry,
       "ccmGatewayTrunkIndex": ccmGatewayTrunkIndex,
       "ccmGatewayTrunkType": ccmGatewayTrunkType,
       "ccmGatewayTrunkName": ccmGatewayTrunkName,
       "ccmTrunkGatewayIndex": ccmTrunkGatewayIndex,
       "ccmGatewayTrunkStatus": ccmGatewayTrunkStatus,
       "ccmGlobalInfo": ccmGlobalInfo,
       "ccmActivePhones": ccmActivePhones,
       "ccmInActivePhones": ccmInActivePhones,
       "ccmActiveGateways": ccmActiveGateways,
       "ccmInActiveGateways": ccmInActiveGateways,
       "ccmRegisteredPhones": ccmRegisteredPhones,
       "ccmUnregisteredPhones": ccmUnregisteredPhones,
       "ccmRejectedPhones": ccmRejectedPhones,
       "ccmRegisteredGateways": ccmRegisteredGateways,
       "ccmUnregisteredGateways": ccmUnregisteredGateways,
       "ccmRejectedGateways": ccmRejectedGateways,
       "ccmRegisteredMediaDevices": ccmRegisteredMediaDevices,
       "ccmUnregisteredMediaDevices": ccmUnregisteredMediaDevices,
       "ccmRejectedMediaDevices": ccmRejectedMediaDevices,
       "ccmRegisteredCTIDevices": ccmRegisteredCTIDevices,
       "ccmUnregisteredCTIDevices": ccmUnregisteredCTIDevices,
       "ccmRejectedCTIDevices": ccmRejectedCTIDevices,
       "ccmRegisteredVoiceMailDevices": ccmRegisteredVoiceMailDevices,
       "ccmUnregisteredVoiceMailDevices": ccmUnregisteredVoiceMailDevices,
       "ccmRejectedVoiceMailDevices": ccmRejectedVoiceMailDevices,
       "ccmCallManagerStartTime": ccmCallManagerStartTime,
       "ccmPhoneTableStateId": ccmPhoneTableStateId,
       "ccmPhoneExtensionTableStateId": ccmPhoneExtensionTableStateId,
       "ccmPhoneStatusUpdateTableStateId": ccmPhoneStatusUpdateTableStateId,
       "ccmGatewayTableStateId": ccmGatewayTableStateId,
       "ccmCTIDeviceTableStateId": ccmCTIDeviceTableStateId,
       "ccmCTIDeviceDirNumTableStateId": ccmCTIDeviceDirNumTableStateId,
       "ccmPhStatUpdtTblLastAddedIndex": ccmPhStatUpdtTblLastAddedIndex,
       "ccmPhFailedTblLastAddedIndex": ccmPhFailedTblLastAddedIndex,
       "ccmSystemVersion": ccmSystemVersion,
       "ccmInstallationId": ccmInstallationId,
       "ccmPartiallyRegisteredPhones": ccmPartiallyRegisteredPhones,
       "ccmH323TableEntries": ccmH323TableEntries,
       "ccmSIPTableEntries": ccmSIPTableEntries,
       "ccmMediaDeviceInfo": ccmMediaDeviceInfo,
       "ccmMediaDeviceTable": ccmMediaDeviceTable,
       "ccmMediaDeviceEntry": ccmMediaDeviceEntry,
       "ccmMediaDeviceIndex": ccmMediaDeviceIndex,
       "ccmMediaDeviceName": ccmMediaDeviceName,
       "ccmMediaDeviceType": ccmMediaDeviceType,
       "ccmMediaDeviceDescription": ccmMediaDeviceDescription,
       "ccmMediaDeviceStatus": ccmMediaDeviceStatus,
       "ccmMediaDeviceDevicePoolIndex": ccmMediaDeviceDevicePoolIndex,
       "ccmMediaDeviceInetAddressType": ccmMediaDeviceInetAddressType,
       "ccmMediaDeviceInetAddress": ccmMediaDeviceInetAddress,
       "ccmMediaDeviceStatusReason": ccmMediaDeviceStatusReason,
       "ccmMediaDeviceTimeLastStatusUpdt": ccmMediaDeviceTimeLastStatusUpdt,
       "ccmMediaDeviceTimeLastRegistered": ccmMediaDeviceTimeLastRegistered,
       "ccmMediaDeviceProductTypeIndex": ccmMediaDeviceProductTypeIndex,
       "ccmMediaDeviceInetAddressIPv4": ccmMediaDeviceInetAddressIPv4,
       "ccmMediaDeviceInetAddressIPv6": ccmMediaDeviceInetAddressIPv6,
       "ccmMediaDeviceUnregReason": ccmMediaDeviceUnregReason,
       "ccmMediaDeviceRegFailReason": ccmMediaDeviceRegFailReason,
       "ccmGatekeeperInfo": ccmGatekeeperInfo,
       "ccmGatekeeperTable": ccmGatekeeperTable,
       "ccmGatekeeperEntry": ccmGatekeeperEntry,
       "ccmGatekeeperIndex": ccmGatekeeperIndex,
       "ccmGatekeeperName": ccmGatekeeperName,
       "ccmGatekeeperType": ccmGatekeeperType,
       "ccmGatekeeperDescription": ccmGatekeeperDescription,
       "ccmGatekeeperStatus": ccmGatekeeperStatus,
       "ccmGatekeeperDevicePoolIndex": ccmGatekeeperDevicePoolIndex,
       "ccmGatekeeperInetAddressType": ccmGatekeeperInetAddressType,
       "ccmGatekeeperInetAddress": ccmGatekeeperInetAddress,
       "ccmCTIDeviceInfo": ccmCTIDeviceInfo,
       "ccmCTIDeviceTable": ccmCTIDeviceTable,
       "ccmCTIDeviceEntry": ccmCTIDeviceEntry,
       "ccmCTIDeviceIndex": ccmCTIDeviceIndex,
       "ccmCTIDeviceName": ccmCTIDeviceName,
       "ccmCTIDeviceType": ccmCTIDeviceType,
       "ccmCTIDeviceDescription": ccmCTIDeviceDescription,
       "ccmCTIDeviceStatus": ccmCTIDeviceStatus,
       "ccmCTIDevicePoolIndex": ccmCTIDevicePoolIndex,
       "ccmCTIDeviceInetAddressType": ccmCTIDeviceInetAddressType,
       "ccmCTIDeviceInetAddress": ccmCTIDeviceInetAddress,
       "ccmCTIDeviceAppInfo": ccmCTIDeviceAppInfo,
       "ccmCTIDeviceStatusReason": ccmCTIDeviceStatusReason,
       "ccmCTIDeviceTimeLastStatusUpdt": ccmCTIDeviceTimeLastStatusUpdt,
       "ccmCTIDeviceTimeLastRegistered": ccmCTIDeviceTimeLastRegistered,
       "ccmCTIDeviceProductTypeIndex": ccmCTIDeviceProductTypeIndex,
       "ccmCTIDeviceInetAddressIPv4": ccmCTIDeviceInetAddressIPv4,
       "ccmCTIDeviceInetAddressIPv6": ccmCTIDeviceInetAddressIPv6,
       "ccmCTIDeviceUnregReason": ccmCTIDeviceUnregReason,
       "ccmCTIDeviceRegFailReason": ccmCTIDeviceRegFailReason,
       "ccmCTIDeviceDirNumTable": ccmCTIDeviceDirNumTable,
       "ccmCTIDeviceDirNumEntry": ccmCTIDeviceDirNumEntry,
       "ccmCTIDeviceDirNumIndex": ccmCTIDeviceDirNumIndex,
       "ccmCTIDeviceDirNum": ccmCTIDeviceDirNum,
       "ccmAlarmConfigInfo": ccmAlarmConfigInfo,
       "ccmCallManagerAlarmEnable": ccmCallManagerAlarmEnable,
       "ccmPhoneFailedAlarmInterval": ccmPhoneFailedAlarmInterval,
       "ccmPhoneFailedStorePeriod": ccmPhoneFailedStorePeriod,
       "ccmPhoneStatusUpdateAlarmInterv": ccmPhoneStatusUpdateAlarmInterv,
       "ccmPhoneStatusUpdateStorePeriod": ccmPhoneStatusUpdateStorePeriod,
       "ccmGatewayAlarmEnable": ccmGatewayAlarmEnable,
       "ccmMaliciousCallAlarmEnable": ccmMaliciousCallAlarmEnable,
       "ccmNotificationsInfo": ccmNotificationsInfo,
       "ccmAlarmSeverity": ccmAlarmSeverity,
       "ccmFailCauseCode": ccmFailCauseCode,
       "ccmPhoneFailures": ccmPhoneFailures,
       "ccmPhoneUpdates": ccmPhoneUpdates,
       "ccmGatewayFailCauseCode": ccmGatewayFailCauseCode,
       "ccmMediaResourceType": ccmMediaResourceType,
       "ccmMediaResourceListName": ccmMediaResourceListName,
       "ccmRouteListName": ccmRouteListName,
       "ccmGatewayPhysIfIndex": ccmGatewayPhysIfIndex,
       "ccmGatewayPhysIfL2Status": ccmGatewayPhysIfL2Status,
       "ccmMaliCallCalledPartyName": ccmMaliCallCalledPartyName,
       "ccmMaliCallCalledPartyNumber": ccmMaliCallCalledPartyNumber,
       "ccmMaliCallCalledDeviceName": ccmMaliCallCalledDeviceName,
       "ccmMaliCallCallingPartyName": ccmMaliCallCallingPartyName,
       "ccmMaliCallCallingPartyNumber": ccmMaliCallCallingPartyNumber,
       "ccmMaliCallCallingDeviceName": ccmMaliCallCallingDeviceName,
       "ccmMaliCallTime": ccmMaliCallTime,
       "ccmQualityRprtSourceDevName": ccmQualityRprtSourceDevName,
       "ccmQualityRprtClusterId": ccmQualityRprtClusterId,
       "ccmQualityRprtCategory": ccmQualityRprtCategory,
       "ccmQualityRprtReasonCode": ccmQualityRprtReasonCode,
       "ccmQualityRprtTime": ccmQualityRprtTime,
       "ccmTLSDevName": ccmTLSDevName,
       "ccmTLSDevInetAddressType": ccmTLSDevInetAddressType,
       "ccmTLSDevInetAddress": ccmTLSDevInetAddress,
       "ccmTLSConnFailTime": ccmTLSConnFailTime,
       "ccmTLSConnectionFailReasonCode": ccmTLSConnectionFailReasonCode,
       "ccmGatewayRegFailCauseCode": ccmGatewayRegFailCauseCode,
       "ccmH323DeviceInfo": ccmH323DeviceInfo,
       "ccmH323DeviceTable": ccmH323DeviceTable,
       "ccmH323DeviceEntry": ccmH323DeviceEntry,
       "ccmH323DevIndex": ccmH323DevIndex,
       "ccmH323DevName": ccmH323DevName,
       "ccmH323DevProductId": ccmH323DevProductId,
       "ccmH323DevDescription": ccmH323DevDescription,
       "ccmH323DevInetAddressType": ccmH323DevInetAddressType,
       "ccmH323DevInetAddress": ccmH323DevInetAddress,
       "ccmH323DevCnfgGKInetAddressType": ccmH323DevCnfgGKInetAddressType,
       "ccmH323DevCnfgGKInetAddress": ccmH323DevCnfgGKInetAddress,
       "ccmH323DevAltGK1InetAddressType": ccmH323DevAltGK1InetAddressType,
       "ccmH323DevAltGK1InetAddress": ccmH323DevAltGK1InetAddress,
       "ccmH323DevAltGK2InetAddressType": ccmH323DevAltGK2InetAddressType,
       "ccmH323DevAltGK2InetAddress": ccmH323DevAltGK2InetAddress,
       "ccmH323DevAltGK3InetAddressType": ccmH323DevAltGK3InetAddressType,
       "ccmH323DevAltGK3InetAddress": ccmH323DevAltGK3InetAddress,
       "ccmH323DevAltGK4InetAddressType": ccmH323DevAltGK4InetAddressType,
       "ccmH323DevAltGK4InetAddress": ccmH323DevAltGK4InetAddress,
       "ccmH323DevAltGK5InetAddressType": ccmH323DevAltGK5InetAddressType,
       "ccmH323DevAltGK5InetAddress": ccmH323DevAltGK5InetAddress,
       "ccmH323DevActGKInetAddressType": ccmH323DevActGKInetAddressType,
       "ccmH323DevActGKInetAddress": ccmH323DevActGKInetAddress,
       "ccmH323DevStatus": ccmH323DevStatus,
       "ccmH323DevStatusReason": ccmH323DevStatusReason,
       "ccmH323DevTimeLastStatusUpdt": ccmH323DevTimeLastStatusUpdt,
       "ccmH323DevTimeLastRegistered": ccmH323DevTimeLastRegistered,
       "ccmH323DevRmtCM1InetAddressType": ccmH323DevRmtCM1InetAddressType,
       "ccmH323DevRmtCM1InetAddress": ccmH323DevRmtCM1InetAddress,
       "ccmH323DevRmtCM2InetAddressType": ccmH323DevRmtCM2InetAddressType,
       "ccmH323DevRmtCM2InetAddress": ccmH323DevRmtCM2InetAddress,
       "ccmH323DevRmtCM3InetAddressType": ccmH323DevRmtCM3InetAddressType,
       "ccmH323DevRmtCM3InetAddress": ccmH323DevRmtCM3InetAddress,
       "ccmH323DevProductTypeIndex": ccmH323DevProductTypeIndex,
       "ccmH323DevUnregReason": ccmH323DevUnregReason,
       "ccmH323DevRegFailReason": ccmH323DevRegFailReason,
       "ccmVoiceMailDeviceInfo": ccmVoiceMailDeviceInfo,
       "ccmVoiceMailDeviceTable": ccmVoiceMailDeviceTable,
       "ccmVoiceMailDeviceEntry": ccmVoiceMailDeviceEntry,
       "ccmVMailDevIndex": ccmVMailDevIndex,
       "ccmVMailDevName": ccmVMailDevName,
       "ccmVMailDevProductId": ccmVMailDevProductId,
       "ccmVMailDevDescription": ccmVMailDevDescription,
       "ccmVMailDevStatus": ccmVMailDevStatus,
       "ccmVMailDevInetAddressType": ccmVMailDevInetAddressType,
       "ccmVMailDevInetAddress": ccmVMailDevInetAddress,
       "ccmVMailDevStatusReason": ccmVMailDevStatusReason,
       "ccmVMailDevTimeLastStatusUpdt": ccmVMailDevTimeLastStatusUpdt,
       "ccmVMailDevTimeLastRegistered": ccmVMailDevTimeLastRegistered,
       "ccmVMailDevProductTypeIndex": ccmVMailDevProductTypeIndex,
       "ccmVMailDevUnregReason": ccmVMailDevUnregReason,
       "ccmVMailDevRegFailReason": ccmVMailDevRegFailReason,
       "ccmVoiceMailDeviceDirNumTable": ccmVoiceMailDeviceDirNumTable,
       "ccmVoiceMailDeviceDirNumEntry": ccmVoiceMailDeviceDirNumEntry,
       "ccmVMailDevDirNumIndex": ccmVMailDevDirNumIndex,
       "ccmVMailDevDirNum": ccmVMailDevDirNum,
       "ccmQualityReportAlarmConfigInfo": ccmQualityReportAlarmConfigInfo,
       "ccmQualityReportAlarmEnable": ccmQualityReportAlarmEnable,
       "ccmSIPDeviceInfo": ccmSIPDeviceInfo,
       "ccmSIPDeviceTable": ccmSIPDeviceTable,
       "ccmSIPDeviceEntry": ccmSIPDeviceEntry,
       "ccmSIPDevIndex": ccmSIPDevIndex,
       "ccmSIPDevName": ccmSIPDevName,
       "ccmSIPDevProductTypeIndex": ccmSIPDevProductTypeIndex,
       "ccmSIPDevDescription": ccmSIPDevDescription,
       "ccmSIPDevInetAddressType": ccmSIPDevInetAddressType,
       "ccmSIPDevInetAddress": ccmSIPDevInetAddress,
       "ccmSIPInTransportProtocolType": ccmSIPInTransportProtocolType,
       "ccmSIPInPortNumber": ccmSIPInPortNumber,
       "ccmSIPOutTransportProtocolType": ccmSIPOutTransportProtocolType,
       "ccmSIPOutPortNumber": ccmSIPOutPortNumber,
       "ccmSIPDevInetAddressIPv4": ccmSIPDevInetAddressIPv4,
       "ccmSIPDevInetAddressIPv6": ccmSIPDevInetAddressIPv6,
       "ccmMIBNotificationPrefix": ccmMIBNotificationPrefix,
       "ccmMIBNotifications": ccmMIBNotifications,
       "ccmCallManagerFailed": ccmCallManagerFailed,
       "ccmPhoneFailed": ccmPhoneFailed,
       "ccmPhoneStatusUpdate": ccmPhoneStatusUpdate,
       "ccmGatewayFailed": ccmGatewayFailed,
       "ccmMediaResourceListExhausted": ccmMediaResourceListExhausted,
       "ccmRouteListExhausted": ccmRouteListExhausted,
       "ccmGatewayLayer2Change": ccmGatewayLayer2Change,
       "ccmMaliciousCall": ccmMaliciousCall,
       "ccmQualityReport": ccmQualityReport,
       "ccmTLSConnectionFailure": ccmTLSConnectionFailure,
       "ccmGatewayFailedReason": ccmGatewayFailedReason,
       "ciscoCcmMIBConformance": ciscoCcmMIBConformance,
       "ciscoCcmMIBCompliances": ciscoCcmMIBCompliances,
       "ciscoCcmMIBCompliance": ciscoCcmMIBCompliance,
       "ciscoCcmMIBComplianceRev1": ciscoCcmMIBComplianceRev1,
       "ciscoCcmMIBComplianceRev2": ciscoCcmMIBComplianceRev2,
       "ciscoCcmMIBComplianceRev3": ciscoCcmMIBComplianceRev3,
       "ciscoCcmMIBComplianceRev4": ciscoCcmMIBComplianceRev4,
       "ciscoCcmMIBComplianceRev5": ciscoCcmMIBComplianceRev5,
       "ciscoCcmMIBComplianceRev6": ciscoCcmMIBComplianceRev6,
       "ciscoCcmMIBComplianceRev7": ciscoCcmMIBComplianceRev7,
       "ciscoCcmMIBGroups": ciscoCcmMIBGroups,
       "ccmInfoGroup": ccmInfoGroup,
       "ccmPhoneInfoGroup": ccmPhoneInfoGroup,
       "ccmGatewayInfoGroup": ccmGatewayInfoGroup,
       "ccmInfoGroupRev1": ccmInfoGroupRev1,
       "ccmPhoneInfoGroupRev1": ccmPhoneInfoGroupRev1,
       "ccmGatewayInfoGroupRev1": ccmGatewayInfoGroupRev1,
       "ccmMediaDeviceInfoGroup": ccmMediaDeviceInfoGroup,
       "ccmGatekeeperInfoGroup": ccmGatekeeperInfoGroup,
       "ccmCTIDeviceInfoGroup": ccmCTIDeviceInfoGroup,
       "ccmNotificationsInfoGroup": ccmNotificationsInfoGroup,
       "ccmNotificationsGroup": ccmNotificationsGroup,
       "ccmInfoGroupRev2": ccmInfoGroupRev2,
       "ccmPhoneInfoGroupRev2": ccmPhoneInfoGroupRev2,
       "ccmGatewayInfoGroupRev2": ccmGatewayInfoGroupRev2,
       "ccmMediaDeviceInfoGroupRev1": ccmMediaDeviceInfoGroupRev1,
       "ccmCTIDeviceInfoGroupRev1": ccmCTIDeviceInfoGroupRev1,
       "ccmH323DeviceInfoGroup": ccmH323DeviceInfoGroup,
       "ccmVoiceMailDeviceInfoGroup": ccmVoiceMailDeviceInfoGroup,
       "ccmNotificationsInfoGroupRev1": ccmNotificationsInfoGroupRev1,
       "ccmInfoGroupRev3": ccmInfoGroupRev3,
       "ccmNotificationsInfoGroupRev2": ccmNotificationsInfoGroupRev2,
       "ccmNotificationsGroupRev1": ccmNotificationsGroupRev1,
       "ccmSIPDeviceInfoGroup": ccmSIPDeviceInfoGroup,
       "ccmPhoneInfoGroupRev3": ccmPhoneInfoGroupRev3,
       "ccmGatewayInfoGroupRev3": ccmGatewayInfoGroupRev3,
       "ccmMediaDeviceInfoGroupRev2": ccmMediaDeviceInfoGroupRev2,
       "ccmCTIDeviceInfoGroupRev2": ccmCTIDeviceInfoGroupRev2,
       "ccmH323DeviceInfoGroupRev1": ccmH323DeviceInfoGroupRev1,
       "ccmVoiceMailDeviceInfoGroupRev1": ccmVoiceMailDeviceInfoGroupRev1,
       "ccmPhoneInfoGroupRev4": ccmPhoneInfoGroupRev4,
       "ccmSIPDeviceInfoGroupRev1": ccmSIPDeviceInfoGroupRev1,
       "ccmNotificationsInfoGroupRev3": ccmNotificationsInfoGroupRev3,
       "ccmNotificationsGroupRev2": ccmNotificationsGroupRev2,
       "ccmInfoGroupRev4": ccmInfoGroupRev4,
       "ccmPhoneInfoGroupRev5": ccmPhoneInfoGroupRev5,
       "ccmMediaDeviceInfoGroupRev3": ccmMediaDeviceInfoGroupRev3,
       "ccmSIPDeviceInfoGroupRev2": ccmSIPDeviceInfoGroupRev2,
       "ccmNotificationsInfoGroupRev4": ccmNotificationsInfoGroupRev4,
       "ccmH323DeviceInfoGroupRev2": ccmH323DeviceInfoGroupRev2,
       "ccmCTIDeviceInfoGroupRev3": ccmCTIDeviceInfoGroupRev3,
       "ccmPhoneInfoGroupRev6": ccmPhoneInfoGroupRev6,
       "ccmNotificationsInfoGroupRev5": ccmNotificationsInfoGroupRev5,
       "ccmGatewayInfoGroupRev4": ccmGatewayInfoGroupRev4,
       "ccmMediaDeviceInfoGroupRev4": ccmMediaDeviceInfoGroupRev4,
       "ccmCTIDeviceInfoGroupRev4": ccmCTIDeviceInfoGroupRev4,
       "ccmH323DeviceInfoGroupRev3": ccmH323DeviceInfoGroupRev3,
       "ccmVoiceMailDeviceInfoGroupRev2": ccmVoiceMailDeviceInfoGroupRev2,
       "ccmNotificationsGroupRev3": ccmNotificationsGroupRev3}
)
