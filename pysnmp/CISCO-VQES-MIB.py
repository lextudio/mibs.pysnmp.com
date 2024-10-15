# SNMP MIB module (CISCO-VQES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VQES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:37 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVqeSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942)
)
ciscoVqeSMIB.setRevisions(
        ("2010-01-14 11:10",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVqeSMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVqeSMIBNotifs = _CiscoVqeSMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 0)
)
_CiscoVqeSMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVqeSMIBObjects = _CiscoVqeSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1)
)
_CvqsControlInfo_ObjectIdentity = ObjectIdentity
cvqsControlInfo = _CvqsControlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 1)
)


class _CvqsNotificationsEnable_Type(TruthValue):
    """Custom type cvqsNotificationsEnable based on TruthValue"""


_CvqsNotificationsEnable_Object = MibScalar
cvqsNotificationsEnable = _CvqsNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 1, 1),
    _CvqsNotificationsEnable_Type()
)
cvqsNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvqsNotificationsEnable.setStatus("current")
_CvqsChannelInfo_ObjectIdentity = ObjectIdentity
cvqsChannelInfo = _CvqsChannelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2)
)
_CvqsNumberofChannels_Type = Gauge32
_CvqsNumberofChannels_Object = MibScalar
cvqsNumberofChannels = _CvqsNumberofChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 1),
    _CvqsNumberofChannels_Type()
)
cvqsNumberofChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsNumberofChannels.setStatus("current")
_CvqsActiveChannels_Type = Gauge32
_CvqsActiveChannels_Object = MibScalar
cvqsActiveChannels = _CvqsActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 2),
    _CvqsActiveChannels_Type()
)
cvqsActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsActiveChannels.setStatus("current")
_CvqsLastUpdatedTime_Type = DateAndTime
_CvqsLastUpdatedTime_Object = MibScalar
cvqsLastUpdatedTime = _CvqsLastUpdatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 3),
    _CvqsLastUpdatedTime_Type()
)
cvqsLastUpdatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsLastUpdatedTime.setStatus("current")
_CvqsChannelTable_Object = MibTable
cvqsChannelTable = _CvqsChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cvqsChannelTable.setStatus("current")
_CvqsChannelTableEntry_Object = MibTableRow
cvqsChannelTableEntry = _CvqsChannelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4, 1)
)
cvqsChannelTableEntry.setIndexNames(
    (0, "CISCO-VQES-MIB", "cvqsChannelIndex"),
)
if mibBuilder.loadTexts:
    cvqsChannelTableEntry.setStatus("current")


class _CvqsChannelIndex_Type(Unsigned32):
    """Custom type cvqsChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CvqsChannelIndex_Type.__name__ = "Unsigned32"
_CvqsChannelIndex_Object = MibTableColumn
cvqsChannelIndex = _CvqsChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4, 1, 1),
    _CvqsChannelIndex_Type()
)
cvqsChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvqsChannelIndex.setStatus("current")
_CvqsChannelMulticastIPType_Type = InetAddressType
_CvqsChannelMulticastIPType_Object = MibTableColumn
cvqsChannelMulticastIPType = _CvqsChannelMulticastIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4, 1, 2),
    _CvqsChannelMulticastIPType_Type()
)
cvqsChannelMulticastIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsChannelMulticastIPType.setStatus("current")
_CvqsChannelMulticastIPAddr_Type = InetAddress
_CvqsChannelMulticastIPAddr_Object = MibTableColumn
cvqsChannelMulticastIPAddr = _CvqsChannelMulticastIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4, 1, 3),
    _CvqsChannelMulticastIPAddr_Type()
)
cvqsChannelMulticastIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsChannelMulticastIPAddr.setStatus("current")
_CvqsChannelMulticastPort_Type = InetPortNumber
_CvqsChannelMulticastPort_Object = MibTableColumn
cvqsChannelMulticastPort = _CvqsChannelMulticastPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4, 1, 4),
    _CvqsChannelMulticastPort_Type()
)
cvqsChannelMulticastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsChannelMulticastPort.setStatus("current")


class _CvqsChannelStatus_Type(Integer32):
    """Custom type cvqsChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("inoperative", 3))
    )


_CvqsChannelStatus_Type.__name__ = "Integer32"
_CvqsChannelStatus_Object = MibTableColumn
cvqsChannelStatus = _CvqsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4, 1, 5),
    _CvqsChannelStatus_Type()
)
cvqsChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsChannelStatus.setStatus("current")
_CvqsChannelMemberPopulation_Type = Gauge32
_CvqsChannelMemberPopulation_Object = MibTableColumn
cvqsChannelMemberPopulation = _CvqsChannelMemberPopulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 2, 4, 1, 6),
    _CvqsChannelMemberPopulation_Type()
)
cvqsChannelMemberPopulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsChannelMemberPopulation.setStatus("current")
_CvqsErrorRepair_ObjectIdentity = ObjectIdentity
cvqsErrorRepair = _CvqsErrorRepair_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 3)
)
_CvqsTotalReceivedERMsgs_Type = Counter64
_CvqsTotalReceivedERMsgs_Object = MibScalar
cvqsTotalReceivedERMsgs = _CvqsTotalReceivedERMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 3, 1),
    _CvqsTotalReceivedERMsgs_Type()
)
cvqsTotalReceivedERMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalReceivedERMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalReceivedERMsgs.setUnits("ER requests")
_CvqsTotalReceivedInvalidERMsgs_Type = Counter64
_CvqsTotalReceivedInvalidERMsgs_Object = MibScalar
cvqsTotalReceivedInvalidERMsgs = _CvqsTotalReceivedInvalidERMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 3, 2),
    _CvqsTotalReceivedInvalidERMsgs_Type()
)
cvqsTotalReceivedInvalidERMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalReceivedInvalidERMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalReceivedInvalidERMsgs.setUnits("ER requests")
_CvqsTotalReceivedERPkts_Type = Counter64
_CvqsTotalReceivedERPkts_Object = MibScalar
cvqsTotalReceivedERPkts = _CvqsTotalReceivedERPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 3, 3),
    _CvqsTotalReceivedERPkts_Type()
)
cvqsTotalReceivedERPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalReceivedERPkts.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalReceivedERPkts.setUnits("ER packets")
_CvqsTotalSentERPkts_Type = Counter64
_CvqsTotalSentERPkts_Object = MibScalar
cvqsTotalSentERPkts = _CvqsTotalSentERPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 3, 4),
    _CvqsTotalSentERPkts_Type()
)
cvqsTotalSentERPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalSentERPkts.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalSentERPkts.setUnits("ER packets")
_CvqsRCC_ObjectIdentity = ObjectIdentity
cvqsRCC = _CvqsRCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 4)
)
_CvqsTotalReceivedRCCs_Type = Counter64
_CvqsTotalReceivedRCCs_Object = MibScalar
cvqsTotalReceivedRCCs = _CvqsTotalReceivedRCCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 4, 1),
    _CvqsTotalReceivedRCCs_Type()
)
cvqsTotalReceivedRCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalReceivedRCCs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalReceivedRCCs.setUnits("RCC requests")
_CvqsTotalAcceptedRCCs_Type = Counter64
_CvqsTotalAcceptedRCCs_Object = MibScalar
cvqsTotalAcceptedRCCs = _CvqsTotalAcceptedRCCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 4, 2),
    _CvqsTotalAcceptedRCCs_Type()
)
cvqsTotalAcceptedRCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalAcceptedRCCs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalAcceptedRCCs.setUnits("RCC requests")
_CvqsTotalRefusedRCCs_Type = Counter64
_CvqsTotalRefusedRCCs_Object = MibScalar
cvqsTotalRefusedRCCs = _CvqsTotalRefusedRCCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 4, 3),
    _CvqsTotalRefusedRCCs_Type()
)
cvqsTotalRefusedRCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalRefusedRCCs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalRefusedRCCs.setUnits("RCC requests")
_CvqsCapacity_ObjectIdentity = ObjectIdentity
cvqsCapacity = _CvqsCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 5)
)
_CvqsTotalRTCPReceivers_Type = Gauge32
_CvqsTotalRTCPReceivers_Object = MibScalar
cvqsTotalRTCPReceivers = _CvqsTotalRTCPReceivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 5, 1),
    _CvqsTotalRTCPReceivers_Type()
)
cvqsTotalRTCPReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsTotalRTCPReceivers.setStatus("current")
if mibBuilder.loadTexts:
    cvqsTotalRTCPReceivers.setUnits("RTCP receivers")
_CvqsRejectedRTCPs_Type = Counter64
_CvqsRejectedRTCPs_Object = MibScalar
cvqsRejectedRTCPs = _CvqsRejectedRTCPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 5, 2),
    _CvqsRejectedRTCPs_Type()
)
cvqsRejectedRTCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsRejectedRTCPs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsRejectedRTCPs.setUnits("RTCP packets")
_CvqsRejectedERs_Type = Counter64
_CvqsRejectedERs_Object = MibScalar
cvqsRejectedERs = _CvqsRejectedERs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 5, 3),
    _CvqsRejectedERs_Type()
)
cvqsRejectedERs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsRejectedERs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsRejectedERs.setUnits("ER requests")
_CvqsRejectedRCCs_Type = Counter64
_CvqsRejectedRCCs_Object = MibScalar
cvqsRejectedRCCs = _CvqsRejectedRCCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 1, 5, 4),
    _CvqsRejectedRCCs_Type()
)
cvqsRejectedRCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqsRejectedRCCs.setStatus("current")
if mibBuilder.loadTexts:
    cvqsRejectedRCCs.setUnits("RCC requests")
_CiscoVqeSMIBConform_ObjectIdentity = ObjectIdentity
ciscoVqeSMIBConform = _CiscoVqeSMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2)
)
_CvqsMIBCompliances_ObjectIdentity = ObjectIdentity
cvqsMIBCompliances = _CvqsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 1)
)
_CvqsMIBGroups_ObjectIdentity = ObjectIdentity
cvqsMIBGroups = _CvqsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 2)
)

# Managed Objects groups

ciscoVqeSControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 2, 1)
)
ciscoVqeSControlGroup.setObjects(
    ("CISCO-VQES-MIB", "cvqsNotificationsEnable")
)
if mibBuilder.loadTexts:
    ciscoVqeSControlGroup.setStatus("current")

ciscoVqeSChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 2, 2)
)
ciscoVqeSChannelGroup.setObjects(
      *(("CISCO-VQES-MIB", "cvqsNumberofChannels"),
        ("CISCO-VQES-MIB", "cvqsActiveChannels"),
        ("CISCO-VQES-MIB", "cvqsLastUpdatedTime"),
        ("CISCO-VQES-MIB", "cvqsChannelMulticastIPType"),
        ("CISCO-VQES-MIB", "cvqsChannelMulticastIPAddr"),
        ("CISCO-VQES-MIB", "cvqsChannelMulticastPort"),
        ("CISCO-VQES-MIB", "cvqsChannelStatus"),
        ("CISCO-VQES-MIB", "cvqsChannelMemberPopulation"))
)
if mibBuilder.loadTexts:
    ciscoVqeSChannelGroup.setStatus("current")

ciscoVqeSERGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 2, 3)
)
ciscoVqeSERGroup.setObjects(
      *(("CISCO-VQES-MIB", "cvqsTotalReceivedERMsgs"),
        ("CISCO-VQES-MIB", "cvqsTotalReceivedInvalidERMsgs"),
        ("CISCO-VQES-MIB", "cvqsTotalReceivedERPkts"),
        ("CISCO-VQES-MIB", "cvqsTotalSentERPkts"))
)
if mibBuilder.loadTexts:
    ciscoVqeSERGroup.setStatus("current")

ciscoVqeSRCCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 2, 4)
)
ciscoVqeSRCCGroup.setObjects(
      *(("CISCO-VQES-MIB", "cvqsTotalReceivedRCCs"),
        ("CISCO-VQES-MIB", "cvqsTotalAcceptedRCCs"),
        ("CISCO-VQES-MIB", "cvqsTotalRefusedRCCs"))
)
if mibBuilder.loadTexts:
    ciscoVqeSRCCGroup.setStatus("current")

ciscoVqeSCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 2, 5)
)
ciscoVqeSCapacityGroup.setObjects(
      *(("CISCO-VQES-MIB", "cvqsTotalRTCPReceivers"),
        ("CISCO-VQES-MIB", "cvqsRejectedRTCPs"),
        ("CISCO-VQES-MIB", "cvqsRejectedERs"),
        ("CISCO-VQES-MIB", "cvqsRejectedRCCs"))
)
if mibBuilder.loadTexts:
    ciscoVqeSCapacityGroup.setStatus("current")


# Notification objects

cvqsChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 0, 1)
)
cvqsChannelUp.setObjects(
      *(("CISCO-VQES-MIB", "cvqsChannelMulticastIPType"),
        ("CISCO-VQES-MIB", "cvqsChannelMulticastIPAddr"),
        ("CISCO-VQES-MIB", "cvqsChannelMulticastPort"))
)
if mibBuilder.loadTexts:
    cvqsChannelUp.setStatus(
        "current"
    )

cvqsChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 0, 2)
)
cvqsChannelDown.setObjects(
      *(("CISCO-VQES-MIB", "cvqsChannelMulticastIPType"),
        ("CISCO-VQES-MIB", "cvqsChannelMulticastIPAddr"),
        ("CISCO-VQES-MIB", "cvqsChannelMulticastPort"))
)
if mibBuilder.loadTexts:
    cvqsChannelDown.setStatus(
        "current"
    )


# Notifications groups

ciscoVqeSNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 2, 6)
)
ciscoVqeSNotifGroup.setObjects(
      *(("CISCO-VQES-MIB", "cvqsChannelUp"),
        ("CISCO-VQES-MIB", "cvqsChannelDown"))
)
if mibBuilder.loadTexts:
    ciscoVqeSNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvqsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 942, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvqsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VQES-MIB",
    **{"ciscoVqeSMIB": ciscoVqeSMIB,
       "ciscoVqeSMIBNotifs": ciscoVqeSMIBNotifs,
       "cvqsChannelUp": cvqsChannelUp,
       "cvqsChannelDown": cvqsChannelDown,
       "ciscoVqeSMIBObjects": ciscoVqeSMIBObjects,
       "cvqsControlInfo": cvqsControlInfo,
       "cvqsNotificationsEnable": cvqsNotificationsEnable,
       "cvqsChannelInfo": cvqsChannelInfo,
       "cvqsNumberofChannels": cvqsNumberofChannels,
       "cvqsActiveChannels": cvqsActiveChannels,
       "cvqsLastUpdatedTime": cvqsLastUpdatedTime,
       "cvqsChannelTable": cvqsChannelTable,
       "cvqsChannelTableEntry": cvqsChannelTableEntry,
       "cvqsChannelIndex": cvqsChannelIndex,
       "cvqsChannelMulticastIPType": cvqsChannelMulticastIPType,
       "cvqsChannelMulticastIPAddr": cvqsChannelMulticastIPAddr,
       "cvqsChannelMulticastPort": cvqsChannelMulticastPort,
       "cvqsChannelStatus": cvqsChannelStatus,
       "cvqsChannelMemberPopulation": cvqsChannelMemberPopulation,
       "cvqsErrorRepair": cvqsErrorRepair,
       "cvqsTotalReceivedERMsgs": cvqsTotalReceivedERMsgs,
       "cvqsTotalReceivedInvalidERMsgs": cvqsTotalReceivedInvalidERMsgs,
       "cvqsTotalReceivedERPkts": cvqsTotalReceivedERPkts,
       "cvqsTotalSentERPkts": cvqsTotalSentERPkts,
       "cvqsRCC": cvqsRCC,
       "cvqsTotalReceivedRCCs": cvqsTotalReceivedRCCs,
       "cvqsTotalAcceptedRCCs": cvqsTotalAcceptedRCCs,
       "cvqsTotalRefusedRCCs": cvqsTotalRefusedRCCs,
       "cvqsCapacity": cvqsCapacity,
       "cvqsTotalRTCPReceivers": cvqsTotalRTCPReceivers,
       "cvqsRejectedRTCPs": cvqsRejectedRTCPs,
       "cvqsRejectedERs": cvqsRejectedERs,
       "cvqsRejectedRCCs": cvqsRejectedRCCs,
       "ciscoVqeSMIBConform": ciscoVqeSMIBConform,
       "cvqsMIBCompliances": cvqsMIBCompliances,
       "cvqsMIBCompliance": cvqsMIBCompliance,
       "cvqsMIBGroups": cvqsMIBGroups,
       "ciscoVqeSControlGroup": ciscoVqeSControlGroup,
       "ciscoVqeSChannelGroup": ciscoVqeSChannelGroup,
       "ciscoVqeSERGroup": ciscoVqeSERGroup,
       "ciscoVqeSRCCGroup": ciscoVqeSRCCGroup,
       "ciscoVqeSCapacityGroup": ciscoVqeSCapacityGroup,
       "ciscoVqeSNotifGroup": ciscoVqeSNotifGroup}
)
