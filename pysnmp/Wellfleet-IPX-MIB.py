# SNMP MIB module (Wellfleet-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:31 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfIpxGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpxGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpxBase_ObjectIdentity = ObjectIdentity
wfIpxBase = _WfIpxBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1)
)


class _WfIpxBaseDelete_Type(Integer32):
    """Custom type wfIpxBaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxBaseDelete_Type.__name__ = "Integer32"
_WfIpxBaseDelete_Object = MibScalar
wfIpxBaseDelete = _WfIpxBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 1),
    _WfIpxBaseDelete_Type()
)
wfIpxBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseDelete.setStatus("deprecated")


class _WfIpxBaseDisable_Type(Integer32):
    """Custom type wfIpxBaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxBaseDisable_Type.__name__ = "Integer32"
_WfIpxBaseDisable_Object = MibScalar
wfIpxBaseDisable = _WfIpxBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 2),
    _WfIpxBaseDisable_Type()
)
wfIpxBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseDisable.setStatus("deprecated")


class _WfIpxBaseState_Type(Integer32):
    """Custom type wfIpxBaseState based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("in", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxBaseState_Type.__name__ = "Integer32"
_WfIpxBaseState_Object = MibScalar
wfIpxBaseState = _WfIpxBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 3),
    _WfIpxBaseState_Type()
)
wfIpxBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseState.setStatus("deprecated")
_WfIpxBaseCfgHostNumber_Type = OctetString
_WfIpxBaseCfgHostNumber_Object = MibScalar
wfIpxBaseCfgHostNumber = _WfIpxBaseCfgHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 4),
    _WfIpxBaseCfgHostNumber_Type()
)
wfIpxBaseCfgHostNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseCfgHostNumber.setStatus("deprecated")
_WfIpxBaseActiveHostNumber_Type = OctetString
_WfIpxBaseActiveHostNumber_Object = MibScalar
wfIpxBaseActiveHostNumber = _WfIpxBaseActiveHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 5),
    _WfIpxBaseActiveHostNumber_Type()
)
wfIpxBaseActiveHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseActiveHostNumber.setStatus("deprecated")
_WfIpxBaseNetCount_Type = Counter32
_WfIpxBaseNetCount_Object = MibScalar
wfIpxBaseNetCount = _WfIpxBaseNetCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 6),
    _WfIpxBaseNetCount_Type()
)
wfIpxBaseNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseNetCount.setStatus("deprecated")
_WfIpxBaseServiceCount_Type = Counter32
_WfIpxBaseServiceCount_Object = MibScalar
wfIpxBaseServiceCount = _WfIpxBaseServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 7),
    _WfIpxBaseServiceCount_Type()
)
wfIpxBaseServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseServiceCount.setStatus("deprecated")


class _WfIpxBaseLogFilter_Type(Integer32):
    """Custom type wfIpxBaseLogFilter based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("debug", 1),
          ("debuginfo", 3),
          ("debuginfotrace", 19),
          ("debugtrace", 17),
          ("info", 2),
          ("infotrace", 18),
          ("trace", 16))
    )


_WfIpxBaseLogFilter_Type.__name__ = "Integer32"
_WfIpxBaseLogFilter_Object = MibScalar
wfIpxBaseLogFilter = _WfIpxBaseLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 8),
    _WfIpxBaseLogFilter_Type()
)
wfIpxBaseLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseLogFilter.setStatus("deprecated")
_WfIpxBaseNetTblSize_Type = Integer32
_WfIpxBaseNetTblSize_Object = MibScalar
wfIpxBaseNetTblSize = _WfIpxBaseNetTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 9),
    _WfIpxBaseNetTblSize_Type()
)
wfIpxBaseNetTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseNetTblSize.setStatus("deprecated")
_WfIpxBaseRouterName_Type = DisplayString
_WfIpxBaseRouterName_Object = MibScalar
wfIpxBaseRouterName = _WfIpxBaseRouterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 10),
    _WfIpxBaseRouterName_Type()
)
wfIpxBaseRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseRouterName.setStatus("deprecated")
_WfIpxBasePrimaryNetNumber_Type = OctetString
_WfIpxBasePrimaryNetNumber_Object = MibScalar
wfIpxBasePrimaryNetNumber = _WfIpxBasePrimaryNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 11),
    _WfIpxBasePrimaryNetNumber_Type()
)
wfIpxBasePrimaryNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBasePrimaryNetNumber.setStatus("deprecated")


class _WfIpxBaseRipMethod_Type(Integer32):
    """Custom type wfIpxBaseRipMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("metric", 1),
          ("tick", 2))
    )


_WfIpxBaseRipMethod_Type.__name__ = "Integer32"
_WfIpxBaseRipMethod_Object = MibScalar
wfIpxBaseRipMethod = _WfIpxBaseRipMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 12),
    _WfIpxBaseRipMethod_Type()
)
wfIpxBaseRipMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseRipMethod.setStatus("deprecated")


class _WfIpxBaseMaximumPath_Type(Integer32):
    """Custom type wfIpxBaseMaximumPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfIpxBaseMaximumPath_Type.__name__ = "Integer32"
_WfIpxBaseMaximumPath_Object = MibScalar
wfIpxBaseMaximumPath = _WfIpxBaseMaximumPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 13),
    _WfIpxBaseMaximumPath_Type()
)
wfIpxBaseMaximumPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseMaximumPath.setStatus("deprecated")
_WfIpxBaseHostCount_Type = Counter32
_WfIpxBaseHostCount_Object = MibScalar
wfIpxBaseHostCount = _WfIpxBaseHostCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 14),
    _WfIpxBaseHostCount_Type()
)
wfIpxBaseHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseHostCount.setStatus("deprecated")


class _WfIpxBaseMultipleHostAddrs_Type(Integer32):
    """Custom type wfIpxBaseMultipleHostAddrs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxBaseMultipleHostAddrs_Type.__name__ = "Integer32"
_WfIpxBaseMultipleHostAddrs_Object = MibScalar
wfIpxBaseMultipleHostAddrs = _WfIpxBaseMultipleHostAddrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 15),
    _WfIpxBaseMultipleHostAddrs_Type()
)
wfIpxBaseMultipleHostAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseMultipleHostAddrs.setStatus("deprecated")


class _WfIpxBaseNovellCertificationConformance_Type(Integer32):
    """Custom type wfIpxBaseNovellCertificationConformance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxBaseNovellCertificationConformance_Type.__name__ = "Integer32"
_WfIpxBaseNovellCertificationConformance_Object = MibScalar
wfIpxBaseNovellCertificationConformance = _WfIpxBaseNovellCertificationConformance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 16),
    _WfIpxBaseNovellCertificationConformance_Type()
)
wfIpxBaseNovellCertificationConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseNovellCertificationConformance.setStatus("deprecated")


class _WfIpxBaseTrigUpdateEn_Type(Integer32):
    """Custom type wfIpxBaseTrigUpdateEn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxBaseTrigUpdateEn_Type.__name__ = "Integer32"
_WfIpxBaseTrigUpdateEn_Object = MibScalar
wfIpxBaseTrigUpdateEn = _WfIpxBaseTrigUpdateEn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 17),
    _WfIpxBaseTrigUpdateEn_Type()
)
wfIpxBaseTrigUpdateEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseTrigUpdateEn.setStatus("deprecated")


class _WfIpxBaseNetSizeBoundEn_Type(Integer32):
    """Custom type wfIpxBaseNetSizeBoundEn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxBaseNetSizeBoundEn_Type.__name__ = "Integer32"
_WfIpxBaseNetSizeBoundEn_Object = MibScalar
wfIpxBaseNetSizeBoundEn = _WfIpxBaseNetSizeBoundEn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 18),
    _WfIpxBaseNetSizeBoundEn_Type()
)
wfIpxBaseNetSizeBoundEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseNetSizeBoundEn.setStatus("deprecated")
_WfIpxBaseMaxNetTblSize_Type = Integer32
_WfIpxBaseMaxNetTblSize_Object = MibScalar
wfIpxBaseMaxNetTblSize = _WfIpxBaseMaxNetTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 19),
    _WfIpxBaseMaxNetTblSize_Type()
)
wfIpxBaseMaxNetTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseMaxNetTblSize.setStatus("deprecated")


class _WfIpxBaseNetTblFillNotify_Type(Integer32):
    """Custom type wfIpxBaseNetTblFillNotify based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfIpxBaseNetTblFillNotify_Type.__name__ = "Integer32"
_WfIpxBaseNetTblFillNotify_Object = MibScalar
wfIpxBaseNetTblFillNotify = _WfIpxBaseNetTblFillNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 20),
    _WfIpxBaseNetTblFillNotify_Type()
)
wfIpxBaseNetTblFillNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseNetTblFillNotify.setStatus("deprecated")
_WfIpxBaseRtEntryTable_Object = MibTable
wfIpxBaseRtEntryTable = _WfIpxBaseRtEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2)
)
if mibBuilder.loadTexts:
    wfIpxBaseRtEntryTable.setStatus("obsolete")
_WfIpxBaseRtEntry_Object = MibTableRow
wfIpxBaseRtEntry = _WfIpxBaseRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1)
)
wfIpxBaseRtEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxBaseRouteDest"),
)
if mibBuilder.loadTexts:
    wfIpxBaseRtEntry.setStatus("obsolete")


class _WfIpxBaseRouteDest_Type(OctetString):
    """Custom type wfIpxBaseRouteDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxBaseRouteDest_Type.__name__ = "OctetString"
_WfIpxBaseRouteDest_Object = MibTableColumn
wfIpxBaseRouteDest = _WfIpxBaseRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 1),
    _WfIpxBaseRouteDest_Type()
)
wfIpxBaseRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteDest.setStatus("obsolete")
_WfIpxBaseRouteIfIndex_Type = Integer32
_WfIpxBaseRouteIfIndex_Object = MibTableColumn
wfIpxBaseRouteIfIndex = _WfIpxBaseRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 2),
    _WfIpxBaseRouteIfIndex_Type()
)
wfIpxBaseRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteIfIndex.setStatus("obsolete")
_WfIpxBaseRouteMetric_Type = Integer32
_WfIpxBaseRouteMetric_Object = MibTableColumn
wfIpxBaseRouteMetric = _WfIpxBaseRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 3),
    _WfIpxBaseRouteMetric_Type()
)
wfIpxBaseRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteMetric.setStatus("obsolete")
_WfIpxBaseRouteNextHopNetwork_Type = OctetString
_WfIpxBaseRouteNextHopNetwork_Object = MibTableColumn
wfIpxBaseRouteNextHopNetwork = _WfIpxBaseRouteNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 4),
    _WfIpxBaseRouteNextHopNetwork_Type()
)
wfIpxBaseRouteNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteNextHopNetwork.setStatus("obsolete")
_WfIpxBaseRouteNextHopHost_Type = OctetString
_WfIpxBaseRouteNextHopHost_Object = MibTableColumn
wfIpxBaseRouteNextHopHost = _WfIpxBaseRouteNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 5),
    _WfIpxBaseRouteNextHopHost_Type()
)
wfIpxBaseRouteNextHopHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteNextHopHost.setStatus("obsolete")


class _WfIpxBaseRouteType_Type(Integer32):
    """Custom type wfIpxBaseRouteType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1),
          ("static", 5))
    )


_WfIpxBaseRouteType_Type.__name__ = "Integer32"
_WfIpxBaseRouteType_Object = MibTableColumn
wfIpxBaseRouteType = _WfIpxBaseRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 6),
    _WfIpxBaseRouteType_Type()
)
wfIpxBaseRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteType.setStatus("obsolete")


class _WfIpxBaseRouteProto_Type(Integer32):
    """Custom type wfIpxBaseRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("netmgmt", 3),
          ("other", 1),
          ("rip", 4))
    )


_WfIpxBaseRouteProto_Type.__name__ = "Integer32"
_WfIpxBaseRouteProto_Object = MibTableColumn
wfIpxBaseRouteProto = _WfIpxBaseRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 7),
    _WfIpxBaseRouteProto_Type()
)
wfIpxBaseRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteProto.setStatus("obsolete")
_WfIpxBaseRouteAge_Type = Integer32
_WfIpxBaseRouteAge_Object = MibTableColumn
wfIpxBaseRouteAge = _WfIpxBaseRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 8),
    _WfIpxBaseRouteAge_Type()
)
wfIpxBaseRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteAge.setStatus("obsolete")
_WfIpxBaseRouteInfo_Type = OctetString
_WfIpxBaseRouteInfo_Object = MibTableColumn
wfIpxBaseRouteInfo = _WfIpxBaseRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 9),
    _WfIpxBaseRouteInfo_Type()
)
wfIpxBaseRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteInfo.setStatus("obsolete")
_WfIpxBaseSapEntryTable_Object = MibTable
wfIpxBaseSapEntryTable = _WfIpxBaseSapEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3)
)
if mibBuilder.loadTexts:
    wfIpxBaseSapEntryTable.setStatus("obsolete")
_WfIpxBaseSapEntry_Object = MibTableRow
wfIpxBaseSapEntry = _WfIpxBaseSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1)
)
wfIpxBaseSapEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxBaseSapIndex"),
)
if mibBuilder.loadTexts:
    wfIpxBaseSapEntry.setStatus("obsolete")
_WfIpxBaseSapType_Type = OctetString
_WfIpxBaseSapType_Object = MibTableColumn
wfIpxBaseSapType = _WfIpxBaseSapType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 1),
    _WfIpxBaseSapType_Type()
)
wfIpxBaseSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapType.setStatus("obsolete")
_WfIpxBaseSapNetwork_Type = OctetString
_WfIpxBaseSapNetwork_Object = MibTableColumn
wfIpxBaseSapNetwork = _WfIpxBaseSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 2),
    _WfIpxBaseSapNetwork_Type()
)
wfIpxBaseSapNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapNetwork.setStatus("obsolete")
_WfIpxBaseSapHost_Type = OctetString
_WfIpxBaseSapHost_Object = MibTableColumn
wfIpxBaseSapHost = _WfIpxBaseSapHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 3),
    _WfIpxBaseSapHost_Type()
)
wfIpxBaseSapHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapHost.setStatus("obsolete")
_WfIpxBaseSapSocket_Type = OctetString
_WfIpxBaseSapSocket_Object = MibTableColumn
wfIpxBaseSapSocket = _WfIpxBaseSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 4),
    _WfIpxBaseSapSocket_Type()
)
wfIpxBaseSapSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapSocket.setStatus("obsolete")
_WfIpxBaseSapName_Type = DisplayString
_WfIpxBaseSapName_Object = MibTableColumn
wfIpxBaseSapName = _WfIpxBaseSapName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 5),
    _WfIpxBaseSapName_Type()
)
wfIpxBaseSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapName.setStatus("obsolete")
_WfIpxBaseSapAge_Type = Integer32
_WfIpxBaseSapAge_Object = MibTableColumn
wfIpxBaseSapAge = _WfIpxBaseSapAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 6),
    _WfIpxBaseSapAge_Type()
)
wfIpxBaseSapAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapAge.setStatus("obsolete")
_WfIpxBaseSapHops_Type = Integer32
_WfIpxBaseSapHops_Object = MibTableColumn
wfIpxBaseSapHops = _WfIpxBaseSapHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 7),
    _WfIpxBaseSapHops_Type()
)
wfIpxBaseSapHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapHops.setStatus("obsolete")


class _WfIpxBaseSapIndex_Type(OctetString):
    """Custom type wfIpxBaseSapIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_WfIpxBaseSapIndex_Type.__name__ = "OctetString"
_WfIpxBaseSapIndex_Object = MibTableColumn
wfIpxBaseSapIndex = _WfIpxBaseSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 8),
    _WfIpxBaseSapIndex_Type()
)
wfIpxBaseSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapIndex.setStatus("obsolete")
_WfIpxBaseSapIntf_Type = OctetString
_WfIpxBaseSapIntf_Object = MibTableColumn
wfIpxBaseSapIntf = _WfIpxBaseSapIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 9),
    _WfIpxBaseSapIntf_Type()
)
wfIpxBaseSapIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapIntf.setStatus("obsolete")
_WfIpxInterfaceTable_Object = MibTable
wfIpxInterfaceTable = _WfIpxInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4)
)
if mibBuilder.loadTexts:
    wfIpxInterfaceTable.setStatus("deprecated")
_WfIpxInterfaceEntry_Object = MibTableRow
wfIpxInterfaceEntry = _WfIpxInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1)
)
wfIpxInterfaceEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxInterfaceNetworkNumber"),
    (0, "Wellfleet-IPX-MIB", "wfIpxInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfIpxInterfaceEntry.setStatus("deprecated")
_WfIpxInterfaceIndex_Type = Integer32
_WfIpxInterfaceIndex_Object = MibTableColumn
wfIpxInterfaceIndex = _WfIpxInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 1),
    _WfIpxInterfaceIndex_Type()
)
wfIpxInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceIndex.setStatus("deprecated")


class _WfIpxInterfaceDelete_Type(Integer32):
    """Custom type wfIpxInterfaceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxInterfaceDelete_Type.__name__ = "Integer32"
_WfIpxInterfaceDelete_Object = MibTableColumn
wfIpxInterfaceDelete = _WfIpxInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 2),
    _WfIpxInterfaceDelete_Type()
)
wfIpxInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceDelete.setStatus("deprecated")


class _WfIpxInterfaceDisable_Type(Integer32):
    """Custom type wfIpxInterfaceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceDisable_Type.__name__ = "Integer32"
_WfIpxInterfaceDisable_Object = MibTableColumn
wfIpxInterfaceDisable = _WfIpxInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 3),
    _WfIpxInterfaceDisable_Type()
)
wfIpxInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceDisable.setStatus("deprecated")


class _WfIpxInterfaceState_Type(Integer32):
    """Custom type wfIpxInterfaceState based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxInterfaceState_Type.__name__ = "Integer32"
_WfIpxInterfaceState_Object = MibTableColumn
wfIpxInterfaceState = _WfIpxInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 4),
    _WfIpxInterfaceState_Type()
)
wfIpxInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceState.setStatus("deprecated")
_WfIpxInterfaceCircuit_Type = Integer32
_WfIpxInterfaceCircuit_Object = MibTableColumn
wfIpxInterfaceCircuit = _WfIpxInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 5),
    _WfIpxInterfaceCircuit_Type()
)
wfIpxInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceCircuit.setStatus("deprecated")


class _WfIpxInterfaceNetworkNumber_Type(OctetString):
    """Custom type wfIpxInterfaceNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxInterfaceNetworkNumber_Type.__name__ = "OctetString"
_WfIpxInterfaceNetworkNumber_Object = MibTableColumn
wfIpxInterfaceNetworkNumber = _WfIpxInterfaceNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 6),
    _WfIpxInterfaceNetworkNumber_Type()
)
wfIpxInterfaceNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceNetworkNumber.setStatus("deprecated")


class _WfIpxInterfaceCost_Type(Integer32):
    """Custom type wfIpxInterfaceCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cost", 1)
    )


_WfIpxInterfaceCost_Type.__name__ = "Integer32"
_WfIpxInterfaceCost_Object = MibTableColumn
wfIpxInterfaceCost = _WfIpxInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 7),
    _WfIpxInterfaceCost_Type()
)
wfIpxInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceCost.setStatus("deprecated")


class _WfIpxInterfaceXsumOn_Type(Integer32):
    """Custom type wfIpxInterfaceXsumOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceXsumOn_Type.__name__ = "Integer32"
_WfIpxInterfaceXsumOn_Object = MibTableColumn
wfIpxInterfaceXsumOn = _WfIpxInterfaceXsumOn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 8),
    _WfIpxInterfaceXsumOn_Type()
)
wfIpxInterfaceXsumOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceXsumOn.setStatus("deprecated")


class _WfIpxInterfaceCfgEncaps_Type(Integer32):
    """Custom type wfIpxInterfaceCfgEncaps based on Integer32"""
    defaultValue = 1

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
        *(("ethernet", 1),
          ("lsap", 2),
          ("novell", 3),
          ("ppp", 5),
          ("snap", 4))
    )


_WfIpxInterfaceCfgEncaps_Type.__name__ = "Integer32"
_WfIpxInterfaceCfgEncaps_Object = MibTableColumn
wfIpxInterfaceCfgEncaps = _WfIpxInterfaceCfgEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 9),
    _WfIpxInterfaceCfgEncaps_Type()
)
wfIpxInterfaceCfgEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceCfgEncaps.setStatus("deprecated")
_WfIpxInterfaceMacAddress_Type = OctetString
_WfIpxInterfaceMacAddress_Object = MibTableColumn
wfIpxInterfaceMacAddress = _WfIpxInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 10),
    _WfIpxInterfaceMacAddress_Type()
)
wfIpxInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceMacAddress.setStatus("deprecated")
_WfIpxInterfaceSMDSGroupAddress_Type = OctetString
_WfIpxInterfaceSMDSGroupAddress_Object = MibTableColumn
wfIpxInterfaceSMDSGroupAddress = _WfIpxInterfaceSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 11),
    _WfIpxInterfaceSMDSGroupAddress_Type()
)
wfIpxInterfaceSMDSGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceSMDSGroupAddress.setStatus("deprecated")
_WfIpxInterfaceMaxInfo_Type = Integer32
_WfIpxInterfaceMaxInfo_Object = MibTableColumn
wfIpxInterfaceMaxInfo = _WfIpxInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 12),
    _WfIpxInterfaceMaxInfo_Type()
)
wfIpxInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceMaxInfo.setStatus("deprecated")
_WfIpxInterfaceInReceives_Type = Counter32
_WfIpxInterfaceInReceives_Object = MibTableColumn
wfIpxInterfaceInReceives = _WfIpxInterfaceInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 13),
    _WfIpxInterfaceInReceives_Type()
)
wfIpxInterfaceInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInReceives.setStatus("deprecated")
_WfIpxInterfaceInHdrErrors_Type = Counter32
_WfIpxInterfaceInHdrErrors_Object = MibTableColumn
wfIpxInterfaceInHdrErrors = _WfIpxInterfaceInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 14),
    _WfIpxInterfaceInHdrErrors_Type()
)
wfIpxInterfaceInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInHdrErrors.setStatus("deprecated")
_WfIpxInterfaceInAddrErrors_Type = Counter32
_WfIpxInterfaceInAddrErrors_Object = MibTableColumn
wfIpxInterfaceInAddrErrors = _WfIpxInterfaceInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 15),
    _WfIpxInterfaceInAddrErrors_Type()
)
wfIpxInterfaceInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInAddrErrors.setStatus("deprecated")
_WfIpxInterfaceForwDatagrams_Type = Counter32
_WfIpxInterfaceForwDatagrams_Object = MibTableColumn
wfIpxInterfaceForwDatagrams = _WfIpxInterfaceForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 16),
    _WfIpxInterfaceForwDatagrams_Type()
)
wfIpxInterfaceForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceForwDatagrams.setStatus("deprecated")
_WfIpxInterfaceInUnknownProtos_Type = Counter32
_WfIpxInterfaceInUnknownProtos_Object = MibTableColumn
wfIpxInterfaceInUnknownProtos = _WfIpxInterfaceInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 17),
    _WfIpxInterfaceInUnknownProtos_Type()
)
wfIpxInterfaceInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInUnknownProtos.setStatus("deprecated")
_WfIpxInterfaceInDiscards_Type = Counter32
_WfIpxInterfaceInDiscards_Object = MibTableColumn
wfIpxInterfaceInDiscards = _WfIpxInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 18),
    _WfIpxInterfaceInDiscards_Type()
)
wfIpxInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInDiscards.setStatus("deprecated")
_WfIpxInterfaceInDelivers_Type = Counter32
_WfIpxInterfaceInDelivers_Object = MibTableColumn
wfIpxInterfaceInDelivers = _WfIpxInterfaceInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 19),
    _WfIpxInterfaceInDelivers_Type()
)
wfIpxInterfaceInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInDelivers.setStatus("deprecated")
_WfIpxInterfaceOutRequests_Type = Counter32
_WfIpxInterfaceOutRequests_Object = MibTableColumn
wfIpxInterfaceOutRequests = _WfIpxInterfaceOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 20),
    _WfIpxInterfaceOutRequests_Type()
)
wfIpxInterfaceOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceOutRequests.setStatus("deprecated")
_WfIpxInterfaceOutDiscards_Type = Counter32
_WfIpxInterfaceOutDiscards_Object = MibTableColumn
wfIpxInterfaceOutDiscards = _WfIpxInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 21),
    _WfIpxInterfaceOutDiscards_Type()
)
wfIpxInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceOutDiscards.setStatus("deprecated")
_WfIpxInterfaceOutNoRoutes_Type = Counter32
_WfIpxInterfaceOutNoRoutes_Object = MibTableColumn
wfIpxInterfaceOutNoRoutes = _WfIpxInterfaceOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 22),
    _WfIpxInterfaceOutNoRoutes_Type()
)
wfIpxInterfaceOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceOutNoRoutes.setStatus("deprecated")


class _WfIpxInterfaceTrEndStation_Type(Integer32):
    """Custom type wfIpxInterfaceTrEndStation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceTrEndStation_Type.__name__ = "Integer32"
_WfIpxInterfaceTrEndStation_Object = MibTableColumn
wfIpxInterfaceTrEndStation = _WfIpxInterfaceTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 23),
    _WfIpxInterfaceTrEndStation_Type()
)
wfIpxInterfaceTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceTrEndStation.setStatus("deprecated")


class _WfIpxInterfaceNetbiosAccept_Type(Integer32):
    """Custom type wfIpxInterfaceNetbiosAccept based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceNetbiosAccept_Type.__name__ = "Integer32"
_WfIpxInterfaceNetbiosAccept_Object = MibTableColumn
wfIpxInterfaceNetbiosAccept = _WfIpxInterfaceNetbiosAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 24),
    _WfIpxInterfaceNetbiosAccept_Type()
)
wfIpxInterfaceNetbiosAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceNetbiosAccept.setStatus("deprecated")


class _WfIpxInterfaceNetbiosDeliver_Type(Integer32):
    """Custom type wfIpxInterfaceNetbiosDeliver based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceNetbiosDeliver_Type.__name__ = "Integer32"
_WfIpxInterfaceNetbiosDeliver_Object = MibTableColumn
wfIpxInterfaceNetbiosDeliver = _WfIpxInterfaceNetbiosDeliver_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 25),
    _WfIpxInterfaceNetbiosDeliver_Type()
)
wfIpxInterfaceNetbiosDeliver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceNetbiosDeliver.setStatus("deprecated")


class _WfIpxInterfaceWanSapPeriod_Type(Integer32):
    """Custom type wfIpxInterfaceWanSapPeriod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("default", 2)
    )


_WfIpxInterfaceWanSapPeriod_Type.__name__ = "Integer32"
_WfIpxInterfaceWanSapPeriod_Object = MibTableColumn
wfIpxInterfaceWanSapPeriod = _WfIpxInterfaceWanSapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 26),
    _WfIpxInterfaceWanSapPeriod_Type()
)
wfIpxInterfaceWanSapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceWanSapPeriod.setStatus("deprecated")
_WfIpxInterfaceFRBcast_Type = OctetString
_WfIpxInterfaceFRBcast_Object = MibTableColumn
wfIpxInterfaceFRBcast = _WfIpxInterfaceFRBcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 27),
    _WfIpxInterfaceFRBcast_Type()
)
wfIpxInterfaceFRBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceFRBcast.setStatus("deprecated")
_WfIpxInterfaceFRMcast_Type = OctetString
_WfIpxInterfaceFRMcast_Object = MibTableColumn
wfIpxInterfaceFRMcast = _WfIpxInterfaceFRMcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 28),
    _WfIpxInterfaceFRMcast_Type()
)
wfIpxInterfaceFRMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceFRMcast.setStatus("deprecated")


class _WfIpxInterfaceEncaps_Type(Integer32):
    """Custom type wfIpxInterfaceEncaps based on Integer32"""
    defaultValue = 1

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
        *(("ethernet", 1),
          ("lsap", 2),
          ("novell", 3),
          ("ppp", 5),
          ("snap", 4))
    )


_WfIpxInterfaceEncaps_Type.__name__ = "Integer32"
_WfIpxInterfaceEncaps_Object = MibTableColumn
wfIpxInterfaceEncaps = _WfIpxInterfaceEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 29),
    _WfIpxInterfaceEncaps_Type()
)
wfIpxInterfaceEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceEncaps.setStatus("deprecated")


class _WfIpxInterfaceSplit_Type(Integer32):
    """Custom type wfIpxInterfaceSplit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceSplit_Type.__name__ = "Integer32"
_WfIpxInterfaceSplit_Object = MibTableColumn
wfIpxInterfaceSplit = _WfIpxInterfaceSplit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 30),
    _WfIpxInterfaceSplit_Type()
)
wfIpxInterfaceSplit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceSplit.setStatus("deprecated")
_WfIpxInterfaceCacheHit_Type = Counter32
_WfIpxInterfaceCacheHit_Object = MibTableColumn
wfIpxInterfaceCacheHit = _WfIpxInterfaceCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 31),
    _WfIpxInterfaceCacheHit_Type()
)
wfIpxInterfaceCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceCacheHit.setStatus("deprecated")


class _WfIpxInterfaceIpxWanDisable_Type(Integer32):
    """Custom type wfIpxInterfaceIpxWanDisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceIpxWanDisable_Type.__name__ = "Integer32"
_WfIpxInterfaceIpxWanDisable_Object = MibTableColumn
wfIpxInterfaceIpxWanDisable = _WfIpxInterfaceIpxWanDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 32),
    _WfIpxInterfaceIpxWanDisable_Type()
)
wfIpxInterfaceIpxWanDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceIpxWanDisable.setStatus("deprecated")
_WfIpxInterfaceIpxWanCommonNet_Type = OctetString
_WfIpxInterfaceIpxWanCommonNet_Object = MibTableColumn
wfIpxInterfaceIpxWanCommonNet = _WfIpxInterfaceIpxWanCommonNet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 33),
    _WfIpxInterfaceIpxWanCommonNet_Type()
)
wfIpxInterfaceIpxWanCommonNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceIpxWanCommonNet.setStatus("deprecated")


class _WfIpxInterfaceIpxWanTimeOut_Type(Integer32):
    """Custom type wfIpxInterfaceIpxWanTimeOut based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            60
        )
    )
    namedValues = NamedValues(
        ("default", 60)
    )


_WfIpxInterfaceIpxWanTimeOut_Type.__name__ = "Integer32"
_WfIpxInterfaceIpxWanTimeOut_Object = MibTableColumn
wfIpxInterfaceIpxWanTimeOut = _WfIpxInterfaceIpxWanTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 34),
    _WfIpxInterfaceIpxWanTimeOut_Type()
)
wfIpxInterfaceIpxWanTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceIpxWanTimeOut.setStatus("deprecated")


class _WfIpxInterfaceIpxWanLinkRetry_Type(Integer32):
    """Custom type wfIpxInterfaceIpxWanLinkRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("default", 5)
    )


_WfIpxInterfaceIpxWanLinkRetry_Type.__name__ = "Integer32"
_WfIpxInterfaceIpxWanLinkRetry_Object = MibTableColumn
wfIpxInterfaceIpxWanLinkRetry = _WfIpxInterfaceIpxWanLinkRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 35),
    _WfIpxInterfaceIpxWanLinkRetry_Type()
)
wfIpxInterfaceIpxWanLinkRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceIpxWanLinkRetry.setStatus("deprecated")


class _WfIpxInterfaceWanRipPeriod_Type(Integer32):
    """Custom type wfIpxInterfaceWanRipPeriod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("default", 2)
    )


_WfIpxInterfaceWanRipPeriod_Type.__name__ = "Integer32"
_WfIpxInterfaceWanRipPeriod_Object = MibTableColumn
wfIpxInterfaceWanRipPeriod = _WfIpxInterfaceWanRipPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 36),
    _WfIpxInterfaceWanRipPeriod_Type()
)
wfIpxInterfaceWanRipPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceWanRipPeriod.setStatus("deprecated")
_WfIpxInterfaceCfgHostNumber_Type = OctetString
_WfIpxInterfaceCfgHostNumber_Object = MibTableColumn
wfIpxInterfaceCfgHostNumber = _WfIpxInterfaceCfgHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 37),
    _WfIpxInterfaceCfgHostNumber_Type()
)
wfIpxInterfaceCfgHostNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceCfgHostNumber.setStatus("deprecated")
_WfIpxInterfaceActiveHostNumber_Type = OctetString
_WfIpxInterfaceActiveHostNumber_Object = MibTableColumn
wfIpxInterfaceActiveHostNumber = _WfIpxInterfaceActiveHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 38),
    _WfIpxInterfaceActiveHostNumber_Type()
)
wfIpxInterfaceActiveHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceActiveHostNumber.setStatus("deprecated")
_WfIpxRipIntfTable_Object = MibTable
wfIpxRipIntfTable = _WfIpxRipIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5)
)
if mibBuilder.loadTexts:
    wfIpxRipIntfTable.setStatus("deprecated")
_WfIpxRipIntfEntry_Object = MibTableRow
wfIpxRipIntfEntry = _WfIpxRipIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1)
)
wfIpxRipIntfEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxRipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfIpxRipIntfEntry.setStatus("deprecated")


class _WfIpxRipInterfaceDelete_Type(Integer32):
    """Custom type wfIpxRipInterfaceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxRipInterfaceDelete_Type.__name__ = "Integer32"
_WfIpxRipInterfaceDelete_Object = MibTableColumn
wfIpxRipInterfaceDelete = _WfIpxRipInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 1),
    _WfIpxRipInterfaceDelete_Type()
)
wfIpxRipInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceDelete.setStatus("deprecated")


class _WfIpxRipInterfaceDisable_Type(Integer32):
    """Custom type wfIpxRipInterfaceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxRipInterfaceDisable_Type.__name__ = "Integer32"
_WfIpxRipInterfaceDisable_Object = MibTableColumn
wfIpxRipInterfaceDisable = _WfIpxRipInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 2),
    _WfIpxRipInterfaceDisable_Type()
)
wfIpxRipInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceDisable.setStatus("deprecated")


class _WfIpxRipInterfaceState_Type(Integer32):
    """Custom type wfIpxRipInterfaceState based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxRipInterfaceState_Type.__name__ = "Integer32"
_WfIpxRipInterfaceState_Object = MibTableColumn
wfIpxRipInterfaceState = _WfIpxRipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 3),
    _WfIpxRipInterfaceState_Type()
)
wfIpxRipInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceState.setStatus("deprecated")


class _WfIpxRipInterfaceIndex_Type(OctetString):
    """Custom type wfIpxRipInterfaceIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxRipInterfaceIndex_Type.__name__ = "OctetString"
_WfIpxRipInterfaceIndex_Object = MibTableColumn
wfIpxRipInterfaceIndex = _WfIpxRipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 4),
    _WfIpxRipInterfaceIndex_Type()
)
wfIpxRipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceIndex.setStatus("deprecated")


class _WfIpxRipInterfaceSupply_Type(Integer32):
    """Custom type wfIpxRipInterfaceSupply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxRipInterfaceSupply_Type.__name__ = "Integer32"
_WfIpxRipInterfaceSupply_Object = MibTableColumn
wfIpxRipInterfaceSupply = _WfIpxRipInterfaceSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 5),
    _WfIpxRipInterfaceSupply_Type()
)
wfIpxRipInterfaceSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceSupply.setStatus("deprecated")


class _WfIpxRipInterfaceListen_Type(Integer32):
    """Custom type wfIpxRipInterfaceListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxRipInterfaceListen_Type.__name__ = "Integer32"
_WfIpxRipInterfaceListen_Object = MibTableColumn
wfIpxRipInterfaceListen = _WfIpxRipInterfaceListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 6),
    _WfIpxRipInterfaceListen_Type()
)
wfIpxRipInterfaceListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceListen.setStatus("deprecated")
_WfIpxAdjacentHostTable_Object = MibTable
wfIpxAdjacentHostTable = _WfIpxAdjacentHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6)
)
if mibBuilder.loadTexts:
    wfIpxAdjacentHostTable.setStatus("deprecated")
_WfIpxAdjacentHostEntry_Object = MibTableRow
wfIpxAdjacentHostEntry = _WfIpxAdjacentHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1)
)
wfIpxAdjacentHostEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxAhTargHostNetwork"),
    (0, "Wellfleet-IPX-MIB", "wfIpxAhTargHostId"),
)
if mibBuilder.loadTexts:
    wfIpxAdjacentHostEntry.setStatus("deprecated")


class _WfIpxAhDelete_Type(Integer32):
    """Custom type wfIpxAhDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxAhDelete_Type.__name__ = "Integer32"
_WfIpxAhDelete_Object = MibTableColumn
wfIpxAhDelete = _WfIpxAhDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 1),
    _WfIpxAhDelete_Type()
)
wfIpxAhDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhDelete.setStatus("deprecated")


class _WfIpxAhDisable_Type(Integer32):
    """Custom type wfIpxAhDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxAhDisable_Type.__name__ = "Integer32"
_WfIpxAhDisable_Object = MibTableColumn
wfIpxAhDisable = _WfIpxAhDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 2),
    _WfIpxAhDisable_Type()
)
wfIpxAhDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhDisable.setStatus("deprecated")


class _WfIpxAhTargHostNetwork_Type(OctetString):
    """Custom type wfIpxAhTargHostNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxAhTargHostNetwork_Type.__name__ = "OctetString"
_WfIpxAhTargHostNetwork_Object = MibTableColumn
wfIpxAhTargHostNetwork = _WfIpxAhTargHostNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 3),
    _WfIpxAhTargHostNetwork_Type()
)
wfIpxAhTargHostNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAhTargHostNetwork.setStatus("deprecated")


class _WfIpxAhTargHostId_Type(OctetString):
    """Custom type wfIpxAhTargHostId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfIpxAhTargHostId_Type.__name__ = "OctetString"
_WfIpxAhTargHostId_Object = MibTableColumn
wfIpxAhTargHostId = _WfIpxAhTargHostId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 4),
    _WfIpxAhTargHostId_Type()
)
wfIpxAhTargHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAhTargHostId.setStatus("deprecated")
_WfIpxAhNextHopIntf_Type = OctetString
_WfIpxAhNextHopIntf_Object = MibTableColumn
wfIpxAhNextHopIntf = _WfIpxAhNextHopIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 5),
    _WfIpxAhNextHopIntf_Type()
)
wfIpxAhNextHopIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhNextHopIntf.setStatus("deprecated")
_WfIpxAhDlci_Type = OctetString
_WfIpxAhDlci_Object = MibTableColumn
wfIpxAhDlci = _WfIpxAhDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 6),
    _WfIpxAhDlci_Type()
)
wfIpxAhDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhDlci.setStatus("deprecated")
_WfIpxStaticRouteTable_Object = MibTable
wfIpxStaticRouteTable = _WfIpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7)
)
if mibBuilder.loadTexts:
    wfIpxStaticRouteTable.setStatus("deprecated")
_WfIpxStaticRouteEntry_Object = MibTableRow
wfIpxStaticRouteEntry = _WfIpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1)
)
wfIpxStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxSrTargNetwork"),
    (0, "Wellfleet-IPX-MIB", "wfIpxSrNextHopNetwork"),
)
if mibBuilder.loadTexts:
    wfIpxStaticRouteEntry.setStatus("deprecated")


class _WfIpxSrDelete_Type(Integer32):
    """Custom type wfIpxSrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxSrDelete_Type.__name__ = "Integer32"
_WfIpxSrDelete_Object = MibTableColumn
wfIpxSrDelete = _WfIpxSrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 1),
    _WfIpxSrDelete_Type()
)
wfIpxSrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrDelete.setStatus("deprecated")


class _WfIpxSrDisable_Type(Integer32):
    """Custom type wfIpxSrDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxSrDisable_Type.__name__ = "Integer32"
_WfIpxSrDisable_Object = MibTableColumn
wfIpxSrDisable = _WfIpxSrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 2),
    _WfIpxSrDisable_Type()
)
wfIpxSrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrDisable.setStatus("deprecated")


class _WfIpxSrTargNetwork_Type(OctetString):
    """Custom type wfIpxSrTargNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxSrTargNetwork_Type.__name__ = "OctetString"
_WfIpxSrTargNetwork_Object = MibTableColumn
wfIpxSrTargNetwork = _WfIpxSrTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 3),
    _WfIpxSrTargNetwork_Type()
)
wfIpxSrTargNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSrTargNetwork.setStatus("deprecated")
_WfIpxSrCost_Type = Integer32
_WfIpxSrCost_Object = MibTableColumn
wfIpxSrCost = _WfIpxSrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 4),
    _WfIpxSrCost_Type()
)
wfIpxSrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrCost.setStatus("deprecated")


class _WfIpxSrNextHopNetwork_Type(OctetString):
    """Custom type wfIpxSrNextHopNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxSrNextHopNetwork_Type.__name__ = "OctetString"
_WfIpxSrNextHopNetwork_Object = MibTableColumn
wfIpxSrNextHopNetwork = _WfIpxSrNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 5),
    _WfIpxSrNextHopNetwork_Type()
)
wfIpxSrNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSrNextHopNetwork.setStatus("deprecated")
_WfIpxSrNextHopHost_Type = OctetString
_WfIpxSrNextHopHost_Object = MibTableColumn
wfIpxSrNextHopHost = _WfIpxSrNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 6),
    _WfIpxSrNextHopHost_Type()
)
wfIpxSrNextHopHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrNextHopHost.setStatus("deprecated")
_WfIpxSrTargNetworkRt_Type = Integer32
_WfIpxSrTargNetworkRt_Object = MibTableColumn
wfIpxSrTargNetworkRt = _WfIpxSrTargNetworkRt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 7),
    _WfIpxSrTargNetworkRt_Type()
)
wfIpxSrTargNetworkRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSrTargNetworkRt.setStatus("deprecated")
_WfIpxSrTickCost_Type = OctetString
_WfIpxSrTickCost_Object = MibTableColumn
wfIpxSrTickCost = _WfIpxSrTickCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 8),
    _WfIpxSrTickCost_Type()
)
wfIpxSrTickCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrTickCost.setStatus("deprecated")
_WfIpxNetBiosStaticRouteTable_Object = MibTable
wfIpxNetBiosStaticRouteTable = _WfIpxNetBiosStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8)
)
if mibBuilder.loadTexts:
    wfIpxNetBiosStaticRouteTable.setStatus("deprecated")
_WfIpxNetBiosStaticRouteEntry_Object = MibTableRow
wfIpxNetBiosStaticRouteEntry = _WfIpxNetBiosStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1)
)
wfIpxNetBiosStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxNetBiosSrTargNetwork"),
    (0, "Wellfleet-IPX-MIB", "wfIpxNetBiosSrIntf"),
)
if mibBuilder.loadTexts:
    wfIpxNetBiosStaticRouteEntry.setStatus("deprecated")


class _WfIpxNetBiosSrDelete_Type(Integer32):
    """Custom type wfIpxNetBiosSrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxNetBiosSrDelete_Type.__name__ = "Integer32"
_WfIpxNetBiosSrDelete_Object = MibTableColumn
wfIpxNetBiosSrDelete = _WfIpxNetBiosSrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 1),
    _WfIpxNetBiosSrDelete_Type()
)
wfIpxNetBiosSrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrDelete.setStatus("deprecated")


class _WfIpxNetBiosSrDisable_Type(Integer32):
    """Custom type wfIpxNetBiosSrDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxNetBiosSrDisable_Type.__name__ = "Integer32"
_WfIpxNetBiosSrDisable_Object = MibTableColumn
wfIpxNetBiosSrDisable = _WfIpxNetBiosSrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 2),
    _WfIpxNetBiosSrDisable_Type()
)
wfIpxNetBiosSrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrDisable.setStatus("deprecated")


class _WfIpxNetBiosSrTargNetwork_Type(OctetString):
    """Custom type wfIpxNetBiosSrTargNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxNetBiosSrTargNetwork_Type.__name__ = "OctetString"
_WfIpxNetBiosSrTargNetwork_Object = MibTableColumn
wfIpxNetBiosSrTargNetwork = _WfIpxNetBiosSrTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 3),
    _WfIpxNetBiosSrTargNetwork_Type()
)
wfIpxNetBiosSrTargNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrTargNetwork.setStatus("deprecated")
_WfIpxNetBiosSrName_Type = DisplayString
_WfIpxNetBiosSrName_Object = MibTableColumn
wfIpxNetBiosSrName = _WfIpxNetBiosSrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 4),
    _WfIpxNetBiosSrName_Type()
)
wfIpxNetBiosSrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrName.setStatus("deprecated")


class _WfIpxNetBiosSrIntf_Type(OctetString):
    """Custom type wfIpxNetBiosSrIntf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxNetBiosSrIntf_Type.__name__ = "OctetString"
_WfIpxNetBiosSrIntf_Object = MibTableColumn
wfIpxNetBiosSrIntf = _WfIpxNetBiosSrIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 5),
    _WfIpxNetBiosSrIntf_Type()
)
wfIpxNetBiosSrIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrIntf.setStatus("deprecated")
_WfIpxNetBiosSrIndex_Type = Integer32
_WfIpxNetBiosSrIndex_Object = MibTableColumn
wfIpxNetBiosSrIndex = _WfIpxNetBiosSrIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 6),
    _WfIpxNetBiosSrIndex_Type()
)
wfIpxNetBiosSrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrIndex.setStatus("deprecated")
_WfIpxSapNetLvlFilterTable_Object = MibTable
wfIpxSapNetLvlFilterTable = _WfIpxSapNetLvlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9)
)
if mibBuilder.loadTexts:
    wfIpxSapNetLvlFilterTable.setStatus("deprecated")
_WfIpxSapNetLvlFilter_Object = MibTableRow
wfIpxSapNetLvlFilter = _WfIpxSapNetLvlFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1)
)
wfIpxSapNetLvlFilter.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxSapNetLvlIntf"),
    (0, "Wellfleet-IPX-MIB", "wfIpxSapNetLvlIndex"),
)
if mibBuilder.loadTexts:
    wfIpxSapNetLvlFilter.setStatus("deprecated")


class _WfIpxSapNetLvlDelete_Type(Integer32):
    """Custom type wfIpxSapNetLvlDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxSapNetLvlDelete_Type.__name__ = "Integer32"
_WfIpxSapNetLvlDelete_Object = MibTableColumn
wfIpxSapNetLvlDelete = _WfIpxSapNetLvlDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 1),
    _WfIpxSapNetLvlDelete_Type()
)
wfIpxSapNetLvlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlDelete.setStatus("deprecated")


class _WfIpxSapNetLvlDisable_Type(Integer32):
    """Custom type wfIpxSapNetLvlDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxSapNetLvlDisable_Type.__name__ = "Integer32"
_WfIpxSapNetLvlDisable_Object = MibTableColumn
wfIpxSapNetLvlDisable = _WfIpxSapNetLvlDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 2),
    _WfIpxSapNetLvlDisable_Type()
)
wfIpxSapNetLvlDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlDisable.setStatus("deprecated")
_WfIpxSapNetLvlTargNetwork_Type = OctetString
_WfIpxSapNetLvlTargNetwork_Object = MibTableColumn
wfIpxSapNetLvlTargNetwork = _WfIpxSapNetLvlTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 3),
    _WfIpxSapNetLvlTargNetwork_Type()
)
wfIpxSapNetLvlTargNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlTargNetwork.setStatus("deprecated")
_WfIpxSapNetLvlType_Type = OctetString
_WfIpxSapNetLvlType_Object = MibTableColumn
wfIpxSapNetLvlType = _WfIpxSapNetLvlType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 4),
    _WfIpxSapNetLvlType_Type()
)
wfIpxSapNetLvlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlType.setStatus("deprecated")


class _WfIpxSapNetLvlAction_Type(Integer32):
    """Custom type wfIpxSapNetLvlAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WfIpxSapNetLvlAction_Type.__name__ = "Integer32"
_WfIpxSapNetLvlAction_Object = MibTableColumn
wfIpxSapNetLvlAction = _WfIpxSapNetLvlAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 5),
    _WfIpxSapNetLvlAction_Type()
)
wfIpxSapNetLvlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlAction.setStatus("deprecated")


class _WfIpxSapNetLvlIntf_Type(OctetString):
    """Custom type wfIpxSapNetLvlIntf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxSapNetLvlIntf_Type.__name__ = "OctetString"
_WfIpxSapNetLvlIntf_Object = MibTableColumn
wfIpxSapNetLvlIntf = _WfIpxSapNetLvlIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 6),
    _WfIpxSapNetLvlIntf_Type()
)
wfIpxSapNetLvlIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlIntf.setStatus("deprecated")
_WfIpxSapNetLvlIndex_Type = Integer32
_WfIpxSapNetLvlIndex_Object = MibTableColumn
wfIpxSapNetLvlIndex = _WfIpxSapNetLvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 7),
    _WfIpxSapNetLvlIndex_Type()
)
wfIpxSapNetLvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlIndex.setStatus("deprecated")
_WfIpxSapServtLvlFilterTable_Object = MibTable
wfIpxSapServtLvlFilterTable = _WfIpxSapServtLvlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10)
)
if mibBuilder.loadTexts:
    wfIpxSapServtLvlFilterTable.setStatus("deprecated")
_WfIpxSapServLvlFilter_Object = MibTableRow
wfIpxSapServLvlFilter = _WfIpxSapServLvlFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1)
)
wfIpxSapServLvlFilter.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxSapServLvlIntf"),
    (0, "Wellfleet-IPX-MIB", "wfIpxSapServLvlIndex"),
)
if mibBuilder.loadTexts:
    wfIpxSapServLvlFilter.setStatus("deprecated")


class _WfIpxSapServLvlDelete_Type(Integer32):
    """Custom type wfIpxSapServLvlDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxSapServLvlDelete_Type.__name__ = "Integer32"
_WfIpxSapServLvlDelete_Object = MibTableColumn
wfIpxSapServLvlDelete = _WfIpxSapServLvlDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 1),
    _WfIpxSapServLvlDelete_Type()
)
wfIpxSapServLvlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlDelete.setStatus("deprecated")


class _WfIpxSapServLvlDisable_Type(Integer32):
    """Custom type wfIpxSapServLvlDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxSapServLvlDisable_Type.__name__ = "Integer32"
_WfIpxSapServLvlDisable_Object = MibTableColumn
wfIpxSapServLvlDisable = _WfIpxSapServLvlDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 2),
    _WfIpxSapServLvlDisable_Type()
)
wfIpxSapServLvlDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlDisable.setStatus("deprecated")
_WfIpxSapServLvlTargServer_Type = DisplayString
_WfIpxSapServLvlTargServer_Object = MibTableColumn
wfIpxSapServLvlTargServer = _WfIpxSapServLvlTargServer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 3),
    _WfIpxSapServLvlTargServer_Type()
)
wfIpxSapServLvlTargServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlTargServer.setStatus("deprecated")
_WfIpxSapServLvlType_Type = OctetString
_WfIpxSapServLvlType_Object = MibTableColumn
wfIpxSapServLvlType = _WfIpxSapServLvlType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 4),
    _WfIpxSapServLvlType_Type()
)
wfIpxSapServLvlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlType.setStatus("deprecated")


class _WfIpxSapServLvlAction_Type(Integer32):
    """Custom type wfIpxSapServLvlAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WfIpxSapServLvlAction_Type.__name__ = "Integer32"
_WfIpxSapServLvlAction_Object = MibTableColumn
wfIpxSapServLvlAction = _WfIpxSapServLvlAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 5),
    _WfIpxSapServLvlAction_Type()
)
wfIpxSapServLvlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlAction.setStatus("deprecated")


class _WfIpxSapServLvlIntf_Type(OctetString):
    """Custom type wfIpxSapServLvlIntf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxSapServLvlIntf_Type.__name__ = "OctetString"
_WfIpxSapServLvlIntf_Object = MibTableColumn
wfIpxSapServLvlIntf = _WfIpxSapServLvlIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 6),
    _WfIpxSapServLvlIntf_Type()
)
wfIpxSapServLvlIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapServLvlIntf.setStatus("deprecated")
_WfIpxSapServLvlIndex_Type = Integer32
_WfIpxSapServLvlIndex_Object = MibTableColumn
wfIpxSapServLvlIndex = _WfIpxSapServLvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 7),
    _WfIpxSapServLvlIndex_Type()
)
wfIpxSapServLvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapServLvlIndex.setStatus("deprecated")
_WfIpxTrafficFilterTable_Object = MibTable
wfIpxTrafficFilterTable = _WfIpxTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11)
)
if mibBuilder.loadTexts:
    wfIpxTrafficFilterTable.setStatus("deprecated")
_WfIpxTrafficFilterEntry_Object = MibTableRow
wfIpxTrafficFilterEntry = _WfIpxTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1)
)
wfIpxTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxTrafficFilterInterface"),
    (0, "Wellfleet-IPX-MIB", "wfIpxTrafficFilterCircuit"),
    (0, "Wellfleet-IPX-MIB", "wfIpxTrafficFilterRuleNumber"),
    (0, "Wellfleet-IPX-MIB", "wfIpxTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfIpxTrafficFilterEntry.setStatus("deprecated")


class _WfIpxTrafficFilterCreate_Type(Integer32):
    """Custom type wfIpxTrafficFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxTrafficFilterCreate_Type.__name__ = "Integer32"
_WfIpxTrafficFilterCreate_Object = MibTableColumn
wfIpxTrafficFilterCreate = _WfIpxTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 1),
    _WfIpxTrafficFilterCreate_Type()
)
wfIpxTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterCreate.setStatus("deprecated")


class _WfIpxTrafficFilterEnable_Type(Integer32):
    """Custom type wfIpxTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxTrafficFilterEnable_Type.__name__ = "Integer32"
_WfIpxTrafficFilterEnable_Object = MibTableColumn
wfIpxTrafficFilterEnable = _WfIpxTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 2),
    _WfIpxTrafficFilterEnable_Type()
)
wfIpxTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterEnable.setStatus("deprecated")


class _WfIpxTrafficFilterStatus_Type(Integer32):
    """Custom type wfIpxTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfIpxTrafficFilterStatus_Type.__name__ = "Integer32"
_WfIpxTrafficFilterStatus_Object = MibTableColumn
wfIpxTrafficFilterStatus = _WfIpxTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 3),
    _WfIpxTrafficFilterStatus_Type()
)
wfIpxTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterStatus.setStatus("deprecated")
_WfIpxTrafficFilterCounter_Type = Counter32
_WfIpxTrafficFilterCounter_Object = MibTableColumn
wfIpxTrafficFilterCounter = _WfIpxTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 4),
    _WfIpxTrafficFilterCounter_Type()
)
wfIpxTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterCounter.setStatus("deprecated")
_WfIpxTrafficFilterDefinition_Type = Opaque
_WfIpxTrafficFilterDefinition_Object = MibTableColumn
wfIpxTrafficFilterDefinition = _WfIpxTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 5),
    _WfIpxTrafficFilterDefinition_Type()
)
wfIpxTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterDefinition.setStatus("deprecated")
_WfIpxTrafficFilterReserved_Type = Integer32
_WfIpxTrafficFilterReserved_Object = MibTableColumn
wfIpxTrafficFilterReserved = _WfIpxTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 6),
    _WfIpxTrafficFilterReserved_Type()
)
wfIpxTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterReserved.setStatus("deprecated")


class _WfIpxTrafficFilterInterface_Type(OctetString):
    """Custom type wfIpxTrafficFilterInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxTrafficFilterInterface_Type.__name__ = "OctetString"
_WfIpxTrafficFilterInterface_Object = MibTableColumn
wfIpxTrafficFilterInterface = _WfIpxTrafficFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 7),
    _WfIpxTrafficFilterInterface_Type()
)
wfIpxTrafficFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterInterface.setStatus("deprecated")
_WfIpxTrafficFilterCircuit_Type = Integer32
_WfIpxTrafficFilterCircuit_Object = MibTableColumn
wfIpxTrafficFilterCircuit = _WfIpxTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 8),
    _WfIpxTrafficFilterCircuit_Type()
)
wfIpxTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterCircuit.setStatus("deprecated")
_WfIpxTrafficFilterRuleNumber_Type = Integer32
_WfIpxTrafficFilterRuleNumber_Object = MibTableColumn
wfIpxTrafficFilterRuleNumber = _WfIpxTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 9),
    _WfIpxTrafficFilterRuleNumber_Type()
)
wfIpxTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterRuleNumber.setStatus("deprecated")
_WfIpxTrafficFilterFragment_Type = Integer32
_WfIpxTrafficFilterFragment_Object = MibTableColumn
wfIpxTrafficFilterFragment = _WfIpxTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 10),
    _WfIpxTrafficFilterFragment_Type()
)
wfIpxTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterFragment.setStatus("deprecated")
_WfIpxTrafficFilterName_Type = DisplayString
_WfIpxTrafficFilterName_Object = MibTableColumn
wfIpxTrafficFilterName = _WfIpxTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 11),
    _WfIpxTrafficFilterName_Type()
)
wfIpxTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterName.setStatus("deprecated")
_WfIpxStaticSapTable_Object = MibTable
wfIpxStaticSapTable = _WfIpxStaticSapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12)
)
if mibBuilder.loadTexts:
    wfIpxStaticSapTable.setStatus("deprecated")
_WfIpxStaticSapEntry_Object = MibTableRow
wfIpxStaticSapEntry = _WfIpxStaticSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1)
)
wfIpxStaticSapEntry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxStaticSapIntf"),
    (0, "Wellfleet-IPX-MIB", "wfIpxStaticSapCircuit"),
    (0, "Wellfleet-IPX-MIB", "wfIpxStaticSapType"),
    (0, "Wellfleet-IPX-MIB", "wfIpxStaticSapNetwork"),
    (0, "Wellfleet-IPX-MIB", "wfIpxStaticSapSocket"),
)
if mibBuilder.loadTexts:
    wfIpxStaticSapEntry.setStatus("deprecated")


class _WfIpxStaticSapDelete_Type(Integer32):
    """Custom type wfIpxStaticSapDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpxStaticSapDelete_Type.__name__ = "Integer32"
_WfIpxStaticSapDelete_Object = MibTableColumn
wfIpxStaticSapDelete = _WfIpxStaticSapDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 1),
    _WfIpxStaticSapDelete_Type()
)
wfIpxStaticSapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticSapDelete.setStatus("deprecated")


class _WfIpxStaticSapDisable_Type(Integer32):
    """Custom type wfIpxStaticSapDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxStaticSapDisable_Type.__name__ = "Integer32"
_WfIpxStaticSapDisable_Object = MibTableColumn
wfIpxStaticSapDisable = _WfIpxStaticSapDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 2),
    _WfIpxStaticSapDisable_Type()
)
wfIpxStaticSapDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticSapDisable.setStatus("deprecated")


class _WfIpxStaticSapType_Type(OctetString):
    """Custom type wfIpxStaticSapType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WfIpxStaticSapType_Type.__name__ = "OctetString"
_WfIpxStaticSapType_Object = MibTableColumn
wfIpxStaticSapType = _WfIpxStaticSapType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 3),
    _WfIpxStaticSapType_Type()
)
wfIpxStaticSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticSapType.setStatus("deprecated")


class _WfIpxStaticSapNetwork_Type(OctetString):
    """Custom type wfIpxStaticSapNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxStaticSapNetwork_Type.__name__ = "OctetString"
_WfIpxStaticSapNetwork_Object = MibTableColumn
wfIpxStaticSapNetwork = _WfIpxStaticSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 4),
    _WfIpxStaticSapNetwork_Type()
)
wfIpxStaticSapNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticSapNetwork.setStatus("deprecated")
_WfIpxStaticSapHost_Type = OctetString
_WfIpxStaticSapHost_Object = MibTableColumn
wfIpxStaticSapHost = _WfIpxStaticSapHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 5),
    _WfIpxStaticSapHost_Type()
)
wfIpxStaticSapHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticSapHost.setStatus("deprecated")


class _WfIpxStaticSapSocket_Type(OctetString):
    """Custom type wfIpxStaticSapSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WfIpxStaticSapSocket_Type.__name__ = "OctetString"
_WfIpxStaticSapSocket_Object = MibTableColumn
wfIpxStaticSapSocket = _WfIpxStaticSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 6),
    _WfIpxStaticSapSocket_Type()
)
wfIpxStaticSapSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticSapSocket.setStatus("deprecated")
_WfIpxStaticSapName_Type = DisplayString
_WfIpxStaticSapName_Object = MibTableColumn
wfIpxStaticSapName = _WfIpxStaticSapName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 7),
    _WfIpxStaticSapName_Type()
)
wfIpxStaticSapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticSapName.setStatus("deprecated")
_WfIpxStaticSapHops_Type = Integer32
_WfIpxStaticSapHops_Object = MibTableColumn
wfIpxStaticSapHops = _WfIpxStaticSapHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 8),
    _WfIpxStaticSapHops_Type()
)
wfIpxStaticSapHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticSapHops.setStatus("deprecated")
_WfIpxStaticSapIndex_Type = OctetString
_WfIpxStaticSapIndex_Object = MibTableColumn
wfIpxStaticSapIndex = _WfIpxStaticSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 9),
    _WfIpxStaticSapIndex_Type()
)
wfIpxStaticSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticSapIndex.setStatus("deprecated")


class _WfIpxStaticSapIntf_Type(OctetString):
    """Custom type wfIpxStaticSapIntf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxStaticSapIntf_Type.__name__ = "OctetString"
_WfIpxStaticSapIntf_Object = MibTableColumn
wfIpxStaticSapIntf = _WfIpxStaticSapIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 10),
    _WfIpxStaticSapIntf_Type()
)
wfIpxStaticSapIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticSapIntf.setStatus("deprecated")
_WfIpxStaticSapCircuit_Type = Integer32
_WfIpxStaticSapCircuit_Object = MibTableColumn
wfIpxStaticSapCircuit = _WfIpxStaticSapCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 12, 1, 11),
    _WfIpxStaticSapCircuit_Type()
)
wfIpxStaticSapCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticSapCircuit.setStatus("deprecated")
_WfIpxBaseRt2EntryTable_Object = MibTable
wfIpxBaseRt2EntryTable = _WfIpxBaseRt2EntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13)
)
if mibBuilder.loadTexts:
    wfIpxBaseRt2EntryTable.setStatus("obsolete")
_WfIpxBaseRt2Entry_Object = MibTableRow
wfIpxBaseRt2Entry = _WfIpxBaseRt2Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1)
)
wfIpxBaseRt2Entry.setIndexNames(
    (0, "Wellfleet-IPX-MIB", "wfIpxBaseRoute2Proto"),
    (0, "Wellfleet-IPX-MIB", "wfIpxBaseRoute2Dest"),
    (0, "Wellfleet-IPX-MIB", "wfIpxBaseRoute2NextHopNetwork"),
    (0, "Wellfleet-IPX-MIB", "wfIpxBaseRoute2NextHopHost"),
)
if mibBuilder.loadTexts:
    wfIpxBaseRt2Entry.setStatus("obsolete")


class _WfIpxBaseRoute2Dest_Type(OctetString):
    """Custom type wfIpxBaseRoute2Dest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxBaseRoute2Dest_Type.__name__ = "OctetString"
_WfIpxBaseRoute2Dest_Object = MibTableColumn
wfIpxBaseRoute2Dest = _WfIpxBaseRoute2Dest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 1),
    _WfIpxBaseRoute2Dest_Type()
)
wfIpxBaseRoute2Dest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2Dest.setStatus("obsolete")
_WfIpxBaseRoute2IfIndex_Type = Integer32
_WfIpxBaseRoute2IfIndex_Object = MibTableColumn
wfIpxBaseRoute2IfIndex = _WfIpxBaseRoute2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 2),
    _WfIpxBaseRoute2IfIndex_Type()
)
wfIpxBaseRoute2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2IfIndex.setStatus("obsolete")
_WfIpxBaseRoute2Ticks_Type = Integer32
_WfIpxBaseRoute2Ticks_Object = MibTableColumn
wfIpxBaseRoute2Ticks = _WfIpxBaseRoute2Ticks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 3),
    _WfIpxBaseRoute2Ticks_Type()
)
wfIpxBaseRoute2Ticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2Ticks.setStatus("obsolete")
_WfIpxBaseRoute2Hops_Type = Integer32
_WfIpxBaseRoute2Hops_Object = MibTableColumn
wfIpxBaseRoute2Hops = _WfIpxBaseRoute2Hops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 4),
    _WfIpxBaseRoute2Hops_Type()
)
wfIpxBaseRoute2Hops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2Hops.setStatus("obsolete")


class _WfIpxBaseRoute2NextHopNetwork_Type(OctetString):
    """Custom type wfIpxBaseRoute2NextHopNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxBaseRoute2NextHopNetwork_Type.__name__ = "OctetString"
_WfIpxBaseRoute2NextHopNetwork_Object = MibTableColumn
wfIpxBaseRoute2NextHopNetwork = _WfIpxBaseRoute2NextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 5),
    _WfIpxBaseRoute2NextHopNetwork_Type()
)
wfIpxBaseRoute2NextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2NextHopNetwork.setStatus("obsolete")


class _WfIpxBaseRoute2NextHopHost_Type(OctetString):
    """Custom type wfIpxBaseRoute2NextHopHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfIpxBaseRoute2NextHopHost_Type.__name__ = "OctetString"
_WfIpxBaseRoute2NextHopHost_Object = MibTableColumn
wfIpxBaseRoute2NextHopHost = _WfIpxBaseRoute2NextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 6),
    _WfIpxBaseRoute2NextHopHost_Type()
)
wfIpxBaseRoute2NextHopHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2NextHopHost.setStatus("obsolete")


class _WfIpxBaseRoute2Type_Type(Integer32):
    """Custom type wfIpxBaseRoute2Type based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1),
          ("static", 5))
    )


_WfIpxBaseRoute2Type_Type.__name__ = "Integer32"
_WfIpxBaseRoute2Type_Object = MibTableColumn
wfIpxBaseRoute2Type = _WfIpxBaseRoute2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 7),
    _WfIpxBaseRoute2Type_Type()
)
wfIpxBaseRoute2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2Type.setStatus("obsolete")


class _WfIpxBaseRoute2Proto_Type(Integer32):
    """Custom type wfIpxBaseRoute2Proto based on Integer32"""
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
        *(("local", 2),
          ("netmgmt", 3),
          ("nlsp", 5),
          ("other", 1),
          ("rip", 4))
    )


_WfIpxBaseRoute2Proto_Type.__name__ = "Integer32"
_WfIpxBaseRoute2Proto_Object = MibTableColumn
wfIpxBaseRoute2Proto = _WfIpxBaseRoute2Proto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 8),
    _WfIpxBaseRoute2Proto_Type()
)
wfIpxBaseRoute2Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2Proto.setStatus("obsolete")
_WfIpxBaseRoute2Age_Type = Integer32
_WfIpxBaseRoute2Age_Object = MibTableColumn
wfIpxBaseRoute2Age = _WfIpxBaseRoute2Age_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 9),
    _WfIpxBaseRoute2Age_Type()
)
wfIpxBaseRoute2Age.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2Age.setStatus("obsolete")
_WfIpxBaseRoute2Info_Type = OctetString
_WfIpxBaseRoute2Info_Object = MibTableColumn
wfIpxBaseRoute2Info = _WfIpxBaseRoute2Info_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 13, 1, 10),
    _WfIpxBaseRoute2Info_Type()
)
wfIpxBaseRoute2Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRoute2Info.setStatus("obsolete")
_WfIpxAggrStats_ObjectIdentity = ObjectIdentity
wfIpxAggrStats = _WfIpxAggrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14)
)
_WfIpxAggrInDatagrams_Type = Counter32
_WfIpxAggrInDatagrams_Object = MibScalar
wfIpxAggrInDatagrams = _WfIpxAggrInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 1),
    _WfIpxAggrInDatagrams_Type()
)
wfIpxAggrInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrInDatagrams.setStatus("mandatory")
_WfIpxAggrOutDatagrams_Type = Counter32
_WfIpxAggrOutDatagrams_Object = MibScalar
wfIpxAggrOutDatagrams = _WfIpxAggrOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 2),
    _WfIpxAggrOutDatagrams_Type()
)
wfIpxAggrOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrOutDatagrams.setStatus("mandatory")
_WfIpxAggrFwdDatagrams_Type = Counter32
_WfIpxAggrFwdDatagrams_Object = MibScalar
wfIpxAggrFwdDatagrams = _WfIpxAggrFwdDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 3),
    _WfIpxAggrFwdDatagrams_Type()
)
wfIpxAggrFwdDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrFwdDatagrams.setStatus("mandatory")
_WfIpxAggrInDiscards_Type = Counter32
_WfIpxAggrInDiscards_Object = MibScalar
wfIpxAggrInDiscards = _WfIpxAggrInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 4),
    _WfIpxAggrInDiscards_Type()
)
wfIpxAggrInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrInDiscards.setStatus("mandatory")
_WfIpxAggrInHdrErrs_Type = Counter32
_WfIpxAggrInHdrErrs_Object = MibScalar
wfIpxAggrInHdrErrs = _WfIpxAggrInHdrErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 5),
    _WfIpxAggrInHdrErrs_Type()
)
wfIpxAggrInHdrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrInHdrErrs.setStatus("mandatory")
_WfIpxAggrInAddrErrs_Type = Counter32
_WfIpxAggrInAddrErrs_Object = MibScalar
wfIpxAggrInAddrErrs = _WfIpxAggrInAddrErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 6),
    _WfIpxAggrInAddrErrs_Type()
)
wfIpxAggrInAddrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrInAddrErrs.setStatus("mandatory")
_WfIpxAggrInUnknownProtos_Type = Counter32
_WfIpxAggrInUnknownProtos_Object = MibScalar
wfIpxAggrInUnknownProtos = _WfIpxAggrInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 7),
    _WfIpxAggrInUnknownProtos_Type()
)
wfIpxAggrInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrInUnknownProtos.setStatus("mandatory")
_WfIpxAggrOutDiscards_Type = Counter32
_WfIpxAggrOutDiscards_Object = MibScalar
wfIpxAggrOutDiscards = _WfIpxAggrOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 8),
    _WfIpxAggrOutDiscards_Type()
)
wfIpxAggrOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrOutDiscards.setStatus("mandatory")
_WfIpxAggrOutNoRoutes_Type = Counter32
_WfIpxAggrOutNoRoutes_Object = MibScalar
wfIpxAggrOutNoRoutes = _WfIpxAggrOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 14, 9),
    _WfIpxAggrOutNoRoutes_Type()
)
wfIpxAggrOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAggrOutNoRoutes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IPX-MIB",
    **{"wfIpxBase": wfIpxBase,
       "wfIpxBaseDelete": wfIpxBaseDelete,
       "wfIpxBaseDisable": wfIpxBaseDisable,
       "wfIpxBaseState": wfIpxBaseState,
       "wfIpxBaseCfgHostNumber": wfIpxBaseCfgHostNumber,
       "wfIpxBaseActiveHostNumber": wfIpxBaseActiveHostNumber,
       "wfIpxBaseNetCount": wfIpxBaseNetCount,
       "wfIpxBaseServiceCount": wfIpxBaseServiceCount,
       "wfIpxBaseLogFilter": wfIpxBaseLogFilter,
       "wfIpxBaseNetTblSize": wfIpxBaseNetTblSize,
       "wfIpxBaseRouterName": wfIpxBaseRouterName,
       "wfIpxBasePrimaryNetNumber": wfIpxBasePrimaryNetNumber,
       "wfIpxBaseRipMethod": wfIpxBaseRipMethod,
       "wfIpxBaseMaximumPath": wfIpxBaseMaximumPath,
       "wfIpxBaseHostCount": wfIpxBaseHostCount,
       "wfIpxBaseMultipleHostAddrs": wfIpxBaseMultipleHostAddrs,
       "wfIpxBaseNovellCertificationConformance": wfIpxBaseNovellCertificationConformance,
       "wfIpxBaseTrigUpdateEn": wfIpxBaseTrigUpdateEn,
       "wfIpxBaseNetSizeBoundEn": wfIpxBaseNetSizeBoundEn,
       "wfIpxBaseMaxNetTblSize": wfIpxBaseMaxNetTblSize,
       "wfIpxBaseNetTblFillNotify": wfIpxBaseNetTblFillNotify,
       "wfIpxBaseRtEntryTable": wfIpxBaseRtEntryTable,
       "wfIpxBaseRtEntry": wfIpxBaseRtEntry,
       "wfIpxBaseRouteDest": wfIpxBaseRouteDest,
       "wfIpxBaseRouteIfIndex": wfIpxBaseRouteIfIndex,
       "wfIpxBaseRouteMetric": wfIpxBaseRouteMetric,
       "wfIpxBaseRouteNextHopNetwork": wfIpxBaseRouteNextHopNetwork,
       "wfIpxBaseRouteNextHopHost": wfIpxBaseRouteNextHopHost,
       "wfIpxBaseRouteType": wfIpxBaseRouteType,
       "wfIpxBaseRouteProto": wfIpxBaseRouteProto,
       "wfIpxBaseRouteAge": wfIpxBaseRouteAge,
       "wfIpxBaseRouteInfo": wfIpxBaseRouteInfo,
       "wfIpxBaseSapEntryTable": wfIpxBaseSapEntryTable,
       "wfIpxBaseSapEntry": wfIpxBaseSapEntry,
       "wfIpxBaseSapType": wfIpxBaseSapType,
       "wfIpxBaseSapNetwork": wfIpxBaseSapNetwork,
       "wfIpxBaseSapHost": wfIpxBaseSapHost,
       "wfIpxBaseSapSocket": wfIpxBaseSapSocket,
       "wfIpxBaseSapName": wfIpxBaseSapName,
       "wfIpxBaseSapAge": wfIpxBaseSapAge,
       "wfIpxBaseSapHops": wfIpxBaseSapHops,
       "wfIpxBaseSapIndex": wfIpxBaseSapIndex,
       "wfIpxBaseSapIntf": wfIpxBaseSapIntf,
       "wfIpxInterfaceTable": wfIpxInterfaceTable,
       "wfIpxInterfaceEntry": wfIpxInterfaceEntry,
       "wfIpxInterfaceIndex": wfIpxInterfaceIndex,
       "wfIpxInterfaceDelete": wfIpxInterfaceDelete,
       "wfIpxInterfaceDisable": wfIpxInterfaceDisable,
       "wfIpxInterfaceState": wfIpxInterfaceState,
       "wfIpxInterfaceCircuit": wfIpxInterfaceCircuit,
       "wfIpxInterfaceNetworkNumber": wfIpxInterfaceNetworkNumber,
       "wfIpxInterfaceCost": wfIpxInterfaceCost,
       "wfIpxInterfaceXsumOn": wfIpxInterfaceXsumOn,
       "wfIpxInterfaceCfgEncaps": wfIpxInterfaceCfgEncaps,
       "wfIpxInterfaceMacAddress": wfIpxInterfaceMacAddress,
       "wfIpxInterfaceSMDSGroupAddress": wfIpxInterfaceSMDSGroupAddress,
       "wfIpxInterfaceMaxInfo": wfIpxInterfaceMaxInfo,
       "wfIpxInterfaceInReceives": wfIpxInterfaceInReceives,
       "wfIpxInterfaceInHdrErrors": wfIpxInterfaceInHdrErrors,
       "wfIpxInterfaceInAddrErrors": wfIpxInterfaceInAddrErrors,
       "wfIpxInterfaceForwDatagrams": wfIpxInterfaceForwDatagrams,
       "wfIpxInterfaceInUnknownProtos": wfIpxInterfaceInUnknownProtos,
       "wfIpxInterfaceInDiscards": wfIpxInterfaceInDiscards,
       "wfIpxInterfaceInDelivers": wfIpxInterfaceInDelivers,
       "wfIpxInterfaceOutRequests": wfIpxInterfaceOutRequests,
       "wfIpxInterfaceOutDiscards": wfIpxInterfaceOutDiscards,
       "wfIpxInterfaceOutNoRoutes": wfIpxInterfaceOutNoRoutes,
       "wfIpxInterfaceTrEndStation": wfIpxInterfaceTrEndStation,
       "wfIpxInterfaceNetbiosAccept": wfIpxInterfaceNetbiosAccept,
       "wfIpxInterfaceNetbiosDeliver": wfIpxInterfaceNetbiosDeliver,
       "wfIpxInterfaceWanSapPeriod": wfIpxInterfaceWanSapPeriod,
       "wfIpxInterfaceFRBcast": wfIpxInterfaceFRBcast,
       "wfIpxInterfaceFRMcast": wfIpxInterfaceFRMcast,
       "wfIpxInterfaceEncaps": wfIpxInterfaceEncaps,
       "wfIpxInterfaceSplit": wfIpxInterfaceSplit,
       "wfIpxInterfaceCacheHit": wfIpxInterfaceCacheHit,
       "wfIpxInterfaceIpxWanDisable": wfIpxInterfaceIpxWanDisable,
       "wfIpxInterfaceIpxWanCommonNet": wfIpxInterfaceIpxWanCommonNet,
       "wfIpxInterfaceIpxWanTimeOut": wfIpxInterfaceIpxWanTimeOut,
       "wfIpxInterfaceIpxWanLinkRetry": wfIpxInterfaceIpxWanLinkRetry,
       "wfIpxInterfaceWanRipPeriod": wfIpxInterfaceWanRipPeriod,
       "wfIpxInterfaceCfgHostNumber": wfIpxInterfaceCfgHostNumber,
       "wfIpxInterfaceActiveHostNumber": wfIpxInterfaceActiveHostNumber,
       "wfIpxRipIntfTable": wfIpxRipIntfTable,
       "wfIpxRipIntfEntry": wfIpxRipIntfEntry,
       "wfIpxRipInterfaceDelete": wfIpxRipInterfaceDelete,
       "wfIpxRipInterfaceDisable": wfIpxRipInterfaceDisable,
       "wfIpxRipInterfaceState": wfIpxRipInterfaceState,
       "wfIpxRipInterfaceIndex": wfIpxRipInterfaceIndex,
       "wfIpxRipInterfaceSupply": wfIpxRipInterfaceSupply,
       "wfIpxRipInterfaceListen": wfIpxRipInterfaceListen,
       "wfIpxAdjacentHostTable": wfIpxAdjacentHostTable,
       "wfIpxAdjacentHostEntry": wfIpxAdjacentHostEntry,
       "wfIpxAhDelete": wfIpxAhDelete,
       "wfIpxAhDisable": wfIpxAhDisable,
       "wfIpxAhTargHostNetwork": wfIpxAhTargHostNetwork,
       "wfIpxAhTargHostId": wfIpxAhTargHostId,
       "wfIpxAhNextHopIntf": wfIpxAhNextHopIntf,
       "wfIpxAhDlci": wfIpxAhDlci,
       "wfIpxStaticRouteTable": wfIpxStaticRouteTable,
       "wfIpxStaticRouteEntry": wfIpxStaticRouteEntry,
       "wfIpxSrDelete": wfIpxSrDelete,
       "wfIpxSrDisable": wfIpxSrDisable,
       "wfIpxSrTargNetwork": wfIpxSrTargNetwork,
       "wfIpxSrCost": wfIpxSrCost,
       "wfIpxSrNextHopNetwork": wfIpxSrNextHopNetwork,
       "wfIpxSrNextHopHost": wfIpxSrNextHopHost,
       "wfIpxSrTargNetworkRt": wfIpxSrTargNetworkRt,
       "wfIpxSrTickCost": wfIpxSrTickCost,
       "wfIpxNetBiosStaticRouteTable": wfIpxNetBiosStaticRouteTable,
       "wfIpxNetBiosStaticRouteEntry": wfIpxNetBiosStaticRouteEntry,
       "wfIpxNetBiosSrDelete": wfIpxNetBiosSrDelete,
       "wfIpxNetBiosSrDisable": wfIpxNetBiosSrDisable,
       "wfIpxNetBiosSrTargNetwork": wfIpxNetBiosSrTargNetwork,
       "wfIpxNetBiosSrName": wfIpxNetBiosSrName,
       "wfIpxNetBiosSrIntf": wfIpxNetBiosSrIntf,
       "wfIpxNetBiosSrIndex": wfIpxNetBiosSrIndex,
       "wfIpxSapNetLvlFilterTable": wfIpxSapNetLvlFilterTable,
       "wfIpxSapNetLvlFilter": wfIpxSapNetLvlFilter,
       "wfIpxSapNetLvlDelete": wfIpxSapNetLvlDelete,
       "wfIpxSapNetLvlDisable": wfIpxSapNetLvlDisable,
       "wfIpxSapNetLvlTargNetwork": wfIpxSapNetLvlTargNetwork,
       "wfIpxSapNetLvlType": wfIpxSapNetLvlType,
       "wfIpxSapNetLvlAction": wfIpxSapNetLvlAction,
       "wfIpxSapNetLvlIntf": wfIpxSapNetLvlIntf,
       "wfIpxSapNetLvlIndex": wfIpxSapNetLvlIndex,
       "wfIpxSapServtLvlFilterTable": wfIpxSapServtLvlFilterTable,
       "wfIpxSapServLvlFilter": wfIpxSapServLvlFilter,
       "wfIpxSapServLvlDelete": wfIpxSapServLvlDelete,
       "wfIpxSapServLvlDisable": wfIpxSapServLvlDisable,
       "wfIpxSapServLvlTargServer": wfIpxSapServLvlTargServer,
       "wfIpxSapServLvlType": wfIpxSapServLvlType,
       "wfIpxSapServLvlAction": wfIpxSapServLvlAction,
       "wfIpxSapServLvlIntf": wfIpxSapServLvlIntf,
       "wfIpxSapServLvlIndex": wfIpxSapServLvlIndex,
       "wfIpxTrafficFilterTable": wfIpxTrafficFilterTable,
       "wfIpxTrafficFilterEntry": wfIpxTrafficFilterEntry,
       "wfIpxTrafficFilterCreate": wfIpxTrafficFilterCreate,
       "wfIpxTrafficFilterEnable": wfIpxTrafficFilterEnable,
       "wfIpxTrafficFilterStatus": wfIpxTrafficFilterStatus,
       "wfIpxTrafficFilterCounter": wfIpxTrafficFilterCounter,
       "wfIpxTrafficFilterDefinition": wfIpxTrafficFilterDefinition,
       "wfIpxTrafficFilterReserved": wfIpxTrafficFilterReserved,
       "wfIpxTrafficFilterInterface": wfIpxTrafficFilterInterface,
       "wfIpxTrafficFilterCircuit": wfIpxTrafficFilterCircuit,
       "wfIpxTrafficFilterRuleNumber": wfIpxTrafficFilterRuleNumber,
       "wfIpxTrafficFilterFragment": wfIpxTrafficFilterFragment,
       "wfIpxTrafficFilterName": wfIpxTrafficFilterName,
       "wfIpxStaticSapTable": wfIpxStaticSapTable,
       "wfIpxStaticSapEntry": wfIpxStaticSapEntry,
       "wfIpxStaticSapDelete": wfIpxStaticSapDelete,
       "wfIpxStaticSapDisable": wfIpxStaticSapDisable,
       "wfIpxStaticSapType": wfIpxStaticSapType,
       "wfIpxStaticSapNetwork": wfIpxStaticSapNetwork,
       "wfIpxStaticSapHost": wfIpxStaticSapHost,
       "wfIpxStaticSapSocket": wfIpxStaticSapSocket,
       "wfIpxStaticSapName": wfIpxStaticSapName,
       "wfIpxStaticSapHops": wfIpxStaticSapHops,
       "wfIpxStaticSapIndex": wfIpxStaticSapIndex,
       "wfIpxStaticSapIntf": wfIpxStaticSapIntf,
       "wfIpxStaticSapCircuit": wfIpxStaticSapCircuit,
       "wfIpxBaseRt2EntryTable": wfIpxBaseRt2EntryTable,
       "wfIpxBaseRt2Entry": wfIpxBaseRt2Entry,
       "wfIpxBaseRoute2Dest": wfIpxBaseRoute2Dest,
       "wfIpxBaseRoute2IfIndex": wfIpxBaseRoute2IfIndex,
       "wfIpxBaseRoute2Ticks": wfIpxBaseRoute2Ticks,
       "wfIpxBaseRoute2Hops": wfIpxBaseRoute2Hops,
       "wfIpxBaseRoute2NextHopNetwork": wfIpxBaseRoute2NextHopNetwork,
       "wfIpxBaseRoute2NextHopHost": wfIpxBaseRoute2NextHopHost,
       "wfIpxBaseRoute2Type": wfIpxBaseRoute2Type,
       "wfIpxBaseRoute2Proto": wfIpxBaseRoute2Proto,
       "wfIpxBaseRoute2Age": wfIpxBaseRoute2Age,
       "wfIpxBaseRoute2Info": wfIpxBaseRoute2Info,
       "wfIpxAggrStats": wfIpxAggrStats,
       "wfIpxAggrInDatagrams": wfIpxAggrInDatagrams,
       "wfIpxAggrOutDatagrams": wfIpxAggrOutDatagrams,
       "wfIpxAggrFwdDatagrams": wfIpxAggrFwdDatagrams,
       "wfIpxAggrInDiscards": wfIpxAggrInDiscards,
       "wfIpxAggrInHdrErrs": wfIpxAggrInHdrErrs,
       "wfIpxAggrInAddrErrs": wfIpxAggrInAddrErrs,
       "wfIpxAggrInUnknownProtos": wfIpxAggrInUnknownProtos,
       "wfIpxAggrOutDiscards": wfIpxAggrOutDiscards,
       "wfIpxAggrOutNoRoutes": wfIpxAggrOutNoRoutes}
)
