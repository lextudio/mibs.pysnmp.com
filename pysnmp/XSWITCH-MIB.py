# SNMP MIB module (XSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XSWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:39 2024
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwitchChip_ObjectIdentity = ObjectIdentity
switchChip = _SwitchChip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28)
)
_ScGen_ObjectIdentity = ObjectIdentity
scGen = _ScGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1)
)
_ScGenChassis_ObjectIdentity = ObjectIdentity
scGenChassis = _ScGenChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 1)
)


class _ScGenChMainAgPosition_Type(Integer32):
    """Custom type scGenChMainAgPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ScGenChMainAgPosition_Type.__name__ = "Integer32"
_ScGenChMainAgPosition_Object = MibScalar
scGenChMainAgPosition = _ScGenChMainAgPosition_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 1, 1),
    _ScGenChMainAgPosition_Type()
)
scGenChMainAgPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenChMainAgPosition.setStatus("mandatory")


class _ScGenChRedunAgPosition_Type(Integer32):
    """Custom type scGenChRedunAgPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ScGenChRedunAgPosition_Type.__name__ = "Integer32"
_ScGenChRedunAgPosition_Object = MibScalar
scGenChRedunAgPosition = _ScGenChRedunAgPosition_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 1, 2),
    _ScGenChRedunAgPosition_Type()
)
scGenChRedunAgPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenChRedunAgPosition.setStatus("mandatory")


class _ScGenChRedunAgActivityStatus_Type(Integer32):
    """Custom type scGenChRedunAgActivityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("dormant", 2),
          ("notPresent", 1),
          ("notSupported", 255))
    )


_ScGenChRedunAgActivityStatus_Type.__name__ = "Integer32"
_ScGenChRedunAgActivityStatus_Object = MibScalar
scGenChRedunAgActivityStatus = _ScGenChRedunAgActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 1, 3),
    _ScGenChRedunAgActivityStatus_Type()
)
scGenChRedunAgActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenChRedunAgActivityStatus.setStatus("mandatory")


class _ScGenChAgVLAN_Type(Integer32):
    """Custom type scGenChAgVLAN based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ScGenChAgVLAN_Type.__name__ = "Integer32"
_ScGenChAgVLAN_Object = MibScalar
scGenChAgVLAN = _ScGenChAgVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 1, 4),
    _ScGenChAgVLAN_Type()
)
scGenChAgVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenChAgVLAN.setStatus("mandatory")
_ScGenMon_ObjectIdentity = ObjectIdentity
scGenMon = _ScGenMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2)
)
_ScGenMonTable_Object = MibTable
scGenMonTable = _ScGenMonTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    scGenMonTable.setStatus("mandatory")
_ScGenMonEntry_Object = MibTableRow
scGenMonEntry = _ScGenMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1)
)
scGenMonEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenMonSwitchId"),
)
if mibBuilder.loadTexts:
    scGenMonEntry.setStatus("mandatory")


class _ScGenMonSwitchId_Type(Integer32):
    """Custom type scGenMonSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenMonSwitchId_Type.__name__ = "Integer32"
_ScGenMonSwitchId_Object = MibTableColumn
scGenMonSwitchId = _ScGenMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 1),
    _ScGenMonSwitchId_Type()
)
scGenMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonSwitchId.setStatus("mandatory")
_ScGenMonDropEvents_Type = Counter32
_ScGenMonDropEvents_Object = MibTableColumn
scGenMonDropEvents = _ScGenMonDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 2),
    _ScGenMonDropEvents_Type()
)
scGenMonDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonDropEvents.setStatus("mandatory")
_ScGenMonOctets_Type = Counter32
_ScGenMonOctets_Object = MibTableColumn
scGenMonOctets = _ScGenMonOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 3),
    _ScGenMonOctets_Type()
)
scGenMonOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonOctets.setStatus("mandatory")
_ScGenMonPkts_Type = Counter32
_ScGenMonPkts_Object = MibTableColumn
scGenMonPkts = _ScGenMonPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 4),
    _ScGenMonPkts_Type()
)
scGenMonPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonPkts.setStatus("mandatory")
_ScGenMonGoodBroadcastPkts_Type = Counter32
_ScGenMonGoodBroadcastPkts_Object = MibTableColumn
scGenMonGoodBroadcastPkts = _ScGenMonGoodBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 5),
    _ScGenMonGoodBroadcastPkts_Type()
)
scGenMonGoodBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonGoodBroadcastPkts.setStatus("mandatory")
_ScGenMonGoodMulticastPkts_Type = Counter32
_ScGenMonGoodMulticastPkts_Object = MibTableColumn
scGenMonGoodMulticastPkts = _ScGenMonGoodMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 6),
    _ScGenMonGoodMulticastPkts_Type()
)
scGenMonGoodMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonGoodMulticastPkts.setStatus("mandatory")
_ScGenMonGoodPkts_Type = Counter32
_ScGenMonGoodPkts_Object = MibTableColumn
scGenMonGoodPkts = _ScGenMonGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 7),
    _ScGenMonGoodPkts_Type()
)
scGenMonGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonGoodPkts.setStatus("mandatory")
_ScGenMonBadPkts_Type = Counter32
_ScGenMonBadPkts_Object = MibTableColumn
scGenMonBadPkts = _ScGenMonBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 8),
    _ScGenMonBadPkts_Type()
)
scGenMonBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonBadPkts.setStatus("mandatory")
_ScGenMonGoodOctets_Type = Counter32
_ScGenMonGoodOctets_Object = MibTableColumn
scGenMonGoodOctets = _ScGenMonGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 9),
    _ScGenMonGoodOctets_Type()
)
scGenMonGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonGoodOctets.setStatus("mandatory")
_ScGenMonBadOctets_Type = Counter32
_ScGenMonBadOctets_Object = MibTableColumn
scGenMonBadOctets = _ScGenMonBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 10),
    _ScGenMonBadOctets_Type()
)
scGenMonBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonBadOctets.setStatus("mandatory")


class _ScGenMonSmonCapability_Type(OctetString):
    """Custom type scGenMonSmonCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScGenMonSmonCapability_Type.__name__ = "OctetString"
_ScGenMonSmonCapability_Object = MibTableColumn
scGenMonSmonCapability = _ScGenMonSmonCapability_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 11),
    _ScGenMonSmonCapability_Type()
)
scGenMonSmonCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonSmonCapability.setStatus("mandatory")


class _ScGenMonMIBCtrMode_Type(Integer32):
    """Custom type scGenMonMIBCtrMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenMonMIBCtrMode_Type.__name__ = "Integer32"
_ScGenMonMIBCtrMode_Object = MibTableColumn
scGenMonMIBCtrMode = _ScGenMonMIBCtrMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 12),
    _ScGenMonMIBCtrMode_Type()
)
scGenMonMIBCtrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenMonMIBCtrMode.setStatus("mandatory")


class _ScGenMonSwitchVLANList_Type(OctetString):
    """Custom type scGenMonSwitchVLANList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ScGenMonSwitchVLANList_Type.__name__ = "OctetString"
_ScGenMonSwitchVLANList_Object = MibTableColumn
scGenMonSwitchVLANList = _ScGenMonSwitchVLANList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 13),
    _ScGenMonSwitchVLANList_Type()
)
scGenMonSwitchVLANList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonSwitchVLANList.setStatus("mandatory")


class _ScGenMonMIBCtrList_Type(OctetString):
    """Custom type scGenMonMIBCtrList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ScGenMonMIBCtrList_Type.__name__ = "OctetString"
_ScGenMonMIBCtrList_Object = MibTableColumn
scGenMonMIBCtrList = _ScGenMonMIBCtrList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 14),
    _ScGenMonMIBCtrList_Type()
)
scGenMonMIBCtrList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonMIBCtrList.setStatus("mandatory")
_ScGenMonTimeStamp_Type = TimeTicks
_ScGenMonTimeStamp_Object = MibTableColumn
scGenMonTimeStamp = _ScGenMonTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 15),
    _ScGenMonTimeStamp_Type()
)
scGenMonTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonTimeStamp.setStatus("mandatory")
_ScGenMonVlanTimeStamp_Type = TimeTicks
_ScGenMonVlanTimeStamp_Object = MibTableColumn
scGenMonVlanTimeStamp = _ScGenMonVlanTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 1, 1, 16),
    _ScGenMonVlanTimeStamp_Type()
)
scGenMonVlanTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVlanTimeStamp.setStatus("mandatory")
_ScGenMonPriorityTable_Object = MibTable
scGenMonPriorityTable = _ScGenMonPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 2)
)
if mibBuilder.loadTexts:
    scGenMonPriorityTable.setStatus("mandatory")
_ScGenMonPriorityEntry_Object = MibTableRow
scGenMonPriorityEntry = _ScGenMonPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 2, 1)
)
scGenMonPriorityEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenMonPrioritySwitchId"),
    (0, "XSWITCH-MIB", "scGenMonPriorityId"),
)
if mibBuilder.loadTexts:
    scGenMonPriorityEntry.setStatus("mandatory")


class _ScGenMonPrioritySwitchId_Type(Integer32):
    """Custom type scGenMonPrioritySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenMonPrioritySwitchId_Type.__name__ = "Integer32"
_ScGenMonPrioritySwitchId_Object = MibTableColumn
scGenMonPrioritySwitchId = _ScGenMonPrioritySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 2, 1, 1),
    _ScGenMonPrioritySwitchId_Type()
)
scGenMonPrioritySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonPrioritySwitchId.setStatus("mandatory")


class _ScGenMonPriorityId_Type(Integer32):
    """Custom type scGenMonPriorityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ScGenMonPriorityId_Type.__name__ = "Integer32"
_ScGenMonPriorityId_Object = MibTableColumn
scGenMonPriorityId = _ScGenMonPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 2, 1, 2),
    _ScGenMonPriorityId_Type()
)
scGenMonPriorityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonPriorityId.setStatus("mandatory")
_ScGenMonPriorityGoodPkts_Type = Counter32
_ScGenMonPriorityGoodPkts_Object = MibTableColumn
scGenMonPriorityGoodPkts = _ScGenMonPriorityGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 2, 1, 3),
    _ScGenMonPriorityGoodPkts_Type()
)
scGenMonPriorityGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonPriorityGoodPkts.setStatus("mandatory")
_ScGenMonPriorityGoodOctets_Type = Counter32
_ScGenMonPriorityGoodOctets_Object = MibTableColumn
scGenMonPriorityGoodOctets = _ScGenMonPriorityGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 2, 1, 4),
    _ScGenMonPriorityGoodOctets_Type()
)
scGenMonPriorityGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonPriorityGoodOctets.setStatus("mandatory")


class _ScGenMonVLANList_Type(OctetString):
    """Custom type scGenMonVLANList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ScGenMonVLANList_Type.__name__ = "OctetString"
_ScGenMonVLANList_Object = MibScalar
scGenMonVLANList = _ScGenMonVLANList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 3),
    _ScGenMonVLANList_Type()
)
scGenMonVLANList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANList.setStatus("mandatory")
_ScGenMonVLANTable_Object = MibTable
scGenMonVLANTable = _ScGenMonVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4)
)
if mibBuilder.loadTexts:
    scGenMonVLANTable.setStatus("mandatory")
_ScGenMonVLANEntry_Object = MibTableRow
scGenMonVLANEntry = _ScGenMonVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1)
)
scGenMonVLANEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenMonVLANSwitchId"),
    (0, "XSWITCH-MIB", "scGenMonVLANId"),
)
if mibBuilder.loadTexts:
    scGenMonVLANEntry.setStatus("mandatory")


class _ScGenMonVLANSwitchId_Type(Integer32):
    """Custom type scGenMonVLANSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenMonVLANSwitchId_Type.__name__ = "Integer32"
_ScGenMonVLANSwitchId_Object = MibTableColumn
scGenMonVLANSwitchId = _ScGenMonVLANSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1, 1),
    _ScGenMonVLANSwitchId_Type()
)
scGenMonVLANSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANSwitchId.setStatus("mandatory")
_ScGenMonVLANId_Type = Integer32
_ScGenMonVLANId_Object = MibTableColumn
scGenMonVLANId = _ScGenMonVLANId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1, 2),
    _ScGenMonVLANId_Type()
)
scGenMonVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANId.setStatus("mandatory")
_ScGenMonVLANGoodPkts_Type = Counter32
_ScGenMonVLANGoodPkts_Object = MibTableColumn
scGenMonVLANGoodPkts = _ScGenMonVLANGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1, 3),
    _ScGenMonVLANGoodPkts_Type()
)
scGenMonVLANGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANGoodPkts.setStatus("mandatory")
_ScGenMonVLANGoodOctets_Type = Counter32
_ScGenMonVLANGoodOctets_Object = MibTableColumn
scGenMonVLANGoodOctets = _ScGenMonVLANGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1, 4),
    _ScGenMonVLANGoodOctets_Type()
)
scGenMonVLANGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANGoodOctets.setStatus("mandatory")
_ScGenMonVLANStatsUcastPkts_Type = Counter32
_ScGenMonVLANStatsUcastPkts_Object = MibTableColumn
scGenMonVLANStatsUcastPkts = _ScGenMonVLANStatsUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1, 5),
    _ScGenMonVLANStatsUcastPkts_Type()
)
scGenMonVLANStatsUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANStatsUcastPkts.setStatus("mandatory")
_ScGenMonVLANStatsMcastPkts_Type = Counter32
_ScGenMonVLANStatsMcastPkts_Object = MibTableColumn
scGenMonVLANStatsMcastPkts = _ScGenMonVLANStatsMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1, 6),
    _ScGenMonVLANStatsMcastPkts_Type()
)
scGenMonVLANStatsMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANStatsMcastPkts.setStatus("mandatory")
_ScGenMonVLANStatsBcastPkts_Type = Counter32
_ScGenMonVLANStatsBcastPkts_Object = MibTableColumn
scGenMonVLANStatsBcastPkts = _ScGenMonVLANStatsBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 4, 1, 7),
    _ScGenMonVLANStatsBcastPkts_Type()
)
scGenMonVLANStatsBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonVLANStatsBcastPkts.setStatus("mandatory")


class _ScGenMonSwitches_Type(OctetString):
    """Custom type scGenMonSwitches based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ScGenMonSwitches_Type.__name__ = "OctetString"
_ScGenMonSwitches_Object = MibScalar
scGenMonSwitches = _ScGenMonSwitches_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 5),
    _ScGenMonSwitches_Type()
)
scGenMonSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenMonSwitches.setStatus("mandatory")
_ScHostTimePortCorrTable_Object = MibTable
scHostTimePortCorrTable = _ScHostTimePortCorrTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 6)
)
if mibBuilder.loadTexts:
    scHostTimePortCorrTable.setStatus("mandatory")
_ScHostTimePortCorrEntry_Object = MibTableRow
scHostTimePortCorrEntry = _ScHostTimePortCorrEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 6, 1)
)
scHostTimePortCorrEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scHostTimeIndex"),
    (0, "XSWITCH-MIB", "scHostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    scHostTimePortCorrEntry.setStatus("mandatory")
_ScHostTimeAddress_Type = OctetString
_ScHostTimeAddress_Object = MibTableColumn
scHostTimeAddress = _ScHostTimeAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 6, 1, 1),
    _ScHostTimeAddress_Type()
)
scHostTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHostTimeAddress.setStatus("mandatory")


class _ScHostTimeCreationOrder_Type(Integer32):
    """Custom type scHostTimeCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ScHostTimeCreationOrder_Type.__name__ = "Integer32"
_ScHostTimeCreationOrder_Object = MibTableColumn
scHostTimeCreationOrder = _ScHostTimeCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 6, 1, 2),
    _ScHostTimeCreationOrder_Type()
)
scHostTimeCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHostTimeCreationOrder.setStatus("mandatory")


class _ScHostTimeIndex_Type(Integer32):
    """Custom type scHostTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ScHostTimeIndex_Type.__name__ = "Integer32"
_ScHostTimeIndex_Object = MibTableColumn
scHostTimeIndex = _ScHostTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 6, 1, 3),
    _ScHostTimeIndex_Type()
)
scHostTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHostTimeIndex.setStatus("mandatory")
_ScHostTimePortConnection_Type = Integer32
_ScHostTimePortConnection_Object = MibTableColumn
scHostTimePortConnection = _ScHostTimePortConnection_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 2, 6, 1, 4),
    _ScHostTimePortConnection_Type()
)
scHostTimePortConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHostTimePortConnection.setStatus("mandatory")
_ScGenGroup_ObjectIdentity = ObjectIdentity
scGenGroup = _ScGenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3)
)
_ScGenGroupTable_Object = MibTable
scGenGroupTable = _ScGenGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1)
)
if mibBuilder.loadTexts:
    scGenGroupTable.setStatus("mandatory")
_ScGenGroupEntry_Object = MibTableRow
scGenGroupEntry = _ScGenGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1)
)
scGenGroupEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenGroupId"),
)
if mibBuilder.loadTexts:
    scGenGroupEntry.setStatus("mandatory")
_ScGenGroupId_Type = Integer32
_ScGenGroupId_Object = MibTableColumn
scGenGroupId = _ScGenGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 1),
    _ScGenGroupId_Type()
)
scGenGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupId.setStatus("mandatory")


class _ScGenGroupUseSwitches_Type(Integer32):
    """Custom type scGenGroupUseSwitches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenGroupUseSwitches_Type.__name__ = "Integer32"
_ScGenGroupUseSwitches_Object = MibTableColumn
scGenGroupUseSwitches = _ScGenGroupUseSwitches_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 2),
    _ScGenGroupUseSwitches_Type()
)
scGenGroupUseSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupUseSwitches.setStatus("mandatory")


class _ScGenGroupCopyPortSupport_Type(Integer32):
    """Custom type scGenGroupCopyPortSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenGroupCopyPortSupport_Type.__name__ = "Integer32"
_ScGenGroupCopyPortSupport_Object = MibTableColumn
scGenGroupCopyPortSupport = _ScGenGroupCopyPortSupport_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 3),
    _ScGenGroupCopyPortSupport_Type()
)
scGenGroupCopyPortSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupCopyPortSupport.setStatus("mandatory")


class _ScGenGroupXswitchConnection_Type(Integer32):
    """Custom type scGenGroupXswitchConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenGroupXswitchConnection_Type.__name__ = "Integer32"
_ScGenGroupXswitchConnection_Object = MibTableColumn
scGenGroupXswitchConnection = _ScGenGroupXswitchConnection_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 4),
    _ScGenGroupXswitchConnection_Type()
)
scGenGroupXswitchConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupXswitchConnection.setStatus("mandatory")


class _ScGenGroupStatus_Type(Integer32):
    """Custom type scGenGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("loadsBudgetProblem", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_ScGenGroupStatus_Type.__name__ = "Integer32"
_ScGenGroupStatus_Object = MibTableColumn
scGenGroupStatus = _ScGenGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 5),
    _ScGenGroupStatus_Type()
)
scGenGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupStatus.setStatus("mandatory")


class _ScGenGroupSwitchType_Type(Integer32):
    """Custom type scGenGroupSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("notSupported", 255),
          ("token-ring", 2))
    )


_ScGenGroupSwitchType_Type.__name__ = "Integer32"
_ScGenGroupSwitchType_Object = MibTableColumn
scGenGroupSwitchType = _ScGenGroupSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 6),
    _ScGenGroupSwitchType_Type()
)
scGenGroupSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSwitchType.setStatus("mandatory")


class _ScGenGroupNumberOfLoads_Type(Integer32):
    """Custom type scGenGroupNumberOfLoads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenGroupNumberOfLoads_Type.__name__ = "Integer32"
_ScGenGroupNumberOfLoads_Object = MibTableColumn
scGenGroupNumberOfLoads = _ScGenGroupNumberOfLoads_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 7),
    _ScGenGroupNumberOfLoads_Type()
)
scGenGroupNumberOfLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupNumberOfLoads.setStatus("mandatory")


class _ScGenGroupSetDefaults_Type(Integer32):
    """Custom type scGenGroupSetDefaults based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("layer2Only", 3),
          ("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenGroupSetDefaults_Type.__name__ = "Integer32"
_ScGenGroupSetDefaults_Object = MibTableColumn
scGenGroupSetDefaults = _ScGenGroupSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 8),
    _ScGenGroupSetDefaults_Type()
)
scGenGroupSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupSetDefaults.setStatus("mandatory")
_ScGenGroupSupportCopyPortList_Type = OctetString
_ScGenGroupSupportCopyPortList_Object = MibTableColumn
scGenGroupSupportCopyPortList = _ScGenGroupSupportCopyPortList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 9),
    _ScGenGroupSupportCopyPortList_Type()
)
scGenGroupSupportCopyPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSupportCopyPortList.setStatus("mandatory")
_ScGenGroupSupportPortCountersList_Type = OctetString
_ScGenGroupSupportPortCountersList_Object = MibTableColumn
scGenGroupSupportPortCountersList = _ScGenGroupSupportPortCountersList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 10),
    _ScGenGroupSupportPortCountersList_Type()
)
scGenGroupSupportPortCountersList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSupportPortCountersList.setStatus("mandatory")
_ScGenGroupSupportSegCountersList_Type = OctetString
_ScGenGroupSupportSegCountersList_Object = MibTableColumn
scGenGroupSupportSegCountersList = _ScGenGroupSupportSegCountersList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 11),
    _ScGenGroupSupportSegCountersList_Type()
)
scGenGroupSupportSegCountersList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSupportSegCountersList.setStatus("mandatory")


class _ScGenGroupUpLinkType_Type(Integer32):
    """Custom type scGenGroupUpLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1),
          ("notSupported", 255))
    )


_ScGenGroupUpLinkType_Type.__name__ = "Integer32"
_ScGenGroupUpLinkType_Object = MibTableColumn
scGenGroupUpLinkType = _ScGenGroupUpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 12),
    _ScGenGroupUpLinkType_Type()
)
scGenGroupUpLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupUpLinkType.setStatus("mandatory")


class _ScGenGroupPlugInType_Type(Integer32):
    """Custom type scGenGroupPlugInType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              31,
              32,
              33,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cajunX120F2", 2),
          ("cajunX120F4", 8),
          ("cajunX120G2", 9),
          ("cajunX120GT2", 10),
          ("cajunX120L1", 5),
          ("cajunX120L2", 6),
          ("cajunX120S1", 3),
          ("cajunX120S2", 4),
          ("cajunX120T16", 7),
          ("cajunX120T8", 1),
          ("cajunX130F2", 31),
          ("cajunX130G2", 32),
          ("cajunX130GT2", 33),
          ("cajunX330-OC12F1", 18),
          ("cajunX330-OC12F2", 19),
          ("cajunX330-OC12S1", 22),
          ("cajunX330-OC12S2", 23),
          ("cajunX330-OC3F1", 20),
          ("cajunX330-OC3F2", 21),
          ("cajunX330F2", 13),
          ("cajunX330F4", 12),
          ("cajunX330G2", 26),
          ("cajunX330GT2", 25),
          ("cajunX330GT4", 24),
          ("cajunX330L1", 16),
          ("cajunX330L2", 14),
          ("cajunX330S1", 17),
          ("cajunX330S2", 15),
          ("cajunX330SSM", 27),
          ("cajunX330T16", 11),
          ("none", 255),
          ("unknown", 254))
    )


_ScGenGroupPlugInType_Type.__name__ = "Integer32"
_ScGenGroupPlugInType_Object = MibTableColumn
scGenGroupPlugInType = _ScGenGroupPlugInType_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 13),
    _ScGenGroupPlugInType_Type()
)
scGenGroupPlugInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupPlugInType.setStatus("mandatory")


class _ScGenGroupPlugInDescr_Type(DisplayString):
    """Custom type scGenGroupPlugInDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScGenGroupPlugInDescr_Type.__name__ = "DisplayString"
_ScGenGroupPlugInDescr_Object = MibTableColumn
scGenGroupPlugInDescr = _ScGenGroupPlugInDescr_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 14),
    _ScGenGroupPlugInDescr_Type()
)
scGenGroupPlugInDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupPlugInDescr.setStatus("mandatory")
_ScGenGroupPlugInCS_Type = DisplayString
_ScGenGroupPlugInCS_Object = MibTableColumn
scGenGroupPlugInCS = _ScGenGroupPlugInCS_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 15),
    _ScGenGroupPlugInCS_Type()
)
scGenGroupPlugInCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupPlugInCS.setStatus("mandatory")


class _ScGenGroupDefaultVLAN_Type(Integer32):
    """Custom type scGenGroupDefaultVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("vlan0", 1),
          ("vlan1", 2))
    )


_ScGenGroupDefaultVLAN_Type.__name__ = "Integer32"
_ScGenGroupDefaultVLAN_Object = MibTableColumn
scGenGroupDefaultVLAN = _ScGenGroupDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 16),
    _ScGenGroupDefaultVLAN_Type()
)
scGenGroupDefaultVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupDefaultVLAN.setStatus("mandatory")


class _ScGenGroupCascadingType_Type(Integer32):
    """Custom type scGenGroupCascadingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cajunX330MLSTK", 2),
          ("cajunX330STK", 1),
          ("none", 255),
          ("unknown", 254))
    )


_ScGenGroupCascadingType_Type.__name__ = "Integer32"
_ScGenGroupCascadingType_Object = MibTableColumn
scGenGroupCascadingType = _ScGenGroupCascadingType_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 17),
    _ScGenGroupCascadingType_Type()
)
scGenGroupCascadingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupCascadingType.setStatus("mandatory")


class _ScGenGroupCascadingDescr_Type(DisplayString):
    """Custom type scGenGroupCascadingDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScGenGroupCascadingDescr_Type.__name__ = "DisplayString"
_ScGenGroupCascadingDescr_Object = MibTableColumn
scGenGroupCascadingDescr = _ScGenGroupCascadingDescr_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 18),
    _ScGenGroupCascadingDescr_Type()
)
scGenGroupCascadingDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupCascadingDescr.setStatus("mandatory")
_ScGenGroupCascadingCS_Type = DisplayString
_ScGenGroupCascadingCS_Object = MibTableColumn
scGenGroupCascadingCS = _ScGenGroupCascadingCS_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 19),
    _ScGenGroupCascadingCS_Type()
)
scGenGroupCascadingCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupCascadingCS.setStatus("mandatory")
_ScGenGroupSupportDstCopyPortList_Type = OctetString
_ScGenGroupSupportDstCopyPortList_Object = MibTableColumn
scGenGroupSupportDstCopyPortList = _ScGenGroupSupportDstCopyPortList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 20),
    _ScGenGroupSupportDstCopyPortList_Type()
)
scGenGroupSupportDstCopyPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSupportDstCopyPortList.setStatus("mandatory")


class _ScGenGroupBUPSType_Type(Integer32):
    """Custom type scGenGroupBUPSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("none", 255))
    )


_ScGenGroupBUPSType_Type.__name__ = "Integer32"
_ScGenGroupBUPSType_Object = MibTableColumn
scGenGroupBUPSType = _ScGenGroupBUPSType_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 21),
    _ScGenGroupBUPSType_Type()
)
scGenGroupBUPSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupBUPSType.setStatus("mandatory")
_ScGenGroupBUPSCS_Type = DisplayString
_ScGenGroupBUPSCS_Object = MibTableColumn
scGenGroupBUPSCS = _ScGenGroupBUPSCS_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 22),
    _ScGenGroupBUPSCS_Type()
)
scGenGroupBUPSCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupBUPSCS.setStatus("mandatory")


class _ScGenGroupBUPSFansStatus_Type(Integer32):
    """Custom type scGenGroupBUPSFansStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allFansOK", 1),
          ("notSupported", 255),
          ("oneFanFailed", 2))
    )


_ScGenGroupBUPSFansStatus_Type.__name__ = "Integer32"
_ScGenGroupBUPSFansStatus_Object = MibTableColumn
scGenGroupBUPSFansStatus = _ScGenGroupBUPSFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 23),
    _ScGenGroupBUPSFansStatus_Type()
)
scGenGroupBUPSFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupBUPSFansStatus.setStatus("mandatory")


class _ScGenGroupFansStatus_Type(Integer32):
    """Custom type scGenGroupFansStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allFansOK", 1),
          ("notSupported", 255),
          ("oneFanFailed", 2))
    )


_ScGenGroupFansStatus_Type.__name__ = "Integer32"
_ScGenGroupFansStatus_Object = MibTableColumn
scGenGroupFansStatus = _ScGenGroupFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 24),
    _ScGenGroupFansStatus_Type()
)
scGenGroupFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupFansStatus.setStatus("mandatory")


class _ScGenGroupInternalBuffering_Type(Integer32):
    """Custom type scGenGroupInternalBuffering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("max", 2),
          ("med", 3),
          ("min", 1),
          ("notSupported", 255))
    )


_ScGenGroupInternalBuffering_Type.__name__ = "Integer32"
_ScGenGroupInternalBuffering_Object = MibTableColumn
scGenGroupInternalBuffering = _ScGenGroupInternalBuffering_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 25),
    _ScGenGroupInternalBuffering_Type()
)
scGenGroupInternalBuffering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupInternalBuffering.setStatus("mandatory")


class _ScGenGroupMcFilterBoxSupport_Type(Integer32):
    """Custom type scGenGroupMcFilterBoxSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("filterNotSupport", 2),
          ("filteringSupported", 1),
          ("notSupported", 255))
    )


_ScGenGroupMcFilterBoxSupport_Type.__name__ = "Integer32"
_ScGenGroupMcFilterBoxSupport_Object = MibTableColumn
scGenGroupMcFilterBoxSupport = _ScGenGroupMcFilterBoxSupport_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 26),
    _ScGenGroupMcFilterBoxSupport_Type()
)
scGenGroupMcFilterBoxSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupMcFilterBoxSupport.setStatus("mandatory")


class _ScGenGroupMcFilterPersonalitySupport_Type(Integer32):
    """Custom type scGenGroupMcFilterPersonalitySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("filterNotSupport", 2),
          ("filteringSupported", 1),
          ("notSupported", 255),
          ("personalityNotInstalled", 3))
    )


_ScGenGroupMcFilterPersonalitySupport_Type.__name__ = "Integer32"
_ScGenGroupMcFilterPersonalitySupport_Object = MibTableColumn
scGenGroupMcFilterPersonalitySupport = _ScGenGroupMcFilterPersonalitySupport_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 27),
    _ScGenGroupMcFilterPersonalitySupport_Type()
)
scGenGroupMcFilterPersonalitySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupMcFilterPersonalitySupport.setStatus("mandatory")


class _ScGenGroupMcFilterStackingSupport_Type(Integer32):
    """Custom type scGenGroupMcFilterStackingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("filterNotSupport", 2),
          ("filteringSupported", 1),
          ("notSupported", 255),
          ("stackingNotInstalled", 3))
    )


_ScGenGroupMcFilterStackingSupport_Type.__name__ = "Integer32"
_ScGenGroupMcFilterStackingSupport_Object = MibTableColumn
scGenGroupMcFilterStackingSupport = _ScGenGroupMcFilterStackingSupport_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 28),
    _ScGenGroupMcFilterStackingSupport_Type()
)
scGenGroupMcFilterStackingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupMcFilterStackingSupport.setStatus("mandatory")


class _ScGenGroupLACPMode_Type(Integer32):
    """Custom type scGenGroupLACPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ScGenGroupLACPMode_Type.__name__ = "Integer32"
_ScGenGroupLACPMode_Object = MibTableColumn
scGenGroupLACPMode = _ScGenGroupLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 29),
    _ScGenGroupLACPMode_Type()
)
scGenGroupLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupLACPMode.setStatus("mandatory")


class _ScGenGroupSecurityMode_Type(Integer32):
    """Custom type scGenGroupSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("nonSecurityMode", 1),
          ("notSupported", 255),
          ("securityMode", 2))
    )


_ScGenGroupSecurityMode_Type.__name__ = "Integer32"
_ScGenGroupSecurityMode_Object = MibTableColumn
scGenGroupSecurityMode = _ScGenGroupSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 30),
    _ScGenGroupSecurityMode_Type()
)
scGenGroupSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupSecurityMode.setStatus("mandatory")


class _ScGenGroupBroadcastStormControl_Type(Integer32):
    """Custom type scGenGroupBroadcastStormControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenGroupBroadcastStormControl_Type.__name__ = "Integer32"
_ScGenGroupBroadcastStormControl_Object = MibTableColumn
scGenGroupBroadcastStormControl = _ScGenGroupBroadcastStormControl_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 31),
    _ScGenGroupBroadcastStormControl_Type()
)
scGenGroupBroadcastStormControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupBroadcastStormControl.setStatus("mandatory")


class _ScGenGroupBroadcastThreshold_Type(Integer32):
    """Custom type scGenGroupBroadcastThreshold based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 144000),
    )


_ScGenGroupBroadcastThreshold_Type.__name__ = "Integer32"
_ScGenGroupBroadcastThreshold_Object = MibTableColumn
scGenGroupBroadcastThreshold = _ScGenGroupBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 32),
    _ScGenGroupBroadcastThreshold_Type()
)
scGenGroupBroadcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupBroadcastThreshold.setStatus("mandatory")


class _ScGenGroupPriorityQueuesScheduling_Type(Integer32):
    """Custom type scGenGroupPriorityQueuesScheduling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("strict", 1),
          ("weighted", 2))
    )


_ScGenGroupPriorityQueuesScheduling_Type.__name__ = "Integer32"
_ScGenGroupPriorityQueuesScheduling_Object = MibTableColumn
scGenGroupPriorityQueuesScheduling = _ScGenGroupPriorityQueuesScheduling_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 33),
    _ScGenGroupPriorityQueuesScheduling_Type()
)
scGenGroupPriorityQueuesScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupPriorityQueuesScheduling.setStatus("mandatory")


class _ScGenGroupBoundedDelay_Type(Integer32):
    """Custom type scGenGroupBoundedDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenGroupBoundedDelay_Type.__name__ = "Integer32"
_ScGenGroupBoundedDelay_Object = MibTableColumn
scGenGroupBoundedDelay = _ScGenGroupBoundedDelay_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 34),
    _ScGenGroupBoundedDelay_Type()
)
scGenGroupBoundedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupBoundedDelay.setStatus("mandatory")


class _ScGenGroupSLDAdminStatus_Type(Integer32):
    """Custom type scGenGroupSLDAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenGroupSLDAdminStatus_Type.__name__ = "Integer32"
_ScGenGroupSLDAdminStatus_Object = MibTableColumn
scGenGroupSLDAdminStatus = _ScGenGroupSLDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 1, 1, 35),
    _ScGenGroupSLDAdminStatus_Type()
)
scGenGroupSLDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupSLDAdminStatus.setStatus("mandatory")
_ScGenGroupSmonTable_Object = MibTable
scGenGroupSmonTable = _ScGenGroupSmonTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2)
)
if mibBuilder.loadTexts:
    scGenGroupSmonTable.setStatus("mandatory")
_ScGenGroupSmonEntry_Object = MibTableRow
scGenGroupSmonEntry = _ScGenGroupSmonEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1)
)
scGenGroupSmonEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenGroupSmonGroupId"),
)
if mibBuilder.loadTexts:
    scGenGroupSmonEntry.setStatus("mandatory")
_ScGenGroupSmonGroupId_Type = Integer32
_ScGenGroupSmonGroupId_Object = MibTableColumn
scGenGroupSmonGroupId = _ScGenGroupSmonGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 1),
    _ScGenGroupSmonGroupId_Type()
)
scGenGroupSmonGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonGroupId.setStatus("mandatory")


class _ScGenGroupSmonCapability_Type(OctetString):
    """Custom type scGenGroupSmonCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScGenGroupSmonCapability_Type.__name__ = "OctetString"
_ScGenGroupSmonCapability_Object = MibTableColumn
scGenGroupSmonCapability = _ScGenGroupSmonCapability_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 2),
    _ScGenGroupSmonCapability_Type()
)
scGenGroupSmonCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonCapability.setStatus("mandatory")


class _ScGenGroupSmonVlanList_Type(OctetString):
    """Custom type scGenGroupSmonVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ScGenGroupSmonVlanList_Type.__name__ = "OctetString"
_ScGenGroupSmonVlanList_Object = MibTableColumn
scGenGroupSmonVlanList = _ScGenGroupSmonVlanList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 3),
    _ScGenGroupSmonVlanList_Type()
)
scGenGroupSmonVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonVlanList.setStatus("mandatory")
_ScGenGroupSmonDropEvents_Type = Counter32
_ScGenGroupSmonDropEvents_Object = MibTableColumn
scGenGroupSmonDropEvents = _ScGenGroupSmonDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 4),
    _ScGenGroupSmonDropEvents_Type()
)
scGenGroupSmonDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonDropEvents.setStatus("mandatory")
_ScGenGroupSmonGoodBroadcastPkts_Type = Counter32
_ScGenGroupSmonGoodBroadcastPkts_Object = MibTableColumn
scGenGroupSmonGoodBroadcastPkts = _ScGenGroupSmonGoodBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 5),
    _ScGenGroupSmonGoodBroadcastPkts_Type()
)
scGenGroupSmonGoodBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonGoodBroadcastPkts.setStatus("mandatory")
_ScGenGroupSmonGoodMulticastPkts_Type = Counter32
_ScGenGroupSmonGoodMulticastPkts_Object = MibTableColumn
scGenGroupSmonGoodMulticastPkts = _ScGenGroupSmonGoodMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 6),
    _ScGenGroupSmonGoodMulticastPkts_Type()
)
scGenGroupSmonGoodMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonGoodMulticastPkts.setStatus("mandatory")
_ScGenGroupSmonGoodPkts_Type = Counter32
_ScGenGroupSmonGoodPkts_Object = MibTableColumn
scGenGroupSmonGoodPkts = _ScGenGroupSmonGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 7),
    _ScGenGroupSmonGoodPkts_Type()
)
scGenGroupSmonGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonGoodPkts.setStatus("mandatory")
_ScGenGroupSmonBadPkts_Type = Counter32
_ScGenGroupSmonBadPkts_Object = MibTableColumn
scGenGroupSmonBadPkts = _ScGenGroupSmonBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 8),
    _ScGenGroupSmonBadPkts_Type()
)
scGenGroupSmonBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonBadPkts.setStatus("mandatory")
_ScGenGroupSmonGoodOctets_Type = Counter32
_ScGenGroupSmonGoodOctets_Object = MibTableColumn
scGenGroupSmonGoodOctets = _ScGenGroupSmonGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 9),
    _ScGenGroupSmonGoodOctets_Type()
)
scGenGroupSmonGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonGoodOctets.setStatus("mandatory")
_ScGenGroupSmonBadOctets_Type = Counter32
_ScGenGroupSmonBadOctets_Object = MibTableColumn
scGenGroupSmonBadOctets = _ScGenGroupSmonBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 10),
    _ScGenGroupSmonBadOctets_Type()
)
scGenGroupSmonBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonBadOctets.setStatus("mandatory")
_ScGenGroupSmonPkts_Type = Counter32
_ScGenGroupSmonPkts_Object = MibTableColumn
scGenGroupSmonPkts = _ScGenGroupSmonPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 11),
    _ScGenGroupSmonPkts_Type()
)
scGenGroupSmonPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonPkts.setStatus("mandatory")
_ScGenGroupSmonOctets_Type = Counter32
_ScGenGroupSmonOctets_Object = MibTableColumn
scGenGroupSmonOctets = _ScGenGroupSmonOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 12),
    _ScGenGroupSmonOctets_Type()
)
scGenGroupSmonOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupSmonOctets.setStatus("mandatory")


class _ScGenGroupSmonMIBCtrMode_Type(Integer32):
    """Custom type scGenGroupSmonMIBCtrMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenGroupSmonMIBCtrMode_Type.__name__ = "Integer32"
_ScGenGroupSmonMIBCtrMode_Object = MibTableColumn
scGenGroupSmonMIBCtrMode = _ScGenGroupSmonMIBCtrMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 2, 1, 13),
    _ScGenGroupSmonMIBCtrMode_Type()
)
scGenGroupSmonMIBCtrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupSmonMIBCtrMode.setStatus("mandatory")
_ScGenGroupVlanTable_Object = MibTable
scGenGroupVlanTable = _ScGenGroupVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3)
)
if mibBuilder.loadTexts:
    scGenGroupVlanTable.setStatus("mandatory")
_ScGenGroupVlanEntry_Object = MibTableRow
scGenGroupVlanEntry = _ScGenGroupVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1)
)
scGenGroupVlanEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenGroupVlanGroupId"),
    (0, "XSWITCH-MIB", "scGenGroupVlanId"),
)
if mibBuilder.loadTexts:
    scGenGroupVlanEntry.setStatus("mandatory")
_ScGenGroupVlanGroupId_Type = Integer32
_ScGenGroupVlanGroupId_Object = MibTableColumn
scGenGroupVlanGroupId = _ScGenGroupVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 1),
    _ScGenGroupVlanGroupId_Type()
)
scGenGroupVlanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanGroupId.setStatus("mandatory")
_ScGenGroupVlanId_Type = Integer32
_ScGenGroupVlanId_Object = MibTableColumn
scGenGroupVlanId = _ScGenGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 2),
    _ScGenGroupVlanId_Type()
)
scGenGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanId.setStatus("mandatory")
_ScGenGroupVlanUcastPkts_Type = Counter32
_ScGenGroupVlanUcastPkts_Object = MibTableColumn
scGenGroupVlanUcastPkts = _ScGenGroupVlanUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 3),
    _ScGenGroupVlanUcastPkts_Type()
)
scGenGroupVlanUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanUcastPkts.setStatus("mandatory")
_ScGenGroupVlanMcastPkts_Type = Counter32
_ScGenGroupVlanMcastPkts_Object = MibTableColumn
scGenGroupVlanMcastPkts = _ScGenGroupVlanMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 4),
    _ScGenGroupVlanMcastPkts_Type()
)
scGenGroupVlanMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanMcastPkts.setStatus("mandatory")
_ScGenGroupVlanBcastPkts_Type = Counter32
_ScGenGroupVlanBcastPkts_Object = MibTableColumn
scGenGroupVlanBcastPkts = _ScGenGroupVlanBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 5),
    _ScGenGroupVlanBcastPkts_Type()
)
scGenGroupVlanBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanBcastPkts.setStatus("mandatory")
_ScGenGroupVlanGoodPkts_Type = Counter32
_ScGenGroupVlanGoodPkts_Object = MibTableColumn
scGenGroupVlanGoodPkts = _ScGenGroupVlanGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 6),
    _ScGenGroupVlanGoodPkts_Type()
)
scGenGroupVlanGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanGoodPkts.setStatus("mandatory")
_ScGenGroupVlanGoodOctets_Type = Counter32
_ScGenGroupVlanGoodOctets_Object = MibTableColumn
scGenGroupVlanGoodOctets = _ScGenGroupVlanGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 7),
    _ScGenGroupVlanGoodOctets_Type()
)
scGenGroupVlanGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanGoodOctets.setStatus("mandatory")
_ScGenGroupVlanUcastOctets_Type = Counter32
_ScGenGroupVlanUcastOctets_Object = MibTableColumn
scGenGroupVlanUcastOctets = _ScGenGroupVlanUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 8),
    _ScGenGroupVlanUcastOctets_Type()
)
scGenGroupVlanUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanUcastOctets.setStatus("mandatory")
_ScGenGroupVlanMcastOctets_Type = Counter32
_ScGenGroupVlanMcastOctets_Object = MibTableColumn
scGenGroupVlanMcastOctets = _ScGenGroupVlanMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 9),
    _ScGenGroupVlanMcastOctets_Type()
)
scGenGroupVlanMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanMcastOctets.setStatus("mandatory")
_ScGenGroupVlanBcastOctets_Type = Counter32
_ScGenGroupVlanBcastOctets_Object = MibTableColumn
scGenGroupVlanBcastOctets = _ScGenGroupVlanBcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 10),
    _ScGenGroupVlanBcastOctets_Type()
)
scGenGroupVlanBcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanBcastOctets.setStatus("mandatory")
_ScGenGroupVlanCurrentEgressPorts_Type = OctetString
_ScGenGroupVlanCurrentEgressPorts_Object = MibTableColumn
scGenGroupVlanCurrentEgressPorts = _ScGenGroupVlanCurrentEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 11),
    _ScGenGroupVlanCurrentEgressPorts_Type()
)
scGenGroupVlanCurrentEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanCurrentEgressPorts.setStatus("mandatory")
_ScGenGroupVlanCurrentUntaggedPorts_Type = OctetString
_ScGenGroupVlanCurrentUntaggedPorts_Object = MibTableColumn
scGenGroupVlanCurrentUntaggedPorts = _ScGenGroupVlanCurrentUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 12),
    _ScGenGroupVlanCurrentUntaggedPorts_Type()
)
scGenGroupVlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupVlanCurrentUntaggedPorts.setStatus("mandatory")
_ScGenGroupVlanStaticEgressPorts_Type = OctetString
_ScGenGroupVlanStaticEgressPorts_Object = MibTableColumn
scGenGroupVlanStaticEgressPorts = _ScGenGroupVlanStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 13),
    _ScGenGroupVlanStaticEgressPorts_Type()
)
scGenGroupVlanStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupVlanStaticEgressPorts.setStatus("mandatory")
_ScGenGroupVlanStaticUntaggedPorts_Type = OctetString
_ScGenGroupVlanStaticUntaggedPorts_Object = MibTableColumn
scGenGroupVlanStaticUntaggedPorts = _ScGenGroupVlanStaticUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 3, 1, 14),
    _ScGenGroupVlanStaticUntaggedPorts_Type()
)
scGenGroupVlanStaticUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupVlanStaticUntaggedPorts.setStatus("mandatory")
_ScGenGroupRspTable_Object = MibTable
scGenGroupRspTable = _ScGenGroupRspTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4)
)
if mibBuilder.loadTexts:
    scGenGroupRspTable.setStatus("mandatory")
_ScGenGroupRspEntry_Object = MibTableRow
scGenGroupRspEntry = _ScGenGroupRspEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1)
)
scGenGroupRspEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenGroupRspGroupId"),
)
if mibBuilder.loadTexts:
    scGenGroupRspEntry.setStatus("mandatory")
_ScGenGroupRspGroupId_Type = Integer32
_ScGenGroupRspGroupId_Object = MibTableColumn
scGenGroupRspGroupId = _ScGenGroupRspGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 1),
    _ScGenGroupRspGroupId_Type()
)
scGenGroupRspGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenGroupRspGroupId.setStatus("mandatory")


class _ScGenGroupRspHelloInterval_Type(Integer32):
    """Custom type scGenGroupRspHelloInterval based on Integer32"""
    defaultValue = 1


_ScGenGroupRspHelloInterval_Object = MibTableColumn
scGenGroupRspHelloInterval = _ScGenGroupRspHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 2),
    _ScGenGroupRspHelloInterval_Type()
)
scGenGroupRspHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspHelloInterval.setStatus("mandatory")


class _ScGenGroupRspDevicePollingInterval_Type(Integer32):
    """Custom type scGenGroupRspDevicePollingInterval based on Integer32"""
    defaultValue = 1


_ScGenGroupRspDevicePollingInterval_Object = MibTableColumn
scGenGroupRspDevicePollingInterval = _ScGenGroupRspDevicePollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 3),
    _ScGenGroupRspDevicePollingInterval_Type()
)
scGenGroupRspDevicePollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspDevicePollingInterval.setStatus("mandatory")


class _ScGenGroupRspDeviceNotRespondingTimeout_Type(Integer32):
    """Custom type scGenGroupRspDeviceNotRespondingTimeout based on Integer32"""
    defaultValue = 5


_ScGenGroupRspDeviceNotRespondingTimeout_Object = MibTableColumn
scGenGroupRspDeviceNotRespondingTimeout = _ScGenGroupRspDeviceNotRespondingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 4),
    _ScGenGroupRspDeviceNotRespondingTimeout_Type()
)
scGenGroupRspDeviceNotRespondingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspDeviceNotRespondingTimeout.setStatus("mandatory")


class _ScGenGroupRspSwitchNotRespondingTimeout_Type(Integer32):
    """Custom type scGenGroupRspSwitchNotRespondingTimeout based on Integer32"""
    defaultValue = 5


_ScGenGroupRspSwitchNotRespondingTimeout_Object = MibTableColumn
scGenGroupRspSwitchNotRespondingTimeout = _ScGenGroupRspSwitchNotRespondingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 5),
    _ScGenGroupRspSwitchNotRespondingTimeout_Type()
)
scGenGroupRspSwitchNotRespondingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspSwitchNotRespondingTimeout.setStatus("mandatory")


class _ScGenGroupRspMoveToForwardingInterval_Type(Integer32):
    """Custom type scGenGroupRspMoveToForwardingInterval based on Integer32"""
    defaultValue = 5


_ScGenGroupRspMoveToForwardingInterval_Object = MibTableColumn
scGenGroupRspMoveToForwardingInterval = _ScGenGroupRspMoveToForwardingInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 6),
    _ScGenGroupRspMoveToForwardingInterval_Type()
)
scGenGroupRspMoveToForwardingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspMoveToForwardingInterval.setStatus("mandatory")


class _ScGenGroupRspBroadcastArpShortInterval_Type(Integer32):
    """Custom type scGenGroupRspBroadcastArpShortInterval based on Integer32"""
    defaultValue = 5


_ScGenGroupRspBroadcastArpShortInterval_Object = MibTableColumn
scGenGroupRspBroadcastArpShortInterval = _ScGenGroupRspBroadcastArpShortInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 7),
    _ScGenGroupRspBroadcastArpShortInterval_Type()
)
scGenGroupRspBroadcastArpShortInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspBroadcastArpShortInterval.setStatus("mandatory")


class _ScGenGroupRspBroadcastArpShortIntervalNumber_Type(Integer32):
    """Custom type scGenGroupRspBroadcastArpShortIntervalNumber based on Integer32"""
    defaultValue = 5


_ScGenGroupRspBroadcastArpShortIntervalNumber_Object = MibTableColumn
scGenGroupRspBroadcastArpShortIntervalNumber = _ScGenGroupRspBroadcastArpShortIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 8),
    _ScGenGroupRspBroadcastArpShortIntervalNumber_Type()
)
scGenGroupRspBroadcastArpShortIntervalNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspBroadcastArpShortIntervalNumber.setStatus("mandatory")


class _ScGenGroupRspBroadcastArpLongInterval_Type(Integer32):
    """Custom type scGenGroupRspBroadcastArpLongInterval based on Integer32"""
    defaultValue = 150


_ScGenGroupRspBroadcastArpLongInterval_Object = MibTableColumn
scGenGroupRspBroadcastArpLongInterval = _ScGenGroupRspBroadcastArpLongInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 9),
    _ScGenGroupRspBroadcastArpLongInterval_Type()
)
scGenGroupRspBroadcastArpLongInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspBroadcastArpLongInterval.setStatus("mandatory")
_ScGenGroupRspPeriodicPingsBoxIpAddress_Type = IpAddress
_ScGenGroupRspPeriodicPingsBoxIpAddress_Object = MibTableColumn
scGenGroupRspPeriodicPingsBoxIpAddress = _ScGenGroupRspPeriodicPingsBoxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 10),
    _ScGenGroupRspPeriodicPingsBoxIpAddress_Type()
)
scGenGroupRspPeriodicPingsBoxIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspPeriodicPingsBoxIpAddress.setStatus("mandatory")
_ScGenGroupRspPeriodicPingsDestinationIpAddress_Type = IpAddress
_ScGenGroupRspPeriodicPingsDestinationIpAddress_Object = MibTableColumn
scGenGroupRspPeriodicPingsDestinationIpAddress = _ScGenGroupRspPeriodicPingsDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 11),
    _ScGenGroupRspPeriodicPingsDestinationIpAddress_Type()
)
scGenGroupRspPeriodicPingsDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspPeriodicPingsDestinationIpAddress.setStatus("mandatory")


class _ScGenGroupRspMode_Type(Integer32):
    """Custom type scGenGroupRspMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("rsp-modue-mode-role-B", 2),
          ("rsp-module-mode-role-A", 1))
    )


_ScGenGroupRspMode_Type.__name__ = "Integer32"
_ScGenGroupRspMode_Object = MibTableColumn
scGenGroupRspMode = _ScGenGroupRspMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 3, 4, 1, 12),
    _ScGenGroupRspMode_Type()
)
scGenGroupRspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenGroupRspMode.setStatus("mandatory")
_ScGenPort_ObjectIdentity = ObjectIdentity
scGenPort = _ScGenPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4)
)
_ScGenPortTable_Object = MibTable
scGenPortTable = _ScGenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1)
)
if mibBuilder.loadTexts:
    scGenPortTable.setStatus("mandatory")
_ScGenPortEntry_Object = MibTableRow
scGenPortEntry = _ScGenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1)
)
scGenPortEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenPortGroupId"),
    (0, "XSWITCH-MIB", "scGenPortId"),
)
if mibBuilder.loadTexts:
    scGenPortEntry.setStatus("mandatory")
_ScGenPortGroupId_Type = Integer32
_ScGenPortGroupId_Object = MibTableColumn
scGenPortGroupId = _ScGenPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 1),
    _ScGenPortGroupId_Type()
)
scGenPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortGroupId.setStatus("mandatory")
_ScGenPortId_Type = Integer32
_ScGenPortId_Object = MibTableColumn
scGenPortId = _ScGenPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 2),
    _ScGenPortId_Type()
)
scGenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortId.setStatus("mandatory")


class _ScGenPortVLAN_Type(Integer32):
    """Custom type scGenPortVLAN based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ScGenPortVLAN_Type.__name__ = "Integer32"
_ScGenPortVLAN_Object = MibTableColumn
scGenPortVLAN = _ScGenPortVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 3),
    _ScGenPortVLAN_Type()
)
scGenPortVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortVLAN.setStatus("mandatory")


class _ScGenPortPriority_Type(Integer32):
    """Custom type scGenPortPriority based on Integer32"""
    defaultValue = 1

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("notSupported", 255),
          ("regular", 1),
          ("userPriority1", 3),
          ("userPriority2", 4),
          ("userPriority3", 5),
          ("userPriority4", 6),
          ("userPriority5", 7),
          ("userPriority6", 8),
          ("userPriority7", 9),
          ("userPriority8", 10))
    )


_ScGenPortPriority_Type.__name__ = "Integer32"
_ScGenPortPriority_Object = MibTableColumn
scGenPortPriority = _ScGenPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 4),
    _ScGenPortPriority_Type()
)
scGenPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortPriority.setStatus("mandatory")


class _ScGenPortSetDefaults_Type(Integer32):
    """Custom type scGenPortSetDefaults based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenPortSetDefaults_Type.__name__ = "Integer32"
_ScGenPortSetDefaults_Object = MibTableColumn
scGenPortSetDefaults = _ScGenPortSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 5),
    _ScGenPortSetDefaults_Type()
)
scGenPortSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortSetDefaults.setStatus("mandatory")


class _ScGenPortBackbone_Type(Integer32):
    """Custom type scGenPortBackbone based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenPortBackbone_Type.__name__ = "Integer32"
_ScGenPortBackbone_Object = MibTableColumn
scGenPortBackbone = _ScGenPortBackbone_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 6),
    _ScGenPortBackbone_Type()
)
scGenPortBackbone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortBackbone.setStatus("mandatory")


class _ScGenPortCopyMode_Type(Integer32):
    """Custom type scGenPortCopyMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenPortCopyMode_Type.__name__ = "Integer32"
_ScGenPortCopyMode_Object = MibTableColumn
scGenPortCopyMode = _ScGenPortCopyMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 7),
    _ScGenPortCopyMode_Type()
)
scGenPortCopyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortCopyMode.setStatus("mandatory")


class _ScGenPortCopyDestination_Type(Integer32):
    """Custom type scGenPortCopyDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8092),
    )


_ScGenPortCopyDestination_Type.__name__ = "Integer32"
_ScGenPortCopyDestination_Object = MibTableColumn
scGenPortCopyDestination = _ScGenPortCopyDestination_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 8),
    _ScGenPortCopyDestination_Type()
)
scGenPortCopyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortCopyDestination.setStatus("mandatory")


class _ScGenPortLinkAggregationNumber_Type(Integer32):
    """Custom type scGenPortLinkAggregationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ScGenPortLinkAggregationNumber_Type.__name__ = "Integer32"
_ScGenPortLinkAggregationNumber_Object = MibTableColumn
scGenPortLinkAggregationNumber = _ScGenPortLinkAggregationNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 9),
    _ScGenPortLinkAggregationNumber_Type()
)
scGenPortLinkAggregationNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortLinkAggregationNumber.setStatus("mandatory")


class _ScGenPortSendBridgedPackets_Type(Integer32):
    """Custom type scGenPortSendBridgedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenPortSendBridgedPackets_Type.__name__ = "Integer32"
_ScGenPortSendBridgedPackets_Object = MibTableColumn
scGenPortSendBridgedPackets = _ScGenPortSendBridgedPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 10),
    _ScGenPortSendBridgedPackets_Type()
)
scGenPortSendBridgedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortSendBridgedPackets.setStatus("mandatory")


class _ScGenPortVLANEgressStaticConfiguration_Type(OctetString):
    """Custom type scGenPortVLANEgressStaticConfiguration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ScGenPortVLANEgressStaticConfiguration_Type.__name__ = "OctetString"
_ScGenPortVLANEgressStaticConfiguration_Object = MibTableColumn
scGenPortVLANEgressStaticConfiguration = _ScGenPortVLANEgressStaticConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 11),
    _ScGenPortVLANEgressStaticConfiguration_Type()
)
scGenPortVLANEgressStaticConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortVLANEgressStaticConfiguration.setStatus("mandatory")


class _ScGenPortStaticVLANBinding_Type(Integer32):
    """Custom type scGenPortStaticVLANBinding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenPortStaticVLANBinding_Type.__name__ = "Integer32"
_ScGenPortStaticVLANBinding_Object = MibTableColumn
scGenPortStaticVLANBinding = _ScGenPortStaticVLANBinding_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 12),
    _ScGenPortStaticVLANBinding_Type()
)
scGenPortStaticVLANBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortStaticVLANBinding.setStatus("mandatory")


class _ScGenPortSecId_Type(Integer32):
    """Custom type scGenPortSecId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenPortSecId_Type.__name__ = "Integer32"
_ScGenPortSecId_Object = MibTableColumn
scGenPortSecId = _ScGenPortSecId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 13),
    _ScGenPortSecId_Type()
)
scGenPortSecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortSecId.setStatus("mandatory")


class _ScGenPortMaxLagsOnSec_Type(Integer32):
    """Custom type scGenPortMaxLagsOnSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ScGenPortMaxLagsOnSec_Type.__name__ = "Integer32"
_ScGenPortMaxLagsOnSec_Object = MibTableColumn
scGenPortMaxLagsOnSec = _ScGenPortMaxLagsOnSec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 14),
    _ScGenPortMaxLagsOnSec_Type()
)
scGenPortMaxLagsOnSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortMaxLagsOnSec.setStatus("mandatory")


class _ScGenPortGenericTrap_Type(Integer32):
    """Custom type scGenPortGenericTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ScGenPortGenericTrap_Type.__name__ = "Integer32"
_ScGenPortGenericTrap_Object = MibTableColumn
scGenPortGenericTrap = _ScGenPortGenericTrap_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 15),
    _ScGenPortGenericTrap_Type()
)
scGenPortGenericTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortGenericTrap.setStatus("mandatory")


class _ScGenPortLACPMode_Type(Integer32):
    """Custom type scGenPortLACPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ScGenPortLACPMode_Type.__name__ = "Integer32"
_ScGenPortLACPMode_Object = MibTableColumn
scGenPortLACPMode = _ScGenPortLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 16),
    _ScGenPortLACPMode_Type()
)
scGenPortLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortLACPMode.setStatus("mandatory")
_ScGenPortLastIntruderSourceAddr_Type = OctetString
_ScGenPortLastIntruderSourceAddr_Object = MibTableColumn
scGenPortLastIntruderSourceAddr = _ScGenPortLastIntruderSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 17),
    _ScGenPortLastIntruderSourceAddr_Type()
)
scGenPortLastIntruderSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortLastIntruderSourceAddr.setStatus("mandatory")


class _ScGenPortSecurityMode_Type(Integer32):
    """Custom type scGenPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("nonSecurityMode", 1),
          ("notSupported", 255),
          ("securityMode", 2))
    )


_ScGenPortSecurityMode_Type.__name__ = "Integer32"
_ScGenPortSecurityMode_Object = MibTableColumn
scGenPortSecurityMode = _ScGenPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 18),
    _ScGenPortSecurityMode_Type()
)
scGenPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortSecurityMode.setStatus("mandatory")


class _ScGenPortSTA_Type(Integer32):
    """Custom type scGenPortSTA based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenPortSTA_Type.__name__ = "Integer32"
_ScGenPortSTA_Object = MibTableColumn
scGenPortSTA = _ScGenPortSTA_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 19),
    _ScGenPortSTA_Type()
)
scGenPortSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortSTA.setStatus("mandatory")
_ScGenPortLagCapability_Type = OctetString
_ScGenPortLagCapability_Object = MibTableColumn
scGenPortLagCapability = _ScGenPortLagCapability_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 20),
    _ScGenPortLagCapability_Type()
)
scGenPortLagCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortLagCapability.setStatus("mandatory")
_ScGenPortCapability_Type = OctetString
_ScGenPortCapability_Object = MibTableColumn
scGenPortCapability = _ScGenPortCapability_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 21),
    _ScGenPortCapability_Type()
)
scGenPortCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortCapability.setStatus("mandatory")


class _ScGenPortSLDAdminStatus_Type(Integer32):
    """Custom type scGenPortSLDAdminStatus based on Integer32"""
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


_ScGenPortSLDAdminStatus_Type.__name__ = "Integer32"
_ScGenPortSLDAdminStatus_Object = MibTableColumn
scGenPortSLDAdminStatus = _ScGenPortSLDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 22),
    _ScGenPortSLDAdminStatus_Type()
)
scGenPortSLDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortSLDAdminStatus.setStatus("mandatory")


class _ScGenPortSLDStatus_Type(Integer32):
    """Custom type scGenPortSLDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noSelfLoop", 2),
          ("notSupported", 255),
          ("selfLoop", 1))
    )


_ScGenPortSLDStatus_Type.__name__ = "Integer32"
_ScGenPortSLDStatus_Object = MibTableColumn
scGenPortSLDStatus = _ScGenPortSLDStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 1, 1, 23),
    _ScGenPortSLDStatus_Type()
)
scGenPortSLDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortSLDStatus.setStatus("mandatory")
_ScGenPortRspTable_Object = MibTable
scGenPortRspTable = _ScGenPortRspTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 2)
)
if mibBuilder.loadTexts:
    scGenPortRspTable.setStatus("mandatory")
_ScGenPortRspEntry_Object = MibTableRow
scGenPortRspEntry = _ScGenPortRspEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 2, 1)
)
scGenPortRspEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenPortRspGroupId"),
    (0, "XSWITCH-MIB", "scGenPortRspId"),
)
if mibBuilder.loadTexts:
    scGenPortRspEntry.setStatus("mandatory")
_ScGenPortRspGroupId_Type = Integer32
_ScGenPortRspGroupId_Object = MibTableColumn
scGenPortRspGroupId = _ScGenPortRspGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 2, 1, 1),
    _ScGenPortRspGroupId_Type()
)
scGenPortRspGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortRspGroupId.setStatus("mandatory")
_ScGenPortRspId_Type = Integer32
_ScGenPortRspId_Object = MibTableColumn
scGenPortRspId = _ScGenPortRspId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 2, 1, 2),
    _ScGenPortRspId_Type()
)
scGenPortRspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortRspId.setStatus("mandatory")


class _ScGenPortRspMode_Type(Integer32):
    """Custom type scGenPortRspMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("device-mode", 4),
          ("notSupported", 255),
          ("regular", 1),
          ("rsp-mode-role-A", 2),
          ("rsp-mode-role-B", 3))
    )


_ScGenPortRspMode_Type.__name__ = "Integer32"
_ScGenPortRspMode_Object = MibTableColumn
scGenPortRspMode = _ScGenPortRspMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 4, 2, 1, 3),
    _ScGenPortRspMode_Type()
)
scGenPortRspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortRspMode.setStatus("mandatory")
_ScGenSwitch_ObjectIdentity = ObjectIdentity
scGenSwitch = _ScGenSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5)
)
_ScGenSwitchTable_Object = MibTable
scGenSwitchTable = _ScGenSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1)
)
if mibBuilder.loadTexts:
    scGenSwitchTable.setStatus("mandatory")
_ScGenSwitchEntry_Object = MibTableRow
scGenSwitchEntry = _ScGenSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1)
)
scGenSwitchEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenSwitchId"),
)
if mibBuilder.loadTexts:
    scGenSwitchEntry.setStatus("mandatory")


class _ScGenSwitchId_Type(Integer32):
    """Custom type scGenSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenSwitchId_Type.__name__ = "Integer32"
_ScGenSwitchId_Object = MibTableColumn
scGenSwitchId = _ScGenSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 1),
    _ScGenSwitchId_Type()
)
scGenSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchId.setStatus("mandatory")


class _ScGenSwitchCopyMode_Type(Integer32):
    """Custom type scGenSwitchCopyMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenSwitchCopyMode_Type.__name__ = "Integer32"
_ScGenSwitchCopyMode_Object = MibTableColumn
scGenSwitchCopyMode = _ScGenSwitchCopyMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 2),
    _ScGenSwitchCopyMode_Type()
)
scGenSwitchCopyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchCopyMode.setStatus("mandatory")
_ScGenSwitchCopySource_Type = Integer32
_ScGenSwitchCopySource_Object = MibTableColumn
scGenSwitchCopySource = _ScGenSwitchCopySource_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 3),
    _ScGenSwitchCopySource_Type()
)
scGenSwitchCopySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchCopySource.setStatus("mandatory")
_ScGenSwitchCopyDestination_Type = Integer32
_ScGenSwitchCopyDestination_Object = MibTableColumn
scGenSwitchCopyDestination = _ScGenSwitchCopyDestination_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 4),
    _ScGenSwitchCopyDestination_Type()
)
scGenSwitchCopyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchCopyDestination.setStatus("mandatory")


class _ScGenSwitchSetDefaults_Type(Integer32):
    """Custom type scGenSwitchSetDefaults based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenSwitchSetDefaults_Type.__name__ = "Integer32"
_ScGenSwitchSetDefaults_Object = MibTableColumn
scGenSwitchSetDefaults = _ScGenSwitchSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 5),
    _ScGenSwitchSetDefaults_Type()
)
scGenSwitchSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchSetDefaults.setStatus("mandatory")


class _ScGenSwitchVIDP_Type(Integer32):
    """Custom type scGenSwitchVIDP based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenSwitchVIDP_Type.__name__ = "Integer32"
_ScGenSwitchVIDP_Object = MibTableColumn
scGenSwitchVIDP = _ScGenSwitchVIDP_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 6),
    _ScGenSwitchVIDP_Type()
)
scGenSwitchVIDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchVIDP.setStatus("mandatory")


class _ScGenSwitchType_Type(Integer32):
    """Custom type scGenSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("notSupported", 255),
          ("token-ring", 2))
    )


_ScGenSwitchType_Type.__name__ = "Integer32"
_ScGenSwitchType_Object = MibTableColumn
scGenSwitchType = _ScGenSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 7),
    _ScGenSwitchType_Type()
)
scGenSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchType.setStatus("mandatory")


class _ScGenSwitchMasterId_Type(Integer32):
    """Custom type scGenSwitchMasterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenSwitchMasterId_Type.__name__ = "Integer32"
_ScGenSwitchMasterId_Object = MibTableColumn
scGenSwitchMasterId = _ScGenSwitchMasterId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 8),
    _ScGenSwitchMasterId_Type()
)
scGenSwitchMasterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchMasterId.setStatus("mandatory")


class _ScGenSwitchReset_Type(Integer32):
    """Custom type scGenSwitchReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenSwitchReset_Type.__name__ = "Integer32"
_ScGenSwitchReset_Object = MibTableColumn
scGenSwitchReset = _ScGenSwitchReset_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 9),
    _ScGenSwitchReset_Type()
)
scGenSwitchReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchReset.setStatus("mandatory")


class _ScGenSwitchNumberOfLoads_Type(Integer32):
    """Custom type scGenSwitchNumberOfLoads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ScGenSwitchNumberOfLoads_Type.__name__ = "Integer32"
_ScGenSwitchNumberOfLoads_Object = MibTableColumn
scGenSwitchNumberOfLoads = _ScGenSwitchNumberOfLoads_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 10),
    _ScGenSwitchNumberOfLoads_Type()
)
scGenSwitchNumberOfLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchNumberOfLoads.setStatus("mandatory")


class _ScGenSwitchAgVLAN_Type(Integer32):
    """Custom type scGenSwitchAgVLAN based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ScGenSwitchAgVLAN_Type.__name__ = "Integer32"
_ScGenSwitchAgVLAN_Object = MibTableColumn
scGenSwitchAgVLAN = _ScGenSwitchAgVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 11),
    _ScGenSwitchAgVLAN_Type()
)
scGenSwitchAgVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchAgVLAN.setStatus("mandatory")


class _ScGenSwitchVLANList_Type(OctetString):
    """Custom type scGenSwitchVLANList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ScGenSwitchVLANList_Type.__name__ = "OctetString"
_ScGenSwitchVLANList_Object = MibTableColumn
scGenSwitchVLANList = _ScGenSwitchVLANList_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 12),
    _ScGenSwitchVLANList_Type()
)
scGenSwitchVLANList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchVLANList.setStatus("mandatory")


class _ScGenSwitchSTA_Type(Integer32):
    """Custom type scGenSwitchSTA based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenSwitchSTA_Type.__name__ = "Integer32"
_ScGenSwitchSTA_Object = MibTableColumn
scGenSwitchSTA = _ScGenSwitchSTA_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 13),
    _ScGenSwitchSTA_Type()
)
scGenSwitchSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchSTA.setStatus("mandatory")


class _ScGenSwitchSecurityMode_Type(Integer32):
    """Custom type scGenSwitchSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("nonSecurityMode", 1),
          ("notSupported", 255),
          ("securityMode", 2))
    )


_ScGenSwitchSecurityMode_Type.__name__ = "Integer32"
_ScGenSwitchSecurityMode_Object = MibTableColumn
scGenSwitchSecurityMode = _ScGenSwitchSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 14),
    _ScGenSwitchSecurityMode_Type()
)
scGenSwitchSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchSecurityMode.setStatus("mandatory")
_ScGenSwitchFindQuery_Type = OctetString
_ScGenSwitchFindQuery_Object = MibTableColumn
scGenSwitchFindQuery = _ScGenSwitchFindQuery_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 15),
    _ScGenSwitchFindQuery_Type()
)
scGenSwitchFindQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchFindQuery.setStatus("mandatory")
_ScGenSwitchFindResult_Type = OctetString
_ScGenSwitchFindResult_Object = MibTableColumn
scGenSwitchFindResult = _ScGenSwitchFindResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 16),
    _ScGenSwitchFindResult_Type()
)
scGenSwitchFindResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchFindResult.setStatus("mandatory")
_ScGenSwitchSWRdChange_Type = OctetString
_ScGenSwitchSWRdChange_Object = MibTableColumn
scGenSwitchSWRdChange = _ScGenSwitchSWRdChange_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 17),
    _ScGenSwitchSWRdChange_Type()
)
scGenSwitchSWRdChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchSWRdChange.setStatus("mandatory")


class _ScGenSwitchDefaultVLAN_Type(Integer32):
    """Custom type scGenSwitchDefaultVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("vlan0", 1),
          ("vlan1", 2))
    )


_ScGenSwitchDefaultVLAN_Type.__name__ = "Integer32"
_ScGenSwitchDefaultVLAN_Object = MibTableColumn
scGenSwitchDefaultVLAN = _ScGenSwitchDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 18),
    _ScGenSwitchDefaultVLAN_Type()
)
scGenSwitchDefaultVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchDefaultVLAN.setStatus("mandatory")


class _ScGenSwitchVLANBridging_Type(Integer32):
    """Custom type scGenSwitchVLANBridging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenSwitchVLANBridging_Type.__name__ = "Integer32"
_ScGenSwitchVLANBridging_Object = MibTableColumn
scGenSwitchVLANBridging = _ScGenSwitchVLANBridging_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 19),
    _ScGenSwitchVLANBridging_Type()
)
scGenSwitchVLANBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchVLANBridging.setStatus("mandatory")


class _ScGenSwitchOldVersionModules_Type(DisplayString):
    """Custom type scGenSwitchOldVersionModules based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScGenSwitchOldVersionModules_Type.__name__ = "DisplayString"
_ScGenSwitchOldVersionModules_Object = MibTableColumn
scGenSwitchOldVersionModules = _ScGenSwitchOldVersionModules_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 20),
    _ScGenSwitchOldVersionModules_Type()
)
scGenSwitchOldVersionModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchOldVersionModules.setStatus("mandatory")


class _ScGenSwitchVIDPNonSupportedModules_Type(DisplayString):
    """Custom type scGenSwitchVIDPNonSupportedModules based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScGenSwitchVIDPNonSupportedModules_Type.__name__ = "DisplayString"
_ScGenSwitchVIDPNonSupportedModules_Object = MibTableColumn
scGenSwitchVIDPNonSupportedModules = _ScGenSwitchVIDPNonSupportedModules_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 21),
    _ScGenSwitchVIDPNonSupportedModules_Type()
)
scGenSwitchVIDPNonSupportedModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchVIDPNonSupportedModules.setStatus("mandatory")


class _ScGenSwitchSTANonSupportedModules_Type(DisplayString):
    """Custom type scGenSwitchSTANonSupportedModules based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScGenSwitchSTANonSupportedModules_Type.__name__ = "DisplayString"
_ScGenSwitchSTANonSupportedModules_Object = MibTableColumn
scGenSwitchSTANonSupportedModules = _ScGenSwitchSTANonSupportedModules_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 22),
    _ScGenSwitchSTANonSupportedModules_Type()
)
scGenSwitchSTANonSupportedModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchSTANonSupportedModules.setStatus("mandatory")


class _ScGenSwitchIDSNonSupportedModules_Type(DisplayString):
    """Custom type scGenSwitchIDSNonSupportedModules based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScGenSwitchIDSNonSupportedModules_Type.__name__ = "DisplayString"
_ScGenSwitchIDSNonSupportedModules_Object = MibTableColumn
scGenSwitchIDSNonSupportedModules = _ScGenSwitchIDSNonSupportedModules_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 23),
    _ScGenSwitchIDSNonSupportedModules_Type()
)
scGenSwitchIDSNonSupportedModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenSwitchIDSNonSupportedModules.setStatus("mandatory")


class _ScGenSwitchMcFilter_Type(Integer32):
    """Custom type scGenSwitchMcFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScGenSwitchMcFilter_Type.__name__ = "Integer32"
_ScGenSwitchMcFilter_Object = MibTableColumn
scGenSwitchMcFilter = _ScGenSwitchMcFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 24),
    _ScGenSwitchMcFilter_Type()
)
scGenSwitchMcFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchMcFilter.setStatus("mandatory")


class _ScGenSwitchMcFilterHostAgingTime_Type(Integer32):
    """Custom type scGenSwitchMcFilterHostAgingTime based on Integer32"""
    defaultValue = 600


_ScGenSwitchMcFilterHostAgingTime_Object = MibTableColumn
scGenSwitchMcFilterHostAgingTime = _ScGenSwitchMcFilterHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 25),
    _ScGenSwitchMcFilterHostAgingTime_Type()
)
scGenSwitchMcFilterHostAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchMcFilterHostAgingTime.setStatus("mandatory")


class _ScGenSwitchMcFilterRouterAgingTime_Type(Integer32):
    """Custom type scGenSwitchMcFilterRouterAgingTime based on Integer32"""
    defaultValue = 1800


_ScGenSwitchMcFilterRouterAgingTime_Object = MibTableColumn
scGenSwitchMcFilterRouterAgingTime = _ScGenSwitchMcFilterRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 26),
    _ScGenSwitchMcFilterRouterAgingTime_Type()
)
scGenSwitchMcFilterRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchMcFilterRouterAgingTime.setStatus("mandatory")


class _ScGenSwitchMcFilterDelayTime_Type(Integer32):
    """Custom type scGenSwitchMcFilterDelayTime based on Integer32"""
    defaultValue = 10


_ScGenSwitchMcFilterDelayTime_Object = MibTableColumn
scGenSwitchMcFilterDelayTime = _ScGenSwitchMcFilterDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 27),
    _ScGenSwitchMcFilterDelayTime_Type()
)
scGenSwitchMcFilterDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchMcFilterDelayTime.setStatus("mandatory")


class _ScGenSwitchLACPMode_Type(Integer32):
    """Custom type scGenSwitchLACPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ScGenSwitchLACPMode_Type.__name__ = "Integer32"
_ScGenSwitchLACPMode_Object = MibTableColumn
scGenSwitchLACPMode = _ScGenSwitchLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 28),
    _ScGenSwitchLACPMode_Type()
)
scGenSwitchLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchLACPMode.setStatus("mandatory")
_ScGenSwitchSecurityModePermit_Type = Integer32
_ScGenSwitchSecurityModePermit_Object = MibTableColumn
scGenSwitchSecurityModePermit = _ScGenSwitchSecurityModePermit_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 29),
    _ScGenSwitchSecurityModePermit_Type()
)
scGenSwitchSecurityModePermit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchSecurityModePermit.setStatus("mandatory")


class _ScGenSwitchFastAgingOnRemoteTopChg_Type(Integer32):
    """Custom type scGenSwitchFastAgingOnRemoteTopChg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 255))
    )


_ScGenSwitchFastAgingOnRemoteTopChg_Type.__name__ = "Integer32"
_ScGenSwitchFastAgingOnRemoteTopChg_Object = MibTableColumn
scGenSwitchFastAgingOnRemoteTopChg = _ScGenSwitchFastAgingOnRemoteTopChg_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 30),
    _ScGenSwitchFastAgingOnRemoteTopChg_Type()
)
scGenSwitchFastAgingOnRemoteTopChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchFastAgingOnRemoteTopChg.setStatus("mandatory")


class _ScGenSwitchGigaMode_Type(Integer32):
    """Custom type scGenSwitchGigaMode based on Integer32"""
    defaultValue = 1

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
        *(("link-load-sharing", 2),
          ("primary-bottom", 3),
          ("primary-top", 4),
          ("regular", 1))
    )


_ScGenSwitchGigaMode_Type.__name__ = "Integer32"
_ScGenSwitchGigaMode_Object = MibTableColumn
scGenSwitchGigaMode = _ScGenSwitchGigaMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 31),
    _ScGenSwitchGigaMode_Type()
)
scGenSwitchGigaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchGigaMode.setStatus("mandatory")


class _ScGenSwitchCAMClear_Type(Integer32):
    """Custom type scGenSwitchCAMClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ScGenSwitchCAMClear_Type.__name__ = "Integer32"
_ScGenSwitchCAMClear_Object = MibTableColumn
scGenSwitchCAMClear = _ScGenSwitchCAMClear_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 5, 1, 1, 32),
    _ScGenSwitchCAMClear_Type()
)
scGenSwitchCAMClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenSwitchCAMClear.setStatus("mandatory")
_ScGenLinkAggregation_ObjectIdentity = ObjectIdentity
scGenLinkAggregation = _ScGenLinkAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6)
)
_ScGenLinkAggregationTable_Object = MibTable
scGenLinkAggregationTable = _ScGenLinkAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1)
)
if mibBuilder.loadTexts:
    scGenLinkAggregationTable.setStatus("mandatory")
_ScGenLinkAggregationEntry_Object = MibTableRow
scGenLinkAggregationEntry = _ScGenLinkAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1)
)
scGenLinkAggregationEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenLinkAggregationId"),
)
if mibBuilder.loadTexts:
    scGenLinkAggregationEntry.setStatus("mandatory")


class _ScGenLinkAggregationId_Type(Integer32):
    """Custom type scGenLinkAggregationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ScGenLinkAggregationId_Type.__name__ = "Integer32"
_ScGenLinkAggregationId_Object = MibTableColumn
scGenLinkAggregationId = _ScGenLinkAggregationId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 1),
    _ScGenLinkAggregationId_Type()
)
scGenLinkAggregationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenLinkAggregationId.setStatus("mandatory")


class _ScGenLinkAggregationName_Type(DisplayString):
    """Custom type scGenLinkAggregationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ScGenLinkAggregationName_Type.__name__ = "DisplayString"
_ScGenLinkAggregationName_Object = MibTableColumn
scGenLinkAggregationName = _ScGenLinkAggregationName_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 2),
    _ScGenLinkAggregationName_Type()
)
scGenLinkAggregationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenLinkAggregationName.setStatus("mandatory")
_ScGenLinkAggregationBasePortGroupId_Type = Integer32
_ScGenLinkAggregationBasePortGroupId_Object = MibTableColumn
scGenLinkAggregationBasePortGroupId = _ScGenLinkAggregationBasePortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 3),
    _ScGenLinkAggregationBasePortGroupId_Type()
)
scGenLinkAggregationBasePortGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenLinkAggregationBasePortGroupId.setStatus("mandatory")
_ScGenLinkAggregationBasePortId_Type = Integer32
_ScGenLinkAggregationBasePortId_Object = MibTableColumn
scGenLinkAggregationBasePortId = _ScGenLinkAggregationBasePortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 4),
    _ScGenLinkAggregationBasePortId_Type()
)
scGenLinkAggregationBasePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenLinkAggregationBasePortId.setStatus("mandatory")
_ScGenLinkAggregationNumberOfPorts_Type = Integer32
_ScGenLinkAggregationNumberOfPorts_Object = MibTableColumn
scGenLinkAggregationNumberOfPorts = _ScGenLinkAggregationNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 5),
    _ScGenLinkAggregationNumberOfPorts_Type()
)
scGenLinkAggregationNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenLinkAggregationNumberOfPorts.setStatus("mandatory")
_ScGenLinkAggregationLogicalPortGroupId_Type = Integer32
_ScGenLinkAggregationLogicalPortGroupId_Object = MibTableColumn
scGenLinkAggregationLogicalPortGroupId = _ScGenLinkAggregationLogicalPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 6),
    _ScGenLinkAggregationLogicalPortGroupId_Type()
)
scGenLinkAggregationLogicalPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenLinkAggregationLogicalPortGroupId.setStatus("mandatory")
_ScGenLinkAggregationLogicalPortId_Type = Integer32
_ScGenLinkAggregationLogicalPortId_Object = MibTableColumn
scGenLinkAggregationLogicalPortId = _ScGenLinkAggregationLogicalPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 7),
    _ScGenLinkAggregationLogicalPortId_Type()
)
scGenLinkAggregationLogicalPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenLinkAggregationLogicalPortId.setStatus("mandatory")


class _ScGenLinkAggregationFunctionalStatus_Type(Integer32):
    """Custom type scGenLinkAggregationFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notSupported", 255),
          ("ok", 1),
          ("partialFail", 3))
    )


_ScGenLinkAggregationFunctionalStatus_Type.__name__ = "Integer32"
_ScGenLinkAggregationFunctionalStatus_Object = MibTableColumn
scGenLinkAggregationFunctionalStatus = _ScGenLinkAggregationFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 8),
    _ScGenLinkAggregationFunctionalStatus_Type()
)
scGenLinkAggregationFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenLinkAggregationFunctionalStatus.setStatus("mandatory")


class _ScGenLinkAggregationAutoNegResults_Type(Integer32):
    """Custom type scGenLinkAggregationAutoNegResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoNegInconsistantResults", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_ScGenLinkAggregationAutoNegResults_Type.__name__ = "Integer32"
_ScGenLinkAggregationAutoNegResults_Object = MibTableColumn
scGenLinkAggregationAutoNegResults = _ScGenLinkAggregationAutoNegResults_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 9),
    _ScGenLinkAggregationAutoNegResults_Type()
)
scGenLinkAggregationAutoNegResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenLinkAggregationAutoNegResults.setStatus("mandatory")
_ScGenLinkAggregationFaultMask_Type = OctetString
_ScGenLinkAggregationFaultMask_Object = MibTableColumn
scGenLinkAggregationFaultMask = _ScGenLinkAggregationFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 10),
    _ScGenLinkAggregationFaultMask_Type()
)
scGenLinkAggregationFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenLinkAggregationFaultMask.setStatus("mandatory")
_ScGenLinkAggregationStatus_Type = RowStatus
_ScGenLinkAggregationStatus_Object = MibTableColumn
scGenLinkAggregationStatus = _ScGenLinkAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 6, 1, 1, 11),
    _ScGenLinkAggregationStatus_Type()
)
scGenLinkAggregationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenLinkAggregationStatus.setStatus("mandatory")
_ScGenPortIPAddressRsp_ObjectIdentity = ObjectIdentity
scGenPortIPAddressRsp = _ScGenPortIPAddressRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 7)
)
_ScGenPortIPAddressRspTable_Object = MibTable
scGenPortIPAddressRspTable = _ScGenPortIPAddressRspTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 7, 1)
)
if mibBuilder.loadTexts:
    scGenPortIPAddressRspTable.setStatus("mandatory")
_ScGenPortIPAddressRspEntry_Object = MibTableRow
scGenPortIPAddressRspEntry = _ScGenPortIPAddressRspEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 7, 1, 1)
)
scGenPortIPAddressRspEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scGenPortIPAddressRspGroupId"),
    (0, "XSWITCH-MIB", "scGenPortIPAddressRspPortId"),
    (0, "XSWITCH-MIB", "scGenPortIPAddressRspIpAddressIndex"),
)
if mibBuilder.loadTexts:
    scGenPortIPAddressRspEntry.setStatus("mandatory")
_ScGenPortIPAddressRspGroupId_Type = Integer32
_ScGenPortIPAddressRspGroupId_Object = MibTableColumn
scGenPortIPAddressRspGroupId = _ScGenPortIPAddressRspGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 7, 1, 1, 1),
    _ScGenPortIPAddressRspGroupId_Type()
)
scGenPortIPAddressRspGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortIPAddressRspGroupId.setStatus("mandatory")
_ScGenPortIPAddressRspPortId_Type = Integer32
_ScGenPortIPAddressRspPortId_Object = MibTableColumn
scGenPortIPAddressRspPortId = _ScGenPortIPAddressRspPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 7, 1, 1, 2),
    _ScGenPortIPAddressRspPortId_Type()
)
scGenPortIPAddressRspPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortIPAddressRspPortId.setStatus("mandatory")
_ScGenPortIPAddressRspIpAddressIndex_Type = Integer32
_ScGenPortIPAddressRspIpAddressIndex_Object = MibTableColumn
scGenPortIPAddressRspIpAddressIndex = _ScGenPortIPAddressRspIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 7, 1, 1, 3),
    _ScGenPortIPAddressRspIpAddressIndex_Type()
)
scGenPortIPAddressRspIpAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scGenPortIPAddressRspIpAddressIndex.setStatus("mandatory")
_ScGenPortIPAddressRspIpAddress_Type = IpAddress
_ScGenPortIPAddressRspIpAddress_Object = MibTableColumn
scGenPortIPAddressRspIpAddress = _ScGenPortIPAddressRspIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 1, 7, 1, 1, 4),
    _ScGenPortIPAddressRspIpAddress_Type()
)
scGenPortIPAddressRspIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scGenPortIPAddressRspIpAddress.setStatus("mandatory")
_ScEth_ObjectIdentity = ObjectIdentity
scEth = _ScEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 2)
)
_ScEthPort_ObjectIdentity = ObjectIdentity
scEthPort = _ScEthPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1)
)
_ScEthPortTable_Object = MibTable
scEthPortTable = _ScEthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1)
)
if mibBuilder.loadTexts:
    scEthPortTable.setStatus("mandatory")
_ScEthPortEntry_Object = MibTableRow
scEthPortEntry = _ScEthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1)
)
scEthPortEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scEthPortGroupId"),
    (0, "XSWITCH-MIB", "scEthPortId"),
)
if mibBuilder.loadTexts:
    scEthPortEntry.setStatus("mandatory")
_ScEthPortGroupId_Type = Integer32
_ScEthPortGroupId_Object = MibTableColumn
scEthPortGroupId = _ScEthPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 1),
    _ScEthPortGroupId_Type()
)
scEthPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGroupId.setStatus("mandatory")
_ScEthPortId_Type = Integer32
_ScEthPortId_Object = MibTableColumn
scEthPortId = _ScEthPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 2),
    _ScEthPortId_Type()
)
scEthPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortId.setStatus("mandatory")
_ScEthPortOctetsRec_Type = Counter32
_ScEthPortOctetsRec_Object = MibTableColumn
scEthPortOctetsRec = _ScEthPortOctetsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 3),
    _ScEthPortOctetsRec_Type()
)
scEthPortOctetsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortOctetsRec.setStatus("mandatory")
_ScEthPortPktsRec_Type = Counter32
_ScEthPortPktsRec_Object = MibTableColumn
scEthPortPktsRec = _ScEthPortPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 4),
    _ScEthPortPktsRec_Type()
)
scEthPortPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortPktsRec.setStatus("mandatory")
_ScEthPortGoodBroadcastPktsRec_Type = Counter32
_ScEthPortGoodBroadcastPktsRec_Object = MibTableColumn
scEthPortGoodBroadcastPktsRec = _ScEthPortGoodBroadcastPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 5),
    _ScEthPortGoodBroadcastPktsRec_Type()
)
scEthPortGoodBroadcastPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodBroadcastPktsRec.setStatus("mandatory")
_ScEthPortGoodMulticastPktsRec_Type = Counter32
_ScEthPortGoodMulticastPktsRec_Object = MibTableColumn
scEthPortGoodMulticastPktsRec = _ScEthPortGoodMulticastPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 6),
    _ScEthPortGoodMulticastPktsRec_Type()
)
scEthPortGoodMulticastPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodMulticastPktsRec.setStatus("mandatory")
_ScEthPortCRCAlignErrors_Type = Counter32
_ScEthPortCRCAlignErrors_Object = MibTableColumn
scEthPortCRCAlignErrors = _ScEthPortCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 7),
    _ScEthPortCRCAlignErrors_Type()
)
scEthPortCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortCRCAlignErrors.setStatus("mandatory")
_ScEthPortOversizePkts_Type = Counter32
_ScEthPortOversizePkts_Object = MibTableColumn
scEthPortOversizePkts = _ScEthPortOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 8),
    _ScEthPortOversizePkts_Type()
)
scEthPortOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortOversizePkts.setStatus("mandatory")
_ScEthPortFragments_Type = Counter32
_ScEthPortFragments_Object = MibTableColumn
scEthPortFragments = _ScEthPortFragments_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 9),
    _ScEthPortFragments_Type()
)
scEthPortFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortFragments.setStatus("mandatory")
_ScEthPortJabber_Type = Counter32
_ScEthPortJabber_Object = MibTableColumn
scEthPortJabber = _ScEthPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 10),
    _ScEthPortJabber_Type()
)
scEthPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortJabber.setStatus("mandatory")
_ScEthPortCollisions_Type = Counter32
_ScEthPortCollisions_Object = MibTableColumn
scEthPortCollisions = _ScEthPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 11),
    _ScEthPortCollisions_Type()
)
scEthPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortCollisions.setStatus("mandatory")
_ScEthPortPkts64Octets_Type = Counter32
_ScEthPortPkts64Octets_Object = MibTableColumn
scEthPortPkts64Octets = _ScEthPortPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 12),
    _ScEthPortPkts64Octets_Type()
)
scEthPortPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortPkts64Octets.setStatus("mandatory")
_ScEthPortPkts65to127Octets_Type = Counter32
_ScEthPortPkts65to127Octets_Object = MibTableColumn
scEthPortPkts65to127Octets = _ScEthPortPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 13),
    _ScEthPortPkts65to127Octets_Type()
)
scEthPortPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortPkts65to127Octets.setStatus("mandatory")
_ScEthPortPkts128to255Octets_Type = Counter32
_ScEthPortPkts128to255Octets_Object = MibTableColumn
scEthPortPkts128to255Octets = _ScEthPortPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 14),
    _ScEthPortPkts128to255Octets_Type()
)
scEthPortPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortPkts128to255Octets.setStatus("mandatory")
_ScEthPortPkts256to511Octets_Type = Counter32
_ScEthPortPkts256to511Octets_Object = MibTableColumn
scEthPortPkts256to511Octets = _ScEthPortPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 15),
    _ScEthPortPkts256to511Octets_Type()
)
scEthPortPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortPkts256to511Octets.setStatus("mandatory")
_ScEthPortPkts512to1023Octets_Type = Counter32
_ScEthPortPkts512to1023Octets_Object = MibTableColumn
scEthPortPkts512to1023Octets = _ScEthPortPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 16),
    _ScEthPortPkts512to1023Octets_Type()
)
scEthPortPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortPkts512to1023Octets.setStatus("mandatory")
_ScEthPortPkts1024to1518Octets_Type = Counter32
_ScEthPortPkts1024to1518Octets_Object = MibTableColumn
scEthPortPkts1024to1518Octets = _ScEthPortPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 17),
    _ScEthPortPkts1024to1518Octets_Type()
)
scEthPortPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortPkts1024to1518Octets.setStatus("mandatory")
_ScEthPortGoodPktsRec_Type = Counter32
_ScEthPortGoodPktsRec_Object = MibTableColumn
scEthPortGoodPktsRec = _ScEthPortGoodPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 18),
    _ScEthPortGoodPktsRec_Type()
)
scEthPortGoodPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodPktsRec.setStatus("mandatory")
_ScEthPortBadPkts_Type = Counter32
_ScEthPortBadPkts_Object = MibTableColumn
scEthPortBadPkts = _ScEthPortBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 19),
    _ScEthPortBadPkts_Type()
)
scEthPortBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortBadPkts.setStatus("mandatory")
_ScEthPortGoodOctetsRec_Type = Counter32
_ScEthPortGoodOctetsRec_Object = MibTableColumn
scEthPortGoodOctetsRec = _ScEthPortGoodOctetsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 20),
    _ScEthPortGoodOctetsRec_Type()
)
scEthPortGoodOctetsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodOctetsRec.setStatus("mandatory")
_ScEthPortBadOctets_Type = Counter32
_ScEthPortBadOctets_Object = MibTableColumn
scEthPortBadOctets = _ScEthPortBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 21),
    _ScEthPortBadOctets_Type()
)
scEthPortBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortBadOctets.setStatus("mandatory")
_ScEthPortGoodBroadcastOctetsRec_Type = Counter32
_ScEthPortGoodBroadcastOctetsRec_Object = MibTableColumn
scEthPortGoodBroadcastOctetsRec = _ScEthPortGoodBroadcastOctetsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 22),
    _ScEthPortGoodBroadcastOctetsRec_Type()
)
scEthPortGoodBroadcastOctetsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodBroadcastOctetsRec.setStatus("mandatory")
_ScEthPortGoodMulticastOctetsRec_Type = Counter32
_ScEthPortGoodMulticastOctetsRec_Object = MibTableColumn
scEthPortGoodMulticastOctetsRec = _ScEthPortGoodMulticastOctetsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 23),
    _ScEthPortGoodMulticastOctetsRec_Type()
)
scEthPortGoodMulticastOctetsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodMulticastOctetsRec.setStatus("mandatory")
_ScEthPortGoodOctetsSent_Type = Counter32
_ScEthPortGoodOctetsSent_Object = MibTableColumn
scEthPortGoodOctetsSent = _ScEthPortGoodOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 24),
    _ScEthPortGoodOctetsSent_Type()
)
scEthPortGoodOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodOctetsSent.setStatus("mandatory")
_ScEthPortGoodPktsSent_Type = Counter32
_ScEthPortGoodPktsSent_Object = MibTableColumn
scEthPortGoodPktsSent = _ScEthPortGoodPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 25),
    _ScEthPortGoodPktsSent_Type()
)
scEthPortGoodPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodPktsSent.setStatus("mandatory")
_ScEthPortLateCollisions_Type = Counter32
_ScEthPortLateCollisions_Object = MibTableColumn
scEthPortLateCollisions = _ScEthPortLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 26),
    _ScEthPortLateCollisions_Type()
)
scEthPortLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortLateCollisions.setStatus("mandatory")


class _ScEthPortFunctionalStatus_Type(Integer32):
    """Custom type scEthPortFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("ok", 1),
          ("partition", 8),
          ("remoteFault", 10),
          ("rld", 2),
          ("rspError", 11),
          ("rxJabber", 3))
    )


_ScEthPortFunctionalStatus_Type.__name__ = "Integer32"
_ScEthPortFunctionalStatus_Object = MibTableColumn
scEthPortFunctionalStatus = _ScEthPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 27),
    _ScEthPortFunctionalStatus_Type()
)
scEthPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortFunctionalStatus.setStatus("mandatory")


class _ScEthPortMode_Type(Integer32):
    """Custom type scEthPortMode based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplexAsymRxPause", 8),
          ("fullDuplexAsymTxPause", 6),
          ("fullDuplexFlowControlISL", 5),
          ("fullDuplexISL", 4),
          ("fullDuplexNoPause", 2),
          ("fullDuplexProprietaryFC", 3),
          ("fullDuplexSymPause", 7),
          ("halfDuplex", 1),
          ("notSupported", 255))
    )


_ScEthPortMode_Type.__name__ = "Integer32"
_ScEthPortMode_Object = MibTableColumn
scEthPortMode = _ScEthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 28),
    _ScEthPortMode_Type()
)
scEthPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEthPortMode.setStatus("mandatory")


class _ScEthPortSpeed_Type(Integer32):
    """Custom type scEthPortSpeed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("a155Mbps", 4),
          ("a622Mbps", 5),
          ("ethernet", 1),
          ("fastEthernet", 2),
          ("gigabitEthernet", 3),
          ("notSupported", 255))
    )


_ScEthPortSpeed_Type.__name__ = "Integer32"
_ScEthPortSpeed_Object = MibTableColumn
scEthPortSpeed = _ScEthPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 29),
    _ScEthPortSpeed_Type()
)
scEthPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEthPortSpeed.setStatus("mandatory")


class _ScEthPortAutoNegotiation_Type(Integer32):
    """Custom type scEthPortAutoNegotiation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScEthPortAutoNegotiation_Type.__name__ = "Integer32"
_ScEthPortAutoNegotiation_Object = MibTableColumn
scEthPortAutoNegotiation = _ScEthPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 30),
    _ScEthPortAutoNegotiation_Type()
)
scEthPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEthPortAutoNegotiation.setStatus("mandatory")


class _ScEthPortAutoNegotiationStatus_Type(Integer32):
    """Custom type scEthPortAutoNegotiationStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("fail", 2),
          ("inProgress", 4),
          ("notSupported", 255),
          ("pass", 1))
    )


_ScEthPortAutoNegotiationStatus_Type.__name__ = "Integer32"
_ScEthPortAutoNegotiationStatus_Object = MibTableColumn
scEthPortAutoNegotiationStatus = _ScEthPortAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 31),
    _ScEthPortAutoNegotiationStatus_Type()
)
scEthPortAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortAutoNegotiationStatus.setStatus("mandatory")
_ScEthPortTotalOctets_Type = Counter32
_ScEthPortTotalOctets_Object = MibTableColumn
scEthPortTotalOctets = _ScEthPortTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 32),
    _ScEthPortTotalOctets_Type()
)
scEthPortTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortTotalOctets.setStatus("mandatory")
_ScEthPortTotalPkts_Type = Counter32
_ScEthPortTotalPkts_Object = MibTableColumn
scEthPortTotalPkts = _ScEthPortTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 33),
    _ScEthPortTotalPkts_Type()
)
scEthPortTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortTotalPkts.setStatus("mandatory")
_ScEthPortDropEvents_Type = Counter32
_ScEthPortDropEvents_Object = MibTableColumn
scEthPortDropEvents = _ScEthPortDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 34),
    _ScEthPortDropEvents_Type()
)
scEthPortDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortDropEvents.setStatus("mandatory")


class _ScEthPortGigaPauseStatus_Type(Integer32):
    """Custom type scEthPortGigaPauseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("asymmetricPauseRx", 3),
          ("noPause", 1),
          ("notSupported", 255),
          ("symmetricPause", 2))
    )


_ScEthPortGigaPauseStatus_Type.__name__ = "Integer32"
_ScEthPortGigaPauseStatus_Object = MibTableColumn
scEthPortGigaPauseStatus = _ScEthPortGigaPauseStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 35),
    _ScEthPortGigaPauseStatus_Type()
)
scEthPortGigaPauseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGigaPauseStatus.setStatus("mandatory")
_ScEthPortLower32OctetsRec_Type = Counter32
_ScEthPortLower32OctetsRec_Object = MibTableColumn
scEthPortLower32OctetsRec = _ScEthPortLower32OctetsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 36),
    _ScEthPortLower32OctetsRec_Type()
)
scEthPortLower32OctetsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortLower32OctetsRec.setStatus("mandatory")
_ScEthPortUpper32OctetsRec_Type = Counter32
_ScEthPortUpper32OctetsRec_Object = MibTableColumn
scEthPortUpper32OctetsRec = _ScEthPortUpper32OctetsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 37),
    _ScEthPortUpper32OctetsRec_Type()
)
scEthPortUpper32OctetsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortUpper32OctetsRec.setStatus("mandatory")
_ScEthPortLower32OctetsSent_Type = Counter32
_ScEthPortLower32OctetsSent_Object = MibTableColumn
scEthPortLower32OctetsSent = _ScEthPortLower32OctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 38),
    _ScEthPortLower32OctetsSent_Type()
)
scEthPortLower32OctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortLower32OctetsSent.setStatus("mandatory")
_ScEthPortUpper32OctetsSent_Type = Counter32
_ScEthPortUpper32OctetsSent_Object = MibTableColumn
scEthPortUpper32OctetsSent = _ScEthPortUpper32OctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 39),
    _ScEthPortUpper32OctetsSent_Type()
)
scEthPortUpper32OctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortUpper32OctetsSent.setStatus("mandatory")
_ScEthPortGoodUnicastPktsRec_Type = Counter32
_ScEthPortGoodUnicastPktsRec_Object = MibTableColumn
scEthPortGoodUnicastPktsRec = _ScEthPortGoodUnicastPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 40),
    _ScEthPortGoodUnicastPktsRec_Type()
)
scEthPortGoodUnicastPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortGoodUnicastPktsRec.setStatus("mandatory")
_ScEthPortDiscardPktsRec_Type = Counter32
_ScEthPortDiscardPktsRec_Object = MibTableColumn
scEthPortDiscardPktsRec = _ScEthPortDiscardPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 41),
    _ScEthPortDiscardPktsRec_Type()
)
scEthPortDiscardPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortDiscardPktsRec.setStatus("mandatory")
_ScEthPortUnicastPktsSent_Type = Counter32
_ScEthPortUnicastPktsSent_Object = MibTableColumn
scEthPortUnicastPktsSent = _ScEthPortUnicastPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 42),
    _ScEthPortUnicastPktsSent_Type()
)
scEthPortUnicastPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortUnicastPktsSent.setStatus("mandatory")
_ScEthPortDiscardPktsSent_Type = Counter32
_ScEthPortDiscardPktsSent_Object = MibTableColumn
scEthPortDiscardPktsSent = _ScEthPortDiscardPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 43),
    _ScEthPortDiscardPktsSent_Type()
)
scEthPortDiscardPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortDiscardPktsSent.setStatus("mandatory")


class _ScEthPortPauseCapabilities_Type(Integer32):
    """Custom type scEthPortPauseCapabilities based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("asymTxFlowControlOnly", 2),
          ("noFlowControl", 1),
          ("notSupported", 255),
          ("symAndAsymRxFlowControl", 4),
          ("symFlowControlOnly", 3))
    )


_ScEthPortPauseCapabilities_Type.__name__ = "Integer32"
_ScEthPortPauseCapabilities_Object = MibTableColumn
scEthPortPauseCapabilities = _ScEthPortPauseCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 44),
    _ScEthPortPauseCapabilities_Type()
)
scEthPortPauseCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEthPortPauseCapabilities.setStatus("mandatory")
_ScEthPortMulticastPktsSent_Type = Counter32
_ScEthPortMulticastPktsSent_Object = MibTableColumn
scEthPortMulticastPktsSent = _ScEthPortMulticastPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 45),
    _ScEthPortMulticastPktsSent_Type()
)
scEthPortMulticastPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortMulticastPktsSent.setStatus("mandatory")
_ScEthPortUndersizePktsRec_Type = Counter32
_ScEthPortUndersizePktsRec_Object = MibTableColumn
scEthPortUndersizePktsRec = _ScEthPortUndersizePktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 46),
    _ScEthPortUndersizePktsRec_Type()
)
scEthPortUndersizePktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthPortUndersizePktsRec.setStatus("mandatory")


class _ScEthPortFlowControl_Type(Integer32):
    """Custom type scEthPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("asymRxFlowControl", 4),
          ("asymTxFlowControl", 2),
          ("noFlowControl", 1),
          ("notSupported", 255),
          ("proprietaryFlowControl", 5),
          ("symFlowControl", 3))
    )


_ScEthPortFlowControl_Type.__name__ = "Integer32"
_ScEthPortFlowControl_Object = MibTableColumn
scEthPortFlowControl = _ScEthPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 1, 1, 1, 47),
    _ScEthPortFlowControl_Type()
)
scEthPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEthPortFlowControl.setStatus("mandatory")
_ScEthGroup_ObjectIdentity = ObjectIdentity
scEthGroup = _ScEthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 2)
)
_ScEthGroupTable_Object = MibTable
scEthGroupTable = _ScEthGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 2, 1)
)
if mibBuilder.loadTexts:
    scEthGroupTable.setStatus("mandatory")
_ScEthGroupEntry_Object = MibTableRow
scEthGroupEntry = _ScEthGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 2, 1, 1)
)
scEthGroupEntry.setIndexNames(
    (0, "XSWITCH-MIB", "scEthGroupId"),
)
if mibBuilder.loadTexts:
    scEthGroupEntry.setStatus("mandatory")
_ScEthGroupId_Type = Integer32
_ScEthGroupId_Object = MibTableColumn
scEthGroupId = _ScEthGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 2, 1, 1, 1),
    _ScEthGroupId_Type()
)
scEthGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEthGroupId.setStatus("mandatory")


class _ScEthGroupAutoPartitionEnable_Type(Integer32):
    """Custom type scEthGroupAutoPartitionEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScEthGroupAutoPartitionEnable_Type.__name__ = "Integer32"
_ScEthGroupAutoPartitionEnable_Object = MibTableColumn
scEthGroupAutoPartitionEnable = _ScEthGroupAutoPartitionEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 2, 1, 1, 2),
    _ScEthGroupAutoPartitionEnable_Type()
)
scEthGroupAutoPartitionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEthGroupAutoPartitionEnable.setStatus("mandatory")


class _ScEthGroupFefiEnable_Type(Integer32):
    """Custom type scEthGroupFefiEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_ScEthGroupFefiEnable_Type.__name__ = "Integer32"
_ScEthGroupFefiEnable_Object = MibTableColumn
scEthGroupFefiEnable = _ScEthGroupFefiEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 28, 2, 2, 1, 1, 3),
    _ScEthGroupFefiEnable_Type()
)
scEthGroupFefiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEthGroupFefiEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XSWITCH-MIB",
    **{"RowStatus": RowStatus,
       "switchChip": switchChip,
       "scGen": scGen,
       "scGenChassis": scGenChassis,
       "scGenChMainAgPosition": scGenChMainAgPosition,
       "scGenChRedunAgPosition": scGenChRedunAgPosition,
       "scGenChRedunAgActivityStatus": scGenChRedunAgActivityStatus,
       "scGenChAgVLAN": scGenChAgVLAN,
       "scGenMon": scGenMon,
       "scGenMonTable": scGenMonTable,
       "scGenMonEntry": scGenMonEntry,
       "scGenMonSwitchId": scGenMonSwitchId,
       "scGenMonDropEvents": scGenMonDropEvents,
       "scGenMonOctets": scGenMonOctets,
       "scGenMonPkts": scGenMonPkts,
       "scGenMonGoodBroadcastPkts": scGenMonGoodBroadcastPkts,
       "scGenMonGoodMulticastPkts": scGenMonGoodMulticastPkts,
       "scGenMonGoodPkts": scGenMonGoodPkts,
       "scGenMonBadPkts": scGenMonBadPkts,
       "scGenMonGoodOctets": scGenMonGoodOctets,
       "scGenMonBadOctets": scGenMonBadOctets,
       "scGenMonSmonCapability": scGenMonSmonCapability,
       "scGenMonMIBCtrMode": scGenMonMIBCtrMode,
       "scGenMonSwitchVLANList": scGenMonSwitchVLANList,
       "scGenMonMIBCtrList": scGenMonMIBCtrList,
       "scGenMonTimeStamp": scGenMonTimeStamp,
       "scGenMonVlanTimeStamp": scGenMonVlanTimeStamp,
       "scGenMonPriorityTable": scGenMonPriorityTable,
       "scGenMonPriorityEntry": scGenMonPriorityEntry,
       "scGenMonPrioritySwitchId": scGenMonPrioritySwitchId,
       "scGenMonPriorityId": scGenMonPriorityId,
       "scGenMonPriorityGoodPkts": scGenMonPriorityGoodPkts,
       "scGenMonPriorityGoodOctets": scGenMonPriorityGoodOctets,
       "scGenMonVLANList": scGenMonVLANList,
       "scGenMonVLANTable": scGenMonVLANTable,
       "scGenMonVLANEntry": scGenMonVLANEntry,
       "scGenMonVLANSwitchId": scGenMonVLANSwitchId,
       "scGenMonVLANId": scGenMonVLANId,
       "scGenMonVLANGoodPkts": scGenMonVLANGoodPkts,
       "scGenMonVLANGoodOctets": scGenMonVLANGoodOctets,
       "scGenMonVLANStatsUcastPkts": scGenMonVLANStatsUcastPkts,
       "scGenMonVLANStatsMcastPkts": scGenMonVLANStatsMcastPkts,
       "scGenMonVLANStatsBcastPkts": scGenMonVLANStatsBcastPkts,
       "scGenMonSwitches": scGenMonSwitches,
       "scHostTimePortCorrTable": scHostTimePortCorrTable,
       "scHostTimePortCorrEntry": scHostTimePortCorrEntry,
       "scHostTimeAddress": scHostTimeAddress,
       "scHostTimeCreationOrder": scHostTimeCreationOrder,
       "scHostTimeIndex": scHostTimeIndex,
       "scHostTimePortConnection": scHostTimePortConnection,
       "scGenGroup": scGenGroup,
       "scGenGroupTable": scGenGroupTable,
       "scGenGroupEntry": scGenGroupEntry,
       "scGenGroupId": scGenGroupId,
       "scGenGroupUseSwitches": scGenGroupUseSwitches,
       "scGenGroupCopyPortSupport": scGenGroupCopyPortSupport,
       "scGenGroupXswitchConnection": scGenGroupXswitchConnection,
       "scGenGroupStatus": scGenGroupStatus,
       "scGenGroupSwitchType": scGenGroupSwitchType,
       "scGenGroupNumberOfLoads": scGenGroupNumberOfLoads,
       "scGenGroupSetDefaults": scGenGroupSetDefaults,
       "scGenGroupSupportCopyPortList": scGenGroupSupportCopyPortList,
       "scGenGroupSupportPortCountersList": scGenGroupSupportPortCountersList,
       "scGenGroupSupportSegCountersList": scGenGroupSupportSegCountersList,
       "scGenGroupUpLinkType": scGenGroupUpLinkType,
       "scGenGroupPlugInType": scGenGroupPlugInType,
       "scGenGroupPlugInDescr": scGenGroupPlugInDescr,
       "scGenGroupPlugInCS": scGenGroupPlugInCS,
       "scGenGroupDefaultVLAN": scGenGroupDefaultVLAN,
       "scGenGroupCascadingType": scGenGroupCascadingType,
       "scGenGroupCascadingDescr": scGenGroupCascadingDescr,
       "scGenGroupCascadingCS": scGenGroupCascadingCS,
       "scGenGroupSupportDstCopyPortList": scGenGroupSupportDstCopyPortList,
       "scGenGroupBUPSType": scGenGroupBUPSType,
       "scGenGroupBUPSCS": scGenGroupBUPSCS,
       "scGenGroupBUPSFansStatus": scGenGroupBUPSFansStatus,
       "scGenGroupFansStatus": scGenGroupFansStatus,
       "scGenGroupInternalBuffering": scGenGroupInternalBuffering,
       "scGenGroupMcFilterBoxSupport": scGenGroupMcFilterBoxSupport,
       "scGenGroupMcFilterPersonalitySupport": scGenGroupMcFilterPersonalitySupport,
       "scGenGroupMcFilterStackingSupport": scGenGroupMcFilterStackingSupport,
       "scGenGroupLACPMode": scGenGroupLACPMode,
       "scGenGroupSecurityMode": scGenGroupSecurityMode,
       "scGenGroupBroadcastStormControl": scGenGroupBroadcastStormControl,
       "scGenGroupBroadcastThreshold": scGenGroupBroadcastThreshold,
       "scGenGroupPriorityQueuesScheduling": scGenGroupPriorityQueuesScheduling,
       "scGenGroupBoundedDelay": scGenGroupBoundedDelay,
       "scGenGroupSLDAdminStatus": scGenGroupSLDAdminStatus,
       "scGenGroupSmonTable": scGenGroupSmonTable,
       "scGenGroupSmonEntry": scGenGroupSmonEntry,
       "scGenGroupSmonGroupId": scGenGroupSmonGroupId,
       "scGenGroupSmonCapability": scGenGroupSmonCapability,
       "scGenGroupSmonVlanList": scGenGroupSmonVlanList,
       "scGenGroupSmonDropEvents": scGenGroupSmonDropEvents,
       "scGenGroupSmonGoodBroadcastPkts": scGenGroupSmonGoodBroadcastPkts,
       "scGenGroupSmonGoodMulticastPkts": scGenGroupSmonGoodMulticastPkts,
       "scGenGroupSmonGoodPkts": scGenGroupSmonGoodPkts,
       "scGenGroupSmonBadPkts": scGenGroupSmonBadPkts,
       "scGenGroupSmonGoodOctets": scGenGroupSmonGoodOctets,
       "scGenGroupSmonBadOctets": scGenGroupSmonBadOctets,
       "scGenGroupSmonPkts": scGenGroupSmonPkts,
       "scGenGroupSmonOctets": scGenGroupSmonOctets,
       "scGenGroupSmonMIBCtrMode": scGenGroupSmonMIBCtrMode,
       "scGenGroupVlanTable": scGenGroupVlanTable,
       "scGenGroupVlanEntry": scGenGroupVlanEntry,
       "scGenGroupVlanGroupId": scGenGroupVlanGroupId,
       "scGenGroupVlanId": scGenGroupVlanId,
       "scGenGroupVlanUcastPkts": scGenGroupVlanUcastPkts,
       "scGenGroupVlanMcastPkts": scGenGroupVlanMcastPkts,
       "scGenGroupVlanBcastPkts": scGenGroupVlanBcastPkts,
       "scGenGroupVlanGoodPkts": scGenGroupVlanGoodPkts,
       "scGenGroupVlanGoodOctets": scGenGroupVlanGoodOctets,
       "scGenGroupVlanUcastOctets": scGenGroupVlanUcastOctets,
       "scGenGroupVlanMcastOctets": scGenGroupVlanMcastOctets,
       "scGenGroupVlanBcastOctets": scGenGroupVlanBcastOctets,
       "scGenGroupVlanCurrentEgressPorts": scGenGroupVlanCurrentEgressPorts,
       "scGenGroupVlanCurrentUntaggedPorts": scGenGroupVlanCurrentUntaggedPorts,
       "scGenGroupVlanStaticEgressPorts": scGenGroupVlanStaticEgressPorts,
       "scGenGroupVlanStaticUntaggedPorts": scGenGroupVlanStaticUntaggedPorts,
       "scGenGroupRspTable": scGenGroupRspTable,
       "scGenGroupRspEntry": scGenGroupRspEntry,
       "scGenGroupRspGroupId": scGenGroupRspGroupId,
       "scGenGroupRspHelloInterval": scGenGroupRspHelloInterval,
       "scGenGroupRspDevicePollingInterval": scGenGroupRspDevicePollingInterval,
       "scGenGroupRspDeviceNotRespondingTimeout": scGenGroupRspDeviceNotRespondingTimeout,
       "scGenGroupRspSwitchNotRespondingTimeout": scGenGroupRspSwitchNotRespondingTimeout,
       "scGenGroupRspMoveToForwardingInterval": scGenGroupRspMoveToForwardingInterval,
       "scGenGroupRspBroadcastArpShortInterval": scGenGroupRspBroadcastArpShortInterval,
       "scGenGroupRspBroadcastArpShortIntervalNumber": scGenGroupRspBroadcastArpShortIntervalNumber,
       "scGenGroupRspBroadcastArpLongInterval": scGenGroupRspBroadcastArpLongInterval,
       "scGenGroupRspPeriodicPingsBoxIpAddress": scGenGroupRspPeriodicPingsBoxIpAddress,
       "scGenGroupRspPeriodicPingsDestinationIpAddress": scGenGroupRspPeriodicPingsDestinationIpAddress,
       "scGenGroupRspMode": scGenGroupRspMode,
       "scGenPort": scGenPort,
       "scGenPortTable": scGenPortTable,
       "scGenPortEntry": scGenPortEntry,
       "scGenPortGroupId": scGenPortGroupId,
       "scGenPortId": scGenPortId,
       "scGenPortVLAN": scGenPortVLAN,
       "scGenPortPriority": scGenPortPriority,
       "scGenPortSetDefaults": scGenPortSetDefaults,
       "scGenPortBackbone": scGenPortBackbone,
       "scGenPortCopyMode": scGenPortCopyMode,
       "scGenPortCopyDestination": scGenPortCopyDestination,
       "scGenPortLinkAggregationNumber": scGenPortLinkAggregationNumber,
       "scGenPortSendBridgedPackets": scGenPortSendBridgedPackets,
       "scGenPortVLANEgressStaticConfiguration": scGenPortVLANEgressStaticConfiguration,
       "scGenPortStaticVLANBinding": scGenPortStaticVLANBinding,
       "scGenPortSecId": scGenPortSecId,
       "scGenPortMaxLagsOnSec": scGenPortMaxLagsOnSec,
       "scGenPortGenericTrap": scGenPortGenericTrap,
       "scGenPortLACPMode": scGenPortLACPMode,
       "scGenPortLastIntruderSourceAddr": scGenPortLastIntruderSourceAddr,
       "scGenPortSecurityMode": scGenPortSecurityMode,
       "scGenPortSTA": scGenPortSTA,
       "scGenPortLagCapability": scGenPortLagCapability,
       "scGenPortCapability": scGenPortCapability,
       "scGenPortSLDAdminStatus": scGenPortSLDAdminStatus,
       "scGenPortSLDStatus": scGenPortSLDStatus,
       "scGenPortRspTable": scGenPortRspTable,
       "scGenPortRspEntry": scGenPortRspEntry,
       "scGenPortRspGroupId": scGenPortRspGroupId,
       "scGenPortRspId": scGenPortRspId,
       "scGenPortRspMode": scGenPortRspMode,
       "scGenSwitch": scGenSwitch,
       "scGenSwitchTable": scGenSwitchTable,
       "scGenSwitchEntry": scGenSwitchEntry,
       "scGenSwitchId": scGenSwitchId,
       "scGenSwitchCopyMode": scGenSwitchCopyMode,
       "scGenSwitchCopySource": scGenSwitchCopySource,
       "scGenSwitchCopyDestination": scGenSwitchCopyDestination,
       "scGenSwitchSetDefaults": scGenSwitchSetDefaults,
       "scGenSwitchVIDP": scGenSwitchVIDP,
       "scGenSwitchType": scGenSwitchType,
       "scGenSwitchMasterId": scGenSwitchMasterId,
       "scGenSwitchReset": scGenSwitchReset,
       "scGenSwitchNumberOfLoads": scGenSwitchNumberOfLoads,
       "scGenSwitchAgVLAN": scGenSwitchAgVLAN,
       "scGenSwitchVLANList": scGenSwitchVLANList,
       "scGenSwitchSTA": scGenSwitchSTA,
       "scGenSwitchSecurityMode": scGenSwitchSecurityMode,
       "scGenSwitchFindQuery": scGenSwitchFindQuery,
       "scGenSwitchFindResult": scGenSwitchFindResult,
       "scGenSwitchSWRdChange": scGenSwitchSWRdChange,
       "scGenSwitchDefaultVLAN": scGenSwitchDefaultVLAN,
       "scGenSwitchVLANBridging": scGenSwitchVLANBridging,
       "scGenSwitchOldVersionModules": scGenSwitchOldVersionModules,
       "scGenSwitchVIDPNonSupportedModules": scGenSwitchVIDPNonSupportedModules,
       "scGenSwitchSTANonSupportedModules": scGenSwitchSTANonSupportedModules,
       "scGenSwitchIDSNonSupportedModules": scGenSwitchIDSNonSupportedModules,
       "scGenSwitchMcFilter": scGenSwitchMcFilter,
       "scGenSwitchMcFilterHostAgingTime": scGenSwitchMcFilterHostAgingTime,
       "scGenSwitchMcFilterRouterAgingTime": scGenSwitchMcFilterRouterAgingTime,
       "scGenSwitchMcFilterDelayTime": scGenSwitchMcFilterDelayTime,
       "scGenSwitchLACPMode": scGenSwitchLACPMode,
       "scGenSwitchSecurityModePermit": scGenSwitchSecurityModePermit,
       "scGenSwitchFastAgingOnRemoteTopChg": scGenSwitchFastAgingOnRemoteTopChg,
       "scGenSwitchGigaMode": scGenSwitchGigaMode,
       "scGenSwitchCAMClear": scGenSwitchCAMClear,
       "scGenLinkAggregation": scGenLinkAggregation,
       "scGenLinkAggregationTable": scGenLinkAggregationTable,
       "scGenLinkAggregationEntry": scGenLinkAggregationEntry,
       "scGenLinkAggregationId": scGenLinkAggregationId,
       "scGenLinkAggregationName": scGenLinkAggregationName,
       "scGenLinkAggregationBasePortGroupId": scGenLinkAggregationBasePortGroupId,
       "scGenLinkAggregationBasePortId": scGenLinkAggregationBasePortId,
       "scGenLinkAggregationNumberOfPorts": scGenLinkAggregationNumberOfPorts,
       "scGenLinkAggregationLogicalPortGroupId": scGenLinkAggregationLogicalPortGroupId,
       "scGenLinkAggregationLogicalPortId": scGenLinkAggregationLogicalPortId,
       "scGenLinkAggregationFunctionalStatus": scGenLinkAggregationFunctionalStatus,
       "scGenLinkAggregationAutoNegResults": scGenLinkAggregationAutoNegResults,
       "scGenLinkAggregationFaultMask": scGenLinkAggregationFaultMask,
       "scGenLinkAggregationStatus": scGenLinkAggregationStatus,
       "scGenPortIPAddressRsp": scGenPortIPAddressRsp,
       "scGenPortIPAddressRspTable": scGenPortIPAddressRspTable,
       "scGenPortIPAddressRspEntry": scGenPortIPAddressRspEntry,
       "scGenPortIPAddressRspGroupId": scGenPortIPAddressRspGroupId,
       "scGenPortIPAddressRspPortId": scGenPortIPAddressRspPortId,
       "scGenPortIPAddressRspIpAddressIndex": scGenPortIPAddressRspIpAddressIndex,
       "scGenPortIPAddressRspIpAddress": scGenPortIPAddressRspIpAddress,
       "scEth": scEth,
       "scEthPort": scEthPort,
       "scEthPortTable": scEthPortTable,
       "scEthPortEntry": scEthPortEntry,
       "scEthPortGroupId": scEthPortGroupId,
       "scEthPortId": scEthPortId,
       "scEthPortOctetsRec": scEthPortOctetsRec,
       "scEthPortPktsRec": scEthPortPktsRec,
       "scEthPortGoodBroadcastPktsRec": scEthPortGoodBroadcastPktsRec,
       "scEthPortGoodMulticastPktsRec": scEthPortGoodMulticastPktsRec,
       "scEthPortCRCAlignErrors": scEthPortCRCAlignErrors,
       "scEthPortOversizePkts": scEthPortOversizePkts,
       "scEthPortFragments": scEthPortFragments,
       "scEthPortJabber": scEthPortJabber,
       "scEthPortCollisions": scEthPortCollisions,
       "scEthPortPkts64Octets": scEthPortPkts64Octets,
       "scEthPortPkts65to127Octets": scEthPortPkts65to127Octets,
       "scEthPortPkts128to255Octets": scEthPortPkts128to255Octets,
       "scEthPortPkts256to511Octets": scEthPortPkts256to511Octets,
       "scEthPortPkts512to1023Octets": scEthPortPkts512to1023Octets,
       "scEthPortPkts1024to1518Octets": scEthPortPkts1024to1518Octets,
       "scEthPortGoodPktsRec": scEthPortGoodPktsRec,
       "scEthPortBadPkts": scEthPortBadPkts,
       "scEthPortGoodOctetsRec": scEthPortGoodOctetsRec,
       "scEthPortBadOctets": scEthPortBadOctets,
       "scEthPortGoodBroadcastOctetsRec": scEthPortGoodBroadcastOctetsRec,
       "scEthPortGoodMulticastOctetsRec": scEthPortGoodMulticastOctetsRec,
       "scEthPortGoodOctetsSent": scEthPortGoodOctetsSent,
       "scEthPortGoodPktsSent": scEthPortGoodPktsSent,
       "scEthPortLateCollisions": scEthPortLateCollisions,
       "scEthPortFunctionalStatus": scEthPortFunctionalStatus,
       "scEthPortMode": scEthPortMode,
       "scEthPortSpeed": scEthPortSpeed,
       "scEthPortAutoNegotiation": scEthPortAutoNegotiation,
       "scEthPortAutoNegotiationStatus": scEthPortAutoNegotiationStatus,
       "scEthPortTotalOctets": scEthPortTotalOctets,
       "scEthPortTotalPkts": scEthPortTotalPkts,
       "scEthPortDropEvents": scEthPortDropEvents,
       "scEthPortGigaPauseStatus": scEthPortGigaPauseStatus,
       "scEthPortLower32OctetsRec": scEthPortLower32OctetsRec,
       "scEthPortUpper32OctetsRec": scEthPortUpper32OctetsRec,
       "scEthPortLower32OctetsSent": scEthPortLower32OctetsSent,
       "scEthPortUpper32OctetsSent": scEthPortUpper32OctetsSent,
       "scEthPortGoodUnicastPktsRec": scEthPortGoodUnicastPktsRec,
       "scEthPortDiscardPktsRec": scEthPortDiscardPktsRec,
       "scEthPortUnicastPktsSent": scEthPortUnicastPktsSent,
       "scEthPortDiscardPktsSent": scEthPortDiscardPktsSent,
       "scEthPortPauseCapabilities": scEthPortPauseCapabilities,
       "scEthPortMulticastPktsSent": scEthPortMulticastPktsSent,
       "scEthPortUndersizePktsRec": scEthPortUndersizePktsRec,
       "scEthPortFlowControl": scEthPortFlowControl,
       "scEthGroup": scEthGroup,
       "scEthGroupTable": scEthGroupTable,
       "scEthGroupEntry": scEthGroupEntry,
       "scEthGroupId": scEthGroupId,
       "scEthGroupAutoPartitionEnable": scEthGroupAutoPartitionEnable,
       "scEthGroupFefiEnable": scEthGroupFefiEnable}
)
