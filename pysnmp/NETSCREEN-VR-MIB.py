# SNMP MIB module (NETSCREEN-VR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:08 2024
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

(netscreenVR,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVR")

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

netscreenVRMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 0)
)
netscreenVRMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2001-09-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrTable_Object = MibTable
vrTable = _VrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1)
)
if mibBuilder.loadTexts:
    vrTable.setStatus("current")
_VrEntry_Object = MibTableRow
vrEntry = _VrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1)
)
vrEntry.setIndexNames(
    (0, "NETSCREEN-VR-MIB", "vrId"),
)
if mibBuilder.loadTexts:
    vrEntry.setStatus("current")
_VrName_Type = OctetString
_VrName_Object = MibTableColumn
vrName = _VrName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 1),
    _VrName_Type()
)
vrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrName.setStatus("current")


class _VrId_Type(Integer32):
    """Custom type vrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrId_Type.__name__ = "Integer32"
_VrId_Object = MibTableColumn
vrId = _VrId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 2),
    _VrId_Type()
)
vrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrId.setStatus("current")
_VrVsysName_Type = OctetString
_VrVsysName_Object = MibTableColumn
vrVsysName = _VrVsysName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 3),
    _VrVsysName_Type()
)
vrVsysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrVsysName.setStatus("current")
_VrRouteId_Type = Integer32
_VrRouteId_Object = MibTableColumn
vrRouteId = _VrRouteId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 4),
    _VrRouteId_Type()
)
vrRouteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrRouteId.setStatus("current")
_VrMaxRoutes_Type = Integer32
_VrMaxRoutes_Object = MibTableColumn
vrMaxRoutes = _VrMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 5),
    _VrMaxRoutes_Type()
)
vrMaxRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMaxRoutes.setStatus("current")
_VrNumRoutes_Type = Integer32
_VrNumRoutes_Object = MibTableColumn
vrNumRoutes = _VrNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 6),
    _VrNumRoutes_Type()
)
vrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNumRoutes.setStatus("current")
_VrSharable_Type = Integer32
_VrSharable_Object = MibTableColumn
vrSharable = _VrSharable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 7),
    _VrSharable_Type()
)
vrSharable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSharable.setStatus("current")
_VrOspfRipBgpEnabled_Type = Integer32
_VrOspfRipBgpEnabled_Object = MibTableColumn
vrOspfRipBgpEnabled = _VrOspfRipBgpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 8),
    _VrOspfRipBgpEnabled_Type()
)
vrOspfRipBgpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrOspfRipBgpEnabled.setStatus("current")
_VrTrapPrivate_Type = Integer32
_VrTrapPrivate_Object = MibTableColumn
vrTrapPrivate = _VrTrapPrivate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 1, 1, 9),
    _VrTrapPrivate_Type()
)
vrTrapPrivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrTrapPrivate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VR-MIB",
    **{"netscreenVRMibModule": netscreenVRMibModule,
       "vrTable": vrTable,
       "vrEntry": vrEntry,
       "vrName": vrName,
       "vrId": vrId,
       "vrVsysName": vrVsysName,
       "vrRouteId": vrRouteId,
       "vrMaxRoutes": vrMaxRoutes,
       "vrNumRoutes": vrNumRoutes,
       "vrSharable": vrSharable,
       "vrOspfRipBgpEnabled": vrOspfRipBgpEnabled,
       "vrTrapPrivate": vrTrapPrivate}
)
