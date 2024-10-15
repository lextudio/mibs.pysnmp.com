# SNMP MIB module (ACC-FAKE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-FAKE
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:44 2024
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

(acc,) = mibBuilder.importSymbols(
    "ACC-MIB",
    "acc")

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



class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""




class AreaID(IpAddress):
    """Custom type AreaID based on IpAddress"""




class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class RouterID(IpAddress):
    """Custom type RouterID based on IpAddress"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class Status(Integer32):
    """Custom type Status based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccFake_ObjectIdentity = ObjectIdentity
accFake = _AccFake_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 2)
)


class _IfOperStatus_Type(Integer32):
    """Custom type ifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_IfOperStatus_Type.__name__ = "Integer32"
_IfOperStatus_Object = MibScalar
ifOperStatus = _IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 1),
    _IfOperStatus_Type()
)
ifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOperStatus.setStatus("mandatory")
_FrCircuitDlci_Type = DLCI
_FrCircuitDlci_Object = MibScalar
frCircuitDlci = _FrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 2),
    _FrCircuitDlci_Type()
)
frCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitDlci.setStatus("mandatory")
_OspfIfIpAddress_Type = IpAddress
_OspfIfIpAddress_Object = MibScalar
ospfIfIpAddress = _OspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 3),
    _OspfIfIpAddress_Type()
)
ospfIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfIpAddress.setStatus("mandatory")
_OspfAddressLessIf_Type = Integer32
_OspfAddressLessIf_Object = MibScalar
ospfAddressLessIf = _OspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 4),
    _OspfAddressLessIf_Type()
)
ospfAddressLessIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAddressLessIf.setStatus("mandatory")
_OspfAreaId_Type = AreaID
_OspfAreaId_Object = MibScalar
ospfAreaId = _OspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 5),
    _OspfAreaId_Type()
)
ospfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaId.setStatus("mandatory")


class _OspfIfType_Type(Integer32):
    """Custom type ospfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3))
    )


_OspfIfType_Type.__name__ = "Integer32"
_OspfIfType_Object = MibScalar
ospfIfType = _OspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 6),
    _OspfIfType_Type()
)
ospfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfType.setStatus("mandatory")
_OspfVirtIfAreaId_Type = AreaID
_OspfVirtIfAreaId_Object = MibScalar
ospfVirtIfAreaId = _OspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 7),
    _OspfVirtIfAreaId_Type()
)
ospfVirtIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfAreaId.setStatus("mandatory")
_OspfVirtIfNeighbor_Type = RouterID
_OspfVirtIfNeighbor_Object = MibScalar
ospfVirtIfNeighbor = _OspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 8),
    _OspfVirtIfNeighbor_Type()
)
ospfVirtIfNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfNeighbor.setStatus("mandatory")
_OspfVirtNbrArea_Type = AreaID
_OspfVirtNbrArea_Object = MibScalar
ospfVirtNbrArea = _OspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 9),
    _OspfVirtNbrArea_Type()
)
ospfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrArea.setStatus("mandatory")
_OspfRouterId_Type = RouterID
_OspfRouterId_Object = MibScalar
ospfRouterId = _OspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 10),
    _OspfRouterId_Type()
)
ospfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRouterId.setStatus("mandatory")
_OspfASBdrRtrStatus_Type = TruthValue
_OspfASBdrRtrStatus_Object = MibScalar
ospfASBdrRtrStatus = _OspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 11),
    _OspfASBdrRtrStatus_Type()
)
ospfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfASBdrRtrStatus.setStatus("mandatory")
_OspfTOSSupport_Type = TruthValue
_OspfTOSSupport_Object = MibScalar
ospfTOSSupport = _OspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 12),
    _OspfTOSSupport_Type()
)
ospfTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfTOSSupport.setStatus("mandatory")
_OspfAdminStat_Type = Status
_OspfAdminStat_Object = MibScalar
ospfAdminStat = _OspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 13),
    _OspfAdminStat_Type()
)
ospfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAdminStat.setStatus("mandatory")
_OspfNbrIpAddr_Type = IpAddress
_OspfNbrIpAddr_Object = MibScalar
ospfNbrIpAddr = _OspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 14),
    _OspfNbrIpAddr_Type()
)
ospfNbrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbrIpAddr.setStatus("mandatory")


class _OspfLsdbType_Type(Integer32):
    """Custom type ospfLsdbType based on Integer32"""
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
        *(("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("networkLink", 2),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_OspfLsdbType_Type.__name__ = "Integer32"
_OspfLsdbType_Object = MibScalar
ospfLsdbType = _OspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 15),
    _OspfLsdbType_Type()
)
ospfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbType.setStatus("mandatory")
_OspfLsdbAreaId_Type = AreaID
_OspfLsdbAreaId_Object = MibScalar
ospfLsdbAreaId = _OspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 16),
    _OspfLsdbAreaId_Type()
)
ospfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbAreaId.setStatus("mandatory")
_OspfNbrAddressLessIndex_Type = InterfaceIndex
_OspfNbrAddressLessIndex_Object = MibScalar
ospfNbrAddressLessIndex = _OspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 17),
    _OspfNbrAddressLessIndex_Type()
)
ospfNbrAddressLessIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbrAddressLessIndex.setStatus("mandatory")
_OspfMulticastExtensions_Type = Integer32
_OspfMulticastExtensions_Object = MibScalar
ospfMulticastExtensions = _OspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 18),
    _OspfMulticastExtensions_Type()
)
ospfMulticastExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfMulticastExtensions.setStatus("current")
_OspfAreaAggregateAreaID_Type = AreaID
_OspfAreaAggregateAreaID_Object = MibScalar
ospfAreaAggregateAreaID = _OspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 19),
    _OspfAreaAggregateAreaID_Type()
)
ospfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAggregateAreaID.setStatus("current")
_OspfAreaAggregateNet_Type = IpAddress
_OspfAreaAggregateNet_Object = MibScalar
ospfAreaAggregateNet = _OspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 20),
    _OspfAreaAggregateNet_Type()
)
ospfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAggregateNet.setStatus("current")
_OspfAreaAggregateMask_Type = IpAddress
_OspfAreaAggregateMask_Object = MibScalar
ospfAreaAggregateMask = _OspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 21),
    _OspfAreaAggregateMask_Type()
)
ospfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAggregateMask.setStatus("current")
_IpCidrRouteDest_Type = IpAddress
_IpCidrRouteDest_Object = MibScalar
ipCidrRouteDest = _IpCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 22),
    _IpCidrRouteDest_Type()
)
ipCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteDest.setStatus("current")
_IpCidrRouteMask_Type = IpAddress
_IpCidrRouteMask_Object = MibScalar
ipCidrRouteMask = _IpCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 23),
    _IpCidrRouteMask_Type()
)
ipCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteMask.setStatus("current")
_IpCidrRouteTos_Type = Integer32
_IpCidrRouteTos_Object = MibScalar
ipCidrRouteTos = _IpCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 24),
    _IpCidrRouteTos_Type()
)
ipCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteTos.setStatus("current")
_IpCidrRouteNextHop_Type = IpAddress
_IpCidrRouteNextHop_Object = MibScalar
ipCidrRouteNextHop = _IpCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 25),
    _IpCidrRouteNextHop_Type()
)
ipCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteNextHop.setStatus("current")
_IfName_Type = DisplayString
_IfName_Object = MibScalar
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 5, 2, 26),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-FAKE",
    **{"DLCI": DLCI,
       "AreaID": AreaID,
       "InterfaceIndex": InterfaceIndex,
       "RouterID": RouterID,
       "TruthValue": TruthValue,
       "Status": Status,
       "accFake": accFake,
       "ifOperStatus": ifOperStatus,
       "frCircuitDlci": frCircuitDlci,
       "ospfIfIpAddress": ospfIfIpAddress,
       "ospfAddressLessIf": ospfAddressLessIf,
       "ospfAreaId": ospfAreaId,
       "ospfIfType": ospfIfType,
       "ospfVirtIfAreaId": ospfVirtIfAreaId,
       "ospfVirtIfNeighbor": ospfVirtIfNeighbor,
       "ospfVirtNbrArea": ospfVirtNbrArea,
       "ospfRouterId": ospfRouterId,
       "ospfASBdrRtrStatus": ospfASBdrRtrStatus,
       "ospfTOSSupport": ospfTOSSupport,
       "ospfAdminStat": ospfAdminStat,
       "ospfNbrIpAddr": ospfNbrIpAddr,
       "ospfLsdbType": ospfLsdbType,
       "ospfLsdbAreaId": ospfLsdbAreaId,
       "ospfNbrAddressLessIndex": ospfNbrAddressLessIndex,
       "ospfMulticastExtensions": ospfMulticastExtensions,
       "ospfAreaAggregateAreaID": ospfAreaAggregateAreaID,
       "ospfAreaAggregateNet": ospfAreaAggregateNet,
       "ospfAreaAggregateMask": ospfAreaAggregateMask,
       "ipCidrRouteDest": ipCidrRouteDest,
       "ipCidrRouteMask": ipCidrRouteMask,
       "ipCidrRouteTos": ipCidrRouteTos,
       "ipCidrRouteNextHop": ipCidrRouteNextHop,
       "ifName": ifName}
)
