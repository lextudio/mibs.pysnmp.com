# SNMP MIB module (HPN-ICF-RCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:39 2024
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

(hpnicfRCP,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRCP")

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

hpnicfRCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1)
)
hpnicfRCPMIB.setRevisions(
        ("2006-09-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfRCPLeaf_ObjectIdentity = ObjectIdentity
hpnicfRCPLeaf = _HpnicfRCPLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1)
)
_HpnicfRCPServerEnableStatus_Type = TruthValue
_HpnicfRCPServerEnableStatus_Object = MibScalar
hpnicfRCPServerEnableStatus = _HpnicfRCPServerEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 1),
    _HpnicfRCPServerEnableStatus_Type()
)
hpnicfRCPServerEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRCPServerEnableStatus.setStatus("current")
_HpnicfRCPConnTimeout_Type = Integer32
_HpnicfRCPConnTimeout_Object = MibScalar
hpnicfRCPConnTimeout = _HpnicfRCPConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 2),
    _HpnicfRCPConnTimeout_Type()
)
hpnicfRCPConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRCPConnTimeout.setStatus("current")
_HpnicfRCPRuleTimeout_Type = Integer32
_HpnicfRCPRuleTimeout_Object = MibScalar
hpnicfRCPRuleTimeout = _HpnicfRCPRuleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 3),
    _HpnicfRCPRuleTimeout_Type()
)
hpnicfRCPRuleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRCPRuleTimeout.setStatus("current")
_HpnicfRCPServerMaxConn_Type = Integer32
_HpnicfRCPServerMaxConn_Object = MibScalar
hpnicfRCPServerMaxConn = _HpnicfRCPServerMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 4),
    _HpnicfRCPServerMaxConn_Type()
)
hpnicfRCPServerMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRCPServerMaxConn.setStatus("current")
_HpnicfRCPServerCurConn_Type = Integer32
_HpnicfRCPServerCurConn_Object = MibScalar
hpnicfRCPServerCurConn = _HpnicfRCPServerCurConn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 5),
    _HpnicfRCPServerCurConn_Type()
)
hpnicfRCPServerCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPServerCurConn.setStatus("current")
_HpnicfRCPConnTimeoutMaxValue_Type = Integer32
_HpnicfRCPConnTimeoutMaxValue_Object = MibScalar
hpnicfRCPConnTimeoutMaxValue = _HpnicfRCPConnTimeoutMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 6),
    _HpnicfRCPConnTimeoutMaxValue_Type()
)
hpnicfRCPConnTimeoutMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPConnTimeoutMaxValue.setStatus("current")
_HpnicfRCPRuleTimeoutMaxValue_Type = Integer32
_HpnicfRCPRuleTimeoutMaxValue_Object = MibScalar
hpnicfRCPRuleTimeoutMaxValue = _HpnicfRCPRuleTimeoutMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 7),
    _HpnicfRCPRuleTimeoutMaxValue_Type()
)
hpnicfRCPRuleTimeoutMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPRuleTimeoutMaxValue.setStatus("current")
_HpnicfRCPServerMaxConnMaxValue_Type = Integer32
_HpnicfRCPServerMaxConnMaxValue_Object = MibScalar
hpnicfRCPServerMaxConnMaxValue = _HpnicfRCPServerMaxConnMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 8),
    _HpnicfRCPServerMaxConnMaxValue_Type()
)
hpnicfRCPServerMaxConnMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPServerMaxConnMaxValue.setStatus("current")
_HpnicfRCPBalanceGroupIdMinValue_Type = Integer32
_HpnicfRCPBalanceGroupIdMinValue_Object = MibScalar
hpnicfRCPBalanceGroupIdMinValue = _HpnicfRCPBalanceGroupIdMinValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 9),
    _HpnicfRCPBalanceGroupIdMinValue_Type()
)
hpnicfRCPBalanceGroupIdMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPBalanceGroupIdMinValue.setStatus("current")
_HpnicfRCPBalanceGroupIdMaxValue_Type = Integer32
_HpnicfRCPBalanceGroupIdMaxValue_Object = MibScalar
hpnicfRCPBalanceGroupIdMaxValue = _HpnicfRCPBalanceGroupIdMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 10),
    _HpnicfRCPBalanceGroupIdMaxValue_Type()
)
hpnicfRCPBalanceGroupIdMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPBalanceGroupIdMaxValue.setStatus("current")
_HpnicfRCPTotalUsers_Type = Integer32
_HpnicfRCPTotalUsers_Object = MibScalar
hpnicfRCPTotalUsers = _HpnicfRCPTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 11),
    _HpnicfRCPTotalUsers_Type()
)
hpnicfRCPTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPTotalUsers.setStatus("current")
_HpnicfRCPTotalClientIPs_Type = Integer32
_HpnicfRCPTotalClientIPs_Object = MibScalar
hpnicfRCPTotalClientIPs = _HpnicfRCPTotalClientIPs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 1, 12),
    _HpnicfRCPTotalClientIPs_Type()
)
hpnicfRCPTotalClientIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPTotalClientIPs.setStatus("current")
_HpnicfRCPTable_ObjectIdentity = ObjectIdentity
hpnicfRCPTable = _HpnicfRCPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2)
)
_HpnicfRCPUserTable_Object = MibTable
hpnicfRCPUserTable = _HpnicfRCPUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfRCPUserTable.setStatus("current")
_HpnicfRCPUserEntry_Object = MibTableRow
hpnicfRCPUserEntry = _HpnicfRCPUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 1, 1)
)
hpnicfRCPUserEntry.setIndexNames(
    (0, "HPN-ICF-RCP-MIB", "hpnicfRCPUserName"),
)
if mibBuilder.loadTexts:
    hpnicfRCPUserEntry.setStatus("current")


class _HpnicfRCPUserName_Type(DisplayString):
    """Custom type hpnicfRCPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpnicfRCPUserName_Type.__name__ = "DisplayString"
_HpnicfRCPUserName_Object = MibTableColumn
hpnicfRCPUserName = _HpnicfRCPUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 1, 1, 1),
    _HpnicfRCPUserName_Type()
)
hpnicfRCPUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRCPUserName.setStatus("current")


class _HpnicfRCPUserPassword_Type(DisplayString):
    """Custom type hpnicfRCPUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpnicfRCPUserPassword_Type.__name__ = "DisplayString"
_HpnicfRCPUserPassword_Object = MibTableColumn
hpnicfRCPUserPassword = _HpnicfRCPUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 1, 1, 2),
    _HpnicfRCPUserPassword_Type()
)
hpnicfRCPUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRCPUserPassword.setStatus("current")
_HpnicfRCPUserRedirectInterface_Type = InterfaceIndexOrZero
_HpnicfRCPUserRedirectInterface_Object = MibTableColumn
hpnicfRCPUserRedirectInterface = _HpnicfRCPUserRedirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 1, 1, 3),
    _HpnicfRCPUserRedirectInterface_Type()
)
hpnicfRCPUserRedirectInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRCPUserRedirectInterface.setStatus("current")
_HpnicfRCPUserRedirectBalanceGroup_Type = Integer32
_HpnicfRCPUserRedirectBalanceGroup_Object = MibTableColumn
hpnicfRCPUserRedirectBalanceGroup = _HpnicfRCPUserRedirectBalanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 1, 1, 4),
    _HpnicfRCPUserRedirectBalanceGroup_Type()
)
hpnicfRCPUserRedirectBalanceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRCPUserRedirectBalanceGroup.setStatus("current")
_HpnicfRCPUserRowStatus_Type = RowStatus
_HpnicfRCPUserRowStatus_Object = MibTableColumn
hpnicfRCPUserRowStatus = _HpnicfRCPUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 1, 1, 5),
    _HpnicfRCPUserRowStatus_Type()
)
hpnicfRCPUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRCPUserRowStatus.setStatus("current")
_HpnicfRCPClientIPTable_Object = MibTable
hpnicfRCPClientIPTable = _HpnicfRCPClientIPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfRCPClientIPTable.setStatus("current")
_HpnicfRCPClientIPEntry_Object = MibTableRow
hpnicfRCPClientIPEntry = _HpnicfRCPClientIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 2, 1)
)
hpnicfRCPClientIPEntry.setIndexNames(
    (0, "HPN-ICF-RCP-MIB", "hpnicfRCPClientIPType"),
    (0, "HPN-ICF-RCP-MIB", "hpnicfRCPClientIP"),
)
if mibBuilder.loadTexts:
    hpnicfRCPClientIPEntry.setStatus("current")
_HpnicfRCPClientIPType_Type = InetAddressType
_HpnicfRCPClientIPType_Object = MibTableColumn
hpnicfRCPClientIPType = _HpnicfRCPClientIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 2, 1, 1),
    _HpnicfRCPClientIPType_Type()
)
hpnicfRCPClientIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRCPClientIPType.setStatus("current")
_HpnicfRCPClientIP_Type = InetAddress
_HpnicfRCPClientIP_Object = MibTableColumn
hpnicfRCPClientIP = _HpnicfRCPClientIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 2, 1, 2),
    _HpnicfRCPClientIP_Type()
)
hpnicfRCPClientIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRCPClientIP.setStatus("current")
_HpnicfRCPClientIPRowStatus_Type = RowStatus
_HpnicfRCPClientIPRowStatus_Object = MibTableColumn
hpnicfRCPClientIPRowStatus = _HpnicfRCPClientIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 2, 1, 3),
    _HpnicfRCPClientIPRowStatus_Type()
)
hpnicfRCPClientIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRCPClientIPRowStatus.setStatus("current")
_HpnicfRCPSessionTable_Object = MibTable
hpnicfRCPSessionTable = _HpnicfRCPSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfRCPSessionTable.setStatus("current")
_HpnicfRCPSessionEntry_Object = MibTableRow
hpnicfRCPSessionEntry = _HpnicfRCPSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 3, 1)
)
hpnicfRCPSessionEntry.setIndexNames(
    (0, "HPN-ICF-RCP-MIB", "hpnicfRCPSessionId"),
)
if mibBuilder.loadTexts:
    hpnicfRCPSessionEntry.setStatus("current")
_HpnicfRCPSessionId_Type = Integer32
_HpnicfRCPSessionId_Object = MibTableColumn
hpnicfRCPSessionId = _HpnicfRCPSessionId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 3, 1, 1),
    _HpnicfRCPSessionId_Type()
)
hpnicfRCPSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRCPSessionId.setStatus("current")
_HpnicfRCPSessionClientIPType_Type = InetAddressType
_HpnicfRCPSessionClientIPType_Object = MibTableColumn
hpnicfRCPSessionClientIPType = _HpnicfRCPSessionClientIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 3, 1, 2),
    _HpnicfRCPSessionClientIPType_Type()
)
hpnicfRCPSessionClientIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPSessionClientIPType.setStatus("current")
_HpnicfRCPSessionClientIP_Type = InetAddress
_HpnicfRCPSessionClientIP_Object = MibTableColumn
hpnicfRCPSessionClientIP = _HpnicfRCPSessionClientIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 3, 1, 3),
    _HpnicfRCPSessionClientIP_Type()
)
hpnicfRCPSessionClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPSessionClientIP.setStatus("current")


class _HpnicfRCPSessionRunningStatus_Type(Integer32):
    """Custom type hpnicfRCPSessionRunningStatus based on Integer32"""
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


_HpnicfRCPSessionRunningStatus_Type.__name__ = "Integer32"
_HpnicfRCPSessionRunningStatus_Object = MibTableColumn
hpnicfRCPSessionRunningStatus = _HpnicfRCPSessionRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 3, 1, 4),
    _HpnicfRCPSessionRunningStatus_Type()
)
hpnicfRCPSessionRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPSessionRunningStatus.setStatus("current")
_HpnicfRCPSessionUserName_Type = DisplayString
_HpnicfRCPSessionUserName_Object = MibTableColumn
hpnicfRCPSessionUserName = _HpnicfRCPSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73, 1, 2, 3, 1, 5),
    _HpnicfRCPSessionUserName_Type()
)
hpnicfRCPSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRCPSessionUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RCP-MIB",
    **{"hpnicfRCPMIB": hpnicfRCPMIB,
       "hpnicfRCPLeaf": hpnicfRCPLeaf,
       "hpnicfRCPServerEnableStatus": hpnicfRCPServerEnableStatus,
       "hpnicfRCPConnTimeout": hpnicfRCPConnTimeout,
       "hpnicfRCPRuleTimeout": hpnicfRCPRuleTimeout,
       "hpnicfRCPServerMaxConn": hpnicfRCPServerMaxConn,
       "hpnicfRCPServerCurConn": hpnicfRCPServerCurConn,
       "hpnicfRCPConnTimeoutMaxValue": hpnicfRCPConnTimeoutMaxValue,
       "hpnicfRCPRuleTimeoutMaxValue": hpnicfRCPRuleTimeoutMaxValue,
       "hpnicfRCPServerMaxConnMaxValue": hpnicfRCPServerMaxConnMaxValue,
       "hpnicfRCPBalanceGroupIdMinValue": hpnicfRCPBalanceGroupIdMinValue,
       "hpnicfRCPBalanceGroupIdMaxValue": hpnicfRCPBalanceGroupIdMaxValue,
       "hpnicfRCPTotalUsers": hpnicfRCPTotalUsers,
       "hpnicfRCPTotalClientIPs": hpnicfRCPTotalClientIPs,
       "hpnicfRCPTable": hpnicfRCPTable,
       "hpnicfRCPUserTable": hpnicfRCPUserTable,
       "hpnicfRCPUserEntry": hpnicfRCPUserEntry,
       "hpnicfRCPUserName": hpnicfRCPUserName,
       "hpnicfRCPUserPassword": hpnicfRCPUserPassword,
       "hpnicfRCPUserRedirectInterface": hpnicfRCPUserRedirectInterface,
       "hpnicfRCPUserRedirectBalanceGroup": hpnicfRCPUserRedirectBalanceGroup,
       "hpnicfRCPUserRowStatus": hpnicfRCPUserRowStatus,
       "hpnicfRCPClientIPTable": hpnicfRCPClientIPTable,
       "hpnicfRCPClientIPEntry": hpnicfRCPClientIPEntry,
       "hpnicfRCPClientIPType": hpnicfRCPClientIPType,
       "hpnicfRCPClientIP": hpnicfRCPClientIP,
       "hpnicfRCPClientIPRowStatus": hpnicfRCPClientIPRowStatus,
       "hpnicfRCPSessionTable": hpnicfRCPSessionTable,
       "hpnicfRCPSessionEntry": hpnicfRCPSessionEntry,
       "hpnicfRCPSessionId": hpnicfRCPSessionId,
       "hpnicfRCPSessionClientIPType": hpnicfRCPSessionClientIPType,
       "hpnicfRCPSessionClientIP": hpnicfRCPSessionClientIP,
       "hpnicfRCPSessionRunningStatus": hpnicfRCPSessionRunningStatus,
       "hpnicfRCPSessionUserName": hpnicfRCPSessionUserName}
)
