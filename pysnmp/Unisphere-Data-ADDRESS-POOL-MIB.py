# SNMP MIB module (Unisphere-Data-ADDRESS-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ADDRESS-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:17 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(usdRouterName,) = mibBuilder.importSymbols(
    "Unisphere-Data-ROUTER-MIB",
    "usdRouterName")


# MODULE-IDENTITY

usdAddressPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21)
)
usdAddressPoolMIB.setRevisions(
        ("2002-05-06 18:38",
         "2001-05-02 11:57",
         "2001-04-27 15:00",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdAddressPoolObjects_ObjectIdentity = ObjectIdentity
usdAddressPoolObjects = _UsdAddressPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1)
)
_UsdAddressPool_ObjectIdentity = ObjectIdentity
usdAddressPool = _UsdAddressPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1)
)
_UsdAddressPoolTable_Object = MibTable
usdAddressPoolTable = _UsdAddressPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdAddressPoolTable.setStatus("current")
_UsdAddressPoolEntry_Object = MibTableRow
usdAddressPoolEntry = _UsdAddressPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1)
)
usdAddressPoolEntry.setIndexNames(
    (0, "Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolIndex"),
)
if mibBuilder.loadTexts:
    usdAddressPoolEntry.setStatus("current")


class _UsdAddressPoolIndex_Type(Integer32):
    """Custom type usdAddressPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdAddressPoolIndex_Type.__name__ = "Integer32"
_UsdAddressPoolIndex_Object = MibTableColumn
usdAddressPoolIndex = _UsdAddressPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 1),
    _UsdAddressPoolIndex_Type()
)
usdAddressPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAddressPoolIndex.setStatus("current")
_UsdAddressPoolRowStatus_Type = RowStatus
_UsdAddressPoolRowStatus_Object = MibTableColumn
usdAddressPoolRowStatus = _UsdAddressPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 2),
    _UsdAddressPoolRowStatus_Type()
)
usdAddressPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolRowStatus.setStatus("current")


class _UsdAddressPoolName_Type(OctetString):
    """Custom type usdAddressPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_UsdAddressPoolName_Type.__name__ = "OctetString"
_UsdAddressPoolName_Object = MibTableColumn
usdAddressPoolName = _UsdAddressPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 3),
    _UsdAddressPoolName_Type()
)
usdAddressPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolName.setStatus("current")
_UsdAddressPoolStart_Type = IpAddress
_UsdAddressPoolStart_Object = MibTableColumn
usdAddressPoolStart = _UsdAddressPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 4),
    _UsdAddressPoolStart_Type()
)
usdAddressPoolStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolStart.setStatus("deprecated")
_UsdAddressPoolEnd_Type = IpAddress
_UsdAddressPoolEnd_Object = MibTableColumn
usdAddressPoolEnd = _UsdAddressPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 5),
    _UsdAddressPoolEnd_Type()
)
usdAddressPoolEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolEnd.setStatus("deprecated")
_UsdAddressPoolSize_Type = Integer32
_UsdAddressPoolSize_Object = MibTableColumn
usdAddressPoolSize = _UsdAddressPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 6),
    _UsdAddressPoolSize_Type()
)
usdAddressPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAddressPoolSize.setStatus("deprecated")
_UsdAddressPoolInUse_Type = Integer32
_UsdAddressPoolInUse_Object = MibTableColumn
usdAddressPoolInUse = _UsdAddressPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 7),
    _UsdAddressPoolInUse_Type()
)
usdAddressPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAddressPoolInUse.setStatus("deprecated")


class _UsdAddressPoolHighUtilThreshold_Type(Integer32):
    """Custom type usdAddressPoolHighUtilThreshold based on Integer32"""
    defaultValue = 85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_UsdAddressPoolHighUtilThreshold_Type.__name__ = "Integer32"
_UsdAddressPoolHighUtilThreshold_Object = MibTableColumn
usdAddressPoolHighUtilThreshold = _UsdAddressPoolHighUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 8),
    _UsdAddressPoolHighUtilThreshold_Type()
)
usdAddressPoolHighUtilThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolHighUtilThreshold.setStatus("current")


class _UsdAddressPoolAbatedUtilThreshold_Type(Integer32):
    """Custom type usdAddressPoolAbatedUtilThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_UsdAddressPoolAbatedUtilThreshold_Type.__name__ = "Integer32"
_UsdAddressPoolAbatedUtilThreshold_Object = MibTableColumn
usdAddressPoolAbatedUtilThreshold = _UsdAddressPoolAbatedUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 9),
    _UsdAddressPoolAbatedUtilThreshold_Type()
)
usdAddressPoolAbatedUtilThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolAbatedUtilThreshold.setStatus("current")


class _UsdAddressPoolUtilPct_Type(Integer32):
    """Custom type usdAddressPoolUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_UsdAddressPoolUtilPct_Type.__name__ = "Integer32"
_UsdAddressPoolUtilPct_Object = MibTableColumn
usdAddressPoolUtilPct = _UsdAddressPoolUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 10),
    _UsdAddressPoolUtilPct_Type()
)
usdAddressPoolUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAddressPoolUtilPct.setStatus("current")
_UsdAddressPoolTrapEnable_Type = TruthValue
_UsdAddressPoolTrapEnable_Object = MibTableColumn
usdAddressPoolTrapEnable = _UsdAddressPoolTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 11),
    _UsdAddressPoolTrapEnable_Type()
)
usdAddressPoolTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolTrapEnable.setStatus("current")


class _UsdAddressPoolNextPoolIndex_Type(Integer32):
    """Custom type usdAddressPoolNextPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAddressPoolNextPoolIndex_Type.__name__ = "Integer32"
_UsdAddressPoolNextPoolIndex_Object = MibScalar
usdAddressPoolNextPoolIndex = _UsdAddressPoolNextPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 2),
    _UsdAddressPoolNextPoolIndex_Type()
)
usdAddressPoolNextPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAddressPoolNextPoolIndex.setStatus("current")
_UsdAddressPoolProfileTable_Object = MibTable
usdAddressPoolProfileTable = _UsdAddressPoolProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdAddressPoolProfileTable.setStatus("current")
_UsdAddressPoolProfileEntry_Object = MibTableRow
usdAddressPoolProfileEntry = _UsdAddressPoolProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1)
)
usdAddressPoolProfileEntry.setIndexNames(
    (0, "Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolIndex"),
    (0, "Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolProfileIndex"),
)
if mibBuilder.loadTexts:
    usdAddressPoolProfileEntry.setStatus("current")


class _UsdAddressPoolProfileIndex_Type(Integer32):
    """Custom type usdAddressPoolProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdAddressPoolProfileIndex_Type.__name__ = "Integer32"
_UsdAddressPoolProfileIndex_Object = MibTableColumn
usdAddressPoolProfileIndex = _UsdAddressPoolProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 1),
    _UsdAddressPoolProfileIndex_Type()
)
usdAddressPoolProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAddressPoolProfileIndex.setStatus("current")
_UsdAddressPoolProfileRowStatus_Type = RowStatus
_UsdAddressPoolProfileRowStatus_Object = MibTableColumn
usdAddressPoolProfileRowStatus = _UsdAddressPoolProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 2),
    _UsdAddressPoolProfileRowStatus_Type()
)
usdAddressPoolProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolProfileRowStatus.setStatus("current")
_UsdAddressPoolProfileStart_Type = IpAddress
_UsdAddressPoolProfileStart_Object = MibTableColumn
usdAddressPoolProfileStart = _UsdAddressPoolProfileStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 3),
    _UsdAddressPoolProfileStart_Type()
)
usdAddressPoolProfileStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolProfileStart.setStatus("current")
_UsdAddressPoolProfileEnd_Type = IpAddress
_UsdAddressPoolProfileEnd_Object = MibTableColumn
usdAddressPoolProfileEnd = _UsdAddressPoolProfileEnd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 4),
    _UsdAddressPoolProfileEnd_Type()
)
usdAddressPoolProfileEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAddressPoolProfileEnd.setStatus("current")
_UsdAddressPoolProfileSize_Type = Integer32
_UsdAddressPoolProfileSize_Object = MibTableColumn
usdAddressPoolProfileSize = _UsdAddressPoolProfileSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 5),
    _UsdAddressPoolProfileSize_Type()
)
usdAddressPoolProfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAddressPoolProfileSize.setStatus("current")
_UsdAddressPoolProfileInUse_Type = Integer32
_UsdAddressPoolProfileInUse_Object = MibTableColumn
usdAddressPoolProfileInUse = _UsdAddressPoolProfileInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 6),
    _UsdAddressPoolProfileInUse_Type()
)
usdAddressPoolProfileInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAddressPoolProfileInUse.setStatus("current")
_UsdAddressPoolTraps_ObjectIdentity = ObjectIdentity
usdAddressPoolTraps = _UsdAddressPoolTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3)
)
_UsdAddressPoolTrapPrefix_ObjectIdentity = ObjectIdentity
usdAddressPoolTrapPrefix = _UsdAddressPoolTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0)
)
_UsdAddressPoolMIBConformance_ObjectIdentity = ObjectIdentity
usdAddressPoolMIBConformance = _UsdAddressPoolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4)
)
_UsdAddressPoolMIBCompliances_ObjectIdentity = ObjectIdentity
usdAddressPoolMIBCompliances = _UsdAddressPoolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1)
)
_UsdAddressPoolMIBGroups_ObjectIdentity = ObjectIdentity
usdAddressPoolMIBGroups = _UsdAddressPoolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2)
)

# Managed Objects groups

usdAddressPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 1)
)
usdAddressPoolGroup.setObjects(
      *(("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolRowStatus"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolStart"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolEnd"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolSize"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolInUse"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolNextPoolIndex"))
)
if mibBuilder.loadTexts:
    usdAddressPoolGroup.setStatus("obsolete")

usdAddressPoolGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 2)
)
usdAddressPoolGroup2.setObjects(
      *(("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolRowStatus"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolStart"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolEnd"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolSize"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolInUse"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolNextPoolIndex"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolHighUtilThreshold"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolAbatedUtilThreshold"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolUtilPct"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolTrapEnable"))
)
if mibBuilder.loadTexts:
    usdAddressPoolGroup2.setStatus("deprecated")

usdAddressPoolGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 4)
)
usdAddressPoolGroup3.setObjects(
      *(("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolRowStatus"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolNextPoolIndex"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolHighUtilThreshold"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolAbatedUtilThreshold"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolUtilPct"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolTrapEnable"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolProfileRowStatus"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolProfileStart"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolProfileEnd"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolProfileSize"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolProfileInUse"))
)
if mibBuilder.loadTexts:
    usdAddressPoolGroup3.setStatus("current")


# Notification objects

usdAddressPoolHighAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0, 1)
)
usdAddressPoolHighAddrUtil.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolSize"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolInUse"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolUtilPct"))
)
if mibBuilder.loadTexts:
    usdAddressPoolHighAddrUtil.setStatus(
        "current"
    )

usdAddressPoolAbatedAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0, 2)
)
usdAddressPoolAbatedAddrUtil.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolSize"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolInUse"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolUtilPct"))
)
if mibBuilder.loadTexts:
    usdAddressPoolAbatedAddrUtil.setStatus(
        "current"
    )

usdAddressPoolNoAddresses = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0, 3)
)
usdAddressPoolNoAddresses.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolName"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolSize"))
)
if mibBuilder.loadTexts:
    usdAddressPoolNoAddresses.setStatus(
        "current"
    )


# Notifications groups

usdAddressPoolTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 3)
)
usdAddressPoolTrapGroup.setObjects(
      *(("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolHighAddrUtil"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolAbatedAddrUtil"),
        ("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolNoAddresses"))
)
if mibBuilder.loadTexts:
    usdAddressPoolTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

usdAddressPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdAddressPoolCompliance.setStatus(
        "obsolete"
    )

usdAddressPoolCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdAddressPoolCompliance2.setStatus(
        "obsolete"
    )

usdAddressPoolCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdAddressPoolCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ADDRESS-POOL-MIB",
    **{"usdAddressPoolMIB": usdAddressPoolMIB,
       "usdAddressPoolObjects": usdAddressPoolObjects,
       "usdAddressPool": usdAddressPool,
       "usdAddressPoolTable": usdAddressPoolTable,
       "usdAddressPoolEntry": usdAddressPoolEntry,
       "usdAddressPoolIndex": usdAddressPoolIndex,
       "usdAddressPoolRowStatus": usdAddressPoolRowStatus,
       "usdAddressPoolName": usdAddressPoolName,
       "usdAddressPoolStart": usdAddressPoolStart,
       "usdAddressPoolEnd": usdAddressPoolEnd,
       "usdAddressPoolSize": usdAddressPoolSize,
       "usdAddressPoolInUse": usdAddressPoolInUse,
       "usdAddressPoolHighUtilThreshold": usdAddressPoolHighUtilThreshold,
       "usdAddressPoolAbatedUtilThreshold": usdAddressPoolAbatedUtilThreshold,
       "usdAddressPoolUtilPct": usdAddressPoolUtilPct,
       "usdAddressPoolTrapEnable": usdAddressPoolTrapEnable,
       "usdAddressPoolNextPoolIndex": usdAddressPoolNextPoolIndex,
       "usdAddressPoolProfileTable": usdAddressPoolProfileTable,
       "usdAddressPoolProfileEntry": usdAddressPoolProfileEntry,
       "usdAddressPoolProfileIndex": usdAddressPoolProfileIndex,
       "usdAddressPoolProfileRowStatus": usdAddressPoolProfileRowStatus,
       "usdAddressPoolProfileStart": usdAddressPoolProfileStart,
       "usdAddressPoolProfileEnd": usdAddressPoolProfileEnd,
       "usdAddressPoolProfileSize": usdAddressPoolProfileSize,
       "usdAddressPoolProfileInUse": usdAddressPoolProfileInUse,
       "usdAddressPoolTraps": usdAddressPoolTraps,
       "usdAddressPoolTrapPrefix": usdAddressPoolTrapPrefix,
       "usdAddressPoolHighAddrUtil": usdAddressPoolHighAddrUtil,
       "usdAddressPoolAbatedAddrUtil": usdAddressPoolAbatedAddrUtil,
       "usdAddressPoolNoAddresses": usdAddressPoolNoAddresses,
       "usdAddressPoolMIBConformance": usdAddressPoolMIBConformance,
       "usdAddressPoolMIBCompliances": usdAddressPoolMIBCompliances,
       "usdAddressPoolCompliance": usdAddressPoolCompliance,
       "usdAddressPoolCompliance2": usdAddressPoolCompliance2,
       "usdAddressPoolCompliance3": usdAddressPoolCompliance3,
       "usdAddressPoolMIBGroups": usdAddressPoolMIBGroups,
       "usdAddressPoolGroup": usdAddressPoolGroup,
       "usdAddressPoolGroup2": usdAddressPoolGroup2,
       "usdAddressPoolTrapGroup": usdAddressPoolTrapGroup,
       "usdAddressPoolGroup3": usdAddressPoolGroup3}
)
