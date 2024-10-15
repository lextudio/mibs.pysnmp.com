# SNMP MIB module (ZYXEL-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:17 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelAaa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelAaaSetup_ObjectIdentity = ObjectIdentity
zyxelAaaSetup = _ZyxelAaaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1)
)
_ZyxelAaaAuthenticationSetup_ObjectIdentity = ObjectIdentity
zyxelAaaAuthenticationSetup = _ZyxelAaaAuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1)
)
_ZyxelAaaAuthenticationTypeTable_Object = MibTable
zyxelAaaAuthenticationTypeTable = _ZyxelAaaAuthenticationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelAaaAuthenticationTypeTable.setStatus("current")
_ZyxelAaaAuthenticationTypeEntry_Object = MibTableRow
zyxelAaaAuthenticationTypeEntry = _ZyxelAaaAuthenticationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1, 1)
)
zyxelAaaAuthenticationTypeEntry.setIndexNames(
    (0, "ZYXEL-AAA-MIB", "zyAaaAuthenticationTypeName"),
)
if mibBuilder.loadTexts:
    zyxelAaaAuthenticationTypeEntry.setStatus("current")
_ZyAaaAuthenticationTypeName_Type = DisplayString
_ZyAaaAuthenticationTypeName_Object = MibTableColumn
zyAaaAuthenticationTypeName = _ZyAaaAuthenticationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1, 1, 1),
    _ZyAaaAuthenticationTypeName_Type()
)
zyAaaAuthenticationTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAaaAuthenticationTypeName.setStatus("current")
_ZyAaaAuthenticationTypeMethodList_Type = OctetString
_ZyAaaAuthenticationTypeMethodList_Object = MibTableColumn
zyAaaAuthenticationTypeMethodList = _ZyAaaAuthenticationTypeMethodList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1, 1, 2),
    _ZyAaaAuthenticationTypeMethodList_Type()
)
zyAaaAuthenticationTypeMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAuthenticationTypeMethodList.setStatus("current")
_ZyxelAaaAuthorizationSetup_ObjectIdentity = ObjectIdentity
zyxelAaaAuthorizationSetup = _ZyxelAaaAuthorizationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2)
)
_ZyAaaAuthorizationConsoleState_Type = EnabledStatus
_ZyAaaAuthorizationConsoleState_Object = MibScalar
zyAaaAuthorizationConsoleState = _ZyAaaAuthorizationConsoleState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 1),
    _ZyAaaAuthorizationConsoleState_Type()
)
zyAaaAuthorizationConsoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAuthorizationConsoleState.setStatus("current")
_ZyxelAaaAuthorizationTypeTable_Object = MibTable
zyxelAaaAuthorizationTypeTable = _ZyxelAaaAuthorizationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelAaaAuthorizationTypeTable.setStatus("current")
_ZyxelAaaAuthorizationTypeEntry_Object = MibTableRow
zyxelAaaAuthorizationTypeEntry = _ZyxelAaaAuthorizationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1)
)
zyxelAaaAuthorizationTypeEntry.setIndexNames(
    (0, "ZYXEL-AAA-MIB", "zyAaaAuthorizationTypeName"),
)
if mibBuilder.loadTexts:
    zyxelAaaAuthorizationTypeEntry.setStatus("current")
_ZyAaaAuthorizationTypeName_Type = DisplayString
_ZyAaaAuthorizationTypeName_Object = MibTableColumn
zyAaaAuthorizationTypeName = _ZyAaaAuthorizationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1, 1),
    _ZyAaaAuthorizationTypeName_Type()
)
zyAaaAuthorizationTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAaaAuthorizationTypeName.setStatus("current")
_ZyAaaAuthorizationTypeState_Type = EnabledStatus
_ZyAaaAuthorizationTypeState_Object = MibTableColumn
zyAaaAuthorizationTypeState = _ZyAaaAuthorizationTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1, 2),
    _ZyAaaAuthorizationTypeState_Type()
)
zyAaaAuthorizationTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAuthorizationTypeState.setStatus("current")


class _ZyAaaAuthorizationTypeMethod_Type(Integer32):
    """Custom type zyAaaAuthorizationTypeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_ZyAaaAuthorizationTypeMethod_Type.__name__ = "Integer32"
_ZyAaaAuthorizationTypeMethod_Object = MibTableColumn
zyAaaAuthorizationTypeMethod = _ZyAaaAuthorizationTypeMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1, 3),
    _ZyAaaAuthorizationTypeMethod_Type()
)
zyAaaAuthorizationTypeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAuthorizationTypeMethod.setStatus("current")
_ZyxelAaaAccountingSetup_ObjectIdentity = ObjectIdentity
zyxelAaaAccountingSetup = _ZyxelAaaAccountingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3)
)
_ZyAaaAccountingUpdatePeriod_Type = Integer32
_ZyAaaAccountingUpdatePeriod_Object = MibScalar
zyAaaAccountingUpdatePeriod = _ZyAaaAccountingUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 1),
    _ZyAaaAccountingUpdatePeriod_Type()
)
zyAaaAccountingUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAccountingUpdatePeriod.setStatus("current")
_ZyxelAaaAccountingTypeTable_Object = MibTable
zyxelAaaAccountingTypeTable = _ZyxelAaaAccountingTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zyxelAaaAccountingTypeTable.setStatus("current")
_ZyxelAaaAccountingTypeEntry_Object = MibTableRow
zyxelAaaAccountingTypeEntry = _ZyxelAaaAccountingTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1)
)
zyxelAaaAccountingTypeEntry.setIndexNames(
    (0, "ZYXEL-AAA-MIB", "zyAaaAccountingTypeName"),
)
if mibBuilder.loadTexts:
    zyxelAaaAccountingTypeEntry.setStatus("current")
_ZyAaaAccountingTypeName_Type = DisplayString
_ZyAaaAccountingTypeName_Object = MibTableColumn
zyAaaAccountingTypeName = _ZyAaaAccountingTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 1),
    _ZyAaaAccountingTypeName_Type()
)
zyAaaAccountingTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAaaAccountingTypeName.setStatus("current")
_ZyAaaAccountingTypeState_Type = EnabledStatus
_ZyAaaAccountingTypeState_Object = MibTableColumn
zyAaaAccountingTypeState = _ZyAaaAccountingTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 2),
    _ZyAaaAccountingTypeState_Type()
)
zyAaaAccountingTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAccountingTypeState.setStatus("current")
_ZyAaaAccountingTypeBroadcastState_Type = EnabledStatus
_ZyAaaAccountingTypeBroadcastState_Object = MibTableColumn
zyAaaAccountingTypeBroadcastState = _ZyAaaAccountingTypeBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 3),
    _ZyAaaAccountingTypeBroadcastState_Type()
)
zyAaaAccountingTypeBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAccountingTypeBroadcastState.setStatus("current")


class _ZyAaaAccountingTypeMode_Type(Integer32):
    """Custom type zyAaaAccountingTypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 255),
          ("startStop", 1),
          ("stopOnly", 2))
    )


_ZyAaaAccountingTypeMode_Type.__name__ = "Integer32"
_ZyAaaAccountingTypeMode_Object = MibTableColumn
zyAaaAccountingTypeMode = _ZyAaaAccountingTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 4),
    _ZyAaaAccountingTypeMode_Type()
)
zyAaaAccountingTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAccountingTypeMode.setStatus("current")


class _ZyAaaAccountingTypeMethod_Type(Integer32):
    """Custom type zyAaaAccountingTypeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_ZyAaaAccountingTypeMethod_Type.__name__ = "Integer32"
_ZyAaaAccountingTypeMethod_Object = MibTableColumn
zyAaaAccountingTypeMethod = _ZyAaaAccountingTypeMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 5),
    _ZyAaaAccountingTypeMethod_Type()
)
zyAaaAccountingTypeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAccountingTypeMethod.setStatus("current")


class _ZyAaaAccountingTypePrivilege_Type(Integer32):
    """Custom type zyAaaAccountingTypePrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 255),
          ("privilege0", 0),
          ("privilege1", 1),
          ("privilege10", 10),
          ("privilege11", 11),
          ("privilege12", 12),
          ("privilege13", 13),
          ("privilege14", 14),
          ("privilege2", 2),
          ("privilege3", 3),
          ("privilege4", 4),
          ("privilege5", 5),
          ("privilege6", 6),
          ("privilege7", 7),
          ("privilege8", 8),
          ("privilege9", 9))
    )


_ZyAaaAccountingTypePrivilege_Type.__name__ = "Integer32"
_ZyAaaAccountingTypePrivilege_Object = MibTableColumn
zyAaaAccountingTypePrivilege = _ZyAaaAccountingTypePrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 6),
    _ZyAaaAccountingTypePrivilege_Type()
)
zyAaaAccountingTypePrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyAaaAccountingTypePrivilege.setStatus("current")
_ZyxelAaaTrapInfoObjects_ObjectIdentity = ObjectIdentity
zyxelAaaTrapInfoObjects = _ZyxelAaaTrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 2)
)


class _ZyAaaTrapAuthenticationMethod_Type(Integer32):
    """Custom type zyAaaTrapAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("console", 2),
          ("ftp", 1),
          ("http", 5),
          ("https", 4),
          ("snmp", 0),
          ("ssh", 3),
          ("telnet", 6))
    )


_ZyAaaTrapAuthenticationMethod_Type.__name__ = "Integer32"
_ZyAaaTrapAuthenticationMethod_Object = MibScalar
zyAaaTrapAuthenticationMethod = _ZyAaaTrapAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 2, 1),
    _ZyAaaTrapAuthenticationMethod_Type()
)
zyAaaTrapAuthenticationMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAaaTrapAuthenticationMethod.setStatus("current")


class _ZyAaaTrapAuthorizationMethod_Type(Integer32):
    """Custom type zyAaaTrapAuthorizationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("console", 5),
          ("dot1x", 0),
          ("ftp", 4),
          ("http", 2),
          ("ssh", 1),
          ("telnet", 3))
    )


_ZyAaaTrapAuthorizationMethod_Type.__name__ = "Integer32"
_ZyAaaTrapAuthorizationMethod_Object = MibScalar
zyAaaTrapAuthorizationMethod = _ZyAaaTrapAuthorizationMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 2, 2),
    _ZyAaaTrapAuthorizationMethod_Type()
)
zyAaaTrapAuthorizationMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAaaTrapAuthorizationMethod.setStatus("current")
_ZyxelAaaNotifications_ObjectIdentity = ObjectIdentity
zyxelAaaNotifications = _ZyxelAaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 3)
)

# Managed Objects groups


# Notification objects

zyAaaAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 3, 1)
)
zyAaaAuthenticationFailure.setObjects(
    ("ZYXEL-AAA-MIB", "zyAaaTrapAuthenticationMethod")
)
if mibBuilder.loadTexts:
    zyAaaAuthenticationFailure.setStatus(
        "current"
    )

zyAaaAuthorizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 3, 2)
)
zyAaaAuthorizationFailure.setObjects(
    ("ZYXEL-AAA-MIB", "zyAaaTrapAuthorizationMethod")
)
if mibBuilder.loadTexts:
    zyAaaAuthorizationFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-AAA-MIB",
    **{"zyxelAaa": zyxelAaa,
       "zyxelAaaSetup": zyxelAaaSetup,
       "zyxelAaaAuthenticationSetup": zyxelAaaAuthenticationSetup,
       "zyxelAaaAuthenticationTypeTable": zyxelAaaAuthenticationTypeTable,
       "zyxelAaaAuthenticationTypeEntry": zyxelAaaAuthenticationTypeEntry,
       "zyAaaAuthenticationTypeName": zyAaaAuthenticationTypeName,
       "zyAaaAuthenticationTypeMethodList": zyAaaAuthenticationTypeMethodList,
       "zyxelAaaAuthorizationSetup": zyxelAaaAuthorizationSetup,
       "zyAaaAuthorizationConsoleState": zyAaaAuthorizationConsoleState,
       "zyxelAaaAuthorizationTypeTable": zyxelAaaAuthorizationTypeTable,
       "zyxelAaaAuthorizationTypeEntry": zyxelAaaAuthorizationTypeEntry,
       "zyAaaAuthorizationTypeName": zyAaaAuthorizationTypeName,
       "zyAaaAuthorizationTypeState": zyAaaAuthorizationTypeState,
       "zyAaaAuthorizationTypeMethod": zyAaaAuthorizationTypeMethod,
       "zyxelAaaAccountingSetup": zyxelAaaAccountingSetup,
       "zyAaaAccountingUpdatePeriod": zyAaaAccountingUpdatePeriod,
       "zyxelAaaAccountingTypeTable": zyxelAaaAccountingTypeTable,
       "zyxelAaaAccountingTypeEntry": zyxelAaaAccountingTypeEntry,
       "zyAaaAccountingTypeName": zyAaaAccountingTypeName,
       "zyAaaAccountingTypeState": zyAaaAccountingTypeState,
       "zyAaaAccountingTypeBroadcastState": zyAaaAccountingTypeBroadcastState,
       "zyAaaAccountingTypeMode": zyAaaAccountingTypeMode,
       "zyAaaAccountingTypeMethod": zyAaaAccountingTypeMethod,
       "zyAaaAccountingTypePrivilege": zyAaaAccountingTypePrivilege,
       "zyxelAaaTrapInfoObjects": zyxelAaaTrapInfoObjects,
       "zyAaaTrapAuthenticationMethod": zyAaaTrapAuthenticationMethod,
       "zyAaaTrapAuthorizationMethod": zyAaaTrapAuthorizationMethod,
       "zyxelAaaNotifications": zyxelAaaNotifications,
       "zyAaaAuthenticationFailure": zyAaaAuthenticationFailure,
       "zyAaaAuthorizationFailure": zyAaaAuthorizationFailure}
)
