# SNMP MIB module (CISCO-CSG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CSG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:51 2024
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

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoCsgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331)
)
ciscoCsgMIB.setRevisions(
        ("2003-02-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CsgSlotNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class CsgEntityName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )



class CsgServerPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )



class CsgUserTableUpperBound(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCsgMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCsgMIBNotifs = _CiscoCsgMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 0)
)
_CiscoCsgMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCsgMIBObjects = _CiscoCsgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1)
)
_CsgScalars_ObjectIdentity = ObjectIdentity
csgScalars = _CsgScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 1)
)


class _CsgAgentLostRecordTimer_Type(TimeInterval):
    """Custom type csgAgentLostRecordTimer based on TimeInterval"""
    defaultValue = 60


_CsgAgentLostRecordTimer_Object = MibScalar
csgAgentLostRecordTimer = _CsgAgentLostRecordTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 1, 1),
    _CsgAgentLostRecordTimer_Type()
)
csgAgentLostRecordTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csgAgentLostRecordTimer.setStatus("current")


class _CsgQuotaMgrLostRecordTimer_Type(TimeInterval):
    """Custom type csgQuotaMgrLostRecordTimer based on TimeInterval"""
    defaultValue = 60


_CsgQuotaMgrLostRecordTimer_Object = MibScalar
csgQuotaMgrLostRecordTimer = _CsgQuotaMgrLostRecordTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 1, 2),
    _CsgQuotaMgrLostRecordTimer_Type()
)
csgQuotaMgrLostRecordTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csgQuotaMgrLostRecordTimer.setStatus("current")
_CsgUserStats_ObjectIdentity = ObjectIdentity
csgUserStats = _CsgUserStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2)
)
_CsgUserTable_Object = MibTable
csgUserTable = _CsgUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csgUserTable.setStatus("current")
_CsgUserTableEntry_Object = MibTableRow
csgUserTableEntry = _CsgUserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1)
)
csgUserTableEntry.setIndexNames(
    (0, "CISCO-CSG-MIB", "csgUserCardId"),
    (0, "CISCO-CSG-MIB", "csgUserGroupName"),
)
if mibBuilder.loadTexts:
    csgUserTableEntry.setStatus("current")
_CsgUserCardId_Type = CsgSlotNumber
_CsgUserCardId_Object = MibTableColumn
csgUserCardId = _CsgUserCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 1),
    _CsgUserCardId_Type()
)
csgUserCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgUserCardId.setStatus("current")
_CsgUserGroupName_Type = CsgEntityName
_CsgUserGroupName_Object = MibTableColumn
csgUserGroupName = _CsgUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 2),
    _CsgUserGroupName_Type()
)
csgUserGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgUserGroupName.setStatus("current")
_CsgUserMaxEntries_Type = CsgUserTableUpperBound
_CsgUserMaxEntries_Object = MibTableColumn
csgUserMaxEntries = _CsgUserMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 3),
    _CsgUserMaxEntries_Type()
)
csgUserMaxEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgUserMaxEntries.setStatus("current")
_CsgUserCurrEntries_Type = Gauge32
_CsgUserCurrEntries_Object = MibTableColumn
csgUserCurrEntries = _CsgUserCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 4),
    _CsgUserCurrEntries_Type()
)
csgUserCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserCurrEntries.setStatus("current")


class _CsgUserHighWater_Type(CsgUserTableUpperBound):
    """Custom type csgUserHighWater based on CsgUserTableUpperBound"""
    defaultValue = 0


_CsgUserHighWater_Object = MibTableColumn
csgUserHighWater = _CsgUserHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 5),
    _CsgUserHighWater_Type()
)
csgUserHighWater.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgUserHighWater.setStatus("current")
_CsgUserLRUSteals_Type = Counter32
_CsgUserLRUSteals_Object = MibTableColumn
csgUserLRUSteals = _CsgUserLRUSteals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 6),
    _CsgUserLRUSteals_Type()
)
csgUserLRUSteals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserLRUSteals.setStatus("current")
_CsgUserRowStatus_Type = RowStatus
_CsgUserRowStatus_Object = MibTableColumn
csgUserRowStatus = _CsgUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 7),
    _CsgUserRowStatus_Type()
)
csgUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgUserRowStatus.setStatus("current")
_CsgUserDataBaseStats_ObjectIdentity = ObjectIdentity
csgUserDataBaseStats = _CsgUserDataBaseStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3)
)
_CsgUserDbTable_Object = MibTable
csgUserDbTable = _CsgUserDbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1)
)
if mibBuilder.loadTexts:
    csgUserDbTable.setStatus("current")
_CsgUserDbTableEntry_Object = MibTableRow
csgUserDbTableEntry = _CsgUserDbTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1)
)
csgUserDbTableEntry.setIndexNames(
    (0, "CISCO-CSG-MIB", "csgUserCardId"),
    (0, "CISCO-CSG-MIB", "csgUserGroupName"),
    (0, "CISCO-CSG-MIB", "csgUserDbIpAddrType"),
    (0, "CISCO-CSG-MIB", "csgUserDbIpAddr"),
    (0, "CISCO-CSG-MIB", "csgUserDbPort"),
)
if mibBuilder.loadTexts:
    csgUserDbTableEntry.setStatus("current")
_CsgUserDbIpAddrType_Type = InetAddressType
_CsgUserDbIpAddrType_Object = MibTableColumn
csgUserDbIpAddrType = _CsgUserDbIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 1),
    _CsgUserDbIpAddrType_Type()
)
csgUserDbIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgUserDbIpAddrType.setStatus("current")
_CsgUserDbIpAddr_Type = InetAddress
_CsgUserDbIpAddr_Object = MibTableColumn
csgUserDbIpAddr = _CsgUserDbIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 2),
    _CsgUserDbIpAddr_Type()
)
csgUserDbIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgUserDbIpAddr.setStatus("current")
_CsgUserDbPort_Type = InetPortNumber
_CsgUserDbPort_Object = MibTableColumn
csgUserDbPort = _CsgUserDbPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 3),
    _CsgUserDbPort_Type()
)
csgUserDbPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgUserDbPort.setStatus("current")


class _CsgUserDbState_Type(Integer32):
    """Custom type csgUserDbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("failed", 3),
          ("reset", 1))
    )


_CsgUserDbState_Type.__name__ = "Integer32"
_CsgUserDbState_Object = MibTableColumn
csgUserDbState = _CsgUserDbState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 4),
    _CsgUserDbState_Type()
)
csgUserDbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserDbState.setStatus("current")
_CsgUserDbRequests_Type = Counter64
_CsgUserDbRequests_Object = MibTableColumn
csgUserDbRequests = _CsgUserDbRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 5),
    _CsgUserDbRequests_Type()
)
csgUserDbRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserDbRequests.setStatus("current")
_CsgUserDbUidsReturned_Type = Counter64
_CsgUserDbUidsReturned_Object = MibTableColumn
csgUserDbUidsReturned = _CsgUserDbUidsReturned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 6),
    _CsgUserDbUidsReturned_Type()
)
csgUserDbUidsReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserDbUidsReturned.setStatus("current")
_CsgUserDbReqResent_Type = Counter32
_CsgUserDbReqResent_Object = MibTableColumn
csgUserDbReqResent = _CsgUserDbReqResent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 7),
    _CsgUserDbReqResent_Type()
)
csgUserDbReqResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserDbReqResent.setStatus("current")
_CsgUserDbReqTimeouts_Type = Counter32
_CsgUserDbReqTimeouts_Object = MibTableColumn
csgUserDbReqTimeouts = _CsgUserDbReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 8),
    _CsgUserDbReqTimeouts_Type()
)
csgUserDbReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserDbReqTimeouts.setStatus("current")
_CsgUserDbReqErrors_Type = Counter32
_CsgUserDbReqErrors_Object = MibTableColumn
csgUserDbReqErrors = _CsgUserDbReqErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 9),
    _CsgUserDbReqErrors_Type()
)
csgUserDbReqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgUserDbReqErrors.setStatus("current")
_CsgUserDbRowStatus_Type = RowStatus
_CsgUserDbRowStatus_Object = MibTableColumn
csgUserDbRowStatus = _CsgUserDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 10),
    _CsgUserDbRowStatus_Type()
)
csgUserDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgUserDbRowStatus.setStatus("current")
_CsgAgentStats_ObjectIdentity = ObjectIdentity
csgAgentStats = _CsgAgentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4)
)
_CsgAgentTable_Object = MibTable
csgAgentTable = _CsgAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1)
)
if mibBuilder.loadTexts:
    csgAgentTable.setStatus("current")
_CsgAgentTableEntry_Object = MibTableRow
csgAgentTableEntry = _CsgAgentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1)
)
csgAgentTableEntry.setIndexNames(
    (0, "CISCO-CSG-MIB", "csgUserCardId"),
    (0, "CISCO-CSG-MIB", "csgAgentIpAddrType"),
    (0, "CISCO-CSG-MIB", "csgAgentIpAddr"),
    (0, "CISCO-CSG-MIB", "csgAgentPort"),
)
if mibBuilder.loadTexts:
    csgAgentTableEntry.setStatus("current")
_CsgAgentIpAddrType_Type = InetAddressType
_CsgAgentIpAddrType_Object = MibTableColumn
csgAgentIpAddrType = _CsgAgentIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 1),
    _CsgAgentIpAddrType_Type()
)
csgAgentIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgAgentIpAddrType.setStatus("current")
_CsgAgentIpAddr_Type = InetAddress
_CsgAgentIpAddr_Object = MibTableColumn
csgAgentIpAddr = _CsgAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 2),
    _CsgAgentIpAddr_Type()
)
csgAgentIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgAgentIpAddr.setStatus("current")
_CsgAgentPort_Type = InetPortNumber
_CsgAgentPort_Object = MibTableColumn
csgAgentPort = _CsgAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 3),
    _CsgAgentPort_Type()
)
csgAgentPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgAgentPort.setStatus("current")
_CsgAgentAcctName_Type = CsgEntityName
_CsgAgentAcctName_Object = MibTableColumn
csgAgentAcctName = _CsgAgentAcctName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 4),
    _CsgAgentAcctName_Type()
)
csgAgentAcctName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgAgentAcctName.setStatus("current")
_CsgAgentPriority_Type = CsgServerPriority
_CsgAgentPriority_Object = MibTableColumn
csgAgentPriority = _CsgAgentPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 5),
    _CsgAgentPriority_Type()
)
csgAgentPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgAgentPriority.setStatus("current")


class _CsgAgentState_Type(Integer32):
    """Custom type csgAgentState based on Integer32"""
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
        *(("active", 3),
          ("echowait", 4),
          ("failed", 2),
          ("nawait", 5),
          ("standby", 1),
          ("suspended", 6))
    )


_CsgAgentState_Type.__name__ = "Integer32"
_CsgAgentState_Object = MibTableColumn
csgAgentState = _CsgAgentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 6),
    _CsgAgentState_Type()
)
csgAgentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgAgentState.setStatus("current")
_CsgAgentLostRecords_Type = Counter32
_CsgAgentLostRecords_Object = MibTableColumn
csgAgentLostRecords = _CsgAgentLostRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 7),
    _CsgAgentLostRecords_Type()
)
csgAgentLostRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgAgentLostRecords.setStatus("current")
_CsgAgentTotalSent_Type = Counter64
_CsgAgentTotalSent_Object = MibTableColumn
csgAgentTotalSent = _CsgAgentTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 8),
    _CsgAgentTotalSent_Type()
)
csgAgentTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgAgentTotalSent.setStatus("current")
_CsgAgentFailAck_Type = Counter32
_CsgAgentFailAck_Object = MibTableColumn
csgAgentFailAck = _CsgAgentFailAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 9),
    _CsgAgentFailAck_Type()
)
csgAgentFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgAgentFailAck.setStatus("current")
_CsgAgentOutstanding_Type = Gauge32
_CsgAgentOutstanding_Object = MibTableColumn
csgAgentOutstanding = _CsgAgentOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 10),
    _CsgAgentOutstanding_Type()
)
csgAgentOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgAgentOutstanding.setStatus("current")


class _CsgAgentHighWater_Type(Unsigned32):
    """Custom type csgAgentHighWater based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsgAgentHighWater_Type.__name__ = "Unsigned32"
_CsgAgentHighWater_Object = MibTableColumn
csgAgentHighWater = _CsgAgentHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 11),
    _CsgAgentHighWater_Type()
)
csgAgentHighWater.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgAgentHighWater.setStatus("current")
_CsgAgentBadRecord_Type = Counter32
_CsgAgentBadRecord_Object = MibTableColumn
csgAgentBadRecord = _CsgAgentBadRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 12),
    _CsgAgentBadRecord_Type()
)
csgAgentBadRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgAgentBadRecord.setStatus("current")
_CsgAgentRetransmit_Type = Counter32
_CsgAgentRetransmit_Object = MibTableColumn
csgAgentRetransmit = _CsgAgentRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 13),
    _CsgAgentRetransmit_Type()
)
csgAgentRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgAgentRetransmit.setStatus("current")
_CsgAgentRowStatus_Type = RowStatus
_CsgAgentRowStatus_Object = MibTableColumn
csgAgentRowStatus = _CsgAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 14),
    _CsgAgentRowStatus_Type()
)
csgAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgAgentRowStatus.setStatus("current")
_CsgQuotaMgrStats_ObjectIdentity = ObjectIdentity
csgQuotaMgrStats = _CsgQuotaMgrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5)
)
_CsgQuotaMgrTable_Object = MibTable
csgQuotaMgrTable = _CsgQuotaMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1)
)
if mibBuilder.loadTexts:
    csgQuotaMgrTable.setStatus("current")
_CsgQuotaMgrTableEntry_Object = MibTableRow
csgQuotaMgrTableEntry = _CsgQuotaMgrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1)
)
csgQuotaMgrTableEntry.setIndexNames(
    (0, "CISCO-CSG-MIB", "csgUserCardId"),
    (0, "CISCO-CSG-MIB", "csgQuotaMgrIpAddrType"),
    (0, "CISCO-CSG-MIB", "csgQuotaMgrIpAddr"),
    (0, "CISCO-CSG-MIB", "csgQuotaMgrPort"),
)
if mibBuilder.loadTexts:
    csgQuotaMgrTableEntry.setStatus("current")
_CsgQuotaMgrIpAddrType_Type = InetAddressType
_CsgQuotaMgrIpAddrType_Object = MibTableColumn
csgQuotaMgrIpAddrType = _CsgQuotaMgrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 1),
    _CsgQuotaMgrIpAddrType_Type()
)
csgQuotaMgrIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgQuotaMgrIpAddrType.setStatus("current")
_CsgQuotaMgrIpAddr_Type = InetAddress
_CsgQuotaMgrIpAddr_Object = MibTableColumn
csgQuotaMgrIpAddr = _CsgQuotaMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 2),
    _CsgQuotaMgrIpAddr_Type()
)
csgQuotaMgrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgQuotaMgrIpAddr.setStatus("current")
_CsgQuotaMgrPort_Type = InetPortNumber
_CsgQuotaMgrPort_Object = MibTableColumn
csgQuotaMgrPort = _CsgQuotaMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 3),
    _CsgQuotaMgrPort_Type()
)
csgQuotaMgrPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csgQuotaMgrPort.setStatus("current")
_CsgQuotaMgrUserGroupName_Type = CsgEntityName
_CsgQuotaMgrUserGroupName_Object = MibTableColumn
csgQuotaMgrUserGroupName = _CsgQuotaMgrUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 4),
    _CsgQuotaMgrUserGroupName_Type()
)
csgQuotaMgrUserGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrUserGroupName.setStatus("current")
_CsgQuotaMgrPriority_Type = CsgServerPriority
_CsgQuotaMgrPriority_Object = MibTableColumn
csgQuotaMgrPriority = _CsgQuotaMgrPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 5),
    _CsgQuotaMgrPriority_Type()
)
csgQuotaMgrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgQuotaMgrPriority.setStatus("current")


class _CsgQuotaMgrState_Type(Integer32):
    """Custom type csgQuotaMgrState based on Integer32"""
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
        *(("active", 3),
          ("echowait", 4),
          ("failed", 2),
          ("nawait", 5),
          ("standby", 1),
          ("suspended", 6))
    )


_CsgQuotaMgrState_Type.__name__ = "Integer32"
_CsgQuotaMgrState_Object = MibTableColumn
csgQuotaMgrState = _CsgQuotaMgrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 6),
    _CsgQuotaMgrState_Type()
)
csgQuotaMgrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrState.setStatus("current")
_CsgQuotaMgrLostRecords_Type = Counter32
_CsgQuotaMgrLostRecords_Object = MibTableColumn
csgQuotaMgrLostRecords = _CsgQuotaMgrLostRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 7),
    _CsgQuotaMgrLostRecords_Type()
)
csgQuotaMgrLostRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrLostRecords.setStatus("current")
_CsgQuotaMgrTotalSent_Type = Counter64
_CsgQuotaMgrTotalSent_Object = MibTableColumn
csgQuotaMgrTotalSent = _CsgQuotaMgrTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 8),
    _CsgQuotaMgrTotalSent_Type()
)
csgQuotaMgrTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrTotalSent.setStatus("current")
_CsgQuotaMgrFailAck_Type = Counter32
_CsgQuotaMgrFailAck_Object = MibTableColumn
csgQuotaMgrFailAck = _CsgQuotaMgrFailAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 9),
    _CsgQuotaMgrFailAck_Type()
)
csgQuotaMgrFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrFailAck.setStatus("current")
_CsgQuotaMgrOutstanding_Type = Gauge32
_CsgQuotaMgrOutstanding_Object = MibTableColumn
csgQuotaMgrOutstanding = _CsgQuotaMgrOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 10),
    _CsgQuotaMgrOutstanding_Type()
)
csgQuotaMgrOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrOutstanding.setStatus("current")


class _CsgQuotaMgrHighWater_Type(Unsigned32):
    """Custom type csgQuotaMgrHighWater based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsgQuotaMgrHighWater_Type.__name__ = "Unsigned32"
_CsgQuotaMgrHighWater_Object = MibTableColumn
csgQuotaMgrHighWater = _CsgQuotaMgrHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 11),
    _CsgQuotaMgrHighWater_Type()
)
csgQuotaMgrHighWater.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgQuotaMgrHighWater.setStatus("current")
_CsgQuotaMgrBadRecord_Type = Counter32
_CsgQuotaMgrBadRecord_Object = MibTableColumn
csgQuotaMgrBadRecord = _CsgQuotaMgrBadRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 12),
    _CsgQuotaMgrBadRecord_Type()
)
csgQuotaMgrBadRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrBadRecord.setStatus("current")
_CsgQuotaMgrRetransmit_Type = Counter32
_CsgQuotaMgrRetransmit_Object = MibTableColumn
csgQuotaMgrRetransmit = _CsgQuotaMgrRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 13),
    _CsgQuotaMgrRetransmit_Type()
)
csgQuotaMgrRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgQuotaMgrRetransmit.setStatus("current")
_CsgQuotaMgrRowStatus_Type = RowStatus
_CsgQuotaMgrRowStatus_Object = MibTableColumn
csgQuotaMgrRowStatus = _CsgQuotaMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 14),
    _CsgQuotaMgrRowStatus_Type()
)
csgQuotaMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csgQuotaMgrRowStatus.setStatus("current")
_CsgNotifsEnable_ObjectIdentity = ObjectIdentity
csgNotifsEnable = _CsgNotifsEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6)
)


class _CsgAgentNotifsEnabled_Type(TruthValue):
    """Custom type csgAgentNotifsEnabled based on TruthValue"""


_CsgAgentNotifsEnabled_Object = MibScalar
csgAgentNotifsEnabled = _CsgAgentNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6, 1),
    _CsgAgentNotifsEnabled_Type()
)
csgAgentNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csgAgentNotifsEnabled.setStatus("current")


class _CsgQuotaNotifsEnabled_Type(TruthValue):
    """Custom type csgQuotaNotifsEnabled based on TruthValue"""


_CsgQuotaNotifsEnabled_Object = MibScalar
csgQuotaNotifsEnabled = _CsgQuotaNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6, 2),
    _CsgQuotaNotifsEnabled_Type()
)
csgQuotaNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csgQuotaNotifsEnabled.setStatus("current")


class _CsgDatabaseNotifsEnabled_Type(TruthValue):
    """Custom type csgDatabaseNotifsEnabled based on TruthValue"""


_CsgDatabaseNotifsEnabled_Object = MibScalar
csgDatabaseNotifsEnabled = _CsgDatabaseNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6, 3),
    _CsgDatabaseNotifsEnabled_Type()
)
csgDatabaseNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csgDatabaseNotifsEnabled.setStatus("current")
_CiscoCsgMIBConform_ObjectIdentity = ObjectIdentity
ciscoCsgMIBConform = _CiscoCsgMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2)
)
_CiscoCsgMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCsgMIBCompliances = _CiscoCsgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 1)
)
_CiscoCsgMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCsgMIBGroups = _CiscoCsgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2)
)

# Managed Objects groups

ciscoUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 1)
)
ciscoUserGroup.setObjects(
      *(("CISCO-CSG-MIB", "csgUserMaxEntries"),
        ("CISCO-CSG-MIB", "csgUserCurrEntries"),
        ("CISCO-CSG-MIB", "csgUserHighWater"),
        ("CISCO-CSG-MIB", "csgUserLRUSteals"),
        ("CISCO-CSG-MIB", "csgUserRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoUserGroup.setStatus("current")

ciscoUserDbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 2)
)
ciscoUserDbGroup.setObjects(
      *(("CISCO-CSG-MIB", "csgUserDbState"),
        ("CISCO-CSG-MIB", "csgUserDbRequests"),
        ("CISCO-CSG-MIB", "csgUserDbUidsReturned"),
        ("CISCO-CSG-MIB", "csgUserDbReqResent"),
        ("CISCO-CSG-MIB", "csgUserDbReqTimeouts"),
        ("CISCO-CSG-MIB", "csgUserDbReqErrors"),
        ("CISCO-CSG-MIB", "csgUserDbRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoUserDbGroup.setStatus("current")

ciscoAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 3)
)
ciscoAgentGroup.setObjects(
      *(("CISCO-CSG-MIB", "csgAgentAcctName"),
        ("CISCO-CSG-MIB", "csgAgentPriority"),
        ("CISCO-CSG-MIB", "csgAgentState"),
        ("CISCO-CSG-MIB", "csgAgentLostRecords"),
        ("CISCO-CSG-MIB", "csgAgentTotalSent"),
        ("CISCO-CSG-MIB", "csgAgentFailAck"),
        ("CISCO-CSG-MIB", "csgAgentOutstanding"),
        ("CISCO-CSG-MIB", "csgAgentHighWater"),
        ("CISCO-CSG-MIB", "csgAgentBadRecord"),
        ("CISCO-CSG-MIB", "csgAgentRetransmit"),
        ("CISCO-CSG-MIB", "csgAgentLostRecordTimer"),
        ("CISCO-CSG-MIB", "csgAgentRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoAgentGroup.setStatus("current")

ciscoQuotaMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 4)
)
ciscoQuotaMgrGroup.setObjects(
      *(("CISCO-CSG-MIB", "csgQuotaMgrUserGroupName"),
        ("CISCO-CSG-MIB", "csgQuotaMgrPriority"),
        ("CISCO-CSG-MIB", "csgQuotaMgrState"),
        ("CISCO-CSG-MIB", "csgQuotaMgrLostRecords"),
        ("CISCO-CSG-MIB", "csgQuotaMgrTotalSent"),
        ("CISCO-CSG-MIB", "csgQuotaMgrFailAck"),
        ("CISCO-CSG-MIB", "csgQuotaMgrOutstanding"),
        ("CISCO-CSG-MIB", "csgQuotaMgrHighWater"),
        ("CISCO-CSG-MIB", "csgQuotaMgrBadRecord"),
        ("CISCO-CSG-MIB", "csgQuotaMgrRetransmit"),
        ("CISCO-CSG-MIB", "csgQuotaMgrLostRecordTimer"),
        ("CISCO-CSG-MIB", "csgQuotaMgrRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoQuotaMgrGroup.setStatus("current")

ciscoCsgNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 5)
)
ciscoCsgNotifEnableGroup.setObjects(
      *(("CISCO-CSG-MIB", "csgAgentNotifsEnabled"),
        ("CISCO-CSG-MIB", "csgQuotaNotifsEnabled"),
        ("CISCO-CSG-MIB", "csgDatabaseNotifsEnabled"))
)
if mibBuilder.loadTexts:
    ciscoCsgNotifEnableGroup.setStatus("current")


# Notification objects

ciscoCsgAgentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 1)
)
ciscoCsgAgentStateChange.setObjects(
      *(("CISCO-CSG-MIB", "csgAgentState"),
        ("CISCO-CSG-MIB", "csgAgentLostRecords"),
        ("CISCO-CSG-MIB", "csgAgentTotalSent"),
        ("CISCO-CSG-MIB", "csgAgentFailAck"),
        ("CISCO-CSG-MIB", "csgAgentOutstanding"),
        ("CISCO-CSG-MIB", "csgAgentHighWater"),
        ("CISCO-CSG-MIB", "csgAgentBadRecord"),
        ("CISCO-CSG-MIB", "csgAgentRetransmit"))
)
if mibBuilder.loadTexts:
    ciscoCsgAgentStateChange.setStatus(
        "current"
    )

ciscoCsgQuotaMgrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 2)
)
ciscoCsgQuotaMgrStateChange.setObjects(
      *(("CISCO-CSG-MIB", "csgQuotaMgrState"),
        ("CISCO-CSG-MIB", "csgQuotaMgrLostRecords"),
        ("CISCO-CSG-MIB", "csgQuotaMgrTotalSent"),
        ("CISCO-CSG-MIB", "csgQuotaMgrFailAck"),
        ("CISCO-CSG-MIB", "csgQuotaMgrOutstanding"),
        ("CISCO-CSG-MIB", "csgQuotaMgrHighWater"),
        ("CISCO-CSG-MIB", "csgQuotaMgrBadRecord"),
        ("CISCO-CSG-MIB", "csgQuotaMgrRetransmit"))
)
if mibBuilder.loadTexts:
    ciscoCsgQuotaMgrStateChange.setStatus(
        "current"
    )

ciscoCsgUserDbStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 3)
)
ciscoCsgUserDbStateChange.setObjects(
      *(("CISCO-CSG-MIB", "csgUserDbState"),
        ("CISCO-CSG-MIB", "csgUserDbRequests"),
        ("CISCO-CSG-MIB", "csgUserDbUidsReturned"),
        ("CISCO-CSG-MIB", "csgUserDbReqResent"),
        ("CISCO-CSG-MIB", "csgUserDbReqTimeouts"),
        ("CISCO-CSG-MIB", "csgUserDbReqErrors"))
)
if mibBuilder.loadTexts:
    ciscoCsgUserDbStateChange.setStatus(
        "current"
    )

ciscoCsgAgentLostRecordEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 4)
)
ciscoCsgAgentLostRecordEvent.setObjects(
      *(("CISCO-CSG-MIB", "csgAgentState"),
        ("CISCO-CSG-MIB", "csgAgentLostRecords"),
        ("CISCO-CSG-MIB", "csgAgentTotalSent"),
        ("CISCO-CSG-MIB", "csgAgentFailAck"),
        ("CISCO-CSG-MIB", "csgAgentOutstanding"),
        ("CISCO-CSG-MIB", "csgAgentHighWater"),
        ("CISCO-CSG-MIB", "csgAgentBadRecord"),
        ("CISCO-CSG-MIB", "csgAgentRetransmit"))
)
if mibBuilder.loadTexts:
    ciscoCsgAgentLostRecordEvent.setStatus(
        "current"
    )

ciscoCsgQuotaMgrLostRecordEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 5)
)
ciscoCsgQuotaMgrLostRecordEvent.setObjects(
      *(("CISCO-CSG-MIB", "csgQuotaMgrState"),
        ("CISCO-CSG-MIB", "csgQuotaMgrLostRecords"),
        ("CISCO-CSG-MIB", "csgQuotaMgrTotalSent"),
        ("CISCO-CSG-MIB", "csgQuotaMgrFailAck"),
        ("CISCO-CSG-MIB", "csgQuotaMgrOutstanding"),
        ("CISCO-CSG-MIB", "csgQuotaMgrHighWater"),
        ("CISCO-CSG-MIB", "csgQuotaMgrBadRecord"),
        ("CISCO-CSG-MIB", "csgQuotaMgrRetransmit"))
)
if mibBuilder.loadTexts:
    ciscoCsgQuotaMgrLostRecordEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoCsgNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 6)
)
ciscoCsgNotifGroup.setObjects(
      *(("CISCO-CSG-MIB", "ciscoCsgAgentStateChange"),
        ("CISCO-CSG-MIB", "ciscoCsgQuotaMgrStateChange"),
        ("CISCO-CSG-MIB", "ciscoCsgUserDbStateChange"),
        ("CISCO-CSG-MIB", "ciscoCsgAgentLostRecordEvent"),
        ("CISCO-CSG-MIB", "ciscoCsgQuotaMgrLostRecordEvent"))
)
if mibBuilder.loadTexts:
    ciscoCsgNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCsgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCsgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CSG-MIB",
    **{"CsgSlotNumber": CsgSlotNumber,
       "CsgEntityName": CsgEntityName,
       "CsgServerPriority": CsgServerPriority,
       "CsgUserTableUpperBound": CsgUserTableUpperBound,
       "ciscoCsgMIB": ciscoCsgMIB,
       "ciscoCsgMIBNotifs": ciscoCsgMIBNotifs,
       "ciscoCsgAgentStateChange": ciscoCsgAgentStateChange,
       "ciscoCsgQuotaMgrStateChange": ciscoCsgQuotaMgrStateChange,
       "ciscoCsgUserDbStateChange": ciscoCsgUserDbStateChange,
       "ciscoCsgAgentLostRecordEvent": ciscoCsgAgentLostRecordEvent,
       "ciscoCsgQuotaMgrLostRecordEvent": ciscoCsgQuotaMgrLostRecordEvent,
       "ciscoCsgMIBObjects": ciscoCsgMIBObjects,
       "csgScalars": csgScalars,
       "csgAgentLostRecordTimer": csgAgentLostRecordTimer,
       "csgQuotaMgrLostRecordTimer": csgQuotaMgrLostRecordTimer,
       "csgUserStats": csgUserStats,
       "csgUserTable": csgUserTable,
       "csgUserTableEntry": csgUserTableEntry,
       "csgUserCardId": csgUserCardId,
       "csgUserGroupName": csgUserGroupName,
       "csgUserMaxEntries": csgUserMaxEntries,
       "csgUserCurrEntries": csgUserCurrEntries,
       "csgUserHighWater": csgUserHighWater,
       "csgUserLRUSteals": csgUserLRUSteals,
       "csgUserRowStatus": csgUserRowStatus,
       "csgUserDataBaseStats": csgUserDataBaseStats,
       "csgUserDbTable": csgUserDbTable,
       "csgUserDbTableEntry": csgUserDbTableEntry,
       "csgUserDbIpAddrType": csgUserDbIpAddrType,
       "csgUserDbIpAddr": csgUserDbIpAddr,
       "csgUserDbPort": csgUserDbPort,
       "csgUserDbState": csgUserDbState,
       "csgUserDbRequests": csgUserDbRequests,
       "csgUserDbUidsReturned": csgUserDbUidsReturned,
       "csgUserDbReqResent": csgUserDbReqResent,
       "csgUserDbReqTimeouts": csgUserDbReqTimeouts,
       "csgUserDbReqErrors": csgUserDbReqErrors,
       "csgUserDbRowStatus": csgUserDbRowStatus,
       "csgAgentStats": csgAgentStats,
       "csgAgentTable": csgAgentTable,
       "csgAgentTableEntry": csgAgentTableEntry,
       "csgAgentIpAddrType": csgAgentIpAddrType,
       "csgAgentIpAddr": csgAgentIpAddr,
       "csgAgentPort": csgAgentPort,
       "csgAgentAcctName": csgAgentAcctName,
       "csgAgentPriority": csgAgentPriority,
       "csgAgentState": csgAgentState,
       "csgAgentLostRecords": csgAgentLostRecords,
       "csgAgentTotalSent": csgAgentTotalSent,
       "csgAgentFailAck": csgAgentFailAck,
       "csgAgentOutstanding": csgAgentOutstanding,
       "csgAgentHighWater": csgAgentHighWater,
       "csgAgentBadRecord": csgAgentBadRecord,
       "csgAgentRetransmit": csgAgentRetransmit,
       "csgAgentRowStatus": csgAgentRowStatus,
       "csgQuotaMgrStats": csgQuotaMgrStats,
       "csgQuotaMgrTable": csgQuotaMgrTable,
       "csgQuotaMgrTableEntry": csgQuotaMgrTableEntry,
       "csgQuotaMgrIpAddrType": csgQuotaMgrIpAddrType,
       "csgQuotaMgrIpAddr": csgQuotaMgrIpAddr,
       "csgQuotaMgrPort": csgQuotaMgrPort,
       "csgQuotaMgrUserGroupName": csgQuotaMgrUserGroupName,
       "csgQuotaMgrPriority": csgQuotaMgrPriority,
       "csgQuotaMgrState": csgQuotaMgrState,
       "csgQuotaMgrLostRecords": csgQuotaMgrLostRecords,
       "csgQuotaMgrTotalSent": csgQuotaMgrTotalSent,
       "csgQuotaMgrFailAck": csgQuotaMgrFailAck,
       "csgQuotaMgrOutstanding": csgQuotaMgrOutstanding,
       "csgQuotaMgrHighWater": csgQuotaMgrHighWater,
       "csgQuotaMgrBadRecord": csgQuotaMgrBadRecord,
       "csgQuotaMgrRetransmit": csgQuotaMgrRetransmit,
       "csgQuotaMgrRowStatus": csgQuotaMgrRowStatus,
       "csgNotifsEnable": csgNotifsEnable,
       "csgAgentNotifsEnabled": csgAgentNotifsEnabled,
       "csgQuotaNotifsEnabled": csgQuotaNotifsEnabled,
       "csgDatabaseNotifsEnabled": csgDatabaseNotifsEnabled,
       "ciscoCsgMIBConform": ciscoCsgMIBConform,
       "ciscoCsgMIBCompliances": ciscoCsgMIBCompliances,
       "ciscoCsgMIBCompliance": ciscoCsgMIBCompliance,
       "ciscoCsgMIBGroups": ciscoCsgMIBGroups,
       "ciscoUserGroup": ciscoUserGroup,
       "ciscoUserDbGroup": ciscoUserDbGroup,
       "ciscoAgentGroup": ciscoAgentGroup,
       "ciscoQuotaMgrGroup": ciscoQuotaMgrGroup,
       "ciscoCsgNotifEnableGroup": ciscoCsgNotifEnableGroup,
       "ciscoCsgNotifGroup": ciscoCsgNotifGroup}
)
