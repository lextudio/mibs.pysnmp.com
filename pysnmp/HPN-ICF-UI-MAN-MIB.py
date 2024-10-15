# SNMP MIB module (HPN-ICF-UI-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-UI-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:04 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfUIMgt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfUIMgtObjects_ObjectIdentity = ObjectIdentity
hpnicfUIMgtObjects = _HpnicfUIMgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1)
)
_HpnicfUIBasicInfo_ObjectIdentity = ObjectIdentity
hpnicfUIBasicInfo = _HpnicfUIBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1)
)
_HpnicfUIScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfUIScalarObjects = _HpnicfUIScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 1)
)
_HpnicfUITrapBindObjects_ObjectIdentity = ObjectIdentity
hpnicfUITrapBindObjects = _HpnicfUITrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2)
)
_HpnicfTerminalUserName_Type = DisplayString
_HpnicfTerminalUserName_Object = MibScalar
hpnicfTerminalUserName = _HpnicfTerminalUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2, 1),
    _HpnicfTerminalUserName_Type()
)
hpnicfTerminalUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfTerminalUserName.setStatus("current")
_HpnicfTerminalSource_Type = DisplayString
_HpnicfTerminalSource_Object = MibScalar
hpnicfTerminalSource = _HpnicfTerminalSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2, 2),
    _HpnicfTerminalSource_Type()
)
hpnicfTerminalSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfTerminalSource.setStatus("current")


class _HpnicfTerminalUserAuthFailureReason_Type(Integer32):
    """Custom type hpnicfTerminalUserAuthFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authTimeout", 2),
          ("exceedRetries", 1),
          ("otherReason", 3))
    )


_HpnicfTerminalUserAuthFailureReason_Type.__name__ = "Integer32"
_HpnicfTerminalUserAuthFailureReason_Object = MibScalar
hpnicfTerminalUserAuthFailureReason = _HpnicfTerminalUserAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2, 3),
    _HpnicfTerminalUserAuthFailureReason_Type()
)
hpnicfTerminalUserAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfTerminalUserAuthFailureReason.setStatus("current")
_HpnicfUINotifications_ObjectIdentity = ObjectIdentity
hpnicfUINotifications = _HpnicfUINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3)
)
_HpnicfUINotificationsPrefix_ObjectIdentity = ObjectIdentity
hpnicfUINotificationsPrefix = _HpnicfUINotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0)
)
_HpnicfVtyMan_ObjectIdentity = ObjectIdentity
hpnicfVtyMan = _HpnicfVtyMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2)
)
_HpnicfVtyAccTable_Object = MibTable
hpnicfVtyAccTable = _HpnicfVtyAccTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfVtyAccTable.setStatus("current")
_HpnicfVtyAccEntry_Object = MibTableRow
hpnicfVtyAccEntry = _HpnicfVtyAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1)
)
hpnicfVtyAccEntry.setIndexNames(
    (0, "HPN-ICF-UI-MAN-MIB", "hpnicfVtyAccUserIndex"),
    (0, "HPN-ICF-UI-MAN-MIB", "hpnicfVtyAccConnway"),
)
if mibBuilder.loadTexts:
    hpnicfVtyAccEntry.setStatus("current")


class _HpnicfVtyAccUserIndex_Type(Integer32):
    """Custom type hpnicfVtyAccUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfVtyAccUserIndex_Type.__name__ = "Integer32"
_HpnicfVtyAccUserIndex_Object = MibTableColumn
hpnicfVtyAccUserIndex = _HpnicfVtyAccUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 1),
    _HpnicfVtyAccUserIndex_Type()
)
hpnicfVtyAccUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVtyAccUserIndex.setStatus("current")


class _HpnicfVtyAccConnway_Type(Integer32):
    """Custom type hpnicfVtyAccConnway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("acl6inbound", 11),
          ("acl6outbound", 12),
          ("inbound", 1),
          ("linkinbound", 3),
          ("outbound", 2))
    )


_HpnicfVtyAccConnway_Type.__name__ = "Integer32"
_HpnicfVtyAccConnway_Object = MibTableColumn
hpnicfVtyAccConnway = _HpnicfVtyAccConnway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 2),
    _HpnicfVtyAccConnway_Type()
)
hpnicfVtyAccConnway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVtyAccConnway.setStatus("current")
_HpnicfVtyAccAclNum_Type = Integer32
_HpnicfVtyAccAclNum_Object = MibTableColumn
hpnicfVtyAccAclNum = _HpnicfVtyAccAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 3),
    _HpnicfVtyAccAclNum_Type()
)
hpnicfVtyAccAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVtyAccAclNum.setStatus("current")
_HpnicfVtyAccEntryRowStatus_Type = RowStatus
_HpnicfVtyAccEntryRowStatus_Object = MibTableColumn
hpnicfVtyAccEntryRowStatus = _HpnicfVtyAccEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 4),
    _HpnicfVtyAccEntryRowStatus_Type()
)
hpnicfVtyAccEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVtyAccEntryRowStatus.setStatus("current")
_HpnicfConStatus_ObjectIdentity = ObjectIdentity
hpnicfConStatus = _HpnicfConStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3)
)
_HpnicfConStatusTable_Object = MibTable
hpnicfConStatusTable = _HpnicfConStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfConStatusTable.setStatus("current")
_HpnicfConStatusEntry_Object = MibTableRow
hpnicfConStatusEntry = _HpnicfConStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1, 1)
)
hpnicfConStatusEntry.setIndexNames(
    (0, "HPN-ICF-UI-MAN-MIB", "hpnicfConUserIndex"),
)
if mibBuilder.loadTexts:
    hpnicfConStatusEntry.setStatus("current")
_HpnicfConUserIndex_Type = Integer32
_HpnicfConUserIndex_Object = MibTableColumn
hpnicfConUserIndex = _HpnicfConUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1, 1, 1),
    _HpnicfConUserIndex_Type()
)
hpnicfConUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfConUserIndex.setStatus("current")


class _HpnicfConReAuth_Type(Integer32):
    """Custom type hpnicfConReAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HpnicfConReAuth_Type.__name__ = "Integer32"
_HpnicfConReAuth_Object = MibTableColumn
hpnicfConReAuth = _HpnicfConReAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1, 1, 2),
    _HpnicfConReAuth_Type()
)
hpnicfConReAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfConReAuth.setStatus("current")
_HpnicfUIMgtMIBConformance18_ObjectIdentity = ObjectIdentity
hpnicfUIMgtMIBConformance18 = _HpnicfUIMgtMIBConformance18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2)
)
_HpnicfUIMgtMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfUIMgtMIBCompliances = _HpnicfUIMgtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 1)
)
_HpnicfUIMgtManMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfUIMgtManMIBGroups = _HpnicfUIMgtManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 2)
)

# Managed Objects groups

hpnicfUIMgtBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 2, 1)
)
hpnicfUIMgtBasicGroup.setObjects(
    ("HPN-ICF-UI-MAN-MIB", "hpnicfVtyAccAclNum")
)
if mibBuilder.loadTexts:
    hpnicfUIMgtBasicGroup.setStatus("current")

hpnicfConStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 2, 2)
)
hpnicfConStatusGroup.setObjects(
    ("HPN-ICF-UI-MAN-MIB", "hpnicfConReAuth")
)
if mibBuilder.loadTexts:
    hpnicfConStatusGroup.setStatus("current")


# Notification objects

hpnicfLogIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0, 1)
)
hpnicfLogIn.setObjects(
      *(("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserName"),
        ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalSource"))
)
if mibBuilder.loadTexts:
    hpnicfLogIn.setStatus(
        "current"
    )

hpnicfLogOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0, 2)
)
hpnicfLogOut.setObjects(
      *(("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserName"),
        ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalSource"))
)
if mibBuilder.loadTexts:
    hpnicfLogOut.setStatus(
        "current"
    )

hpnicfLogInAuthenFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0, 3)
)
hpnicfLogInAuthenFailure.setObjects(
      *(("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserName"),
        ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalSource"),
        ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserAuthFailureReason"))
)
if mibBuilder.loadTexts:
    hpnicfLogInAuthenFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfUIMgtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfUIMgtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-UI-MAN-MIB",
    **{"hpnicfUIMgt": hpnicfUIMgt,
       "hpnicfUIMgtObjects": hpnicfUIMgtObjects,
       "hpnicfUIBasicInfo": hpnicfUIBasicInfo,
       "hpnicfUIScalarObjects": hpnicfUIScalarObjects,
       "hpnicfUITrapBindObjects": hpnicfUITrapBindObjects,
       "hpnicfTerminalUserName": hpnicfTerminalUserName,
       "hpnicfTerminalSource": hpnicfTerminalSource,
       "hpnicfTerminalUserAuthFailureReason": hpnicfTerminalUserAuthFailureReason,
       "hpnicfUINotifications": hpnicfUINotifications,
       "hpnicfUINotificationsPrefix": hpnicfUINotificationsPrefix,
       "hpnicfLogIn": hpnicfLogIn,
       "hpnicfLogOut": hpnicfLogOut,
       "hpnicfLogInAuthenFailure": hpnicfLogInAuthenFailure,
       "hpnicfVtyMan": hpnicfVtyMan,
       "hpnicfVtyAccTable": hpnicfVtyAccTable,
       "hpnicfVtyAccEntry": hpnicfVtyAccEntry,
       "hpnicfVtyAccUserIndex": hpnicfVtyAccUserIndex,
       "hpnicfVtyAccConnway": hpnicfVtyAccConnway,
       "hpnicfVtyAccAclNum": hpnicfVtyAccAclNum,
       "hpnicfVtyAccEntryRowStatus": hpnicfVtyAccEntryRowStatus,
       "hpnicfConStatus": hpnicfConStatus,
       "hpnicfConStatusTable": hpnicfConStatusTable,
       "hpnicfConStatusEntry": hpnicfConStatusEntry,
       "hpnicfConUserIndex": hpnicfConUserIndex,
       "hpnicfConReAuth": hpnicfConReAuth,
       "hpnicfUIMgtMIBConformance18": hpnicfUIMgtMIBConformance18,
       "hpnicfUIMgtMIBCompliances": hpnicfUIMgtMIBCompliances,
       "hpnicfUIMgtMIBCompliance": hpnicfUIMgtMIBCompliance,
       "hpnicfUIMgtManMIBGroups": hpnicfUIMgtManMIBGroups,
       "hpnicfUIMgtBasicGroup": hpnicfUIMgtBasicGroup,
       "hpnicfConStatusGroup": hpnicfConStatusGroup}
)
