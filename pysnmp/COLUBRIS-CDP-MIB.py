# SNMP MIB module (COLUBRIS-CDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-CDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:12 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubrisCdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisCdpMIBObjects_ObjectIdentity = ObjectIdentity
colubrisCdpMIBObjects = _ColubrisCdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1)
)
_CoCdpCache_ObjectIdentity = ObjectIdentity
coCdpCache = _CoCdpCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1)
)
_CoCdpCacheTable_Object = MibTable
coCdpCacheTable = _CoCdpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coCdpCacheTable.setStatus("current")
_CoCdpCacheEntry_Object = MibTableRow
coCdpCacheEntry = _CoCdpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1)
)
coCdpCacheEntry.setIndexNames(
    (0, "COLUBRIS-CDP-MIB", "coCdpCacheDeviceIndex"),
)
if mibBuilder.loadTexts:
    coCdpCacheEntry.setStatus("current")


class _CoCdpCacheDeviceIndex_Type(Integer32):
    """Custom type coCdpCacheDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoCdpCacheDeviceIndex_Type.__name__ = "Integer32"
_CoCdpCacheDeviceIndex_Object = MibTableColumn
coCdpCacheDeviceIndex = _CoCdpCacheDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 1),
    _CoCdpCacheDeviceIndex_Type()
)
coCdpCacheDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coCdpCacheDeviceIndex.setStatus("current")
_CoCdpCacheLocalInterface_Type = DisplayString
_CoCdpCacheLocalInterface_Object = MibTableColumn
coCdpCacheLocalInterface = _CoCdpCacheLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 2),
    _CoCdpCacheLocalInterface_Type()
)
coCdpCacheLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCacheLocalInterface.setStatus("current")
_CoCdpCacheAddress_Type = IpAddress
_CoCdpCacheAddress_Object = MibTableColumn
coCdpCacheAddress = _CoCdpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 3),
    _CoCdpCacheAddress_Type()
)
coCdpCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCacheAddress.setStatus("current")
_CoCdpCacheDeviceId_Type = DisplayString
_CoCdpCacheDeviceId_Object = MibTableColumn
coCdpCacheDeviceId = _CoCdpCacheDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 4),
    _CoCdpCacheDeviceId_Type()
)
coCdpCacheDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCacheDeviceId.setStatus("current")
_CoCdpCacheTimeToLive_Type = Unsigned32
_CoCdpCacheTimeToLive_Object = MibTableColumn
coCdpCacheTimeToLive = _CoCdpCacheTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 5),
    _CoCdpCacheTimeToLive_Type()
)
coCdpCacheTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCacheTimeToLive.setStatus("current")
_CoCdpCacheCapabilities_Type = DisplayString
_CoCdpCacheCapabilities_Object = MibTableColumn
coCdpCacheCapabilities = _CoCdpCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 6),
    _CoCdpCacheCapabilities_Type()
)
coCdpCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCacheCapabilities.setStatus("current")
_CoCdpCacheVersion_Type = DisplayString
_CoCdpCacheVersion_Object = MibTableColumn
coCdpCacheVersion = _CoCdpCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 7),
    _CoCdpCacheVersion_Type()
)
coCdpCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCacheVersion.setStatus("current")
_CoCdpCachePlatform_Type = DisplayString
_CoCdpCachePlatform_Object = MibTableColumn
coCdpCachePlatform = _CoCdpCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 8),
    _CoCdpCachePlatform_Type()
)
coCdpCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCachePlatform.setStatus("current")
_CoCdpCachePortId_Type = DisplayString
_CoCdpCachePortId_Object = MibTableColumn
coCdpCachePortId = _CoCdpCachePortId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 9),
    _CoCdpCachePortId_Type()
)
coCdpCachePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdpCachePortId.setStatus("current")
_CoCdpGlobal_ObjectIdentity = ObjectIdentity
coCdpGlobal = _CoCdpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2)
)


class _CoCdpGlobalMessageInterval_Type(Integer32):
    """Custom type coCdpGlobalMessageInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_CoCdpGlobalMessageInterval_Type.__name__ = "Integer32"
_CoCdpGlobalMessageInterval_Object = MibScalar
coCdpGlobalMessageInterval = _CoCdpGlobalMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2, 1),
    _CoCdpGlobalMessageInterval_Type()
)
coCdpGlobalMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdpGlobalMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    coCdpGlobalMessageInterval.setUnits("seconds")


class _CoCdpGlobalHoldTime_Type(Integer32):
    """Custom type coCdpGlobalHoldTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_CoCdpGlobalHoldTime_Type.__name__ = "Integer32"
_CoCdpGlobalHoldTime_Object = MibScalar
coCdpGlobalHoldTime = _CoCdpGlobalHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2, 2),
    _CoCdpGlobalHoldTime_Type()
)
coCdpGlobalHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdpGlobalHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    coCdpGlobalHoldTime.setUnits("seconds")
_ColubrisCdpMIBConformance_ObjectIdentity = ObjectIdentity
colubrisCdpMIBConformance = _ColubrisCdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 2)
)
_ColubrisCdpMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisCdpMIBCompliances = _ColubrisCdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 1)
)
_ColubrisCdpMIBGroups_ObjectIdentity = ObjectIdentity
colubrisCdpMIBGroups = _ColubrisCdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 2)
)

# Managed Objects groups

colubrisCdpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 2, 1)
)
colubrisCdpMIBGroup.setObjects(
      *(("COLUBRIS-CDP-MIB", "coCdpCacheLocalInterface"),
        ("COLUBRIS-CDP-MIB", "coCdpCacheAddress"),
        ("COLUBRIS-CDP-MIB", "coCdpCacheDeviceId"),
        ("COLUBRIS-CDP-MIB", "coCdpCacheTimeToLive"),
        ("COLUBRIS-CDP-MIB", "coCdpCacheCapabilities"),
        ("COLUBRIS-CDP-MIB", "coCdpCacheVersion"),
        ("COLUBRIS-CDP-MIB", "coCdpCachePlatform"),
        ("COLUBRIS-CDP-MIB", "coCdpCachePortId"),
        ("COLUBRIS-CDP-MIB", "coCdpGlobalMessageInterval"),
        ("COLUBRIS-CDP-MIB", "coCdpGlobalHoldTime"))
)
if mibBuilder.loadTexts:
    colubrisCdpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisCdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisCdpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-CDP-MIB",
    **{"colubrisCdpMIB": colubrisCdpMIB,
       "colubrisCdpMIBObjects": colubrisCdpMIBObjects,
       "coCdpCache": coCdpCache,
       "coCdpCacheTable": coCdpCacheTable,
       "coCdpCacheEntry": coCdpCacheEntry,
       "coCdpCacheDeviceIndex": coCdpCacheDeviceIndex,
       "coCdpCacheLocalInterface": coCdpCacheLocalInterface,
       "coCdpCacheAddress": coCdpCacheAddress,
       "coCdpCacheDeviceId": coCdpCacheDeviceId,
       "coCdpCacheTimeToLive": coCdpCacheTimeToLive,
       "coCdpCacheCapabilities": coCdpCacheCapabilities,
       "coCdpCacheVersion": coCdpCacheVersion,
       "coCdpCachePlatform": coCdpCachePlatform,
       "coCdpCachePortId": coCdpCachePortId,
       "coCdpGlobal": coCdpGlobal,
       "coCdpGlobalMessageInterval": coCdpGlobalMessageInterval,
       "coCdpGlobalHoldTime": coCdpGlobalHoldTime,
       "colubrisCdpMIBConformance": colubrisCdpMIBConformance,
       "colubrisCdpMIBCompliances": colubrisCdpMIBCompliances,
       "colubrisCdpMIBCompliance": colubrisCdpMIBCompliance,
       "colubrisCdpMIBGroups": colubrisCdpMIBGroups,
       "colubrisCdpMIBGroup": colubrisCdpMIBGroup}
)
