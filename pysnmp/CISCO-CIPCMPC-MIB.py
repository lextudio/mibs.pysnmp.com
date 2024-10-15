# SNMP MIB module (CISCO-CIPCMPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CIPCMPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:26 2024
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

(cipCardDtrBrdIndex,
 cipCardEntryIndex,
 cipCardSubChannelIndex) = mibBuilder.importSymbols(
    "CISCO-CHANNEL-MIB",
    "cipCardDtrBrdIndex",
    "cipCardEntryIndex",
    "cipCardSubChannelIndex")

(ChannelDevice,
 ChannelPath) = mibBuilder.importSymbols(
    "CISCO-CIPCSNA-MIB",
    "ChannelDevice",
    "ChannelPath")

(ChannelTgName,) = mibBuilder.importSymbols(
    "CISCO-CIPTG-MIB",
    "ChannelTgName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TDomain,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TDomain",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoCipCmpcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72)
)
ciscoCipCmpcMIB.setRevisions(
        ("1999-01-25 00:00",
         "1998-01-06 00:00",
         "1997-02-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CipCmpcObjects_ObjectIdentity = ObjectIdentity
cipCmpcObjects = _CipCmpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1)
)
_CipCmpcSubChannel_ObjectIdentity = ObjectIdentity
cipCmpcSubChannel = _CipCmpcSubChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1)
)
_CipCmpcSubChannelAdminTable_Object = MibTable
cipCmpcSubChannelAdminTable = _CipCmpcSubChannelAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminTable.setStatus("current")
_CipCmpcSubChannelAdminEntry_Object = MibTableRow
cipCmpcSubChannelAdminEntry = _CipCmpcSubChannelAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1, 1)
)
cipCmpcSubChannelAdminEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
)
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminEntry.setStatus("current")
_CipCmpcSubChannelAdminPath_Type = ChannelPath
_CipCmpcSubChannelAdminPath_Object = MibTableColumn
cipCmpcSubChannelAdminPath = _CipCmpcSubChannelAdminPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1, 1, 1),
    _CipCmpcSubChannelAdminPath_Type()
)
cipCmpcSubChannelAdminPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminPath.setStatus("current")
_CipCmpcSubChannelAdminDevice_Type = ChannelDevice
_CipCmpcSubChannelAdminDevice_Object = MibTableColumn
cipCmpcSubChannelAdminDevice = _CipCmpcSubChannelAdminDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1, 1, 2),
    _CipCmpcSubChannelAdminDevice_Type()
)
cipCmpcSubChannelAdminDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminDevice.setStatus("current")
_CipCmpcSubChannelAdminTgName_Type = ChannelTgName
_CipCmpcSubChannelAdminTgName_Object = MibTableColumn
cipCmpcSubChannelAdminTgName = _CipCmpcSubChannelAdminTgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1, 1, 3),
    _CipCmpcSubChannelAdminTgName_Type()
)
cipCmpcSubChannelAdminTgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminTgName.setStatus("current")


class _CipCmpcSubChannelAdminDirection_Type(Integer32):
    """Custom type cipCmpcSubChannelAdminDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readOrWrite", 3),
          ("write", 2))
    )


_CipCmpcSubChannelAdminDirection_Type.__name__ = "Integer32"
_CipCmpcSubChannelAdminDirection_Object = MibTableColumn
cipCmpcSubChannelAdminDirection = _CipCmpcSubChannelAdminDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1, 1, 4),
    _CipCmpcSubChannelAdminDirection_Type()
)
cipCmpcSubChannelAdminDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminDirection.setStatus("current")
_CipCmpcSubChannelAdminTgTransport_Type = TDomain
_CipCmpcSubChannelAdminTgTransport_Object = MibTableColumn
cipCmpcSubChannelAdminTgTransport = _CipCmpcSubChannelAdminTgTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1, 1, 5),
    _CipCmpcSubChannelAdminTgTransport_Type()
)
cipCmpcSubChannelAdminTgTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminTgTransport.setStatus("current")
_CipCmpcSubChannelAdminRowStatus_Type = RowStatus
_CipCmpcSubChannelAdminRowStatus_Object = MibTableColumn
cipCmpcSubChannelAdminRowStatus = _CipCmpcSubChannelAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 1, 1, 6),
    _CipCmpcSubChannelAdminRowStatus_Type()
)
cipCmpcSubChannelAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCmpcSubChannelAdminRowStatus.setStatus("current")
_CipCmpcSubChannelOperTable_Object = MibTable
cipCmpcSubChannelOperTable = _CipCmpcSubChannelOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cipCmpcSubChannelOperTable.setStatus("current")
_CipCmpcSubChannelOperEntry_Object = MibTableRow
cipCmpcSubChannelOperEntry = _CipCmpcSubChannelOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipCmpcSubChannelOperEntry.setStatus("current")


class _CipCmpcSubChannelOperState_Type(Integer32):
    """Custom type cipCmpcSubChannelOperState based on Integer32"""
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
        *(("active", 4),
          ("activePlus", 5),
          ("inactive", 2),
          ("shutdown", 1),
          ("xid2Pending", 3))
    )


_CipCmpcSubChannelOperState_Type.__name__ = "Integer32"
_CipCmpcSubChannelOperState_Object = MibTableColumn
cipCmpcSubChannelOperState = _CipCmpcSubChannelOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 2, 1, 1),
    _CipCmpcSubChannelOperState_Type()
)
cipCmpcSubChannelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcSubChannelOperState.setStatus("current")
_CipCmpcSubChannelOperMaxbfru_Type = Integer32
_CipCmpcSubChannelOperMaxbfru_Object = MibTableColumn
cipCmpcSubChannelOperMaxbfru = _CipCmpcSubChannelOperMaxbfru_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 1, 2, 1, 2),
    _CipCmpcSubChannelOperMaxbfru_Type()
)
cipCmpcSubChannelOperMaxbfru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcSubChannelOperMaxbfru.setStatus("current")
_CipCmpcTg_ObjectIdentity = ObjectIdentity
cipCmpcTg = _CipCmpcTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2)
)
_CipCmpcTgOperTable_Object = MibTable
cipCmpcTgOperTable = _CipCmpcTgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipCmpcTgOperTable.setStatus("current")
_CipCmpcTgOperEntry_Object = MibTableRow
cipCmpcTgOperEntry = _CipCmpcTgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1, 1)
)
cipCmpcTgOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPCMPC-MIB", "cipCmpcTgOperName"),
)
if mibBuilder.loadTexts:
    cipCmpcTgOperEntry.setStatus("current")
_CipCmpcTgOperName_Type = ChannelTgName
_CipCmpcTgOperName_Object = MibTableColumn
cipCmpcTgOperName = _CipCmpcTgOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1, 1, 1),
    _CipCmpcTgOperName_Type()
)
cipCmpcTgOperName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipCmpcTgOperName.setStatus("current")


class _CipCmpcTgOperLastSeqNumFailureCause_Type(Integer32):
    """Custom type cipCmpcTgOperLastSeqNumFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockSeqError", 2),
          ("none", 1),
          ("sweepSeqError", 3))
    )


_CipCmpcTgOperLastSeqNumFailureCause_Type.__name__ = "Integer32"
_CipCmpcTgOperLastSeqNumFailureCause_Object = MibTableColumn
cipCmpcTgOperLastSeqNumFailureCause = _CipCmpcTgOperLastSeqNumFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1, 1, 2),
    _CipCmpcTgOperLastSeqNumFailureCause_Type()
)
cipCmpcTgOperLastSeqNumFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgOperLastSeqNumFailureCause.setStatus("current")
_CipCmpcTgOperLastSeqNumFailureTime_Type = TimeStamp
_CipCmpcTgOperLastSeqNumFailureTime_Object = MibTableColumn
cipCmpcTgOperLastSeqNumFailureTime = _CipCmpcTgOperLastSeqNumFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1, 1, 3),
    _CipCmpcTgOperLastSeqNumFailureTime_Type()
)
cipCmpcTgOperLastSeqNumFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgOperLastSeqNumFailureTime.setStatus("current")
_CipCmpcTgOperExpectedReceiveSeqNum_Type = Integer32
_CipCmpcTgOperExpectedReceiveSeqNum_Object = MibTableColumn
cipCmpcTgOperExpectedReceiveSeqNum = _CipCmpcTgOperExpectedReceiveSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1, 1, 4),
    _CipCmpcTgOperExpectedReceiveSeqNum_Type()
)
cipCmpcTgOperExpectedReceiveSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgOperExpectedReceiveSeqNum.setStatus("current")
_CipCmpcTgOperLastSeqNumReceived_Type = Integer32
_CipCmpcTgOperLastSeqNumReceived_Object = MibTableColumn
cipCmpcTgOperLastSeqNumReceived = _CipCmpcTgOperLastSeqNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1, 1, 5),
    _CipCmpcTgOperLastSeqNumReceived_Type()
)
cipCmpcTgOperLastSeqNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgOperLastSeqNumReceived.setStatus("current")
_CipCmpcTgOperLastSeqNumSent_Type = Integer32
_CipCmpcTgOperLastSeqNumSent_Object = MibTableColumn
cipCmpcTgOperLastSeqNumSent = _CipCmpcTgOperLastSeqNumSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 1, 1, 6),
    _CipCmpcTgOperLastSeqNumSent_Type()
)
cipCmpcTgOperLastSeqNumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgOperLastSeqNumSent.setStatus("current")
_CipCmpcTgStatsTable_Object = MibTable
cipCmpcTgStatsTable = _CipCmpcTgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cipCmpcTgStatsTable.setStatus("current")
_CipCmpcTgStatsEntry_Object = MibTableRow
cipCmpcTgStatsEntry = _CipCmpcTgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cipCmpcTgStatsEntry.setStatus("current")
_CipCmpcTgStatsConnectReqs_Type = Counter32
_CipCmpcTgStatsConnectReqs_Object = MibTableColumn
cipCmpcTgStatsConnectReqs = _CipCmpcTgStatsConnectReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 1),
    _CipCmpcTgStatsConnectReqs_Type()
)
cipCmpcTgStatsConnectReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsConnectReqs.setStatus("current")
_CipCmpcTgStatsConnectInds_Type = Counter32
_CipCmpcTgStatsConnectInds_Object = MibTableColumn
cipCmpcTgStatsConnectInds = _CipCmpcTgStatsConnectInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 2),
    _CipCmpcTgStatsConnectInds_Type()
)
cipCmpcTgStatsConnectInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsConnectInds.setStatus("current")
_CipCmpcTgStatsConnectRsps_Type = Counter32
_CipCmpcTgStatsConnectRsps_Object = MibTableColumn
cipCmpcTgStatsConnectRsps = _CipCmpcTgStatsConnectRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 3),
    _CipCmpcTgStatsConnectRsps_Type()
)
cipCmpcTgStatsConnectRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsConnectRsps.setStatus("current")
_CipCmpcTgStatsConnectCnfms_Type = Counter32
_CipCmpcTgStatsConnectCnfms_Object = MibTableColumn
cipCmpcTgStatsConnectCnfms = _CipCmpcTgStatsConnectCnfms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 4),
    _CipCmpcTgStatsConnectCnfms_Type()
)
cipCmpcTgStatsConnectCnfms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsConnectCnfms.setStatus("current")
_CipCmpcTgStatsDiscReqs_Type = Counter32
_CipCmpcTgStatsDiscReqs_Object = MibTableColumn
cipCmpcTgStatsDiscReqs = _CipCmpcTgStatsDiscReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 5),
    _CipCmpcTgStatsDiscReqs_Type()
)
cipCmpcTgStatsDiscReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsDiscReqs.setStatus("current")
_CipCmpcTgStatsDiscInds_Type = Counter32
_CipCmpcTgStatsDiscInds_Object = MibTableColumn
cipCmpcTgStatsDiscInds = _CipCmpcTgStatsDiscInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 6),
    _CipCmpcTgStatsDiscInds_Type()
)
cipCmpcTgStatsDiscInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsDiscInds.setStatus("current")
_CipCmpcTgStatsSweepReqsIn_Type = Counter32
_CipCmpcTgStatsSweepReqsIn_Object = MibTableColumn
cipCmpcTgStatsSweepReqsIn = _CipCmpcTgStatsSweepReqsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 7),
    _CipCmpcTgStatsSweepReqsIn_Type()
)
cipCmpcTgStatsSweepReqsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsSweepReqsIn.setStatus("current")
_CipCmpcTgStatsSweepReqsOut_Type = Counter32
_CipCmpcTgStatsSweepReqsOut_Object = MibTableColumn
cipCmpcTgStatsSweepReqsOut = _CipCmpcTgStatsSweepReqsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 8),
    _CipCmpcTgStatsSweepReqsOut_Type()
)
cipCmpcTgStatsSweepReqsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsSweepReqsOut.setStatus("current")
_CipCmpcTgStatsSweepRspsIn_Type = Counter32
_CipCmpcTgStatsSweepRspsIn_Object = MibTableColumn
cipCmpcTgStatsSweepRspsIn = _CipCmpcTgStatsSweepRspsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 9),
    _CipCmpcTgStatsSweepRspsIn_Type()
)
cipCmpcTgStatsSweepRspsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsSweepRspsIn.setStatus("current")
_CipCmpcTgStatsSweepRspsOut_Type = Counter32
_CipCmpcTgStatsSweepRspsOut_Object = MibTableColumn
cipCmpcTgStatsSweepRspsOut = _CipCmpcTgStatsSweepRspsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 10),
    _CipCmpcTgStatsSweepRspsOut_Type()
)
cipCmpcTgStatsSweepRspsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsSweepRspsOut.setStatus("current")
_CipCmpcTgStatsWraps_Type = Counter32
_CipCmpcTgStatsWraps_Object = MibTableColumn
cipCmpcTgStatsWraps = _CipCmpcTgStatsWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 1, 2, 2, 1, 11),
    _CipCmpcTgStatsWraps_Type()
)
cipCmpcTgStatsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCmpcTgStatsWraps.setStatus("current")
_CipCmpcNotificationPrefix_ObjectIdentity = ObjectIdentity
cipCmpcNotificationPrefix = _CipCmpcNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 2)
)
_CipCmpcNotifications_ObjectIdentity = ObjectIdentity
cipCmpcNotifications = _CipCmpcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 2, 0)
)
_CiscoCipCmpcMibConformance_ObjectIdentity = ObjectIdentity
ciscoCipCmpcMibConformance = _CiscoCipCmpcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 3)
)
_CiscoCipCmpcMibCompliances_ObjectIdentity = ObjectIdentity
ciscoCipCmpcMibCompliances = _CiscoCipCmpcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 3, 1)
)
_CiscoCipCmpcMibGroups_ObjectIdentity = ObjectIdentity
ciscoCipCmpcMibGroups = _CiscoCipCmpcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 3, 2)
)
cipCmpcSubChannelAdminEntry.registerAugmentions(
    ("CISCO-CIPCMPC-MIB",
     "cipCmpcSubChannelOperEntry")
)
cipCmpcSubChannelOperEntry.setIndexNames(*cipCmpcSubChannelAdminEntry.getIndexNames())
cipCmpcTgOperEntry.registerAugmentions(
    ("CISCO-CIPCMPC-MIB",
     "cipCmpcTgStatsEntry")
)
cipCmpcTgStatsEntry.setIndexNames(*cipCmpcTgOperEntry.getIndexNames())

# Managed Objects groups

ciscoCipCmpcSubChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 3, 2, 1)
)
ciscoCipCmpcSubChannelGroup.setObjects(
      *(("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelAdminPath"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelAdminDevice"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelAdminTgName"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelAdminDirection"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelAdminTgTransport"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelAdminRowStatus"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelOperState"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelOperMaxbfru"))
)
if mibBuilder.loadTexts:
    ciscoCipCmpcSubChannelGroup.setStatus("current")

ciscoCipCmpcTgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 3, 2, 2)
)
ciscoCipCmpcTgGroup.setObjects(
      *(("CISCO-CIPCMPC-MIB", "cipCmpcTgOperLastSeqNumFailureCause"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgOperLastSeqNumFailureTime"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgOperExpectedReceiveSeqNum"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgOperLastSeqNumReceived"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgOperLastSeqNumSent"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsConnectReqs"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsConnectInds"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsConnectRsps"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsConnectCnfms"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsDiscReqs"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsDiscInds"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsSweepReqsIn"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsSweepReqsOut"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsSweepRspsIn"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsSweepRspsOut"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgStatsWraps"))
)
if mibBuilder.loadTexts:
    ciscoCipCmpcTgGroup.setStatus("current")


# Notification objects

cipCmpcDirectionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 2, 0, 1)
)
cipCmpcDirectionMismatch.setObjects(
    ("CISCO-CIPCMPC-MIB", "cipCmpcSubChannelAdminDirection")
)
if mibBuilder.loadTexts:
    cipCmpcDirectionMismatch.setStatus(
        "current"
    )

cipCmpcSeqNumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 2, 0, 2)
)
cipCmpcSeqNumError.setObjects(
      *(("CISCO-CIPCMPC-MIB", "cipCmpcTgOperLastSeqNumFailureCause"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgOperExpectedReceiveSeqNum"),
        ("CISCO-CIPCMPC-MIB", "cipCmpcTgOperLastSeqNumReceived"))
)
if mibBuilder.loadTexts:
    cipCmpcSeqNumError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCipCmpcMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 72, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCipCmpcMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CIPCMPC-MIB",
    **{"ciscoCipCmpcMIB": ciscoCipCmpcMIB,
       "cipCmpcObjects": cipCmpcObjects,
       "cipCmpcSubChannel": cipCmpcSubChannel,
       "cipCmpcSubChannelAdminTable": cipCmpcSubChannelAdminTable,
       "cipCmpcSubChannelAdminEntry": cipCmpcSubChannelAdminEntry,
       "cipCmpcSubChannelAdminPath": cipCmpcSubChannelAdminPath,
       "cipCmpcSubChannelAdminDevice": cipCmpcSubChannelAdminDevice,
       "cipCmpcSubChannelAdminTgName": cipCmpcSubChannelAdminTgName,
       "cipCmpcSubChannelAdminDirection": cipCmpcSubChannelAdminDirection,
       "cipCmpcSubChannelAdminTgTransport": cipCmpcSubChannelAdminTgTransport,
       "cipCmpcSubChannelAdminRowStatus": cipCmpcSubChannelAdminRowStatus,
       "cipCmpcSubChannelOperTable": cipCmpcSubChannelOperTable,
       "cipCmpcSubChannelOperEntry": cipCmpcSubChannelOperEntry,
       "cipCmpcSubChannelOperState": cipCmpcSubChannelOperState,
       "cipCmpcSubChannelOperMaxbfru": cipCmpcSubChannelOperMaxbfru,
       "cipCmpcTg": cipCmpcTg,
       "cipCmpcTgOperTable": cipCmpcTgOperTable,
       "cipCmpcTgOperEntry": cipCmpcTgOperEntry,
       "cipCmpcTgOperName": cipCmpcTgOperName,
       "cipCmpcTgOperLastSeqNumFailureCause": cipCmpcTgOperLastSeqNumFailureCause,
       "cipCmpcTgOperLastSeqNumFailureTime": cipCmpcTgOperLastSeqNumFailureTime,
       "cipCmpcTgOperExpectedReceiveSeqNum": cipCmpcTgOperExpectedReceiveSeqNum,
       "cipCmpcTgOperLastSeqNumReceived": cipCmpcTgOperLastSeqNumReceived,
       "cipCmpcTgOperLastSeqNumSent": cipCmpcTgOperLastSeqNumSent,
       "cipCmpcTgStatsTable": cipCmpcTgStatsTable,
       "cipCmpcTgStatsEntry": cipCmpcTgStatsEntry,
       "cipCmpcTgStatsConnectReqs": cipCmpcTgStatsConnectReqs,
       "cipCmpcTgStatsConnectInds": cipCmpcTgStatsConnectInds,
       "cipCmpcTgStatsConnectRsps": cipCmpcTgStatsConnectRsps,
       "cipCmpcTgStatsConnectCnfms": cipCmpcTgStatsConnectCnfms,
       "cipCmpcTgStatsDiscReqs": cipCmpcTgStatsDiscReqs,
       "cipCmpcTgStatsDiscInds": cipCmpcTgStatsDiscInds,
       "cipCmpcTgStatsSweepReqsIn": cipCmpcTgStatsSweepReqsIn,
       "cipCmpcTgStatsSweepReqsOut": cipCmpcTgStatsSweepReqsOut,
       "cipCmpcTgStatsSweepRspsIn": cipCmpcTgStatsSweepRspsIn,
       "cipCmpcTgStatsSweepRspsOut": cipCmpcTgStatsSweepRspsOut,
       "cipCmpcTgStatsWraps": cipCmpcTgStatsWraps,
       "cipCmpcNotificationPrefix": cipCmpcNotificationPrefix,
       "cipCmpcNotifications": cipCmpcNotifications,
       "cipCmpcDirectionMismatch": cipCmpcDirectionMismatch,
       "cipCmpcSeqNumError": cipCmpcSeqNumError,
       "ciscoCipCmpcMibConformance": ciscoCipCmpcMibConformance,
       "ciscoCipCmpcMibCompliances": ciscoCipCmpcMibCompliances,
       "ciscoCipCmpcMibCompliance": ciscoCipCmpcMibCompliance,
       "ciscoCipCmpcMibGroups": ciscoCipCmpcMibGroups,
       "ciscoCipCmpcSubChannelGroup": ciscoCipCmpcSubChannelGroup,
       "ciscoCipCmpcTgGroup": ciscoCipCmpcTgGroup}
)
