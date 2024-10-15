# SNMP MIB module (WWP-GENERIC-IGMP-SNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-GENERIC-IGMP-SNOOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:41 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpGenIgmpSnoopMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19)
)
wwpGenIgmpSnoopMIB.setRevisions(
        ("2005-05-24 00:00",
         "2003-05-02 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpGenIgmpSnoopMIBObjects_ObjectIdentity = ObjectIdentity
wwpGenIgmpSnoopMIBObjects = _WwpGenIgmpSnoopMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1)
)
_WwpGenIgmpSnoop_ObjectIdentity = ObjectIdentity
wwpGenIgmpSnoop = _WwpGenIgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1)
)


class _WwpGenIgmpSnoopGlobalActivate_Type(TruthValue):
    """Custom type wwpGenIgmpSnoopGlobalActivate based on TruthValue"""


_WwpGenIgmpSnoopGlobalActivate_Object = MibScalar
wwpGenIgmpSnoopGlobalActivate = _WwpGenIgmpSnoopGlobalActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 1),
    _WwpGenIgmpSnoopGlobalActivate_Type()
)
wwpGenIgmpSnoopGlobalActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopGlobalActivate.setStatus("current")
_WwpGenIgmpSnoopActTable_Object = MibTable
wwpGenIgmpSnoopActTable = _WwpGenIgmpSnoopActTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopActTable.setStatus("current")
_WwpGenIgmpSnoopActEntry_Object = MibTableRow
wwpGenIgmpSnoopActEntry = _WwpGenIgmpSnoopActEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 2, 1)
)
wwpGenIgmpSnoopActEntry.setIndexNames(
    (0, "WWP-GENERIC-IGMP-SNOOP-MIB", "wwpGenIgmpSnoopActVlanId"),
)
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopActEntry.setStatus("current")
_WwpGenIgmpSnoopActVlanId_Type = VlanId
_WwpGenIgmpSnoopActVlanId_Object = MibTableColumn
wwpGenIgmpSnoopActVlanId = _WwpGenIgmpSnoopActVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 2, 1, 1),
    _WwpGenIgmpSnoopActVlanId_Type()
)
wwpGenIgmpSnoopActVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopActVlanId.setStatus("current")


class _WwpGenIgmpSnoopRouterPort_Type(Integer32):
    """Custom type wwpGenIgmpSnoopRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpGenIgmpSnoopRouterPort_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopRouterPort_Object = MibTableColumn
wwpGenIgmpSnoopRouterPort = _WwpGenIgmpSnoopRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 2, 1, 2),
    _WwpGenIgmpSnoopRouterPort_Type()
)
wwpGenIgmpSnoopRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopRouterPort.setStatus("current")


class _WwpGenIgmpSnoopActivate_Type(TruthValue):
    """Custom type wwpGenIgmpSnoopActivate based on TruthValue"""


_WwpGenIgmpSnoopActivate_Object = MibTableColumn
wwpGenIgmpSnoopActivate = _WwpGenIgmpSnoopActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 2, 1, 3),
    _WwpGenIgmpSnoopActivate_Type()
)
wwpGenIgmpSnoopActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopActivate.setStatus("current")
_WwpGenIgmpSnoopTable_Object = MibTable
wwpGenIgmpSnoopTable = _WwpGenIgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopTable.setStatus("current")
_WwpGenIgmpSnoopEntry_Object = MibTableRow
wwpGenIgmpSnoopEntry = _WwpGenIgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 3, 1)
)
wwpGenIgmpSnoopEntry.setIndexNames(
    (0, "WWP-GENERIC-IGMP-SNOOP-MIB", "wwpGenIgmpSnoopVlanId"),
    (0, "WWP-GENERIC-IGMP-SNOOP-MIB", "wwpGenIgmpSnoopGroupAddress"),
)
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopEntry.setStatus("current")
_WwpGenIgmpSnoopVlanId_Type = VlanId
_WwpGenIgmpSnoopVlanId_Object = MibTableColumn
wwpGenIgmpSnoopVlanId = _WwpGenIgmpSnoopVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 3, 1, 1),
    _WwpGenIgmpSnoopVlanId_Type()
)
wwpGenIgmpSnoopVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopVlanId.setStatus("current")
_WwpGenIgmpSnoopGroupAddress_Type = IpAddress
_WwpGenIgmpSnoopGroupAddress_Object = MibTableColumn
wwpGenIgmpSnoopGroupAddress = _WwpGenIgmpSnoopGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 3, 1, 2),
    _WwpGenIgmpSnoopGroupAddress_Type()
)
wwpGenIgmpSnoopGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopGroupAddress.setStatus("current")
_WwpGenIgmpSnoopActivePorts_Type = PortList
_WwpGenIgmpSnoopActivePorts_Object = MibTableColumn
wwpGenIgmpSnoopActivePorts = _WwpGenIgmpSnoopActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 3, 1, 3),
    _WwpGenIgmpSnoopActivePorts_Type()
)
wwpGenIgmpSnoopActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopActivePorts.setStatus("current")
_WwpGenIgmpSnoopQueryTime_Type = TimeTicks
_WwpGenIgmpSnoopQueryTime_Object = MibTableColumn
wwpGenIgmpSnoopQueryTime = _WwpGenIgmpSnoopQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 3, 1, 4),
    _WwpGenIgmpSnoopQueryTime_Type()
)
wwpGenIgmpSnoopQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopQueryTime.setStatus("current")


class _WwpGenIgmpSnoopNoOfHosts_Type(Integer32):
    """Custom type wwpGenIgmpSnoopNoOfHosts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpGenIgmpSnoopNoOfHosts_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopNoOfHosts_Object = MibTableColumn
wwpGenIgmpSnoopNoOfHosts = _WwpGenIgmpSnoopNoOfHosts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 3, 1, 5),
    _WwpGenIgmpSnoopNoOfHosts_Type()
)
wwpGenIgmpSnoopNoOfHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopNoOfHosts.setStatus("deprecated")
_WwpGenIgmpSnoopStatsTable_Object = MibTable
wwpGenIgmpSnoopStatsTable = _WwpGenIgmpSnoopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopStatsTable.setStatus("current")
_WwpGenIgmpSnoopStatsEntry_Object = MibTableRow
wwpGenIgmpSnoopStatsEntry = _WwpGenIgmpSnoopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 4, 1)
)
wwpGenIgmpSnoopStatsEntry.setIndexNames(
    (0, "WWP-GENERIC-IGMP-SNOOP-MIB", "wwpGenIgmpSnoopStatsVlanId"),
)
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopStatsEntry.setStatus("current")
_WwpGenIgmpSnoopStatsVlanId_Type = VlanId
_WwpGenIgmpSnoopStatsVlanId_Object = MibTableColumn
wwpGenIgmpSnoopStatsVlanId = _WwpGenIgmpSnoopStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 4, 1, 1),
    _WwpGenIgmpSnoopStatsVlanId_Type()
)
wwpGenIgmpSnoopStatsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopStatsVlanId.setStatus("current")
_WwpGenIgmpSnoopQueryMessages_Type = Counter32
_WwpGenIgmpSnoopQueryMessages_Object = MibTableColumn
wwpGenIgmpSnoopQueryMessages = _WwpGenIgmpSnoopQueryMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 4, 1, 2),
    _WwpGenIgmpSnoopQueryMessages_Type()
)
wwpGenIgmpSnoopQueryMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopQueryMessages.setStatus("current")
_WwpGenIgmpSnoopJoinMessages_Type = Counter32
_WwpGenIgmpSnoopJoinMessages_Object = MibTableColumn
wwpGenIgmpSnoopJoinMessages = _WwpGenIgmpSnoopJoinMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 4, 1, 3),
    _WwpGenIgmpSnoopJoinMessages_Type()
)
wwpGenIgmpSnoopJoinMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopJoinMessages.setStatus("current")
_WwpGenIgmpSnoopLeaveMessages_Type = Counter32
_WwpGenIgmpSnoopLeaveMessages_Object = MibTableColumn
wwpGenIgmpSnoopLeaveMessages = _WwpGenIgmpSnoopLeaveMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 4, 1, 4),
    _WwpGenIgmpSnoopLeaveMessages_Type()
)
wwpGenIgmpSnoopLeaveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopLeaveMessages.setStatus("current")
_WwpGenIgmpSnoopRouterDiscards_Type = Counter32
_WwpGenIgmpSnoopRouterDiscards_Object = MibTableColumn
wwpGenIgmpSnoopRouterDiscards = _WwpGenIgmpSnoopRouterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 4, 1, 5),
    _WwpGenIgmpSnoopRouterDiscards_Type()
)
wwpGenIgmpSnoopRouterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopRouterDiscards.setStatus("current")


class _WwpGenIgmpSnoopLingerTimeout_Type(Integer32):
    """Custom type wwpGenIgmpSnoopLingerTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpGenIgmpSnoopLingerTimeout_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopLingerTimeout_Object = MibScalar
wwpGenIgmpSnoopLingerTimeout = _WwpGenIgmpSnoopLingerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 5),
    _WwpGenIgmpSnoopLingerTimeout_Type()
)
wwpGenIgmpSnoopLingerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopLingerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopLingerTimeout.setUnits("seconds")


class _WwpGenIgmpSnoopExpiryTimeout_Type(Integer32):
    """Custom type wwpGenIgmpSnoopExpiryTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpGenIgmpSnoopExpiryTimeout_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopExpiryTimeout_Object = MibScalar
wwpGenIgmpSnoopExpiryTimeout = _WwpGenIgmpSnoopExpiryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 6),
    _WwpGenIgmpSnoopExpiryTimeout_Type()
)
wwpGenIgmpSnoopExpiryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopExpiryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopExpiryTimeout.setUnits("seconds")


class _WwpGenIgmpSnoopQueryRespTimeout_Type(Integer32):
    """Custom type wwpGenIgmpSnoopQueryRespTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpGenIgmpSnoopQueryRespTimeout_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopQueryRespTimeout_Object = MibScalar
wwpGenIgmpSnoopQueryRespTimeout = _WwpGenIgmpSnoopQueryRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 7),
    _WwpGenIgmpSnoopQueryRespTimeout_Type()
)
wwpGenIgmpSnoopQueryRespTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopQueryRespTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopQueryRespTimeout.setUnits("seconds")


class _WwpGenIgmpSnoopFilterActivate_Type(TruthValue):
    """Custom type wwpGenIgmpSnoopFilterActivate based on TruthValue"""


_WwpGenIgmpSnoopFilterActivate_Object = MibScalar
wwpGenIgmpSnoopFilterActivate = _WwpGenIgmpSnoopFilterActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 8),
    _WwpGenIgmpSnoopFilterActivate_Type()
)
wwpGenIgmpSnoopFilterActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopFilterActivate.setStatus("current")
_WwpGenExtIgmpSnoopActEntryTable_Object = MibTable
wwpGenExtIgmpSnoopActEntryTable = _WwpGenExtIgmpSnoopActEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wwpGenExtIgmpSnoopActEntryTable.setStatus("current")
_WwpGenExtIgmpSnoopActEntry_Object = MibTableRow
wwpGenExtIgmpSnoopActEntry = _WwpGenExtIgmpSnoopActEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    wwpGenExtIgmpSnoopActEntry.setStatus("current")


class _WwpGenIgmpSnoopMinQueryTimeout_Type(Integer32):
    """Custom type wwpGenIgmpSnoopMinQueryTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpGenIgmpSnoopMinQueryTimeout_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopMinQueryTimeout_Object = MibTableColumn
wwpGenIgmpSnoopMinQueryTimeout = _WwpGenIgmpSnoopMinQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 9, 1, 1),
    _WwpGenIgmpSnoopMinQueryTimeout_Type()
)
wwpGenIgmpSnoopMinQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopMinQueryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopMinQueryTimeout.setUnits("seconds")


class _WwpGenIgmpSnoopUnresolvedMcastFilter_Type(TruthValue):
    """Custom type wwpGenIgmpSnoopUnresolvedMcastFilter based on TruthValue"""


_WwpGenIgmpSnoopUnresolvedMcastFilter_Object = MibTableColumn
wwpGenIgmpSnoopUnresolvedMcastFilter = _WwpGenIgmpSnoopUnresolvedMcastFilter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 9, 1, 2),
    _WwpGenIgmpSnoopUnresolvedMcastFilter_Type()
)
wwpGenIgmpSnoopUnresolvedMcastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopUnresolvedMcastFilter.setStatus("current")


class _WwpGenIgmpSnoopPktPriority_Type(Integer32):
    """Custom type wwpGenIgmpSnoopPktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpGenIgmpSnoopPktPriority_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopPktPriority_Object = MibTableColumn
wwpGenIgmpSnoopPktPriority = _WwpGenIgmpSnoopPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 9, 1, 3),
    _WwpGenIgmpSnoopPktPriority_Type()
)
wwpGenIgmpSnoopPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopPktPriority.setStatus("current")


class _WwpGenIgmpSnoopLeaveMode_Type(Integer32):
    """Custom type wwpGenIgmpSnoopLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("inquisitive", 2))
    )


_WwpGenIgmpSnoopLeaveMode_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopLeaveMode_Object = MibTableColumn
wwpGenIgmpSnoopLeaveMode = _WwpGenIgmpSnoopLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 9, 1, 4),
    _WwpGenIgmpSnoopLeaveMode_Type()
)
wwpGenIgmpSnoopLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopLeaveMode.setStatus("current")


class _WwpGenIgmpSnoopInqLeaveTimeout_Type(Integer32):
    """Custom type wwpGenIgmpSnoopInqLeaveTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpGenIgmpSnoopInqLeaveTimeout_Type.__name__ = "Integer32"
_WwpGenIgmpSnoopInqLeaveTimeout_Object = MibScalar
wwpGenIgmpSnoopInqLeaveTimeout = _WwpGenIgmpSnoopInqLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 10),
    _WwpGenIgmpSnoopInqLeaveTimeout_Type()
)
wwpGenIgmpSnoopInqLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopInqLeaveTimeout.setStatus("current")


class _WwpGenIgmpSnoopUMFFilterGlobal_Type(TruthValue):
    """Custom type wwpGenIgmpSnoopUMFFilterGlobal based on TruthValue"""


_WwpGenIgmpSnoopUMFFilterGlobal_Object = MibScalar
wwpGenIgmpSnoopUMFFilterGlobal = _WwpGenIgmpSnoopUMFFilterGlobal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 1, 1, 11),
    _WwpGenIgmpSnoopUMFFilterGlobal_Type()
)
wwpGenIgmpSnoopUMFFilterGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpGenIgmpSnoopUMFFilterGlobal.setStatus("current")
_WwpGenIgmpSnoopMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpGenIgmpSnoopMIBNotificationPrefix = _WwpGenIgmpSnoopMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 2)
)
_WwpGenIgmpSnoopMIBNotifications_ObjectIdentity = ObjectIdentity
wwpGenIgmpSnoopMIBNotifications = _WwpGenIgmpSnoopMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 2, 0)
)
_WwpGenIgmpSnoopMIBConformance_ObjectIdentity = ObjectIdentity
wwpGenIgmpSnoopMIBConformance = _WwpGenIgmpSnoopMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 3)
)
_WwpGenIgmpSnoopMIBCompliances_ObjectIdentity = ObjectIdentity
wwpGenIgmpSnoopMIBCompliances = _WwpGenIgmpSnoopMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 3, 1)
)
_WwpGenIgmpSnoopMIBGroups_ObjectIdentity = ObjectIdentity
wwpGenIgmpSnoopMIBGroups = _WwpGenIgmpSnoopMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 19, 3, 2)
)
wwpGenIgmpSnoopActEntry.registerAugmentions(
    ("WWP-GENERIC-IGMP-SNOOP-MIB",
     "wwpGenExtIgmpSnoopActEntry")
)
wwpGenExtIgmpSnoopActEntry.setIndexNames(*wwpGenIgmpSnoopActEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-GENERIC-IGMP-SNOOP-MIB",
    **{"PortList": PortList,
       "VlanId": VlanId,
       "wwpGenIgmpSnoopMIB": wwpGenIgmpSnoopMIB,
       "wwpGenIgmpSnoopMIBObjects": wwpGenIgmpSnoopMIBObjects,
       "wwpGenIgmpSnoop": wwpGenIgmpSnoop,
       "wwpGenIgmpSnoopGlobalActivate": wwpGenIgmpSnoopGlobalActivate,
       "wwpGenIgmpSnoopActTable": wwpGenIgmpSnoopActTable,
       "wwpGenIgmpSnoopActEntry": wwpGenIgmpSnoopActEntry,
       "wwpGenIgmpSnoopActVlanId": wwpGenIgmpSnoopActVlanId,
       "wwpGenIgmpSnoopRouterPort": wwpGenIgmpSnoopRouterPort,
       "wwpGenIgmpSnoopActivate": wwpGenIgmpSnoopActivate,
       "wwpGenIgmpSnoopTable": wwpGenIgmpSnoopTable,
       "wwpGenIgmpSnoopEntry": wwpGenIgmpSnoopEntry,
       "wwpGenIgmpSnoopVlanId": wwpGenIgmpSnoopVlanId,
       "wwpGenIgmpSnoopGroupAddress": wwpGenIgmpSnoopGroupAddress,
       "wwpGenIgmpSnoopActivePorts": wwpGenIgmpSnoopActivePorts,
       "wwpGenIgmpSnoopQueryTime": wwpGenIgmpSnoopQueryTime,
       "wwpGenIgmpSnoopNoOfHosts": wwpGenIgmpSnoopNoOfHosts,
       "wwpGenIgmpSnoopStatsTable": wwpGenIgmpSnoopStatsTable,
       "wwpGenIgmpSnoopStatsEntry": wwpGenIgmpSnoopStatsEntry,
       "wwpGenIgmpSnoopStatsVlanId": wwpGenIgmpSnoopStatsVlanId,
       "wwpGenIgmpSnoopQueryMessages": wwpGenIgmpSnoopQueryMessages,
       "wwpGenIgmpSnoopJoinMessages": wwpGenIgmpSnoopJoinMessages,
       "wwpGenIgmpSnoopLeaveMessages": wwpGenIgmpSnoopLeaveMessages,
       "wwpGenIgmpSnoopRouterDiscards": wwpGenIgmpSnoopRouterDiscards,
       "wwpGenIgmpSnoopLingerTimeout": wwpGenIgmpSnoopLingerTimeout,
       "wwpGenIgmpSnoopExpiryTimeout": wwpGenIgmpSnoopExpiryTimeout,
       "wwpGenIgmpSnoopQueryRespTimeout": wwpGenIgmpSnoopQueryRespTimeout,
       "wwpGenIgmpSnoopFilterActivate": wwpGenIgmpSnoopFilterActivate,
       "wwpGenExtIgmpSnoopActEntryTable": wwpGenExtIgmpSnoopActEntryTable,
       "wwpGenExtIgmpSnoopActEntry": wwpGenExtIgmpSnoopActEntry,
       "wwpGenIgmpSnoopMinQueryTimeout": wwpGenIgmpSnoopMinQueryTimeout,
       "wwpGenIgmpSnoopUnresolvedMcastFilter": wwpGenIgmpSnoopUnresolvedMcastFilter,
       "wwpGenIgmpSnoopPktPriority": wwpGenIgmpSnoopPktPriority,
       "wwpGenIgmpSnoopLeaveMode": wwpGenIgmpSnoopLeaveMode,
       "wwpGenIgmpSnoopInqLeaveTimeout": wwpGenIgmpSnoopInqLeaveTimeout,
       "wwpGenIgmpSnoopUMFFilterGlobal": wwpGenIgmpSnoopUMFFilterGlobal,
       "wwpGenIgmpSnoopMIBNotificationPrefix": wwpGenIgmpSnoopMIBNotificationPrefix,
       "wwpGenIgmpSnoopMIBNotifications": wwpGenIgmpSnoopMIBNotifications,
       "wwpGenIgmpSnoopMIBConformance": wwpGenIgmpSnoopMIBConformance,
       "wwpGenIgmpSnoopMIBCompliances": wwpGenIgmpSnoopMIBCompliances,
       "wwpGenIgmpSnoopMIBGroups": wwpGenIgmpSnoopMIBGroups}
)
