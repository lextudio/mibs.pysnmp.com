# SNMP MIB module (HUAWEI-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:33 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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

hwLineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLineObjects_ObjectIdentity = ObjectIdentity
hwLineObjects = _HwLineObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1)
)
_HwTelnetSet_ObjectIdentity = ObjectIdentity
hwTelnetSet = _HwTelnetSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 1)
)


class _HwMaxVtyNumber_Type(Integer32):
    """Custom type hwMaxVtyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwMaxVtyNumber_Type.__name__ = "Integer32"
_HwMaxVtyNumber_Object = MibScalar
hwMaxVtyNumber = _HwMaxVtyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 1, 1),
    _HwMaxVtyNumber_Type()
)
hwMaxVtyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMaxVtyNumber.setStatus("current")
_HwLoginUserInfo_ObjectIdentity = ObjectIdentity
hwLoginUserInfo = _HwLoginUserInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 2)
)
_HwLoginUserInfoTable_Object = MibTable
hwLoginUserInfoTable = _HwLoginUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwLoginUserInfoTable.setStatus("current")
_HwLoginUserInfoEntry_Object = MibTableRow
hwLoginUserInfoEntry = _HwLoginUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 2, 1, 1)
)
hwLoginUserInfoEntry.setIndexNames(
    (0, "HUAWEI-LINE-MIB", "hwUserInfoIndex"),
)
if mibBuilder.loadTexts:
    hwLoginUserInfoEntry.setStatus("current")


class _HwUserInfoIndex_Type(Integer32):
    """Custom type hwUserInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwUserInfoIndex_Type.__name__ = "Integer32"
_HwUserInfoIndex_Object = MibTableColumn
hwUserInfoIndex = _HwUserInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 2, 1, 1, 1),
    _HwUserInfoIndex_Type()
)
hwUserInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwUserInfoIndex.setStatus("current")


class _HwUserInfoName_Type(OctetString):
    """Custom type hwUserInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwUserInfoName_Type.__name__ = "OctetString"
_HwUserInfoName_Object = MibTableColumn
hwUserInfoName = _HwUserInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 2, 1, 1, 2),
    _HwUserInfoName_Type()
)
hwUserInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserInfoName.setStatus("current")


class _HwUserInfoIpAddr_Type(OctetString):
    """Custom type hwUserInfoIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwUserInfoIpAddr_Type.__name__ = "OctetString"
_HwUserInfoIpAddr_Object = MibTableColumn
hwUserInfoIpAddr = _HwUserInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 2, 1, 1, 3),
    _HwUserInfoIpAddr_Type()
)
hwUserInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserInfoIpAddr.setStatus("current")


class _HwUserInfoChannel_Type(OctetString):
    """Custom type hwUserInfoChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwUserInfoChannel_Type.__name__ = "OctetString"
_HwUserInfoChannel_Object = MibTableColumn
hwUserInfoChannel = _HwUserInfoChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 2, 1, 1, 4),
    _HwUserInfoChannel_Type()
)
hwUserInfoChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserInfoChannel.setStatus("current")
_HwUserInterface_ObjectIdentity = ObjectIdentity
hwUserInterface = _HwUserInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3)
)
_HwUserInterfaceTable_Object = MibTable
hwUserInterfaceTable = _HwUserInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwUserInterfaceTable.setStatus("current")
_HwUserInterfaceEntry_Object = MibTableRow
hwUserInterfaceEntry = _HwUserInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3, 1, 1)
)
hwUserInterfaceEntry.setIndexNames(
    (0, "HUAWEI-LINE-MIB", "hwInterfaceType"),
    (0, "HUAWEI-LINE-MIB", "hwUserInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwUserInterfaceEntry.setStatus("current")


class _HwInterfaceType_Type(Integer32):
    """Custom type hwInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vty", 1)
    )


_HwInterfaceType_Type.__name__ = "Integer32"
_HwInterfaceType_Object = MibTableColumn
hwInterfaceType = _HwInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3, 1, 1, 1),
    _HwInterfaceType_Type()
)
hwInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwInterfaceType.setStatus("current")


class _HwUserInterfaceIndex_Type(Integer32):
    """Custom type hwUserInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwUserInterfaceIndex_Type.__name__ = "Integer32"
_HwUserInterfaceIndex_Object = MibTableColumn
hwUserInterfaceIndex = _HwUserInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3, 1, 1, 2),
    _HwUserInterfaceIndex_Type()
)
hwUserInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwUserInterfaceIndex.setStatus("current")


class _HwAuthenticationMode_Type(Integer32):
    """Custom type hwAuthenticationMode based on Integer32"""
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
        *(("aaa", 3),
          ("none", 1),
          ("password", 2),
          ("undefined", 0))
    )


_HwAuthenticationMode_Type.__name__ = "Integer32"
_HwAuthenticationMode_Object = MibTableColumn
hwAuthenticationMode = _HwAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3, 1, 1, 3),
    _HwAuthenticationMode_Type()
)
hwAuthenticationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthenticationMode.setStatus("current")


class _HwProtocol_Type(Integer32):
    """Custom type hwProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("ssh", 2),
          ("telnet", 1))
    )


_HwProtocol_Type.__name__ = "Integer32"
_HwProtocol_Object = MibTableColumn
hwProtocol = _HwProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3, 1, 1, 4),
    _HwProtocol_Type()
)
hwProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwProtocol.setStatus("current")
_HwUserInterfaceRowStatus_Type = RowStatus
_HwUserInterfaceRowStatus_Object = MibTableColumn
hwUserInterfaceRowStatus = _HwUserInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 1, 3, 1, 1, 5),
    _HwUserInterfaceRowStatus_Type()
)
hwUserInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUserInterfaceRowStatus.setStatus("current")
_HwLineNotification_ObjectIdentity = ObjectIdentity
hwLineNotification = _HwLineNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 2)
)
_HwLineConformance_ObjectIdentity = ObjectIdentity
hwLineConformance = _HwLineConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 3)
)
_HwLineCompliances_ObjectIdentity = ObjectIdentity
hwLineCompliances = _HwLineCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 3, 1)
)
_HwLineGroups_ObjectIdentity = ObjectIdentity
hwLineGroups = _HwLineGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 3, 2)
)

# Managed Objects groups

hwLineUserInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 3, 2, 2)
)
hwLineUserInfoGroup.setObjects(
      *(("HUAWEI-LINE-MIB", "hwUserInfoIndex"),
        ("HUAWEI-LINE-MIB", "hwUserInfoName"),
        ("HUAWEI-LINE-MIB", "hwUserInfoIpAddr"),
        ("HUAWEI-LINE-MIB", "hwUserInfoChannel"))
)
if mibBuilder.loadTexts:
    hwLineUserInfoGroup.setStatus("current")

hwMaxVtyNumberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 3, 2, 3)
)
hwMaxVtyNumberGroup.setObjects(
    ("HUAWEI-LINE-MIB", "hwMaxVtyNumber")
)
if mibBuilder.loadTexts:
    hwMaxVtyNumberGroup.setStatus("current")


# Notification objects

hwVtyNumExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 2, 1)
)
hwVtyNumExceed.setObjects(
    ("HUAWEI-LINE-MIB", "hwMaxVtyNumber")
)
if mibBuilder.loadTexts:
    hwVtyNumExceed.setStatus(
        "current"
    )

hwUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 2, 2)
)
hwUserLogin.setObjects(
      *(("HUAWEI-LINE-MIB", "hwUserInfoName"),
        ("HUAWEI-LINE-MIB", "hwUserInfoIpAddr"),
        ("HUAWEI-LINE-MIB", "hwUserInfoChannel"))
)
if mibBuilder.loadTexts:
    hwUserLogin.setStatus(
        "current"
    )

hwUserLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 2, 3)
)
hwUserLoginFail.setObjects(
      *(("HUAWEI-LINE-MIB", "hwUserInfoName"),
        ("HUAWEI-LINE-MIB", "hwUserInfoIpAddr"),
        ("HUAWEI-LINE-MIB", "hwUserInfoChannel"))
)
if mibBuilder.loadTexts:
    hwUserLoginFail.setStatus(
        "current"
    )

hwUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 2, 4)
)
hwUserLogout.setObjects(
      *(("HUAWEI-LINE-MIB", "hwUserInfoName"),
        ("HUAWEI-LINE-MIB", "hwUserInfoIpAddr"),
        ("HUAWEI-LINE-MIB", "hwUserInfoChannel"))
)
if mibBuilder.loadTexts:
    hwUserLogout.setStatus(
        "current"
    )


# Notifications groups

hwLineNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 3, 2, 1)
)
hwLineNotificationGroup.setObjects(
      *(("HUAWEI-LINE-MIB", "hwVtyNumExceed"),
        ("HUAWEI-LINE-MIB", "hwUserLogin"))
)
if mibBuilder.loadTexts:
    hwLineNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwLineCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 207, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwLineCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LINE-MIB",
    **{"hwLineMIB": hwLineMIB,
       "hwLineObjects": hwLineObjects,
       "hwTelnetSet": hwTelnetSet,
       "hwMaxVtyNumber": hwMaxVtyNumber,
       "hwLoginUserInfo": hwLoginUserInfo,
       "hwLoginUserInfoTable": hwLoginUserInfoTable,
       "hwLoginUserInfoEntry": hwLoginUserInfoEntry,
       "hwUserInfoIndex": hwUserInfoIndex,
       "hwUserInfoName": hwUserInfoName,
       "hwUserInfoIpAddr": hwUserInfoIpAddr,
       "hwUserInfoChannel": hwUserInfoChannel,
       "hwUserInterface": hwUserInterface,
       "hwUserInterfaceTable": hwUserInterfaceTable,
       "hwUserInterfaceEntry": hwUserInterfaceEntry,
       "hwInterfaceType": hwInterfaceType,
       "hwUserInterfaceIndex": hwUserInterfaceIndex,
       "hwAuthenticationMode": hwAuthenticationMode,
       "hwProtocol": hwProtocol,
       "hwUserInterfaceRowStatus": hwUserInterfaceRowStatus,
       "hwLineNotification": hwLineNotification,
       "hwVtyNumExceed": hwVtyNumExceed,
       "hwUserLogin": hwUserLogin,
       "hwUserLoginFail": hwUserLoginFail,
       "hwUserLogout": hwUserLogout,
       "hwLineConformance": hwLineConformance,
       "hwLineCompliances": hwLineCompliances,
       "hwLineCompliance": hwLineCompliance,
       "hwLineGroups": hwLineGroups,
       "hwLineNotificationGroup": hwLineNotificationGroup,
       "hwLineUserInfoGroup": hwLineUserInfoGroup,
       "hwMaxVtyNumberGroup": hwMaxVtyNumberGroup}
)
