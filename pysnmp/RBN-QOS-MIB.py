# SNMP MIB module (RBN-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:02 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(rbnSubsActiveName,
 rbnSubsActiveSessionId) = mibBuilder.importSymbols(
    "RBN-SUBSCRIBER-ACTIVE-MIB",
    "rbnSubsActiveName",
    "rbnSubsActiveSessionId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22)
)
rbnQosMib.setRevisions(
        ("2007-07-30 00:00",
         "2006-09-12 00:00",
         "2005-09-26 00:00",
         "2003-07-18 00:00",
         "2002-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnQosPolicyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atmwfq", 6),
          ("edrr", 3),
          ("mdrr", 4),
          ("metering", 2),
          ("policing", 1),
          ("pq", 5),
          ("pwfq", 7))
    )



class RbnQosClassId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_RbnQosMibObjects_ObjectIdentity = ObjectIdentity
rbnQosMibObjects = _RbnQosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1)
)
_RbnQosInterfaceTable_Object = MibTable
rbnQosInterfaceTable = _RbnQosInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1)
)
if mibBuilder.loadTexts:
    rbnQosInterfaceTable.setStatus("current")
_RbnQosInterfaceEntry_Object = MibTableRow
rbnQosInterfaceEntry = _RbnQosInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1)
)
rbnQosInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rbnQosInterfaceEntry.setStatus("current")
_RbnQosIfInOctets_Type = Counter32
_RbnQosIfInOctets_Object = MibTableColumn
rbnQosIfInOctets = _RbnQosIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 1),
    _RbnQosIfInOctets_Type()
)
rbnQosIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfInOctets.setStatus("current")
_RbnQosIfHCInOctets_Type = Counter64
_RbnQosIfHCInOctets_Object = MibTableColumn
rbnQosIfHCInOctets = _RbnQosIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 2),
    _RbnQosIfHCInOctets_Type()
)
rbnQosIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfHCInOctets.setStatus("current")
_RbnQosIfOutOctets_Type = Counter32
_RbnQosIfOutOctets_Object = MibTableColumn
rbnQosIfOutOctets = _RbnQosIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 3),
    _RbnQosIfOutOctets_Type()
)
rbnQosIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfOutOctets.setStatus("current")
_RbnQosIfHCOutOctets_Type = Counter64
_RbnQosIfHCOutOctets_Object = MibTableColumn
rbnQosIfHCOutOctets = _RbnQosIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 4),
    _RbnQosIfHCOutOctets_Type()
)
rbnQosIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfHCOutOctets.setStatus("current")
_RbnQosIfInDroppedOctets_Type = Counter32
_RbnQosIfInDroppedOctets_Object = MibTableColumn
rbnQosIfInDroppedOctets = _RbnQosIfInDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 5),
    _RbnQosIfInDroppedOctets_Type()
)
rbnQosIfInDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfInDroppedOctets.setStatus("current")
_RbnQosIfHCInDroppedOctets_Type = Counter64
_RbnQosIfHCInDroppedOctets_Object = MibTableColumn
rbnQosIfHCInDroppedOctets = _RbnQosIfHCInDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 6),
    _RbnQosIfHCInDroppedOctets_Type()
)
rbnQosIfHCInDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfHCInDroppedOctets.setStatus("current")
_RbnQosIfOutDroppedOctets_Type = Counter32
_RbnQosIfOutDroppedOctets_Object = MibTableColumn
rbnQosIfOutDroppedOctets = _RbnQosIfOutDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 7),
    _RbnQosIfOutDroppedOctets_Type()
)
rbnQosIfOutDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfOutDroppedOctets.setStatus("current")
_RbnQosIfHCOutDroppedOctets_Type = Counter64
_RbnQosIfHCOutDroppedOctets_Object = MibTableColumn
rbnQosIfHCOutDroppedOctets = _RbnQosIfHCOutDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 1, 1, 8),
    _RbnQosIfHCOutDroppedOctets_Type()
)
rbnQosIfHCOutDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfHCOutDroppedOctets.setStatus("current")
_RbnQosInterfaceQueueStatsTable_Object = MibTable
rbnQosInterfaceQueueStatsTable = _RbnQosInterfaceQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2)
)
if mibBuilder.loadTexts:
    rbnQosInterfaceQueueStatsTable.setStatus("current")
_RbnQosInterfaceQueueStatsEntry_Object = MibTableRow
rbnQosInterfaceQueueStatsEntry = _RbnQosInterfaceQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1)
)
rbnQosInterfaceQueueStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-QOS-MIB", "rbnQosIfQueueId"),
)
if mibBuilder.loadTexts:
    rbnQosInterfaceQueueStatsEntry.setStatus("current")


class _RbnQosIfQueueId_Type(Unsigned32):
    """Custom type rbnQosIfQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnQosIfQueueId_Type.__name__ = "Unsigned32"
_RbnQosIfQueueId_Object = MibTableColumn
rbnQosIfQueueId = _RbnQosIfQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 1),
    _RbnQosIfQueueId_Type()
)
rbnQosIfQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosIfQueueId.setStatus("current")
_RbnQosIfQueueOutOctets_Type = Counter32
_RbnQosIfQueueOutOctets_Object = MibTableColumn
rbnQosIfQueueOutOctets = _RbnQosIfQueueOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 2),
    _RbnQosIfQueueOutOctets_Type()
)
rbnQosIfQueueOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueOutOctets.setStatus("current")
_RbnQosIfQueueOutPkts_Type = Counter32
_RbnQosIfQueueOutPkts_Object = MibTableColumn
rbnQosIfQueueOutPkts = _RbnQosIfQueueOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 3),
    _RbnQosIfQueueOutPkts_Type()
)
rbnQosIfQueueOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueOutPkts.setStatus("current")
_RbnQosIfQueueWredDroppedOctets_Type = Counter32
_RbnQosIfQueueWredDroppedOctets_Object = MibTableColumn
rbnQosIfQueueWredDroppedOctets = _RbnQosIfQueueWredDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 4),
    _RbnQosIfQueueWredDroppedOctets_Type()
)
rbnQosIfQueueWredDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueWredDroppedOctets.setStatus("current")
_RbnQosIfQueueWredDroppedPkts_Type = Counter32
_RbnQosIfQueueWredDroppedPkts_Object = MibTableColumn
rbnQosIfQueueWredDroppedPkts = _RbnQosIfQueueWredDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 5),
    _RbnQosIfQueueWredDroppedPkts_Type()
)
rbnQosIfQueueWredDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueWredDroppedPkts.setStatus("current")
_RbnQosIfQueueTailDroppedOctets_Type = Counter32
_RbnQosIfQueueTailDroppedOctets_Object = MibTableColumn
rbnQosIfQueueTailDroppedOctets = _RbnQosIfQueueTailDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 6),
    _RbnQosIfQueueTailDroppedOctets_Type()
)
rbnQosIfQueueTailDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueTailDroppedOctets.setStatus("current")
_RbnQosIfQueueTailDroppedPkts_Type = Counter32
_RbnQosIfQueueTailDroppedPkts_Object = MibTableColumn
rbnQosIfQueueTailDroppedPkts = _RbnQosIfQueueTailDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 7),
    _RbnQosIfQueueTailDroppedPkts_Type()
)
rbnQosIfQueueTailDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueTailDroppedPkts.setStatus("current")
_RbnQosIfQueueHCOutOctets_Type = Counter64
_RbnQosIfQueueHCOutOctets_Object = MibTableColumn
rbnQosIfQueueHCOutOctets = _RbnQosIfQueueHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 8),
    _RbnQosIfQueueHCOutOctets_Type()
)
rbnQosIfQueueHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueHCOutOctets.setStatus("current")
_RbnQosIfQueueHCOutPkts_Type = Counter64
_RbnQosIfQueueHCOutPkts_Object = MibTableColumn
rbnQosIfQueueHCOutPkts = _RbnQosIfQueueHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 9),
    _RbnQosIfQueueHCOutPkts_Type()
)
rbnQosIfQueueHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueHCOutPkts.setStatus("current")
_RbnQosIfQueueHCWredDroppedOctets_Type = Counter64
_RbnQosIfQueueHCWredDroppedOctets_Object = MibTableColumn
rbnQosIfQueueHCWredDroppedOctets = _RbnQosIfQueueHCWredDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 10),
    _RbnQosIfQueueHCWredDroppedOctets_Type()
)
rbnQosIfQueueHCWredDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueHCWredDroppedOctets.setStatus("current")
_RbnQosIfQueueHCWredDroppedPkts_Type = Counter64
_RbnQosIfQueueHCWredDroppedPkts_Object = MibTableColumn
rbnQosIfQueueHCWredDroppedPkts = _RbnQosIfQueueHCWredDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 11),
    _RbnQosIfQueueHCWredDroppedPkts_Type()
)
rbnQosIfQueueHCWredDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueHCWredDroppedPkts.setStatus("current")
_RbnQosIfQueueHCTailDroppedOctets_Type = Counter64
_RbnQosIfQueueHCTailDroppedOctets_Object = MibTableColumn
rbnQosIfQueueHCTailDroppedOctets = _RbnQosIfQueueHCTailDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 12),
    _RbnQosIfQueueHCTailDroppedOctets_Type()
)
rbnQosIfQueueHCTailDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueHCTailDroppedOctets.setStatus("current")
_RbnQosIfQueueHCTailDroppedPkts_Type = Counter64
_RbnQosIfQueueHCTailDroppedPkts_Object = MibTableColumn
rbnQosIfQueueHCTailDroppedPkts = _RbnQosIfQueueHCTailDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 2, 1, 13),
    _RbnQosIfQueueHCTailDroppedPkts_Type()
)
rbnQosIfQueueHCTailDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfQueueHCTailDroppedPkts.setStatus("current")
_RbnQosSubscriberQueueStatsTable_Object = MibTable
rbnQosSubscriberQueueStatsTable = _RbnQosSubscriberQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3)
)
if mibBuilder.loadTexts:
    rbnQosSubscriberQueueStatsTable.setStatus("current")
_RbnQosSubscriberQueueStatsEntry_Object = MibTableRow
rbnQosSubscriberQueueStatsEntry = _RbnQosSubscriberQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1)
)
rbnQosSubscriberQueueStatsEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveName"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
    (0, "RBN-QOS-MIB", "rbnQosSubsQueueId"),
)
if mibBuilder.loadTexts:
    rbnQosSubscriberQueueStatsEntry.setStatus("current")


class _RbnQosSubsQueueId_Type(Unsigned32):
    """Custom type rbnQosSubsQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RbnQosSubsQueueId_Type.__name__ = "Unsigned32"
_RbnQosSubsQueueId_Object = MibTableColumn
rbnQosSubsQueueId = _RbnQosSubsQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 1),
    _RbnQosSubsQueueId_Type()
)
rbnQosSubsQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosSubsQueueId.setStatus("current")


class _RbnQosSubsQueuePolicyName_Type(SnmpAdminString):
    """Custom type rbnQosSubsQueuePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnQosSubsQueuePolicyName_Type.__name__ = "SnmpAdminString"
_RbnQosSubsQueuePolicyName_Object = MibTableColumn
rbnQosSubsQueuePolicyName = _RbnQosSubsQueuePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 2),
    _RbnQosSubsQueuePolicyName_Type()
)
rbnQosSubsQueuePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueuePolicyName.setStatus("current")
_RbnQosSubsQueueOutOctets_Type = Counter32
_RbnQosSubsQueueOutOctets_Object = MibTableColumn
rbnQosSubsQueueOutOctets = _RbnQosSubsQueueOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 3),
    _RbnQosSubsQueueOutOctets_Type()
)
rbnQosSubsQueueOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueOutOctets.setStatus("current")
_RbnQosSubsQueueOutPkts_Type = Counter32
_RbnQosSubsQueueOutPkts_Object = MibTableColumn
rbnQosSubsQueueOutPkts = _RbnQosSubsQueueOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 4),
    _RbnQosSubsQueueOutPkts_Type()
)
rbnQosSubsQueueOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueOutPkts.setStatus("current")
_RbnQosSubsQueueWredDroppedOctets_Type = Counter32
_RbnQosSubsQueueWredDroppedOctets_Object = MibTableColumn
rbnQosSubsQueueWredDroppedOctets = _RbnQosSubsQueueWredDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 5),
    _RbnQosSubsQueueWredDroppedOctets_Type()
)
rbnQosSubsQueueWredDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueWredDroppedOctets.setStatus("current")
_RbnQosSubsQueueWredDroppedPkts_Type = Counter32
_RbnQosSubsQueueWredDroppedPkts_Object = MibTableColumn
rbnQosSubsQueueWredDroppedPkts = _RbnQosSubsQueueWredDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 6),
    _RbnQosSubsQueueWredDroppedPkts_Type()
)
rbnQosSubsQueueWredDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueWredDroppedPkts.setStatus("current")
_RbnQosSubsQueueTailDroppedOctets_Type = Counter32
_RbnQosSubsQueueTailDroppedOctets_Object = MibTableColumn
rbnQosSubsQueueTailDroppedOctets = _RbnQosSubsQueueTailDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 7),
    _RbnQosSubsQueueTailDroppedOctets_Type()
)
rbnQosSubsQueueTailDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueTailDroppedOctets.setStatus("current")
_RbnQosSubsQueueTailDroppedPkts_Type = Counter32
_RbnQosSubsQueueTailDroppedPkts_Object = MibTableColumn
rbnQosSubsQueueTailDroppedPkts = _RbnQosSubsQueueTailDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 8),
    _RbnQosSubsQueueTailDroppedPkts_Type()
)
rbnQosSubsQueueTailDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueTailDroppedPkts.setStatus("current")
_RbnQosSubsQueueHCOutOctets_Type = Counter64
_RbnQosSubsQueueHCOutOctets_Object = MibTableColumn
rbnQosSubsQueueHCOutOctets = _RbnQosSubsQueueHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 9),
    _RbnQosSubsQueueHCOutOctets_Type()
)
rbnQosSubsQueueHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueHCOutOctets.setStatus("current")
_RbnQosSubsQueueHCOutPkts_Type = Counter64
_RbnQosSubsQueueHCOutPkts_Object = MibTableColumn
rbnQosSubsQueueHCOutPkts = _RbnQosSubsQueueHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 10),
    _RbnQosSubsQueueHCOutPkts_Type()
)
rbnQosSubsQueueHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueHCOutPkts.setStatus("current")
_RbnQosSubsQueueHCWredDroppedOctets_Type = Counter64
_RbnQosSubsQueueHCWredDroppedOctets_Object = MibTableColumn
rbnQosSubsQueueHCWredDroppedOctets = _RbnQosSubsQueueHCWredDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 11),
    _RbnQosSubsQueueHCWredDroppedOctets_Type()
)
rbnQosSubsQueueHCWredDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueHCWredDroppedOctets.setStatus("current")
_RbnQosSubsQueueHCWredDroppedPkts_Type = Counter64
_RbnQosSubsQueueHCWredDroppedPkts_Object = MibTableColumn
rbnQosSubsQueueHCWredDroppedPkts = _RbnQosSubsQueueHCWredDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 12),
    _RbnQosSubsQueueHCWredDroppedPkts_Type()
)
rbnQosSubsQueueHCWredDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueHCWredDroppedPkts.setStatus("current")
_RbnQosSubsQueueHCTailDroppedOctets_Type = Counter64
_RbnQosSubsQueueHCTailDroppedOctets_Object = MibTableColumn
rbnQosSubsQueueHCTailDroppedOctets = _RbnQosSubsQueueHCTailDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 13),
    _RbnQosSubsQueueHCTailDroppedOctets_Type()
)
rbnQosSubsQueueHCTailDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueHCTailDroppedOctets.setStatus("current")
_RbnQosSubsQueueHCTailDroppedPkts_Type = Counter64
_RbnQosSubsQueueHCTailDroppedPkts_Object = MibTableColumn
rbnQosSubsQueueHCTailDroppedPkts = _RbnQosSubsQueueHCTailDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 3, 1, 14),
    _RbnQosSubsQueueHCTailDroppedPkts_Type()
)
rbnQosSubsQueueHCTailDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsQueueHCTailDroppedPkts.setStatus("current")
_RbnQosIntfRLClassStatsTable_Object = MibTable
rbnQosIntfRLClassStatsTable = _RbnQosIntfRLClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4)
)
if mibBuilder.loadTexts:
    rbnQosIntfRLClassStatsTable.setStatus("current")
_RbnQosIntfRLClassStatsEntry_Object = MibTableRow
rbnQosIntfRLClassStatsEntry = _RbnQosIntfRLClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1)
)
rbnQosIntfRLClassStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-QOS-MIB", "rbnQosIfRLPolicyType"),
    (0, "RBN-QOS-MIB", "rbnQosIfRLClassId"),
)
if mibBuilder.loadTexts:
    rbnQosIntfRLClassStatsEntry.setStatus("current")
_RbnQosIfRLPolicyType_Type = RbnQosPolicyType
_RbnQosIfRLPolicyType_Object = MibTableColumn
rbnQosIfRLPolicyType = _RbnQosIfRLPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 1),
    _RbnQosIfRLPolicyType_Type()
)
rbnQosIfRLPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosIfRLPolicyType.setStatus("current")
_RbnQosIfRLClassId_Type = RbnQosClassId
_RbnQosIfRLClassId_Object = MibTableColumn
rbnQosIfRLClassId = _RbnQosIfRLClassId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 2),
    _RbnQosIfRLClassId_Type()
)
rbnQosIfRLClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosIfRLClassId.setStatus("current")


class _RbnQosIfRLPolicyName_Type(SnmpAdminString):
    """Custom type rbnQosIfRLPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnQosIfRLPolicyName_Type.__name__ = "SnmpAdminString"
_RbnQosIfRLPolicyName_Object = MibTableColumn
rbnQosIfRLPolicyName = _RbnQosIfRLPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 3),
    _RbnQosIfRLPolicyName_Type()
)
rbnQosIfRLPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLPolicyName.setStatus("current")


class _RbnQosIfRLClassName_Type(SnmpAdminString):
    """Custom type rbnQosIfRLClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnQosIfRLClassName_Type.__name__ = "SnmpAdminString"
_RbnQosIfRLClassName_Object = MibTableColumn
rbnQosIfRLClassName = _RbnQosIfRLClassName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 4),
    _RbnQosIfRLClassName_Type()
)
rbnQosIfRLClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassName.setStatus("current")
_RbnQosIfRLClassConformOctets_Type = Counter64
_RbnQosIfRLClassConformOctets_Object = MibTableColumn
rbnQosIfRLClassConformOctets = _RbnQosIfRLClassConformOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 5),
    _RbnQosIfRLClassConformOctets_Type()
)
rbnQosIfRLClassConformOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassConformOctets.setStatus("current")
_RbnQosIfRLClassConformPkts_Type = Counter64
_RbnQosIfRLClassConformPkts_Object = MibTableColumn
rbnQosIfRLClassConformPkts = _RbnQosIfRLClassConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 6),
    _RbnQosIfRLClassConformPkts_Type()
)
rbnQosIfRLClassConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassConformPkts.setStatus("current")
_RbnQosIfRLClassConformDroppedOctets_Type = Counter64
_RbnQosIfRLClassConformDroppedOctets_Object = MibTableColumn
rbnQosIfRLClassConformDroppedOctets = _RbnQosIfRLClassConformDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 7),
    _RbnQosIfRLClassConformDroppedOctets_Type()
)
rbnQosIfRLClassConformDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassConformDroppedOctets.setStatus("current")
_RbnQosIfRLClassConformDroppedPkts_Type = Counter64
_RbnQosIfRLClassConformDroppedPkts_Object = MibTableColumn
rbnQosIfRLClassConformDroppedPkts = _RbnQosIfRLClassConformDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 8),
    _RbnQosIfRLClassConformDroppedPkts_Type()
)
rbnQosIfRLClassConformDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassConformDroppedPkts.setStatus("current")
_RbnQosIfRLClassExceedOctets_Type = Counter64
_RbnQosIfRLClassExceedOctets_Object = MibTableColumn
rbnQosIfRLClassExceedOctets = _RbnQosIfRLClassExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 9),
    _RbnQosIfRLClassExceedOctets_Type()
)
rbnQosIfRLClassExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassExceedOctets.setStatus("current")
_RbnQosIfRLClassExceedPkts_Type = Counter64
_RbnQosIfRLClassExceedPkts_Object = MibTableColumn
rbnQosIfRLClassExceedPkts = _RbnQosIfRLClassExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 10),
    _RbnQosIfRLClassExceedPkts_Type()
)
rbnQosIfRLClassExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassExceedPkts.setStatus("current")
_RbnQosIfRLClassExceedDroppedOctets_Type = Counter64
_RbnQosIfRLClassExceedDroppedOctets_Object = MibTableColumn
rbnQosIfRLClassExceedDroppedOctets = _RbnQosIfRLClassExceedDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 11),
    _RbnQosIfRLClassExceedDroppedOctets_Type()
)
rbnQosIfRLClassExceedDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassExceedDroppedOctets.setStatus("current")
_RbnQosIfRLClassExceedDroppedPkts_Type = Counter64
_RbnQosIfRLClassExceedDroppedPkts_Object = MibTableColumn
rbnQosIfRLClassExceedDroppedPkts = _RbnQosIfRLClassExceedDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 12),
    _RbnQosIfRLClassExceedDroppedPkts_Type()
)
rbnQosIfRLClassExceedDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassExceedDroppedPkts.setStatus("current")
_RbnQosIfRLClassViolateOctets_Type = Counter64
_RbnQosIfRLClassViolateOctets_Object = MibTableColumn
rbnQosIfRLClassViolateOctets = _RbnQosIfRLClassViolateOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 13),
    _RbnQosIfRLClassViolateOctets_Type()
)
rbnQosIfRLClassViolateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassViolateOctets.setStatus("current")
_RbnQosIfRLClassViolatePkts_Type = Counter64
_RbnQosIfRLClassViolatePkts_Object = MibTableColumn
rbnQosIfRLClassViolatePkts = _RbnQosIfRLClassViolatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 14),
    _RbnQosIfRLClassViolatePkts_Type()
)
rbnQosIfRLClassViolatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassViolatePkts.setStatus("current")
_RbnQosIfRLClassViolateDroppedOctets_Type = Counter64
_RbnQosIfRLClassViolateDroppedOctets_Object = MibTableColumn
rbnQosIfRLClassViolateDroppedOctets = _RbnQosIfRLClassViolateDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 15),
    _RbnQosIfRLClassViolateDroppedOctets_Type()
)
rbnQosIfRLClassViolateDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassViolateDroppedOctets.setStatus("current")
_RbnQosIfRLClassViolateDroppedPkts_Type = Counter64
_RbnQosIfRLClassViolateDroppedPkts_Object = MibTableColumn
rbnQosIfRLClassViolateDroppedPkts = _RbnQosIfRLClassViolateDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 4, 1, 16),
    _RbnQosIfRLClassViolateDroppedPkts_Type()
)
rbnQosIfRLClassViolateDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosIfRLClassViolateDroppedPkts.setStatus("current")
_RbnQosSubscriberRLClassStatsTable_Object = MibTable
rbnQosSubscriberRLClassStatsTable = _RbnQosSubscriberRLClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5)
)
if mibBuilder.loadTexts:
    rbnQosSubscriberRLClassStatsTable.setStatus("current")
_RbnQosSubscriberRLClassStatsEntry_Object = MibTableRow
rbnQosSubscriberRLClassStatsEntry = _RbnQosSubscriberRLClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1)
)
rbnQosSubscriberRLClassStatsEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveName"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
    (0, "RBN-QOS-MIB", "rbnQosSubsRLPolicyType"),
    (0, "RBN-QOS-MIB", "rbnQosSubsRLClassId"),
)
if mibBuilder.loadTexts:
    rbnQosSubscriberRLClassStatsEntry.setStatus("current")
_RbnQosSubsRLPolicyType_Type = RbnQosPolicyType
_RbnQosSubsRLPolicyType_Object = MibTableColumn
rbnQosSubsRLPolicyType = _RbnQosSubsRLPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 1),
    _RbnQosSubsRLPolicyType_Type()
)
rbnQosSubsRLPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosSubsRLPolicyType.setStatus("current")
_RbnQosSubsRLClassId_Type = RbnQosClassId
_RbnQosSubsRLClassId_Object = MibTableColumn
rbnQosSubsRLClassId = _RbnQosSubsRLClassId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 2),
    _RbnQosSubsRLClassId_Type()
)
rbnQosSubsRLClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassId.setStatus("current")


class _RbnQosSubsRLPolicyName_Type(SnmpAdminString):
    """Custom type rbnQosSubsRLPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnQosSubsRLPolicyName_Type.__name__ = "SnmpAdminString"
_RbnQosSubsRLPolicyName_Object = MibTableColumn
rbnQosSubsRLPolicyName = _RbnQosSubsRLPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 3),
    _RbnQosSubsRLPolicyName_Type()
)
rbnQosSubsRLPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLPolicyName.setStatus("current")


class _RbnQosSubsRLClassName_Type(SnmpAdminString):
    """Custom type rbnQosSubsRLClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnQosSubsRLClassName_Type.__name__ = "SnmpAdminString"
_RbnQosSubsRLClassName_Object = MibTableColumn
rbnQosSubsRLClassName = _RbnQosSubsRLClassName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 4),
    _RbnQosSubsRLClassName_Type()
)
rbnQosSubsRLClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassName.setStatus("current")
_RbnQosSubsRLClassConformOctets_Type = Counter64
_RbnQosSubsRLClassConformOctets_Object = MibTableColumn
rbnQosSubsRLClassConformOctets = _RbnQosSubsRLClassConformOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 5),
    _RbnQosSubsRLClassConformOctets_Type()
)
rbnQosSubsRLClassConformOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassConformOctets.setStatus("current")
_RbnQosSubsRLClassConformPkts_Type = Counter64
_RbnQosSubsRLClassConformPkts_Object = MibTableColumn
rbnQosSubsRLClassConformPkts = _RbnQosSubsRLClassConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 6),
    _RbnQosSubsRLClassConformPkts_Type()
)
rbnQosSubsRLClassConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassConformPkts.setStatus("current")
_RbnQosSubsRLClassConformDroppedOctets_Type = Counter64
_RbnQosSubsRLClassConformDroppedOctets_Object = MibTableColumn
rbnQosSubsRLClassConformDroppedOctets = _RbnQosSubsRLClassConformDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 7),
    _RbnQosSubsRLClassConformDroppedOctets_Type()
)
rbnQosSubsRLClassConformDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassConformDroppedOctets.setStatus("current")
_RbnQosSubsRLClassConformDroppedPkts_Type = Counter64
_RbnQosSubsRLClassConformDroppedPkts_Object = MibTableColumn
rbnQosSubsRLClassConformDroppedPkts = _RbnQosSubsRLClassConformDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 8),
    _RbnQosSubsRLClassConformDroppedPkts_Type()
)
rbnQosSubsRLClassConformDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassConformDroppedPkts.setStatus("current")
_RbnQosSubsRLClassExceedOctets_Type = Counter64
_RbnQosSubsRLClassExceedOctets_Object = MibTableColumn
rbnQosSubsRLClassExceedOctets = _RbnQosSubsRLClassExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 9),
    _RbnQosSubsRLClassExceedOctets_Type()
)
rbnQosSubsRLClassExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassExceedOctets.setStatus("current")
_RbnQosSubsRLClassExceedPkts_Type = Counter64
_RbnQosSubsRLClassExceedPkts_Object = MibTableColumn
rbnQosSubsRLClassExceedPkts = _RbnQosSubsRLClassExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 10),
    _RbnQosSubsRLClassExceedPkts_Type()
)
rbnQosSubsRLClassExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassExceedPkts.setStatus("current")
_RbnQosSubsRLClassExceedDroppedOctets_Type = Counter64
_RbnQosSubsRLClassExceedDroppedOctets_Object = MibTableColumn
rbnQosSubsRLClassExceedDroppedOctets = _RbnQosSubsRLClassExceedDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 11),
    _RbnQosSubsRLClassExceedDroppedOctets_Type()
)
rbnQosSubsRLClassExceedDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassExceedDroppedOctets.setStatus("current")
_RbnQosSubsRLClassExceedDroppedPkts_Type = Counter64
_RbnQosSubsRLClassExceedDroppedPkts_Object = MibTableColumn
rbnQosSubsRLClassExceedDroppedPkts = _RbnQosSubsRLClassExceedDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 12),
    _RbnQosSubsRLClassExceedDroppedPkts_Type()
)
rbnQosSubsRLClassExceedDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassExceedDroppedPkts.setStatus("current")
_RbnQosSubsRLClassViolateOctets_Type = Counter64
_RbnQosSubsRLClassViolateOctets_Object = MibTableColumn
rbnQosSubsRLClassViolateOctets = _RbnQosSubsRLClassViolateOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 13),
    _RbnQosSubsRLClassViolateOctets_Type()
)
rbnQosSubsRLClassViolateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassViolateOctets.setStatus("current")
_RbnQosSubsRLClassViolatePkts_Type = Counter64
_RbnQosSubsRLClassViolatePkts_Object = MibTableColumn
rbnQosSubsRLClassViolatePkts = _RbnQosSubsRLClassViolatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 14),
    _RbnQosSubsRLClassViolatePkts_Type()
)
rbnQosSubsRLClassViolatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassViolatePkts.setStatus("current")
_RbnQosSubsRLClassViolateDroppedOctets_Type = Counter64
_RbnQosSubsRLClassViolateDroppedOctets_Object = MibTableColumn
rbnQosSubsRLClassViolateDroppedOctets = _RbnQosSubsRLClassViolateDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 15),
    _RbnQosSubsRLClassViolateDroppedOctets_Type()
)
rbnQosSubsRLClassViolateDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassViolateDroppedOctets.setStatus("current")
_RbnQosSubsRLClassViolateDroppedPkts_Type = Counter64
_RbnQosSubsRLClassViolateDroppedPkts_Object = MibTableColumn
rbnQosSubsRLClassViolateDroppedPkts = _RbnQosSubsRLClassViolateDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 5, 1, 16),
    _RbnQosSubsRLClassViolateDroppedPkts_Type()
)
rbnQosSubsRLClassViolateDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosSubsRLClassViolateDroppedPkts.setStatus("current")
_RbnQosHierarchicalPolicyStatsTable_Object = MibTable
rbnQosHierarchicalPolicyStatsTable = _RbnQosHierarchicalPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 6)
)
if mibBuilder.loadTexts:
    rbnQosHierarchicalPolicyStatsTable.setStatus("current")
_RbnQosHierarchicalPolicyStatsEntry_Object = MibTableRow
rbnQosHierarchicalPolicyStatsEntry = _RbnQosHierarchicalPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 6, 1)
)
rbnQosHierarchicalPolicyStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-QOS-MIB", "rbnQosHierarchicalPolicyType"),
)
if mibBuilder.loadTexts:
    rbnQosHierarchicalPolicyStatsEntry.setStatus("current")
_RbnQosHierarchicalPolicyType_Type = RbnQosPolicyType
_RbnQosHierarchicalPolicyType_Object = MibTableColumn
rbnQosHierarchicalPolicyType = _RbnQosHierarchicalPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 6, 1, 1),
    _RbnQosHierarchicalPolicyType_Type()
)
rbnQosHierarchicalPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPolicyType.setStatus("current")


class _RbnQosHierarchicalPolicyName_Type(SnmpAdminString):
    """Custom type rbnQosHierarchicalPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnQosHierarchicalPolicyName_Type.__name__ = "SnmpAdminString"
_RbnQosHierarchicalPolicyName_Object = MibTableColumn
rbnQosHierarchicalPolicyName = _RbnQosHierarchicalPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 6, 1, 2),
    _RbnQosHierarchicalPolicyName_Type()
)
rbnQosHierarchicalPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPolicyName.setStatus("current")
_RbnQosHierarchicalPolicyDroppedOctets_Type = Counter64
_RbnQosHierarchicalPolicyDroppedOctets_Object = MibTableColumn
rbnQosHierarchicalPolicyDroppedOctets = _RbnQosHierarchicalPolicyDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 6, 1, 3),
    _RbnQosHierarchicalPolicyDroppedOctets_Type()
)
rbnQosHierarchicalPolicyDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPolicyDroppedOctets.setStatus("current")
_RbnQosHierarchicalPolicyDroppedPkts_Type = Counter64
_RbnQosHierarchicalPolicyDroppedPkts_Object = MibTableColumn
rbnQosHierarchicalPolicyDroppedPkts = _RbnQosHierarchicalPolicyDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 6, 1, 4),
    _RbnQosHierarchicalPolicyDroppedPkts_Type()
)
rbnQosHierarchicalPolicyDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPolicyDroppedPkts.setStatus("current")
_RbnQosHierarchicalPClassStatsTable_Object = MibTable
rbnQosHierarchicalPClassStatsTable = _RbnQosHierarchicalPClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 7)
)
if mibBuilder.loadTexts:
    rbnQosHierarchicalPClassStatsTable.setStatus("current")
_RbnQosHierarchicalPClassStatsEntry_Object = MibTableRow
rbnQosHierarchicalPClassStatsEntry = _RbnQosHierarchicalPClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 7, 1)
)
rbnQosHierarchicalPClassStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-QOS-MIB", "rbnQosHierarchicalPolicyType"),
    (0, "RBN-QOS-MIB", "rbnQosHierarchicalPClassId"),
)
if mibBuilder.loadTexts:
    rbnQosHierarchicalPClassStatsEntry.setStatus("current")
_RbnQosHierarchicalPClassId_Type = RbnQosClassId
_RbnQosHierarchicalPClassId_Object = MibTableColumn
rbnQosHierarchicalPClassId = _RbnQosHierarchicalPClassId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 7, 1, 1),
    _RbnQosHierarchicalPClassId_Type()
)
rbnQosHierarchicalPClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPClassId.setStatus("current")


class _RbnQosHierarchicalPClassName_Type(SnmpAdminString):
    """Custom type rbnQosHierarchicalPClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnQosHierarchicalPClassName_Type.__name__ = "SnmpAdminString"
_RbnQosHierarchicalPClassName_Object = MibTableColumn
rbnQosHierarchicalPClassName = _RbnQosHierarchicalPClassName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 7, 1, 2),
    _RbnQosHierarchicalPClassName_Type()
)
rbnQosHierarchicalPClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPClassName.setStatus("current")
_RbnQosHierarchicalPClassDroppedOctets_Type = Counter64
_RbnQosHierarchicalPClassDroppedOctets_Object = MibTableColumn
rbnQosHierarchicalPClassDroppedOctets = _RbnQosHierarchicalPClassDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 7, 1, 3),
    _RbnQosHierarchicalPClassDroppedOctets_Type()
)
rbnQosHierarchicalPClassDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPClassDroppedOctets.setStatus("current")
_RbnQosHierarchicalPClassDroppedPkts_Type = Counter64
_RbnQosHierarchicalPClassDroppedPkts_Object = MibTableColumn
rbnQosHierarchicalPClassDroppedPkts = _RbnQosHierarchicalPClassDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 1, 7, 1, 4),
    _RbnQosHierarchicalPClassDroppedPkts_Type()
)
rbnQosHierarchicalPClassDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnQosHierarchicalPClassDroppedPkts.setStatus("current")
_RbnQosMibConformance_ObjectIdentity = ObjectIdentity
rbnQosMibConformance = _RbnQosMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2)
)
_RbnQosCompliances_ObjectIdentity = ObjectIdentity
rbnQosCompliances = _RbnQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 1)
)
_RbnQosGroups_ObjectIdentity = ObjectIdentity
rbnQosGroups = _RbnQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 2)
)

# Managed Objects groups

rbnQosIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 2, 1)
)
rbnQosIfGroup.setObjects(
      *(("RBN-QOS-MIB", "rbnQosIfInOctets"),
        ("RBN-QOS-MIB", "rbnQosIfHCInOctets"),
        ("RBN-QOS-MIB", "rbnQosIfOutOctets"),
        ("RBN-QOS-MIB", "rbnQosIfHCOutOctets"),
        ("RBN-QOS-MIB", "rbnQosIfInDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfHCInDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfOutDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfHCOutDroppedOctets"))
)
if mibBuilder.loadTexts:
    rbnQosIfGroup.setStatus("current")

rbnQosIfQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 2, 2)
)
rbnQosIfQueueGroup.setObjects(
      *(("RBN-QOS-MIB", "rbnQosIfQueueOutOctets"),
        ("RBN-QOS-MIB", "rbnQosIfQueueHCOutOctets"),
        ("RBN-QOS-MIB", "rbnQosIfQueueOutPkts"),
        ("RBN-QOS-MIB", "rbnQosIfQueueHCOutPkts"),
        ("RBN-QOS-MIB", "rbnQosIfQueueWredDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfQueueHCWredDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfQueueWredDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosIfQueueHCWredDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosIfQueueTailDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfQueueHCTailDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfQueueTailDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosIfQueueHCTailDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnQosIfQueueGroup.setStatus("current")

rbnQosSubscriberQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 2, 3)
)
rbnQosSubscriberQueueGroup.setObjects(
      *(("RBN-QOS-MIB", "rbnQosSubsQueuePolicyName"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueOutOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueOutPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueWredDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueWredDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueTailDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueTailDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueHCOutOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueHCOutPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueHCWredDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueHCWredDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueHCTailDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsQueueHCTailDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnQosSubscriberQueueGroup.setStatus("current")

rbnQosIfRLClassStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 2, 4)
)
rbnQosIfRLClassStatsGroup.setObjects(
      *(("RBN-QOS-MIB", "rbnQosIfRLPolicyName"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassName"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassConformOctets"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassConformPkts"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassConformDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassConformDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassExceedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassExceedPkts"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassExceedDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassExceedDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassViolateOctets"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassViolatePkts"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassViolateDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosIfRLClassViolateDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnQosIfRLClassStatsGroup.setStatus("current")

rbnQosSubscriberRLClassStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 2, 5)
)
rbnQosSubscriberRLClassStatsGroup.setObjects(
      *(("RBN-QOS-MIB", "rbnQosSubsRLPolicyName"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassName"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassConformOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassConformPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassConformDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassConformDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassExceedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassExceedPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassExceedDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassExceedDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassViolateOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassViolatePkts"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassViolateDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosSubsRLClassViolateDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnQosSubscriberRLClassStatsGroup.setStatus("current")

rbnQosHierarchicalPolicyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 2, 6)
)
rbnQosHierarchicalPolicyStatsGroup.setObjects(
      *(("RBN-QOS-MIB", "rbnQosHierarchicalPolicyName"),
        ("RBN-QOS-MIB", "rbnQosHierarchicalPolicyDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosHierarchicalPolicyDroppedPkts"),
        ("RBN-QOS-MIB", "rbnQosHierarchicalPClassName"),
        ("RBN-QOS-MIB", "rbnQosHierarchicalPClassDroppedOctets"),
        ("RBN-QOS-MIB", "rbnQosHierarchicalPClassDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnQosHierarchicalPolicyStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnQosCompliance.setStatus(
        "deprecated"
    )

rbnQosCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnQosCompliance2.setStatus(
        "current"
    )

rbnQosCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rbnQosCompliance3.setStatus(
        "current"
    )

rbnQosCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rbnQosCompliance4.setStatus(
        "current"
    )

rbnQosCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 22, 2, 1, 5)
)
if mibBuilder.loadTexts:
    rbnQosCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-QOS-MIB",
    **{"RbnQosPolicyType": RbnQosPolicyType,
       "RbnQosClassId": RbnQosClassId,
       "rbnQosMib": rbnQosMib,
       "rbnQosMibObjects": rbnQosMibObjects,
       "rbnQosInterfaceTable": rbnQosInterfaceTable,
       "rbnQosInterfaceEntry": rbnQosInterfaceEntry,
       "rbnQosIfInOctets": rbnQosIfInOctets,
       "rbnQosIfHCInOctets": rbnQosIfHCInOctets,
       "rbnQosIfOutOctets": rbnQosIfOutOctets,
       "rbnQosIfHCOutOctets": rbnQosIfHCOutOctets,
       "rbnQosIfInDroppedOctets": rbnQosIfInDroppedOctets,
       "rbnQosIfHCInDroppedOctets": rbnQosIfHCInDroppedOctets,
       "rbnQosIfOutDroppedOctets": rbnQosIfOutDroppedOctets,
       "rbnQosIfHCOutDroppedOctets": rbnQosIfHCOutDroppedOctets,
       "rbnQosInterfaceQueueStatsTable": rbnQosInterfaceQueueStatsTable,
       "rbnQosInterfaceQueueStatsEntry": rbnQosInterfaceQueueStatsEntry,
       "rbnQosIfQueueId": rbnQosIfQueueId,
       "rbnQosIfQueueOutOctets": rbnQosIfQueueOutOctets,
       "rbnQosIfQueueOutPkts": rbnQosIfQueueOutPkts,
       "rbnQosIfQueueWredDroppedOctets": rbnQosIfQueueWredDroppedOctets,
       "rbnQosIfQueueWredDroppedPkts": rbnQosIfQueueWredDroppedPkts,
       "rbnQosIfQueueTailDroppedOctets": rbnQosIfQueueTailDroppedOctets,
       "rbnQosIfQueueTailDroppedPkts": rbnQosIfQueueTailDroppedPkts,
       "rbnQosIfQueueHCOutOctets": rbnQosIfQueueHCOutOctets,
       "rbnQosIfQueueHCOutPkts": rbnQosIfQueueHCOutPkts,
       "rbnQosIfQueueHCWredDroppedOctets": rbnQosIfQueueHCWredDroppedOctets,
       "rbnQosIfQueueHCWredDroppedPkts": rbnQosIfQueueHCWredDroppedPkts,
       "rbnQosIfQueueHCTailDroppedOctets": rbnQosIfQueueHCTailDroppedOctets,
       "rbnQosIfQueueHCTailDroppedPkts": rbnQosIfQueueHCTailDroppedPkts,
       "rbnQosSubscriberQueueStatsTable": rbnQosSubscriberQueueStatsTable,
       "rbnQosSubscriberQueueStatsEntry": rbnQosSubscriberQueueStatsEntry,
       "rbnQosSubsQueueId": rbnQosSubsQueueId,
       "rbnQosSubsQueuePolicyName": rbnQosSubsQueuePolicyName,
       "rbnQosSubsQueueOutOctets": rbnQosSubsQueueOutOctets,
       "rbnQosSubsQueueOutPkts": rbnQosSubsQueueOutPkts,
       "rbnQosSubsQueueWredDroppedOctets": rbnQosSubsQueueWredDroppedOctets,
       "rbnQosSubsQueueWredDroppedPkts": rbnQosSubsQueueWredDroppedPkts,
       "rbnQosSubsQueueTailDroppedOctets": rbnQosSubsQueueTailDroppedOctets,
       "rbnQosSubsQueueTailDroppedPkts": rbnQosSubsQueueTailDroppedPkts,
       "rbnQosSubsQueueHCOutOctets": rbnQosSubsQueueHCOutOctets,
       "rbnQosSubsQueueHCOutPkts": rbnQosSubsQueueHCOutPkts,
       "rbnQosSubsQueueHCWredDroppedOctets": rbnQosSubsQueueHCWredDroppedOctets,
       "rbnQosSubsQueueHCWredDroppedPkts": rbnQosSubsQueueHCWredDroppedPkts,
       "rbnQosSubsQueueHCTailDroppedOctets": rbnQosSubsQueueHCTailDroppedOctets,
       "rbnQosSubsQueueHCTailDroppedPkts": rbnQosSubsQueueHCTailDroppedPkts,
       "rbnQosIntfRLClassStatsTable": rbnQosIntfRLClassStatsTable,
       "rbnQosIntfRLClassStatsEntry": rbnQosIntfRLClassStatsEntry,
       "rbnQosIfRLPolicyType": rbnQosIfRLPolicyType,
       "rbnQosIfRLClassId": rbnQosIfRLClassId,
       "rbnQosIfRLPolicyName": rbnQosIfRLPolicyName,
       "rbnQosIfRLClassName": rbnQosIfRLClassName,
       "rbnQosIfRLClassConformOctets": rbnQosIfRLClassConformOctets,
       "rbnQosIfRLClassConformPkts": rbnQosIfRLClassConformPkts,
       "rbnQosIfRLClassConformDroppedOctets": rbnQosIfRLClassConformDroppedOctets,
       "rbnQosIfRLClassConformDroppedPkts": rbnQosIfRLClassConformDroppedPkts,
       "rbnQosIfRLClassExceedOctets": rbnQosIfRLClassExceedOctets,
       "rbnQosIfRLClassExceedPkts": rbnQosIfRLClassExceedPkts,
       "rbnQosIfRLClassExceedDroppedOctets": rbnQosIfRLClassExceedDroppedOctets,
       "rbnQosIfRLClassExceedDroppedPkts": rbnQosIfRLClassExceedDroppedPkts,
       "rbnQosIfRLClassViolateOctets": rbnQosIfRLClassViolateOctets,
       "rbnQosIfRLClassViolatePkts": rbnQosIfRLClassViolatePkts,
       "rbnQosIfRLClassViolateDroppedOctets": rbnQosIfRLClassViolateDroppedOctets,
       "rbnQosIfRLClassViolateDroppedPkts": rbnQosIfRLClassViolateDroppedPkts,
       "rbnQosSubscriberRLClassStatsTable": rbnQosSubscriberRLClassStatsTable,
       "rbnQosSubscriberRLClassStatsEntry": rbnQosSubscriberRLClassStatsEntry,
       "rbnQosSubsRLPolicyType": rbnQosSubsRLPolicyType,
       "rbnQosSubsRLClassId": rbnQosSubsRLClassId,
       "rbnQosSubsRLPolicyName": rbnQosSubsRLPolicyName,
       "rbnQosSubsRLClassName": rbnQosSubsRLClassName,
       "rbnQosSubsRLClassConformOctets": rbnQosSubsRLClassConformOctets,
       "rbnQosSubsRLClassConformPkts": rbnQosSubsRLClassConformPkts,
       "rbnQosSubsRLClassConformDroppedOctets": rbnQosSubsRLClassConformDroppedOctets,
       "rbnQosSubsRLClassConformDroppedPkts": rbnQosSubsRLClassConformDroppedPkts,
       "rbnQosSubsRLClassExceedOctets": rbnQosSubsRLClassExceedOctets,
       "rbnQosSubsRLClassExceedPkts": rbnQosSubsRLClassExceedPkts,
       "rbnQosSubsRLClassExceedDroppedOctets": rbnQosSubsRLClassExceedDroppedOctets,
       "rbnQosSubsRLClassExceedDroppedPkts": rbnQosSubsRLClassExceedDroppedPkts,
       "rbnQosSubsRLClassViolateOctets": rbnQosSubsRLClassViolateOctets,
       "rbnQosSubsRLClassViolatePkts": rbnQosSubsRLClassViolatePkts,
       "rbnQosSubsRLClassViolateDroppedOctets": rbnQosSubsRLClassViolateDroppedOctets,
       "rbnQosSubsRLClassViolateDroppedPkts": rbnQosSubsRLClassViolateDroppedPkts,
       "rbnQosHierarchicalPolicyStatsTable": rbnQosHierarchicalPolicyStatsTable,
       "rbnQosHierarchicalPolicyStatsEntry": rbnQosHierarchicalPolicyStatsEntry,
       "rbnQosHierarchicalPolicyType": rbnQosHierarchicalPolicyType,
       "rbnQosHierarchicalPolicyName": rbnQosHierarchicalPolicyName,
       "rbnQosHierarchicalPolicyDroppedOctets": rbnQosHierarchicalPolicyDroppedOctets,
       "rbnQosHierarchicalPolicyDroppedPkts": rbnQosHierarchicalPolicyDroppedPkts,
       "rbnQosHierarchicalPClassStatsTable": rbnQosHierarchicalPClassStatsTable,
       "rbnQosHierarchicalPClassStatsEntry": rbnQosHierarchicalPClassStatsEntry,
       "rbnQosHierarchicalPClassId": rbnQosHierarchicalPClassId,
       "rbnQosHierarchicalPClassName": rbnQosHierarchicalPClassName,
       "rbnQosHierarchicalPClassDroppedOctets": rbnQosHierarchicalPClassDroppedOctets,
       "rbnQosHierarchicalPClassDroppedPkts": rbnQosHierarchicalPClassDroppedPkts,
       "rbnQosMibConformance": rbnQosMibConformance,
       "rbnQosCompliances": rbnQosCompliances,
       "rbnQosCompliance": rbnQosCompliance,
       "rbnQosCompliance2": rbnQosCompliance2,
       "rbnQosCompliance3": rbnQosCompliance3,
       "rbnQosCompliance4": rbnQosCompliance4,
       "rbnQosCompliance5": rbnQosCompliance5,
       "rbnQosGroups": rbnQosGroups,
       "rbnQosIfGroup": rbnQosIfGroup,
       "rbnQosIfQueueGroup": rbnQosIfQueueGroup,
       "rbnQosSubscriberQueueGroup": rbnQosSubscriberQueueGroup,
       "rbnQosIfRLClassStatsGroup": rbnQosIfRLClassStatsGroup,
       "rbnQosSubscriberRLClassStatsGroup": rbnQosSubscriberRLClassStatsGroup,
       "rbnQosHierarchicalPolicyStatsGroup": rbnQosHierarchicalPolicyStatsGroup}
)
