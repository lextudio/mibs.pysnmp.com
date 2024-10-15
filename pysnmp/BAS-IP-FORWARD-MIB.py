# SNMP MIB module (BAS-IP-FORWARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-IP-FORWARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:26 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasCidr) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasCidr")

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


# MODULE-IDENTITY

basIpForward = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasCidrObjects_ObjectIdentity = ObjectIdentity
basCidrObjects = _BasCidrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2)
)
_BasCidrTable_Object = MibTable
basCidrTable = _BasCidrTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 1)
)
if mibBuilder.loadTexts:
    basCidrTable.setStatus("current")
_BasCidrEntry_Object = MibTableRow
basCidrEntry = _BasCidrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 1, 1)
)
basCidrEntry.setIndexNames(
    (0, "BAS-IP-FORWARD-MIB", "basCidrChassis"),
    (0, "BAS-IP-FORWARD-MIB", "basCidrSlot"),
    (0, "BAS-IP-FORWARD-MIB", "basCidrIf"),
    (0, "BAS-IP-FORWARD-MIB", "basCidrLPort"),
)
if mibBuilder.loadTexts:
    basCidrEntry.setStatus("current")
_BasIpCidrRouteNumber_Type = Gauge32
_BasIpCidrRouteNumber_Object = MibTableColumn
basIpCidrRouteNumber = _BasIpCidrRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 1, 1, 3),
    _BasIpCidrRouteNumber_Type()
)
basIpCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpCidrRouteNumber.setStatus("current")
_BasCidrChassis_Type = BasChassisId
_BasCidrChassis_Object = MibTableColumn
basCidrChassis = _BasCidrChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 1, 1, 4),
    _BasCidrChassis_Type()
)
basCidrChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCidrChassis.setStatus("current")
_BasCidrSlot_Type = BasSlotId
_BasCidrSlot_Object = MibTableColumn
basCidrSlot = _BasCidrSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 1, 1, 5),
    _BasCidrSlot_Type()
)
basCidrSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCidrSlot.setStatus("current")
_BasCidrIf_Type = BasInterfaceId
_BasCidrIf_Object = MibTableColumn
basCidrIf = _BasCidrIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 1, 1, 6),
    _BasCidrIf_Type()
)
basCidrIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCidrIf.setStatus("current")
_BasCidrLPort_Type = BasLogicalPortId
_BasCidrLPort_Object = MibTableColumn
basCidrLPort = _BasCidrLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 1, 1, 7),
    _BasCidrLPort_Type()
)
basCidrLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCidrLPort.setStatus("current")
_BasIpCidrRouteTable_Object = MibTable
basIpCidrRouteTable = _BasIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4)
)
if mibBuilder.loadTexts:
    basIpCidrRouteTable.setStatus("current")
_BasIpCidrRouteEntry_Object = MibTableRow
basIpCidrRouteEntry = _BasIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1)
)
basIpCidrRouteEntry.setIndexNames(
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteChassis"),
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteSlot"),
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteIf"),
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteLPort"),
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteDest"),
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteMask"),
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteTos"),
    (0, "BAS-IP-FORWARD-MIB", "basIpCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    basIpCidrRouteEntry.setStatus("current")
_BasIpCidrRouteDest_Type = IpAddress
_BasIpCidrRouteDest_Object = MibTableColumn
basIpCidrRouteDest = _BasIpCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 1),
    _BasIpCidrRouteDest_Type()
)
basIpCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpCidrRouteDest.setStatus("current")
_BasIpCidrRouteMask_Type = IpAddress
_BasIpCidrRouteMask_Object = MibTableColumn
basIpCidrRouteMask = _BasIpCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 2),
    _BasIpCidrRouteMask_Type()
)
basIpCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpCidrRouteMask.setStatus("current")
_BasIpCidrRouteTos_Type = Integer32
_BasIpCidrRouteTos_Object = MibTableColumn
basIpCidrRouteTos = _BasIpCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 3),
    _BasIpCidrRouteTos_Type()
)
basIpCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpCidrRouteTos.setStatus("current")
_BasIpCidrRouteNextHop_Type = IpAddress
_BasIpCidrRouteNextHop_Object = MibTableColumn
basIpCidrRouteNextHop = _BasIpCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 4),
    _BasIpCidrRouteNextHop_Type()
)
basIpCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpCidrRouteNextHop.setStatus("current")


class _BasIpCidrRouteIfIndex_Type(Integer32):
    """Custom type basIpCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_BasIpCidrRouteIfIndex_Object = MibTableColumn
basIpCidrRouteIfIndex = _BasIpCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 5),
    _BasIpCidrRouteIfIndex_Type()
)
basIpCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteIfIndex.setStatus("current")


class _BasIpCidrRouteType_Type(Integer32):
    """Custom type basIpCidrRouteType based on Integer32"""
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


_BasIpCidrRouteType_Type.__name__ = "Integer32"
_BasIpCidrRouteType_Object = MibTableColumn
basIpCidrRouteType = _BasIpCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 6),
    _BasIpCidrRouteType_Type()
)
basIpCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteType.setStatus("current")


class _BasIpCidrRouteProto_Type(Integer32):
    """Custom type basIpCidrRouteProto based on Integer32"""
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


_BasIpCidrRouteProto_Type.__name__ = "Integer32"
_BasIpCidrRouteProto_Object = MibTableColumn
basIpCidrRouteProto = _BasIpCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 7),
    _BasIpCidrRouteProto_Type()
)
basIpCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpCidrRouteProto.setStatus("current")


class _BasIpCidrRouteAge_Type(Integer32):
    """Custom type basIpCidrRouteAge based on Integer32"""
    defaultValue = 0


_BasIpCidrRouteAge_Object = MibTableColumn
basIpCidrRouteAge = _BasIpCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 8),
    _BasIpCidrRouteAge_Type()
)
basIpCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpCidrRouteAge.setStatus("current")
_BasIpCidrRouteInfo_Type = ObjectIdentifier
_BasIpCidrRouteInfo_Object = MibTableColumn
basIpCidrRouteInfo = _BasIpCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 9),
    _BasIpCidrRouteInfo_Type()
)
basIpCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteInfo.setStatus("current")


class _BasIpCidrRouteNextHopAS_Type(Integer32):
    """Custom type basIpCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_BasIpCidrRouteNextHopAS_Object = MibTableColumn
basIpCidrRouteNextHopAS = _BasIpCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 10),
    _BasIpCidrRouteNextHopAS_Type()
)
basIpCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteNextHopAS.setStatus("current")


class _BasIpCidrRouteMetric1_Type(Integer32):
    """Custom type basIpCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_BasIpCidrRouteMetric1_Object = MibTableColumn
basIpCidrRouteMetric1 = _BasIpCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 11),
    _BasIpCidrRouteMetric1_Type()
)
basIpCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteMetric1.setStatus("current")


class _BasIpCidrRouteMetric2_Type(Integer32):
    """Custom type basIpCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_BasIpCidrRouteMetric2_Object = MibTableColumn
basIpCidrRouteMetric2 = _BasIpCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 12),
    _BasIpCidrRouteMetric2_Type()
)
basIpCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteMetric2.setStatus("current")


class _BasIpCidrRouteMetric3_Type(Integer32):
    """Custom type basIpCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_BasIpCidrRouteMetric3_Object = MibTableColumn
basIpCidrRouteMetric3 = _BasIpCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 13),
    _BasIpCidrRouteMetric3_Type()
)
basIpCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteMetric3.setStatus("current")


class _BasIpCidrRouteMetric4_Type(Integer32):
    """Custom type basIpCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_BasIpCidrRouteMetric4_Object = MibTableColumn
basIpCidrRouteMetric4 = _BasIpCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 14),
    _BasIpCidrRouteMetric4_Type()
)
basIpCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteMetric4.setStatus("current")


class _BasIpCidrRouteMetric5_Type(Integer32):
    """Custom type basIpCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_BasIpCidrRouteMetric5_Object = MibTableColumn
basIpCidrRouteMetric5 = _BasIpCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 15),
    _BasIpCidrRouteMetric5_Type()
)
basIpCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteMetric5.setStatus("current")
_BasIpCidrRouteStatus_Type = RowStatus
_BasIpCidrRouteStatus_Object = MibTableColumn
basIpCidrRouteStatus = _BasIpCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 16),
    _BasIpCidrRouteStatus_Type()
)
basIpCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpCidrRouteStatus.setStatus("current")
_BasIpCidrRouteChassis_Type = BasChassisId
_BasIpCidrRouteChassis_Object = MibTableColumn
basIpCidrRouteChassis = _BasIpCidrRouteChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 17),
    _BasIpCidrRouteChassis_Type()
)
basIpCidrRouteChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpCidrRouteChassis.setStatus("current")
_BasIpCidrRouteSlot_Type = BasSlotId
_BasIpCidrRouteSlot_Object = MibTableColumn
basIpCidrRouteSlot = _BasIpCidrRouteSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 18),
    _BasIpCidrRouteSlot_Type()
)
basIpCidrRouteSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpCidrRouteSlot.setStatus("current")
_BasIpCidrRouteIf_Type = BasInterfaceId
_BasIpCidrRouteIf_Object = MibTableColumn
basIpCidrRouteIf = _BasIpCidrRouteIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 19),
    _BasIpCidrRouteIf_Type()
)
basIpCidrRouteIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpCidrRouteIf.setStatus("current")
_BasIpCidrRouteLPort_Type = BasLogicalPortId
_BasIpCidrRouteLPort_Object = MibTableColumn
basIpCidrRouteLPort = _BasIpCidrRouteLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5, 2, 4, 1, 20),
    _BasIpCidrRouteLPort_Type()
)
basIpCidrRouteLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpCidrRouteLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-IP-FORWARD-MIB",
    **{"basIpForward": basIpForward,
       "basCidrObjects": basCidrObjects,
       "basCidrTable": basCidrTable,
       "basCidrEntry": basCidrEntry,
       "basIpCidrRouteNumber": basIpCidrRouteNumber,
       "basCidrChassis": basCidrChassis,
       "basCidrSlot": basCidrSlot,
       "basCidrIf": basCidrIf,
       "basCidrLPort": basCidrLPort,
       "basIpCidrRouteTable": basIpCidrRouteTable,
       "basIpCidrRouteEntry": basIpCidrRouteEntry,
       "basIpCidrRouteDest": basIpCidrRouteDest,
       "basIpCidrRouteMask": basIpCidrRouteMask,
       "basIpCidrRouteTos": basIpCidrRouteTos,
       "basIpCidrRouteNextHop": basIpCidrRouteNextHop,
       "basIpCidrRouteIfIndex": basIpCidrRouteIfIndex,
       "basIpCidrRouteType": basIpCidrRouteType,
       "basIpCidrRouteProto": basIpCidrRouteProto,
       "basIpCidrRouteAge": basIpCidrRouteAge,
       "basIpCidrRouteInfo": basIpCidrRouteInfo,
       "basIpCidrRouteNextHopAS": basIpCidrRouteNextHopAS,
       "basIpCidrRouteMetric1": basIpCidrRouteMetric1,
       "basIpCidrRouteMetric2": basIpCidrRouteMetric2,
       "basIpCidrRouteMetric3": basIpCidrRouteMetric3,
       "basIpCidrRouteMetric4": basIpCidrRouteMetric4,
       "basIpCidrRouteMetric5": basIpCidrRouteMetric5,
       "basIpCidrRouteStatus": basIpCidrRouteStatus,
       "basIpCidrRouteChassis": basIpCidrRouteChassis,
       "basIpCidrRouteSlot": basIpCidrRouteSlot,
       "basIpCidrRouteIf": basIpCidrRouteIf,
       "basIpCidrRouteLPort": basIpCidrRouteLPort}
)
