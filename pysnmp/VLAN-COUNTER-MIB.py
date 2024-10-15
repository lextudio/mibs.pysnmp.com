# SNMP MIB module (VLAN-COUNTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VLAN-COUNTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:45 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swVLANCounterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 65)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwVLANCounterCtrl_ObjectIdentity = ObjectIdentity
swVLANCounterCtrl = _SwVLANCounterCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 1)
)
_SwVLANCounterInfo_ObjectIdentity = ObjectIdentity
swVLANCounterInfo = _SwVLANCounterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 2)
)
_SwVLANCounterMgmt_ObjectIdentity = ObjectIdentity
swVLANCounterMgmt = _SwVLANCounterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3)
)
_SwVLANCounterTable_Object = MibTable
swVLANCounterTable = _SwVLANCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1)
)
if mibBuilder.loadTexts:
    swVLANCounterTable.setStatus("current")
_SwVLANCounterEntry_Object = MibTableRow
swVLANCounterEntry = _SwVLANCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1)
)
swVLANCounterEntry.setIndexNames(
    (0, "VLAN-COUNTER-MIB", "swVLANCounterVID"),
    (0, "VLAN-COUNTER-MIB", "swVLANCounterPort"),
    (0, "VLAN-COUNTER-MIB", "swVLANCounterPktType"),
    (0, "VLAN-COUNTER-MIB", "swVLANCounterLevel"),
)
if mibBuilder.loadTexts:
    swVLANCounterEntry.setStatus("current")
_SwVLANCounterVID_Type = Integer32
_SwVLANCounterVID_Object = MibTableColumn
swVLANCounterVID = _SwVLANCounterVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1, 1),
    _SwVLANCounterVID_Type()
)
swVLANCounterVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVLANCounterVID.setStatus("current")


class _SwVLANCounterPort_Type(Integer32):
    """Custom type swVLANCounterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwVLANCounterPort_Type.__name__ = "Integer32"
_SwVLANCounterPort_Object = MibTableColumn
swVLANCounterPort = _SwVLANCounterPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1, 2),
    _SwVLANCounterPort_Type()
)
swVLANCounterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVLANCounterPort.setStatus("current")


class _SwVLANCounterPktType_Type(Integer32):
    """Custom type swVLANCounterPktType based on Integer32"""
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
        *(("all_frame", 4),
          ("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_SwVLANCounterPktType_Type.__name__ = "Integer32"
_SwVLANCounterPktType_Object = MibTableColumn
swVLANCounterPktType = _SwVLANCounterPktType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1, 3),
    _SwVLANCounterPktType_Type()
)
swVLANCounterPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVLANCounterPktType.setStatus("current")


class _SwVLANCounterLevel_Type(Integer32):
    """Custom type swVLANCounterLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byte", 2),
          ("packet", 1))
    )


_SwVLANCounterLevel_Type.__name__ = "Integer32"
_SwVLANCounterLevel_Object = MibTableColumn
swVLANCounterLevel = _SwVLANCounterLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1, 4),
    _SwVLANCounterLevel_Type()
)
swVLANCounterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVLANCounterLevel.setStatus("current")
_SwVLANCounterTotalStats_Type = Counter64
_SwVLANCounterTotalStats_Object = MibTableColumn
swVLANCounterTotalStats = _SwVLANCounterTotalStats_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1, 5),
    _SwVLANCounterTotalStats_Type()
)
swVLANCounterTotalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVLANCounterTotalStats.setStatus("current")
_SwVLANCounterRateStats_Type = Counter64
_SwVLANCounterRateStats_Object = MibTableColumn
swVLANCounterRateStats = _SwVLANCounterRateStats_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1, 6),
    _SwVLANCounterRateStats_Type()
)
swVLANCounterRateStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVLANCounterRateStats.setStatus("current")
_SwVLANCounterRowStatus_Type = RowStatus
_SwVLANCounterRowStatus_Object = MibTableColumn
swVLANCounterRowStatus = _SwVLANCounterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 1, 1, 7),
    _SwVLANCounterRowStatus_Type()
)
swVLANCounterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVLANCounterRowStatus.setStatus("current")
_SwVLANCounterClearTable_Object = MibTable
swVLANCounterClearTable = _SwVLANCounterClearTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 2)
)
if mibBuilder.loadTexts:
    swVLANCounterClearTable.setStatus("current")
_SwVLANCounterClearEntry_Object = MibTableRow
swVLANCounterClearEntry = _SwVLANCounterClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 2, 1)
)
swVLANCounterClearEntry.setIndexNames(
    (0, "VLAN-COUNTER-MIB", "swVLANCounterVID"),
    (0, "VLAN-COUNTER-MIB", "swVLANCounterPort"),
)
if mibBuilder.loadTexts:
    swVLANCounterClearEntry.setStatus("current")


class _SwVLANCounterClearAction_Type(Integer32):
    """Custom type swVLANCounterClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwVLANCounterClearAction_Type.__name__ = "Integer32"
_SwVLANCounterClearAction_Object = MibTableColumn
swVLANCounterClearAction = _SwVLANCounterClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 65, 3, 2, 1, 1),
    _SwVLANCounterClearAction_Type()
)
swVLANCounterClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVLANCounterClearAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VLAN-COUNTER-MIB",
    **{"PortList": PortList,
       "swVLANCounterMIB": swVLANCounterMIB,
       "swVLANCounterCtrl": swVLANCounterCtrl,
       "swVLANCounterInfo": swVLANCounterInfo,
       "swVLANCounterMgmt": swVLANCounterMgmt,
       "swVLANCounterTable": swVLANCounterTable,
       "swVLANCounterEntry": swVLANCounterEntry,
       "swVLANCounterVID": swVLANCounterVID,
       "swVLANCounterPort": swVLANCounterPort,
       "swVLANCounterPktType": swVLANCounterPktType,
       "swVLANCounterLevel": swVLANCounterLevel,
       "swVLANCounterTotalStats": swVLANCounterTotalStats,
       "swVLANCounterRateStats": swVLANCounterRateStats,
       "swVLANCounterRowStatus": swVLANCounterRowStatus,
       "swVLANCounterClearTable": swVLANCounterClearTable,
       "swVLANCounterClearEntry": swVLANCounterClearEntry,
       "swVLANCounterClearAction": swVLANCounterClearAction}
)
