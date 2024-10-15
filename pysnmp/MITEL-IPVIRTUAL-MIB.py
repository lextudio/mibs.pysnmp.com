# SNMP MIB module (MITEL-IPVIRTUAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-IPVIRTUAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:22 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelIpGrpIpVirtualGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4)
)
mitelIpGrpIpVirtualGroup.setRevisions(
        ("2003-03-24 09:31",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelRouterIpGroup_ObjectIdentity = ObjectIdentity
mitelRouterIpGroup = _MitelRouterIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1)
)
_MitelIpVGrpPortTable_Object = MibTable
mitelIpVGrpPortTable = _MitelIpVGrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mitelIpVGrpPortTable.setStatus("current")
_MitelIpVGrpPortEntry_Object = MibTableRow
mitelIpVGrpPortEntry = _MitelIpVGrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1)
)
mitelIpVGrpPortEntry.setIndexNames(
    (0, "MITEL-IPVIRTUAL-MIB", "mitelIpVGrpPortTableNetAddr"),
    (0, "MITEL-IPVIRTUAL-MIB", "mitelIpVGrpPortTableIfIndex"),
)
if mibBuilder.loadTexts:
    mitelIpVGrpPortEntry.setStatus("current")
_MitelIpVGrpPortTableNetAddr_Type = IpAddress
_MitelIpVGrpPortTableNetAddr_Object = MibTableColumn
mitelIpVGrpPortTableNetAddr = _MitelIpVGrpPortTableNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 1),
    _MitelIpVGrpPortTableNetAddr_Type()
)
mitelIpVGrpPortTableNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIpVGrpPortTableNetAddr.setStatus("current")
_MitelIpVGrpPortTableNetMask_Type = IpAddress
_MitelIpVGrpPortTableNetMask_Object = MibTableColumn
mitelIpVGrpPortTableNetMask = _MitelIpVGrpPortTableNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 2),
    _MitelIpVGrpPortTableNetMask_Type()
)
mitelIpVGrpPortTableNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpVGrpPortTableNetMask.setStatus("current")
_MitelIpVGrpPortTableIfIndex_Type = Integer32
_MitelIpVGrpPortTableIfIndex_Object = MibTableColumn
mitelIpVGrpPortTableIfIndex = _MitelIpVGrpPortTableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 11),
    _MitelIpVGrpPortTableIfIndex_Type()
)
mitelIpVGrpPortTableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIpVGrpPortTableIfIndex.setStatus("current")
_MitelIpVGrpPortTableStatus_Type = RowStatus
_MitelIpVGrpPortTableStatus_Object = MibTableColumn
mitelIpVGrpPortTableStatus = _MitelIpVGrpPortTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 12),
    _MitelIpVGrpPortTableStatus_Type()
)
mitelIpVGrpPortTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelIpVGrpPortTableStatus.setStatus("current")


class _MitelIpVGrpPortTableCfgMethod_Type(Integer32):
    """Custom type mitelIpVGrpPortTableCfgMethod based on Integer32"""
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
        *(("addressless", 2),
          ("dhcp", 3),
          ("ipcp", 4),
          ("static", 1))
    )


_MitelIpVGrpPortTableCfgMethod_Type.__name__ = "Integer32"
_MitelIpVGrpPortTableCfgMethod_Object = MibTableColumn
mitelIpVGrpPortTableCfgMethod = _MitelIpVGrpPortTableCfgMethod_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 15),
    _MitelIpVGrpPortTableCfgMethod_Type()
)
mitelIpVGrpPortTableCfgMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpVGrpPortTableCfgMethod.setStatus("current")
_MitelIpVGrpRipTable_Object = MibTable
mitelIpVGrpRipTable = _MitelIpVGrpRipTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mitelIpVGrpRipTable.setStatus("current")
_MitelIpVGrpRipEntry_Object = MibTableRow
mitelIpVGrpRipEntry = _MitelIpVGrpRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1)
)
mitelIpVGrpRipEntry.setIndexNames(
    (0, "MITEL-IPVIRTUAL-MIB", "mitelIpVGrpTableRipIpAddr"),
)
if mibBuilder.loadTexts:
    mitelIpVGrpRipEntry.setStatus("current")
_MitelIpVGrpTableRipIpAddr_Type = IpAddress
_MitelIpVGrpTableRipIpAddr_Object = MibTableColumn
mitelIpVGrpTableRipIpAddr = _MitelIpVGrpTableRipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 1),
    _MitelIpVGrpTableRipIpAddr_Type()
)
mitelIpVGrpTableRipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIpVGrpTableRipIpAddr.setStatus("current")
_MitelIpVGrpTableRipRxPkts_Type = Counter32
_MitelIpVGrpTableRipRxPkts_Object = MibTableColumn
mitelIpVGrpTableRipRxPkts = _MitelIpVGrpTableRipRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 2),
    _MitelIpVGrpTableRipRxPkts_Type()
)
mitelIpVGrpTableRipRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIpVGrpTableRipRxPkts.setStatus("current")
_MitelIpVGrpTableRipRxBadPkts_Type = Counter32
_MitelIpVGrpTableRipRxBadPkts_Object = MibTableColumn
mitelIpVGrpTableRipRxBadPkts = _MitelIpVGrpTableRipRxBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 3),
    _MitelIpVGrpTableRipRxBadPkts_Type()
)
mitelIpVGrpTableRipRxBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIpVGrpTableRipRxBadPkts.setStatus("current")
_MitelIpVGrpTableRipRxBadRtes_Type = Counter32
_MitelIpVGrpTableRipRxBadRtes_Object = MibTableColumn
mitelIpVGrpTableRipRxBadRtes = _MitelIpVGrpTableRipRxBadRtes_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 4),
    _MitelIpVGrpTableRipRxBadRtes_Type()
)
mitelIpVGrpTableRipRxBadRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIpVGrpTableRipRxBadRtes.setStatus("current")
_MitelIpVGrpTableRipTxUpdates_Type = Counter32
_MitelIpVGrpTableRipTxUpdates_Object = MibTableColumn
mitelIpVGrpTableRipTxUpdates = _MitelIpVGrpTableRipTxUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 5),
    _MitelIpVGrpTableRipTxUpdates_Type()
)
mitelIpVGrpTableRipTxUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIpVGrpTableRipTxUpdates.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-IPVIRTUAL-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpGroup": mitelRouterIpGroup,
       "mitelIpGrpIpVirtualGroup": mitelIpGrpIpVirtualGroup,
       "mitelIpVGrpPortTable": mitelIpVGrpPortTable,
       "mitelIpVGrpPortEntry": mitelIpVGrpPortEntry,
       "mitelIpVGrpPortTableNetAddr": mitelIpVGrpPortTableNetAddr,
       "mitelIpVGrpPortTableNetMask": mitelIpVGrpPortTableNetMask,
       "mitelIpVGrpPortTableIfIndex": mitelIpVGrpPortTableIfIndex,
       "mitelIpVGrpPortTableStatus": mitelIpVGrpPortTableStatus,
       "mitelIpVGrpPortTableCfgMethod": mitelIpVGrpPortTableCfgMethod,
       "mitelIpVGrpRipTable": mitelIpVGrpRipTable,
       "mitelIpVGrpRipEntry": mitelIpVGrpRipEntry,
       "mitelIpVGrpTableRipIpAddr": mitelIpVGrpTableRipIpAddr,
       "mitelIpVGrpTableRipRxPkts": mitelIpVGrpTableRipRxPkts,
       "mitelIpVGrpTableRipRxBadPkts": mitelIpVGrpTableRipRxBadPkts,
       "mitelIpVGrpTableRipRxBadRtes": mitelIpVGrpTableRipRxBadRtes,
       "mitelIpVGrpTableRipTxUpdates": mitelIpVGrpTableRipTxUpdates}
)
