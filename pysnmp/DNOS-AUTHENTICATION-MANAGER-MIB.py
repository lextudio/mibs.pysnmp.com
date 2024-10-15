# SNMP MIB module (DNOS-AUTHENTICATION-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-AUTHENTICATION-MANAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:48 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

fastPathAuthMgr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61)
)
fastPathAuthMgr.setRevisions(
        ("2012-12-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FastpathAuthMgrTraps_ObjectIdentity = ObjectIdentity
fastpathAuthMgrTraps = _FastpathAuthMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 0)
)
_AgentAuthMgrGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrGlobalConfigGroup = _AgentAuthMgrGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 1)
)


class _AgentAuthMgrAdminMode_Type(Integer32):
    """Custom type agentAuthMgrAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentAuthMgrAdminMode_Type.__name__ = "Integer32"
_AgentAuthMgrAdminMode_Object = MibScalar
agentAuthMgrAdminMode = _AgentAuthMgrAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 1, 1),
    _AgentAuthMgrAdminMode_Type()
)
agentAuthMgrAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrAdminMode.setStatus("current")
_AgentAuthMgrInterfaceConfigGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrInterfaceConfigGroup = _AgentAuthMgrInterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2)
)
_AgentAuthMgrInterfaceConfigMethodTable_Object = MibTable
agentAuthMgrInterfaceConfigMethodTable = _AgentAuthMgrInterfaceConfigMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigMethodTable.setStatus("current")
_AgentAuthMgrInterfaceConfigMethodEntry_Object = MibTableRow
agentAuthMgrInterfaceConfigMethodEntry = _AgentAuthMgrInterfaceConfigMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1)
)
agentAuthMgrInterfaceConfigMethodEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrIfIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "methodIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigMethodEntry.setStatus("current")
_AgentAuthMgrIfIndex_Type = InterfaceIndex
_AgentAuthMgrIfIndex_Object = MibTableColumn
agentAuthMgrIfIndex = _AgentAuthMgrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 1),
    _AgentAuthMgrIfIndex_Type()
)
agentAuthMgrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrIfIndex.setStatus("current")
_MethodIndex_Type = Unsigned32
_MethodIndex_Object = MibTableColumn
methodIndex = _MethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 2),
    _MethodIndex_Type()
)
methodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    methodIndex.setStatus("current")


class _AgentAuthMgrMethodOrder_Type(Integer32):
    """Custom type agentAuthMgrMethodOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 3),
          ("dot1x", 1),
          ("mab", 2),
          ("undefined", 0))
    )


_AgentAuthMgrMethodOrder_Type.__name__ = "Integer32"
_AgentAuthMgrMethodOrder_Object = MibTableColumn
agentAuthMgrMethodOrder = _AgentAuthMgrMethodOrder_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 3),
    _AgentAuthMgrMethodOrder_Type()
)
agentAuthMgrMethodOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentAuthMgrMethodOrder.setStatus("current")


class _AgentAuthMgrMethodPriority_Type(Integer32):
    """Custom type agentAuthMgrMethodPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 3),
          ("dot1x", 1),
          ("mab", 2),
          ("undefined", 0))
    )


_AgentAuthMgrMethodPriority_Type.__name__ = "Integer32"
_AgentAuthMgrMethodPriority_Object = MibTableColumn
agentAuthMgrMethodPriority = _AgentAuthMgrMethodPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 1, 1, 4),
    _AgentAuthMgrMethodPriority_Type()
)
agentAuthMgrMethodPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentAuthMgrMethodPriority.setStatus("current")
_AgentAuthMgrInterfaceConfigTimerTable_Object = MibTable
agentAuthMgrInterfaceConfigTimerTable = _AgentAuthMgrInterfaceConfigTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2)
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigTimerTable.setStatus("current")
_AgentAuthMgrInterfaceConfigTimerEntry_Object = MibTableRow
agentAuthMgrInterfaceConfigTimerEntry = _AgentAuthMgrInterfaceConfigTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2, 1)
)
agentAuthMgrInterfaceConfigTimerEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrTimerIfIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceConfigTimerEntry.setStatus("current")
_AgentAuthMgrTimerIfIndex_Type = InterfaceIndex
_AgentAuthMgrTimerIfIndex_Object = MibTableColumn
agentAuthMgrTimerIfIndex = _AgentAuthMgrTimerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2, 1, 1),
    _AgentAuthMgrTimerIfIndex_Type()
)
agentAuthMgrTimerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrTimerIfIndex.setStatus("current")


class _AgentAuthMgrRestart_Type(Unsigned32):
    """Custom type agentAuthMgrRestart based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentAuthMgrRestart_Type.__name__ = "Unsigned32"
_AgentAuthMgrRestart_Object = MibTableColumn
agentAuthMgrRestart = _AgentAuthMgrRestart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 2, 2, 1, 2),
    _AgentAuthMgrRestart_Type()
)
agentAuthMgrRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrRestart.setStatus("current")
_AgentAuthMgrInterfaceStatusGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrInterfaceStatusGroup = _AgentAuthMgrInterfaceStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3)
)
_AgentAuthMgrInterfaceStatusTable_Object = MibTable
agentAuthMgrInterfaceStatusTable = _AgentAuthMgrInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceStatusTable.setStatus("current")
_AgentAuthMgrInterfaceStatusEntry_Object = MibTableRow
agentAuthMgrInterfaceStatusEntry = _AgentAuthMgrInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1, 1)
)
agentAuthMgrInterfaceStatusEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrIfIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "methodIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrInterfaceStatusEntry.setStatus("current")


class _AgentAuthMgrStatusMethodOrder_Type(Integer32):
    """Custom type agentAuthMgrStatusMethodOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 3),
          ("dot1x", 1),
          ("mab", 2),
          ("undefined", 0))
    )


_AgentAuthMgrStatusMethodOrder_Type.__name__ = "Integer32"
_AgentAuthMgrStatusMethodOrder_Object = MibTableColumn
agentAuthMgrStatusMethodOrder = _AgentAuthMgrStatusMethodOrder_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1, 1, 1),
    _AgentAuthMgrStatusMethodOrder_Type()
)
agentAuthMgrStatusMethodOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrStatusMethodOrder.setStatus("current")


class _AgentAuthMgrStatusMethodPriority_Type(Integer32):
    """Custom type agentAuthMgrStatusMethodPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 3),
          ("dot1x", 1),
          ("mab", 2),
          ("undefined", 0))
    )


_AgentAuthMgrStatusMethodPriority_Type.__name__ = "Integer32"
_AgentAuthMgrStatusMethodPriority_Object = MibTableColumn
agentAuthMgrStatusMethodPriority = _AgentAuthMgrStatusMethodPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 3, 1, 1, 2),
    _AgentAuthMgrStatusMethodPriority_Type()
)
agentAuthMgrStatusMethodPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrStatusMethodPriority.setStatus("current")
_AgentAuthMgrClientStatusGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrClientStatusGroup = _AgentAuthMgrClientStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4)
)
_AgentAuthMgrClientStatusTable_Object = MibTable
agentAuthMgrClientStatusTable = _AgentAuthMgrClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrClientStatusTable.setStatus("current")
_AgentAuthMgrClientStatusEntry_Object = MibTableRow
agentAuthMgrClientStatusEntry = _AgentAuthMgrClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1)
)
agentAuthMgrClientStatusEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientMacAddress"),
)
if mibBuilder.loadTexts:
    agentAuthMgrClientStatusEntry.setStatus("current")
_AgentAuthMgrClientMacAddress_Type = MacAddress
_AgentAuthMgrClientMacAddress_Object = MibTableColumn
agentAuthMgrClientMacAddress = _AgentAuthMgrClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 1),
    _AgentAuthMgrClientMacAddress_Type()
)
agentAuthMgrClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientMacAddress.setStatus("current")
_AgentAuthMgrLogicalPort_Type = Unsigned32
_AgentAuthMgrLogicalPort_Object = MibTableColumn
agentAuthMgrLogicalPort = _AgentAuthMgrLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 2),
    _AgentAuthMgrLogicalPort_Type()
)
agentAuthMgrLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrLogicalPort.setStatus("current")
_AgentAuthMgrInterface_Type = Unsigned32
_AgentAuthMgrInterface_Object = MibTableColumn
agentAuthMgrInterface = _AgentAuthMgrInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 3),
    _AgentAuthMgrInterface_Type()
)
agentAuthMgrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrInterface.setStatus("current")


class _AgentAuthMgrClientAuthstatus_Type(Integer32):
    """Custom type agentAuthMgrClientAuthstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )


_AgentAuthMgrClientAuthstatus_Type.__name__ = "Integer32"
_AgentAuthMgrClientAuthstatus_Object = MibTableColumn
agentAuthMgrClientAuthstatus = _AgentAuthMgrClientAuthstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 4),
    _AgentAuthMgrClientAuthstatus_Type()
)
agentAuthMgrClientAuthstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthstatus.setStatus("current")


class _AgentAuthMgrClientAuthMethod_Type(Integer32):
    """Custom type agentAuthMgrClientAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 3),
          ("dot1x", 1),
          ("mab", 2),
          ("undefined", 0))
    )


_AgentAuthMgrClientAuthMethod_Type.__name__ = "Integer32"
_AgentAuthMgrClientAuthMethod_Object = MibTableColumn
agentAuthMgrClientAuthMethod = _AgentAuthMgrClientAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 4, 1, 1, 5),
    _AgentAuthMgrClientAuthMethod_Type()
)
agentAuthMgrClientAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthMethod.setStatus("current")
_AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrAuthHistoryResultsGroup = _AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5)
)
_AgentAuthMgrPortAuthHistoryResultTable_Object = MibTable
agentAuthMgrPortAuthHistoryResultTable = _AgentAuthMgrPortAuthHistoryResultTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultTable.setStatus("current")
_AgentAuthMgrPortAuthHistoryResultEntry_Object = MibTableRow
agentAuthMgrPortAuthHistoryResultEntry = _AgentAuthMgrPortAuthHistoryResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1)
)
agentAuthMgrPortAuthHistoryResultEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrAuthHistoryResultIfaceIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrAuthHistoryResultIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultEntry.setStatus("current")
_AgentAuthMgrAuthHistoryResultIfaceIndex_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultIfaceIndex_Object = MibTableColumn
agentAuthMgrAuthHistoryResultIfaceIndex = _AgentAuthMgrAuthHistoryResultIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 1),
    _AgentAuthMgrAuthHistoryResultIfaceIndex_Type()
)
agentAuthMgrAuthHistoryResultIfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultIfaceIndex.setStatus("current")
_AgentAuthMgrAuthHistoryResultIndex_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultIndex_Object = MibTableColumn
agentAuthMgrAuthHistoryResultIndex = _AgentAuthMgrAuthHistoryResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 2),
    _AgentAuthMgrAuthHistoryResultIndex_Type()
)
agentAuthMgrAuthHistoryResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultIndex.setStatus("current")
_AgentAuthMgrAuthHistoryResultTimeStamp_Type = DateAndTime
_AgentAuthMgrAuthHistoryResultTimeStamp_Object = MibTableColumn
agentAuthMgrAuthHistoryResultTimeStamp = _AgentAuthMgrAuthHistoryResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 3),
    _AgentAuthMgrAuthHistoryResultTimeStamp_Type()
)
agentAuthMgrAuthHistoryResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultTimeStamp.setStatus("current")
_AgentAuthMgrAuthHistoryResultMacAddress_Type = MacAddress
_AgentAuthMgrAuthHistoryResultMacAddress_Object = MibTableColumn
agentAuthMgrAuthHistoryResultMacAddress = _AgentAuthMgrAuthHistoryResultMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 4),
    _AgentAuthMgrAuthHistoryResultMacAddress_Type()
)
agentAuthMgrAuthHistoryResultMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultMacAddress.setStatus("current")
_AgentAuthMgrAuthHistoryResultAuthMethod_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultAuthMethod_Object = MibTableColumn
agentAuthMgrAuthHistoryResultAuthMethod = _AgentAuthMgrAuthHistoryResultAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 5),
    _AgentAuthMgrAuthHistoryResultAuthMethod_Type()
)
agentAuthMgrAuthHistoryResultAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultAuthMethod.setStatus("current")


class _AgentAuthMgrAuthHistoryResultAuthStatus_Type(Integer32):
    """Custom type agentAuthMgrAuthHistoryResultAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_AgentAuthMgrAuthHistoryResultAuthStatus_Type.__name__ = "Integer32"
_AgentAuthMgrAuthHistoryResultAuthStatus_Object = MibTableColumn
agentAuthMgrAuthHistoryResultAuthStatus = _AgentAuthMgrAuthHistoryResultAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 1, 1, 6),
    _AgentAuthMgrAuthHistoryResultAuthStatus_Type()
)
agentAuthMgrAuthHistoryResultAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultAuthStatus.setStatus("current")
_AgentAuthMgrPortAuthHistoryResultClearTable_Object = MibTable
agentAuthMgrPortAuthHistoryResultClearTable = _AgentAuthMgrPortAuthHistoryResultClearTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultClearTable.setStatus("current")
_AgentAuthMgrPortAuthHistoryResultClearEntry_Object = MibTableRow
agentAuthMgrPortAuthHistoryResultClearEntry = _AgentAuthMgrPortAuthHistoryResultClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3, 1)
)
agentAuthMgrPortAuthHistoryResultClearEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrAuthHistoryResultIfIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultClearEntry.setStatus("current")
_AgentAuthMgrAuthHistoryResultIfIndex_Type = Unsigned32
_AgentAuthMgrAuthHistoryResultIfIndex_Object = MibTableColumn
agentAuthMgrAuthHistoryResultIfIndex = _AgentAuthMgrAuthHistoryResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3, 1, 1),
    _AgentAuthMgrAuthHistoryResultIfIndex_Type()
)
agentAuthMgrAuthHistoryResultIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrAuthHistoryResultIfIndex.setStatus("current")


class _AgentAuthMgrPortAuthHistoryResultsClear_Type(Integer32):
    """Custom type agentAuthMgrPortAuthHistoryResultsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentAuthMgrPortAuthHistoryResultsClear_Type.__name__ = "Integer32"
_AgentAuthMgrPortAuthHistoryResultsClear_Object = MibTableColumn
agentAuthMgrPortAuthHistoryResultsClear = _AgentAuthMgrPortAuthHistoryResultsClear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 5, 3, 1, 2),
    _AgentAuthMgrPortAuthHistoryResultsClear_Type()
)
agentAuthMgrPortAuthHistoryResultsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortAuthHistoryResultsClear.setStatus("current")
_AgentAuthMgrAuthStatsGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrAuthStatsGroup = _AgentAuthMgrAuthStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6)
)
_AgentAuthMgrPortStatsTable_Object = MibTable
agentAuthMgrPortStatsTable = _AgentAuthMgrPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsTable.setStatus("current")
_AgentAuthMgrPortStatsEntry_Object = MibTableRow
agentAuthMgrPortStatsEntry = _AgentAuthMgrPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1)
)
agentAuthMgrPortStatsEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrPortIfaceIndex"),
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrPortMethodIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsEntry.setStatus("current")
_AgentAuthMgrPortIfaceIndex_Type = Unsigned32
_AgentAuthMgrPortIfaceIndex_Object = MibTableColumn
agentAuthMgrPortIfaceIndex = _AgentAuthMgrPortIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 1),
    _AgentAuthMgrPortIfaceIndex_Type()
)
agentAuthMgrPortIfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrPortIfaceIndex.setStatus("current")


class _AgentAuthMgrPortMethodIndex_Type(Integer32):
    """Custom type agentAuthMgrPortMethodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 3),
          ("dot1x", 1),
          ("mab", 2))
    )


_AgentAuthMgrPortMethodIndex_Type.__name__ = "Integer32"
_AgentAuthMgrPortMethodIndex_Object = MibTableColumn
agentAuthMgrPortMethodIndex = _AgentAuthMgrPortMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 2),
    _AgentAuthMgrPortMethodIndex_Type()
)
agentAuthMgrPortMethodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthMgrPortMethodIndex.setStatus("current")
_AgentAuthMgrPortStatsAttempts_Type = Unsigned32
_AgentAuthMgrPortStatsAttempts_Object = MibTableColumn
agentAuthMgrPortStatsAttempts = _AgentAuthMgrPortStatsAttempts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 3),
    _AgentAuthMgrPortStatsAttempts_Type()
)
agentAuthMgrPortStatsAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsAttempts.setStatus("current")
_AgentAuthMgrPortStatsFailedAttempts_Type = Unsigned32
_AgentAuthMgrPortStatsFailedAttempts_Object = MibTableColumn
agentAuthMgrPortStatsFailedAttempts = _AgentAuthMgrPortStatsFailedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 1, 1, 4),
    _AgentAuthMgrPortStatsFailedAttempts_Type()
)
agentAuthMgrPortStatsFailedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsFailedAttempts.setStatus("current")
_AgentAuthMgrPortStatsClearTable_Object = MibTable
agentAuthMgrPortStatsClearTable = _AgentAuthMgrPortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 2)
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsClearTable.setStatus("current")
_AgentAuthMgrPortStatsClearEntry_Object = MibTableRow
agentAuthMgrPortStatsClearEntry = _AgentAuthMgrPortStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 2, 1)
)
agentAuthMgrPortStatsClearEntry.setIndexNames(
    (0, "DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrPortIfaceIndex"),
)
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsClearEntry.setStatus("current")


class _AgentAuthMgrPortStatsClear_Type(Integer32):
    """Custom type agentAuthMgrPortStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentAuthMgrPortStatsClear_Type.__name__ = "Integer32"
_AgentAuthMgrPortStatsClear_Object = MibTableColumn
agentAuthMgrPortStatsClear = _AgentAuthMgrPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 6, 2, 1, 2),
    _AgentAuthMgrPortStatsClear_Type()
)
agentAuthMgrPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthMgrPortStatsClear.setStatus("current")
_AgentAuthMgrTrapsConfigGroup_ObjectIdentity = ObjectIdentity
agentAuthMgrTrapsConfigGroup = _AgentAuthMgrTrapsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 7)
)


class _AuthMgrTrapMode_Type(Integer32):
    """Custom type authMgrTrapMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AuthMgrTrapMode_Type.__name__ = "Integer32"
_AuthMgrTrapMode_Object = MibScalar
authMgrTrapMode = _AuthMgrTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 7, 1),
    _AuthMgrTrapMode_Type()
)
authMgrTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMgrTrapMode.setStatus("current")

# Managed Objects groups


# Notification objects

agentAuthMgrClientAuthStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 61, 0, 1)
)
agentAuthMgrClientAuthStatusTrap.setObjects(
      *(("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrInterface"),
        ("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientMacAddress"),
        ("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientAuthMethod"),
        ("DNOS-AUTHENTICATION-MANAGER-MIB", "agentAuthMgrClientAuthstatus"))
)
if mibBuilder.loadTexts:
    agentAuthMgrClientAuthStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-AUTHENTICATION-MANAGER-MIB",
    **{"fastPathAuthMgr": fastPathAuthMgr,
       "fastpathAuthMgrTraps": fastpathAuthMgrTraps,
       "agentAuthMgrClientAuthStatusTrap": agentAuthMgrClientAuthStatusTrap,
       "agentAuthMgrGlobalConfigGroup": agentAuthMgrGlobalConfigGroup,
       "agentAuthMgrAdminMode": agentAuthMgrAdminMode,
       "agentAuthMgrInterfaceConfigGroup": agentAuthMgrInterfaceConfigGroup,
       "agentAuthMgrInterfaceConfigMethodTable": agentAuthMgrInterfaceConfigMethodTable,
       "agentAuthMgrInterfaceConfigMethodEntry": agentAuthMgrInterfaceConfigMethodEntry,
       "agentAuthMgrIfIndex": agentAuthMgrIfIndex,
       "methodIndex": methodIndex,
       "agentAuthMgrMethodOrder": agentAuthMgrMethodOrder,
       "agentAuthMgrMethodPriority": agentAuthMgrMethodPriority,
       "agentAuthMgrInterfaceConfigTimerTable": agentAuthMgrInterfaceConfigTimerTable,
       "agentAuthMgrInterfaceConfigTimerEntry": agentAuthMgrInterfaceConfigTimerEntry,
       "agentAuthMgrTimerIfIndex": agentAuthMgrTimerIfIndex,
       "agentAuthMgrRestart": agentAuthMgrRestart,
       "agentAuthMgrInterfaceStatusGroup": agentAuthMgrInterfaceStatusGroup,
       "agentAuthMgrInterfaceStatusTable": agentAuthMgrInterfaceStatusTable,
       "agentAuthMgrInterfaceStatusEntry": agentAuthMgrInterfaceStatusEntry,
       "agentAuthMgrStatusMethodOrder": agentAuthMgrStatusMethodOrder,
       "agentAuthMgrStatusMethodPriority": agentAuthMgrStatusMethodPriority,
       "agentAuthMgrClientStatusGroup": agentAuthMgrClientStatusGroup,
       "agentAuthMgrClientStatusTable": agentAuthMgrClientStatusTable,
       "agentAuthMgrClientStatusEntry": agentAuthMgrClientStatusEntry,
       "agentAuthMgrClientMacAddress": agentAuthMgrClientMacAddress,
       "agentAuthMgrLogicalPort": agentAuthMgrLogicalPort,
       "agentAuthMgrInterface": agentAuthMgrInterface,
       "agentAuthMgrClientAuthstatus": agentAuthMgrClientAuthstatus,
       "agentAuthMgrClientAuthMethod": agentAuthMgrClientAuthMethod,
       "agentAuthMgrAuthHistoryResultsGroup": agentAuthMgrAuthHistoryResultsGroup,
       "agentAuthMgrPortAuthHistoryResultTable": agentAuthMgrPortAuthHistoryResultTable,
       "agentAuthMgrPortAuthHistoryResultEntry": agentAuthMgrPortAuthHistoryResultEntry,
       "agentAuthMgrAuthHistoryResultIfaceIndex": agentAuthMgrAuthHistoryResultIfaceIndex,
       "agentAuthMgrAuthHistoryResultIndex": agentAuthMgrAuthHistoryResultIndex,
       "agentAuthMgrAuthHistoryResultTimeStamp": agentAuthMgrAuthHistoryResultTimeStamp,
       "agentAuthMgrAuthHistoryResultMacAddress": agentAuthMgrAuthHistoryResultMacAddress,
       "agentAuthMgrAuthHistoryResultAuthMethod": agentAuthMgrAuthHistoryResultAuthMethod,
       "agentAuthMgrAuthHistoryResultAuthStatus": agentAuthMgrAuthHistoryResultAuthStatus,
       "agentAuthMgrPortAuthHistoryResultClearTable": agentAuthMgrPortAuthHistoryResultClearTable,
       "agentAuthMgrPortAuthHistoryResultClearEntry": agentAuthMgrPortAuthHistoryResultClearEntry,
       "agentAuthMgrAuthHistoryResultIfIndex": agentAuthMgrAuthHistoryResultIfIndex,
       "agentAuthMgrPortAuthHistoryResultsClear": agentAuthMgrPortAuthHistoryResultsClear,
       "agentAuthMgrAuthStatsGroup": agentAuthMgrAuthStatsGroup,
       "agentAuthMgrPortStatsTable": agentAuthMgrPortStatsTable,
       "agentAuthMgrPortStatsEntry": agentAuthMgrPortStatsEntry,
       "agentAuthMgrPortIfaceIndex": agentAuthMgrPortIfaceIndex,
       "agentAuthMgrPortMethodIndex": agentAuthMgrPortMethodIndex,
       "agentAuthMgrPortStatsAttempts": agentAuthMgrPortStatsAttempts,
       "agentAuthMgrPortStatsFailedAttempts": agentAuthMgrPortStatsFailedAttempts,
       "agentAuthMgrPortStatsClearTable": agentAuthMgrPortStatsClearTable,
       "agentAuthMgrPortStatsClearEntry": agentAuthMgrPortStatsClearEntry,
       "agentAuthMgrPortStatsClear": agentAuthMgrPortStatsClear,
       "agentAuthMgrTrapsConfigGroup": agentAuthMgrTrapsConfigGroup,
       "authMgrTrapMode": authMgrTrapMode}
)
