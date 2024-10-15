# SNMP MIB module (INCOGNITO-EXPR-IPCOMMANDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INCOGNITO-EXPR-IPCOMMANDER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:04 2024
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

(incognitoExpr,) = mibBuilder.importSymbols(
    "INCOGNITO-MIB",
    "incognitoExpr")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

incognitoIPC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1)
)
incognitoIPC.setRevisions(
        ("2008-02-13 18:02",
         "2008-05-07 18:34",
         "2009-05-08 17:00",
         "2009-07-30 11:00",
         "2009-09-15 09:00",
         "2009-11-06 09:00",
         "2009-11-06 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DraftServerMIB_ObjectIdentity = ObjectIdentity
draftServerMIB = _DraftServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 1)
)
if mibBuilder.loadTexts:
    draftServerMIB.setStatus("current")
_IpcServerObjects_ObjectIdentity = ObjectIdentity
ipcServerObjects = _IpcServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ipcServerObjects.setStatus("current")
_IpcServiceStatisticsConformance_ObjectIdentity = ObjectIdentity
ipcServiceStatisticsConformance = _IpcServiceStatisticsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipcServiceStatisticsConformance.setStatus("current")
_IpcServiceStatisticsCompliances_ObjectIdentity = ObjectIdentity
ipcServiceStatisticsCompliances = _IpcServiceStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 1, 1)
)
_IpcServiceSatisticsGroups_ObjectIdentity = ObjectIdentity
ipcServiceSatisticsGroups = _IpcServiceSatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 1, 2)
)
_IpcServiceInformationGroups_ObjectIdentity = ObjectIdentity
ipcServiceInformationGroups = _IpcServiceInformationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 1, 3)
)
_IpcDHCPStatistics_ObjectIdentity = ObjectIdentity
ipcDHCPStatistics = _IpcDHCPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipcDHCPStatistics.setStatus("current")
_IpcDHCPPacketStatistics_ObjectIdentity = ObjectIdentity
ipcDHCPPacketStatistics = _IpcDHCPPacketStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipcDHCPPacketStatistics.setStatus("current")
_IpcDHCPPacketDiscardStatistics_ObjectIdentity = ObjectIdentity
ipcDHCPPacketDiscardStatistics = _IpcDHCPPacketDiscardStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipcDHCPPacketDiscardStatistics.setStatus("current")
_IpcDHCPDiscoverPacketDiscards_Type = Counter32
_IpcDHCPDiscoverPacketDiscards_Object = MibScalar
ipcDHCPDiscoverPacketDiscards = _IpcDHCPDiscoverPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 1, 1),
    _IpcDHCPDiscoverPacketDiscards_Type()
)
ipcDHCPDiscoverPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPDiscoverPacketDiscards.setStatus("current")
_IpcDHCPRequestPacketDiscards_Type = Counter32
_IpcDHCPRequestPacketDiscards_Object = MibScalar
ipcDHCPRequestPacketDiscards = _IpcDHCPRequestPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 1, 2),
    _IpcDHCPRequestPacketDiscards_Type()
)
ipcDHCPRequestPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPRequestPacketDiscards.setStatus("current")
_IpcDHCPInformPacketDiscards_Type = Counter32
_IpcDHCPInformPacketDiscards_Object = MibScalar
ipcDHCPInformPacketDiscards = _IpcDHCPInformPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 1, 3),
    _IpcDHCPInformPacketDiscards_Type()
)
ipcDHCPInformPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPInformPacketDiscards.setStatus("current")
_IpcDHCPDeclinePacketDiscards_Type = Counter32
_IpcDHCPDeclinePacketDiscards_Object = MibScalar
ipcDHCPDeclinePacketDiscards = _IpcDHCPDeclinePacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 1, 4),
    _IpcDHCPDeclinePacketDiscards_Type()
)
ipcDHCPDeclinePacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPDeclinePacketDiscards.setStatus("current")
_IpcDHCPOtherPacketDiscards_Type = Counter32
_IpcDHCPOtherPacketDiscards_Object = MibScalar
ipcDHCPOtherPacketDiscards = _IpcDHCPOtherPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 1, 5),
    _IpcDHCPOtherPacketDiscards_Type()
)
ipcDHCPOtherPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPOtherPacketDiscards.setStatus("current")
_IpcDHCPPacketSupercedeStatistics_ObjectIdentity = ObjectIdentity
ipcDHCPPacketSupercedeStatistics = _IpcDHCPPacketSupercedeStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ipcDHCPPacketSupercedeStatistics.setStatus("current")
_IpcDHCPDiscoverPacketSupercedes_Type = Counter32
_IpcDHCPDiscoverPacketSupercedes_Object = MibScalar
ipcDHCPDiscoverPacketSupercedes = _IpcDHCPDiscoverPacketSupercedes_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 2, 1),
    _IpcDHCPDiscoverPacketSupercedes_Type()
)
ipcDHCPDiscoverPacketSupercedes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPDiscoverPacketSupercedes.setStatus("current")
_IpcDHCPRequestPacketSupercedes_Type = Counter32
_IpcDHCPRequestPacketSupercedes_Object = MibScalar
ipcDHCPRequestPacketSupercedes = _IpcDHCPRequestPacketSupercedes_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 2, 2),
    _IpcDHCPRequestPacketSupercedes_Type()
)
ipcDHCPRequestPacketSupercedes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPRequestPacketSupercedes.setStatus("current")
_IpcDHCPInformPacketSupercedes_Type = Counter32
_IpcDHCPInformPacketSupercedes_Object = MibScalar
ipcDHCPInformPacketSupercedes = _IpcDHCPInformPacketSupercedes_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 2, 3),
    _IpcDHCPInformPacketSupercedes_Type()
)
ipcDHCPInformPacketSupercedes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPInformPacketSupercedes.setStatus("current")
_IpcDHCPDeclinePacketSupercedes_Type = Counter32
_IpcDHCPDeclinePacketSupercedes_Object = MibScalar
ipcDHCPDeclinePacketSupercedes = _IpcDHCPDeclinePacketSupercedes_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 2, 4),
    _IpcDHCPDeclinePacketSupercedes_Type()
)
ipcDHCPDeclinePacketSupercedes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPDeclinePacketSupercedes.setStatus("current")
_IpcDHCPOtherPacketSupercedes_Type = Counter32
_IpcDHCPOtherPacketSupercedes_Object = MibScalar
ipcDHCPOtherPacketSupercedes = _IpcDHCPOtherPacketSupercedes_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 2, 5),
    _IpcDHCPOtherPacketSupercedes_Type()
)
ipcDHCPOtherPacketSupercedes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPOtherPacketSupercedes.setStatus("current")
_IpcDHCPPacketResponseStatistics_ObjectIdentity = ObjectIdentity
ipcDHCPPacketResponseStatistics = _IpcDHCPPacketResponseStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ipcDHCPPacketResponseStatistics.setStatus("current")
_IpcDHCPBOOTPPacketResponseAvg1minTime_Type = Unsigned32
_IpcDHCPBOOTPPacketResponseAvg1minTime_Object = MibScalar
ipcDHCPBOOTPPacketResponseAvg1minTime = _IpcDHCPBOOTPPacketResponseAvg1minTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 3, 1),
    _IpcDHCPBOOTPPacketResponseAvg1minTime_Type()
)
ipcDHCPBOOTPPacketResponseAvg1minTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPBOOTPPacketResponseAvg1minTime.setStatus("current")
_IpcDHCPBOOTPPacketResponseAvg5minTime_Type = Unsigned32
_IpcDHCPBOOTPPacketResponseAvg5minTime_Object = MibScalar
ipcDHCPBOOTPPacketResponseAvg5minTime = _IpcDHCPBOOTPPacketResponseAvg5minTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 3, 2),
    _IpcDHCPBOOTPPacketResponseAvg5minTime_Type()
)
ipcDHCPBOOTPPacketResponseAvg5minTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPBOOTPPacketResponseAvg5minTime.setStatus("current")
_IpcDHCPBOOTPPacketResponseAvg15minTime_Type = Unsigned32
_IpcDHCPBOOTPPacketResponseAvg15minTime_Object = MibScalar
ipcDHCPBOOTPPacketResponseAvg15minTime = _IpcDHCPBOOTPPacketResponseAvg15minTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 3, 3),
    _IpcDHCPBOOTPPacketResponseAvg15minTime_Type()
)
ipcDHCPBOOTPPacketResponseAvg15minTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPBOOTPPacketResponseAvg15minTime.setStatus("current")
_IpcDHCPDHCPv4PacketResponseAvg1minTime_Type = Unsigned32
_IpcDHCPDHCPv4PacketResponseAvg1minTime_Object = MibScalar
ipcDHCPDHCPv4PacketResponseAvg1minTime = _IpcDHCPDHCPv4PacketResponseAvg1minTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 3, 4),
    _IpcDHCPDHCPv4PacketResponseAvg1minTime_Type()
)
ipcDHCPDHCPv4PacketResponseAvg1minTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPDHCPv4PacketResponseAvg1minTime.setStatus("current")
_IpcDHCPDHCPv4PacketResponseAvg5minTime_Type = Unsigned32
_IpcDHCPDHCPv4PacketResponseAvg5minTime_Object = MibScalar
ipcDHCPDHCPv4PacketResponseAvg5minTime = _IpcDHCPDHCPv4PacketResponseAvg5minTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 3, 5),
    _IpcDHCPDHCPv4PacketResponseAvg5minTime_Type()
)
ipcDHCPDHCPv4PacketResponseAvg5minTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPDHCPv4PacketResponseAvg5minTime.setStatus("current")
_IpcDHCPDHCPv4PacketResponseAvg15minTime_Type = Unsigned32
_IpcDHCPDHCPv4PacketResponseAvg15minTime_Object = MibScalar
ipcDHCPDHCPv4PacketResponseAvg15minTime = _IpcDHCPDHCPv4PacketResponseAvg15minTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 2, 1, 3, 6),
    _IpcDHCPDHCPv4PacketResponseAvg15minTime_Type()
)
ipcDHCPDHCPv4PacketResponseAvg15minTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcDHCPDHCPv4PacketResponseAvg15minTime.setStatus("current")
_IpcConfiguration_ObjectIdentity = ObjectIdentity
ipcConfiguration = _IpcConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipcConfiguration.setStatus("current")
_IpcNotifyObjects_ObjectIdentity = ObjectIdentity
ipcNotifyObjects = _IpcNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ipcNotifyObjects.setStatus("current")
_IpcPausedTime_Type = DateAndTime
_IpcPausedTime_Object = MibScalar
ipcPausedTime = _IpcPausedTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 4, 1),
    _IpcPausedTime_Type()
)
ipcPausedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcPausedTime.setStatus("current")
_IpcResumedTime_Type = DateAndTime
_IpcResumedTime_Object = MibScalar
ipcResumedTime = _IpcResumedTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 4, 2),
    _IpcResumedTime_Type()
)
ipcResumedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcResumedTime.setStatus("current")
_IpcDeprecatedNotifyObjects_ObjectIdentity = ObjectIdentity
ipcDeprecatedNotifyObjects = _IpcDeprecatedNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99)
)
if mibBuilder.loadTexts:
    ipcDeprecatedNotifyObjects.setStatus("current")
_IpcDhcpNotifyObjects_ObjectIdentity = ObjectIdentity
ipcDhcpNotifyObjects = _IpcDhcpNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1)
)
if mibBuilder.loadTexts:
    ipcDhcpNotifyObjects.setStatus("current")
_IpcmdDHCPFreeAddressLowThreshold_Type = Unsigned32
_IpcmdDHCPFreeAddressLowThreshold_Object = MibScalar
ipcmdDHCPFreeAddressLowThreshold = _IpcmdDHCPFreeAddressLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 1),
    _IpcmdDHCPFreeAddressLowThreshold_Type()
)
ipcmdDHCPFreeAddressLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFreeAddressLowThreshold.setStatus("current")
_IpcmdDHCPFreeAddressHighThreshold_Type = Unsigned32
_IpcmdDHCPFreeAddressHighThreshold_Object = MibScalar
ipcmdDHCPFreeAddressHighThreshold = _IpcmdDHCPFreeAddressHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 2),
    _IpcmdDHCPFreeAddressHighThreshold_Type()
)
ipcmdDHCPFreeAddressHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFreeAddressHighThreshold.setStatus("current")
_IpcmdDHCPFreeAddressCriticalThreshold_Type = Unsigned32
_IpcmdDHCPFreeAddressCriticalThreshold_Object = MibScalar
ipcmdDHCPFreeAddressCriticalThreshold = _IpcmdDHCPFreeAddressCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 3),
    _IpcmdDHCPFreeAddressCriticalThreshold_Type()
)
ipcmdDHCPFreeAddressCriticalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFreeAddressCriticalThreshold.setStatus("current")
_IpcmdDHCPFreeAddressValue_Type = Unsigned32
_IpcmdDHCPFreeAddressValue_Object = MibScalar
ipcmdDHCPFreeAddressValue = _IpcmdDHCPFreeAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 4),
    _IpcmdDHCPFreeAddressValue_Type()
)
ipcmdDHCPFreeAddressValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFreeAddressValue.setStatus("current")


class _IpcmdDHCPFreeAddressUnits_Type(Integer32):
    """Custom type ipcmdDHCPFreeAddressUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 2),
          ("value", 1))
    )


_IpcmdDHCPFreeAddressUnits_Type.__name__ = "Integer32"
_IpcmdDHCPFreeAddressUnits_Object = MibScalar
ipcmdDHCPFreeAddressUnits = _IpcmdDHCPFreeAddressUnits_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 5),
    _IpcmdDHCPFreeAddressUnits_Type()
)
ipcmdDHCPFreeAddressUnits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFreeAddressUnits.setStatus("current")


class _IpcmdDHCPRuleID_Type(DisplayString):
    """Custom type ipcmdDHCPRuleID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPRuleID_Type.__name__ = "DisplayString"
_IpcmdDHCPRuleID_Object = MibScalar
ipcmdDHCPRuleID = _IpcmdDHCPRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 6),
    _IpcmdDHCPRuleID_Type()
)
ipcmdDHCPRuleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPRuleID.setStatus("current")


class _IpcmdDHCPRuleName_Type(DisplayString):
    """Custom type ipcmdDHCPRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPRuleName_Type.__name__ = "DisplayString"
_IpcmdDHCPRuleName_Object = MibScalar
ipcmdDHCPRuleName = _IpcmdDHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 7),
    _IpcmdDHCPRuleName_Type()
)
ipcmdDHCPRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPRuleName.setStatus("current")
_IpcmdDHCPRogueServerAddress_Type = IpAddress
_IpcmdDHCPRogueServerAddress_Object = MibScalar
ipcmdDHCPRogueServerAddress = _IpcmdDHCPRogueServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 8),
    _IpcmdDHCPRogueServerAddress_Type()
)
ipcmdDHCPRogueServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPRogueServerAddress.setStatus("current")
_IpcmdDHCPRogueServerNumRequest_Type = Unsigned32
_IpcmdDHCPRogueServerNumRequest_Object = MibScalar
ipcmdDHCPRogueServerNumRequest = _IpcmdDHCPRogueServerNumRequest_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 9),
    _IpcmdDHCPRogueServerNumRequest_Type()
)
ipcmdDHCPRogueServerNumRequest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPRogueServerNumRequest.setStatus("current")


class _IpcmdDHCPRogueServerRequestTime_Type(DisplayString):
    """Custom type ipcmdDHCPRogueServerRequestTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPRogueServerRequestTime_Type.__name__ = "DisplayString"
_IpcmdDHCPRogueServerRequestTime_Object = MibScalar
ipcmdDHCPRogueServerRequestTime = _IpcmdDHCPRogueServerRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 10),
    _IpcmdDHCPRogueServerRequestTime_Type()
)
ipcmdDHCPRogueServerRequestTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPRogueServerRequestTime.setStatus("current")


class _IpcmdDHCPRogueServerInfo_Type(DisplayString):
    """Custom type ipcmdDHCPRogueServerInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPRogueServerInfo_Type.__name__ = "DisplayString"
_IpcmdDHCPRogueServerInfo_Object = MibScalar
ipcmdDHCPRogueServerInfo = _IpcmdDHCPRogueServerInfo_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 11),
    _IpcmdDHCPRogueServerInfo_Type()
)
ipcmdDHCPRogueServerInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPRogueServerInfo.setStatus("current")
_IpcmdDHCPCurrentUserCount_Type = Unsigned32
_IpcmdDHCPCurrentUserCount_Object = MibScalar
ipcmdDHCPCurrentUserCount = _IpcmdDHCPCurrentUserCount_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 12),
    _IpcmdDHCPCurrentUserCount_Type()
)
ipcmdDHCPCurrentUserCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPCurrentUserCount.setStatus("current")
_IpcmdDHCPLicenseCount_Type = Unsigned32
_IpcmdDHCPLicenseCount_Object = MibScalar
ipcmdDHCPLicenseCount = _IpcmdDHCPLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 13),
    _IpcmdDHCPLicenseCount_Type()
)
ipcmdDHCPLicenseCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPLicenseCount.setStatus("current")
_IpcmdDHCPExceedingLicenseLimit_Type = Unsigned32
_IpcmdDHCPExceedingLicenseLimit_Object = MibScalar
ipcmdDHCPExceedingLicenseLimit = _IpcmdDHCPExceedingLicenseLimit_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 14),
    _IpcmdDHCPExceedingLicenseLimit_Type()
)
ipcmdDHCPExceedingLicenseLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPExceedingLicenseLimit.setStatus("current")
_IpcmdDHCPFailoverConflictAddress_Type = IpAddress
_IpcmdDHCPFailoverConflictAddress_Object = MibScalar
ipcmdDHCPFailoverConflictAddress = _IpcmdDHCPFailoverConflictAddress_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 15),
    _IpcmdDHCPFailoverConflictAddress_Type()
)
ipcmdDHCPFailoverConflictAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFailoverConflictAddress.setStatus("current")


class _IpcmdDHCPNetViewName_Type(DisplayString):
    """Custom type ipcmdDHCPNetViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPNetViewName_Type.__name__ = "DisplayString"
_IpcmdDHCPNetViewName_Object = MibScalar
ipcmdDHCPNetViewName = _IpcmdDHCPNetViewName_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 16),
    _IpcmdDHCPNetViewName_Type()
)
ipcmdDHCPNetViewName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPNetViewName.setStatus("current")
_IpcmdDHCPCurrentHWM_Type = Unsigned32
_IpcmdDHCPCurrentHWM_Object = MibScalar
ipcmdDHCPCurrentHWM = _IpcmdDHCPCurrentHWM_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 17),
    _IpcmdDHCPCurrentHWM_Type()
)
ipcmdDHCPCurrentHWM.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPCurrentHWM.setStatus("current")


class _IpcmdDHCPFailoverResynchStartTime_Type(DisplayString):
    """Custom type ipcmdDHCPFailoverResynchStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPFailoverResynchStartTime_Type.__name__ = "DisplayString"
_IpcmdDHCPFailoverResynchStartTime_Object = MibScalar
ipcmdDHCPFailoverResynchStartTime = _IpcmdDHCPFailoverResynchStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 18),
    _IpcmdDHCPFailoverResynchStartTime_Type()
)
ipcmdDHCPFailoverResynchStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFailoverResynchStartTime.setStatus("current")


class _IpcmdDHCPFailoverResynchEndTime_Type(DisplayString):
    """Custom type ipcmdDHCPFailoverResynchEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPFailoverResynchEndTime_Type.__name__ = "DisplayString"
_IpcmdDHCPFailoverResynchEndTime_Object = MibScalar
ipcmdDHCPFailoverResynchEndTime = _IpcmdDHCPFailoverResynchEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 19),
    _IpcmdDHCPFailoverResynchEndTime_Type()
)
ipcmdDHCPFailoverResynchEndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFailoverResynchEndTime.setStatus("current")


class _IpcmdDHCPDuplicateDeviceHWAddress_Type(DisplayString):
    """Custom type ipcmdDHCPDuplicateDeviceHWAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPDuplicateDeviceHWAddress_Type.__name__ = "DisplayString"
_IpcmdDHCPDuplicateDeviceHWAddress_Object = MibScalar
ipcmdDHCPDuplicateDeviceHWAddress = _IpcmdDHCPDuplicateDeviceHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 20),
    _IpcmdDHCPDuplicateDeviceHWAddress_Type()
)
ipcmdDHCPDuplicateDeviceHWAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPDuplicateDeviceHWAddress.setStatus("current")
_IpcmdDHCPDuplicateDeviceIPAddress_Type = IpAddress
_IpcmdDHCPDuplicateDeviceIPAddress_Object = MibScalar
ipcmdDHCPDuplicateDeviceIPAddress = _IpcmdDHCPDuplicateDeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 21),
    _IpcmdDHCPDuplicateDeviceIPAddress_Type()
)
ipcmdDHCPDuplicateDeviceIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPDuplicateDeviceIPAddress.setStatus("current")


class _IpcmdDHCPDuplicateDeviceRemoteID_Type(DisplayString):
    """Custom type ipcmdDHCPDuplicateDeviceRemoteID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPDuplicateDeviceRemoteID_Type.__name__ = "DisplayString"
_IpcmdDHCPDuplicateDeviceRemoteID_Object = MibScalar
ipcmdDHCPDuplicateDeviceRemoteID = _IpcmdDHCPDuplicateDeviceRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 22),
    _IpcmdDHCPDuplicateDeviceRemoteID_Type()
)
ipcmdDHCPDuplicateDeviceRemoteID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPDuplicateDeviceRemoteID.setStatus("current")


class _IpcmdDHCPDuplicateDeviceCircuitID_Type(DisplayString):
    """Custom type ipcmdDHCPDuplicateDeviceCircuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPDuplicateDeviceCircuitID_Type.__name__ = "DisplayString"
_IpcmdDHCPDuplicateDeviceCircuitID_Object = MibScalar
ipcmdDHCPDuplicateDeviceCircuitID = _IpcmdDHCPDuplicateDeviceCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 23),
    _IpcmdDHCPDuplicateDeviceCircuitID_Type()
)
ipcmdDHCPDuplicateDeviceCircuitID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPDuplicateDeviceCircuitID.setStatus("current")
_IpcmdDHCPDuplicateDeviceGWAddress_Type = IpAddress
_IpcmdDHCPDuplicateDeviceGWAddress_Object = MibScalar
ipcmdDHCPDuplicateDeviceGWAddress = _IpcmdDHCPDuplicateDeviceGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 24),
    _IpcmdDHCPDuplicateDeviceGWAddress_Type()
)
ipcmdDHCPDuplicateDeviceGWAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPDuplicateDeviceGWAddress.setStatus("current")
_IpcmdTFTPServerAddress_Type = IpAddress
_IpcmdTFTPServerAddress_Object = MibScalar
ipcmdTFTPServerAddress = _IpcmdTFTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 25),
    _IpcmdTFTPServerAddress_Type()
)
ipcmdTFTPServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdTFTPServerAddress.setStatus("current")


class _IpcmdDHCPFailoverTerminatedReason_Type(DisplayString):
    """Custom type ipcmdDHCPFailoverTerminatedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdDHCPFailoverTerminatedReason_Type.__name__ = "DisplayString"
_IpcmdDHCPFailoverTerminatedReason_Object = MibScalar
ipcmdDHCPFailoverTerminatedReason = _IpcmdDHCPFailoverTerminatedReason_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 1, 26),
    _IpcmdDHCPFailoverTerminatedReason_Type()
)
ipcmdDHCPFailoverTerminatedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdDHCPFailoverTerminatedReason.setStatus("current")
_IpcmdNotifyObjects_ObjectIdentity = ObjectIdentity
ipcmdNotifyObjects = _IpcmdNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2)
)
if mibBuilder.loadTexts:
    ipcmdNotifyObjects.setStatus("current")
_IpcmdNotifyServer_Type = IpAddress
_IpcmdNotifyServer_Object = MibScalar
ipcmdNotifyServer = _IpcmdNotifyServer_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 1),
    _IpcmdNotifyServer_Type()
)
ipcmdNotifyServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdNotifyServer.setStatus("current")


class _IpcmdNotifyServerType_Type(Integer32):
    """Custom type ipcmdNotifyServerType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cfm", 8),
          ("cfmproxy", 9),
          ("dhcp", 2),
          ("dhcpRelay", 7),
          ("dns", 1),
          ("kdc", 6),
          ("ldap", 3),
          ("mps", 4),
          ("tftp", 5),
          ("unknown", 10))
    )


_IpcmdNotifyServerType_Type.__name__ = "Integer32"
_IpcmdNotifyServerType_Object = MibScalar
ipcmdNotifyServerType = _IpcmdNotifyServerType_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 2),
    _IpcmdNotifyServerType_Type()
)
ipcmdNotifyServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdNotifyServerType.setStatus("current")
_IpcmdUnknownIPAddress_Type = IpAddress
_IpcmdUnknownIPAddress_Object = MibScalar
ipcmdUnknownIPAddress = _IpcmdUnknownIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 3),
    _IpcmdUnknownIPAddress_Type()
)
ipcmdUnknownIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdUnknownIPAddress.setStatus("current")
_IpcmdServerDiskSpaceFreeTotal_Type = Unsigned32
_IpcmdServerDiskSpaceFreeTotal_Object = MibScalar
ipcmdServerDiskSpaceFreeTotal = _IpcmdServerDiskSpaceFreeTotal_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 4),
    _IpcmdServerDiskSpaceFreeTotal_Type()
)
ipcmdServerDiskSpaceFreeTotal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdServerDiskSpaceFreeTotal.setStatus("current")
_IpcmdServerDiskSpaceFreeCount_Type = Unsigned32
_IpcmdServerDiskSpaceFreeCount_Object = MibScalar
ipcmdServerDiskSpaceFreeCount = _IpcmdServerDiskSpaceFreeCount_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 5),
    _IpcmdServerDiskSpaceFreeCount_Type()
)
ipcmdServerDiskSpaceFreeCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdServerDiskSpaceFreeCount.setStatus("current")


class _IpcmdServerDiskSpaceFreeUnits_Type(Integer32):
    """Custom type ipcmdServerDiskSpaceFreeUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 2),
          ("value", 1))
    )


_IpcmdServerDiskSpaceFreeUnits_Type.__name__ = "Integer32"
_IpcmdServerDiskSpaceFreeUnits_Object = MibScalar
ipcmdServerDiskSpaceFreeUnits = _IpcmdServerDiskSpaceFreeUnits_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 6),
    _IpcmdServerDiskSpaceFreeUnits_Type()
)
ipcmdServerDiskSpaceFreeUnits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdServerDiskSpaceFreeUnits.setStatus("current")


class _IpcmdServiceStatus_Type(DisplayString):
    """Custom type ipcmdServiceStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdServiceStatus_Type.__name__ = "DisplayString"
_IpcmdServiceStatus_Object = MibScalar
ipcmdServiceStatus = _IpcmdServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 7),
    _IpcmdServiceStatus_Type()
)
ipcmdServiceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdServiceStatus.setStatus("current")


class _IpcmdNotifyHost_Type(DisplayString):
    """Custom type ipcmdNotifyHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdNotifyHost_Type.__name__ = "DisplayString"
_IpcmdNotifyHost_Object = MibScalar
ipcmdNotifyHost = _IpcmdNotifyHost_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 8),
    _IpcmdNotifyHost_Type()
)
ipcmdNotifyHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdNotifyHost.setStatus("current")


class _IpcmdNotifyDevice_Type(DisplayString):
    """Custom type ipcmdNotifyDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcmdNotifyDevice_Type.__name__ = "DisplayString"
_IpcmdNotifyDevice_Object = MibScalar
ipcmdNotifyDevice = _IpcmdNotifyDevice_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 99, 2, 9),
    _IpcmdNotifyDevice_Type()
)
ipcmdNotifyDevice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipcmdNotifyDevice.setStatus("current")
_IpcFailover_ObjectIdentity = ObjectIdentity
ipcFailover = _IpcFailover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100)
)
if mibBuilder.loadTexts:
    ipcFailover.setStatus("current")
_IpcFailoverStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverStatistics = _IpcFailoverStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1)
)
if mibBuilder.loadTexts:
    ipcFailoverStatistics.setStatus("current")
_IpcFailoverSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverSummaryStatistics = _IpcFailoverSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1)
)
if mibBuilder.loadTexts:
    ipcFailoverSummaryStatistics.setStatus("current")
_IpcFailoverTimerSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverTimerSummaryStatistics = _IpcFailoverTimerSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipcFailoverTimerSummaryStatistics.setStatus("current")
_IpcFailStatLastStartTime_Type = DateAndTime
_IpcFailStatLastStartTime_Object = MibScalar
ipcFailStatLastStartTime = _IpcFailStatLastStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 1, 1),
    _IpcFailStatLastStartTime_Type()
)
ipcFailStatLastStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLastStartTime.setStatus("current")
_IpcFailStatLastSyncTime_Type = DateAndTime
_IpcFailStatLastSyncTime_Object = MibScalar
ipcFailStatLastSyncTime = _IpcFailStatLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 1, 2),
    _IpcFailStatLastSyncTime_Type()
)
ipcFailStatLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLastSyncTime.setStatus("current")
_IpcFailStatLastTestTime_Type = DateAndTime
_IpcFailStatLastTestTime_Object = MibScalar
ipcFailStatLastTestTime = _IpcFailStatLastTestTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 1, 3),
    _IpcFailStatLastTestTime_Type()
)
ipcFailStatLastTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLastTestTime.setStatus("current")
_IpcFailStatLastDownTime_Type = DateAndTime
_IpcFailStatLastDownTime_Object = MibScalar
ipcFailStatLastDownTime = _IpcFailStatLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 1, 4),
    _IpcFailStatLastDownTime_Type()
)
ipcFailStatLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLastDownTime.setStatus("current")
_IpcFailStatLastUpTime_Type = DateAndTime
_IpcFailStatLastUpTime_Object = MibScalar
ipcFailStatLastUpTime = _IpcFailStatLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 1, 5),
    _IpcFailStatLastUpTime_Type()
)
ipcFailStatLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLastUpTime.setStatus("current")
_IpcFailoverErrorSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverErrorSummaryStatistics = _IpcFailoverErrorSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipcFailoverErrorSummaryStatistics.setStatus("current")
_IpcFailStatSendErrors_Type = Counter32
_IpcFailStatSendErrors_Object = MibScalar
ipcFailStatSendErrors = _IpcFailStatSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 1),
    _IpcFailStatSendErrors_Type()
)
ipcFailStatSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSendErrors.setStatus("current")
_IpcFailStatRecvErrors_Type = Counter32
_IpcFailStatRecvErrors_Object = MibScalar
ipcFailStatRecvErrors = _IpcFailStatRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 2),
    _IpcFailStatRecvErrors_Type()
)
ipcFailStatRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecvErrors.setStatus("current")
_IpcFailStatPlatformMismatchErrors_Type = Counter32
_IpcFailStatPlatformMismatchErrors_Object = MibScalar
ipcFailStatPlatformMismatchErrors = _IpcFailStatPlatformMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 3),
    _IpcFailStatPlatformMismatchErrors_Type()
)
ipcFailStatPlatformMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatPlatformMismatchErrors.setStatus("current")
_IpcFailStatVersionMismatchErrors_Type = Counter32
_IpcFailStatVersionMismatchErrors_Object = MibScalar
ipcFailStatVersionMismatchErrors = _IpcFailStatVersionMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 4),
    _IpcFailStatVersionMismatchErrors_Type()
)
ipcFailStatVersionMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatVersionMismatchErrors.setStatus("current")
_IpcFailStatRoleMismatchErrors_Type = Counter32
_IpcFailStatRoleMismatchErrors_Object = MibScalar
ipcFailStatRoleMismatchErrors = _IpcFailStatRoleMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 5),
    _IpcFailStatRoleMismatchErrors_Type()
)
ipcFailStatRoleMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRoleMismatchErrors.setStatus("current")
_IpcFailStatCRC1Errors_Type = Counter32
_IpcFailStatCRC1Errors_Object = MibScalar
ipcFailStatCRC1Errors = _IpcFailStatCRC1Errors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 6),
    _IpcFailStatCRC1Errors_Type()
)
ipcFailStatCRC1Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatCRC1Errors.setStatus("current")
_IpcFailStatCRC2Errors_Type = Counter32
_IpcFailStatCRC2Errors_Object = MibScalar
ipcFailStatCRC2Errors = _IpcFailStatCRC2Errors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 7),
    _IpcFailStatCRC2Errors_Type()
)
ipcFailStatCRC2Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatCRC2Errors.setStatus("current")
_IpcFailStatDecryptErrors_Type = Counter32
_IpcFailStatDecryptErrors_Object = MibScalar
ipcFailStatDecryptErrors = _IpcFailStatDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 8),
    _IpcFailStatDecryptErrors_Type()
)
ipcFailStatDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatDecryptErrors.setStatus("current")
_IpcFailStatAccessDeniedErrors_Type = Counter32
_IpcFailStatAccessDeniedErrors_Object = MibScalar
ipcFailStatAccessDeniedErrors = _IpcFailStatAccessDeniedErrors_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 2, 9),
    _IpcFailStatAccessDeniedErrors_Type()
)
ipcFailStatAccessDeniedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatAccessDeniedErrors.setStatus("current")
_IpcFailoverTimeDownSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverTimeDownSummaryStatistics = _IpcFailoverTimeDownSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipcFailoverTimeDownSummaryStatistics.setStatus("current")
_IpcFailStatTotalTimeDown_Type = Counter32
_IpcFailStatTotalTimeDown_Object = MibScalar
ipcFailStatTotalTimeDown = _IpcFailStatTotalTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 3, 1),
    _IpcFailStatTotalTimeDown_Type()
)
ipcFailStatTotalTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatTotalTimeDown.setStatus("current")
_IpcFailStatLongestTimeDown_Type = Counter32
_IpcFailStatLongestTimeDown_Object = MibScalar
ipcFailStatLongestTimeDown = _IpcFailStatLongestTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 3, 2),
    _IpcFailStatLongestTimeDown_Type()
)
ipcFailStatLongestTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLongestTimeDown.setStatus("current")
_IpcFailStatCountTimeDown_Type = Counter32
_IpcFailStatCountTimeDown_Object = MibScalar
ipcFailStatCountTimeDown = _IpcFailStatCountTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 3, 3),
    _IpcFailStatCountTimeDown_Type()
)
ipcFailStatCountTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatCountTimeDown.setStatus("current")
_IpcFailoverResynchSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverResynchSummaryStatistics = _IpcFailoverResynchSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipcFailoverResynchSummaryStatistics.setStatus("current")
_IpcFailStatTotalResynch_Type = Counter32
_IpcFailStatTotalResynch_Object = MibScalar
ipcFailStatTotalResynch = _IpcFailStatTotalResynch_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 4, 1),
    _IpcFailStatTotalResynch_Type()
)
ipcFailStatTotalResynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatTotalResynch.setStatus("current")
_IpcFailStatLongestResynch_Type = Counter32
_IpcFailStatLongestResynch_Object = MibScalar
ipcFailStatLongestResynch = _IpcFailStatLongestResynch_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 4, 2),
    _IpcFailStatLongestResynch_Type()
)
ipcFailStatLongestResynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLongestResynch.setStatus("current")
_IpcFailStatCountResynch_Type = Counter32
_IpcFailStatCountResynch_Object = MibScalar
ipcFailStatCountResynch = _IpcFailStatCountResynch_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 4, 3),
    _IpcFailStatCountResynch_Type()
)
ipcFailStatCountResynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatCountResynch.setStatus("current")
_IpcFailoverTimeupSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverTimeupSummaryStatistics = _IpcFailoverTimeupSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipcFailoverTimeupSummaryStatistics.setStatus("current")
_IpcFailStatTotalTimeUp_Type = Counter32
_IpcFailStatTotalTimeUp_Object = MibScalar
ipcFailStatTotalTimeUp = _IpcFailStatTotalTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 5, 1),
    _IpcFailStatTotalTimeUp_Type()
)
ipcFailStatTotalTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatTotalTimeUp.setStatus("current")
_IpcFailStatLongestTimeUp_Type = Counter32
_IpcFailStatLongestTimeUp_Object = MibScalar
ipcFailStatLongestTimeUp = _IpcFailStatLongestTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 5, 2),
    _IpcFailStatLongestTimeUp_Type()
)
ipcFailStatLongestTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatLongestTimeUp.setStatus("current")
_IpcFailStatCountTimeUp_Type = Counter32
_IpcFailStatCountTimeUp_Object = MibScalar
ipcFailStatCountTimeUp = _IpcFailStatCountTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 5, 3),
    _IpcFailStatCountTimeUp_Type()
)
ipcFailStatCountTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatCountTimeUp.setStatus("current")
_IpcFailoverRecdSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverRecdSummaryStatistics = _IpcFailoverRecdSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipcFailoverRecdSummaryStatistics.setStatus("current")
_IpcFailStatRecdHeartbeats_Type = Counter32
_IpcFailStatRecdHeartbeats_Object = MibScalar
ipcFailStatRecdHeartbeats = _IpcFailStatRecdHeartbeats_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 1),
    _IpcFailStatRecdHeartbeats_Type()
)
ipcFailStatRecdHeartbeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdHeartbeats.setStatus("current")
_IpcFailStatRecdTestRequests_Type = Counter32
_IpcFailStatRecdTestRequests_Object = MibScalar
ipcFailStatRecdTestRequests = _IpcFailStatRecdTestRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 2),
    _IpcFailStatRecdTestRequests_Type()
)
ipcFailStatRecdTestRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdTestRequests.setStatus("current")
_IpcFailStatRecdTestReplies_Type = Counter32
_IpcFailStatRecdTestReplies_Object = MibScalar
ipcFailStatRecdTestReplies = _IpcFailStatRecdTestReplies_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 3),
    _IpcFailStatRecdTestReplies_Type()
)
ipcFailStatRecdTestReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdTestReplies.setStatus("current")
_IpcFailStatRecdDataTxRequests_Type = Counter32
_IpcFailStatRecdDataTxRequests_Object = MibScalar
ipcFailStatRecdDataTxRequests = _IpcFailStatRecdDataTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 4),
    _IpcFailStatRecdDataTxRequests_Type()
)
ipcFailStatRecdDataTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataTxRequests.setStatus("current")
_IpcFailStatRecdDataTxData_Type = Counter32
_IpcFailStatRecdDataTxData_Object = MibScalar
ipcFailStatRecdDataTxData = _IpcFailStatRecdDataTxData_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 5),
    _IpcFailStatRecdDataTxData_Type()
)
ipcFailStatRecdDataTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataTxData.setStatus("current")
_IpcFailStatRecdDataTxAcks_Type = Counter32
_IpcFailStatRecdDataTxAcks_Object = MibScalar
ipcFailStatRecdDataTxAcks = _IpcFailStatRecdDataTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 6),
    _IpcFailStatRecdDataTxAcks_Type()
)
ipcFailStatRecdDataTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataTxAcks.setStatus("current")
_IpcFailStatRecdDataTransactionData_Type = Counter32
_IpcFailStatRecdDataTransactionData_Object = MibScalar
ipcFailStatRecdDataTransactionData = _IpcFailStatRecdDataTransactionData_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 7),
    _IpcFailStatRecdDataTransactionData_Type()
)
ipcFailStatRecdDataTransactionData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataTransactionData.setStatus("current")
_IpcFailStatRecdDataTransactionAcks_Type = Counter32
_IpcFailStatRecdDataTransactionAcks_Object = MibScalar
ipcFailStatRecdDataTransactionAcks = _IpcFailStatRecdDataTransactionAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 8),
    _IpcFailStatRecdDataTransactionAcks_Type()
)
ipcFailStatRecdDataTransactionAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataTransactionAcks.setStatus("current")
_IpcFailStatRecdDataConflicts_Type = Counter32
_IpcFailStatRecdDataConflicts_Object = MibScalar
ipcFailStatRecdDataConflicts = _IpcFailStatRecdDataConflicts_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 9),
    _IpcFailStatRecdDataConflicts_Type()
)
ipcFailStatRecdDataConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataConflicts.setStatus("current")
_IpcFailStatRecdDataConflictAcks_Type = Counter32
_IpcFailStatRecdDataConflictAcks_Object = MibScalar
ipcFailStatRecdDataConflictAcks = _IpcFailStatRecdDataConflictAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 10),
    _IpcFailStatRecdDataConflictAcks_Type()
)
ipcFailStatRecdDataConflictAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataConflictAcks.setStatus("current")
_IpcFailStatRecdDataResynchRequests_Type = Counter32
_IpcFailStatRecdDataResynchRequests_Object = MibScalar
ipcFailStatRecdDataResynchRequests = _IpcFailStatRecdDataResynchRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 11),
    _IpcFailStatRecdDataResynchRequests_Type()
)
ipcFailStatRecdDataResynchRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataResynchRequests.setStatus("current")
_IpcFailStatRecdDataResynchAcks_Type = Counter32
_IpcFailStatRecdDataResynchAcks_Object = MibScalar
ipcFailStatRecdDataResynchAcks = _IpcFailStatRecdDataResynchAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 12),
    _IpcFailStatRecdDataResynchAcks_Type()
)
ipcFailStatRecdDataResynchAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdDataResynchAcks.setStatus("current")
_IpcFailStatRecdShuttingDown_Type = Counter32
_IpcFailStatRecdShuttingDown_Object = MibScalar
ipcFailStatRecdShuttingDown = _IpcFailStatRecdShuttingDown_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 6, 13),
    _IpcFailStatRecdShuttingDown_Type()
)
ipcFailStatRecdShuttingDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatRecdShuttingDown.setStatus("current")
_IpcFailoverSentSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverSentSummaryStatistics = _IpcFailoverSentSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ipcFailoverSentSummaryStatistics.setStatus("current")
_IpcFailStatSentHeartbeats_Type = Counter32
_IpcFailStatSentHeartbeats_Object = MibScalar
ipcFailStatSentHeartbeats = _IpcFailStatSentHeartbeats_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 1),
    _IpcFailStatSentHeartbeats_Type()
)
ipcFailStatSentHeartbeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentHeartbeats.setStatus("current")
_IpcFailStatSentTestRequests_Type = Counter32
_IpcFailStatSentTestRequests_Object = MibScalar
ipcFailStatSentTestRequests = _IpcFailStatSentTestRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 2),
    _IpcFailStatSentTestRequests_Type()
)
ipcFailStatSentTestRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentTestRequests.setStatus("current")
_IpcFailStatSentTestReplies_Type = Counter32
_IpcFailStatSentTestReplies_Object = MibScalar
ipcFailStatSentTestReplies = _IpcFailStatSentTestReplies_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 3),
    _IpcFailStatSentTestReplies_Type()
)
ipcFailStatSentTestReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentTestReplies.setStatus("current")
_IpcFailStatSentDataTxRequests_Type = Counter32
_IpcFailStatSentDataTxRequests_Object = MibScalar
ipcFailStatSentDataTxRequests = _IpcFailStatSentDataTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 4),
    _IpcFailStatSentDataTxRequests_Type()
)
ipcFailStatSentDataTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataTxRequests.setStatus("current")
_IpcFailStatSentDataTxData_Type = Counter32
_IpcFailStatSentDataTxData_Object = MibScalar
ipcFailStatSentDataTxData = _IpcFailStatSentDataTxData_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 5),
    _IpcFailStatSentDataTxData_Type()
)
ipcFailStatSentDataTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataTxData.setStatus("current")
_IpcFailStatSentDataTxAcks_Type = Counter32
_IpcFailStatSentDataTxAcks_Object = MibScalar
ipcFailStatSentDataTxAcks = _IpcFailStatSentDataTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 6),
    _IpcFailStatSentDataTxAcks_Type()
)
ipcFailStatSentDataTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataTxAcks.setStatus("current")
_IpcFailStatSentDataTransactionData_Type = Counter32
_IpcFailStatSentDataTransactionData_Object = MibScalar
ipcFailStatSentDataTransactionData = _IpcFailStatSentDataTransactionData_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 7),
    _IpcFailStatSentDataTransactionData_Type()
)
ipcFailStatSentDataTransactionData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataTransactionData.setStatus("current")
_IpcFailStatSentDataTransactionAcks_Type = Counter32
_IpcFailStatSentDataTransactionAcks_Object = MibScalar
ipcFailStatSentDataTransactionAcks = _IpcFailStatSentDataTransactionAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 8),
    _IpcFailStatSentDataTransactionAcks_Type()
)
ipcFailStatSentDataTransactionAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataTransactionAcks.setStatus("current")
_IpcFailStatSentDataConflicts_Type = Counter32
_IpcFailStatSentDataConflicts_Object = MibScalar
ipcFailStatSentDataConflicts = _IpcFailStatSentDataConflicts_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 9),
    _IpcFailStatSentDataConflicts_Type()
)
ipcFailStatSentDataConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataConflicts.setStatus("current")
_IpcFailStatSentDataConflictAcks_Type = Counter32
_IpcFailStatSentDataConflictAcks_Object = MibScalar
ipcFailStatSentDataConflictAcks = _IpcFailStatSentDataConflictAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 10),
    _IpcFailStatSentDataConflictAcks_Type()
)
ipcFailStatSentDataConflictAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataConflictAcks.setStatus("current")
_IpcFailStatSentDataResynchRequests_Type = Counter32
_IpcFailStatSentDataResynchRequests_Object = MibScalar
ipcFailStatSentDataResynchRequests = _IpcFailStatSentDataResynchRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 11),
    _IpcFailStatSentDataResynchRequests_Type()
)
ipcFailStatSentDataResynchRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataResynchRequests.setStatus("current")
_IpcFailStatSentDataResynchAcks_Type = Counter32
_IpcFailStatSentDataResynchAcks_Object = MibScalar
ipcFailStatSentDataResynchAcks = _IpcFailStatSentDataResynchAcks_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 12),
    _IpcFailStatSentDataResynchAcks_Type()
)
ipcFailStatSentDataResynchAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentDataResynchAcks.setStatus("current")
_IpcFailStatSentShuttingDown_Type = Counter32
_IpcFailStatSentShuttingDown_Object = MibScalar
ipcFailStatSentShuttingDown = _IpcFailStatSentShuttingDown_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 7, 13),
    _IpcFailStatSentShuttingDown_Type()
)
ipcFailStatSentShuttingDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatSentShuttingDown.setStatus("current")
_IpcFailoverTrafficSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverTrafficSummaryStatistics = _IpcFailoverTrafficSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ipcFailoverTrafficSummaryStatistics.setStatus("current")
_IpcFailStatBytesSent_Type = Counter32
_IpcFailStatBytesSent_Object = MibScalar
ipcFailStatBytesSent = _IpcFailStatBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 8, 1),
    _IpcFailStatBytesSent_Type()
)
ipcFailStatBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatBytesSent.setStatus("current")
_IpcFailStatBytesRecd_Type = Counter32
_IpcFailStatBytesRecd_Object = MibScalar
ipcFailStatBytesRecd = _IpcFailStatBytesRecd_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 8, 2),
    _IpcFailStatBytesRecd_Type()
)
ipcFailStatBytesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatBytesRecd.setStatus("current")
_IpcFailStatTxSent_Type = Counter32
_IpcFailStatTxSent_Object = MibScalar
ipcFailStatTxSent = _IpcFailStatTxSent_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 8, 3),
    _IpcFailStatTxSent_Type()
)
ipcFailStatTxSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatTxSent.setStatus("current")
_IpcFailStatTxRecd_Type = Counter32
_IpcFailStatTxRecd_Object = MibScalar
ipcFailStatTxRecd = _IpcFailStatTxRecd_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 8, 4),
    _IpcFailStatTxRecd_Type()
)
ipcFailStatTxRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatTxRecd.setStatus("current")
_IpcFailoverStatusSummaryStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverStatusSummaryStatistics = _IpcFailoverStatusSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ipcFailoverStatusSummaryStatistics.setStatus("current")


class _IpcFailStatStatus_Type(DisplayString):
    """Custom type ipcFailStatStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcFailStatStatus_Type.__name__ = "DisplayString"
_IpcFailStatStatus_Object = MibScalar
ipcFailStatStatus = _IpcFailStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 9, 1),
    _IpcFailStatStatus_Type()
)
ipcFailStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatStatus.setStatus("current")


class _IpcFailStatOperation_Type(DisplayString):
    """Custom type ipcFailStatOperation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcFailStatOperation_Type.__name__ = "DisplayString"
_IpcFailStatOperation_Object = MibScalar
ipcFailStatOperation = _IpcFailStatOperation_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 1, 9, 2),
    _IpcFailStatOperation_Type()
)
ipcFailStatOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcFailStatOperation.setStatus("current")
_IpcFailoverProtocolStatistics_ObjectIdentity = ObjectIdentity
ipcFailoverProtocolStatistics = _IpcFailoverProtocolStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 100, 1, 2)
)
if mibBuilder.loadTexts:
    ipcFailoverProtocolStatistics.setStatus("current")
_IpcServiceStatistics_ObjectIdentity = ObjectIdentity
ipcServiceStatistics = _IpcServiceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 101)
)
if mibBuilder.loadTexts:
    ipcServiceStatistics.setStatus("current")
_IpcServiceLeasesInUse_Type = Counter32
_IpcServiceLeasesInUse_Object = MibScalar
ipcServiceLeasesInUse = _IpcServiceLeasesInUse_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 101, 1),
    _IpcServiceLeasesInUse_Type()
)
ipcServiceLeasesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceLeasesInUse.setStatus("current")
_IpcServiceInformation_ObjectIdentity = ObjectIdentity
ipcServiceInformation = _IpcServiceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102)
)
if mibBuilder.loadTexts:
    ipcServiceInformation.setStatus("current")


class _IpcServiceServerName_Type(DisplayString):
    """Custom type ipcServiceServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcServiceServerName_Type.__name__ = "DisplayString"
_IpcServiceServerName_Object = MibScalar
ipcServiceServerName = _IpcServiceServerName_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 1),
    _IpcServiceServerName_Type()
)
ipcServiceServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceServerName.setStatus("current")


class _IpcServiceName_Type(DisplayString):
    """Custom type ipcServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcServiceName_Type.__name__ = "DisplayString"
_IpcServiceName_Object = MibScalar
ipcServiceName = _IpcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 2),
    _IpcServiceName_Type()
)
ipcServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceName.setStatus("current")


class _IpcServiceVersion_Type(DisplayString):
    """Custom type ipcServiceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcServiceVersion_Type.__name__ = "DisplayString"
_IpcServiceVersion_Object = MibScalar
ipcServiceVersion = _IpcServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 3),
    _IpcServiceVersion_Type()
)
ipcServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceVersion.setStatus("current")
_IpcServiceLicenseUsers_Type = Unsigned32
_IpcServiceLicenseUsers_Object = MibScalar
ipcServiceLicenseUsers = _IpcServiceLicenseUsers_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 4),
    _IpcServiceLicenseUsers_Type()
)
ipcServiceLicenseUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceLicenseUsers.setStatus("current")
_IpcServiceSubscriptionExpiration_Type = DateAndTime
_IpcServiceSubscriptionExpiration_Object = MibScalar
ipcServiceSubscriptionExpiration = _IpcServiceSubscriptionExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 5),
    _IpcServiceSubscriptionExpiration_Type()
)
ipcServiceSubscriptionExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceSubscriptionExpiration.setStatus("current")
_IpcServiceLicenseType_Type = Unsigned32
_IpcServiceLicenseType_Object = MibScalar
ipcServiceLicenseType = _IpcServiceLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 6),
    _IpcServiceLicenseType_Type()
)
ipcServiceLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceLicenseType.setStatus("current")


class _IpcServiceOperatingSystem_Type(DisplayString):
    """Custom type ipcServiceOperatingSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpcServiceOperatingSystem_Type.__name__ = "DisplayString"
_IpcServiceOperatingSystem_Object = MibScalar
ipcServiceOperatingSystem = _IpcServiceOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 7),
    _IpcServiceOperatingSystem_Type()
)
ipcServiceOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceOperatingSystem.setStatus("current")
_IpcServiceStartTime_Type = DateAndTime
_IpcServiceStartTime_Object = MibScalar
ipcServiceStartTime = _IpcServiceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 102, 8),
    _IpcServiceStartTime_Type()
)
ipcServiceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcServiceStartTime.setStatus("current")
_IpcNotificationPrefix_ObjectIdentity = ObjectIdentity
ipcNotificationPrefix = _IpcNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ipcNotificationPrefix.setStatus("current")
_IpcNotifications_ObjectIdentity = ObjectIdentity
ipcNotifications = _IpcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 3, 0)
)
if mibBuilder.loadTexts:
    ipcNotifications.setStatus("current")
_IpcConformance_ObjectIdentity = ObjectIdentity
ipcConformance = _IpcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4)
)
if mibBuilder.loadTexts:
    ipcConformance.setStatus("current")
_IpcCompliances_ObjectIdentity = ObjectIdentity
ipcCompliances = _IpcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipcCompliances.setStatus("current")
_IpcGroups_ObjectIdentity = ObjectIdentity
ipcGroups = _IpcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ipcGroups.setStatus("current")
_IpcDeprecatedGroups_ObjectIdentity = ObjectIdentity
ipcDeprecatedGroups = _IpcDeprecatedGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 99)
)
if mibBuilder.loadTexts:
    ipcDeprecatedGroups.setStatus("current")
_IpcTimeOfDayServer_ObjectIdentity = ObjectIdentity
ipcTimeOfDayServer = _IpcTimeOfDayServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5)
)
if mibBuilder.loadTexts:
    ipcTimeOfDayServer.setStatus("current")
_TodServerObjects_ObjectIdentity = ObjectIdentity
todServerObjects = _TodServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    todServerObjects.setStatus("current")
_TodCounters_ObjectIdentity = ObjectIdentity
todCounters = _TodCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    todCounters.setStatus("current")
_TodCountTcpRequests_Type = Counter32
_TodCountTcpRequests_Object = MibScalar
todCountTcpRequests = _TodCountTcpRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 1, 1, 1),
    _TodCountTcpRequests_Type()
)
todCountTcpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todCountTcpRequests.setStatus("current")
_TodCountUdpRequests_Type = Counter32
_TodCountUdpRequests_Object = MibScalar
todCountUdpRequests = _TodCountUdpRequests_Object(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 1, 1, 2),
    _TodCountUdpRequests_Type()
)
todCountUdpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todCountUdpRequests.setStatus("current")
_TodClientObjects_ObjectIdentity = ObjectIdentity
todClientObjects = _TodClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    todClientObjects.setStatus("current")
_TodServerNotificationPrefix_ObjectIdentity = ObjectIdentity
todServerNotificationPrefix = _TodServerNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 2)
)
_TodServerConformance_ObjectIdentity = ObjectIdentity
todServerConformance = _TodServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 3)
)
if mibBuilder.loadTexts:
    todServerConformance.setStatus("current")
_TodServerCompliances_ObjectIdentity = ObjectIdentity
todServerCompliances = _TodServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 3, 1)
)
_TodServerGroups_ObjectIdentity = ObjectIdentity
todServerGroups = _TodServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 3, 2)
)
_IpcDeprecatedNotificationPrefix_ObjectIdentity = ObjectIdentity
ipcDeprecatedNotificationPrefix = _IpcDeprecatedNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99)
)
if mibBuilder.loadTexts:
    ipcDeprecatedNotificationPrefix.setStatus("current")
_IncognitoNotifyNotifications_ObjectIdentity = ObjectIdentity
incognitoNotifyNotifications = _IncognitoNotifyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0)
)
if mibBuilder.loadTexts:
    incognitoNotifyNotifications.setStatus("current")

# Managed Objects groups

ipcServiceStatisticsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 1, 2, 1)
)
ipcServiceStatisticsObjects.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceLeasesInUse")
)
if mibBuilder.loadTexts:
    ipcServiceStatisticsObjects.setStatus("current")

ipcServiceInformationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 1, 3, 1)
)
ipcServiceInformationObjects.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceServerName"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceName"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceVersion"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceLicenseUsers"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceSubscriptionExpiration"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceLicenseType"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceOperatingSystem"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcServiceStartTime"))
)
if mibBuilder.loadTexts:
    ipcServiceInformationObjects.setStatus("current")

ipcNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 2, 1)
)
ipcNotifyObjectsGroup.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcResumedTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcPausedTime"))
)
if mibBuilder.loadTexts:
    ipcNotifyObjectsGroup.setStatus("current")

ipcFailoverSummaryStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 2, 3)
)
ipcFailoverSummaryStatisticsGroup.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLastStartTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLastSyncTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLastTestTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLastDownTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLastUpTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSendErrors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecvErrors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatPlatformMismatchErrors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatVersionMismatchErrors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRoleMismatchErrors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatCRC1Errors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatCRC2Errors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatDecryptErrors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatAccessDeniedErrors"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatTotalTimeDown"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLongestTimeDown"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatCountTimeDown"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatTotalResynch"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLongestResynch"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatCountResynch"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatTotalTimeUp"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatLongestTimeUp"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatCountTimeUp"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdHeartbeats"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdTestRequests"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdTestReplies"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataTxRequests"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataTxData"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataTxAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataTransactionData"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataTransactionAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataConflicts"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataConflictAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataResynchRequests"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdDataResynchAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatRecdShuttingDown"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentHeartbeats"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentTestRequests"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentTestReplies"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataTxRequests"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataTxData"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataTxAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataTransactionData"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataTransactionAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataConflicts"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataConflictAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataResynchRequests"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentDataResynchAcks"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatSentShuttingDown"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatBytesSent"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatBytesRecd"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatTxSent"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatTxRecd"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatStatus"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcFailStatOperation"))
)
if mibBuilder.loadTexts:
    ipcFailoverSummaryStatisticsGroup.setStatus("current")

ipcDHCPPacketStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 2, 4)
)
ipcDHCPPacketStatisticsGroup.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPDiscoverPacketDiscards"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPRequestPacketDiscards"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPInformPacketDiscards"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPDeclinePacketDiscards"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPOtherPacketDiscards"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPDiscoverPacketSupercedes"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPRequestPacketSupercedes"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPInformPacketSupercedes"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPDeclinePacketSupercedes"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPOtherPacketSupercedes"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPBOOTPPacketResponseAvg1minTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPBOOTPPacketResponseAvg5minTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPBOOTPPacketResponseAvg15minTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPDHCPv4PacketResponseAvg1minTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPDHCPv4PacketResponseAvg5minTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcDHCPDHCPv4PacketResponseAvg15minTime"))
)
if mibBuilder.loadTexts:
    ipcDHCPPacketStatisticsGroup.setStatus("current")

ipcDeprecatedNotifyBaseObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 99, 2)
)
ipcDeprecatedNotifyBaseObjectsGroup.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressLowThreshold"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressHighThreshold"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressCriticalThreshold"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressValue"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressUnits"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleName"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerNumRequest"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerRequestTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerInfo"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPCurrentUserCount"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPLicenseCount"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPExceedingLicenseLimit"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverConflictAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPNetViewName"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPCurrentHWM"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverResynchStartTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverResynchEndTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceHWAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceIPAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceRemoteID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceCircuitID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceGWAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdTFTPServerAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverTerminatedReason"))
)
if mibBuilder.loadTexts:
    ipcDeprecatedNotifyBaseObjectsGroup.setStatus("current")

ipcDeprecatedNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 99, 3)
)
ipcDeprecatedNotifyObjectsGroup.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdUnknownIPAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServerDiskSpaceFreeTotal"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServerDiskSpaceFreeCount"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServerDiskSpaceFreeUnits"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServiceStatus"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyHost"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyDevice"))
)
if mibBuilder.loadTexts:
    ipcDeprecatedNotifyObjectsGroup.setStatus("current")

todServerCounterObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 3, 2, 1)
)
todServerCounterObjects.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "todCountTcpRequests"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "todCountUdpRequests"))
)
if mibBuilder.loadTexts:
    todServerCounterObjects.setStatus("current")


# Notification objects

ipcNotifyServerPaused = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 3, 0, 1)
)
ipcNotifyServerPaused.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcPausedTime")
)
if mibBuilder.loadTexts:
    ipcNotifyServerPaused.setStatus(
        "current"
    )

ipcNotifyServerResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 3, 0, 2)
)
ipcNotifyServerResumed.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcResumedTime")
)
if mibBuilder.loadTexts:
    ipcNotifyServerResumed.setStatus(
        "current"
    )

incognitoIPCMDServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 1)
)
incognitoIPCMDServerStart.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType")
)
if mibBuilder.loadTexts:
    incognitoIPCMDServerStart.setStatus(
        "current"
    )

incognitoIPCMDServerStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 2)
)
incognitoIPCMDServerStop.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType")
)
if mibBuilder.loadTexts:
    incognitoIPCMDServerStop.setStatus(
        "current"
    )

incognitoIPCMDServicePaused = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 3)
)
incognitoIPCMDServicePaused.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServiceStatus")
)
if mibBuilder.loadTexts:
    incognitoIPCMDServicePaused.setStatus(
        "current"
    )

incognitoIPCMDServiceResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 4)
)
incognitoIPCMDServiceResume.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServiceStatus")
)
if mibBuilder.loadTexts:
    incognitoIPCMDServiceResume.setStatus(
        "current"
    )

incognitoIPCMDExceededLicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 5)
)
incognitoIPCMDExceededLicense.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPCurrentUserCount"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPLicenseCount"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPExceedingLicenseLimit"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDExceededLicense.setStatus(
        "current"
    )

incognitoIPCMDFreeAddressHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 6)
)
incognitoIPCMDFreeAddressHigh.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressHighThreshold"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressValue"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressUnits"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleName"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDFreeAddressHigh.setStatus(
        "current"
    )

incognitoIPCMDCriticalAddressLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 7)
)
incognitoIPCMDCriticalAddressLevel.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressCriticalThreshold"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressValue"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressUnits"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleName"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDCriticalAddressLevel.setStatus(
        "current"
    )

incognitoIPCMDOtherServerResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 8)
)
incognitoIPCMDOtherServerResponding.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDOtherServerResponding.setStatus(
        "current"
    )

incognitoIPCMDOtherServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 9)
)
incognitoIPCMDOtherServerNotResponding.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDOtherServerNotResponding.setStatus(
        "current"
    )

incognitoIPCMDFailoverConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 10)
)
incognitoIPCMDFailoverConflict.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverConflictAddress")
)
if mibBuilder.loadTexts:
    incognitoIPCMDFailoverConflict.setStatus(
        "current"
    )

incognitoIPCMDServiceOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 11)
)
incognitoIPCMDServiceOverloaded.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServiceStatus")
)
if mibBuilder.loadTexts:
    incognitoIPCMDServiceOverloaded.setStatus(
        "current"
    )

incognitoIPCMDServiceCaughtUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 12)
)
incognitoIPCMDServiceCaughtUp.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServiceStatus")
)
if mibBuilder.loadTexts:
    incognitoIPCMDServiceCaughtUp.setStatus(
        "current"
    )

incognitoIPCMDDDNSFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 13)
)
incognitoIPCMDDDNSFailure.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDDDNSFailure.setStatus(
        "current"
    )

incognitoIPCMDUnknownDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 14)
)
incognitoIPCMDUnknownDevice.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdUnknownIPAddress")
)
if mibBuilder.loadTexts:
    incognitoIPCMDUnknownDevice.setStatus(
        "current"
    )

incognitoIPCMDRogueServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 15)
)
incognitoIPCMDRogueServer.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerNumRequest"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerRequestTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRogueServerInfo"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDRogueServer.setStatus(
        "current"
    )

incognitoIPCMDDiskStorageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 16)
)
incognitoIPCMDDiskStorageLow.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServerDiskSpaceFreeTotal"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServerDiskSpaceFreeCount"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServerDiskSpaceFreeUnits"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDDiskStorageLow.setStatus(
        "current"
    )

incognitoIPCMDServiceBackupDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 17)
)
incognitoIPCMDServiceBackupDone.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdServiceStatus")
)
if mibBuilder.loadTexts:
    incognitoIPCMDServiceBackupDone.setStatus(
        "current"
    )

incognitoIPCMDFreeAddressLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 18)
)
incognitoIPCMDFreeAddressLow.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressLowThreshold"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressValue"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFreeAddressUnits"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPRuleName"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDFreeAddressLow.setStatus(
        "current"
    )

incognitoIPCMDFailoverResynchOperationStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 19)
)
incognitoIPCMDFailoverResynchOperationStarted.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverResynchStartTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDFailoverResynchOperationStarted.setStatus(
        "current"
    )

incognitoIPCMDFailoverResynchOperationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 20)
)
incognitoIPCMDFailoverResynchOperationCompleted.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverResynchEndTime"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDFailoverResynchOperationCompleted.setStatus(
        "current"
    )

incognitoIPCMDNetViewCriticalHWMExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 21)
)
incognitoIPCMDNetViewCriticalHWMExceeded.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPNetViewName"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPCurrentHWM"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDNetViewCriticalHWMExceeded.setStatus(
        "current"
    )

incognitoIPCMDNetViewWarningHWMExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 22)
)
incognitoIPCMDNetViewWarningHWMExceeded.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPNetViewName"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPCurrentHWM"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDNetViewWarningHWMExceeded.setStatus(
        "current"
    )

incognitoIPCMDPossibleDuplicateDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 23)
)
incognitoIPCMDPossibleDuplicateDevice.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceHWAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceIPAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceRemoteID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceCircuitID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceGWAddress"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDPossibleDuplicateDevice.setStatus(
        "current"
    )

incognitoIPCMDNoMoreAddressesAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 24)
)
incognitoIPCMDNoMoreAddressesAvailable.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceHWAddress"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceRemoteID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceCircuitID"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPDuplicateDeviceGWAddress"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDNoMoreAddressesAvailable.setStatus(
        "current"
    )

incognitoIPCMDTFTPServerJoining = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 25)
)
incognitoIPCMDTFTPServerJoining.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdTFTPServerAddress")
)
if mibBuilder.loadTexts:
    incognitoIPCMDTFTPServerJoining.setStatus(
        "current"
    )

incognitoIPCMDTFTPServerLeaving = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 26)
)
incognitoIPCMDTFTPServerLeaving.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdTFTPServerAddress")
)
if mibBuilder.loadTexts:
    incognitoIPCMDTFTPServerLeaving.setStatus(
        "current"
    )

incognitoIPCMDServerJoinClusterIntegration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 27)
)
incognitoIPCMDServerJoinClusterIntegration.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDServerJoinClusterIntegration.setStatus(
        "current"
    )

incognitoIPCMDServerLeaveClusterIntegration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 28)
)
incognitoIPCMDServerLeaveClusterIntegration.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServerType"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDServerLeaveClusterIntegration.setStatus(
        "current"
    )

incognitoIPCMDFailoverTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 29)
)
incognitoIPCMDFailoverTerminated.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPFailoverTerminatedReason"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyServer"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDFailoverTerminated.setStatus(
        "current"
    )

incognitoIPCMDLDAPCommunicationsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 30)
)
incognitoIPCMDLDAPCommunicationsUp.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyHost")
)
if mibBuilder.loadTexts:
    incognitoIPCMDLDAPCommunicationsUp.setStatus(
        "current"
    )

incognitoIPCMDLDAPCommunicationsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 31)
)
incognitoIPCMDLDAPCommunicationsDown.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyHost")
)
if mibBuilder.loadTexts:
    incognitoIPCMDLDAPCommunicationsDown.setStatus(
        "current"
    )

incognitoIPCMDLDAPTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 32)
)
incognitoIPCMDLDAPTimedOut.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyHost")
)
if mibBuilder.loadTexts:
    incognitoIPCMDLDAPTimedOut.setStatus(
        "current"
    )

incognitoIPCMDRADIUSAccountingHWMExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 33)
)
incognitoIPCMDRADIUSAccountingHWMExceeded.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyHost"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdDHCPCurrentHWM"))
)
if mibBuilder.loadTexts:
    incognitoIPCMDRADIUSAccountingHWMExceeded.setStatus(
        "current"
    )

incognitoIPCMDLDAPSetCommunicationsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 34)
)
incognitoIPCMDLDAPSetCommunicationsUp.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyHost")
)
if mibBuilder.loadTexts:
    incognitoIPCMDLDAPSetCommunicationsUp.setStatus(
        "current"
    )

incognitoIPCMDLDAPSetCommunicationsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 35)
)
incognitoIPCMDLDAPSetCommunicationsDown.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyHost")
)
if mibBuilder.loadTexts:
    incognitoIPCMDLDAPSetCommunicationsDown.setStatus(
        "current"
    )

incognitoIPCMDDHCPDoSExceededLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 36)
)
incognitoIPCMDDHCPDoSExceededLimit.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyDevice")
)
if mibBuilder.loadTexts:
    incognitoIPCMDDHCPDoSExceededLimit.setStatus(
        "current"
    )

incognitoIPCMDDHCPDoSBelowLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 99, 0, 37)
)
incognitoIPCMDDHCPDoSBelowLimit.setObjects(
    ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcmdNotifyDevice")
)
if mibBuilder.loadTexts:
    incognitoIPCMDDHCPDoSBelowLimit.setStatus(
        "current"
    )


# Notifications groups

ipcNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 2, 2)
)
ipcNotificationsGroup.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcNotifyServerResumed"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "ipcNotifyServerPaused"))
)
if mibBuilder.loadTexts:
    ipcNotificationsGroup.setStatus(
        "current"
    )

ipcDeprecatedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 4, 99, 1)
)
ipcDeprecatedNotificationsGroup.setObjects(
      *(("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServerStart"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServerStop"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServicePaused"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServiceResume"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDExceededLicense"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDFreeAddressHigh"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDCriticalAddressLevel"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDOtherServerResponding"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDOtherServerNotResponding"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDFailoverConflict"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServiceOverloaded"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServiceCaughtUp"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDDDNSFailure"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDUnknownDevice"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDRogueServer"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDDiskStorageLow"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServiceBackupDone"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDFreeAddressLow"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDFailoverResynchOperationStarted"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDFailoverResynchOperationCompleted"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDNetViewCriticalHWMExceeded"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDNetViewWarningHWMExceeded"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDPossibleDuplicateDevice"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDNoMoreAddressesAvailable"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDTFTPServerLeaving"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDTFTPServerJoining"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServerJoinClusterIntegration"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDServerLeaveClusterIntegration"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDFailoverTerminated"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDLDAPCommunicationsUp"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDLDAPCommunicationsDown"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDLDAPTimedOut"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDRADIUSAccountingHWMExceeded"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDLDAPSetCommunicationsUp"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDLDAPSetCommunicationsDown"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDDHCPDoSExceededLimit"),
        ("INCOGNITO-EXPR-IPCOMMANDER-MIB", "incognitoIPCMDDHCPDoSBelowLimit"))
)
if mibBuilder.loadTexts:
    ipcDeprecatedNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipcServiceStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipcServiceStatisticsCompliance.setStatus(
        "current"
    )

todServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3606, 7, 1, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    todServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INCOGNITO-EXPR-IPCOMMANDER-MIB",
    **{"incognitoIPC": incognitoIPC,
       "draftServerMIB": draftServerMIB,
       "ipcServerObjects": ipcServerObjects,
       "ipcServiceStatisticsConformance": ipcServiceStatisticsConformance,
       "ipcServiceStatisticsCompliances": ipcServiceStatisticsCompliances,
       "ipcServiceStatisticsCompliance": ipcServiceStatisticsCompliance,
       "ipcServiceSatisticsGroups": ipcServiceSatisticsGroups,
       "ipcServiceStatisticsObjects": ipcServiceStatisticsObjects,
       "ipcServiceInformationGroups": ipcServiceInformationGroups,
       "ipcServiceInformationObjects": ipcServiceInformationObjects,
       "ipcDHCPStatistics": ipcDHCPStatistics,
       "ipcDHCPPacketStatistics": ipcDHCPPacketStatistics,
       "ipcDHCPPacketDiscardStatistics": ipcDHCPPacketDiscardStatistics,
       "ipcDHCPDiscoverPacketDiscards": ipcDHCPDiscoverPacketDiscards,
       "ipcDHCPRequestPacketDiscards": ipcDHCPRequestPacketDiscards,
       "ipcDHCPInformPacketDiscards": ipcDHCPInformPacketDiscards,
       "ipcDHCPDeclinePacketDiscards": ipcDHCPDeclinePacketDiscards,
       "ipcDHCPOtherPacketDiscards": ipcDHCPOtherPacketDiscards,
       "ipcDHCPPacketSupercedeStatistics": ipcDHCPPacketSupercedeStatistics,
       "ipcDHCPDiscoverPacketSupercedes": ipcDHCPDiscoverPacketSupercedes,
       "ipcDHCPRequestPacketSupercedes": ipcDHCPRequestPacketSupercedes,
       "ipcDHCPInformPacketSupercedes": ipcDHCPInformPacketSupercedes,
       "ipcDHCPDeclinePacketSupercedes": ipcDHCPDeclinePacketSupercedes,
       "ipcDHCPOtherPacketSupercedes": ipcDHCPOtherPacketSupercedes,
       "ipcDHCPPacketResponseStatistics": ipcDHCPPacketResponseStatistics,
       "ipcDHCPBOOTPPacketResponseAvg1minTime": ipcDHCPBOOTPPacketResponseAvg1minTime,
       "ipcDHCPBOOTPPacketResponseAvg5minTime": ipcDHCPBOOTPPacketResponseAvg5minTime,
       "ipcDHCPBOOTPPacketResponseAvg15minTime": ipcDHCPBOOTPPacketResponseAvg15minTime,
       "ipcDHCPDHCPv4PacketResponseAvg1minTime": ipcDHCPDHCPv4PacketResponseAvg1minTime,
       "ipcDHCPDHCPv4PacketResponseAvg5minTime": ipcDHCPDHCPv4PacketResponseAvg5minTime,
       "ipcDHCPDHCPv4PacketResponseAvg15minTime": ipcDHCPDHCPv4PacketResponseAvg15minTime,
       "ipcConfiguration": ipcConfiguration,
       "ipcNotifyObjects": ipcNotifyObjects,
       "ipcPausedTime": ipcPausedTime,
       "ipcResumedTime": ipcResumedTime,
       "ipcDeprecatedNotifyObjects": ipcDeprecatedNotifyObjects,
       "ipcDhcpNotifyObjects": ipcDhcpNotifyObjects,
       "ipcmdDHCPFreeAddressLowThreshold": ipcmdDHCPFreeAddressLowThreshold,
       "ipcmdDHCPFreeAddressHighThreshold": ipcmdDHCPFreeAddressHighThreshold,
       "ipcmdDHCPFreeAddressCriticalThreshold": ipcmdDHCPFreeAddressCriticalThreshold,
       "ipcmdDHCPFreeAddressValue": ipcmdDHCPFreeAddressValue,
       "ipcmdDHCPFreeAddressUnits": ipcmdDHCPFreeAddressUnits,
       "ipcmdDHCPRuleID": ipcmdDHCPRuleID,
       "ipcmdDHCPRuleName": ipcmdDHCPRuleName,
       "ipcmdDHCPRogueServerAddress": ipcmdDHCPRogueServerAddress,
       "ipcmdDHCPRogueServerNumRequest": ipcmdDHCPRogueServerNumRequest,
       "ipcmdDHCPRogueServerRequestTime": ipcmdDHCPRogueServerRequestTime,
       "ipcmdDHCPRogueServerInfo": ipcmdDHCPRogueServerInfo,
       "ipcmdDHCPCurrentUserCount": ipcmdDHCPCurrentUserCount,
       "ipcmdDHCPLicenseCount": ipcmdDHCPLicenseCount,
       "ipcmdDHCPExceedingLicenseLimit": ipcmdDHCPExceedingLicenseLimit,
       "ipcmdDHCPFailoverConflictAddress": ipcmdDHCPFailoverConflictAddress,
       "ipcmdDHCPNetViewName": ipcmdDHCPNetViewName,
       "ipcmdDHCPCurrentHWM": ipcmdDHCPCurrentHWM,
       "ipcmdDHCPFailoverResynchStartTime": ipcmdDHCPFailoverResynchStartTime,
       "ipcmdDHCPFailoverResynchEndTime": ipcmdDHCPFailoverResynchEndTime,
       "ipcmdDHCPDuplicateDeviceHWAddress": ipcmdDHCPDuplicateDeviceHWAddress,
       "ipcmdDHCPDuplicateDeviceIPAddress": ipcmdDHCPDuplicateDeviceIPAddress,
       "ipcmdDHCPDuplicateDeviceRemoteID": ipcmdDHCPDuplicateDeviceRemoteID,
       "ipcmdDHCPDuplicateDeviceCircuitID": ipcmdDHCPDuplicateDeviceCircuitID,
       "ipcmdDHCPDuplicateDeviceGWAddress": ipcmdDHCPDuplicateDeviceGWAddress,
       "ipcmdTFTPServerAddress": ipcmdTFTPServerAddress,
       "ipcmdDHCPFailoverTerminatedReason": ipcmdDHCPFailoverTerminatedReason,
       "ipcmdNotifyObjects": ipcmdNotifyObjects,
       "ipcmdNotifyServer": ipcmdNotifyServer,
       "ipcmdNotifyServerType": ipcmdNotifyServerType,
       "ipcmdUnknownIPAddress": ipcmdUnknownIPAddress,
       "ipcmdServerDiskSpaceFreeTotal": ipcmdServerDiskSpaceFreeTotal,
       "ipcmdServerDiskSpaceFreeCount": ipcmdServerDiskSpaceFreeCount,
       "ipcmdServerDiskSpaceFreeUnits": ipcmdServerDiskSpaceFreeUnits,
       "ipcmdServiceStatus": ipcmdServiceStatus,
       "ipcmdNotifyHost": ipcmdNotifyHost,
       "ipcmdNotifyDevice": ipcmdNotifyDevice,
       "ipcFailover": ipcFailover,
       "ipcFailoverStatistics": ipcFailoverStatistics,
       "ipcFailoverSummaryStatistics": ipcFailoverSummaryStatistics,
       "ipcFailoverTimerSummaryStatistics": ipcFailoverTimerSummaryStatistics,
       "ipcFailStatLastStartTime": ipcFailStatLastStartTime,
       "ipcFailStatLastSyncTime": ipcFailStatLastSyncTime,
       "ipcFailStatLastTestTime": ipcFailStatLastTestTime,
       "ipcFailStatLastDownTime": ipcFailStatLastDownTime,
       "ipcFailStatLastUpTime": ipcFailStatLastUpTime,
       "ipcFailoverErrorSummaryStatistics": ipcFailoverErrorSummaryStatistics,
       "ipcFailStatSendErrors": ipcFailStatSendErrors,
       "ipcFailStatRecvErrors": ipcFailStatRecvErrors,
       "ipcFailStatPlatformMismatchErrors": ipcFailStatPlatformMismatchErrors,
       "ipcFailStatVersionMismatchErrors": ipcFailStatVersionMismatchErrors,
       "ipcFailStatRoleMismatchErrors": ipcFailStatRoleMismatchErrors,
       "ipcFailStatCRC1Errors": ipcFailStatCRC1Errors,
       "ipcFailStatCRC2Errors": ipcFailStatCRC2Errors,
       "ipcFailStatDecryptErrors": ipcFailStatDecryptErrors,
       "ipcFailStatAccessDeniedErrors": ipcFailStatAccessDeniedErrors,
       "ipcFailoverTimeDownSummaryStatistics": ipcFailoverTimeDownSummaryStatistics,
       "ipcFailStatTotalTimeDown": ipcFailStatTotalTimeDown,
       "ipcFailStatLongestTimeDown": ipcFailStatLongestTimeDown,
       "ipcFailStatCountTimeDown": ipcFailStatCountTimeDown,
       "ipcFailoverResynchSummaryStatistics": ipcFailoverResynchSummaryStatistics,
       "ipcFailStatTotalResynch": ipcFailStatTotalResynch,
       "ipcFailStatLongestResynch": ipcFailStatLongestResynch,
       "ipcFailStatCountResynch": ipcFailStatCountResynch,
       "ipcFailoverTimeupSummaryStatistics": ipcFailoverTimeupSummaryStatistics,
       "ipcFailStatTotalTimeUp": ipcFailStatTotalTimeUp,
       "ipcFailStatLongestTimeUp": ipcFailStatLongestTimeUp,
       "ipcFailStatCountTimeUp": ipcFailStatCountTimeUp,
       "ipcFailoverRecdSummaryStatistics": ipcFailoverRecdSummaryStatistics,
       "ipcFailStatRecdHeartbeats": ipcFailStatRecdHeartbeats,
       "ipcFailStatRecdTestRequests": ipcFailStatRecdTestRequests,
       "ipcFailStatRecdTestReplies": ipcFailStatRecdTestReplies,
       "ipcFailStatRecdDataTxRequests": ipcFailStatRecdDataTxRequests,
       "ipcFailStatRecdDataTxData": ipcFailStatRecdDataTxData,
       "ipcFailStatRecdDataTxAcks": ipcFailStatRecdDataTxAcks,
       "ipcFailStatRecdDataTransactionData": ipcFailStatRecdDataTransactionData,
       "ipcFailStatRecdDataTransactionAcks": ipcFailStatRecdDataTransactionAcks,
       "ipcFailStatRecdDataConflicts": ipcFailStatRecdDataConflicts,
       "ipcFailStatRecdDataConflictAcks": ipcFailStatRecdDataConflictAcks,
       "ipcFailStatRecdDataResynchRequests": ipcFailStatRecdDataResynchRequests,
       "ipcFailStatRecdDataResynchAcks": ipcFailStatRecdDataResynchAcks,
       "ipcFailStatRecdShuttingDown": ipcFailStatRecdShuttingDown,
       "ipcFailoverSentSummaryStatistics": ipcFailoverSentSummaryStatistics,
       "ipcFailStatSentHeartbeats": ipcFailStatSentHeartbeats,
       "ipcFailStatSentTestRequests": ipcFailStatSentTestRequests,
       "ipcFailStatSentTestReplies": ipcFailStatSentTestReplies,
       "ipcFailStatSentDataTxRequests": ipcFailStatSentDataTxRequests,
       "ipcFailStatSentDataTxData": ipcFailStatSentDataTxData,
       "ipcFailStatSentDataTxAcks": ipcFailStatSentDataTxAcks,
       "ipcFailStatSentDataTransactionData": ipcFailStatSentDataTransactionData,
       "ipcFailStatSentDataTransactionAcks": ipcFailStatSentDataTransactionAcks,
       "ipcFailStatSentDataConflicts": ipcFailStatSentDataConflicts,
       "ipcFailStatSentDataConflictAcks": ipcFailStatSentDataConflictAcks,
       "ipcFailStatSentDataResynchRequests": ipcFailStatSentDataResynchRequests,
       "ipcFailStatSentDataResynchAcks": ipcFailStatSentDataResynchAcks,
       "ipcFailStatSentShuttingDown": ipcFailStatSentShuttingDown,
       "ipcFailoverTrafficSummaryStatistics": ipcFailoverTrafficSummaryStatistics,
       "ipcFailStatBytesSent": ipcFailStatBytesSent,
       "ipcFailStatBytesRecd": ipcFailStatBytesRecd,
       "ipcFailStatTxSent": ipcFailStatTxSent,
       "ipcFailStatTxRecd": ipcFailStatTxRecd,
       "ipcFailoverStatusSummaryStatistics": ipcFailoverStatusSummaryStatistics,
       "ipcFailStatStatus": ipcFailStatStatus,
       "ipcFailStatOperation": ipcFailStatOperation,
       "ipcFailoverProtocolStatistics": ipcFailoverProtocolStatistics,
       "ipcServiceStatistics": ipcServiceStatistics,
       "ipcServiceLeasesInUse": ipcServiceLeasesInUse,
       "ipcServiceInformation": ipcServiceInformation,
       "ipcServiceServerName": ipcServiceServerName,
       "ipcServiceName": ipcServiceName,
       "ipcServiceVersion": ipcServiceVersion,
       "ipcServiceLicenseUsers": ipcServiceLicenseUsers,
       "ipcServiceSubscriptionExpiration": ipcServiceSubscriptionExpiration,
       "ipcServiceLicenseType": ipcServiceLicenseType,
       "ipcServiceOperatingSystem": ipcServiceOperatingSystem,
       "ipcServiceStartTime": ipcServiceStartTime,
       "ipcNotificationPrefix": ipcNotificationPrefix,
       "ipcNotifications": ipcNotifications,
       "ipcNotifyServerPaused": ipcNotifyServerPaused,
       "ipcNotifyServerResumed": ipcNotifyServerResumed,
       "ipcConformance": ipcConformance,
       "ipcCompliances": ipcCompliances,
       "ipcGroups": ipcGroups,
       "ipcNotifyObjectsGroup": ipcNotifyObjectsGroup,
       "ipcNotificationsGroup": ipcNotificationsGroup,
       "ipcFailoverSummaryStatisticsGroup": ipcFailoverSummaryStatisticsGroup,
       "ipcDHCPPacketStatisticsGroup": ipcDHCPPacketStatisticsGroup,
       "ipcDeprecatedGroups": ipcDeprecatedGroups,
       "ipcDeprecatedNotificationsGroup": ipcDeprecatedNotificationsGroup,
       "ipcDeprecatedNotifyBaseObjectsGroup": ipcDeprecatedNotifyBaseObjectsGroup,
       "ipcDeprecatedNotifyObjectsGroup": ipcDeprecatedNotifyObjectsGroup,
       "ipcTimeOfDayServer": ipcTimeOfDayServer,
       "todServerObjects": todServerObjects,
       "todCounters": todCounters,
       "todCountTcpRequests": todCountTcpRequests,
       "todCountUdpRequests": todCountUdpRequests,
       "todClientObjects": todClientObjects,
       "todServerNotificationPrefix": todServerNotificationPrefix,
       "todServerConformance": todServerConformance,
       "todServerCompliances": todServerCompliances,
       "todServerCompliance": todServerCompliance,
       "todServerGroups": todServerGroups,
       "todServerCounterObjects": todServerCounterObjects,
       "ipcDeprecatedNotificationPrefix": ipcDeprecatedNotificationPrefix,
       "incognitoNotifyNotifications": incognitoNotifyNotifications,
       "incognitoIPCMDServerStart": incognitoIPCMDServerStart,
       "incognitoIPCMDServerStop": incognitoIPCMDServerStop,
       "incognitoIPCMDServicePaused": incognitoIPCMDServicePaused,
       "incognitoIPCMDServiceResume": incognitoIPCMDServiceResume,
       "incognitoIPCMDExceededLicense": incognitoIPCMDExceededLicense,
       "incognitoIPCMDFreeAddressHigh": incognitoIPCMDFreeAddressHigh,
       "incognitoIPCMDCriticalAddressLevel": incognitoIPCMDCriticalAddressLevel,
       "incognitoIPCMDOtherServerResponding": incognitoIPCMDOtherServerResponding,
       "incognitoIPCMDOtherServerNotResponding": incognitoIPCMDOtherServerNotResponding,
       "incognitoIPCMDFailoverConflict": incognitoIPCMDFailoverConflict,
       "incognitoIPCMDServiceOverloaded": incognitoIPCMDServiceOverloaded,
       "incognitoIPCMDServiceCaughtUp": incognitoIPCMDServiceCaughtUp,
       "incognitoIPCMDDDNSFailure": incognitoIPCMDDDNSFailure,
       "incognitoIPCMDUnknownDevice": incognitoIPCMDUnknownDevice,
       "incognitoIPCMDRogueServer": incognitoIPCMDRogueServer,
       "incognitoIPCMDDiskStorageLow": incognitoIPCMDDiskStorageLow,
       "incognitoIPCMDServiceBackupDone": incognitoIPCMDServiceBackupDone,
       "incognitoIPCMDFreeAddressLow": incognitoIPCMDFreeAddressLow,
       "incognitoIPCMDFailoverResynchOperationStarted": incognitoIPCMDFailoverResynchOperationStarted,
       "incognitoIPCMDFailoverResynchOperationCompleted": incognitoIPCMDFailoverResynchOperationCompleted,
       "incognitoIPCMDNetViewCriticalHWMExceeded": incognitoIPCMDNetViewCriticalHWMExceeded,
       "incognitoIPCMDNetViewWarningHWMExceeded": incognitoIPCMDNetViewWarningHWMExceeded,
       "incognitoIPCMDPossibleDuplicateDevice": incognitoIPCMDPossibleDuplicateDevice,
       "incognitoIPCMDNoMoreAddressesAvailable": incognitoIPCMDNoMoreAddressesAvailable,
       "incognitoIPCMDTFTPServerJoining": incognitoIPCMDTFTPServerJoining,
       "incognitoIPCMDTFTPServerLeaving": incognitoIPCMDTFTPServerLeaving,
       "incognitoIPCMDServerJoinClusterIntegration": incognitoIPCMDServerJoinClusterIntegration,
       "incognitoIPCMDServerLeaveClusterIntegration": incognitoIPCMDServerLeaveClusterIntegration,
       "incognitoIPCMDFailoverTerminated": incognitoIPCMDFailoverTerminated,
       "incognitoIPCMDLDAPCommunicationsUp": incognitoIPCMDLDAPCommunicationsUp,
       "incognitoIPCMDLDAPCommunicationsDown": incognitoIPCMDLDAPCommunicationsDown,
       "incognitoIPCMDLDAPTimedOut": incognitoIPCMDLDAPTimedOut,
       "incognitoIPCMDRADIUSAccountingHWMExceeded": incognitoIPCMDRADIUSAccountingHWMExceeded,
       "incognitoIPCMDLDAPSetCommunicationsUp": incognitoIPCMDLDAPSetCommunicationsUp,
       "incognitoIPCMDLDAPSetCommunicationsDown": incognitoIPCMDLDAPSetCommunicationsDown,
       "incognitoIPCMDDHCPDoSExceededLimit": incognitoIPCMDDHCPDoSExceededLimit,
       "incognitoIPCMDDHCPDoSBelowLimit": incognitoIPCMDDHCPDoSBelowLimit}
)
