# SNMP MIB module (GSM7312-SWITCHING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GSM7312-SWITCHING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:06 2024
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

(AgentPortMask,
 gsm7312) = mibBuilder.importSymbols(
    "GSM7312-REF-MIB",
    "AgentPortMask",
    "gsm7312")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIndex,
 dot1qFdbId,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex",
    "dot1qFdbId",
    "dot1qVlanIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

gsm7312Switching = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1)
)
gsm7312Switching.setRevisions(
        ("2003-02-06 18:35",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentInfoGroup_ObjectIdentity = ObjectIdentity
agentInfoGroup = _AgentInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1)
)
_AgentInventoryGroup_ObjectIdentity = ObjectIdentity
agentInventoryGroup = _AgentInventoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 1)
)
_AgentInventorySysDescription_Type = DisplayString
_AgentInventorySysDescription_Object = MibScalar
agentInventorySysDescription = _AgentInventorySysDescription_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 1, 1),
    _AgentInventorySysDescription_Type()
)
agentInventorySysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySysDescription.setStatus("current")
_AgentInventoryMachineType_Type = DisplayString
_AgentInventoryMachineType_Object = MibScalar
agentInventoryMachineType = _AgentInventoryMachineType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 1, 2),
    _AgentInventoryMachineType_Type()
)
agentInventoryMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMachineType.setStatus("current")
_AgentInventoryBurnedInMacAddress_Type = PhysAddress
_AgentInventoryBurnedInMacAddress_Object = MibScalar
agentInventoryBurnedInMacAddress = _AgentInventoryBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 1, 3),
    _AgentInventoryBurnedInMacAddress_Type()
)
agentInventoryBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryBurnedInMacAddress.setStatus("current")
_AgentInventoryAdditionalPackages_Type = DisplayString
_AgentInventoryAdditionalPackages_Object = MibScalar
agentInventoryAdditionalPackages = _AgentInventoryAdditionalPackages_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 1, 4),
    _AgentInventoryAdditionalPackages_Type()
)
agentInventoryAdditionalPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryAdditionalPackages.setStatus("current")
_AgentInventorySoftwareVersion_Type = DisplayString
_AgentInventorySoftwareVersion_Object = MibScalar
agentInventorySoftwareVersion = _AgentInventorySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 1, 5),
    _AgentInventorySoftwareVersion_Type()
)
agentInventorySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySoftwareVersion.setStatus("current")
_AgentTrapLogGroup_ObjectIdentity = ObjectIdentity
agentTrapLogGroup = _AgentTrapLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2)
)
_AgentTrapLogTotal_Type = Integer32
_AgentTrapLogTotal_Object = MibScalar
agentTrapLogTotal = _AgentTrapLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2, 1),
    _AgentTrapLogTotal_Type()
)
agentTrapLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTotal.setStatus("current")
_AgentTrapLogTotalSinceLastViewed_Type = Integer32
_AgentTrapLogTotalSinceLastViewed_Object = MibScalar
agentTrapLogTotalSinceLastViewed = _AgentTrapLogTotalSinceLastViewed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2, 3),
    _AgentTrapLogTotalSinceLastViewed_Type()
)
agentTrapLogTotalSinceLastViewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTotalSinceLastViewed.setStatus("deprecated")
_AgentTrapLogTable_Object = MibTable
agentTrapLogTable = _AgentTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    agentTrapLogTable.setStatus("current")
_AgentTrapLogEntry_Object = MibTableRow
agentTrapLogEntry = _AgentTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2, 4, 1)
)
agentTrapLogEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentTrapLogIndex"),
)
if mibBuilder.loadTexts:
    agentTrapLogEntry.setStatus("current")
_AgentTrapLogIndex_Type = Integer32
_AgentTrapLogIndex_Object = MibTableColumn
agentTrapLogIndex = _AgentTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2, 4, 1, 1),
    _AgentTrapLogIndex_Type()
)
agentTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogIndex.setStatus("current")
_AgentTrapLogSystemTime_Type = DisplayString
_AgentTrapLogSystemTime_Object = MibTableColumn
agentTrapLogSystemTime = _AgentTrapLogSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2, 4, 1, 2),
    _AgentTrapLogSystemTime_Type()
)
agentTrapLogSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogSystemTime.setStatus("current")


class _AgentTrapLogTrap_Type(OctetString):
    """Custom type agentTrapLogTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AgentTrapLogTrap_Type.__name__ = "OctetString"
_AgentTrapLogTrap_Object = MibTableColumn
agentTrapLogTrap = _AgentTrapLogTrap_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 2, 4, 1, 3),
    _AgentTrapLogTrap_Type()
)
agentTrapLogTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTrap.setStatus("current")
_AgentSupportedMibTable_Object = MibTable
agentSupportedMibTable = _AgentSupportedMibTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    agentSupportedMibTable.setStatus("current")
_AgentSupportedMibEntry_Object = MibTableRow
agentSupportedMibEntry = _AgentSupportedMibEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 3, 1)
)
agentSupportedMibEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentSupportedMibIndex"),
)
if mibBuilder.loadTexts:
    agentSupportedMibEntry.setStatus("current")
_AgentSupportedMibIndex_Type = Integer32
_AgentSupportedMibIndex_Object = MibTableColumn
agentSupportedMibIndex = _AgentSupportedMibIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 3, 1, 1),
    _AgentSupportedMibIndex_Type()
)
agentSupportedMibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSupportedMibIndex.setStatus("current")
_AgentSupportedMibName_Type = DisplayString
_AgentSupportedMibName_Object = MibTableColumn
agentSupportedMibName = _AgentSupportedMibName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 3, 1, 2),
    _AgentSupportedMibName_Type()
)
agentSupportedMibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSupportedMibName.setStatus("current")


class _AgentSupportedMibDescription_Type(OctetString):
    """Custom type agentSupportedMibDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AgentSupportedMibDescription_Type.__name__ = "OctetString"
_AgentSupportedMibDescription_Object = MibTableColumn
agentSupportedMibDescription = _AgentSupportedMibDescription_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 1, 3, 1, 3),
    _AgentSupportedMibDescription_Type()
)
agentSupportedMibDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSupportedMibDescription.setStatus("current")
_AgentConfigGroup_ObjectIdentity = ObjectIdentity
agentConfigGroup = _AgentConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2)
)
_AgentCLIConfigGroup_ObjectIdentity = ObjectIdentity
agentCLIConfigGroup = _AgentCLIConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1)
)
_AgentLoginSessionTable_Object = MibTable
agentLoginSessionTable = _AgentLoginSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentLoginSessionTable.setStatus("current")
_AgentLoginSessionEntry_Object = MibTableRow
agentLoginSessionEntry = _AgentLoginSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1)
)
agentLoginSessionEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentLoginSessionIndex"),
)
if mibBuilder.loadTexts:
    agentLoginSessionEntry.setStatus("current")
_AgentLoginSessionIndex_Type = Integer32
_AgentLoginSessionIndex_Object = MibTableColumn
agentLoginSessionIndex = _AgentLoginSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1, 1),
    _AgentLoginSessionIndex_Type()
)
agentLoginSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIndex.setStatus("current")
_AgentLoginSessionUserName_Type = DisplayString
_AgentLoginSessionUserName_Object = MibTableColumn
agentLoginSessionUserName = _AgentLoginSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1, 2),
    _AgentLoginSessionUserName_Type()
)
agentLoginSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionUserName.setStatus("current")
_AgentLoginSessionIPAddress_Type = IpAddress
_AgentLoginSessionIPAddress_Object = MibTableColumn
agentLoginSessionIPAddress = _AgentLoginSessionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1, 3),
    _AgentLoginSessionIPAddress_Type()
)
agentLoginSessionIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIPAddress.setStatus("current")


class _AgentLoginSessionConnectionType_Type(Integer32):
    """Custom type agentLoginSessionConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serial", 1),
          ("telnet", 2))
    )


_AgentLoginSessionConnectionType_Type.__name__ = "Integer32"
_AgentLoginSessionConnectionType_Object = MibTableColumn
agentLoginSessionConnectionType = _AgentLoginSessionConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1, 4),
    _AgentLoginSessionConnectionType_Type()
)
agentLoginSessionConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionConnectionType.setStatus("current")
_AgentLoginSessionIdleTime_Type = TimeTicks
_AgentLoginSessionIdleTime_Object = MibTableColumn
agentLoginSessionIdleTime = _AgentLoginSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1, 5),
    _AgentLoginSessionIdleTime_Type()
)
agentLoginSessionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIdleTime.setStatus("current")
_AgentLoginSessionSessionTime_Type = TimeTicks
_AgentLoginSessionSessionTime_Object = MibTableColumn
agentLoginSessionSessionTime = _AgentLoginSessionSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1, 6),
    _AgentLoginSessionSessionTime_Type()
)
agentLoginSessionSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionSessionTime.setStatus("current")
_AgentLoginSessionStatus_Type = RowStatus
_AgentLoginSessionStatus_Object = MibTableColumn
agentLoginSessionStatus = _AgentLoginSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 1, 1, 7),
    _AgentLoginSessionStatus_Type()
)
agentLoginSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLoginSessionStatus.setStatus("current")
_AgentTelnetConfigGroup_ObjectIdentity = ObjectIdentity
agentTelnetConfigGroup = _AgentTelnetConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 2)
)


class _AgentTelnetLoginTimeout_Type(Integer32):
    """Custom type agentTelnetLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_AgentTelnetLoginTimeout_Type.__name__ = "Integer32"
_AgentTelnetLoginTimeout_Object = MibScalar
agentTelnetLoginTimeout = _AgentTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 2, 1),
    _AgentTelnetLoginTimeout_Type()
)
agentTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetLoginTimeout.setStatus("current")


class _AgentTelnetMaxSessions_Type(Integer32):
    """Custom type agentTelnetMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentTelnetMaxSessions_Type.__name__ = "Integer32"
_AgentTelnetMaxSessions_Object = MibScalar
agentTelnetMaxSessions = _AgentTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 2, 2),
    _AgentTelnetMaxSessions_Type()
)
agentTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetMaxSessions.setStatus("current")


class _AgentTelnetAllowNewMode_Type(Integer32):
    """Custom type agentTelnetAllowNewMode based on Integer32"""
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


_AgentTelnetAllowNewMode_Type.__name__ = "Integer32"
_AgentTelnetAllowNewMode_Object = MibScalar
agentTelnetAllowNewMode = _AgentTelnetAllowNewMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 2, 3),
    _AgentTelnetAllowNewMode_Type()
)
agentTelnetAllowNewMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetAllowNewMode.setStatus("current")
_AgentUserConfigGroup_ObjectIdentity = ObjectIdentity
agentUserConfigGroup = _AgentUserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3)
)


class _AgentUserConfigCreate_Type(DisplayString):
    """Custom type agentUserConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AgentUserConfigCreate_Type.__name__ = "DisplayString"
_AgentUserConfigCreate_Object = MibScalar
agentUserConfigCreate = _AgentUserConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 1),
    _AgentUserConfigCreate_Type()
)
agentUserConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserConfigCreate.setStatus("current")
_AgentUserConfigTable_Object = MibTable
agentUserConfigTable = _AgentUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    agentUserConfigTable.setStatus("current")
_AgentUserConfigEntry_Object = MibTableRow
agentUserConfigEntry = _AgentUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1)
)
agentUserConfigEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentUserIndex"),
)
if mibBuilder.loadTexts:
    agentUserConfigEntry.setStatus("current")
_AgentUserIndex_Type = Integer32
_AgentUserIndex_Object = MibTableColumn
agentUserIndex = _AgentUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 1),
    _AgentUserIndex_Type()
)
agentUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentUserIndex.setStatus("current")


class _AgentUserName_Type(DisplayString):
    """Custom type agentUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AgentUserName_Type.__name__ = "DisplayString"
_AgentUserName_Object = MibTableColumn
agentUserName = _AgentUserName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 2),
    _AgentUserName_Type()
)
agentUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserName.setStatus("current")


class _AgentUserPassword_Type(DisplayString):
    """Custom type agentUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AgentUserPassword_Type.__name__ = "DisplayString"
_AgentUserPassword_Object = MibTableColumn
agentUserPassword = _AgentUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 3),
    _AgentUserPassword_Type()
)
agentUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserPassword.setStatus("current")


class _AgentUserAccessMode_Type(Integer32):
    """Custom type agentUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_AgentUserAccessMode_Type.__name__ = "Integer32"
_AgentUserAccessMode_Object = MibTableColumn
agentUserAccessMode = _AgentUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 4),
    _AgentUserAccessMode_Type()
)
agentUserAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUserAccessMode.setStatus("current")
_AgentUserStatus_Type = RowStatus
_AgentUserStatus_Object = MibTableColumn
agentUserStatus = _AgentUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 5),
    _AgentUserStatus_Type()
)
agentUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserStatus.setStatus("current")


class _AgentUserAuthenticationType_Type(Integer32):
    """Custom type agentUserAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hmacmd5", 2),
          ("hmacsha", 3),
          ("none", 1))
    )


_AgentUserAuthenticationType_Type.__name__ = "Integer32"
_AgentUserAuthenticationType_Object = MibTableColumn
agentUserAuthenticationType = _AgentUserAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 6),
    _AgentUserAuthenticationType_Type()
)
agentUserAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserAuthenticationType.setStatus("current")


class _AgentUserEncryptionType_Type(Integer32):
    """Custom type agentUserEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("none", 1))
    )


_AgentUserEncryptionType_Type.__name__ = "Integer32"
_AgentUserEncryptionType_Object = MibTableColumn
agentUserEncryptionType = _AgentUserEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 7),
    _AgentUserEncryptionType_Type()
)
agentUserEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserEncryptionType.setStatus("current")


class _AgentUserEncryptionPassword_Type(DisplayString):
    """Custom type agentUserEncryptionPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_AgentUserEncryptionPassword_Type.__name__ = "DisplayString"
_AgentUserEncryptionPassword_Object = MibTableColumn
agentUserEncryptionPassword = _AgentUserEncryptionPassword_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 3, 2, 1, 8),
    _AgentUserEncryptionPassword_Type()
)
agentUserEncryptionPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserEncryptionPassword.setStatus("current")
_AgentSerialGroup_ObjectIdentity = ObjectIdentity
agentSerialGroup = _AgentSerialGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 5)
)


class _AgentSerialTimeout_Type(Integer32):
    """Custom type agentSerialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_AgentSerialTimeout_Type.__name__ = "Integer32"
_AgentSerialTimeout_Object = MibScalar
agentSerialTimeout = _AgentSerialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 5, 1),
    _AgentSerialTimeout_Type()
)
agentSerialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialTimeout.setStatus("current")


class _AgentSerialBaudrate_Type(Integer32):
    """Custom type agentSerialBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("baud-115200", 8),
          ("baud-1200", 1),
          ("baud-19200", 5),
          ("baud-2400", 2),
          ("baud-38400", 6),
          ("baud-4800", 3),
          ("baud-57600", 7),
          ("baud-9600", 4))
    )


_AgentSerialBaudrate_Type.__name__ = "Integer32"
_AgentSerialBaudrate_Object = MibScalar
agentSerialBaudrate = _AgentSerialBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 5, 2),
    _AgentSerialBaudrate_Type()
)
agentSerialBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialBaudrate.setStatus("current")
_AgentSerialCharacterSize_Type = Integer32
_AgentSerialCharacterSize_Object = MibScalar
agentSerialCharacterSize = _AgentSerialCharacterSize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 5, 3),
    _AgentSerialCharacterSize_Type()
)
agentSerialCharacterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialCharacterSize.setStatus("current")


class _AgentSerialHWFlowControlMode_Type(Integer32):
    """Custom type agentSerialHWFlowControlMode based on Integer32"""
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


_AgentSerialHWFlowControlMode_Type.__name__ = "Integer32"
_AgentSerialHWFlowControlMode_Object = MibScalar
agentSerialHWFlowControlMode = _AgentSerialHWFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 5, 4),
    _AgentSerialHWFlowControlMode_Type()
)
agentSerialHWFlowControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialHWFlowControlMode.setStatus("current")
_AgentSerialStopBits_Type = Integer32
_AgentSerialStopBits_Object = MibScalar
agentSerialStopBits = _AgentSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 5, 5),
    _AgentSerialStopBits_Type()
)
agentSerialStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialStopBits.setStatus("current")


class _AgentSerialParityType_Type(Integer32):
    """Custom type agentSerialParityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("none", 3),
          ("odd", 2))
    )


_AgentSerialParityType_Type.__name__ = "Integer32"
_AgentSerialParityType_Object = MibScalar
agentSerialParityType = _AgentSerialParityType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 1, 5, 6),
    _AgentSerialParityType_Type()
)
agentSerialParityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialParityType.setStatus("current")
_AgentLagConfigGroup_ObjectIdentity = ObjectIdentity
agentLagConfigGroup = _AgentLagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2)
)


class _AgentLagConfigCreate_Type(DisplayString):
    """Custom type agentLagConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentLagConfigCreate_Type.__name__ = "DisplayString"
_AgentLagConfigCreate_Object = MibScalar
agentLagConfigCreate = _AgentLagConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 1),
    _AgentLagConfigCreate_Type()
)
agentLagConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagConfigCreate.setStatus("current")
_AgentLagSummaryConfigTable_Object = MibTable
agentLagSummaryConfigTable = _AgentLagSummaryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    agentLagSummaryConfigTable.setStatus("current")
_AgentLagSummaryConfigEntry_Object = MibTableRow
agentLagSummaryConfigEntry = _AgentLagSummaryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1)
)
agentLagSummaryConfigEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentLagSummaryLagIndex"),
)
if mibBuilder.loadTexts:
    agentLagSummaryConfigEntry.setStatus("current")
_AgentLagSummaryLagIndex_Type = Integer32
_AgentLagSummaryLagIndex_Object = MibTableColumn
agentLagSummaryLagIndex = _AgentLagSummaryLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 1),
    _AgentLagSummaryLagIndex_Type()
)
agentLagSummaryLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagSummaryLagIndex.setStatus("current")


class _AgentLagSummaryName_Type(DisplayString):
    """Custom type agentLagSummaryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentLagSummaryName_Type.__name__ = "DisplayString"
_AgentLagSummaryName_Object = MibTableColumn
agentLagSummaryName = _AgentLagSummaryName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 2),
    _AgentLagSummaryName_Type()
)
agentLagSummaryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryName.setStatus("current")
_AgentLagSummaryFlushTimer_Type = Integer32
_AgentLagSummaryFlushTimer_Object = MibTableColumn
agentLagSummaryFlushTimer = _AgentLagSummaryFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 3),
    _AgentLagSummaryFlushTimer_Type()
)
agentLagSummaryFlushTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryFlushTimer.setStatus("obsolete")


class _AgentLagSummaryLinkTrap_Type(Integer32):
    """Custom type agentLagSummaryLinkTrap based on Integer32"""
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


_AgentLagSummaryLinkTrap_Type.__name__ = "Integer32"
_AgentLagSummaryLinkTrap_Object = MibTableColumn
agentLagSummaryLinkTrap = _AgentLagSummaryLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 4),
    _AgentLagSummaryLinkTrap_Type()
)
agentLagSummaryLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryLinkTrap.setStatus("current")


class _AgentLagSummaryAdminMode_Type(Integer32):
    """Custom type agentLagSummaryAdminMode based on Integer32"""
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


_AgentLagSummaryAdminMode_Type.__name__ = "Integer32"
_AgentLagSummaryAdminMode_Object = MibTableColumn
agentLagSummaryAdminMode = _AgentLagSummaryAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 5),
    _AgentLagSummaryAdminMode_Type()
)
agentLagSummaryAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryAdminMode.setStatus("current")


class _AgentLagSummaryStpMode_Type(Integer32):
    """Custom type agentLagSummaryStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("dot1s", 4),
          ("fast", 2),
          ("off", 3))
    )


_AgentLagSummaryStpMode_Type.__name__ = "Integer32"
_AgentLagSummaryStpMode_Object = MibTableColumn
agentLagSummaryStpMode = _AgentLagSummaryStpMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 6),
    _AgentLagSummaryStpMode_Type()
)
agentLagSummaryStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryStpMode.setStatus("current")
_AgentLagSummaryAddPort_Type = Integer32
_AgentLagSummaryAddPort_Object = MibTableColumn
agentLagSummaryAddPort = _AgentLagSummaryAddPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 7),
    _AgentLagSummaryAddPort_Type()
)
agentLagSummaryAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryAddPort.setStatus("current")
_AgentLagSummaryDeletePort_Type = Integer32
_AgentLagSummaryDeletePort_Object = MibTableColumn
agentLagSummaryDeletePort = _AgentLagSummaryDeletePort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 8),
    _AgentLagSummaryDeletePort_Type()
)
agentLagSummaryDeletePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryDeletePort.setStatus("current")
_AgentLagSummaryStatus_Type = RowStatus
_AgentLagSummaryStatus_Object = MibTableColumn
agentLagSummaryStatus = _AgentLagSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 9),
    _AgentLagSummaryStatus_Type()
)
agentLagSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryStatus.setStatus("current")


class _AgentLagSummaryType_Type(Integer32):
    """Custom type agentLagSummaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AgentLagSummaryType_Type.__name__ = "Integer32"
_AgentLagSummaryType_Object = MibTableColumn
agentLagSummaryType = _AgentLagSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 2, 1, 10),
    _AgentLagSummaryType_Type()
)
agentLagSummaryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagSummaryType.setStatus("current")
_AgentLagDetailedConfigTable_Object = MibTable
agentLagDetailedConfigTable = _AgentLagDetailedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    agentLagDetailedConfigTable.setStatus("current")
_AgentLagDetailedConfigEntry_Object = MibTableRow
agentLagDetailedConfigEntry = _AgentLagDetailedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 3, 1)
)
agentLagDetailedConfigEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentLagDetailedLagIndex"),
    (0, "GSM7312-SWITCHING-MIB", "agentLagDetailedIfIndex"),
)
if mibBuilder.loadTexts:
    agentLagDetailedConfigEntry.setStatus("current")
_AgentLagDetailedLagIndex_Type = Integer32
_AgentLagDetailedLagIndex_Object = MibTableColumn
agentLagDetailedLagIndex = _AgentLagDetailedLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 3, 1, 1),
    _AgentLagDetailedLagIndex_Type()
)
agentLagDetailedLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedLagIndex.setStatus("current")
_AgentLagDetailedIfIndex_Type = Integer32
_AgentLagDetailedIfIndex_Object = MibTableColumn
agentLagDetailedIfIndex = _AgentLagDetailedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 3, 1, 2),
    _AgentLagDetailedIfIndex_Type()
)
agentLagDetailedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedIfIndex.setStatus("current")
_AgentLagDetailedPortSpeed_Type = ObjectIdentifier
_AgentLagDetailedPortSpeed_Object = MibTableColumn
agentLagDetailedPortSpeed = _AgentLagDetailedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 3, 1, 3),
    _AgentLagDetailedPortSpeed_Type()
)
agentLagDetailedPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedPortSpeed.setStatus("current")


class _AgentLagDetailedPortStatus_Type(Integer32):
    """Custom type agentLagDetailedPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentLagDetailedPortStatus_Type.__name__ = "Integer32"
_AgentLagDetailedPortStatus_Object = MibTableColumn
agentLagDetailedPortStatus = _AgentLagDetailedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 3, 1, 4),
    _AgentLagDetailedPortStatus_Type()
)
agentLagDetailedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedPortStatus.setStatus("current")


class _AgentLagConfigStaticCapability_Type(Integer32):
    """Custom type agentLagConfigStaticCapability based on Integer32"""
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


_AgentLagConfigStaticCapability_Type.__name__ = "Integer32"
_AgentLagConfigStaticCapability_Object = MibScalar
agentLagConfigStaticCapability = _AgentLagConfigStaticCapability_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 2, 4),
    _AgentLagConfigStaticCapability_Type()
)
agentLagConfigStaticCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagConfigStaticCapability.setStatus("current")
_AgentNetworkConfigGroup_ObjectIdentity = ObjectIdentity
agentNetworkConfigGroup = _AgentNetworkConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3)
)
_AgentNetworkIPAddress_Type = IpAddress
_AgentNetworkIPAddress_Object = MibScalar
agentNetworkIPAddress = _AgentNetworkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 1),
    _AgentNetworkIPAddress_Type()
)
agentNetworkIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkIPAddress.setStatus("current")
_AgentNetworkSubnetMask_Type = IpAddress
_AgentNetworkSubnetMask_Object = MibScalar
agentNetworkSubnetMask = _AgentNetworkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 2),
    _AgentNetworkSubnetMask_Type()
)
agentNetworkSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkSubnetMask.setStatus("current")
_AgentNetworkDefaultGateway_Type = IpAddress
_AgentNetworkDefaultGateway_Object = MibScalar
agentNetworkDefaultGateway = _AgentNetworkDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 3),
    _AgentNetworkDefaultGateway_Type()
)
agentNetworkDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDefaultGateway.setStatus("current")
_AgentNetworkBurnedInMacAddress_Type = PhysAddress
_AgentNetworkBurnedInMacAddress_Object = MibScalar
agentNetworkBurnedInMacAddress = _AgentNetworkBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 4),
    _AgentNetworkBurnedInMacAddress_Type()
)
agentNetworkBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkBurnedInMacAddress.setStatus("current")


class _AgentNetworkConfigProtocol_Type(Integer32):
    """Custom type agentNetworkConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_AgentNetworkConfigProtocol_Type.__name__ = "Integer32"
_AgentNetworkConfigProtocol_Object = MibScalar
agentNetworkConfigProtocol = _AgentNetworkConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 5),
    _AgentNetworkConfigProtocol_Type()
)
agentNetworkConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkConfigProtocol.setStatus("current")


class _AgentNetworkWebMode_Type(Integer32):
    """Custom type agentNetworkWebMode based on Integer32"""
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


_AgentNetworkWebMode_Type.__name__ = "Integer32"
_AgentNetworkWebMode_Object = MibScalar
agentNetworkWebMode = _AgentNetworkWebMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 6),
    _AgentNetworkWebMode_Type()
)
agentNetworkWebMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkWebMode.setStatus("current")


class _AgentNetworkJavaMode_Type(Integer32):
    """Custom type agentNetworkJavaMode based on Integer32"""
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


_AgentNetworkJavaMode_Type.__name__ = "Integer32"
_AgentNetworkJavaMode_Object = MibScalar
agentNetworkJavaMode = _AgentNetworkJavaMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 7),
    _AgentNetworkJavaMode_Type()
)
agentNetworkJavaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkJavaMode.setStatus("current")


class _AgentNetworkMgmtVlan_Type(Integer32):
    """Custom type agentNetworkMgmtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentNetworkMgmtVlan_Type.__name__ = "Integer32"
_AgentNetworkMgmtVlan_Object = MibScalar
agentNetworkMgmtVlan = _AgentNetworkMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 3, 8),
    _AgentNetworkMgmtVlan_Type()
)
agentNetworkMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkMgmtVlan.setStatus("current")
_AgentServicePortConfigGroup_ObjectIdentity = ObjectIdentity
agentServicePortConfigGroup = _AgentServicePortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 4)
)
_AgentServicePortIPAddress_Type = IpAddress
_AgentServicePortIPAddress_Object = MibScalar
agentServicePortIPAddress = _AgentServicePortIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 4, 1),
    _AgentServicePortIPAddress_Type()
)
agentServicePortIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortIPAddress.setStatus("current")
_AgentServicePortSubnetMask_Type = IpAddress
_AgentServicePortSubnetMask_Object = MibScalar
agentServicePortSubnetMask = _AgentServicePortSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 4, 2),
    _AgentServicePortSubnetMask_Type()
)
agentServicePortSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortSubnetMask.setStatus("current")
_AgentServicePortDefaultGateway_Type = IpAddress
_AgentServicePortDefaultGateway_Object = MibScalar
agentServicePortDefaultGateway = _AgentServicePortDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 4, 3),
    _AgentServicePortDefaultGateway_Type()
)
agentServicePortDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortDefaultGateway.setStatus("current")
_AgentServicePortBurnedInMacAddress_Type = PhysAddress
_AgentServicePortBurnedInMacAddress_Object = MibScalar
agentServicePortBurnedInMacAddress = _AgentServicePortBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 4, 4),
    _AgentServicePortBurnedInMacAddress_Type()
)
agentServicePortBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortBurnedInMacAddress.setStatus("current")


class _AgentServicePortConfigProtocol_Type(Integer32):
    """Custom type agentServicePortConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_AgentServicePortConfigProtocol_Type.__name__ = "Integer32"
_AgentServicePortConfigProtocol_Object = MibScalar
agentServicePortConfigProtocol = _AgentServicePortConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 4, 5),
    _AgentServicePortConfigProtocol_Type()
)
agentServicePortConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortConfigProtocol.setStatus("current")
_AgentSnmpConfigGroup_ObjectIdentity = ObjectIdentity
agentSnmpConfigGroup = _AgentSnmpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6)
)


class _AgentSnmpCommunityCreate_Type(DisplayString):
    """Custom type agentSnmpCommunityCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpCommunityCreate_Type.__name__ = "DisplayString"
_AgentSnmpCommunityCreate_Object = MibScalar
agentSnmpCommunityCreate = _AgentSnmpCommunityCreate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 1),
    _AgentSnmpCommunityCreate_Type()
)
agentSnmpCommunityCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityCreate.setStatus("current")
_AgentSnmpCommunityConfigTable_Object = MibTable
agentSnmpCommunityConfigTable = _AgentSnmpCommunityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    agentSnmpCommunityConfigTable.setStatus("current")
_AgentSnmpCommunityConfigEntry_Object = MibTableRow
agentSnmpCommunityConfigEntry = _AgentSnmpCommunityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2, 1)
)
agentSnmpCommunityConfigEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentSnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    agentSnmpCommunityConfigEntry.setStatus("current")
_AgentSnmpCommunityIndex_Type = Integer32
_AgentSnmpCommunityIndex_Object = MibTableColumn
agentSnmpCommunityIndex = _AgentSnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2, 1, 1),
    _AgentSnmpCommunityIndex_Type()
)
agentSnmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSnmpCommunityIndex.setStatus("current")


class _AgentSnmpCommunityName_Type(DisplayString):
    """Custom type agentSnmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpCommunityName_Type.__name__ = "DisplayString"
_AgentSnmpCommunityName_Object = MibTableColumn
agentSnmpCommunityName = _AgentSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2, 1, 2),
    _AgentSnmpCommunityName_Type()
)
agentSnmpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityName.setStatus("current")
_AgentSnmpCommunityIPAddress_Type = IpAddress
_AgentSnmpCommunityIPAddress_Object = MibTableColumn
agentSnmpCommunityIPAddress = _AgentSnmpCommunityIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2, 1, 3),
    _AgentSnmpCommunityIPAddress_Type()
)
agentSnmpCommunityIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityIPAddress.setStatus("current")
_AgentSnmpCommunityIPMask_Type = IpAddress
_AgentSnmpCommunityIPMask_Object = MibTableColumn
agentSnmpCommunityIPMask = _AgentSnmpCommunityIPMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2, 1, 4),
    _AgentSnmpCommunityIPMask_Type()
)
agentSnmpCommunityIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityIPMask.setStatus("current")


class _AgentSnmpCommunityAccessMode_Type(Integer32):
    """Custom type agentSnmpCommunityAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_AgentSnmpCommunityAccessMode_Type.__name__ = "Integer32"
_AgentSnmpCommunityAccessMode_Object = MibTableColumn
agentSnmpCommunityAccessMode = _AgentSnmpCommunityAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2, 1, 5),
    _AgentSnmpCommunityAccessMode_Type()
)
agentSnmpCommunityAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityAccessMode.setStatus("current")


class _AgentSnmpCommunityStatus_Type(Integer32):
    """Custom type agentSnmpCommunityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("config", 3),
          ("destroy", 4),
          ("notInService", 2))
    )


_AgentSnmpCommunityStatus_Type.__name__ = "Integer32"
_AgentSnmpCommunityStatus_Object = MibTableColumn
agentSnmpCommunityStatus = _AgentSnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 2, 1, 6),
    _AgentSnmpCommunityStatus_Type()
)
agentSnmpCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityStatus.setStatus("current")


class _AgentSnmpTrapReceiverCreate_Type(DisplayString):
    """Custom type agentSnmpTrapReceiverCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpTrapReceiverCreate_Type.__name__ = "DisplayString"
_AgentSnmpTrapReceiverCreate_Object = MibScalar
agentSnmpTrapReceiverCreate = _AgentSnmpTrapReceiverCreate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 3),
    _AgentSnmpTrapReceiverCreate_Type()
)
agentSnmpTrapReceiverCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverCreate.setStatus("current")
_AgentSnmpTrapReceiverConfigTable_Object = MibTable
agentSnmpTrapReceiverConfigTable = _AgentSnmpTrapReceiverConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverConfigTable.setStatus("current")
_AgentSnmpTrapReceiverConfigEntry_Object = MibTableRow
agentSnmpTrapReceiverConfigEntry = _AgentSnmpTrapReceiverConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 4, 1)
)
agentSnmpTrapReceiverConfigEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentSnmpTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverConfigEntry.setStatus("current")
_AgentSnmpTrapReceiverIndex_Type = Integer32
_AgentSnmpTrapReceiverIndex_Object = MibTableColumn
agentSnmpTrapReceiverIndex = _AgentSnmpTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 4, 1, 1),
    _AgentSnmpTrapReceiverIndex_Type()
)
agentSnmpTrapReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverIndex.setStatus("current")


class _AgentSnmpTrapReceiverCommunityName_Type(DisplayString):
    """Custom type agentSnmpTrapReceiverCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpTrapReceiverCommunityName_Type.__name__ = "DisplayString"
_AgentSnmpTrapReceiverCommunityName_Object = MibTableColumn
agentSnmpTrapReceiverCommunityName = _AgentSnmpTrapReceiverCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 4, 1, 2),
    _AgentSnmpTrapReceiverCommunityName_Type()
)
agentSnmpTrapReceiverCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverCommunityName.setStatus("current")
_AgentSnmpTrapReceiverIPAddress_Type = IpAddress
_AgentSnmpTrapReceiverIPAddress_Object = MibTableColumn
agentSnmpTrapReceiverIPAddress = _AgentSnmpTrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 4, 1, 3),
    _AgentSnmpTrapReceiverIPAddress_Type()
)
agentSnmpTrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverIPAddress.setStatus("current")


class _AgentSnmpTrapReceiverStatus_Type(Integer32):
    """Custom type agentSnmpTrapReceiverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("config", 3),
          ("destroy", 4),
          ("notInService", 2))
    )


_AgentSnmpTrapReceiverStatus_Type.__name__ = "Integer32"
_AgentSnmpTrapReceiverStatus_Object = MibTableColumn
agentSnmpTrapReceiverStatus = _AgentSnmpTrapReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 4, 1, 4),
    _AgentSnmpTrapReceiverStatus_Type()
)
agentSnmpTrapReceiverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverStatus.setStatus("current")
_AgentSnmpTrapFlagsConfigGroup_ObjectIdentity = ObjectIdentity
agentSnmpTrapFlagsConfigGroup = _AgentSnmpTrapFlagsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 5)
)


class _AgentSnmpAuthenticationTrapFlag_Type(Integer32):
    """Custom type agentSnmpAuthenticationTrapFlag based on Integer32"""
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


_AgentSnmpAuthenticationTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpAuthenticationTrapFlag_Object = MibScalar
agentSnmpAuthenticationTrapFlag = _AgentSnmpAuthenticationTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 5, 1),
    _AgentSnmpAuthenticationTrapFlag_Type()
)
agentSnmpAuthenticationTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpAuthenticationTrapFlag.setStatus("current")


class _AgentSnmpLinkUpDownTrapFlag_Type(Integer32):
    """Custom type agentSnmpLinkUpDownTrapFlag based on Integer32"""
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


_AgentSnmpLinkUpDownTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpLinkUpDownTrapFlag_Object = MibScalar
agentSnmpLinkUpDownTrapFlag = _AgentSnmpLinkUpDownTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 5, 2),
    _AgentSnmpLinkUpDownTrapFlag_Type()
)
agentSnmpLinkUpDownTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpLinkUpDownTrapFlag.setStatus("current")


class _AgentSnmpMultipleUsersTrapFlag_Type(Integer32):
    """Custom type agentSnmpMultipleUsersTrapFlag based on Integer32"""
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


_AgentSnmpMultipleUsersTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpMultipleUsersTrapFlag_Object = MibScalar
agentSnmpMultipleUsersTrapFlag = _AgentSnmpMultipleUsersTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 5, 3),
    _AgentSnmpMultipleUsersTrapFlag_Type()
)
agentSnmpMultipleUsersTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpMultipleUsersTrapFlag.setStatus("current")


class _AgentSnmpSpanningTreeTrapFlag_Type(Integer32):
    """Custom type agentSnmpSpanningTreeTrapFlag based on Integer32"""
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


_AgentSnmpSpanningTreeTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpSpanningTreeTrapFlag_Object = MibScalar
agentSnmpSpanningTreeTrapFlag = _AgentSnmpSpanningTreeTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 5, 4),
    _AgentSnmpSpanningTreeTrapFlag_Type()
)
agentSnmpSpanningTreeTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpSpanningTreeTrapFlag.setStatus("current")


class _AgentSnmpBroadcastStormTrapFlag_Type(Integer32):
    """Custom type agentSnmpBroadcastStormTrapFlag based on Integer32"""
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


_AgentSnmpBroadcastStormTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpBroadcastStormTrapFlag_Object = MibScalar
agentSnmpBroadcastStormTrapFlag = _AgentSnmpBroadcastStormTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 6, 5, 5),
    _AgentSnmpBroadcastStormTrapFlag_Type()
)
agentSnmpBroadcastStormTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpBroadcastStormTrapFlag.setStatus("current")
_AgentSpanningTreeConfigGroup_ObjectIdentity = ObjectIdentity
agentSpanningTreeConfigGroup = _AgentSpanningTreeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 7)
)


class _AgentSpanningTreeMode_Type(Integer32):
    """Custom type agentSpanningTreeMode based on Integer32"""
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


_AgentSpanningTreeMode_Type.__name__ = "Integer32"
_AgentSpanningTreeMode_Object = MibScalar
agentSpanningTreeMode = _AgentSpanningTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 7, 1),
    _AgentSpanningTreeMode_Type()
)
agentSpanningTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSpanningTreeMode.setStatus("current")
_AgentSwitchConfigGroup_ObjectIdentity = ObjectIdentity
agentSwitchConfigGroup = _AgentSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8)
)


class _AgentSwitchBroadcastControlMode_Type(Integer32):
    """Custom type agentSwitchBroadcastControlMode based on Integer32"""
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


_AgentSwitchBroadcastControlMode_Type.__name__ = "Integer32"
_AgentSwitchBroadcastControlMode_Object = MibScalar
agentSwitchBroadcastControlMode = _AgentSwitchBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 2),
    _AgentSwitchBroadcastControlMode_Type()
)
agentSwitchBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBroadcastControlMode.setStatus("current")


class _AgentSwitchDot3FlowControlMode_Type(Integer32):
    """Custom type agentSwitchDot3FlowControlMode based on Integer32"""
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


_AgentSwitchDot3FlowControlMode_Type.__name__ = "Integer32"
_AgentSwitchDot3FlowControlMode_Object = MibScalar
agentSwitchDot3FlowControlMode = _AgentSwitchDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 3),
    _AgentSwitchDot3FlowControlMode_Type()
)
agentSwitchDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDot3FlowControlMode.setStatus("current")
_AgentSwitchAddressAgingTimeoutTable_Object = MibTable
agentSwitchAddressAgingTimeoutTable = _AgentSwitchAddressAgingTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeoutTable.setStatus("current")
_AgentSwitchAddressAgingTimeoutEntry_Object = MibTableRow
agentSwitchAddressAgingTimeoutEntry = _AgentSwitchAddressAgingTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 4, 1)
)
agentSwitchAddressAgingTimeoutEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeoutEntry.setStatus("current")


class _AgentSwitchAddressAgingTimeout_Type(Integer32):
    """Custom type agentSwitchAddressAgingTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AgentSwitchAddressAgingTimeout_Type.__name__ = "Integer32"
_AgentSwitchAddressAgingTimeout_Object = MibTableColumn
agentSwitchAddressAgingTimeout = _AgentSwitchAddressAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 4, 1, 1),
    _AgentSwitchAddressAgingTimeout_Type()
)
agentSwitchAddressAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeout.setStatus("current")
_AgentSwitchIGMPSnoopingGroup_ObjectIdentity = ObjectIdentity
agentSwitchIGMPSnoopingGroup = _AgentSwitchIGMPSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 6)
)


class _AgentSwitchIGMPSnoopingAdminMode_Type(Integer32):
    """Custom type agentSwitchIGMPSnoopingAdminMode based on Integer32"""
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


_AgentSwitchIGMPSnoopingAdminMode_Type.__name__ = "Integer32"
_AgentSwitchIGMPSnoopingAdminMode_Object = MibScalar
agentSwitchIGMPSnoopingAdminMode = _AgentSwitchIGMPSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 6, 1),
    _AgentSwitchIGMPSnoopingAdminMode_Type()
)
agentSwitchIGMPSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIGMPSnoopingAdminMode.setStatus("current")


class _AgentSwitchIGMPSnoopingGroupMembershipInterval_Type(Integer32):
    """Custom type agentSwitchIGMPSnoopingGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AgentSwitchIGMPSnoopingGroupMembershipInterval_Type.__name__ = "Integer32"
_AgentSwitchIGMPSnoopingGroupMembershipInterval_Object = MibScalar
agentSwitchIGMPSnoopingGroupMembershipInterval = _AgentSwitchIGMPSnoopingGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 6, 2),
    _AgentSwitchIGMPSnoopingGroupMembershipInterval_Type()
)
agentSwitchIGMPSnoopingGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIGMPSnoopingGroupMembershipInterval.setStatus("current")


class _AgentSwitchIGMPSnoopingMaxResponseTime_Type(Integer32):
    """Custom type agentSwitchIGMPSnoopingMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AgentSwitchIGMPSnoopingMaxResponseTime_Type.__name__ = "Integer32"
_AgentSwitchIGMPSnoopingMaxResponseTime_Object = MibScalar
agentSwitchIGMPSnoopingMaxResponseTime = _AgentSwitchIGMPSnoopingMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 6, 3),
    _AgentSwitchIGMPSnoopingMaxResponseTime_Type()
)
agentSwitchIGMPSnoopingMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIGMPSnoopingMaxResponseTime.setStatus("current")


class _AgentSwitchIGMPSnoopingMRPExpirationTime_Type(Integer32):
    """Custom type agentSwitchIGMPSnoopingMRPExpirationTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AgentSwitchIGMPSnoopingMRPExpirationTime_Type.__name__ = "Integer32"
_AgentSwitchIGMPSnoopingMRPExpirationTime_Object = MibScalar
agentSwitchIGMPSnoopingMRPExpirationTime = _AgentSwitchIGMPSnoopingMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 6, 4),
    _AgentSwitchIGMPSnoopingMRPExpirationTime_Type()
)
agentSwitchIGMPSnoopingMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIGMPSnoopingMRPExpirationTime.setStatus("current")


class _AgentSwitchIGMPSnoopingPortMask_Type(AgentPortMask):
    """Custom type agentSwitchIGMPSnoopingPortMask based on AgentPortMask"""
    defaultHexValue = "000000000000"


_AgentSwitchIGMPSnoopingPortMask_Object = MibScalar
agentSwitchIGMPSnoopingPortMask = _AgentSwitchIGMPSnoopingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 6, 5),
    _AgentSwitchIGMPSnoopingPortMask_Type()
)
agentSwitchIGMPSnoopingPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIGMPSnoopingPortMask.setStatus("current")
_AgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Type = Counter32
_AgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Object = MibScalar
agentSwitchIGMPSnoopingMulticastControlFramesProcessed = _AgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 6, 6),
    _AgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Type()
)
agentSwitchIGMPSnoopingMulticastControlFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIGMPSnoopingMulticastControlFramesProcessed.setStatus("current")
_AgentSwitchMFDBGroup_ObjectIdentity = ObjectIdentity
agentSwitchMFDBGroup = _AgentSwitchMFDBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7)
)
_AgentSwitchMFDBTable_Object = MibTable
agentSwitchMFDBTable = _AgentSwitchMFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1)
)
if mibBuilder.loadTexts:
    agentSwitchMFDBTable.setStatus("current")
_AgentSwitchMFDBEntry_Object = MibTableRow
agentSwitchMFDBEntry = _AgentSwitchMFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1)
)
agentSwitchMFDBEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentSwitchMFDBVlanId"),
    (0, "GSM7312-SWITCHING-MIB", "agentSwitchMFDBMacAddress"),
    (0, "GSM7312-SWITCHING-MIB", "agentSwitchMFDBProtocolType"),
)
if mibBuilder.loadTexts:
    agentSwitchMFDBEntry.setStatus("current")
_AgentSwitchMFDBVlanId_Type = VlanIndex
_AgentSwitchMFDBVlanId_Object = MibTableColumn
agentSwitchMFDBVlanId = _AgentSwitchMFDBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1, 1),
    _AgentSwitchMFDBVlanId_Type()
)
agentSwitchMFDBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBVlanId.setStatus("current")
_AgentSwitchMFDBMacAddress_Type = MacAddress
_AgentSwitchMFDBMacAddress_Object = MibTableColumn
agentSwitchMFDBMacAddress = _AgentSwitchMFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1, 2),
    _AgentSwitchMFDBMacAddress_Type()
)
agentSwitchMFDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBMacAddress.setStatus("current")


class _AgentSwitchMFDBProtocolType_Type(Integer32):
    """Custom type agentSwitchMFDBProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gmrp", 2),
          ("igmp", 3),
          ("static", 1))
    )


_AgentSwitchMFDBProtocolType_Type.__name__ = "Integer32"
_AgentSwitchMFDBProtocolType_Object = MibTableColumn
agentSwitchMFDBProtocolType = _AgentSwitchMFDBProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1, 3),
    _AgentSwitchMFDBProtocolType_Type()
)
agentSwitchMFDBProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBProtocolType.setStatus("current")


class _AgentSwitchMFDBType_Type(Integer32):
    """Custom type agentSwitchMFDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AgentSwitchMFDBType_Type.__name__ = "Integer32"
_AgentSwitchMFDBType_Object = MibTableColumn
agentSwitchMFDBType = _AgentSwitchMFDBType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1, 4),
    _AgentSwitchMFDBType_Type()
)
agentSwitchMFDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBType.setStatus("current")
_AgentSwitchMFDBDescription_Type = DisplayString
_AgentSwitchMFDBDescription_Object = MibTableColumn
agentSwitchMFDBDescription = _AgentSwitchMFDBDescription_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1, 5),
    _AgentSwitchMFDBDescription_Type()
)
agentSwitchMFDBDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBDescription.setStatus("current")
_AgentSwitchMFDBForwardingPortMask_Type = AgentPortMask
_AgentSwitchMFDBForwardingPortMask_Object = MibTableColumn
agentSwitchMFDBForwardingPortMask = _AgentSwitchMFDBForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1, 6),
    _AgentSwitchMFDBForwardingPortMask_Type()
)
agentSwitchMFDBForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBForwardingPortMask.setStatus("current")
_AgentSwitchMFDBFilteringPortMask_Type = AgentPortMask
_AgentSwitchMFDBFilteringPortMask_Object = MibTableColumn
agentSwitchMFDBFilteringPortMask = _AgentSwitchMFDBFilteringPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 1, 1, 7),
    _AgentSwitchMFDBFilteringPortMask_Type()
)
agentSwitchMFDBFilteringPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBFilteringPortMask.setStatus("current")
_AgentSwitchMFDBSummaryTable_Object = MibTable
agentSwitchMFDBSummaryTable = _AgentSwitchMFDBSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 2)
)
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryTable.setStatus("current")
_AgentSwitchMFDBSummaryEntry_Object = MibTableRow
agentSwitchMFDBSummaryEntry = _AgentSwitchMFDBSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 2, 1)
)
agentSwitchMFDBSummaryEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentSwitchMFDBSummaryVlanId"),
    (0, "GSM7312-SWITCHING-MIB", "agentSwitchMFDBSummaryMacAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryEntry.setStatus("current")
_AgentSwitchMFDBSummaryVlanId_Type = VlanIndex
_AgentSwitchMFDBSummaryVlanId_Object = MibTableColumn
agentSwitchMFDBSummaryVlanId = _AgentSwitchMFDBSummaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 2, 1, 1),
    _AgentSwitchMFDBSummaryVlanId_Type()
)
agentSwitchMFDBSummaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryVlanId.setStatus("current")
_AgentSwitchMFDBSummaryMacAddress_Type = MacAddress
_AgentSwitchMFDBSummaryMacAddress_Object = MibTableColumn
agentSwitchMFDBSummaryMacAddress = _AgentSwitchMFDBSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 2, 1, 2),
    _AgentSwitchMFDBSummaryMacAddress_Type()
)
agentSwitchMFDBSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryMacAddress.setStatus("current")
_AgentSwitchMFDBSummaryForwardingPortMask_Type = AgentPortMask
_AgentSwitchMFDBSummaryForwardingPortMask_Object = MibTableColumn
agentSwitchMFDBSummaryForwardingPortMask = _AgentSwitchMFDBSummaryForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 2, 1, 3),
    _AgentSwitchMFDBSummaryForwardingPortMask_Type()
)
agentSwitchMFDBSummaryForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryForwardingPortMask.setStatus("current")
_AgentSwitchMFDBMaxTableEntries_Type = Gauge32
_AgentSwitchMFDBMaxTableEntries_Object = MibScalar
agentSwitchMFDBMaxTableEntries = _AgentSwitchMFDBMaxTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 3),
    _AgentSwitchMFDBMaxTableEntries_Type()
)
agentSwitchMFDBMaxTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBMaxTableEntries.setStatus("current")
_AgentSwitchMFDBMostEntriesUsed_Type = Gauge32
_AgentSwitchMFDBMostEntriesUsed_Object = MibScalar
agentSwitchMFDBMostEntriesUsed = _AgentSwitchMFDBMostEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 4),
    _AgentSwitchMFDBMostEntriesUsed_Type()
)
agentSwitchMFDBMostEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBMostEntriesUsed.setStatus("current")
_AgentSwitchMFDBCurrentEntries_Type = Gauge32
_AgentSwitchMFDBCurrentEntries_Object = MibScalar
agentSwitchMFDBCurrentEntries = _AgentSwitchMFDBCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 8, 7, 5),
    _AgentSwitchMFDBCurrentEntries_Type()
)
agentSwitchMFDBCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBCurrentEntries.setStatus("current")
_AgentTransferConfigGroup_ObjectIdentity = ObjectIdentity
agentTransferConfigGroup = _AgentTransferConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9)
)
_AgentTransferUploadGroup_ObjectIdentity = ObjectIdentity
agentTransferUploadGroup = _AgentTransferUploadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1)
)


class _AgentTransferUploadMode_Type(Integer32):
    """Custom type agentTransferUploadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_AgentTransferUploadMode_Type.__name__ = "Integer32"
_AgentTransferUploadMode_Object = MibScalar
agentTransferUploadMode = _AgentTransferUploadMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1, 1),
    _AgentTransferUploadMode_Type()
)
agentTransferUploadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadMode.setStatus("current")
_AgentTransferUploadServerIP_Type = IpAddress
_AgentTransferUploadServerIP_Object = MibScalar
agentTransferUploadServerIP = _AgentTransferUploadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1, 2),
    _AgentTransferUploadServerIP_Type()
)
agentTransferUploadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadServerIP.setStatus("current")


class _AgentTransferUploadPath_Type(DisplayString):
    """Custom type agentTransferUploadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferUploadPath_Type.__name__ = "DisplayString"
_AgentTransferUploadPath_Object = MibScalar
agentTransferUploadPath = _AgentTransferUploadPath_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1, 3),
    _AgentTransferUploadPath_Type()
)
agentTransferUploadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadPath.setStatus("current")


class _AgentTransferUploadFilename_Type(DisplayString):
    """Custom type agentTransferUploadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferUploadFilename_Type.__name__ = "DisplayString"
_AgentTransferUploadFilename_Object = MibScalar
agentTransferUploadFilename = _AgentTransferUploadFilename_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1, 4),
    _AgentTransferUploadFilename_Type()
)
agentTransferUploadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadFilename.setStatus("current")


class _AgentTransferUploadDataType_Type(Integer32):
    """Custom type agentTransferUploadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("errorlog", 3),
          ("messagelog", 4),
          ("traplog", 5))
    )


_AgentTransferUploadDataType_Type.__name__ = "Integer32"
_AgentTransferUploadDataType_Object = MibScalar
agentTransferUploadDataType = _AgentTransferUploadDataType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1, 5),
    _AgentTransferUploadDataType_Type()
)
agentTransferUploadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadDataType.setStatus("current")


class _AgentTransferUploadStart_Type(Integer32):
    """Custom type agentTransferUploadStart based on Integer32"""
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


_AgentTransferUploadStart_Type.__name__ = "Integer32"
_AgentTransferUploadStart_Object = MibScalar
agentTransferUploadStart = _AgentTransferUploadStart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1, 6),
    _AgentTransferUploadStart_Type()
)
agentTransferUploadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadStart.setStatus("current")


class _AgentTransferUploadStatus_Type(Integer32):
    """Custom type agentTransferUploadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_AgentTransferUploadStatus_Type.__name__ = "Integer32"
_AgentTransferUploadStatus_Object = MibScalar
agentTransferUploadStatus = _AgentTransferUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 1, 7),
    _AgentTransferUploadStatus_Type()
)
agentTransferUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferUploadStatus.setStatus("current")
_AgentTransferDownloadGroup_ObjectIdentity = ObjectIdentity
agentTransferDownloadGroup = _AgentTransferDownloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2)
)


class _AgentTransferDownloadMode_Type(Integer32):
    """Custom type agentTransferDownloadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_AgentTransferDownloadMode_Type.__name__ = "Integer32"
_AgentTransferDownloadMode_Object = MibScalar
agentTransferDownloadMode = _AgentTransferDownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2, 1),
    _AgentTransferDownloadMode_Type()
)
agentTransferDownloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadMode.setStatus("current")
_AgentTransferDownloadServerIP_Type = IpAddress
_AgentTransferDownloadServerIP_Object = MibScalar
agentTransferDownloadServerIP = _AgentTransferDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2, 2),
    _AgentTransferDownloadServerIP_Type()
)
agentTransferDownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadServerIP.setStatus("current")


class _AgentTransferDownloadPath_Type(DisplayString):
    """Custom type agentTransferDownloadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferDownloadPath_Type.__name__ = "DisplayString"
_AgentTransferDownloadPath_Object = MibScalar
agentTransferDownloadPath = _AgentTransferDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2, 3),
    _AgentTransferDownloadPath_Type()
)
agentTransferDownloadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadPath.setStatus("current")


class _AgentTransferDownloadFilename_Type(DisplayString):
    """Custom type agentTransferDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferDownloadFilename_Type.__name__ = "DisplayString"
_AgentTransferDownloadFilename_Object = MibScalar
agentTransferDownloadFilename = _AgentTransferDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2, 4),
    _AgentTransferDownloadFilename_Type()
)
agentTransferDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadFilename.setStatus("current")


class _AgentTransferDownloadDataType_Type(Integer32):
    """Custom type agentTransferDownloadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("code", 2),
          ("config", 3),
          ("sshkey-dsa", 6),
          ("sshkey-rsa1", 4),
          ("sshkey-rsa2", 5),
          ("sslpem-dhstrong", 10),
          ("sslpem-dhweak", 9),
          ("sslpem-root", 7),
          ("sslpem-server", 8))
    )


_AgentTransferDownloadDataType_Type.__name__ = "Integer32"
_AgentTransferDownloadDataType_Object = MibScalar
agentTransferDownloadDataType = _AgentTransferDownloadDataType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2, 5),
    _AgentTransferDownloadDataType_Type()
)
agentTransferDownloadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadDataType.setStatus("current")


class _AgentTransferDownloadStart_Type(Integer32):
    """Custom type agentTransferDownloadStart based on Integer32"""
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


_AgentTransferDownloadStart_Type.__name__ = "Integer32"
_AgentTransferDownloadStart_Object = MibScalar
agentTransferDownloadStart = _AgentTransferDownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2, 6),
    _AgentTransferDownloadStart_Type()
)
agentTransferDownloadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadStart.setStatus("current")


class _AgentTransferDownloadStatus_Type(Integer32):
    """Custom type agentTransferDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_AgentTransferDownloadStatus_Type.__name__ = "Integer32"
_AgentTransferDownloadStatus_Object = MibScalar
agentTransferDownloadStatus = _AgentTransferDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 9, 2, 7),
    _AgentTransferDownloadStatus_Type()
)
agentTransferDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferDownloadStatus.setStatus("current")
_AgentPortMirroringGroup_ObjectIdentity = ObjectIdentity
agentPortMirroringGroup = _AgentPortMirroringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 10)
)


class _AgentMirroredPortIfIndex_Type(Integer32):
    """Custom type agentMirroredPortIfIndex based on Integer32"""
    defaultValue = 0


_AgentMirroredPortIfIndex_Object = MibScalar
agentMirroredPortIfIndex = _AgentMirroredPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 10, 1),
    _AgentMirroredPortIfIndex_Type()
)
agentMirroredPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMirroredPortIfIndex.setStatus("current")


class _AgentProbePortIfIndex_Type(Integer32):
    """Custom type agentProbePortIfIndex based on Integer32"""
    defaultValue = 0


_AgentProbePortIfIndex_Object = MibScalar
agentProbePortIfIndex = _AgentProbePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 10, 2),
    _AgentProbePortIfIndex_Type()
)
agentProbePortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProbePortIfIndex.setStatus("current")


class _AgentPortMirroringMode_Type(Integer32):
    """Custom type agentPortMirroringMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_AgentPortMirroringMode_Type.__name__ = "Integer32"
_AgentPortMirroringMode_Object = MibScalar
agentPortMirroringMode = _AgentPortMirroringMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 10, 3),
    _AgentPortMirroringMode_Type()
)
agentPortMirroringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirroringMode.setStatus("current")
_AgentDot3adAggPortTable_Object = MibTable
agentDot3adAggPortTable = _AgentDot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 12)
)
if mibBuilder.loadTexts:
    agentDot3adAggPortTable.setStatus("current")
_AgentDot3adAggPortEntry_Object = MibTableRow
agentDot3adAggPortEntry = _AgentDot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 12, 1)
)
agentDot3adAggPortEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentDot3adAggPort"),
)
if mibBuilder.loadTexts:
    agentDot3adAggPortEntry.setStatus("current")
_AgentDot3adAggPort_Type = Integer32
_AgentDot3adAggPort_Object = MibTableColumn
agentDot3adAggPort = _AgentDot3adAggPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 12, 1, 1),
    _AgentDot3adAggPort_Type()
)
agentDot3adAggPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot3adAggPort.setStatus("current")


class _AgentDot3adAggPortLACPMode_Type(Integer32):
    """Custom type agentDot3adAggPortLACPMode based on Integer32"""
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


_AgentDot3adAggPortLACPMode_Type.__name__ = "Integer32"
_AgentDot3adAggPortLACPMode_Object = MibTableColumn
agentDot3adAggPortLACPMode = _AgentDot3adAggPortLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 12, 1, 2),
    _AgentDot3adAggPortLACPMode_Type()
)
agentDot3adAggPortLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot3adAggPortLACPMode.setStatus("current")
_AgentPortConfigTable_Object = MibTable
agentPortConfigTable = _AgentPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13)
)
if mibBuilder.loadTexts:
    agentPortConfigTable.setStatus("current")
_AgentPortConfigEntry_Object = MibTableRow
agentPortConfigEntry = _AgentPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1)
)
agentPortConfigEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    agentPortConfigEntry.setStatus("current")


class _AgentPortDot1dBasePort_Type(Integer32):
    """Custom type agentPortDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentPortDot1dBasePort_Type.__name__ = "Integer32"
_AgentPortDot1dBasePort_Object = MibTableColumn
agentPortDot1dBasePort = _AgentPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 1),
    _AgentPortDot1dBasePort_Type()
)
agentPortDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortDot1dBasePort.setStatus("current")
_AgentPortIfIndex_Type = Integer32
_AgentPortIfIndex_Object = MibTableColumn
agentPortIfIndex = _AgentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 2),
    _AgentPortIfIndex_Type()
)
agentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortIfIndex.setStatus("current")
_AgentPortIanaType_Type = IANAifType
_AgentPortIanaType_Object = MibTableColumn
agentPortIanaType = _AgentPortIanaType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 3),
    _AgentPortIanaType_Type()
)
agentPortIanaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortIanaType.setStatus("current")


class _AgentPortSTPMode_Type(Integer32):
    """Custom type agentPortSTPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("fast", 2),
          ("off", 3))
    )


_AgentPortSTPMode_Type.__name__ = "Integer32"
_AgentPortSTPMode_Object = MibTableColumn
agentPortSTPMode = _AgentPortSTPMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 4),
    _AgentPortSTPMode_Type()
)
agentPortSTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSTPMode.setStatus("current")


class _AgentPortSTPState_Type(Integer32):
    """Custom type agentPortSTPState based on Integer32"""
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
        *(("blocking", 1),
          ("disabled", 5),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )


_AgentPortSTPState_Type.__name__ = "Integer32"
_AgentPortSTPState_Object = MibTableColumn
agentPortSTPState = _AgentPortSTPState_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 5),
    _AgentPortSTPState_Type()
)
agentPortSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortSTPState.setStatus("current")


class _AgentPortAdminMode_Type(Integer32):
    """Custom type agentPortAdminMode based on Integer32"""
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


_AgentPortAdminMode_Type.__name__ = "Integer32"
_AgentPortAdminMode_Object = MibTableColumn
agentPortAdminMode = _AgentPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 6),
    _AgentPortAdminMode_Type()
)
agentPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortAdminMode.setStatus("current")


class _AgentPortPhysicalMode_Type(Integer32):
    """Custom type agentPortPhysicalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000sx", 8),
          ("full-100fx", 7),
          ("half-10", 2),
          ("half-100", 4),
          ("half-100fx", 6))
    )


_AgentPortPhysicalMode_Type.__name__ = "Integer32"
_AgentPortPhysicalMode_Object = MibTableColumn
agentPortPhysicalMode = _AgentPortPhysicalMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 7),
    _AgentPortPhysicalMode_Type()
)
agentPortPhysicalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortPhysicalMode.setStatus("obsolete")


class _AgentPortPhysicalStatus_Type(Integer32):
    """Custom type agentPortPhysicalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000sx", 8),
          ("full-100fx", 7),
          ("half-10", 2),
          ("half-100", 4),
          ("half-100fx", 6))
    )


_AgentPortPhysicalStatus_Type.__name__ = "Integer32"
_AgentPortPhysicalStatus_Object = MibTableColumn
agentPortPhysicalStatus = _AgentPortPhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 8),
    _AgentPortPhysicalStatus_Type()
)
agentPortPhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortPhysicalStatus.setStatus("obsolete")


class _AgentPortLinkTrapMode_Type(Integer32):
    """Custom type agentPortLinkTrapMode based on Integer32"""
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


_AgentPortLinkTrapMode_Type.__name__ = "Integer32"
_AgentPortLinkTrapMode_Object = MibTableColumn
agentPortLinkTrapMode = _AgentPortLinkTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 9),
    _AgentPortLinkTrapMode_Type()
)
agentPortLinkTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortLinkTrapMode.setStatus("current")


class _AgentPortClearStats_Type(Integer32):
    """Custom type agentPortClearStats based on Integer32"""
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


_AgentPortClearStats_Type.__name__ = "Integer32"
_AgentPortClearStats_Object = MibTableColumn
agentPortClearStats = _AgentPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 10),
    _AgentPortClearStats_Type()
)
agentPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortClearStats.setStatus("current")
_AgentPortDefaultType_Type = ObjectIdentifier
_AgentPortDefaultType_Object = MibTableColumn
agentPortDefaultType = _AgentPortDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 11),
    _AgentPortDefaultType_Type()
)
agentPortDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDefaultType.setStatus("current")
_AgentPortType_Type = ObjectIdentifier
_AgentPortType_Object = MibTableColumn
agentPortType = _AgentPortType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 12),
    _AgentPortType_Type()
)
agentPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortType.setStatus("current")


class _AgentPortAutoNegAdminStatus_Type(Integer32):
    """Custom type agentPortAutoNegAdminStatus based on Integer32"""
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


_AgentPortAutoNegAdminStatus_Type.__name__ = "Integer32"
_AgentPortAutoNegAdminStatus_Object = MibTableColumn
agentPortAutoNegAdminStatus = _AgentPortAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 13),
    _AgentPortAutoNegAdminStatus_Type()
)
agentPortAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortAutoNegAdminStatus.setStatus("current")


class _AgentPortDot3FlowControlMode_Type(Integer32):
    """Custom type agentPortDot3FlowControlMode based on Integer32"""
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


_AgentPortDot3FlowControlMode_Type.__name__ = "Integer32"
_AgentPortDot3FlowControlMode_Object = MibTableColumn
agentPortDot3FlowControlMode = _AgentPortDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 14),
    _AgentPortDot3FlowControlMode_Type()
)
agentPortDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDot3FlowControlMode.setStatus("current")


class _AgentPortDVlanTagMode_Type(Integer32):
    """Custom type agentPortDVlanTagMode based on Integer32"""
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


_AgentPortDVlanTagMode_Type.__name__ = "Integer32"
_AgentPortDVlanTagMode_Object = MibTableColumn
agentPortDVlanTagMode = _AgentPortDVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 15),
    _AgentPortDVlanTagMode_Type()
)
agentPortDVlanTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDVlanTagMode.setStatus("current")


class _AgentPortDVlanTagEthertype_Type(Integer32):
    """Custom type agentPortDVlanTagEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentPortDVlanTagEthertype_Type.__name__ = "Integer32"
_AgentPortDVlanTagEthertype_Object = MibTableColumn
agentPortDVlanTagEthertype = _AgentPortDVlanTagEthertype_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 16),
    _AgentPortDVlanTagEthertype_Type()
)
agentPortDVlanTagEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDVlanTagEthertype.setStatus("current")
_AgentPortDVlanTagCustomerId_Type = Integer32
_AgentPortDVlanTagCustomerId_Object = MibTableColumn
agentPortDVlanTagCustomerId = _AgentPortDVlanTagCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 17),
    _AgentPortDVlanTagCustomerId_Type()
)
agentPortDVlanTagCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDVlanTagCustomerId.setStatus("current")
_AgentPortMaxFrameSizeLimit_Type = Integer32
_AgentPortMaxFrameSizeLimit_Object = MibTableColumn
agentPortMaxFrameSizeLimit = _AgentPortMaxFrameSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 18),
    _AgentPortMaxFrameSizeLimit_Type()
)
agentPortMaxFrameSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortMaxFrameSizeLimit.setStatus("current")
_AgentPortMaxFrameSize_Type = Integer32
_AgentPortMaxFrameSize_Object = MibTableColumn
agentPortMaxFrameSize = _AgentPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 13, 1, 19),
    _AgentPortMaxFrameSize_Type()
)
agentPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMaxFrameSize.setStatus("current")
_AgentProtocolConfigGroup_ObjectIdentity = ObjectIdentity
agentProtocolConfigGroup = _AgentProtocolConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14)
)


class _AgentProtocolGroupCreate_Type(DisplayString):
    """Custom type agentProtocolGroupCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentProtocolGroupCreate_Type.__name__ = "DisplayString"
_AgentProtocolGroupCreate_Object = MibScalar
agentProtocolGroupCreate = _AgentProtocolGroupCreate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 1),
    _AgentProtocolGroupCreate_Type()
)
agentProtocolGroupCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupCreate.setStatus("current")
_AgentProtocolGroupTable_Object = MibTable
agentProtocolGroupTable = _AgentProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    agentProtocolGroupTable.setStatus("current")
_AgentProtocolGroupEntry_Object = MibTableRow
agentProtocolGroupEntry = _AgentProtocolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1)
)
agentProtocolGroupEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentProtocolGroupId"),
)
if mibBuilder.loadTexts:
    agentProtocolGroupEntry.setStatus("current")
_AgentProtocolGroupId_Type = Integer32
_AgentProtocolGroupId_Object = MibTableColumn
agentProtocolGroupId = _AgentProtocolGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1, 1),
    _AgentProtocolGroupId_Type()
)
agentProtocolGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentProtocolGroupId.setStatus("current")
_AgentProtocolGroupName_Type = DisplayString
_AgentProtocolGroupName_Object = MibTableColumn
agentProtocolGroupName = _AgentProtocolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1, 2),
    _AgentProtocolGroupName_Type()
)
agentProtocolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentProtocolGroupName.setStatus("current")
_AgentProtocolGroupVlanId_Type = Integer32
_AgentProtocolGroupVlanId_Object = MibTableColumn
agentProtocolGroupVlanId = _AgentProtocolGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1, 3),
    _AgentProtocolGroupVlanId_Type()
)
agentProtocolGroupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupVlanId.setStatus("current")


class _AgentProtocolGroupProtocolIP_Type(Integer32):
    """Custom type agentProtocolGroupProtocolIP based on Integer32"""
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


_AgentProtocolGroupProtocolIP_Type.__name__ = "Integer32"
_AgentProtocolGroupProtocolIP_Object = MibTableColumn
agentProtocolGroupProtocolIP = _AgentProtocolGroupProtocolIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1, 4),
    _AgentProtocolGroupProtocolIP_Type()
)
agentProtocolGroupProtocolIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolIP.setStatus("current")


class _AgentProtocolGroupProtocolARP_Type(Integer32):
    """Custom type agentProtocolGroupProtocolARP based on Integer32"""
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


_AgentProtocolGroupProtocolARP_Type.__name__ = "Integer32"
_AgentProtocolGroupProtocolARP_Object = MibTableColumn
agentProtocolGroupProtocolARP = _AgentProtocolGroupProtocolARP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1, 5),
    _AgentProtocolGroupProtocolARP_Type()
)
agentProtocolGroupProtocolARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolARP.setStatus("current")


class _AgentProtocolGroupProtocolIPX_Type(Integer32):
    """Custom type agentProtocolGroupProtocolIPX based on Integer32"""
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


_AgentProtocolGroupProtocolIPX_Type.__name__ = "Integer32"
_AgentProtocolGroupProtocolIPX_Object = MibTableColumn
agentProtocolGroupProtocolIPX = _AgentProtocolGroupProtocolIPX_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1, 6),
    _AgentProtocolGroupProtocolIPX_Type()
)
agentProtocolGroupProtocolIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolIPX.setStatus("current")
_AgentProtocolGroupStatus_Type = RowStatus
_AgentProtocolGroupStatus_Object = MibTableColumn
agentProtocolGroupStatus = _AgentProtocolGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 2, 1, 7),
    _AgentProtocolGroupStatus_Type()
)
agentProtocolGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupStatus.setStatus("current")
_AgentProtocolGroupPortTable_Object = MibTable
agentProtocolGroupPortTable = _AgentProtocolGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    agentProtocolGroupPortTable.setStatus("current")
_AgentProtocolGroupPortEntry_Object = MibTableRow
agentProtocolGroupPortEntry = _AgentProtocolGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 3, 1)
)
agentProtocolGroupPortEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentProtocolGroupId"),
    (0, "GSM7312-SWITCHING-MIB", "agentProtocolGroupPortIfIndex"),
)
if mibBuilder.loadTexts:
    agentProtocolGroupPortEntry.setStatus("current")
_AgentProtocolGroupPortIfIndex_Type = Integer32
_AgentProtocolGroupPortIfIndex_Object = MibTableColumn
agentProtocolGroupPortIfIndex = _AgentProtocolGroupPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 3, 1, 1),
    _AgentProtocolGroupPortIfIndex_Type()
)
agentProtocolGroupPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentProtocolGroupPortIfIndex.setStatus("current")
_AgentProtocolGroupPortStatus_Type = RowStatus
_AgentProtocolGroupPortStatus_Object = MibTableColumn
agentProtocolGroupPortStatus = _AgentProtocolGroupPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 14, 3, 1, 2),
    _AgentProtocolGroupPortStatus_Type()
)
agentProtocolGroupPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentProtocolGroupPortStatus.setStatus("current")
_AgentStpSwitchConfigGroup_ObjectIdentity = ObjectIdentity
agentStpSwitchConfigGroup = _AgentStpSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15)
)


class _AgentStpConfigDigestKey_Type(OctetString):
    """Custom type agentStpConfigDigestKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AgentStpConfigDigestKey_Type.__name__ = "OctetString"
_AgentStpConfigDigestKey_Object = MibScalar
agentStpConfigDigestKey = _AgentStpConfigDigestKey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 1),
    _AgentStpConfigDigestKey_Type()
)
agentStpConfigDigestKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpConfigDigestKey.setStatus("current")


class _AgentStpConfigFormatSelector_Type(Unsigned32):
    """Custom type agentStpConfigFormatSelector based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentStpConfigFormatSelector_Type.__name__ = "Unsigned32"
_AgentStpConfigFormatSelector_Object = MibScalar
agentStpConfigFormatSelector = _AgentStpConfigFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 2),
    _AgentStpConfigFormatSelector_Type()
)
agentStpConfigFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpConfigFormatSelector.setStatus("current")


class _AgentStpConfigName_Type(DisplayString):
    """Custom type agentStpConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentStpConfigName_Type.__name__ = "DisplayString"
_AgentStpConfigName_Object = MibScalar
agentStpConfigName = _AgentStpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 3),
    _AgentStpConfigName_Type()
)
agentStpConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpConfigName.setStatus("current")


class _AgentStpConfigRevision_Type(Unsigned32):
    """Custom type agentStpConfigRevision based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentStpConfigRevision_Type.__name__ = "Unsigned32"
_AgentStpConfigRevision_Object = MibScalar
agentStpConfigRevision = _AgentStpConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 4),
    _AgentStpConfigRevision_Type()
)
agentStpConfigRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpConfigRevision.setStatus("current")


class _AgentStpForceVersion_Type(Integer32):
    """Custom type agentStpForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("dot1s", 3),
          ("dot1w", 2))
    )


_AgentStpForceVersion_Type.__name__ = "Integer32"
_AgentStpForceVersion_Object = MibScalar
agentStpForceVersion = _AgentStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 5),
    _AgentStpForceVersion_Type()
)
agentStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpForceVersion.setStatus("current")


class _AgentStpAdminMode_Type(Integer32):
    """Custom type agentStpAdminMode based on Integer32"""
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


_AgentStpAdminMode_Type.__name__ = "Integer32"
_AgentStpAdminMode_Object = MibScalar
agentStpAdminMode = _AgentStpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 6),
    _AgentStpAdminMode_Type()
)
agentStpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpAdminMode.setStatus("current")
_AgentStpPortTable_Object = MibTable
agentStpPortTable = _AgentStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7)
)
if mibBuilder.loadTexts:
    agentStpPortTable.setStatus("current")
_AgentStpPortEntry_Object = MibTableRow
agentStpPortEntry = _AgentStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1)
)
agentStpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentStpPortEntry.setStatus("current")


class _AgentStpPortState_Type(Integer32):
    """Custom type agentStpPortState based on Integer32"""
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


_AgentStpPortState_Type.__name__ = "Integer32"
_AgentStpPortState_Object = MibTableColumn
agentStpPortState = _AgentStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 1),
    _AgentStpPortState_Type()
)
agentStpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpPortState.setStatus("current")
_AgentStpPortStatsMstpBpduRx_Type = Counter32
_AgentStpPortStatsMstpBpduRx_Object = MibTableColumn
agentStpPortStatsMstpBpduRx = _AgentStpPortStatsMstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 2),
    _AgentStpPortStatsMstpBpduRx_Type()
)
agentStpPortStatsMstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsMstpBpduRx.setStatus("current")
_AgentStpPortStatsMstpBpduTx_Type = Counter32
_AgentStpPortStatsMstpBpduTx_Object = MibTableColumn
agentStpPortStatsMstpBpduTx = _AgentStpPortStatsMstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 3),
    _AgentStpPortStatsMstpBpduTx_Type()
)
agentStpPortStatsMstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsMstpBpduTx.setStatus("current")
_AgentStpPortStatsRstpBpduRx_Type = Counter32
_AgentStpPortStatsRstpBpduRx_Object = MibTableColumn
agentStpPortStatsRstpBpduRx = _AgentStpPortStatsRstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 4),
    _AgentStpPortStatsRstpBpduRx_Type()
)
agentStpPortStatsRstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsRstpBpduRx.setStatus("current")
_AgentStpPortStatsRstpBpduTx_Type = Counter32
_AgentStpPortStatsRstpBpduTx_Object = MibTableColumn
agentStpPortStatsRstpBpduTx = _AgentStpPortStatsRstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 5),
    _AgentStpPortStatsRstpBpduTx_Type()
)
agentStpPortStatsRstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsRstpBpduTx.setStatus("current")
_AgentStpPortStatsStpBpduRx_Type = Counter32
_AgentStpPortStatsStpBpduRx_Object = MibTableColumn
agentStpPortStatsStpBpduRx = _AgentStpPortStatsStpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 6),
    _AgentStpPortStatsStpBpduRx_Type()
)
agentStpPortStatsStpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsStpBpduRx.setStatus("current")
_AgentStpPortStatsStpBpduTx_Type = Counter32
_AgentStpPortStatsStpBpduTx_Object = MibTableColumn
agentStpPortStatsStpBpduTx = _AgentStpPortStatsStpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 7),
    _AgentStpPortStatsStpBpduTx_Type()
)
agentStpPortStatsStpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsStpBpduTx.setStatus("current")
_AgentStpPortUpTime_Type = TimeTicks
_AgentStpPortUpTime_Object = MibTableColumn
agentStpPortUpTime = _AgentStpPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 8),
    _AgentStpPortUpTime_Type()
)
agentStpPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortUpTime.setStatus("current")


class _AgentStpPortMigrationCheck_Type(Integer32):
    """Custom type agentStpPortMigrationCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentStpPortMigrationCheck_Type.__name__ = "Integer32"
_AgentStpPortMigrationCheck_Object = MibTableColumn
agentStpPortMigrationCheck = _AgentStpPortMigrationCheck_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 7, 1, 9),
    _AgentStpPortMigrationCheck_Type()
)
agentStpPortMigrationCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpPortMigrationCheck.setStatus("current")
_AgentStpCstConfigGroup_ObjectIdentity = ObjectIdentity
agentStpCstConfigGroup = _AgentStpCstConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8)
)
_AgentStpCstHelloTime_Type = Unsigned32
_AgentStpCstHelloTime_Object = MibScalar
agentStpCstHelloTime = _AgentStpCstHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 1),
    _AgentStpCstHelloTime_Type()
)
agentStpCstHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstHelloTime.setStatus("current")
_AgentStpCstMaxAge_Type = Unsigned32
_AgentStpCstMaxAge_Object = MibScalar
agentStpCstMaxAge = _AgentStpCstMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 2),
    _AgentStpCstMaxAge_Type()
)
agentStpCstMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstMaxAge.setStatus("current")


class _AgentStpCstRegionalRootId_Type(OctetString):
    """Custom type agentStpCstRegionalRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpCstRegionalRootId_Type.__name__ = "OctetString"
_AgentStpCstRegionalRootId_Object = MibScalar
agentStpCstRegionalRootId = _AgentStpCstRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 3),
    _AgentStpCstRegionalRootId_Type()
)
agentStpCstRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstRegionalRootId.setStatus("current")
_AgentStpCstRegionalRootPathCost_Type = Unsigned32
_AgentStpCstRegionalRootPathCost_Object = MibScalar
agentStpCstRegionalRootPathCost = _AgentStpCstRegionalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 4),
    _AgentStpCstRegionalRootPathCost_Type()
)
agentStpCstRegionalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstRegionalRootPathCost.setStatus("current")
_AgentStpCstRootFwdDelay_Type = Unsigned32
_AgentStpCstRootFwdDelay_Object = MibScalar
agentStpCstRootFwdDelay = _AgentStpCstRootFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 5),
    _AgentStpCstRootFwdDelay_Type()
)
agentStpCstRootFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstRootFwdDelay.setStatus("current")


class _AgentStpCstBridgeFwdDelay_Type(Unsigned32):
    """Custom type agentStpCstBridgeFwdDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_AgentStpCstBridgeFwdDelay_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeFwdDelay_Object = MibScalar
agentStpCstBridgeFwdDelay = _AgentStpCstBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 6),
    _AgentStpCstBridgeFwdDelay_Type()
)
agentStpCstBridgeFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgeFwdDelay.setStatus("current")


class _AgentStpCstBridgeHelloTime_Type(Unsigned32):
    """Custom type agentStpCstBridgeHelloTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentStpCstBridgeHelloTime_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeHelloTime_Object = MibScalar
agentStpCstBridgeHelloTime = _AgentStpCstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 7),
    _AgentStpCstBridgeHelloTime_Type()
)
agentStpCstBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgeHelloTime.setStatus("current")
_AgentStpCstBridgeHoldTime_Type = Unsigned32
_AgentStpCstBridgeHoldTime_Object = MibScalar
agentStpCstBridgeHoldTime = _AgentStpCstBridgeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 8),
    _AgentStpCstBridgeHoldTime_Type()
)
agentStpCstBridgeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstBridgeHoldTime.setStatus("current")


class _AgentStpCstBridgeMaxAge_Type(Unsigned32):
    """Custom type agentStpCstBridgeMaxAge based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_AgentStpCstBridgeMaxAge_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeMaxAge_Object = MibScalar
agentStpCstBridgeMaxAge = _AgentStpCstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 8, 9),
    _AgentStpCstBridgeMaxAge_Type()
)
agentStpCstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgeMaxAge.setStatus("current")
_AgentStpCstPortTable_Object = MibTable
agentStpCstPortTable = _AgentStpCstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9)
)
if mibBuilder.loadTexts:
    agentStpCstPortTable.setStatus("current")
_AgentStpCstPortEntry_Object = MibTableRow
agentStpCstPortEntry = _AgentStpCstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1)
)
agentStpCstPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentStpCstPortEntry.setStatus("current")


class _AgentStpCstPortOperEdge_Type(Integer32):
    """Custom type agentStpCstPortOperEdge based on Integer32"""
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


_AgentStpCstPortOperEdge_Type.__name__ = "Integer32"
_AgentStpCstPortOperEdge_Object = MibTableColumn
agentStpCstPortOperEdge = _AgentStpCstPortOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 1),
    _AgentStpCstPortOperEdge_Type()
)
agentStpCstPortOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortOperEdge.setStatus("current")


class _AgentStpCstPortOperPointToPoint_Type(Integer32):
    """Custom type agentStpCstPortOperPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentStpCstPortOperPointToPoint_Type.__name__ = "Integer32"
_AgentStpCstPortOperPointToPoint_Object = MibTableColumn
agentStpCstPortOperPointToPoint = _AgentStpCstPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 2),
    _AgentStpCstPortOperPointToPoint_Type()
)
agentStpCstPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortOperPointToPoint.setStatus("current")


class _AgentStpCstPortTopologyChangeAck_Type(Integer32):
    """Custom type agentStpCstPortTopologyChangeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentStpCstPortTopologyChangeAck_Type.__name__ = "Integer32"
_AgentStpCstPortTopologyChangeAck_Object = MibTableColumn
agentStpCstPortTopologyChangeAck = _AgentStpCstPortTopologyChangeAck_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 3),
    _AgentStpCstPortTopologyChangeAck_Type()
)
agentStpCstPortTopologyChangeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortTopologyChangeAck.setStatus("current")


class _AgentStpCstPortEdge_Type(Integer32):
    """Custom type agentStpCstPortEdge based on Integer32"""
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


_AgentStpCstPortEdge_Type.__name__ = "Integer32"
_AgentStpCstPortEdge_Object = MibTableColumn
agentStpCstPortEdge = _AgentStpCstPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 4),
    _AgentStpCstPortEdge_Type()
)
agentStpCstPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortEdge.setStatus("current")


class _AgentStpCstPortForwardingState_Type(Integer32):
    """Custom type agentStpCstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_AgentStpCstPortForwardingState_Type.__name__ = "Integer32"
_AgentStpCstPortForwardingState_Object = MibTableColumn
agentStpCstPortForwardingState = _AgentStpCstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 5),
    _AgentStpCstPortForwardingState_Type()
)
agentStpCstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortForwardingState.setStatus("current")


class _AgentStpCstPortId_Type(OctetString):
    """Custom type agentStpCstPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AgentStpCstPortId_Type.__name__ = "OctetString"
_AgentStpCstPortId_Object = MibTableColumn
agentStpCstPortId = _AgentStpCstPortId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 6),
    _AgentStpCstPortId_Type()
)
agentStpCstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortId.setStatus("current")


class _AgentStpCstPortPathCost_Type(Unsigned32):
    """Custom type agentStpCstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_AgentStpCstPortPathCost_Type.__name__ = "Unsigned32"
_AgentStpCstPortPathCost_Object = MibTableColumn
agentStpCstPortPathCost = _AgentStpCstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 7),
    _AgentStpCstPortPathCost_Type()
)
agentStpCstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortPathCost.setStatus("current")


class _AgentStpCstPortPriority_Type(Unsigned32):
    """Custom type agentStpCstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_AgentStpCstPortPriority_Type.__name__ = "Unsigned32"
_AgentStpCstPortPriority_Object = MibTableColumn
agentStpCstPortPriority = _AgentStpCstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 8),
    _AgentStpCstPortPriority_Type()
)
agentStpCstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortPriority.setStatus("current")


class _AgentStpCstDesignatedBridgeId_Type(OctetString):
    """Custom type agentStpCstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpCstDesignatedBridgeId_Type.__name__ = "OctetString"
_AgentStpCstDesignatedBridgeId_Object = MibTableColumn
agentStpCstDesignatedBridgeId = _AgentStpCstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 9),
    _AgentStpCstDesignatedBridgeId_Type()
)
agentStpCstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstDesignatedBridgeId.setStatus("current")
_AgentStpCstDesignatedCost_Type = Unsigned32
_AgentStpCstDesignatedCost_Object = MibTableColumn
agentStpCstDesignatedCost = _AgentStpCstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 10),
    _AgentStpCstDesignatedCost_Type()
)
agentStpCstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstDesignatedCost.setStatus("current")


class _AgentStpCstDesignatedPortId_Type(OctetString):
    """Custom type agentStpCstDesignatedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AgentStpCstDesignatedPortId_Type.__name__ = "OctetString"
_AgentStpCstDesignatedPortId_Object = MibTableColumn
agentStpCstDesignatedPortId = _AgentStpCstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 9, 1, 11),
    _AgentStpCstDesignatedPortId_Type()
)
agentStpCstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstDesignatedPortId.setStatus("current")
_AgentStpMstTable_Object = MibTable
agentStpMstTable = _AgentStpMstTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10)
)
if mibBuilder.loadTexts:
    agentStpMstTable.setStatus("current")
_AgentStpMstEntry_Object = MibTableRow
agentStpMstEntry = _AgentStpMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1)
)
agentStpMstEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentStpMstId"),
)
if mibBuilder.loadTexts:
    agentStpMstEntry.setStatus("current")
_AgentStpMstId_Type = Unsigned32
_AgentStpMstId_Object = MibTableColumn
agentStpMstId = _AgentStpMstId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 1),
    _AgentStpMstId_Type()
)
agentStpMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstId.setStatus("current")


class _AgentStpMstBridgePriority_Type(Unsigned32):
    """Custom type agentStpMstBridgePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_AgentStpMstBridgePriority_Type.__name__ = "Unsigned32"
_AgentStpMstBridgePriority_Object = MibTableColumn
agentStpMstBridgePriority = _AgentStpMstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 2),
    _AgentStpMstBridgePriority_Type()
)
agentStpMstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpMstBridgePriority.setStatus("current")


class _AgentStpMstBridgeIdentifier_Type(OctetString):
    """Custom type agentStpMstBridgeIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstBridgeIdentifier_Type.__name__ = "OctetString"
_AgentStpMstBridgeIdentifier_Object = MibTableColumn
agentStpMstBridgeIdentifier = _AgentStpMstBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 3),
    _AgentStpMstBridgeIdentifier_Type()
)
agentStpMstBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstBridgeIdentifier.setStatus("current")


class _AgentStpMstDesignatedRootId_Type(OctetString):
    """Custom type agentStpMstDesignatedRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstDesignatedRootId_Type.__name__ = "OctetString"
_AgentStpMstDesignatedRootId_Object = MibTableColumn
agentStpMstDesignatedRootId = _AgentStpMstDesignatedRootId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 4),
    _AgentStpMstDesignatedRootId_Type()
)
agentStpMstDesignatedRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedRootId.setStatus("current")
_AgentStpMstRootPathCost_Type = Unsigned32
_AgentStpMstRootPathCost_Object = MibTableColumn
agentStpMstRootPathCost = _AgentStpMstRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 5),
    _AgentStpMstRootPathCost_Type()
)
agentStpMstRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstRootPathCost.setStatus("current")


class _AgentStpMstRootPortId_Type(OctetString):
    """Custom type agentStpMstRootPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstRootPortId_Type.__name__ = "OctetString"
_AgentStpMstRootPortId_Object = MibTableColumn
agentStpMstRootPortId = _AgentStpMstRootPortId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 6),
    _AgentStpMstRootPortId_Type()
)
agentStpMstRootPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstRootPortId.setStatus("current")
_AgentStpMstTimeSinceTopologyChange_Type = TimeTicks
_AgentStpMstTimeSinceTopologyChange_Object = MibTableColumn
agentStpMstTimeSinceTopologyChange = _AgentStpMstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 7),
    _AgentStpMstTimeSinceTopologyChange_Type()
)
agentStpMstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstTimeSinceTopologyChange.setStatus("current")
_AgentStpMstTopologyChangeCount_Type = Counter32
_AgentStpMstTopologyChangeCount_Object = MibTableColumn
agentStpMstTopologyChangeCount = _AgentStpMstTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 8),
    _AgentStpMstTopologyChangeCount_Type()
)
agentStpMstTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstTopologyChangeCount.setStatus("current")


class _AgentStpMstTopologyChangeParm_Type(Integer32):
    """Custom type agentStpMstTopologyChangeParm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentStpMstTopologyChangeParm_Type.__name__ = "Integer32"
_AgentStpMstTopologyChangeParm_Object = MibTableColumn
agentStpMstTopologyChangeParm = _AgentStpMstTopologyChangeParm_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 9),
    _AgentStpMstTopologyChangeParm_Type()
)
agentStpMstTopologyChangeParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstTopologyChangeParm.setStatus("current")
_AgentStpMstRowStatus_Type = RowStatus
_AgentStpMstRowStatus_Object = MibTableColumn
agentStpMstRowStatus = _AgentStpMstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 10, 1, 10),
    _AgentStpMstRowStatus_Type()
)
agentStpMstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStpMstRowStatus.setStatus("current")
_AgentStpMstPortTable_Object = MibTable
agentStpMstPortTable = _AgentStpMstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11)
)
if mibBuilder.loadTexts:
    agentStpMstPortTable.setStatus("current")
_AgentStpMstPortEntry_Object = MibTableRow
agentStpMstPortEntry = _AgentStpMstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1)
)
agentStpMstPortEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentStpMstId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentStpMstPortEntry.setStatus("current")


class _AgentStpMstPortForwardingState_Type(Integer32):
    """Custom type agentStpMstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_AgentStpMstPortForwardingState_Type.__name__ = "Integer32"
_AgentStpMstPortForwardingState_Object = MibTableColumn
agentStpMstPortForwardingState = _AgentStpMstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1, 1),
    _AgentStpMstPortForwardingState_Type()
)
agentStpMstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstPortForwardingState.setStatus("current")


class _AgentStpMstPortId_Type(OctetString):
    """Custom type agentStpMstPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AgentStpMstPortId_Type.__name__ = "OctetString"
_AgentStpMstPortId_Object = MibTableColumn
agentStpMstPortId = _AgentStpMstPortId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1, 2),
    _AgentStpMstPortId_Type()
)
agentStpMstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstPortId.setStatus("current")


class _AgentStpMstPortPathCost_Type(Unsigned32):
    """Custom type agentStpMstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_AgentStpMstPortPathCost_Type.__name__ = "Unsigned32"
_AgentStpMstPortPathCost_Object = MibTableColumn
agentStpMstPortPathCost = _AgentStpMstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1, 3),
    _AgentStpMstPortPathCost_Type()
)
agentStpMstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpMstPortPathCost.setStatus("current")


class _AgentStpMstPortPriority_Type(Unsigned32):
    """Custom type agentStpMstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_AgentStpMstPortPriority_Type.__name__ = "Unsigned32"
_AgentStpMstPortPriority_Object = MibTableColumn
agentStpMstPortPriority = _AgentStpMstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1, 4),
    _AgentStpMstPortPriority_Type()
)
agentStpMstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpMstPortPriority.setStatus("current")


class _AgentStpMstDesignatedBridgeId_Type(OctetString):
    """Custom type agentStpMstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstDesignatedBridgeId_Type.__name__ = "OctetString"
_AgentStpMstDesignatedBridgeId_Object = MibTableColumn
agentStpMstDesignatedBridgeId = _AgentStpMstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1, 5),
    _AgentStpMstDesignatedBridgeId_Type()
)
agentStpMstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedBridgeId.setStatus("current")
_AgentStpMstDesignatedCost_Type = Unsigned32
_AgentStpMstDesignatedCost_Object = MibTableColumn
agentStpMstDesignatedCost = _AgentStpMstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1, 6),
    _AgentStpMstDesignatedCost_Type()
)
agentStpMstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedCost.setStatus("current")


class _AgentStpMstDesignatedPortId_Type(OctetString):
    """Custom type agentStpMstDesignatedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AgentStpMstDesignatedPortId_Type.__name__ = "OctetString"
_AgentStpMstDesignatedPortId_Object = MibTableColumn
agentStpMstDesignatedPortId = _AgentStpMstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 11, 1, 7),
    _AgentStpMstDesignatedPortId_Type()
)
agentStpMstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedPortId.setStatus("current")
_AgentStpMstVlanTable_Object = MibTable
agentStpMstVlanTable = _AgentStpMstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 12)
)
if mibBuilder.loadTexts:
    agentStpMstVlanTable.setStatus("current")
_AgentStpMstVlanEntry_Object = MibTableRow
agentStpMstVlanEntry = _AgentStpMstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 12, 1)
)
agentStpMstVlanEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentStpMstId"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    agentStpMstVlanEntry.setStatus("current")
_AgentStpMstVlanRowStatus_Type = RowStatus
_AgentStpMstVlanRowStatus_Object = MibTableColumn
agentStpMstVlanRowStatus = _AgentStpMstVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 15, 12, 1, 1),
    _AgentStpMstVlanRowStatus_Type()
)
agentStpMstVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStpMstVlanRowStatus.setStatus("current")
_AgentAuthenticationGroup_ObjectIdentity = ObjectIdentity
agentAuthenticationGroup = _AgentAuthenticationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16)
)


class _AgentAuthenticationListCreate_Type(DisplayString):
    """Custom type agentAuthenticationListCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentAuthenticationListCreate_Type.__name__ = "DisplayString"
_AgentAuthenticationListCreate_Object = MibScalar
agentAuthenticationListCreate = _AgentAuthenticationListCreate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 1),
    _AgentAuthenticationListCreate_Type()
)
agentAuthenticationListCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListCreate.setStatus("current")
_AgentAuthenticationListTable_Object = MibTable
agentAuthenticationListTable = _AgentAuthenticationListTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2)
)
if mibBuilder.loadTexts:
    agentAuthenticationListTable.setStatus("current")
_AgentAuthenticationListEntry_Object = MibTableRow
agentAuthenticationListEntry = _AgentAuthenticationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2, 1)
)
agentAuthenticationListEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentAuthenticationListIndex"),
)
if mibBuilder.loadTexts:
    agentAuthenticationListEntry.setStatus("current")
_AgentAuthenticationListIndex_Type = Unsigned32
_AgentAuthenticationListIndex_Object = MibTableColumn
agentAuthenticationListIndex = _AgentAuthenticationListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2, 1, 1),
    _AgentAuthenticationListIndex_Type()
)
agentAuthenticationListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthenticationListIndex.setStatus("current")


class _AgentAuthenticationListName_Type(DisplayString):
    """Custom type agentAuthenticationListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentAuthenticationListName_Type.__name__ = "DisplayString"
_AgentAuthenticationListName_Object = MibTableColumn
agentAuthenticationListName = _AgentAuthenticationListName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2, 1, 2),
    _AgentAuthenticationListName_Type()
)
agentAuthenticationListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthenticationListName.setStatus("current")


class _AgentAuthenticationListMethod1_Type(Integer32):
    """Custom type agentAuthenticationListMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("reject", 3))
    )


_AgentAuthenticationListMethod1_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod1_Object = MibTableColumn
agentAuthenticationListMethod1 = _AgentAuthenticationListMethod1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2, 1, 3),
    _AgentAuthenticationListMethod1_Type()
)
agentAuthenticationListMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod1.setStatus("current")


class _AgentAuthenticationListMethod2_Type(Integer32):
    """Custom type agentAuthenticationListMethod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 3),
          ("reject", 4),
          ("undefined", 1))
    )


_AgentAuthenticationListMethod2_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod2_Object = MibTableColumn
agentAuthenticationListMethod2 = _AgentAuthenticationListMethod2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2, 1, 4),
    _AgentAuthenticationListMethod2_Type()
)
agentAuthenticationListMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod2.setStatus("current")


class _AgentAuthenticationListMethod3_Type(Integer32):
    """Custom type agentAuthenticationListMethod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 3),
          ("reject", 4),
          ("undefined", 1))
    )


_AgentAuthenticationListMethod3_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod3_Object = MibTableColumn
agentAuthenticationListMethod3 = _AgentAuthenticationListMethod3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2, 1, 5),
    _AgentAuthenticationListMethod3_Type()
)
agentAuthenticationListMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod3.setStatus("current")
_AgentAuthenticationListStatus_Type = RowStatus
_AgentAuthenticationListStatus_Object = MibTableColumn
agentAuthenticationListStatus = _AgentAuthenticationListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 2, 1, 6),
    _AgentAuthenticationListStatus_Type()
)
agentAuthenticationListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListStatus.setStatus("current")


class _AgentUserConfigDefaultAuthenticationList_Type(DisplayString):
    """Custom type agentUserConfigDefaultAuthenticationList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentUserConfigDefaultAuthenticationList_Type.__name__ = "DisplayString"
_AgentUserConfigDefaultAuthenticationList_Object = MibScalar
agentUserConfigDefaultAuthenticationList = _AgentUserConfigDefaultAuthenticationList_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 3),
    _AgentUserConfigDefaultAuthenticationList_Type()
)
agentUserConfigDefaultAuthenticationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserConfigDefaultAuthenticationList.setStatus("current")
_AgentUserAuthenticationConfigTable_Object = MibTable
agentUserAuthenticationConfigTable = _AgentUserAuthenticationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 4)
)
if mibBuilder.loadTexts:
    agentUserAuthenticationConfigTable.setStatus("current")
_AgentUserAuthenticationConfigEntry_Object = MibTableRow
agentUserAuthenticationConfigEntry = _AgentUserAuthenticationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    agentUserAuthenticationConfigEntry.setStatus("current")


class _AgentUserAuthenticationList_Type(DisplayString):
    """Custom type agentUserAuthenticationList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentUserAuthenticationList_Type.__name__ = "DisplayString"
_AgentUserAuthenticationList_Object = MibTableColumn
agentUserAuthenticationList = _AgentUserAuthenticationList_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 4, 1, 1),
    _AgentUserAuthenticationList_Type()
)
agentUserAuthenticationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserAuthenticationList.setStatus("current")
_AgentUserPortConfigTable_Object = MibTable
agentUserPortConfigTable = _AgentUserPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 5)
)
if mibBuilder.loadTexts:
    agentUserPortConfigTable.setStatus("current")
_AgentUserPortConfigEntry_Object = MibTableRow
agentUserPortConfigEntry = _AgentUserPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 5, 1)
)
if mibBuilder.loadTexts:
    agentUserPortConfigEntry.setStatus("current")
_AgentUserPortSecurity_Type = AgentPortMask
_AgentUserPortSecurity_Object = MibTableColumn
agentUserPortSecurity = _AgentUserPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 16, 5, 1, 1),
    _AgentUserPortSecurity_Type()
)
agentUserPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserPortSecurity.setStatus("current")
_AgentClassOfServiceGroup_ObjectIdentity = ObjectIdentity
agentClassOfServiceGroup = _AgentClassOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 17)
)
_AgentClassOfServiceTable_Object = MibTable
agentClassOfServiceTable = _AgentClassOfServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    agentClassOfServiceTable.setStatus("current")
_AgentClassOfServiceEntry_Object = MibTableRow
agentClassOfServiceEntry = _AgentClassOfServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 17, 1, 1)
)
agentClassOfServiceEntry.setIndexNames(
    (0, "GSM7312-SWITCHING-MIB", "agentClassOfServicePriority"),
)
if mibBuilder.loadTexts:
    agentClassOfServiceEntry.setStatus("current")


class _AgentClassOfServicePriority_Type(Integer32):
    """Custom type agentClassOfServicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentClassOfServicePriority_Type.__name__ = "Integer32"
_AgentClassOfServicePriority_Object = MibTableColumn
agentClassOfServicePriority = _AgentClassOfServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 17, 1, 1, 1),
    _AgentClassOfServicePriority_Type()
)
agentClassOfServicePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentClassOfServicePriority.setStatus("current")


class _AgentClassOfServiceClass_Type(Integer32):
    """Custom type agentClassOfServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentClassOfServiceClass_Type.__name__ = "Integer32"
_AgentClassOfServiceClass_Object = MibTableColumn
agentClassOfServiceClass = _AgentClassOfServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 2, 17, 1, 1, 2),
    _AgentClassOfServiceClass_Type()
)
agentClassOfServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClassOfServiceClass.setStatus("current")
_AgentSystemGroup_ObjectIdentity = ObjectIdentity
agentSystemGroup = _AgentSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3)
)


class _AgentSaveConfig_Type(Integer32):
    """Custom type agentSaveConfig based on Integer32"""
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


_AgentSaveConfig_Type.__name__ = "Integer32"
_AgentSaveConfig_Object = MibScalar
agentSaveConfig = _AgentSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 1),
    _AgentSaveConfig_Type()
)
agentSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSaveConfig.setStatus("current")


class _AgentClearConfig_Type(Integer32):
    """Custom type agentClearConfig based on Integer32"""
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


_AgentClearConfig_Type.__name__ = "Integer32"
_AgentClearConfig_Object = MibScalar
agentClearConfig = _AgentClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 2),
    _AgentClearConfig_Type()
)
agentClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearConfig.setStatus("current")


class _AgentClearLags_Type(Integer32):
    """Custom type agentClearLags based on Integer32"""
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


_AgentClearLags_Type.__name__ = "Integer32"
_AgentClearLags_Object = MibScalar
agentClearLags = _AgentClearLags_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 3),
    _AgentClearLags_Type()
)
agentClearLags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearLags.setStatus("current")


class _AgentClearLoginSessions_Type(Integer32):
    """Custom type agentClearLoginSessions based on Integer32"""
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


_AgentClearLoginSessions_Type.__name__ = "Integer32"
_AgentClearLoginSessions_Object = MibScalar
agentClearLoginSessions = _AgentClearLoginSessions_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 4),
    _AgentClearLoginSessions_Type()
)
agentClearLoginSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearLoginSessions.setStatus("current")


class _AgentClearPasswords_Type(Integer32):
    """Custom type agentClearPasswords based on Integer32"""
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


_AgentClearPasswords_Type.__name__ = "Integer32"
_AgentClearPasswords_Object = MibScalar
agentClearPasswords = _AgentClearPasswords_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 5),
    _AgentClearPasswords_Type()
)
agentClearPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearPasswords.setStatus("current")


class _AgentClearPortStats_Type(Integer32):
    """Custom type agentClearPortStats based on Integer32"""
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


_AgentClearPortStats_Type.__name__ = "Integer32"
_AgentClearPortStats_Object = MibScalar
agentClearPortStats = _AgentClearPortStats_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 6),
    _AgentClearPortStats_Type()
)
agentClearPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearPortStats.setStatus("current")


class _AgentClearSwitchStats_Type(Integer32):
    """Custom type agentClearSwitchStats based on Integer32"""
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


_AgentClearSwitchStats_Type.__name__ = "Integer32"
_AgentClearSwitchStats_Object = MibScalar
agentClearSwitchStats = _AgentClearSwitchStats_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 7),
    _AgentClearSwitchStats_Type()
)
agentClearSwitchStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearSwitchStats.setStatus("current")


class _AgentClearTrapLog_Type(Integer32):
    """Custom type agentClearTrapLog based on Integer32"""
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


_AgentClearTrapLog_Type.__name__ = "Integer32"
_AgentClearTrapLog_Object = MibScalar
agentClearTrapLog = _AgentClearTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 8),
    _AgentClearTrapLog_Type()
)
agentClearTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearTrapLog.setStatus("current")


class _AgentClearVlan_Type(Integer32):
    """Custom type agentClearVlan based on Integer32"""
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


_AgentClearVlan_Type.__name__ = "Integer32"
_AgentClearVlan_Object = MibScalar
agentClearVlan = _AgentClearVlan_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 9),
    _AgentClearVlan_Type()
)
agentClearVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearVlan.setStatus("current")


class _AgentResetSystem_Type(Integer32):
    """Custom type agentResetSystem based on Integer32"""
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


_AgentResetSystem_Type.__name__ = "Integer32"
_AgentResetSystem_Object = MibScalar
agentResetSystem = _AgentResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 10),
    _AgentResetSystem_Type()
)
agentResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResetSystem.setStatus("current")


class _AgentSaveConfigStatus_Type(Integer32):
    """Custom type agentSaveConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInitiated", 1),
          ("savingComplete", 3),
          ("savingInProcess", 2))
    )


_AgentSaveConfigStatus_Type.__name__ = "Integer32"
_AgentSaveConfigStatus_Object = MibScalar
agentSaveConfigStatus = _AgentSaveConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 3, 11),
    _AgentSaveConfigStatus_Type()
)
agentSaveConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSaveConfigStatus.setStatus("current")
_AgentCableTesterGroup_ObjectIdentity = ObjectIdentity
agentCableTesterGroup = _AgentCableTesterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 4)
)


class _AgentCableTesterStatus_Type(Integer32):
    """Custom type agentCableTesterStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failure", 3),
          ("success", 2),
          ("uninitialized", 4))
    )


_AgentCableTesterStatus_Type.__name__ = "Integer32"
_AgentCableTesterStatus_Object = MibScalar
agentCableTesterStatus = _AgentCableTesterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 4, 1),
    _AgentCableTesterStatus_Type()
)
agentCableTesterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCableTesterStatus.setStatus("current")


class _AgentCableTesterIfIndex_Type(Unsigned32):
    """Custom type agentCableTesterIfIndex based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterIfIndex_Object = MibScalar
agentCableTesterIfIndex = _AgentCableTesterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 4, 2),
    _AgentCableTesterIfIndex_Type()
)
agentCableTesterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCableTesterIfIndex.setStatus("current")


class _AgentCableTesterCableStatus_Type(Integer32):
    """Custom type agentCableTesterCableStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("open", 2),
          ("short", 3),
          ("unknown", 4))
    )


_AgentCableTesterCableStatus_Type.__name__ = "Integer32"
_AgentCableTesterCableStatus_Object = MibScalar
agentCableTesterCableStatus = _AgentCableTesterCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 4, 3),
    _AgentCableTesterCableStatus_Type()
)
agentCableTesterCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterCableStatus.setStatus("current")


class _AgentCableTesterMinimumCableLength_Type(Unsigned32):
    """Custom type agentCableTesterMinimumCableLength based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterMinimumCableLength_Object = MibScalar
agentCableTesterMinimumCableLength = _AgentCableTesterMinimumCableLength_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 4, 4),
    _AgentCableTesterMinimumCableLength_Type()
)
agentCableTesterMinimumCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterMinimumCableLength.setStatus("current")


class _AgentCableTesterMaximumCableLength_Type(Unsigned32):
    """Custom type agentCableTesterMaximumCableLength based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterMaximumCableLength_Object = MibScalar
agentCableTesterMaximumCableLength = _AgentCableTesterMaximumCableLength_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 4, 5),
    _AgentCableTesterMaximumCableLength_Type()
)
agentCableTesterMaximumCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterMaximumCableLength.setStatus("current")


class _AgentCableTesterCableFailureLocation_Type(Unsigned32):
    """Custom type agentCableTesterCableFailureLocation based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterCableFailureLocation_Object = MibScalar
agentCableTesterCableFailureLocation = _AgentCableTesterCableFailureLocation_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 4, 6),
    _AgentCableTesterCableFailureLocation_Type()
)
agentCableTesterCableFailureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterCableFailureLocation.setStatus("current")
_Gsm7312SwitchingTraps_ObjectIdentity = ObjectIdentity
gsm7312SwitchingTraps = _Gsm7312SwitchingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50)
)
agentUserConfigEntry.registerAugmentions(
    ("GSM7312-SWITCHING-MIB",
     "agentUserAuthenticationConfigEntry")
)
agentUserAuthenticationConfigEntry.setIndexNames(*agentUserConfigEntry.getIndexNames())
agentUserConfigEntry.registerAugmentions(
    ("GSM7312-SWITCHING-MIB",
     "agentUserPortConfigEntry")
)
agentUserPortConfigEntry.setIndexNames(*agentUserConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

multipleUsersTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 1)
)
if mibBuilder.loadTexts:
    multipleUsersTrap.setStatus(
        "current"
    )

broadcastStormStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 2)
)
if mibBuilder.loadTexts:
    broadcastStormStartTrap.setStatus(
        "current"
    )

broadcastStormEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 3)
)
if mibBuilder.loadTexts:
    broadcastStormEndTrap.setStatus(
        "current"
    )

linkFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 4)
)
if mibBuilder.loadTexts:
    linkFailureTrap.setStatus(
        "current"
    )

vlanRequestFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 5)
)
vlanRequestFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRequestFailureTrap.setStatus(
        "current"
    )

vlanDeleteLastTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 6)
)
vlanDeleteLastTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDeleteLastTrap.setStatus(
        "current"
    )

vlanDefaultCfgFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 7)
)
vlanDefaultCfgFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDefaultCfgFailureTrap.setStatus(
        "current"
    )

vlanRestoreFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 8)
)
vlanRestoreFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRestoreFailureTrap.setStatus(
        "current"
    )

fanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 9)
)
if mibBuilder.loadTexts:
    fanFailureTrap.setStatus(
        "current"
    )

stpInstanceNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 10)
)
stpInstanceNewRootTrap.setObjects(
    ("GSM7312-SWITCHING-MIB", "agentStpMstId")
)
if mibBuilder.loadTexts:
    stpInstanceNewRootTrap.setStatus(
        "current"
    )

stpInstanceTopologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 11)
)
stpInstanceTopologyChangeTrap.setObjects(
    ("GSM7312-SWITCHING-MIB", "agentStpMstId")
)
if mibBuilder.loadTexts:
    stpInstanceTopologyChangeTrap.setStatus(
        "current"
    )

powerSupplyStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6, 1, 50, 12)
)
if mibBuilder.loadTexts:
    powerSupplyStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GSM7312-SWITCHING-MIB",
    **{"gsm7312Switching": gsm7312Switching,
       "agentInfoGroup": agentInfoGroup,
       "agentInventoryGroup": agentInventoryGroup,
       "agentInventorySysDescription": agentInventorySysDescription,
       "agentInventoryMachineType": agentInventoryMachineType,
       "agentInventoryBurnedInMacAddress": agentInventoryBurnedInMacAddress,
       "agentInventoryAdditionalPackages": agentInventoryAdditionalPackages,
       "agentInventorySoftwareVersion": agentInventorySoftwareVersion,
       "agentTrapLogGroup": agentTrapLogGroup,
       "agentTrapLogTotal": agentTrapLogTotal,
       "agentTrapLogTotalSinceLastViewed": agentTrapLogTotalSinceLastViewed,
       "agentTrapLogTable": agentTrapLogTable,
       "agentTrapLogEntry": agentTrapLogEntry,
       "agentTrapLogIndex": agentTrapLogIndex,
       "agentTrapLogSystemTime": agentTrapLogSystemTime,
       "agentTrapLogTrap": agentTrapLogTrap,
       "agentSupportedMibTable": agentSupportedMibTable,
       "agentSupportedMibEntry": agentSupportedMibEntry,
       "agentSupportedMibIndex": agentSupportedMibIndex,
       "agentSupportedMibName": agentSupportedMibName,
       "agentSupportedMibDescription": agentSupportedMibDescription,
       "agentConfigGroup": agentConfigGroup,
       "agentCLIConfigGroup": agentCLIConfigGroup,
       "agentLoginSessionTable": agentLoginSessionTable,
       "agentLoginSessionEntry": agentLoginSessionEntry,
       "agentLoginSessionIndex": agentLoginSessionIndex,
       "agentLoginSessionUserName": agentLoginSessionUserName,
       "agentLoginSessionIPAddress": agentLoginSessionIPAddress,
       "agentLoginSessionConnectionType": agentLoginSessionConnectionType,
       "agentLoginSessionIdleTime": agentLoginSessionIdleTime,
       "agentLoginSessionSessionTime": agentLoginSessionSessionTime,
       "agentLoginSessionStatus": agentLoginSessionStatus,
       "agentTelnetConfigGroup": agentTelnetConfigGroup,
       "agentTelnetLoginTimeout": agentTelnetLoginTimeout,
       "agentTelnetMaxSessions": agentTelnetMaxSessions,
       "agentTelnetAllowNewMode": agentTelnetAllowNewMode,
       "agentUserConfigGroup": agentUserConfigGroup,
       "agentUserConfigCreate": agentUserConfigCreate,
       "agentUserConfigTable": agentUserConfigTable,
       "agentUserConfigEntry": agentUserConfigEntry,
       "agentUserIndex": agentUserIndex,
       "agentUserName": agentUserName,
       "agentUserPassword": agentUserPassword,
       "agentUserAccessMode": agentUserAccessMode,
       "agentUserStatus": agentUserStatus,
       "agentUserAuthenticationType": agentUserAuthenticationType,
       "agentUserEncryptionType": agentUserEncryptionType,
       "agentUserEncryptionPassword": agentUserEncryptionPassword,
       "agentSerialGroup": agentSerialGroup,
       "agentSerialTimeout": agentSerialTimeout,
       "agentSerialBaudrate": agentSerialBaudrate,
       "agentSerialCharacterSize": agentSerialCharacterSize,
       "agentSerialHWFlowControlMode": agentSerialHWFlowControlMode,
       "agentSerialStopBits": agentSerialStopBits,
       "agentSerialParityType": agentSerialParityType,
       "agentLagConfigGroup": agentLagConfigGroup,
       "agentLagConfigCreate": agentLagConfigCreate,
       "agentLagSummaryConfigTable": agentLagSummaryConfigTable,
       "agentLagSummaryConfigEntry": agentLagSummaryConfigEntry,
       "agentLagSummaryLagIndex": agentLagSummaryLagIndex,
       "agentLagSummaryName": agentLagSummaryName,
       "agentLagSummaryFlushTimer": agentLagSummaryFlushTimer,
       "agentLagSummaryLinkTrap": agentLagSummaryLinkTrap,
       "agentLagSummaryAdminMode": agentLagSummaryAdminMode,
       "agentLagSummaryStpMode": agentLagSummaryStpMode,
       "agentLagSummaryAddPort": agentLagSummaryAddPort,
       "agentLagSummaryDeletePort": agentLagSummaryDeletePort,
       "agentLagSummaryStatus": agentLagSummaryStatus,
       "agentLagSummaryType": agentLagSummaryType,
       "agentLagDetailedConfigTable": agentLagDetailedConfigTable,
       "agentLagDetailedConfigEntry": agentLagDetailedConfigEntry,
       "agentLagDetailedLagIndex": agentLagDetailedLagIndex,
       "agentLagDetailedIfIndex": agentLagDetailedIfIndex,
       "agentLagDetailedPortSpeed": agentLagDetailedPortSpeed,
       "agentLagDetailedPortStatus": agentLagDetailedPortStatus,
       "agentLagConfigStaticCapability": agentLagConfigStaticCapability,
       "agentNetworkConfigGroup": agentNetworkConfigGroup,
       "agentNetworkIPAddress": agentNetworkIPAddress,
       "agentNetworkSubnetMask": agentNetworkSubnetMask,
       "agentNetworkDefaultGateway": agentNetworkDefaultGateway,
       "agentNetworkBurnedInMacAddress": agentNetworkBurnedInMacAddress,
       "agentNetworkConfigProtocol": agentNetworkConfigProtocol,
       "agentNetworkWebMode": agentNetworkWebMode,
       "agentNetworkJavaMode": agentNetworkJavaMode,
       "agentNetworkMgmtVlan": agentNetworkMgmtVlan,
       "agentServicePortConfigGroup": agentServicePortConfigGroup,
       "agentServicePortIPAddress": agentServicePortIPAddress,
       "agentServicePortSubnetMask": agentServicePortSubnetMask,
       "agentServicePortDefaultGateway": agentServicePortDefaultGateway,
       "agentServicePortBurnedInMacAddress": agentServicePortBurnedInMacAddress,
       "agentServicePortConfigProtocol": agentServicePortConfigProtocol,
       "agentSnmpConfigGroup": agentSnmpConfigGroup,
       "agentSnmpCommunityCreate": agentSnmpCommunityCreate,
       "agentSnmpCommunityConfigTable": agentSnmpCommunityConfigTable,
       "agentSnmpCommunityConfigEntry": agentSnmpCommunityConfigEntry,
       "agentSnmpCommunityIndex": agentSnmpCommunityIndex,
       "agentSnmpCommunityName": agentSnmpCommunityName,
       "agentSnmpCommunityIPAddress": agentSnmpCommunityIPAddress,
       "agentSnmpCommunityIPMask": agentSnmpCommunityIPMask,
       "agentSnmpCommunityAccessMode": agentSnmpCommunityAccessMode,
       "agentSnmpCommunityStatus": agentSnmpCommunityStatus,
       "agentSnmpTrapReceiverCreate": agentSnmpTrapReceiverCreate,
       "agentSnmpTrapReceiverConfigTable": agentSnmpTrapReceiverConfigTable,
       "agentSnmpTrapReceiverConfigEntry": agentSnmpTrapReceiverConfigEntry,
       "agentSnmpTrapReceiverIndex": agentSnmpTrapReceiverIndex,
       "agentSnmpTrapReceiverCommunityName": agentSnmpTrapReceiverCommunityName,
       "agentSnmpTrapReceiverIPAddress": agentSnmpTrapReceiverIPAddress,
       "agentSnmpTrapReceiverStatus": agentSnmpTrapReceiverStatus,
       "agentSnmpTrapFlagsConfigGroup": agentSnmpTrapFlagsConfigGroup,
       "agentSnmpAuthenticationTrapFlag": agentSnmpAuthenticationTrapFlag,
       "agentSnmpLinkUpDownTrapFlag": agentSnmpLinkUpDownTrapFlag,
       "agentSnmpMultipleUsersTrapFlag": agentSnmpMultipleUsersTrapFlag,
       "agentSnmpSpanningTreeTrapFlag": agentSnmpSpanningTreeTrapFlag,
       "agentSnmpBroadcastStormTrapFlag": agentSnmpBroadcastStormTrapFlag,
       "agentSpanningTreeConfigGroup": agentSpanningTreeConfigGroup,
       "agentSpanningTreeMode": agentSpanningTreeMode,
       "agentSwitchConfigGroup": agentSwitchConfigGroup,
       "agentSwitchBroadcastControlMode": agentSwitchBroadcastControlMode,
       "agentSwitchDot3FlowControlMode": agentSwitchDot3FlowControlMode,
       "agentSwitchAddressAgingTimeoutTable": agentSwitchAddressAgingTimeoutTable,
       "agentSwitchAddressAgingTimeoutEntry": agentSwitchAddressAgingTimeoutEntry,
       "agentSwitchAddressAgingTimeout": agentSwitchAddressAgingTimeout,
       "agentSwitchIGMPSnoopingGroup": agentSwitchIGMPSnoopingGroup,
       "agentSwitchIGMPSnoopingAdminMode": agentSwitchIGMPSnoopingAdminMode,
       "agentSwitchIGMPSnoopingGroupMembershipInterval": agentSwitchIGMPSnoopingGroupMembershipInterval,
       "agentSwitchIGMPSnoopingMaxResponseTime": agentSwitchIGMPSnoopingMaxResponseTime,
       "agentSwitchIGMPSnoopingMRPExpirationTime": agentSwitchIGMPSnoopingMRPExpirationTime,
       "agentSwitchIGMPSnoopingPortMask": agentSwitchIGMPSnoopingPortMask,
       "agentSwitchIGMPSnoopingMulticastControlFramesProcessed": agentSwitchIGMPSnoopingMulticastControlFramesProcessed,
       "agentSwitchMFDBGroup": agentSwitchMFDBGroup,
       "agentSwitchMFDBTable": agentSwitchMFDBTable,
       "agentSwitchMFDBEntry": agentSwitchMFDBEntry,
       "agentSwitchMFDBVlanId": agentSwitchMFDBVlanId,
       "agentSwitchMFDBMacAddress": agentSwitchMFDBMacAddress,
       "agentSwitchMFDBProtocolType": agentSwitchMFDBProtocolType,
       "agentSwitchMFDBType": agentSwitchMFDBType,
       "agentSwitchMFDBDescription": agentSwitchMFDBDescription,
       "agentSwitchMFDBForwardingPortMask": agentSwitchMFDBForwardingPortMask,
       "agentSwitchMFDBFilteringPortMask": agentSwitchMFDBFilteringPortMask,
       "agentSwitchMFDBSummaryTable": agentSwitchMFDBSummaryTable,
       "agentSwitchMFDBSummaryEntry": agentSwitchMFDBSummaryEntry,
       "agentSwitchMFDBSummaryVlanId": agentSwitchMFDBSummaryVlanId,
       "agentSwitchMFDBSummaryMacAddress": agentSwitchMFDBSummaryMacAddress,
       "agentSwitchMFDBSummaryForwardingPortMask": agentSwitchMFDBSummaryForwardingPortMask,
       "agentSwitchMFDBMaxTableEntries": agentSwitchMFDBMaxTableEntries,
       "agentSwitchMFDBMostEntriesUsed": agentSwitchMFDBMostEntriesUsed,
       "agentSwitchMFDBCurrentEntries": agentSwitchMFDBCurrentEntries,
       "agentTransferConfigGroup": agentTransferConfigGroup,
       "agentTransferUploadGroup": agentTransferUploadGroup,
       "agentTransferUploadMode": agentTransferUploadMode,
       "agentTransferUploadServerIP": agentTransferUploadServerIP,
       "agentTransferUploadPath": agentTransferUploadPath,
       "agentTransferUploadFilename": agentTransferUploadFilename,
       "agentTransferUploadDataType": agentTransferUploadDataType,
       "agentTransferUploadStart": agentTransferUploadStart,
       "agentTransferUploadStatus": agentTransferUploadStatus,
       "agentTransferDownloadGroup": agentTransferDownloadGroup,
       "agentTransferDownloadMode": agentTransferDownloadMode,
       "agentTransferDownloadServerIP": agentTransferDownloadServerIP,
       "agentTransferDownloadPath": agentTransferDownloadPath,
       "agentTransferDownloadFilename": agentTransferDownloadFilename,
       "agentTransferDownloadDataType": agentTransferDownloadDataType,
       "agentTransferDownloadStart": agentTransferDownloadStart,
       "agentTransferDownloadStatus": agentTransferDownloadStatus,
       "agentPortMirroringGroup": agentPortMirroringGroup,
       "agentMirroredPortIfIndex": agentMirroredPortIfIndex,
       "agentProbePortIfIndex": agentProbePortIfIndex,
       "agentPortMirroringMode": agentPortMirroringMode,
       "agentDot3adAggPortTable": agentDot3adAggPortTable,
       "agentDot3adAggPortEntry": agentDot3adAggPortEntry,
       "agentDot3adAggPort": agentDot3adAggPort,
       "agentDot3adAggPortLACPMode": agentDot3adAggPortLACPMode,
       "agentPortConfigTable": agentPortConfigTable,
       "agentPortConfigEntry": agentPortConfigEntry,
       "agentPortDot1dBasePort": agentPortDot1dBasePort,
       "agentPortIfIndex": agentPortIfIndex,
       "agentPortIanaType": agentPortIanaType,
       "agentPortSTPMode": agentPortSTPMode,
       "agentPortSTPState": agentPortSTPState,
       "agentPortAdminMode": agentPortAdminMode,
       "agentPortPhysicalMode": agentPortPhysicalMode,
       "agentPortPhysicalStatus": agentPortPhysicalStatus,
       "agentPortLinkTrapMode": agentPortLinkTrapMode,
       "agentPortClearStats": agentPortClearStats,
       "agentPortDefaultType": agentPortDefaultType,
       "agentPortType": agentPortType,
       "agentPortAutoNegAdminStatus": agentPortAutoNegAdminStatus,
       "agentPortDot3FlowControlMode": agentPortDot3FlowControlMode,
       "agentPortDVlanTagMode": agentPortDVlanTagMode,
       "agentPortDVlanTagEthertype": agentPortDVlanTagEthertype,
       "agentPortDVlanTagCustomerId": agentPortDVlanTagCustomerId,
       "agentPortMaxFrameSizeLimit": agentPortMaxFrameSizeLimit,
       "agentPortMaxFrameSize": agentPortMaxFrameSize,
       "agentProtocolConfigGroup": agentProtocolConfigGroup,
       "agentProtocolGroupCreate": agentProtocolGroupCreate,
       "agentProtocolGroupTable": agentProtocolGroupTable,
       "agentProtocolGroupEntry": agentProtocolGroupEntry,
       "agentProtocolGroupId": agentProtocolGroupId,
       "agentProtocolGroupName": agentProtocolGroupName,
       "agentProtocolGroupVlanId": agentProtocolGroupVlanId,
       "agentProtocolGroupProtocolIP": agentProtocolGroupProtocolIP,
       "agentProtocolGroupProtocolARP": agentProtocolGroupProtocolARP,
       "agentProtocolGroupProtocolIPX": agentProtocolGroupProtocolIPX,
       "agentProtocolGroupStatus": agentProtocolGroupStatus,
       "agentProtocolGroupPortTable": agentProtocolGroupPortTable,
       "agentProtocolGroupPortEntry": agentProtocolGroupPortEntry,
       "agentProtocolGroupPortIfIndex": agentProtocolGroupPortIfIndex,
       "agentProtocolGroupPortStatus": agentProtocolGroupPortStatus,
       "agentStpSwitchConfigGroup": agentStpSwitchConfigGroup,
       "agentStpConfigDigestKey": agentStpConfigDigestKey,
       "agentStpConfigFormatSelector": agentStpConfigFormatSelector,
       "agentStpConfigName": agentStpConfigName,
       "agentStpConfigRevision": agentStpConfigRevision,
       "agentStpForceVersion": agentStpForceVersion,
       "agentStpAdminMode": agentStpAdminMode,
       "agentStpPortTable": agentStpPortTable,
       "agentStpPortEntry": agentStpPortEntry,
       "agentStpPortState": agentStpPortState,
       "agentStpPortStatsMstpBpduRx": agentStpPortStatsMstpBpduRx,
       "agentStpPortStatsMstpBpduTx": agentStpPortStatsMstpBpduTx,
       "agentStpPortStatsRstpBpduRx": agentStpPortStatsRstpBpduRx,
       "agentStpPortStatsRstpBpduTx": agentStpPortStatsRstpBpduTx,
       "agentStpPortStatsStpBpduRx": agentStpPortStatsStpBpduRx,
       "agentStpPortStatsStpBpduTx": agentStpPortStatsStpBpduTx,
       "agentStpPortUpTime": agentStpPortUpTime,
       "agentStpPortMigrationCheck": agentStpPortMigrationCheck,
       "agentStpCstConfigGroup": agentStpCstConfigGroup,
       "agentStpCstHelloTime": agentStpCstHelloTime,
       "agentStpCstMaxAge": agentStpCstMaxAge,
       "agentStpCstRegionalRootId": agentStpCstRegionalRootId,
       "agentStpCstRegionalRootPathCost": agentStpCstRegionalRootPathCost,
       "agentStpCstRootFwdDelay": agentStpCstRootFwdDelay,
       "agentStpCstBridgeFwdDelay": agentStpCstBridgeFwdDelay,
       "agentStpCstBridgeHelloTime": agentStpCstBridgeHelloTime,
       "agentStpCstBridgeHoldTime": agentStpCstBridgeHoldTime,
       "agentStpCstBridgeMaxAge": agentStpCstBridgeMaxAge,
       "agentStpCstPortTable": agentStpCstPortTable,
       "agentStpCstPortEntry": agentStpCstPortEntry,
       "agentStpCstPortOperEdge": agentStpCstPortOperEdge,
       "agentStpCstPortOperPointToPoint": agentStpCstPortOperPointToPoint,
       "agentStpCstPortTopologyChangeAck": agentStpCstPortTopologyChangeAck,
       "agentStpCstPortEdge": agentStpCstPortEdge,
       "agentStpCstPortForwardingState": agentStpCstPortForwardingState,
       "agentStpCstPortId": agentStpCstPortId,
       "agentStpCstPortPathCost": agentStpCstPortPathCost,
       "agentStpCstPortPriority": agentStpCstPortPriority,
       "agentStpCstDesignatedBridgeId": agentStpCstDesignatedBridgeId,
       "agentStpCstDesignatedCost": agentStpCstDesignatedCost,
       "agentStpCstDesignatedPortId": agentStpCstDesignatedPortId,
       "agentStpMstTable": agentStpMstTable,
       "agentStpMstEntry": agentStpMstEntry,
       "agentStpMstId": agentStpMstId,
       "agentStpMstBridgePriority": agentStpMstBridgePriority,
       "agentStpMstBridgeIdentifier": agentStpMstBridgeIdentifier,
       "agentStpMstDesignatedRootId": agentStpMstDesignatedRootId,
       "agentStpMstRootPathCost": agentStpMstRootPathCost,
       "agentStpMstRootPortId": agentStpMstRootPortId,
       "agentStpMstTimeSinceTopologyChange": agentStpMstTimeSinceTopologyChange,
       "agentStpMstTopologyChangeCount": agentStpMstTopologyChangeCount,
       "agentStpMstTopologyChangeParm": agentStpMstTopologyChangeParm,
       "agentStpMstRowStatus": agentStpMstRowStatus,
       "agentStpMstPortTable": agentStpMstPortTable,
       "agentStpMstPortEntry": agentStpMstPortEntry,
       "agentStpMstPortForwardingState": agentStpMstPortForwardingState,
       "agentStpMstPortId": agentStpMstPortId,
       "agentStpMstPortPathCost": agentStpMstPortPathCost,
       "agentStpMstPortPriority": agentStpMstPortPriority,
       "agentStpMstDesignatedBridgeId": agentStpMstDesignatedBridgeId,
       "agentStpMstDesignatedCost": agentStpMstDesignatedCost,
       "agentStpMstDesignatedPortId": agentStpMstDesignatedPortId,
       "agentStpMstVlanTable": agentStpMstVlanTable,
       "agentStpMstVlanEntry": agentStpMstVlanEntry,
       "agentStpMstVlanRowStatus": agentStpMstVlanRowStatus,
       "agentAuthenticationGroup": agentAuthenticationGroup,
       "agentAuthenticationListCreate": agentAuthenticationListCreate,
       "agentAuthenticationListTable": agentAuthenticationListTable,
       "agentAuthenticationListEntry": agentAuthenticationListEntry,
       "agentAuthenticationListIndex": agentAuthenticationListIndex,
       "agentAuthenticationListName": agentAuthenticationListName,
       "agentAuthenticationListMethod1": agentAuthenticationListMethod1,
       "agentAuthenticationListMethod2": agentAuthenticationListMethod2,
       "agentAuthenticationListMethod3": agentAuthenticationListMethod3,
       "agentAuthenticationListStatus": agentAuthenticationListStatus,
       "agentUserConfigDefaultAuthenticationList": agentUserConfigDefaultAuthenticationList,
       "agentUserAuthenticationConfigTable": agentUserAuthenticationConfigTable,
       "agentUserAuthenticationConfigEntry": agentUserAuthenticationConfigEntry,
       "agentUserAuthenticationList": agentUserAuthenticationList,
       "agentUserPortConfigTable": agentUserPortConfigTable,
       "agentUserPortConfigEntry": agentUserPortConfigEntry,
       "agentUserPortSecurity": agentUserPortSecurity,
       "agentClassOfServiceGroup": agentClassOfServiceGroup,
       "agentClassOfServiceTable": agentClassOfServiceTable,
       "agentClassOfServiceEntry": agentClassOfServiceEntry,
       "agentClassOfServicePriority": agentClassOfServicePriority,
       "agentClassOfServiceClass": agentClassOfServiceClass,
       "agentSystemGroup": agentSystemGroup,
       "agentSaveConfig": agentSaveConfig,
       "agentClearConfig": agentClearConfig,
       "agentClearLags": agentClearLags,
       "agentClearLoginSessions": agentClearLoginSessions,
       "agentClearPasswords": agentClearPasswords,
       "agentClearPortStats": agentClearPortStats,
       "agentClearSwitchStats": agentClearSwitchStats,
       "agentClearTrapLog": agentClearTrapLog,
       "agentClearVlan": agentClearVlan,
       "agentResetSystem": agentResetSystem,
       "agentSaveConfigStatus": agentSaveConfigStatus,
       "agentCableTesterGroup": agentCableTesterGroup,
       "agentCableTesterStatus": agentCableTesterStatus,
       "agentCableTesterIfIndex": agentCableTesterIfIndex,
       "agentCableTesterCableStatus": agentCableTesterCableStatus,
       "agentCableTesterMinimumCableLength": agentCableTesterMinimumCableLength,
       "agentCableTesterMaximumCableLength": agentCableTesterMaximumCableLength,
       "agentCableTesterCableFailureLocation": agentCableTesterCableFailureLocation,
       "gsm7312SwitchingTraps": gsm7312SwitchingTraps,
       "multipleUsersTrap": multipleUsersTrap,
       "broadcastStormStartTrap": broadcastStormStartTrap,
       "broadcastStormEndTrap": broadcastStormEndTrap,
       "linkFailureTrap": linkFailureTrap,
       "vlanRequestFailureTrap": vlanRequestFailureTrap,
       "vlanDeleteLastTrap": vlanDeleteLastTrap,
       "vlanDefaultCfgFailureTrap": vlanDefaultCfgFailureTrap,
       "vlanRestoreFailureTrap": vlanRestoreFailureTrap,
       "fanFailureTrap": fanFailureTrap,
       "stpInstanceNewRootTrap": stpInstanceNewRootTrap,
       "stpInstanceTopologyChangeTrap": stpInstanceTopologyChangeTrap,
       "powerSupplyStatusChangeTrap": powerSupplyStatusChangeTrap}
)
