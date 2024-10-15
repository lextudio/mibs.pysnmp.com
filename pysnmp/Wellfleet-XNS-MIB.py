# SNMP MIB module (Wellfleet-XNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-XNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:34 2024
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

(wfXnsGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfXnsGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfXnsBase_ObjectIdentity = ObjectIdentity
wfXnsBase = _WfXnsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1)
)


class _WfXnsBaseDelete_Type(Integer32):
    """Custom type wfXnsBaseDelete based on Integer32"""
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


_WfXnsBaseDelete_Type.__name__ = "Integer32"
_WfXnsBaseDelete_Object = MibScalar
wfXnsBaseDelete = _WfXnsBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 1),
    _WfXnsBaseDelete_Type()
)
wfXnsBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseDelete.setStatus("mandatory")


class _WfXnsBaseDisable_Type(Integer32):
    """Custom type wfXnsBaseDisable based on Integer32"""
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


_WfXnsBaseDisable_Type.__name__ = "Integer32"
_WfXnsBaseDisable_Object = MibScalar
wfXnsBaseDisable = _WfXnsBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 2),
    _WfXnsBaseDisable_Type()
)
wfXnsBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseDisable.setStatus("mandatory")


class _WfXnsBaseState_Type(Integer32):
    """Custom type wfXnsBaseState based on Integer32"""
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


_WfXnsBaseState_Type.__name__ = "Integer32"
_WfXnsBaseState_Object = MibScalar
wfXnsBaseState = _WfXnsBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 3),
    _WfXnsBaseState_Type()
)
wfXnsBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseState.setStatus("mandatory")
_WfXnsBaseCfgHostNumber_Type = OctetString
_WfXnsBaseCfgHostNumber_Object = MibScalar
wfXnsBaseCfgHostNumber = _WfXnsBaseCfgHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 4),
    _WfXnsBaseCfgHostNumber_Type()
)
wfXnsBaseCfgHostNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseCfgHostNumber.setStatus("mandatory")
_WfXnsBaseActiveHostNumber_Type = OctetString
_WfXnsBaseActiveHostNumber_Object = MibScalar
wfXnsBaseActiveHostNumber = _WfXnsBaseActiveHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 5),
    _WfXnsBaseActiveHostNumber_Type()
)
wfXnsBaseActiveHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseActiveHostNumber.setStatus("mandatory")


class _WfXnsBaseImplement_Type(Integer32):
    """Custom type wfXnsBaseImplement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ungb", 2),
          ("xerox", 1))
    )


_WfXnsBaseImplement_Type.__name__ = "Integer32"
_WfXnsBaseImplement_Object = MibScalar
wfXnsBaseImplement = _WfXnsBaseImplement_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 6),
    _WfXnsBaseImplement_Type()
)
wfXnsBaseImplement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseImplement.setStatus("mandatory")
_WfXnsBaseNetCount_Type = Counter32
_WfXnsBaseNetCount_Object = MibScalar
wfXnsBaseNetCount = _WfXnsBaseNetCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 7),
    _WfXnsBaseNetCount_Type()
)
wfXnsBaseNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseNetCount.setStatus("mandatory")
_WfXnsBaseHostCount_Type = Counter32
_WfXnsBaseHostCount_Object = MibScalar
wfXnsBaseHostCount = _WfXnsBaseHostCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 8),
    _WfXnsBaseHostCount_Type()
)
wfXnsBaseHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseHostCount.setStatus("mandatory")


class _WfXnsBaseLogFilter_Type(Integer32):
    """Custom type wfXnsBaseLogFilter based on Integer32"""
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


_WfXnsBaseLogFilter_Type.__name__ = "Integer32"
_WfXnsBaseLogFilter_Object = MibScalar
wfXnsBaseLogFilter = _WfXnsBaseLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 9),
    _WfXnsBaseLogFilter_Type()
)
wfXnsBaseLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseLogFilter.setStatus("mandatory")
_WfXnsBaseRtEntryTable_Object = MibTable
wfXnsBaseRtEntryTable = _WfXnsBaseRtEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2)
)
if mibBuilder.loadTexts:
    wfXnsBaseRtEntryTable.setStatus("mandatory")
_WfXnsBaseRtEntry_Object = MibTableRow
wfXnsBaseRtEntry = _WfXnsBaseRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1)
)
wfXnsBaseRtEntry.setIndexNames(
    (0, "Wellfleet-XNS-MIB", "wfXnsBaseRouteDest"),
)
if mibBuilder.loadTexts:
    wfXnsBaseRtEntry.setStatus("mandatory")


class _WfXnsBaseRouteDest_Type(OctetString):
    """Custom type wfXnsBaseRouteDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsBaseRouteDest_Type.__name__ = "OctetString"
_WfXnsBaseRouteDest_Object = MibTableColumn
wfXnsBaseRouteDest = _WfXnsBaseRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 1),
    _WfXnsBaseRouteDest_Type()
)
wfXnsBaseRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteDest.setStatus("mandatory")
_WfXnsBaseRouteIfIndex_Type = Integer32
_WfXnsBaseRouteIfIndex_Object = MibTableColumn
wfXnsBaseRouteIfIndex = _WfXnsBaseRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 2),
    _WfXnsBaseRouteIfIndex_Type()
)
wfXnsBaseRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteIfIndex.setStatus("mandatory")
_WfXnsBaseRouteMetric_Type = Integer32
_WfXnsBaseRouteMetric_Object = MibTableColumn
wfXnsBaseRouteMetric = _WfXnsBaseRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 3),
    _WfXnsBaseRouteMetric_Type()
)
wfXnsBaseRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteMetric.setStatus("mandatory")
_WfXnsBaseRouteNextHopNetwork_Type = OctetString
_WfXnsBaseRouteNextHopNetwork_Object = MibTableColumn
wfXnsBaseRouteNextHopNetwork = _WfXnsBaseRouteNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 4),
    _WfXnsBaseRouteNextHopNetwork_Type()
)
wfXnsBaseRouteNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteNextHopNetwork.setStatus("mandatory")
_WfXnsBaseRouteNextHopHost_Type = OctetString
_WfXnsBaseRouteNextHopHost_Object = MibTableColumn
wfXnsBaseRouteNextHopHost = _WfXnsBaseRouteNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 5),
    _WfXnsBaseRouteNextHopHost_Type()
)
wfXnsBaseRouteNextHopHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteNextHopHost.setStatus("mandatory")


class _WfXnsBaseRouteType_Type(Integer32):
    """Custom type wfXnsBaseRouteType based on Integer32"""
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


_WfXnsBaseRouteType_Type.__name__ = "Integer32"
_WfXnsBaseRouteType_Object = MibTableColumn
wfXnsBaseRouteType = _WfXnsBaseRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 6),
    _WfXnsBaseRouteType_Type()
)
wfXnsBaseRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteType.setStatus("mandatory")


class _WfXnsBaseRouteProto_Type(Integer32):
    """Custom type wfXnsBaseRouteProto based on Integer32"""
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


_WfXnsBaseRouteProto_Type.__name__ = "Integer32"
_WfXnsBaseRouteProto_Object = MibTableColumn
wfXnsBaseRouteProto = _WfXnsBaseRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 7),
    _WfXnsBaseRouteProto_Type()
)
wfXnsBaseRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteProto.setStatus("mandatory")
_WfXnsBaseRouteAge_Type = Integer32
_WfXnsBaseRouteAge_Object = MibTableColumn
wfXnsBaseRouteAge = _WfXnsBaseRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 8),
    _WfXnsBaseRouteAge_Type()
)
wfXnsBaseRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteAge.setStatus("mandatory")
_WfXnsBaseRouteInfo_Type = OctetString
_WfXnsBaseRouteInfo_Object = MibTableColumn
wfXnsBaseRouteInfo = _WfXnsBaseRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 9),
    _WfXnsBaseRouteInfo_Type()
)
wfXnsBaseRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteInfo.setStatus("mandatory")
_WfXnsInterfaceTable_Object = MibTable
wfXnsInterfaceTable = _WfXnsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3)
)
if mibBuilder.loadTexts:
    wfXnsInterfaceTable.setStatus("mandatory")
_WfXnsInterfaceEntry_Object = MibTableRow
wfXnsInterfaceEntry = _WfXnsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1)
)
wfXnsInterfaceEntry.setIndexNames(
    (0, "Wellfleet-XNS-MIB", "wfXnsInterfaceNetworkNumber"),
    (0, "Wellfleet-XNS-MIB", "wfXnsInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfXnsInterfaceEntry.setStatus("mandatory")
_WfXnsInterfaceIndex_Type = Integer32
_WfXnsInterfaceIndex_Object = MibTableColumn
wfXnsInterfaceIndex = _WfXnsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 1),
    _WfXnsInterfaceIndex_Type()
)
wfXnsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceIndex.setStatus("mandatory")


class _WfXnsInterfaceDelete_Type(Integer32):
    """Custom type wfXnsInterfaceDelete based on Integer32"""
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


_WfXnsInterfaceDelete_Type.__name__ = "Integer32"
_WfXnsInterfaceDelete_Object = MibTableColumn
wfXnsInterfaceDelete = _WfXnsInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 2),
    _WfXnsInterfaceDelete_Type()
)
wfXnsInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceDelete.setStatus("mandatory")


class _WfXnsInterfaceDisable_Type(Integer32):
    """Custom type wfXnsInterfaceDisable based on Integer32"""
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


_WfXnsInterfaceDisable_Type.__name__ = "Integer32"
_WfXnsInterfaceDisable_Object = MibTableColumn
wfXnsInterfaceDisable = _WfXnsInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 3),
    _WfXnsInterfaceDisable_Type()
)
wfXnsInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceDisable.setStatus("mandatory")


class _WfXnsInterfaceState_Type(Integer32):
    """Custom type wfXnsInterfaceState based on Integer32"""
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


_WfXnsInterfaceState_Type.__name__ = "Integer32"
_WfXnsInterfaceState_Object = MibTableColumn
wfXnsInterfaceState = _WfXnsInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 4),
    _WfXnsInterfaceState_Type()
)
wfXnsInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceState.setStatus("mandatory")
_WfXnsInterfaceCircuit_Type = Integer32
_WfXnsInterfaceCircuit_Object = MibTableColumn
wfXnsInterfaceCircuit = _WfXnsInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 5),
    _WfXnsInterfaceCircuit_Type()
)
wfXnsInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceCircuit.setStatus("mandatory")


class _WfXnsInterfaceNetworkNumber_Type(OctetString):
    """Custom type wfXnsInterfaceNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsInterfaceNetworkNumber_Type.__name__ = "OctetString"
_WfXnsInterfaceNetworkNumber_Object = MibTableColumn
wfXnsInterfaceNetworkNumber = _WfXnsInterfaceNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 6),
    _WfXnsInterfaceNetworkNumber_Type()
)
wfXnsInterfaceNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceNetworkNumber.setStatus("mandatory")
_WfXnsInterfaceCost_Type = Integer32
_WfXnsInterfaceCost_Object = MibTableColumn
wfXnsInterfaceCost = _WfXnsInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 7),
    _WfXnsInterfaceCost_Type()
)
wfXnsInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceCost.setStatus("mandatory")


class _WfXnsInterfaceXsumOn_Type(Integer32):
    """Custom type wfXnsInterfaceXsumOn based on Integer32"""
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


_WfXnsInterfaceXsumOn_Type.__name__ = "Integer32"
_WfXnsInterfaceXsumOn_Object = MibTableColumn
wfXnsInterfaceXsumOn = _WfXnsInterfaceXsumOn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 8),
    _WfXnsInterfaceXsumOn_Type()
)
wfXnsInterfaceXsumOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceXsumOn.setStatus("mandatory")


class _WfXnsInterfaceEncaps_Type(Integer32):
    """Custom type wfXnsInterfaceEncaps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("snap", 2))
    )


_WfXnsInterfaceEncaps_Type.__name__ = "Integer32"
_WfXnsInterfaceEncaps_Object = MibTableColumn
wfXnsInterfaceEncaps = _WfXnsInterfaceEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 9),
    _WfXnsInterfaceEncaps_Type()
)
wfXnsInterfaceEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceEncaps.setStatus("mandatory")
_WfXnsInterfaceMacAddress_Type = OctetString
_WfXnsInterfaceMacAddress_Object = MibTableColumn
wfXnsInterfaceMacAddress = _WfXnsInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 10),
    _WfXnsInterfaceMacAddress_Type()
)
wfXnsInterfaceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceMacAddress.setStatus("mandatory")
_WfXnsInterfaceSMDSGroupAddress_Type = OctetString
_WfXnsInterfaceSMDSGroupAddress_Object = MibTableColumn
wfXnsInterfaceSMDSGroupAddress = _WfXnsInterfaceSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 11),
    _WfXnsInterfaceSMDSGroupAddress_Type()
)
wfXnsInterfaceSMDSGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceSMDSGroupAddress.setStatus("mandatory")
_WfXnsInterfaceMaxInfo_Type = Integer32
_WfXnsInterfaceMaxInfo_Object = MibTableColumn
wfXnsInterfaceMaxInfo = _WfXnsInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 12),
    _WfXnsInterfaceMaxInfo_Type()
)
wfXnsInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceMaxInfo.setStatus("mandatory")


class _WfXnsInterfaceExtServer_Type(Integer32):
    """Custom type wfXnsInterfaceExtServer based on Integer32"""
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


_WfXnsInterfaceExtServer_Type.__name__ = "Integer32"
_WfXnsInterfaceExtServer_Object = MibTableColumn
wfXnsInterfaceExtServer = _WfXnsInterfaceExtServer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 13),
    _WfXnsInterfaceExtServer_Type()
)
wfXnsInterfaceExtServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExtServer.setStatus("mandatory")
_WfXnsInterfaceExServNetwork_Type = OctetString
_WfXnsInterfaceExServNetwork_Object = MibTableColumn
wfXnsInterfaceExServNetwork = _WfXnsInterfaceExServNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 14),
    _WfXnsInterfaceExServNetwork_Type()
)
wfXnsInterfaceExServNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServNetwork.setStatus("mandatory")
_WfXnsInterfaceExServHostId_Type = OctetString
_WfXnsInterfaceExServHostId_Object = MibTableColumn
wfXnsInterfaceExServHostId = _WfXnsInterfaceExServHostId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 15),
    _WfXnsInterfaceExServHostId_Type()
)
wfXnsInterfaceExServHostId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServHostId.setStatus("mandatory")
_WfXnsInterfaceExServPktType_Type = OctetString
_WfXnsInterfaceExServPktType_Object = MibTableColumn
wfXnsInterfaceExServPktType = _WfXnsInterfaceExServPktType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 16),
    _WfXnsInterfaceExServPktType_Type()
)
wfXnsInterfaceExServPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServPktType.setStatus("mandatory")
_WfXnsInterfaceExServSockNm_Type = OctetString
_WfXnsInterfaceExServSockNm_Object = MibTableColumn
wfXnsInterfaceExServSockNm = _WfXnsInterfaceExServSockNm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 17),
    _WfXnsInterfaceExServSockNm_Type()
)
wfXnsInterfaceExServSockNm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServSockNm.setStatus("mandatory")
_WfXnsInterfaceInReceives_Type = Counter32
_WfXnsInterfaceInReceives_Object = MibTableColumn
wfXnsInterfaceInReceives = _WfXnsInterfaceInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 18),
    _WfXnsInterfaceInReceives_Type()
)
wfXnsInterfaceInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInReceives.setStatus("mandatory")
_WfXnsInterfaceInHdrErrors_Type = Counter32
_WfXnsInterfaceInHdrErrors_Object = MibTableColumn
wfXnsInterfaceInHdrErrors = _WfXnsInterfaceInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 19),
    _WfXnsInterfaceInHdrErrors_Type()
)
wfXnsInterfaceInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInHdrErrors.setStatus("mandatory")
_WfXnsInterfaceInAddrErrors_Type = Counter32
_WfXnsInterfaceInAddrErrors_Object = MibTableColumn
wfXnsInterfaceInAddrErrors = _WfXnsInterfaceInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 20),
    _WfXnsInterfaceInAddrErrors_Type()
)
wfXnsInterfaceInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInAddrErrors.setStatus("mandatory")
_WfXnsInterfaceForwDatagrams_Type = Counter32
_WfXnsInterfaceForwDatagrams_Object = MibTableColumn
wfXnsInterfaceForwDatagrams = _WfXnsInterfaceForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 21),
    _WfXnsInterfaceForwDatagrams_Type()
)
wfXnsInterfaceForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceForwDatagrams.setStatus("mandatory")
_WfXnsInterfaceInUnknownProtos_Type = Counter32
_WfXnsInterfaceInUnknownProtos_Object = MibTableColumn
wfXnsInterfaceInUnknownProtos = _WfXnsInterfaceInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 22),
    _WfXnsInterfaceInUnknownProtos_Type()
)
wfXnsInterfaceInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInUnknownProtos.setStatus("mandatory")
_WfXnsInterfaceInDiscards_Type = Counter32
_WfXnsInterfaceInDiscards_Object = MibTableColumn
wfXnsInterfaceInDiscards = _WfXnsInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 23),
    _WfXnsInterfaceInDiscards_Type()
)
wfXnsInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInDiscards.setStatus("mandatory")
_WfXnsInterfaceInDelivers_Type = Counter32
_WfXnsInterfaceInDelivers_Object = MibTableColumn
wfXnsInterfaceInDelivers = _WfXnsInterfaceInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 24),
    _WfXnsInterfaceInDelivers_Type()
)
wfXnsInterfaceInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInDelivers.setStatus("mandatory")
_WfXnsInterfaceOutRequests_Type = Counter32
_WfXnsInterfaceOutRequests_Object = MibTableColumn
wfXnsInterfaceOutRequests = _WfXnsInterfaceOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 25),
    _WfXnsInterfaceOutRequests_Type()
)
wfXnsInterfaceOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceOutRequests.setStatus("mandatory")
_WfXnsInterfaceOutDiscards_Type = Counter32
_WfXnsInterfaceOutDiscards_Object = MibTableColumn
wfXnsInterfaceOutDiscards = _WfXnsInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 26),
    _WfXnsInterfaceOutDiscards_Type()
)
wfXnsInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceOutDiscards.setStatus("mandatory")
_WfXnsInterfaceOutNoRoutes_Type = Counter32
_WfXnsInterfaceOutNoRoutes_Object = MibTableColumn
wfXnsInterfaceOutNoRoutes = _WfXnsInterfaceOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 27),
    _WfXnsInterfaceOutNoRoutes_Type()
)
wfXnsInterfaceOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceOutNoRoutes.setStatus("mandatory")
_WfXnsInterfaceFRBcast_Type = OctetString
_WfXnsInterfaceFRBcast_Object = MibTableColumn
wfXnsInterfaceFRBcast = _WfXnsInterfaceFRBcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 28),
    _WfXnsInterfaceFRBcast_Type()
)
wfXnsInterfaceFRBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceFRBcast.setStatus("mandatory")
_WfXnsInterfaceFRMcast_Type = OctetString
_WfXnsInterfaceFRMcast_Object = MibTableColumn
wfXnsInterfaceFRMcast = _WfXnsInterfaceFRMcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 29),
    _WfXnsInterfaceFRMcast_Type()
)
wfXnsInterfaceFRMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceFRMcast.setStatus("mandatory")


class _WfXnsInterfaceSplit_Type(Integer32):
    """Custom type wfXnsInterfaceSplit based on Integer32"""
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


_WfXnsInterfaceSplit_Type.__name__ = "Integer32"
_WfXnsInterfaceSplit_Object = MibTableColumn
wfXnsInterfaceSplit = _WfXnsInterfaceSplit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 30),
    _WfXnsInterfaceSplit_Type()
)
wfXnsInterfaceSplit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceSplit.setStatus("mandatory")
_WfXnsRipIntfTable_Object = MibTable
wfXnsRipIntfTable = _WfXnsRipIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4)
)
if mibBuilder.loadTexts:
    wfXnsRipIntfTable.setStatus("mandatory")
_WfXnsRipIntfEntry_Object = MibTableRow
wfXnsRipIntfEntry = _WfXnsRipIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1)
)
wfXnsRipIntfEntry.setIndexNames(
    (0, "Wellfleet-XNS-MIB", "wfXnsRipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfXnsRipIntfEntry.setStatus("mandatory")


class _WfXnsRipInterfaceDelete_Type(Integer32):
    """Custom type wfXnsRipInterfaceDelete based on Integer32"""
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


_WfXnsRipInterfaceDelete_Type.__name__ = "Integer32"
_WfXnsRipInterfaceDelete_Object = MibTableColumn
wfXnsRipInterfaceDelete = _WfXnsRipInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 1),
    _WfXnsRipInterfaceDelete_Type()
)
wfXnsRipInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceDelete.setStatus("mandatory")


class _WfXnsRipInterfaceDisable_Type(Integer32):
    """Custom type wfXnsRipInterfaceDisable based on Integer32"""
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


_WfXnsRipInterfaceDisable_Type.__name__ = "Integer32"
_WfXnsRipInterfaceDisable_Object = MibTableColumn
wfXnsRipInterfaceDisable = _WfXnsRipInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 2),
    _WfXnsRipInterfaceDisable_Type()
)
wfXnsRipInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceDisable.setStatus("mandatory")


class _WfXnsRipInterfaceState_Type(Integer32):
    """Custom type wfXnsRipInterfaceState based on Integer32"""
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


_WfXnsRipInterfaceState_Type.__name__ = "Integer32"
_WfXnsRipInterfaceState_Object = MibTableColumn
wfXnsRipInterfaceState = _WfXnsRipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 3),
    _WfXnsRipInterfaceState_Type()
)
wfXnsRipInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceState.setStatus("mandatory")


class _WfXnsRipInterfaceIndex_Type(OctetString):
    """Custom type wfXnsRipInterfaceIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsRipInterfaceIndex_Type.__name__ = "OctetString"
_WfXnsRipInterfaceIndex_Object = MibTableColumn
wfXnsRipInterfaceIndex = _WfXnsRipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 4),
    _WfXnsRipInterfaceIndex_Type()
)
wfXnsRipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceIndex.setStatus("mandatory")


class _WfXnsRipInterfaceSupply_Type(Integer32):
    """Custom type wfXnsRipInterfaceSupply based on Integer32"""
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


_WfXnsRipInterfaceSupply_Type.__name__ = "Integer32"
_WfXnsRipInterfaceSupply_Object = MibTableColumn
wfXnsRipInterfaceSupply = _WfXnsRipInterfaceSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 5),
    _WfXnsRipInterfaceSupply_Type()
)
wfXnsRipInterfaceSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceSupply.setStatus("mandatory")


class _WfXnsRipInterfaceListen_Type(Integer32):
    """Custom type wfXnsRipInterfaceListen based on Integer32"""
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


_WfXnsRipInterfaceListen_Type.__name__ = "Integer32"
_WfXnsRipInterfaceListen_Object = MibTableColumn
wfXnsRipInterfaceListen = _WfXnsRipInterfaceListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 6),
    _WfXnsRipInterfaceListen_Type()
)
wfXnsRipInterfaceListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceListen.setStatus("mandatory")
_WfXnsAdjacentHostTable_Object = MibTable
wfXnsAdjacentHostTable = _WfXnsAdjacentHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5)
)
if mibBuilder.loadTexts:
    wfXnsAdjacentHostTable.setStatus("mandatory")
_WfXnsAdjacentHostEntry_Object = MibTableRow
wfXnsAdjacentHostEntry = _WfXnsAdjacentHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1)
)
wfXnsAdjacentHostEntry.setIndexNames(
    (0, "Wellfleet-XNS-MIB", "wfXnsAhTargHostNetwork"),
    (0, "Wellfleet-XNS-MIB", "wfXnsAhTargHostId"),
)
if mibBuilder.loadTexts:
    wfXnsAdjacentHostEntry.setStatus("mandatory")


class _WfXnsAhDelete_Type(Integer32):
    """Custom type wfXnsAhDelete based on Integer32"""
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


_WfXnsAhDelete_Type.__name__ = "Integer32"
_WfXnsAhDelete_Object = MibTableColumn
wfXnsAhDelete = _WfXnsAhDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 1),
    _WfXnsAhDelete_Type()
)
wfXnsAhDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhDelete.setStatus("mandatory")


class _WfXnsAhDisable_Type(Integer32):
    """Custom type wfXnsAhDisable based on Integer32"""
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


_WfXnsAhDisable_Type.__name__ = "Integer32"
_WfXnsAhDisable_Object = MibTableColumn
wfXnsAhDisable = _WfXnsAhDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 2),
    _WfXnsAhDisable_Type()
)
wfXnsAhDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhDisable.setStatus("mandatory")


class _WfXnsAhTargHostNetwork_Type(OctetString):
    """Custom type wfXnsAhTargHostNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsAhTargHostNetwork_Type.__name__ = "OctetString"
_WfXnsAhTargHostNetwork_Object = MibTableColumn
wfXnsAhTargHostNetwork = _WfXnsAhTargHostNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 3),
    _WfXnsAhTargHostNetwork_Type()
)
wfXnsAhTargHostNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAhTargHostNetwork.setStatus("mandatory")


class _WfXnsAhTargHostId_Type(OctetString):
    """Custom type wfXnsAhTargHostId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfXnsAhTargHostId_Type.__name__ = "OctetString"
_WfXnsAhTargHostId_Object = MibTableColumn
wfXnsAhTargHostId = _WfXnsAhTargHostId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 4),
    _WfXnsAhTargHostId_Type()
)
wfXnsAhTargHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAhTargHostId.setStatus("mandatory")
_WfXnsAhNextHopIntf_Type = OctetString
_WfXnsAhNextHopIntf_Object = MibTableColumn
wfXnsAhNextHopIntf = _WfXnsAhNextHopIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 5),
    _WfXnsAhNextHopIntf_Type()
)
wfXnsAhNextHopIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhNextHopIntf.setStatus("mandatory")
_WfXnsAhDlci_Type = OctetString
_WfXnsAhDlci_Object = MibTableColumn
wfXnsAhDlci = _WfXnsAhDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 6),
    _WfXnsAhDlci_Type()
)
wfXnsAhDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhDlci.setStatus("mandatory")
_WfXnsStaticRouteTable_Object = MibTable
wfXnsStaticRouteTable = _WfXnsStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6)
)
if mibBuilder.loadTexts:
    wfXnsStaticRouteTable.setStatus("mandatory")
_WfXnsStaticRouteEntry_Object = MibTableRow
wfXnsStaticRouteEntry = _WfXnsStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1)
)
wfXnsStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-XNS-MIB", "wfXnsSrTargNetwork"),
    (0, "Wellfleet-XNS-MIB", "wfXnsSrNextHopNetwork"),
)
if mibBuilder.loadTexts:
    wfXnsStaticRouteEntry.setStatus("mandatory")


class _WfXnsSrDelete_Type(Integer32):
    """Custom type wfXnsSrDelete based on Integer32"""
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


_WfXnsSrDelete_Type.__name__ = "Integer32"
_WfXnsSrDelete_Object = MibTableColumn
wfXnsSrDelete = _WfXnsSrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 1),
    _WfXnsSrDelete_Type()
)
wfXnsSrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrDelete.setStatus("mandatory")


class _WfXnsSrDisable_Type(Integer32):
    """Custom type wfXnsSrDisable based on Integer32"""
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


_WfXnsSrDisable_Type.__name__ = "Integer32"
_WfXnsSrDisable_Object = MibTableColumn
wfXnsSrDisable = _WfXnsSrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 2),
    _WfXnsSrDisable_Type()
)
wfXnsSrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrDisable.setStatus("mandatory")


class _WfXnsSrTargNetwork_Type(OctetString):
    """Custom type wfXnsSrTargNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsSrTargNetwork_Type.__name__ = "OctetString"
_WfXnsSrTargNetwork_Object = MibTableColumn
wfXnsSrTargNetwork = _WfXnsSrTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 3),
    _WfXnsSrTargNetwork_Type()
)
wfXnsSrTargNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsSrTargNetwork.setStatus("mandatory")
_WfXnsSrCost_Type = Integer32
_WfXnsSrCost_Object = MibTableColumn
wfXnsSrCost = _WfXnsSrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 4),
    _WfXnsSrCost_Type()
)
wfXnsSrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrCost.setStatus("mandatory")


class _WfXnsSrNextHopNetwork_Type(OctetString):
    """Custom type wfXnsSrNextHopNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsSrNextHopNetwork_Type.__name__ = "OctetString"
_WfXnsSrNextHopNetwork_Object = MibTableColumn
wfXnsSrNextHopNetwork = _WfXnsSrNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 5),
    _WfXnsSrNextHopNetwork_Type()
)
wfXnsSrNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsSrNextHopNetwork.setStatus("mandatory")
_WfXnsSrNextHopHost_Type = OctetString
_WfXnsSrNextHopHost_Object = MibTableColumn
wfXnsSrNextHopHost = _WfXnsSrNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 6),
    _WfXnsSrNextHopHost_Type()
)
wfXnsSrNextHopHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrNextHopHost.setStatus("mandatory")
_WfXnsSrTargNetworkRt_Type = Integer32
_WfXnsSrTargNetworkRt_Object = MibTableColumn
wfXnsSrTargNetworkRt = _WfXnsSrTargNetworkRt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 7),
    _WfXnsSrTargNetworkRt_Type()
)
wfXnsSrTargNetworkRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsSrTargNetworkRt.setStatus("mandatory")
_WfXnsTrafficFilterTable_Object = MibTable
wfXnsTrafficFilterTable = _WfXnsTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7)
)
if mibBuilder.loadTexts:
    wfXnsTrafficFilterTable.setStatus("mandatory")
_WfXnsTrafficFilterEntry_Object = MibTableRow
wfXnsTrafficFilterEntry = _WfXnsTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1)
)
wfXnsTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-XNS-MIB", "wfXnsTrafficFilterInterface"),
    (0, "Wellfleet-XNS-MIB", "wfXnsTrafficFilterCircuit"),
    (0, "Wellfleet-XNS-MIB", "wfXnsTrafficFilterRuleNumber"),
    (0, "Wellfleet-XNS-MIB", "wfXnsTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfXnsTrafficFilterEntry.setStatus("mandatory")


class _WfXnsTrafficFilterCreate_Type(Integer32):
    """Custom type wfXnsTrafficFilterCreate based on Integer32"""
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


_WfXnsTrafficFilterCreate_Type.__name__ = "Integer32"
_WfXnsTrafficFilterCreate_Object = MibTableColumn
wfXnsTrafficFilterCreate = _WfXnsTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 1),
    _WfXnsTrafficFilterCreate_Type()
)
wfXnsTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterCreate.setStatus("mandatory")


class _WfXnsTrafficFilterEnable_Type(Integer32):
    """Custom type wfXnsTrafficFilterEnable based on Integer32"""
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


_WfXnsTrafficFilterEnable_Type.__name__ = "Integer32"
_WfXnsTrafficFilterEnable_Object = MibTableColumn
wfXnsTrafficFilterEnable = _WfXnsTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 2),
    _WfXnsTrafficFilterEnable_Type()
)
wfXnsTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterEnable.setStatus("mandatory")


class _WfXnsTrafficFilterStatus_Type(Integer32):
    """Custom type wfXnsTrafficFilterStatus based on Integer32"""
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


_WfXnsTrafficFilterStatus_Type.__name__ = "Integer32"
_WfXnsTrafficFilterStatus_Object = MibTableColumn
wfXnsTrafficFilterStatus = _WfXnsTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 3),
    _WfXnsTrafficFilterStatus_Type()
)
wfXnsTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterStatus.setStatus("mandatory")
_WfXnsTrafficFilterCounter_Type = Counter32
_WfXnsTrafficFilterCounter_Object = MibTableColumn
wfXnsTrafficFilterCounter = _WfXnsTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 4),
    _WfXnsTrafficFilterCounter_Type()
)
wfXnsTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterCounter.setStatus("mandatory")
_WfXnsTrafficFilterDefinition_Type = Opaque
_WfXnsTrafficFilterDefinition_Object = MibTableColumn
wfXnsTrafficFilterDefinition = _WfXnsTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 5),
    _WfXnsTrafficFilterDefinition_Type()
)
wfXnsTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterDefinition.setStatus("mandatory")
_WfXnsTrafficFilterReserved_Type = Integer32
_WfXnsTrafficFilterReserved_Object = MibTableColumn
wfXnsTrafficFilterReserved = _WfXnsTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 6),
    _WfXnsTrafficFilterReserved_Type()
)
wfXnsTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterReserved.setStatus("mandatory")


class _WfXnsTrafficFilterInterface_Type(OctetString):
    """Custom type wfXnsTrafficFilterInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsTrafficFilterInterface_Type.__name__ = "OctetString"
_WfXnsTrafficFilterInterface_Object = MibTableColumn
wfXnsTrafficFilterInterface = _WfXnsTrafficFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 7),
    _WfXnsTrafficFilterInterface_Type()
)
wfXnsTrafficFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterInterface.setStatus("mandatory")
_WfXnsTrafficFilterCircuit_Type = Integer32
_WfXnsTrafficFilterCircuit_Object = MibTableColumn
wfXnsTrafficFilterCircuit = _WfXnsTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 8),
    _WfXnsTrafficFilterCircuit_Type()
)
wfXnsTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterCircuit.setStatus("mandatory")
_WfXnsTrafficFilterRuleNumber_Type = Integer32
_WfXnsTrafficFilterRuleNumber_Object = MibTableColumn
wfXnsTrafficFilterRuleNumber = _WfXnsTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 9),
    _WfXnsTrafficFilterRuleNumber_Type()
)
wfXnsTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterRuleNumber.setStatus("mandatory")
_WfXnsTrafficFilterFragment_Type = Integer32
_WfXnsTrafficFilterFragment_Object = MibTableColumn
wfXnsTrafficFilterFragment = _WfXnsTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 10),
    _WfXnsTrafficFilterFragment_Type()
)
wfXnsTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterFragment.setStatus("mandatory")
_WfXnsTrafficFilterName_Type = DisplayString
_WfXnsTrafficFilterName_Object = MibTableColumn
wfXnsTrafficFilterName = _WfXnsTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 11),
    _WfXnsTrafficFilterName_Type()
)
wfXnsTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterName.setStatus("mandatory")
_WfXnsBaseAdjEntryTable_Object = MibTable
wfXnsBaseAdjEntryTable = _WfXnsBaseAdjEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8)
)
if mibBuilder.loadTexts:
    wfXnsBaseAdjEntryTable.setStatus("mandatory")
_WfXnsBaseAdjEntry_Object = MibTableRow
wfXnsBaseAdjEntry = _WfXnsBaseAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8, 1)
)
wfXnsBaseAdjEntry.setIndexNames(
    (0, "Wellfleet-XNS-MIB", "wfXnsBaseAdjacencyNetwork"),
    (0, "Wellfleet-XNS-MIB", "wfXnsBaseAdjacencyHostid"),
)
if mibBuilder.loadTexts:
    wfXnsBaseAdjEntry.setStatus("mandatory")


class _WfXnsBaseAdjacencyNetwork_Type(OctetString):
    """Custom type wfXnsBaseAdjacencyNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfXnsBaseAdjacencyNetwork_Type.__name__ = "OctetString"
_WfXnsBaseAdjacencyNetwork_Object = MibTableColumn
wfXnsBaseAdjacencyNetwork = _WfXnsBaseAdjacencyNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8, 1, 1),
    _WfXnsBaseAdjacencyNetwork_Type()
)
wfXnsBaseAdjacencyNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseAdjacencyNetwork.setStatus("mandatory")


class _WfXnsBaseAdjacencyHostid_Type(OctetString):
    """Custom type wfXnsBaseAdjacencyHostid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfXnsBaseAdjacencyHostid_Type.__name__ = "OctetString"
_WfXnsBaseAdjacencyHostid_Object = MibTableColumn
wfXnsBaseAdjacencyHostid = _WfXnsBaseAdjacencyHostid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8, 1, 2),
    _WfXnsBaseAdjacencyHostid_Type()
)
wfXnsBaseAdjacencyHostid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseAdjacencyHostid.setStatus("mandatory")
_WfXnsBaseAdjacencyCost_Type = Integer32
_WfXnsBaseAdjacencyCost_Object = MibTableColumn
wfXnsBaseAdjacencyCost = _WfXnsBaseAdjacencyCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8, 1, 3),
    _WfXnsBaseAdjacencyCost_Type()
)
wfXnsBaseAdjacencyCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseAdjacencyCost.setStatus("mandatory")
_WfXnsBaseAdjacencyAge_Type = Integer32
_WfXnsBaseAdjacencyAge_Object = MibTableColumn
wfXnsBaseAdjacencyAge = _WfXnsBaseAdjacencyAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8, 1, 4),
    _WfXnsBaseAdjacencyAge_Type()
)
wfXnsBaseAdjacencyAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseAdjacencyAge.setStatus("mandatory")
_WfXnsBaseAdjacencyIntf_Type = OctetString
_WfXnsBaseAdjacencyIntf_Object = MibTableColumn
wfXnsBaseAdjacencyIntf = _WfXnsBaseAdjacencyIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8, 1, 5),
    _WfXnsBaseAdjacencyIntf_Type()
)
wfXnsBaseAdjacencyIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseAdjacencyIntf.setStatus("mandatory")
_WfXnsBaseAdjacencyCct_Type = Integer32
_WfXnsBaseAdjacencyCct_Object = MibTableColumn
wfXnsBaseAdjacencyCct = _WfXnsBaseAdjacencyCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 8, 1, 6),
    _WfXnsBaseAdjacencyCct_Type()
)
wfXnsBaseAdjacencyCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseAdjacencyCct.setStatus("mandatory")
_WfXnsAggrStats_ObjectIdentity = ObjectIdentity
wfXnsAggrStats = _WfXnsAggrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9)
)
_WfXnsAggrInDatagrams_Type = Counter32
_WfXnsAggrInDatagrams_Object = MibScalar
wfXnsAggrInDatagrams = _WfXnsAggrInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 1),
    _WfXnsAggrInDatagrams_Type()
)
wfXnsAggrInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrInDatagrams.setStatus("mandatory")
_WfXnsAggrOutDatagrams_Type = Counter32
_WfXnsAggrOutDatagrams_Object = MibScalar
wfXnsAggrOutDatagrams = _WfXnsAggrOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 2),
    _WfXnsAggrOutDatagrams_Type()
)
wfXnsAggrOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrOutDatagrams.setStatus("mandatory")
_WfXnsAggrFwdDatagrams_Type = Counter32
_WfXnsAggrFwdDatagrams_Object = MibScalar
wfXnsAggrFwdDatagrams = _WfXnsAggrFwdDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 3),
    _WfXnsAggrFwdDatagrams_Type()
)
wfXnsAggrFwdDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrFwdDatagrams.setStatus("mandatory")
_WfXnsAggrInDiscards_Type = Counter32
_WfXnsAggrInDiscards_Object = MibScalar
wfXnsAggrInDiscards = _WfXnsAggrInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 4),
    _WfXnsAggrInDiscards_Type()
)
wfXnsAggrInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrInDiscards.setStatus("mandatory")
_WfXnsAggrInHdrErrs_Type = Counter32
_WfXnsAggrInHdrErrs_Object = MibScalar
wfXnsAggrInHdrErrs = _WfXnsAggrInHdrErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 5),
    _WfXnsAggrInHdrErrs_Type()
)
wfXnsAggrInHdrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrInHdrErrs.setStatus("mandatory")
_WfXnsAggrInAddrErrs_Type = Counter32
_WfXnsAggrInAddrErrs_Object = MibScalar
wfXnsAggrInAddrErrs = _WfXnsAggrInAddrErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 6),
    _WfXnsAggrInAddrErrs_Type()
)
wfXnsAggrInAddrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrInAddrErrs.setStatus("mandatory")
_WfXnsAggrInUnknownProtos_Type = Counter32
_WfXnsAggrInUnknownProtos_Object = MibScalar
wfXnsAggrInUnknownProtos = _WfXnsAggrInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 7),
    _WfXnsAggrInUnknownProtos_Type()
)
wfXnsAggrInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrInUnknownProtos.setStatus("mandatory")
_WfXnsAggrOutDiscards_Type = Counter32
_WfXnsAggrOutDiscards_Object = MibScalar
wfXnsAggrOutDiscards = _WfXnsAggrOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 8),
    _WfXnsAggrOutDiscards_Type()
)
wfXnsAggrOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrOutDiscards.setStatus("mandatory")
_WfXnsAggrOutNoRoutes_Type = Counter32
_WfXnsAggrOutNoRoutes_Object = MibScalar
wfXnsAggrOutNoRoutes = _WfXnsAggrOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 9, 9),
    _WfXnsAggrOutNoRoutes_Type()
)
wfXnsAggrOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAggrOutNoRoutes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-XNS-MIB",
    **{"wfXnsBase": wfXnsBase,
       "wfXnsBaseDelete": wfXnsBaseDelete,
       "wfXnsBaseDisable": wfXnsBaseDisable,
       "wfXnsBaseState": wfXnsBaseState,
       "wfXnsBaseCfgHostNumber": wfXnsBaseCfgHostNumber,
       "wfXnsBaseActiveHostNumber": wfXnsBaseActiveHostNumber,
       "wfXnsBaseImplement": wfXnsBaseImplement,
       "wfXnsBaseNetCount": wfXnsBaseNetCount,
       "wfXnsBaseHostCount": wfXnsBaseHostCount,
       "wfXnsBaseLogFilter": wfXnsBaseLogFilter,
       "wfXnsBaseRtEntryTable": wfXnsBaseRtEntryTable,
       "wfXnsBaseRtEntry": wfXnsBaseRtEntry,
       "wfXnsBaseRouteDest": wfXnsBaseRouteDest,
       "wfXnsBaseRouteIfIndex": wfXnsBaseRouteIfIndex,
       "wfXnsBaseRouteMetric": wfXnsBaseRouteMetric,
       "wfXnsBaseRouteNextHopNetwork": wfXnsBaseRouteNextHopNetwork,
       "wfXnsBaseRouteNextHopHost": wfXnsBaseRouteNextHopHost,
       "wfXnsBaseRouteType": wfXnsBaseRouteType,
       "wfXnsBaseRouteProto": wfXnsBaseRouteProto,
       "wfXnsBaseRouteAge": wfXnsBaseRouteAge,
       "wfXnsBaseRouteInfo": wfXnsBaseRouteInfo,
       "wfXnsInterfaceTable": wfXnsInterfaceTable,
       "wfXnsInterfaceEntry": wfXnsInterfaceEntry,
       "wfXnsInterfaceIndex": wfXnsInterfaceIndex,
       "wfXnsInterfaceDelete": wfXnsInterfaceDelete,
       "wfXnsInterfaceDisable": wfXnsInterfaceDisable,
       "wfXnsInterfaceState": wfXnsInterfaceState,
       "wfXnsInterfaceCircuit": wfXnsInterfaceCircuit,
       "wfXnsInterfaceNetworkNumber": wfXnsInterfaceNetworkNumber,
       "wfXnsInterfaceCost": wfXnsInterfaceCost,
       "wfXnsInterfaceXsumOn": wfXnsInterfaceXsumOn,
       "wfXnsInterfaceEncaps": wfXnsInterfaceEncaps,
       "wfXnsInterfaceMacAddress": wfXnsInterfaceMacAddress,
       "wfXnsInterfaceSMDSGroupAddress": wfXnsInterfaceSMDSGroupAddress,
       "wfXnsInterfaceMaxInfo": wfXnsInterfaceMaxInfo,
       "wfXnsInterfaceExtServer": wfXnsInterfaceExtServer,
       "wfXnsInterfaceExServNetwork": wfXnsInterfaceExServNetwork,
       "wfXnsInterfaceExServHostId": wfXnsInterfaceExServHostId,
       "wfXnsInterfaceExServPktType": wfXnsInterfaceExServPktType,
       "wfXnsInterfaceExServSockNm": wfXnsInterfaceExServSockNm,
       "wfXnsInterfaceInReceives": wfXnsInterfaceInReceives,
       "wfXnsInterfaceInHdrErrors": wfXnsInterfaceInHdrErrors,
       "wfXnsInterfaceInAddrErrors": wfXnsInterfaceInAddrErrors,
       "wfXnsInterfaceForwDatagrams": wfXnsInterfaceForwDatagrams,
       "wfXnsInterfaceInUnknownProtos": wfXnsInterfaceInUnknownProtos,
       "wfXnsInterfaceInDiscards": wfXnsInterfaceInDiscards,
       "wfXnsInterfaceInDelivers": wfXnsInterfaceInDelivers,
       "wfXnsInterfaceOutRequests": wfXnsInterfaceOutRequests,
       "wfXnsInterfaceOutDiscards": wfXnsInterfaceOutDiscards,
       "wfXnsInterfaceOutNoRoutes": wfXnsInterfaceOutNoRoutes,
       "wfXnsInterfaceFRBcast": wfXnsInterfaceFRBcast,
       "wfXnsInterfaceFRMcast": wfXnsInterfaceFRMcast,
       "wfXnsInterfaceSplit": wfXnsInterfaceSplit,
       "wfXnsRipIntfTable": wfXnsRipIntfTable,
       "wfXnsRipIntfEntry": wfXnsRipIntfEntry,
       "wfXnsRipInterfaceDelete": wfXnsRipInterfaceDelete,
       "wfXnsRipInterfaceDisable": wfXnsRipInterfaceDisable,
       "wfXnsRipInterfaceState": wfXnsRipInterfaceState,
       "wfXnsRipInterfaceIndex": wfXnsRipInterfaceIndex,
       "wfXnsRipInterfaceSupply": wfXnsRipInterfaceSupply,
       "wfXnsRipInterfaceListen": wfXnsRipInterfaceListen,
       "wfXnsAdjacentHostTable": wfXnsAdjacentHostTable,
       "wfXnsAdjacentHostEntry": wfXnsAdjacentHostEntry,
       "wfXnsAhDelete": wfXnsAhDelete,
       "wfXnsAhDisable": wfXnsAhDisable,
       "wfXnsAhTargHostNetwork": wfXnsAhTargHostNetwork,
       "wfXnsAhTargHostId": wfXnsAhTargHostId,
       "wfXnsAhNextHopIntf": wfXnsAhNextHopIntf,
       "wfXnsAhDlci": wfXnsAhDlci,
       "wfXnsStaticRouteTable": wfXnsStaticRouteTable,
       "wfXnsStaticRouteEntry": wfXnsStaticRouteEntry,
       "wfXnsSrDelete": wfXnsSrDelete,
       "wfXnsSrDisable": wfXnsSrDisable,
       "wfXnsSrTargNetwork": wfXnsSrTargNetwork,
       "wfXnsSrCost": wfXnsSrCost,
       "wfXnsSrNextHopNetwork": wfXnsSrNextHopNetwork,
       "wfXnsSrNextHopHost": wfXnsSrNextHopHost,
       "wfXnsSrTargNetworkRt": wfXnsSrTargNetworkRt,
       "wfXnsTrafficFilterTable": wfXnsTrafficFilterTable,
       "wfXnsTrafficFilterEntry": wfXnsTrafficFilterEntry,
       "wfXnsTrafficFilterCreate": wfXnsTrafficFilterCreate,
       "wfXnsTrafficFilterEnable": wfXnsTrafficFilterEnable,
       "wfXnsTrafficFilterStatus": wfXnsTrafficFilterStatus,
       "wfXnsTrafficFilterCounter": wfXnsTrafficFilterCounter,
       "wfXnsTrafficFilterDefinition": wfXnsTrafficFilterDefinition,
       "wfXnsTrafficFilterReserved": wfXnsTrafficFilterReserved,
       "wfXnsTrafficFilterInterface": wfXnsTrafficFilterInterface,
       "wfXnsTrafficFilterCircuit": wfXnsTrafficFilterCircuit,
       "wfXnsTrafficFilterRuleNumber": wfXnsTrafficFilterRuleNumber,
       "wfXnsTrafficFilterFragment": wfXnsTrafficFilterFragment,
       "wfXnsTrafficFilterName": wfXnsTrafficFilterName,
       "wfXnsBaseAdjEntryTable": wfXnsBaseAdjEntryTable,
       "wfXnsBaseAdjEntry": wfXnsBaseAdjEntry,
       "wfXnsBaseAdjacencyNetwork": wfXnsBaseAdjacencyNetwork,
       "wfXnsBaseAdjacencyHostid": wfXnsBaseAdjacencyHostid,
       "wfXnsBaseAdjacencyCost": wfXnsBaseAdjacencyCost,
       "wfXnsBaseAdjacencyAge": wfXnsBaseAdjacencyAge,
       "wfXnsBaseAdjacencyIntf": wfXnsBaseAdjacencyIntf,
       "wfXnsBaseAdjacencyCct": wfXnsBaseAdjacencyCct,
       "wfXnsAggrStats": wfXnsAggrStats,
       "wfXnsAggrInDatagrams": wfXnsAggrInDatagrams,
       "wfXnsAggrOutDatagrams": wfXnsAggrOutDatagrams,
       "wfXnsAggrFwdDatagrams": wfXnsAggrFwdDatagrams,
       "wfXnsAggrInDiscards": wfXnsAggrInDiscards,
       "wfXnsAggrInHdrErrs": wfXnsAggrInHdrErrs,
       "wfXnsAggrInAddrErrs": wfXnsAggrInAddrErrs,
       "wfXnsAggrInUnknownProtos": wfXnsAggrInUnknownProtos,
       "wfXnsAggrOutDiscards": wfXnsAggrOutDiscards,
       "wfXnsAggrOutNoRoutes": wfXnsAggrOutNoRoutes}
)
