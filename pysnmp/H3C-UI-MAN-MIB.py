# SNMP MIB module (H3C-UI-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-UI-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:36 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cUIMgt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cUIMgtObjects_ObjectIdentity = ObjectIdentity
h3cUIMgtObjects = _H3cUIMgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1)
)
_H3cUIBasicInfo_ObjectIdentity = ObjectIdentity
h3cUIBasicInfo = _H3cUIBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1)
)
_H3cUIScalarObjects_ObjectIdentity = ObjectIdentity
h3cUIScalarObjects = _H3cUIScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 1)
)
_H3cUITrapBindObjects_ObjectIdentity = ObjectIdentity
h3cUITrapBindObjects = _H3cUITrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 2)
)
_H3cTerminalUserName_Type = DisplayString
_H3cTerminalUserName_Object = MibScalar
h3cTerminalUserName = _H3cTerminalUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 2, 1),
    _H3cTerminalUserName_Type()
)
h3cTerminalUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cTerminalUserName.setStatus("current")
_H3cTerminalSource_Type = DisplayString
_H3cTerminalSource_Object = MibScalar
h3cTerminalSource = _H3cTerminalSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 2, 2),
    _H3cTerminalSource_Type()
)
h3cTerminalSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cTerminalSource.setStatus("current")


class _H3cTerminalUserAuthFailureReason_Type(Integer32):
    """Custom type h3cTerminalUserAuthFailureReason based on Integer32"""
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


_H3cTerminalUserAuthFailureReason_Type.__name__ = "Integer32"
_H3cTerminalUserAuthFailureReason_Object = MibScalar
h3cTerminalUserAuthFailureReason = _H3cTerminalUserAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 2, 3),
    _H3cTerminalUserAuthFailureReason_Type()
)
h3cTerminalUserAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cTerminalUserAuthFailureReason.setStatus("current")
_H3cUINotifications_ObjectIdentity = ObjectIdentity
h3cUINotifications = _H3cUINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 3)
)
_H3cUINotificationsPrefix_ObjectIdentity = ObjectIdentity
h3cUINotificationsPrefix = _H3cUINotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 3, 0)
)
_H3cVtyMan_ObjectIdentity = ObjectIdentity
h3cVtyMan = _H3cVtyMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 2)
)
_H3cVtyAccTable_Object = MibTable
h3cVtyAccTable = _H3cVtyAccTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cVtyAccTable.setStatus("current")
_H3cVtyAccEntry_Object = MibTableRow
h3cVtyAccEntry = _H3cVtyAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 2, 1, 1)
)
h3cVtyAccEntry.setIndexNames(
    (0, "H3C-UI-MAN-MIB", "h3cVtyAccUserIndex"),
    (0, "H3C-UI-MAN-MIB", "h3cVtyAccConnway"),
)
if mibBuilder.loadTexts:
    h3cVtyAccEntry.setStatus("current")


class _H3cVtyAccUserIndex_Type(Integer32):
    """Custom type h3cVtyAccUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cVtyAccUserIndex_Type.__name__ = "Integer32"
_H3cVtyAccUserIndex_Object = MibTableColumn
h3cVtyAccUserIndex = _H3cVtyAccUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 2, 1, 1, 1),
    _H3cVtyAccUserIndex_Type()
)
h3cVtyAccUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVtyAccUserIndex.setStatus("current")


class _H3cVtyAccConnway_Type(Integer32):
    """Custom type h3cVtyAccConnway based on Integer32"""
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


_H3cVtyAccConnway_Type.__name__ = "Integer32"
_H3cVtyAccConnway_Object = MibTableColumn
h3cVtyAccConnway = _H3cVtyAccConnway_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 2, 1, 1, 2),
    _H3cVtyAccConnway_Type()
)
h3cVtyAccConnway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVtyAccConnway.setStatus("current")
_H3cVtyAccAclNum_Type = Integer32
_H3cVtyAccAclNum_Object = MibTableColumn
h3cVtyAccAclNum = _H3cVtyAccAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 2, 1, 1, 3),
    _H3cVtyAccAclNum_Type()
)
h3cVtyAccAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVtyAccAclNum.setStatus("current")
_H3cVtyAccEntryRowStatus_Type = RowStatus
_H3cVtyAccEntryRowStatus_Object = MibTableColumn
h3cVtyAccEntryRowStatus = _H3cVtyAccEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 2, 1, 1, 4),
    _H3cVtyAccEntryRowStatus_Type()
)
h3cVtyAccEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVtyAccEntryRowStatus.setStatus("current")
_H3cConStatus_ObjectIdentity = ObjectIdentity
h3cConStatus = _H3cConStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 3)
)
_H3cConStatusTable_Object = MibTable
h3cConStatusTable = _H3cConStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cConStatusTable.setStatus("current")
_H3cConStatusEntry_Object = MibTableRow
h3cConStatusEntry = _H3cConStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 3, 1, 1)
)
h3cConStatusEntry.setIndexNames(
    (0, "H3C-UI-MAN-MIB", "h3cConUserIndex"),
)
if mibBuilder.loadTexts:
    h3cConStatusEntry.setStatus("current")
_H3cConUserIndex_Type = Integer32
_H3cConUserIndex_Object = MibTableColumn
h3cConUserIndex = _H3cConUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 3, 1, 1, 1),
    _H3cConUserIndex_Type()
)
h3cConUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cConUserIndex.setStatus("current")


class _H3cConReAuth_Type(Integer32):
    """Custom type h3cConReAuth based on Integer32"""
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


_H3cConReAuth_Type.__name__ = "Integer32"
_H3cConReAuth_Object = MibTableColumn
h3cConReAuth = _H3cConReAuth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 3, 1, 1, 2),
    _H3cConReAuth_Type()
)
h3cConReAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cConReAuth.setStatus("current")
_H3cUIMgtMIBConformance18_ObjectIdentity = ObjectIdentity
h3cUIMgtMIBConformance18 = _H3cUIMgtMIBConformance18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 2)
)
_H3cUIMgtMIBCompliances_ObjectIdentity = ObjectIdentity
h3cUIMgtMIBCompliances = _H3cUIMgtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 2, 1)
)
_H3cUIMgtManMIBGroups_ObjectIdentity = ObjectIdentity
h3cUIMgtManMIBGroups = _H3cUIMgtManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 2, 2)
)

# Managed Objects groups

h3cUIMgtBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 2, 2, 1)
)
h3cUIMgtBasicGroup.setObjects(
    ("H3C-UI-MAN-MIB", "h3cVtyAccAclNum")
)
if mibBuilder.loadTexts:
    h3cUIMgtBasicGroup.setStatus("current")

h3cConStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 2, 2, 2)
)
h3cConStatusGroup.setObjects(
    ("H3C-UI-MAN-MIB", "h3cConReAuth")
)
if mibBuilder.loadTexts:
    h3cConStatusGroup.setStatus("current")


# Notification objects

h3cLogIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 3, 0, 1)
)
h3cLogIn.setObjects(
      *(("H3C-UI-MAN-MIB", "h3cTerminalUserName"),
        ("H3C-UI-MAN-MIB", "h3cTerminalSource"))
)
if mibBuilder.loadTexts:
    h3cLogIn.setStatus(
        "current"
    )

h3cLogOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 3, 0, 2)
)
h3cLogOut.setObjects(
      *(("H3C-UI-MAN-MIB", "h3cTerminalUserName"),
        ("H3C-UI-MAN-MIB", "h3cTerminalSource"))
)
if mibBuilder.loadTexts:
    h3cLogOut.setStatus(
        "current"
    )

h3cLogInAuthenFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 1, 1, 3, 0, 3)
)
h3cLogInAuthenFailure.setObjects(
      *(("H3C-UI-MAN-MIB", "h3cTerminalUserName"),
        ("H3C-UI-MAN-MIB", "h3cTerminalSource"),
        ("H3C-UI-MAN-MIB", "h3cTerminalUserAuthFailureReason"))
)
if mibBuilder.loadTexts:
    h3cLogInAuthenFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

h3cUIMgtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cUIMgtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-UI-MAN-MIB",
    **{"h3cUIMgt": h3cUIMgt,
       "h3cUIMgtObjects": h3cUIMgtObjects,
       "h3cUIBasicInfo": h3cUIBasicInfo,
       "h3cUIScalarObjects": h3cUIScalarObjects,
       "h3cUITrapBindObjects": h3cUITrapBindObjects,
       "h3cTerminalUserName": h3cTerminalUserName,
       "h3cTerminalSource": h3cTerminalSource,
       "h3cTerminalUserAuthFailureReason": h3cTerminalUserAuthFailureReason,
       "h3cUINotifications": h3cUINotifications,
       "h3cUINotificationsPrefix": h3cUINotificationsPrefix,
       "h3cLogIn": h3cLogIn,
       "h3cLogOut": h3cLogOut,
       "h3cLogInAuthenFailure": h3cLogInAuthenFailure,
       "h3cVtyMan": h3cVtyMan,
       "h3cVtyAccTable": h3cVtyAccTable,
       "h3cVtyAccEntry": h3cVtyAccEntry,
       "h3cVtyAccUserIndex": h3cVtyAccUserIndex,
       "h3cVtyAccConnway": h3cVtyAccConnway,
       "h3cVtyAccAclNum": h3cVtyAccAclNum,
       "h3cVtyAccEntryRowStatus": h3cVtyAccEntryRowStatus,
       "h3cConStatus": h3cConStatus,
       "h3cConStatusTable": h3cConStatusTable,
       "h3cConStatusEntry": h3cConStatusEntry,
       "h3cConUserIndex": h3cConUserIndex,
       "h3cConReAuth": h3cConReAuth,
       "h3cUIMgtMIBConformance18": h3cUIMgtMIBConformance18,
       "h3cUIMgtMIBCompliances": h3cUIMgtMIBCompliances,
       "h3cUIMgtMIBCompliance": h3cUIMgtMIBCompliance,
       "h3cUIMgtManMIBGroups": h3cUIMgtManMIBGroups,
       "h3cUIMgtBasicGroup": h3cUIMgtBasicGroup,
       "h3cConStatusGroup": h3cConStatusGroup}
)
