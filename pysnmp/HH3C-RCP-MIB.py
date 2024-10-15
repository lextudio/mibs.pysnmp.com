# SNMP MIB module (HH3C-RCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:42 2024
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

(hh3cRCP,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRCP")

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

hh3cRCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1)
)
hh3cRCPMIB.setRevisions(
        ("2006-09-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cRCPLeaf_ObjectIdentity = ObjectIdentity
hh3cRCPLeaf = _Hh3cRCPLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1)
)
_Hh3cRCPServerEnableStatus_Type = TruthValue
_Hh3cRCPServerEnableStatus_Object = MibScalar
hh3cRCPServerEnableStatus = _Hh3cRCPServerEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 1),
    _Hh3cRCPServerEnableStatus_Type()
)
hh3cRCPServerEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRCPServerEnableStatus.setStatus("current")
_Hh3cRCPConnTimeout_Type = Integer32
_Hh3cRCPConnTimeout_Object = MibScalar
hh3cRCPConnTimeout = _Hh3cRCPConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 2),
    _Hh3cRCPConnTimeout_Type()
)
hh3cRCPConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRCPConnTimeout.setStatus("current")
_Hh3cRCPRuleTimeout_Type = Integer32
_Hh3cRCPRuleTimeout_Object = MibScalar
hh3cRCPRuleTimeout = _Hh3cRCPRuleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 3),
    _Hh3cRCPRuleTimeout_Type()
)
hh3cRCPRuleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRCPRuleTimeout.setStatus("current")
_Hh3cRCPServerMaxConn_Type = Integer32
_Hh3cRCPServerMaxConn_Object = MibScalar
hh3cRCPServerMaxConn = _Hh3cRCPServerMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 4),
    _Hh3cRCPServerMaxConn_Type()
)
hh3cRCPServerMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRCPServerMaxConn.setStatus("current")
_Hh3cRCPServerCurConn_Type = Integer32
_Hh3cRCPServerCurConn_Object = MibScalar
hh3cRCPServerCurConn = _Hh3cRCPServerCurConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 5),
    _Hh3cRCPServerCurConn_Type()
)
hh3cRCPServerCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPServerCurConn.setStatus("current")
_Hh3cRCPConnTimeoutMaxValue_Type = Integer32
_Hh3cRCPConnTimeoutMaxValue_Object = MibScalar
hh3cRCPConnTimeoutMaxValue = _Hh3cRCPConnTimeoutMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 6),
    _Hh3cRCPConnTimeoutMaxValue_Type()
)
hh3cRCPConnTimeoutMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPConnTimeoutMaxValue.setStatus("current")
_Hh3cRCPRuleTimeoutMaxValue_Type = Integer32
_Hh3cRCPRuleTimeoutMaxValue_Object = MibScalar
hh3cRCPRuleTimeoutMaxValue = _Hh3cRCPRuleTimeoutMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 7),
    _Hh3cRCPRuleTimeoutMaxValue_Type()
)
hh3cRCPRuleTimeoutMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPRuleTimeoutMaxValue.setStatus("current")
_Hh3cRCPServerMaxConnMaxValue_Type = Integer32
_Hh3cRCPServerMaxConnMaxValue_Object = MibScalar
hh3cRCPServerMaxConnMaxValue = _Hh3cRCPServerMaxConnMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 8),
    _Hh3cRCPServerMaxConnMaxValue_Type()
)
hh3cRCPServerMaxConnMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPServerMaxConnMaxValue.setStatus("current")
_Hh3cRCPBalanceGroupIdMinValue_Type = Integer32
_Hh3cRCPBalanceGroupIdMinValue_Object = MibScalar
hh3cRCPBalanceGroupIdMinValue = _Hh3cRCPBalanceGroupIdMinValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 9),
    _Hh3cRCPBalanceGroupIdMinValue_Type()
)
hh3cRCPBalanceGroupIdMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPBalanceGroupIdMinValue.setStatus("current")
_Hh3cRCPBalanceGroupIdMaxValue_Type = Integer32
_Hh3cRCPBalanceGroupIdMaxValue_Object = MibScalar
hh3cRCPBalanceGroupIdMaxValue = _Hh3cRCPBalanceGroupIdMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 10),
    _Hh3cRCPBalanceGroupIdMaxValue_Type()
)
hh3cRCPBalanceGroupIdMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPBalanceGroupIdMaxValue.setStatus("current")
_Hh3cRCPTotalUsers_Type = Integer32
_Hh3cRCPTotalUsers_Object = MibScalar
hh3cRCPTotalUsers = _Hh3cRCPTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 11),
    _Hh3cRCPTotalUsers_Type()
)
hh3cRCPTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPTotalUsers.setStatus("current")
_Hh3cRCPTotalClientIPs_Type = Integer32
_Hh3cRCPTotalClientIPs_Object = MibScalar
hh3cRCPTotalClientIPs = _Hh3cRCPTotalClientIPs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 12),
    _Hh3cRCPTotalClientIPs_Type()
)
hh3cRCPTotalClientIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPTotalClientIPs.setStatus("current")
_Hh3cRCPTable_ObjectIdentity = ObjectIdentity
hh3cRCPTable = _Hh3cRCPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2)
)
_Hh3cRCPUserTable_Object = MibTable
hh3cRCPUserTable = _Hh3cRCPUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cRCPUserTable.setStatus("current")
_Hh3cRCPUserEntry_Object = MibTableRow
hh3cRCPUserEntry = _Hh3cRCPUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1)
)
hh3cRCPUserEntry.setIndexNames(
    (0, "HH3C-RCP-MIB", "hh3cRCPUserName"),
)
if mibBuilder.loadTexts:
    hh3cRCPUserEntry.setStatus("current")


class _Hh3cRCPUserName_Type(DisplayString):
    """Custom type hh3cRCPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Hh3cRCPUserName_Type.__name__ = "DisplayString"
_Hh3cRCPUserName_Object = MibTableColumn
hh3cRCPUserName = _Hh3cRCPUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 1),
    _Hh3cRCPUserName_Type()
)
hh3cRCPUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRCPUserName.setStatus("current")


class _Hh3cRCPUserPassword_Type(DisplayString):
    """Custom type hh3cRCPUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Hh3cRCPUserPassword_Type.__name__ = "DisplayString"
_Hh3cRCPUserPassword_Object = MibTableColumn
hh3cRCPUserPassword = _Hh3cRCPUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 2),
    _Hh3cRCPUserPassword_Type()
)
hh3cRCPUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRCPUserPassword.setStatus("current")
_Hh3cRCPUserRedirectInterface_Type = InterfaceIndexOrZero
_Hh3cRCPUserRedirectInterface_Object = MibTableColumn
hh3cRCPUserRedirectInterface = _Hh3cRCPUserRedirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 3),
    _Hh3cRCPUserRedirectInterface_Type()
)
hh3cRCPUserRedirectInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRCPUserRedirectInterface.setStatus("current")
_Hh3cRCPUserRedirectBalanceGroup_Type = Integer32
_Hh3cRCPUserRedirectBalanceGroup_Object = MibTableColumn
hh3cRCPUserRedirectBalanceGroup = _Hh3cRCPUserRedirectBalanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 4),
    _Hh3cRCPUserRedirectBalanceGroup_Type()
)
hh3cRCPUserRedirectBalanceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRCPUserRedirectBalanceGroup.setStatus("current")
_Hh3cRCPUserRowStatus_Type = RowStatus
_Hh3cRCPUserRowStatus_Object = MibTableColumn
hh3cRCPUserRowStatus = _Hh3cRCPUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 5),
    _Hh3cRCPUserRowStatus_Type()
)
hh3cRCPUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRCPUserRowStatus.setStatus("current")
_Hh3cRCPClientIPTable_Object = MibTable
hh3cRCPClientIPTable = _Hh3cRCPClientIPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cRCPClientIPTable.setStatus("current")
_Hh3cRCPClientIPEntry_Object = MibTableRow
hh3cRCPClientIPEntry = _Hh3cRCPClientIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1)
)
hh3cRCPClientIPEntry.setIndexNames(
    (0, "HH3C-RCP-MIB", "hh3cRCPClientIPType"),
    (0, "HH3C-RCP-MIB", "hh3cRCPClientIP"),
)
if mibBuilder.loadTexts:
    hh3cRCPClientIPEntry.setStatus("current")
_Hh3cRCPClientIPType_Type = InetAddressType
_Hh3cRCPClientIPType_Object = MibTableColumn
hh3cRCPClientIPType = _Hh3cRCPClientIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1, 1),
    _Hh3cRCPClientIPType_Type()
)
hh3cRCPClientIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRCPClientIPType.setStatus("current")
_Hh3cRCPClientIP_Type = InetAddress
_Hh3cRCPClientIP_Object = MibTableColumn
hh3cRCPClientIP = _Hh3cRCPClientIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1, 2),
    _Hh3cRCPClientIP_Type()
)
hh3cRCPClientIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRCPClientIP.setStatus("current")
_Hh3cRCPClientIPRowStatus_Type = RowStatus
_Hh3cRCPClientIPRowStatus_Object = MibTableColumn
hh3cRCPClientIPRowStatus = _Hh3cRCPClientIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1, 3),
    _Hh3cRCPClientIPRowStatus_Type()
)
hh3cRCPClientIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRCPClientIPRowStatus.setStatus("current")
_Hh3cRCPSessionTable_Object = MibTable
hh3cRCPSessionTable = _Hh3cRCPSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cRCPSessionTable.setStatus("current")
_Hh3cRCPSessionEntry_Object = MibTableRow
hh3cRCPSessionEntry = _Hh3cRCPSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1)
)
hh3cRCPSessionEntry.setIndexNames(
    (0, "HH3C-RCP-MIB", "hh3cRCPSessionId"),
)
if mibBuilder.loadTexts:
    hh3cRCPSessionEntry.setStatus("current")
_Hh3cRCPSessionId_Type = Integer32
_Hh3cRCPSessionId_Object = MibTableColumn
hh3cRCPSessionId = _Hh3cRCPSessionId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 1),
    _Hh3cRCPSessionId_Type()
)
hh3cRCPSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRCPSessionId.setStatus("current")
_Hh3cRCPSessionClientIPType_Type = InetAddressType
_Hh3cRCPSessionClientIPType_Object = MibTableColumn
hh3cRCPSessionClientIPType = _Hh3cRCPSessionClientIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 2),
    _Hh3cRCPSessionClientIPType_Type()
)
hh3cRCPSessionClientIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPSessionClientIPType.setStatus("current")
_Hh3cRCPSessionClientIP_Type = InetAddress
_Hh3cRCPSessionClientIP_Object = MibTableColumn
hh3cRCPSessionClientIP = _Hh3cRCPSessionClientIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 3),
    _Hh3cRCPSessionClientIP_Type()
)
hh3cRCPSessionClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPSessionClientIP.setStatus("current")


class _Hh3cRCPSessionRunningStatus_Type(Integer32):
    """Custom type hh3cRCPSessionRunningStatus based on Integer32"""
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


_Hh3cRCPSessionRunningStatus_Type.__name__ = "Integer32"
_Hh3cRCPSessionRunningStatus_Object = MibTableColumn
hh3cRCPSessionRunningStatus = _Hh3cRCPSessionRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 4),
    _Hh3cRCPSessionRunningStatus_Type()
)
hh3cRCPSessionRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPSessionRunningStatus.setStatus("current")
_Hh3cRCPSessionUserName_Type = DisplayString
_Hh3cRCPSessionUserName_Object = MibTableColumn
hh3cRCPSessionUserName = _Hh3cRCPSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 5),
    _Hh3cRCPSessionUserName_Type()
)
hh3cRCPSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRCPSessionUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RCP-MIB",
    **{"hh3cRCPMIB": hh3cRCPMIB,
       "hh3cRCPLeaf": hh3cRCPLeaf,
       "hh3cRCPServerEnableStatus": hh3cRCPServerEnableStatus,
       "hh3cRCPConnTimeout": hh3cRCPConnTimeout,
       "hh3cRCPRuleTimeout": hh3cRCPRuleTimeout,
       "hh3cRCPServerMaxConn": hh3cRCPServerMaxConn,
       "hh3cRCPServerCurConn": hh3cRCPServerCurConn,
       "hh3cRCPConnTimeoutMaxValue": hh3cRCPConnTimeoutMaxValue,
       "hh3cRCPRuleTimeoutMaxValue": hh3cRCPRuleTimeoutMaxValue,
       "hh3cRCPServerMaxConnMaxValue": hh3cRCPServerMaxConnMaxValue,
       "hh3cRCPBalanceGroupIdMinValue": hh3cRCPBalanceGroupIdMinValue,
       "hh3cRCPBalanceGroupIdMaxValue": hh3cRCPBalanceGroupIdMaxValue,
       "hh3cRCPTotalUsers": hh3cRCPTotalUsers,
       "hh3cRCPTotalClientIPs": hh3cRCPTotalClientIPs,
       "hh3cRCPTable": hh3cRCPTable,
       "hh3cRCPUserTable": hh3cRCPUserTable,
       "hh3cRCPUserEntry": hh3cRCPUserEntry,
       "hh3cRCPUserName": hh3cRCPUserName,
       "hh3cRCPUserPassword": hh3cRCPUserPassword,
       "hh3cRCPUserRedirectInterface": hh3cRCPUserRedirectInterface,
       "hh3cRCPUserRedirectBalanceGroup": hh3cRCPUserRedirectBalanceGroup,
       "hh3cRCPUserRowStatus": hh3cRCPUserRowStatus,
       "hh3cRCPClientIPTable": hh3cRCPClientIPTable,
       "hh3cRCPClientIPEntry": hh3cRCPClientIPEntry,
       "hh3cRCPClientIPType": hh3cRCPClientIPType,
       "hh3cRCPClientIP": hh3cRCPClientIP,
       "hh3cRCPClientIPRowStatus": hh3cRCPClientIPRowStatus,
       "hh3cRCPSessionTable": hh3cRCPSessionTable,
       "hh3cRCPSessionEntry": hh3cRCPSessionEntry,
       "hh3cRCPSessionId": hh3cRCPSessionId,
       "hh3cRCPSessionClientIPType": hh3cRCPSessionClientIPType,
       "hh3cRCPSessionClientIP": hh3cRCPSessionClientIP,
       "hh3cRCPSessionRunningStatus": hh3cRCPSessionRunningStatus,
       "hh3cRCPSessionUserName": hh3cRCPSessionUserName}
)
