# SNMP MIB module (M2000-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/M2000-V1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:54 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IMAP_ObjectIdentity = ObjectIdentity
iMAP = _IMAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_IMAPNetManagement_ObjectIdentity = ObjectIdentity
iMAPNetManagement = _IMAPNetManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15)
)
_IMAPNorthbound_ObjectIdentity = ObjectIdentity
iMAPNorthbound = _IMAPNorthbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2)
)
_IMAPNorthboundCommon_ObjectIdentity = ObjectIdentity
iMAPNorthboundCommon = _IMAPNorthboundCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1)
)
_IMAPNorthboundEventMgmt_ObjectIdentity = ObjectIdentity
iMAPNorthboundEventMgmt = _IMAPNorthboundEventMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2)
)
_IMAPNorthboundNotificationReport_ObjectIdentity = ObjectIdentity
iMAPNorthboundNotificationReport = _IMAPNorthboundNotificationReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1)
)
_IMAPNorthboundNotificationCommon_ObjectIdentity = ObjectIdentity
iMAPNorthboundNotificationCommon = _IMAPNorthboundNotificationCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1, 1)
)
_IMAPNorthboundHeartbeatNotification_ObjectIdentity = ObjectIdentity
iMAPNorthboundHeartbeatNotification = _IMAPNorthboundHeartbeatNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1, 1, 1)
)
_IMAPNorthboundHeartbeatNotificationV2_ObjectIdentity = ObjectIdentity
iMAPNorthboundHeartbeatNotificationV2 = _IMAPNorthboundHeartbeatNotificationV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1, 1, 1, 0)
)
_IMAPNorthboundHeartbeatSystemLabel_Type = OctetString
_IMAPNorthboundHeartbeatSystemLabel_Object = MibScalar
iMAPNorthboundHeartbeatSystemLabel = _IMAPNorthboundHeartbeatSystemLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1, 1, 1, 1),
    _IMAPNorthboundHeartbeatSystemLabel_Type()
)
iMAPNorthboundHeartbeatSystemLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundHeartbeatSystemLabel.setStatus("mandatory")
_IMAPNorthboundHeartbeatPeriod_Type = Integer32
_IMAPNorthboundHeartbeatPeriod_Object = MibScalar
iMAPNorthboundHeartbeatPeriod = _IMAPNorthboundHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1, 1, 1, 2),
    _IMAPNorthboundHeartbeatPeriod_Type()
)
iMAPNorthboundHeartbeatPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundHeartbeatPeriod.setStatus("mandatory")
_IMAPNorthboundHeartbeatTimeStamp_Type = OctetString
_IMAPNorthboundHeartbeatTimeStamp_Object = MibScalar
iMAPNorthboundHeartbeatTimeStamp = _IMAPNorthboundHeartbeatTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1, 1, 1, 3),
    _IMAPNorthboundHeartbeatTimeStamp_Type()
)
iMAPNorthboundHeartbeatTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundHeartbeatTimeStamp.setStatus("mandatory")
_IMAPNorthboundCommuLinkMonitor_ObjectIdentity = ObjectIdentity
iMAPNorthboundCommuLinkMonitor = _IMAPNorthboundCommuLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 3)
)
_IMAPNorthboundHeartbeatSvc_ObjectIdentity = ObjectIdentity
iMAPNorthboundHeartbeatSvc = _IMAPNorthboundHeartbeatSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 3, 1)
)
_IMAPNorthboundHeartbeatSvcReportInterval_Type = Integer32
_IMAPNorthboundHeartbeatSvcReportInterval_Object = MibScalar
iMAPNorthboundHeartbeatSvcReportInterval = _IMAPNorthboundHeartbeatSvcReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 3, 1, 1),
    _IMAPNorthboundHeartbeatSvcReportInterval_Type()
)
iMAPNorthboundHeartbeatSvcReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iMAPNorthboundHeartbeatSvcReportInterval.setStatus("mandatory")
_IMAPNorthboundFault_ObjectIdentity = ObjectIdentity
iMAPNorthboundFault = _IMAPNorthboundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4)
)
_IMAPNorthboundFaultQuery_ObjectIdentity = ObjectIdentity
iMAPNorthboundFaultQuery = _IMAPNorthboundFaultQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 1)
)
_IMAPNorthboundAlarmQuery_Type = OctetString
_IMAPNorthboundAlarmQuery_Object = MibScalar
iMAPNorthboundAlarmQuery = _IMAPNorthboundAlarmQuery_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 1, 5),
    _IMAPNorthboundAlarmQuery_Type()
)
iMAPNorthboundAlarmQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmQuery.setStatus("mandatory")
_IMAPNorthboundFaultNotification_ObjectIdentity = ObjectIdentity
iMAPNorthboundFaultNotification = _IMAPNorthboundFaultNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3)
)
_IMAPNorthboundFaultAlarmNotification_ObjectIdentity = ObjectIdentity
iMAPNorthboundFaultAlarmNotification = _IMAPNorthboundFaultAlarmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3)
)
_IMAPNorthboundFaultAlarmNotificationV2_ObjectIdentity = ObjectIdentity
iMAPNorthboundFaultAlarmNotificationV2 = _IMAPNorthboundFaultAlarmNotificationV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 0)
)
_IMAPNorthboundAlarmCSN_Type = OctetString
_IMAPNorthboundAlarmCSN_Object = MibScalar
iMAPNorthboundAlarmCSN = _IMAPNorthboundAlarmCSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 1),
    _IMAPNorthboundAlarmCSN_Type()
)
iMAPNorthboundAlarmCSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmCSN.setStatus("mandatory")
_IMAPNorthboundAlarmCategory_Type = OctetString
_IMAPNorthboundAlarmCategory_Object = MibScalar
iMAPNorthboundAlarmCategory = _IMAPNorthboundAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 2),
    _IMAPNorthboundAlarmCategory_Type()
)
iMAPNorthboundAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmCategory.setStatus("mandatory")
_IMAPNorthboundAlarmOccurTime_Type = OctetString
_IMAPNorthboundAlarmOccurTime_Object = MibScalar
iMAPNorthboundAlarmOccurTime = _IMAPNorthboundAlarmOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 3),
    _IMAPNorthboundAlarmOccurTime_Type()
)
iMAPNorthboundAlarmOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmOccurTime.setStatus("mandatory")
_IMAPNorthboundAlarmMOName_Type = OctetString
_IMAPNorthboundAlarmMOName_Object = MibScalar
iMAPNorthboundAlarmMOName = _IMAPNorthboundAlarmMOName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 4),
    _IMAPNorthboundAlarmMOName_Type()
)
iMAPNorthboundAlarmMOName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmMOName.setStatus("mandatory")


class _IMAPNorthboundAlarmProductID_Type(Integer32):
    """Custom type iMAPNorthboundAlarmProductID based on Integer32"""
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
        *(("bandFixedBand", 4),
          ("fixedNetworkNarrow", 3),
          ("intelligence", 5),
          ("mobile", 2),
          ("omc", 6),
          ("transmission", 1))
    )


_IMAPNorthboundAlarmProductID_Type.__name__ = "Integer32"
_IMAPNorthboundAlarmProductID_Object = MibScalar
iMAPNorthboundAlarmProductID = _IMAPNorthboundAlarmProductID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 5),
    _IMAPNorthboundAlarmProductID_Type()
)
iMAPNorthboundAlarmProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmProductID.setStatus("mandatory")
_IMAPNorthboundAlarmNEType_Type = OctetString
_IMAPNorthboundAlarmNEType_Object = MibScalar
iMAPNorthboundAlarmNEType = _IMAPNorthboundAlarmNEType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 6),
    _IMAPNorthboundAlarmNEType_Type()
)
iMAPNorthboundAlarmNEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmNEType.setStatus("mandatory")
_IMAPNorthboundAlarmNEDevID_Type = OctetString
_IMAPNorthboundAlarmNEDevID_Object = MibScalar
iMAPNorthboundAlarmNEDevID = _IMAPNorthboundAlarmNEDevID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 7),
    _IMAPNorthboundAlarmNEDevID_Type()
)
iMAPNorthboundAlarmNEDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmNEDevID.setStatus("mandatory")
_IMAPNorthboundAlarmDevCsn_Type = OctetString
_IMAPNorthboundAlarmDevCsn_Object = MibScalar
iMAPNorthboundAlarmDevCsn = _IMAPNorthboundAlarmDevCsn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 8),
    _IMAPNorthboundAlarmDevCsn_Type()
)
iMAPNorthboundAlarmDevCsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmDevCsn.setStatus("mandatory")
_IMAPNorthboundAlarmID_Type = Integer32
_IMAPNorthboundAlarmID_Object = MibScalar
iMAPNorthboundAlarmID = _IMAPNorthboundAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 9),
    _IMAPNorthboundAlarmID_Type()
)
iMAPNorthboundAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmID.setStatus("mandatory")
_IMAPNorthboundAlarmType_Type = Integer32
_IMAPNorthboundAlarmType_Object = MibScalar
iMAPNorthboundAlarmType = _IMAPNorthboundAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 10),
    _IMAPNorthboundAlarmType_Type()
)
iMAPNorthboundAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmType.setStatus("mandatory")


class _IMAPNorthboundAlarmLevel_Type(Integer32):
    """Custom type iMAPNorthboundAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 6),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_IMAPNorthboundAlarmLevel_Type.__name__ = "Integer32"
_IMAPNorthboundAlarmLevel_Object = MibScalar
iMAPNorthboundAlarmLevel = _IMAPNorthboundAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 11),
    _IMAPNorthboundAlarmLevel_Type()
)
iMAPNorthboundAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmLevel.setStatus("mandatory")


class _IMAPNorthboundAlarmRestore_Type(Integer32):
    """Custom type iMAPNorthboundAlarmRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("uncleared", 2))
    )


_IMAPNorthboundAlarmRestore_Type.__name__ = "Integer32"
_IMAPNorthboundAlarmRestore_Object = MibScalar
iMAPNorthboundAlarmRestore = _IMAPNorthboundAlarmRestore_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 12),
    _IMAPNorthboundAlarmRestore_Type()
)
iMAPNorthboundAlarmRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmRestore.setStatus("mandatory")


class _IMAPNorthboundAlarmConfirm_Type(Integer32):
    """Custom type iMAPNorthboundAlarmConfirm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 1),
          ("unacknowledged", 2))
    )


_IMAPNorthboundAlarmConfirm_Type.__name__ = "Integer32"
_IMAPNorthboundAlarmConfirm_Object = MibScalar
iMAPNorthboundAlarmConfirm = _IMAPNorthboundAlarmConfirm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 13),
    _IMAPNorthboundAlarmConfirm_Type()
)
iMAPNorthboundAlarmConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmConfirm.setStatus("mandatory")
_IMAPNorthboundAlarmAckTime_Type = OctetString
_IMAPNorthboundAlarmAckTime_Object = MibScalar
iMAPNorthboundAlarmAckTime = _IMAPNorthboundAlarmAckTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 14),
    _IMAPNorthboundAlarmAckTime_Type()
)
iMAPNorthboundAlarmAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmAckTime.setStatus("mandatory")
_IMAPNorthboundAlarmRestoreTime_Type = OctetString
_IMAPNorthboundAlarmRestoreTime_Object = MibScalar
iMAPNorthboundAlarmRestoreTime = _IMAPNorthboundAlarmRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 15),
    _IMAPNorthboundAlarmRestoreTime_Type()
)
iMAPNorthboundAlarmRestoreTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmRestoreTime.setStatus("mandatory")
_IMAPNorthboundAlarmOperator_Type = OctetString
_IMAPNorthboundAlarmOperator_Object = MibScalar
iMAPNorthboundAlarmOperator = _IMAPNorthboundAlarmOperator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 16),
    _IMAPNorthboundAlarmOperator_Type()
)
iMAPNorthboundAlarmOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmOperator.setStatus("mandatory")
_IMAPNorthboundAlarmParas1_Type = Integer32
_IMAPNorthboundAlarmParas1_Object = MibScalar
iMAPNorthboundAlarmParas1 = _IMAPNorthboundAlarmParas1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 17),
    _IMAPNorthboundAlarmParas1_Type()
)
iMAPNorthboundAlarmParas1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas1.setStatus("mandatory")
_IMAPNorthboundAlarmParas2_Type = Integer32
_IMAPNorthboundAlarmParas2_Object = MibScalar
iMAPNorthboundAlarmParas2 = _IMAPNorthboundAlarmParas2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 18),
    _IMAPNorthboundAlarmParas2_Type()
)
iMAPNorthboundAlarmParas2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas2.setStatus("mandatory")
_IMAPNorthboundAlarmParas3_Type = Integer32
_IMAPNorthboundAlarmParas3_Object = MibScalar
iMAPNorthboundAlarmParas3 = _IMAPNorthboundAlarmParas3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 19),
    _IMAPNorthboundAlarmParas3_Type()
)
iMAPNorthboundAlarmParas3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas3.setStatus("mandatory")
_IMAPNorthboundAlarmParas4_Type = Integer32
_IMAPNorthboundAlarmParas4_Object = MibScalar
iMAPNorthboundAlarmParas4 = _IMAPNorthboundAlarmParas4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 20),
    _IMAPNorthboundAlarmParas4_Type()
)
iMAPNorthboundAlarmParas4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas4.setStatus("mandatory")
_IMAPNorthboundAlarmParas5_Type = Integer32
_IMAPNorthboundAlarmParas5_Object = MibScalar
iMAPNorthboundAlarmParas5 = _IMAPNorthboundAlarmParas5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 21),
    _IMAPNorthboundAlarmParas5_Type()
)
iMAPNorthboundAlarmParas5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas5.setStatus("mandatory")
_IMAPNorthboundAlarmParas6_Type = Integer32
_IMAPNorthboundAlarmParas6_Object = MibScalar
iMAPNorthboundAlarmParas6 = _IMAPNorthboundAlarmParas6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 22),
    _IMAPNorthboundAlarmParas6_Type()
)
iMAPNorthboundAlarmParas6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas6.setStatus("mandatory")
_IMAPNorthboundAlarmParas7_Type = Integer32
_IMAPNorthboundAlarmParas7_Object = MibScalar
iMAPNorthboundAlarmParas7 = _IMAPNorthboundAlarmParas7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 23),
    _IMAPNorthboundAlarmParas7_Type()
)
iMAPNorthboundAlarmParas7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas7.setStatus("mandatory")
_IMAPNorthboundAlarmParas8_Type = Integer32
_IMAPNorthboundAlarmParas8_Object = MibScalar
iMAPNorthboundAlarmParas8 = _IMAPNorthboundAlarmParas8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 24),
    _IMAPNorthboundAlarmParas8_Type()
)
iMAPNorthboundAlarmParas8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas8.setStatus("mandatory")
_IMAPNorthboundAlarmParas9_Type = Integer32
_IMAPNorthboundAlarmParas9_Object = MibScalar
iMAPNorthboundAlarmParas9 = _IMAPNorthboundAlarmParas9_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 25),
    _IMAPNorthboundAlarmParas9_Type()
)
iMAPNorthboundAlarmParas9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas9.setStatus("mandatory")
_IMAPNorthboundAlarmParas10_Type = Integer32
_IMAPNorthboundAlarmParas10_Object = MibScalar
iMAPNorthboundAlarmParas10 = _IMAPNorthboundAlarmParas10_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 26),
    _IMAPNorthboundAlarmParas10_Type()
)
iMAPNorthboundAlarmParas10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmParas10.setStatus("mandatory")
_IMAPNorthboundAlarmExtendInfo_Type = OctetString
_IMAPNorthboundAlarmExtendInfo_Object = MibScalar
iMAPNorthboundAlarmExtendInfo = _IMAPNorthboundAlarmExtendInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 27),
    _IMAPNorthboundAlarmExtendInfo_Type()
)
iMAPNorthboundAlarmExtendInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmExtendInfo.setStatus("mandatory")
_IMAPNorthboundAlarmProbablecause_Type = OctetString
_IMAPNorthboundAlarmProbablecause_Object = MibScalar
iMAPNorthboundAlarmProbablecause = _IMAPNorthboundAlarmProbablecause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 28),
    _IMAPNorthboundAlarmProbablecause_Type()
)
iMAPNorthboundAlarmProbablecause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmProbablecause.setStatus("mandatory")
_IMAPNorthboundAlarmProposedrepairactions_Type = OctetString
_IMAPNorthboundAlarmProposedrepairactions_Object = MibScalar
iMAPNorthboundAlarmProposedrepairactions = _IMAPNorthboundAlarmProposedrepairactions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 29),
    _IMAPNorthboundAlarmProposedrepairactions_Type()
)
iMAPNorthboundAlarmProposedrepairactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmProposedrepairactions.setStatus("mandatory")
_IMAPNorthboundAlarmSpecificproblems_Type = OctetString
_IMAPNorthboundAlarmSpecificproblems_Object = MibScalar
iMAPNorthboundAlarmSpecificproblems = _IMAPNorthboundAlarmSpecificproblems_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 30),
    _IMAPNorthboundAlarmSpecificproblems_Type()
)
iMAPNorthboundAlarmSpecificproblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmSpecificproblems.setStatus("mandatory")


class _IMAPNorthboundAlarmClearOperator_Type(OctetString):
    """Custom type iMAPNorthboundAlarmClearOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IMAPNorthboundAlarmClearOperator_Type.__name__ = "OctetString"
_IMAPNorthboundAlarmClearOperator_Object = MibScalar
iMAPNorthboundAlarmClearOperator = _IMAPNorthboundAlarmClearOperator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 46),
    _IMAPNorthboundAlarmClearOperator_Type()
)
iMAPNorthboundAlarmClearOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmClearOperator.setStatus("mandatory")
_IMAPNorthboundAlarmObjectInstanceType_Type = OctetString
_IMAPNorthboundAlarmObjectInstanceType_Object = MibScalar
iMAPNorthboundAlarmObjectInstanceType = _IMAPNorthboundAlarmObjectInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 47),
    _IMAPNorthboundAlarmObjectInstanceType_Type()
)
iMAPNorthboundAlarmObjectInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmObjectInstanceType.setStatus("mandatory")
_IMAPNorthboundAlarmClearCategory_Type = OctetString
_IMAPNorthboundAlarmClearCategory_Object = MibScalar
iMAPNorthboundAlarmClearCategory = _IMAPNorthboundAlarmClearCategory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 48),
    _IMAPNorthboundAlarmClearCategory_Type()
)
iMAPNorthboundAlarmClearCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmClearCategory.setStatus("mandatory")
_IMAPNorthboundAlarmClearType_Type = OctetString
_IMAPNorthboundAlarmClearType_Object = MibScalar
iMAPNorthboundAlarmClearType = _IMAPNorthboundAlarmClearType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 49),
    _IMAPNorthboundAlarmClearType_Type()
)
iMAPNorthboundAlarmClearType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmClearType.setStatus("mandatory")
_IMAPNorthboundAlarmServiceAffectFlag_Type = OctetString
_IMAPNorthboundAlarmServiceAffectFlag_Object = MibScalar
iMAPNorthboundAlarmServiceAffectFlag = _IMAPNorthboundAlarmServiceAffectFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 50),
    _IMAPNorthboundAlarmServiceAffectFlag_Type()
)
iMAPNorthboundAlarmServiceAffectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmServiceAffectFlag.setStatus("mandatory")


class _IMAPNorthboundAlarmAdditionalInfo_Type(OctetString):
    """Custom type iMAPNorthboundAlarmAdditionalInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_IMAPNorthboundAlarmAdditionalInfo_Type.__name__ = "OctetString"
_IMAPNorthboundAlarmAdditionalInfo_Object = MibScalar
iMAPNorthboundAlarmAdditionalInfo = _IMAPNorthboundAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 51),
    _IMAPNorthboundAlarmAdditionalInfo_Type()
)
iMAPNorthboundAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmAdditionalInfo.setStatus("mandatory")
_IMAPNorthboundFaultAcknowledge_ObjectIdentity = ObjectIdentity
iMAPNorthboundFaultAcknowledge = _IMAPNorthboundFaultAcknowledge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 4)
)
_IMAPNorthboundAlarmAcknowledge_Type = OctetString
_IMAPNorthboundAlarmAcknowledge_Object = MibScalar
iMAPNorthboundAlarmAcknowledge = _IMAPNorthboundAlarmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 4, 1),
    _IMAPNorthboundAlarmAcknowledge_Type()
)
iMAPNorthboundAlarmAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmAcknowledge.setStatus("mandatory")
_IMAPNorthboundFaultUnAcknowledge_ObjectIdentity = ObjectIdentity
iMAPNorthboundFaultUnAcknowledge = _IMAPNorthboundFaultUnAcknowledge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 5)
)
_IMAPNorthboundAlarmUnAcknowledge_Type = OctetString
_IMAPNorthboundAlarmUnAcknowledge_Object = MibScalar
iMAPNorthboundAlarmUnAcknowledge = _IMAPNorthboundAlarmUnAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 5, 1),
    _IMAPNorthboundAlarmUnAcknowledge_Type()
)
iMAPNorthboundAlarmUnAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmUnAcknowledge.setStatus("mandatory")
_IMAPNorthboundFaultClear_ObjectIdentity = ObjectIdentity
iMAPNorthboundFaultClear = _IMAPNorthboundFaultClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 6)
)
_IMAPNorthboundAlarmClear_Type = OctetString
_IMAPNorthboundAlarmClear_Object = MibScalar
iMAPNorthboundAlarmClear = _IMAPNorthboundAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 6, 1),
    _IMAPNorthboundAlarmClear_Type()
)
iMAPNorthboundAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iMAPNorthboundAlarmClear.setStatus("mandatory")
_IMAPConformance_ObjectIdentity = ObjectIdentity
iMAPConformance = _IMAPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 3)
)
_IMAPGroups_ObjectIdentity = ObjectIdentity
iMAPGroups = _IMAPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 3, 1)
)
_CurrentObjectGroup_ObjectIdentity = ObjectIdentity
currentObjectGroup = _CurrentObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 3, 1, 1)
)
_CurrentNotificationGroup_ObjectIdentity = ObjectIdentity
currentNotificationGroup = _CurrentNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 3, 1, 2)
)
_IMAPCompliances_ObjectIdentity = ObjectIdentity
iMAPCompliances = _IMAPCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 3, 2)
)
_BasicCompliance_ObjectIdentity = ObjectIdentity
basicCompliance = _BasicCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 3, 2, 1)
)

# Managed Objects groups


# Notification objects

iMAPNorthboundHeartbeatNotificationType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 1, 2, 1, 1, 1, 0, 5)
)
iMAPNorthboundHeartbeatNotificationType.setObjects(
      *(("M2000-V1", "iMAPNorthboundHeartbeatSystemLabel"),
        ("M2000-V1", "iMAPNorthboundHeartbeatPeriod"),
        ("M2000-V1", "iMAPNorthboundHeartbeatTimeStamp"))
)
if mibBuilder.loadTexts:
    iMAPNorthboundHeartbeatNotificationType.setStatus(
        ""
    )

iMAPNorthboundFaultAlarmReportNotificationType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 0, 1)
)
iMAPNorthboundFaultAlarmReportNotificationType.setObjects(
      *(("M2000-V1", "iMAPNorthboundAlarmCSN"),
        ("M2000-V1", "iMAPNorthboundAlarmCategory"),
        ("M2000-V1", "iMAPNorthboundAlarmOccurTime"),
        ("M2000-V1", "iMAPNorthboundAlarmMOName"),
        ("M2000-V1", "iMAPNorthboundAlarmProductID"),
        ("M2000-V1", "iMAPNorthboundAlarmNEType"),
        ("M2000-V1", "iMAPNorthboundAlarmNEDevID"),
        ("M2000-V1", "iMAPNorthboundAlarmDevCsn"),
        ("M2000-V1", "iMAPNorthboundAlarmID"),
        ("M2000-V1", "iMAPNorthboundAlarmType"),
        ("M2000-V1", "iMAPNorthboundAlarmLevel"),
        ("M2000-V1", "iMAPNorthboundAlarmRestore"),
        ("M2000-V1", "iMAPNorthboundAlarmConfirm"),
        ("M2000-V1", "iMAPNorthboundAlarmAckTime"),
        ("M2000-V1", "iMAPNorthboundAlarmRestoreTime"),
        ("M2000-V1", "iMAPNorthboundAlarmOperator"),
        ("M2000-V1", "iMAPNorthboundAlarmParas1"),
        ("M2000-V1", "iMAPNorthboundAlarmParas2"),
        ("M2000-V1", "iMAPNorthboundAlarmParas3"),
        ("M2000-V1", "iMAPNorthboundAlarmParas4"),
        ("M2000-V1", "iMAPNorthboundAlarmParas5"),
        ("M2000-V1", "iMAPNorthboundAlarmParas6"),
        ("M2000-V1", "iMAPNorthboundAlarmParas7"),
        ("M2000-V1", "iMAPNorthboundAlarmParas8"),
        ("M2000-V1", "iMAPNorthboundAlarmParas9"),
        ("M2000-V1", "iMAPNorthboundAlarmParas10"),
        ("M2000-V1", "iMAPNorthboundAlarmExtendInfo"),
        ("M2000-V1", "iMAPNorthboundAlarmProbablecause"),
        ("M2000-V1", "iMAPNorthboundAlarmProposedrepairactions"),
        ("M2000-V1", "iMAPNorthboundAlarmSpecificproblems"),
        ("M2000-V1", "iMAPNorthboundAlarmClearOperator"),
        ("M2000-V1", "iMAPNorthboundAlarmAdditionalInfo"),
        ("M2000-V1", "iMAPNorthboundAlarmClearType"),
        ("M2000-V1", "iMAPNorthboundAlarmClearCategory"),
        ("M2000-V1", "iMAPNorthboundAlarmServiceAffectFlag"),
        ("M2000-V1", "iMAPNorthboundAlarmObjectInstanceType"))
)
if mibBuilder.loadTexts:
    iMAPNorthboundFaultAlarmReportNotificationType.setStatus(
        ""
    )

iMAPNorthboundFaultAlarmQueryBeginNotificationType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 0, 2)
)
if mibBuilder.loadTexts:
    iMAPNorthboundFaultAlarmQueryBeginNotificationType.setStatus(
        ""
    )

iMAPNorthboundFaultAlarmQueryNotificationType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 0, 3)
)
iMAPNorthboundFaultAlarmQueryNotificationType.setObjects(
      *(("M2000-V1", "iMAPNorthboundAlarmCSN"),
        ("M2000-V1", "iMAPNorthboundAlarmCategory"),
        ("M2000-V1", "iMAPNorthboundAlarmOccurTime"),
        ("M2000-V1", "iMAPNorthboundAlarmMOName"),
        ("M2000-V1", "iMAPNorthboundAlarmProductID"),
        ("M2000-V1", "iMAPNorthboundAlarmNEType"),
        ("M2000-V1", "iMAPNorthboundAlarmNEDevID"),
        ("M2000-V1", "iMAPNorthboundAlarmDevCsn"),
        ("M2000-V1", "iMAPNorthboundAlarmID"),
        ("M2000-V1", "iMAPNorthboundAlarmType"),
        ("M2000-V1", "iMAPNorthboundAlarmLevel"),
        ("M2000-V1", "iMAPNorthboundAlarmRestore"),
        ("M2000-V1", "iMAPNorthboundAlarmConfirm"),
        ("M2000-V1", "iMAPNorthboundAlarmAckTime"),
        ("M2000-V1", "iMAPNorthboundAlarmRestoreTime"),
        ("M2000-V1", "iMAPNorthboundAlarmOperator"),
        ("M2000-V1", "iMAPNorthboundAlarmParas1"),
        ("M2000-V1", "iMAPNorthboundAlarmParas2"),
        ("M2000-V1", "iMAPNorthboundAlarmParas3"),
        ("M2000-V1", "iMAPNorthboundAlarmParas4"),
        ("M2000-V1", "iMAPNorthboundAlarmParas5"),
        ("M2000-V1", "iMAPNorthboundAlarmParas6"),
        ("M2000-V1", "iMAPNorthboundAlarmParas7"),
        ("M2000-V1", "iMAPNorthboundAlarmParas8"),
        ("M2000-V1", "iMAPNorthboundAlarmParas9"),
        ("M2000-V1", "iMAPNorthboundAlarmParas10"),
        ("M2000-V1", "iMAPNorthboundAlarmExtendInfo"),
        ("M2000-V1", "iMAPNorthboundAlarmProbablecause"),
        ("M2000-V1", "iMAPNorthboundAlarmProposedrepairactions"),
        ("M2000-V1", "iMAPNorthboundAlarmSpecificproblems"),
        ("M2000-V1", "iMAPNorthboundAlarmClearOperator"),
        ("M2000-V1", "iMAPNorthboundAlarmAdditionalInfo"),
        ("M2000-V1", "iMAPNorthboundAlarmServiceAffectFlag"),
        ("M2000-V1", "iMAPNorthboundAlarmClearType"),
        ("M2000-V1", "iMAPNorthboundAlarmClearCategory"),
        ("M2000-V1", "iMAPNorthboundAlarmObjectInstanceType"))
)
if mibBuilder.loadTexts:
    iMAPNorthboundFaultAlarmQueryNotificationType.setStatus(
        ""
    )

iMAPNorthboundFaultAlarmQueryEndNotificationType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 2, 4, 3, 3, 0, 4)
)
if mibBuilder.loadTexts:
    iMAPNorthboundFaultAlarmQueryEndNotificationType.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "M2000-V1",
    **{"iMAP": iMAP,
       "products": products,
       "iMAPNetManagement": iMAPNetManagement,
       "iMAPNorthbound": iMAPNorthbound,
       "iMAPNorthboundCommon": iMAPNorthboundCommon,
       "iMAPNorthboundEventMgmt": iMAPNorthboundEventMgmt,
       "iMAPNorthboundNotificationReport": iMAPNorthboundNotificationReport,
       "iMAPNorthboundNotificationCommon": iMAPNorthboundNotificationCommon,
       "iMAPNorthboundHeartbeatNotification": iMAPNorthboundHeartbeatNotification,
       "iMAPNorthboundHeartbeatNotificationV2": iMAPNorthboundHeartbeatNotificationV2,
       "iMAPNorthboundHeartbeatNotificationType": iMAPNorthboundHeartbeatNotificationType,
       "iMAPNorthboundHeartbeatSystemLabel": iMAPNorthboundHeartbeatSystemLabel,
       "iMAPNorthboundHeartbeatPeriod": iMAPNorthboundHeartbeatPeriod,
       "iMAPNorthboundHeartbeatTimeStamp": iMAPNorthboundHeartbeatTimeStamp,
       "iMAPNorthboundCommuLinkMonitor": iMAPNorthboundCommuLinkMonitor,
       "iMAPNorthboundHeartbeatSvc": iMAPNorthboundHeartbeatSvc,
       "iMAPNorthboundHeartbeatSvcReportInterval": iMAPNorthboundHeartbeatSvcReportInterval,
       "iMAPNorthboundFault": iMAPNorthboundFault,
       "iMAPNorthboundFaultQuery": iMAPNorthboundFaultQuery,
       "iMAPNorthboundAlarmQuery": iMAPNorthboundAlarmQuery,
       "iMAPNorthboundFaultNotification": iMAPNorthboundFaultNotification,
       "iMAPNorthboundFaultAlarmNotification": iMAPNorthboundFaultAlarmNotification,
       "iMAPNorthboundFaultAlarmNotificationV2": iMAPNorthboundFaultAlarmNotificationV2,
       "iMAPNorthboundFaultAlarmReportNotificationType": iMAPNorthboundFaultAlarmReportNotificationType,
       "iMAPNorthboundFaultAlarmQueryBeginNotificationType": iMAPNorthboundFaultAlarmQueryBeginNotificationType,
       "iMAPNorthboundFaultAlarmQueryNotificationType": iMAPNorthboundFaultAlarmQueryNotificationType,
       "iMAPNorthboundFaultAlarmQueryEndNotificationType": iMAPNorthboundFaultAlarmQueryEndNotificationType,
       "iMAPNorthboundAlarmCSN": iMAPNorthboundAlarmCSN,
       "iMAPNorthboundAlarmCategory": iMAPNorthboundAlarmCategory,
       "iMAPNorthboundAlarmOccurTime": iMAPNorthboundAlarmOccurTime,
       "iMAPNorthboundAlarmMOName": iMAPNorthboundAlarmMOName,
       "iMAPNorthboundAlarmProductID": iMAPNorthboundAlarmProductID,
       "iMAPNorthboundAlarmNEType": iMAPNorthboundAlarmNEType,
       "iMAPNorthboundAlarmNEDevID": iMAPNorthboundAlarmNEDevID,
       "iMAPNorthboundAlarmDevCsn": iMAPNorthboundAlarmDevCsn,
       "iMAPNorthboundAlarmID": iMAPNorthboundAlarmID,
       "iMAPNorthboundAlarmType": iMAPNorthboundAlarmType,
       "iMAPNorthboundAlarmLevel": iMAPNorthboundAlarmLevel,
       "iMAPNorthboundAlarmRestore": iMAPNorthboundAlarmRestore,
       "iMAPNorthboundAlarmConfirm": iMAPNorthboundAlarmConfirm,
       "iMAPNorthboundAlarmAckTime": iMAPNorthboundAlarmAckTime,
       "iMAPNorthboundAlarmRestoreTime": iMAPNorthboundAlarmRestoreTime,
       "iMAPNorthboundAlarmOperator": iMAPNorthboundAlarmOperator,
       "iMAPNorthboundAlarmParas1": iMAPNorthboundAlarmParas1,
       "iMAPNorthboundAlarmParas2": iMAPNorthboundAlarmParas2,
       "iMAPNorthboundAlarmParas3": iMAPNorthboundAlarmParas3,
       "iMAPNorthboundAlarmParas4": iMAPNorthboundAlarmParas4,
       "iMAPNorthboundAlarmParas5": iMAPNorthboundAlarmParas5,
       "iMAPNorthboundAlarmParas6": iMAPNorthboundAlarmParas6,
       "iMAPNorthboundAlarmParas7": iMAPNorthboundAlarmParas7,
       "iMAPNorthboundAlarmParas8": iMAPNorthboundAlarmParas8,
       "iMAPNorthboundAlarmParas9": iMAPNorthboundAlarmParas9,
       "iMAPNorthboundAlarmParas10": iMAPNorthboundAlarmParas10,
       "iMAPNorthboundAlarmExtendInfo": iMAPNorthboundAlarmExtendInfo,
       "iMAPNorthboundAlarmProbablecause": iMAPNorthboundAlarmProbablecause,
       "iMAPNorthboundAlarmProposedrepairactions": iMAPNorthboundAlarmProposedrepairactions,
       "iMAPNorthboundAlarmSpecificproblems": iMAPNorthboundAlarmSpecificproblems,
       "iMAPNorthboundAlarmClearOperator": iMAPNorthboundAlarmClearOperator,
       "iMAPNorthboundAlarmObjectInstanceType": iMAPNorthboundAlarmObjectInstanceType,
       "iMAPNorthboundAlarmClearCategory": iMAPNorthboundAlarmClearCategory,
       "iMAPNorthboundAlarmClearType": iMAPNorthboundAlarmClearType,
       "iMAPNorthboundAlarmServiceAffectFlag": iMAPNorthboundAlarmServiceAffectFlag,
       "iMAPNorthboundAlarmAdditionalInfo": iMAPNorthboundAlarmAdditionalInfo,
       "iMAPNorthboundFaultAcknowledge": iMAPNorthboundFaultAcknowledge,
       "iMAPNorthboundAlarmAcknowledge": iMAPNorthboundAlarmAcknowledge,
       "iMAPNorthboundFaultUnAcknowledge": iMAPNorthboundFaultUnAcknowledge,
       "iMAPNorthboundAlarmUnAcknowledge": iMAPNorthboundAlarmUnAcknowledge,
       "iMAPNorthboundFaultClear": iMAPNorthboundFaultClear,
       "iMAPNorthboundAlarmClear": iMAPNorthboundAlarmClear,
       "iMAPConformance": iMAPConformance,
       "iMAPGroups": iMAPGroups,
       "currentObjectGroup": currentObjectGroup,
       "currentNotificationGroup": currentNotificationGroup,
       "iMAPCompliances": iMAPCompliances,
       "basicCompliance": basicCompliance}
)
