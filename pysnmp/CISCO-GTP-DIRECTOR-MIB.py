# SNMP MIB module (CISCO-GTP-DIRECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GTP-DIRECTOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:04 2024
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

ciscoGtpDirectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245)
)
ciscoGtpDirectorMIB.setRevisions(
        ("2001-09-13 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGtpDirectorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGtpDirectorMIBObjects = _CiscoGtpDirectorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1)
)
_CgdConfigurations_ObjectIdentity = ObjectIdentity
cgdConfigurations = _CgdConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 1)
)


class _CgdCreatePdpRequestInfoSaveTimer_Type(Unsigned32):
    """Custom type cgdCreatePdpRequestInfoSaveTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgdCreatePdpRequestInfoSaveTimer_Type.__name__ = "Unsigned32"
_CgdCreatePdpRequestInfoSaveTimer_Object = MibScalar
cgdCreatePdpRequestInfoSaveTimer = _CgdCreatePdpRequestInfoSaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 1, 1),
    _CgdCreatePdpRequestInfoSaveTimer_Type()
)
cgdCreatePdpRequestInfoSaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgdCreatePdpRequestInfoSaveTimer.setStatus("current")
if mibBuilder.loadTexts:
    cgdCreatePdpRequestInfoSaveTimer.setUnits("seconds")
_CgdStatus_ObjectIdentity = ObjectIdentity
cgdStatus = _CgdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 2)
)
_CgdPendingPdps_Type = Gauge32
_CgdPendingPdps_Object = MibScalar
cgdPendingPdps = _CgdPendingPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 2, 1),
    _CgdPendingPdps_Type()
)
cgdPendingPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdPendingPdps.setStatus("current")
_CgdStatistics_ObjectIdentity = ObjectIdentity
cgdStatistics = _CgdStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3)
)
_CgdCreatePdpRequestFwded_Type = Counter32
_CgdCreatePdpRequestFwded_Object = MibScalar
cgdCreatePdpRequestFwded = _CgdCreatePdpRequestFwded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 1),
    _CgdCreatePdpRequestFwded_Type()
)
cgdCreatePdpRequestFwded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdCreatePdpRequestFwded.setStatus("current")
_CgdTotalCreatePdpRequestFwded_Type = Counter32
_CgdTotalCreatePdpRequestFwded_Object = MibScalar
cgdTotalCreatePdpRequestFwded = _CgdTotalCreatePdpRequestFwded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 2),
    _CgdTotalCreatePdpRequestFwded_Type()
)
cgdTotalCreatePdpRequestFwded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalCreatePdpRequestFwded.setStatus("current")
_CgdCreateRequestRejected_Type = Counter32
_CgdCreateRequestRejected_Object = MibScalar
cgdCreateRequestRejected = _CgdCreateRequestRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 3),
    _CgdCreateRequestRejected_Type()
)
cgdCreateRequestRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdCreateRequestRejected.setStatus("current")
_CgdTotalUnsupportedMessages_Type = Counter32
_CgdTotalUnsupportedMessages_Object = MibScalar
cgdTotalUnsupportedMessages = _CgdTotalUnsupportedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 4),
    _CgdTotalUnsupportedMessages_Type()
)
cgdTotalUnsupportedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalUnsupportedMessages.setStatus("current")
_CgdPdpRequestDropped_Type = Counter32
_CgdPdpRequestDropped_Object = MibScalar
cgdPdpRequestDropped = _CgdPdpRequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 5),
    _CgdPdpRequestDropped_Type()
)
cgdPdpRequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdPdpRequestDropped.setStatus("current")
_CgdNotifMgmt_ObjectIdentity = ObjectIdentity
cgdNotifMgmt = _CgdNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 4)
)


class _CgdNotifEnable_Type(TruthValue):
    """Custom type cgdNotifEnable based on TruthValue"""


_CgdNotifEnable_Object = MibScalar
cgdNotifEnable = _CgdNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 4, 1),
    _CgdNotifEnable_Type()
)
cgdNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgdNotifEnable.setStatus("current")


class _CgdNotifType_Type(Integer32):
    """Custom type cgdNotifType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gdmServiceDown", 2),
          ("gdmServiceUp", 1))
    )


_CgdNotifType_Type.__name__ = "Integer32"
_CgdNotifType_Object = MibScalar
cgdNotifType = _CgdNotifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 4, 2),
    _CgdNotifType_Type()
)
cgdNotifType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgdNotifType.setStatus("current")
_CiscoGtpDirectorNotifPrefix_ObjectIdentity = ObjectIdentity
ciscoGtpDirectorNotifPrefix = _CiscoGtpDirectorNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 2)
)
_CiscoGtpDirectorNotifications_ObjectIdentity = ObjectIdentity
ciscoGtpDirectorNotifications = _CiscoGtpDirectorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 2, 0)
)
_CiscoGtpDirectorMIBConformance_ObjectIdentity = ObjectIdentity
ciscoGtpDirectorMIBConformance = _CiscoGtpDirectorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3)
)
_CiscoGtpDirectorMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGtpDirectorMIBCompliances = _CiscoGtpDirectorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 1)
)
_CiscoGtpDirectorMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGtpDirectorMIBGroups = _CiscoGtpDirectorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2)
)

# Managed Objects groups

ciscoGtpDirectorConfigurationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 1)
)
ciscoGtpDirectorConfigurationsGroup.setObjects(
    ("CISCO-GTP-DIRECTOR-MIB", "cgdCreatePdpRequestInfoSaveTimer")
)
if mibBuilder.loadTexts:
    ciscoGtpDirectorConfigurationsGroup.setStatus("current")

ciscoGtpDirectorStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 2)
)
ciscoGtpDirectorStatusGroup.setObjects(
    ("CISCO-GTP-DIRECTOR-MIB", "cgdPendingPdps")
)
if mibBuilder.loadTexts:
    ciscoGtpDirectorStatusGroup.setStatus("current")

ciscoGtpDirectorStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 3)
)
ciscoGtpDirectorStatisticsGroup.setObjects(
      *(("CISCO-GTP-DIRECTOR-MIB", "cgdCreatePdpRequestFwded"),
        ("CISCO-GTP-DIRECTOR-MIB", "cgdTotalCreatePdpRequestFwded"),
        ("CISCO-GTP-DIRECTOR-MIB", "cgdCreateRequestRejected"),
        ("CISCO-GTP-DIRECTOR-MIB", "cgdTotalUnsupportedMessages"),
        ("CISCO-GTP-DIRECTOR-MIB", "cgdPdpRequestDropped"))
)
if mibBuilder.loadTexts:
    ciscoGtpDirectorStatisticsGroup.setStatus("current")

ciscoGtpDirectorNotifMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 4)
)
ciscoGtpDirectorNotifMgmtGroup.setObjects(
      *(("CISCO-GTP-DIRECTOR-MIB", "cgdNotifEnable"),
        ("CISCO-GTP-DIRECTOR-MIB", "cgdNotifType"))
)
if mibBuilder.loadTexts:
    ciscoGtpDirectorNotifMgmtGroup.setStatus("current")


# Notification objects

ciscoGtpDirectorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 2, 0, 1)
)
ciscoGtpDirectorNotification.setObjects(
    ("CISCO-GTP-DIRECTOR-MIB", "cgdNotifType")
)
if mibBuilder.loadTexts:
    ciscoGtpDirectorNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoGtpDirectorNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 5)
)
ciscoGtpDirectorNotifGroup.setObjects(
    ("CISCO-GTP-DIRECTOR-MIB", "ciscoGtpDirectorNotification")
)
if mibBuilder.loadTexts:
    ciscoGtpDirectorNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGtpDirectorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGtpDirectorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GTP-DIRECTOR-MIB",
    **{"ciscoGtpDirectorMIB": ciscoGtpDirectorMIB,
       "ciscoGtpDirectorMIBObjects": ciscoGtpDirectorMIBObjects,
       "cgdConfigurations": cgdConfigurations,
       "cgdCreatePdpRequestInfoSaveTimer": cgdCreatePdpRequestInfoSaveTimer,
       "cgdStatus": cgdStatus,
       "cgdPendingPdps": cgdPendingPdps,
       "cgdStatistics": cgdStatistics,
       "cgdCreatePdpRequestFwded": cgdCreatePdpRequestFwded,
       "cgdTotalCreatePdpRequestFwded": cgdTotalCreatePdpRequestFwded,
       "cgdCreateRequestRejected": cgdCreateRequestRejected,
       "cgdTotalUnsupportedMessages": cgdTotalUnsupportedMessages,
       "cgdPdpRequestDropped": cgdPdpRequestDropped,
       "cgdNotifMgmt": cgdNotifMgmt,
       "cgdNotifEnable": cgdNotifEnable,
       "cgdNotifType": cgdNotifType,
       "ciscoGtpDirectorNotifPrefix": ciscoGtpDirectorNotifPrefix,
       "ciscoGtpDirectorNotifications": ciscoGtpDirectorNotifications,
       "ciscoGtpDirectorNotification": ciscoGtpDirectorNotification,
       "ciscoGtpDirectorMIBConformance": ciscoGtpDirectorMIBConformance,
       "ciscoGtpDirectorMIBCompliances": ciscoGtpDirectorMIBCompliances,
       "ciscoGtpDirectorMIBCompliance": ciscoGtpDirectorMIBCompliance,
       "ciscoGtpDirectorMIBGroups": ciscoGtpDirectorMIBGroups,
       "ciscoGtpDirectorConfigurationsGroup": ciscoGtpDirectorConfigurationsGroup,
       "ciscoGtpDirectorStatusGroup": ciscoGtpDirectorStatusGroup,
       "ciscoGtpDirectorStatisticsGroup": ciscoGtpDirectorStatisticsGroup,
       "ciscoGtpDirectorNotifMgmtGroup": ciscoGtpDirectorNotifMgmtGroup,
       "ciscoGtpDirectorNotifGroup": ciscoGtpDirectorNotifGroup}
)
