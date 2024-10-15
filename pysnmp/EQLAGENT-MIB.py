# SNMP MIB module (EQLAGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLAGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:59 2024
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

(eqlGroupId,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

eqlAgentModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 12)
)
eqlAgentModule.setRevisions(
        ("2002-11-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlAgentObjects_ObjectIdentity = ObjectIdentity
eqlAgentObjects = _EqlAgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 12, 1)
)
_EqlExtErrorTable_Object = MibTable
eqlExtErrorTable = _EqlExtErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 1, 1)
)
if mibBuilder.loadTexts:
    eqlExtErrorTable.setStatus("current")
_EqlExtErrorEntry_Object = MibTableRow
eqlExtErrorEntry = _EqlExtErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1)
)
eqlExtErrorEntry.setIndexNames(
    (0, "EQLAGENT-MIB", "eqlEntIpAddr"),
    (0, "EQLAGENT-MIB", "eqlSNMPrid"),
)
if mibBuilder.loadTexts:
    eqlExtErrorEntry.setStatus("current")
_EqlEntIpAddr_Type = IpAddress
_EqlEntIpAddr_Object = MibTableColumn
eqlEntIpAddr = _EqlEntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 1),
    _EqlEntIpAddr_Type()
)
eqlEntIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlEntIpAddr.setStatus("current")
_EqlSNMPrid_Type = Integer32
_EqlSNMPrid_Object = MibTableColumn
eqlSNMPrid = _EqlSNMPrid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 2),
    _EqlSNMPrid_Type()
)
eqlSNMPrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSNMPrid.setStatus("current")
_EqlSNMPExtErrCode_Type = Integer32
_EqlSNMPExtErrCode_Object = MibTableColumn
eqlSNMPExtErrCode = _EqlSNMPExtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 3),
    _EqlSNMPExtErrCode_Type()
)
eqlSNMPExtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSNMPExtErrCode.setStatus("current")
_EqlSNMPExtErrMsg_Type = DisplayString
_EqlSNMPExtErrMsg_Object = MibTableColumn
eqlSNMPExtErrMsg = _EqlSNMPExtErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 1, 1, 1, 4),
    _EqlSNMPExtErrMsg_Type()
)
eqlSNMPExtErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSNMPExtErrMsg.setStatus("current")
_EqlAgentNotifications_ObjectIdentity = ObjectIdentity
eqlAgentNotifications = _EqlAgentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 12, 2)
)
_EqlAgentConformance_ObjectIdentity = ObjectIdentity
eqlAgentConformance = _EqlAgentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 12, 3)
)
_EqlAgentInetObjects_ObjectIdentity = ObjectIdentity
eqlAgentInetObjects = _EqlAgentInetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4)
)
_EqlExtInetErrorTable_Object = MibTable
eqlExtInetErrorTable = _EqlExtInetErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4, 4)
)
if mibBuilder.loadTexts:
    eqlExtInetErrorTable.setStatus("current")
_EqlExtInetErrorEntry_Object = MibTableRow
eqlExtInetErrorEntry = _EqlExtInetErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1)
)
eqlExtInetErrorEntry.setIndexNames(
    (0, "EQLAGENT-MIB", "eqlEntInetAddrType"),
    (0, "EQLAGENT-MIB", "eqlEntInetAddr"),
    (0, "EQLAGENT-MIB", "eqlSNMPInetrid"),
)
if mibBuilder.loadTexts:
    eqlExtInetErrorEntry.setStatus("current")
_EqlEntInetAddrType_Type = InetAddressType
_EqlEntInetAddrType_Object = MibTableColumn
eqlEntInetAddrType = _EqlEntInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 1),
    _EqlEntInetAddrType_Type()
)
eqlEntInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlEntInetAddrType.setStatus("current")
_EqlEntInetAddr_Type = InetAddress
_EqlEntInetAddr_Object = MibTableColumn
eqlEntInetAddr = _EqlEntInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 2),
    _EqlEntInetAddr_Type()
)
eqlEntInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlEntInetAddr.setStatus("current")
_EqlSNMPInetrid_Type = Integer32
_EqlSNMPInetrid_Object = MibTableColumn
eqlSNMPInetrid = _EqlSNMPInetrid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 3),
    _EqlSNMPInetrid_Type()
)
eqlSNMPInetrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSNMPInetrid.setStatus("current")
_EqlSNMPInetExtErrCode_Type = Integer32
_EqlSNMPInetExtErrCode_Object = MibTableColumn
eqlSNMPInetExtErrCode = _EqlSNMPInetExtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 4),
    _EqlSNMPInetExtErrCode_Type()
)
eqlSNMPInetExtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSNMPInetExtErrCode.setStatus("current")
_EqlSNMPInetExtErrMsg_Type = DisplayString
_EqlSNMPInetExtErrMsg_Object = MibTableColumn
eqlSNMPInetExtErrMsg = _EqlSNMPInetExtErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 12, 4, 4, 1, 5),
    _EqlSNMPInetExtErrMsg_Type()
)
eqlSNMPInetExtErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSNMPInetExtErrMsg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLAGENT-MIB",
    **{"eqlAgentModule": eqlAgentModule,
       "eqlAgentObjects": eqlAgentObjects,
       "eqlExtErrorTable": eqlExtErrorTable,
       "eqlExtErrorEntry": eqlExtErrorEntry,
       "eqlEntIpAddr": eqlEntIpAddr,
       "eqlSNMPrid": eqlSNMPrid,
       "eqlSNMPExtErrCode": eqlSNMPExtErrCode,
       "eqlSNMPExtErrMsg": eqlSNMPExtErrMsg,
       "eqlAgentNotifications": eqlAgentNotifications,
       "eqlAgentConformance": eqlAgentConformance,
       "eqlAgentInetObjects": eqlAgentInetObjects,
       "eqlExtInetErrorTable": eqlExtInetErrorTable,
       "eqlExtInetErrorEntry": eqlExtInetErrorEntry,
       "eqlEntInetAddrType": eqlEntInetAddrType,
       "eqlEntInetAddr": eqlEntInetAddr,
       "eqlSNMPInetrid": eqlSNMPInetrid,
       "eqlSNMPInetExtErrCode": eqlSNMPInetExtErrCode,
       "eqlSNMPInetExtErrMsg": eqlSNMPInetExtErrMsg}
)
