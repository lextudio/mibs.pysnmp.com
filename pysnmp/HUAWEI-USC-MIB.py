# SNMP MIB module (HUAWEI-USC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-USC-MIB
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

hwUSC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19)
)
hwUSC.setRevisions(
        ("2014-07-11 16:00",
         "2010-08-11 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwUSCObjects_ObjectIdentity = ObjectIdentity
hwUSCObjects = _HwUSCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1)
)
_HwUSCConfigTable_Object = MibTable
hwUSCConfigTable = _HwUSCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1)
)
if mibBuilder.loadTexts:
    hwUSCConfigTable.setStatus("current")
_HwUSCConfigEntry_Object = MibTableRow
hwUSCConfigEntry = _HwUSCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1)
)
hwUSCConfigEntry.setIndexNames(
    (0, "HUAWEI-USC-MIB", "hwUSCPortIndex"),
)
if mibBuilder.loadTexts:
    hwUSCConfigEntry.setStatus("current")


class _HwUSCPortIndex_Type(Integer32):
    """Custom type hwUSCPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwUSCPortIndex_Type.__name__ = "Integer32"
_HwUSCPortIndex_Object = MibTableColumn
hwUSCPortIndex = _HwUSCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 1),
    _HwUSCPortIndex_Type()
)
hwUSCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUSCPortIndex.setStatus("current")


class _HwUSCInterfaceName_Type(DisplayString):
    """Custom type hwUSCInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwUSCInterfaceName_Type.__name__ = "DisplayString"
_HwUSCInterfaceName_Object = MibTableColumn
hwUSCInterfaceName = _HwUSCInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 2),
    _HwUSCInterfaceName_Type()
)
hwUSCInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUSCInterfaceName.setStatus("current")


class _HwAuthenControlPoint_Type(Integer32):
    """Custom type hwAuthenControlPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_HwAuthenControlPoint_Type.__name__ = "Integer32"
_HwAuthenControlPoint_Object = MibTableColumn
hwAuthenControlPoint = _HwAuthenControlPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 3),
    _HwAuthenControlPoint_Type()
)
hwAuthenControlPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthenControlPoint.setStatus("current")


class _HwUSCLinkDownOffline_Type(Integer32):
    """Custom type hwUSCLinkDownOffline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwUSCLinkDownOffline_Type.__name__ = "Integer32"
_HwUSCLinkDownOffline_Object = MibTableColumn
hwUSCLinkDownOffline = _HwUSCLinkDownOffline_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 4),
    _HwUSCLinkDownOffline_Type()
)
hwUSCLinkDownOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUSCLinkDownOffline.setStatus("current")


class _HwUSCControlDownOffline_Type(Integer32):
    """Custom type hwUSCControlDownOffline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwUSCControlDownOffline_Type.__name__ = "Integer32"
_HwUSCControlDownOffline_Object = MibTableColumn
hwUSCControlDownOffline = _HwUSCControlDownOffline_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 5),
    _HwUSCControlDownOffline_Type()
)
hwUSCControlDownOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUSCControlDownOffline.setStatus("current")


class _HwUSCUserSyncInterval_Type(Integer32):
    """Custom type hwUSCUserSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_HwUSCUserSyncInterval_Type.__name__ = "Integer32"
_HwUSCUserSyncInterval_Object = MibTableColumn
hwUSCUserSyncInterval = _HwUSCUserSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 6),
    _HwUSCUserSyncInterval_Type()
)
hwUSCUserSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUSCUserSyncInterval.setStatus("current")


class _HwUSCUserSyncRetry_Type(Integer32):
    """Custom type hwUSCUserSyncRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HwUSCUserSyncRetry_Type.__name__ = "Integer32"
_HwUSCUserSyncRetry_Object = MibTableColumn
hwUSCUserSyncRetry = _HwUSCUserSyncRetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 7),
    _HwUSCUserSyncRetry_Type()
)
hwUSCUserSyncRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUSCUserSyncRetry.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-USC-MIB",
    **{"hwUSC": hwUSC,
       "hwUSCObjects": hwUSCObjects,
       "hwUSCConfigTable": hwUSCConfigTable,
       "hwUSCConfigEntry": hwUSCConfigEntry,
       "hwUSCPortIndex": hwUSCPortIndex,
       "hwUSCInterfaceName": hwUSCInterfaceName,
       "hwAuthenControlPoint": hwAuthenControlPoint,
       "hwUSCLinkDownOffline": hwUSCLinkDownOffline,
       "hwUSCControlDownOffline": hwUSCControlDownOffline,
       "hwUSCUserSyncInterval": hwUSCUserSyncInterval,
       "hwUSCUserSyncRetry": hwUSCUserSyncRetry}
)
