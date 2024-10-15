# SNMP MIB module (ALVARION-USER-ACCOUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-USER-ACCOUNT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:47 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alvarionUserAccountMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionUserAccountMIBObjects_ObjectIdentity = ObjectIdentity
alvarionUserAccountMIBObjects = _AlvarionUserAccountMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1)
)
_CoUserAccountStatusGroup_ObjectIdentity = ObjectIdentity
coUserAccountStatusGroup = _CoUserAccountStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1)
)
_CoUserAccountStatusTable_Object = MibTable
coUserAccountStatusTable = _CoUserAccountStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coUserAccountStatusTable.setStatus("current")
_CoUserAccountStatusEntry_Object = MibTableRow
coUserAccountStatusEntry = _CoUserAccountStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1)
)
coUserAccountStatusEntry.setIndexNames(
    (0, "ALVARION-USER-ACCOUNT-MIB", "coUserAccIndex"),
)
if mibBuilder.loadTexts:
    coUserAccountStatusEntry.setStatus("current")


class _CoUserAccIndex_Type(Integer32):
    """Custom type coUserAccIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoUserAccIndex_Type.__name__ = "Integer32"
_CoUserAccIndex_Object = MibTableColumn
coUserAccIndex = _CoUserAccIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 1),
    _CoUserAccIndex_Type()
)
coUserAccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coUserAccIndex.setStatus("current")
_CoUserAccUserName_Type = DisplayString
_CoUserAccUserName_Object = MibTableColumn
coUserAccUserName = _CoUserAccUserName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 2),
    _CoUserAccUserName_Type()
)
coUserAccUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccUserName.setStatus("current")
_CoUserAccPlanName_Type = DisplayString
_CoUserAccPlanName_Object = MibTableColumn
coUserAccPlanName = _CoUserAccPlanName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 3),
    _CoUserAccPlanName_Type()
)
coUserAccPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccPlanName.setStatus("current")
_CoUserAccRemainingOnlineTime_Type = Integer32
_CoUserAccRemainingOnlineTime_Object = MibTableColumn
coUserAccRemainingOnlineTime = _CoUserAccRemainingOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 4),
    _CoUserAccRemainingOnlineTime_Type()
)
coUserAccRemainingOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccRemainingOnlineTime.setStatus("current")
if mibBuilder.loadTexts:
    coUserAccRemainingOnlineTime.setUnits("seconds")
_CoUserAccFirstLoginTime_Type = DisplayString
_CoUserAccFirstLoginTime_Object = MibTableColumn
coUserAccFirstLoginTime = _CoUserAccFirstLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 5),
    _CoUserAccFirstLoginTime_Type()
)
coUserAccFirstLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccFirstLoginTime.setStatus("current")
_CoUserAccRemainingSessionTime_Type = Integer32
_CoUserAccRemainingSessionTime_Object = MibTableColumn
coUserAccRemainingSessionTime = _CoUserAccRemainingSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 6),
    _CoUserAccRemainingSessionTime_Type()
)
coUserAccRemainingSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccRemainingSessionTime.setStatus("current")
if mibBuilder.loadTexts:
    coUserAccRemainingSessionTime.setUnits("seconds")


class _CoUserAccStatus_Type(Integer32):
    """Custom type coUserAccStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_CoUserAccStatus_Type.__name__ = "Integer32"
_CoUserAccStatus_Object = MibTableColumn
coUserAccStatus = _CoUserAccStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 7),
    _CoUserAccStatus_Type()
)
coUserAccStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccStatus.setStatus("current")
_CoUserAccExpirationTime_Type = DisplayString
_CoUserAccExpirationTime_Object = MibTableColumn
coUserAccExpirationTime = _CoUserAccExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 1, 1, 1, 1, 8),
    _CoUserAccExpirationTime_Type()
)
coUserAccExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccExpirationTime.setStatus("current")
_AlvarionUserAccountMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionUserAccountMIBNotificationPrefix = _AlvarionUserAccountMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 2)
)
_AlvarionUserAccountMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionUserAccountMIBNotifications = _AlvarionUserAccountMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 2, 0)
)
_AlvarionUserAccountMIBConformance_ObjectIdentity = ObjectIdentity
alvarionUserAccountMIBConformance = _AlvarionUserAccountMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 3)
)
_AlvarionUserAccountMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionUserAccountMIBCompliances = _AlvarionUserAccountMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 3, 1)
)
_AlvarionUserAccountMIBGroups_ObjectIdentity = ObjectIdentity
alvarionUserAccountMIBGroups = _AlvarionUserAccountMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 3, 2)
)

# Managed Objects groups

alvarionUserAccountStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 3, 2, 1)
)
alvarionUserAccountStatusMIBGroup.setObjects(
      *(("ALVARION-USER-ACCOUNT-MIB", "coUserAccUserName"),
        ("ALVARION-USER-ACCOUNT-MIB", "coUserAccPlanName"),
        ("ALVARION-USER-ACCOUNT-MIB", "coUserAccRemainingOnlineTime"),
        ("ALVARION-USER-ACCOUNT-MIB", "coUserAccFirstLoginTime"),
        ("ALVARION-USER-ACCOUNT-MIB", "coUserAccRemainingSessionTime"),
        ("ALVARION-USER-ACCOUNT-MIB", "coUserAccStatus"),
        ("ALVARION-USER-ACCOUNT-MIB", "coUserAccExpirationTime"))
)
if mibBuilder.loadTexts:
    alvarionUserAccountStatusMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionUserAccountMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 35, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionUserAccountMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-USER-ACCOUNT-MIB",
    **{"alvarionUserAccountMIB": alvarionUserAccountMIB,
       "alvarionUserAccountMIBObjects": alvarionUserAccountMIBObjects,
       "coUserAccountStatusGroup": coUserAccountStatusGroup,
       "coUserAccountStatusTable": coUserAccountStatusTable,
       "coUserAccountStatusEntry": coUserAccountStatusEntry,
       "coUserAccIndex": coUserAccIndex,
       "coUserAccUserName": coUserAccUserName,
       "coUserAccPlanName": coUserAccPlanName,
       "coUserAccRemainingOnlineTime": coUserAccRemainingOnlineTime,
       "coUserAccFirstLoginTime": coUserAccFirstLoginTime,
       "coUserAccRemainingSessionTime": coUserAccRemainingSessionTime,
       "coUserAccStatus": coUserAccStatus,
       "coUserAccExpirationTime": coUserAccExpirationTime,
       "alvarionUserAccountMIBNotificationPrefix": alvarionUserAccountMIBNotificationPrefix,
       "alvarionUserAccountMIBNotifications": alvarionUserAccountMIBNotifications,
       "alvarionUserAccountMIBConformance": alvarionUserAccountMIBConformance,
       "alvarionUserAccountMIBCompliances": alvarionUserAccountMIBCompliances,
       "alvarionUserAccountMIBCompliance": alvarionUserAccountMIBCompliance,
       "alvarionUserAccountMIBGroups": alvarionUserAccountMIBGroups,
       "alvarionUserAccountStatusMIBGroup": alvarionUserAccountStatusMIBGroup}
)
