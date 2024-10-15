# SNMP MIB module (MIB-INTEL-RIP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIB-INTEL-RIP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:30 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rip_ObjectIdentity = ObjectIdentity
rip = _Rip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 39)
)
_RipIpRouteTable_Object = MibTable
ripIpRouteTable = _RipIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1)
)
if mibBuilder.loadTexts:
    ripIpRouteTable.setStatus("optional")
_RipIpRouteEntry_Object = MibTableRow
ripIpRouteEntry = _RipIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1)
)
ripIpRouteEntry.setIndexNames(
    (0, "MIB-INTEL-RIP", "ripIpRouteChassis"),
    (0, "MIB-INTEL-RIP", "ripIpRouteModule"),
    (0, "MIB-INTEL-RIP", "ripIpRouteInst"),
    (0, "MIB-INTEL-RIP", "ripIpRouteDest"),
    (0, "MIB-INTEL-RIP", "ripIpRouteMask"),
    (0, "MIB-INTEL-RIP", "ripIpIfIndex"),
    (0, "MIB-INTEL-RIP", "ripIpRouteNextHop"),
)
if mibBuilder.loadTexts:
    ripIpRouteEntry.setStatus("optional")
_RipIpRouteChassis_Type = Integer32
_RipIpRouteChassis_Object = MibTableColumn
ripIpRouteChassis = _RipIpRouteChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 1),
    _RipIpRouteChassis_Type()
)
ripIpRouteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteChassis.setStatus("optional")
_RipIpRouteModule_Type = Integer32
_RipIpRouteModule_Object = MibTableColumn
ripIpRouteModule = _RipIpRouteModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 2),
    _RipIpRouteModule_Type()
)
ripIpRouteModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteModule.setStatus("optional")
_RipIpRouteInst_Type = Integer32
_RipIpRouteInst_Object = MibTableColumn
ripIpRouteInst = _RipIpRouteInst_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 3),
    _RipIpRouteInst_Type()
)
ripIpRouteInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteInst.setStatus("optional")
_RipIpRouteDest_Type = IpAddress
_RipIpRouteDest_Object = MibTableColumn
ripIpRouteDest = _RipIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 4),
    _RipIpRouteDest_Type()
)
ripIpRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteDest.setStatus("optional")
_RipIpRouteMask_Type = IpAddress
_RipIpRouteMask_Object = MibTableColumn
ripIpRouteMask = _RipIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 5),
    _RipIpRouteMask_Type()
)
ripIpRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteMask.setStatus("optional")
_RipIpIfIndex_Type = Integer32
_RipIpIfIndex_Object = MibTableColumn
ripIpIfIndex = _RipIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 6),
    _RipIpIfIndex_Type()
)
ripIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpIfIndex.setStatus("optional")
_RipIpRouteNextHop_Type = IpAddress
_RipIpRouteNextHop_Object = MibTableColumn
ripIpRouteNextHop = _RipIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 7),
    _RipIpRouteNextHop_Type()
)
ripIpRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteNextHop.setStatus("optional")
_RipIpRoutePref_Type = Integer32
_RipIpRoutePref_Object = MibTableColumn
ripIpRoutePref = _RipIpRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 8),
    _RipIpRoutePref_Type()
)
ripIpRoutePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRoutePref.setStatus("optional")
_RipIpRouteMetric_Type = Integer32
_RipIpRouteMetric_Object = MibTableColumn
ripIpRouteMetric = _RipIpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 9),
    _RipIpRouteMetric_Type()
)
ripIpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteMetric.setStatus("optional")


class _RipIpRouteState_Type(Integer32):
    """Custom type ripIpRouteState based on Integer32"""
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


_RipIpRouteState_Type.__name__ = "Integer32"
_RipIpRouteState_Object = MibTableColumn
ripIpRouteState = _RipIpRouteState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 10),
    _RipIpRouteState_Type()
)
ripIpRouteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIpRouteState.setStatus("optional")
_RipIpRouteAge_Type = Integer32
_RipIpRouteAge_Object = MibTableColumn
ripIpRouteAge = _RipIpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 11),
    _RipIpRouteAge_Type()
)
ripIpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteAge.setStatus("optional")


class _RipIpRouteProtoVersion_Type(Integer32):
    """Custom type ripIpRouteProtoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip1", 1),
          ("rip2", 2))
    )


_RipIpRouteProtoVersion_Type.__name__ = "Integer32"
_RipIpRouteProtoVersion_Object = MibTableColumn
ripIpRouteProtoVersion = _RipIpRouteProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 12),
    _RipIpRouteProtoVersion_Type()
)
ripIpRouteProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteProtoVersion.setStatus("optional")


class _RipIpRouteProtoTrigger_Type(Integer32):
    """Custom type ripIpRouteProtoTrigger based on Integer32"""
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


_RipIpRouteProtoTrigger_Type.__name__ = "Integer32"
_RipIpRouteProtoTrigger_Object = MibTableColumn
ripIpRouteProtoTrigger = _RipIpRouteProtoTrigger_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 39, 1, 1, 13),
    _RipIpRouteProtoTrigger_Type()
)
ripIpRouteProtoTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIpRouteProtoTrigger.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-INTEL-RIP",
    **{"rip": rip,
       "ripIpRouteTable": ripIpRouteTable,
       "ripIpRouteEntry": ripIpRouteEntry,
       "ripIpRouteChassis": ripIpRouteChassis,
       "ripIpRouteModule": ripIpRouteModule,
       "ripIpRouteInst": ripIpRouteInst,
       "ripIpRouteDest": ripIpRouteDest,
       "ripIpRouteMask": ripIpRouteMask,
       "ripIpIfIndex": ripIpIfIndex,
       "ripIpRouteNextHop": ripIpRouteNextHop,
       "ripIpRoutePref": ripIpRoutePref,
       "ripIpRouteMetric": ripIpRouteMetric,
       "ripIpRouteState": ripIpRouteState,
       "ripIpRouteAge": ripIpRouteAge,
       "ripIpRouteProtoVersion": ripIpRouteProtoVersion,
       "ripIpRouteProtoTrigger": ripIpRouteProtoTrigger}
)
