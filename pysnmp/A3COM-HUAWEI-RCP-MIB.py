# SNMP MIB module (A3COM-HUAWEI-RCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-RCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:58 2024
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

(h3cRCP,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cRCP")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cRCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1)
)
h3cRCPMIB.setRevisions(
        ("2006-09-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cRCPLeaf_ObjectIdentity = ObjectIdentity
h3cRCPLeaf = _H3cRCPLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1)
)
_H3cRCPServerEnableStatus_Type = TruthValue
_H3cRCPServerEnableStatus_Object = MibScalar
h3cRCPServerEnableStatus = _H3cRCPServerEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 1),
    _H3cRCPServerEnableStatus_Type()
)
h3cRCPServerEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRCPServerEnableStatus.setStatus("current")
_H3cRCPConnTimeout_Type = Integer32
_H3cRCPConnTimeout_Object = MibScalar
h3cRCPConnTimeout = _H3cRCPConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 2),
    _H3cRCPConnTimeout_Type()
)
h3cRCPConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRCPConnTimeout.setStatus("current")
_H3cRCPRuleTimeout_Type = Integer32
_H3cRCPRuleTimeout_Object = MibScalar
h3cRCPRuleTimeout = _H3cRCPRuleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 3),
    _H3cRCPRuleTimeout_Type()
)
h3cRCPRuleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRCPRuleTimeout.setStatus("current")
_H3cRCPServerMaxConn_Type = Integer32
_H3cRCPServerMaxConn_Object = MibScalar
h3cRCPServerMaxConn = _H3cRCPServerMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 4),
    _H3cRCPServerMaxConn_Type()
)
h3cRCPServerMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRCPServerMaxConn.setStatus("current")
_H3cRCPServerCurConn_Type = Integer32
_H3cRCPServerCurConn_Object = MibScalar
h3cRCPServerCurConn = _H3cRCPServerCurConn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 5),
    _H3cRCPServerCurConn_Type()
)
h3cRCPServerCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPServerCurConn.setStatus("current")
_H3cRCPConnTimeoutMaxValue_Type = Integer32
_H3cRCPConnTimeoutMaxValue_Object = MibScalar
h3cRCPConnTimeoutMaxValue = _H3cRCPConnTimeoutMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 6),
    _H3cRCPConnTimeoutMaxValue_Type()
)
h3cRCPConnTimeoutMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPConnTimeoutMaxValue.setStatus("current")
_H3cRCPRuleTimeoutMaxValue_Type = Integer32
_H3cRCPRuleTimeoutMaxValue_Object = MibScalar
h3cRCPRuleTimeoutMaxValue = _H3cRCPRuleTimeoutMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 7),
    _H3cRCPRuleTimeoutMaxValue_Type()
)
h3cRCPRuleTimeoutMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPRuleTimeoutMaxValue.setStatus("current")
_H3cRCPServerMaxConnMaxValue_Type = Integer32
_H3cRCPServerMaxConnMaxValue_Object = MibScalar
h3cRCPServerMaxConnMaxValue = _H3cRCPServerMaxConnMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 8),
    _H3cRCPServerMaxConnMaxValue_Type()
)
h3cRCPServerMaxConnMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPServerMaxConnMaxValue.setStatus("current")
_H3cRCPBalanceGroupIdMinValue_Type = Integer32
_H3cRCPBalanceGroupIdMinValue_Object = MibScalar
h3cRCPBalanceGroupIdMinValue = _H3cRCPBalanceGroupIdMinValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 9),
    _H3cRCPBalanceGroupIdMinValue_Type()
)
h3cRCPBalanceGroupIdMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPBalanceGroupIdMinValue.setStatus("current")
_H3cRCPBalanceGroupIdMaxValue_Type = Integer32
_H3cRCPBalanceGroupIdMaxValue_Object = MibScalar
h3cRCPBalanceGroupIdMaxValue = _H3cRCPBalanceGroupIdMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 10),
    _H3cRCPBalanceGroupIdMaxValue_Type()
)
h3cRCPBalanceGroupIdMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPBalanceGroupIdMaxValue.setStatus("current")
_H3cRCPTotalUsers_Type = Integer32
_H3cRCPTotalUsers_Object = MibScalar
h3cRCPTotalUsers = _H3cRCPTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 11),
    _H3cRCPTotalUsers_Type()
)
h3cRCPTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPTotalUsers.setStatus("current")
_H3cRCPTotalClientIPs_Type = Integer32
_H3cRCPTotalClientIPs_Object = MibScalar
h3cRCPTotalClientIPs = _H3cRCPTotalClientIPs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 1, 12),
    _H3cRCPTotalClientIPs_Type()
)
h3cRCPTotalClientIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPTotalClientIPs.setStatus("current")
_H3cRCPTable_ObjectIdentity = ObjectIdentity
h3cRCPTable = _H3cRCPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2)
)
_H3cRCPUserTable_Object = MibTable
h3cRCPUserTable = _H3cRCPUserTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cRCPUserTable.setStatus("current")
_H3cRCPUserEntry_Object = MibTableRow
h3cRCPUserEntry = _H3cRCPUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 1, 1)
)
h3cRCPUserEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCP-MIB", "h3cRCPUserName"),
)
if mibBuilder.loadTexts:
    h3cRCPUserEntry.setStatus("current")


class _H3cRCPUserName_Type(DisplayString):
    """Custom type h3cRCPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_H3cRCPUserName_Type.__name__ = "DisplayString"
_H3cRCPUserName_Object = MibTableColumn
h3cRCPUserName = _H3cRCPUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 1, 1, 1),
    _H3cRCPUserName_Type()
)
h3cRCPUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRCPUserName.setStatus("current")


class _H3cRCPUserPassword_Type(DisplayString):
    """Custom type h3cRCPUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_H3cRCPUserPassword_Type.__name__ = "DisplayString"
_H3cRCPUserPassword_Object = MibTableColumn
h3cRCPUserPassword = _H3cRCPUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 1, 1, 2),
    _H3cRCPUserPassword_Type()
)
h3cRCPUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRCPUserPassword.setStatus("current")
_H3cRCPUserRedirectInterface_Type = InterfaceIndexOrZero
_H3cRCPUserRedirectInterface_Object = MibTableColumn
h3cRCPUserRedirectInterface = _H3cRCPUserRedirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 1, 1, 3),
    _H3cRCPUserRedirectInterface_Type()
)
h3cRCPUserRedirectInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRCPUserRedirectInterface.setStatus("current")
_H3cRCPUserRedirectBalanceGroup_Type = Integer32
_H3cRCPUserRedirectBalanceGroup_Object = MibTableColumn
h3cRCPUserRedirectBalanceGroup = _H3cRCPUserRedirectBalanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 1, 1, 4),
    _H3cRCPUserRedirectBalanceGroup_Type()
)
h3cRCPUserRedirectBalanceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRCPUserRedirectBalanceGroup.setStatus("current")
_H3cRCPUserRowStatus_Type = RowStatus
_H3cRCPUserRowStatus_Object = MibTableColumn
h3cRCPUserRowStatus = _H3cRCPUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 1, 1, 5),
    _H3cRCPUserRowStatus_Type()
)
h3cRCPUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRCPUserRowStatus.setStatus("current")
_H3cRCPClientIPTable_Object = MibTable
h3cRCPClientIPTable = _H3cRCPClientIPTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cRCPClientIPTable.setStatus("current")
_H3cRCPClientIPEntry_Object = MibTableRow
h3cRCPClientIPEntry = _H3cRCPClientIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 2, 1)
)
h3cRCPClientIPEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCP-MIB", "h3cRCPClientIPType"),
    (0, "A3COM-HUAWEI-RCP-MIB", "h3cRCPClientIP"),
)
if mibBuilder.loadTexts:
    h3cRCPClientIPEntry.setStatus("current")
_H3cRCPClientIPType_Type = InetAddressType
_H3cRCPClientIPType_Object = MibTableColumn
h3cRCPClientIPType = _H3cRCPClientIPType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 2, 1, 1),
    _H3cRCPClientIPType_Type()
)
h3cRCPClientIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRCPClientIPType.setStatus("current")
_H3cRCPClientIP_Type = InetAddress
_H3cRCPClientIP_Object = MibTableColumn
h3cRCPClientIP = _H3cRCPClientIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 2, 1, 2),
    _H3cRCPClientIP_Type()
)
h3cRCPClientIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRCPClientIP.setStatus("current")
_H3cRCPClientIPRowStatus_Type = RowStatus
_H3cRCPClientIPRowStatus_Object = MibTableColumn
h3cRCPClientIPRowStatus = _H3cRCPClientIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 2, 1, 3),
    _H3cRCPClientIPRowStatus_Type()
)
h3cRCPClientIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRCPClientIPRowStatus.setStatus("current")
_H3cRCPSessionTable_Object = MibTable
h3cRCPSessionTable = _H3cRCPSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cRCPSessionTable.setStatus("current")
_H3cRCPSessionEntry_Object = MibTableRow
h3cRCPSessionEntry = _H3cRCPSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 3, 1)
)
h3cRCPSessionEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCP-MIB", "h3cRCPSessionId"),
)
if mibBuilder.loadTexts:
    h3cRCPSessionEntry.setStatus("current")
_H3cRCPSessionId_Type = Integer32
_H3cRCPSessionId_Object = MibTableColumn
h3cRCPSessionId = _H3cRCPSessionId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 3, 1, 1),
    _H3cRCPSessionId_Type()
)
h3cRCPSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRCPSessionId.setStatus("current")
_H3cRCPSessionClientIPType_Type = InetAddressType
_H3cRCPSessionClientIPType_Object = MibTableColumn
h3cRCPSessionClientIPType = _H3cRCPSessionClientIPType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 3, 1, 2),
    _H3cRCPSessionClientIPType_Type()
)
h3cRCPSessionClientIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPSessionClientIPType.setStatus("current")
_H3cRCPSessionClientIP_Type = InetAddress
_H3cRCPSessionClientIP_Object = MibTableColumn
h3cRCPSessionClientIP = _H3cRCPSessionClientIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 3, 1, 3),
    _H3cRCPSessionClientIP_Type()
)
h3cRCPSessionClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPSessionClientIP.setStatus("current")


class _H3cRCPSessionRunningStatus_Type(Integer32):
    """Custom type h3cRCPSessionRunningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("operational", 2))
    )


_H3cRCPSessionRunningStatus_Type.__name__ = "Integer32"
_H3cRCPSessionRunningStatus_Object = MibTableColumn
h3cRCPSessionRunningStatus = _H3cRCPSessionRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 3, 1, 4),
    _H3cRCPSessionRunningStatus_Type()
)
h3cRCPSessionRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPSessionRunningStatus.setStatus("current")
_H3cRCPSessionUserName_Type = DisplayString
_H3cRCPSessionUserName_Object = MibTableColumn
h3cRCPSessionUserName = _H3cRCPSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 73, 1, 2, 3, 1, 5),
    _H3cRCPSessionUserName_Type()
)
h3cRCPSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRCPSessionUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-RCP-MIB",
    **{"h3cRCPMIB": h3cRCPMIB,
       "h3cRCPLeaf": h3cRCPLeaf,
       "h3cRCPServerEnableStatus": h3cRCPServerEnableStatus,
       "h3cRCPConnTimeout": h3cRCPConnTimeout,
       "h3cRCPRuleTimeout": h3cRCPRuleTimeout,
       "h3cRCPServerMaxConn": h3cRCPServerMaxConn,
       "h3cRCPServerCurConn": h3cRCPServerCurConn,
       "h3cRCPConnTimeoutMaxValue": h3cRCPConnTimeoutMaxValue,
       "h3cRCPRuleTimeoutMaxValue": h3cRCPRuleTimeoutMaxValue,
       "h3cRCPServerMaxConnMaxValue": h3cRCPServerMaxConnMaxValue,
       "h3cRCPBalanceGroupIdMinValue": h3cRCPBalanceGroupIdMinValue,
       "h3cRCPBalanceGroupIdMaxValue": h3cRCPBalanceGroupIdMaxValue,
       "h3cRCPTotalUsers": h3cRCPTotalUsers,
       "h3cRCPTotalClientIPs": h3cRCPTotalClientIPs,
       "h3cRCPTable": h3cRCPTable,
       "h3cRCPUserTable": h3cRCPUserTable,
       "h3cRCPUserEntry": h3cRCPUserEntry,
       "h3cRCPUserName": h3cRCPUserName,
       "h3cRCPUserPassword": h3cRCPUserPassword,
       "h3cRCPUserRedirectInterface": h3cRCPUserRedirectInterface,
       "h3cRCPUserRedirectBalanceGroup": h3cRCPUserRedirectBalanceGroup,
       "h3cRCPUserRowStatus": h3cRCPUserRowStatus,
       "h3cRCPClientIPTable": h3cRCPClientIPTable,
       "h3cRCPClientIPEntry": h3cRCPClientIPEntry,
       "h3cRCPClientIPType": h3cRCPClientIPType,
       "h3cRCPClientIP": h3cRCPClientIP,
       "h3cRCPClientIPRowStatus": h3cRCPClientIPRowStatus,
       "h3cRCPSessionTable": h3cRCPSessionTable,
       "h3cRCPSessionEntry": h3cRCPSessionEntry,
       "h3cRCPSessionId": h3cRCPSessionId,
       "h3cRCPSessionClientIPType": h3cRCPSessionClientIPType,
       "h3cRCPSessionClientIP": h3cRCPSessionClientIP,
       "h3cRCPSessionRunningStatus": h3cRCPSessionRunningStatus,
       "h3cRCPSessionUserName": h3cRCPSessionUserName}
)
