# SNMP MIB module (Lannet-Trapsv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Lannet-Trapsv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:39 2024
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

(lseIntPortCAMLastChange,
 vnsPacketBoxAgentIP,
 vnsPacketDetectedIfName,
 vnsPacketDetectedVLAN,
 vnsPacketExpectedIfName,
 vnsPacketExpectedVLAN,
 vnsPacketIPAddress,
 vnsPacketIPNetMask,
 vnsPacketMACAddress) = mibBuilder.importSymbols(
    "APPLIC-MIB",
    "lseIntPortCAMLastChange",
    "vnsPacketBoxAgentIP",
    "vnsPacketDetectedIfName",
    "vnsPacketDetectedVLAN",
    "vnsPacketExpectedIfName",
    "vnsPacketExpectedVLAN",
    "vnsPacketIPAddress",
    "vnsPacketIPNetMask",
    "vnsPacketMACAddress")

(chHWIntTempThresh,
 chHWIntTempWarning,
 chLntAgIntTemp,
 genGroupBUPSActivityStatus,
 genGroupCascadDownStatus,
 genGroupCascadUpStatus,
 genGroupFaultMask,
 genGroupId,
 genGroupMPSActivityStatus,
 genPortFaultMask,
 genPortFunctionalStatus,
 genPortGroupId,
 genPortId,
 softRedundancyGroupId1,
 softRedundancyGroupId2,
 softRedundancyName,
 softRedundancyPortId1,
 softRedundancyPortId2,
 softRedundancyStatus) = mibBuilder.importSymbols(
    "CONFIG-MIB",
    "chHWIntTempThresh",
    "chHWIntTempWarning",
    "chLntAgIntTemp",
    "genGroupBUPSActivityStatus",
    "genGroupCascadDownStatus",
    "genGroupCascadUpStatus",
    "genGroupFaultMask",
    "genGroupId",
    "genGroupMPSActivityStatus",
    "genPortFaultMask",
    "genPortFunctionalStatus",
    "genPortGroupId",
    "genPortId",
    "softRedundancyGroupId1",
    "softRedundancyGroupId2",
    "softRedundancyName",
    "softRedundancyPortId1",
    "softRedundancyPortId2",
    "softRedundancyStatus")

(dsx1LineStatus,) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1LineStatus")

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

(ifAdminStatus,
 ifAlias,
 ifIndex,
 ifName,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifAlias",
    "ifIndex",
    "ifName",
    "ifOperStatus")

(ipNetToMediaNetAddress,
 ipNetToMediaPhysAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaNetAddress",
    "ipNetToMediaPhysAddress")

(ipPolicyAccessControlViolationDstAddr,
 ipPolicyAccessControlViolationEntID,
 ipPolicyAccessControlViolationEstablished,
 ipPolicyAccessControlViolationIfIndex,
 ipPolicyAccessControlViolationL4DstPort,
 ipPolicyAccessControlViolationL4SrcPort,
 ipPolicyAccessControlViolationProtocol,
 ipPolicyAccessControlViolationRuleType,
 ipPolicyAccessControlViolationSrcAddr,
 ipPolicyAccessControlViolationSubCtxt,
 ipPolicyAccessControlViolationTime,
 ipPolicyActivationEntID,
 ipPolicyActivationList,
 ipPolicyActivationSubContext,
 ipPolicyActivationifIndex,
 ipPolicyControlSlot,
 ipPolicyListID,
 ipPolicyRuleDescription,
 ipPolicyRuleID,
 ipPolicyRuleListID) = mibBuilder.importSymbols(
    "POLICY-MIB",
    "ipPolicyAccessControlViolationDstAddr",
    "ipPolicyAccessControlViolationEntID",
    "ipPolicyAccessControlViolationEstablished",
    "ipPolicyAccessControlViolationIfIndex",
    "ipPolicyAccessControlViolationL4DstPort",
    "ipPolicyAccessControlViolationL4SrcPort",
    "ipPolicyAccessControlViolationProtocol",
    "ipPolicyAccessControlViolationRuleType",
    "ipPolicyAccessControlViolationSrcAddr",
    "ipPolicyAccessControlViolationSubCtxt",
    "ipPolicyAccessControlViolationTime",
    "ipPolicyActivationEntID",
    "ipPolicyActivationList",
    "ipPolicyActivationSubContext",
    "ipPolicyActivationifIndex",
    "ipPolicyControlSlot",
    "ipPolicyListID",
    "ipPolicyRuleDescription",
    "ipPolicyRuleID",
    "ipPolicyRuleListID")

(rmonNotificationGroup,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "rmonNotificationGroup")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(authenticationFailure,
 coldStart,
 warmStart) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "authenticationFailure",
    "coldStart",
    "warmStart")

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

(scEthPortFunctionalStatus,
 scEthPortGroupId,
 scEthPortId,
 scGenGroupBUPSFansStatus,
 scGenGroupDot1xSystemMaxNumSupplicant,
 scGenGroupFansStatus,
 scGenLinkAggregationAutoNegResults,
 scGenLinkAggregationFaultMask,
 scGenLinkAggregationFunctionalStatus,
 scGenLinkAggregationId,
 scGenLinkAggregationName,
 scGenLinkAggregationStatus,
 scGenPortDot1xMAC,
 scGenPortGroupId,
 scGenPortId,
 scGenPortLastIntruderSourceAddr,
 scGenSwitchDot1xPortMaxSuppNum) = mibBuilder.importSymbols(
    "XSWITCH-MIB",
    "scEthPortFunctionalStatus",
    "scEthPortGroupId",
    "scEthPortId",
    "scGenGroupBUPSFansStatus",
    "scGenGroupDot1xSystemMaxNumSupplicant",
    "scGenGroupFansStatus",
    "scGenLinkAggregationAutoNegResults",
    "scGenLinkAggregationFaultMask",
    "scGenLinkAggregationFunctionalStatus",
    "scGenLinkAggregationId",
    "scGenLinkAggregationName",
    "scGenLinkAggregationStatus",
    "scGenPortDot1xMAC",
    "scGenPortGroupId",
    "scGenPortId",
    "scGenPortLastIntruderSourceAddr",
    "scGenSwitchDot1xPortMaxSuppNum")


# MODULE-IDENTITY

lntTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LntConfigChangeEvents_ObjectIdentity = ObjectIdentity
lntConfigChangeEvents = _LntConfigChangeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 1)
)
if mibBuilder.loadTexts:
    lntConfigChangeEvents.setStatus("current")
_LntConfigChangePrefix_ObjectIdentity = ObjectIdentity
lntConfigChangePrefix = _LntConfigChangePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 1, 0)
)
if mibBuilder.loadTexts:
    lntConfigChangePrefix.setStatus("current")
_LntSWRedundancyEvents_ObjectIdentity = ObjectIdentity
lntSWRedundancyEvents = _LntSWRedundancyEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 2)
)
if mibBuilder.loadTexts:
    lntSWRedundancyEvents.setStatus("current")
_LntSWRedundancyPrefix_ObjectIdentity = ObjectIdentity
lntSWRedundancyPrefix = _LntSWRedundancyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 2, 0)
)
if mibBuilder.loadTexts:
    lntSWRedundancyPrefix.setStatus("current")
_LntTempratureEvents_ObjectIdentity = ObjectIdentity
lntTempratureEvents = _LntTempratureEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 3)
)
if mibBuilder.loadTexts:
    lntTempratureEvents.setStatus("current")
_LntTempratureWarningPrefix_ObjectIdentity = ObjectIdentity
lntTempratureWarningPrefix = _LntTempratureWarningPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 3, 0)
)
if mibBuilder.loadTexts:
    lntTempratureWarningPrefix.setStatus("current")
_LntCAMChangeEvents_ObjectIdentity = ObjectIdentity
lntCAMChangeEvents = _LntCAMChangeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 4)
)
if mibBuilder.loadTexts:
    lntCAMChangeEvents.setStatus("current")
_LntCAMChangePrefix_ObjectIdentity = ObjectIdentity
lntCAMChangePrefix = _LntCAMChangePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 4, 0)
)
if mibBuilder.loadTexts:
    lntCAMChangePrefix.setStatus("current")
_LntPSUEvents_ObjectIdentity = ObjectIdentity
lntPSUEvents = _LntPSUEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 5)
)
if mibBuilder.loadTexts:
    lntPSUEvents.setStatus("current")
_LntPSUPrefix_ObjectIdentity = ObjectIdentity
lntPSUPrefix = _LntPSUPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 5, 0)
)
if mibBuilder.loadTexts:
    lntPSUPrefix.setStatus("current")
_LntL3Events_ObjectIdentity = ObjectIdentity
lntL3Events = _LntL3Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 6)
)
if mibBuilder.loadTexts:
    lntL3Events.setStatus("current")
_LntL3FaultsPrefix_ObjectIdentity = ObjectIdentity
lntL3FaultsPrefix = _LntL3FaultsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 6, 0)
)
if mibBuilder.loadTexts:
    lntL3FaultsPrefix.setStatus("current")
_LntLinkEvents_ObjectIdentity = ObjectIdentity
lntLinkEvents = _LntLinkEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 7)
)
if mibBuilder.loadTexts:
    lntLinkEvents.setStatus("current")
_LntLinkEventsPrefix_ObjectIdentity = ObjectIdentity
lntLinkEventsPrefix = _LntLinkEventsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 7, 0)
)
if mibBuilder.loadTexts:
    lntLinkEventsPrefix.setStatus("current")
_LntLAGEvents_ObjectIdentity = ObjectIdentity
lntLAGEvents = _LntLAGEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 8)
)
if mibBuilder.loadTexts:
    lntLAGEvents.setStatus("current")
_LntLAGPrefix_ObjectIdentity = ObjectIdentity
lntLAGPrefix = _LntLAGPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0)
)
if mibBuilder.loadTexts:
    lntLAGPrefix.setStatus("current")
_LntFansEvents_ObjectIdentity = ObjectIdentity
lntFansEvents = _LntFansEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 9)
)
if mibBuilder.loadTexts:
    lntFansEvents.setStatus("current")
_LntFansPrefix_ObjectIdentity = ObjectIdentity
lntFansPrefix = _LntFansPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 9, 0)
)
if mibBuilder.loadTexts:
    lntFansPrefix.setStatus("current")
_LntCascadeEvents_ObjectIdentity = ObjectIdentity
lntCascadeEvents = _LntCascadeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 10)
)
if mibBuilder.loadTexts:
    lntCascadeEvents.setStatus("current")
_LntCascadeFaultsPrefix_ObjectIdentity = ObjectIdentity
lntCascadeFaultsPrefix = _LntCascadeFaultsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 10, 0)
)
if mibBuilder.loadTexts:
    lntCascadeFaultsPrefix.setStatus("current")
_LntPolicyEvents_ObjectIdentity = ObjectIdentity
lntPolicyEvents = _LntPolicyEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 11)
)
if mibBuilder.loadTexts:
    lntPolicyEvents.setStatus("current")
_LntPolicyPrefix_ObjectIdentity = ObjectIdentity
lntPolicyPrefix = _LntPolicyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 11, 0)
)
if mibBuilder.loadTexts:
    lntPolicyPrefix.setStatus("current")
_LntEthPortFaultEvents_ObjectIdentity = ObjectIdentity
lntEthPortFaultEvents = _LntEthPortFaultEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 12)
)
if mibBuilder.loadTexts:
    lntEthPortFaultEvents.setStatus("current")
_LntEthPortFaultPrefix_ObjectIdentity = ObjectIdentity
lntEthPortFaultPrefix = _LntEthPortFaultPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0)
)
if mibBuilder.loadTexts:
    lntEthPortFaultPrefix.setStatus("current")
_LntSecurityEvents_ObjectIdentity = ObjectIdentity
lntSecurityEvents = _LntSecurityEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 13)
)
if mibBuilder.loadTexts:
    lntSecurityEvents.setStatus("current")
_LntSecurityPrefix_ObjectIdentity = ObjectIdentity
lntSecurityPrefix = _LntSecurityPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0)
)
if mibBuilder.loadTexts:
    lntSecurityPrefix.setStatus("current")
_LntNotificationVarbinds_ObjectIdentity = ObjectIdentity
lntNotificationVarbinds = _LntNotificationVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 14)
)
if mibBuilder.loadTexts:
    lntNotificationVarbinds.setStatus("current")
_LntConfigChangeValue_Type = DisplayString
_LntConfigChangeValue_Object = MibScalar
lntConfigChangeValue = _LntConfigChangeValue_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 1),
    _LntConfigChangeValue_Type()
)
lntConfigChangeValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lntConfigChangeValue.setStatus("current")
_LntConfigChangeOID_Type = ObjectIdentifier
_LntConfigChangeOID_Object = MibScalar
lntConfigChangeOID = _LntConfigChangeOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 2),
    _LntConfigChangeOID_Type()
)
lntConfigChangeOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lntConfigChangeOID.setStatus("current")


class _LntUnauthUserName_Type(OctetString):
    """Custom type lntUnauthUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LntUnauthUserName_Type.__name__ = "OctetString"
_LntUnauthUserName_Object = MibScalar
lntUnauthUserName = _LntUnauthUserName_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 3),
    _LntUnauthUserName_Type()
)
lntUnauthUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lntUnauthUserName.setStatus("current")
_LntUnauthIpAddress_Type = IpAddress
_LntUnauthIpAddress_Object = MibScalar
lntUnauthIpAddress = _LntUnauthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 4),
    _LntUnauthIpAddress_Type()
)
lntUnauthIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lntUnauthIpAddress.setStatus("current")


class _LntUnauthProtocol_Type(Integer32):
    """Custom type lntUnauthProtocol based on Integer32"""
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
        *(("lntConsoleAccess", 6890),
          ("lntHTTPAccess", 80),
          ("lntHTTPSAccess", 443),
          ("lntIKEAccess", 500),
          ("lntPPPAccess", 6891),
          ("lntRASAccess", 6889),
          ("lntSNMPAccess", 161),
          ("lntSSHAccess", 22),
          ("lntTELNETAccess", 23))
    )


_LntUnauthProtocol_Type.__name__ = "Integer32"
_LntUnauthProtocol_Object = MibScalar
lntUnauthProtocol = _LntUnauthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 5),
    _LntUnauthProtocol_Type()
)
lntUnauthProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lntUnauthProtocol.setStatus("current")


class _LntSCPStrictCheckingMode_Type(Integer32):
    """Custom type lntSCPStrictCheckingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ask", 3),
          ("no", 2),
          ("yes", 1))
    )


_LntSCPStrictCheckingMode_Type.__name__ = "Integer32"
_LntSCPStrictCheckingMode_Object = MibScalar
lntSCPStrictCheckingMode = _LntSCPStrictCheckingMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 6),
    _LntSCPStrictCheckingMode_Type()
)
lntSCPStrictCheckingMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lntSCPStrictCheckingMode.setStatus("current")


class _LntLicenseErrorCodes_Type(Integer32):
    """Custom type lntLicenseErrorCodes based on Integer32"""
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
        *(("lntInvalidLicFeture", 4),
          ("lntInvalidSignature", 2),
          ("lntPlatformTypeMismatch", 3),
          ("lntSerialNumMismatch", 1))
    )


_LntLicenseErrorCodes_Type.__name__ = "Integer32"
_LntLicenseErrorCodes_Object = MibScalar
lntLicenseErrorCodes = _LntLicenseErrorCodes_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 7),
    _LntLicenseErrorCodes_Type()
)
lntLicenseErrorCodes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lntLicenseErrorCodes.setStatus("current")
_ScGenPortDot1xFailureString_Type = DisplayString
_ScGenPortDot1xFailureString_Object = MibScalar
scGenPortDot1xFailureString = _ScGenPortDot1xFailureString_Object(
    (1, 3, 6, 1, 4, 1, 81, 38, 14, 8),
    _ScGenPortDot1xFailureString_Type()
)
scGenPortDot1xFailureString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scGenPortDot1xFailureString.setStatus("current")
_LntWanEvents_ObjectIdentity = ObjectIdentity
lntWanEvents = _LntWanEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 15)
)
if mibBuilder.loadTexts:
    lntWanEvents.setStatus("current")
_LntWanPrefix_ObjectIdentity = ObjectIdentity
lntWanPrefix = _LntWanPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0)
)
if mibBuilder.loadTexts:
    lntWanPrefix.setStatus("current")
_LntNotificationGroups_ObjectIdentity = ObjectIdentity
lntNotificationGroups = _LntNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007)
)
_LntNotificationAgentCapabilities_ObjectIdentity = ObjectIdentity
lntNotificationAgentCapabilities = _LntNotificationAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 38, 10008)
)

# Managed Objects groups

lntConfigChangeVarbinds = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 1)
)
lntConfigChangeVarbinds.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntConfigChangeValue"),
        ("Lannet-Trapsv2-MIB", "lntConfigChangeOID"),
        ("Lannet-Trapsv2-MIB", "lntUnauthIpAddress"),
        ("Lannet-Trapsv2-MIB", "lntUnauthUserName"),
        ("Lannet-Trapsv2-MIB", "lntLicenseErrorCodes"),
        ("Lannet-Trapsv2-MIB", "lntSCPStrictCheckingMode"),
        ("Lannet-Trapsv2-MIB", "lntUnauthProtocol"))
)
if mibBuilder.loadTexts:
    lntConfigChangeVarbinds.setStatus("current")


# Notification objects

lntConfigChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 1, 0, 1)
)
lntConfigChangeEvent.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntConfigChangeOID"),
        ("Lannet-Trapsv2-MIB", "lntConfigChangeValue"))
)
if mibBuilder.loadTexts:
    lntConfigChangeEvent.setStatus(
        "current"
    )

lntStackMasterReelection = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 1, 0, 82)
)
lntStackMasterReelection.setObjects(
    ("CONFIG-MIB", "genGroupId")
)
if mibBuilder.loadTexts:
    lntStackMasterReelection.setStatus(
        "current"
    )

lntSoftRedDelEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 2, 0, 12)
)
lntSoftRedDelEvent.setObjects(
    ("CONFIG-MIB", "softRedundancyStatus")
)
if mibBuilder.loadTexts:
    lntSoftRedDelEvent.setStatus(
        "current"
    )

lntSoftRedNewEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 2, 0, 13)
)
lntSoftRedNewEvent.setObjects(
      *(("CONFIG-MIB", "softRedundancyName"),
        ("CONFIG-MIB", "softRedundancyGroupId1"),
        ("CONFIG-MIB", "softRedundancyPortId1"),
        ("CONFIG-MIB", "softRedundancyGroupId2"),
        ("CONFIG-MIB", "softRedundancyPortId2"),
        ("CONFIG-MIB", "softRedundancyStatus"))
)
if mibBuilder.loadTexts:
    lntSoftRedNewEvent.setStatus(
        "current"
    )

lntTempratureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 3, 0, 14)
)
lntTempratureWarning.setObjects(
      *(("CONFIG-MIB", "chHWIntTempWarning"),
        ("CONFIG-MIB", "chHWIntTempThresh"),
        ("CONFIG-MIB", "chLntAgIntTemp"))
)
if mibBuilder.loadTexts:
    lntTempratureWarning.setStatus(
        "current"
    )

lntTempratureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 3, 0, 23)
)
lntTempratureOk.setObjects(
      *(("CONFIG-MIB", "chHWIntTempWarning"),
        ("CONFIG-MIB", "chHWIntTempThresh"),
        ("CONFIG-MIB", "chLntAgIntTemp"))
)
if mibBuilder.loadTexts:
    lntTempratureOk.setStatus(
        "current"
    )

lntPortCAMLastChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 4, 0, 22)
)
lntPortCAMLastChange.setObjects(
    ("APPLIC-MIB", "lseIntPortCAMLastChange")
)
if mibBuilder.loadTexts:
    lntPortCAMLastChange.setStatus(
        "obsolete"
    )

lntMainPSUFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 5, 0, 2303)
)
lntMainPSUFlt.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupMPSActivityStatus"))
)
if mibBuilder.loadTexts:
    lntMainPSUFlt.setStatus(
        "current"
    )

lntMainPSUOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 5, 0, 2304)
)
lntMainPSUOk.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupMPSActivityStatus"))
)
if mibBuilder.loadTexts:
    lntMainPSUOk.setStatus(
        "current"
    )

lntBackupPSUFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 5, 0, 2305)
)
lntBackupPSUFlt.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupBUPSActivityStatus"))
)
if mibBuilder.loadTexts:
    lntBackupPSUFlt.setStatus(
        "current"
    )

lntBackupPSUOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 5, 0, 2306)
)
lntBackupPSUOk.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupMPSActivityStatus"))
)
if mibBuilder.loadTexts:
    lntBackupPSUOk.setStatus(
        "current"
    )

lntDuplicateIPFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 6, 0, 27)
)
lntDuplicateIPFlt.setObjects(
      *(("IP-MIB", "ipNetToMediaPhysAddress"),
        ("IP-MIB", "ipNetToMediaNetAddress"))
)
if mibBuilder.loadTexts:
    lntDuplicateIPFlt.setStatus(
        "current"
    )

lntVLANViolationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 6, 0, 28)
)
lntVLANViolationEvent.setObjects(
      *(("APPLIC-MIB", "vnsPacketMACAddress"),
        ("APPLIC-MIB", "vnsPacketIPAddress"),
        ("APPLIC-MIB", "vnsPacketIPNetMask"),
        ("APPLIC-MIB", "vnsPacketExpectedVLAN"),
        ("APPLIC-MIB", "vnsPacketDetectedVLAN"),
        ("APPLIC-MIB", "vnsPacketBoxAgentIP"))
)
if mibBuilder.loadTexts:
    lntVLANViolationEvent.setStatus(
        "current"
    )

lntARPViolationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 6, 0, 70)
)
lntARPViolationEvent.setObjects(
      *(("APPLIC-MIB", "vnsPacketMACAddress"),
        ("APPLIC-MIB", "vnsPacketIPAddress"),
        ("APPLIC-MIB", "vnsPacketIPNetMask"),
        ("APPLIC-MIB", "vnsPacketExpectedVLAN"),
        ("APPLIC-MIB", "vnsPacketDetectedVLAN"),
        ("APPLIC-MIB", "vnsPacketBoxAgentIP"),
        ("APPLIC-MIB", "vnsPacketExpectedIfName"),
        ("APPLIC-MIB", "vnsPacketDetectedIfName"))
)
if mibBuilder.loadTexts:
    lntARPViolationEvent.setStatus(
        "current"
    )

lntPortLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 7, 0, 3039)
)
lntPortLinkDownEvent.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortLinkDownEvent.setStatus(
        "current"
    )

lntPortLinkUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 7, 0, 3040)
)
lntPortLinkUpEvent.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortLinkUpEvent.setStatus(
        "current"
    )

lntVPortLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 7, 0, 3041)
)
lntVPortLinkDownEvent.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntVPortLinkDownEvent.setStatus(
        "current"
    )

lntVPortLinkUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 7, 0, 3042)
)
lntVPortLinkUpEvent.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntVPortLinkUpEvent.setStatus(
        "current"
    )

lntLAGConnLostFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 44)
)
lntLAGConnLostFlt.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationFaultMask"),
        ("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationFunctionalStatus"))
)
if mibBuilder.loadTexts:
    lntLAGConnLostFlt.setStatus(
        "current"
    )

lntLAGConnLostOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 46)
)
lntLAGConnLostOk.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationFaultMask"),
        ("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationFunctionalStatus"))
)
if mibBuilder.loadTexts:
    lntLAGConnLostOk.setStatus(
        "current"
    )

lntLAGPartialConnLostFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 48)
)
lntLAGPartialConnLostFlt.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationFaultMask"),
        ("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationFunctionalStatus"))
)
if mibBuilder.loadTexts:
    lntLAGPartialConnLostFlt.setStatus(
        "current"
    )

lntLAGPartialConnLostOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 50)
)
lntLAGPartialConnLostOk.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationFaultMask"),
        ("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationFunctionalStatus"))
)
if mibBuilder.loadTexts:
    lntLAGPartialConnLostOk.setStatus(
        "current"
    )

lntLAGAutoNegFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 52)
)
lntLAGAutoNegFlt.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationFaultMask"),
        ("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationAutoNegResults"))
)
if mibBuilder.loadTexts:
    lntLAGAutoNegFlt.setStatus(
        "current"
    )

lntLAGAutoNegOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 54)
)
lntLAGAutoNegOk.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationFaultMask"),
        ("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationAutoNegResults"))
)
if mibBuilder.loadTexts:
    lntLAGAutoNegOk.setStatus(
        "current"
    )

lntLAGDeleteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 56)
)
lntLAGDeleteEvent.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationStatus"))
)
if mibBuilder.loadTexts:
    lntLAGDeleteEvent.setStatus(
        "current"
    )

lntLAGCreateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 8, 0, 58)
)
lntLAGCreateEvent.setObjects(
      *(("XSWITCH-MIB", "scGenLinkAggregationId"),
        ("XSWITCH-MIB", "scGenLinkAggregationName"),
        ("XSWITCH-MIB", "scGenLinkAggregationStatus"))
)
if mibBuilder.loadTexts:
    lntLAGCreateEvent.setStatus(
        "current"
    )

lntMainFansFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 9, 0, 2307)
)
lntMainFansFlt.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("XSWITCH-MIB", "scGenGroupFansStatus"))
)
if mibBuilder.loadTexts:
    lntMainFansFlt.setStatus(
        "current"
    )

lntMainFansOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 9, 0, 2308)
)
lntMainFansOK.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("XSWITCH-MIB", "scGenGroupFansStatus"))
)
if mibBuilder.loadTexts:
    lntMainFansOK.setStatus(
        "current"
    )

lntBackupFansFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 9, 0, 2309)
)
lntBackupFansFlt.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("XSWITCH-MIB", "scGenGroupBUPSFansStatus"))
)
if mibBuilder.loadTexts:
    lntBackupFansFlt.setStatus(
        "current"
    )

lntBackupFansOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 9, 0, 2310)
)
lntBackupFansOK.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("XSWITCH-MIB", "scGenGroupBUPSFansStatus"))
)
if mibBuilder.loadTexts:
    lntBackupFansOK.setStatus(
        "current"
    )

lntCascadUpConnFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 10, 0, 2315)
)
lntCascadUpConnFlt.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupCascadUpStatus"))
)
if mibBuilder.loadTexts:
    lntCascadUpConnFlt.setStatus(
        "current"
    )

lntCascadUpConnOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 10, 0, 2316)
)
lntCascadUpConnOk.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupCascadUpStatus"))
)
if mibBuilder.loadTexts:
    lntCascadUpConnOk.setStatus(
        "current"
    )

lntCascadDownConnFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 10, 0, 2317)
)
lntCascadDownConnFlt.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupCascadDownStatus"))
)
if mibBuilder.loadTexts:
    lntCascadDownConnFlt.setStatus(
        "current"
    )

lntCascadDownConnOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 10, 0, 2318)
)
lntCascadDownConnOk.setObjects(
      *(("CONFIG-MIB", "genGroupFaultMask"),
        ("CONFIG-MIB", "genGroupId"),
        ("CONFIG-MIB", "genGroupCascadDownStatus"))
)
if mibBuilder.loadTexts:
    lntCascadDownConnOk.setStatus(
        "current"
    )

lntPolicyChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 11, 0, 60)
)
lntPolicyChangeEvent.setObjects(
      *(("POLICY-MIB", "ipPolicyActivationEntID"),
        ("POLICY-MIB", "ipPolicyActivationList"),
        ("POLICY-MIB", "ipPolicyActivationifIndex"),
        ("POLICY-MIB", "ipPolicyActivationSubContext"))
)
if mibBuilder.loadTexts:
    lntPolicyChangeEvent.setStatus(
        "current"
    )

lntPolicyAccessControlListLvlRuleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 11, 0, 62)
)
lntPolicyAccessControlListLvlRuleTrap.setObjects(
      *(("POLICY-MIB", "ipPolicyAccessControlViolationEntID"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationSrcAddr"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationDstAddr"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationProtocol"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationL4SrcPort"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationL4DstPort"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationEstablished"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationRuleType"),
        ("POLICY-MIB", "ipPolicyListID"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationIfIndex"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationSubCtxt"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationTime"))
)
if mibBuilder.loadTexts:
    lntPolicyAccessControlListLvlRuleTrap.setStatus(
        "current"
    )

lntPolicyAccessControlViolationFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 11, 0, 64)
)
lntPolicyAccessControlViolationFlt.setObjects(
      *(("POLICY-MIB", "ipPolicyAccessControlViolationEntID"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationSrcAddr"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationDstAddr"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationProtocol"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationL4SrcPort"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationL4DstPort"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationEstablished"),
        ("POLICY-MIB", "ipPolicyRuleID"),
        ("POLICY-MIB", "ipPolicyRuleListID"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationIfIndex"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationSubCtxt"),
        ("POLICY-MIB", "ipPolicyAccessControlViolationTime"),
        ("POLICY-MIB", "ipPolicyRuleDescription"))
)
if mibBuilder.loadTexts:
    lntPolicyAccessControlViolationFlt.setStatus(
        "current"
    )

lntEthPortAutoNegotiationFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3001)
)
lntEthPortAutoNegotiationFlt.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntEthPortAutoNegotiationFlt.setStatus(
        "current"
    )

lntEthPortAutoNegotiationOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3002)
)
lntEthPortAutoNegotiationOK.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntEthPortAutoNegotiationOK.setStatus(
        "current"
    )

lntPortFEFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3005)
)
lntPortFEFlt.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortFEFlt.setStatus(
        "current"
    )

lntPortFEOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3006)
)
lntPortFEOk.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortFEOk.setStatus(
        "current"
    )

lntVPortFEFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3015)
)
lntVPortFEFlt.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntVPortFEFlt.setStatus(
        "current"
    )

lntVPortFEOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3016)
)
lntVPortFEOk.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntVPortFEOk.setStatus(
        "current"
    )

lntPortAutoPartFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3023)
)
lntPortAutoPartFlt.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortAutoPartFlt.setStatus(
        "current"
    )

lntPortAutoPartOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3024)
)
lntPortAutoPartOk.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortAutoPartOk.setStatus(
        "current"
    )

lntVPortAutoPartFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3025)
)
lntVPortAutoPartFlt.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntVPortAutoPartFlt.setStatus(
        "current"
    )

lntVPortAutoPartOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3026)
)
lntVPortAutoPartOK.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntVPortAutoPartOK.setStatus(
        "current"
    )

lntEthVPortAutoNegotiationFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3031)
)
lntEthVPortAutoNegotiationFlt.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntEthVPortAutoNegotiationFlt.setStatus(
        "current"
    )

lntEthVPortAutoNegotiationOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3032)
)
lntEthVPortAutoNegotiationOK.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntEthVPortAutoNegotiationOK.setStatus(
        "current"
    )

lntPortInlinePowerFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3933)
)
lntPortInlinePowerFlt.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortInlinePowerFlt.setStatus(
        "current"
    )

lntPortInlinePowerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 12, 0, 3934)
)
lntPortInlinePowerOK.setObjects(
      *(("CONFIG-MIB", "genPortFaultMask"),
        ("CONFIG-MIB", "genPortGroupId"),
        ("CONFIG-MIB", "genPortId"))
)
if mibBuilder.loadTexts:
    lntPortInlinePowerOK.setStatus(
        "current"
    )

lntUnAuthAccessEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 68)
)
lntUnAuthAccessEvent.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntUnauthUserName"),
        ("Lannet-Trapsv2-MIB", "lntUnauthIpAddress"),
        ("Lannet-Trapsv2-MIB", "lntUnauthProtocol"))
)
if mibBuilder.loadTexts:
    lntUnAuthAccessEvent.setStatus(
        "current"
    )

lntMACSecurityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 104)
)
lntMACSecurityEvent.setObjects(
      *(("XSWITCH-MIB", "scGenPortLastIntruderSourceAddr"),
        ("XSWITCH-MIB", "scGenPortGroupId"),
        ("XSWITCH-MIB", "scGenPortId"))
)
if mibBuilder.loadTexts:
    lntMACSecurityEvent.setStatus(
        "current"
    )

lntUnknownHostCopyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1002)
)
lntUnknownHostCopyEvent.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntUnauthUserName"),
        ("Lannet-Trapsv2-MIB", "lntUnauthIpAddress"),
        ("Lannet-Trapsv2-MIB", "lntSCPStrictCheckingMode"))
)
if mibBuilder.loadTexts:
    lntUnknownHostCopyEvent.setStatus(
        "current"
    )

lntAccountLockoutEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1003)
)
lntAccountLockoutEvent.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntUnauthUserName"),
        ("Lannet-Trapsv2-MIB", "lntUnauthIpAddress"),
        ("Lannet-Trapsv2-MIB", "lntUnauthProtocol"))
)
if mibBuilder.loadTexts:
    lntAccountLockoutEvent.setStatus(
        "current"
    )

lntLicenseStartupValidationFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1004)
)
lntLicenseStartupValidationFlt.setObjects(
    ("Lannet-Trapsv2-MIB", "lntLicenseErrorCodes")
)
if mibBuilder.loadTexts:
    lntLicenseStartupValidationFlt.setStatus(
        "current"
    )

lntLicenseDownloadValidationFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1005)
)
lntLicenseDownloadValidationFlt.setObjects(
    ("Lannet-Trapsv2-MIB", "lntLicenseErrorCodes")
)
if mibBuilder.loadTexts:
    lntLicenseDownloadValidationFlt.setStatus(
        "current"
    )

lntDot1xMaxAuthRateReachedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1006)
)
lntDot1xMaxAuthRateReachedEvent.setObjects(
    ("XSWITCH-MIB", "scGenPortGroupId")
)
if mibBuilder.loadTexts:
    lntDot1xMaxAuthRateReachedEvent.setStatus(
        "current"
    )

lntDot1xAuthFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1007)
)
lntDot1xAuthFailureEvent.setObjects(
      *(("XSWITCH-MIB", "scGenPortDot1xMAC"),
        ("XSWITCH-MIB", "scGenPortGroupId"),
        ("XSWITCH-MIB", "scGenPortId"),
        ("Lannet-Trapsv2-MIB", "scGenPortDot1xFailureString"))
)
if mibBuilder.loadTexts:
    lntDot1xAuthFailureEvent.setStatus(
        "current"
    )

lntDot1xMaxAuthModuleNumReachedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1008)
)
lntDot1xMaxAuthModuleNumReachedEvent.setObjects(
      *(("XSWITCH-MIB", "scGenGroupDot1xSystemMaxNumSupplicant"),
        ("XSWITCH-MIB", "scGenPortGroupId"))
)
if mibBuilder.loadTexts:
    lntDot1xMaxAuthModuleNumReachedEvent.setStatus(
        "current"
    )

lntDot1xMaxAuthPortNumReachedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 13, 0, 1009)
)
lntDot1xMaxAuthPortNumReachedEvent.setObjects(
      *(("XSWITCH-MIB", "scGenSwitchDot1xPortMaxSuppNum"),
        ("XSWITCH-MIB", "scGenPortGroupId"),
        ("XSWITCH-MIB", "scGenPortId"))
)
if mibBuilder.loadTexts:
    lntDot1xMaxAuthPortNumReachedEvent.setStatus(
        "current"
    )

lntWanPhysicalAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 30)
)
lntWanPhysicalAlarmOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanPhysicalAlarmOn.setStatus(
        "current"
    )

lntWanPhysicalAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 31)
)
lntWanPhysicalAlarmOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanPhysicalAlarmOff.setStatus(
        "current"
    )

lntWanLocalAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 32)
)
lntWanLocalAlarmOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanLocalAlarmOn.setStatus(
        "current"
    )

lntWanLocalAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 33)
)
lntWanLocalAlarmOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanLocalAlarmOff.setStatus(
        "current"
    )

lntWanRemoteAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 34)
)
lntWanRemoteAlarmOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanRemoteAlarmOn.setStatus(
        "current"
    )

lntWanRemoteAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 35)
)
lntWanRemoteAlarmOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanRemoteAlarmOff.setStatus(
        "current"
    )

lntWanMinorAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 36)
)
lntWanMinorAlarmOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanMinorAlarmOn.setStatus(
        "current"
    )

lntWanMinorAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 38, 15, 0, 37)
)
lntWanMinorAlarmOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    lntWanMinorAlarmOff.setStatus(
        "current"
    )


# Notifications groups

lntLagNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 5)
)
lntLagNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntLAGConnLostFlt"),
        ("Lannet-Trapsv2-MIB", "lntLAGConnLostOk"),
        ("Lannet-Trapsv2-MIB", "lntLAGPartialConnLostFlt"),
        ("Lannet-Trapsv2-MIB", "lntLAGPartialConnLostOk"),
        ("Lannet-Trapsv2-MIB", "lntLAGAutoNegFlt"),
        ("Lannet-Trapsv2-MIB", "lntLAGAutoNegOk"),
        ("Lannet-Trapsv2-MIB", "lntLAGDeleteEvent"),
        ("Lannet-Trapsv2-MIB", "lntLAGCreateEvent"))
)
if mibBuilder.loadTexts:
    lntLagNotificationGroup.setStatus(
        "current"
    )

lntSWRedundancyNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 6)
)
lntSWRedundancyNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntSoftRedDelEvent"),
        ("Lannet-Trapsv2-MIB", "lntSoftRedNewEvent"))
)
if mibBuilder.loadTexts:
    lntSWRedundancyNotificationGroup.setStatus(
        "current"
    )

lntPSUFaultNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 7)
)
lntPSUFaultNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntMainPSUFlt"),
        ("Lannet-Trapsv2-MIB", "lntMainPSUOk"),
        ("Lannet-Trapsv2-MIB", "lntBackupPSUFlt"),
        ("Lannet-Trapsv2-MIB", "lntBackupPSUOk"))
)
if mibBuilder.loadTexts:
    lntPSUFaultNotificationGroup.setStatus(
        "current"
    )

lntTempratureNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 8)
)
lntTempratureNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntTempratureOk"),
        ("Lannet-Trapsv2-MIB", "lntTempratureWarning"))
)
if mibBuilder.loadTexts:
    lntTempratureNotificationGroup.setStatus(
        "current"
    )

lntL3FaultNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 9)
)
lntL3FaultNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntDuplicateIPFlt"),
        ("Lannet-Trapsv2-MIB", "lntVLANViolationEvent"),
        ("Lannet-Trapsv2-MIB", "lntARPViolationEvent"))
)
if mibBuilder.loadTexts:
    lntL3FaultNotificationGroup.setStatus(
        "current"
    )

lntLinkDownNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 10)
)
lntLinkDownNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntPortLinkDownEvent"),
        ("Lannet-Trapsv2-MIB", "lntPortLinkUpEvent"),
        ("Lannet-Trapsv2-MIB", "lntVPortLinkDownEvent"),
        ("Lannet-Trapsv2-MIB", "lntVPortLinkUpEvent"))
)
if mibBuilder.loadTexts:
    lntLinkDownNotificationGroup.setStatus(
        "current"
    )

lntCascadeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 11)
)
lntCascadeNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntCascadUpConnFlt"),
        ("Lannet-Trapsv2-MIB", "lntCascadUpConnOk"),
        ("Lannet-Trapsv2-MIB", "lntCascadDownConnOk"),
        ("Lannet-Trapsv2-MIB", "lntCascadDownConnFlt"))
)
if mibBuilder.loadTexts:
    lntCascadeNotificationGroup.setStatus(
        "current"
    )

lntEthPortNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 12)
)
lntEthPortNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntPortFEFlt"),
        ("Lannet-Trapsv2-MIB", "lntPortFEOk"),
        ("Lannet-Trapsv2-MIB", "lntVPortFEFlt"),
        ("Lannet-Trapsv2-MIB", "lntVPortFEOk"),
        ("Lannet-Trapsv2-MIB", "lntPortAutoPartFlt"),
        ("Lannet-Trapsv2-MIB", "lntPortAutoPartOk"),
        ("Lannet-Trapsv2-MIB", "lntVPortAutoPartFlt"),
        ("Lannet-Trapsv2-MIB", "lntVPortAutoPartOK"),
        ("Lannet-Trapsv2-MIB", "lntEthVPortAutoNegotiationOK"),
        ("Lannet-Trapsv2-MIB", "lntEthPortAutoNegotiationOK"),
        ("Lannet-Trapsv2-MIB", "lntEthPortAutoNegotiationFlt"),
        ("Lannet-Trapsv2-MIB", "lntEthVPortAutoNegotiationFlt"),
        ("Lannet-Trapsv2-MIB", "lntPortInlinePowerFlt"),
        ("Lannet-Trapsv2-MIB", "lntPortInlinePowerOK"))
)
if mibBuilder.loadTexts:
    lntEthPortNotificationGroup.setStatus(
        "current"
    )

lntCAMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 13)
)
lntCAMNotificationGroup.setObjects(
    ("Lannet-Trapsv2-MIB", "lntPortCAMLastChange")
)
if mibBuilder.loadTexts:
    lntCAMNotificationGroup.setStatus(
        "obsolete"
    )

lntConfigChangeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 14)
)
lntConfigChangeNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntConfigChangeEvent"),
        ("Lannet-Trapsv2-MIB", "lntStackMasterReelection"))
)
if mibBuilder.loadTexts:
    lntConfigChangeNotificationGroup.setStatus(
        "current"
    )

lntPolicyNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 15)
)
lntPolicyNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntPolicyAccessControlListLvlRuleTrap"),
        ("Lannet-Trapsv2-MIB", "lntPolicyAccessControlViolationFlt"),
        ("Lannet-Trapsv2-MIB", "lntPolicyChangeEvent"))
)
if mibBuilder.loadTexts:
    lntPolicyNotificationGroup.setStatus(
        "current"
    )

lntFansNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 16)
)
lntFansNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntBackupFansFlt"),
        ("Lannet-Trapsv2-MIB", "lntBackupFansOK"),
        ("Lannet-Trapsv2-MIB", "lntMainFansFlt"),
        ("Lannet-Trapsv2-MIB", "lntMainFansOK"))
)
if mibBuilder.loadTexts:
    lntFansNotificationGroup.setStatus(
        "current"
    )

lntSecurityNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 17)
)
lntSecurityNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntAccountLockoutEvent"),
        ("Lannet-Trapsv2-MIB", "lntMACSecurityEvent"),
        ("Lannet-Trapsv2-MIB", "lntUnAuthAccessEvent"),
        ("Lannet-Trapsv2-MIB", "lntUnknownHostCopyEvent"),
        ("Lannet-Trapsv2-MIB", "lntLicenseStartupValidationFlt"),
        ("Lannet-Trapsv2-MIB", "lntLicenseDownloadValidationFlt"))
)
if mibBuilder.loadTexts:
    lntSecurityNotificationGroup.setStatus(
        "current"
    )

lntWanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 81, 38, 10007, 18)
)
lntWanNotificationGroup.setObjects(
      *(("Lannet-Trapsv2-MIB", "lntWanPhysicalAlarmOn"),
        ("Lannet-Trapsv2-MIB", "lntWanPhysicalAlarmOff"),
        ("Lannet-Trapsv2-MIB", "lntWanLocalAlarmOn"),
        ("Lannet-Trapsv2-MIB", "lntWanLocalAlarmOff"),
        ("Lannet-Trapsv2-MIB", "lntWanRemoteAlarmOn"),
        ("Lannet-Trapsv2-MIB", "lntWanRemoteAlarmOff"),
        ("Lannet-Trapsv2-MIB", "lntWanMinorAlarmOn"),
        ("Lannet-Trapsv2-MIB", "lntWanMinorAlarmOff"))
)
if mibBuilder.loadTexts:
    lntWanNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities

lntP330L3NotificationAgentCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 81, 38, 10008, 1)
)
if mibBuilder.loadTexts:
    lntP330L3NotificationAgentCapabilities.setStatus(
        "current"
    )

lntP330L2NotificationAgentCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 81, 38, 10008, 2)
)
if mibBuilder.loadTexts:
    lntP330L2NotificationAgentCapabilities.setStatus(
        "current"
    )

lntP130TrapAgentCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 81, 38, 10008, 3)
)
if mibBuilder.loadTexts:
    lntP130TrapAgentCapabilities.setStatus(
        "current"
    )

lntP330MLNotificationAgentCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 81, 38, 10008, 4)
)
if mibBuilder.loadTexts:
    lntP330MLNotificationAgentCapabilities.setStatus(
        "current"
    )

lntG350NotificationAgentCapability = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 81, 38, 10008, 5)
)
if mibBuilder.loadTexts:
    lntG350NotificationAgentCapability.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Lannet-Trapsv2-MIB",
    **{"lntTraps": lntTraps,
       "lntConfigChangeEvents": lntConfigChangeEvents,
       "lntConfigChangePrefix": lntConfigChangePrefix,
       "lntConfigChangeEvent": lntConfigChangeEvent,
       "lntStackMasterReelection": lntStackMasterReelection,
       "lntSWRedundancyEvents": lntSWRedundancyEvents,
       "lntSWRedundancyPrefix": lntSWRedundancyPrefix,
       "lntSoftRedDelEvent": lntSoftRedDelEvent,
       "lntSoftRedNewEvent": lntSoftRedNewEvent,
       "lntTempratureEvents": lntTempratureEvents,
       "lntTempratureWarningPrefix": lntTempratureWarningPrefix,
       "lntTempratureWarning": lntTempratureWarning,
       "lntTempratureOk": lntTempratureOk,
       "lntCAMChangeEvents": lntCAMChangeEvents,
       "lntCAMChangePrefix": lntCAMChangePrefix,
       "lntPortCAMLastChange": lntPortCAMLastChange,
       "lntPSUEvents": lntPSUEvents,
       "lntPSUPrefix": lntPSUPrefix,
       "lntMainPSUFlt": lntMainPSUFlt,
       "lntMainPSUOk": lntMainPSUOk,
       "lntBackupPSUFlt": lntBackupPSUFlt,
       "lntBackupPSUOk": lntBackupPSUOk,
       "lntL3Events": lntL3Events,
       "lntL3FaultsPrefix": lntL3FaultsPrefix,
       "lntDuplicateIPFlt": lntDuplicateIPFlt,
       "lntVLANViolationEvent": lntVLANViolationEvent,
       "lntARPViolationEvent": lntARPViolationEvent,
       "lntLinkEvents": lntLinkEvents,
       "lntLinkEventsPrefix": lntLinkEventsPrefix,
       "lntPortLinkDownEvent": lntPortLinkDownEvent,
       "lntPortLinkUpEvent": lntPortLinkUpEvent,
       "lntVPortLinkDownEvent": lntVPortLinkDownEvent,
       "lntVPortLinkUpEvent": lntVPortLinkUpEvent,
       "lntLAGEvents": lntLAGEvents,
       "lntLAGPrefix": lntLAGPrefix,
       "lntLAGConnLostFlt": lntLAGConnLostFlt,
       "lntLAGConnLostOk": lntLAGConnLostOk,
       "lntLAGPartialConnLostFlt": lntLAGPartialConnLostFlt,
       "lntLAGPartialConnLostOk": lntLAGPartialConnLostOk,
       "lntLAGAutoNegFlt": lntLAGAutoNegFlt,
       "lntLAGAutoNegOk": lntLAGAutoNegOk,
       "lntLAGDeleteEvent": lntLAGDeleteEvent,
       "lntLAGCreateEvent": lntLAGCreateEvent,
       "lntFansEvents": lntFansEvents,
       "lntFansPrefix": lntFansPrefix,
       "lntMainFansFlt": lntMainFansFlt,
       "lntMainFansOK": lntMainFansOK,
       "lntBackupFansFlt": lntBackupFansFlt,
       "lntBackupFansOK": lntBackupFansOK,
       "lntCascadeEvents": lntCascadeEvents,
       "lntCascadeFaultsPrefix": lntCascadeFaultsPrefix,
       "lntCascadUpConnFlt": lntCascadUpConnFlt,
       "lntCascadUpConnOk": lntCascadUpConnOk,
       "lntCascadDownConnFlt": lntCascadDownConnFlt,
       "lntCascadDownConnOk": lntCascadDownConnOk,
       "lntPolicyEvents": lntPolicyEvents,
       "lntPolicyPrefix": lntPolicyPrefix,
       "lntPolicyChangeEvent": lntPolicyChangeEvent,
       "lntPolicyAccessControlListLvlRuleTrap": lntPolicyAccessControlListLvlRuleTrap,
       "lntPolicyAccessControlViolationFlt": lntPolicyAccessControlViolationFlt,
       "lntEthPortFaultEvents": lntEthPortFaultEvents,
       "lntEthPortFaultPrefix": lntEthPortFaultPrefix,
       "lntEthPortAutoNegotiationFlt": lntEthPortAutoNegotiationFlt,
       "lntEthPortAutoNegotiationOK": lntEthPortAutoNegotiationOK,
       "lntPortFEFlt": lntPortFEFlt,
       "lntPortFEOk": lntPortFEOk,
       "lntVPortFEFlt": lntVPortFEFlt,
       "lntVPortFEOk": lntVPortFEOk,
       "lntPortAutoPartFlt": lntPortAutoPartFlt,
       "lntPortAutoPartOk": lntPortAutoPartOk,
       "lntVPortAutoPartFlt": lntVPortAutoPartFlt,
       "lntVPortAutoPartOK": lntVPortAutoPartOK,
       "lntEthVPortAutoNegotiationFlt": lntEthVPortAutoNegotiationFlt,
       "lntEthVPortAutoNegotiationOK": lntEthVPortAutoNegotiationOK,
       "lntPortInlinePowerFlt": lntPortInlinePowerFlt,
       "lntPortInlinePowerOK": lntPortInlinePowerOK,
       "lntSecurityEvents": lntSecurityEvents,
       "lntSecurityPrefix": lntSecurityPrefix,
       "lntUnAuthAccessEvent": lntUnAuthAccessEvent,
       "lntMACSecurityEvent": lntMACSecurityEvent,
       "lntUnknownHostCopyEvent": lntUnknownHostCopyEvent,
       "lntAccountLockoutEvent": lntAccountLockoutEvent,
       "lntLicenseStartupValidationFlt": lntLicenseStartupValidationFlt,
       "lntLicenseDownloadValidationFlt": lntLicenseDownloadValidationFlt,
       "lntDot1xMaxAuthRateReachedEvent": lntDot1xMaxAuthRateReachedEvent,
       "lntDot1xAuthFailureEvent": lntDot1xAuthFailureEvent,
       "lntDot1xMaxAuthModuleNumReachedEvent": lntDot1xMaxAuthModuleNumReachedEvent,
       "lntDot1xMaxAuthPortNumReachedEvent": lntDot1xMaxAuthPortNumReachedEvent,
       "lntNotificationVarbinds": lntNotificationVarbinds,
       "lntConfigChangeValue": lntConfigChangeValue,
       "lntConfigChangeOID": lntConfigChangeOID,
       "lntUnauthUserName": lntUnauthUserName,
       "lntUnauthIpAddress": lntUnauthIpAddress,
       "lntUnauthProtocol": lntUnauthProtocol,
       "lntSCPStrictCheckingMode": lntSCPStrictCheckingMode,
       "lntLicenseErrorCodes": lntLicenseErrorCodes,
       "scGenPortDot1xFailureString": scGenPortDot1xFailureString,
       "lntWanEvents": lntWanEvents,
       "lntWanPrefix": lntWanPrefix,
       "lntWanPhysicalAlarmOn": lntWanPhysicalAlarmOn,
       "lntWanPhysicalAlarmOff": lntWanPhysicalAlarmOff,
       "lntWanLocalAlarmOn": lntWanLocalAlarmOn,
       "lntWanLocalAlarmOff": lntWanLocalAlarmOff,
       "lntWanRemoteAlarmOn": lntWanRemoteAlarmOn,
       "lntWanRemoteAlarmOff": lntWanRemoteAlarmOff,
       "lntWanMinorAlarmOn": lntWanMinorAlarmOn,
       "lntWanMinorAlarmOff": lntWanMinorAlarmOff,
       "lntNotificationGroups": lntNotificationGroups,
       "lntConfigChangeVarbinds": lntConfigChangeVarbinds,
       "lntLagNotificationGroup": lntLagNotificationGroup,
       "lntSWRedundancyNotificationGroup": lntSWRedundancyNotificationGroup,
       "lntPSUFaultNotificationGroup": lntPSUFaultNotificationGroup,
       "lntTempratureNotificationGroup": lntTempratureNotificationGroup,
       "lntL3FaultNotificationGroup": lntL3FaultNotificationGroup,
       "lntLinkDownNotificationGroup": lntLinkDownNotificationGroup,
       "lntCascadeNotificationGroup": lntCascadeNotificationGroup,
       "lntEthPortNotificationGroup": lntEthPortNotificationGroup,
       "lntCAMNotificationGroup": lntCAMNotificationGroup,
       "lntConfigChangeNotificationGroup": lntConfigChangeNotificationGroup,
       "lntPolicyNotificationGroup": lntPolicyNotificationGroup,
       "lntFansNotificationGroup": lntFansNotificationGroup,
       "lntSecurityNotificationGroup": lntSecurityNotificationGroup,
       "lntWanNotificationGroup": lntWanNotificationGroup,
       "lntNotificationAgentCapabilities": lntNotificationAgentCapabilities,
       "lntP330L3NotificationAgentCapabilities": lntP330L3NotificationAgentCapabilities,
       "lntP330L2NotificationAgentCapabilities": lntP330L2NotificationAgentCapabilities,
       "lntP130TrapAgentCapabilities": lntP130TrapAgentCapabilities,
       "lntP330MLNotificationAgentCapabilities": lntP330MLNotificationAgentCapabilities,
       "lntG350NotificationAgentCapability": lntG350NotificationAgentCapability}
)
