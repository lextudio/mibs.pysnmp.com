# SNMP MIB module (XIPMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XIPMROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:41 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xipMRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XipMRouteMIBObjects_ObjectIdentity = ObjectIdentity
xipMRouteMIBObjects = _XipMRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1)
)
_XipMRoute_ObjectIdentity = ObjectIdentity
xipMRoute = _XipMRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1, 1)
)
_XipMRouteInterfaceTable_Object = MibTable
xipMRouteInterfaceTable = _XipMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xipMRouteInterfaceTable.setStatus("current")
_XipMRouteInterfaceEntry_Object = MibTableRow
xipMRouteInterfaceEntry = _XipMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1, 1, 1, 1)
)
xipMRouteInterfaceEntry.setIndexNames(
    (0, "XIPMROUTE-MIB", "xipMRouteInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    xipMRouteInterfaceEntry.setStatus("current")
_XipMRouteInterfaceIfIndex_Type = InterfaceIndex
_XipMRouteInterfaceIfIndex_Object = MibTableColumn
xipMRouteInterfaceIfIndex = _XipMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1, 1, 1, 1, 1),
    _XipMRouteInterfaceIfIndex_Type()
)
xipMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xipMRouteInterfaceIfIndex.setStatus("current")


class _XipMRouteInterfaceProtocol_Type(Integer32):
    """Custom type xipMRouteInterfaceProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dvmrp", 4),
          ("none", 0),
          ("pimDenseMode", 9))
    )


_XipMRouteInterfaceProtocol_Type.__name__ = "Integer32"
_XipMRouteInterfaceProtocol_Object = MibTableColumn
xipMRouteInterfaceProtocol = _XipMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1, 1, 1, 1, 2),
    _XipMRouteInterfaceProtocol_Type()
)
xipMRouteInterfaceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xipMRouteInterfaceProtocol.setStatus("current")


class _XipMRouteInterfaceAdminStatus_Type(Integer32):
    """Custom type xipMRouteInterfaceAdminStatus based on Integer32"""
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


_XipMRouteInterfaceAdminStatus_Type.__name__ = "Integer32"
_XipMRouteInterfaceAdminStatus_Object = MibTableColumn
xipMRouteInterfaceAdminStatus = _XipMRouteInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1, 1, 1, 1, 3),
    _XipMRouteInterfaceAdminStatus_Type()
)
xipMRouteInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xipMRouteInterfaceAdminStatus.setStatus("current")


class _XipMRouteInterfaceAddress_Type(IpAddress):
    """Custom type xipMRouteInterfaceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_XipMRouteInterfaceAddress_Object = MibTableColumn
xipMRouteInterfaceAddress = _XipMRouteInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 29, 1, 1, 1, 1, 4),
    _XipMRouteInterfaceAddress_Type()
)
xipMRouteInterfaceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xipMRouteInterfaceAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XIPMROUTE-MIB",
    **{"xipMRouteMIB": xipMRouteMIB,
       "xipMRouteMIBObjects": xipMRouteMIBObjects,
       "xipMRoute": xipMRoute,
       "xipMRouteInterfaceTable": xipMRouteInterfaceTable,
       "xipMRouteInterfaceEntry": xipMRouteInterfaceEntry,
       "xipMRouteInterfaceIfIndex": xipMRouteInterfaceIfIndex,
       "xipMRouteInterfaceProtocol": xipMRouteInterfaceProtocol,
       "xipMRouteInterfaceAdminStatus": xipMRouteInterfaceAdminStatus,
       "xipMRouteInterfaceAddress": xipMRouteInterfaceAddress}
)
