# SNMP MIB module (BAS-RIPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-RIPv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:32 2024
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
 basAliasRip) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasRip")

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

basRip2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RouteTag(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_BasRipObjects_ObjectIdentity = ObjectIdentity
basRipObjects = _BasRipObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1)
)
_BasRip2GlobalsTable_Object = MibTable
basRip2GlobalsTable = _BasRip2GlobalsTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1)
)
if mibBuilder.loadTexts:
    basRip2GlobalsTable.setStatus("current")
_BasRip2GlobalEntry_Object = MibTableRow
basRip2GlobalEntry = _BasRip2GlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1, 1)
)
basRip2GlobalEntry.setIndexNames(
    (0, "BAS-RIPv2-MIB", "basRip2GlobalChassis"),
    (0, "BAS-RIPv2-MIB", "basRip2GlobalSlot"),
    (0, "BAS-RIPv2-MIB", "basRip2GlobalIf"),
    (0, "BAS-RIPv2-MIB", "basRip2GlobalLPort"),
)
if mibBuilder.loadTexts:
    basRip2GlobalEntry.setStatus("current")
_BasRip2GlobalRouteChanges_Type = Counter32
_BasRip2GlobalRouteChanges_Object = MibTableColumn
basRip2GlobalRouteChanges = _BasRip2GlobalRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1, 1, 1),
    _BasRip2GlobalRouteChanges_Type()
)
basRip2GlobalRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2GlobalRouteChanges.setStatus("current")
_BasRip2GlobalQueries_Type = Counter32
_BasRip2GlobalQueries_Object = MibTableColumn
basRip2GlobalQueries = _BasRip2GlobalQueries_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1, 1, 2),
    _BasRip2GlobalQueries_Type()
)
basRip2GlobalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2GlobalQueries.setStatus("current")
_BasRip2GlobalChassis_Type = BasChassisId
_BasRip2GlobalChassis_Object = MibTableColumn
basRip2GlobalChassis = _BasRip2GlobalChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1, 1, 3),
    _BasRip2GlobalChassis_Type()
)
basRip2GlobalChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2GlobalChassis.setStatus("current")
_BasRip2GlobalSlot_Type = BasSlotId
_BasRip2GlobalSlot_Object = MibTableColumn
basRip2GlobalSlot = _BasRip2GlobalSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1, 1, 4),
    _BasRip2GlobalSlot_Type()
)
basRip2GlobalSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2GlobalSlot.setStatus("current")
_BasRip2GlobalIf_Type = BasInterfaceId
_BasRip2GlobalIf_Object = MibTableColumn
basRip2GlobalIf = _BasRip2GlobalIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1, 1, 5),
    _BasRip2GlobalIf_Type()
)
basRip2GlobalIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2GlobalIf.setStatus("current")
_BasRip2GlobalLPort_Type = BasLogicalPortId
_BasRip2GlobalLPort_Object = MibTableColumn
basRip2GlobalLPort = _BasRip2GlobalLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 1, 1, 6),
    _BasRip2GlobalLPort_Type()
)
basRip2GlobalLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2GlobalLPort.setStatus("current")
_BasRip2IfStatTable_Object = MibTable
basRip2IfStatTable = _BasRip2IfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2)
)
if mibBuilder.loadTexts:
    basRip2IfStatTable.setStatus("current")
_BasRip2IfStatEntry_Object = MibTableRow
basRip2IfStatEntry = _BasRip2IfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1)
)
basRip2IfStatEntry.setIndexNames(
    (0, "BAS-RIPv2-MIB", "basRip2GlobalChassis"),
    (0, "BAS-RIPv2-MIB", "basRip2GlobalSlot"),
    (0, "BAS-RIPv2-MIB", "basRip2GlobalIf"),
    (0, "BAS-RIPv2-MIB", "basRip2GlobalLPort"),
    (0, "BAS-RIPv2-MIB", "basRip2IfStatAddress"),
)
if mibBuilder.loadTexts:
    basRip2IfStatEntry.setStatus("current")
_BasRip2IfStatAddress_Type = IpAddress
_BasRip2IfStatAddress_Object = MibTableColumn
basRip2IfStatAddress = _BasRip2IfStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 1),
    _BasRip2IfStatAddress_Type()
)
basRip2IfStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2IfStatAddress.setStatus("current")
_BasRip2IfStatRcvBadPackets_Type = Counter32
_BasRip2IfStatRcvBadPackets_Object = MibTableColumn
basRip2IfStatRcvBadPackets = _BasRip2IfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 2),
    _BasRip2IfStatRcvBadPackets_Type()
)
basRip2IfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2IfStatRcvBadPackets.setStatus("current")
_BasRip2IfStatRcvBadRoutes_Type = Counter32
_BasRip2IfStatRcvBadRoutes_Object = MibTableColumn
basRip2IfStatRcvBadRoutes = _BasRip2IfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 3),
    _BasRip2IfStatRcvBadRoutes_Type()
)
basRip2IfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2IfStatRcvBadRoutes.setStatus("current")
_BasRip2IfStatSentUpdates_Type = Counter32
_BasRip2IfStatSentUpdates_Object = MibTableColumn
basRip2IfStatSentUpdates = _BasRip2IfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 4),
    _BasRip2IfStatSentUpdates_Type()
)
basRip2IfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2IfStatSentUpdates.setStatus("current")
_BasRip2IfStatStatus_Type = RowStatus
_BasRip2IfStatStatus_Object = MibTableColumn
basRip2IfStatStatus = _BasRip2IfStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 5),
    _BasRip2IfStatStatus_Type()
)
basRip2IfStatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfStatStatus.setStatus("current")
_BasRip2IfStatChassis_Type = BasChassisId
_BasRip2IfStatChassis_Object = MibTableColumn
basRip2IfStatChassis = _BasRip2IfStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 6),
    _BasRip2IfStatChassis_Type()
)
basRip2IfStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfStatChassis.setStatus("current")
_BasRip2IfStatSlot_Type = BasSlotId
_BasRip2IfStatSlot_Object = MibTableColumn
basRip2IfStatSlot = _BasRip2IfStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 7),
    _BasRip2IfStatSlot_Type()
)
basRip2IfStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfStatSlot.setStatus("current")
_BasRip2IfStatIf_Type = BasInterfaceId
_BasRip2IfStatIf_Object = MibTableColumn
basRip2IfStatIf = _BasRip2IfStatIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 8),
    _BasRip2IfStatIf_Type()
)
basRip2IfStatIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfStatIf.setStatus("current")
_BasRip2IfStatLPort_Type = BasLogicalPortId
_BasRip2IfStatLPort_Object = MibTableColumn
basRip2IfStatLPort = _BasRip2IfStatLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 2, 1, 9),
    _BasRip2IfStatLPort_Type()
)
basRip2IfStatLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfStatLPort.setStatus("current")
_BasRip2IfConfTable_Object = MibTable
basRip2IfConfTable = _BasRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3)
)
if mibBuilder.loadTexts:
    basRip2IfConfTable.setStatus("current")
_BasRip2IfConfEntry_Object = MibTableRow
basRip2IfConfEntry = _BasRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1)
)
basRip2IfConfEntry.setIndexNames(
    (0, "BAS-RIPv2-MIB", "basRip2IfConfChassis"),
    (0, "BAS-RIPv2-MIB", "basRip2IfConfSlot"),
    (0, "BAS-RIPv2-MIB", "basRip2IfConfIf"),
    (0, "BAS-RIPv2-MIB", "basRip2IfConfLPort"),
    (0, "BAS-RIPv2-MIB", "basRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    basRip2IfConfEntry.setStatus("current")
_BasRip2IfConfAddress_Type = IpAddress
_BasRip2IfConfAddress_Object = MibTableColumn
basRip2IfConfAddress = _BasRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 1),
    _BasRip2IfConfAddress_Type()
)
basRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2IfConfAddress.setStatus("current")


class _BasRip2IfConfDomain_Type(RouteTag):
    """Custom type basRip2IfConfDomain based on RouteTag"""
    defaultHexValue = "0000"


_BasRip2IfConfDomain_Object = MibTableColumn
basRip2IfConfDomain = _BasRip2IfConfDomain_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 2),
    _BasRip2IfConfDomain_Type()
)
basRip2IfConfDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfDomain.setStatus("obsolete")


class _BasRip2IfConfAuthType_Type(Integer32):
    """Custom type basRip2IfConfAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_BasRip2IfConfAuthType_Type.__name__ = "Integer32"
_BasRip2IfConfAuthType_Object = MibTableColumn
basRip2IfConfAuthType = _BasRip2IfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 3),
    _BasRip2IfConfAuthType_Type()
)
basRip2IfConfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfAuthType.setStatus("current")


class _BasRip2IfConfAuthKey_Type(OctetString):
    """Custom type basRip2IfConfAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasRip2IfConfAuthKey_Type.__name__ = "OctetString"
_BasRip2IfConfAuthKey_Object = MibTableColumn
basRip2IfConfAuthKey = _BasRip2IfConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 4),
    _BasRip2IfConfAuthKey_Type()
)
basRip2IfConfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfAuthKey.setStatus("current")


class _BasRip2IfConfSend_Type(Integer32):
    """Custom type basRip2IfConfSend based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("doNotSend", 1),
          ("rip1Compatible", 3),
          ("ripV1Demand", 5),
          ("ripV2Demand", 6),
          ("ripVersion1", 2),
          ("ripVersion2", 4))
    )


_BasRip2IfConfSend_Type.__name__ = "Integer32"
_BasRip2IfConfSend_Object = MibTableColumn
basRip2IfConfSend = _BasRip2IfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 5),
    _BasRip2IfConfSend_Type()
)
basRip2IfConfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfSend.setStatus("current")


class _BasRip2IfConfReceive_Type(Integer32):
    """Custom type basRip2IfConfReceive based on Integer32"""
    defaultValue = 3

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
        *(("doNotRecieve", 4),
          ("rip1", 1),
          ("rip1OrRip2", 3),
          ("rip2", 2))
    )


_BasRip2IfConfReceive_Type.__name__ = "Integer32"
_BasRip2IfConfReceive_Object = MibTableColumn
basRip2IfConfReceive = _BasRip2IfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 6),
    _BasRip2IfConfReceive_Type()
)
basRip2IfConfReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfReceive.setStatus("current")


class _BasRip2IfConfDefaultMetric_Type(Integer32):
    """Custom type basRip2IfConfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BasRip2IfConfDefaultMetric_Type.__name__ = "Integer32"
_BasRip2IfConfDefaultMetric_Object = MibTableColumn
basRip2IfConfDefaultMetric = _BasRip2IfConfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 7),
    _BasRip2IfConfDefaultMetric_Type()
)
basRip2IfConfDefaultMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfDefaultMetric.setStatus("current")
_BasRip2IfConfStatus_Type = RowStatus
_BasRip2IfConfStatus_Object = MibTableColumn
basRip2IfConfStatus = _BasRip2IfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 8),
    _BasRip2IfConfStatus_Type()
)
basRip2IfConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfStatus.setStatus("current")
_BasRip2IfConfSrcAddress_Type = IpAddress
_BasRip2IfConfSrcAddress_Object = MibTableColumn
basRip2IfConfSrcAddress = _BasRip2IfConfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 9),
    _BasRip2IfConfSrcAddress_Type()
)
basRip2IfConfSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRip2IfConfSrcAddress.setStatus("current")
_BasRip2IfConfChassis_Type = BasChassisId
_BasRip2IfConfChassis_Object = MibTableColumn
basRip2IfConfChassis = _BasRip2IfConfChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 10),
    _BasRip2IfConfChassis_Type()
)
basRip2IfConfChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfConfChassis.setStatus("current")
_BasRip2IfConfSlot_Type = BasSlotId
_BasRip2IfConfSlot_Object = MibTableColumn
basRip2IfConfSlot = _BasRip2IfConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 11),
    _BasRip2IfConfSlot_Type()
)
basRip2IfConfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfConfSlot.setStatus("current")
_BasRip2IfConfIf_Type = BasInterfaceId
_BasRip2IfConfIf_Object = MibTableColumn
basRip2IfConfIf = _BasRip2IfConfIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 12),
    _BasRip2IfConfIf_Type()
)
basRip2IfConfIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfConfIf.setStatus("current")
_BasRip2IfConfLPort_Type = BasLogicalPortId
_BasRip2IfConfLPort_Object = MibTableColumn
basRip2IfConfLPort = _BasRip2IfConfLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 3, 1, 13),
    _BasRip2IfConfLPort_Type()
)
basRip2IfConfLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2IfConfLPort.setStatus("current")
_BasRip2PeerTable_Object = MibTable
basRip2PeerTable = _BasRip2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4)
)
if mibBuilder.loadTexts:
    basRip2PeerTable.setStatus("current")
_BasRip2PeerEntry_Object = MibTableRow
basRip2PeerEntry = _BasRip2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1)
)
basRip2PeerEntry.setIndexNames(
    (0, "BAS-RIPv2-MIB", "basRip2PeerChassis"),
    (0, "BAS-RIPv2-MIB", "basRip2PeerSlot"),
    (0, "BAS-RIPv2-MIB", "basRip2PeerIf"),
    (0, "BAS-RIPv2-MIB", "basRip2PeerLPort"),
    (0, "BAS-RIPv2-MIB", "basRip2PeerAddress"),
    (0, "BAS-RIPv2-MIB", "basRip2PeerDomain"),
)
if mibBuilder.loadTexts:
    basRip2PeerEntry.setStatus("current")
_BasRip2PeerAddress_Type = IpAddress
_BasRip2PeerAddress_Object = MibTableColumn
basRip2PeerAddress = _BasRip2PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 1),
    _BasRip2PeerAddress_Type()
)
basRip2PeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2PeerAddress.setStatus("current")
_BasRip2PeerDomain_Type = RouteTag
_BasRip2PeerDomain_Object = MibTableColumn
basRip2PeerDomain = _BasRip2PeerDomain_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 2),
    _BasRip2PeerDomain_Type()
)
basRip2PeerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2PeerDomain.setStatus("current")
_BasRip2PeerLastUpdate_Type = TimeTicks
_BasRip2PeerLastUpdate_Object = MibTableColumn
basRip2PeerLastUpdate = _BasRip2PeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 3),
    _BasRip2PeerLastUpdate_Type()
)
basRip2PeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2PeerLastUpdate.setStatus("current")


class _BasRip2PeerVersion_Type(Integer32):
    """Custom type basRip2PeerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasRip2PeerVersion_Type.__name__ = "Integer32"
_BasRip2PeerVersion_Object = MibTableColumn
basRip2PeerVersion = _BasRip2PeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 4),
    _BasRip2PeerVersion_Type()
)
basRip2PeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2PeerVersion.setStatus("current")
_BasRip2PeerRcvBadPackets_Type = Counter32
_BasRip2PeerRcvBadPackets_Object = MibTableColumn
basRip2PeerRcvBadPackets = _BasRip2PeerRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 5),
    _BasRip2PeerRcvBadPackets_Type()
)
basRip2PeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2PeerRcvBadPackets.setStatus("current")
_BasRip2PeerRcvBadRoutes_Type = Counter32
_BasRip2PeerRcvBadRoutes_Object = MibTableColumn
basRip2PeerRcvBadRoutes = _BasRip2PeerRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 6),
    _BasRip2PeerRcvBadRoutes_Type()
)
basRip2PeerRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRip2PeerRcvBadRoutes.setStatus("current")
_BasRip2PeerChassis_Type = BasChassisId
_BasRip2PeerChassis_Object = MibTableColumn
basRip2PeerChassis = _BasRip2PeerChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 7),
    _BasRip2PeerChassis_Type()
)
basRip2PeerChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2PeerChassis.setStatus("current")
_BasRip2PeerSlot_Type = BasSlotId
_BasRip2PeerSlot_Object = MibTableColumn
basRip2PeerSlot = _BasRip2PeerSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 8),
    _BasRip2PeerSlot_Type()
)
basRip2PeerSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2PeerSlot.setStatus("current")
_BasRip2PeerIf_Type = BasInterfaceId
_BasRip2PeerIf_Object = MibTableColumn
basRip2PeerIf = _BasRip2PeerIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 9),
    _BasRip2PeerIf_Type()
)
basRip2PeerIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2PeerIf.setStatus("current")
_BasRip2PeerLPort_Type = BasLogicalPortId
_BasRip2PeerLPort_Object = MibTableColumn
basRip2PeerLPort = _BasRip2PeerLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6, 1, 4, 1, 10),
    _BasRip2PeerLPort_Type()
)
basRip2PeerLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRip2PeerLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-RIPv2-MIB",
    **{"RouteTag": RouteTag,
       "basRip2": basRip2,
       "basRipObjects": basRipObjects,
       "basRip2GlobalsTable": basRip2GlobalsTable,
       "basRip2GlobalEntry": basRip2GlobalEntry,
       "basRip2GlobalRouteChanges": basRip2GlobalRouteChanges,
       "basRip2GlobalQueries": basRip2GlobalQueries,
       "basRip2GlobalChassis": basRip2GlobalChassis,
       "basRip2GlobalSlot": basRip2GlobalSlot,
       "basRip2GlobalIf": basRip2GlobalIf,
       "basRip2GlobalLPort": basRip2GlobalLPort,
       "basRip2IfStatTable": basRip2IfStatTable,
       "basRip2IfStatEntry": basRip2IfStatEntry,
       "basRip2IfStatAddress": basRip2IfStatAddress,
       "basRip2IfStatRcvBadPackets": basRip2IfStatRcvBadPackets,
       "basRip2IfStatRcvBadRoutes": basRip2IfStatRcvBadRoutes,
       "basRip2IfStatSentUpdates": basRip2IfStatSentUpdates,
       "basRip2IfStatStatus": basRip2IfStatStatus,
       "basRip2IfStatChassis": basRip2IfStatChassis,
       "basRip2IfStatSlot": basRip2IfStatSlot,
       "basRip2IfStatIf": basRip2IfStatIf,
       "basRip2IfStatLPort": basRip2IfStatLPort,
       "basRip2IfConfTable": basRip2IfConfTable,
       "basRip2IfConfEntry": basRip2IfConfEntry,
       "basRip2IfConfAddress": basRip2IfConfAddress,
       "basRip2IfConfDomain": basRip2IfConfDomain,
       "basRip2IfConfAuthType": basRip2IfConfAuthType,
       "basRip2IfConfAuthKey": basRip2IfConfAuthKey,
       "basRip2IfConfSend": basRip2IfConfSend,
       "basRip2IfConfReceive": basRip2IfConfReceive,
       "basRip2IfConfDefaultMetric": basRip2IfConfDefaultMetric,
       "basRip2IfConfStatus": basRip2IfConfStatus,
       "basRip2IfConfSrcAddress": basRip2IfConfSrcAddress,
       "basRip2IfConfChassis": basRip2IfConfChassis,
       "basRip2IfConfSlot": basRip2IfConfSlot,
       "basRip2IfConfIf": basRip2IfConfIf,
       "basRip2IfConfLPort": basRip2IfConfLPort,
       "basRip2PeerTable": basRip2PeerTable,
       "basRip2PeerEntry": basRip2PeerEntry,
       "basRip2PeerAddress": basRip2PeerAddress,
       "basRip2PeerDomain": basRip2PeerDomain,
       "basRip2PeerLastUpdate": basRip2PeerLastUpdate,
       "basRip2PeerVersion": basRip2PeerVersion,
       "basRip2PeerRcvBadPackets": basRip2PeerRcvBadPackets,
       "basRip2PeerRcvBadRoutes": basRip2PeerRcvBadRoutes,
       "basRip2PeerChassis": basRip2PeerChassis,
       "basRip2PeerSlot": basRip2PeerSlot,
       "basRip2PeerIf": basRip2PeerIf,
       "basRip2PeerLPort": basRip2PeerLPort}
)
