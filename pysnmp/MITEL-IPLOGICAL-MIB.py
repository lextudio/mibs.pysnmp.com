# SNMP MIB module (MITEL-IPLOGICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-IPLOGICAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:20 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

mitelIpGrpLogicalGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5)
)
mitelIpGrpLogicalGroup.setRevisions(
        ("2003-03-24 09:13",
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
_MitelIpLogGrpLogicalTable_Object = MibTable
mitelIpLogGrpLogicalTable = _MitelIpLogGrpLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mitelIpLogGrpLogicalTable.setStatus("current")
_MitelIpLogGrpLogicalEntry_Object = MibTableRow
mitelIpLogGrpLogicalEntry = _MitelIpLogGrpLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1)
)
mitelIpLogGrpLogicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mitelIpLogGrpLogicalEntry.setStatus("current")
_MitelIpLogAdvertisementAddress_Type = IpAddress
_MitelIpLogAdvertisementAddress_Object = MibTableColumn
mitelIpLogAdvertisementAddress = _MitelIpLogAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 1),
    _MitelIpLogAdvertisementAddress_Type()
)
mitelIpLogAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpLogAdvertisementAddress.setStatus("current")


class _MitelIpLogMaxAdvertisementInterval_Type(Integer32):
    """Custom type mitelIpLogMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_MitelIpLogMaxAdvertisementInterval_Type.__name__ = "Integer32"
_MitelIpLogMaxAdvertisementInterval_Object = MibTableColumn
mitelIpLogMaxAdvertisementInterval = _MitelIpLogMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 2),
    _MitelIpLogMaxAdvertisementInterval_Type()
)
mitelIpLogMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpLogMaxAdvertisementInterval.setStatus("current")


class _MitelIpLogMinAdvertisementInterval_Type(Integer32):
    """Custom type mitelIpLogMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_MitelIpLogMinAdvertisementInterval_Type.__name__ = "Integer32"
_MitelIpLogMinAdvertisementInterval_Object = MibTableColumn
mitelIpLogMinAdvertisementInterval = _MitelIpLogMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 3),
    _MitelIpLogMinAdvertisementInterval_Type()
)
mitelIpLogMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpLogMinAdvertisementInterval.setStatus("current")


class _MitelIpLogAdvertisementLifetime_Type(Integer32):
    """Custom type mitelIpLogAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_MitelIpLogAdvertisementLifetime_Type.__name__ = "Integer32"
_MitelIpLogAdvertisementLifetime_Object = MibTableColumn
mitelIpLogAdvertisementLifetime = _MitelIpLogAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 4),
    _MitelIpLogAdvertisementLifetime_Type()
)
mitelIpLogAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpLogAdvertisementLifetime.setStatus("current")


class _MitelIpLogPerformRouterDiscovery_Type(Integer32):
    """Custom type mitelIpLogPerformRouterDiscovery based on Integer32"""
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


_MitelIpLogPerformRouterDiscovery_Type.__name__ = "Integer32"
_MitelIpLogPerformRouterDiscovery_Object = MibTableColumn
mitelIpLogPerformRouterDiscovery = _MitelIpLogPerformRouterDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 5),
    _MitelIpLogPerformRouterDiscovery_Type()
)
mitelIpLogPerformRouterDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpLogPerformRouterDiscovery.setStatus("current")
_MitelIpLogSolicitationAddress_Type = IpAddress
_MitelIpLogSolicitationAddress_Object = MibTableColumn
mitelIpLogSolicitationAddress = _MitelIpLogSolicitationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 6),
    _MitelIpLogSolicitationAddress_Type()
)
mitelIpLogSolicitationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpLogSolicitationAddress.setStatus("current")
_MitelIpLogStatus_Type = RowStatus
_MitelIpLogStatus_Object = MibTableColumn
mitelIpLogStatus = _MitelIpLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 7),
    _MitelIpLogStatus_Type()
)
mitelIpLogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelIpLogStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-IPLOGICAL-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpGroup": mitelRouterIpGroup,
       "mitelIpGrpLogicalGroup": mitelIpGrpLogicalGroup,
       "mitelIpLogGrpLogicalTable": mitelIpLogGrpLogicalTable,
       "mitelIpLogGrpLogicalEntry": mitelIpLogGrpLogicalEntry,
       "mitelIpLogAdvertisementAddress": mitelIpLogAdvertisementAddress,
       "mitelIpLogMaxAdvertisementInterval": mitelIpLogMaxAdvertisementInterval,
       "mitelIpLogMinAdvertisementInterval": mitelIpLogMinAdvertisementInterval,
       "mitelIpLogAdvertisementLifetime": mitelIpLogAdvertisementLifetime,
       "mitelIpLogPerformRouterDiscovery": mitelIpLogPerformRouterDiscovery,
       "mitelIpLogSolicitationAddress": mitelIpLogSolicitationAddress,
       "mitelIpLogStatus": mitelIpLogStatus}
)
