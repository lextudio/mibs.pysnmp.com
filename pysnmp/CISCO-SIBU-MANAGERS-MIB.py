# SNMP MIB module (CISCO-SIBU-MANAGERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SIBU-MANAGERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:15 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSibuManagersMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46)
)
ciscoSibuManagersMIB.setRevisions(
        ("1998-10-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSibuManagersMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSibuManagersMIBObjects = _CiscoSibuManagersMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1)
)
_CmIpConfig_ObjectIdentity = ObjectIdentity
cmIpConfig = _CmIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 1)
)


class _CmIpConfigMethod_Type(Integer32):
    """Custom type cmIpConfigMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("manual", 1))
    )


_CmIpConfigMethod_Type.__name__ = "Integer32"
_CmIpConfigMethod_Object = MibScalar
cmIpConfigMethod = _CmIpConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 1, 1),
    _CmIpConfigMethod_Type()
)
cmIpConfigMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpConfigMethod.setStatus("current")


class _CmIpConfigAddress_Type(IpAddress):
    """Custom type cmIpConfigAddress based on IpAddress"""
    defaultHexValue = "00000000"


_CmIpConfigAddress_Object = MibScalar
cmIpConfigAddress = _CmIpConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 1, 2),
    _CmIpConfigAddress_Type()
)
cmIpConfigAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpConfigAddress.setStatus("current")


class _CmIpConfigSubnetMask_Type(IpAddress):
    """Custom type cmIpConfigSubnetMask based on IpAddress"""
    defaultHexValue = "00000000"


_CmIpConfigSubnetMask_Object = MibScalar
cmIpConfigSubnetMask = _CmIpConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 1, 3),
    _CmIpConfigSubnetMask_Type()
)
cmIpConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpConfigSubnetMask.setStatus("current")


class _CmIpConfigDefaultGateway_Type(IpAddress):
    """Custom type cmIpConfigDefaultGateway based on IpAddress"""
    defaultHexValue = "00000000"


_CmIpConfigDefaultGateway_Object = MibScalar
cmIpConfigDefaultGateway = _CmIpConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 1, 4),
    _CmIpConfigDefaultGateway_Type()
)
cmIpConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpConfigDefaultGateway.setStatus("current")
_CmConsoleConfig_ObjectIdentity = ObjectIdentity
cmConsoleConfig = _CmConsoleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 2)
)


class _CmConsoleCLIInactiveTimeout_Type(Integer32):
    """Custom type cmConsoleCLIInactiveTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 65500),
    )


_CmConsoleCLIInactiveTimeout_Type.__name__ = "Integer32"
_CmConsoleCLIInactiveTimeout_Object = MibScalar
cmConsoleCLIInactiveTimeout = _CmConsoleCLIInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 2, 1),
    _CmConsoleCLIInactiveTimeout_Type()
)
cmConsoleCLIInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmConsoleCLIInactiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cmConsoleCLIInactiveTimeout.setUnits("seconds")


class _CmConsoleCLIPasswordMaxAttempts_Type(Integer32):
    """Custom type cmConsoleCLIPasswordMaxAttempts based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_CmConsoleCLIPasswordMaxAttempts_Type.__name__ = "Integer32"
_CmConsoleCLIPasswordMaxAttempts_Object = MibScalar
cmConsoleCLIPasswordMaxAttempts = _CmConsoleCLIPasswordMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 2, 2),
    _CmConsoleCLIPasswordMaxAttempts_Type()
)
cmConsoleCLIPasswordMaxAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmConsoleCLIPasswordMaxAttempts.setStatus("current")
if mibBuilder.loadTexts:
    cmConsoleCLIPasswordMaxAttempts.setUnits("attempts")


class _CmConsoleCLISilentTime_Type(Integer32):
    """Custom type cmConsoleCLISilentTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_CmConsoleCLISilentTime_Type.__name__ = "Integer32"
_CmConsoleCLISilentTime_Object = MibScalar
cmConsoleCLISilentTime = _CmConsoleCLISilentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 2, 3),
    _CmConsoleCLISilentTime_Type()
)
cmConsoleCLISilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmConsoleCLISilentTime.setStatus("current")


class _CmConsoleWebAdminState_Type(Integer32):
    """Custom type cmConsoleWebAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CmConsoleWebAdminState_Type.__name__ = "Integer32"
_CmConsoleWebAdminState_Object = MibScalar
cmConsoleWebAdminState = _CmConsoleWebAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 2, 4),
    _CmConsoleWebAdminState_Type()
)
cmConsoleWebAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmConsoleWebAdminState.setStatus("current")


class _CmConsoleWebHttpPort_Type(Integer32):
    """Custom type cmConsoleWebHttpPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmConsoleWebHttpPort_Type.__name__ = "Integer32"
_CmConsoleWebHttpPort_Object = MibScalar
cmConsoleWebHttpPort = _CmConsoleWebHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 2, 5),
    _CmConsoleWebHttpPort_Type()
)
cmConsoleWebHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmConsoleWebHttpPort.setStatus("current")
_CmSnmpSetManager_ObjectIdentity = ObjectIdentity
cmSnmpSetManager = _CmSnmpSetManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 3)
)
_CmSnmpSetManagerTable_Object = MibTable
cmSnmpSetManagerTable = _CmSnmpSetManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmSnmpSetManagerTable.setStatus("current")
_CmSnmpSetManagerEntry_Object = MibTableRow
cmSnmpSetManagerEntry = _CmSnmpSetManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 3, 1, 1)
)
cmSnmpSetManagerEntry.setIndexNames(
    (0, "CISCO-SIBU-MANAGERS-MIB", "cmSnmpSetManagerAddr"),
)
if mibBuilder.loadTexts:
    cmSnmpSetManagerEntry.setStatus("current")
_CmSnmpSetManagerAddr_Type = IpAddress
_CmSnmpSetManagerAddr_Object = MibTableColumn
cmSnmpSetManagerAddr = _CmSnmpSetManagerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 3, 1, 1, 1),
    _CmSnmpSetManagerAddr_Type()
)
cmSnmpSetManagerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmSnmpSetManagerAddr.setStatus("current")
_CmSnmpSetManagerRowStatus_Type = RowStatus
_CmSnmpSetManagerRowStatus_Object = MibTableColumn
cmSnmpSetManagerRowStatus = _CmSnmpSetManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 3, 1, 1, 2),
    _CmSnmpSetManagerRowStatus_Type()
)
cmSnmpSetManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSnmpSetManagerRowStatus.setStatus("current")
_CmSnmpTrapManager_ObjectIdentity = ObjectIdentity
cmSnmpTrapManager = _CmSnmpTrapManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 4)
)
_CmSnmpTrapManagerTable_Object = MibTable
cmSnmpTrapManagerTable = _CmSnmpTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cmSnmpTrapManagerTable.setStatus("current")
_CmSnmpTrapManagerEntry_Object = MibTableRow
cmSnmpTrapManagerEntry = _CmSnmpTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 4, 1, 1)
)
cmSnmpTrapManagerEntry.setIndexNames(
    (0, "CISCO-SIBU-MANAGERS-MIB", "cmSnmpTrapManagerAddr"),
)
if mibBuilder.loadTexts:
    cmSnmpTrapManagerEntry.setStatus("current")
_CmSnmpTrapManagerAddr_Type = IpAddress
_CmSnmpTrapManagerAddr_Object = MibTableColumn
cmSnmpTrapManagerAddr = _CmSnmpTrapManagerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 4, 1, 1, 1),
    _CmSnmpTrapManagerAddr_Type()
)
cmSnmpTrapManagerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmSnmpTrapManagerAddr.setStatus("current")


class _CmSnmpTrapManagerCommunity_Type(DisplayString):
    """Custom type cmSnmpTrapManagerCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmSnmpTrapManagerCommunity_Type.__name__ = "DisplayString"
_CmSnmpTrapManagerCommunity_Object = MibTableColumn
cmSnmpTrapManagerCommunity = _CmSnmpTrapManagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 4, 1, 1, 2),
    _CmSnmpTrapManagerCommunity_Type()
)
cmSnmpTrapManagerCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSnmpTrapManagerCommunity.setStatus("current")
_CmSnmpTrapManagerRowStatus_Type = RowStatus
_CmSnmpTrapManagerRowStatus_Object = MibTableColumn
cmSnmpTrapManagerRowStatus = _CmSnmpTrapManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 1, 4, 1, 1, 3),
    _CmSnmpTrapManagerRowStatus_Type()
)
cmSnmpTrapManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSnmpTrapManagerRowStatus.setStatus("current")
_CiscoSibuManagersNotifications_ObjectIdentity = ObjectIdentity
ciscoSibuManagersNotifications = _CiscoSibuManagersNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 2)
)
_CiscoSibuManagersNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoSibuManagersNotificationsPrefix = _CiscoSibuManagersNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 2, 0)
)
_CiscoSibuManagersMIBComformance_ObjectIdentity = ObjectIdentity
ciscoSibuManagersMIBComformance = _CiscoSibuManagersMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3)
)
_CiscoSibuManagersMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSibuManagersMIBCompliances = _CiscoSibuManagersMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 1)
)
_CiscoSibuManagersMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSibuManagersMIBGroups = _CiscoSibuManagersMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 2)
)

# Managed Objects groups

ciscoSibuManagersIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 2, 1)
)
ciscoSibuManagersIpConfigGroup.setObjects(
      *(("CISCO-SIBU-MANAGERS-MIB", "cmIpConfigMethod"),
        ("CISCO-SIBU-MANAGERS-MIB", "cmIpConfigAddress"),
        ("CISCO-SIBU-MANAGERS-MIB", "cmIpConfigSubnetMask"),
        ("CISCO-SIBU-MANAGERS-MIB", "cmIpConfigDefaultGateway"))
)
if mibBuilder.loadTexts:
    ciscoSibuManagersIpConfigGroup.setStatus("current")

ciscoSibuManagersCLIConsoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 2, 2)
)
ciscoSibuManagersCLIConsoleGroup.setObjects(
      *(("CISCO-SIBU-MANAGERS-MIB", "cmConsoleCLIInactiveTimeout"),
        ("CISCO-SIBU-MANAGERS-MIB", "cmConsoleCLIPasswordMaxAttempts"),
        ("CISCO-SIBU-MANAGERS-MIB", "cmConsoleCLISilentTime"))
)
if mibBuilder.loadTexts:
    ciscoSibuManagersCLIConsoleGroup.setStatus("current")

ciscoSibuManagersWebConsoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 2, 3)
)
ciscoSibuManagersWebConsoleGroup.setObjects(
      *(("CISCO-SIBU-MANAGERS-MIB", "cmConsoleWebAdminState"),
        ("CISCO-SIBU-MANAGERS-MIB", "cmConsoleWebHttpPort"))
)
if mibBuilder.loadTexts:
    ciscoSibuManagersWebConsoleGroup.setStatus("current")

ciscoSibuManagersSnmpSetManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 2, 4)
)
ciscoSibuManagersSnmpSetManagerGroup.setObjects(
    ("CISCO-SIBU-MANAGERS-MIB", "cmSnmpSetManagerRowStatus")
)
if mibBuilder.loadTexts:
    ciscoSibuManagersSnmpSetManagerGroup.setStatus("current")

ciscoSibuManagersSnmpTrapManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 2, 5)
)
ciscoSibuManagersSnmpTrapManagerGroup.setObjects(
      *(("CISCO-SIBU-MANAGERS-MIB", "cmSnmpTrapManagerCommunity"),
        ("CISCO-SIBU-MANAGERS-MIB", "cmSnmpTrapManagerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSibuManagersSnmpTrapManagerGroup.setStatus("current")


# Notification objects

ciscoSibuManagersConsoleLogonIntruder = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 2, 0, 1)
)
if mibBuilder.loadTexts:
    ciscoSibuManagersConsoleLogonIntruder.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSibuManagersCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 46, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSibuManagersCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SIBU-MANAGERS-MIB",
    **{"ciscoSibuManagersMIB": ciscoSibuManagersMIB,
       "ciscoSibuManagersMIBObjects": ciscoSibuManagersMIBObjects,
       "cmIpConfig": cmIpConfig,
       "cmIpConfigMethod": cmIpConfigMethod,
       "cmIpConfigAddress": cmIpConfigAddress,
       "cmIpConfigSubnetMask": cmIpConfigSubnetMask,
       "cmIpConfigDefaultGateway": cmIpConfigDefaultGateway,
       "cmConsoleConfig": cmConsoleConfig,
       "cmConsoleCLIInactiveTimeout": cmConsoleCLIInactiveTimeout,
       "cmConsoleCLIPasswordMaxAttempts": cmConsoleCLIPasswordMaxAttempts,
       "cmConsoleCLISilentTime": cmConsoleCLISilentTime,
       "cmConsoleWebAdminState": cmConsoleWebAdminState,
       "cmConsoleWebHttpPort": cmConsoleWebHttpPort,
       "cmSnmpSetManager": cmSnmpSetManager,
       "cmSnmpSetManagerTable": cmSnmpSetManagerTable,
       "cmSnmpSetManagerEntry": cmSnmpSetManagerEntry,
       "cmSnmpSetManagerAddr": cmSnmpSetManagerAddr,
       "cmSnmpSetManagerRowStatus": cmSnmpSetManagerRowStatus,
       "cmSnmpTrapManager": cmSnmpTrapManager,
       "cmSnmpTrapManagerTable": cmSnmpTrapManagerTable,
       "cmSnmpTrapManagerEntry": cmSnmpTrapManagerEntry,
       "cmSnmpTrapManagerAddr": cmSnmpTrapManagerAddr,
       "cmSnmpTrapManagerCommunity": cmSnmpTrapManagerCommunity,
       "cmSnmpTrapManagerRowStatus": cmSnmpTrapManagerRowStatus,
       "ciscoSibuManagersNotifications": ciscoSibuManagersNotifications,
       "ciscoSibuManagersNotificationsPrefix": ciscoSibuManagersNotificationsPrefix,
       "ciscoSibuManagersConsoleLogonIntruder": ciscoSibuManagersConsoleLogonIntruder,
       "ciscoSibuManagersMIBComformance": ciscoSibuManagersMIBComformance,
       "ciscoSibuManagersMIBCompliances": ciscoSibuManagersMIBCompliances,
       "ciscoSibuManagersCompliance": ciscoSibuManagersCompliance,
       "ciscoSibuManagersMIBGroups": ciscoSibuManagersMIBGroups,
       "ciscoSibuManagersIpConfigGroup": ciscoSibuManagersIpConfigGroup,
       "ciscoSibuManagersCLIConsoleGroup": ciscoSibuManagersCLIConsoleGroup,
       "ciscoSibuManagersWebConsoleGroup": ciscoSibuManagersWebConsoleGroup,
       "ciscoSibuManagersSnmpSetManagerGroup": ciscoSibuManagersSnmpSetManagerGroup,
       "ciscoSibuManagersSnmpTrapManagerGroup": ciscoSibuManagersSnmpTrapManagerGroup}
)
