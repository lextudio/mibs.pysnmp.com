# SNMP MIB module (MIB-INTEL-IP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIB-INTEL-IP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:28 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipr_ObjectIdentity = ObjectIdentity
ipr = _Ipr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 38)
)
_RtIpRouteTable_Object = MibTable
rtIpRouteTable = _RtIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1)
)
if mibBuilder.loadTexts:
    rtIpRouteTable.setStatus("optional")
_RtIpRouteEntry_Object = MibTableRow
rtIpRouteEntry = _RtIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1)
)
rtIpRouteEntry.setIndexNames(
    (0, "MIB-INTEL-IP", "rtIpRouteChassis"),
    (0, "MIB-INTEL-IP", "rtIpRouteModule"),
    (0, "MIB-INTEL-IP", "rtIpRouteInst"),
    (0, "MIB-INTEL-IP", "rtIpRouteDest"),
    (0, "MIB-INTEL-IP", "rtIpRouteMask"),
    (0, "MIB-INTEL-IP", "rtIpRouteIfIndex"),
    (0, "MIB-INTEL-IP", "rtIpRouteNextHop"),
)
if mibBuilder.loadTexts:
    rtIpRouteEntry.setStatus("optional")
_RtIpRouteChassis_Type = Integer32
_RtIpRouteChassis_Object = MibTableColumn
rtIpRouteChassis = _RtIpRouteChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 1),
    _RtIpRouteChassis_Type()
)
rtIpRouteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteChassis.setStatus("optional")
_RtIpRouteModule_Type = Integer32
_RtIpRouteModule_Object = MibTableColumn
rtIpRouteModule = _RtIpRouteModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 2),
    _RtIpRouteModule_Type()
)
rtIpRouteModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteModule.setStatus("optional")
_RtIpRouteInst_Type = Integer32
_RtIpRouteInst_Object = MibTableColumn
rtIpRouteInst = _RtIpRouteInst_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 3),
    _RtIpRouteInst_Type()
)
rtIpRouteInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteInst.setStatus("optional")
_RtIpRouteDest_Type = IpAddress
_RtIpRouteDest_Object = MibTableColumn
rtIpRouteDest = _RtIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 4),
    _RtIpRouteDest_Type()
)
rtIpRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteDest.setStatus("optional")
_RtIpRouteMask_Type = IpAddress
_RtIpRouteMask_Object = MibTableColumn
rtIpRouteMask = _RtIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 5),
    _RtIpRouteMask_Type()
)
rtIpRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteMask.setStatus("optional")
_RtIpRouteIfIndex_Type = Integer32
_RtIpRouteIfIndex_Object = MibTableColumn
rtIpRouteIfIndex = _RtIpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 6),
    _RtIpRouteIfIndex_Type()
)
rtIpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteIfIndex.setStatus("optional")
_RtIpRouteNextHop_Type = IpAddress
_RtIpRouteNextHop_Object = MibTableColumn
rtIpRouteNextHop = _RtIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 7),
    _RtIpRouteNextHop_Type()
)
rtIpRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteNextHop.setStatus("optional")
_RtIpRoutePref_Type = Integer32
_RtIpRoutePref_Object = MibTableColumn
rtIpRoutePref = _RtIpRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 8),
    _RtIpRoutePref_Type()
)
rtIpRoutePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRoutePref.setStatus("optional")
_RtIpRouteMetric_Type = Integer32
_RtIpRouteMetric_Object = MibTableColumn
rtIpRouteMetric = _RtIpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 9),
    _RtIpRouteMetric_Type()
)
rtIpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteMetric.setStatus("optional")


class _RtIpRouteProto_Type(Integer32):
    """Custom type rtIpRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 6),
          ("direct", 1),
          ("ospf", 3),
          ("other", 5),
          ("rip", 4),
          ("static", 2))
    )


_RtIpRouteProto_Type.__name__ = "Integer32"
_RtIpRouteProto_Object = MibTableColumn
rtIpRouteProto = _RtIpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 10),
    _RtIpRouteProto_Type()
)
rtIpRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteProto.setStatus("optional")
_RtIpRouteAge_Type = Integer32
_RtIpRouteAge_Object = MibTableColumn
rtIpRouteAge = _RtIpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 11),
    _RtIpRouteAge_Type()
)
rtIpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRouteAge.setStatus("optional")
_RtIpRteTable_Object = MibTable
rtIpRteTable = _RtIpRteTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2)
)
if mibBuilder.loadTexts:
    rtIpRteTable.setStatus("optional")
_RtIpRteEntry_Object = MibTableRow
rtIpRteEntry = _RtIpRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1)
)
rtIpRteEntry.setIndexNames(
    (0, "MIB-INTEL-IP", "rtIpRteChassis"),
    (0, "MIB-INTEL-IP", "rtIpRteModule"),
    (0, "MIB-INTEL-IP", "rtIpRteInst"),
    (0, "MIB-INTEL-IP", "rtIpRteDest"),
    (0, "MIB-INTEL-IP", "rtIpRteMask"),
    (0, "MIB-INTEL-IP", "rtIpRtePref"),
    (0, "MIB-INTEL-IP", "rtIpRteProto"),
    (0, "MIB-INTEL-IP", "rtIpRteIfIndex"),
    (0, "MIB-INTEL-IP", "rtIpRteNextHop"),
)
if mibBuilder.loadTexts:
    rtIpRteEntry.setStatus("optional")
_RtIpRteChassis_Type = Integer32
_RtIpRteChassis_Object = MibTableColumn
rtIpRteChassis = _RtIpRteChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 1),
    _RtIpRteChassis_Type()
)
rtIpRteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteChassis.setStatus("optional")
_RtIpRteModule_Type = Integer32
_RtIpRteModule_Object = MibTableColumn
rtIpRteModule = _RtIpRteModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 2),
    _RtIpRteModule_Type()
)
rtIpRteModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteModule.setStatus("optional")
_RtIpRteInst_Type = Integer32
_RtIpRteInst_Object = MibTableColumn
rtIpRteInst = _RtIpRteInst_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 3),
    _RtIpRteInst_Type()
)
rtIpRteInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteInst.setStatus("optional")
_RtIpRteDest_Type = IpAddress
_RtIpRteDest_Object = MibTableColumn
rtIpRteDest = _RtIpRteDest_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 4),
    _RtIpRteDest_Type()
)
rtIpRteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteDest.setStatus("optional")
_RtIpRteMask_Type = IpAddress
_RtIpRteMask_Object = MibTableColumn
rtIpRteMask = _RtIpRteMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 5),
    _RtIpRteMask_Type()
)
rtIpRteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteMask.setStatus("optional")
_RtIpRtePref_Type = Integer32
_RtIpRtePref_Object = MibTableColumn
rtIpRtePref = _RtIpRtePref_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 6),
    _RtIpRtePref_Type()
)
rtIpRtePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRtePref.setStatus("optional")


class _RtIpRteProto_Type(Integer32):
    """Custom type rtIpRteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 6),
          ("direct", 1),
          ("ospf", 3),
          ("other", 5),
          ("rip", 4),
          ("static", 2))
    )


_RtIpRteProto_Type.__name__ = "Integer32"
_RtIpRteProto_Object = MibTableColumn
rtIpRteProto = _RtIpRteProto_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 7),
    _RtIpRteProto_Type()
)
rtIpRteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteProto.setStatus("optional")
_RtIpRteIfIndex_Type = Integer32
_RtIpRteIfIndex_Object = MibTableColumn
rtIpRteIfIndex = _RtIpRteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 8),
    _RtIpRteIfIndex_Type()
)
rtIpRteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteIfIndex.setStatus("optional")
_RtIpRteNextHop_Type = IpAddress
_RtIpRteNextHop_Object = MibTableColumn
rtIpRteNextHop = _RtIpRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 9),
    _RtIpRteNextHop_Type()
)
rtIpRteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteNextHop.setStatus("optional")


class _RtIpRteState_Type(Integer32):
    """Custom type rtIpRteState based on Integer32"""
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


_RtIpRteState_Type.__name__ = "Integer32"
_RtIpRteState_Object = MibTableColumn
rtIpRteState = _RtIpRteState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 10),
    _RtIpRteState_Type()
)
rtIpRteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpRteState.setStatus("optional")
_RtIpRteAge_Type = Integer32
_RtIpRteAge_Object = MibTableColumn
rtIpRteAge = _RtIpRteAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 11),
    _RtIpRteAge_Type()
)
rtIpRteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIpRteAge.setStatus("optional")
_RtIpRteMetric_Type = Integer32
_RtIpRteMetric_Object = MibTableColumn
rtIpRteMetric = _RtIpRteMetric_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 12),
    _RtIpRteMetric_Type()
)
rtIpRteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpRteMetric.setStatus("optional")
_RtIpStaticRouteTable_Object = MibTable
rtIpStaticRouteTable = _RtIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3)
)
if mibBuilder.loadTexts:
    rtIpStaticRouteTable.setStatus("optional")
_RtIpStaticRouteEntry_Object = MibTableRow
rtIpStaticRouteEntry = _RtIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1)
)
rtIpStaticRouteEntry.setIndexNames(
    (0, "MIB-INTEL-IP", "rtIpStRtChassis"),
    (0, "MIB-INTEL-IP", "rtIpStRtModule"),
    (0, "MIB-INTEL-IP", "rtIpStRtInst"),
    (0, "MIB-INTEL-IP", "rtIpStRtDest"),
    (0, "MIB-INTEL-IP", "rtIpStRtMask"),
    (0, "MIB-INTEL-IP", "rtIpStRtPref"),
    (0, "MIB-INTEL-IP", "rtIpStRtIfIndex"),
    (0, "MIB-INTEL-IP", "rtIpStRtNextHop"),
)
if mibBuilder.loadTexts:
    rtIpStaticRouteEntry.setStatus("optional")
_RtIpStRtChassis_Type = Integer32
_RtIpStRtChassis_Object = MibTableColumn
rtIpStRtChassis = _RtIpStRtChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 1),
    _RtIpStRtChassis_Type()
)
rtIpStRtChassis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtChassis.setStatus("optional")
_RtIpStRtModule_Type = Integer32
_RtIpStRtModule_Object = MibTableColumn
rtIpStRtModule = _RtIpStRtModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 2),
    _RtIpStRtModule_Type()
)
rtIpStRtModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtModule.setStatus("optional")
_RtIpStRtInst_Type = Integer32
_RtIpStRtInst_Object = MibTableColumn
rtIpStRtInst = _RtIpStRtInst_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 3),
    _RtIpStRtInst_Type()
)
rtIpStRtInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtInst.setStatus("optional")
_RtIpStRtDest_Type = IpAddress
_RtIpStRtDest_Object = MibTableColumn
rtIpStRtDest = _RtIpStRtDest_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 4),
    _RtIpStRtDest_Type()
)
rtIpStRtDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtDest.setStatus("optional")
_RtIpStRtMask_Type = IpAddress
_RtIpStRtMask_Object = MibTableColumn
rtIpStRtMask = _RtIpStRtMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 5),
    _RtIpStRtMask_Type()
)
rtIpStRtMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtMask.setStatus("optional")
_RtIpStRtPref_Type = Integer32
_RtIpStRtPref_Object = MibTableColumn
rtIpStRtPref = _RtIpStRtPref_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 6),
    _RtIpStRtPref_Type()
)
rtIpStRtPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtPref.setStatus("optional")
_RtIpStRtIfIndex_Type = Integer32
_RtIpStRtIfIndex_Object = MibTableColumn
rtIpStRtIfIndex = _RtIpStRtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 7),
    _RtIpStRtIfIndex_Type()
)
rtIpStRtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtIfIndex.setStatus("optional")
_RtIpStRtNextHop_Type = IpAddress
_RtIpStRtNextHop_Object = MibTableColumn
rtIpStRtNextHop = _RtIpStRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 8),
    _RtIpStRtNextHop_Type()
)
rtIpStRtNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtNextHop.setStatus("optional")
_RtIpStRtMetric_Type = Integer32
_RtIpStRtMetric_Object = MibTableColumn
rtIpStRtMetric = _RtIpStRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 9),
    _RtIpStRtMetric_Type()
)
rtIpStRtMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtMetric.setStatus("optional")
_RtIpStRtStatus_Type = RowStatus
_RtIpStRtStatus_Object = MibTableColumn
rtIpStRtStatus = _RtIpStRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 10),
    _RtIpStRtStatus_Type()
)
rtIpStRtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtStatus.setStatus("optional")


class _RtIpStRtState_Type(Integer32):
    """Custom type rtIpStRtState based on Integer32"""
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


_RtIpStRtState_Type.__name__ = "Integer32"
_RtIpStRtState_Object = MibTableColumn
rtIpStRtState = _RtIpStRtState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 11),
    _RtIpStRtState_Type()
)
rtIpStRtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIpStRtState.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-INTEL-IP",
    **{"RowStatus": RowStatus,
       "ipr": ipr,
       "rtIpRouteTable": rtIpRouteTable,
       "rtIpRouteEntry": rtIpRouteEntry,
       "rtIpRouteChassis": rtIpRouteChassis,
       "rtIpRouteModule": rtIpRouteModule,
       "rtIpRouteInst": rtIpRouteInst,
       "rtIpRouteDest": rtIpRouteDest,
       "rtIpRouteMask": rtIpRouteMask,
       "rtIpRouteIfIndex": rtIpRouteIfIndex,
       "rtIpRouteNextHop": rtIpRouteNextHop,
       "rtIpRoutePref": rtIpRoutePref,
       "rtIpRouteMetric": rtIpRouteMetric,
       "rtIpRouteProto": rtIpRouteProto,
       "rtIpRouteAge": rtIpRouteAge,
       "rtIpRteTable": rtIpRteTable,
       "rtIpRteEntry": rtIpRteEntry,
       "rtIpRteChassis": rtIpRteChassis,
       "rtIpRteModule": rtIpRteModule,
       "rtIpRteInst": rtIpRteInst,
       "rtIpRteDest": rtIpRteDest,
       "rtIpRteMask": rtIpRteMask,
       "rtIpRtePref": rtIpRtePref,
       "rtIpRteProto": rtIpRteProto,
       "rtIpRteIfIndex": rtIpRteIfIndex,
       "rtIpRteNextHop": rtIpRteNextHop,
       "rtIpRteState": rtIpRteState,
       "rtIpRteAge": rtIpRteAge,
       "rtIpRteMetric": rtIpRteMetric,
       "rtIpStaticRouteTable": rtIpStaticRouteTable,
       "rtIpStaticRouteEntry": rtIpStaticRouteEntry,
       "rtIpStRtChassis": rtIpStRtChassis,
       "rtIpStRtModule": rtIpStRtModule,
       "rtIpStRtInst": rtIpStRtInst,
       "rtIpStRtDest": rtIpStRtDest,
       "rtIpStRtMask": rtIpStRtMask,
       "rtIpStRtPref": rtIpStRtPref,
       "rtIpStRtIfIndex": rtIpStRtIfIndex,
       "rtIpStRtNextHop": rtIpStRtNextHop,
       "rtIpStRtMetric": rtIpStRtMetric,
       "rtIpStRtStatus": rtIpStRtStatus,
       "rtIpStRtState": rtIpStRtState}
)
