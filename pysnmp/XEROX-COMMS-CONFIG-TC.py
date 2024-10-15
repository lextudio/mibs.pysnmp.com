# SNMP MIB module (XEROX-COMMS-CONFIG-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-COMMS-CONFIG-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:14 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmCommsConfigTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmSnmpNetbiosAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class XcmSnmpIPHostnameAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )



class XcmCommsConfigGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmCommsDirRecordType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              100,
              101,
              200,
              201,
              300,
              301,
              400,
              401,
              500,
              501,
              600,
              601,
              700,
              701,
              800,
              801,
              900,
              901)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("recordAccount", 200),
          ("recordAccountGroup", 201),
          ("recordButtonDial", 800),
          ("recordButtonDialGroup", 801),
          ("recordDepartment", 300),
          ("recordDepartmentGroup", 301),
          ("recordMailbox", 400),
          ("recordMailboxGroup", 401),
          ("recordRepository", 900),
          ("recordRepositoryGroup", 901),
          ("recordResource", 500),
          ("recordResourceGroup", 501),
          ("recordService", 100),
          ("recordServiceGroup", 101),
          ("recordSpeedDial", 600),
          ("recordSpeedDialGroup", 601),
          ("recordUser", 700),
          ("recordUserGroup", 701),
          ("top", 10),
          ("unknown", 2))
    )



class XcmCommsDirAttributeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              13,
              20,
              21,
              22,
              23,
              30,
              31,
              32,
              33,
              100,
              101,
              102,
              103,
              110,
              111,
              112,
              120,
              121,
              122,
              123,
              124,
              125,
              130,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              160,
              161,
              162,
              163,
              170,
              171,
              172,
              173,
              180,
              181,
              182,
              183,
              200,
              201,
              202,
              203,
              210,
              211,
              212,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              260,
              261,
              300,
              301,
              350,
              351,
              352,
              360,
              361,
              400,
              401,
              450,
              451,
              452,
              460,
              461,
              500,
              501,
              502,
              503,
              510,
              511,
              512,
              540,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              550,
              551,
              552,
              553,
              554,
              555,
              556,
              557,
              560,
              561,
              600,
              601,
              650,
              651,
              652,
              660,
              661,
              700,
              701,
              702,
              703,
              710,
              711,
              712,
              740,
              741,
              742,
              743,
              744,
              745,
              746,
              747,
              750,
              751,
              752,
              753,
              754,
              755,
              756,
              757,
              760,
              761,
              800,
              801,
              850,
              851,
              852,
              860,
              861,
              900,
              901,
              902,
              903,
              911,
              912,
              950,
              951,
              952,
              953,
              954,
              955,
              956,
              957,
              960,
              961,
              1000,
              1001,
              1002,
              1003,
              1004,
              1010,
              1011,
              1030,
              1510,
              1511,
              1512,
              1513,
              1514,
              1515,
              1520,
              1521,
              1522,
              1523,
              1530,
              1531,
              1532,
              1533,
              1534,
              1535,
              1536,
              1537,
              1540,
              1541,
              1542,
              1543,
              1544,
              1550,
              1551,
              1552,
              1553,
              1554,
              1560,
              1561,
              1562,
              1570,
              1571,
              1572,
              1580,
              1581,
              1582,
              1583,
              1584,
              1585,
              1590,
              1591,
              1592,
              1593,
              1600,
              1601,
              1602,
              1603,
              1604,
              1605,
              1606,
              1610,
              1611,
              1620,
              1621,
              1622,
              1623,
              1624,
              1625,
              1626,
              1627,
              1628,
              1630,
              1631,
              2000,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2010,
              2011,
              2012,
              2013,
              2014,
              2015,
              2020,
              2021,
              2022,
              2023,
              2030,
              2031,
              2032,
              2033,
              2040,
              3000)
        )
    )
    namedValues = NamedValues(
        *(("accountAlias", 255),
          ("accountCode", 252),
          ("accountDescription", 260),
          ("accountFullName", 251),
          ("accountGroupIndex", 201),
          ("accountIndex", 200),
          ("accountLifetimeErrorCount", 244),
          ("accountLifetimeErrorLimit", 245),
          ("accountLifetimeLimit", 243),
          ("accountLifetimeUnit", 242),
          ("accountLifetimeUnitClass", 241),
          ("accountLifetimeUsage", 240),
          ("accountLifetimeWarningCount", 246),
          ("accountLifetimeWarningLimit", 247),
          ("accountLocation", 261),
          ("accountLoginDate", 256),
          ("accountLogoutDate", 257),
          ("accountName", 250),
          ("accountPasscode", 254),
          ("accountPassword", 253),
          ("accountPosixRights", 202),
          ("accountPosixVerbs", 203),
          ("accountRole", 210),
          ("accountScope", 212),
          ("accountSkill", 211),
          ("buttonDialCode", 852),
          ("buttonDialDescription", 860),
          ("buttonDialFullName", 851),
          ("buttonDialGroupIndex", 801),
          ("buttonDialIndex", 800),
          ("buttonDialLocation", 861),
          ("buttonDialName", 850),
          ("childGroupRecordIndex", 33),
          ("childGroupRecordType", 32),
          ("childRecordIndex", 31),
          ("childRecordType", 30),
          ("departmentCode", 352),
          ("departmentDescription", 360),
          ("departmentFullName", 351),
          ("departmentGroupIndex", 301),
          ("departmentIndex", 300),
          ("departmentLocation", 361),
          ("departmentName", 350),
          ("mailboxCode", 452),
          ("mailboxDescription", 460),
          ("mailboxFullName", 451),
          ("mailboxGroupIndex", 401),
          ("mailboxIndex", 400),
          ("mailboxLocation", 461),
          ("mailboxName", 450),
          ("other", 1),
          ("parentGroupRecordIndex", 13),
          ("parentGroupRecordType", 12),
          ("parentRecordIndex", 11),
          ("parentRecordType", 10),
          ("peerGroupRecordIndex", 23),
          ("peerGroupRecordType", 22),
          ("peerRecordIndex", 21),
          ("peerRecordType", 20),
          ("protocolAutoSwitch", 1583),
          ("protocolBidirectional", 1534),
          ("protocolBinaryPS", 1584),
          ("protocolCableAdaptive", 1515),
          ("protocolCableType", 1514),
          ("protocolConnectorAdaptive", 1511),
          ("protocolConnectorType", 1510),
          ("protocolDefaultPDL", 1585),
          ("protocolDeviceIndex", 1010),
          ("protocolDirection", 1535),
          ("protocolFlowControl", 1536),
          ("protocolFrameAdaptive", 1521),
          ("protocolFrameType", 1520),
          ("protocolInputFlowWindow", 1541),
          ("protocolInputPrime", 1542),
          ("protocolInputTimeout", 1540),
          ("protocolInterfaceIndex", 1011),
          ("protocolJobTimeout", 1582),
          ("protocolLayer", 1004),
          ("protocolListen", 1570),
          ("protocolListenInterval", 1572),
          ("protocolListenSocket", 1571),
          ("protocolMaxConnections", 1537),
          ("protocolMaxFrameSize", 1523),
          ("protocolMaxInputChars", 1544),
          ("protocolMaxOutputChars", 1554),
          ("protocolMaxRetries", 1560),
          ("protocolMaxSpeed", 1533),
          ("protocolMaxSpool", 1581),
          ("protocolMinFrameSize", 1522),
          ("protocolMinInputChars", 1543),
          ("protocolMinOutputChars", 1553),
          ("protocolMinSpeed", 1532),
          ("protocolOutputFlowWindow", 1551),
          ("protocolOutputPrime", 1552),
          ("protocolOutputTimeout", 1550),
          ("protocolPollInterval", 1562),
          ("protocolPriority", 1030),
          ("protocolPurpose", 1001),
          ("protocolReceiveAutoReduce", 1626),
          ("protocolReceiveCollate", 1628),
          ("protocolReceiveCoverSheet", 1621),
          ("protocolReceiveEndTime", 1593),
          ("protocolReceiveErrorCorrection", 1631),
          ("protocolReceiveFooter", 1622),
          ("protocolReceiveLineNumber", 1620),
          ("protocolReceiveManual", 1624),
          ("protocolReceiveOverflow", 1627),
          ("protocolReceiveResolution", 1630),
          ("protocolReceiveSecurity", 1625),
          ("protocolReceiveStartTime", 1592),
          ("protocolReceiveToMemory", 1623),
          ("protocolRetryInterval", 1561),
          ("protocolRole", 1002),
          ("protocolSendConfirmPrint", 1603),
          ("protocolSendCoverSheet", 1601),
          ("protocolSendEndTime", 1591),
          ("protocolSendErrorCorrection", 1611),
          ("protocolSendHeader", 1602),
          ("protocolSendLineNumber", 1600),
          ("protocolSendManual", 1604),
          ("protocolSendResolution", 1610),
          ("protocolSendSecurity", 1605),
          ("protocolSendStartTime", 1590),
          ("protocolSendStoreTime", 1606),
          ("protocolSignalAdaptive", 1513),
          ("protocolSignalType", 1512),
          ("protocolSpeed", 1530),
          ("protocolSpeedAdaptive", 1531),
          ("protocolSpool", 1580),
          ("protocolSuite", 1003),
          ("protocolType", 1000),
          ("protocolTypedAcceptAddress", 2020),
          ("protocolTypedAcceptSubnet", 2021),
          ("protocolTypedAddress", 2010),
          ("protocolTypedBroadcastAddress", 2011),
          ("protocolTypedConfirmAddress", 2014),
          ("protocolTypedConfirmURL", 2015),
          ("protocolTypedDescription", 2006),
          ("protocolTypedDeviceName", 2040),
          ("protocolTypedFullName", 2001),
          ("protocolTypedHostName", 2003),
          ("protocolTypedListenAddress", 2012),
          ("protocolTypedLocation", 2007),
          ("protocolTypedMulticastAddress", 2013),
          ("protocolTypedName", 2000),
          ("protocolTypedPassword", 2002),
          ("protocolTypedQueueName", 2004),
          ("protocolTypedRejectAddress", 2022),
          ("protocolTypedRejectSubnet", 2023),
          ("protocolTypedServerName", 2005),
          ("protocolTypedURC", 2030),
          ("protocolTypedURI", 2031),
          ("protocolTypedURL", 2032),
          ("protocolTypedURN", 2033),
          ("repositoryAlias", 955),
          ("repositoryCode", 952),
          ("repositoryDescription", 960),
          ("repositoryFullName", 951),
          ("repositoryGroupIndex", 901),
          ("repositoryIndex", 900),
          ("repositoryLocation", 961),
          ("repositoryLoginDate", 956),
          ("repositoryLogoutDate", 957),
          ("repositoryName", 950),
          ("repositoryPasscode", 954),
          ("repositoryPassword", 953),
          ("repositoryPosixRights", 902),
          ("repositoryPosixVerbs", 903),
          ("repositoryScope", 912),
          ("repositorySkill", 911),
          ("reserved", 3000),
          ("resourceAlias", 555),
          ("resourceCode", 552),
          ("resourceDescription", 560),
          ("resourceFullName", 551),
          ("resourceGroupIndex", 501),
          ("resourceIndex", 500),
          ("resourceLifetimeErrorCount", 544),
          ("resourceLifetimeErrorLimit", 545),
          ("resourceLifetimeLimit", 543),
          ("resourceLifetimeUnit", 542),
          ("resourceLifetimeUnitClass", 541),
          ("resourceLifetimeUsage", 540),
          ("resourceLifetimeWarningCount", 546),
          ("resourceLifetimeWarningLimit", 547),
          ("resourceLocation", 561),
          ("resourceLoginDate", 556),
          ("resourceLogoutDate", 557),
          ("resourceName", 550),
          ("resourcePasscode", 554),
          ("resourcePassword", 553),
          ("resourcePosixRights", 502),
          ("resourcePosixVerbs", 503),
          ("resourceScope", 512),
          ("resourceSkill", 511),
          ("resourceType", 510),
          ("serviceAlias", 155),
          ("serviceCharsetConfigured", 172),
          ("serviceCharsetSupported", 173),
          ("serviceCode", 152),
          ("serviceContext", 181),
          ("serviceDescription", 160),
          ("serviceExternalDeviceIndex", 122),
          ("serviceFullName", 151),
          ("serviceGroupIndex", 101),
          ("serviceIndex", 100),
          ("serviceLanguageConfigured", 170),
          ("serviceLanguageSupported", 171),
          ("serviceLifetimeErrorCount", 144),
          ("serviceLifetimeErrorLimit", 145),
          ("serviceLifetimeLimit", 143),
          ("serviceLifetimeUnit", 142),
          ("serviceLifetimeUnitClass", 141),
          ("serviceLifetimeUsage", 140),
          ("serviceLifetimeWarningCount", 146),
          ("serviceLifetimeWarningLimit", 147),
          ("serviceLocation", 161),
          ("serviceLogicalDeviceIndex", 121),
          ("serviceLoginDate", 156),
          ("serviceLogoutDate", 157),
          ("serviceName", 150),
          ("servicePasscode", 154),
          ("servicePassword", 153),
          ("servicePath", 183),
          ("servicePhysicalDeviceIndex", 120),
          ("servicePosixRights", 102),
          ("servicePosixVerbs", 103),
          ("servicePriority", 130),
          ("serviceProductID", 163),
          ("serviceSWInstalledIndex", 124),
          ("serviceSWRunIndex", 123),
          ("serviceScope", 112),
          ("serviceSkill", 111),
          ("serviceStorageIndex", 125),
          ("serviceTree", 180),
          ("serviceType", 110),
          ("serviceTypeOID", 162),
          ("serviceVolume", 182),
          ("speedDialCode", 652),
          ("speedDialDescription", 660),
          ("speedDialFullName", 651),
          ("speedDialGroupIndex", 601),
          ("speedDialIndex", 600),
          ("speedDialLocation", 661),
          ("speedDialName", 650),
          ("unknown", 2),
          ("userAlias", 755),
          ("userCode", 752),
          ("userDescription", 760),
          ("userFullName", 751),
          ("userGroupIndex", 701),
          ("userIndex", 700),
          ("userLifetimeErrorCount", 744),
          ("userLifetimeErrorLimit", 745),
          ("userLifetimeLimit", 743),
          ("userLifetimeUnit", 742),
          ("userLifetimeUnitClass", 741),
          ("userLifetimeUsage", 740),
          ("userLifetimeWarningCount", 746),
          ("userLifetimeWarningLimit", 747),
          ("userLocation", 761),
          ("userLoginDate", 756),
          ("userLogoutDate", 757),
          ("userName", 750),
          ("userPasscode", 754),
          ("userPassword", 753),
          ("userPosixRights", 702),
          ("userPosixVerbs", 703),
          ("userRole", 710),
          ("userScope", 712),
          ("userSkill", 711))
    )



class XcmCommsLDAPAttributeType(Integer32, TextualConvention):
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
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              121,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              138,
              143,
              145,
              146,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              300)
        )
    )
    namedValues = NamedValues(
        *(("associatedDomain", 127),
          ("associatedName", 128),
          ("audio", 145),
          ("authorityRevocationList", 38),
          ("buildingName", 138),
          ("businessCategory", 15),
          ("caCertificate", 37),
          ("carLicense", 201),
          ("certificateRevocationList", 39),
          ("city", 7),
          ("commonName", 3),
          ("country", 6),
          ("crossCertificatePair", 40),
          ("deltaRevocationList", 53),
          ("departmentNumber", 202),
          ("description", 13),
          ("destinationIndicator", 27),
          ("displayName", 203),
          ("distinguishedName", 49),
          ("dmdName", 54),
          ("dnQualifier", 46),
          ("documentAuthor", 114),
          ("documentIdentifier", 111),
          ("documentLocation", 115),
          ("documentPublisher", 146),
          ("documentTitle", 112),
          ("documentVersion", 113),
          ("domainComponent", 121),
          ("employeeNumber", 204),
          ("employeeType", 205),
          ("enhancedSearchGuide", 47),
          ("favoriteDrink", 105),
          ("faxNumber", 23),
          ("friendlyCountry", 133),
          ("generationQualifier", 44),
          ("givenName", 42),
          ("homePhone", 116),
          ("homePostalAddress", 129),
          ("host", 109),
          ("houseIdentifier", 51),
          ("info", 104),
          ("initials", 43),
          ("isdnNumber", 25),
          ("jpegPhoto", 206),
          ("labeledURI", 300),
          ("mail", 103),
          ("manager", 110),
          ("member", 31),
          ("mobile", 131),
          ("name", 41),
          ("office", 19),
          ("org", 10),
          ("orgStatus", 135),
          ("orgUnit", 11),
          ("other", 1),
          ("otherMailbox", 118),
          ("owner", 32),
          ("pager", 132),
          ("personalSignature", 143),
          ("personalTitle", 130),
          ("photo", 107),
          ("postOfficeBox", 18),
          ("postalAddress", 16),
          ("postalCode", 17),
          ("preferredDeliveryMethod", 28),
          ("preferredLanguage", 207),
          ("presentationAddress", 29),
          ("protocolInformation", 48),
          ("registeredAddress", 26),
          ("role", 33),
          ("roomNumber", 106),
          ("searchGuide", 14),
          ("secretary", 117),
          ("seeAlso", 34),
          ("serialNumber", 5),
          ("state", 8),
          ("streetAddress", 9),
          ("supportedAlgorithms", 52),
          ("supportedContext", 30),
          ("surname", 4),
          ("telephoneNumber", 20),
          ("teletexTerminal", 22),
          ("telexNumber", 21),
          ("textEncodedORAddress", 102),
          ("title", 12),
          ("uid", 101),
          ("uniqueIdentifier", 134),
          ("uniqueMember", 50),
          ("unknown", 2),
          ("userCertificate", 36),
          ("userClass", 108),
          ("userPKCS12", 209),
          ("userPassword", 35),
          ("userSMIMECertificate", 208),
          ("x121Address", 24),
          ("x500UniqueIdentifier", 45))
    )



# MIB Managed Objects in the order of their OIDs

_XcmSnmpNetbiosDomain_ObjectIdentity = ObjectIdentity
xcmSnmpNetbiosDomain = _XcmSnmpNetbiosDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 3)
)
if mibBuilder.loadTexts:
    xcmSnmpNetbiosDomain.setStatus("current")
_XcmCOSpecialTypes_ObjectIdentity = ObjectIdentity
xcmCOSpecialTypes = _XcmCOSpecialTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4)
)
if mibBuilder.loadTexts:
    xcmCOSpecialTypes.setStatus("current")
_XcmCOSpecialLabel_ObjectIdentity = ObjectIdentity
xcmCOSpecialLabel = _XcmCOSpecialLabel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 1)
)
if mibBuilder.loadTexts:
    xcmCOSpecialLabel.setStatus("current")
_XcmCOSpecialImport_ObjectIdentity = ObjectIdentity
xcmCOSpecialImport = _XcmCOSpecialImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 2)
)
if mibBuilder.loadTexts:
    xcmCOSpecialImport.setStatus("current")
_XcmCOSpecialRemark_ObjectIdentity = ObjectIdentity
xcmCOSpecialRemark = _XcmCOSpecialRemark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 3)
)
if mibBuilder.loadTexts:
    xcmCOSpecialRemark.setStatus("current")
_XcmCOSpecialAddress_ObjectIdentity = ObjectIdentity
xcmCOSpecialAddress = _XcmCOSpecialAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 4)
)
if mibBuilder.loadTexts:
    xcmCOSpecialAddress.setStatus("current")
_XcmCOSpecialState_ObjectIdentity = ObjectIdentity
xcmCOSpecialState = _XcmCOSpecialState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 5)
)
if mibBuilder.loadTexts:
    xcmCOSpecialState.setStatus("current")
_XcmCOSpecialConditions_ObjectIdentity = ObjectIdentity
xcmCOSpecialConditions = _XcmCOSpecialConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 6)
)
if mibBuilder.loadTexts:
    xcmCOSpecialConditions.setStatus("current")
_XcmCOSpecialName_ObjectIdentity = ObjectIdentity
xcmCOSpecialName = _XcmCOSpecialName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 7)
)
if mibBuilder.loadTexts:
    xcmCOSpecialName.setStatus("current")
_XcmCOSpecialSupportedInteger_ObjectIdentity = ObjectIdentity
xcmCOSpecialSupportedInteger = _XcmCOSpecialSupportedInteger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 8)
)
if mibBuilder.loadTexts:
    xcmCOSpecialSupportedInteger.setStatus("current")
_XcmCOSpecialSupportedString_ObjectIdentity = ObjectIdentity
xcmCOSpecialSupportedString = _XcmCOSpecialSupportedString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 9)
)
if mibBuilder.loadTexts:
    xcmCOSpecialSupportedString.setStatus("current")
_XcmCOSpecialAcceptAddress_ObjectIdentity = ObjectIdentity
xcmCOSpecialAcceptAddress = _XcmCOSpecialAcceptAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 10)
)
if mibBuilder.loadTexts:
    xcmCOSpecialAcceptAddress.setStatus("current")
_XcmCOSpecialAcceptSubnet_ObjectIdentity = ObjectIdentity
xcmCOSpecialAcceptSubnet = _XcmCOSpecialAcceptSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 11)
)
if mibBuilder.loadTexts:
    xcmCOSpecialAcceptSubnet.setStatus("current")
_XcmCOSpecialRejectAddress_ObjectIdentity = ObjectIdentity
xcmCOSpecialRejectAddress = _XcmCOSpecialRejectAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 12)
)
if mibBuilder.loadTexts:
    xcmCOSpecialRejectAddress.setStatus("current")
_XcmCOSpecialRejectSubnet_ObjectIdentity = ObjectIdentity
xcmCOSpecialRejectSubnet = _XcmCOSpecialRejectSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 13)
)
if mibBuilder.loadTexts:
    xcmCOSpecialRejectSubnet.setStatus("current")
_XcmCOSpecialMaxRequestRetries_ObjectIdentity = ObjectIdentity
xcmCOSpecialMaxRequestRetries = _XcmCOSpecialMaxRequestRetries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 14)
)
if mibBuilder.loadTexts:
    xcmCOSpecialMaxRequestRetries.setStatus("current")
_XcmCOSpecialRequestTimeout_ObjectIdentity = ObjectIdentity
xcmCOSpecialRequestTimeout = _XcmCOSpecialRequestTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 15)
)
if mibBuilder.loadTexts:
    xcmCOSpecialRequestTimeout.setStatus("current")
_XcmCOSpecialSecurity_ObjectIdentity = ObjectIdentity
xcmCOSpecialSecurity = _XcmCOSpecialSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 4, 16)
)
if mibBuilder.loadTexts:
    xcmCOSpecialSecurity.setStatus("current")
_XcmSnmpIPHostnameDomain_ObjectIdentity = ObjectIdentity
xcmSnmpIPHostnameDomain = _XcmSnmpIPHostnameDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 5)
)
if mibBuilder.loadTexts:
    xcmSnmpIPHostnameDomain.setStatus("current")
_XcmCOOsilanSuite_ObjectIdentity = ObjectIdentity
xcmCOOsilanSuite = _XcmCOOsilanSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11)
)
_XcmCOOsilanPhysicals_ObjectIdentity = ObjectIdentity
xcmCOOsilanPhysicals = _XcmCOOsilanPhysicals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100)
)
_XcmCOOsilanConnectorType_ObjectIdentity = ObjectIdentity
xcmCOOsilanConnectorType = _XcmCOOsilanConnectorType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 1)
)
_XcmCOOsilanConnectorOverride_ObjectIdentity = ObjectIdentity
xcmCOOsilanConnectorOverride = _XcmCOOsilanConnectorOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 1, 1)
)
_XcmCOOsilanConnectorDetected_ObjectIdentity = ObjectIdentity
xcmCOOsilanConnectorDetected = _XcmCOOsilanConnectorDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 1, 2)
)
_XcmCOOsilanConnectorAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsilanConnectorAdaptive = _XcmCOOsilanConnectorAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 1, 3)
)
_XcmCOOsilanSignalType_ObjectIdentity = ObjectIdentity
xcmCOOsilanSignalType = _XcmCOOsilanSignalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 2)
)
_XcmCOOsilanSignalOverride_ObjectIdentity = ObjectIdentity
xcmCOOsilanSignalOverride = _XcmCOOsilanSignalOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 2, 1)
)
_XcmCOOsilanSignalDetected_ObjectIdentity = ObjectIdentity
xcmCOOsilanSignalDetected = _XcmCOOsilanSignalDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 2, 2)
)
_XcmCOOsilanSignalAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsilanSignalAdaptive = _XcmCOOsilanSignalAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 2, 3)
)
_XcmCOOsilanSignalSupport_ObjectIdentity = ObjectIdentity
xcmCOOsilanSignalSupport = _XcmCOOsilanSignalSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 2, 4)
)
_XcmCOOsilanSignalCapability_ObjectIdentity = ObjectIdentity
xcmCOOsilanSignalCapability = _XcmCOOsilanSignalCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 2, 5)
)
_XcmCOOsilanCableType_ObjectIdentity = ObjectIdentity
xcmCOOsilanCableType = _XcmCOOsilanCableType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 3)
)
_XcmCOOsilanCableOverride_ObjectIdentity = ObjectIdentity
xcmCOOsilanCableOverride = _XcmCOOsilanCableOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 3, 1)
)
_XcmCOOsilanCableDetected_ObjectIdentity = ObjectIdentity
xcmCOOsilanCableDetected = _XcmCOOsilanCableDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 3, 2)
)
_XcmCOOsilanCableAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsilanCableAdaptive = _XcmCOOsilanCableAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 3, 3)
)
_XcmCOOsilanCableSupport_ObjectIdentity = ObjectIdentity
xcmCOOsilanCableSupport = _XcmCOOsilanCableSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1100, 3, 4)
)
_XcmCOOsilanDatalinks_ObjectIdentity = ObjectIdentity
xcmCOOsilanDatalinks = _XcmCOOsilanDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1200)
)
_XcmCOOsilanFrameType_ObjectIdentity = ObjectIdentity
xcmCOOsilanFrameType = _XcmCOOsilanFrameType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1201)
)
_XcmCOOsilanFrameOverride_ObjectIdentity = ObjectIdentity
xcmCOOsilanFrameOverride = _XcmCOOsilanFrameOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1201, 1)
)
_XcmCOOsilanFrameDetected_ObjectIdentity = ObjectIdentity
xcmCOOsilanFrameDetected = _XcmCOOsilanFrameDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1201, 2)
)
_XcmCOOsilanFrameAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsilanFrameAdaptive = _XcmCOOsilanFrameAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1201, 3)
)
_XcmCOOsilanEthernet_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernet = _XcmCOOsilanEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203)
)
_XcmCOOsilanEthernetType_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetType = _XcmCOOsilanEthernetType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 1)
)
_XcmCOOsilanEthernetDevice_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetDevice = _XcmCOOsilanEthernetDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 2)
)
_XcmCOOsilanEthernetDeviceName_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetDeviceName = _XcmCOOsilanEthernetDeviceName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 2, 1)
)
_XcmCOOsilanEthernetSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetSpeed = _XcmCOOsilanEthernetSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 3)
)
_XcmCOOsilanEthernetSpeedOverride_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetSpeedOverride = _XcmCOOsilanEthernetSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 3, 1)
)
_XcmCOOsilanEthernetSpeedDetected_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetSpeedDetected = _XcmCOOsilanEthernetSpeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 3, 2)
)
_XcmCOOsilanEthernetSpeedAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetSpeedAdaptive = _XcmCOOsilanEthernetSpeedAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 3, 3)
)
_XcmCOOsilanEthernetSpeedSupport_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetSpeedSupport = _XcmCOOsilanEthernetSpeedSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 3, 4)
)
_XcmCOOsilanEthernetMinSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetMinSpeed = _XcmCOOsilanEthernetMinSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 3, 5)
)
_XcmCOOsilanEthernetMaxSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetMaxSpeed = _XcmCOOsilanEthernetMaxSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 3, 6)
)
_XcmCOOsilanEthernetMaxFrameSize_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetMaxFrameSize = _XcmCOOsilanEthernetMaxFrameSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 4)
)
_XcmCOOsilanEthernetInterface_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetInterface = _XcmCOOsilanEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 5)
)
_XcmCOOsilanEthernetMACAddress_ObjectIdentity = ObjectIdentity
xcmCOOsilanEthernetMACAddress = _XcmCOOsilanEthernetMACAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1203, 6)
)
_XcmCOOsilanTokenBus_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenBus = _XcmCOOsilanTokenBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1204)
)
_XcmCOOsilanTokenRing_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRing = _XcmCOOsilanTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205)
)
_XcmCOOsilanTokenRingType_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingType = _XcmCOOsilanTokenRingType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 1)
)
_XcmCOOsilanTokenRingDevice_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingDevice = _XcmCOOsilanTokenRingDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 2)
)
_XcmCOOsilanTokenRingDeviceName_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingDeviceName = _XcmCOOsilanTokenRingDeviceName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 2, 1)
)
_XcmCOOsilanTokenRingSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSpeed = _XcmCOOsilanTokenRingSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 3)
)
_XcmCOOsilanTokenRingSpeedOverride_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSpeedOverride = _XcmCOOsilanTokenRingSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 3, 1)
)
_XcmCOOsilanTokenRingSpeedDetected_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSpeedDetected = _XcmCOOsilanTokenRingSpeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 3, 2)
)
_XcmCOOsilanTokenRingSpeedAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSpeedAdaptive = _XcmCOOsilanTokenRingSpeedAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 3, 3)
)
_XcmCOOsilanTokenRingSpeedSupport_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSpeedSupport = _XcmCOOsilanTokenRingSpeedSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 3, 4)
)
_XcmCOOsilanTokenRingMinSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingMinSpeed = _XcmCOOsilanTokenRingMinSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 3, 5)
)
_XcmCOOsilanTokenRingMaxSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingMaxSpeed = _XcmCOOsilanTokenRingMaxSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 3, 6)
)
_XcmCOOsilanTokenRingMaxFrameSize_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingMaxFrameSize = _XcmCOOsilanTokenRingMaxFrameSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 4)
)
_XcmCOOsilanTokenRingInterface_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingInterface = _XcmCOOsilanTokenRingInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 5)
)
_XcmCOOsilanTokenRingMACAddress_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingMACAddress = _XcmCOOsilanTokenRingMACAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 6)
)
_XcmCOOsilanTokenRingSSR_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSSR = _XcmCOOsilanTokenRingSSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 11)
)
_XcmCOOsilanTokenRingSSRAllRoute_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSSRAllRoute = _XcmCOOsilanTokenRingSSRAllRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 12)
)
_XcmCOOsilanTokenRingSSRSingleRR_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSSRSingleRR = _XcmCOOsilanTokenRingSSRSingleRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 13)
)
_XcmCOOsilanTokenRingSSRAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingSSRAdaptive = _XcmCOOsilanTokenRingSSRAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 14)
)
_XcmCOOsilanTokenRingMACOverride_ObjectIdentity = ObjectIdentity
xcmCOOsilanTokenRingMACOverride = _XcmCOOsilanTokenRingMACOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1205, 21)
)
_XcmCOOsilanFDDI_ObjectIdentity = ObjectIdentity
xcmCOOsilanFDDI = _XcmCOOsilanFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 11, 1207)
)
_XcmCOOsiwanSuite_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSuite = _XcmCOOsiwanSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13)
)
_XcmCOOsiwanPhysicals_ObjectIdentity = ObjectIdentity
xcmCOOsiwanPhysicals = _XcmCOOsiwanPhysicals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100)
)
_XcmCOOsiwanConnectorType_ObjectIdentity = ObjectIdentity
xcmCOOsiwanConnectorType = _XcmCOOsiwanConnectorType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 1)
)
_XcmCOOsiwanConnectorOverride_ObjectIdentity = ObjectIdentity
xcmCOOsiwanConnectorOverride = _XcmCOOsiwanConnectorOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 1, 1)
)
_XcmCOOsiwanConnectorDetected_ObjectIdentity = ObjectIdentity
xcmCOOsiwanConnectorDetected = _XcmCOOsiwanConnectorDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 1, 2)
)
_XcmCOOsiwanConnectorAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsiwanConnectorAdaptive = _XcmCOOsiwanConnectorAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 1, 3)
)
_XcmCOOsiwanSignalType_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSignalType = _XcmCOOsiwanSignalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 2)
)
_XcmCOOsiwanSignalOverride_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSignalOverride = _XcmCOOsiwanSignalOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 2, 1)
)
_XcmCOOsiwanSignalDetected_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSignalDetected = _XcmCOOsiwanSignalDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 2, 2)
)
_XcmCOOsiwanSignalAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSignalAdaptive = _XcmCOOsiwanSignalAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 2, 3)
)
_XcmCOOsiwanSignalSupport_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSignalSupport = _XcmCOOsiwanSignalSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 2, 4)
)
_XcmCOOsiwanLineNumber_ObjectIdentity = ObjectIdentity
xcmCOOsiwanLineNumber = _XcmCOOsiwanLineNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 4)
)
_XcmCOOsiwanSendManual_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSendManual = _XcmCOOsiwanSendManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 5)
)
_XcmCOOsiwanReceiveManual_ObjectIdentity = ObjectIdentity
xcmCOOsiwanReceiveManual = _XcmCOOsiwanReceiveManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 6)
)
_XcmCOOsiwanRingsBeforeAnswer_ObjectIdentity = ObjectIdentity
xcmCOOsiwanRingsBeforeAnswer = _XcmCOOsiwanRingsBeforeAnswer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 7)
)
_XcmCOOsiwanErrorCorrection_ObjectIdentity = ObjectIdentity
xcmCOOsiwanErrorCorrection = _XcmCOOsiwanErrorCorrection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 8)
)
_XcmCOOsiwanDirection_ObjectIdentity = ObjectIdentity
xcmCOOsiwanDirection = _XcmCOOsiwanDirection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 9)
)
_XcmCOOsiwanSendStartTime_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSendStartTime = _XcmCOOsiwanSendStartTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 10)
)
_XcmCOOsiwanSendEndTime_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSendEndTime = _XcmCOOsiwanSendEndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 11)
)
_XcmCOOsiwanReceiveStartTime_ObjectIdentity = ObjectIdentity
xcmCOOsiwanReceiveStartTime = _XcmCOOsiwanReceiveStartTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 12)
)
_XcmCOOsiwanReceiveEndTime_ObjectIdentity = ObjectIdentity
xcmCOOsiwanReceiveEndTime = _XcmCOOsiwanReceiveEndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 13)
)
_XcmCOOsiwanRingerVolume_ObjectIdentity = ObjectIdentity
xcmCOOsiwanRingerVolume = _XcmCOOsiwanRingerVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 20)
)
_XcmCOOsiwanMonitorVolume_ObjectIdentity = ObjectIdentity
xcmCOOsiwanMonitorVolume = _XcmCOOsiwanMonitorVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 21)
)
_XcmCOOsiwanAlarmVolume_ObjectIdentity = ObjectIdentity
xcmCOOsiwanAlarmVolume = _XcmCOOsiwanAlarmVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 22)
)
_XcmCOOsiwanKeyboardVolume_ObjectIdentity = ObjectIdentity
xcmCOOsiwanKeyboardVolume = _XcmCOOsiwanKeyboardVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1100, 23)
)
_XcmCOOsiwanDatalinks_ObjectIdentity = ObjectIdentity
xcmCOOsiwanDatalinks = _XcmCOOsiwanDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1200)
)
_XcmCOOsiwanFax_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFax = _XcmCOOsiwanFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241)
)
_XcmCOOsiwanFaxAddress_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxAddress = _XcmCOOsiwanFaxAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 1)
)
_XcmCOOsiwanFaxDevice_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxDevice = _XcmCOOsiwanFaxDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 2)
)
_XcmCOOsiwanFaxDeviceName_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxDeviceName = _XcmCOOsiwanFaxDeviceName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 2, 1)
)
_XcmCOOsiwanFaxSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSpeed = _XcmCOOsiwanFaxSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 3)
)
_XcmCOOsiwanFaxSpeedOverride_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSpeedOverride = _XcmCOOsiwanFaxSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 3, 1)
)
_XcmCOOsiwanFaxSpeedDetected_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSpeedDetected = _XcmCOOsiwanFaxSpeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 3, 2)
)
_XcmCOOsiwanFaxSpeedAdaptive_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSpeedAdaptive = _XcmCOOsiwanFaxSpeedAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 3, 3)
)
_XcmCOOsiwanFaxSpeedSupport_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSpeedSupport = _XcmCOOsiwanFaxSpeedSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 3, 4)
)
_XcmCOOsiwanFaxMinSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxMinSpeed = _XcmCOOsiwanFaxMinSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 3, 5)
)
_XcmCOOsiwanFaxMaxSpeed_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxMaxSpeed = _XcmCOOsiwanFaxMaxSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 3, 6)
)
_XcmCOOsiwanFaxInterface_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxInterface = _XcmCOOsiwanFaxInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 5)
)
_XcmCOOsiwanFaxAcceptAddress_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxAcceptAddress = _XcmCOOsiwanFaxAcceptAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 11)
)
_XcmCOOsiwanFaxRejectAddress_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxRejectAddress = _XcmCOOsiwanFaxRejectAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 12)
)
_XcmCOOsiwanFaxSendCoverSheet_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSendCoverSheet = _XcmCOOsiwanFaxSendCoverSheet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 20)
)
_XcmCOOsiwanFaxSendHeader_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSendHeader = _XcmCOOsiwanFaxSendHeader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 21)
)
_XcmCOOsiwanFaxSendManual_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSendManual = _XcmCOOsiwanFaxSendManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 22)
)
_XcmCOOsiwanFaxSendSecurity_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSendSecurity = _XcmCOOsiwanFaxSendSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 23)
)
_XcmCOOsiwanFaxMaxRetries_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxMaxRetries = _XcmCOOsiwanFaxMaxRetries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 24)
)
_XcmCOOsiwanFaxRetryInterval_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxRetryInterval = _XcmCOOsiwanFaxRetryInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 25)
)
_XcmCOOsiwanFaxSendStoreTime_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxSendStoreTime = _XcmCOOsiwanFaxSendStoreTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 26)
)
_XcmCOOsiwanFaxMaxOriginalLength_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxMaxOriginalLength = _XcmCOOsiwanFaxMaxOriginalLength_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 27)
)
_XcmCOOsiwanFaxReceiveCoverSheet_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveCoverSheet = _XcmCOOsiwanFaxReceiveCoverSheet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 30)
)
_XcmCOOsiwanFaxReceiveFooter_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveFooter = _XcmCOOsiwanFaxReceiveFooter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 31)
)
_XcmCOOsiwanFaxReceiveToMemory_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveToMemory = _XcmCOOsiwanFaxReceiveToMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 32)
)
_XcmCOOsiwanFaxReceiveManual_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveManual = _XcmCOOsiwanFaxReceiveManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 33)
)
_XcmCOOsiwanFaxReceiveSecurity_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveSecurity = _XcmCOOsiwanFaxReceiveSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 34)
)
_XcmCOOsiwanFaxReceiveAutoReduce_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveAutoReduce = _XcmCOOsiwanFaxReceiveAutoReduce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 35)
)
_XcmCOOsiwanFaxReceiveOverflow_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveOverflow = _XcmCOOsiwanFaxReceiveOverflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 36)
)
_XcmCOOsiwanFaxReceiveCollate_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxReceiveCollate = _XcmCOOsiwanFaxReceiveCollate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 37)
)
_XcmCOOsiwanFaxG3_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxG3 = _XcmCOOsiwanFaxG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 40)
)
_XcmCOOsiwanFaxG4_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxG4 = _XcmCOOsiwanFaxG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 41)
)
_XcmCOOsiwanFaxLineSwitching_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxLineSwitching = _XcmCOOsiwanFaxLineSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 42)
)
_XcmCOOsiwanFaxMaxSpeedDial_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFaxMaxSpeedDial = _XcmCOOsiwanFaxMaxSpeedDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1241, 43)
)
_XcmCOOsiwanPSTN_ObjectIdentity = ObjectIdentity
xcmCOOsiwanPSTN = _XcmCOOsiwanPSTN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1251)
)
_XcmCOOsiwanPSTNAddress_ObjectIdentity = ObjectIdentity
xcmCOOsiwanPSTNAddress = _XcmCOOsiwanPSTNAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1251, 1)
)
_XcmCOOsiwanISDN_ObjectIdentity = ObjectIdentity
xcmCOOsiwanISDN = _XcmCOOsiwanISDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1261)
)
_XcmCOOsiwanISDNAddress_ObjectIdentity = ObjectIdentity
xcmCOOsiwanISDNAddress = _XcmCOOsiwanISDNAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1261, 1)
)
_XcmCOOsiwanTransports_ObjectIdentity = ObjectIdentity
xcmCOOsiwanTransports = _XcmCOOsiwanTransports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1400)
)
_XcmCOOsiwanApplications_ObjectIdentity = ObjectIdentity
xcmCOOsiwanApplications = _XcmCOOsiwanApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1700)
)
_XcmCOOsiwanDPA_ObjectIdentity = ObjectIdentity
xcmCOOsiwanDPA = _XcmCOOsiwanDPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1713)
)
_XcmCOOsiwanFTAM_ObjectIdentity = ObjectIdentity
xcmCOOsiwanFTAM = _XcmCOOsiwanFTAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1714)
)
_XcmCOOsiwanVT_ObjectIdentity = ObjectIdentity
xcmCOOsiwanVT = _XcmCOOsiwanVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1716)
)
_XcmCOOsiwanMHS_ObjectIdentity = ObjectIdentity
xcmCOOsiwanMHS = _XcmCOOsiwanMHS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1740)
)
_XcmCOOsiwanDS_ObjectIdentity = ObjectIdentity
xcmCOOsiwanDS = _XcmCOOsiwanDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1750)
)
_XcmCOOsiwanDAP_ObjectIdentity = ObjectIdentity
xcmCOOsiwanDAP = _XcmCOOsiwanDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1751)
)
_XcmCOOsiwanDSP_ObjectIdentity = ObjectIdentity
xcmCOOsiwanDSP = _XcmCOOsiwanDSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1752)
)
_XcmCOOsiwanMgmt_ObjectIdentity = ObjectIdentity
xcmCOOsiwanMgmt = _XcmCOOsiwanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1770)
)
_XcmCOOsiwanCMIP_ObjectIdentity = ObjectIdentity
xcmCOOsiwanCMIP = _XcmCOOsiwanCMIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1771)
)
_XcmCOOsiwanSecurity_ObjectIdentity = ObjectIdentity
xcmCOOsiwanSecurity = _XcmCOOsiwanSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 13, 1780)
)
_XcmCOInternetSuite_ObjectIdentity = ObjectIdentity
xcmCOInternetSuite = _XcmCOInternetSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14)
)
_XcmCOInternetDatalinks_ObjectIdentity = ObjectIdentity
xcmCOInternetDatalinks = _XcmCOInternetDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1200)
)
_XcmCOInternetSLIP_ObjectIdentity = ObjectIdentity
xcmCOInternetSLIP = _XcmCOInternetSLIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1201)
)
_XcmCOInternetPPP_ObjectIdentity = ObjectIdentity
xcmCOInternetPPP = _XcmCOInternetPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1202)
)
_XcmCOInternetIP_ObjectIdentity = ObjectIdentity
xcmCOInternetIP = _XcmCOInternetIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301)
)
_XcmCOInternetIPAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPAddress = _XcmCOInternetIPAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 1)
)
_XcmCOInternetIPSocketAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPSocketAddress = _XcmCOInternetIPSocketAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 1, 1)
)
_XcmCOInternetIPSubnetMask_ObjectIdentity = ObjectIdentity
xcmCOInternetIPSubnetMask = _XcmCOInternetIPSubnetMask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 2)
)
_XcmCOInternetIPAddressViaRARP_ObjectIdentity = ObjectIdentity
xcmCOInternetIPAddressViaRARP = _XcmCOInternetIPAddressViaRARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 3)
)
_XcmCOInternetIPDefaultGateway_ObjectIdentity = ObjectIdentity
xcmCOInternetIPDefaultGateway = _XcmCOInternetIPDefaultGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 4)
)
_XcmCOInternetIPAddressSource_ObjectIdentity = ObjectIdentity
xcmCOInternetIPAddressSource = _XcmCOInternetIPAddressSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 5)
)
_XcmCOInternetIPDatalinks_ObjectIdentity = ObjectIdentity
xcmCOInternetIPDatalinks = _XcmCOInternetIPDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 12)
)
_XcmCOInternetIPHostName_ObjectIdentity = ObjectIdentity
xcmCOInternetIPHostName = _XcmCOInternetIPHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 50)
)
_XcmCOInternetIPAutoIPAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPAutoIPAddress = _XcmCOInternetIPAutoIPAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 51)
)
_XcmCOInternetIPAutoEnable_ObjectIdentity = ObjectIdentity
xcmCOInternetIPAutoEnable = _XcmCOInternetIPAutoEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 60)
)
_XcmCOInternetIPBcastCache_ObjectIdentity = ObjectIdentity
xcmCOInternetIPBcastCache = _XcmCOInternetIPBcastCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 61)
)
_XcmCOInternetIPBCacheEnabled_ObjectIdentity = ObjectIdentity
xcmCOInternetIPBCacheEnabled = _XcmCOInternetIPBCacheEnabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 61, 1)
)
_XcmCOInternetIPBCacheAddress1_ObjectIdentity = ObjectIdentity
xcmCOInternetIPBCacheAddress1 = _XcmCOInternetIPBCacheAddress1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 61, 2)
)
_XcmCOInternetIPBCacheAddress2_ObjectIdentity = ObjectIdentity
xcmCOInternetIPBCacheAddress2 = _XcmCOInternetIPBCacheAddress2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 61, 3)
)
_XcmCOInternetIPBCacheAddress3_ObjectIdentity = ObjectIdentity
xcmCOInternetIPBCacheAddress3 = _XcmCOInternetIPBCacheAddress3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 61, 4)
)
_XcmCOInternetIPBCacheAddress4_ObjectIdentity = ObjectIdentity
xcmCOInternetIPBCacheAddress4 = _XcmCOInternetIPBCacheAddress4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 61, 5)
)
_XcmCOInternetIPInstall_ObjectIdentity = ObjectIdentity
xcmCOInternetIPInstall = _XcmCOInternetIPInstall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 62)
)
_XcmCOInternetIPInstallSelect_ObjectIdentity = ObjectIdentity
xcmCOInternetIPInstallSelect = _XcmCOInternetIPInstallSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 62, 1)
)
_XcmCOInternetIPAllSubnetsLocal_ObjectIdentity = ObjectIdentity
xcmCOInternetIPAllSubnetsLocal = _XcmCOInternetIPAllSubnetsLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 62, 2)
)
_XcmCOInternetIPSec_ObjectIdentity = ObjectIdentity
xcmCOInternetIPSec = _XcmCOInternetIPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1301, 70)
)
_XcmCOInternetICMP_ObjectIdentity = ObjectIdentity
xcmCOInternetICMP = _XcmCOInternetICMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1302)
)
_XcmCOInternetARP_ObjectIdentity = ObjectIdentity
xcmCOInternetARP = _XcmCOInternetARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1303)
)
_XcmCOInternetDHCP_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCP = _XcmCOInternetDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304)
)
_XcmCOInternetDHCPClassID_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPClassID = _XcmCOInternetDHCPClassID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 1)
)
_XcmCOInternetDHCPLeaseTime_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPLeaseTime = _XcmCOInternetDHCPLeaseTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 2)
)
_XcmCOInternetDHCPRequestTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPRequestTimeout = _XcmCOInternetDHCPRequestTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 3)
)
_XcmCOInternetDHCPServer_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPServer = _XcmCOInternetDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 4)
)
_XcmCOInternetDHCPOptionGet_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPOptionGet = _XcmCOInternetDHCPOptionGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10)
)
_XcmCODHCPGetSubnetMask_ObjectIdentity = ObjectIdentity
xcmCODHCPGetSubnetMask = _XcmCODHCPGetSubnetMask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 1)
)
_XcmCODHCPGetSubnetTimeOffset_ObjectIdentity = ObjectIdentity
xcmCODHCPGetSubnetTimeOffset = _XcmCODHCPGetSubnetTimeOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 2)
)
_XcmCODHCPGetRouter_ObjectIdentity = ObjectIdentity
xcmCODHCPGetRouter = _XcmCODHCPGetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 3)
)
_XcmCODHCPGetTPTimeServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetTPTimeServer = _XcmCODHCPGetTPTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 4)
)
_XcmCODHCPGetIEN116NameServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetIEN116NameServer = _XcmCODHCPGetIEN116NameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 5)
)
_XcmCODHCPGetDNSNameServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetDNSNameServer = _XcmCODHCPGetDNSNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 6)
)
_XcmCODHCPGetLogServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetLogServer = _XcmCODHCPGetLogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 7)
)
_XcmCODHCPGetCookieServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetCookieServer = _XcmCODHCPGetCookieServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 8)
)
_XcmCODHCPGetLPRServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetLPRServer = _XcmCODHCPGetLPRServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 9)
)
_XcmCODHCPGetImpressServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetImpressServer = _XcmCODHCPGetImpressServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 10)
)
_XcmCODHCPGetResourceLocServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetResourceLocServer = _XcmCODHCPGetResourceLocServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 11)
)
_XcmCODHCPGetHostName_ObjectIdentity = ObjectIdentity
xcmCODHCPGetHostName = _XcmCODHCPGetHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 12)
)
_XcmCODHCPGetBootFileSize_ObjectIdentity = ObjectIdentity
xcmCODHCPGetBootFileSize = _XcmCODHCPGetBootFileSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 13)
)
_XcmCODHCPGetMeritDumpFile_ObjectIdentity = ObjectIdentity
xcmCODHCPGetMeritDumpFile = _XcmCODHCPGetMeritDumpFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 14)
)
_XcmCODHCPGetDNSDomainName_ObjectIdentity = ObjectIdentity
xcmCODHCPGetDNSDomainName = _XcmCODHCPGetDNSDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 15)
)
_XcmCODHCPGetSwapServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetSwapServer = _XcmCODHCPGetSwapServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 16)
)
_XcmCODHCPGetRootPath_ObjectIdentity = ObjectIdentity
xcmCODHCPGetRootPath = _XcmCODHCPGetRootPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 17)
)
_XcmCODHCPGetExtensionsPath_ObjectIdentity = ObjectIdentity
xcmCODHCPGetExtensionsPath = _XcmCODHCPGetExtensionsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 18)
)
_XcmCODHCPGetIPForwarding_ObjectIdentity = ObjectIdentity
xcmCODHCPGetIPForwarding = _XcmCODHCPGetIPForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 19)
)
_XcmCODHCPGetNLSourceRouting_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNLSourceRouting = _XcmCODHCPGetNLSourceRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 20)
)
_XcmCODHCPGetNLPolicyFilter_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNLPolicyFilter = _XcmCODHCPGetNLPolicyFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 21)
)
_XcmCODHCPGetMaxIPDatagramSize_ObjectIdentity = ObjectIdentity
xcmCODHCPGetMaxIPDatagramSize = _XcmCODHCPGetMaxIPDatagramSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 22)
)
_XcmCODHCPGetIPDefaultTTL_ObjectIdentity = ObjectIdentity
xcmCODHCPGetIPDefaultTTL = _XcmCODHCPGetIPDefaultTTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 23)
)
_XcmCODHCPGetPathMTUAgeTimeout_ObjectIdentity = ObjectIdentity
xcmCODHCPGetPathMTUAgeTimeout = _XcmCODHCPGetPathMTUAgeTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 24)
)
_XcmCODHCPGetPathMTUPlateau_ObjectIdentity = ObjectIdentity
xcmCODHCPGetPathMTUPlateau = _XcmCODHCPGetPathMTUPlateau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 25)
)
_XcmCODHCPGetInterfaceMTUSize_ObjectIdentity = ObjectIdentity
xcmCODHCPGetInterfaceMTUSize = _XcmCODHCPGetInterfaceMTUSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 26)
)
_XcmCODHCPGetAllSubnetsLocal_ObjectIdentity = ObjectIdentity
xcmCODHCPGetAllSubnetsLocal = _XcmCODHCPGetAllSubnetsLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 27)
)
_XcmCODHCPGetBroadcastAddress_ObjectIdentity = ObjectIdentity
xcmCODHCPGetBroadcastAddress = _XcmCODHCPGetBroadcastAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 28)
)
_XcmCODHCPGetMaskDiscovery_ObjectIdentity = ObjectIdentity
xcmCODHCPGetMaskDiscovery = _XcmCODHCPGetMaskDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 29)
)
_XcmCODHCPGetMaskSupplier_ObjectIdentity = ObjectIdentity
xcmCODHCPGetMaskSupplier = _XcmCODHCPGetMaskSupplier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 30)
)
_XcmCODHCPGetRouterDiscovery_ObjectIdentity = ObjectIdentity
xcmCODHCPGetRouterDiscovery = _XcmCODHCPGetRouterDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 31)
)
_XcmCODHCPGetRouterSolAddress_ObjectIdentity = ObjectIdentity
xcmCODHCPGetRouterSolAddress = _XcmCODHCPGetRouterSolAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 32)
)
_XcmCODHCPGetStaticRoute_ObjectIdentity = ObjectIdentity
xcmCODHCPGetStaticRoute = _XcmCODHCPGetStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 33)
)
_XcmCODHCPGetARPTrailer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetARPTrailer = _XcmCODHCPGetARPTrailer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 34)
)
_XcmCODHCPGetARPCacheTimeout_ObjectIdentity = ObjectIdentity
xcmCODHCPGetARPCacheTimeout = _XcmCODHCPGetARPCacheTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 35)
)
_XcmCODHCPGetEthernetFrameIEEE_ObjectIdentity = ObjectIdentity
xcmCODHCPGetEthernetFrameIEEE = _XcmCODHCPGetEthernetFrameIEEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 36)
)
_XcmCODHCPGetTCPDefaultTTL_ObjectIdentity = ObjectIdentity
xcmCODHCPGetTCPDefaultTTL = _XcmCODHCPGetTCPDefaultTTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 37)
)
_XcmCODHCPGetTCPKeepInterval_ObjectIdentity = ObjectIdentity
xcmCODHCPGetTCPKeepInterval = _XcmCODHCPGetTCPKeepInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 38)
)
_XcmCODHCPGetTCPKeepGarbage_ObjectIdentity = ObjectIdentity
xcmCODHCPGetTCPKeepGarbage = _XcmCODHCPGetTCPKeepGarbage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 39)
)
_XcmCODHCPGetNISDomainName_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNISDomainName = _XcmCODHCPGetNISDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 40)
)
_XcmCODHCPGetNISNameServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNISNameServer = _XcmCODHCPGetNISNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 41)
)
_XcmCODHCPGetNTPTimeServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNTPTimeServer = _XcmCODHCPGetNTPTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 42)
)
_XcmCODHCPGetVendorSpecific_ObjectIdentity = ObjectIdentity
xcmCODHCPGetVendorSpecific = _XcmCODHCPGetVendorSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 43)
)
_XcmCODHCPGetNetbiosNameServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNetbiosNameServer = _XcmCODHCPGetNetbiosNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 44)
)
_XcmCODHCPGetNetbiosDistServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNetbiosDistServer = _XcmCODHCPGetNetbiosDistServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 45)
)
_XcmCODHCPGetNetbiosNodeType_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNetbiosNodeType = _XcmCODHCPGetNetbiosNodeType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 46)
)
_XcmCODHCPGetNetbiosScope_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNetbiosScope = _XcmCODHCPGetNetbiosScope_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 47)
)
_XcmCODHCPGetXWindowFontServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetXWindowFontServer = _XcmCODHCPGetXWindowFontServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 48)
)
_XcmCODHCPGetXWindowDisplayMgr_ObjectIdentity = ObjectIdentity
xcmCODHCPGetXWindowDisplayMgr = _XcmCODHCPGetXWindowDisplayMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 49)
)
_XcmCODHCPGetMessageType_ObjectIdentity = ObjectIdentity
xcmCODHCPGetMessageType = _XcmCODHCPGetMessageType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 53)
)
_XcmCODHCPGetServerID_ObjectIdentity = ObjectIdentity
xcmCODHCPGetServerID = _XcmCODHCPGetServerID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 54)
)
_XcmCODHCPGetParameterRequest_ObjectIdentity = ObjectIdentity
xcmCODHCPGetParameterRequest = _XcmCODHCPGetParameterRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 55)
)
_XcmCODHCPGetErrorMessage_ObjectIdentity = ObjectIdentity
xcmCODHCPGetErrorMessage = _XcmCODHCPGetErrorMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 56)
)
_XcmCODHCPGetMaxMessageSize_ObjectIdentity = ObjectIdentity
xcmCODHCPGetMaxMessageSize = _XcmCODHCPGetMaxMessageSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 57)
)
_XcmCODHCPGetRenewT1Interval_ObjectIdentity = ObjectIdentity
xcmCODHCPGetRenewT1Interval = _XcmCODHCPGetRenewT1Interval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 58)
)
_XcmCODHCPGetRebindT2Interval_ObjectIdentity = ObjectIdentity
xcmCODHCPGetRebindT2Interval = _XcmCODHCPGetRebindT2Interval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 59)
)
_XcmCODHCPGetNISPlusDomainName_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNISPlusDomainName = _XcmCODHCPGetNISPlusDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 64)
)
_XcmCODHCPGetNISPlusNameServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNISPlusNameServer = _XcmCODHCPGetNISPlusNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 65)
)
_XcmCODHCPGetTFTPServerName_ObjectIdentity = ObjectIdentity
xcmCODHCPGetTFTPServerName = _XcmCODHCPGetTFTPServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 66)
)
_XcmCODHCPGetBootFileName_ObjectIdentity = ObjectIdentity
xcmCODHCPGetBootFileName = _XcmCODHCPGetBootFileName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 67)
)
_XcmCODHCPGetMobileIPHomeAgent_ObjectIdentity = ObjectIdentity
xcmCODHCPGetMobileIPHomeAgent = _XcmCODHCPGetMobileIPHomeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 68)
)
_XcmCODHCPGetSMTPMailServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetSMTPMailServer = _XcmCODHCPGetSMTPMailServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 69)
)
_XcmCODHCPGetPOP3MailServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetPOP3MailServer = _XcmCODHCPGetPOP3MailServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 70)
)
_XcmCODHCPGetNNTPNewsServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNNTPNewsServer = _XcmCODHCPGetNNTPNewsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 71)
)
_XcmCODHCPGetWWWServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetWWWServer = _XcmCODHCPGetWWWServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 72)
)
_XcmCODHCPGetFingerServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetFingerServer = _XcmCODHCPGetFingerServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 73)
)
_XcmCODHCPGetIRCServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetIRCServer = _XcmCODHCPGetIRCServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 74)
)
_XcmCODHCPGetStreetTalkServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetStreetTalkServer = _XcmCODHCPGetStreetTalkServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 75)
)
_XcmCODHCPGetStreetTalkDAServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetStreetTalkDAServer = _XcmCODHCPGetStreetTalkDAServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 76)
)
_XcmCODHCPGetNDSNameServer_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNDSNameServer = _XcmCODHCPGetNDSNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 85)
)
_XcmCODHCPGetNDSTreeName_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNDSTreeName = _XcmCODHCPGetNDSTreeName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 86)
)
_XcmCODHCPGetNDSContext_ObjectIdentity = ObjectIdentity
xcmCODHCPGetNDSContext = _XcmCODHCPGetNDSContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 10, 87)
)
_XcmCOInternetDHCPOptionSet_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPOptionSet = _XcmCOInternetDHCPOptionSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 11)
)
_XcmCODHCPSetIPAddressRequest_ObjectIdentity = ObjectIdentity
xcmCODHCPSetIPAddressRequest = _XcmCODHCPSetIPAddressRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 11, 50)
)
_XcmCODHCPSetIPAddressLeaseTime_ObjectIdentity = ObjectIdentity
xcmCODHCPSetIPAddressLeaseTime = _XcmCODHCPSetIPAddressLeaseTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 11, 51)
)
_XcmCODHCPSetOptionOverload_ObjectIdentity = ObjectIdentity
xcmCODHCPSetOptionOverload = _XcmCODHCPSetOptionOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 11, 52)
)
_XcmCODHCPSetClassID_ObjectIdentity = ObjectIdentity
xcmCODHCPSetClassID = _XcmCODHCPSetClassID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 11, 60)
)
_XcmCODHCPSetClientID_ObjectIdentity = ObjectIdentity
xcmCODHCPSetClientID = _XcmCODHCPSetClientID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1304, 11, 61)
)
_XcmCOInternetBOOTP_ObjectIdentity = ObjectIdentity
xcmCOInternetBOOTP = _XcmCOInternetBOOTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1305)
)
_XcmCOInternetBOOTPBroadcastEnabled_ObjectIdentity = ObjectIdentity
xcmCOInternetBOOTPBroadcastEnabled = _XcmCOInternetBOOTPBroadcastEnabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1305, 1)
)
_XcmCOInternetRARP_ObjectIdentity = ObjectIdentity
xcmCOInternetRARP = _XcmCOInternetRARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1306)
)
_XcmCOInternetIPv6_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6 = _XcmCOInternetIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310)
)
_XcmCOInternetIPv6Address_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6Address = _XcmCOInternetIPv6Address_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1)
)
_XcmCOInternetIPv6SocketAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6SocketAddress = _XcmCOInternetIPv6SocketAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1, 1)
)
_XcmCOInternetIPv6ManuallyAssignedAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6ManuallyAssignedAddress = _XcmCOInternetIPv6ManuallyAssignedAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1, 2)
)
_XcmCOInternetIPv6DHCPv6AssignedAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6DHCPv6AssignedAddress = _XcmCOInternetIPv6DHCPv6AssignedAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1, 3)
)
_XcmCOInternetIPv6LinkLocalAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6LinkLocalAddress = _XcmCOInternetIPv6LinkLocalAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1, 4)
)
_XcmCOInternetIPv6StatelessAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6StatelessAddress = _XcmCOInternetIPv6StatelessAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1, 5)
)
_XcmCOInternetIPv6RandomAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6RandomAddress = _XcmCOInternetIPv6RandomAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1, 6)
)
_XcmCOInternetIPv6AutomaticAddressing_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6AutomaticAddressing = _XcmCOInternetIPv6AutomaticAddressing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 1, 7)
)
_XcmCOInternetIPv6EUI64InterfaceId_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6EUI64InterfaceId = _XcmCOInternetIPv6EUI64InterfaceId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 2)
)
_XcmCOInternetIPv6RouterAdvertisementAddressPrefix_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6RouterAdvertisementAddressPrefix = _XcmCOInternetIPv6RouterAdvertisementAddressPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 3)
)
_XcmCOInternetIPv6DefaultGateway_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6DefaultGateway = _XcmCOInternetIPv6DefaultGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 4)
)
_XcmCOInternetIPv6HostName_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6HostName = _XcmCOInternetIPv6HostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1310, 5)
)
_XcmCOInternetTransports_ObjectIdentity = ObjectIdentity
xcmCOInternetTransports = _XcmCOInternetTransports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1400)
)
_XcmCOInternetUDP_ObjectIdentity = ObjectIdentity
xcmCOInternetUDP = _XcmCOInternetUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1401)
)
_XcmCOInternetUDPAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetUDPAddress = _XcmCOInternetUDPAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1401, 1)
)
_XcmCOInternetUDPPort_ObjectIdentity = ObjectIdentity
xcmCOInternetUDPPort = _XcmCOInternetUDPPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1401, 2)
)
_XcmCOInternetTCP_ObjectIdentity = ObjectIdentity
xcmCOInternetTCP = _XcmCOInternetTCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1402)
)
_XcmCOInternetTCPAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetTCPAddress = _XcmCOInternetTCPAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1402, 1)
)
_XcmCOInternetTCPPort_ObjectIdentity = ObjectIdentity
xcmCOInternetTCPPort = _XcmCOInternetTCPPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1402, 2)
)
_XcmCOInternetTCPMaxSegmentSize_ObjectIdentity = ObjectIdentity
xcmCOInternetTCPMaxSegmentSize = _XcmCOInternetTCPMaxSegmentSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1402, 3)
)
_XcmCOInternetPing_ObjectIdentity = ObjectIdentity
xcmCOInternetPing = _XcmCOInternetPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1404)
)
_XcmCOInternetSSL3_ObjectIdentity = ObjectIdentity
xcmCOInternetSSL3 = _XcmCOInternetSSL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1405)
)
_XcmCOInternetSSL3Port_ObjectIdentity = ObjectIdentity
xcmCOInternetSSL3Port = _XcmCOInternetSSL3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1405, 1)
)
_XcmCOInternetSSL3CipherStrength_ObjectIdentity = ObjectIdentity
xcmCOInternetSSL3CipherStrength = _XcmCOInternetSSL3CipherStrength_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1405, 2)
)
_XcmCOInternetTLS_ObjectIdentity = ObjectIdentity
xcmCOInternetTLS = _XcmCOInternetTLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1406)
)
_XcmCOInternetICMPv6_ObjectIdentity = ObjectIdentity
xcmCOInternetICMPv6 = _XcmCOInternetICMPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1410)
)
_XcmCOInternetRaw_ObjectIdentity = ObjectIdentity
xcmCOInternetRaw = _XcmCOInternetRaw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501)
)
_XcmCOInternetRawHostName_ObjectIdentity = ObjectIdentity
xcmCOInternetRawHostName = _XcmCOInternetRawHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 1)
)
_XcmCOInternetRawHostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetRawHostAddress = _XcmCOInternetRawHostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 2)
)
_XcmCOInternetRawListenSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetRawListenSocket = _XcmCOInternetRawListenSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 3)
)
_XcmCOInternetRawMaxClients_ObjectIdentity = ObjectIdentity
xcmCOInternetRawMaxClients = _XcmCOInternetRawMaxClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 4)
)
_XcmCOInternetRawAcceptAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetRawAcceptAddress = _XcmCOInternetRawAcceptAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 11)
)
_XcmCOInternetRawAcceptSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetRawAcceptSubnet = _XcmCOInternetRawAcceptSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 12)
)
_XcmCOInternetRawRejectAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetRawRejectAddress = _XcmCOInternetRawRejectAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 21)
)
_XcmCOInternetRawRejectSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetRawRejectSubnet = _XcmCOInternetRawRejectSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 22)
)
_XcmCOInternetRawSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetRawSpool = _XcmCOInternetRawSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 31)
)
_XcmCOInternetRawMaxSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetRawMaxSpool = _XcmCOInternetRawMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 32)
)
_XcmCOInternetRawJobTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetRawJobTimeout = _XcmCOInternetRawJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 40)
)
_XcmCOInternetRawAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCOInternetRawAutoSwitch = _XcmCOInternetRawAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 41)
)
_XcmCOInternetRawBinaryPS_ObjectIdentity = ObjectIdentity
xcmCOInternetRawBinaryPS = _XcmCOInternetRawBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 42)
)
_XcmCOInternetRawDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCOInternetRawDefaultPDL = _XcmCOInternetRawDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 43)
)
_XcmCOInternetRawBidirectional_ObjectIdentity = ObjectIdentity
xcmCOInternetRawBidirectional = _XcmCOInternetRawBidirectional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1501, 44)
)
_XcmCOInternetIPP_ObjectIdentity = ObjectIdentity
xcmCOInternetIPP = _XcmCOInternetIPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502)
)
_XcmCOInternetIPPHostName_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPHostName = _XcmCOInternetIPPHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 1)
)
_XcmCOInternetIPPHostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPHostAddress = _XcmCOInternetIPPHostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 2)
)
_XcmCOInternetIPPListenSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPListenSocket = _XcmCOInternetIPPListenSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 3)
)
_XcmCOInternetIPPMaxClients_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPMaxClients = _XcmCOInternetIPPMaxClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 4)
)
_XcmCOInternetIPPVersionString_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPVersionString = _XcmCOInternetIPPVersionString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 9)
)
_XcmCOInternetIPPAcceptAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPAcceptAddress = _XcmCOInternetIPPAcceptAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 11)
)
_XcmCOInternetIPPAcceptSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPAcceptSubnet = _XcmCOInternetIPPAcceptSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 12)
)
_XcmCOInternetIPPRejectAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPRejectAddress = _XcmCOInternetIPPRejectAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 21)
)
_XcmCOInternetIPPRejectSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPRejectSubnet = _XcmCOInternetIPPRejectSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 22)
)
_XcmCOInternetIPPSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPSpool = _XcmCOInternetIPPSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 31)
)
_XcmCOInternetIPPMaxSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPMaxSpool = _XcmCOInternetIPPMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 32)
)
_XcmCOInternetIPPJobTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPJobTimeout = _XcmCOInternetIPPJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 40)
)
_XcmCOInternetIPPAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPAutoSwitch = _XcmCOInternetIPPAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 41)
)
_XcmCOInternetIPPBinaryPS_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPBinaryPS = _XcmCOInternetIPPBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 42)
)
_XcmCOInternetIPPDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPDefaultPDL = _XcmCOInternetIPPDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 43)
)
_XcmCOInternetIPPAuthScheme_ObjectIdentity = ObjectIdentity
xcmCOInternetIPPAuthScheme = _XcmCOInternetIPPAuthScheme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1502, 50)
)
_XcmCOInternetLPR_ObjectIdentity = ObjectIdentity
xcmCOInternetLPR = _XcmCOInternetLPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503)
)
_XcmCOInternetLPRHostName_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRHostName = _XcmCOInternetLPRHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 1)
)
_XcmCOInternetLPRHostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRHostAddress = _XcmCOInternetLPRHostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 2)
)
_XcmCOInternetLPRListenSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRListenSocket = _XcmCOInternetLPRListenSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 3)
)
_XcmCOInternetLPRMaxClients_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRMaxClients = _XcmCOInternetLPRMaxClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 4)
)
_XcmCOInternetLPRAcceptAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRAcceptAddress = _XcmCOInternetLPRAcceptAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 11)
)
_XcmCOInternetLPRAcceptSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRAcceptSubnet = _XcmCOInternetLPRAcceptSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 12)
)
_XcmCOInternetLPRRejectAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRRejectAddress = _XcmCOInternetLPRRejectAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 21)
)
_XcmCOInternetLPRRejectSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRRejectSubnet = _XcmCOInternetLPRRejectSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 22)
)
_XcmCOInternetLPRSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRSpool = _XcmCOInternetLPRSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 31)
)
_XcmCOInternetLPRMaxSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRMaxSpool = _XcmCOInternetLPRMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 32)
)
_XcmCOInternetLPRJobTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRJobTimeout = _XcmCOInternetLPRJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 40)
)
_XcmCOInternetLPRAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRAutoSwitch = _XcmCOInternetLPRAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 41)
)
_XcmCOInternetLPRBinaryPS_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRBinaryPS = _XcmCOInternetLPRBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 42)
)
_XcmCOInternetLPRDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCOInternetLPRDefaultPDL = _XcmCOInternetLPRDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1503, 43)
)
_XcmCOInternetFTP_ObjectIdentity = ObjectIdentity
xcmCOInternetFTP = _XcmCOInternetFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1504)
)
_XcmCOInternetFTPPassiveMode_ObjectIdentity = ObjectIdentity
xcmCOInternetFTPPassiveMode = _XcmCOInternetFTPPassiveMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1504, 1)
)
_XcmCOInternetSMTP_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTP = _XcmCOInternetSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505)
)
_XcmCOInternetSMTPHostName_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPHostName = _XcmCOInternetSMTPHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 1)
)
_XcmCOInternetSMTPHostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPHostAddress = _XcmCOInternetSMTPHostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 2)
)
_XcmCOInternetSMTPListenSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPListenSocket = _XcmCOInternetSMTPListenSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 3)
)
_XcmCOInternetSMTPMaxClients_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxClients = _XcmCOInternetSMTPMaxClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 4)
)
_XcmCOInternetSMTPAcceptAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPAcceptAddress = _XcmCOInternetSMTPAcceptAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 11)
)
_XcmCOInternetSMTPAcceptSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPAcceptSubnet = _XcmCOInternetSMTPAcceptSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 12)
)
_XcmCOInternetSMTPRejectAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPRejectAddress = _XcmCOInternetSMTPRejectAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 21)
)
_XcmCOInternetSMTPRejectSubnet_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPRejectSubnet = _XcmCOInternetSMTPRejectSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 22)
)
_XcmCOInternetSMTPSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPSpool = _XcmCOInternetSMTPSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 31)
)
_XcmCOInternetSMTPMaxSpool_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxSpool = _XcmCOInternetSMTPMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 32)
)
_XcmCOInternetSMTPJobTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPJobTimeout = _XcmCOInternetSMTPJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 40)
)
_XcmCOInternetSMTPAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPAutoSwitch = _XcmCOInternetSMTPAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 41)
)
_XcmCOInternetSMTPBinaryPS_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPBinaryPS = _XcmCOInternetSMTPBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 42)
)
_XcmCOInternetSMTPDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPDefaultPDL = _XcmCOInternetSMTPDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 43)
)
_XcmCOInternetSMTPSubject_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPSubject = _XcmCOInternetSMTPSubject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 44)
)
_XcmCOInternetSMTPSignatureLine_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPSignatureLine = _XcmCOInternetSMTPSignatureLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 45)
)
_XcmCOInternetSMTPUserName_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPUserName = _XcmCOInternetSMTPUserName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 47)
)
_XcmCOInternetSMTPPassword_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPPassword = _XcmCOInternetSMTPPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 48)
)
_XcmCOInternetSMTPMaxInputText_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxInputText = _XcmCOInternetSMTPMaxInputText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 50)
)
_XcmCOInternetSMTPMaxInputAttach_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxInputAttach = _XcmCOInternetSMTPMaxInputAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 51)
)
_XcmCOInternetSMTPMaxOutputText_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxOutputText = _XcmCOInternetSMTPMaxOutputText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 52)
)
_XcmCOInternetSMTPMaxOutputAttach_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxOutputAttach = _XcmCOInternetSMTPMaxOutputAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 53)
)
_XcmCOInternetSMTPConfirmRequest_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPConfirmRequest = _XcmCOInternetSMTPConfirmRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 54)
)
_XcmCOInternetSMTPConfirmReply_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPConfirmReply = _XcmCOInternetSMTPConfirmReply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 55)
)
_XcmCOInternetSMTPConfirmTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPConfirmTimeout = _XcmCOInternetSMTPConfirmTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 56)
)
_XcmCOInternetSMTPFeatureReply_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPFeatureReply = _XcmCOInternetSMTPFeatureReply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 57)
)
_XcmCOInternetSMTPMailAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMailAddress = _XcmCOInternetSMTPMailAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 58)
)
_XcmCOInternetSMTPMaxInFragments_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxInFragments = _XcmCOInternetSMTPMaxInFragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 59)
)
_XcmCOInternetSMTPMaxOutFragments_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxOutFragments = _XcmCOInternetSMTPMaxOutFragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 60)
)
_XcmCOInternetSMTPMaxInAttachments_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxInAttachments = _XcmCOInternetSMTPMaxInAttachments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 61)
)
_XcmCOInternetSMTPMaxOutAttachments_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxOutAttachments = _XcmCOInternetSMTPMaxOutAttachments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 62)
)
_XcmCOInternetSMTPMaxInputSize_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxInputSize = _XcmCOInternetSMTPMaxInputSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 63)
)
_XcmCOInternetSMTPMaxOutputSize_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPMaxOutputSize = _XcmCOInternetSMTPMaxOutputSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 64)
)
_XcmCOInternetSMTPReversePath_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPReversePath = _XcmCOInternetSMTPReversePath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 65)
)
_XcmCOInternetSMTPAutoServer_ObjectIdentity = ObjectIdentity
xcmCOInternetSMTPAutoServer = _XcmCOInternetSMTPAutoServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1505, 70)
)
_XcmCOInternetTelnet_ObjectIdentity = ObjectIdentity
xcmCOInternetTelnet = _XcmCOInternetTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1506)
)
_XcmCOInternetDNS_ObjectIdentity = ObjectIdentity
xcmCOInternetDNS = _XcmCOInternetDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507)
)
_XcmCOInternetDNSDomainName_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSDomainName = _XcmCOInternetDNSDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 1)
)
_XcmCOInternetDNSLanguage_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSLanguage = _XcmCOInternetDNSLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 3)
)
_XcmCOInternetDNSCharset_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSCharset = _XcmCOInternetDNSCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 4)
)
_XcmCOInternetDNSServerName_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSServerName = _XcmCOInternetDNSServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 5)
)
_XcmCOInternetDNSServerAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSServerAddress = _XcmCOInternetDNSServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 6)
)
_XcmCOInternetDNSServerResolvedAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSServerResolvedAddress = _XcmCOInternetDNSServerResolvedAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 7)
)
_XcmCOInternetDNSServerTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSServerTimeout = _XcmCOInternetDNSServerTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 8)
)
_XcmCOInternetDNSAppendDomainName_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSAppendDomainName = _XcmCOInternetDNSAppendDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 9)
)
_XcmCOInternetDNSAppendParentDomains_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSAppendParentDomains = _XcmCOInternetDNSAppendParentDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 10)
)
_XcmCOInternetDNSDomainNameList_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSDomainNameList = _XcmCOInternetDNSDomainNameList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 11)
)
_XcmCOInternetDNSDynamicUpdate_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSDynamicUpdate = _XcmCOInternetDNSDynamicUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 13)
)
_XcmCOInternetDNSUpdatePolicy_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSUpdatePolicy = _XcmCOInternetDNSUpdatePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 14)
)
_XcmCOInternetDNSMulticastEnable_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSMulticastEnable = _XcmCOInternetDNSMulticastEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 30)
)
_XcmCOInternetIOSDiscoveryEnable_ObjectIdentity = ObjectIdentity
xcmCOInternetIOSDiscoveryEnable = _XcmCOInternetIOSDiscoveryEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1507, 31)
)
_XcmCOInternetTFTP_ObjectIdentity = ObjectIdentity
xcmCOInternetTFTP = _XcmCOInternetTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1508)
)
_XcmCOInternetHTTP_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTP = _XcmCOInternetHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509)
)
_XcmCOInternetHTTPAddressURL_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPAddressURL = _XcmCOInternetHTTPAddressURL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 1)
)
_XcmCOInternetHTTPAddressURI_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPAddressURI = _XcmCOInternetHTTPAddressURI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 2)
)
_XcmCOInternetHTTPAddressURN_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPAddressURN = _XcmCOInternetHTTPAddressURN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 3)
)
_XcmCOInternetHTTPVersionString_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPVersionString = _XcmCOInternetHTTPVersionString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 9)
)
_XcmCOInternetHTTPListenSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPListenSocket = _XcmCOInternetHTTPListenSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 11)
)
_XcmCOInternetHTTPMaxClients_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPMaxClients = _XcmCOInternetHTTPMaxClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 12)
)
_XcmCOInternetHTTPClientTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPClientTimeout = _XcmCOInternetHTTPClientTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 13)
)
_XcmCOInternetHTTPStatusRefresh_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPStatusRefresh = _XcmCOInternetHTTPStatusRefresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 14)
)
_XcmCOInternetHTTPAdminAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPAdminAddress = _XcmCOInternetHTTPAdminAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 15)
)
_XcmCOInternetHTTPKeyUsrAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPKeyUsrAddress = _XcmCOInternetHTTPKeyUsrAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 16)
)
_XcmCOInternetHTTPProxy_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxy = _XcmCOInternetHTTPProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20)
)
_XcmCOInternetHTTPProxyIPAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyIPAddress = _XcmCOInternetHTTPProxyIPAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 1)
)
_XcmCOInternetHTTPProxyHostName_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyHostName = _XcmCOInternetHTTPProxyHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 2)
)
_XcmCOInternetHTTPProxyPortNumber_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyPortNumber = _XcmCOInternetHTTPProxyPortNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 3)
)
_XcmCOInternetHTTPProxyExceptions_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyExceptions = _XcmCOInternetHTTPProxyExceptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 4)
)
_XcmCOInternetHTTPProxyServer_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyServer = _XcmCOInternetHTTPProxyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 5)
)
_XcmCOInternetHTTPProxyUserName_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyUserName = _XcmCOInternetHTTPProxyUserName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 6)
)
_XcmCOInternetHTTPProxyPassword_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyPassword = _XcmCOInternetHTTPProxyPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 7)
)
_XcmCOInternetHTTPProxyAutoDetect_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyAutoDetect = _XcmCOInternetHTTPProxyAutoDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 8)
)
_XcmCOInternetHTTPProxyShareSettings_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyShareSettings = _XcmCOInternetHTTPProxyShareSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 9)
)
_XcmCOInternetHTTPProxyAuthValid_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPProxyAuthValid = _XcmCOInternetHTTPProxyAuthValid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 20, 10)
)
_XcmCOInternetHTTPInfoFwd_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPInfoFwd = _XcmCOInternetHTTPInfoFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1509, 25)
)
_XcmCOInternetSNMP_ObjectIdentity = ObjectIdentity
xcmCOInternetSNMP = _XcmCOInternetSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1510)
)
_XcmCOInternetSNMPVersion_ObjectIdentity = ObjectIdentity
xcmCOInternetSNMPVersion = _XcmCOInternetSNMPVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1510, 1)
)
_XcmCOInternetSNMPAdminAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetSNMPAdminAddress = _XcmCOInternetSNMPAdminAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1510, 2)
)
_XcmCOInternetSNMPv1_ObjectIdentity = ObjectIdentity
xcmCOInternetSNMPv1 = _XcmCOInternetSNMPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1511)
)
_XcmCOInternetSNMPv2_ObjectIdentity = ObjectIdentity
xcmCOInternetSNMPv2 = _XcmCOInternetSNMPv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1512)
)
_XcmCOInternetSNMPv3_ObjectIdentity = ObjectIdentity
xcmCOInternetSNMPv3 = _XcmCOInternetSNMPv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1513)
)
_XcmCOInternetPOP3_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3 = _XcmCOInternetPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514)
)
_XcmCOInternetPOP3HostName_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3HostName = _XcmCOInternetPOP3HostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 1)
)
_XcmCOInternetPOP3HostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3HostAddress = _XcmCOInternetPOP3HostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 2)
)
_XcmCOInternetPOP3PollInterval_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3PollInterval = _XcmCOInternetPOP3PollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 4)
)
_XcmCOInternetPOP3Subject_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3Subject = _XcmCOInternetPOP3Subject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 44)
)
_XcmCOInternetPOP3SignatureLine_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3SignatureLine = _XcmCOInternetPOP3SignatureLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 45)
)
_XcmCOInternetPOP3UserName_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3UserName = _XcmCOInternetPOP3UserName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 47)
)
_XcmCOInternetPOP3Password_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3Password = _XcmCOInternetPOP3Password_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 48)
)
_XcmCOInternetPOP3MaxInputText_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxInputText = _XcmCOInternetPOP3MaxInputText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 50)
)
_XcmCOInternetPOP3MaxInputAttach_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxInputAttach = _XcmCOInternetPOP3MaxInputAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 51)
)
_XcmCOInternetPOP3MaxOutputText_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxOutputText = _XcmCOInternetPOP3MaxOutputText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 52)
)
_XcmCOInternetPOP3MaxOutputAttach_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxOutputAttach = _XcmCOInternetPOP3MaxOutputAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 53)
)
_XcmCOInternetPOP3ConfirmRequest_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3ConfirmRequest = _XcmCOInternetPOP3ConfirmRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 54)
)
_XcmCOInternetPOP3ConfirmReply_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3ConfirmReply = _XcmCOInternetPOP3ConfirmReply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 55)
)
_XcmCOInternetPOP3ConfirmTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3ConfirmTimeout = _XcmCOInternetPOP3ConfirmTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 56)
)
_XcmCOInternetPOP3FeatureReply_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3FeatureReply = _XcmCOInternetPOP3FeatureReply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 57)
)
_XcmCOInternetPOP3MailAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MailAddress = _XcmCOInternetPOP3MailAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 58)
)
_XcmCOInternetPOP3MaxInFragments_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxInFragments = _XcmCOInternetPOP3MaxInFragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 59)
)
_XcmCOInternetPOP3MaxOutFragments_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxOutFragments = _XcmCOInternetPOP3MaxOutFragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 60)
)
_XcmCOInternetPOP3MaxInAttachments_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxInAttachments = _XcmCOInternetPOP3MaxInAttachments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 61)
)
_XcmCOInternetPOP3MaxOutAttachments_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxOutAttachments = _XcmCOInternetPOP3MaxOutAttachments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 62)
)
_XcmCOInternetPOP3MaxInputSize_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxInputSize = _XcmCOInternetPOP3MaxInputSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 63)
)
_XcmCOInternetPOP3MaxOutputSize_ObjectIdentity = ObjectIdentity
xcmCOInternetPOP3MaxOutputSize = _XcmCOInternetPOP3MaxOutputSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1514, 64)
)
_XcmCOInternetIMAP4_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4 = _XcmCOInternetIMAP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515)
)
_XcmCOInternetIMAP4HostName_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4HostName = _XcmCOInternetIMAP4HostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 1)
)
_XcmCOInternetIMAP4HostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4HostAddress = _XcmCOInternetIMAP4HostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 2)
)
_XcmCOInternetIMAP4PollInterval_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4PollInterval = _XcmCOInternetIMAP4PollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 4)
)
_XcmCOInternetIMAP4Subject_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4Subject = _XcmCOInternetIMAP4Subject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 44)
)
_XcmCOInternetIMAP4SignatureLine_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4SignatureLine = _XcmCOInternetIMAP4SignatureLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 45)
)
_XcmCOInternetIMAP4UserName_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4UserName = _XcmCOInternetIMAP4UserName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 47)
)
_XcmCOInternetIMAP4Password_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4Password = _XcmCOInternetIMAP4Password_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 48)
)
_XcmCOInternetIMAP4MaxInputText_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxInputText = _XcmCOInternetIMAP4MaxInputText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 50)
)
_XcmCOInternetIMAP4MaxInputAttach_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxInputAttach = _XcmCOInternetIMAP4MaxInputAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 51)
)
_XcmCOInternetIMAP4MaxOutputText_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxOutputText = _XcmCOInternetIMAP4MaxOutputText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 52)
)
_XcmCOInternetIMAP4MaxOutputAttach_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxOutputAttach = _XcmCOInternetIMAP4MaxOutputAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 53)
)
_XcmCOInternetIMAP4ConfirmRequest_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4ConfirmRequest = _XcmCOInternetIMAP4ConfirmRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 54)
)
_XcmCOInternetIMAP4ConfirmReply_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4ConfirmReply = _XcmCOInternetIMAP4ConfirmReply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 55)
)
_XcmCOInternetIMAP4ConfirmTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4ConfirmTimeout = _XcmCOInternetIMAP4ConfirmTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 56)
)
_XcmCOInternetIMAP4FeatureReply_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4FeatureReply = _XcmCOInternetIMAP4FeatureReply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 57)
)
_XcmCOInternetIMAP4MailAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MailAddress = _XcmCOInternetIMAP4MailAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 58)
)
_XcmCOInternetIMAP4MaxInFragments_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxInFragments = _XcmCOInternetIMAP4MaxInFragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 59)
)
_XcmCOInternetIMAP4MaxOutFragments_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxOutFragments = _XcmCOInternetIMAP4MaxOutFragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 60)
)
_XcmCOInternetIMAP4MaxInAttachments_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxInAttachments = _XcmCOInternetIMAP4MaxInAttachments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 61)
)
_XcmCOInternetIMAP4MaxOutAttachments_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxOutAttachments = _XcmCOInternetIMAP4MaxOutAttachments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 62)
)
_XcmCOInternetIMAP4MaxInputSize_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxInputSize = _XcmCOInternetIMAP4MaxInputSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 63)
)
_XcmCOInternetIMAP4MaxOutputSize_ObjectIdentity = ObjectIdentity
xcmCOInternetIMAP4MaxOutputSize = _XcmCOInternetIMAP4MaxOutputSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1515, 64)
)
_XcmCOInternetFax_ObjectIdentity = ObjectIdentity
xcmCOInternetFax = _XcmCOInternetFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1516)
)
_XcmCOInternetNTP_ObjectIdentity = ObjectIdentity
xcmCOInternetNTP = _XcmCOInternetNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517)
)
_XcmCOInternetNTPHostName_ObjectIdentity = ObjectIdentity
xcmCOInternetNTPHostName = _XcmCOInternetNTPHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517, 1)
)
_XcmCOInternetNTPHostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetNTPHostAddress = _XcmCOInternetNTPHostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517, 2)
)
_XcmCOInternetNTPv6HostAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetNTPv6HostAddress = _XcmCOInternetNTPv6HostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517, 3)
)
_XcmCOInternetNTPPort_ObjectIdentity = ObjectIdentity
xcmCOInternetNTPPort = _XcmCOInternetNTPPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517, 4)
)
_XcmCOInternetNTPGMTOffset_ObjectIdentity = ObjectIdentity
xcmCOInternetNTPGMTOffset = _XcmCOInternetNTPGMTOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517, 5)
)
_XcmCOInternetNTPPollInterval_ObjectIdentity = ObjectIdentity
xcmCOInternetNTPPollInterval = _XcmCOInternetNTPPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517, 6)
)
_XcmCOInternetNTPSkewTime_ObjectIdentity = ObjectIdentity
xcmCOInternetNTPSkewTime = _XcmCOInternetNTPSkewTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1517, 7)
)
_XcmCOInternetSFTP_ObjectIdentity = ObjectIdentity
xcmCOInternetSFTP = _XcmCOInternetSFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1518)
)
_XcmCOInternetWINS_ObjectIdentity = ObjectIdentity
xcmCOInternetWINS = _XcmCOInternetWINS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1519)
)
_XcmCOInternetWINSDomainName_ObjectIdentity = ObjectIdentity
xcmCOInternetWINSDomainName = _XcmCOInternetWINSDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1519, 1)
)
_XcmCOInternetWINSLanguage_ObjectIdentity = ObjectIdentity
xcmCOInternetWINSLanguage = _XcmCOInternetWINSLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1519, 3)
)
_XcmCOInternetWINSCharset_ObjectIdentity = ObjectIdentity
xcmCOInternetWINSCharset = _XcmCOInternetWINSCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1519, 4)
)
_XcmCOInternetWINSServerName_ObjectIdentity = ObjectIdentity
xcmCOInternetWINSServerName = _XcmCOInternetWINSServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1519, 5)
)
_XcmCOInternetWINSServerAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetWINSServerAddress = _XcmCOInternetWINSServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1519, 6)
)
_XcmCOInternetWINSServerSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetWINSServerSocket = _XcmCOInternetWINSServerSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1519, 7)
)
_XcmCOInternetSunOncSuite_ObjectIdentity = ObjectIdentity
xcmCOInternetSunOncSuite = _XcmCOInternetSunOncSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1520)
)
_XcmCOInternetSunOncNIS_ObjectIdentity = ObjectIdentity
xcmCOInternetSunOncNIS = _XcmCOInternetSunOncNIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1521)
)
_XcmCOInternetSunOncPlusNIS_ObjectIdentity = ObjectIdentity
xcmCOInternetSunOncPlusNIS = _XcmCOInternetSunOncPlusNIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1522)
)
_XcmCOInternetSunOncRPC_ObjectIdentity = ObjectIdentity
xcmCOInternetSunOncRPC = _XcmCOInternetSunOncRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1523)
)
_XcmCOInternetSunOncPlusRPC_ObjectIdentity = ObjectIdentity
xcmCOInternetSunOncPlusRPC = _XcmCOInternetSunOncPlusRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1524)
)
_XcmCOInternetSunTiRPC_ObjectIdentity = ObjectIdentity
xcmCOInternetSunTiRPC = _XcmCOInternetSunTiRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1525)
)
_XcmCOInternetHTTPS_ObjectIdentity = ObjectIdentity
xcmCOInternetHTTPS = _XcmCOInternetHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1526)
)
_XcmCOInternetOsfDceSuite_ObjectIdentity = ObjectIdentity
xcmCOInternetOsfDceSuite = _XcmCOInternetOsfDceSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1530)
)
_XcmCOInternetOsfDceCDS_ObjectIdentity = ObjectIdentity
xcmCOInternetOsfDceCDS = _XcmCOInternetOsfDceCDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1531)
)
_XcmCOInternetOsfDceRPC_ObjectIdentity = ObjectIdentity
xcmCOInternetOsfDceRPC = _XcmCOInternetOsfDceRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1532)
)
_XcmCOInternetOsfDceKerberos_ObjectIdentity = ObjectIdentity
xcmCOInternetOsfDceKerberos = _XcmCOInternetOsfDceKerberos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1533)
)
_XcmCOInternetOsfDceKerberosRealm_ObjectIdentity = ObjectIdentity
xcmCOInternetOsfDceKerberosRealm = _XcmCOInternetOsfDceKerberosRealm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1533, 1)
)
_XcmCOInternetOsfDmeSuite_ObjectIdentity = ObjectIdentity
xcmCOInternetOsfDmeSuite = _XcmCOInternetOsfDmeSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1540)
)
_XcmCOInternetLDAP_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAP = _XcmCOInternetLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551)
)
_XcmCOInternetLDAPLanguage_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPLanguage = _XcmCOInternetLDAPLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 3)
)
_XcmCOInternetLDAPCharset_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPCharset = _XcmCOInternetLDAPCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 4)
)
_XcmCOInternetLDAPServerName_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPServerName = _XcmCOInternetLDAPServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 5)
)
_XcmCOInternetLDAPServerAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPServerAddress = _XcmCOInternetLDAPServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 6)
)
_XcmCOInternetLDAPServerSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPServerSocket = _XcmCOInternetLDAPServerSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 7)
)
_XcmCOInternetLDAPPollInterval_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPPollInterval = _XcmCOInternetLDAPPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 8)
)
_XcmCOInternetLDAPBindDN_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPBindDN = _XcmCOInternetLDAPBindDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 11)
)
_XcmCOInternetLDAPBindPassword_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPBindPassword = _XcmCOInternetLDAPBindPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 12)
)
_XcmCOInternetLDAPBaseDN_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPBaseDN = _XcmCOInternetLDAPBaseDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 13)
)
_XcmCOInternetLDAPPrinterName_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPPrinterName = _XcmCOInternetLDAPPrinterName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 21)
)
_XcmCOInternetLDAPPrinterClass_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPPrinterClass = _XcmCOInternetLDAPPrinterClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 22)
)
_XcmCOInternetLDAPAttributeName_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPAttributeName = _XcmCOInternetLDAPAttributeName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 31)
)
_XcmCOInternetLDAPAttributeType_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPAttributeType = _XcmCOInternetLDAPAttributeType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 32)
)
_XcmCOInternetLDAPAttributeInt_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPAttributeInt = _XcmCOInternetLDAPAttributeInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 33)
)
_XcmCOInternetLDAPAttributeStr_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPAttributeStr = _XcmCOInternetLDAPAttributeStr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 34)
)
_XcmCOInternetLDAPMaxSearchResult_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPMaxSearchResult = _XcmCOInternetLDAPMaxSearchResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 35)
)
_XcmCOInternetLDAPSearchTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetLDAPSearchTimeout = _XcmCOInternetLDAPSearchTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1551, 36)
)
_XcmCOInternetCLDAP_ObjectIdentity = ObjectIdentity
xcmCOInternetCLDAP = _XcmCOInternetCLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1552)
)
_XcmCOInternetSalutation_ObjectIdentity = ObjectIdentity
xcmCOInternetSalutation = _XcmCOInternetSalutation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1561)
)
_XcmCOInternetUpnpSuite_ObjectIdentity = ObjectIdentity
xcmCOInternetUpnpSuite = _XcmCOInternetUpnpSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1570)
)
_XcmCOInternetUpnpSSDP_ObjectIdentity = ObjectIdentity
xcmCOInternetUpnpSSDP = _XcmCOInternetUpnpSSDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1571)
)
_XcmCOInternetSSDPCacheTimeout_ObjectIdentity = ObjectIdentity
xcmCOInternetSSDPCacheTimeout = _XcmCOInternetSSDPCacheTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1571, 1)
)
_XcmCOInternetSSDPTimeToLive_ObjectIdentity = ObjectIdentity
xcmCOInternetSSDPTimeToLive = _XcmCOInternetSSDPTimeToLive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1571, 2)
)
_XcmCOInternetSSDPServerVersion_ObjectIdentity = ObjectIdentity
xcmCOInternetSSDPServerVersion = _XcmCOInternetSSDPServerVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1571, 3)
)
_XcmCOInternetUpnpGENA_ObjectIdentity = ObjectIdentity
xcmCOInternetUpnpGENA = _XcmCOInternetUpnpGENA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1572)
)
_XcmCOInternetSLP_ObjectIdentity = ObjectIdentity
xcmCOInternetSLP = _XcmCOInternetSLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591)
)
_XcmCOInternetSLPVersion_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPVersion = _XcmCOInternetSLPVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 1)
)
_XcmCOInternetSLPLanguage_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPLanguage = _XcmCOInternetSLPLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 3)
)
_XcmCOInternetSLPCharset_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPCharset = _XcmCOInternetSLPCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 4)
)
_XcmCOInternetSLPServerName_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPServerName = _XcmCOInternetSLPServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 5)
)
_XcmCOInternetSLPServerAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPServerAddress = _XcmCOInternetSLPServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 6)
)
_XcmCOInternetSLPServerSocket_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPServerSocket = _XcmCOInternetSLPServerSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 7)
)
_XcmCOInternetSLPPollInterval_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPPollInterval = _XcmCOInternetSLPPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 8)
)
_XcmCOInternetSLPMaxMulticastTime_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPMaxMulticastTime = _XcmCOInternetSLPMaxMulticastTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 10)
)
_XcmCOInternetSLPDAFindStartWait_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPDAFindStartWait = _XcmCOInternetSLPDAFindStartWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 11)
)
_XcmCOInternetSLPInitialRetryWait_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPInitialRetryWait = _XcmCOInternetSLPInitialRetryWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 12)
)
_XcmCOInternetSLPMaxUnicastTime_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPMaxUnicastTime = _XcmCOInternetSLPMaxUnicastTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 13)
)
_XcmCOInternetSLPDAHeartbeatTime_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPDAHeartbeatTime = _XcmCOInternetSLPDAHeartbeatTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 14)
)
_XcmCOInternetSLPDAFindActiveWait_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPDAFindActiveWait = _XcmCOInternetSLPDAFindActiveWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 15)
)
_XcmCOInternetSLPRegPassiveWait_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPRegPassiveWait = _XcmCOInternetSLPRegPassiveWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 16)
)
_XcmCOInternetSLPRegActiveWait_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPRegActiveWait = _XcmCOInternetSLPRegActiveWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 17)
)
_XcmCOInternetSLPCloseConnWait_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPCloseConnWait = _XcmCOInternetSLPCloseConnWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 18)
)
_XcmCOInternetSLPCacheReplyTime_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPCacheReplyTime = _XcmCOInternetSLPCacheReplyTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 20)
)
_XcmCOInternetSLPMaxRegLifetime_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPMaxRegLifetime = _XcmCOInternetSLPMaxRegLifetime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 21)
)
_XcmCOInternetSLPDAFindRetryWait_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPDAFindRetryWait = _XcmCOInternetSLPDAFindRetryWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 22)
)
_XcmCOInternetSLPMaxDARequestTime_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPMaxDARequestTime = _XcmCOInternetSLPMaxDARequestTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 23)
)
_XcmCOInternetSLPMulticastEnable_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPMulticastEnable = _XcmCOInternetSLPMulticastEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 30)
)
_XcmCOInternetSLPMulticastRadius_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPMulticastRadius = _XcmCOInternetSLPMulticastRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 31)
)
_XcmCOInternetSLPPathMTUSize_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPPathMTUSize = _XcmCOInternetSLPPathMTUSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 32)
)
_XcmCOInternetSLPScopeName_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPScopeName = _XcmCOInternetSLPScopeName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 40)
)
_XcmCOInternetSLPScopeKey_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPScopeKey = _XcmCOInternetSLPScopeKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 41)
)
_XcmCOInternetSLPAttributesEnable_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPAttributesEnable = _XcmCOInternetSLPAttributesEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1591, 50)
)
_XcmCOInternetSLPv1_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPv1 = _XcmCOInternetSLPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1592)
)
_XcmCOInternetSLPv2_ObjectIdentity = ObjectIdentity
xcmCOInternetSLPv2 = _XcmCOInternetSLPv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1593)
)
_XcmCOInternetWSDSuite_ObjectIdentity = ObjectIdentity
xcmCOInternetWSDSuite = _XcmCOInternetWSDSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595)
)
_XcmCOInternetWSDiscovery_ObjectIdentity = ObjectIdentity
xcmCOInternetWSDiscovery = _XcmCOInternetWSDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595, 1)
)
_XcmCOInternetWSDiscoveryMulticast_ObjectIdentity = ObjectIdentity
xcmCOInternetWSDiscoveryMulticast = _XcmCOInternetWSDiscoveryMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595, 1, 1)
)
_XcmCOInternetWSDiscoveryPort_ObjectIdentity = ObjectIdentity
xcmCOInternetWSDiscoveryPort = _XcmCOInternetWSDiscoveryPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595, 1, 2)
)
_XcmCOInternetWSXResourcePort_ObjectIdentity = ObjectIdentity
xcmCOInternetWSXResourcePort = _XcmCOInternetWSXResourcePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595, 2)
)
_XcmCOInternetWSPrintPort_ObjectIdentity = ObjectIdentity
xcmCOInternetWSPrintPort = _XcmCOInternetWSPrintPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595, 3)
)
_XcmCOInternetWSScanPort_ObjectIdentity = ObjectIdentity
xcmCOInternetWSScanPort = _XcmCOInternetWSScanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595, 4)
)
_XcmCOInternetWSTransferPort_ObjectIdentity = ObjectIdentity
xcmCOInternetWSTransferPort = _XcmCOInternetWSTransferPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1595, 5)
)
_XcmCOInternetDeallocateAllDynamicResources_ObjectIdentity = ObjectIdentity
xcmCOInternetDeallocateAllDynamicResources = _XcmCOInternetDeallocateAllDynamicResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1600)
)
_XcmCOInternetApplications_ObjectIdentity = ObjectIdentity
xcmCOInternetApplications = _XcmCOInternetApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1700)
)
_XcmCOInternetDHCPv6_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPv6 = _XcmCOInternetDHCPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1800)
)
_XcmCOInternetDHCPv6ConfigState_ObjectIdentity = ObjectIdentity
xcmCOInternetDHCPv6ConfigState = _XcmCOInternetDHCPv6ConfigState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1800, 1)
)
_XcmCOInternetDNSv6_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSv6 = _XcmCOInternetDNSv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1801)
)
_XcmCOInternetDNSv6DomainName_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSv6DomainName = _XcmCOInternetDNSv6DomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1801, 1)
)
_XcmCOInternetDNSv6ServerAddress_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSv6ServerAddress = _XcmCOInternetDNSv6ServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1801, 2)
)
_XcmCOInternetDNSv6DynamicUpdate_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSv6DynamicUpdate = _XcmCOInternetDNSv6DynamicUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1801, 3)
)
_XcmCOInternetDNSv6ResolutionPolicy_ObjectIdentity = ObjectIdentity
xcmCOInternetDNSv6ResolutionPolicy = _XcmCOInternetDNSv6ResolutionPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1801, 4)
)
_XcmCOInternetIPv6DeallocateAllDynamicResources_ObjectIdentity = ObjectIdentity
xcmCOInternetIPv6DeallocateAllDynamicResources = _XcmCOInternetIPv6DeallocateAllDynamicResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 14, 1802)
)
_XcmCOAppletalkSuite_ObjectIdentity = ObjectIdentity
xcmCOAppletalkSuite = _XcmCOAppletalkSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18)
)
_XcmCOAppletalkDatalinks_ObjectIdentity = ObjectIdentity
xcmCOAppletalkDatalinks = _XcmCOAppletalkDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1200)
)
_XcmCOAppletalkLLAP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkLLAP = _XcmCOAppletalkLLAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1201)
)
_XcmCOAppletalkELAP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkELAP = _XcmCOAppletalkELAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1202)
)
_XcmCOAppletalkTLAP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkTLAP = _XcmCOAppletalkTLAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1203)
)
_XcmCOAppletalkPhase_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPhase = _XcmCOAppletalkPhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1211)
)
_XcmCOAppletalkDDP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkDDP = _XcmCOAppletalkDDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1301)
)
_XcmCOAppletalkDDPAddress_ObjectIdentity = ObjectIdentity
xcmCOAppletalkDDPAddress = _XcmCOAppletalkDDPAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1301, 1)
)
_XcmCOAppletalkDDPSocketAddress_ObjectIdentity = ObjectIdentity
xcmCOAppletalkDDPSocketAddress = _XcmCOAppletalkDDPSocketAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1301, 1, 1)
)
_XcmCOAppletalkDDPDatalinks_ObjectIdentity = ObjectIdentity
xcmCOAppletalkDDPDatalinks = _XcmCOAppletalkDDPDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1301, 12)
)
_XcmCOAppletalkAARP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkAARP = _XcmCOAppletalkAARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1303)
)
_XcmCOAppletalkTransports_ObjectIdentity = ObjectIdentity
xcmCOAppletalkTransports = _XcmCOAppletalkTransports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1400)
)
_XcmCOAppletalkATP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkATP = _XcmCOAppletalkATP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1401)
)
_XcmCOAppletalkADSP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkADSP = _XcmCOAppletalkADSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1402)
)
_XcmCOAppletalkRTMP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkRTMP = _XcmCOAppletalkRTMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1403)
)
_XcmCOAppletalkAEP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkAEP = _XcmCOAppletalkAEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1404)
)
_XcmCOAppletalkNBP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBP = _XcmCOAppletalkNBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405)
)
_XcmCOAppletalkNBPHostName_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPHostName = _XcmCOAppletalkNBPHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 1)
)
_XcmCOAppletalkNBPLanguage_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPLanguage = _XcmCOAppletalkNBPLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 3)
)
_XcmCOAppletalkNBPCharset_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPCharset = _XcmCOAppletalkNBPCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 4)
)
_XcmCOAppletalkNBPObject_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPObject = _XcmCOAppletalkNBPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 11)
)
_XcmCOAppletalkNBPType_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPType = _XcmCOAppletalkNBPType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 12)
)
_XcmCOAppletalkNBPZone_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPZone = _XcmCOAppletalkNBPZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 13)
)
_XcmCOAppletalkNBPNetwork_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPNetwork = _XcmCOAppletalkNBPNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 21)
)
_XcmCOAppletalkNBPNode_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPNode = _XcmCOAppletalkNBPNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 22)
)
_XcmCOAppletalkNBPSocket_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPSocket = _XcmCOAppletalkNBPSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 23)
)
_XcmCOAppletalkNBPZoneToNetworks_ObjectIdentity = ObjectIdentity
xcmCOAppletalkNBPZoneToNetworks = _XcmCOAppletalkNBPZoneToNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1405, 31)
)
_XcmCOAppletalkASP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkASP = _XcmCOAppletalkASP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1501)
)
_XcmCOAppletalkZIP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkZIP = _XcmCOAppletalkZIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1502)
)
_XcmCOAppletalkPAP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAP = _XcmCOAppletalkPAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503)
)
_XcmCOAppletalkPAPHostName_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPHostName = _XcmCOAppletalkPAPHostName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 1)
)
_XcmCOAppletalkPAPHostAddress_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPHostAddress = _XcmCOAppletalkPAPHostAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 2)
)
_XcmCOAppletalkPAPListenSocket_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPListenSocket = _XcmCOAppletalkPAPListenSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 3)
)
_XcmCOAppletalkPAPMaxClients_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPMaxClients = _XcmCOAppletalkPAPMaxClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 4)
)
_XcmCOAppletalkPAPMaxPrinters_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPMaxPrinters = _XcmCOAppletalkPAPMaxPrinters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 5)
)
_XcmCOAppletalkPAPObject_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPObject = _XcmCOAppletalkPAPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 11)
)
_XcmCOAppletalkPAPType_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPType = _XcmCOAppletalkPAPType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 12)
)
_XcmCOAppletalkPAPZone_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPZone = _XcmCOAppletalkPAPZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 13)
)
_XcmCOAppletalkPAPNetwork_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPNetwork = _XcmCOAppletalkPAPNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 21)
)
_XcmCOAppletalkPAPNode_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPNode = _XcmCOAppletalkPAPNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 22)
)
_XcmCOAppletalkPAPSpool_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPSpool = _XcmCOAppletalkPAPSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 31)
)
_XcmCOAppletalkPAPMaxSpool_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPMaxSpool = _XcmCOAppletalkPAPMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 32)
)
_XcmCOAppletalkPAPJobTimeout_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPJobTimeout = _XcmCOAppletalkPAPJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 40)
)
_XcmCOAppletalkPAPAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPAutoSwitch = _XcmCOAppletalkPAPAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 41)
)
_XcmCOAppletalkPAPBinaryPS_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPBinaryPS = _XcmCOAppletalkPAPBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 42)
)
_XcmCOAppletalkPAPDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPAPDefaultPDL = _XcmCOAppletalkPAPDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1503, 43)
)
_XcmCOAppletalkSNMP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkSNMP = _XcmCOAppletalkSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1510)
)
_XcmCOAppletalkSNMPv1_ObjectIdentity = ObjectIdentity
xcmCOAppletalkSNMPv1 = _XcmCOAppletalkSNMPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1511)
)
_XcmCOAppletalkSNMPv2_ObjectIdentity = ObjectIdentity
xcmCOAppletalkSNMPv2 = _XcmCOAppletalkSNMPv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1512)
)
_XcmCOAppletalkSNMPv3_ObjectIdentity = ObjectIdentity
xcmCOAppletalkSNMPv3 = _XcmCOAppletalkSNMPv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1513)
)
_XcmCOAppletalkAFP_ObjectIdentity = ObjectIdentity
xcmCOAppletalkAFP = _XcmCOAppletalkAFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1601)
)
_XcmCOAppletalkPS_ObjectIdentity = ObjectIdentity
xcmCOAppletalkPS = _XcmCOAppletalkPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1602)
)
_XcmCOAppletalkApplications_ObjectIdentity = ObjectIdentity
xcmCOAppletalkApplications = _XcmCOAppletalkApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 18, 1700)
)
_XcmCONetwareSuite_ObjectIdentity = ObjectIdentity
xcmCONetwareSuite = _XcmCONetwareSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19)
)
_XcmCONetwareDatalinks_ObjectIdentity = ObjectIdentity
xcmCONetwareDatalinks = _XcmCONetwareDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1200)
)
_XcmCONetwareIPX_ObjectIdentity = ObjectIdentity
xcmCONetwareIPX = _XcmCONetwareIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1301)
)
_XcmCONetwareIPXAddress_ObjectIdentity = ObjectIdentity
xcmCONetwareIPXAddress = _XcmCONetwareIPXAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1301, 1)
)
_XcmCONetwareIPXSocketAddress_ObjectIdentity = ObjectIdentity
xcmCONetwareIPXSocketAddress = _XcmCONetwareIPXSocketAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1301, 1, 1)
)
_XcmCONetwareIPXDatalinks_ObjectIdentity = ObjectIdentity
xcmCONetwareIPXDatalinks = _XcmCONetwareIPXDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1301, 12)
)
_XcmCONetwareIP_ObjectIdentity = ObjectIdentity
xcmCONetwareIP = _XcmCONetwareIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1302)
)
_XcmCONetwareTransports_ObjectIdentity = ObjectIdentity
xcmCONetwareTransports = _XcmCONetwareTransports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1400)
)
_XcmCONetwareSPX_ObjectIdentity = ObjectIdentity
xcmCONetwareSPX = _XcmCONetwareSPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1402)
)
_XcmCONetwareRIP_ObjectIdentity = ObjectIdentity
xcmCONetwareRIP = _XcmCONetwareRIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1403)
)
_XcmCONetwareEcho_ObjectIdentity = ObjectIdentity
xcmCONetwareEcho = _XcmCONetwareEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1404)
)
_XcmCONetwareNCP_ObjectIdentity = ObjectIdentity
xcmCONetwareNCP = _XcmCONetwareNCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1501)
)
_XcmCONetwareNetbios_ObjectIdentity = ObjectIdentity
xcmCONetwareNetbios = _XcmCONetwareNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1502)
)
_XcmCONetwarePServer_ObjectIdentity = ObjectIdentity
xcmCONetwarePServer = _XcmCONetwarePServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503)
)
_XcmCONetwarePServerName_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerName = _XcmCONetwarePServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 1)
)
_XcmCONetwarePServerPassword_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerPassword = _XcmCONetwarePServerPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 2)
)
_XcmCONetwarePServerQueueName_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerQueueName = _XcmCONetwarePServerQueueName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 3)
)
_XcmCONetwarePServerPollInterval_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerPollInterval = _XcmCONetwarePServerPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 4)
)
_XcmCONetwarePServerFindFServer_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerFindFServer = _XcmCONetwarePServerFindFServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 5)
)
_XcmCONetwarePServerMaxFServers_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerMaxFServers = _XcmCONetwarePServerMaxFServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 6)
)
_XcmCONetwarePServerNotify_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerNotify = _XcmCONetwarePServerNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 7)
)
_XcmCONetwarePServerNotifyLocale_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerNotifyLocale = _XcmCONetwarePServerNotifyLocale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 7, 1)
)
_XcmCONetwarePServerMaxPrinters_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerMaxPrinters = _XcmCONetwarePServerMaxPrinters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 8)
)
_XcmCONetwarePServerSuspendPoll_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerSuspendPoll = _XcmCONetwarePServerSuspendPoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 9)
)
_XcmCONetwarePServerSuspendPollInterval_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerSuspendPollInterval = _XcmCONetwarePServerSuspendPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 10)
)
_XcmCONetwarePServerSpool_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerSpool = _XcmCONetwarePServerSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 31)
)
_XcmCONetwarePServerMaxSpool_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerMaxSpool = _XcmCONetwarePServerMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 32)
)
_XcmCONetwarePServerJobTimeout_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerJobTimeout = _XcmCONetwarePServerJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 40)
)
_XcmCONetwarePServerAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerAutoSwitch = _XcmCONetwarePServerAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 41)
)
_XcmCONetwarePServerBinaryPS_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerBinaryPS = _XcmCONetwarePServerBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 42)
)
_XcmCONetwarePServerDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerDefaultPDL = _XcmCONetwarePServerDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 43)
)
_XcmCONetwarePServerConfigTimeout_ObjectIdentity = ObjectIdentity
xcmCONetwarePServerConfigTimeout = _XcmCONetwarePServerConfigTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1503, 50)
)
_XcmCONetwareFServer_ObjectIdentity = ObjectIdentity
xcmCONetwareFServer = _XcmCONetwareFServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1504)
)
_XcmCONetwareFServerName_ObjectIdentity = ObjectIdentity
xcmCONetwareFServerName = _XcmCONetwareFServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1504, 1)
)
_XcmCONetwareFServerPassword_ObjectIdentity = ObjectIdentity
xcmCONetwareFServerPassword = _XcmCONetwareFServerPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1504, 2)
)
_XcmCONetwareFServerAddress_ObjectIdentity = ObjectIdentity
xcmCONetwareFServerAddress = _XcmCONetwareFServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1504, 3)
)
_XcmCONetwareMHS_ObjectIdentity = ObjectIdentity
xcmCONetwareMHS = _XcmCONetwareMHS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1505)
)
_XcmCONetwareBindery_ObjectIdentity = ObjectIdentity
xcmCONetwareBindery = _XcmCONetwareBindery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1507)
)
_XcmCONetwareBinderyLanguage_ObjectIdentity = ObjectIdentity
xcmCONetwareBinderyLanguage = _XcmCONetwareBinderyLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1507, 3)
)
_XcmCONetwareBinderyCharset_ObjectIdentity = ObjectIdentity
xcmCONetwareBinderyCharset = _XcmCONetwareBinderyCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1507, 4)
)
_XcmCONetwareNDS_ObjectIdentity = ObjectIdentity
xcmCONetwareNDS = _XcmCONetwareNDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1508)
)
_XcmCONetwareNDSTreeName_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSTreeName = _XcmCONetwareNDSTreeName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1508, 1)
)
_XcmCONetwareNDSContext_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSContext = _XcmCONetwareNDSContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1508, 2)
)
_XcmCONetwareNDSLanguage_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSLanguage = _XcmCONetwareNDSLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1508, 3)
)
_XcmCONetwareNDSCharset_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSCharset = _XcmCONetwareNDSCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1508, 4)
)
_XcmCONetwareRPrinter_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinter = _XcmCONetwareRPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509)
)
_XcmCONetwareRPrinterName_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinterName = _XcmCONetwareRPrinterName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509, 1)
)
_XcmCONetwareRPrinterNumber_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinterNumber = _XcmCONetwareRPrinterNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509, 2)
)
_XcmCONetwareRPrinterPollInterval_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinterPollInterval = _XcmCONetwareRPrinterPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509, 3)
)
_XcmCONetwareRPrinterJobTimeout_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinterJobTimeout = _XcmCONetwareRPrinterJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509, 40)
)
_XcmCONetwareRPrinterAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinterAutoSwitch = _XcmCONetwareRPrinterAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509, 41)
)
_XcmCONetwareRPrinterBinaryPS_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinterBinaryPS = _XcmCONetwareRPrinterBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509, 42)
)
_XcmCONetwareRPrinterDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCONetwareRPrinterDefaultPDL = _XcmCONetwareRPrinterDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1509, 43)
)
_XcmCONetwareSNMP_ObjectIdentity = ObjectIdentity
xcmCONetwareSNMP = _XcmCONetwareSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1510)
)
_XcmCONetwareSNMPv1_ObjectIdentity = ObjectIdentity
xcmCONetwareSNMPv1 = _XcmCONetwareSNMPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1511)
)
_XcmCONetwareSNMPv2_ObjectIdentity = ObjectIdentity
xcmCONetwareSNMPv2 = _XcmCONetwareSNMPv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1512)
)
_XcmCONetwareSNMPv3_ObjectIdentity = ObjectIdentity
xcmCONetwareSNMPv3 = _XcmCONetwareSNMPv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1513)
)
_XcmCONetwareSAP_ObjectIdentity = ObjectIdentity
xcmCONetwareSAP = _XcmCONetwareSAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591)
)
_XcmCONetwareSAPInterval_ObjectIdentity = ObjectIdentity
xcmCONetwareSAPInterval = _XcmCONetwareSAPInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591, 1)
)
_XcmCONetwareSAPNumber_ObjectIdentity = ObjectIdentity
xcmCONetwareSAPNumber = _XcmCONetwareSAPNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591, 2)
)
_XcmCONetwareSAPValueString_ObjectIdentity = ObjectIdentity
xcmCONetwareSAPValueString = _XcmCONetwareSAPValueString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591, 3)
)
_XcmCONetwareSAPUnitName_ObjectIdentity = ObjectIdentity
xcmCONetwareSAPUnitName = _XcmCONetwareSAPUnitName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591, 4)
)
_XcmCONetwareSAPFormatID_ObjectIdentity = ObjectIdentity
xcmCONetwareSAPFormatID = _XcmCONetwareSAPFormatID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591, 5)
)
_XcmCONetwareSAPSuspend_ObjectIdentity = ObjectIdentity
xcmCONetwareSAPSuspend = _XcmCONetwareSAPSuspend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591, 6)
)
_XcmCONetwareSAPSuspendInterval_ObjectIdentity = ObjectIdentity
xcmCONetwareSAPSuspendInterval = _XcmCONetwareSAPSuspendInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1591, 7)
)
_XcmCONetwareNDSIP_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSIP = _XcmCONetwareNDSIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1600)
)
_XcmCONetwareNDSIPHostname_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSIPHostname = _XcmCONetwareNDSIPHostname_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1600, 1)
)
_XcmCONetwareNDSIPAddress_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSIPAddress = _XcmCONetwareNDSIPAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1600, 2)
)
_XcmCONetwareNDSIPUseHostname_ObjectIdentity = ObjectIdentity
xcmCONetwareNDSIPUseHostname = _XcmCONetwareNDSIPUseHostname_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1600, 3)
)
_XcmCONetwareApplications_ObjectIdentity = ObjectIdentity
xcmCONetwareApplications = _XcmCONetwareApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 19, 1700)
)
_XcmCOVinesSuite_ObjectIdentity = ObjectIdentity
xcmCOVinesSuite = _XcmCOVinesSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20)
)
_XcmCOVinesDatalinks_ObjectIdentity = ObjectIdentity
xcmCOVinesDatalinks = _XcmCOVinesDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1200)
)
_XcmCOVinesVIP_ObjectIdentity = ObjectIdentity
xcmCOVinesVIP = _XcmCOVinesVIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1301)
)
_XcmCOVinesVICP_ObjectIdentity = ObjectIdentity
xcmCOVinesVICP = _XcmCOVinesVICP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1302)
)
_XcmCOVinesVARP_ObjectIdentity = ObjectIdentity
xcmCOVinesVARP = _XcmCOVinesVARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1303)
)
_XcmCOVinesIP_ObjectIdentity = ObjectIdentity
xcmCOVinesIP = _XcmCOVinesIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1311)
)
_XcmCOVinesICMP_ObjectIdentity = ObjectIdentity
xcmCOVinesICMP = _XcmCOVinesICMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1312)
)
_XcmCOVinesARP_ObjectIdentity = ObjectIdentity
xcmCOVinesARP = _XcmCOVinesARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1313)
)
_XcmCOVinesVRTP_ObjectIdentity = ObjectIdentity
xcmCOVinesVRTP = _XcmCOVinesVRTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1314)
)
_XcmCOVinesTransports_ObjectIdentity = ObjectIdentity
xcmCOVinesTransports = _XcmCOVinesTransports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1400)
)
_XcmCOVinesVIPC_ObjectIdentity = ObjectIdentity
xcmCOVinesVIPC = _XcmCOVinesVIPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1401)
)
_XcmCOVinesVSPP_ObjectIdentity = ObjectIdentity
xcmCOVinesVSPP = _XcmCOVinesVSPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1402)
)
_XcmCOVinesUDP_ObjectIdentity = ObjectIdentity
xcmCOVinesUDP = _XcmCOVinesUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1411)
)
_XcmCOVinesTCP_ObjectIdentity = ObjectIdentity
xcmCOVinesTCP = _XcmCOVinesTCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1412)
)
_XcmCOVinesNetRPC_ObjectIdentity = ObjectIdentity
xcmCOVinesNetRPC = _XcmCOVinesNetRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1501)
)
_XcmCOVinesSocket_ObjectIdentity = ObjectIdentity
xcmCOVinesSocket = _XcmCOVinesSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1502)
)
_XcmCOVinesNetbios_ObjectIdentity = ObjectIdentity
xcmCOVinesNetbios = _XcmCOVinesNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1503)
)
_XcmCOVinesApplications_ObjectIdentity = ObjectIdentity
xcmCOVinesApplications = _XcmCOVinesApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1700)
)
_XcmCOVinesPrint_ObjectIdentity = ObjectIdentity
xcmCOVinesPrint = _XcmCOVinesPrint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701)
)
_XcmCOVinesPrintName_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintName = _XcmCOVinesPrintName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 1)
)
_XcmCOVinesPrintPassword_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintPassword = _XcmCOVinesPrintPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 2)
)
_XcmCOVinesPrintPollInterval_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintPollInterval = _XcmCOVinesPrintPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 4)
)
_XcmCOVinesPrintMaxServers_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintMaxServers = _XcmCOVinesPrintMaxServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 5)
)
_XcmCOVinesPrintServerName_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintServerName = _XcmCOVinesPrintServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 6)
)
_XcmCOVinesPrintSpool_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintSpool = _XcmCOVinesPrintSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 31)
)
_XcmCOVinesPrintMaxSpool_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintMaxSpool = _XcmCOVinesPrintMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 32)
)
_XcmCOVinesPrintJobTimeout_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintJobTimeout = _XcmCOVinesPrintJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 40)
)
_XcmCOVinesPrintAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintAutoSwitch = _XcmCOVinesPrintAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 41)
)
_XcmCOVinesPrintBinaryPS_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintBinaryPS = _XcmCOVinesPrintBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 42)
)
_XcmCOVinesPrintDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCOVinesPrintDefaultPDL = _XcmCOVinesPrintDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1701, 43)
)
_XcmCOVinesFiling_ObjectIdentity = ObjectIdentity
xcmCOVinesFiling = _XcmCOVinesFiling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1702)
)
_XcmCOVinesMail_ObjectIdentity = ObjectIdentity
xcmCOVinesMail = _XcmCOVinesMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1703)
)
_XcmCOVinesStreetTalk_ObjectIdentity = ObjectIdentity
xcmCOVinesStreetTalk = _XcmCOVinesStreetTalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1704)
)
_XcmCOVinesStreetTalkLanguage_ObjectIdentity = ObjectIdentity
xcmCOVinesStreetTalkLanguage = _XcmCOVinesStreetTalkLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1704, 3)
)
_XcmCOVinesStreetTalkCharset_ObjectIdentity = ObjectIdentity
xcmCOVinesStreetTalkCharset = _XcmCOVinesStreetTalkCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 20, 1704, 4)
)
_XcmCONetbiosSuite_ObjectIdentity = ObjectIdentity
xcmCONetbiosSuite = _XcmCONetbiosSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25)
)
_XcmCONetbiosDatalinks_ObjectIdentity = ObjectIdentity
xcmCONetbiosDatalinks = _XcmCONetbiosDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1200)
)
_XcmCONetbiosTransports_ObjectIdentity = ObjectIdentity
xcmCONetbiosTransports = _XcmCONetbiosTransports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1400)
)
_XcmCONetbiosNBP_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBP = _XcmCONetbiosNBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501)
)
_XcmCONetbiosNBPName_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPName = _XcmCONetbiosNBPName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 1)
)
_XcmCONetbiosNBPGroupName_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPGroupName = _XcmCONetbiosNBPGroupName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 2)
)
_XcmCONetbiosNBPPassword_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPPassword = _XcmCONetbiosNBPPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 3)
)
_XcmCONetbiosNBPService_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPService = _XcmCONetbiosNBPService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 4)
)
_XcmCONetbiosNBPRemark_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPRemark = _XcmCONetbiosNBPRemark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 5)
)
_XcmCONetbiosNBPServiceRemark_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPServiceRemark = _XcmCONetbiosNBPServiceRemark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 6)
)
_XcmCONetbiosNBPIPCRemark_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPIPCRemark = _XcmCONetbiosNBPIPCRemark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 7)
)
_XcmCONetbiosNBPLanguage_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPLanguage = _XcmCONetbiosNBPLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 8)
)
_XcmCONetbiosNBPCharset_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPCharset = _XcmCONetbiosNBPCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 9)
)
_XcmCONetbiosNBPOverNetbeui_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPOverNetbeui = _XcmCONetbiosNBPOverNetbeui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 11)
)
_XcmCONetbiosNBPOverInternet_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPOverInternet = _XcmCONetbiosNBPOverInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 12)
)
_XcmCONetbiosNBPOverNetware_ObjectIdentity = ObjectIdentity
xcmCONetbiosNBPOverNetware = _XcmCONetbiosNBPOverNetware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1501, 13)
)
_XcmCONetbiosSNMP_ObjectIdentity = ObjectIdentity
xcmCONetbiosSNMP = _XcmCONetbiosSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1510)
)
_XcmCONetbiosSNMPv1_ObjectIdentity = ObjectIdentity
xcmCONetbiosSNMPv1 = _XcmCONetbiosSNMPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1511)
)
_XcmCONetbiosSNMPv2_ObjectIdentity = ObjectIdentity
xcmCONetbiosSNMPv2 = _XcmCONetbiosSNMPv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1512)
)
_XcmCONetbiosSNMPv3_ObjectIdentity = ObjectIdentity
xcmCONetbiosSNMPv3 = _XcmCONetbiosSNMPv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1513)
)
_XcmCONetbiosIntEndNode_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntEndNode = _XcmCONetbiosIntEndNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1520)
)
_XcmCONetbiosIntEndNodeAddress_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntEndNodeAddress = _XcmCONetbiosIntEndNodeAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1520, 1)
)
_XcmCONetbiosIntEndNodeSource_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntEndNodeSource = _XcmCONetbiosIntEndNodeSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1520, 2)
)
_XcmCONetbiosIntNodeType_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntNodeType = _XcmCONetbiosIntNodeType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1520, 3)
)
_XcmCONetbiosIntNodeTypeSource_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntNodeTypeSource = _XcmCONetbiosIntNodeTypeSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1520, 4)
)
_XcmCONetbiosIntNodeScope_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntNodeScope = _XcmCONetbiosIntNodeScope_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1520, 5)
)
_XcmCONetbiosIntNodeScopeSource_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntNodeScopeSource = _XcmCONetbiosIntNodeScopeSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1520, 6)
)
_XcmCONetbiosIntNameServer_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntNameServer = _XcmCONetbiosIntNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1521)
)
_XcmCONetbiosIntNameServerAddress_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntNameServerAddress = _XcmCONetbiosIntNameServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1521, 1)
)
_XcmCONetbiosIntNameServerSource_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntNameServerSource = _XcmCONetbiosIntNameServerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1521, 2)
)
_XcmCONetbiosIntDistServer_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntDistServer = _XcmCONetbiosIntDistServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1522)
)
_XcmCONetbiosIntDistServerAddress_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntDistServerAddress = _XcmCONetbiosIntDistServerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1522, 1)
)
_XcmCONetbiosIntDistServerSource_ObjectIdentity = ObjectIdentity
xcmCONetbiosIntDistServerSource = _XcmCONetbiosIntDistServerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1522, 2)
)
_XcmCONetbiosSAP_ObjectIdentity = ObjectIdentity
xcmCONetbiosSAP = _XcmCONetbiosSAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1591)
)
_XcmCONetbiosSAPInterval_ObjectIdentity = ObjectIdentity
xcmCONetbiosSAPInterval = _XcmCONetbiosSAPInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1591, 1)
)
_XcmCONetbiosApplications_ObjectIdentity = ObjectIdentity
xcmCONetbiosApplications = _XcmCONetbiosApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1700)
)
_XcmCONetbiosSMB_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMB = _XcmCONetbiosSMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1701)
)
_XcmCONetbiosSMBPClient_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClient = _XcmCONetbiosSMBPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702)
)
_XcmCONetbiosSMBPClientMaxConns_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClientMaxConns = _XcmCONetbiosSMBPClientMaxConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702, 4)
)
_XcmCONetbiosSMBPClientSpool_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClientSpool = _XcmCONetbiosSMBPClientSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702, 31)
)
_XcmCONetbiosSMBPClientMaxSpool_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClientMaxSpool = _XcmCONetbiosSMBPClientMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702, 32)
)
_XcmCONetbiosSMBPClientJobTimeout_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClientJobTimeout = _XcmCONetbiosSMBPClientJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702, 40)
)
_XcmCONetbiosSMBPClientAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClientAutoSwitch = _XcmCONetbiosSMBPClientAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702, 41)
)
_XcmCONetbiosSMBPClientBinaryPS_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClientBinaryPS = _XcmCONetbiosSMBPClientBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702, 42)
)
_XcmCONetbiosSMBPClientDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPClientDefaultPDL = _XcmCONetbiosSMBPClientDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1702, 43)
)
_XcmCONetbiosSMBPServer_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServer = _XcmCONetbiosSMBPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703)
)
_XcmCONetbiosSMBPServerMaxConns_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServerMaxConns = _XcmCONetbiosSMBPServerMaxConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703, 4)
)
_XcmCONetbiosSMBPServerSpool_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServerSpool = _XcmCONetbiosSMBPServerSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703, 31)
)
_XcmCONetbiosSMBPServerMaxSpool_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServerMaxSpool = _XcmCONetbiosSMBPServerMaxSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703, 32)
)
_XcmCONetbiosSMBPServerJobTimeout_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServerJobTimeout = _XcmCONetbiosSMBPServerJobTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703, 40)
)
_XcmCONetbiosSMBPServerAutoSwitch_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServerAutoSwitch = _XcmCONetbiosSMBPServerAutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703, 41)
)
_XcmCONetbiosSMBPServerBinaryPS_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServerBinaryPS = _XcmCONetbiosSMBPServerBinaryPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703, 42)
)
_XcmCONetbiosSMBPServerDefaultPDL_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBPServerDefaultPDL = _XcmCONetbiosSMBPServerDefaultPDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1703, 43)
)
_XcmCONetbiosSMBFClient_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBFClient = _XcmCONetbiosSMBFClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1704)
)
_XcmCONetbiosSMBFServer_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBFServer = _XcmCONetbiosSMBFServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1705)
)
_XcmCONetbiosSMBFServerName_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBFServerName = _XcmCONetbiosSMBFServerName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1705, 1)
)
_XcmCONetbiosSMBDomain_ObjectIdentity = ObjectIdentity
xcmCONetbiosSMBDomain = _XcmCONetbiosSMBDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 25, 1706)
)
_XcmCONetbeuiSuite_ObjectIdentity = ObjectIdentity
xcmCONetbeuiSuite = _XcmCONetbeuiSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 26)
)
_XcmCONetbeuiDatalinks_ObjectIdentity = ObjectIdentity
xcmCONetbeuiDatalinks = _XcmCONetbeuiDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 26, 1200)
)
_XcmCONetbeuiLLC_ObjectIdentity = ObjectIdentity
xcmCONetbeuiLLC = _XcmCONetbeuiLLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 26, 1201)
)
_XcmCONetbeuiDLC_ObjectIdentity = ObjectIdentity
xcmCONetbeuiDLC = _XcmCONetbeuiDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 26, 1202)
)
_XcmCOSerialSuite_ObjectIdentity = ObjectIdentity
xcmCOSerialSuite = _XcmCOSerialSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27)
)
_XcmCOSerialPhysical_ObjectIdentity = ObjectIdentity
xcmCOSerialPhysical = _XcmCOSerialPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1100)
)
_XcmCOSerialSignalType_ObjectIdentity = ObjectIdentity
xcmCOSerialSignalType = _XcmCOSerialSignalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1101)
)
_XcmCOSerialSignalOverride_ObjectIdentity = ObjectIdentity
xcmCOSerialSignalOverride = _XcmCOSerialSignalOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1101, 1)
)
_XcmCOSerialSignalDetected_ObjectIdentity = ObjectIdentity
xcmCOSerialSignalDetected = _XcmCOSerialSignalDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1101, 2)
)
_XcmCOSerialSignalAdaptive_ObjectIdentity = ObjectIdentity
xcmCOSerialSignalAdaptive = _XcmCOSerialSignalAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1101, 3)
)
_XcmCOSerialSignalSupport_ObjectIdentity = ObjectIdentity
xcmCOSerialSignalSupport = _XcmCOSerialSignalSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1101, 4)
)
_XcmCOSerialDevice_ObjectIdentity = ObjectIdentity
xcmCOSerialDevice = _XcmCOSerialDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1102)
)
_XcmCOSerialDeviceName_ObjectIdentity = ObjectIdentity
xcmCOSerialDeviceName = _XcmCOSerialDeviceName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1102, 1)
)
_XcmCOSerialSpeed_ObjectIdentity = ObjectIdentity
xcmCOSerialSpeed = _XcmCOSerialSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1103)
)
_XcmCOSerialSpeedOverride_ObjectIdentity = ObjectIdentity
xcmCOSerialSpeedOverride = _XcmCOSerialSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1103, 1)
)
_XcmCOSerialSpeedDetected_ObjectIdentity = ObjectIdentity
xcmCOSerialSpeedDetected = _XcmCOSerialSpeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1103, 2)
)
_XcmCOSerialSpeedAdaptive_ObjectIdentity = ObjectIdentity
xcmCOSerialSpeedAdaptive = _XcmCOSerialSpeedAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1103, 3)
)
_XcmCOSerialSpeedSupport_ObjectIdentity = ObjectIdentity
xcmCOSerialSpeedSupport = _XcmCOSerialSpeedSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1103, 4)
)
_XcmCOSerialMinSpeed_ObjectIdentity = ObjectIdentity
xcmCOSerialMinSpeed = _XcmCOSerialMinSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1103, 5)
)
_XcmCOSerialMaxSpeed_ObjectIdentity = ObjectIdentity
xcmCOSerialMaxSpeed = _XcmCOSerialMaxSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1103, 6)
)
_XcmCOSerialBidirectional_ObjectIdentity = ObjectIdentity
xcmCOSerialBidirectional = _XcmCOSerialBidirectional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1104)
)
_XcmCOSerialInputTimeout_ObjectIdentity = ObjectIdentity
xcmCOSerialInputTimeout = _XcmCOSerialInputTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1105)
)
_XcmCOSerialOutputTimeout_ObjectIdentity = ObjectIdentity
xcmCOSerialOutputTimeout = _XcmCOSerialOutputTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1106)
)
_XcmCOSerialConnectorType_ObjectIdentity = ObjectIdentity
xcmCOSerialConnectorType = _XcmCOSerialConnectorType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1107)
)
_XcmCOSerialConnectorOverride_ObjectIdentity = ObjectIdentity
xcmCOSerialConnectorOverride = _XcmCOSerialConnectorOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1107, 1)
)
_XcmCOSerialConnectorDetected_ObjectIdentity = ObjectIdentity
xcmCOSerialConnectorDetected = _XcmCOSerialConnectorDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1107, 2)
)
_XcmCOSerialConnectorAdaptive_ObjectIdentity = ObjectIdentity
xcmCOSerialConnectorAdaptive = _XcmCOSerialConnectorAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1107, 3)
)
_XcmCOSerialMinInputChars_ObjectIdentity = ObjectIdentity
xcmCOSerialMinInputChars = _XcmCOSerialMinInputChars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1108)
)
_XcmCOSerialMaxInputChars_ObjectIdentity = ObjectIdentity
xcmCOSerialMaxInputChars = _XcmCOSerialMaxInputChars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1109)
)
_XcmCOSerialParity_ObjectIdentity = ObjectIdentity
xcmCOSerialParity = _XcmCOSerialParity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1111)
)
_XcmCOSerialDataBits_ObjectIdentity = ObjectIdentity
xcmCOSerialDataBits = _XcmCOSerialDataBits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1112)
)
_XcmCOSerialFlowControl_ObjectIdentity = ObjectIdentity
xcmCOSerialFlowControl = _XcmCOSerialFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1113)
)
_XcmCOSerialStartBits_ObjectIdentity = ObjectIdentity
xcmCOSerialStartBits = _XcmCOSerialStartBits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1114)
)
_XcmCOSerialStopBits_ObjectIdentity = ObjectIdentity
xcmCOSerialStopBits = _XcmCOSerialStopBits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1115)
)
_XcmCOSerialInputPrime_ObjectIdentity = ObjectIdentity
xcmCOSerialInputPrime = _XcmCOSerialInputPrime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1116)
)
_XcmCOSerialDTR_ObjectIdentity = ObjectIdentity
xcmCOSerialDTR = _XcmCOSerialDTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1121)
)
_XcmCOSerialDSR_ObjectIdentity = ObjectIdentity
xcmCOSerialDSR = _XcmCOSerialDSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1122)
)
_XcmCOSerialCTS_ObjectIdentity = ObjectIdentity
xcmCOSerialCTS = _XcmCOSerialCTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1123)
)
_XcmCOSerialRTS_ObjectIdentity = ObjectIdentity
xcmCOSerialRTS = _XcmCOSerialRTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1124)
)
_XcmCOSerialDatalinks_ObjectIdentity = ObjectIdentity
xcmCOSerialDatalinks = _XcmCOSerialDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1200)
)
_XcmCOSerialProtocol_ObjectIdentity = ObjectIdentity
xcmCOSerialProtocol = _XcmCOSerialProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 27, 1200, 1)
)
_XcmCOParallelSuite_ObjectIdentity = ObjectIdentity
xcmCOParallelSuite = _XcmCOParallelSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28)
)
_XcmCOParallelPhysical_ObjectIdentity = ObjectIdentity
xcmCOParallelPhysical = _XcmCOParallelPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1100)
)
_XcmCOParallelSignalType_ObjectIdentity = ObjectIdentity
xcmCOParallelSignalType = _XcmCOParallelSignalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1101)
)
_XcmCOParallelSignalOverride_ObjectIdentity = ObjectIdentity
xcmCOParallelSignalOverride = _XcmCOParallelSignalOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1101, 1)
)
_XcmCOParallelSignalDetected_ObjectIdentity = ObjectIdentity
xcmCOParallelSignalDetected = _XcmCOParallelSignalDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1101, 2)
)
_XcmCOParallelSignalAdaptive_ObjectIdentity = ObjectIdentity
xcmCOParallelSignalAdaptive = _XcmCOParallelSignalAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1101, 3)
)
_XcmCOParallelSignalSupport_ObjectIdentity = ObjectIdentity
xcmCOParallelSignalSupport = _XcmCOParallelSignalSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1101, 4)
)
_XcmCOParallelDevice_ObjectIdentity = ObjectIdentity
xcmCOParallelDevice = _XcmCOParallelDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1102)
)
_XcmCOParallelDeviceName_ObjectIdentity = ObjectIdentity
xcmCOParallelDeviceName = _XcmCOParallelDeviceName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1102, 1)
)
_XcmCOParallelDeviceID_ObjectIdentity = ObjectIdentity
xcmCOParallelDeviceID = _XcmCOParallelDeviceID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1102, 2)
)
_XcmCOParallelSpeed_ObjectIdentity = ObjectIdentity
xcmCOParallelSpeed = _XcmCOParallelSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1103)
)
_XcmCOParallelSpeedOverride_ObjectIdentity = ObjectIdentity
xcmCOParallelSpeedOverride = _XcmCOParallelSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1103, 1)
)
_XcmCOParallelSpeedDetected_ObjectIdentity = ObjectIdentity
xcmCOParallelSpeedDetected = _XcmCOParallelSpeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1103, 2)
)
_XcmCOParallelSpeedAdaptive_ObjectIdentity = ObjectIdentity
xcmCOParallelSpeedAdaptive = _XcmCOParallelSpeedAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1103, 3)
)
_XcmCOParallelSpeedSupport_ObjectIdentity = ObjectIdentity
xcmCOParallelSpeedSupport = _XcmCOParallelSpeedSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1103, 4)
)
_XcmCOParallelMinSpeed_ObjectIdentity = ObjectIdentity
xcmCOParallelMinSpeed = _XcmCOParallelMinSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1103, 5)
)
_XcmCOParallelMaxSpeed_ObjectIdentity = ObjectIdentity
xcmCOParallelMaxSpeed = _XcmCOParallelMaxSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1103, 6)
)
_XcmCOParallelBidirectional_ObjectIdentity = ObjectIdentity
xcmCOParallelBidirectional = _XcmCOParallelBidirectional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1104)
)
_XcmCOParallelInputTimeout_ObjectIdentity = ObjectIdentity
xcmCOParallelInputTimeout = _XcmCOParallelInputTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1105)
)
_XcmCOParallelOutputTimeout_ObjectIdentity = ObjectIdentity
xcmCOParallelOutputTimeout = _XcmCOParallelOutputTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1106)
)
_XcmCOParallelConnectorType_ObjectIdentity = ObjectIdentity
xcmCOParallelConnectorType = _XcmCOParallelConnectorType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1107)
)
_XcmCOParallelConnectorOverride_ObjectIdentity = ObjectIdentity
xcmCOParallelConnectorOverride = _XcmCOParallelConnectorOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1107, 1)
)
_XcmCOParallelConnectorDetected_ObjectIdentity = ObjectIdentity
xcmCOParallelConnectorDetected = _XcmCOParallelConnectorDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1107, 2)
)
_XcmCOParallelConnectorAdaptive_ObjectIdentity = ObjectIdentity
xcmCOParallelConnectorAdaptive = _XcmCOParallelConnectorAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1107, 3)
)
_XcmCOParallelMinInputChars_ObjectIdentity = ObjectIdentity
xcmCOParallelMinInputChars = _XcmCOParallelMinInputChars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1108)
)
_XcmCOParallelMaxInputChars_ObjectIdentity = ObjectIdentity
xcmCOParallelMaxInputChars = _XcmCOParallelMaxInputChars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1109)
)
_XcmCOParallelParity_ObjectIdentity = ObjectIdentity
xcmCOParallelParity = _XcmCOParallelParity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1111)
)
_XcmCOParallelDataBits_ObjectIdentity = ObjectIdentity
xcmCOParallelDataBits = _XcmCOParallelDataBits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1112)
)
_XcmCOParallelFlowControl_ObjectIdentity = ObjectIdentity
xcmCOParallelFlowControl = _XcmCOParallelFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1113)
)
_XcmCOParallelInputPrime_ObjectIdentity = ObjectIdentity
xcmCOParallelInputPrime = _XcmCOParallelInputPrime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1116)
)
_XcmCOParallelHandshake_ObjectIdentity = ObjectIdentity
xcmCOParallelHandshake = _XcmCOParallelHandshake_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1117)
)
_XcmCOParallelDataStrobe_ObjectIdentity = ObjectIdentity
xcmCOParallelDataStrobe = _XcmCOParallelDataStrobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1118)
)
_XcmCOParallelDatalinks_ObjectIdentity = ObjectIdentity
xcmCOParallelDatalinks = _XcmCOParallelDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1200)
)
_XcmCOParallelProtocol_ObjectIdentity = ObjectIdentity
xcmCOParallelProtocol = _XcmCOParallelProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 28, 1200, 1)
)
_XcmCODirectPrintSuite_ObjectIdentity = ObjectIdentity
xcmCODirectPrintSuite = _XcmCODirectPrintSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 29)
)
_XcmCODirectPrintPhysical_ObjectIdentity = ObjectIdentity
xcmCODirectPrintPhysical = _XcmCODirectPrintPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 29, 1100)
)
_XcmCODirectPrintDatalinks_ObjectIdentity = ObjectIdentity
xcmCODirectPrintDatalinks = _XcmCODirectPrintDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 29, 1200)
)
_XcmCODirectPrintProtocol_ObjectIdentity = ObjectIdentity
xcmCODirectPrintProtocol = _XcmCODirectPrintProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 29, 1200, 1)
)
_XcmCOUsbSuite_ObjectIdentity = ObjectIdentity
xcmCOUsbSuite = _XcmCOUsbSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30)
)
_XcmCOUsbPhysical_ObjectIdentity = ObjectIdentity
xcmCOUsbPhysical = _XcmCOUsbPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1100)
)
_XcmCOUsbDevice_ObjectIdentity = ObjectIdentity
xcmCOUsbDevice = _XcmCOUsbDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1102)
)
_XcmCOUsbDeviceName_ObjectIdentity = ObjectIdentity
xcmCOUsbDeviceName = _XcmCOUsbDeviceName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1102, 1)
)
_XcmCOUsbSpeed_ObjectIdentity = ObjectIdentity
xcmCOUsbSpeed = _XcmCOUsbSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1103)
)
_XcmCOUsbSpeedOverride_ObjectIdentity = ObjectIdentity
xcmCOUsbSpeedOverride = _XcmCOUsbSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1103, 1)
)
_XcmCOUsbSpeedDetected_ObjectIdentity = ObjectIdentity
xcmCOUsbSpeedDetected = _XcmCOUsbSpeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1103, 2)
)
_XcmCOUsbSpeedAdaptive_ObjectIdentity = ObjectIdentity
xcmCOUsbSpeedAdaptive = _XcmCOUsbSpeedAdaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1103, 3)
)
_XcmCOUsbSpeedSupport_ObjectIdentity = ObjectIdentity
xcmCOUsbSpeedSupport = _XcmCOUsbSpeedSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1103, 4)
)
_XcmCOUsbMinSpeed_ObjectIdentity = ObjectIdentity
xcmCOUsbMinSpeed = _XcmCOUsbMinSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1103, 5)
)
_XcmCOUsbMaxSpeed_ObjectIdentity = ObjectIdentity
xcmCOUsbMaxSpeed = _XcmCOUsbMaxSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1103, 6)
)
_XcmCOUsbBidirectional_ObjectIdentity = ObjectIdentity
xcmCOUsbBidirectional = _XcmCOUsbBidirectional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1104)
)
_XcmCOUsbInputTimeout_ObjectIdentity = ObjectIdentity
xcmCOUsbInputTimeout = _XcmCOUsbInputTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1105)
)
_XcmCOUsbOutputTimeout_ObjectIdentity = ObjectIdentity
xcmCOUsbOutputTimeout = _XcmCOUsbOutputTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1106)
)
_XcmCOUsbMinInputChars_ObjectIdentity = ObjectIdentity
xcmCOUsbMinInputChars = _XcmCOUsbMinInputChars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1108)
)
_XcmCOUsbMaxInputChars_ObjectIdentity = ObjectIdentity
xcmCOUsbMaxInputChars = _XcmCOUsbMaxInputChars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1109)
)
_XcmCOUsbDatalinks_ObjectIdentity = ObjectIdentity
xcmCOUsbDatalinks = _XcmCOUsbDatalinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1200)
)
_XcmCOUsbProtocol_ObjectIdentity = ObjectIdentity
xcmCOUsbProtocol = _XcmCOUsbProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 30, 1200, 1)
)
_XCmCommsConfigDummy_ObjectIdentity = ObjectIdentity
xCmCommsConfigDummy = _XCmCommsConfigDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 999)
)
_XCmSnmpNetbiosAddress_Type = XcmSnmpNetbiosAddress
_XCmSnmpNetbiosAddress_Object = MibScalar
xCmSnmpNetbiosAddress = _XCmSnmpNetbiosAddress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 999, 1),
    _XCmSnmpNetbiosAddress_Type()
)
xCmSnmpNetbiosAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSnmpNetbiosAddress.setStatus("current")
_XCmCommsConfigGroupSupport_Type = XcmCommsConfigGroupSupport
_XCmCommsConfigGroupSupport_Object = MibScalar
xCmCommsConfigGroupSupport = _XCmCommsConfigGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 999, 2),
    _XCmCommsConfigGroupSupport_Type()
)
xCmCommsConfigGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsConfigGroupSupport.setStatus("current")
_XCmCommsDirRecordType_Type = XcmCommsDirRecordType
_XCmCommsDirRecordType_Object = MibScalar
xCmCommsDirRecordType = _XCmCommsDirRecordType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 999, 3),
    _XCmCommsDirRecordType_Type()
)
xCmCommsDirRecordType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsDirRecordType.setStatus("current")
_XCmCommsDirAttributeType_Type = XcmCommsDirAttributeType
_XCmCommsDirAttributeType_Object = MibScalar
xCmCommsDirAttributeType = _XCmCommsDirAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 999, 4),
    _XCmCommsDirAttributeType_Type()
)
xCmCommsDirAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsDirAttributeType.setStatus("current")
_XCmCommsLDAPAttributeType_Type = XcmCommsLDAPAttributeType
_XCmCommsLDAPAttributeType_Object = MibScalar
xCmCommsLDAPAttributeType = _XCmCommsLDAPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 999, 5),
    _XCmCommsLDAPAttributeType_Type()
)
xCmCommsLDAPAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsLDAPAttributeType.setStatus("current")
_XCmSnmpIPHostnameAddress_Type = XcmSnmpIPHostnameAddress
_XCmSnmpIPHostnameAddress_Object = MibScalar
xCmSnmpIPHostnameAddress = _XCmSnmpIPHostnameAddress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 63, 999, 6),
    _XCmSnmpIPHostnameAddress_Type()
)
xCmSnmpIPHostnameAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSnmpIPHostnameAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-COMMS-CONFIG-TC",
    **{"XcmSnmpNetbiosAddress": XcmSnmpNetbiosAddress,
       "XcmSnmpIPHostnameAddress": XcmSnmpIPHostnameAddress,
       "XcmCommsConfigGroupSupport": XcmCommsConfigGroupSupport,
       "XcmCommsDirRecordType": XcmCommsDirRecordType,
       "XcmCommsDirAttributeType": XcmCommsDirAttributeType,
       "XcmCommsLDAPAttributeType": XcmCommsLDAPAttributeType,
       "xcmCommsConfigTC": xcmCommsConfigTC,
       "xcmSnmpNetbiosDomain": xcmSnmpNetbiosDomain,
       "xcmCOSpecialTypes": xcmCOSpecialTypes,
       "xcmCOSpecialLabel": xcmCOSpecialLabel,
       "xcmCOSpecialImport": xcmCOSpecialImport,
       "xcmCOSpecialRemark": xcmCOSpecialRemark,
       "xcmCOSpecialAddress": xcmCOSpecialAddress,
       "xcmCOSpecialState": xcmCOSpecialState,
       "xcmCOSpecialConditions": xcmCOSpecialConditions,
       "xcmCOSpecialName": xcmCOSpecialName,
       "xcmCOSpecialSupportedInteger": xcmCOSpecialSupportedInteger,
       "xcmCOSpecialSupportedString": xcmCOSpecialSupportedString,
       "xcmCOSpecialAcceptAddress": xcmCOSpecialAcceptAddress,
       "xcmCOSpecialAcceptSubnet": xcmCOSpecialAcceptSubnet,
       "xcmCOSpecialRejectAddress": xcmCOSpecialRejectAddress,
       "xcmCOSpecialRejectSubnet": xcmCOSpecialRejectSubnet,
       "xcmCOSpecialMaxRequestRetries": xcmCOSpecialMaxRequestRetries,
       "xcmCOSpecialRequestTimeout": xcmCOSpecialRequestTimeout,
       "xcmCOSpecialSecurity": xcmCOSpecialSecurity,
       "xcmSnmpIPHostnameDomain": xcmSnmpIPHostnameDomain,
       "xcmCOOsilanSuite": xcmCOOsilanSuite,
       "xcmCOOsilanPhysicals": xcmCOOsilanPhysicals,
       "xcmCOOsilanConnectorType": xcmCOOsilanConnectorType,
       "xcmCOOsilanConnectorOverride": xcmCOOsilanConnectorOverride,
       "xcmCOOsilanConnectorDetected": xcmCOOsilanConnectorDetected,
       "xcmCOOsilanConnectorAdaptive": xcmCOOsilanConnectorAdaptive,
       "xcmCOOsilanSignalType": xcmCOOsilanSignalType,
       "xcmCOOsilanSignalOverride": xcmCOOsilanSignalOverride,
       "xcmCOOsilanSignalDetected": xcmCOOsilanSignalDetected,
       "xcmCOOsilanSignalAdaptive": xcmCOOsilanSignalAdaptive,
       "xcmCOOsilanSignalSupport": xcmCOOsilanSignalSupport,
       "xcmCOOsilanSignalCapability": xcmCOOsilanSignalCapability,
       "xcmCOOsilanCableType": xcmCOOsilanCableType,
       "xcmCOOsilanCableOverride": xcmCOOsilanCableOverride,
       "xcmCOOsilanCableDetected": xcmCOOsilanCableDetected,
       "xcmCOOsilanCableAdaptive": xcmCOOsilanCableAdaptive,
       "xcmCOOsilanCableSupport": xcmCOOsilanCableSupport,
       "xcmCOOsilanDatalinks": xcmCOOsilanDatalinks,
       "xcmCOOsilanFrameType": xcmCOOsilanFrameType,
       "xcmCOOsilanFrameOverride": xcmCOOsilanFrameOverride,
       "xcmCOOsilanFrameDetected": xcmCOOsilanFrameDetected,
       "xcmCOOsilanFrameAdaptive": xcmCOOsilanFrameAdaptive,
       "xcmCOOsilanEthernet": xcmCOOsilanEthernet,
       "xcmCOOsilanEthernetType": xcmCOOsilanEthernetType,
       "xcmCOOsilanEthernetDevice": xcmCOOsilanEthernetDevice,
       "xcmCOOsilanEthernetDeviceName": xcmCOOsilanEthernetDeviceName,
       "xcmCOOsilanEthernetSpeed": xcmCOOsilanEthernetSpeed,
       "xcmCOOsilanEthernetSpeedOverride": xcmCOOsilanEthernetSpeedOverride,
       "xcmCOOsilanEthernetSpeedDetected": xcmCOOsilanEthernetSpeedDetected,
       "xcmCOOsilanEthernetSpeedAdaptive": xcmCOOsilanEthernetSpeedAdaptive,
       "xcmCOOsilanEthernetSpeedSupport": xcmCOOsilanEthernetSpeedSupport,
       "xcmCOOsilanEthernetMinSpeed": xcmCOOsilanEthernetMinSpeed,
       "xcmCOOsilanEthernetMaxSpeed": xcmCOOsilanEthernetMaxSpeed,
       "xcmCOOsilanEthernetMaxFrameSize": xcmCOOsilanEthernetMaxFrameSize,
       "xcmCOOsilanEthernetInterface": xcmCOOsilanEthernetInterface,
       "xcmCOOsilanEthernetMACAddress": xcmCOOsilanEthernetMACAddress,
       "xcmCOOsilanTokenBus": xcmCOOsilanTokenBus,
       "xcmCOOsilanTokenRing": xcmCOOsilanTokenRing,
       "xcmCOOsilanTokenRingType": xcmCOOsilanTokenRingType,
       "xcmCOOsilanTokenRingDevice": xcmCOOsilanTokenRingDevice,
       "xcmCOOsilanTokenRingDeviceName": xcmCOOsilanTokenRingDeviceName,
       "xcmCOOsilanTokenRingSpeed": xcmCOOsilanTokenRingSpeed,
       "xcmCOOsilanTokenRingSpeedOverride": xcmCOOsilanTokenRingSpeedOverride,
       "xcmCOOsilanTokenRingSpeedDetected": xcmCOOsilanTokenRingSpeedDetected,
       "xcmCOOsilanTokenRingSpeedAdaptive": xcmCOOsilanTokenRingSpeedAdaptive,
       "xcmCOOsilanTokenRingSpeedSupport": xcmCOOsilanTokenRingSpeedSupport,
       "xcmCOOsilanTokenRingMinSpeed": xcmCOOsilanTokenRingMinSpeed,
       "xcmCOOsilanTokenRingMaxSpeed": xcmCOOsilanTokenRingMaxSpeed,
       "xcmCOOsilanTokenRingMaxFrameSize": xcmCOOsilanTokenRingMaxFrameSize,
       "xcmCOOsilanTokenRingInterface": xcmCOOsilanTokenRingInterface,
       "xcmCOOsilanTokenRingMACAddress": xcmCOOsilanTokenRingMACAddress,
       "xcmCOOsilanTokenRingSSR": xcmCOOsilanTokenRingSSR,
       "xcmCOOsilanTokenRingSSRAllRoute": xcmCOOsilanTokenRingSSRAllRoute,
       "xcmCOOsilanTokenRingSSRSingleRR": xcmCOOsilanTokenRingSSRSingleRR,
       "xcmCOOsilanTokenRingSSRAdaptive": xcmCOOsilanTokenRingSSRAdaptive,
       "xcmCOOsilanTokenRingMACOverride": xcmCOOsilanTokenRingMACOverride,
       "xcmCOOsilanFDDI": xcmCOOsilanFDDI,
       "xcmCOOsiwanSuite": xcmCOOsiwanSuite,
       "xcmCOOsiwanPhysicals": xcmCOOsiwanPhysicals,
       "xcmCOOsiwanConnectorType": xcmCOOsiwanConnectorType,
       "xcmCOOsiwanConnectorOverride": xcmCOOsiwanConnectorOverride,
       "xcmCOOsiwanConnectorDetected": xcmCOOsiwanConnectorDetected,
       "xcmCOOsiwanConnectorAdaptive": xcmCOOsiwanConnectorAdaptive,
       "xcmCOOsiwanSignalType": xcmCOOsiwanSignalType,
       "xcmCOOsiwanSignalOverride": xcmCOOsiwanSignalOverride,
       "xcmCOOsiwanSignalDetected": xcmCOOsiwanSignalDetected,
       "xcmCOOsiwanSignalAdaptive": xcmCOOsiwanSignalAdaptive,
       "xcmCOOsiwanSignalSupport": xcmCOOsiwanSignalSupport,
       "xcmCOOsiwanLineNumber": xcmCOOsiwanLineNumber,
       "xcmCOOsiwanSendManual": xcmCOOsiwanSendManual,
       "xcmCOOsiwanReceiveManual": xcmCOOsiwanReceiveManual,
       "xcmCOOsiwanRingsBeforeAnswer": xcmCOOsiwanRingsBeforeAnswer,
       "xcmCOOsiwanErrorCorrection": xcmCOOsiwanErrorCorrection,
       "xcmCOOsiwanDirection": xcmCOOsiwanDirection,
       "xcmCOOsiwanSendStartTime": xcmCOOsiwanSendStartTime,
       "xcmCOOsiwanSendEndTime": xcmCOOsiwanSendEndTime,
       "xcmCOOsiwanReceiveStartTime": xcmCOOsiwanReceiveStartTime,
       "xcmCOOsiwanReceiveEndTime": xcmCOOsiwanReceiveEndTime,
       "xcmCOOsiwanRingerVolume": xcmCOOsiwanRingerVolume,
       "xcmCOOsiwanMonitorVolume": xcmCOOsiwanMonitorVolume,
       "xcmCOOsiwanAlarmVolume": xcmCOOsiwanAlarmVolume,
       "xcmCOOsiwanKeyboardVolume": xcmCOOsiwanKeyboardVolume,
       "xcmCOOsiwanDatalinks": xcmCOOsiwanDatalinks,
       "xcmCOOsiwanFax": xcmCOOsiwanFax,
       "xcmCOOsiwanFaxAddress": xcmCOOsiwanFaxAddress,
       "xcmCOOsiwanFaxDevice": xcmCOOsiwanFaxDevice,
       "xcmCOOsiwanFaxDeviceName": xcmCOOsiwanFaxDeviceName,
       "xcmCOOsiwanFaxSpeed": xcmCOOsiwanFaxSpeed,
       "xcmCOOsiwanFaxSpeedOverride": xcmCOOsiwanFaxSpeedOverride,
       "xcmCOOsiwanFaxSpeedDetected": xcmCOOsiwanFaxSpeedDetected,
       "xcmCOOsiwanFaxSpeedAdaptive": xcmCOOsiwanFaxSpeedAdaptive,
       "xcmCOOsiwanFaxSpeedSupport": xcmCOOsiwanFaxSpeedSupport,
       "xcmCOOsiwanFaxMinSpeed": xcmCOOsiwanFaxMinSpeed,
       "xcmCOOsiwanFaxMaxSpeed": xcmCOOsiwanFaxMaxSpeed,
       "xcmCOOsiwanFaxInterface": xcmCOOsiwanFaxInterface,
       "xcmCOOsiwanFaxAcceptAddress": xcmCOOsiwanFaxAcceptAddress,
       "xcmCOOsiwanFaxRejectAddress": xcmCOOsiwanFaxRejectAddress,
       "xcmCOOsiwanFaxSendCoverSheet": xcmCOOsiwanFaxSendCoverSheet,
       "xcmCOOsiwanFaxSendHeader": xcmCOOsiwanFaxSendHeader,
       "xcmCOOsiwanFaxSendManual": xcmCOOsiwanFaxSendManual,
       "xcmCOOsiwanFaxSendSecurity": xcmCOOsiwanFaxSendSecurity,
       "xcmCOOsiwanFaxMaxRetries": xcmCOOsiwanFaxMaxRetries,
       "xcmCOOsiwanFaxRetryInterval": xcmCOOsiwanFaxRetryInterval,
       "xcmCOOsiwanFaxSendStoreTime": xcmCOOsiwanFaxSendStoreTime,
       "xcmCOOsiwanFaxMaxOriginalLength": xcmCOOsiwanFaxMaxOriginalLength,
       "xcmCOOsiwanFaxReceiveCoverSheet": xcmCOOsiwanFaxReceiveCoverSheet,
       "xcmCOOsiwanFaxReceiveFooter": xcmCOOsiwanFaxReceiveFooter,
       "xcmCOOsiwanFaxReceiveToMemory": xcmCOOsiwanFaxReceiveToMemory,
       "xcmCOOsiwanFaxReceiveManual": xcmCOOsiwanFaxReceiveManual,
       "xcmCOOsiwanFaxReceiveSecurity": xcmCOOsiwanFaxReceiveSecurity,
       "xcmCOOsiwanFaxReceiveAutoReduce": xcmCOOsiwanFaxReceiveAutoReduce,
       "xcmCOOsiwanFaxReceiveOverflow": xcmCOOsiwanFaxReceiveOverflow,
       "xcmCOOsiwanFaxReceiveCollate": xcmCOOsiwanFaxReceiveCollate,
       "xcmCOOsiwanFaxG3": xcmCOOsiwanFaxG3,
       "xcmCOOsiwanFaxG4": xcmCOOsiwanFaxG4,
       "xcmCOOsiwanFaxLineSwitching": xcmCOOsiwanFaxLineSwitching,
       "xcmCOOsiwanFaxMaxSpeedDial": xcmCOOsiwanFaxMaxSpeedDial,
       "xcmCOOsiwanPSTN": xcmCOOsiwanPSTN,
       "xcmCOOsiwanPSTNAddress": xcmCOOsiwanPSTNAddress,
       "xcmCOOsiwanISDN": xcmCOOsiwanISDN,
       "xcmCOOsiwanISDNAddress": xcmCOOsiwanISDNAddress,
       "xcmCOOsiwanTransports": xcmCOOsiwanTransports,
       "xcmCOOsiwanApplications": xcmCOOsiwanApplications,
       "xcmCOOsiwanDPA": xcmCOOsiwanDPA,
       "xcmCOOsiwanFTAM": xcmCOOsiwanFTAM,
       "xcmCOOsiwanVT": xcmCOOsiwanVT,
       "xcmCOOsiwanMHS": xcmCOOsiwanMHS,
       "xcmCOOsiwanDS": xcmCOOsiwanDS,
       "xcmCOOsiwanDAP": xcmCOOsiwanDAP,
       "xcmCOOsiwanDSP": xcmCOOsiwanDSP,
       "xcmCOOsiwanMgmt": xcmCOOsiwanMgmt,
       "xcmCOOsiwanCMIP": xcmCOOsiwanCMIP,
       "xcmCOOsiwanSecurity": xcmCOOsiwanSecurity,
       "xcmCOInternetSuite": xcmCOInternetSuite,
       "xcmCOInternetDatalinks": xcmCOInternetDatalinks,
       "xcmCOInternetSLIP": xcmCOInternetSLIP,
       "xcmCOInternetPPP": xcmCOInternetPPP,
       "xcmCOInternetIP": xcmCOInternetIP,
       "xcmCOInternetIPAddress": xcmCOInternetIPAddress,
       "xcmCOInternetIPSocketAddress": xcmCOInternetIPSocketAddress,
       "xcmCOInternetIPSubnetMask": xcmCOInternetIPSubnetMask,
       "xcmCOInternetIPAddressViaRARP": xcmCOInternetIPAddressViaRARP,
       "xcmCOInternetIPDefaultGateway": xcmCOInternetIPDefaultGateway,
       "xcmCOInternetIPAddressSource": xcmCOInternetIPAddressSource,
       "xcmCOInternetIPDatalinks": xcmCOInternetIPDatalinks,
       "xcmCOInternetIPHostName": xcmCOInternetIPHostName,
       "xcmCOInternetIPAutoIPAddress": xcmCOInternetIPAutoIPAddress,
       "xcmCOInternetIPAutoEnable": xcmCOInternetIPAutoEnable,
       "xcmCOInternetIPBcastCache": xcmCOInternetIPBcastCache,
       "xcmCOInternetIPBCacheEnabled": xcmCOInternetIPBCacheEnabled,
       "xcmCOInternetIPBCacheAddress1": xcmCOInternetIPBCacheAddress1,
       "xcmCOInternetIPBCacheAddress2": xcmCOInternetIPBCacheAddress2,
       "xcmCOInternetIPBCacheAddress3": xcmCOInternetIPBCacheAddress3,
       "xcmCOInternetIPBCacheAddress4": xcmCOInternetIPBCacheAddress4,
       "xcmCOInternetIPInstall": xcmCOInternetIPInstall,
       "xcmCOInternetIPInstallSelect": xcmCOInternetIPInstallSelect,
       "xcmCOInternetIPAllSubnetsLocal": xcmCOInternetIPAllSubnetsLocal,
       "xcmCOInternetIPSec": xcmCOInternetIPSec,
       "xcmCOInternetICMP": xcmCOInternetICMP,
       "xcmCOInternetARP": xcmCOInternetARP,
       "xcmCOInternetDHCP": xcmCOInternetDHCP,
       "xcmCOInternetDHCPClassID": xcmCOInternetDHCPClassID,
       "xcmCOInternetDHCPLeaseTime": xcmCOInternetDHCPLeaseTime,
       "xcmCOInternetDHCPRequestTimeout": xcmCOInternetDHCPRequestTimeout,
       "xcmCOInternetDHCPServer": xcmCOInternetDHCPServer,
       "xcmCOInternetDHCPOptionGet": xcmCOInternetDHCPOptionGet,
       "xcmCODHCPGetSubnetMask": xcmCODHCPGetSubnetMask,
       "xcmCODHCPGetSubnetTimeOffset": xcmCODHCPGetSubnetTimeOffset,
       "xcmCODHCPGetRouter": xcmCODHCPGetRouter,
       "xcmCODHCPGetTPTimeServer": xcmCODHCPGetTPTimeServer,
       "xcmCODHCPGetIEN116NameServer": xcmCODHCPGetIEN116NameServer,
       "xcmCODHCPGetDNSNameServer": xcmCODHCPGetDNSNameServer,
       "xcmCODHCPGetLogServer": xcmCODHCPGetLogServer,
       "xcmCODHCPGetCookieServer": xcmCODHCPGetCookieServer,
       "xcmCODHCPGetLPRServer": xcmCODHCPGetLPRServer,
       "xcmCODHCPGetImpressServer": xcmCODHCPGetImpressServer,
       "xcmCODHCPGetResourceLocServer": xcmCODHCPGetResourceLocServer,
       "xcmCODHCPGetHostName": xcmCODHCPGetHostName,
       "xcmCODHCPGetBootFileSize": xcmCODHCPGetBootFileSize,
       "xcmCODHCPGetMeritDumpFile": xcmCODHCPGetMeritDumpFile,
       "xcmCODHCPGetDNSDomainName": xcmCODHCPGetDNSDomainName,
       "xcmCODHCPGetSwapServer": xcmCODHCPGetSwapServer,
       "xcmCODHCPGetRootPath": xcmCODHCPGetRootPath,
       "xcmCODHCPGetExtensionsPath": xcmCODHCPGetExtensionsPath,
       "xcmCODHCPGetIPForwarding": xcmCODHCPGetIPForwarding,
       "xcmCODHCPGetNLSourceRouting": xcmCODHCPGetNLSourceRouting,
       "xcmCODHCPGetNLPolicyFilter": xcmCODHCPGetNLPolicyFilter,
       "xcmCODHCPGetMaxIPDatagramSize": xcmCODHCPGetMaxIPDatagramSize,
       "xcmCODHCPGetIPDefaultTTL": xcmCODHCPGetIPDefaultTTL,
       "xcmCODHCPGetPathMTUAgeTimeout": xcmCODHCPGetPathMTUAgeTimeout,
       "xcmCODHCPGetPathMTUPlateau": xcmCODHCPGetPathMTUPlateau,
       "xcmCODHCPGetInterfaceMTUSize": xcmCODHCPGetInterfaceMTUSize,
       "xcmCODHCPGetAllSubnetsLocal": xcmCODHCPGetAllSubnetsLocal,
       "xcmCODHCPGetBroadcastAddress": xcmCODHCPGetBroadcastAddress,
       "xcmCODHCPGetMaskDiscovery": xcmCODHCPGetMaskDiscovery,
       "xcmCODHCPGetMaskSupplier": xcmCODHCPGetMaskSupplier,
       "xcmCODHCPGetRouterDiscovery": xcmCODHCPGetRouterDiscovery,
       "xcmCODHCPGetRouterSolAddress": xcmCODHCPGetRouterSolAddress,
       "xcmCODHCPGetStaticRoute": xcmCODHCPGetStaticRoute,
       "xcmCODHCPGetARPTrailer": xcmCODHCPGetARPTrailer,
       "xcmCODHCPGetARPCacheTimeout": xcmCODHCPGetARPCacheTimeout,
       "xcmCODHCPGetEthernetFrameIEEE": xcmCODHCPGetEthernetFrameIEEE,
       "xcmCODHCPGetTCPDefaultTTL": xcmCODHCPGetTCPDefaultTTL,
       "xcmCODHCPGetTCPKeepInterval": xcmCODHCPGetTCPKeepInterval,
       "xcmCODHCPGetTCPKeepGarbage": xcmCODHCPGetTCPKeepGarbage,
       "xcmCODHCPGetNISDomainName": xcmCODHCPGetNISDomainName,
       "xcmCODHCPGetNISNameServer": xcmCODHCPGetNISNameServer,
       "xcmCODHCPGetNTPTimeServer": xcmCODHCPGetNTPTimeServer,
       "xcmCODHCPGetVendorSpecific": xcmCODHCPGetVendorSpecific,
       "xcmCODHCPGetNetbiosNameServer": xcmCODHCPGetNetbiosNameServer,
       "xcmCODHCPGetNetbiosDistServer": xcmCODHCPGetNetbiosDistServer,
       "xcmCODHCPGetNetbiosNodeType": xcmCODHCPGetNetbiosNodeType,
       "xcmCODHCPGetNetbiosScope": xcmCODHCPGetNetbiosScope,
       "xcmCODHCPGetXWindowFontServer": xcmCODHCPGetXWindowFontServer,
       "xcmCODHCPGetXWindowDisplayMgr": xcmCODHCPGetXWindowDisplayMgr,
       "xcmCODHCPGetMessageType": xcmCODHCPGetMessageType,
       "xcmCODHCPGetServerID": xcmCODHCPGetServerID,
       "xcmCODHCPGetParameterRequest": xcmCODHCPGetParameterRequest,
       "xcmCODHCPGetErrorMessage": xcmCODHCPGetErrorMessage,
       "xcmCODHCPGetMaxMessageSize": xcmCODHCPGetMaxMessageSize,
       "xcmCODHCPGetRenewT1Interval": xcmCODHCPGetRenewT1Interval,
       "xcmCODHCPGetRebindT2Interval": xcmCODHCPGetRebindT2Interval,
       "xcmCODHCPGetNISPlusDomainName": xcmCODHCPGetNISPlusDomainName,
       "xcmCODHCPGetNISPlusNameServer": xcmCODHCPGetNISPlusNameServer,
       "xcmCODHCPGetTFTPServerName": xcmCODHCPGetTFTPServerName,
       "xcmCODHCPGetBootFileName": xcmCODHCPGetBootFileName,
       "xcmCODHCPGetMobileIPHomeAgent": xcmCODHCPGetMobileIPHomeAgent,
       "xcmCODHCPGetSMTPMailServer": xcmCODHCPGetSMTPMailServer,
       "xcmCODHCPGetPOP3MailServer": xcmCODHCPGetPOP3MailServer,
       "xcmCODHCPGetNNTPNewsServer": xcmCODHCPGetNNTPNewsServer,
       "xcmCODHCPGetWWWServer": xcmCODHCPGetWWWServer,
       "xcmCODHCPGetFingerServer": xcmCODHCPGetFingerServer,
       "xcmCODHCPGetIRCServer": xcmCODHCPGetIRCServer,
       "xcmCODHCPGetStreetTalkServer": xcmCODHCPGetStreetTalkServer,
       "xcmCODHCPGetStreetTalkDAServer": xcmCODHCPGetStreetTalkDAServer,
       "xcmCODHCPGetNDSNameServer": xcmCODHCPGetNDSNameServer,
       "xcmCODHCPGetNDSTreeName": xcmCODHCPGetNDSTreeName,
       "xcmCODHCPGetNDSContext": xcmCODHCPGetNDSContext,
       "xcmCOInternetDHCPOptionSet": xcmCOInternetDHCPOptionSet,
       "xcmCODHCPSetIPAddressRequest": xcmCODHCPSetIPAddressRequest,
       "xcmCODHCPSetIPAddressLeaseTime": xcmCODHCPSetIPAddressLeaseTime,
       "xcmCODHCPSetOptionOverload": xcmCODHCPSetOptionOverload,
       "xcmCODHCPSetClassID": xcmCODHCPSetClassID,
       "xcmCODHCPSetClientID": xcmCODHCPSetClientID,
       "xcmCOInternetBOOTP": xcmCOInternetBOOTP,
       "xcmCOInternetBOOTPBroadcastEnabled": xcmCOInternetBOOTPBroadcastEnabled,
       "xcmCOInternetRARP": xcmCOInternetRARP,
       "xcmCOInternetIPv6": xcmCOInternetIPv6,
       "xcmCOInternetIPv6Address": xcmCOInternetIPv6Address,
       "xcmCOInternetIPv6SocketAddress": xcmCOInternetIPv6SocketAddress,
       "xcmCOInternetIPv6ManuallyAssignedAddress": xcmCOInternetIPv6ManuallyAssignedAddress,
       "xcmCOInternetIPv6DHCPv6AssignedAddress": xcmCOInternetIPv6DHCPv6AssignedAddress,
       "xcmCOInternetIPv6LinkLocalAddress": xcmCOInternetIPv6LinkLocalAddress,
       "xcmCOInternetIPv6StatelessAddress": xcmCOInternetIPv6StatelessAddress,
       "xcmCOInternetIPv6RandomAddress": xcmCOInternetIPv6RandomAddress,
       "xcmCOInternetIPv6AutomaticAddressing": xcmCOInternetIPv6AutomaticAddressing,
       "xcmCOInternetIPv6EUI64InterfaceId": xcmCOInternetIPv6EUI64InterfaceId,
       "xcmCOInternetIPv6RouterAdvertisementAddressPrefix": xcmCOInternetIPv6RouterAdvertisementAddressPrefix,
       "xcmCOInternetIPv6DefaultGateway": xcmCOInternetIPv6DefaultGateway,
       "xcmCOInternetIPv6HostName": xcmCOInternetIPv6HostName,
       "xcmCOInternetTransports": xcmCOInternetTransports,
       "xcmCOInternetUDP": xcmCOInternetUDP,
       "xcmCOInternetUDPAddress": xcmCOInternetUDPAddress,
       "xcmCOInternetUDPPort": xcmCOInternetUDPPort,
       "xcmCOInternetTCP": xcmCOInternetTCP,
       "xcmCOInternetTCPAddress": xcmCOInternetTCPAddress,
       "xcmCOInternetTCPPort": xcmCOInternetTCPPort,
       "xcmCOInternetTCPMaxSegmentSize": xcmCOInternetTCPMaxSegmentSize,
       "xcmCOInternetPing": xcmCOInternetPing,
       "xcmCOInternetSSL3": xcmCOInternetSSL3,
       "xcmCOInternetSSL3Port": xcmCOInternetSSL3Port,
       "xcmCOInternetSSL3CipherStrength": xcmCOInternetSSL3CipherStrength,
       "xcmCOInternetTLS": xcmCOInternetTLS,
       "xcmCOInternetICMPv6": xcmCOInternetICMPv6,
       "xcmCOInternetRaw": xcmCOInternetRaw,
       "xcmCOInternetRawHostName": xcmCOInternetRawHostName,
       "xcmCOInternetRawHostAddress": xcmCOInternetRawHostAddress,
       "xcmCOInternetRawListenSocket": xcmCOInternetRawListenSocket,
       "xcmCOInternetRawMaxClients": xcmCOInternetRawMaxClients,
       "xcmCOInternetRawAcceptAddress": xcmCOInternetRawAcceptAddress,
       "xcmCOInternetRawAcceptSubnet": xcmCOInternetRawAcceptSubnet,
       "xcmCOInternetRawRejectAddress": xcmCOInternetRawRejectAddress,
       "xcmCOInternetRawRejectSubnet": xcmCOInternetRawRejectSubnet,
       "xcmCOInternetRawSpool": xcmCOInternetRawSpool,
       "xcmCOInternetRawMaxSpool": xcmCOInternetRawMaxSpool,
       "xcmCOInternetRawJobTimeout": xcmCOInternetRawJobTimeout,
       "xcmCOInternetRawAutoSwitch": xcmCOInternetRawAutoSwitch,
       "xcmCOInternetRawBinaryPS": xcmCOInternetRawBinaryPS,
       "xcmCOInternetRawDefaultPDL": xcmCOInternetRawDefaultPDL,
       "xcmCOInternetRawBidirectional": xcmCOInternetRawBidirectional,
       "xcmCOInternetIPP": xcmCOInternetIPP,
       "xcmCOInternetIPPHostName": xcmCOInternetIPPHostName,
       "xcmCOInternetIPPHostAddress": xcmCOInternetIPPHostAddress,
       "xcmCOInternetIPPListenSocket": xcmCOInternetIPPListenSocket,
       "xcmCOInternetIPPMaxClients": xcmCOInternetIPPMaxClients,
       "xcmCOInternetIPPVersionString": xcmCOInternetIPPVersionString,
       "xcmCOInternetIPPAcceptAddress": xcmCOInternetIPPAcceptAddress,
       "xcmCOInternetIPPAcceptSubnet": xcmCOInternetIPPAcceptSubnet,
       "xcmCOInternetIPPRejectAddress": xcmCOInternetIPPRejectAddress,
       "xcmCOInternetIPPRejectSubnet": xcmCOInternetIPPRejectSubnet,
       "xcmCOInternetIPPSpool": xcmCOInternetIPPSpool,
       "xcmCOInternetIPPMaxSpool": xcmCOInternetIPPMaxSpool,
       "xcmCOInternetIPPJobTimeout": xcmCOInternetIPPJobTimeout,
       "xcmCOInternetIPPAutoSwitch": xcmCOInternetIPPAutoSwitch,
       "xcmCOInternetIPPBinaryPS": xcmCOInternetIPPBinaryPS,
       "xcmCOInternetIPPDefaultPDL": xcmCOInternetIPPDefaultPDL,
       "xcmCOInternetIPPAuthScheme": xcmCOInternetIPPAuthScheme,
       "xcmCOInternetLPR": xcmCOInternetLPR,
       "xcmCOInternetLPRHostName": xcmCOInternetLPRHostName,
       "xcmCOInternetLPRHostAddress": xcmCOInternetLPRHostAddress,
       "xcmCOInternetLPRListenSocket": xcmCOInternetLPRListenSocket,
       "xcmCOInternetLPRMaxClients": xcmCOInternetLPRMaxClients,
       "xcmCOInternetLPRAcceptAddress": xcmCOInternetLPRAcceptAddress,
       "xcmCOInternetLPRAcceptSubnet": xcmCOInternetLPRAcceptSubnet,
       "xcmCOInternetLPRRejectAddress": xcmCOInternetLPRRejectAddress,
       "xcmCOInternetLPRRejectSubnet": xcmCOInternetLPRRejectSubnet,
       "xcmCOInternetLPRSpool": xcmCOInternetLPRSpool,
       "xcmCOInternetLPRMaxSpool": xcmCOInternetLPRMaxSpool,
       "xcmCOInternetLPRJobTimeout": xcmCOInternetLPRJobTimeout,
       "xcmCOInternetLPRAutoSwitch": xcmCOInternetLPRAutoSwitch,
       "xcmCOInternetLPRBinaryPS": xcmCOInternetLPRBinaryPS,
       "xcmCOInternetLPRDefaultPDL": xcmCOInternetLPRDefaultPDL,
       "xcmCOInternetFTP": xcmCOInternetFTP,
       "xcmCOInternetFTPPassiveMode": xcmCOInternetFTPPassiveMode,
       "xcmCOInternetSMTP": xcmCOInternetSMTP,
       "xcmCOInternetSMTPHostName": xcmCOInternetSMTPHostName,
       "xcmCOInternetSMTPHostAddress": xcmCOInternetSMTPHostAddress,
       "xcmCOInternetSMTPListenSocket": xcmCOInternetSMTPListenSocket,
       "xcmCOInternetSMTPMaxClients": xcmCOInternetSMTPMaxClients,
       "xcmCOInternetSMTPAcceptAddress": xcmCOInternetSMTPAcceptAddress,
       "xcmCOInternetSMTPAcceptSubnet": xcmCOInternetSMTPAcceptSubnet,
       "xcmCOInternetSMTPRejectAddress": xcmCOInternetSMTPRejectAddress,
       "xcmCOInternetSMTPRejectSubnet": xcmCOInternetSMTPRejectSubnet,
       "xcmCOInternetSMTPSpool": xcmCOInternetSMTPSpool,
       "xcmCOInternetSMTPMaxSpool": xcmCOInternetSMTPMaxSpool,
       "xcmCOInternetSMTPJobTimeout": xcmCOInternetSMTPJobTimeout,
       "xcmCOInternetSMTPAutoSwitch": xcmCOInternetSMTPAutoSwitch,
       "xcmCOInternetSMTPBinaryPS": xcmCOInternetSMTPBinaryPS,
       "xcmCOInternetSMTPDefaultPDL": xcmCOInternetSMTPDefaultPDL,
       "xcmCOInternetSMTPSubject": xcmCOInternetSMTPSubject,
       "xcmCOInternetSMTPSignatureLine": xcmCOInternetSMTPSignatureLine,
       "xcmCOInternetSMTPUserName": xcmCOInternetSMTPUserName,
       "xcmCOInternetSMTPPassword": xcmCOInternetSMTPPassword,
       "xcmCOInternetSMTPMaxInputText": xcmCOInternetSMTPMaxInputText,
       "xcmCOInternetSMTPMaxInputAttach": xcmCOInternetSMTPMaxInputAttach,
       "xcmCOInternetSMTPMaxOutputText": xcmCOInternetSMTPMaxOutputText,
       "xcmCOInternetSMTPMaxOutputAttach": xcmCOInternetSMTPMaxOutputAttach,
       "xcmCOInternetSMTPConfirmRequest": xcmCOInternetSMTPConfirmRequest,
       "xcmCOInternetSMTPConfirmReply": xcmCOInternetSMTPConfirmReply,
       "xcmCOInternetSMTPConfirmTimeout": xcmCOInternetSMTPConfirmTimeout,
       "xcmCOInternetSMTPFeatureReply": xcmCOInternetSMTPFeatureReply,
       "xcmCOInternetSMTPMailAddress": xcmCOInternetSMTPMailAddress,
       "xcmCOInternetSMTPMaxInFragments": xcmCOInternetSMTPMaxInFragments,
       "xcmCOInternetSMTPMaxOutFragments": xcmCOInternetSMTPMaxOutFragments,
       "xcmCOInternetSMTPMaxInAttachments": xcmCOInternetSMTPMaxInAttachments,
       "xcmCOInternetSMTPMaxOutAttachments": xcmCOInternetSMTPMaxOutAttachments,
       "xcmCOInternetSMTPMaxInputSize": xcmCOInternetSMTPMaxInputSize,
       "xcmCOInternetSMTPMaxOutputSize": xcmCOInternetSMTPMaxOutputSize,
       "xcmCOInternetSMTPReversePath": xcmCOInternetSMTPReversePath,
       "xcmCOInternetSMTPAutoServer": xcmCOInternetSMTPAutoServer,
       "xcmCOInternetTelnet": xcmCOInternetTelnet,
       "xcmCOInternetDNS": xcmCOInternetDNS,
       "xcmCOInternetDNSDomainName": xcmCOInternetDNSDomainName,
       "xcmCOInternetDNSLanguage": xcmCOInternetDNSLanguage,
       "xcmCOInternetDNSCharset": xcmCOInternetDNSCharset,
       "xcmCOInternetDNSServerName": xcmCOInternetDNSServerName,
       "xcmCOInternetDNSServerAddress": xcmCOInternetDNSServerAddress,
       "xcmCOInternetDNSServerResolvedAddress": xcmCOInternetDNSServerResolvedAddress,
       "xcmCOInternetDNSServerTimeout": xcmCOInternetDNSServerTimeout,
       "xcmCOInternetDNSAppendDomainName": xcmCOInternetDNSAppendDomainName,
       "xcmCOInternetDNSAppendParentDomains": xcmCOInternetDNSAppendParentDomains,
       "xcmCOInternetDNSDomainNameList": xcmCOInternetDNSDomainNameList,
       "xcmCOInternetDNSDynamicUpdate": xcmCOInternetDNSDynamicUpdate,
       "xcmCOInternetDNSUpdatePolicy": xcmCOInternetDNSUpdatePolicy,
       "xcmCOInternetDNSMulticastEnable": xcmCOInternetDNSMulticastEnable,
       "xcmCOInternetIOSDiscoveryEnable": xcmCOInternetIOSDiscoveryEnable,
       "xcmCOInternetTFTP": xcmCOInternetTFTP,
       "xcmCOInternetHTTP": xcmCOInternetHTTP,
       "xcmCOInternetHTTPAddressURL": xcmCOInternetHTTPAddressURL,
       "xcmCOInternetHTTPAddressURI": xcmCOInternetHTTPAddressURI,
       "xcmCOInternetHTTPAddressURN": xcmCOInternetHTTPAddressURN,
       "xcmCOInternetHTTPVersionString": xcmCOInternetHTTPVersionString,
       "xcmCOInternetHTTPListenSocket": xcmCOInternetHTTPListenSocket,
       "xcmCOInternetHTTPMaxClients": xcmCOInternetHTTPMaxClients,
       "xcmCOInternetHTTPClientTimeout": xcmCOInternetHTTPClientTimeout,
       "xcmCOInternetHTTPStatusRefresh": xcmCOInternetHTTPStatusRefresh,
       "xcmCOInternetHTTPAdminAddress": xcmCOInternetHTTPAdminAddress,
       "xcmCOInternetHTTPKeyUsrAddress": xcmCOInternetHTTPKeyUsrAddress,
       "xcmCOInternetHTTPProxy": xcmCOInternetHTTPProxy,
       "xcmCOInternetHTTPProxyIPAddress": xcmCOInternetHTTPProxyIPAddress,
       "xcmCOInternetHTTPProxyHostName": xcmCOInternetHTTPProxyHostName,
       "xcmCOInternetHTTPProxyPortNumber": xcmCOInternetHTTPProxyPortNumber,
       "xcmCOInternetHTTPProxyExceptions": xcmCOInternetHTTPProxyExceptions,
       "xcmCOInternetHTTPProxyServer": xcmCOInternetHTTPProxyServer,
       "xcmCOInternetHTTPProxyUserName": xcmCOInternetHTTPProxyUserName,
       "xcmCOInternetHTTPProxyPassword": xcmCOInternetHTTPProxyPassword,
       "xcmCOInternetHTTPProxyAutoDetect": xcmCOInternetHTTPProxyAutoDetect,
       "xcmCOInternetHTTPProxyShareSettings": xcmCOInternetHTTPProxyShareSettings,
       "xcmCOInternetHTTPProxyAuthValid": xcmCOInternetHTTPProxyAuthValid,
       "xcmCOInternetHTTPInfoFwd": xcmCOInternetHTTPInfoFwd,
       "xcmCOInternetSNMP": xcmCOInternetSNMP,
       "xcmCOInternetSNMPVersion": xcmCOInternetSNMPVersion,
       "xcmCOInternetSNMPAdminAddress": xcmCOInternetSNMPAdminAddress,
       "xcmCOInternetSNMPv1": xcmCOInternetSNMPv1,
       "xcmCOInternetSNMPv2": xcmCOInternetSNMPv2,
       "xcmCOInternetSNMPv3": xcmCOInternetSNMPv3,
       "xcmCOInternetPOP3": xcmCOInternetPOP3,
       "xcmCOInternetPOP3HostName": xcmCOInternetPOP3HostName,
       "xcmCOInternetPOP3HostAddress": xcmCOInternetPOP3HostAddress,
       "xcmCOInternetPOP3PollInterval": xcmCOInternetPOP3PollInterval,
       "xcmCOInternetPOP3Subject": xcmCOInternetPOP3Subject,
       "xcmCOInternetPOP3SignatureLine": xcmCOInternetPOP3SignatureLine,
       "xcmCOInternetPOP3UserName": xcmCOInternetPOP3UserName,
       "xcmCOInternetPOP3Password": xcmCOInternetPOP3Password,
       "xcmCOInternetPOP3MaxInputText": xcmCOInternetPOP3MaxInputText,
       "xcmCOInternetPOP3MaxInputAttach": xcmCOInternetPOP3MaxInputAttach,
       "xcmCOInternetPOP3MaxOutputText": xcmCOInternetPOP3MaxOutputText,
       "xcmCOInternetPOP3MaxOutputAttach": xcmCOInternetPOP3MaxOutputAttach,
       "xcmCOInternetPOP3ConfirmRequest": xcmCOInternetPOP3ConfirmRequest,
       "xcmCOInternetPOP3ConfirmReply": xcmCOInternetPOP3ConfirmReply,
       "xcmCOInternetPOP3ConfirmTimeout": xcmCOInternetPOP3ConfirmTimeout,
       "xcmCOInternetPOP3FeatureReply": xcmCOInternetPOP3FeatureReply,
       "xcmCOInternetPOP3MailAddress": xcmCOInternetPOP3MailAddress,
       "xcmCOInternetPOP3MaxInFragments": xcmCOInternetPOP3MaxInFragments,
       "xcmCOInternetPOP3MaxOutFragments": xcmCOInternetPOP3MaxOutFragments,
       "xcmCOInternetPOP3MaxInAttachments": xcmCOInternetPOP3MaxInAttachments,
       "xcmCOInternetPOP3MaxOutAttachments": xcmCOInternetPOP3MaxOutAttachments,
       "xcmCOInternetPOP3MaxInputSize": xcmCOInternetPOP3MaxInputSize,
       "xcmCOInternetPOP3MaxOutputSize": xcmCOInternetPOP3MaxOutputSize,
       "xcmCOInternetIMAP4": xcmCOInternetIMAP4,
       "xcmCOInternetIMAP4HostName": xcmCOInternetIMAP4HostName,
       "xcmCOInternetIMAP4HostAddress": xcmCOInternetIMAP4HostAddress,
       "xcmCOInternetIMAP4PollInterval": xcmCOInternetIMAP4PollInterval,
       "xcmCOInternetIMAP4Subject": xcmCOInternetIMAP4Subject,
       "xcmCOInternetIMAP4SignatureLine": xcmCOInternetIMAP4SignatureLine,
       "xcmCOInternetIMAP4UserName": xcmCOInternetIMAP4UserName,
       "xcmCOInternetIMAP4Password": xcmCOInternetIMAP4Password,
       "xcmCOInternetIMAP4MaxInputText": xcmCOInternetIMAP4MaxInputText,
       "xcmCOInternetIMAP4MaxInputAttach": xcmCOInternetIMAP4MaxInputAttach,
       "xcmCOInternetIMAP4MaxOutputText": xcmCOInternetIMAP4MaxOutputText,
       "xcmCOInternetIMAP4MaxOutputAttach": xcmCOInternetIMAP4MaxOutputAttach,
       "xcmCOInternetIMAP4ConfirmRequest": xcmCOInternetIMAP4ConfirmRequest,
       "xcmCOInternetIMAP4ConfirmReply": xcmCOInternetIMAP4ConfirmReply,
       "xcmCOInternetIMAP4ConfirmTimeout": xcmCOInternetIMAP4ConfirmTimeout,
       "xcmCOInternetIMAP4FeatureReply": xcmCOInternetIMAP4FeatureReply,
       "xcmCOInternetIMAP4MailAddress": xcmCOInternetIMAP4MailAddress,
       "xcmCOInternetIMAP4MaxInFragments": xcmCOInternetIMAP4MaxInFragments,
       "xcmCOInternetIMAP4MaxOutFragments": xcmCOInternetIMAP4MaxOutFragments,
       "xcmCOInternetIMAP4MaxInAttachments": xcmCOInternetIMAP4MaxInAttachments,
       "xcmCOInternetIMAP4MaxOutAttachments": xcmCOInternetIMAP4MaxOutAttachments,
       "xcmCOInternetIMAP4MaxInputSize": xcmCOInternetIMAP4MaxInputSize,
       "xcmCOInternetIMAP4MaxOutputSize": xcmCOInternetIMAP4MaxOutputSize,
       "xcmCOInternetFax": xcmCOInternetFax,
       "xcmCOInternetNTP": xcmCOInternetNTP,
       "xcmCOInternetNTPHostName": xcmCOInternetNTPHostName,
       "xcmCOInternetNTPHostAddress": xcmCOInternetNTPHostAddress,
       "xcmCOInternetNTPv6HostAddress": xcmCOInternetNTPv6HostAddress,
       "xcmCOInternetNTPPort": xcmCOInternetNTPPort,
       "xcmCOInternetNTPGMTOffset": xcmCOInternetNTPGMTOffset,
       "xcmCOInternetNTPPollInterval": xcmCOInternetNTPPollInterval,
       "xcmCOInternetNTPSkewTime": xcmCOInternetNTPSkewTime,
       "xcmCOInternetSFTP": xcmCOInternetSFTP,
       "xcmCOInternetWINS": xcmCOInternetWINS,
       "xcmCOInternetWINSDomainName": xcmCOInternetWINSDomainName,
       "xcmCOInternetWINSLanguage": xcmCOInternetWINSLanguage,
       "xcmCOInternetWINSCharset": xcmCOInternetWINSCharset,
       "xcmCOInternetWINSServerName": xcmCOInternetWINSServerName,
       "xcmCOInternetWINSServerAddress": xcmCOInternetWINSServerAddress,
       "xcmCOInternetWINSServerSocket": xcmCOInternetWINSServerSocket,
       "xcmCOInternetSunOncSuite": xcmCOInternetSunOncSuite,
       "xcmCOInternetSunOncNIS": xcmCOInternetSunOncNIS,
       "xcmCOInternetSunOncPlusNIS": xcmCOInternetSunOncPlusNIS,
       "xcmCOInternetSunOncRPC": xcmCOInternetSunOncRPC,
       "xcmCOInternetSunOncPlusRPC": xcmCOInternetSunOncPlusRPC,
       "xcmCOInternetSunTiRPC": xcmCOInternetSunTiRPC,
       "xcmCOInternetHTTPS": xcmCOInternetHTTPS,
       "xcmCOInternetOsfDceSuite": xcmCOInternetOsfDceSuite,
       "xcmCOInternetOsfDceCDS": xcmCOInternetOsfDceCDS,
       "xcmCOInternetOsfDceRPC": xcmCOInternetOsfDceRPC,
       "xcmCOInternetOsfDceKerberos": xcmCOInternetOsfDceKerberos,
       "xcmCOInternetOsfDceKerberosRealm": xcmCOInternetOsfDceKerberosRealm,
       "xcmCOInternetOsfDmeSuite": xcmCOInternetOsfDmeSuite,
       "xcmCOInternetLDAP": xcmCOInternetLDAP,
       "xcmCOInternetLDAPLanguage": xcmCOInternetLDAPLanguage,
       "xcmCOInternetLDAPCharset": xcmCOInternetLDAPCharset,
       "xcmCOInternetLDAPServerName": xcmCOInternetLDAPServerName,
       "xcmCOInternetLDAPServerAddress": xcmCOInternetLDAPServerAddress,
       "xcmCOInternetLDAPServerSocket": xcmCOInternetLDAPServerSocket,
       "xcmCOInternetLDAPPollInterval": xcmCOInternetLDAPPollInterval,
       "xcmCOInternetLDAPBindDN": xcmCOInternetLDAPBindDN,
       "xcmCOInternetLDAPBindPassword": xcmCOInternetLDAPBindPassword,
       "xcmCOInternetLDAPBaseDN": xcmCOInternetLDAPBaseDN,
       "xcmCOInternetLDAPPrinterName": xcmCOInternetLDAPPrinterName,
       "xcmCOInternetLDAPPrinterClass": xcmCOInternetLDAPPrinterClass,
       "xcmCOInternetLDAPAttributeName": xcmCOInternetLDAPAttributeName,
       "xcmCOInternetLDAPAttributeType": xcmCOInternetLDAPAttributeType,
       "xcmCOInternetLDAPAttributeInt": xcmCOInternetLDAPAttributeInt,
       "xcmCOInternetLDAPAttributeStr": xcmCOInternetLDAPAttributeStr,
       "xcmCOInternetLDAPMaxSearchResult": xcmCOInternetLDAPMaxSearchResult,
       "xcmCOInternetLDAPSearchTimeout": xcmCOInternetLDAPSearchTimeout,
       "xcmCOInternetCLDAP": xcmCOInternetCLDAP,
       "xcmCOInternetSalutation": xcmCOInternetSalutation,
       "xcmCOInternetUpnpSuite": xcmCOInternetUpnpSuite,
       "xcmCOInternetUpnpSSDP": xcmCOInternetUpnpSSDP,
       "xcmCOInternetSSDPCacheTimeout": xcmCOInternetSSDPCacheTimeout,
       "xcmCOInternetSSDPTimeToLive": xcmCOInternetSSDPTimeToLive,
       "xcmCOInternetSSDPServerVersion": xcmCOInternetSSDPServerVersion,
       "xcmCOInternetUpnpGENA": xcmCOInternetUpnpGENA,
       "xcmCOInternetSLP": xcmCOInternetSLP,
       "xcmCOInternetSLPVersion": xcmCOInternetSLPVersion,
       "xcmCOInternetSLPLanguage": xcmCOInternetSLPLanguage,
       "xcmCOInternetSLPCharset": xcmCOInternetSLPCharset,
       "xcmCOInternetSLPServerName": xcmCOInternetSLPServerName,
       "xcmCOInternetSLPServerAddress": xcmCOInternetSLPServerAddress,
       "xcmCOInternetSLPServerSocket": xcmCOInternetSLPServerSocket,
       "xcmCOInternetSLPPollInterval": xcmCOInternetSLPPollInterval,
       "xcmCOInternetSLPMaxMulticastTime": xcmCOInternetSLPMaxMulticastTime,
       "xcmCOInternetSLPDAFindStartWait": xcmCOInternetSLPDAFindStartWait,
       "xcmCOInternetSLPInitialRetryWait": xcmCOInternetSLPInitialRetryWait,
       "xcmCOInternetSLPMaxUnicastTime": xcmCOInternetSLPMaxUnicastTime,
       "xcmCOInternetSLPDAHeartbeatTime": xcmCOInternetSLPDAHeartbeatTime,
       "xcmCOInternetSLPDAFindActiveWait": xcmCOInternetSLPDAFindActiveWait,
       "xcmCOInternetSLPRegPassiveWait": xcmCOInternetSLPRegPassiveWait,
       "xcmCOInternetSLPRegActiveWait": xcmCOInternetSLPRegActiveWait,
       "xcmCOInternetSLPCloseConnWait": xcmCOInternetSLPCloseConnWait,
       "xcmCOInternetSLPCacheReplyTime": xcmCOInternetSLPCacheReplyTime,
       "xcmCOInternetSLPMaxRegLifetime": xcmCOInternetSLPMaxRegLifetime,
       "xcmCOInternetSLPDAFindRetryWait": xcmCOInternetSLPDAFindRetryWait,
       "xcmCOInternetSLPMaxDARequestTime": xcmCOInternetSLPMaxDARequestTime,
       "xcmCOInternetSLPMulticastEnable": xcmCOInternetSLPMulticastEnable,
       "xcmCOInternetSLPMulticastRadius": xcmCOInternetSLPMulticastRadius,
       "xcmCOInternetSLPPathMTUSize": xcmCOInternetSLPPathMTUSize,
       "xcmCOInternetSLPScopeName": xcmCOInternetSLPScopeName,
       "xcmCOInternetSLPScopeKey": xcmCOInternetSLPScopeKey,
       "xcmCOInternetSLPAttributesEnable": xcmCOInternetSLPAttributesEnable,
       "xcmCOInternetSLPv1": xcmCOInternetSLPv1,
       "xcmCOInternetSLPv2": xcmCOInternetSLPv2,
       "xcmCOInternetWSDSuite": xcmCOInternetWSDSuite,
       "xcmCOInternetWSDiscovery": xcmCOInternetWSDiscovery,
       "xcmCOInternetWSDiscoveryMulticast": xcmCOInternetWSDiscoveryMulticast,
       "xcmCOInternetWSDiscoveryPort": xcmCOInternetWSDiscoveryPort,
       "xcmCOInternetWSXResourcePort": xcmCOInternetWSXResourcePort,
       "xcmCOInternetWSPrintPort": xcmCOInternetWSPrintPort,
       "xcmCOInternetWSScanPort": xcmCOInternetWSScanPort,
       "xcmCOInternetWSTransferPort": xcmCOInternetWSTransferPort,
       "xcmCOInternetDeallocateAllDynamicResources": xcmCOInternetDeallocateAllDynamicResources,
       "xcmCOInternetApplications": xcmCOInternetApplications,
       "xcmCOInternetDHCPv6": xcmCOInternetDHCPv6,
       "xcmCOInternetDHCPv6ConfigState": xcmCOInternetDHCPv6ConfigState,
       "xcmCOInternetDNSv6": xcmCOInternetDNSv6,
       "xcmCOInternetDNSv6DomainName": xcmCOInternetDNSv6DomainName,
       "xcmCOInternetDNSv6ServerAddress": xcmCOInternetDNSv6ServerAddress,
       "xcmCOInternetDNSv6DynamicUpdate": xcmCOInternetDNSv6DynamicUpdate,
       "xcmCOInternetDNSv6ResolutionPolicy": xcmCOInternetDNSv6ResolutionPolicy,
       "xcmCOInternetIPv6DeallocateAllDynamicResources": xcmCOInternetIPv6DeallocateAllDynamicResources,
       "xcmCOAppletalkSuite": xcmCOAppletalkSuite,
       "xcmCOAppletalkDatalinks": xcmCOAppletalkDatalinks,
       "xcmCOAppletalkLLAP": xcmCOAppletalkLLAP,
       "xcmCOAppletalkELAP": xcmCOAppletalkELAP,
       "xcmCOAppletalkTLAP": xcmCOAppletalkTLAP,
       "xcmCOAppletalkPhase": xcmCOAppletalkPhase,
       "xcmCOAppletalkDDP": xcmCOAppletalkDDP,
       "xcmCOAppletalkDDPAddress": xcmCOAppletalkDDPAddress,
       "xcmCOAppletalkDDPSocketAddress": xcmCOAppletalkDDPSocketAddress,
       "xcmCOAppletalkDDPDatalinks": xcmCOAppletalkDDPDatalinks,
       "xcmCOAppletalkAARP": xcmCOAppletalkAARP,
       "xcmCOAppletalkTransports": xcmCOAppletalkTransports,
       "xcmCOAppletalkATP": xcmCOAppletalkATP,
       "xcmCOAppletalkADSP": xcmCOAppletalkADSP,
       "xcmCOAppletalkRTMP": xcmCOAppletalkRTMP,
       "xcmCOAppletalkAEP": xcmCOAppletalkAEP,
       "xcmCOAppletalkNBP": xcmCOAppletalkNBP,
       "xcmCOAppletalkNBPHostName": xcmCOAppletalkNBPHostName,
       "xcmCOAppletalkNBPLanguage": xcmCOAppletalkNBPLanguage,
       "xcmCOAppletalkNBPCharset": xcmCOAppletalkNBPCharset,
       "xcmCOAppletalkNBPObject": xcmCOAppletalkNBPObject,
       "xcmCOAppletalkNBPType": xcmCOAppletalkNBPType,
       "xcmCOAppletalkNBPZone": xcmCOAppletalkNBPZone,
       "xcmCOAppletalkNBPNetwork": xcmCOAppletalkNBPNetwork,
       "xcmCOAppletalkNBPNode": xcmCOAppletalkNBPNode,
       "xcmCOAppletalkNBPSocket": xcmCOAppletalkNBPSocket,
       "xcmCOAppletalkNBPZoneToNetworks": xcmCOAppletalkNBPZoneToNetworks,
       "xcmCOAppletalkASP": xcmCOAppletalkASP,
       "xcmCOAppletalkZIP": xcmCOAppletalkZIP,
       "xcmCOAppletalkPAP": xcmCOAppletalkPAP,
       "xcmCOAppletalkPAPHostName": xcmCOAppletalkPAPHostName,
       "xcmCOAppletalkPAPHostAddress": xcmCOAppletalkPAPHostAddress,
       "xcmCOAppletalkPAPListenSocket": xcmCOAppletalkPAPListenSocket,
       "xcmCOAppletalkPAPMaxClients": xcmCOAppletalkPAPMaxClients,
       "xcmCOAppletalkPAPMaxPrinters": xcmCOAppletalkPAPMaxPrinters,
       "xcmCOAppletalkPAPObject": xcmCOAppletalkPAPObject,
       "xcmCOAppletalkPAPType": xcmCOAppletalkPAPType,
       "xcmCOAppletalkPAPZone": xcmCOAppletalkPAPZone,
       "xcmCOAppletalkPAPNetwork": xcmCOAppletalkPAPNetwork,
       "xcmCOAppletalkPAPNode": xcmCOAppletalkPAPNode,
       "xcmCOAppletalkPAPSpool": xcmCOAppletalkPAPSpool,
       "xcmCOAppletalkPAPMaxSpool": xcmCOAppletalkPAPMaxSpool,
       "xcmCOAppletalkPAPJobTimeout": xcmCOAppletalkPAPJobTimeout,
       "xcmCOAppletalkPAPAutoSwitch": xcmCOAppletalkPAPAutoSwitch,
       "xcmCOAppletalkPAPBinaryPS": xcmCOAppletalkPAPBinaryPS,
       "xcmCOAppletalkPAPDefaultPDL": xcmCOAppletalkPAPDefaultPDL,
       "xcmCOAppletalkSNMP": xcmCOAppletalkSNMP,
       "xcmCOAppletalkSNMPv1": xcmCOAppletalkSNMPv1,
       "xcmCOAppletalkSNMPv2": xcmCOAppletalkSNMPv2,
       "xcmCOAppletalkSNMPv3": xcmCOAppletalkSNMPv3,
       "xcmCOAppletalkAFP": xcmCOAppletalkAFP,
       "xcmCOAppletalkPS": xcmCOAppletalkPS,
       "xcmCOAppletalkApplications": xcmCOAppletalkApplications,
       "xcmCONetwareSuite": xcmCONetwareSuite,
       "xcmCONetwareDatalinks": xcmCONetwareDatalinks,
       "xcmCONetwareIPX": xcmCONetwareIPX,
       "xcmCONetwareIPXAddress": xcmCONetwareIPXAddress,
       "xcmCONetwareIPXSocketAddress": xcmCONetwareIPXSocketAddress,
       "xcmCONetwareIPXDatalinks": xcmCONetwareIPXDatalinks,
       "xcmCONetwareIP": xcmCONetwareIP,
       "xcmCONetwareTransports": xcmCONetwareTransports,
       "xcmCONetwareSPX": xcmCONetwareSPX,
       "xcmCONetwareRIP": xcmCONetwareRIP,
       "xcmCONetwareEcho": xcmCONetwareEcho,
       "xcmCONetwareNCP": xcmCONetwareNCP,
       "xcmCONetwareNetbios": xcmCONetwareNetbios,
       "xcmCONetwarePServer": xcmCONetwarePServer,
       "xcmCONetwarePServerName": xcmCONetwarePServerName,
       "xcmCONetwarePServerPassword": xcmCONetwarePServerPassword,
       "xcmCONetwarePServerQueueName": xcmCONetwarePServerQueueName,
       "xcmCONetwarePServerPollInterval": xcmCONetwarePServerPollInterval,
       "xcmCONetwarePServerFindFServer": xcmCONetwarePServerFindFServer,
       "xcmCONetwarePServerMaxFServers": xcmCONetwarePServerMaxFServers,
       "xcmCONetwarePServerNotify": xcmCONetwarePServerNotify,
       "xcmCONetwarePServerNotifyLocale": xcmCONetwarePServerNotifyLocale,
       "xcmCONetwarePServerMaxPrinters": xcmCONetwarePServerMaxPrinters,
       "xcmCONetwarePServerSuspendPoll": xcmCONetwarePServerSuspendPoll,
       "xcmCONetwarePServerSuspendPollInterval": xcmCONetwarePServerSuspendPollInterval,
       "xcmCONetwarePServerSpool": xcmCONetwarePServerSpool,
       "xcmCONetwarePServerMaxSpool": xcmCONetwarePServerMaxSpool,
       "xcmCONetwarePServerJobTimeout": xcmCONetwarePServerJobTimeout,
       "xcmCONetwarePServerAutoSwitch": xcmCONetwarePServerAutoSwitch,
       "xcmCONetwarePServerBinaryPS": xcmCONetwarePServerBinaryPS,
       "xcmCONetwarePServerDefaultPDL": xcmCONetwarePServerDefaultPDL,
       "xcmCONetwarePServerConfigTimeout": xcmCONetwarePServerConfigTimeout,
       "xcmCONetwareFServer": xcmCONetwareFServer,
       "xcmCONetwareFServerName": xcmCONetwareFServerName,
       "xcmCONetwareFServerPassword": xcmCONetwareFServerPassword,
       "xcmCONetwareFServerAddress": xcmCONetwareFServerAddress,
       "xcmCONetwareMHS": xcmCONetwareMHS,
       "xcmCONetwareBindery": xcmCONetwareBindery,
       "xcmCONetwareBinderyLanguage": xcmCONetwareBinderyLanguage,
       "xcmCONetwareBinderyCharset": xcmCONetwareBinderyCharset,
       "xcmCONetwareNDS": xcmCONetwareNDS,
       "xcmCONetwareNDSTreeName": xcmCONetwareNDSTreeName,
       "xcmCONetwareNDSContext": xcmCONetwareNDSContext,
       "xcmCONetwareNDSLanguage": xcmCONetwareNDSLanguage,
       "xcmCONetwareNDSCharset": xcmCONetwareNDSCharset,
       "xcmCONetwareRPrinter": xcmCONetwareRPrinter,
       "xcmCONetwareRPrinterName": xcmCONetwareRPrinterName,
       "xcmCONetwareRPrinterNumber": xcmCONetwareRPrinterNumber,
       "xcmCONetwareRPrinterPollInterval": xcmCONetwareRPrinterPollInterval,
       "xcmCONetwareRPrinterJobTimeout": xcmCONetwareRPrinterJobTimeout,
       "xcmCONetwareRPrinterAutoSwitch": xcmCONetwareRPrinterAutoSwitch,
       "xcmCONetwareRPrinterBinaryPS": xcmCONetwareRPrinterBinaryPS,
       "xcmCONetwareRPrinterDefaultPDL": xcmCONetwareRPrinterDefaultPDL,
       "xcmCONetwareSNMP": xcmCONetwareSNMP,
       "xcmCONetwareSNMPv1": xcmCONetwareSNMPv1,
       "xcmCONetwareSNMPv2": xcmCONetwareSNMPv2,
       "xcmCONetwareSNMPv3": xcmCONetwareSNMPv3,
       "xcmCONetwareSAP": xcmCONetwareSAP,
       "xcmCONetwareSAPInterval": xcmCONetwareSAPInterval,
       "xcmCONetwareSAPNumber": xcmCONetwareSAPNumber,
       "xcmCONetwareSAPValueString": xcmCONetwareSAPValueString,
       "xcmCONetwareSAPUnitName": xcmCONetwareSAPUnitName,
       "xcmCONetwareSAPFormatID": xcmCONetwareSAPFormatID,
       "xcmCONetwareSAPSuspend": xcmCONetwareSAPSuspend,
       "xcmCONetwareSAPSuspendInterval": xcmCONetwareSAPSuspendInterval,
       "xcmCONetwareNDSIP": xcmCONetwareNDSIP,
       "xcmCONetwareNDSIPHostname": xcmCONetwareNDSIPHostname,
       "xcmCONetwareNDSIPAddress": xcmCONetwareNDSIPAddress,
       "xcmCONetwareNDSIPUseHostname": xcmCONetwareNDSIPUseHostname,
       "xcmCONetwareApplications": xcmCONetwareApplications,
       "xcmCOVinesSuite": xcmCOVinesSuite,
       "xcmCOVinesDatalinks": xcmCOVinesDatalinks,
       "xcmCOVinesVIP": xcmCOVinesVIP,
       "xcmCOVinesVICP": xcmCOVinesVICP,
       "xcmCOVinesVARP": xcmCOVinesVARP,
       "xcmCOVinesIP": xcmCOVinesIP,
       "xcmCOVinesICMP": xcmCOVinesICMP,
       "xcmCOVinesARP": xcmCOVinesARP,
       "xcmCOVinesVRTP": xcmCOVinesVRTP,
       "xcmCOVinesTransports": xcmCOVinesTransports,
       "xcmCOVinesVIPC": xcmCOVinesVIPC,
       "xcmCOVinesVSPP": xcmCOVinesVSPP,
       "xcmCOVinesUDP": xcmCOVinesUDP,
       "xcmCOVinesTCP": xcmCOVinesTCP,
       "xcmCOVinesNetRPC": xcmCOVinesNetRPC,
       "xcmCOVinesSocket": xcmCOVinesSocket,
       "xcmCOVinesNetbios": xcmCOVinesNetbios,
       "xcmCOVinesApplications": xcmCOVinesApplications,
       "xcmCOVinesPrint": xcmCOVinesPrint,
       "xcmCOVinesPrintName": xcmCOVinesPrintName,
       "xcmCOVinesPrintPassword": xcmCOVinesPrintPassword,
       "xcmCOVinesPrintPollInterval": xcmCOVinesPrintPollInterval,
       "xcmCOVinesPrintMaxServers": xcmCOVinesPrintMaxServers,
       "xcmCOVinesPrintServerName": xcmCOVinesPrintServerName,
       "xcmCOVinesPrintSpool": xcmCOVinesPrintSpool,
       "xcmCOVinesPrintMaxSpool": xcmCOVinesPrintMaxSpool,
       "xcmCOVinesPrintJobTimeout": xcmCOVinesPrintJobTimeout,
       "xcmCOVinesPrintAutoSwitch": xcmCOVinesPrintAutoSwitch,
       "xcmCOVinesPrintBinaryPS": xcmCOVinesPrintBinaryPS,
       "xcmCOVinesPrintDefaultPDL": xcmCOVinesPrintDefaultPDL,
       "xcmCOVinesFiling": xcmCOVinesFiling,
       "xcmCOVinesMail": xcmCOVinesMail,
       "xcmCOVinesStreetTalk": xcmCOVinesStreetTalk,
       "xcmCOVinesStreetTalkLanguage": xcmCOVinesStreetTalkLanguage,
       "xcmCOVinesStreetTalkCharset": xcmCOVinesStreetTalkCharset,
       "xcmCONetbiosSuite": xcmCONetbiosSuite,
       "xcmCONetbiosDatalinks": xcmCONetbiosDatalinks,
       "xcmCONetbiosTransports": xcmCONetbiosTransports,
       "xcmCONetbiosNBP": xcmCONetbiosNBP,
       "xcmCONetbiosNBPName": xcmCONetbiosNBPName,
       "xcmCONetbiosNBPGroupName": xcmCONetbiosNBPGroupName,
       "xcmCONetbiosNBPPassword": xcmCONetbiosNBPPassword,
       "xcmCONetbiosNBPService": xcmCONetbiosNBPService,
       "xcmCONetbiosNBPRemark": xcmCONetbiosNBPRemark,
       "xcmCONetbiosNBPServiceRemark": xcmCONetbiosNBPServiceRemark,
       "xcmCONetbiosNBPIPCRemark": xcmCONetbiosNBPIPCRemark,
       "xcmCONetbiosNBPLanguage": xcmCONetbiosNBPLanguage,
       "xcmCONetbiosNBPCharset": xcmCONetbiosNBPCharset,
       "xcmCONetbiosNBPOverNetbeui": xcmCONetbiosNBPOverNetbeui,
       "xcmCONetbiosNBPOverInternet": xcmCONetbiosNBPOverInternet,
       "xcmCONetbiosNBPOverNetware": xcmCONetbiosNBPOverNetware,
       "xcmCONetbiosSNMP": xcmCONetbiosSNMP,
       "xcmCONetbiosSNMPv1": xcmCONetbiosSNMPv1,
       "xcmCONetbiosSNMPv2": xcmCONetbiosSNMPv2,
       "xcmCONetbiosSNMPv3": xcmCONetbiosSNMPv3,
       "xcmCONetbiosIntEndNode": xcmCONetbiosIntEndNode,
       "xcmCONetbiosIntEndNodeAddress": xcmCONetbiosIntEndNodeAddress,
       "xcmCONetbiosIntEndNodeSource": xcmCONetbiosIntEndNodeSource,
       "xcmCONetbiosIntNodeType": xcmCONetbiosIntNodeType,
       "xcmCONetbiosIntNodeTypeSource": xcmCONetbiosIntNodeTypeSource,
       "xcmCONetbiosIntNodeScope": xcmCONetbiosIntNodeScope,
       "xcmCONetbiosIntNodeScopeSource": xcmCONetbiosIntNodeScopeSource,
       "xcmCONetbiosIntNameServer": xcmCONetbiosIntNameServer,
       "xcmCONetbiosIntNameServerAddress": xcmCONetbiosIntNameServerAddress,
       "xcmCONetbiosIntNameServerSource": xcmCONetbiosIntNameServerSource,
       "xcmCONetbiosIntDistServer": xcmCONetbiosIntDistServer,
       "xcmCONetbiosIntDistServerAddress": xcmCONetbiosIntDistServerAddress,
       "xcmCONetbiosIntDistServerSource": xcmCONetbiosIntDistServerSource,
       "xcmCONetbiosSAP": xcmCONetbiosSAP,
       "xcmCONetbiosSAPInterval": xcmCONetbiosSAPInterval,
       "xcmCONetbiosApplications": xcmCONetbiosApplications,
       "xcmCONetbiosSMB": xcmCONetbiosSMB,
       "xcmCONetbiosSMBPClient": xcmCONetbiosSMBPClient,
       "xcmCONetbiosSMBPClientMaxConns": xcmCONetbiosSMBPClientMaxConns,
       "xcmCONetbiosSMBPClientSpool": xcmCONetbiosSMBPClientSpool,
       "xcmCONetbiosSMBPClientMaxSpool": xcmCONetbiosSMBPClientMaxSpool,
       "xcmCONetbiosSMBPClientJobTimeout": xcmCONetbiosSMBPClientJobTimeout,
       "xcmCONetbiosSMBPClientAutoSwitch": xcmCONetbiosSMBPClientAutoSwitch,
       "xcmCONetbiosSMBPClientBinaryPS": xcmCONetbiosSMBPClientBinaryPS,
       "xcmCONetbiosSMBPClientDefaultPDL": xcmCONetbiosSMBPClientDefaultPDL,
       "xcmCONetbiosSMBPServer": xcmCONetbiosSMBPServer,
       "xcmCONetbiosSMBPServerMaxConns": xcmCONetbiosSMBPServerMaxConns,
       "xcmCONetbiosSMBPServerSpool": xcmCONetbiosSMBPServerSpool,
       "xcmCONetbiosSMBPServerMaxSpool": xcmCONetbiosSMBPServerMaxSpool,
       "xcmCONetbiosSMBPServerJobTimeout": xcmCONetbiosSMBPServerJobTimeout,
       "xcmCONetbiosSMBPServerAutoSwitch": xcmCONetbiosSMBPServerAutoSwitch,
       "xcmCONetbiosSMBPServerBinaryPS": xcmCONetbiosSMBPServerBinaryPS,
       "xcmCONetbiosSMBPServerDefaultPDL": xcmCONetbiosSMBPServerDefaultPDL,
       "xcmCONetbiosSMBFClient": xcmCONetbiosSMBFClient,
       "xcmCONetbiosSMBFServer": xcmCONetbiosSMBFServer,
       "xcmCONetbiosSMBFServerName": xcmCONetbiosSMBFServerName,
       "xcmCONetbiosSMBDomain": xcmCONetbiosSMBDomain,
       "xcmCONetbeuiSuite": xcmCONetbeuiSuite,
       "xcmCONetbeuiDatalinks": xcmCONetbeuiDatalinks,
       "xcmCONetbeuiLLC": xcmCONetbeuiLLC,
       "xcmCONetbeuiDLC": xcmCONetbeuiDLC,
       "xcmCOSerialSuite": xcmCOSerialSuite,
       "xcmCOSerialPhysical": xcmCOSerialPhysical,
       "xcmCOSerialSignalType": xcmCOSerialSignalType,
       "xcmCOSerialSignalOverride": xcmCOSerialSignalOverride,
       "xcmCOSerialSignalDetected": xcmCOSerialSignalDetected,
       "xcmCOSerialSignalAdaptive": xcmCOSerialSignalAdaptive,
       "xcmCOSerialSignalSupport": xcmCOSerialSignalSupport,
       "xcmCOSerialDevice": xcmCOSerialDevice,
       "xcmCOSerialDeviceName": xcmCOSerialDeviceName,
       "xcmCOSerialSpeed": xcmCOSerialSpeed,
       "xcmCOSerialSpeedOverride": xcmCOSerialSpeedOverride,
       "xcmCOSerialSpeedDetected": xcmCOSerialSpeedDetected,
       "xcmCOSerialSpeedAdaptive": xcmCOSerialSpeedAdaptive,
       "xcmCOSerialSpeedSupport": xcmCOSerialSpeedSupport,
       "xcmCOSerialMinSpeed": xcmCOSerialMinSpeed,
       "xcmCOSerialMaxSpeed": xcmCOSerialMaxSpeed,
       "xcmCOSerialBidirectional": xcmCOSerialBidirectional,
       "xcmCOSerialInputTimeout": xcmCOSerialInputTimeout,
       "xcmCOSerialOutputTimeout": xcmCOSerialOutputTimeout,
       "xcmCOSerialConnectorType": xcmCOSerialConnectorType,
       "xcmCOSerialConnectorOverride": xcmCOSerialConnectorOverride,
       "xcmCOSerialConnectorDetected": xcmCOSerialConnectorDetected,
       "xcmCOSerialConnectorAdaptive": xcmCOSerialConnectorAdaptive,
       "xcmCOSerialMinInputChars": xcmCOSerialMinInputChars,
       "xcmCOSerialMaxInputChars": xcmCOSerialMaxInputChars,
       "xcmCOSerialParity": xcmCOSerialParity,
       "xcmCOSerialDataBits": xcmCOSerialDataBits,
       "xcmCOSerialFlowControl": xcmCOSerialFlowControl,
       "xcmCOSerialStartBits": xcmCOSerialStartBits,
       "xcmCOSerialStopBits": xcmCOSerialStopBits,
       "xcmCOSerialInputPrime": xcmCOSerialInputPrime,
       "xcmCOSerialDTR": xcmCOSerialDTR,
       "xcmCOSerialDSR": xcmCOSerialDSR,
       "xcmCOSerialCTS": xcmCOSerialCTS,
       "xcmCOSerialRTS": xcmCOSerialRTS,
       "xcmCOSerialDatalinks": xcmCOSerialDatalinks,
       "xcmCOSerialProtocol": xcmCOSerialProtocol,
       "xcmCOParallelSuite": xcmCOParallelSuite,
       "xcmCOParallelPhysical": xcmCOParallelPhysical,
       "xcmCOParallelSignalType": xcmCOParallelSignalType,
       "xcmCOParallelSignalOverride": xcmCOParallelSignalOverride,
       "xcmCOParallelSignalDetected": xcmCOParallelSignalDetected,
       "xcmCOParallelSignalAdaptive": xcmCOParallelSignalAdaptive,
       "xcmCOParallelSignalSupport": xcmCOParallelSignalSupport,
       "xcmCOParallelDevice": xcmCOParallelDevice,
       "xcmCOParallelDeviceName": xcmCOParallelDeviceName,
       "xcmCOParallelDeviceID": xcmCOParallelDeviceID,
       "xcmCOParallelSpeed": xcmCOParallelSpeed,
       "xcmCOParallelSpeedOverride": xcmCOParallelSpeedOverride,
       "xcmCOParallelSpeedDetected": xcmCOParallelSpeedDetected,
       "xcmCOParallelSpeedAdaptive": xcmCOParallelSpeedAdaptive,
       "xcmCOParallelSpeedSupport": xcmCOParallelSpeedSupport,
       "xcmCOParallelMinSpeed": xcmCOParallelMinSpeed,
       "xcmCOParallelMaxSpeed": xcmCOParallelMaxSpeed,
       "xcmCOParallelBidirectional": xcmCOParallelBidirectional,
       "xcmCOParallelInputTimeout": xcmCOParallelInputTimeout,
       "xcmCOParallelOutputTimeout": xcmCOParallelOutputTimeout,
       "xcmCOParallelConnectorType": xcmCOParallelConnectorType,
       "xcmCOParallelConnectorOverride": xcmCOParallelConnectorOverride,
       "xcmCOParallelConnectorDetected": xcmCOParallelConnectorDetected,
       "xcmCOParallelConnectorAdaptive": xcmCOParallelConnectorAdaptive,
       "xcmCOParallelMinInputChars": xcmCOParallelMinInputChars,
       "xcmCOParallelMaxInputChars": xcmCOParallelMaxInputChars,
       "xcmCOParallelParity": xcmCOParallelParity,
       "xcmCOParallelDataBits": xcmCOParallelDataBits,
       "xcmCOParallelFlowControl": xcmCOParallelFlowControl,
       "xcmCOParallelInputPrime": xcmCOParallelInputPrime,
       "xcmCOParallelHandshake": xcmCOParallelHandshake,
       "xcmCOParallelDataStrobe": xcmCOParallelDataStrobe,
       "xcmCOParallelDatalinks": xcmCOParallelDatalinks,
       "xcmCOParallelProtocol": xcmCOParallelProtocol,
       "xcmCODirectPrintSuite": xcmCODirectPrintSuite,
       "xcmCODirectPrintPhysical": xcmCODirectPrintPhysical,
       "xcmCODirectPrintDatalinks": xcmCODirectPrintDatalinks,
       "xcmCODirectPrintProtocol": xcmCODirectPrintProtocol,
       "xcmCOUsbSuite": xcmCOUsbSuite,
       "xcmCOUsbPhysical": xcmCOUsbPhysical,
       "xcmCOUsbDevice": xcmCOUsbDevice,
       "xcmCOUsbDeviceName": xcmCOUsbDeviceName,
       "xcmCOUsbSpeed": xcmCOUsbSpeed,
       "xcmCOUsbSpeedOverride": xcmCOUsbSpeedOverride,
       "xcmCOUsbSpeedDetected": xcmCOUsbSpeedDetected,
       "xcmCOUsbSpeedAdaptive": xcmCOUsbSpeedAdaptive,
       "xcmCOUsbSpeedSupport": xcmCOUsbSpeedSupport,
       "xcmCOUsbMinSpeed": xcmCOUsbMinSpeed,
       "xcmCOUsbMaxSpeed": xcmCOUsbMaxSpeed,
       "xcmCOUsbBidirectional": xcmCOUsbBidirectional,
       "xcmCOUsbInputTimeout": xcmCOUsbInputTimeout,
       "xcmCOUsbOutputTimeout": xcmCOUsbOutputTimeout,
       "xcmCOUsbMinInputChars": xcmCOUsbMinInputChars,
       "xcmCOUsbMaxInputChars": xcmCOUsbMaxInputChars,
       "xcmCOUsbDatalinks": xcmCOUsbDatalinks,
       "xcmCOUsbProtocol": xcmCOUsbProtocol,
       "xCmCommsConfigDummy": xCmCommsConfigDummy,
       "xCmSnmpNetbiosAddress": xCmSnmpNetbiosAddress,
       "xCmCommsConfigGroupSupport": xCmCommsConfigGroupSupport,
       "xCmCommsDirRecordType": xCmCommsDirRecordType,
       "xCmCommsDirAttributeType": xCmCommsDirAttributeType,
       "xCmCommsLDAPAttributeType": xCmCommsLDAPAttributeType,
       "xCmSnmpIPHostnameAddress": xCmSnmpIPHostnameAddress}
)
