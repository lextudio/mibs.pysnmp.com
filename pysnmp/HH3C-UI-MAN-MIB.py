# SNMP MIB module (HH3C-UI-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-UI-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:10 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cUIMgt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cUIMgtObjects_ObjectIdentity = ObjectIdentity
hh3cUIMgtObjects = _Hh3cUIMgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1)
)
_Hh3cUIBasicInfo_ObjectIdentity = ObjectIdentity
hh3cUIBasicInfo = _Hh3cUIBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1)
)
_Hh3cUIScalarObjects_ObjectIdentity = ObjectIdentity
hh3cUIScalarObjects = _Hh3cUIScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 1)
)
_Hh3cUITrapBindObjects_ObjectIdentity = ObjectIdentity
hh3cUITrapBindObjects = _Hh3cUITrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2)
)
_Hh3cTerminalUserName_Type = DisplayString
_Hh3cTerminalUserName_Object = MibScalar
hh3cTerminalUserName = _Hh3cTerminalUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2, 1),
    _Hh3cTerminalUserName_Type()
)
hh3cTerminalUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cTerminalUserName.setStatus("current")
_Hh3cTerminalSource_Type = DisplayString
_Hh3cTerminalSource_Object = MibScalar
hh3cTerminalSource = _Hh3cTerminalSource_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2, 2),
    _Hh3cTerminalSource_Type()
)
hh3cTerminalSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cTerminalSource.setStatus("current")


class _Hh3cTerminalUserAuthFailureReason_Type(Integer32):
    """Custom type hh3cTerminalUserAuthFailureReason based on Integer32"""
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


_Hh3cTerminalUserAuthFailureReason_Type.__name__ = "Integer32"
_Hh3cTerminalUserAuthFailureReason_Object = MibScalar
hh3cTerminalUserAuthFailureReason = _Hh3cTerminalUserAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2, 3),
    _Hh3cTerminalUserAuthFailureReason_Type()
)
hh3cTerminalUserAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cTerminalUserAuthFailureReason.setStatus("current")
_Hh3cUINotifications_ObjectIdentity = ObjectIdentity
hh3cUINotifications = _Hh3cUINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3)
)
_Hh3cUINotificationsPrefix_ObjectIdentity = ObjectIdentity
hh3cUINotificationsPrefix = _Hh3cUINotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0)
)
_Hh3cVtyMan_ObjectIdentity = ObjectIdentity
hh3cVtyMan = _Hh3cVtyMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2)
)
_Hh3cVtyAccTable_Object = MibTable
hh3cVtyAccTable = _Hh3cVtyAccTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cVtyAccTable.setStatus("current")
_Hh3cVtyAccEntry_Object = MibTableRow
hh3cVtyAccEntry = _Hh3cVtyAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1)
)
hh3cVtyAccEntry.setIndexNames(
    (0, "HH3C-UI-MAN-MIB", "hh3cVtyAccUserIndex"),
    (0, "HH3C-UI-MAN-MIB", "hh3cVtyAccConnway"),
)
if mibBuilder.loadTexts:
    hh3cVtyAccEntry.setStatus("current")


class _Hh3cVtyAccUserIndex_Type(Integer32):
    """Custom type hh3cVtyAccUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVtyAccUserIndex_Type.__name__ = "Integer32"
_Hh3cVtyAccUserIndex_Object = MibTableColumn
hh3cVtyAccUserIndex = _Hh3cVtyAccUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 1),
    _Hh3cVtyAccUserIndex_Type()
)
hh3cVtyAccUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVtyAccUserIndex.setStatus("current")


class _Hh3cVtyAccConnway_Type(Integer32):
    """Custom type hh3cVtyAccConnway based on Integer32"""
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


_Hh3cVtyAccConnway_Type.__name__ = "Integer32"
_Hh3cVtyAccConnway_Object = MibTableColumn
hh3cVtyAccConnway = _Hh3cVtyAccConnway_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 2),
    _Hh3cVtyAccConnway_Type()
)
hh3cVtyAccConnway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVtyAccConnway.setStatus("current")
_Hh3cVtyAccAclNum_Type = Integer32
_Hh3cVtyAccAclNum_Object = MibTableColumn
hh3cVtyAccAclNum = _Hh3cVtyAccAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 3),
    _Hh3cVtyAccAclNum_Type()
)
hh3cVtyAccAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVtyAccAclNum.setStatus("current")
_Hh3cVtyAccEntryRowStatus_Type = RowStatus
_Hh3cVtyAccEntryRowStatus_Object = MibTableColumn
hh3cVtyAccEntryRowStatus = _Hh3cVtyAccEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 4),
    _Hh3cVtyAccEntryRowStatus_Type()
)
hh3cVtyAccEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVtyAccEntryRowStatus.setStatus("current")
_Hh3cConStatus_ObjectIdentity = ObjectIdentity
hh3cConStatus = _Hh3cConStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3)
)
_Hh3cConStatusTable_Object = MibTable
hh3cConStatusTable = _Hh3cConStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cConStatusTable.setStatus("current")
_Hh3cConStatusEntry_Object = MibTableRow
hh3cConStatusEntry = _Hh3cConStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1, 1)
)
hh3cConStatusEntry.setIndexNames(
    (0, "HH3C-UI-MAN-MIB", "hh3cConUserIndex"),
)
if mibBuilder.loadTexts:
    hh3cConStatusEntry.setStatus("current")
_Hh3cConUserIndex_Type = Integer32
_Hh3cConUserIndex_Object = MibTableColumn
hh3cConUserIndex = _Hh3cConUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1, 1, 1),
    _Hh3cConUserIndex_Type()
)
hh3cConUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cConUserIndex.setStatus("current")


class _Hh3cConReAuth_Type(Integer32):
    """Custom type hh3cConReAuth based on Integer32"""
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


_Hh3cConReAuth_Type.__name__ = "Integer32"
_Hh3cConReAuth_Object = MibTableColumn
hh3cConReAuth = _Hh3cConReAuth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1, 1, 2),
    _Hh3cConReAuth_Type()
)
hh3cConReAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cConReAuth.setStatus("current")
_Hh3cUIMgtMIBConformance18_ObjectIdentity = ObjectIdentity
hh3cUIMgtMIBConformance18 = _Hh3cUIMgtMIBConformance18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 2)
)
_Hh3cUIMgtMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cUIMgtMIBCompliances = _Hh3cUIMgtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 1)
)
_Hh3cUIMgtManMIBGroups_ObjectIdentity = ObjectIdentity
hh3cUIMgtManMIBGroups = _Hh3cUIMgtManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 2)
)

# Managed Objects groups

hh3cUIMgtBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 2, 1)
)
hh3cUIMgtBasicGroup.setObjects(
    ("HH3C-UI-MAN-MIB", "hh3cVtyAccAclNum")
)
if mibBuilder.loadTexts:
    hh3cUIMgtBasicGroup.setStatus("current")

hh3cConStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 2, 2)
)
hh3cConStatusGroup.setObjects(
    ("HH3C-UI-MAN-MIB", "hh3cConReAuth")
)
if mibBuilder.loadTexts:
    hh3cConStatusGroup.setStatus("current")


# Notification objects

hh3cLogIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0, 1)
)
hh3cLogIn.setObjects(
      *(("HH3C-UI-MAN-MIB", "hh3cTerminalUserName"),
        ("HH3C-UI-MAN-MIB", "hh3cTerminalSource"))
)
if mibBuilder.loadTexts:
    hh3cLogIn.setStatus(
        "current"
    )

hh3cLogOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0, 2)
)
hh3cLogOut.setObjects(
      *(("HH3C-UI-MAN-MIB", "hh3cTerminalUserName"),
        ("HH3C-UI-MAN-MIB", "hh3cTerminalSource"))
)
if mibBuilder.loadTexts:
    hh3cLogOut.setStatus(
        "current"
    )

hh3cLogInAuthenFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0, 3)
)
hh3cLogInAuthenFailure.setObjects(
      *(("HH3C-UI-MAN-MIB", "hh3cTerminalUserName"),
        ("HH3C-UI-MAN-MIB", "hh3cTerminalSource"),
        ("HH3C-UI-MAN-MIB", "hh3cTerminalUserAuthFailureReason"))
)
if mibBuilder.loadTexts:
    hh3cLogInAuthenFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hh3cUIMgtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cUIMgtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-UI-MAN-MIB",
    **{"hh3cUIMgt": hh3cUIMgt,
       "hh3cUIMgtObjects": hh3cUIMgtObjects,
       "hh3cUIBasicInfo": hh3cUIBasicInfo,
       "hh3cUIScalarObjects": hh3cUIScalarObjects,
       "hh3cUITrapBindObjects": hh3cUITrapBindObjects,
       "hh3cTerminalUserName": hh3cTerminalUserName,
       "hh3cTerminalSource": hh3cTerminalSource,
       "hh3cTerminalUserAuthFailureReason": hh3cTerminalUserAuthFailureReason,
       "hh3cUINotifications": hh3cUINotifications,
       "hh3cUINotificationsPrefix": hh3cUINotificationsPrefix,
       "hh3cLogIn": hh3cLogIn,
       "hh3cLogOut": hh3cLogOut,
       "hh3cLogInAuthenFailure": hh3cLogInAuthenFailure,
       "hh3cVtyMan": hh3cVtyMan,
       "hh3cVtyAccTable": hh3cVtyAccTable,
       "hh3cVtyAccEntry": hh3cVtyAccEntry,
       "hh3cVtyAccUserIndex": hh3cVtyAccUserIndex,
       "hh3cVtyAccConnway": hh3cVtyAccConnway,
       "hh3cVtyAccAclNum": hh3cVtyAccAclNum,
       "hh3cVtyAccEntryRowStatus": hh3cVtyAccEntryRowStatus,
       "hh3cConStatus": hh3cConStatus,
       "hh3cConStatusTable": hh3cConStatusTable,
       "hh3cConStatusEntry": hh3cConStatusEntry,
       "hh3cConUserIndex": hh3cConUserIndex,
       "hh3cConReAuth": hh3cConReAuth,
       "hh3cUIMgtMIBConformance18": hh3cUIMgtMIBConformance18,
       "hh3cUIMgtMIBCompliances": hh3cUIMgtMIBCompliances,
       "hh3cUIMgtMIBCompliance": hh3cUIMgtMIBCompliance,
       "hh3cUIMgtManMIBGroups": hh3cUIMgtManMIBGroups,
       "hh3cUIMgtBasicGroup": hh3cUIMgtBasicGroup,
       "hh3cConStatusGroup": hh3cConStatusGroup}
)
