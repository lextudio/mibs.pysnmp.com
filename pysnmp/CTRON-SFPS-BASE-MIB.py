# SNMP MIB module (CTRON-SFPS-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:16 2024
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

(sfpsATalkAMRVLANControl,
 sfpsBlockSource,
 sfpsBlockSourceAPI,
 sfpsBlockSourceExclude,
 sfpsBlockSourceOnly,
 sfpsBlockSourcePort,
 sfpsBlockSourceStats,
 sfpsCPResources,
 sfpsCSPControl,
 sfpsDHCPServerVLAN,
 sfpsServiceCenter) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsATalkAMRVLANControl",
    "sfpsBlockSource",
    "sfpsBlockSourceAPI",
    "sfpsBlockSourceExclude",
    "sfpsBlockSourceOnly",
    "sfpsBlockSourcePort",
    "sfpsBlockSourceStats",
    "sfpsCPResources",
    "sfpsCSPControl",
    "sfpsDHCPServerVLAN",
    "sfpsServiceCenter")

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


# MODULE-IDENTITY


# Types definitions



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsCPResourcesTable_Object = MibTable
sfpsCPResourcesTable = _SfpsCPResourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sfpsCPResourcesTable.setStatus("mandatory")
_SfpsCPResourcesTableEntry_Object = MibTableRow
sfpsCPResourcesTableEntry = _SfpsCPResourcesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1)
)
sfpsCPResourcesTableEntry.setIndexNames(
    (0, "CTRON-SFPS-BASE-MIB", "sfpsCPResourcesTableId"),
)
if mibBuilder.loadTexts:
    sfpsCPResourcesTableEntry.setStatus("mandatory")
_SfpsCPResourcesTableId_Type = Integer32
_SfpsCPResourcesTableId_Object = MibTableColumn
sfpsCPResourcesTableId = _SfpsCPResourcesTableId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 1),
    _SfpsCPResourcesTableId_Type()
)
sfpsCPResourcesTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTableId.setStatus("mandatory")
_SfpsCPResourcesTableName_Type = DisplayString
_SfpsCPResourcesTableName_Object = MibTableColumn
sfpsCPResourcesTableName = _SfpsCPResourcesTableName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 2),
    _SfpsCPResourcesTableName_Type()
)
sfpsCPResourcesTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTableName.setStatus("mandatory")


class _SfpsCPResourcesTableOperStatus_Type(Integer32):
    """Custom type sfpsCPResourcesTableOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsCPResourcesTableOperStatus_Type.__name__ = "Integer32"
_SfpsCPResourcesTableOperStatus_Object = MibTableColumn
sfpsCPResourcesTableOperStatus = _SfpsCPResourcesTableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 3),
    _SfpsCPResourcesTableOperStatus_Type()
)
sfpsCPResourcesTableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTableOperStatus.setStatus("mandatory")


class _SfpsCPResourcesTableAdminStatus_Type(Integer32):
    """Custom type sfpsCPResourcesTableAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsCPResourcesTableAdminStatus_Type.__name__ = "Integer32"
_SfpsCPResourcesTableAdminStatus_Object = MibTableColumn
sfpsCPResourcesTableAdminStatus = _SfpsCPResourcesTableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 4),
    _SfpsCPResourcesTableAdminStatus_Type()
)
sfpsCPResourcesTableAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTableAdminStatus.setStatus("mandatory")
_SfpsCPResourcesTableStateTime_Type = TimeTicks
_SfpsCPResourcesTableStateTime_Object = MibTableColumn
sfpsCPResourcesTableStateTime = _SfpsCPResourcesTableStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 5),
    _SfpsCPResourcesTableStateTime_Type()
)
sfpsCPResourcesTableStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTableStateTime.setStatus("mandatory")
_SfpsCPResourcesTablePtsIn_Type = Integer32
_SfpsCPResourcesTablePtsIn_Object = MibTableColumn
sfpsCPResourcesTablePtsIn = _SfpsCPResourcesTablePtsIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 6),
    _SfpsCPResourcesTablePtsIn_Type()
)
sfpsCPResourcesTablePtsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTablePtsIn.setStatus("mandatory")
_SfpsCPResourcesTablePtsUsed_Type = Integer32
_SfpsCPResourcesTablePtsUsed_Object = MibTableColumn
sfpsCPResourcesTablePtsUsed = _SfpsCPResourcesTablePtsUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 7),
    _SfpsCPResourcesTablePtsUsed_Type()
)
sfpsCPResourcesTablePtsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTablePtsUsed.setStatus("mandatory")
_SfpsCPResourcesTablePolicyFlood_Type = Integer32
_SfpsCPResourcesTablePolicyFlood_Object = MibTableColumn
sfpsCPResourcesTablePolicyFlood = _SfpsCPResourcesTablePolicyFlood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 8),
    _SfpsCPResourcesTablePolicyFlood_Type()
)
sfpsCPResourcesTablePolicyFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTablePolicyFlood.setStatus("mandatory")
_SfpsCPResourcesResolveFlood_Type = Integer32
_SfpsCPResourcesResolveFlood_Object = MibTableColumn
sfpsCPResourcesResolveFlood = _SfpsCPResourcesResolveFlood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 9),
    _SfpsCPResourcesResolveFlood_Type()
)
sfpsCPResourcesResolveFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesResolveFlood.setStatus("mandatory")
_SfpsCPResourcesConnectOK_Type = Integer32
_SfpsCPResourcesConnectOK_Object = MibTableColumn
sfpsCPResourcesConnectOK = _SfpsCPResourcesConnectOK_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 10),
    _SfpsCPResourcesConnectOK_Type()
)
sfpsCPResourcesConnectOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesConnectOK.setStatus("mandatory")
_SfpsCPResourcesDuplicate_Type = Integer32
_SfpsCPResourcesDuplicate_Object = MibTableColumn
sfpsCPResourcesDuplicate = _SfpsCPResourcesDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 11),
    _SfpsCPResourcesDuplicate_Type()
)
sfpsCPResourcesDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesDuplicate.setStatus("mandatory")
_SfpsCPResourcesDiscoverOnly_Type = Integer32
_SfpsCPResourcesDiscoverOnly_Object = MibTableColumn
sfpsCPResourcesDiscoverOnly = _SfpsCPResourcesDiscoverOnly_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 12),
    _SfpsCPResourcesDiscoverOnly_Type()
)
sfpsCPResourcesDiscoverOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesDiscoverOnly.setStatus("mandatory")
_SfpsCPResourcesDiscoverError_Type = Integer32
_SfpsCPResourcesDiscoverError_Object = MibTableColumn
sfpsCPResourcesDiscoverError = _SfpsCPResourcesDiscoverError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 13),
    _SfpsCPResourcesDiscoverError_Type()
)
sfpsCPResourcesDiscoverError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesDiscoverError.setStatus("mandatory")
_SfpsCPResourcesResolveFail_Type = Integer32
_SfpsCPResourcesResolveFail_Object = MibTableColumn
sfpsCPResourcesResolveFail = _SfpsCPResourcesResolveFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 14),
    _SfpsCPResourcesResolveFail_Type()
)
sfpsCPResourcesResolveFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesResolveFail.setStatus("mandatory")
_SfpsCPResourcesResolveError_Type = Integer32
_SfpsCPResourcesResolveError_Object = MibTableColumn
sfpsCPResourcesResolveError = _SfpsCPResourcesResolveError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 15),
    _SfpsCPResourcesResolveError_Type()
)
sfpsCPResourcesResolveError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesResolveError.setStatus("mandatory")
_SfpsCPResourcesPolicyFail_Type = Integer32
_SfpsCPResourcesPolicyFail_Object = MibTableColumn
sfpsCPResourcesPolicyFail = _SfpsCPResourcesPolicyFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 16),
    _SfpsCPResourcesPolicyFail_Type()
)
sfpsCPResourcesPolicyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesPolicyFail.setStatus("mandatory")
_SfpsCPResourcesPolicyError_Type = Integer32
_SfpsCPResourcesPolicyError_Object = MibTableColumn
sfpsCPResourcesPolicyError = _SfpsCPResourcesPolicyError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 17),
    _SfpsCPResourcesPolicyError_Type()
)
sfpsCPResourcesPolicyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesPolicyError.setStatus("mandatory")
_SfpsCPResourcesConnectFail_Type = Integer32
_SfpsCPResourcesConnectFail_Object = MibTableColumn
sfpsCPResourcesConnectFail = _SfpsCPResourcesConnectFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 18),
    _SfpsCPResourcesConnectFail_Type()
)
sfpsCPResourcesConnectFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesConnectFail.setStatus("mandatory")
_SfpsCPResourcesConnectFlood_Type = Integer32
_SfpsCPResourcesConnectFlood_Object = MibTableColumn
sfpsCPResourcesConnectFlood = _SfpsCPResourcesConnectFlood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 19),
    _SfpsCPResourcesConnectFlood_Type()
)
sfpsCPResourcesConnectFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesConnectFlood.setStatus("mandatory")
_SfpsCPResourcesConnectError_Type = Integer32
_SfpsCPResourcesConnectError_Object = MibTableColumn
sfpsCPResourcesConnectError = _SfpsCPResourcesConnectError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 20),
    _SfpsCPResourcesConnectError_Type()
)
sfpsCPResourcesConnectError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesConnectError.setStatus("mandatory")
_SfpsCPResourcesConfigTime_Type = TimeTicks
_SfpsCPResourcesConfigTime_Object = MibTableColumn
sfpsCPResourcesConfigTime = _SfpsCPResourcesConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 21),
    _SfpsCPResourcesConfigTime_Type()
)
sfpsCPResourcesConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesConfigTime.setStatus("mandatory")
_SfpsCPResourcesNeedFlood_Type = Integer32
_SfpsCPResourcesNeedFlood_Object = MibTableColumn
sfpsCPResourcesNeedFlood = _SfpsCPResourcesNeedFlood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 22),
    _SfpsCPResourcesNeedFlood_Type()
)
sfpsCPResourcesNeedFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesNeedFlood.setStatus("mandatory")
_SfpsCPResourcesNeedResolve_Type = Integer32
_SfpsCPResourcesNeedResolve_Object = MibTableColumn
sfpsCPResourcesNeedResolve = _SfpsCPResourcesNeedResolve_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 23),
    _SfpsCPResourcesNeedResolve_Type()
)
sfpsCPResourcesNeedResolve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesNeedResolve.setStatus("mandatory")
_SfpsCPResourcesNeedDiscover_Type = Integer32
_SfpsCPResourcesNeedDiscover_Object = MibTableColumn
sfpsCPResourcesNeedDiscover = _SfpsCPResourcesNeedDiscover_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 24),
    _SfpsCPResourcesNeedDiscover_Type()
)
sfpsCPResourcesNeedDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesNeedDiscover.setStatus("mandatory")
_SfpsCPResourcesDiscoverAll_Type = Integer32
_SfpsCPResourcesDiscoverAll_Object = MibTableColumn
sfpsCPResourcesDiscoverAll = _SfpsCPResourcesDiscoverAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 25),
    _SfpsCPResourcesDiscoverAll_Type()
)
sfpsCPResourcesDiscoverAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesDiscoverAll.setStatus("mandatory")
_SfpsCPResourcesNeedProxyOut_Type = Integer32
_SfpsCPResourcesNeedProxyOut_Object = MibTableColumn
sfpsCPResourcesNeedProxyOut = _SfpsCPResourcesNeedProxyOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 26),
    _SfpsCPResourcesNeedProxyOut_Type()
)
sfpsCPResourcesNeedProxyOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesNeedProxyOut.setStatus("mandatory")
_SfpsCPResourcesNeedProxyIn_Type = Integer32
_SfpsCPResourcesNeedProxyIn_Object = MibTableColumn
sfpsCPResourcesNeedProxyIn = _SfpsCPResourcesNeedProxyIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 27),
    _SfpsCPResourcesNeedProxyIn_Type()
)
sfpsCPResourcesNeedProxyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesNeedProxyIn.setStatus("mandatory")
_SfpsCPResourcesNeedFilter_Type = Integer32
_SfpsCPResourcesNeedFilter_Object = MibTableColumn
sfpsCPResourcesNeedFilter = _SfpsCPResourcesNeedFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 28),
    _SfpsCPResourcesNeedFilter_Type()
)
sfpsCPResourcesNeedFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesNeedFilter.setStatus("mandatory")
_SfpsCPResourcesAcceptRate_Type = Integer32
_SfpsCPResourcesAcceptRate_Object = MibTableColumn
sfpsCPResourcesAcceptRate = _SfpsCPResourcesAcceptRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 29),
    _SfpsCPResourcesAcceptRate_Type()
)
sfpsCPResourcesAcceptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesAcceptRate.setStatus("mandatory")
_SfpsCPResourcesTotalRate_Type = Integer32
_SfpsCPResourcesTotalRate_Object = MibTableColumn
sfpsCPResourcesTotalRate = _SfpsCPResourcesTotalRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 30),
    _SfpsCPResourcesTotalRate_Type()
)
sfpsCPResourcesTotalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesTotalRate.setStatus("mandatory")
_SfpsCPResourcesSingleFlood_Type = Integer32
_SfpsCPResourcesSingleFlood_Object = MibTableColumn
sfpsCPResourcesSingleFlood = _SfpsCPResourcesSingleFlood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 34),
    _SfpsCPResourcesSingleFlood_Type()
)
sfpsCPResourcesSingleFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesSingleFlood.setStatus("mandatory")
_SfpsCPResourcesNeedValidNet_Type = Integer32
_SfpsCPResourcesNeedValidNet_Object = MibTableColumn
sfpsCPResourcesNeedValidNet = _SfpsCPResourcesNeedValidNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 35),
    _SfpsCPResourcesNeedValidNet_Type()
)
sfpsCPResourcesNeedValidNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesNeedValidNet.setStatus("mandatory")
_SfpsCPResourcesInvalidNetDrops_Type = Integer32
_SfpsCPResourcesInvalidNetDrops_Object = MibTableColumn
sfpsCPResourcesInvalidNetDrops = _SfpsCPResourcesInvalidNetDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 36),
    _SfpsCPResourcesInvalidNetDrops_Type()
)
sfpsCPResourcesInvalidNetDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesInvalidNetDrops.setStatus("mandatory")
_SfpsCPResourcesPersistMask_Type = Integer32
_SfpsCPResourcesPersistMask_Object = MibTableColumn
sfpsCPResourcesPersistMask = _SfpsCPResourcesPersistMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 1, 1, 37),
    _SfpsCPResourcesPersistMask_Type()
)
sfpsCPResourcesPersistMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCPResourcesPersistMask.setStatus("mandatory")
_SfpsCPResourcesAPI_ObjectIdentity = ObjectIdentity
sfpsCPResourcesAPI = _SfpsCPResourcesAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 2)
)
_SfpsCPResourcesAPIID_Type = Integer32
_SfpsCPResourcesAPIID_Object = MibScalar
sfpsCPResourcesAPIID = _SfpsCPResourcesAPIID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 2, 1),
    _SfpsCPResourcesAPIID_Type()
)
sfpsCPResourcesAPIID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCPResourcesAPIID.setStatus("mandatory")


class _SfpsCPResourcesAPIAdminStatus_Type(Integer32):
    """Custom type sfpsCPResourcesAPIAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsCPResourcesAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsCPResourcesAPIAdminStatus_Object = MibScalar
sfpsCPResourcesAPIAdminStatus = _SfpsCPResourcesAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 2, 2),
    _SfpsCPResourcesAPIAdminStatus_Type()
)
sfpsCPResourcesAPIAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCPResourcesAPIAdminStatus.setStatus("mandatory")


class _SfpsCPResourcesAPIAttribute_Type(Integer32):
    """Custom type sfpsCPResourcesAPIAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("discover", 7),
          ("discoverAll", 9),
          ("filter", 15),
          ("flood", 3),
          ("noDiscover", 6),
          ("noDiscoverAll", 8),
          ("noFlood", 2),
          ("noProxyIn", 10),
          ("noProxyOut", 12),
          ("noResolve", 4),
          ("noValidateNet", 16),
          ("nofilter", 14),
          ("none", 1),
          ("proxyIn", 11),
          ("proxyOut", 13),
          ("resolve", 5),
          ("validNet", 17))
    )


_SfpsCPResourcesAPIAttribute_Type.__name__ = "Integer32"
_SfpsCPResourcesAPIAttribute_Object = MibScalar
sfpsCPResourcesAPIAttribute = _SfpsCPResourcesAPIAttribute_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 2, 3),
    _SfpsCPResourcesAPIAttribute_Type()
)
sfpsCPResourcesAPIAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCPResourcesAPIAttribute.setStatus("mandatory")


class _SfpsCPResourcesAPIScope_Type(Integer32):
    """Custom type sfpsCPResourcesAPIScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 2),
          ("switch", 1))
    )


_SfpsCPResourcesAPIScope_Type.__name__ = "Integer32"
_SfpsCPResourcesAPIScope_Object = MibScalar
sfpsCPResourcesAPIScope = _SfpsCPResourcesAPIScope_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 2, 4),
    _SfpsCPResourcesAPIScope_Type()
)
sfpsCPResourcesAPIScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCPResourcesAPIScope.setStatus("mandatory")


class _SfpsCPResourcesAPIPersistance_Type(Integer32):
    """Custom type sfpsCPResourcesAPIPersistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("persistDisabled", 2),
          ("persistEnabled", 3),
          ("persistOther", 1))
    )


_SfpsCPResourcesAPIPersistance_Type.__name__ = "Integer32"
_SfpsCPResourcesAPIPersistance_Object = MibScalar
sfpsCPResourcesAPIPersistance = _SfpsCPResourcesAPIPersistance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 2, 5),
    _SfpsCPResourcesAPIPersistance_Type()
)
sfpsCPResourcesAPIPersistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCPResourcesAPIPersistance.setStatus("mandatory")


class _SfpsCPResourcesAPIVerb_Type(Integer32):
    """Custom type sfpsCPResourcesAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("set", 2))
    )


_SfpsCPResourcesAPIVerb_Type.__name__ = "Integer32"
_SfpsCPResourcesAPIVerb_Object = MibScalar
sfpsCPResourcesAPIVerb = _SfpsCPResourcesAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3, 2, 6),
    _SfpsCPResourcesAPIVerb_Type()
)
sfpsCPResourcesAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCPResourcesAPIVerb.setStatus("mandatory")
_SfpsServiceCenterFacilityTable_Object = MibTable
sfpsServiceCenterFacilityTable = _SfpsServiceCenterFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityTable.setStatus("mandatory")
_SfpsServiceCenterFacilityEntry_Object = MibTableRow
sfpsServiceCenterFacilityEntry = _SfpsServiceCenterFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1)
)
sfpsServiceCenterFacilityEntry.setIndexNames(
    (0, "CTRON-SFPS-BASE-MIB", "sfpsServiceCenterFacilityHashLeaf"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityEntry.setStatus("mandatory")
_SfpsServiceCenterFacilityHashLeaf_Type = HexInteger
_SfpsServiceCenterFacilityHashLeaf_Object = MibTableColumn
sfpsServiceCenterFacilityHashLeaf = _SfpsServiceCenterFacilityHashLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 1),
    _SfpsServiceCenterFacilityHashLeaf_Type()
)
sfpsServiceCenterFacilityHashLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityHashLeaf.setStatus("mandatory")
_SfpsServiceCenterFacilityMetric_Type = Integer32
_SfpsServiceCenterFacilityMetric_Object = MibTableColumn
sfpsServiceCenterFacilityMetric = _SfpsServiceCenterFacilityMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 2),
    _SfpsServiceCenterFacilityMetric_Type()
)
sfpsServiceCenterFacilityMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityMetric.setStatus("mandatory")
_SfpsServiceCenterFacilityName_Type = DisplayString
_SfpsServiceCenterFacilityName_Object = MibTableColumn
sfpsServiceCenterFacilityName = _SfpsServiceCenterFacilityName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 3),
    _SfpsServiceCenterFacilityName_Type()
)
sfpsServiceCenterFacilityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityName.setStatus("mandatory")


class _SfpsServiceCenterFacilityOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterFacilityOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsServiceCenterFacilityOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterFacilityOperStatus_Object = MibTableColumn
sfpsServiceCenterFacilityOperStatus = _SfpsServiceCenterFacilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 4),
    _SfpsServiceCenterFacilityOperStatus_Type()
)
sfpsServiceCenterFacilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityOperStatus.setStatus("mandatory")


class _SfpsServiceCenterFacilityAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterFacilityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsServiceCenterFacilityAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterFacilityAdminStatus_Object = MibTableColumn
sfpsServiceCenterFacilityAdminStatus = _SfpsServiceCenterFacilityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 5),
    _SfpsServiceCenterFacilityAdminStatus_Type()
)
sfpsServiceCenterFacilityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityAdminStatus.setStatus("mandatory")
_SfpsServiceCenterFacilityStatusTime_Type = TimeTicks
_SfpsServiceCenterFacilityStatusTime_Object = MibTableColumn
sfpsServiceCenterFacilityStatusTime = _SfpsServiceCenterFacilityStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 6),
    _SfpsServiceCenterFacilityStatusTime_Type()
)
sfpsServiceCenterFacilityStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityStatusTime.setStatus("mandatory")
_SfpsServiceCenterFacilityRequests_Type = Integer32
_SfpsServiceCenterFacilityRequests_Object = MibTableColumn
sfpsServiceCenterFacilityRequests = _SfpsServiceCenterFacilityRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 7),
    _SfpsServiceCenterFacilityRequests_Type()
)
sfpsServiceCenterFacilityRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityRequests.setStatus("mandatory")
_SfpsServiceCenterFacilityReply_Type = Integer32
_SfpsServiceCenterFacilityReply_Object = MibTableColumn
sfpsServiceCenterFacilityReply = _SfpsServiceCenterFacilityReply_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 9, 1, 8),
    _SfpsServiceCenterFacilityReply_Type()
)
sfpsServiceCenterFacilityReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterFacilityReply.setStatus("mandatory")
_SfpsCSPControlTable_Object = MibTable
sfpsCSPControlTable = _SfpsCSPControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsCSPControlTable.setStatus("mandatory")
_SfpsCSPControlTableEntry_Object = MibTableRow
sfpsCSPControlTableEntry = _SfpsCSPControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1)
)
sfpsCSPControlTableEntry.setIndexNames(
    (0, "CTRON-SFPS-BASE-MIB", "sfpsCSPControlTableIndex"),
)
if mibBuilder.loadTexts:
    sfpsCSPControlTableEntry.setStatus("mandatory")
_SfpsCSPControlTableIndex_Type = Integer32
_SfpsCSPControlTableIndex_Object = MibTableColumn
sfpsCSPControlTableIndex = _SfpsCSPControlTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1, 1),
    _SfpsCSPControlTableIndex_Type()
)
sfpsCSPControlTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPControlTableIndex.setStatus("mandatory")
_SfpsCSPControlTableCSPType_Type = Integer32
_SfpsCSPControlTableCSPType_Object = MibTableColumn
sfpsCSPControlTableCSPType = _SfpsCSPControlTableCSPType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1, 2),
    _SfpsCSPControlTableCSPType_Type()
)
sfpsCSPControlTableCSPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPControlTableCSPType.setStatus("mandatory")
_SfpsCSPControlTableCSPName_Type = DisplayString
_SfpsCSPControlTableCSPName_Object = MibTableColumn
sfpsCSPControlTableCSPName = _SfpsCSPControlTableCSPName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1, 3),
    _SfpsCSPControlTableCSPName_Type()
)
sfpsCSPControlTableCSPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPControlTableCSPName.setStatus("mandatory")


class _SfpsCSPControlTableAdminStatus_Type(Integer32):
    """Custom type sfpsCSPControlTableAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsCSPControlTableAdminStatus_Type.__name__ = "Integer32"
_SfpsCSPControlTableAdminStatus_Object = MibTableColumn
sfpsCSPControlTableAdminStatus = _SfpsCSPControlTableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1, 4),
    _SfpsCSPControlTableAdminStatus_Type()
)
sfpsCSPControlTableAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCSPControlTableAdminStatus.setStatus("mandatory")


class _SfpsCSPControlTableSwitchToCallProc_Type(Integer32):
    """Custom type sfpsCSPControlTableSwitchToCallProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsCSPControlTableSwitchToCallProc_Type.__name__ = "Integer32"
_SfpsCSPControlTableSwitchToCallProc_Object = MibTableColumn
sfpsCSPControlTableSwitchToCallProc = _SfpsCSPControlTableSwitchToCallProc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1, 5),
    _SfpsCSPControlTableSwitchToCallProc_Type()
)
sfpsCSPControlTableSwitchToCallProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPControlTableSwitchToCallProc.setStatus("mandatory")
_SfpsCSPControlTablePktsProcessed_Type = Integer32
_SfpsCSPControlTablePktsProcessed_Object = MibTableColumn
sfpsCSPControlTablePktsProcessed = _SfpsCSPControlTablePktsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1, 6),
    _SfpsCSPControlTablePktsProcessed_Type()
)
sfpsCSPControlTablePktsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPControlTablePktsProcessed.setStatus("mandatory")
_SfpsCSPControlTablePktRate_Type = Integer32
_SfpsCSPControlTablePktRate_Object = MibTableColumn
sfpsCSPControlTablePktRate = _SfpsCSPControlTablePktRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5, 1, 1, 7),
    _SfpsCSPControlTablePktRate_Type()
)
sfpsCSPControlTablePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCSPControlTablePktRate.setStatus("mandatory")
_SfpsBlockSourceTable_Object = MibTable
sfpsBlockSourceTable = _SfpsBlockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsBlockSourceTable.setStatus("mandatory")
_SfpsBlockSourceEntry_Object = MibTableRow
sfpsBlockSourceEntry = _SfpsBlockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1)
)
sfpsBlockSourceEntry.setIndexNames(
    (0, "CTRON-SFPS-BASE-MIB", "sfpsBlockSourceIndex"),
)
if mibBuilder.loadTexts:
    sfpsBlockSourceEntry.setStatus("mandatory")
_SfpsBlockSourceIndex_Type = Integer32
_SfpsBlockSourceIndex_Object = MibTableColumn
sfpsBlockSourceIndex = _SfpsBlockSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 1),
    _SfpsBlockSourceIndex_Type()
)
sfpsBlockSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceIndex.setStatus("mandatory")
_SfpsBlockSourceMAC_Type = SfpsAddress
_SfpsBlockSourceMAC_Object = MibTableColumn
sfpsBlockSourceMAC = _SfpsBlockSourceMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 2),
    _SfpsBlockSourceMAC_Type()
)
sfpsBlockSourceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceMAC.setStatus("mandatory")
_SfpsBlockSourceElapTimeShort_Type = TimeTicks
_SfpsBlockSourceElapTimeShort_Object = MibTableColumn
sfpsBlockSourceElapTimeShort = _SfpsBlockSourceElapTimeShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 3),
    _SfpsBlockSourceElapTimeShort_Type()
)
sfpsBlockSourceElapTimeShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceElapTimeShort.setStatus("mandatory")
_SfpsBlockSourceNumCallsShort_Type = Integer32
_SfpsBlockSourceNumCallsShort_Object = MibTableColumn
sfpsBlockSourceNumCallsShort = _SfpsBlockSourceNumCallsShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 4),
    _SfpsBlockSourceNumCallsShort_Type()
)
sfpsBlockSourceNumCallsShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceNumCallsShort.setStatus("mandatory")
_SfpsBlockSourceElapTimeLong_Type = TimeTicks
_SfpsBlockSourceElapTimeLong_Object = MibTableColumn
sfpsBlockSourceElapTimeLong = _SfpsBlockSourceElapTimeLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 5),
    _SfpsBlockSourceElapTimeLong_Type()
)
sfpsBlockSourceElapTimeLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceElapTimeLong.setStatus("mandatory")
_SfpsBlockSourceNumCallLong_Type = Integer32
_SfpsBlockSourceNumCallLong_Object = MibTableColumn
sfpsBlockSourceNumCallLong = _SfpsBlockSourceNumCallLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 6),
    _SfpsBlockSourceNumCallLong_Type()
)
sfpsBlockSourceNumCallLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceNumCallLong.setStatus("mandatory")


class _SfpsBlockSourceBlockFlag_Type(Integer32):
    """Custom type sfpsBlockSourceBlockFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("wouldBeBlocked", 2))
    )


_SfpsBlockSourceBlockFlag_Type.__name__ = "Integer32"
_SfpsBlockSourceBlockFlag_Object = MibTableColumn
sfpsBlockSourceBlockFlag = _SfpsBlockSourceBlockFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 7),
    _SfpsBlockSourceBlockFlag_Type()
)
sfpsBlockSourceBlockFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceBlockFlag.setStatus("mandatory")


class _SfpsBlockSourceUnBlockableFlag_Type(Integer32):
    """Custom type sfpsBlockSourceUnBlockableFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unblockable", 1)
    )


_SfpsBlockSourceUnBlockableFlag_Type.__name__ = "Integer32"
_SfpsBlockSourceUnBlockableFlag_Object = MibTableColumn
sfpsBlockSourceUnBlockableFlag = _SfpsBlockSourceUnBlockableFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 8),
    _SfpsBlockSourceUnBlockableFlag_Type()
)
sfpsBlockSourceUnBlockableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceUnBlockableFlag.setStatus("mandatory")
_SfpsBlockSourceFilterPresent_Type = Integer32
_SfpsBlockSourceFilterPresent_Object = MibTableColumn
sfpsBlockSourceFilterPresent = _SfpsBlockSourceFilterPresent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 9),
    _SfpsBlockSourceFilterPresent_Type()
)
sfpsBlockSourceFilterPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceFilterPresent.setStatus("mandatory")
_SfpsBlockSourceNext_Type = Integer32
_SfpsBlockSourceNext_Object = MibTableColumn
sfpsBlockSourceNext = _SfpsBlockSourceNext_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 10),
    _SfpsBlockSourceNext_Type()
)
sfpsBlockSourceNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceNext.setStatus("mandatory")
_SfpsBlockSourceBlocksOnlyIndex_Type = Integer32
_SfpsBlockSourceBlocksOnlyIndex_Object = MibTableColumn
sfpsBlockSourceBlocksOnlyIndex = _SfpsBlockSourceBlocksOnlyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1, 1, 1, 11),
    _SfpsBlockSourceBlocksOnlyIndex_Type()
)
sfpsBlockSourceBlocksOnlyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceBlocksOnlyIndex.setStatus("mandatory")
_SfpsBlockSourceOnlyTable_Object = MibTable
sfpsBlockSourceOnlyTable = _SfpsBlockSourceOnlyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyTable.setStatus("mandatory")
_SfpsBlockSourceOnlyEntry_Object = MibTableRow
sfpsBlockSourceOnlyEntry = _SfpsBlockSourceOnlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1)
)
sfpsBlockSourceOnlyEntry.setIndexNames(
    (0, "CTRON-SFPS-BASE-MIB", "sfpsBlockSourceOnlyIndex"),
)
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyEntry.setStatus("mandatory")
_SfpsBlockSourceOnlyIndex_Type = Integer32
_SfpsBlockSourceOnlyIndex_Object = MibTableColumn
sfpsBlockSourceOnlyIndex = _SfpsBlockSourceOnlyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 1),
    _SfpsBlockSourceOnlyIndex_Type()
)
sfpsBlockSourceOnlyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyIndex.setStatus("mandatory")
_SfpsBlockSourceOnlyMAC_Type = SfpsAddress
_SfpsBlockSourceOnlyMAC_Object = MibTableColumn
sfpsBlockSourceOnlyMAC = _SfpsBlockSourceOnlyMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 2),
    _SfpsBlockSourceOnlyMAC_Type()
)
sfpsBlockSourceOnlyMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyMAC.setStatus("mandatory")
_SfpsBlockSourceOnlyElapTimeShort_Type = TimeTicks
_SfpsBlockSourceOnlyElapTimeShort_Object = MibTableColumn
sfpsBlockSourceOnlyElapTimeShort = _SfpsBlockSourceOnlyElapTimeShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 3),
    _SfpsBlockSourceOnlyElapTimeShort_Type()
)
sfpsBlockSourceOnlyElapTimeShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyElapTimeShort.setStatus("mandatory")
_SfpsBlockSourceOnlyNumCallsShort_Type = Integer32
_SfpsBlockSourceOnlyNumCallsShort_Object = MibTableColumn
sfpsBlockSourceOnlyNumCallsShort = _SfpsBlockSourceOnlyNumCallsShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 4),
    _SfpsBlockSourceOnlyNumCallsShort_Type()
)
sfpsBlockSourceOnlyNumCallsShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyNumCallsShort.setStatus("mandatory")
_SfpsBlockSourceOnlyElapTimeLong_Type = TimeTicks
_SfpsBlockSourceOnlyElapTimeLong_Object = MibTableColumn
sfpsBlockSourceOnlyElapTimeLong = _SfpsBlockSourceOnlyElapTimeLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 5),
    _SfpsBlockSourceOnlyElapTimeLong_Type()
)
sfpsBlockSourceOnlyElapTimeLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyElapTimeLong.setStatus("mandatory")
_SfpsBlockSourceOnlyNumCallLong_Type = Integer32
_SfpsBlockSourceOnlyNumCallLong_Object = MibTableColumn
sfpsBlockSourceOnlyNumCallLong = _SfpsBlockSourceOnlyNumCallLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 6),
    _SfpsBlockSourceOnlyNumCallLong_Type()
)
sfpsBlockSourceOnlyNumCallLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyNumCallLong.setStatus("mandatory")


class _SfpsBlockSourceOnlyBlockFlag_Type(Integer32):
    """Custom type sfpsBlockSourceOnlyBlockFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("wouldBeBlocked", 2))
    )


_SfpsBlockSourceOnlyBlockFlag_Type.__name__ = "Integer32"
_SfpsBlockSourceOnlyBlockFlag_Object = MibTableColumn
sfpsBlockSourceOnlyBlockFlag = _SfpsBlockSourceOnlyBlockFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 7),
    _SfpsBlockSourceOnlyBlockFlag_Type()
)
sfpsBlockSourceOnlyBlockFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyBlockFlag.setStatus("mandatory")


class _SfpsBlockSourceOnlyUnBlockableFlag_Type(Integer32):
    """Custom type sfpsBlockSourceOnlyUnBlockableFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unblockable", 1)
    )


_SfpsBlockSourceOnlyUnBlockableFlag_Type.__name__ = "Integer32"
_SfpsBlockSourceOnlyUnBlockableFlag_Object = MibTableColumn
sfpsBlockSourceOnlyUnBlockableFlag = _SfpsBlockSourceOnlyUnBlockableFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 8),
    _SfpsBlockSourceOnlyUnBlockableFlag_Type()
)
sfpsBlockSourceOnlyUnBlockableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyUnBlockableFlag.setStatus("mandatory")
_SfpsBlockSourceOnlyFilterPresent_Type = Integer32
_SfpsBlockSourceOnlyFilterPresent_Object = MibTableColumn
sfpsBlockSourceOnlyFilterPresent = _SfpsBlockSourceOnlyFilterPresent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 9),
    _SfpsBlockSourceOnlyFilterPresent_Type()
)
sfpsBlockSourceOnlyFilterPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyFilterPresent.setStatus("mandatory")
_SfpsBlockSourceOnlyNext_Type = Integer32
_SfpsBlockSourceOnlyNext_Object = MibTableColumn
sfpsBlockSourceOnlyNext = _SfpsBlockSourceOnlyNext_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 10),
    _SfpsBlockSourceOnlyNext_Type()
)
sfpsBlockSourceOnlyNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyNext.setStatus("mandatory")
_SfpsBlockSourceOnlyBlocksOnlyIndex_Type = Integer32
_SfpsBlockSourceOnlyBlocksOnlyIndex_Object = MibTableColumn
sfpsBlockSourceOnlyBlocksOnlyIndex = _SfpsBlockSourceOnlyBlocksOnlyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2, 1, 1, 11),
    _SfpsBlockSourceOnlyBlocksOnlyIndex_Type()
)
sfpsBlockSourceOnlyBlocksOnlyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceOnlyBlocksOnlyIndex.setStatus("mandatory")
_SfpsBlockSourcePortTable_Object = MibTable
sfpsBlockSourcePortTable = _SfpsBlockSourcePortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    sfpsBlockSourcePortTable.setStatus("mandatory")
_SfpsBlockSourcePortEntry_Object = MibTableRow
sfpsBlockSourcePortEntry = _SfpsBlockSourcePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 3, 1, 1)
)
sfpsBlockSourcePortEntry.setIndexNames(
    (0, "CTRON-SFPS-BASE-MIB", "sfpsBlockSourcePortPort"),
)
if mibBuilder.loadTexts:
    sfpsBlockSourcePortEntry.setStatus("mandatory")
_SfpsBlockSourcePortPort_Type = Integer32
_SfpsBlockSourcePortPort_Object = MibTableColumn
sfpsBlockSourcePortPort = _SfpsBlockSourcePortPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 3, 1, 1, 1),
    _SfpsBlockSourcePortPort_Type()
)
sfpsBlockSourcePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourcePortPort.setStatus("mandatory")


class _SfpsBlockSourcePortBlockability_Type(Integer32):
    """Custom type sfpsBlockSourcePortBlockability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unblockable", 1)
    )


_SfpsBlockSourcePortBlockability_Type.__name__ = "Integer32"
_SfpsBlockSourcePortBlockability_Object = MibTableColumn
sfpsBlockSourcePortBlockability = _SfpsBlockSourcePortBlockability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 3, 1, 1, 2),
    _SfpsBlockSourcePortBlockability_Type()
)
sfpsBlockSourcePortBlockability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourcePortBlockability.setStatus("mandatory")


class _SfpsBlockSourceAPIVerb_Type(Integer32):
    """Custom type sfpsBlockSourceAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("blockMac", 9),
          ("clearAll", 8),
          ("other", 1),
          ("setLongPeriod", 7),
          ("setLongThreshold", 6),
          ("setMacBlockable", 12),
          ("setMacUnblockable", 11),
          ("setPortBlockable", 14),
          ("setPortUnblockable", 13),
          ("setReapUserCnx", 15),
          ("setShortPeriod", 5),
          ("setShortThreshold", 4),
          ("switchToBlocking", 3),
          ("switchToLearning", 2),
          ("unblockMac", 10))
    )


_SfpsBlockSourceAPIVerb_Type.__name__ = "Integer32"
_SfpsBlockSourceAPIVerb_Object = MibScalar
sfpsBlockSourceAPIVerb = _SfpsBlockSourceAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 1),
    _SfpsBlockSourceAPIVerb_Type()
)
sfpsBlockSourceAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIVerb.setStatus("mandatory")
_SfpsBlockSourceAPIInputValue_Type = Integer32
_SfpsBlockSourceAPIInputValue_Object = MibScalar
sfpsBlockSourceAPIInputValue = _SfpsBlockSourceAPIInputValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 2),
    _SfpsBlockSourceAPIInputValue_Type()
)
sfpsBlockSourceAPIInputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIInputValue.setStatus("mandatory")
_SfpsBlockSourceAPIPort_Type = Integer32
_SfpsBlockSourceAPIPort_Object = MibScalar
sfpsBlockSourceAPIPort = _SfpsBlockSourceAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 3),
    _SfpsBlockSourceAPIPort_Type()
)
sfpsBlockSourceAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIPort.setStatus("mandatory")
_SfpsBlockSourceAPIMAC_Type = SfpsAddress
_SfpsBlockSourceAPIMAC_Object = MibScalar
sfpsBlockSourceAPIMAC = _SfpsBlockSourceAPIMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 4),
    _SfpsBlockSourceAPIMAC_Type()
)
sfpsBlockSourceAPIMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIMAC.setStatus("mandatory")


class _SfpsBlockSourceAPIBlockStatus_Type(Integer32):
    """Custom type sfpsBlockSourceAPIBlockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("learning", 2),
          ("other", 1))
    )


_SfpsBlockSourceAPIBlockStatus_Type.__name__ = "Integer32"
_SfpsBlockSourceAPIBlockStatus_Object = MibScalar
sfpsBlockSourceAPIBlockStatus = _SfpsBlockSourceAPIBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 5),
    _SfpsBlockSourceAPIBlockStatus_Type()
)
sfpsBlockSourceAPIBlockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIBlockStatus.setStatus("mandatory")
_SfpsBlockSourceAPIShortThreshold_Type = Integer32
_SfpsBlockSourceAPIShortThreshold_Object = MibScalar
sfpsBlockSourceAPIShortThreshold = _SfpsBlockSourceAPIShortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 6),
    _SfpsBlockSourceAPIShortThreshold_Type()
)
sfpsBlockSourceAPIShortThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIShortThreshold.setStatus("mandatory")
_SfpsBlockSourceAPIShortPeriod_Type = Integer32
_SfpsBlockSourceAPIShortPeriod_Object = MibScalar
sfpsBlockSourceAPIShortPeriod = _SfpsBlockSourceAPIShortPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 7),
    _SfpsBlockSourceAPIShortPeriod_Type()
)
sfpsBlockSourceAPIShortPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIShortPeriod.setStatus("mandatory")
_SfpsBlockSourceAPILongThreshold_Type = Integer32
_SfpsBlockSourceAPILongThreshold_Object = MibScalar
sfpsBlockSourceAPILongThreshold = _SfpsBlockSourceAPILongThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 8),
    _SfpsBlockSourceAPILongThreshold_Type()
)
sfpsBlockSourceAPILongThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPILongThreshold.setStatus("mandatory")
_SfpsBlockSourceAPILongPeriod_Type = Integer32
_SfpsBlockSourceAPILongPeriod_Object = MibScalar
sfpsBlockSourceAPILongPeriod = _SfpsBlockSourceAPILongPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 9),
    _SfpsBlockSourceAPILongPeriod_Type()
)
sfpsBlockSourceAPILongPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPILongPeriod.setStatus("mandatory")
_SfpsBlockSourceAPIReapUserCnxs_Type = Integer32
_SfpsBlockSourceAPIReapUserCnxs_Object = MibScalar
sfpsBlockSourceAPIReapUserCnxs = _SfpsBlockSourceAPIReapUserCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4, 10),
    _SfpsBlockSourceAPIReapUserCnxs_Type()
)
sfpsBlockSourceAPIReapUserCnxs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockSourceAPIReapUserCnxs.setStatus("mandatory")
_SfpsBlockSourceExcludeTable_Object = MibTable
sfpsBlockSourceExcludeTable = _SfpsBlockSourceExcludeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeTable.setStatus("mandatory")
_SfpsBlockSourceExcludeEntry_Object = MibTableRow
sfpsBlockSourceExcludeEntry = _SfpsBlockSourceExcludeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1)
)
sfpsBlockSourceExcludeEntry.setIndexNames(
    (0, "CTRON-SFPS-BASE-MIB", "sfpsBlockSourceExcludeIndex"),
)
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeEntry.setStatus("mandatory")
_SfpsBlockSourceExcludeIndex_Type = Integer32
_SfpsBlockSourceExcludeIndex_Object = MibTableColumn
sfpsBlockSourceExcludeIndex = _SfpsBlockSourceExcludeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 1),
    _SfpsBlockSourceExcludeIndex_Type()
)
sfpsBlockSourceExcludeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeIndex.setStatus("mandatory")
_SfpsBlockSourceExcludeMAC_Type = SfpsAddress
_SfpsBlockSourceExcludeMAC_Object = MibTableColumn
sfpsBlockSourceExcludeMAC = _SfpsBlockSourceExcludeMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 2),
    _SfpsBlockSourceExcludeMAC_Type()
)
sfpsBlockSourceExcludeMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeMAC.setStatus("mandatory")
_SfpsBlockSourceExcludeElapTimeShort_Type = TimeTicks
_SfpsBlockSourceExcludeElapTimeShort_Object = MibTableColumn
sfpsBlockSourceExcludeElapTimeShort = _SfpsBlockSourceExcludeElapTimeShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 3),
    _SfpsBlockSourceExcludeElapTimeShort_Type()
)
sfpsBlockSourceExcludeElapTimeShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeElapTimeShort.setStatus("mandatory")
_SfpsBlockSourceExcludeNumCallsShort_Type = Integer32
_SfpsBlockSourceExcludeNumCallsShort_Object = MibTableColumn
sfpsBlockSourceExcludeNumCallsShort = _SfpsBlockSourceExcludeNumCallsShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 4),
    _SfpsBlockSourceExcludeNumCallsShort_Type()
)
sfpsBlockSourceExcludeNumCallsShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeNumCallsShort.setStatus("mandatory")
_SfpsBlockSourceExcludeElapTimeLong_Type = TimeTicks
_SfpsBlockSourceExcludeElapTimeLong_Object = MibTableColumn
sfpsBlockSourceExcludeElapTimeLong = _SfpsBlockSourceExcludeElapTimeLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 5),
    _SfpsBlockSourceExcludeElapTimeLong_Type()
)
sfpsBlockSourceExcludeElapTimeLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeElapTimeLong.setStatus("mandatory")
_SfpsBlockSourceExcludeNumCallLong_Type = Integer32
_SfpsBlockSourceExcludeNumCallLong_Object = MibTableColumn
sfpsBlockSourceExcludeNumCallLong = _SfpsBlockSourceExcludeNumCallLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 6),
    _SfpsBlockSourceExcludeNumCallLong_Type()
)
sfpsBlockSourceExcludeNumCallLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeNumCallLong.setStatus("mandatory")


class _SfpsBlockSourceExcludeBlockFlag_Type(Integer32):
    """Custom type sfpsBlockSourceExcludeBlockFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("wouldBeBlocked", 2))
    )


_SfpsBlockSourceExcludeBlockFlag_Type.__name__ = "Integer32"
_SfpsBlockSourceExcludeBlockFlag_Object = MibTableColumn
sfpsBlockSourceExcludeBlockFlag = _SfpsBlockSourceExcludeBlockFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 7),
    _SfpsBlockSourceExcludeBlockFlag_Type()
)
sfpsBlockSourceExcludeBlockFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeBlockFlag.setStatus("mandatory")


class _SfpsBlockSourceExcludeUnBlockableFlag_Type(Integer32):
    """Custom type sfpsBlockSourceExcludeUnBlockableFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unblockable", 1)
    )


_SfpsBlockSourceExcludeUnBlockableFlag_Type.__name__ = "Integer32"
_SfpsBlockSourceExcludeUnBlockableFlag_Object = MibTableColumn
sfpsBlockSourceExcludeUnBlockableFlag = _SfpsBlockSourceExcludeUnBlockableFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 8),
    _SfpsBlockSourceExcludeUnBlockableFlag_Type()
)
sfpsBlockSourceExcludeUnBlockableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeUnBlockableFlag.setStatus("mandatory")
_SfpsBlockSourceExcludeFilterPresent_Type = Integer32
_SfpsBlockSourceExcludeFilterPresent_Object = MibTableColumn
sfpsBlockSourceExcludeFilterPresent = _SfpsBlockSourceExcludeFilterPresent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 9),
    _SfpsBlockSourceExcludeFilterPresent_Type()
)
sfpsBlockSourceExcludeFilterPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeFilterPresent.setStatus("mandatory")
_SfpsBlockSourceExcludeNext_Type = Integer32
_SfpsBlockSourceExcludeNext_Object = MibTableColumn
sfpsBlockSourceExcludeNext = _SfpsBlockSourceExcludeNext_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 10),
    _SfpsBlockSourceExcludeNext_Type()
)
sfpsBlockSourceExcludeNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeNext.setStatus("mandatory")
_SfpsBlockSourceExcludeBlockSourceOnlyIndex_Type = Integer32
_SfpsBlockSourceExcludeBlockSourceOnlyIndex_Object = MibTableColumn
sfpsBlockSourceExcludeBlockSourceOnlyIndex = _SfpsBlockSourceExcludeBlockSourceOnlyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5, 1, 1, 11),
    _SfpsBlockSourceExcludeBlockSourceOnlyIndex_Type()
)
sfpsBlockSourceExcludeBlockSourceOnlyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceExcludeBlockSourceOnlyIndex.setStatus("mandatory")
_SfpsBlockSourceStatsNumBlocks_Type = Integer32
_SfpsBlockSourceStatsNumBlocks_Object = MibScalar
sfpsBlockSourceStatsNumBlocks = _SfpsBlockSourceStatsNumBlocks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 1),
    _SfpsBlockSourceStatsNumBlocks_Type()
)
sfpsBlockSourceStatsNumBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsNumBlocks.setStatus("mandatory")
_SfpsBlockSourceStatsNumCollisions_Type = Integer32
_SfpsBlockSourceStatsNumCollisions_Object = MibScalar
sfpsBlockSourceStatsNumCollisions = _SfpsBlockSourceStatsNumCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 2),
    _SfpsBlockSourceStatsNumCollisions_Type()
)
sfpsBlockSourceStatsNumCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsNumCollisions.setStatus("mandatory")
_SfpsBlockSourceStatsLongestChain_Type = Integer32
_SfpsBlockSourceStatsLongestChain_Object = MibScalar
sfpsBlockSourceStatsLongestChain = _SfpsBlockSourceStatsLongestChain_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 3),
    _SfpsBlockSourceStatsLongestChain_Type()
)
sfpsBlockSourceStatsLongestChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsLongestChain.setStatus("mandatory")
_SfpsBlockSourceStatsNumEntries_Type = Integer32
_SfpsBlockSourceStatsNumEntries_Object = MibScalar
sfpsBlockSourceStatsNumEntries = _SfpsBlockSourceStatsNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 4),
    _SfpsBlockSourceStatsNumEntries_Type()
)
sfpsBlockSourceStatsNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsNumEntries.setStatus("mandatory")
_SfpsBlockSourceStatsMaxNumEntries_Type = Integer32
_SfpsBlockSourceStatsMaxNumEntries_Object = MibScalar
sfpsBlockSourceStatsMaxNumEntries = _SfpsBlockSourceStatsMaxNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 5),
    _SfpsBlockSourceStatsMaxNumEntries_Type()
)
sfpsBlockSourceStatsMaxNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsMaxNumEntries.setStatus("mandatory")
_SfpsBlockSourceStatsSizeOfObj_Type = Integer32
_SfpsBlockSourceStatsSizeOfObj_Object = MibScalar
sfpsBlockSourceStatsSizeOfObj = _SfpsBlockSourceStatsSizeOfObj_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 6),
    _SfpsBlockSourceStatsSizeOfObj_Type()
)
sfpsBlockSourceStatsSizeOfObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsSizeOfObj.setStatus("mandatory")
_SfpsBlockSourceStatsHashModValue_Type = Integer32
_SfpsBlockSourceStatsHashModValue_Object = MibScalar
sfpsBlockSourceStatsHashModValue = _SfpsBlockSourceStatsHashModValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 7),
    _SfpsBlockSourceStatsHashModValue_Type()
)
sfpsBlockSourceStatsHashModValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsHashModValue.setStatus("mandatory")
_SfpsBlockSourceStatsHashSlotsSize_Type = Integer32
_SfpsBlockSourceStatsHashSlotsSize_Object = MibScalar
sfpsBlockSourceStatsHashSlotsSize = _SfpsBlockSourceStatsHashSlotsSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 8),
    _SfpsBlockSourceStatsHashSlotsSize_Type()
)
sfpsBlockSourceStatsHashSlotsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsHashSlotsSize.setStatus("mandatory")
_SfpsBlockSourceStatsTableSize_Type = Integer32
_SfpsBlockSourceStatsTableSize_Object = MibScalar
sfpsBlockSourceStatsTableSize = _SfpsBlockSourceStatsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 9),
    _SfpsBlockSourceStatsTableSize_Type()
)
sfpsBlockSourceStatsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsTableSize.setStatus("mandatory")
_SfpsBlockSourceStatsBlockSourceOnlySize_Type = Integer32
_SfpsBlockSourceStatsBlockSourceOnlySize_Object = MibScalar
sfpsBlockSourceStatsBlockSourceOnlySize = _SfpsBlockSourceStatsBlockSourceOnlySize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 10),
    _SfpsBlockSourceStatsBlockSourceOnlySize_Type()
)
sfpsBlockSourceStatsBlockSourceOnlySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsBlockSourceOnlySize.setStatus("mandatory")
_SfpsBlockSourceStatsUnblockableSize_Type = Integer32
_SfpsBlockSourceStatsUnblockableSize_Object = MibScalar
sfpsBlockSourceStatsUnblockableSize = _SfpsBlockSourceStatsUnblockableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 11),
    _SfpsBlockSourceStatsUnblockableSize_Type()
)
sfpsBlockSourceStatsUnblockableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsUnblockableSize.setStatus("mandatory")
_SfpsBlockSourceStatsPortMaskSize_Type = Integer32
_SfpsBlockSourceStatsPortMaskSize_Object = MibScalar
sfpsBlockSourceStatsPortMaskSize = _SfpsBlockSourceStatsPortMaskSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 12),
    _SfpsBlockSourceStatsPortMaskSize_Type()
)
sfpsBlockSourceStatsPortMaskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsPortMaskSize.setStatus("mandatory")
_SfpsBlockSourceStatsTotalHeapBytes_Type = Integer32
_SfpsBlockSourceStatsTotalHeapBytes_Object = MibScalar
sfpsBlockSourceStatsTotalHeapBytes = _SfpsBlockSourceStatsTotalHeapBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6, 13),
    _SfpsBlockSourceStatsTotalHeapBytes_Type()
)
sfpsBlockSourceStatsTotalHeapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockSourceStatsTotalHeapBytes.setStatus("mandatory")
_SfpsDHCPServerVLANName_Type = OctetString
_SfpsDHCPServerVLANName_Object = MibScalar
sfpsDHCPServerVLANName = _SfpsDHCPServerVLANName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 15, 1),
    _SfpsDHCPServerVLANName_Type()
)
sfpsDHCPServerVLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDHCPServerVLANName.setStatus("mandatory")


class _SfpsDHCPServerVLANSingleFloodStatus_Type(Integer32):
    """Custom type sfpsDHCPServerVLANSingleFloodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SfpsDHCPServerVLANSingleFloodStatus_Type.__name__ = "Integer32"
_SfpsDHCPServerVLANSingleFloodStatus_Object = MibScalar
sfpsDHCPServerVLANSingleFloodStatus = _SfpsDHCPServerVLANSingleFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 15, 2),
    _SfpsDHCPServerVLANSingleFloodStatus_Type()
)
sfpsDHCPServerVLANSingleFloodStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDHCPServerVLANSingleFloodStatus.setStatus("mandatory")
_SfpsDHCPServerVLANVersion_Type = Integer32
_SfpsDHCPServerVLANVersion_Object = MibScalar
sfpsDHCPServerVLANVersion = _SfpsDHCPServerVLANVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 15, 3),
    _SfpsDHCPServerVLANVersion_Type()
)
sfpsDHCPServerVLANVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDHCPServerVLANVersion.setStatus("mandatory")
_SfpsATalkAMRVLANControlName_Type = OctetString
_SfpsATalkAMRVLANControlName_Object = MibScalar
sfpsATalkAMRVLANControlName = _SfpsATalkAMRVLANControlName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 16, 1),
    _SfpsATalkAMRVLANControlName_Type()
)
sfpsATalkAMRVLANControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATalkAMRVLANControlName.setStatus("mandatory")
_SfpsATalkAMRVLANControlVersion_Type = Integer32
_SfpsATalkAMRVLANControlVersion_Object = MibScalar
sfpsATalkAMRVLANControlVersion = _SfpsATalkAMRVLANControlVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 16, 2),
    _SfpsATalkAMRVLANControlVersion_Type()
)
sfpsATalkAMRVLANControlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATalkAMRVLANControlVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-BASE-MIB",
    **{"HexInteger": HexInteger,
       "SfpsAddress": SfpsAddress,
       "sfpsCPResourcesTable": sfpsCPResourcesTable,
       "sfpsCPResourcesTableEntry": sfpsCPResourcesTableEntry,
       "sfpsCPResourcesTableId": sfpsCPResourcesTableId,
       "sfpsCPResourcesTableName": sfpsCPResourcesTableName,
       "sfpsCPResourcesTableOperStatus": sfpsCPResourcesTableOperStatus,
       "sfpsCPResourcesTableAdminStatus": sfpsCPResourcesTableAdminStatus,
       "sfpsCPResourcesTableStateTime": sfpsCPResourcesTableStateTime,
       "sfpsCPResourcesTablePtsIn": sfpsCPResourcesTablePtsIn,
       "sfpsCPResourcesTablePtsUsed": sfpsCPResourcesTablePtsUsed,
       "sfpsCPResourcesTablePolicyFlood": sfpsCPResourcesTablePolicyFlood,
       "sfpsCPResourcesResolveFlood": sfpsCPResourcesResolveFlood,
       "sfpsCPResourcesConnectOK": sfpsCPResourcesConnectOK,
       "sfpsCPResourcesDuplicate": sfpsCPResourcesDuplicate,
       "sfpsCPResourcesDiscoverOnly": sfpsCPResourcesDiscoverOnly,
       "sfpsCPResourcesDiscoverError": sfpsCPResourcesDiscoverError,
       "sfpsCPResourcesResolveFail": sfpsCPResourcesResolveFail,
       "sfpsCPResourcesResolveError": sfpsCPResourcesResolveError,
       "sfpsCPResourcesPolicyFail": sfpsCPResourcesPolicyFail,
       "sfpsCPResourcesPolicyError": sfpsCPResourcesPolicyError,
       "sfpsCPResourcesConnectFail": sfpsCPResourcesConnectFail,
       "sfpsCPResourcesConnectFlood": sfpsCPResourcesConnectFlood,
       "sfpsCPResourcesConnectError": sfpsCPResourcesConnectError,
       "sfpsCPResourcesConfigTime": sfpsCPResourcesConfigTime,
       "sfpsCPResourcesNeedFlood": sfpsCPResourcesNeedFlood,
       "sfpsCPResourcesNeedResolve": sfpsCPResourcesNeedResolve,
       "sfpsCPResourcesNeedDiscover": sfpsCPResourcesNeedDiscover,
       "sfpsCPResourcesDiscoverAll": sfpsCPResourcesDiscoverAll,
       "sfpsCPResourcesNeedProxyOut": sfpsCPResourcesNeedProxyOut,
       "sfpsCPResourcesNeedProxyIn": sfpsCPResourcesNeedProxyIn,
       "sfpsCPResourcesNeedFilter": sfpsCPResourcesNeedFilter,
       "sfpsCPResourcesAcceptRate": sfpsCPResourcesAcceptRate,
       "sfpsCPResourcesTotalRate": sfpsCPResourcesTotalRate,
       "sfpsCPResourcesSingleFlood": sfpsCPResourcesSingleFlood,
       "sfpsCPResourcesNeedValidNet": sfpsCPResourcesNeedValidNet,
       "sfpsCPResourcesInvalidNetDrops": sfpsCPResourcesInvalidNetDrops,
       "sfpsCPResourcesPersistMask": sfpsCPResourcesPersistMask,
       "sfpsCPResourcesAPI": sfpsCPResourcesAPI,
       "sfpsCPResourcesAPIID": sfpsCPResourcesAPIID,
       "sfpsCPResourcesAPIAdminStatus": sfpsCPResourcesAPIAdminStatus,
       "sfpsCPResourcesAPIAttribute": sfpsCPResourcesAPIAttribute,
       "sfpsCPResourcesAPIScope": sfpsCPResourcesAPIScope,
       "sfpsCPResourcesAPIPersistance": sfpsCPResourcesAPIPersistance,
       "sfpsCPResourcesAPIVerb": sfpsCPResourcesAPIVerb,
       "sfpsServiceCenterFacilityTable": sfpsServiceCenterFacilityTable,
       "sfpsServiceCenterFacilityEntry": sfpsServiceCenterFacilityEntry,
       "sfpsServiceCenterFacilityHashLeaf": sfpsServiceCenterFacilityHashLeaf,
       "sfpsServiceCenterFacilityMetric": sfpsServiceCenterFacilityMetric,
       "sfpsServiceCenterFacilityName": sfpsServiceCenterFacilityName,
       "sfpsServiceCenterFacilityOperStatus": sfpsServiceCenterFacilityOperStatus,
       "sfpsServiceCenterFacilityAdminStatus": sfpsServiceCenterFacilityAdminStatus,
       "sfpsServiceCenterFacilityStatusTime": sfpsServiceCenterFacilityStatusTime,
       "sfpsServiceCenterFacilityRequests": sfpsServiceCenterFacilityRequests,
       "sfpsServiceCenterFacilityReply": sfpsServiceCenterFacilityReply,
       "sfpsCSPControlTable": sfpsCSPControlTable,
       "sfpsCSPControlTableEntry": sfpsCSPControlTableEntry,
       "sfpsCSPControlTableIndex": sfpsCSPControlTableIndex,
       "sfpsCSPControlTableCSPType": sfpsCSPControlTableCSPType,
       "sfpsCSPControlTableCSPName": sfpsCSPControlTableCSPName,
       "sfpsCSPControlTableAdminStatus": sfpsCSPControlTableAdminStatus,
       "sfpsCSPControlTableSwitchToCallProc": sfpsCSPControlTableSwitchToCallProc,
       "sfpsCSPControlTablePktsProcessed": sfpsCSPControlTablePktsProcessed,
       "sfpsCSPControlTablePktRate": sfpsCSPControlTablePktRate,
       "sfpsBlockSourceTable": sfpsBlockSourceTable,
       "sfpsBlockSourceEntry": sfpsBlockSourceEntry,
       "sfpsBlockSourceIndex": sfpsBlockSourceIndex,
       "sfpsBlockSourceMAC": sfpsBlockSourceMAC,
       "sfpsBlockSourceElapTimeShort": sfpsBlockSourceElapTimeShort,
       "sfpsBlockSourceNumCallsShort": sfpsBlockSourceNumCallsShort,
       "sfpsBlockSourceElapTimeLong": sfpsBlockSourceElapTimeLong,
       "sfpsBlockSourceNumCallLong": sfpsBlockSourceNumCallLong,
       "sfpsBlockSourceBlockFlag": sfpsBlockSourceBlockFlag,
       "sfpsBlockSourceUnBlockableFlag": sfpsBlockSourceUnBlockableFlag,
       "sfpsBlockSourceFilterPresent": sfpsBlockSourceFilterPresent,
       "sfpsBlockSourceNext": sfpsBlockSourceNext,
       "sfpsBlockSourceBlocksOnlyIndex": sfpsBlockSourceBlocksOnlyIndex,
       "sfpsBlockSourceOnlyTable": sfpsBlockSourceOnlyTable,
       "sfpsBlockSourceOnlyEntry": sfpsBlockSourceOnlyEntry,
       "sfpsBlockSourceOnlyIndex": sfpsBlockSourceOnlyIndex,
       "sfpsBlockSourceOnlyMAC": sfpsBlockSourceOnlyMAC,
       "sfpsBlockSourceOnlyElapTimeShort": sfpsBlockSourceOnlyElapTimeShort,
       "sfpsBlockSourceOnlyNumCallsShort": sfpsBlockSourceOnlyNumCallsShort,
       "sfpsBlockSourceOnlyElapTimeLong": sfpsBlockSourceOnlyElapTimeLong,
       "sfpsBlockSourceOnlyNumCallLong": sfpsBlockSourceOnlyNumCallLong,
       "sfpsBlockSourceOnlyBlockFlag": sfpsBlockSourceOnlyBlockFlag,
       "sfpsBlockSourceOnlyUnBlockableFlag": sfpsBlockSourceOnlyUnBlockableFlag,
       "sfpsBlockSourceOnlyFilterPresent": sfpsBlockSourceOnlyFilterPresent,
       "sfpsBlockSourceOnlyNext": sfpsBlockSourceOnlyNext,
       "sfpsBlockSourceOnlyBlocksOnlyIndex": sfpsBlockSourceOnlyBlocksOnlyIndex,
       "sfpsBlockSourcePortTable": sfpsBlockSourcePortTable,
       "sfpsBlockSourcePortEntry": sfpsBlockSourcePortEntry,
       "sfpsBlockSourcePortPort": sfpsBlockSourcePortPort,
       "sfpsBlockSourcePortBlockability": sfpsBlockSourcePortBlockability,
       "sfpsBlockSourceAPIVerb": sfpsBlockSourceAPIVerb,
       "sfpsBlockSourceAPIInputValue": sfpsBlockSourceAPIInputValue,
       "sfpsBlockSourceAPIPort": sfpsBlockSourceAPIPort,
       "sfpsBlockSourceAPIMAC": sfpsBlockSourceAPIMAC,
       "sfpsBlockSourceAPIBlockStatus": sfpsBlockSourceAPIBlockStatus,
       "sfpsBlockSourceAPIShortThreshold": sfpsBlockSourceAPIShortThreshold,
       "sfpsBlockSourceAPIShortPeriod": sfpsBlockSourceAPIShortPeriod,
       "sfpsBlockSourceAPILongThreshold": sfpsBlockSourceAPILongThreshold,
       "sfpsBlockSourceAPILongPeriod": sfpsBlockSourceAPILongPeriod,
       "sfpsBlockSourceAPIReapUserCnxs": sfpsBlockSourceAPIReapUserCnxs,
       "sfpsBlockSourceExcludeTable": sfpsBlockSourceExcludeTable,
       "sfpsBlockSourceExcludeEntry": sfpsBlockSourceExcludeEntry,
       "sfpsBlockSourceExcludeIndex": sfpsBlockSourceExcludeIndex,
       "sfpsBlockSourceExcludeMAC": sfpsBlockSourceExcludeMAC,
       "sfpsBlockSourceExcludeElapTimeShort": sfpsBlockSourceExcludeElapTimeShort,
       "sfpsBlockSourceExcludeNumCallsShort": sfpsBlockSourceExcludeNumCallsShort,
       "sfpsBlockSourceExcludeElapTimeLong": sfpsBlockSourceExcludeElapTimeLong,
       "sfpsBlockSourceExcludeNumCallLong": sfpsBlockSourceExcludeNumCallLong,
       "sfpsBlockSourceExcludeBlockFlag": sfpsBlockSourceExcludeBlockFlag,
       "sfpsBlockSourceExcludeUnBlockableFlag": sfpsBlockSourceExcludeUnBlockableFlag,
       "sfpsBlockSourceExcludeFilterPresent": sfpsBlockSourceExcludeFilterPresent,
       "sfpsBlockSourceExcludeNext": sfpsBlockSourceExcludeNext,
       "sfpsBlockSourceExcludeBlockSourceOnlyIndex": sfpsBlockSourceExcludeBlockSourceOnlyIndex,
       "sfpsBlockSourceStatsNumBlocks": sfpsBlockSourceStatsNumBlocks,
       "sfpsBlockSourceStatsNumCollisions": sfpsBlockSourceStatsNumCollisions,
       "sfpsBlockSourceStatsLongestChain": sfpsBlockSourceStatsLongestChain,
       "sfpsBlockSourceStatsNumEntries": sfpsBlockSourceStatsNumEntries,
       "sfpsBlockSourceStatsMaxNumEntries": sfpsBlockSourceStatsMaxNumEntries,
       "sfpsBlockSourceStatsSizeOfObj": sfpsBlockSourceStatsSizeOfObj,
       "sfpsBlockSourceStatsHashModValue": sfpsBlockSourceStatsHashModValue,
       "sfpsBlockSourceStatsHashSlotsSize": sfpsBlockSourceStatsHashSlotsSize,
       "sfpsBlockSourceStatsTableSize": sfpsBlockSourceStatsTableSize,
       "sfpsBlockSourceStatsBlockSourceOnlySize": sfpsBlockSourceStatsBlockSourceOnlySize,
       "sfpsBlockSourceStatsUnblockableSize": sfpsBlockSourceStatsUnblockableSize,
       "sfpsBlockSourceStatsPortMaskSize": sfpsBlockSourceStatsPortMaskSize,
       "sfpsBlockSourceStatsTotalHeapBytes": sfpsBlockSourceStatsTotalHeapBytes,
       "sfpsDHCPServerVLANName": sfpsDHCPServerVLANName,
       "sfpsDHCPServerVLANSingleFloodStatus": sfpsDHCPServerVLANSingleFloodStatus,
       "sfpsDHCPServerVLANVersion": sfpsDHCPServerVLANVersion,
       "sfpsATalkAMRVLANControlName": sfpsATalkAMRVLANControlName,
       "sfpsATalkAMRVLANControlVersion": sfpsATalkAMRVLANControlVersion}
)
