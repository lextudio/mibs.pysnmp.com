# SNMP MIB module (Unisphere-Data-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:36 2024
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

(dvmrpInterfaceEntry,) = mibBuilder.importSymbols(
    "DVMRP-STD-MIB",
    "dvmrpInterfaceEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdDvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44)
)
usdDvmrpMIB.setRevisions(
        ("2001-05-11 15:46",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
usdDvmrpMIBObjects = _UsdDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1)
)
_UsdDvmrp_ObjectIdentity = ObjectIdentity
usdDvmrp = _UsdDvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1)
)
_UsdDvmrpTraps_ObjectIdentity = ObjectIdentity
usdDvmrpTraps = _UsdDvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 0)
)
_UsdDvmrpScalar_ObjectIdentity = ObjectIdentity
usdDvmrpScalar = _UsdDvmrpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1)
)


class _UsdDvmrpAdminState_Type(Integer32):
    """Custom type usdDvmrpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdDvmrpAdminState_Type.__name__ = "Integer32"
_UsdDvmrpAdminState_Object = MibScalar
usdDvmrpAdminState = _UsdDvmrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 1),
    _UsdDvmrpAdminState_Type()
)
usdDvmrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdDvmrpAdminState.setStatus("current")


class _UsdDvmrpMcastAdminState_Type(Integer32):
    """Custom type usdDvmrpMcastAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdDvmrpMcastAdminState_Type.__name__ = "Integer32"
_UsdDvmrpMcastAdminState_Object = MibScalar
usdDvmrpMcastAdminState = _UsdDvmrpMcastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 2),
    _UsdDvmrpMcastAdminState_Type()
)
usdDvmrpMcastAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDvmrpMcastAdminState.setStatus("current")
_UsdDvmrpRouteHogNotification_Type = Integer32
_UsdDvmrpRouteHogNotification_Object = MibScalar
usdDvmrpRouteHogNotification = _UsdDvmrpRouteHogNotification_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 3),
    _UsdDvmrpRouteHogNotification_Type()
)
usdDvmrpRouteHogNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdDvmrpRouteHogNotification.setStatus("current")
_UsdDvmrpRouteLimit_Type = Integer32
_UsdDvmrpRouteLimit_Object = MibScalar
usdDvmrpRouteLimit = _UsdDvmrpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 4),
    _UsdDvmrpRouteLimit_Type()
)
usdDvmrpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdDvmrpRouteLimit.setStatus("current")


class _UsdDvmrpS32PrunesOnly_Type(Integer32):
    """Custom type usdDvmrpS32PrunesOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdDvmrpS32PrunesOnly_Type.__name__ = "Integer32"
_UsdDvmrpS32PrunesOnly_Object = MibScalar
usdDvmrpS32PrunesOnly = _UsdDvmrpS32PrunesOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 5),
    _UsdDvmrpS32PrunesOnly_Type()
)
usdDvmrpS32PrunesOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDvmrpS32PrunesOnly.setStatus("current")
_UsdDvmrpAclDistNbrTable_Object = MibTable
usdDvmrpAclDistNbrTable = _UsdDvmrpAclDistNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrTable.setStatus("current")
_UsdDvmrpAclDistNbrEntry_Object = MibTableRow
usdDvmrpAclDistNbrEntry = _UsdDvmrpAclDistNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1)
)
usdDvmrpAclDistNbrEntry.setIndexNames(
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpAclDistNbrIfIndex"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpAclDistNbrAclListName"),
)
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrEntry.setStatus("current")
_UsdDvmrpAclDistNbrIfIndex_Type = InterfaceIndex
_UsdDvmrpAclDistNbrIfIndex_Object = MibTableColumn
usdDvmrpAclDistNbrIfIndex = _UsdDvmrpAclDistNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 1),
    _UsdDvmrpAclDistNbrIfIndex_Type()
)
usdDvmrpAclDistNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrIfIndex.setStatus("current")


class _UsdDvmrpAclDistNbrAclListName_Type(DisplayString):
    """Custom type usdDvmrpAclDistNbrAclListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_UsdDvmrpAclDistNbrAclListName_Type.__name__ = "DisplayString"
_UsdDvmrpAclDistNbrAclListName_Object = MibTableColumn
usdDvmrpAclDistNbrAclListName = _UsdDvmrpAclDistNbrAclListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 2),
    _UsdDvmrpAclDistNbrAclListName_Type()
)
usdDvmrpAclDistNbrAclListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrAclListName.setStatus("current")


class _UsdDvmrpAclDistNbrDistance_Type(Integer32):
    """Custom type usdDvmrpAclDistNbrDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdDvmrpAclDistNbrDistance_Type.__name__ = "Integer32"
_UsdDvmrpAclDistNbrDistance_Object = MibTableColumn
usdDvmrpAclDistNbrDistance = _UsdDvmrpAclDistNbrDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 3),
    _UsdDvmrpAclDistNbrDistance_Type()
)
usdDvmrpAclDistNbrDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrDistance.setStatus("current")


class _UsdDvmrpAclDistNbrNbrListName_Type(DisplayString):
    """Custom type usdDvmrpAclDistNbrNbrListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_UsdDvmrpAclDistNbrNbrListName_Type.__name__ = "DisplayString"
_UsdDvmrpAclDistNbrNbrListName_Object = MibTableColumn
usdDvmrpAclDistNbrNbrListName = _UsdDvmrpAclDistNbrNbrListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 4),
    _UsdDvmrpAclDistNbrNbrListName_Type()
)
usdDvmrpAclDistNbrNbrListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrNbrListName.setStatus("current")
_UsdDvmrpAclDistNbrStatus_Type = RowStatus
_UsdDvmrpAclDistNbrStatus_Object = MibTableColumn
usdDvmrpAclDistNbrStatus = _UsdDvmrpAclDistNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 5),
    _UsdDvmrpAclDistNbrStatus_Type()
)
usdDvmrpAclDistNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrStatus.setStatus("current")
_UsdDvmrpLocalAddrTable_Object = MibTable
usdDvmrpLocalAddrTable = _UsdDvmrpLocalAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdDvmrpLocalAddrTable.setStatus("current")
_UsdDvmrpLocalAddrTableEntry_Object = MibTableRow
usdDvmrpLocalAddrTableEntry = _UsdDvmrpLocalAddrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1)
)
usdDvmrpLocalAddrTableEntry.setIndexNames(
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpLocalAddrIfIndex"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpLocalAddrAddrOrIfIndex"),
)
if mibBuilder.loadTexts:
    usdDvmrpLocalAddrTableEntry.setStatus("current")
_UsdDvmrpLocalAddrIfIndex_Type = InterfaceIndex
_UsdDvmrpLocalAddrIfIndex_Object = MibTableColumn
usdDvmrpLocalAddrIfIndex = _UsdDvmrpLocalAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 1),
    _UsdDvmrpLocalAddrIfIndex_Type()
)
usdDvmrpLocalAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpLocalAddrIfIndex.setStatus("current")
_UsdDvmrpLocalAddrAddrOrIfIndex_Type = Unsigned32
_UsdDvmrpLocalAddrAddrOrIfIndex_Object = MibTableColumn
usdDvmrpLocalAddrAddrOrIfIndex = _UsdDvmrpLocalAddrAddrOrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 2),
    _UsdDvmrpLocalAddrAddrOrIfIndex_Type()
)
usdDvmrpLocalAddrAddrOrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpLocalAddrAddrOrIfIndex.setStatus("current")
_UsdDvmrpLocalAddrMask_Type = IpAddress
_UsdDvmrpLocalAddrMask_Object = MibTableColumn
usdDvmrpLocalAddrMask = _UsdDvmrpLocalAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 3),
    _UsdDvmrpLocalAddrMask_Type()
)
usdDvmrpLocalAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDvmrpLocalAddrMask.setStatus("current")
_UsdDvmrpSummaryAddrTable_Object = MibTable
usdDvmrpSummaryAddrTable = _UsdDvmrpSummaryAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usdDvmrpSummaryAddrTable.setStatus("current")
_UsdDvmrpSummaryAddrTableEntry_Object = MibTableRow
usdDvmrpSummaryAddrTableEntry = _UsdDvmrpSummaryAddrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1)
)
usdDvmrpSummaryAddrTableEntry.setIndexNames(
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpSummaryAddrIfIndex"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpSummaryAddrAddress"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpSummaryAddrMask"),
)
if mibBuilder.loadTexts:
    usdDvmrpSummaryAddrTableEntry.setStatus("current")
_UsdDvmrpSummaryAddrIfIndex_Type = InterfaceIndex
_UsdDvmrpSummaryAddrIfIndex_Object = MibTableColumn
usdDvmrpSummaryAddrIfIndex = _UsdDvmrpSummaryAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 1),
    _UsdDvmrpSummaryAddrIfIndex_Type()
)
usdDvmrpSummaryAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpSummaryAddrIfIndex.setStatus("current")
_UsdDvmrpSummaryAddrAddress_Type = IpAddress
_UsdDvmrpSummaryAddrAddress_Object = MibTableColumn
usdDvmrpSummaryAddrAddress = _UsdDvmrpSummaryAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 2),
    _UsdDvmrpSummaryAddrAddress_Type()
)
usdDvmrpSummaryAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpSummaryAddrAddress.setStatus("current")
_UsdDvmrpSummaryAddrMask_Type = IpAddress
_UsdDvmrpSummaryAddrMask_Object = MibTableColumn
usdDvmrpSummaryAddrMask = _UsdDvmrpSummaryAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 3),
    _UsdDvmrpSummaryAddrMask_Type()
)
usdDvmrpSummaryAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpSummaryAddrMask.setStatus("current")


class _UsdDvmrpSummaryAddrCost_Type(Integer32):
    """Custom type usdDvmrpSummaryAddrCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_UsdDvmrpSummaryAddrCost_Type.__name__ = "Integer32"
_UsdDvmrpSummaryAddrCost_Object = MibTableColumn
usdDvmrpSummaryAddrCost = _UsdDvmrpSummaryAddrCost_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 4),
    _UsdDvmrpSummaryAddrCost_Type()
)
usdDvmrpSummaryAddrCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpSummaryAddrCost.setStatus("current")
_UsdDvmrpSummaryAddrStatus_Type = RowStatus
_UsdDvmrpSummaryAddrStatus_Object = MibTableColumn
usdDvmrpSummaryAddrStatus = _UsdDvmrpSummaryAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 5),
    _UsdDvmrpSummaryAddrStatus_Type()
)
usdDvmrpSummaryAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpSummaryAddrStatus.setStatus("current")
_UsdDvmrpInterfaceTable_Object = MibTable
usdDvmrpInterfaceTable = _UsdDvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5)
)
if mibBuilder.loadTexts:
    usdDvmrpInterfaceTable.setStatus("current")
_UsdDvmrpInterfaceEntry_Object = MibTableRow
usdDvmrpInterfaceEntry = _UsdDvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    usdDvmrpInterfaceEntry.setStatus("current")


class _UsdDvmrpInterfaceAutoSummary_Type(Integer32):
    """Custom type usdDvmrpInterfaceAutoSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdDvmrpInterfaceAutoSummary_Type.__name__ = "Integer32"
_UsdDvmrpInterfaceAutoSummary_Object = MibTableColumn
usdDvmrpInterfaceAutoSummary = _UsdDvmrpInterfaceAutoSummary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 3),
    _UsdDvmrpInterfaceAutoSummary_Type()
)
usdDvmrpInterfaceAutoSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpInterfaceAutoSummary.setStatus("current")


class _UsdDvmrpInterfaceMetricOffsetOut_Type(Integer32):
    """Custom type usdDvmrpInterfaceMetricOffsetOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_UsdDvmrpInterfaceMetricOffsetOut_Type.__name__ = "Integer32"
_UsdDvmrpInterfaceMetricOffsetOut_Object = MibTableColumn
usdDvmrpInterfaceMetricOffsetOut = _UsdDvmrpInterfaceMetricOffsetOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 4),
    _UsdDvmrpInterfaceMetricOffsetOut_Type()
)
usdDvmrpInterfaceMetricOffsetOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpInterfaceMetricOffsetOut.setStatus("current")


class _UsdDvmrpInterfaceMetricOffsetIn_Type(Integer32):
    """Custom type usdDvmrpInterfaceMetricOffsetIn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_UsdDvmrpInterfaceMetricOffsetIn_Type.__name__ = "Integer32"
_UsdDvmrpInterfaceMetricOffsetIn_Object = MibTableColumn
usdDvmrpInterfaceMetricOffsetIn = _UsdDvmrpInterfaceMetricOffsetIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 5),
    _UsdDvmrpInterfaceMetricOffsetIn_Type()
)
usdDvmrpInterfaceMetricOffsetIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpInterfaceMetricOffsetIn.setStatus("current")


class _UsdDvmrpInterfaceAdminState_Type(Integer32):
    """Custom type usdDvmrpInterfaceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdDvmrpInterfaceAdminState_Type.__name__ = "Integer32"
_UsdDvmrpInterfaceAdminState_Object = MibTableColumn
usdDvmrpInterfaceAdminState = _UsdDvmrpInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 6),
    _UsdDvmrpInterfaceAdminState_Type()
)
usdDvmrpInterfaceAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDvmrpInterfaceAdminState.setStatus("current")
_UsdDvmrpPruneTable_Object = MibTable
usdDvmrpPruneTable = _UsdDvmrpPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6)
)
if mibBuilder.loadTexts:
    usdDvmrpPruneTable.setStatus("current")
_UsdDvmrpPruneEntry_Object = MibTableRow
usdDvmrpPruneEntry = _UsdDvmrpPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1)
)
usdDvmrpPruneEntry.setIndexNames(
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpPruneGroup"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpPruneSource"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpPruneSourceMask"),
)
if mibBuilder.loadTexts:
    usdDvmrpPruneEntry.setStatus("current")
_UsdDvmrpPruneGroup_Type = IpAddress
_UsdDvmrpPruneGroup_Object = MibTableColumn
usdDvmrpPruneGroup = _UsdDvmrpPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 1),
    _UsdDvmrpPruneGroup_Type()
)
usdDvmrpPruneGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpPruneGroup.setStatus("current")
_UsdDvmrpPruneSource_Type = IpAddress
_UsdDvmrpPruneSource_Object = MibTableColumn
usdDvmrpPruneSource = _UsdDvmrpPruneSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 2),
    _UsdDvmrpPruneSource_Type()
)
usdDvmrpPruneSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpPruneSource.setStatus("current")
_UsdDvmrpPruneSourceMask_Type = IpAddress
_UsdDvmrpPruneSourceMask_Object = MibTableColumn
usdDvmrpPruneSourceMask = _UsdDvmrpPruneSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 3),
    _UsdDvmrpPruneSourceMask_Type()
)
usdDvmrpPruneSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpPruneSourceMask.setStatus("current")
_UsdDvmrpPruneIIFIfIndex_Type = InterfaceIndex
_UsdDvmrpPruneIIFIfIndex_Object = MibTableColumn
usdDvmrpPruneIIFIfIndex = _UsdDvmrpPruneIIFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 4),
    _UsdDvmrpPruneIIFIfIndex_Type()
)
usdDvmrpPruneIIFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDvmrpPruneIIFIfIndex.setStatus("current")
_UsdDvmrpPruneUpTime_Type = TimeTicks
_UsdDvmrpPruneUpTime_Object = MibTableColumn
usdDvmrpPruneUpTime = _UsdDvmrpPruneUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 5),
    _UsdDvmrpPruneUpTime_Type()
)
usdDvmrpPruneUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDvmrpPruneUpTime.setStatus("current")
_UsdDvmrpSrcGrpOifTable_Object = MibTable
usdDvmrpSrcGrpOifTable = _UsdDvmrpSrcGrpOifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7)
)
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifTable.setStatus("current")
_UsdDvmrpSrcGrpOifEntry_Object = MibTableRow
usdDvmrpSrcGrpOifEntry = _UsdDvmrpSrcGrpOifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1)
)
usdDvmrpSrcGrpOifEntry.setIndexNames(
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpSrcGrpOifGroup"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpSrcGrpOifSource"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpSrcGrpOifSourceMask"),
    (0, "Unisphere-Data-DVMRP-MIB", "usdDvmrpSrcGrpOifOIFIfIndex"),
)
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifEntry.setStatus("current")
_UsdDvmrpSrcGrpOifGroup_Type = IpAddress
_UsdDvmrpSrcGrpOifGroup_Object = MibTableColumn
usdDvmrpSrcGrpOifGroup = _UsdDvmrpSrcGrpOifGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 1),
    _UsdDvmrpSrcGrpOifGroup_Type()
)
usdDvmrpSrcGrpOifGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifGroup.setStatus("current")
_UsdDvmrpSrcGrpOifSource_Type = IpAddress
_UsdDvmrpSrcGrpOifSource_Object = MibTableColumn
usdDvmrpSrcGrpOifSource = _UsdDvmrpSrcGrpOifSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 2),
    _UsdDvmrpSrcGrpOifSource_Type()
)
usdDvmrpSrcGrpOifSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifSource.setStatus("current")
_UsdDvmrpSrcGrpOifSourceMask_Type = IpAddress
_UsdDvmrpSrcGrpOifSourceMask_Object = MibTableColumn
usdDvmrpSrcGrpOifSourceMask = _UsdDvmrpSrcGrpOifSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 3),
    _UsdDvmrpSrcGrpOifSourceMask_Type()
)
usdDvmrpSrcGrpOifSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifSourceMask.setStatus("current")
_UsdDvmrpSrcGrpOifOIFIfIndex_Type = InterfaceIndex
_UsdDvmrpSrcGrpOifOIFIfIndex_Object = MibTableColumn
usdDvmrpSrcGrpOifOIFIfIndex = _UsdDvmrpSrcGrpOifOIFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 4),
    _UsdDvmrpSrcGrpOifOIFIfIndex_Type()
)
usdDvmrpSrcGrpOifOIFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifOIFIfIndex.setStatus("current")


class _UsdDvmrpSrcGrpOifOIFPruned_Type(Integer32):
    """Custom type usdDvmrpSrcGrpOifOIFPruned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_UsdDvmrpSrcGrpOifOIFPruned_Type.__name__ = "Integer32"
_UsdDvmrpSrcGrpOifOIFPruned_Object = MibTableColumn
usdDvmrpSrcGrpOifOIFPruned = _UsdDvmrpSrcGrpOifOIFPruned_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 5),
    _UsdDvmrpSrcGrpOifOIFPruned_Type()
)
usdDvmrpSrcGrpOifOIFPruned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifOIFPruned.setStatus("current")
_UsdDvmrpSrcGrpOifOIFDnTTL_Type = TimeTicks
_UsdDvmrpSrcGrpOifOIFDnTTL_Object = MibTableColumn
usdDvmrpSrcGrpOifOIFDnTTL = _UsdDvmrpSrcGrpOifOIFDnTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 6),
    _UsdDvmrpSrcGrpOifOIFDnTTL_Type()
)
usdDvmrpSrcGrpOifOIFDnTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDvmrpSrcGrpOifOIFDnTTL.setStatus("current")
_UsdDvmrpConformance_ObjectIdentity = ObjectIdentity
usdDvmrpConformance = _UsdDvmrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4)
)
_UsdDvmrpCompliances_ObjectIdentity = ObjectIdentity
usdDvmrpCompliances = _UsdDvmrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1)
)
_UsdDvmrpGroups_ObjectIdentity = ObjectIdentity
usdDvmrpGroups = _UsdDvmrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2)
)
dvmrpInterfaceEntry.registerAugmentions(
    ("Unisphere-Data-DVMRP-MIB",
     "usdDvmrpInterfaceEntry")
)
usdDvmrpInterfaceEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())

# Managed Objects groups

usdDvmrpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 1)
)
usdDvmrpBaseGroup.setObjects(
      *(("Unisphere-Data-DVMRP-MIB", "usdDvmrpAdminState"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpMcastAdminState"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpRouteHogNotification"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpRouteLimit"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpS32PrunesOnly"))
)
if mibBuilder.loadTexts:
    usdDvmrpBaseGroup.setStatus("current")

usdDvmrpAclDistNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 2)
)
usdDvmrpAclDistNbrGroup.setObjects(
      *(("Unisphere-Data-DVMRP-MIB", "usdDvmrpAclDistNbrDistance"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpAclDistNbrNbrListName"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpAclDistNbrStatus"))
)
if mibBuilder.loadTexts:
    usdDvmrpAclDistNbrGroup.setStatus("current")

usdDvmrpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 3)
)
usdDvmrpInterfaceGroup.setObjects(
      *(("Unisphere-Data-DVMRP-MIB", "usdDvmrpLocalAddrMask"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpSummaryAddrCost"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpSummaryAddrStatus"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpInterfaceAutoSummary"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpInterfaceMetricOffsetOut"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpInterfaceMetricOffsetIn"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpInterfaceAdminState"))
)
if mibBuilder.loadTexts:
    usdDvmrpInterfaceGroup.setStatus("current")

usdDvmrpSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 4)
)
usdDvmrpSourceGroup.setObjects(
      *(("Unisphere-Data-DVMRP-MIB", "usdDvmrpPruneIIFIfIndex"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpPruneUpTime"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpSrcGrpOifOIFPruned"),
        ("Unisphere-Data-DVMRP-MIB", "usdDvmrpSrcGrpOifOIFDnTTL"))
)
if mibBuilder.loadTexts:
    usdDvmrpSourceGroup.setStatus("current")


# Notification objects

usdDvmrpRouteHogNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    usdDvmrpRouteHogNotificationTrap.setStatus(
        "current"
    )


# Notifications groups

usdDvmrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 8)
)
usdDvmrpNotificationGroup.setObjects(
    ("Unisphere-Data-DVMRP-MIB", "usdDvmrpRouteHogNotificationTrap")
)
if mibBuilder.loadTexts:
    usdDvmrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

usdDvmrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdDvmrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DVMRP-MIB",
    **{"usdDvmrpMIB": usdDvmrpMIB,
       "usdDvmrpMIBObjects": usdDvmrpMIBObjects,
       "usdDvmrp": usdDvmrp,
       "usdDvmrpTraps": usdDvmrpTraps,
       "usdDvmrpRouteHogNotificationTrap": usdDvmrpRouteHogNotificationTrap,
       "usdDvmrpScalar": usdDvmrpScalar,
       "usdDvmrpAdminState": usdDvmrpAdminState,
       "usdDvmrpMcastAdminState": usdDvmrpMcastAdminState,
       "usdDvmrpRouteHogNotification": usdDvmrpRouteHogNotification,
       "usdDvmrpRouteLimit": usdDvmrpRouteLimit,
       "usdDvmrpS32PrunesOnly": usdDvmrpS32PrunesOnly,
       "usdDvmrpAclDistNbrTable": usdDvmrpAclDistNbrTable,
       "usdDvmrpAclDistNbrEntry": usdDvmrpAclDistNbrEntry,
       "usdDvmrpAclDistNbrIfIndex": usdDvmrpAclDistNbrIfIndex,
       "usdDvmrpAclDistNbrAclListName": usdDvmrpAclDistNbrAclListName,
       "usdDvmrpAclDistNbrDistance": usdDvmrpAclDistNbrDistance,
       "usdDvmrpAclDistNbrNbrListName": usdDvmrpAclDistNbrNbrListName,
       "usdDvmrpAclDistNbrStatus": usdDvmrpAclDistNbrStatus,
       "usdDvmrpLocalAddrTable": usdDvmrpLocalAddrTable,
       "usdDvmrpLocalAddrTableEntry": usdDvmrpLocalAddrTableEntry,
       "usdDvmrpLocalAddrIfIndex": usdDvmrpLocalAddrIfIndex,
       "usdDvmrpLocalAddrAddrOrIfIndex": usdDvmrpLocalAddrAddrOrIfIndex,
       "usdDvmrpLocalAddrMask": usdDvmrpLocalAddrMask,
       "usdDvmrpSummaryAddrTable": usdDvmrpSummaryAddrTable,
       "usdDvmrpSummaryAddrTableEntry": usdDvmrpSummaryAddrTableEntry,
       "usdDvmrpSummaryAddrIfIndex": usdDvmrpSummaryAddrIfIndex,
       "usdDvmrpSummaryAddrAddress": usdDvmrpSummaryAddrAddress,
       "usdDvmrpSummaryAddrMask": usdDvmrpSummaryAddrMask,
       "usdDvmrpSummaryAddrCost": usdDvmrpSummaryAddrCost,
       "usdDvmrpSummaryAddrStatus": usdDvmrpSummaryAddrStatus,
       "usdDvmrpInterfaceTable": usdDvmrpInterfaceTable,
       "usdDvmrpInterfaceEntry": usdDvmrpInterfaceEntry,
       "usdDvmrpInterfaceAutoSummary": usdDvmrpInterfaceAutoSummary,
       "usdDvmrpInterfaceMetricOffsetOut": usdDvmrpInterfaceMetricOffsetOut,
       "usdDvmrpInterfaceMetricOffsetIn": usdDvmrpInterfaceMetricOffsetIn,
       "usdDvmrpInterfaceAdminState": usdDvmrpInterfaceAdminState,
       "usdDvmrpPruneTable": usdDvmrpPruneTable,
       "usdDvmrpPruneEntry": usdDvmrpPruneEntry,
       "usdDvmrpPruneGroup": usdDvmrpPruneGroup,
       "usdDvmrpPruneSource": usdDvmrpPruneSource,
       "usdDvmrpPruneSourceMask": usdDvmrpPruneSourceMask,
       "usdDvmrpPruneIIFIfIndex": usdDvmrpPruneIIFIfIndex,
       "usdDvmrpPruneUpTime": usdDvmrpPruneUpTime,
       "usdDvmrpSrcGrpOifTable": usdDvmrpSrcGrpOifTable,
       "usdDvmrpSrcGrpOifEntry": usdDvmrpSrcGrpOifEntry,
       "usdDvmrpSrcGrpOifGroup": usdDvmrpSrcGrpOifGroup,
       "usdDvmrpSrcGrpOifSource": usdDvmrpSrcGrpOifSource,
       "usdDvmrpSrcGrpOifSourceMask": usdDvmrpSrcGrpOifSourceMask,
       "usdDvmrpSrcGrpOifOIFIfIndex": usdDvmrpSrcGrpOifOIFIfIndex,
       "usdDvmrpSrcGrpOifOIFPruned": usdDvmrpSrcGrpOifOIFPruned,
       "usdDvmrpSrcGrpOifOIFDnTTL": usdDvmrpSrcGrpOifOIFDnTTL,
       "usdDvmrpConformance": usdDvmrpConformance,
       "usdDvmrpCompliances": usdDvmrpCompliances,
       "usdDvmrpCompliance": usdDvmrpCompliance,
       "usdDvmrpGroups": usdDvmrpGroups,
       "usdDvmrpBaseGroup": usdDvmrpBaseGroup,
       "usdDvmrpAclDistNbrGroup": usdDvmrpAclDistNbrGroup,
       "usdDvmrpInterfaceGroup": usdDvmrpInterfaceGroup,
       "usdDvmrpSourceGroup": usdDvmrpSourceGroup,
       "usdDvmrpNotificationGroup": usdDvmrpNotificationGroup}
)
