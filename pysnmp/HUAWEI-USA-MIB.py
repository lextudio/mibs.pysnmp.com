# SNMP MIB module (HUAWEI-USA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-USA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:21 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwUSA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20)
)
hwUSA.setRevisions(
        ("2010-08-11 16:00",
         "2010-09-11 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwUSAObjects_ObjectIdentity = ObjectIdentity
hwUSAObjects = _HwUSAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1)
)
_HwUSAConfigTable_Object = MibTable
hwUSAConfigTable = _HwUSAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1)
)
if mibBuilder.loadTexts:
    hwUSAConfigTable.setStatus("current")
_HwUSAConfigEntry_Object = MibTableRow
hwUSAConfigEntry = _HwUSAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1)
)
hwUSAConfigEntry.setIndexNames(
    (0, "HUAWEI-USA-MIB", "hwUSAPortIndex"),
)
if mibBuilder.loadTexts:
    hwUSAConfigEntry.setStatus("current")


class _HwUSAPortIndex_Type(Integer32):
    """Custom type hwUSAPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HwUSAPortIndex_Type.__name__ = "Integer32"
_HwUSAPortIndex_Object = MibTableColumn
hwUSAPortIndex = _HwUSAPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1, 1),
    _HwUSAPortIndex_Type()
)
hwUSAPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUSAPortIndex.setStatus("current")


class _HwUSAInterfaceName_Type(DisplayString):
    """Custom type hwUSAInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwUSAInterfaceName_Type.__name__ = "DisplayString"
_HwUSAInterfaceName_Object = MibTableColumn
hwUSAInterfaceName = _HwUSAInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1, 2),
    _HwUSAInterfaceName_Type()
)
hwUSAInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUSAInterfaceName.setStatus("current")


class _HwAuthenAccessPoint_Type(EnabledStatus):
    """Custom type hwAuthenAccessPoint based on EnabledStatus"""


_HwAuthenAccessPoint_Object = MibTableColumn
hwAuthenAccessPoint = _HwAuthenAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1, 3),
    _HwAuthenAccessPoint_Type()
)
hwAuthenAccessPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthenAccessPoint.setStatus("current")
_HwAssociateUserTable_Object = MibTable
hwAssociateUserTable = _HwAssociateUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2)
)
if mibBuilder.loadTexts:
    hwAssociateUserTable.setStatus("current")
_HwAssociateUserEntry_Object = MibTableRow
hwAssociateUserEntry = _HwAssociateUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1)
)
hwAssociateUserEntry.setIndexNames(
    (0, "HUAWEI-USA-MIB", "hwAssociateUserIndex"),
)
if mibBuilder.loadTexts:
    hwAssociateUserEntry.setStatus("current")


class _HwAssociateUserIndex_Type(Integer32):
    """Custom type hwAssociateUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwAssociateUserIndex_Type.__name__ = "Integer32"
_HwAssociateUserIndex_Object = MibTableColumn
hwAssociateUserIndex = _HwAssociateUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 1),
    _HwAssociateUserIndex_Type()
)
hwAssociateUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociateUserIndex.setStatus("current")
_HwAssociateUserMac_Type = MacAddress
_HwAssociateUserMac_Object = MibTableColumn
hwAssociateUserMac = _HwAssociateUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 2),
    _HwAssociateUserMac_Type()
)
hwAssociateUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociateUserMac.setStatus("current")
_HwAssociateUserIp_Type = IpAddress
_HwAssociateUserIp_Object = MibTableColumn
hwAssociateUserIp = _HwAssociateUserIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 3),
    _HwAssociateUserIp_Type()
)
hwAssociateUserIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociateUserIp.setStatus("current")


class _HwAssociateUserStates_Type(Integer32):
    """Custom type hwAssociateUserStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("idle", 0),
          ("up", 2))
    )


_HwAssociateUserStates_Type.__name__ = "Integer32"
_HwAssociateUserStates_Object = MibTableColumn
hwAssociateUserStates = _HwAssociateUserStates_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 4),
    _HwAssociateUserStates_Type()
)
hwAssociateUserStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociateUserStates.setStatus("current")


class _HwAssociateType_Type(Integer32):
    """Custom type hwAssociateType based on Integer32"""
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
        *(("arp", 0),
          ("dhcp", 2),
          ("dot1x", 1),
          ("http", 3))
    )


_HwAssociateType_Type.__name__ = "Integer32"
_HwAssociateType_Object = MibTableColumn
hwAssociateType = _HwAssociateType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 5),
    _HwAssociateType_Type()
)
hwAssociateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociateType.setStatus("current")


class _HwUserDetectInterval_Type(Integer32):
    """Custom type hwUserDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwUserDetectInterval_Type.__name__ = "Integer32"
_HwUserDetectInterval_Object = MibScalar
hwUserDetectInterval = _HwUserDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 3),
    _HwUserDetectInterval_Type()
)
hwUserDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserDetectInterval.setStatus("current")


class _HwUserDetectRetry_Type(Integer32):
    """Custom type hwUserDetectRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwUserDetectRetry_Type.__name__ = "Integer32"
_HwUserDetectRetry_Object = MibScalar
hwUserDetectRetry = _HwUserDetectRetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 4),
    _HwUserDetectRetry_Type()
)
hwUserDetectRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserDetectRetry.setStatus("current")


class _HwUserSyncInterval_Type(Integer32):
    """Custom type hwUserSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_HwUserSyncInterval_Type.__name__ = "Integer32"
_HwUserSyncInterval_Object = MibScalar
hwUserSyncInterval = _HwUserSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 5),
    _HwUserSyncInterval_Type()
)
hwUserSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserSyncInterval.setStatus("current")


class _HwGlobalLinkDownOffline_Type(Integer32):
    """Custom type hwGlobalLinkDownOffline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwGlobalLinkDownOffline_Type.__name__ = "Integer32"
_HwGlobalLinkDownOffline_Object = MibScalar
hwGlobalLinkDownOffline = _HwGlobalLinkDownOffline_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 6),
    _HwGlobalLinkDownOffline_Type()
)
hwGlobalLinkDownOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalLinkDownOffline.setStatus("current")


class _HwGlobalControlDownOffline_Type(Integer32):
    """Custom type hwGlobalControlDownOffline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwGlobalControlDownOffline_Type.__name__ = "Integer32"
_HwGlobalControlDownOffline_Object = MibScalar
hwGlobalControlDownOffline = _HwGlobalControlDownOffline_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 7),
    _HwGlobalControlDownOffline_Type()
)
hwGlobalControlDownOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalControlDownOffline.setStatus("current")


class _HwAuthenSpeedLimitMaxNum_Type(Integer32):
    """Custom type hwAuthenSpeedLimitMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwAuthenSpeedLimitMaxNum_Type.__name__ = "Integer32"
_HwAuthenSpeedLimitMaxNum_Object = MibScalar
hwAuthenSpeedLimitMaxNum = _HwAuthenSpeedLimitMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 8),
    _HwAuthenSpeedLimitMaxNum_Type()
)
hwAuthenSpeedLimitMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthenSpeedLimitMaxNum.setStatus("current")


class _HwAuthenSpeedLimitInterval_Type(Integer32):
    """Custom type hwAuthenSpeedLimitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwAuthenSpeedLimitInterval_Type.__name__ = "Integer32"
_HwAuthenSpeedLimitInterval_Object = MibScalar
hwAuthenSpeedLimitInterval = _HwAuthenSpeedLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 9),
    _HwAuthenSpeedLimitInterval_Type()
)
hwAuthenSpeedLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthenSpeedLimitInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-USA-MIB",
    **{"hwUSA": hwUSA,
       "hwUSAObjects": hwUSAObjects,
       "hwUSAConfigTable": hwUSAConfigTable,
       "hwUSAConfigEntry": hwUSAConfigEntry,
       "hwUSAPortIndex": hwUSAPortIndex,
       "hwUSAInterfaceName": hwUSAInterfaceName,
       "hwAuthenAccessPoint": hwAuthenAccessPoint,
       "hwAssociateUserTable": hwAssociateUserTable,
       "hwAssociateUserEntry": hwAssociateUserEntry,
       "hwAssociateUserIndex": hwAssociateUserIndex,
       "hwAssociateUserMac": hwAssociateUserMac,
       "hwAssociateUserIp": hwAssociateUserIp,
       "hwAssociateUserStates": hwAssociateUserStates,
       "hwAssociateType": hwAssociateType,
       "hwUserDetectInterval": hwUserDetectInterval,
       "hwUserDetectRetry": hwUserDetectRetry,
       "hwUserSyncInterval": hwUserSyncInterval,
       "hwGlobalLinkDownOffline": hwGlobalLinkDownOffline,
       "hwGlobalControlDownOffline": hwGlobalControlDownOffline,
       "hwAuthenSpeedLimitMaxNum": hwAuthenSpeedLimitMaxNum,
       "hwAuthenSpeedLimitInterval": hwAuthenSpeedLimitInterval}
)
