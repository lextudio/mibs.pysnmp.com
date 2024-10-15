# SNMP MIB module (Juniper-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:07 2024
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

(junidDvmrpInterfaceEntry,) = mibBuilder.importSymbols(
    "DVMRP-STD-MIB-JUNI",
    "junidDvmrpInterfaceEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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


# MODULE-IDENTITY

juniDvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44)
)
juniDvmrpMIB.setRevisions(
        ("2003-01-16 20:55",
         "2001-11-30 21:24")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
juniDvmrpMIBObjects = _JuniDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1)
)
_JuniDvmrp_ObjectIdentity = ObjectIdentity
juniDvmrp = _JuniDvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1)
)
_JuniDvmrpTraps_ObjectIdentity = ObjectIdentity
juniDvmrpTraps = _JuniDvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 0)
)
_JuniDvmrpScalar_ObjectIdentity = ObjectIdentity
juniDvmrpScalar = _JuniDvmrpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1)
)


class _JuniDvmrpAdminState_Type(Integer32):
    """Custom type juniDvmrpAdminState based on Integer32"""
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


_JuniDvmrpAdminState_Type.__name__ = "Integer32"
_JuniDvmrpAdminState_Object = MibScalar
juniDvmrpAdminState = _JuniDvmrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 1),
    _JuniDvmrpAdminState_Type()
)
juniDvmrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDvmrpAdminState.setStatus("current")


class _JuniDvmrpMcastAdminState_Type(Integer32):
    """Custom type juniDvmrpMcastAdminState based on Integer32"""
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


_JuniDvmrpMcastAdminState_Type.__name__ = "Integer32"
_JuniDvmrpMcastAdminState_Object = MibScalar
juniDvmrpMcastAdminState = _JuniDvmrpMcastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 2),
    _JuniDvmrpMcastAdminState_Type()
)
juniDvmrpMcastAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDvmrpMcastAdminState.setStatus("current")


class _JuniDvmrpRouteHogNotification_Type(Integer32):
    """Custom type juniDvmrpRouteHogNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 134217727),
    )


_JuniDvmrpRouteHogNotification_Type.__name__ = "Integer32"
_JuniDvmrpRouteHogNotification_Object = MibScalar
juniDvmrpRouteHogNotification = _JuniDvmrpRouteHogNotification_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 3),
    _JuniDvmrpRouteHogNotification_Type()
)
juniDvmrpRouteHogNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDvmrpRouteHogNotification.setStatus("current")


class _JuniDvmrpRouteLimit_Type(Integer32):
    """Custom type juniDvmrpRouteLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 134217727),
    )


_JuniDvmrpRouteLimit_Type.__name__ = "Integer32"
_JuniDvmrpRouteLimit_Object = MibScalar
juniDvmrpRouteLimit = _JuniDvmrpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 4),
    _JuniDvmrpRouteLimit_Type()
)
juniDvmrpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDvmrpRouteLimit.setStatus("current")


class _JuniDvmrpS32PrunesOnly_Type(Integer32):
    """Custom type juniDvmrpS32PrunesOnly based on Integer32"""
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


_JuniDvmrpS32PrunesOnly_Type.__name__ = "Integer32"
_JuniDvmrpS32PrunesOnly_Object = MibScalar
juniDvmrpS32PrunesOnly = _JuniDvmrpS32PrunesOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 5),
    _JuniDvmrpS32PrunesOnly_Type()
)
juniDvmrpS32PrunesOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDvmrpS32PrunesOnly.setStatus("current")
_JuniDvmrpUnicastRouting_Type = TruthValue
_JuniDvmrpUnicastRouting_Object = MibScalar
juniDvmrpUnicastRouting = _JuniDvmrpUnicastRouting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 6),
    _JuniDvmrpUnicastRouting_Type()
)
juniDvmrpUnicastRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDvmrpUnicastRouting.setStatus("current")
_JuniDvmrpAclDistNbrTable_Object = MibTable
juniDvmrpAclDistNbrTable = _JuniDvmrpAclDistNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrTable.setStatus("current")
_JuniDvmrpAclDistNbrEntry_Object = MibTableRow
juniDvmrpAclDistNbrEntry = _JuniDvmrpAclDistNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1)
)
juniDvmrpAclDistNbrEntry.setIndexNames(
    (0, "Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrIfIndex"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrAclListName"),
)
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrEntry.setStatus("current")
_JuniDvmrpAclDistNbrIfIndex_Type = InterfaceIndex
_JuniDvmrpAclDistNbrIfIndex_Object = MibTableColumn
juniDvmrpAclDistNbrIfIndex = _JuniDvmrpAclDistNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 1),
    _JuniDvmrpAclDistNbrIfIndex_Type()
)
juniDvmrpAclDistNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrIfIndex.setStatus("current")


class _JuniDvmrpAclDistNbrAclListName_Type(DisplayString):
    """Custom type juniDvmrpAclDistNbrAclListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JuniDvmrpAclDistNbrAclListName_Type.__name__ = "DisplayString"
_JuniDvmrpAclDistNbrAclListName_Object = MibTableColumn
juniDvmrpAclDistNbrAclListName = _JuniDvmrpAclDistNbrAclListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 2),
    _JuniDvmrpAclDistNbrAclListName_Type()
)
juniDvmrpAclDistNbrAclListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrAclListName.setStatus("current")


class _JuniDvmrpAclDistNbrDistance_Type(Integer32):
    """Custom type juniDvmrpAclDistNbrDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniDvmrpAclDistNbrDistance_Type.__name__ = "Integer32"
_JuniDvmrpAclDistNbrDistance_Object = MibTableColumn
juniDvmrpAclDistNbrDistance = _JuniDvmrpAclDistNbrDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 3),
    _JuniDvmrpAclDistNbrDistance_Type()
)
juniDvmrpAclDistNbrDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrDistance.setStatus("current")


class _JuniDvmrpAclDistNbrNbrListName_Type(DisplayString):
    """Custom type juniDvmrpAclDistNbrNbrListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JuniDvmrpAclDistNbrNbrListName_Type.__name__ = "DisplayString"
_JuniDvmrpAclDistNbrNbrListName_Object = MibTableColumn
juniDvmrpAclDistNbrNbrListName = _JuniDvmrpAclDistNbrNbrListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 4),
    _JuniDvmrpAclDistNbrNbrListName_Type()
)
juniDvmrpAclDistNbrNbrListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrNbrListName.setStatus("current")
_JuniDvmrpAclDistNbrStatus_Type = RowStatus
_JuniDvmrpAclDistNbrStatus_Object = MibTableColumn
juniDvmrpAclDistNbrStatus = _JuniDvmrpAclDistNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 5),
    _JuniDvmrpAclDistNbrStatus_Type()
)
juniDvmrpAclDistNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrStatus.setStatus("current")
_JuniDvmrpLocalAddrTable_Object = MibTable
juniDvmrpLocalAddrTable = _JuniDvmrpLocalAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniDvmrpLocalAddrTable.setStatus("current")
_JuniDvmrpLocalAddrTableEntry_Object = MibTableRow
juniDvmrpLocalAddrTableEntry = _JuniDvmrpLocalAddrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1)
)
juniDvmrpLocalAddrTableEntry.setIndexNames(
    (0, "Juniper-DVMRP-MIB", "juniDvmrpLocalAddrIfIndex"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpLocalAddrAddrOrIfIndex"),
)
if mibBuilder.loadTexts:
    juniDvmrpLocalAddrTableEntry.setStatus("current")
_JuniDvmrpLocalAddrIfIndex_Type = InterfaceIndex
_JuniDvmrpLocalAddrIfIndex_Object = MibTableColumn
juniDvmrpLocalAddrIfIndex = _JuniDvmrpLocalAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 1),
    _JuniDvmrpLocalAddrIfIndex_Type()
)
juniDvmrpLocalAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpLocalAddrIfIndex.setStatus("current")
_JuniDvmrpLocalAddrAddrOrIfIndex_Type = Unsigned32
_JuniDvmrpLocalAddrAddrOrIfIndex_Object = MibTableColumn
juniDvmrpLocalAddrAddrOrIfIndex = _JuniDvmrpLocalAddrAddrOrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 2),
    _JuniDvmrpLocalAddrAddrOrIfIndex_Type()
)
juniDvmrpLocalAddrAddrOrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpLocalAddrAddrOrIfIndex.setStatus("current")
_JuniDvmrpLocalAddrMask_Type = IpAddress
_JuniDvmrpLocalAddrMask_Object = MibTableColumn
juniDvmrpLocalAddrMask = _JuniDvmrpLocalAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 3),
    _JuniDvmrpLocalAddrMask_Type()
)
juniDvmrpLocalAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDvmrpLocalAddrMask.setStatus("current")
_JuniDvmrpSummaryAddrTable_Object = MibTable
juniDvmrpSummaryAddrTable = _JuniDvmrpSummaryAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniDvmrpSummaryAddrTable.setStatus("current")
_JuniDvmrpSummaryAddrTableEntry_Object = MibTableRow
juniDvmrpSummaryAddrTableEntry = _JuniDvmrpSummaryAddrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1)
)
juniDvmrpSummaryAddrTableEntry.setIndexNames(
    (0, "Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrIfIndex"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrAddress"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrMask"),
)
if mibBuilder.loadTexts:
    juniDvmrpSummaryAddrTableEntry.setStatus("current")
_JuniDvmrpSummaryAddrIfIndex_Type = InterfaceIndex
_JuniDvmrpSummaryAddrIfIndex_Object = MibTableColumn
juniDvmrpSummaryAddrIfIndex = _JuniDvmrpSummaryAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 1),
    _JuniDvmrpSummaryAddrIfIndex_Type()
)
juniDvmrpSummaryAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpSummaryAddrIfIndex.setStatus("current")
_JuniDvmrpSummaryAddrAddress_Type = IpAddress
_JuniDvmrpSummaryAddrAddress_Object = MibTableColumn
juniDvmrpSummaryAddrAddress = _JuniDvmrpSummaryAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 2),
    _JuniDvmrpSummaryAddrAddress_Type()
)
juniDvmrpSummaryAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpSummaryAddrAddress.setStatus("current")
_JuniDvmrpSummaryAddrMask_Type = IpAddress
_JuniDvmrpSummaryAddrMask_Object = MibTableColumn
juniDvmrpSummaryAddrMask = _JuniDvmrpSummaryAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 3),
    _JuniDvmrpSummaryAddrMask_Type()
)
juniDvmrpSummaryAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpSummaryAddrMask.setStatus("current")


class _JuniDvmrpSummaryAddrCost_Type(Integer32):
    """Custom type juniDvmrpSummaryAddrCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_JuniDvmrpSummaryAddrCost_Type.__name__ = "Integer32"
_JuniDvmrpSummaryAddrCost_Object = MibTableColumn
juniDvmrpSummaryAddrCost = _JuniDvmrpSummaryAddrCost_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 4),
    _JuniDvmrpSummaryAddrCost_Type()
)
juniDvmrpSummaryAddrCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpSummaryAddrCost.setStatus("current")
_JuniDvmrpSummaryAddrStatus_Type = RowStatus
_JuniDvmrpSummaryAddrStatus_Object = MibTableColumn
juniDvmrpSummaryAddrStatus = _JuniDvmrpSummaryAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 5),
    _JuniDvmrpSummaryAddrStatus_Type()
)
juniDvmrpSummaryAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpSummaryAddrStatus.setStatus("current")
_JuniDvmrpInterfaceTable_Object = MibTable
juniDvmrpInterfaceTable = _JuniDvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5)
)
if mibBuilder.loadTexts:
    juniDvmrpInterfaceTable.setStatus("current")
_JuniDvmrpInterfaceEntry_Object = MibTableRow
juniDvmrpInterfaceEntry = _JuniDvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniDvmrpInterfaceEntry.setStatus("current")


class _JuniDvmrpInterfaceAutoSummary_Type(Integer32):
    """Custom type juniDvmrpInterfaceAutoSummary based on Integer32"""
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


_JuniDvmrpInterfaceAutoSummary_Type.__name__ = "Integer32"
_JuniDvmrpInterfaceAutoSummary_Object = MibTableColumn
juniDvmrpInterfaceAutoSummary = _JuniDvmrpInterfaceAutoSummary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 3),
    _JuniDvmrpInterfaceAutoSummary_Type()
)
juniDvmrpInterfaceAutoSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpInterfaceAutoSummary.setStatus("current")


class _JuniDvmrpInterfaceMetricOffsetOut_Type(Integer32):
    """Custom type juniDvmrpInterfaceMetricOffsetOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_JuniDvmrpInterfaceMetricOffsetOut_Type.__name__ = "Integer32"
_JuniDvmrpInterfaceMetricOffsetOut_Object = MibTableColumn
juniDvmrpInterfaceMetricOffsetOut = _JuniDvmrpInterfaceMetricOffsetOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 4),
    _JuniDvmrpInterfaceMetricOffsetOut_Type()
)
juniDvmrpInterfaceMetricOffsetOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpInterfaceMetricOffsetOut.setStatus("current")


class _JuniDvmrpInterfaceMetricOffsetIn_Type(Integer32):
    """Custom type juniDvmrpInterfaceMetricOffsetIn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_JuniDvmrpInterfaceMetricOffsetIn_Type.__name__ = "Integer32"
_JuniDvmrpInterfaceMetricOffsetIn_Object = MibTableColumn
juniDvmrpInterfaceMetricOffsetIn = _JuniDvmrpInterfaceMetricOffsetIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 5),
    _JuniDvmrpInterfaceMetricOffsetIn_Type()
)
juniDvmrpInterfaceMetricOffsetIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpInterfaceMetricOffsetIn.setStatus("current")


class _JuniDvmrpInterfaceAdminState_Type(Integer32):
    """Custom type juniDvmrpInterfaceAdminState based on Integer32"""
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


_JuniDvmrpInterfaceAdminState_Type.__name__ = "Integer32"
_JuniDvmrpInterfaceAdminState_Object = MibTableColumn
juniDvmrpInterfaceAdminState = _JuniDvmrpInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 6),
    _JuniDvmrpInterfaceAdminState_Type()
)
juniDvmrpInterfaceAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpInterfaceAdminState.setStatus("current")
_JuniDvmrpInterfaceAnnounceListName_Type = DisplayString
_JuniDvmrpInterfaceAnnounceListName_Object = MibTableColumn
juniDvmrpInterfaceAnnounceListName = _JuniDvmrpInterfaceAnnounceListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 7),
    _JuniDvmrpInterfaceAnnounceListName_Type()
)
juniDvmrpInterfaceAnnounceListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDvmrpInterfaceAnnounceListName.setStatus("current")
_JuniDvmrpPruneTable_Object = MibTable
juniDvmrpPruneTable = _JuniDvmrpPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6)
)
if mibBuilder.loadTexts:
    juniDvmrpPruneTable.setStatus("current")
_JuniDvmrpPruneEntry_Object = MibTableRow
juniDvmrpPruneEntry = _JuniDvmrpPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1)
)
juniDvmrpPruneEntry.setIndexNames(
    (0, "Juniper-DVMRP-MIB", "juniDvmrpPruneGroup"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpPruneSource"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpPruneSourceMask"),
)
if mibBuilder.loadTexts:
    juniDvmrpPruneEntry.setStatus("current")
_JuniDvmrpPruneGroup_Type = IpAddress
_JuniDvmrpPruneGroup_Object = MibTableColumn
juniDvmrpPruneGroup = _JuniDvmrpPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 1),
    _JuniDvmrpPruneGroup_Type()
)
juniDvmrpPruneGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpPruneGroup.setStatus("current")
_JuniDvmrpPruneSource_Type = IpAddress
_JuniDvmrpPruneSource_Object = MibTableColumn
juniDvmrpPruneSource = _JuniDvmrpPruneSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 2),
    _JuniDvmrpPruneSource_Type()
)
juniDvmrpPruneSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpPruneSource.setStatus("current")
_JuniDvmrpPruneSourceMask_Type = IpAddress
_JuniDvmrpPruneSourceMask_Object = MibTableColumn
juniDvmrpPruneSourceMask = _JuniDvmrpPruneSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 3),
    _JuniDvmrpPruneSourceMask_Type()
)
juniDvmrpPruneSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpPruneSourceMask.setStatus("current")
_JuniDvmrpPruneIIFIfIndex_Type = InterfaceIndex
_JuniDvmrpPruneIIFIfIndex_Object = MibTableColumn
juniDvmrpPruneIIFIfIndex = _JuniDvmrpPruneIIFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 4),
    _JuniDvmrpPruneIIFIfIndex_Type()
)
juniDvmrpPruneIIFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDvmrpPruneIIFIfIndex.setStatus("current")
_JuniDvmrpPruneUpTime_Type = TimeTicks
_JuniDvmrpPruneUpTime_Object = MibTableColumn
juniDvmrpPruneUpTime = _JuniDvmrpPruneUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 5),
    _JuniDvmrpPruneUpTime_Type()
)
juniDvmrpPruneUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDvmrpPruneUpTime.setStatus("current")
_JuniDvmrpSrcGrpOifTable_Object = MibTable
juniDvmrpSrcGrpOifTable = _JuniDvmrpSrcGrpOifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7)
)
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifTable.setStatus("current")
_JuniDvmrpSrcGrpOifEntry_Object = MibTableRow
juniDvmrpSrcGrpOifEntry = _JuniDvmrpSrcGrpOifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1)
)
juniDvmrpSrcGrpOifEntry.setIndexNames(
    (0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifGroup"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifSource"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifSourceMask"),
    (0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifOIFIfIndex"),
)
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifEntry.setStatus("current")
_JuniDvmrpSrcGrpOifGroup_Type = IpAddress
_JuniDvmrpSrcGrpOifGroup_Object = MibTableColumn
juniDvmrpSrcGrpOifGroup = _JuniDvmrpSrcGrpOifGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 1),
    _JuniDvmrpSrcGrpOifGroup_Type()
)
juniDvmrpSrcGrpOifGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifGroup.setStatus("current")
_JuniDvmrpSrcGrpOifSource_Type = IpAddress
_JuniDvmrpSrcGrpOifSource_Object = MibTableColumn
juniDvmrpSrcGrpOifSource = _JuniDvmrpSrcGrpOifSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 2),
    _JuniDvmrpSrcGrpOifSource_Type()
)
juniDvmrpSrcGrpOifSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifSource.setStatus("current")
_JuniDvmrpSrcGrpOifSourceMask_Type = IpAddress
_JuniDvmrpSrcGrpOifSourceMask_Object = MibTableColumn
juniDvmrpSrcGrpOifSourceMask = _JuniDvmrpSrcGrpOifSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 3),
    _JuniDvmrpSrcGrpOifSourceMask_Type()
)
juniDvmrpSrcGrpOifSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifSourceMask.setStatus("current")
_JuniDvmrpSrcGrpOifOIFIfIndex_Type = InterfaceIndex
_JuniDvmrpSrcGrpOifOIFIfIndex_Object = MibTableColumn
juniDvmrpSrcGrpOifOIFIfIndex = _JuniDvmrpSrcGrpOifOIFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 4),
    _JuniDvmrpSrcGrpOifOIFIfIndex_Type()
)
juniDvmrpSrcGrpOifOIFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifOIFIfIndex.setStatus("current")


class _JuniDvmrpSrcGrpOifOIFPruned_Type(Integer32):
    """Custom type juniDvmrpSrcGrpOifOIFPruned based on Integer32"""
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


_JuniDvmrpSrcGrpOifOIFPruned_Type.__name__ = "Integer32"
_JuniDvmrpSrcGrpOifOIFPruned_Object = MibTableColumn
juniDvmrpSrcGrpOifOIFPruned = _JuniDvmrpSrcGrpOifOIFPruned_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 5),
    _JuniDvmrpSrcGrpOifOIFPruned_Type()
)
juniDvmrpSrcGrpOifOIFPruned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifOIFPruned.setStatus("current")
_JuniDvmrpSrcGrpOifOIFDnTTL_Type = TimeTicks
_JuniDvmrpSrcGrpOifOIFDnTTL_Object = MibTableColumn
juniDvmrpSrcGrpOifOIFDnTTL = _JuniDvmrpSrcGrpOifOIFDnTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 6),
    _JuniDvmrpSrcGrpOifOIFDnTTL_Type()
)
juniDvmrpSrcGrpOifOIFDnTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDvmrpSrcGrpOifOIFDnTTL.setStatus("current")
_JuniDvmrpConformance_ObjectIdentity = ObjectIdentity
juniDvmrpConformance = _JuniDvmrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4)
)
_JuniDvmrpCompliances_ObjectIdentity = ObjectIdentity
juniDvmrpCompliances = _JuniDvmrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1)
)
_JuniDvmrpGroups_ObjectIdentity = ObjectIdentity
juniDvmrpGroups = _JuniDvmrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2)
)
junidDvmrpInterfaceEntry.registerAugmentions(
    ("Juniper-DVMRP-MIB",
     "juniDvmrpInterfaceEntry")
)
juniDvmrpInterfaceEntry.setIndexNames(*junidDvmrpInterfaceEntry.getIndexNames())

# Managed Objects groups

juniDvmrpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 1)
)
juniDvmrpBaseGroup.setObjects(
      *(("Juniper-DVMRP-MIB", "juniDvmrpAdminState"),
        ("Juniper-DVMRP-MIB", "juniDvmrpMcastAdminState"),
        ("Juniper-DVMRP-MIB", "juniDvmrpRouteHogNotification"),
        ("Juniper-DVMRP-MIB", "juniDvmrpRouteLimit"),
        ("Juniper-DVMRP-MIB", "juniDvmrpS32PrunesOnly"))
)
if mibBuilder.loadTexts:
    juniDvmrpBaseGroup.setStatus("obsolete")

juniDvmrpAclDistNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 2)
)
juniDvmrpAclDistNbrGroup.setObjects(
      *(("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrDistance"),
        ("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrNbrListName"),
        ("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrStatus"))
)
if mibBuilder.loadTexts:
    juniDvmrpAclDistNbrGroup.setStatus("current")

juniDvmrpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 3)
)
juniDvmrpInterfaceGroup.setObjects(
      *(("Juniper-DVMRP-MIB", "juniDvmrpLocalAddrMask"),
        ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrCost"),
        ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrStatus"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAutoSummary"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetOut"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetIn"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAdminState"))
)
if mibBuilder.loadTexts:
    juniDvmrpInterfaceGroup.setStatus("obsolete")

juniDvmrpSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 4)
)
juniDvmrpSourceGroup.setObjects(
      *(("Juniper-DVMRP-MIB", "juniDvmrpPruneIIFIfIndex"),
        ("Juniper-DVMRP-MIB", "juniDvmrpPruneUpTime"),
        ("Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifOIFPruned"),
        ("Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifOIFDnTTL"))
)
if mibBuilder.loadTexts:
    juniDvmrpSourceGroup.setStatus("current")

juniDvmrpBaseGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 6)
)
juniDvmrpBaseGroup2.setObjects(
      *(("Juniper-DVMRP-MIB", "juniDvmrpAdminState"),
        ("Juniper-DVMRP-MIB", "juniDvmrpMcastAdminState"),
        ("Juniper-DVMRP-MIB", "juniDvmrpRouteHogNotification"),
        ("Juniper-DVMRP-MIB", "juniDvmrpRouteLimit"),
        ("Juniper-DVMRP-MIB", "juniDvmrpS32PrunesOnly"),
        ("Juniper-DVMRP-MIB", "juniDvmrpUnicastRouting"))
)
if mibBuilder.loadTexts:
    juniDvmrpBaseGroup2.setStatus("current")

juniDvmrpInterfaceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 7)
)
juniDvmrpInterfaceGroup2.setObjects(
      *(("Juniper-DVMRP-MIB", "juniDvmrpLocalAddrMask"),
        ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrCost"),
        ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrStatus"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAutoSummary"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetOut"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetIn"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAdminState"),
        ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAnnounceListName"))
)
if mibBuilder.loadTexts:
    juniDvmrpInterfaceGroup2.setStatus("current")


# Notification objects

juniDvmrpRouteHogNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    juniDvmrpRouteHogNotificationTrap.setStatus(
        "current"
    )


# Notifications groups

juniDvmrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 5)
)
juniDvmrpNotificationGroup.setObjects(
    ("Juniper-DVMRP-MIB", "juniDvmrpRouteHogNotificationTrap")
)
if mibBuilder.loadTexts:
    juniDvmrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniDvmrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniDvmrpCompliance.setStatus(
        "obsolete"
    )

juniDvmrpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniDvmrpCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DVMRP-MIB",
    **{"juniDvmrpMIB": juniDvmrpMIB,
       "juniDvmrpMIBObjects": juniDvmrpMIBObjects,
       "juniDvmrp": juniDvmrp,
       "juniDvmrpTraps": juniDvmrpTraps,
       "juniDvmrpRouteHogNotificationTrap": juniDvmrpRouteHogNotificationTrap,
       "juniDvmrpScalar": juniDvmrpScalar,
       "juniDvmrpAdminState": juniDvmrpAdminState,
       "juniDvmrpMcastAdminState": juniDvmrpMcastAdminState,
       "juniDvmrpRouteHogNotification": juniDvmrpRouteHogNotification,
       "juniDvmrpRouteLimit": juniDvmrpRouteLimit,
       "juniDvmrpS32PrunesOnly": juniDvmrpS32PrunesOnly,
       "juniDvmrpUnicastRouting": juniDvmrpUnicastRouting,
       "juniDvmrpAclDistNbrTable": juniDvmrpAclDistNbrTable,
       "juniDvmrpAclDistNbrEntry": juniDvmrpAclDistNbrEntry,
       "juniDvmrpAclDistNbrIfIndex": juniDvmrpAclDistNbrIfIndex,
       "juniDvmrpAclDistNbrAclListName": juniDvmrpAclDistNbrAclListName,
       "juniDvmrpAclDistNbrDistance": juniDvmrpAclDistNbrDistance,
       "juniDvmrpAclDistNbrNbrListName": juniDvmrpAclDistNbrNbrListName,
       "juniDvmrpAclDistNbrStatus": juniDvmrpAclDistNbrStatus,
       "juniDvmrpLocalAddrTable": juniDvmrpLocalAddrTable,
       "juniDvmrpLocalAddrTableEntry": juniDvmrpLocalAddrTableEntry,
       "juniDvmrpLocalAddrIfIndex": juniDvmrpLocalAddrIfIndex,
       "juniDvmrpLocalAddrAddrOrIfIndex": juniDvmrpLocalAddrAddrOrIfIndex,
       "juniDvmrpLocalAddrMask": juniDvmrpLocalAddrMask,
       "juniDvmrpSummaryAddrTable": juniDvmrpSummaryAddrTable,
       "juniDvmrpSummaryAddrTableEntry": juniDvmrpSummaryAddrTableEntry,
       "juniDvmrpSummaryAddrIfIndex": juniDvmrpSummaryAddrIfIndex,
       "juniDvmrpSummaryAddrAddress": juniDvmrpSummaryAddrAddress,
       "juniDvmrpSummaryAddrMask": juniDvmrpSummaryAddrMask,
       "juniDvmrpSummaryAddrCost": juniDvmrpSummaryAddrCost,
       "juniDvmrpSummaryAddrStatus": juniDvmrpSummaryAddrStatus,
       "juniDvmrpInterfaceTable": juniDvmrpInterfaceTable,
       "juniDvmrpInterfaceEntry": juniDvmrpInterfaceEntry,
       "juniDvmrpInterfaceAutoSummary": juniDvmrpInterfaceAutoSummary,
       "juniDvmrpInterfaceMetricOffsetOut": juniDvmrpInterfaceMetricOffsetOut,
       "juniDvmrpInterfaceMetricOffsetIn": juniDvmrpInterfaceMetricOffsetIn,
       "juniDvmrpInterfaceAdminState": juniDvmrpInterfaceAdminState,
       "juniDvmrpInterfaceAnnounceListName": juniDvmrpInterfaceAnnounceListName,
       "juniDvmrpPruneTable": juniDvmrpPruneTable,
       "juniDvmrpPruneEntry": juniDvmrpPruneEntry,
       "juniDvmrpPruneGroup": juniDvmrpPruneGroup,
       "juniDvmrpPruneSource": juniDvmrpPruneSource,
       "juniDvmrpPruneSourceMask": juniDvmrpPruneSourceMask,
       "juniDvmrpPruneIIFIfIndex": juniDvmrpPruneIIFIfIndex,
       "juniDvmrpPruneUpTime": juniDvmrpPruneUpTime,
       "juniDvmrpSrcGrpOifTable": juniDvmrpSrcGrpOifTable,
       "juniDvmrpSrcGrpOifEntry": juniDvmrpSrcGrpOifEntry,
       "juniDvmrpSrcGrpOifGroup": juniDvmrpSrcGrpOifGroup,
       "juniDvmrpSrcGrpOifSource": juniDvmrpSrcGrpOifSource,
       "juniDvmrpSrcGrpOifSourceMask": juniDvmrpSrcGrpOifSourceMask,
       "juniDvmrpSrcGrpOifOIFIfIndex": juniDvmrpSrcGrpOifOIFIfIndex,
       "juniDvmrpSrcGrpOifOIFPruned": juniDvmrpSrcGrpOifOIFPruned,
       "juniDvmrpSrcGrpOifOIFDnTTL": juniDvmrpSrcGrpOifOIFDnTTL,
       "juniDvmrpConformance": juniDvmrpConformance,
       "juniDvmrpCompliances": juniDvmrpCompliances,
       "juniDvmrpCompliance": juniDvmrpCompliance,
       "juniDvmrpCompliance2": juniDvmrpCompliance2,
       "juniDvmrpGroups": juniDvmrpGroups,
       "juniDvmrpBaseGroup": juniDvmrpBaseGroup,
       "juniDvmrpAclDistNbrGroup": juniDvmrpAclDistNbrGroup,
       "juniDvmrpInterfaceGroup": juniDvmrpInterfaceGroup,
       "juniDvmrpSourceGroup": juniDvmrpSourceGroup,
       "juniDvmrpNotificationGroup": juniDvmrpNotificationGroup,
       "juniDvmrpBaseGroup2": juniDvmrpBaseGroup2,
       "juniDvmrpInterfaceGroup2": juniDvmrpInterfaceGroup2}
)
