# SNMP MIB module (CISCO-DMN-DSG-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-ROUTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:32 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGRouting = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40)
)
ciscoDSGRouting.setRevisions(
        ("2012-05-14 15:00",
         "2012-03-07 07:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MulticastRouteTable_Object = MibTable
multicastRouteTable = _MulticastRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 1)
)
if mibBuilder.loadTexts:
    multicastRouteTable.setStatus("current")
_MulticastRouteEntry_Object = MibTableRow
multicastRouteEntry = _MulticastRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 1, 1)
)
multicastRouteEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ROUTING-MIB", "multicastRouteIndex"),
)
if mibBuilder.loadTexts:
    multicastRouteEntry.setStatus("current")


class _MulticastRouteIndex_Type(Integer32):
    """Custom type multicastRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MulticastRouteIndex_Type.__name__ = "Integer32"
_MulticastRouteIndex_Object = MibTableColumn
multicastRouteIndex = _MulticastRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 1, 1, 1),
    _MulticastRouteIndex_Type()
)
multicastRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRouteIndex.setStatus("current")
_MulticastRouteV4IPAddr_Type = IpAddress
_MulticastRouteV4IPAddr_Object = MibTableColumn
multicastRouteV4IPAddr = _MulticastRouteV4IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 1, 1, 2),
    _MulticastRouteV4IPAddr_Type()
)
multicastRouteV4IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastRouteV4IPAddr.setStatus("current")
_MulticastRouteRowStatus_Type = RowStatus
_MulticastRouteRowStatus_Object = MibTableColumn
multicastRouteRowStatus = _MulticastRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 1, 1, 3),
    _MulticastRouteRowStatus_Type()
)
multicastRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastRouteRowStatus.setStatus("current")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1)
)
staticRouteEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ROUTING-MIB", "staticRouteIndex"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")


class _StaticRouteIndex_Type(Integer32):
    """Custom type staticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaticRouteIndex_Type.__name__ = "Integer32"
_StaticRouteIndex_Object = MibTableColumn
staticRouteIndex = _StaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 1),
    _StaticRouteIndex_Type()
)
staticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteIndex.setStatus("current")
_StaticRouteV4IPAddr_Type = IpAddress
_StaticRouteV4IPAddr_Object = MibTableColumn
staticRouteV4IPAddr = _StaticRouteV4IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 2),
    _StaticRouteV4IPAddr_Type()
)
staticRouteV4IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteV4IPAddr.setStatus("current")


class _StaticRouteV4Mask_Type(Integer32):
    """Custom type staticRouteV4Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 30),
    )


_StaticRouteV4Mask_Type.__name__ = "Integer32"
_StaticRouteV4Mask_Object = MibTableColumn
staticRouteV4Mask = _StaticRouteV4Mask_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 3),
    _StaticRouteV4Mask_Type()
)
staticRouteV4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteV4Mask.setStatus("current")
_StaticRouteV4Gateway_Type = IpAddress
_StaticRouteV4Gateway_Object = MibTableColumn
staticRouteV4Gateway = _StaticRouteV4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 4),
    _StaticRouteV4Gateway_Type()
)
staticRouteV4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteV4Gateway.setStatus("current")


class _StaticRoutePort1Enable_Type(Integer32):
    """Custom type staticRoutePort1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StaticRoutePort1Enable_Type.__name__ = "Integer32"
_StaticRoutePort1Enable_Object = MibTableColumn
staticRoutePort1Enable = _StaticRoutePort1Enable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 5),
    _StaticRoutePort1Enable_Type()
)
staticRoutePort1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRoutePort1Enable.setStatus("current")


class _StaticRoutePort2Enable_Type(Integer32):
    """Custom type staticRoutePort2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StaticRoutePort2Enable_Type.__name__ = "Integer32"
_StaticRoutePort2Enable_Object = MibTableColumn
staticRoutePort2Enable = _StaticRoutePort2Enable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 6),
    _StaticRoutePort2Enable_Type()
)
staticRoutePort2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRoutePort2Enable.setStatus("current")


class _StaticRoutePort3Enable_Type(Integer32):
    """Custom type staticRoutePort3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StaticRoutePort3Enable_Type.__name__ = "Integer32"
_StaticRoutePort3Enable_Object = MibTableColumn
staticRoutePort3Enable = _StaticRoutePort3Enable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 7),
    _StaticRoutePort3Enable_Type()
)
staticRoutePort3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRoutePort3Enable.setStatus("current")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 2, 1, 8),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("current")
_UnicastRoutesTable_Object = MibTable
unicastRoutesTable = _UnicastRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3)
)
if mibBuilder.loadTexts:
    unicastRoutesTable.setStatus("current")
_UnicastRoutesEntry_Object = MibTableRow
unicastRoutesEntry = _UnicastRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1)
)
unicastRoutesEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-ROUTING-MIB", "unicastRoutesIndex"),
)
if mibBuilder.loadTexts:
    unicastRoutesEntry.setStatus("current")


class _UnicastRoutesIndex_Type(Integer32):
    """Custom type unicastRoutesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_UnicastRoutesIndex_Type.__name__ = "Integer32"
_UnicastRoutesIndex_Object = MibTableColumn
unicastRoutesIndex = _UnicastRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 1),
    _UnicastRoutesIndex_Type()
)
unicastRoutesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesIndex.setStatus("current")


class _UnicastRoutesPortID_Type(Integer32):
    """Custom type unicastRoutesPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UnicastRoutesPortID_Type.__name__ = "Integer32"
_UnicastRoutesPortID_Object = MibTableColumn
unicastRoutesPortID = _UnicastRoutesPortID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 2),
    _UnicastRoutesPortID_Type()
)
unicastRoutesPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesPortID.setStatus("current")
_UnicastRoutesV4IPAddr_Type = IpAddress
_UnicastRoutesV4IPAddr_Object = MibTableColumn
unicastRoutesV4IPAddr = _UnicastRoutesV4IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 3),
    _UnicastRoutesV4IPAddr_Type()
)
unicastRoutesV4IPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesV4IPAddr.setStatus("current")


class _UnicastRoutesV4Mask_Type(Integer32):
    """Custom type unicastRoutesV4Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UnicastRoutesV4Mask_Type.__name__ = "Integer32"
_UnicastRoutesV4Mask_Object = MibTableColumn
unicastRoutesV4Mask = _UnicastRoutesV4Mask_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 4),
    _UnicastRoutesV4Mask_Type()
)
unicastRoutesV4Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesV4Mask.setStatus("current")
_UnicastRoutesV4Gateway_Type = IpAddress
_UnicastRoutesV4Gateway_Object = MibTableColumn
unicastRoutesV4Gateway = _UnicastRoutesV4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 5),
    _UnicastRoutesV4Gateway_Type()
)
unicastRoutesV4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesV4Gateway.setStatus("current")
_UnicastRoutesMTU_Type = Counter32
_UnicastRoutesMTU_Object = MibTableColumn
unicastRoutesMTU = _UnicastRoutesMTU_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 6),
    _UnicastRoutesMTU_Type()
)
unicastRoutesMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesMTU.setStatus("current")
_UnicastRoutesTTL_Type = Counter32
_UnicastRoutesTTL_Object = MibTableColumn
unicastRoutesTTL = _UnicastRoutesTTL_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 7),
    _UnicastRoutesTTL_Type()
)
unicastRoutesTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesTTL.setStatus("current")


class _UnicastRoutesGWOrHost_Type(Integer32):
    """Custom type unicastRoutesGWOrHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 1),
          ("host", 2))
    )


_UnicastRoutesGWOrHost_Type.__name__ = "Integer32"
_UnicastRoutesGWOrHost_Object = MibTableColumn
unicastRoutesGWOrHost = _UnicastRoutesGWOrHost_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 8),
    _UnicastRoutesGWOrHost_Type()
)
unicastRoutesGWOrHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesGWOrHost.setStatus("current")


class _UnicastRoutesType_Type(Integer32):
    """Custom type unicastRoutesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_UnicastRoutesType_Type.__name__ = "Integer32"
_UnicastRoutesType_Object = MibTableColumn
unicastRoutesType = _UnicastRoutesType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 40, 3, 1, 9),
    _UnicastRoutesType_Type()
)
unicastRoutesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastRoutesType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-ROUTING-MIB",
    **{"ciscoDSGRouting": ciscoDSGRouting,
       "multicastRouteTable": multicastRouteTable,
       "multicastRouteEntry": multicastRouteEntry,
       "multicastRouteIndex": multicastRouteIndex,
       "multicastRouteV4IPAddr": multicastRouteV4IPAddr,
       "multicastRouteRowStatus": multicastRouteRowStatus,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteIndex": staticRouteIndex,
       "staticRouteV4IPAddr": staticRouteV4IPAddr,
       "staticRouteV4Mask": staticRouteV4Mask,
       "staticRouteV4Gateway": staticRouteV4Gateway,
       "staticRoutePort1Enable": staticRoutePort1Enable,
       "staticRoutePort2Enable": staticRoutePort2Enable,
       "staticRoutePort3Enable": staticRoutePort3Enable,
       "staticRouteRowStatus": staticRouteRowStatus,
       "unicastRoutesTable": unicastRoutesTable,
       "unicastRoutesEntry": unicastRoutesEntry,
       "unicastRoutesIndex": unicastRoutesIndex,
       "unicastRoutesPortID": unicastRoutesPortID,
       "unicastRoutesV4IPAddr": unicastRoutesV4IPAddr,
       "unicastRoutesV4Mask": unicastRoutesV4Mask,
       "unicastRoutesV4Gateway": unicastRoutesV4Gateway,
       "unicastRoutesMTU": unicastRoutesMTU,
       "unicastRoutesTTL": unicastRoutesTTL,
       "unicastRoutesGWOrHost": unicastRoutesGWOrHost,
       "unicastRoutesType": unicastRoutesType}
)
