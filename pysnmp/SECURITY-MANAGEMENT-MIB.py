# SNMP MIB module (SECURITY-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SECURITY-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:15 2024
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

(avEntPhySeverity,) = mibBuilder.importSymbols(
    "AVAYA-ENTITY-MIB",
    "avEntPhySeverity")

(lsg,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "lsg")

(cmgTrapLocation,
 cmgTrapModule,
 cmgTrapOnBoard,
 cmgTrapOnIccMissing,
 cmgTrapSubsystem) = mibBuilder.importSymbols(
    "G700-MG-MIB",
    "cmgTrapLocation",
    "cmgTrapModule",
    "cmgTrapOnBoard",
    "cmgTrapOnIccMissing",
    "cmgTrapSubsystem")

(ifIndex,
 ifName,
 ifPhysAddress,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName",
    "ifPhysAddress",
    "ifType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(genAppFileId,
 genAppFileName,
 genAppFileVersionNumber,
 genOpLastFailureDisplay) = mibBuilder.importSymbols(
    "LOAD-MIB",
    "genAppFileId",
    "genAppFileName",
    "genAppFileVersionNumber",
    "genOpLastFailureDisplay")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

secMngModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1)
)
secMngModule.setRevisions(
        ("2006-03-13 18:49",
         "2005-11-23 13:21",
         "2005-01-11 16:54",
         "2005-03-02 16:02",
         "2005-04-20 16:06",
         "2006-02-27 19:16",
         "2010-03-23 10:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OnOffType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )



class ServiceStateType(Integer32, TextualConvention):
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
        *(("notSupported", 3),
          ("off", 2),
          ("on", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AvayaSecurity_ObjectIdentity = ObjectIdentity
avayaSecurity = _AvayaSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14)
)
_SecMode_Type = OnOffType
_SecMode_Object = MibScalar
secMode = _SecMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 1),
    _SecMode_Type()
)
secMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secMode.setStatus("current")
_SecTcpSynCookies_ObjectIdentity = ObjectIdentity
secTcpSynCookies = _SecTcpSynCookies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 2)
)
_SecTcpSynCkiOpState_Type = OnOffType
_SecTcpSynCkiOpState_Object = MibScalar
secTcpSynCkiOpState = _SecTcpSynCkiOpState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 2, 1),
    _SecTcpSynCkiOpState_Type()
)
secTcpSynCkiOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secTcpSynCkiOpState.setStatus("current")
_SecTcpSynCkiCfgState_Type = OnOffType
_SecTcpSynCkiCfgState_Object = MibScalar
secTcpSynCkiCfgState = _SecTcpSynCkiCfgState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 2, 2),
    _SecTcpSynCkiCfgState_Type()
)
secTcpSynCkiCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secTcpSynCkiCfgState.setStatus("current")
_SecMngProtoTable_Object = MibTable
secMngProtoTable = _SecMngProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    secMngProtoTable.setStatus("current")
_SecMngProtoEntry_Object = MibTableRow
secMngProtoEntry = _SecMngProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 3, 1)
)
secMngProtoEntry.setIndexNames(
    (0, "SECURITY-MANAGEMENT-MIB", "secMngProtoId"),
)
if mibBuilder.loadTexts:
    secMngProtoEntry.setStatus("current")


class _SecMngProtoId_Type(Integer32):
    """Custom type secMngProtoId based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("arpInspection", 23),
          ("dhcp", 17),
          ("dnsRelay", 22),
          ("dnsResolver", 18),
          ("ftpClient", 15),
          ("http", 6),
          ("https", 7),
          ("icmp", 10),
          ("icmpEcho", 14),
          ("icmpRedirection", 9),
          ("recoveryPassword", 11),
          ("scpClient", 19),
          ("scpConfigFiles", 1),
          ("scpImageFiles", 2),
          ("snmpv1", 13),
          ("snmpv3", 5),
          ("ssh", 3),
          ("sshClient", 12),
          ("telnet", 4),
          ("telnetClient", 8),
          ("telnetServices", 21),
          ("tftp", 16),
          ("tftpClient", 20))
    )


_SecMngProtoId_Type.__name__ = "Integer32"
_SecMngProtoId_Object = MibTableColumn
secMngProtoId = _SecMngProtoId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 3, 1, 1),
    _SecMngProtoId_Type()
)
secMngProtoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secMngProtoId.setStatus("current")
_SecMngProtoStatus_Type = ServiceStateType
_SecMngProtoStatus_Object = MibTableColumn
secMngProtoStatus = _SecMngProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 3, 1, 2),
    _SecMngProtoStatus_Type()
)
secMngProtoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secMngProtoStatus.setStatus("current")
_SecMngConformance_ObjectIdentity = ObjectIdentity
secMngConformance = _SecMngConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 4)
)
_SecMngGroups_ObjectIdentity = ObjectIdentity
secMngGroups = _SecMngGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 4, 1)
)
_SecMngCompliance_ObjectIdentity = ObjectIdentity
secMngCompliance = _SecMngCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 4, 2)
)
_LsgLicManagement_ObjectIdentity = ObjectIdentity
lsgLicManagement = _LsgLicManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    lsgLicManagement.setStatus("current")
_LsgLicMngTable_Object = MibTable
lsgLicMngTable = _LsgLicMngTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lsgLicMngTable.setStatus("current")
_LsgLicMngEntry_Object = MibTableRow
lsgLicMngEntry = _LsgLicMngEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1, 1)
)
lsgLicMngEntry.setIndexNames(
    (0, "SECURITY-MANAGEMENT-MIB", "lsgLicMngFeatureKeyword"),
)
if mibBuilder.loadTexts:
    lsgLicMngEntry.setStatus("current")
_LsgLicMngFeatureKeyword_Type = OctetString
_LsgLicMngFeatureKeyword_Object = MibTableColumn
lsgLicMngFeatureKeyword = _LsgLicMngFeatureKeyword_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1, 1, 1),
    _LsgLicMngFeatureKeyword_Type()
)
lsgLicMngFeatureKeyword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lsgLicMngFeatureKeyword.setStatus("current")


class _LsgLicMngFeatureType_Type(Integer32):
    """Custom type lsgLicMngFeatureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onOffFeature", 1),
          ("quantifiableFeature", 2))
    )


_LsgLicMngFeatureType_Type.__name__ = "Integer32"
_LsgLicMngFeatureType_Object = MibTableColumn
lsgLicMngFeatureType = _LsgLicMngFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1, 1, 2),
    _LsgLicMngFeatureType_Type()
)
lsgLicMngFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsgLicMngFeatureType.setStatus("current")
_LsgLicMngAdminStatus_Type = OnOffType
_LsgLicMngAdminStatus_Object = MibTableColumn
lsgLicMngAdminStatus = _LsgLicMngAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1, 1, 3),
    _LsgLicMngAdminStatus_Type()
)
lsgLicMngAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsgLicMngAdminStatus.setStatus("current")
_LsgLicMngOperStatus_Type = OnOffType
_LsgLicMngOperStatus_Object = MibTableColumn
lsgLicMngOperStatus = _LsgLicMngOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1, 1, 4),
    _LsgLicMngOperStatus_Type()
)
lsgLicMngOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsgLicMngOperStatus.setStatus("current")
_LsgLicMngCountedValue_Type = Unsigned32
_LsgLicMngCountedValue_Object = MibTableColumn
lsgLicMngCountedValue = _LsgLicMngCountedValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1, 1, 5),
    _LsgLicMngCountedValue_Type()
)
lsgLicMngCountedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsgLicMngCountedValue.setStatus("current")


class _LsgLicMngLastError_Type(Integer32):
    """Custom type lsgLicMngLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("licNoError", 2)
    )


_LsgLicMngLastError_Type.__name__ = "Integer32"
_LsgLicMngLastError_Object = MibTableColumn
lsgLicMngLastError = _LsgLicMngLastError_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 1, 1, 6),
    _LsgLicMngLastError_Type()
)
lsgLicMngLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsgLicMngLastError.setStatus("current")
_LsgLicMngConformance_ObjectIdentity = ObjectIdentity
lsgLicMngConformance = _LsgLicMngConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 20)
)
if mibBuilder.loadTexts:
    lsgLicMngConformance.setStatus("current")
_LsgLicMngGroups_ObjectIdentity = ObjectIdentity
lsgLicMngGroups = _LsgLicMngGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 20, 1)
)
if mibBuilder.loadTexts:
    lsgLicMngGroups.setStatus("current")
_Fips140_ObjectIdentity = ObjectIdentity
fips140 = _Fips140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 6)
)
if mibBuilder.loadTexts:
    fips140.setStatus("current")
_FipsEnhancedSecurityFlg_Type = OnOffType
_FipsEnhancedSecurityFlg_Object = MibScalar
fipsEnhancedSecurityFlg = _FipsEnhancedSecurityFlg_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 6, 1),
    _FipsEnhancedSecurityFlg_Type()
)
fipsEnhancedSecurityFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fipsEnhancedSecurityFlg.setStatus("current")
_AvMssNotifications_ObjectIdentity = ObjectIdentity
avMssNotifications = _AvMssNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7)
)
if mibBuilder.loadTexts:
    avMssNotifications.setStatus("current")
_AvMssNotificationPrefix_ObjectIdentity = ObjectIdentity
avMssNotificationPrefix = _AvMssNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 0)
)
if mibBuilder.loadTexts:
    avMssNotificationPrefix.setStatus("current")


class _AvMSSNotificationRate_Type(Integer32):
    """Custom type avMSSNotificationRate based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 28800),
    )


_AvMSSNotificationRate_Type.__name__ = "Integer32"
_AvMSSNotificationRate_Object = MibScalar
avMSSNotificationRate = _AvMSSNotificationRate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 2),
    _AvMSSNotificationRate_Type()
)
avMSSNotificationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avMSSNotificationRate.setStatus("current")
if mibBuilder.loadTexts:
    avMSSNotificationRate.setUnits("Second")
_AvMSSVarbinds_ObjectIdentity = ObjectIdentity
avMSSVarbinds = _AvMSSVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4)
)
if mibBuilder.loadTexts:
    avMSSVarbinds.setStatus("current")


class _AvMSSVarbindsDoSType_Type(Integer32):
    """Custom type avMSSVarbindsDoSType based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105)
        )
    )
    namedValues = NamedValues(
        *(("avMSSDoSFraggleAttack", 9),
          ("avMSSDoSICMPReflectAttack", 3),
          ("avMSSDoSLandAttack", 2),
          ("avMSSDoSMalFragmentIP", 10),
          ("avMSSDoSMalformedARPs", 1),
          ("avMSSDoSMalformedIP", 6),
          ("avMSSDoSSmurfAttack", 8),
          ("avMSSDoSSynFlood", 7),
          ("avMSSDoSUknownPort", 4),
          ("avMSSDoSUrgTCPOption", 5),
          ("avMSSSpoofedIP", 11),
          ("avMSSUnknownL4Protocol", 12),
          ("avMSSUserDefinedDoSAttack100", 100),
          ("avMSSUserDefinedDoSAttack101", 101),
          ("avMSSUserDefinedDoSAttack102", 102),
          ("avMSSUserDefinedDoSAttack103", 103),
          ("avMSSUserDefinedDoSAttack104", 104),
          ("avMSSUserDefinedDoSAttack105", 105),
          ("avMSSunAuthenticatedAccess", 13))
    )


_AvMSSVarbindsDoSType_Type.__name__ = "Integer32"
_AvMSSVarbindsDoSType_Object = MibScalar
avMSSVarbindsDoSType = _AvMSSVarbindsDoSType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 1),
    _AvMSSVarbindsDoSType_Type()
)
avMSSVarbindsDoSType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsDoSType.setStatus("current")
_AvMSSVarbindsDescription_Type = DisplayString
_AvMSSVarbindsDescription_Object = MibScalar
avMSSVarbindsDescription = _AvMSSVarbindsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 2),
    _AvMSSVarbindsDescription_Type()
)
avMSSVarbindsDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsDescription.setStatus("current")
_AvMSSVarbindsSrcAddr_Type = IpAddress
_AvMSSVarbindsSrcAddr_Object = MibScalar
avMSSVarbindsSrcAddr = _AvMSSVarbindsSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 3),
    _AvMSSVarbindsSrcAddr_Type()
)
avMSSVarbindsSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsSrcAddr.setStatus("current")
_AvMSSVarbindsDstAddr_Type = IpAddress
_AvMSSVarbindsDstAddr_Object = MibScalar
avMSSVarbindsDstAddr = _AvMSSVarbindsDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 4),
    _AvMSSVarbindsDstAddr_Type()
)
avMSSVarbindsDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsDstAddr.setStatus("current")


class _AvMSSVarbindsDstPort_Type(Integer32):
    """Custom type avMSSVarbindsDstPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvMSSVarbindsDstPort_Type.__name__ = "Integer32"
_AvMSSVarbindsDstPort_Object = MibScalar
avMSSVarbindsDstPort = _AvMSSVarbindsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 5),
    _AvMSSVarbindsDstPort_Type()
)
avMSSVarbindsDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsDstPort.setStatus("current")


class _AvMSSVarbindsIpProtocol_Type(Integer32):
    """Custom type avMSSVarbindsIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvMSSVarbindsIpProtocol_Type.__name__ = "Integer32"
_AvMSSVarbindsIpProtocol_Object = MibScalar
avMSSVarbindsIpProtocol = _AvMSSVarbindsIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 6),
    _AvMSSVarbindsIpProtocol_Type()
)
avMSSVarbindsIpProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsIpProtocol.setStatus("current")
_AvMSSVarbindsCount_Type = Counter64
_AvMSSVarbindsCount_Object = MibScalar
avMSSVarbindsCount = _AvMSSVarbindsCount_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 7),
    _AvMSSVarbindsCount_Type()
)
avMSSVarbindsCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsCount.setStatus("current")


class _AvMSSVarbindsSrcMACAddr_Type(PhysAddress):
    """Custom type avMSSVarbindsSrcMACAddr based on PhysAddress"""
    defaultValue = OctetString("00:00:00:00:00:00")


_AvMSSVarbindsSrcMACAddr_Object = MibScalar
avMSSVarbindsSrcMACAddr = _AvMSSVarbindsSrcMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 4, 8),
    _AvMSSVarbindsSrcMACAddr_Type()
)
avMSSVarbindsSrcMACAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avMSSVarbindsSrcMACAddr.setStatus("current")
_SecMngNotifications_ObjectIdentity = ObjectIdentity
secMngNotifications = _SecMngNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10)
)
if mibBuilder.loadTexts:
    secMngNotifications.setStatus("current")
_SecMngNotificationsPrefix_ObjectIdentity = ObjectIdentity
secMngNotificationsPrefix = _SecMngNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 0)
)
if mibBuilder.loadTexts:
    secMngNotificationsPrefix.setStatus("current")
_SecMngVarbinds_ObjectIdentity = ObjectIdentity
secMngVarbinds = _SecMngVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1)
)
if mibBuilder.loadTexts:
    secMngVarbinds.setStatus("current")
_SecMngNumOfDays2Expire_Type = Unsigned32
_SecMngNumOfDays2Expire_Object = MibScalar
secMngNumOfDays2Expire = _SecMngNumOfDays2Expire_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 1),
    _SecMngNumOfDays2Expire_Type()
)
secMngNumOfDays2Expire.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    secMngNumOfDays2Expire.setStatus("current")
if mibBuilder.loadTexts:
    secMngNumOfDays2Expire.setUnits("Days")


class _AvUnauthUserName_Type(OctetString):
    """Custom type avUnauthUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvUnauthUserName_Type.__name__ = "OctetString"
_AvUnauthUserName_Object = MibScalar
avUnauthUserName = _AvUnauthUserName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 3),
    _AvUnauthUserName_Type()
)
avUnauthUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avUnauthUserName.setStatus("current")


class _AvUnauthProtocol_Type(Integer32):
    """Custom type avUnauthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(22,
              23,
              80,
              161,
              443,
              500,
              6889,
              6890,
              6891)
        )
    )
    namedValues = NamedValues(
        *(("avConsoleAccess", 6890),
          ("avHTTPAccess", 80),
          ("avHTTPSAccess", 443),
          ("avIKEAccess", 500),
          ("avPPPAccess", 6891),
          ("avRASAccess", 6889),
          ("avSNMPAccess", 161),
          ("avSSHAccess", 22),
          ("avTELNETAccess", 23))
    )


_AvUnauthProtocol_Type.__name__ = "Integer32"
_AvUnauthProtocol_Object = MibScalar
avUnauthProtocol = _AvUnauthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 5),
    _AvUnauthProtocol_Type()
)
avUnauthProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avUnauthProtocol.setStatus("current")
_AvUnauthInetAddressType_Type = InetAddressType
_AvUnauthInetAddressType_Object = MibScalar
avUnauthInetAddressType = _AvUnauthInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 9),
    _AvUnauthInetAddressType_Type()
)
avUnauthInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avUnauthInetAddressType.setStatus("current")
_AvUnauthInetAddress_Type = InetAddress
_AvUnauthInetAddress_Object = MibScalar
avUnauthInetAddress = _AvUnauthInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 10),
    _AvUnauthInetAddress_Type()
)
avUnauthInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avUnauthInetAddress.setStatus("current")
_AvDuplicatedInetAddressType_Type = InetAddressType
_AvDuplicatedInetAddressType_Object = MibScalar
avDuplicatedInetAddressType = _AvDuplicatedInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 11),
    _AvDuplicatedInetAddressType_Type()
)
avDuplicatedInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avDuplicatedInetAddressType.setStatus("current")
_AvDuplicatedInetAddress_Type = InetAddress
_AvDuplicatedInetAddress_Object = MibScalar
avDuplicatedInetAddress = _AvDuplicatedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 12),
    _AvDuplicatedInetAddress_Type()
)
avDuplicatedInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avDuplicatedInetAddress.setStatus("current")
_AvDuplicatedMACAddress_Type = PhysAddress
_AvDuplicatedMACAddress_Object = MibScalar
avDuplicatedMACAddress = _AvDuplicatedMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 1, 13),
    _AvDuplicatedMACAddress_Type()
)
avDuplicatedMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avDuplicatedMACAddress.setStatus("current")
_AvASGAuthenticationFiles_ObjectIdentity = ObjectIdentity
avASGAuthenticationFiles = _AvASGAuthenticationFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12)
)
if mibBuilder.loadTexts:
    avASGAuthenticationFiles.setStatus("current")
_AvASGAuthFileHeader_ObjectIdentity = ObjectIdentity
avASGAuthFileHeader = _AvASGAuthFileHeader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3)
)
if mibBuilder.loadTexts:
    avASGAuthFileHeader.setStatus("current")


class _AvASGAuthFileAFID_Type(DisplayString):
    """Custom type avASGAuthFileAFID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AvASGAuthFileAFID_Type.__name__ = "DisplayString"
_AvASGAuthFileAFID_Object = MibScalar
avASGAuthFileAFID = _AvASGAuthFileAFID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 1),
    _AvASGAuthFileAFID_Type()
)
avASGAuthFileAFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avASGAuthFileAFID.setStatus("current")
_AvASGAuthFileGenDate_Type = DisplayString
_AvASGAuthFileGenDate_Object = MibScalar
avASGAuthFileGenDate = _AvASGAuthFileGenDate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 2),
    _AvASGAuthFileGenDate_Type()
)
avASGAuthFileGenDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avASGAuthFileGenDate.setStatus("current")
if mibBuilder.loadTexts:
    avASGAuthFileGenDate.setUnits("YYYY/MM/DD")


class _AvASGAuthFileGenTime_Type(DisplayString):
    """Custom type avASGAuthFileGenTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AvASGAuthFileGenTime_Type.__name__ = "DisplayString"
_AvASGAuthFileGenTime_Object = MibScalar
avASGAuthFileGenTime = _AvASGAuthFileGenTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 3),
    _AvASGAuthFileGenTime_Type()
)
avASGAuthFileGenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avASGAuthFileGenTime.setStatus("current")
if mibBuilder.loadTexts:
    avASGAuthFileGenTime.setUnits("HH:MM:SS")
_AvASGAuthFileRelease_Type = DisplayString
_AvASGAuthFileRelease_Object = MibScalar
avASGAuthFileRelease = _AvASGAuthFileRelease_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 4),
    _AvASGAuthFileRelease_Type()
)
avASGAuthFileRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avASGAuthFileRelease.setStatus("current")
_AvASGNotifications_ObjectIdentity = ObjectIdentity
avASGNotifications = _AvASGNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 5)
)
if mibBuilder.loadTexts:
    avASGNotifications.setStatus("current")
_AvASGNotificationsPrefix_ObjectIdentity = ObjectIdentity
avASGNotificationsPrefix = _AvASGNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 5, 0)
)
if mibBuilder.loadTexts:
    avASGNotificationsPrefix.setStatus("current")
_AvSecLocalDateAndTime_Type = DateAndTime
_AvSecLocalDateAndTime_Object = MibScalar
avSecLocalDateAndTime = _AvSecLocalDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 13),
    _AvSecLocalDateAndTime_Type()
)
avSecLocalDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSecLocalDateAndTime.setStatus("current")

# Managed Objects groups

secMngBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 4, 1, 1)
)
secMngBasicGroup.setObjects(
      *(("SECURITY-MANAGEMENT-MIB", "secMode"),
        ("SECURITY-MANAGEMENT-MIB", "secMngProtoId"),
        ("SECURITY-MANAGEMENT-MIB", "secMngProtoStatus"),
        ("SECURITY-MANAGEMENT-MIB", "secTcpSynCkiOpState"),
        ("SECURITY-MANAGEMENT-MIB", "secTcpSynCkiCfgState"),
        ("SECURITY-MANAGEMENT-MIB", "fipsEnhancedSecurityFlg"))
)
if mibBuilder.loadTexts:
    secMngBasicGroup.setStatus("current")

lsgLicMngBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 5, 20, 1, 1)
)
lsgLicMngBasicGroup.setObjects(
      *(("SECURITY-MANAGEMENT-MIB", "lsgLicMngFeatureKeyword"),
        ("SECURITY-MANAGEMENT-MIB", "lsgLicMngFeatureType"),
        ("SECURITY-MANAGEMENT-MIB", "lsgLicMngAdminStatus"),
        ("SECURITY-MANAGEMENT-MIB", "lsgLicMngOperStatus"),
        ("SECURITY-MANAGEMENT-MIB", "lsgLicMngCountedValue"),
        ("SECURITY-MANAGEMENT-MIB", "lsgLicMngLastError"))
)
if mibBuilder.loadTexts:
    lsgLicMngBasicGroup.setStatus("current")

avMSSgroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 8)
)
avMSSgroup.setObjects(
      *(("SECURITY-MANAGEMENT-MIB", "avMSSNotificationRate"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsSrcAddr"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsDstAddr"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsDstPort"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsDescription"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsIpProtocol"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsDoSType"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsCount"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsSrcMACAddr"))
)
if mibBuilder.loadTexts:
    avMSSgroup.setStatus("current")

avMngNotificationCompliance = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 2)
)
avMngNotificationCompliance.setObjects(
    ("SECURITY-MANAGEMENT-MIB", "secMngNumOfDays2Expire")
)
if mibBuilder.loadTexts:
    avMngNotificationCompliance.setStatus("current")

avASGAuthFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 1000)
)
avASGAuthFileGroup.setObjects(
      *(("SECURITY-MANAGEMENT-MIB", "avASGAuthFileAFID"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileGenDate"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileGenTime"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileRelease"))
)
if mibBuilder.loadTexts:
    avASGAuthFileGroup.setStatus("current")


# Notification objects

avMSSDenialOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 7, 0, 1)
)
avMSSDenialOfService.setObjects(
      *(("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsDoSType"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsSrcAddr"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsDstAddr"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsDstPort"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsCount"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsIpProtocol"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("SECURITY-MANAGEMENT-MIB", "avMSSVarbindsSrcMACAddr"))
)
if mibBuilder.loadTexts:
    avMSSDenialOfService.setStatus(
        "current"
    )

avConfigurationEncKeyMismatchFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 0, 1)
)
avConfigurationEncKeyMismatchFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("LOAD-MIB", "genAppFileId"),
        ("LOAD-MIB", "genAppFileName"),
        ("LOAD-MIB", "genAppFileVersionNumber"),
        ("LOAD-MIB", "genOpLastFailureDisplay"))
)
if mibBuilder.loadTexts:
    avConfigurationEncKeyMismatchFault.setStatus(
        "current"
    )

avConfigurationMasterKeyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 0, 2)
)
avConfigurationMasterKeyChange.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    avConfigurationMasterKeyChange.setStatus(
        "current"
    )

avPasswordToExpireAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 0, 3)
)
avPasswordToExpireAlert.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("SECURITY-MANAGEMENT-MIB", "secMngNumOfDays2Expire"))
)
if mibBuilder.loadTexts:
    avPasswordToExpireAlert.setStatus(
        "current"
    )

avUnAuthAccessEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 0, 200)
)
avUnAuthAccessEvent.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthUserName"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthInetAddressType"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthInetAddress"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthProtocol"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileAFID"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avUnAuthAccessEvent.setStatus(
        "current"
    )

avAccountLockoutEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 0, 201)
)
avAccountLockoutEvent.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthUserName"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthInetAddressType"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthInetAddress"),
        ("SECURITY-MANAGEMENT-MIB", "avUnauthProtocol"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileAFID"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avAccountLockoutEvent.setStatus(
        "current"
    )

avIPv6AddressDuplicationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 10, 0, 202)
)
avIPv6AddressDuplicationEvent.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("SECURITY-MANAGEMENT-MIB", "avDuplicatedInetAddressType"),
        ("SECURITY-MANAGEMENT-MIB", "avDuplicatedInetAddress"),
        ("SECURITY-MANAGEMENT-MIB", "avDuplicatedMACAddress"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileAFID"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avIPv6AddressDuplicationEvent.setStatus(
        "current"
    )

avASGAFDownloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 5, 0, 1)
)
avASGAFDownloadSuccess.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("LOAD-MIB", "genAppFileId"),
        ("LOAD-MIB", "genAppFileName"),
        ("LOAD-MIB", "genAppFileVersionNumber"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileAFID"))
)
if mibBuilder.loadTexts:
    avASGAFDownloadSuccess.setStatus(
        "current"
    )

avASGAFDownloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 3, 5, 0, 2)
)
avASGAFDownloadFailure.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("LOAD-MIB", "genAppFileId"),
        ("LOAD-MIB", "genAppFileName"),
        ("LOAD-MIB", "genAppFileVersionNumber"),
        ("LOAD-MIB", "genOpLastFailureDisplay"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAuthFileAFID"))
)
if mibBuilder.loadTexts:
    avASGAFDownloadFailure.setStatus(
        "current"
    )


# Notifications groups

mssNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 9)
)
mssNotificationGroup.setObjects(
    ("SECURITY-MANAGEMENT-MIB", "avMSSDenialOfService")
)
if mibBuilder.loadTexts:
    mssNotificationGroup.setStatus(
        "current"
    )

secMngNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 11)
)
secMngNotificationGroup.setObjects(
      *(("SECURITY-MANAGEMENT-MIB", "avConfigurationEncKeyMismatchFault"),
        ("SECURITY-MANAGEMENT-MIB", "avConfigurationMasterKeyChange"))
)
if mibBuilder.loadTexts:
    secMngNotificationGroup.setStatus(
        "current"
    )

avASGAuthFileNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 14, 1, 12, 1001)
)
avASGAuthFileNotificationGroup.setObjects(
      *(("SECURITY-MANAGEMENT-MIB", "avASGAFDownloadFailure"),
        ("SECURITY-MANAGEMENT-MIB", "avASGAFDownloadSuccess"))
)
if mibBuilder.loadTexts:
    avASGAuthFileNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SECURITY-MANAGEMENT-MIB",
    **{"OnOffType": OnOffType,
       "ServiceStateType": ServiceStateType,
       "avayaSecurity": avayaSecurity,
       "secMngModule": secMngModule,
       "secMode": secMode,
       "secTcpSynCookies": secTcpSynCookies,
       "secTcpSynCkiOpState": secTcpSynCkiOpState,
       "secTcpSynCkiCfgState": secTcpSynCkiCfgState,
       "secMngProtoTable": secMngProtoTable,
       "secMngProtoEntry": secMngProtoEntry,
       "secMngProtoId": secMngProtoId,
       "secMngProtoStatus": secMngProtoStatus,
       "secMngConformance": secMngConformance,
       "secMngGroups": secMngGroups,
       "secMngBasicGroup": secMngBasicGroup,
       "secMngCompliance": secMngCompliance,
       "lsgLicManagement": lsgLicManagement,
       "lsgLicMngTable": lsgLicMngTable,
       "lsgLicMngEntry": lsgLicMngEntry,
       "lsgLicMngFeatureKeyword": lsgLicMngFeatureKeyword,
       "lsgLicMngFeatureType": lsgLicMngFeatureType,
       "lsgLicMngAdminStatus": lsgLicMngAdminStatus,
       "lsgLicMngOperStatus": lsgLicMngOperStatus,
       "lsgLicMngCountedValue": lsgLicMngCountedValue,
       "lsgLicMngLastError": lsgLicMngLastError,
       "lsgLicMngConformance": lsgLicMngConformance,
       "lsgLicMngGroups": lsgLicMngGroups,
       "lsgLicMngBasicGroup": lsgLicMngBasicGroup,
       "fips140": fips140,
       "fipsEnhancedSecurityFlg": fipsEnhancedSecurityFlg,
       "avMssNotifications": avMssNotifications,
       "avMssNotificationPrefix": avMssNotificationPrefix,
       "avMSSDenialOfService": avMSSDenialOfService,
       "avMSSNotificationRate": avMSSNotificationRate,
       "avMSSVarbinds": avMSSVarbinds,
       "avMSSVarbindsDoSType": avMSSVarbindsDoSType,
       "avMSSVarbindsDescription": avMSSVarbindsDescription,
       "avMSSVarbindsSrcAddr": avMSSVarbindsSrcAddr,
       "avMSSVarbindsDstAddr": avMSSVarbindsDstAddr,
       "avMSSVarbindsDstPort": avMSSVarbindsDstPort,
       "avMSSVarbindsIpProtocol": avMSSVarbindsIpProtocol,
       "avMSSVarbindsCount": avMSSVarbindsCount,
       "avMSSVarbindsSrcMACAddr": avMSSVarbindsSrcMACAddr,
       "avMSSgroup": avMSSgroup,
       "mssNotificationGroup": mssNotificationGroup,
       "secMngNotifications": secMngNotifications,
       "secMngNotificationsPrefix": secMngNotificationsPrefix,
       "avConfigurationEncKeyMismatchFault": avConfigurationEncKeyMismatchFault,
       "avConfigurationMasterKeyChange": avConfigurationMasterKeyChange,
       "avPasswordToExpireAlert": avPasswordToExpireAlert,
       "avUnAuthAccessEvent": avUnAuthAccessEvent,
       "avAccountLockoutEvent": avAccountLockoutEvent,
       "avIPv6AddressDuplicationEvent": avIPv6AddressDuplicationEvent,
       "secMngVarbinds": secMngVarbinds,
       "secMngNumOfDays2Expire": secMngNumOfDays2Expire,
       "avUnauthUserName": avUnauthUserName,
       "avUnauthProtocol": avUnauthProtocol,
       "avUnauthInetAddressType": avUnauthInetAddressType,
       "avUnauthInetAddress": avUnauthInetAddress,
       "avDuplicatedInetAddressType": avDuplicatedInetAddressType,
       "avDuplicatedInetAddress": avDuplicatedInetAddress,
       "avDuplicatedMACAddress": avDuplicatedMACAddress,
       "avMngNotificationCompliance": avMngNotificationCompliance,
       "secMngNotificationGroup": secMngNotificationGroup,
       "avASGAuthenticationFiles": avASGAuthenticationFiles,
       "avASGAuthFileHeader": avASGAuthFileHeader,
       "avASGAuthFileAFID": avASGAuthFileAFID,
       "avASGAuthFileGenDate": avASGAuthFileGenDate,
       "avASGAuthFileGenTime": avASGAuthFileGenTime,
       "avASGAuthFileRelease": avASGAuthFileRelease,
       "avASGNotifications": avASGNotifications,
       "avASGNotificationsPrefix": avASGNotificationsPrefix,
       "avASGAFDownloadSuccess": avASGAFDownloadSuccess,
       "avASGAFDownloadFailure": avASGAFDownloadFailure,
       "avASGAuthFileGroup": avASGAuthFileGroup,
       "avASGAuthFileNotificationGroup": avASGAuthFileNotificationGroup,
       "avSecLocalDateAndTime": avSecLocalDateAndTime}
)
