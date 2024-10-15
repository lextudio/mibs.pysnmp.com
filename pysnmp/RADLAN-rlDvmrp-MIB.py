# SNMP MIB module (RADLAN-rlDvmrp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-rlDvmrp-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:09 2024
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

(dvmrpRouteNextHopEntry,
 dvmrpRouteNextHopIfIndex,
 dvmrpRouteNextHopSource,
 dvmrpRouteNextHopSourceMask) = mibBuilder.importSymbols(
    "DVMRP-STD-MIB",
    "dvmrpRouteNextHopEntry",
    "dvmrpRouteNextHopIfIndex",
    "dvmrpRouteNextHopSource",
    "dvmrpRouteNextHopSourceMask")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rnd,
 rndNotifications) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd",
    "rndNotifications")

(rlIPmulticast,) = mibBuilder.importSymbols(
    "RADLAN-rlIPMulticast-MIB",
    "rlIPmulticast")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDvmrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46, 4)
)
rlDvmrp.setRevisions(
        ("2004-04-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDvmrpMibVersion_Type = Integer32
_RlDvmrpMibVersion_Object = MibScalar
rlDvmrpMibVersion = _RlDvmrpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 2),
    _RlDvmrpMibVersion_Type()
)
rlDvmrpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDvmrpMibVersion.setStatus("current")


class _RlDvmrpEnable_Type(Integer32):
    """Custom type rlDvmrpEnable based on Integer32"""
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


_RlDvmrpEnable_Type.__name__ = "Integer32"
_RlDvmrpEnable_Object = MibScalar
rlDvmrpEnable = _RlDvmrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 3),
    _RlDvmrpEnable_Type()
)
rlDvmrpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDvmrpEnable.setStatus("current")


class _RlDvmrpProbeInterval_Type(Integer32):
    """Custom type rlDvmrpProbeInterval based on Integer32"""
    defaultValue = 10


_RlDvmrpProbeInterval_Object = MibScalar
rlDvmrpProbeInterval = _RlDvmrpProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 4),
    _RlDvmrpProbeInterval_Type()
)
rlDvmrpProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDvmrpProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlDvmrpProbeInterval.setUnits("seconds")


class _RlDvmrpNeighborTimeOutInterval_Type(Integer32):
    """Custom type rlDvmrpNeighborTimeOutInterval based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 400),
    )


_RlDvmrpNeighborTimeOutInterval_Type.__name__ = "Integer32"
_RlDvmrpNeighborTimeOutInterval_Object = MibScalar
rlDvmrpNeighborTimeOutInterval = _RlDvmrpNeighborTimeOutInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 5),
    _RlDvmrpNeighborTimeOutInterval_Type()
)
rlDvmrpNeighborTimeOutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDvmrpNeighborTimeOutInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlDvmrpNeighborTimeOutInterval.setUnits("seconds")


class _RlDvmrpMinFlashUpdateInterval_Type(Integer32):
    """Custom type rlDvmrpMinFlashUpdateInterval based on Integer32"""
    defaultValue = 5


_RlDvmrpMinFlashUpdateInterval_Object = MibScalar
rlDvmrpMinFlashUpdateInterval = _RlDvmrpMinFlashUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 6),
    _RlDvmrpMinFlashUpdateInterval_Type()
)
rlDvmrpMinFlashUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDvmrpMinFlashUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlDvmrpMinFlashUpdateInterval.setUnits("seconds")


class _RlDvmrpRouteReportInterval_Type(Integer32):
    """Custom type rlDvmrpRouteReportInterval based on Integer32"""
    defaultValue = 60


_RlDvmrpRouteReportInterval_Object = MibScalar
rlDvmrpRouteReportInterval = _RlDvmrpRouteReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 7),
    _RlDvmrpRouteReportInterval_Type()
)
rlDvmrpRouteReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDvmrpRouteReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlDvmrpRouteReportInterval.setUnits("seconds")


class _RlDvmrpRouteExpirationTime_Type(Integer32):
    """Custom type rlDvmrpRouteExpirationTime based on Integer32"""
    defaultValue = 140


_RlDvmrpRouteExpirationTime_Object = MibScalar
rlDvmrpRouteExpirationTime = _RlDvmrpRouteExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 8),
    _RlDvmrpRouteExpirationTime_Type()
)
rlDvmrpRouteExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDvmrpRouteExpirationTime.setStatus("current")
if mibBuilder.loadTexts:
    rlDvmrpRouteExpirationTime.setUnits("seconds")


class _RlDvmrpPruneLifetime_Type(Integer32):
    """Custom type rlDvmrpPruneLifetime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 7200),
    )


_RlDvmrpPruneLifetime_Type.__name__ = "Integer32"
_RlDvmrpPruneLifetime_Object = MibScalar
rlDvmrpPruneLifetime = _RlDvmrpPruneLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 9),
    _RlDvmrpPruneLifetime_Type()
)
rlDvmrpPruneLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDvmrpPruneLifetime.setStatus("current")
if mibBuilder.loadTexts:
    rlDvmrpPruneLifetime.setUnits("seconds")
_RlDvmrpRouteDesignatedForwarderExtTable_Object = MibTable
rlDvmrpRouteDesignatedForwarderExtTable = _RlDvmrpRouteDesignatedForwarderExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 10)
)
if mibBuilder.loadTexts:
    rlDvmrpRouteDesignatedForwarderExtTable.setStatus("current")
_RlDvmrpRouteDesignatedForwarderExtEntry_Object = MibTableRow
rlDvmrpRouteDesignatedForwarderExtEntry = _RlDvmrpRouteDesignatedForwarderExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 10, 1)
)
if mibBuilder.loadTexts:
    rlDvmrpRouteDesignatedForwarderExtEntry.setStatus("current")
_RlDvmrpRouteDesignatedForwarder_Type = IpAddress
_RlDvmrpRouteDesignatedForwarder_Object = MibTableColumn
rlDvmrpRouteDesignatedForwarder = _RlDvmrpRouteDesignatedForwarder_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 4, 10, 1, 1),
    _RlDvmrpRouteDesignatedForwarder_Type()
)
rlDvmrpRouteDesignatedForwarder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDvmrpRouteDesignatedForwarder.setStatus("current")
dvmrpRouteNextHopEntry.registerAugmentions(
    ("RADLAN-rlDvmrp-MIB",
     "rlDvmrpRouteDesignatedForwarderExtEntry")
)
rlDvmrpRouteDesignatedForwarderExtEntry.setIndexNames(*dvmrpRouteNextHopEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rlDvmrpTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 155)
)
rlDvmrpTableOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlDvmrpTableOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-rlDvmrp-MIB",
    **{"rlDvmrpTableOverflow": rlDvmrpTableOverflow,
       "rlDvmrp": rlDvmrp,
       "rlDvmrpMibVersion": rlDvmrpMibVersion,
       "rlDvmrpEnable": rlDvmrpEnable,
       "rlDvmrpProbeInterval": rlDvmrpProbeInterval,
       "rlDvmrpNeighborTimeOutInterval": rlDvmrpNeighborTimeOutInterval,
       "rlDvmrpMinFlashUpdateInterval": rlDvmrpMinFlashUpdateInterval,
       "rlDvmrpRouteReportInterval": rlDvmrpRouteReportInterval,
       "rlDvmrpRouteExpirationTime": rlDvmrpRouteExpirationTime,
       "rlDvmrpPruneLifetime": rlDvmrpPruneLifetime,
       "rlDvmrpRouteDesignatedForwarderExtTable": rlDvmrpRouteDesignatedForwarderExtTable,
       "rlDvmrpRouteDesignatedForwarderExtEntry": rlDvmrpRouteDesignatedForwarderExtEntry,
       "rlDvmrpRouteDesignatedForwarder": rlDvmrpRouteDesignatedForwarder}
)
