# SNMP MIB module (SONUS-IP-FORWARDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-IP-FORWARDING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:59 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusPacketMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusPacketMIBs")


# MODULE-IDENTITY

sonusIpForwardingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusIpForwardGeneralGroupTable_Object = MibTable
sonusIpForwardGeneralGroupTable = _SonusIpForwardGeneralGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sonusIpForwardGeneralGroupTable.setStatus("current")
_SonusIpForwardGeneralGroupEntry_Object = MibTableRow
sonusIpForwardGeneralGroupEntry = _SonusIpForwardGeneralGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 1, 1)
)
sonusIpForwardGeneralGroupEntry.setIndexNames(
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpForwardGeneralGroupShelf"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpForwardGeneralGroupSlot"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpForwardGeneralGroupInstance"),
)
if mibBuilder.loadTexts:
    sonusIpForwardGeneralGroupEntry.setStatus("current")
_SonusIpCidrRouteNumber_Type = Gauge32
_SonusIpCidrRouteNumber_Object = MibTableColumn
sonusIpCidrRouteNumber = _SonusIpCidrRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 1, 1, 3),
    _SonusIpCidrRouteNumber_Type()
)
sonusIpCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteNumber.setStatus("current")
_SonusIpForwardGeneralGroupShelf_Type = Integer32
_SonusIpForwardGeneralGroupShelf_Object = MibTableColumn
sonusIpForwardGeneralGroupShelf = _SonusIpForwardGeneralGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 1, 1, 4),
    _SonusIpForwardGeneralGroupShelf_Type()
)
sonusIpForwardGeneralGroupShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpForwardGeneralGroupShelf.setStatus("current")
_SonusIpForwardGeneralGroupSlot_Type = Integer32
_SonusIpForwardGeneralGroupSlot_Object = MibTableColumn
sonusIpForwardGeneralGroupSlot = _SonusIpForwardGeneralGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 1, 1, 5),
    _SonusIpForwardGeneralGroupSlot_Type()
)
sonusIpForwardGeneralGroupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpForwardGeneralGroupSlot.setStatus("current")
_SonusIpForwardGeneralGroupInstance_Type = Integer32
_SonusIpForwardGeneralGroupInstance_Object = MibTableColumn
sonusIpForwardGeneralGroupInstance = _SonusIpForwardGeneralGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 1, 1, 6),
    _SonusIpForwardGeneralGroupInstance_Type()
)
sonusIpForwardGeneralGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpForwardGeneralGroupInstance.setStatus("current")
_SonusIpCidrRouteTable_Object = MibTable
sonusIpCidrRouteTable = _SonusIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    sonusIpCidrRouteTable.setStatus("current")
_SonusIpCidrRouteEntry_Object = MibTableRow
sonusIpCidrRouteEntry = _SonusIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1)
)
sonusIpCidrRouteEntry.setIndexNames(
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrRouteShelf"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrRouteSlot"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrRouteInstance"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrRouteDest"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrRouteMask"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrRouteTos"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    sonusIpCidrRouteEntry.setStatus("current")
_SonusIpCidrRouteDest_Type = IpAddress
_SonusIpCidrRouteDest_Object = MibTableColumn
sonusIpCidrRouteDest = _SonusIpCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 1),
    _SonusIpCidrRouteDest_Type()
)
sonusIpCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteDest.setStatus("current")
_SonusIpCidrRouteMask_Type = IpAddress
_SonusIpCidrRouteMask_Object = MibTableColumn
sonusIpCidrRouteMask = _SonusIpCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 2),
    _SonusIpCidrRouteMask_Type()
)
sonusIpCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteMask.setStatus("current")
_SonusIpCidrRouteTos_Type = Integer32
_SonusIpCidrRouteTos_Object = MibTableColumn
sonusIpCidrRouteTos = _SonusIpCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 3),
    _SonusIpCidrRouteTos_Type()
)
sonusIpCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteTos.setStatus("current")
_SonusIpCidrRouteNextHop_Type = IpAddress
_SonusIpCidrRouteNextHop_Object = MibTableColumn
sonusIpCidrRouteNextHop = _SonusIpCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 4),
    _SonusIpCidrRouteNextHop_Type()
)
sonusIpCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteNextHop.setStatus("current")


class _SonusIpCidrRouteIfIndex_Type(Integer32):
    """Custom type sonusIpCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_SonusIpCidrRouteIfIndex_Object = MibTableColumn
sonusIpCidrRouteIfIndex = _SonusIpCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 5),
    _SonusIpCidrRouteIfIndex_Type()
)
sonusIpCidrRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteIfIndex.setStatus("current")


class _SonusIpCidrRouteType_Type(Integer32):
    """Custom type sonusIpCidrRouteType based on Integer32"""
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
        *(("local", 3),
          ("other", 1),
          ("reject", 2),
          ("remote", 4))
    )


_SonusIpCidrRouteType_Type.__name__ = "Integer32"
_SonusIpCidrRouteType_Object = MibTableColumn
sonusIpCidrRouteType = _SonusIpCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 6),
    _SonusIpCidrRouteType_Type()
)
sonusIpCidrRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteType.setStatus("current")


class _SonusIpCidrRouteProto_Type(Integer32):
    """Custom type sonusIpCidrRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoEigrp", 16),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("esIs", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("isIs", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_SonusIpCidrRouteProto_Type.__name__ = "Integer32"
_SonusIpCidrRouteProto_Object = MibTableColumn
sonusIpCidrRouteProto = _SonusIpCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 7),
    _SonusIpCidrRouteProto_Type()
)
sonusIpCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteProto.setStatus("current")


class _SonusIpCidrRouteAge_Type(Integer32):
    """Custom type sonusIpCidrRouteAge based on Integer32"""
    defaultValue = 0


_SonusIpCidrRouteAge_Object = MibTableColumn
sonusIpCidrRouteAge = _SonusIpCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 8),
    _SonusIpCidrRouteAge_Type()
)
sonusIpCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteAge.setStatus("current")
_SonusIpCidrRouteInfo_Type = ObjectIdentifier
_SonusIpCidrRouteInfo_Object = MibTableColumn
sonusIpCidrRouteInfo = _SonusIpCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 9),
    _SonusIpCidrRouteInfo_Type()
)
sonusIpCidrRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteInfo.setStatus("current")


class _SonusIpCidrRouteNextHopAS_Type(Integer32):
    """Custom type sonusIpCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_SonusIpCidrRouteNextHopAS_Object = MibTableColumn
sonusIpCidrRouteNextHopAS = _SonusIpCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 10),
    _SonusIpCidrRouteNextHopAS_Type()
)
sonusIpCidrRouteNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteNextHopAS.setStatus("current")


class _SonusIpCidrRouteMetric1_Type(Integer32):
    """Custom type sonusIpCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_SonusIpCidrRouteMetric1_Object = MibTableColumn
sonusIpCidrRouteMetric1 = _SonusIpCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 11),
    _SonusIpCidrRouteMetric1_Type()
)
sonusIpCidrRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteMetric1.setStatus("current")


class _SonusIpCidrRouteMetric2_Type(Integer32):
    """Custom type sonusIpCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_SonusIpCidrRouteMetric2_Object = MibTableColumn
sonusIpCidrRouteMetric2 = _SonusIpCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 12),
    _SonusIpCidrRouteMetric2_Type()
)
sonusIpCidrRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteMetric2.setStatus("current")


class _SonusIpCidrRouteMetric3_Type(Integer32):
    """Custom type sonusIpCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_SonusIpCidrRouteMetric3_Object = MibTableColumn
sonusIpCidrRouteMetric3 = _SonusIpCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 13),
    _SonusIpCidrRouteMetric3_Type()
)
sonusIpCidrRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteMetric3.setStatus("current")


class _SonusIpCidrRouteMetric4_Type(Integer32):
    """Custom type sonusIpCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_SonusIpCidrRouteMetric4_Object = MibTableColumn
sonusIpCidrRouteMetric4 = _SonusIpCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 14),
    _SonusIpCidrRouteMetric4_Type()
)
sonusIpCidrRouteMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteMetric4.setStatus("current")


class _SonusIpCidrRouteMetric5_Type(Integer32):
    """Custom type sonusIpCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_SonusIpCidrRouteMetric5_Object = MibTableColumn
sonusIpCidrRouteMetric5 = _SonusIpCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 15),
    _SonusIpCidrRouteMetric5_Type()
)
sonusIpCidrRouteMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteMetric5.setStatus("current")
_SonusIpCidrRouteStatus_Type = RowStatus
_SonusIpCidrRouteStatus_Object = MibTableColumn
sonusIpCidrRouteStatus = _SonusIpCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 16),
    _SonusIpCidrRouteStatus_Type()
)
sonusIpCidrRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteStatus.setStatus("current")
_SonusIpCidrRouteShelf_Type = Integer32
_SonusIpCidrRouteShelf_Object = MibTableColumn
sonusIpCidrRouteShelf = _SonusIpCidrRouteShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 17),
    _SonusIpCidrRouteShelf_Type()
)
sonusIpCidrRouteShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteShelf.setStatus("current")
_SonusIpCidrRouteSlot_Type = Integer32
_SonusIpCidrRouteSlot_Object = MibTableColumn
sonusIpCidrRouteSlot = _SonusIpCidrRouteSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 18),
    _SonusIpCidrRouteSlot_Type()
)
sonusIpCidrRouteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteSlot.setStatus("current")
_SonusIpCidrRouteInstance_Type = Integer32
_SonusIpCidrRouteInstance_Object = MibTableColumn
sonusIpCidrRouteInstance = _SonusIpCidrRouteInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 2, 1, 19),
    _SonusIpCidrRouteInstance_Type()
)
sonusIpCidrRouteInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpCidrRouteInstance.setStatus("current")
_SonusIpCidrAdminRouteTable_Object = MibTable
sonusIpCidrAdminRouteTable = _SonusIpCidrAdminRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    sonusIpCidrAdminRouteTable.setStatus("current")
_SonusIpCidrAdminRouteEntry_Object = MibTableRow
sonusIpCidrAdminRouteEntry = _SonusIpCidrAdminRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 3, 1)
)
sonusIpCidrAdminRouteEntry.setIndexNames(
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrAdminRouteDest"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrAdminRouteMask"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrAdminRouteNextHop"),
    (0, "SONUS-IP-FORWARDING-MIB", "sonusIpCidrAdminRouteIfIndex"),
)
if mibBuilder.loadTexts:
    sonusIpCidrAdminRouteEntry.setStatus("current")
_SonusIpCidrAdminRouteDest_Type = IpAddress
_SonusIpCidrAdminRouteDest_Object = MibTableColumn
sonusIpCidrAdminRouteDest = _SonusIpCidrAdminRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 3, 1, 1),
    _SonusIpCidrAdminRouteDest_Type()
)
sonusIpCidrAdminRouteDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpCidrAdminRouteDest.setStatus("current")
_SonusIpCidrAdminRouteMask_Type = IpAddress
_SonusIpCidrAdminRouteMask_Object = MibTableColumn
sonusIpCidrAdminRouteMask = _SonusIpCidrAdminRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 3, 1, 2),
    _SonusIpCidrAdminRouteMask_Type()
)
sonusIpCidrAdminRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpCidrAdminRouteMask.setStatus("current")
_SonusIpCidrAdminRouteNextHop_Type = IpAddress
_SonusIpCidrAdminRouteNextHop_Object = MibTableColumn
sonusIpCidrAdminRouteNextHop = _SonusIpCidrAdminRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 3, 1, 3),
    _SonusIpCidrAdminRouteNextHop_Type()
)
sonusIpCidrAdminRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpCidrAdminRouteNextHop.setStatus("current")
_SonusIpCidrAdminRouteIfIndex_Type = Integer32
_SonusIpCidrAdminRouteIfIndex_Object = MibTableColumn
sonusIpCidrAdminRouteIfIndex = _SonusIpCidrAdminRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 3, 1, 4),
    _SonusIpCidrAdminRouteIfIndex_Type()
)
sonusIpCidrAdminRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpCidrAdminRouteIfIndex.setStatus("current")
_SonusIpCidrAdminRouteStatus_Type = RowStatus
_SonusIpCidrAdminRouteStatus_Object = MibTableColumn
sonusIpCidrAdminRouteStatus = _SonusIpCidrAdminRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 3, 3, 1, 5),
    _SonusIpCidrAdminRouteStatus_Type()
)
sonusIpCidrAdminRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpCidrAdminRouteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-IP-FORWARDING-MIB",
    **{"sonusIpForwardingMIB": sonusIpForwardingMIB,
       "sonusIpForwardGeneralGroupTable": sonusIpForwardGeneralGroupTable,
       "sonusIpForwardGeneralGroupEntry": sonusIpForwardGeneralGroupEntry,
       "sonusIpCidrRouteNumber": sonusIpCidrRouteNumber,
       "sonusIpForwardGeneralGroupShelf": sonusIpForwardGeneralGroupShelf,
       "sonusIpForwardGeneralGroupSlot": sonusIpForwardGeneralGroupSlot,
       "sonusIpForwardGeneralGroupInstance": sonusIpForwardGeneralGroupInstance,
       "sonusIpCidrRouteTable": sonusIpCidrRouteTable,
       "sonusIpCidrRouteEntry": sonusIpCidrRouteEntry,
       "sonusIpCidrRouteDest": sonusIpCidrRouteDest,
       "sonusIpCidrRouteMask": sonusIpCidrRouteMask,
       "sonusIpCidrRouteTos": sonusIpCidrRouteTos,
       "sonusIpCidrRouteNextHop": sonusIpCidrRouteNextHop,
       "sonusIpCidrRouteIfIndex": sonusIpCidrRouteIfIndex,
       "sonusIpCidrRouteType": sonusIpCidrRouteType,
       "sonusIpCidrRouteProto": sonusIpCidrRouteProto,
       "sonusIpCidrRouteAge": sonusIpCidrRouteAge,
       "sonusIpCidrRouteInfo": sonusIpCidrRouteInfo,
       "sonusIpCidrRouteNextHopAS": sonusIpCidrRouteNextHopAS,
       "sonusIpCidrRouteMetric1": sonusIpCidrRouteMetric1,
       "sonusIpCidrRouteMetric2": sonusIpCidrRouteMetric2,
       "sonusIpCidrRouteMetric3": sonusIpCidrRouteMetric3,
       "sonusIpCidrRouteMetric4": sonusIpCidrRouteMetric4,
       "sonusIpCidrRouteMetric5": sonusIpCidrRouteMetric5,
       "sonusIpCidrRouteStatus": sonusIpCidrRouteStatus,
       "sonusIpCidrRouteShelf": sonusIpCidrRouteShelf,
       "sonusIpCidrRouteSlot": sonusIpCidrRouteSlot,
       "sonusIpCidrRouteInstance": sonusIpCidrRouteInstance,
       "sonusIpCidrAdminRouteTable": sonusIpCidrAdminRouteTable,
       "sonusIpCidrAdminRouteEntry": sonusIpCidrAdminRouteEntry,
       "sonusIpCidrAdminRouteDest": sonusIpCidrAdminRouteDest,
       "sonusIpCidrAdminRouteMask": sonusIpCidrAdminRouteMask,
       "sonusIpCidrAdminRouteNextHop": sonusIpCidrAdminRouteNextHop,
       "sonusIpCidrAdminRouteIfIndex": sonusIpCidrAdminRouteIfIndex,
       "sonusIpCidrAdminRouteStatus": sonusIpCidrAdminRouteStatus}
)
