# SNMP MIB module (BROCADE-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:30 2024
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

(brcdQos,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "brcdQos")

(PortPriorityTC,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "PortPriorityTC")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

brcdQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1)
)
brcdQosMIB.setRevisions(
        ("2012-07-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdHqosObjects_ObjectIdentity = ObjectIdentity
brcdHqosObjects = _BrcdHqosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1)
)
_BrcdHqosStatsTable_Object = MibTable
brcdHqosStatsTable = _BrcdHqosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    brcdHqosStatsTable.setStatus("current")
_BrcdHqosStatsEntry_Object = MibTableRow
brcdHqosStatsEntry = _BrcdHqosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1)
)
brcdHqosStatsEntry.setIndexNames(
    (0, "BROCADE-QOS-MIB", "brcdHqosIfIndex"),
    (0, "BROCADE-QOS-MIB", "brcdHqosEndpointType"),
    (0, "BROCADE-QOS-MIB", "brcdHqosEndpointTag"),
    (0, "BROCADE-QOS-MIB", "brcdHqosEndpointInnerTag"),
    (0, "BROCADE-QOS-MIB", "brcdHqosStatsPriority"),
)
if mibBuilder.loadTexts:
    brcdHqosStatsEntry.setStatus("current")
_BrcdHqosIfIndex_Type = InterfaceIndex
_BrcdHqosIfIndex_Object = MibTableColumn
brcdHqosIfIndex = _BrcdHqosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 1),
    _BrcdHqosIfIndex_Type()
)
brcdHqosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdHqosIfIndex.setStatus("current")


class _BrcdHqosEndpointType_Type(Integer32):
    """Custom type brcdHqosEndpointType based on Integer32"""
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
        *(("bVlanIsid", 4),
          ("doubleTaggedVlan", 3),
          ("other", 1),
          ("singleTaggedVlan", 2))
    )


_BrcdHqosEndpointType_Type.__name__ = "Integer32"
_BrcdHqosEndpointType_Object = MibTableColumn
brcdHqosEndpointType = _BrcdHqosEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 2),
    _BrcdHqosEndpointType_Type()
)
brcdHqosEndpointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdHqosEndpointType.setStatus("current")
_BrcdHqosEndpointTag_Type = Unsigned32
_BrcdHqosEndpointTag_Object = MibTableColumn
brcdHqosEndpointTag = _BrcdHqosEndpointTag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 3),
    _BrcdHqosEndpointTag_Type()
)
brcdHqosEndpointTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdHqosEndpointTag.setStatus("current")
_BrcdHqosEndpointInnerTag_Type = Unsigned32
_BrcdHqosEndpointInnerTag_Object = MibTableColumn
brcdHqosEndpointInnerTag = _BrcdHqosEndpointInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 4),
    _BrcdHqosEndpointInnerTag_Type()
)
brcdHqosEndpointInnerTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdHqosEndpointInnerTag.setStatus("current")
_BrcdHqosStatsPriority_Type = PortPriorityTC
_BrcdHqosStatsPriority_Object = MibTableColumn
brcdHqosStatsPriority = _BrcdHqosStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 5),
    _BrcdHqosStatsPriority_Type()
)
brcdHqosStatsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdHqosStatsPriority.setStatus("current")
_BrcdHqosStatsDescription_Type = DisplayString
_BrcdHqosStatsDescription_Object = MibTableColumn
brcdHqosStatsDescription = _BrcdHqosStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 6),
    _BrcdHqosStatsDescription_Type()
)
brcdHqosStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsDescription.setStatus("current")
_BrcdHqosStatsEnquePkts_Type = Counter64
_BrcdHqosStatsEnquePkts_Object = MibTableColumn
brcdHqosStatsEnquePkts = _BrcdHqosStatsEnquePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 7),
    _BrcdHqosStatsEnquePkts_Type()
)
brcdHqosStatsEnquePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsEnquePkts.setStatus("current")
_BrcdHqosStatsEnqueBytes_Type = Counter64
_BrcdHqosStatsEnqueBytes_Object = MibTableColumn
brcdHqosStatsEnqueBytes = _BrcdHqosStatsEnqueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 8),
    _BrcdHqosStatsEnqueBytes_Type()
)
brcdHqosStatsEnqueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsEnqueBytes.setStatus("current")
_BrcdHqosStatsDequePkts_Type = Counter64
_BrcdHqosStatsDequePkts_Object = MibTableColumn
brcdHqosStatsDequePkts = _BrcdHqosStatsDequePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 9),
    _BrcdHqosStatsDequePkts_Type()
)
brcdHqosStatsDequePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsDequePkts.setStatus("current")
_BrcdHqosStatsDequeBytes_Type = Counter64
_BrcdHqosStatsDequeBytes_Object = MibTableColumn
brcdHqosStatsDequeBytes = _BrcdHqosStatsDequeBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 10),
    _BrcdHqosStatsDequeBytes_Type()
)
brcdHqosStatsDequeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsDequeBytes.setStatus("current")
_BrcdHqosStatsTotalDiscardPkts_Type = Counter64
_BrcdHqosStatsTotalDiscardPkts_Object = MibTableColumn
brcdHqosStatsTotalDiscardPkts = _BrcdHqosStatsTotalDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 11),
    _BrcdHqosStatsTotalDiscardPkts_Type()
)
brcdHqosStatsTotalDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsTotalDiscardPkts.setStatus("current")
_BrcdHqosStatsTotalDiscardBytes_Type = Counter64
_BrcdHqosStatsTotalDiscardBytes_Object = MibTableColumn
brcdHqosStatsTotalDiscardBytes = _BrcdHqosStatsTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 12),
    _BrcdHqosStatsTotalDiscardBytes_Type()
)
brcdHqosStatsTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsTotalDiscardBytes.setStatus("current")
_BrcdHqosStatsOldestDiscardPkts_Type = Counter64
_BrcdHqosStatsOldestDiscardPkts_Object = MibTableColumn
brcdHqosStatsOldestDiscardPkts = _BrcdHqosStatsOldestDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 13),
    _BrcdHqosStatsOldestDiscardPkts_Type()
)
brcdHqosStatsOldestDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsOldestDiscardPkts.setStatus("current")
_BrcdHqosStatsOldestDiscardBytes_Type = Counter64
_BrcdHqosStatsOldestDiscardBytes_Object = MibTableColumn
brcdHqosStatsOldestDiscardBytes = _BrcdHqosStatsOldestDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 14),
    _BrcdHqosStatsOldestDiscardBytes_Type()
)
brcdHqosStatsOldestDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsOldestDiscardBytes.setStatus("current")
_BrcdHqosStatsWREDDroppedPkts_Type = Counter64
_BrcdHqosStatsWREDDroppedPkts_Object = MibTableColumn
brcdHqosStatsWREDDroppedPkts = _BrcdHqosStatsWREDDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 15),
    _BrcdHqosStatsWREDDroppedPkts_Type()
)
brcdHqosStatsWREDDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsWREDDroppedPkts.setStatus("current")
_BrcdHqosStatsWREDDroppedBytes_Type = Counter64
_BrcdHqosStatsWREDDroppedBytes_Object = MibTableColumn
brcdHqosStatsWREDDroppedBytes = _BrcdHqosStatsWREDDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 16),
    _BrcdHqosStatsWREDDroppedBytes_Type()
)
brcdHqosStatsWREDDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsWREDDroppedBytes.setStatus("current")
_BrcdHqosStatsCurrentQDepth_Type = Counter64
_BrcdHqosStatsCurrentQDepth_Object = MibTableColumn
brcdHqosStatsCurrentQDepth = _BrcdHqosStatsCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 17),
    _BrcdHqosStatsCurrentQDepth_Type()
)
brcdHqosStatsCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsCurrentQDepth.setStatus("current")
_BrcdHqosStatsMaxQDepthSinceLastRead_Type = Counter64
_BrcdHqosStatsMaxQDepthSinceLastRead_Object = MibTableColumn
brcdHqosStatsMaxQDepthSinceLastRead = _BrcdHqosStatsMaxQDepthSinceLastRead_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 18),
    _BrcdHqosStatsMaxQDepthSinceLastRead_Type()
)
brcdHqosStatsMaxQDepthSinceLastRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdHqosStatsMaxQDepthSinceLastRead.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-QOS-MIB",
    **{"brcdQosMIB": brcdQosMIB,
       "brcdHqosObjects": brcdHqosObjects,
       "brcdHqosStatsTable": brcdHqosStatsTable,
       "brcdHqosStatsEntry": brcdHqosStatsEntry,
       "brcdHqosIfIndex": brcdHqosIfIndex,
       "brcdHqosEndpointType": brcdHqosEndpointType,
       "brcdHqosEndpointTag": brcdHqosEndpointTag,
       "brcdHqosEndpointInnerTag": brcdHqosEndpointInnerTag,
       "brcdHqosStatsPriority": brcdHqosStatsPriority,
       "brcdHqosStatsDescription": brcdHqosStatsDescription,
       "brcdHqosStatsEnquePkts": brcdHqosStatsEnquePkts,
       "brcdHqosStatsEnqueBytes": brcdHqosStatsEnqueBytes,
       "brcdHqosStatsDequePkts": brcdHqosStatsDequePkts,
       "brcdHqosStatsDequeBytes": brcdHqosStatsDequeBytes,
       "brcdHqosStatsTotalDiscardPkts": brcdHqosStatsTotalDiscardPkts,
       "brcdHqosStatsTotalDiscardBytes": brcdHqosStatsTotalDiscardBytes,
       "brcdHqosStatsOldestDiscardPkts": brcdHqosStatsOldestDiscardPkts,
       "brcdHqosStatsOldestDiscardBytes": brcdHqosStatsOldestDiscardBytes,
       "brcdHqosStatsWREDDroppedPkts": brcdHqosStatsWREDDroppedPkts,
       "brcdHqosStatsWREDDroppedBytes": brcdHqosStatsWREDDroppedBytes,
       "brcdHqosStatsCurrentQDepth": brcdHqosStatsCurrentQDepth,
       "brcdHqosStatsMaxQDepthSinceLastRead": brcdHqosStatsMaxQDepthSinceLastRead}
)
