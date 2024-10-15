# SNMP MIB module (TPLINK-STATICMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-STATICMROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:44 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkStaticMrouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79)
)
tplinkStaticMrouteMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkStaticMrouteMIBObjects_ObjectIdentity = ObjectIdentity
tplinkStaticMrouteMIBObjects = _TplinkStaticMrouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1)
)
_TplinkStaticMrouteConfig_ObjectIdentity = ObjectIdentity
tplinkStaticMrouteConfig = _TplinkStaticMrouteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1)
)
_TpStaticMrouteTable_Object = MibTable
tpStaticMrouteTable = _TpStaticMrouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpStaticMrouteTable.setStatus("current")
_TpStaticMrouteEntry_Object = MibTableRow
tpStaticMrouteEntry = _TpStaticMrouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1, 1, 1)
)
tpStaticMrouteEntry.setIndexNames(
    (0, "TPLINK-STATICMROUTE-MIB", "tpStaticMrouteSource"),
    (0, "TPLINK-STATICMROUTE-MIB", "tpStaticMrouteSourceMask"),
)
if mibBuilder.loadTexts:
    tpStaticMrouteEntry.setStatus("current")
_TpStaticMrouteSource_Type = IpAddress
_TpStaticMrouteSource_Object = MibTableColumn
tpStaticMrouteSource = _TpStaticMrouteSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1, 1, 1, 1),
    _TpStaticMrouteSource_Type()
)
tpStaticMrouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticMrouteSource.setStatus("current")
_TpStaticMrouteSourceMask_Type = IpAddress
_TpStaticMrouteSourceMask_Object = MibTableColumn
tpStaticMrouteSourceMask = _TpStaticMrouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1, 1, 1, 2),
    _TpStaticMrouteSourceMask_Type()
)
tpStaticMrouteSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticMrouteSourceMask.setStatus("current")
_TpStaticMrouteRpfNeigbor_Type = IpAddress
_TpStaticMrouteRpfNeigbor_Object = MibTableColumn
tpStaticMrouteRpfNeigbor = _TpStaticMrouteRpfNeigbor_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1, 1, 1, 3),
    _TpStaticMrouteRpfNeigbor_Type()
)
tpStaticMrouteRpfNeigbor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticMrouteRpfNeigbor.setStatus("current")


class _TpStaticMrouteDistance_Type(Integer32):
    """Custom type tpStaticMrouteDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TpStaticMrouteDistance_Type.__name__ = "Integer32"
_TpStaticMrouteDistance_Object = MibTableColumn
tpStaticMrouteDistance = _TpStaticMrouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1, 1, 1, 4),
    _TpStaticMrouteDistance_Type()
)
tpStaticMrouteDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticMrouteDistance.setStatus("current")
_TpStaticMrouteStatus_Type = TPRowStatus
_TpStaticMrouteStatus_Object = MibTableColumn
tpStaticMrouteStatus = _TpStaticMrouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 1, 1, 1, 1, 5),
    _TpStaticMrouteStatus_Type()
)
tpStaticMrouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticMrouteStatus.setStatus("current")
_TplinkStaticMrouteNotifications_ObjectIdentity = ObjectIdentity
tplinkStaticMrouteNotifications = _TplinkStaticMrouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 79, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-STATICMROUTE-MIB",
    **{"tplinkStaticMrouteMIB": tplinkStaticMrouteMIB,
       "tplinkStaticMrouteMIBObjects": tplinkStaticMrouteMIBObjects,
       "tplinkStaticMrouteConfig": tplinkStaticMrouteConfig,
       "tpStaticMrouteTable": tpStaticMrouteTable,
       "tpStaticMrouteEntry": tpStaticMrouteEntry,
       "tpStaticMrouteSource": tpStaticMrouteSource,
       "tpStaticMrouteSourceMask": tpStaticMrouteSourceMask,
       "tpStaticMrouteRpfNeigbor": tpStaticMrouteRpfNeigbor,
       "tpStaticMrouteDistance": tpStaticMrouteDistance,
       "tpStaticMrouteStatus": tpStaticMrouteStatus,
       "tplinkStaticMrouteNotifications": tplinkStaticMrouteNotifications}
)
