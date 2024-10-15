# SNMP MIB module (IEEE8023-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8023-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:54 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lagMIB = ModuleIdentity(
    (1, 2, 840, 10006, 300, 43)
)
lagMIB.setRevisions(
        ("2016-10-12 00:00",
         "2014-12-18 00:00",
         "2012-01-16 00:00",
         "2007-06-29 00:00",
         "2000-06-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LacpKey(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LacpState(Bits, TextualConvention):
    status = "current"


class DrcpState(Bits, TextualConvention):
    status = "current"


class ChurnState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("churn", 2),
          ("churnMonitor", 3),
          ("noChurn", 1))
    )



class AggState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class DrniConvAdminGatewayList(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x,"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class PortalLinkList(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d,"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )



class ServiceIdList(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d,"


# MIB Managed Objects in the order of their OIDs

_LagMIBNotifications_ObjectIdentity = ObjectIdentity
lagMIBNotifications = _LagMIBNotifications_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 0)
)
_LagMIBObjects_ObjectIdentity = ObjectIdentity
lagMIBObjects = _LagMIBObjects_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 1)
)
_Dot3adAgg_ObjectIdentity = ObjectIdentity
dot3adAgg = _Dot3adAgg_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 1, 1)
)
_Dot3adAggTable_Object = MibTable
dot3adAggTable = _Dot3adAggTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3adAggTable.setStatus("current")
_Dot3adAggEntry_Object = MibTableRow
dot3adAggEntry = _Dot3adAggEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1)
)
dot3adAggEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggEntry.setStatus("current")
_Dot3adAggIndex_Type = InterfaceIndex
_Dot3adAggIndex_Object = MibTableColumn
dot3adAggIndex = _Dot3adAggIndex_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 1),
    _Dot3adAggIndex_Type()
)
dot3adAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggIndex.setStatus("current")
_Dot3adAggMACAddress_Type = MacAddress
_Dot3adAggMACAddress_Object = MibTableColumn
dot3adAggMACAddress = _Dot3adAggMACAddress_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 2),
    _Dot3adAggMACAddress_Type()
)
dot3adAggMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggMACAddress.setStatus("current")


class _Dot3adAggActorSystemPriority_Type(Integer32):
    """Custom type dot3adAggActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggActorSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggActorSystemPriority_Object = MibTableColumn
dot3adAggActorSystemPriority = _Dot3adAggActorSystemPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 3),
    _Dot3adAggActorSystemPriority_Type()
)
dot3adAggActorSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggActorSystemPriority.setStatus("current")
_Dot3adAggActorSystemID_Type = MacAddress
_Dot3adAggActorSystemID_Object = MibTableColumn
dot3adAggActorSystemID = _Dot3adAggActorSystemID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 4),
    _Dot3adAggActorSystemID_Type()
)
dot3adAggActorSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggActorSystemID.setStatus("current")
_Dot3adAggAggregateOrIndividual_Type = TruthValue
_Dot3adAggAggregateOrIndividual_Object = MibTableColumn
dot3adAggAggregateOrIndividual = _Dot3adAggAggregateOrIndividual_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 5),
    _Dot3adAggAggregateOrIndividual_Type()
)
dot3adAggAggregateOrIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggAggregateOrIndividual.setStatus("current")
_Dot3adAggActorAdminKey_Type = LacpKey
_Dot3adAggActorAdminKey_Object = MibTableColumn
dot3adAggActorAdminKey = _Dot3adAggActorAdminKey_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 6),
    _Dot3adAggActorAdminKey_Type()
)
dot3adAggActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggActorAdminKey.setStatus("current")
_Dot3adAggActorOperKey_Type = LacpKey
_Dot3adAggActorOperKey_Object = MibTableColumn
dot3adAggActorOperKey = _Dot3adAggActorOperKey_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 7),
    _Dot3adAggActorOperKey_Type()
)
dot3adAggActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggActorOperKey.setStatus("current")
_Dot3adAggPartnerSystemID_Type = MacAddress
_Dot3adAggPartnerSystemID_Object = MibTableColumn
dot3adAggPartnerSystemID = _Dot3adAggPartnerSystemID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 8),
    _Dot3adAggPartnerSystemID_Type()
)
dot3adAggPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPartnerSystemID.setStatus("current")


class _Dot3adAggPartnerSystemPriority_Type(Integer32):
    """Custom type dot3adAggPartnerSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPartnerSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPartnerSystemPriority_Object = MibTableColumn
dot3adAggPartnerSystemPriority = _Dot3adAggPartnerSystemPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 9),
    _Dot3adAggPartnerSystemPriority_Type()
)
dot3adAggPartnerSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPartnerSystemPriority.setStatus("current")
_Dot3adAggPartnerOperKey_Type = LacpKey
_Dot3adAggPartnerOperKey_Object = MibTableColumn
dot3adAggPartnerOperKey = _Dot3adAggPartnerOperKey_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 10),
    _Dot3adAggPartnerOperKey_Type()
)
dot3adAggPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPartnerOperKey.setStatus("current")


class _Dot3adAggCollectorMaxDelay_Type(Integer32):
    """Custom type dot3adAggCollectorMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggCollectorMaxDelay_Type.__name__ = "Integer32"
_Dot3adAggCollectorMaxDelay_Object = MibTableColumn
dot3adAggCollectorMaxDelay = _Dot3adAggCollectorMaxDelay_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 11),
    _Dot3adAggCollectorMaxDelay_Type()
)
dot3adAggCollectorMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggCollectorMaxDelay.setStatus("current")
_Dot3adAggPortListTable_Object = MibTable
dot3adAggPortListTable = _Dot3adAggPortListTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot3adAggPortListTable.setStatus("current")
_Dot3adAggPortListEntry_Object = MibTableRow
dot3adAggPortListEntry = _Dot3adAggPortListEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 2, 1)
)
dot3adAggPortListEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortListEntry.setStatus("current")
_Dot3adAggPortListPorts_Type = PortList
_Dot3adAggPortListPorts_Object = MibTableColumn
dot3adAggPortListPorts = _Dot3adAggPortListPorts_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 2, 1, 1),
    _Dot3adAggPortListPorts_Type()
)
dot3adAggPortListPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortListPorts.setStatus("current")
_Dot3adAggXTable_Object = MibTable
dot3adAggXTable = _Dot3adAggXTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dot3adAggXTable.setStatus("current")
_Dot3adAggXEntry_Object = MibTableRow
dot3adAggXEntry = _Dot3adAggXEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot3adAggXEntry.setStatus("current")
_Dot3adAggDescription_Type = DisplayString
_Dot3adAggDescription_Object = MibTableColumn
dot3adAggDescription = _Dot3adAggDescription_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 1),
    _Dot3adAggDescription_Type()
)
dot3adAggDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggDescription.setStatus("current")
_Dot3adAggName_Type = DisplayString
_Dot3adAggName_Object = MibTableColumn
dot3adAggName = _Dot3adAggName_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 2),
    _Dot3adAggName_Type()
)
dot3adAggName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggName.setStatus("current")
_Dot3adAggAdminState_Type = AggState
_Dot3adAggAdminState_Object = MibTableColumn
dot3adAggAdminState = _Dot3adAggAdminState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 3),
    _Dot3adAggAdminState_Type()
)
dot3adAggAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggAdminState.setStatus("current")
_Dot3adAggOperState_Type = AggState
_Dot3adAggOperState_Object = MibTableColumn
dot3adAggOperState = _Dot3adAggOperState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 4),
    _Dot3adAggOperState_Type()
)
dot3adAggOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggOperState.setStatus("current")
_Dot3adAggTimeOfLastOperChange_Type = Integer32
_Dot3adAggTimeOfLastOperChange_Object = MibTableColumn
dot3adAggTimeOfLastOperChange = _Dot3adAggTimeOfLastOperChange_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 5),
    _Dot3adAggTimeOfLastOperChange_Type()
)
dot3adAggTimeOfLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggTimeOfLastOperChange.setStatus("current")
_Dot3adAggDataRate_Type = Integer32
_Dot3adAggDataRate_Object = MibTableColumn
dot3adAggDataRate = _Dot3adAggDataRate_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 6),
    _Dot3adAggDataRate_Type()
)
dot3adAggDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggDataRate.setStatus("current")
_Dot3adAggOctetsTxOK_Type = Counter64
_Dot3adAggOctetsTxOK_Object = MibTableColumn
dot3adAggOctetsTxOK = _Dot3adAggOctetsTxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 7),
    _Dot3adAggOctetsTxOK_Type()
)
dot3adAggOctetsTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggOctetsTxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggOctetsTxOK.setUnits("octets")
_Dot3adAggOctetsRxOK_Type = Counter64
_Dot3adAggOctetsRxOK_Object = MibTableColumn
dot3adAggOctetsRxOK = _Dot3adAggOctetsRxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 8),
    _Dot3adAggOctetsRxOK_Type()
)
dot3adAggOctetsRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggOctetsRxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggOctetsRxOK.setUnits("octets")
_Dot3adAggFramesTxOK_Type = Counter64
_Dot3adAggFramesTxOK_Object = MibTableColumn
dot3adAggFramesTxOK = _Dot3adAggFramesTxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 9),
    _Dot3adAggFramesTxOK_Type()
)
dot3adAggFramesTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggFramesTxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggFramesTxOK.setUnits("frames")
_Dot3adAggFramesRxOK_Type = Counter64
_Dot3adAggFramesRxOK_Object = MibTableColumn
dot3adAggFramesRxOK = _Dot3adAggFramesRxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 10),
    _Dot3adAggFramesRxOK_Type()
)
dot3adAggFramesRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggFramesRxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggFramesRxOK.setUnits("frames")
_Dot3adAggMulticastFramesTxOK_Type = Counter64
_Dot3adAggMulticastFramesTxOK_Object = MibTableColumn
dot3adAggMulticastFramesTxOK = _Dot3adAggMulticastFramesTxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 11),
    _Dot3adAggMulticastFramesTxOK_Type()
)
dot3adAggMulticastFramesTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggMulticastFramesTxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggMulticastFramesTxOK.setUnits("frames")
_Dot3adAggMulticastFramesRxOK_Type = Counter64
_Dot3adAggMulticastFramesRxOK_Object = MibTableColumn
dot3adAggMulticastFramesRxOK = _Dot3adAggMulticastFramesRxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 12),
    _Dot3adAggMulticastFramesRxOK_Type()
)
dot3adAggMulticastFramesRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggMulticastFramesRxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggMulticastFramesRxOK.setUnits("frames")
_Dot3adAggBroadcastFramesTxOK_Type = Counter64
_Dot3adAggBroadcastFramesTxOK_Object = MibTableColumn
dot3adAggBroadcastFramesTxOK = _Dot3adAggBroadcastFramesTxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 13),
    _Dot3adAggBroadcastFramesTxOK_Type()
)
dot3adAggBroadcastFramesTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggBroadcastFramesTxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggBroadcastFramesTxOK.setUnits("frames")
_Dot3adAggBroadcastFramesRxOK_Type = Counter64
_Dot3adAggBroadcastFramesRxOK_Object = MibTableColumn
dot3adAggBroadcastFramesRxOK = _Dot3adAggBroadcastFramesRxOK_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 14),
    _Dot3adAggBroadcastFramesRxOK_Type()
)
dot3adAggBroadcastFramesRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggBroadcastFramesRxOK.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggBroadcastFramesRxOK.setUnits("frames")
_Dot3adAggFramesDiscardedOnTx_Type = Counter64
_Dot3adAggFramesDiscardedOnTx_Object = MibTableColumn
dot3adAggFramesDiscardedOnTx = _Dot3adAggFramesDiscardedOnTx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 15),
    _Dot3adAggFramesDiscardedOnTx_Type()
)
dot3adAggFramesDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggFramesDiscardedOnTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggFramesDiscardedOnTx.setUnits("frames")
_Dot3adAggFramesDiscardedOnRx_Type = Counter64
_Dot3adAggFramesDiscardedOnRx_Object = MibTableColumn
dot3adAggFramesDiscardedOnRx = _Dot3adAggFramesDiscardedOnRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 16),
    _Dot3adAggFramesDiscardedOnRx_Type()
)
dot3adAggFramesDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggFramesDiscardedOnRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggFramesDiscardedOnRx.setUnits("frames")
_Dot3adAggFramesWithTxErrors_Type = Counter64
_Dot3adAggFramesWithTxErrors_Object = MibTableColumn
dot3adAggFramesWithTxErrors = _Dot3adAggFramesWithTxErrors_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 17),
    _Dot3adAggFramesWithTxErrors_Type()
)
dot3adAggFramesWithTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggFramesWithTxErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggFramesWithTxErrors.setUnits("frames")
_Dot3adAggFramesWithRxErrors_Type = Counter64
_Dot3adAggFramesWithRxErrors_Object = MibTableColumn
dot3adAggFramesWithRxErrors = _Dot3adAggFramesWithRxErrors_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 18),
    _Dot3adAggFramesWithRxErrors_Type()
)
dot3adAggFramesWithRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggFramesWithRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggFramesWithRxErrors.setUnits("frames")
_Dot3adAggUnknownProtocolFrames_Type = Counter64
_Dot3adAggUnknownProtocolFrames_Object = MibTableColumn
dot3adAggUnknownProtocolFrames = _Dot3adAggUnknownProtocolFrames_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 19),
    _Dot3adAggUnknownProtocolFrames_Type()
)
dot3adAggUnknownProtocolFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggUnknownProtocolFrames.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggUnknownProtocolFrames.setUnits("frames")


class _Dot3adAggLinkUpDownNotificationEnable_Type(Integer32):
    """Custom type dot3adAggLinkUpDownNotificationEnable based on Integer32"""
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


_Dot3adAggLinkUpDownNotificationEnable_Type.__name__ = "Integer32"
_Dot3adAggLinkUpDownNotificationEnable_Object = MibTableColumn
dot3adAggLinkUpDownNotificationEnable = _Dot3adAggLinkUpDownNotificationEnable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 20),
    _Dot3adAggLinkUpDownNotificationEnable_Type()
)
dot3adAggLinkUpDownNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggLinkUpDownNotificationEnable.setStatus("current")


class _Dot3adAggPortAlgorithm_Type(OctetString):
    """Custom type dot3adAggPortAlgorithm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot3adAggPortAlgorithm_Type.__name__ = "OctetString"
_Dot3adAggPortAlgorithm_Object = MibTableColumn
dot3adAggPortAlgorithm = _Dot3adAggPortAlgorithm_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 21),
    _Dot3adAggPortAlgorithm_Type()
)
dot3adAggPortAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortAlgorithm.setStatus("current")


class _Dot3adAggPartnerAdminPortAlgorithm_Type(OctetString):
    """Custom type dot3adAggPartnerAdminPortAlgorithm based on OctetString"""
    defaultHexValue = "0080C200"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot3adAggPartnerAdminPortAlgorithm_Type.__name__ = "OctetString"
_Dot3adAggPartnerAdminPortAlgorithm_Object = MibTableColumn
dot3adAggPartnerAdminPortAlgorithm = _Dot3adAggPartnerAdminPortAlgorithm_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 22),
    _Dot3adAggPartnerAdminPortAlgorithm_Type()
)
dot3adAggPartnerAdminPortAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPartnerAdminPortAlgorithm.setStatus("current")


class _Dot3adAggPartnerAdminPortConversationListDigest_Type(OctetString):
    """Custom type dot3adAggPartnerAdminPortConversationListDigest based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Dot3adAggPartnerAdminPortConversationListDigest_Type.__name__ = "OctetString"
_Dot3adAggPartnerAdminPortConversationListDigest_Object = MibTableColumn
dot3adAggPartnerAdminPortConversationListDigest = _Dot3adAggPartnerAdminPortConversationListDigest_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 23),
    _Dot3adAggPartnerAdminPortConversationListDigest_Type()
)
dot3adAggPartnerAdminPortConversationListDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPartnerAdminPortConversationListDigest.setStatus("current")
_Dot3adAggAdminDiscardWrongConversation_Type = TruthValue
_Dot3adAggAdminDiscardWrongConversation_Object = MibTableColumn
dot3adAggAdminDiscardWrongConversation = _Dot3adAggAdminDiscardWrongConversation_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 24),
    _Dot3adAggAdminDiscardWrongConversation_Type()
)
dot3adAggAdminDiscardWrongConversation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggAdminDiscardWrongConversation.setStatus("deprecated")


class _Dot3adAggPartnerAdminConvServiceMappingDigest_Type(OctetString):
    """Custom type dot3adAggPartnerAdminConvServiceMappingDigest based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Dot3adAggPartnerAdminConvServiceMappingDigest_Type.__name__ = "OctetString"
_Dot3adAggPartnerAdminConvServiceMappingDigest_Object = MibTableColumn
dot3adAggPartnerAdminConvServiceMappingDigest = _Dot3adAggPartnerAdminConvServiceMappingDigest_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 25),
    _Dot3adAggPartnerAdminConvServiceMappingDigest_Type()
)
dot3adAggPartnerAdminConvServiceMappingDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPartnerAdminConvServiceMappingDigest.setStatus("current")


class _Dot3adAggAdminDiscardWrongConversation2_Type(Integer32):
    """Custom type dot3adAggAdminDiscardWrongConversation2 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_Dot3adAggAdminDiscardWrongConversation2_Type.__name__ = "Integer32"
_Dot3adAggAdminDiscardWrongConversation2_Object = MibTableColumn
dot3adAggAdminDiscardWrongConversation2 = _Dot3adAggAdminDiscardWrongConversation2_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 3, 1, 26),
    _Dot3adAggAdminDiscardWrongConversation2_Type()
)
dot3adAggAdminDiscardWrongConversation2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggAdminDiscardWrongConversation2.setStatus("current")
_Dot3adAggConversationAdminLinkTable_Object = MibTable
dot3adAggConversationAdminLinkTable = _Dot3adAggConversationAdminLinkTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dot3adAggConversationAdminLinkTable.setStatus("current")
_Dot3adAggConversationAdminLinkEntry_Object = MibTableRow
dot3adAggConversationAdminLinkEntry = _Dot3adAggConversationAdminLinkEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 4, 1)
)
dot3adAggConversationAdminLinkEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggConversationAdminLinkId"),
    (0, "IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggConversationAdminLinkEntry.setStatus("current")


class _Dot3adAggConversationAdminLinkId_Type(Integer32):
    """Custom type dot3adAggConversationAdminLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Dot3adAggConversationAdminLinkId_Type.__name__ = "Integer32"
_Dot3adAggConversationAdminLinkId_Object = MibTableColumn
dot3adAggConversationAdminLinkId = _Dot3adAggConversationAdminLinkId_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 4, 1, 1),
    _Dot3adAggConversationAdminLinkId_Type()
)
dot3adAggConversationAdminLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggConversationAdminLinkId.setStatus("current")
_Dot3adAggConversationAdminLinkList_Type = OctetString
_Dot3adAggConversationAdminLinkList_Object = MibTableColumn
dot3adAggConversationAdminLinkList = _Dot3adAggConversationAdminLinkList_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 4, 1, 2),
    _Dot3adAggConversationAdminLinkList_Type()
)
dot3adAggConversationAdminLinkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggConversationAdminLinkList.setStatus("current")
_Dot3adAggAdminServiceConversationMapTable_Object = MibTable
dot3adAggAdminServiceConversationMapTable = _Dot3adAggAdminServiceConversationMapTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dot3adAggAdminServiceConversationMapTable.setStatus("current")
_Dot3adAggAdminServiceConversationMapEntry_Object = MibTableRow
dot3adAggAdminServiceConversationMapEntry = _Dot3adAggAdminServiceConversationMapEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 5, 1)
)
dot3adAggAdminServiceConversationMapEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggAdminServiceConversationMapId"),
    (0, "IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggAdminServiceConversationMapEntry.setStatus("current")


class _Dot3adAggAdminServiceConversationMapId_Type(Integer32):
    """Custom type dot3adAggAdminServiceConversationMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Dot3adAggAdminServiceConversationMapId_Type.__name__ = "Integer32"
_Dot3adAggAdminServiceConversationMapId_Object = MibTableColumn
dot3adAggAdminServiceConversationMapId = _Dot3adAggAdminServiceConversationMapId_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 5, 1, 1),
    _Dot3adAggAdminServiceConversationMapId_Type()
)
dot3adAggAdminServiceConversationMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggAdminServiceConversationMapId.setStatus("current")
_Dot3adAggAdminServiceConversationServiceIDList_Type = ServiceIdList
_Dot3adAggAdminServiceConversationServiceIDList_Object = MibTableColumn
dot3adAggAdminServiceConversationServiceIDList = _Dot3adAggAdminServiceConversationServiceIDList_Object(
    (1, 2, 840, 10006, 300, 43, 1, 1, 5, 1, 2),
    _Dot3adAggAdminServiceConversationServiceIDList_Type()
)
dot3adAggAdminServiceConversationServiceIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggAdminServiceConversationServiceIDList.setStatus("current")
_Dot3adAggPort_ObjectIdentity = ObjectIdentity
dot3adAggPort = _Dot3adAggPort_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 1, 2)
)
_Dot3adAggPortTable_Object = MibTable
dot3adAggPortTable = _Dot3adAggPortTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot3adAggPortTable.setStatus("current")
_Dot3adAggPortEntry_Object = MibTableRow
dot3adAggPortEntry = _Dot3adAggPortEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1)
)
dot3adAggPortEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortEntry.setStatus("current")
_Dot3adAggPortIndex_Type = InterfaceIndex
_Dot3adAggPortIndex_Object = MibTableColumn
dot3adAggPortIndex = _Dot3adAggPortIndex_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 1),
    _Dot3adAggPortIndex_Type()
)
dot3adAggPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggPortIndex.setStatus("current")


class _Dot3adAggPortActorSystemPriority_Type(Integer32):
    """Custom type dot3adAggPortActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortActorSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPortActorSystemPriority_Object = MibTableColumn
dot3adAggPortActorSystemPriority = _Dot3adAggPortActorSystemPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 2),
    _Dot3adAggPortActorSystemPriority_Type()
)
dot3adAggPortActorSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortActorSystemPriority.setStatus("current")
_Dot3adAggPortActorSystemID_Type = MacAddress
_Dot3adAggPortActorSystemID_Object = MibTableColumn
dot3adAggPortActorSystemID = _Dot3adAggPortActorSystemID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 3),
    _Dot3adAggPortActorSystemID_Type()
)
dot3adAggPortActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorSystemID.setStatus("current")
_Dot3adAggPortActorAdminKey_Type = LacpKey
_Dot3adAggPortActorAdminKey_Object = MibTableColumn
dot3adAggPortActorAdminKey = _Dot3adAggPortActorAdminKey_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 4),
    _Dot3adAggPortActorAdminKey_Type()
)
dot3adAggPortActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortActorAdminKey.setStatus("current")
_Dot3adAggPortActorOperKey_Type = LacpKey
_Dot3adAggPortActorOperKey_Object = MibTableColumn
dot3adAggPortActorOperKey = _Dot3adAggPortActorOperKey_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 5),
    _Dot3adAggPortActorOperKey_Type()
)
dot3adAggPortActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperKey.setStatus("current")


class _Dot3adAggPortPartnerAdminSystemPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerAdminSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerAdminSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerAdminSystemPriority_Object = MibTableColumn
dot3adAggPortPartnerAdminSystemPriority = _Dot3adAggPortPartnerAdminSystemPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 6),
    _Dot3adAggPortPartnerAdminSystemPriority_Type()
)
dot3adAggPortPartnerAdminSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminSystemPriority.setStatus("current")


class _Dot3adAggPortPartnerOperSystemPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerOperSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerOperSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerOperSystemPriority_Object = MibTableColumn
dot3adAggPortPartnerOperSystemPriority = _Dot3adAggPortPartnerOperSystemPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 7),
    _Dot3adAggPortPartnerOperSystemPriority_Type()
)
dot3adAggPortPartnerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperSystemPriority.setStatus("current")
_Dot3adAggPortPartnerAdminSystemID_Type = MacAddress
_Dot3adAggPortPartnerAdminSystemID_Object = MibTableColumn
dot3adAggPortPartnerAdminSystemID = _Dot3adAggPortPartnerAdminSystemID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 8),
    _Dot3adAggPortPartnerAdminSystemID_Type()
)
dot3adAggPortPartnerAdminSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminSystemID.setStatus("current")
_Dot3adAggPortPartnerOperSystemID_Type = MacAddress
_Dot3adAggPortPartnerOperSystemID_Object = MibTableColumn
dot3adAggPortPartnerOperSystemID = _Dot3adAggPortPartnerOperSystemID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 9),
    _Dot3adAggPortPartnerOperSystemID_Type()
)
dot3adAggPortPartnerOperSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperSystemID.setStatus("current")
_Dot3adAggPortPartnerAdminKey_Type = LacpKey
_Dot3adAggPortPartnerAdminKey_Object = MibTableColumn
dot3adAggPortPartnerAdminKey = _Dot3adAggPortPartnerAdminKey_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 10),
    _Dot3adAggPortPartnerAdminKey_Type()
)
dot3adAggPortPartnerAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminKey.setStatus("current")
_Dot3adAggPortPartnerOperKey_Type = LacpKey
_Dot3adAggPortPartnerOperKey_Object = MibTableColumn
dot3adAggPortPartnerOperKey = _Dot3adAggPortPartnerOperKey_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 11),
    _Dot3adAggPortPartnerOperKey_Type()
)
dot3adAggPortPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperKey.setStatus("current")
_Dot3adAggPortSelectedAggID_Type = InterfaceIndex
_Dot3adAggPortSelectedAggID_Object = MibTableColumn
dot3adAggPortSelectedAggID = _Dot3adAggPortSelectedAggID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 12),
    _Dot3adAggPortSelectedAggID_Type()
)
dot3adAggPortSelectedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortSelectedAggID.setStatus("current")
_Dot3adAggPortAttachedAggID_Type = InterfaceIndex
_Dot3adAggPortAttachedAggID_Object = MibTableColumn
dot3adAggPortAttachedAggID = _Dot3adAggPortAttachedAggID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 13),
    _Dot3adAggPortAttachedAggID_Type()
)
dot3adAggPortAttachedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortAttachedAggID.setStatus("current")


class _Dot3adAggPortActorPort_Type(Integer32):
    """Custom type dot3adAggPortActorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortActorPort_Type.__name__ = "Integer32"
_Dot3adAggPortActorPort_Object = MibTableColumn
dot3adAggPortActorPort = _Dot3adAggPortActorPort_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 14),
    _Dot3adAggPortActorPort_Type()
)
dot3adAggPortActorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorPort.setStatus("current")


class _Dot3adAggPortActorPortPriority_Type(Integer32):
    """Custom type dot3adAggPortActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortActorPortPriority_Type.__name__ = "Integer32"
_Dot3adAggPortActorPortPriority_Object = MibTableColumn
dot3adAggPortActorPortPriority = _Dot3adAggPortActorPortPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 15),
    _Dot3adAggPortActorPortPriority_Type()
)
dot3adAggPortActorPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortActorPortPriority.setStatus("current")


class _Dot3adAggPortPartnerAdminPort_Type(Integer32):
    """Custom type dot3adAggPortPartnerAdminPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerAdminPort_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerAdminPort_Object = MibTableColumn
dot3adAggPortPartnerAdminPort = _Dot3adAggPortPartnerAdminPort_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 16),
    _Dot3adAggPortPartnerAdminPort_Type()
)
dot3adAggPortPartnerAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminPort.setStatus("current")


class _Dot3adAggPortPartnerOperPort_Type(Integer32):
    """Custom type dot3adAggPortPartnerOperPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerOperPort_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerOperPort_Object = MibTableColumn
dot3adAggPortPartnerOperPort = _Dot3adAggPortPartnerOperPort_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 17),
    _Dot3adAggPortPartnerOperPort_Type()
)
dot3adAggPortPartnerOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperPort.setStatus("current")


class _Dot3adAggPortPartnerAdminPortPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerAdminPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerAdminPortPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerAdminPortPriority_Object = MibTableColumn
dot3adAggPortPartnerAdminPortPriority = _Dot3adAggPortPartnerAdminPortPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 18),
    _Dot3adAggPortPartnerAdminPortPriority_Type()
)
dot3adAggPortPartnerAdminPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminPortPriority.setStatus("current")


class _Dot3adAggPortPartnerOperPortPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerOperPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerOperPortPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerOperPortPriority_Object = MibTableColumn
dot3adAggPortPartnerOperPortPriority = _Dot3adAggPortPartnerOperPortPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 19),
    _Dot3adAggPortPartnerOperPortPriority_Type()
)
dot3adAggPortPartnerOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperPortPriority.setStatus("current")
_Dot3adAggPortActorAdminState_Type = LacpState
_Dot3adAggPortActorAdminState_Object = MibTableColumn
dot3adAggPortActorAdminState = _Dot3adAggPortActorAdminState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 20),
    _Dot3adAggPortActorAdminState_Type()
)
dot3adAggPortActorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortActorAdminState.setStatus("current")
_Dot3adAggPortActorOperState_Type = LacpState
_Dot3adAggPortActorOperState_Object = MibTableColumn
dot3adAggPortActorOperState = _Dot3adAggPortActorOperState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 21),
    _Dot3adAggPortActorOperState_Type()
)
dot3adAggPortActorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperState.setStatus("current")
_Dot3adAggPortPartnerAdminState_Type = LacpState
_Dot3adAggPortPartnerAdminState_Object = MibTableColumn
dot3adAggPortPartnerAdminState = _Dot3adAggPortPartnerAdminState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 22),
    _Dot3adAggPortPartnerAdminState_Type()
)
dot3adAggPortPartnerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminState.setStatus("current")
_Dot3adAggPortPartnerOperState_Type = LacpState
_Dot3adAggPortPartnerOperState_Object = MibTableColumn
dot3adAggPortPartnerOperState = _Dot3adAggPortPartnerOperState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 23),
    _Dot3adAggPortPartnerOperState_Type()
)
dot3adAggPortPartnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperState.setStatus("current")
_Dot3adAggPortAggregateOrIndividual_Type = TruthValue
_Dot3adAggPortAggregateOrIndividual_Object = MibTableColumn
dot3adAggPortAggregateOrIndividual = _Dot3adAggPortAggregateOrIndividual_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 24),
    _Dot3adAggPortAggregateOrIndividual_Type()
)
dot3adAggPortAggregateOrIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortAggregateOrIndividual.setStatus("current")
_Dot3adAggPortStatsTable_Object = MibTable
dot3adAggPortStatsTable = _Dot3adAggPortStatsTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot3adAggPortStatsTable.setStatus("current")
_Dot3adAggPortStatsEntry_Object = MibTableRow
dot3adAggPortStatsEntry = _Dot3adAggPortStatsEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1)
)
dot3adAggPortStatsEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortStatsEntry.setStatus("current")
_Dot3adAggPortStatsLACPDUsRx_Type = Counter32
_Dot3adAggPortStatsLACPDUsRx_Object = MibTableColumn
dot3adAggPortStatsLACPDUsRx = _Dot3adAggPortStatsLACPDUsRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 1),
    _Dot3adAggPortStatsLACPDUsRx_Type()
)
dot3adAggPortStatsLACPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsLACPDUsRx.setStatus("current")
_Dot3adAggPortStatsMarkerPDUsRx_Type = Counter32
_Dot3adAggPortStatsMarkerPDUsRx_Object = MibTableColumn
dot3adAggPortStatsMarkerPDUsRx = _Dot3adAggPortStatsMarkerPDUsRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 2),
    _Dot3adAggPortStatsMarkerPDUsRx_Type()
)
dot3adAggPortStatsMarkerPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerPDUsRx.setStatus("current")
_Dot3adAggPortStatsMarkerResponsePDUsRx_Type = Counter32
_Dot3adAggPortStatsMarkerResponsePDUsRx_Object = MibTableColumn
dot3adAggPortStatsMarkerResponsePDUsRx = _Dot3adAggPortStatsMarkerResponsePDUsRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 3),
    _Dot3adAggPortStatsMarkerResponsePDUsRx_Type()
)
dot3adAggPortStatsMarkerResponsePDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerResponsePDUsRx.setStatus("current")
_Dot3adAggPortStatsUnknownRx_Type = Counter32
_Dot3adAggPortStatsUnknownRx_Object = MibTableColumn
dot3adAggPortStatsUnknownRx = _Dot3adAggPortStatsUnknownRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 4),
    _Dot3adAggPortStatsUnknownRx_Type()
)
dot3adAggPortStatsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsUnknownRx.setStatus("current")
_Dot3adAggPortStatsIllegalRx_Type = Counter32
_Dot3adAggPortStatsIllegalRx_Object = MibTableColumn
dot3adAggPortStatsIllegalRx = _Dot3adAggPortStatsIllegalRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 5),
    _Dot3adAggPortStatsIllegalRx_Type()
)
dot3adAggPortStatsIllegalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsIllegalRx.setStatus("current")
_Dot3adAggPortStatsLACPDUsTx_Type = Counter32
_Dot3adAggPortStatsLACPDUsTx_Object = MibTableColumn
dot3adAggPortStatsLACPDUsTx = _Dot3adAggPortStatsLACPDUsTx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 6),
    _Dot3adAggPortStatsLACPDUsTx_Type()
)
dot3adAggPortStatsLACPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsLACPDUsTx.setStatus("current")
_Dot3adAggPortStatsMarkerPDUsTx_Type = Counter32
_Dot3adAggPortStatsMarkerPDUsTx_Object = MibTableColumn
dot3adAggPortStatsMarkerPDUsTx = _Dot3adAggPortStatsMarkerPDUsTx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 7),
    _Dot3adAggPortStatsMarkerPDUsTx_Type()
)
dot3adAggPortStatsMarkerPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerPDUsTx.setStatus("current")
_Dot3adAggPortStatsMarkerResponsePDUsTx_Type = Counter32
_Dot3adAggPortStatsMarkerResponsePDUsTx_Object = MibTableColumn
dot3adAggPortStatsMarkerResponsePDUsTx = _Dot3adAggPortStatsMarkerResponsePDUsTx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 8),
    _Dot3adAggPortStatsMarkerResponsePDUsTx_Type()
)
dot3adAggPortStatsMarkerResponsePDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerResponsePDUsTx.setStatus("current")
_Dot3adAggPortDebugTable_Object = MibTable
dot3adAggPortDebugTable = _Dot3adAggPortDebugTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugTable.setStatus("current")
_Dot3adAggPortDebugEntry_Object = MibTableRow
dot3adAggPortDebugEntry = _Dot3adAggPortDebugEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1)
)
dot3adAggPortDebugEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugEntry.setStatus("current")


class _Dot3adAggPortDebugRxState_Type(Integer32):
    """Custom type dot3adAggPortDebugRxState based on Integer32"""
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
        *(("currentRx", 1),
          ("defaulted", 3),
          ("expired", 2),
          ("initialize", 4),
          ("lacpDisabled", 5),
          ("portDisabled", 6))
    )


_Dot3adAggPortDebugRxState_Type.__name__ = "Integer32"
_Dot3adAggPortDebugRxState_Object = MibTableColumn
dot3adAggPortDebugRxState = _Dot3adAggPortDebugRxState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 1),
    _Dot3adAggPortDebugRxState_Type()
)
dot3adAggPortDebugRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugRxState.setStatus("current")
_Dot3adAggPortDebugLastRxTime_Type = TimeTicks
_Dot3adAggPortDebugLastRxTime_Object = MibTableColumn
dot3adAggPortDebugLastRxTime = _Dot3adAggPortDebugLastRxTime_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 2),
    _Dot3adAggPortDebugLastRxTime_Type()
)
dot3adAggPortDebugLastRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugLastRxTime.setStatus("current")


class _Dot3adAggPortDebugMuxState_Type(Integer32):
    """Custom type dot3adAggPortDebugMuxState based on Integer32"""
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
        *(("attached", 3),
          ("collecting", 4),
          ("collectingDistributing", 6),
          ("detached", 1),
          ("distributing", 5),
          ("waiting", 2))
    )


_Dot3adAggPortDebugMuxState_Type.__name__ = "Integer32"
_Dot3adAggPortDebugMuxState_Object = MibTableColumn
dot3adAggPortDebugMuxState = _Dot3adAggPortDebugMuxState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 3),
    _Dot3adAggPortDebugMuxState_Type()
)
dot3adAggPortDebugMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugMuxState.setStatus("current")
_Dot3adAggPortDebugMuxReason_Type = DisplayString
_Dot3adAggPortDebugMuxReason_Object = MibTableColumn
dot3adAggPortDebugMuxReason = _Dot3adAggPortDebugMuxReason_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 4),
    _Dot3adAggPortDebugMuxReason_Type()
)
dot3adAggPortDebugMuxReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugMuxReason.setStatus("current")
_Dot3adAggPortDebugActorChurnState_Type = ChurnState
_Dot3adAggPortDebugActorChurnState_Object = MibTableColumn
dot3adAggPortDebugActorChurnState = _Dot3adAggPortDebugActorChurnState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 5),
    _Dot3adAggPortDebugActorChurnState_Type()
)
dot3adAggPortDebugActorChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorChurnState.setStatus("current")
_Dot3adAggPortDebugPartnerChurnState_Type = ChurnState
_Dot3adAggPortDebugPartnerChurnState_Object = MibTableColumn
dot3adAggPortDebugPartnerChurnState = _Dot3adAggPortDebugPartnerChurnState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 6),
    _Dot3adAggPortDebugPartnerChurnState_Type()
)
dot3adAggPortDebugPartnerChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerChurnState.setStatus("current")
_Dot3adAggPortDebugActorChurnCount_Type = Counter32
_Dot3adAggPortDebugActorChurnCount_Object = MibTableColumn
dot3adAggPortDebugActorChurnCount = _Dot3adAggPortDebugActorChurnCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 7),
    _Dot3adAggPortDebugActorChurnCount_Type()
)
dot3adAggPortDebugActorChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorChurnCount.setStatus("current")
_Dot3adAggPortDebugPartnerChurnCount_Type = Counter32
_Dot3adAggPortDebugPartnerChurnCount_Object = MibTableColumn
dot3adAggPortDebugPartnerChurnCount = _Dot3adAggPortDebugPartnerChurnCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 8),
    _Dot3adAggPortDebugPartnerChurnCount_Type()
)
dot3adAggPortDebugPartnerChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerChurnCount.setStatus("current")
_Dot3adAggPortDebugActorSyncTransitionCount_Type = Counter32
_Dot3adAggPortDebugActorSyncTransitionCount_Object = MibTableColumn
dot3adAggPortDebugActorSyncTransitionCount = _Dot3adAggPortDebugActorSyncTransitionCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 9),
    _Dot3adAggPortDebugActorSyncTransitionCount_Type()
)
dot3adAggPortDebugActorSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorSyncTransitionCount.setStatus("current")
_Dot3adAggPortDebugPartnerSyncTransitionCount_Type = Counter32
_Dot3adAggPortDebugPartnerSyncTransitionCount_Object = MibTableColumn
dot3adAggPortDebugPartnerSyncTransitionCount = _Dot3adAggPortDebugPartnerSyncTransitionCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 10),
    _Dot3adAggPortDebugPartnerSyncTransitionCount_Type()
)
dot3adAggPortDebugPartnerSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerSyncTransitionCount.setStatus("current")
_Dot3adAggPortDebugActorChangeCount_Type = Counter32
_Dot3adAggPortDebugActorChangeCount_Object = MibTableColumn
dot3adAggPortDebugActorChangeCount = _Dot3adAggPortDebugActorChangeCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 11),
    _Dot3adAggPortDebugActorChangeCount_Type()
)
dot3adAggPortDebugActorChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorChangeCount.setStatus("current")
_Dot3adAggPortDebugPartnerChangeCount_Type = Counter32
_Dot3adAggPortDebugPartnerChangeCount_Object = MibTableColumn
dot3adAggPortDebugPartnerChangeCount = _Dot3adAggPortDebugPartnerChangeCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 12),
    _Dot3adAggPortDebugPartnerChangeCount_Type()
)
dot3adAggPortDebugPartnerChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerChangeCount.setStatus("current")
_Dot3adAggPortXTable_Object = MibTable
dot3adAggPortXTable = _Dot3adAggPortXTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dot3adAggPortXTable.setStatus("current")
_Dot3adAggPortXEntry_Object = MibTableRow
dot3adAggPortXEntry = _Dot3adAggPortXEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dot3adAggPortXEntry.setStatus("current")


class _Dot3adAggPortProtocolDA_Type(MacAddress):
    """Custom type dot3adAggPortProtocolDA based on MacAddress"""
    defaultHexValue = "0180C2000002"


_Dot3adAggPortProtocolDA_Object = MibTableColumn
dot3adAggPortProtocolDA = _Dot3adAggPortProtocolDA_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 4, 1, 1),
    _Dot3adAggPortProtocolDA_Type()
)
dot3adAggPortProtocolDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortProtocolDA.setStatus("current")
_Dot3adAggPortSecondXTable_Object = MibTable
dot3adAggPortSecondXTable = _Dot3adAggPortSecondXTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5)
)
if mibBuilder.loadTexts:
    dot3adAggPortSecondXTable.setStatus("current")
_Dot3adAggPortSecondXEntry_Object = MibTableRow
dot3adAggPortSecondXEntry = _Dot3adAggPortSecondXEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    dot3adAggPortSecondXEntry.setStatus("current")


class _Dot3adAggPortOperConversationPasses_Type(OctetString):
    """Custom type dot3adAggPortOperConversationPasses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_Dot3adAggPortOperConversationPasses_Type.__name__ = "OctetString"
_Dot3adAggPortOperConversationPasses_Object = MibTableColumn
dot3adAggPortOperConversationPasses = _Dot3adAggPortOperConversationPasses_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5, 1, 1),
    _Dot3adAggPortOperConversationPasses_Type()
)
dot3adAggPortOperConversationPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortOperConversationPasses.setStatus("current")


class _Dot3adAggPortOperConversationCollected_Type(OctetString):
    """Custom type dot3adAggPortOperConversationCollected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_Dot3adAggPortOperConversationCollected_Type.__name__ = "OctetString"
_Dot3adAggPortOperConversationCollected_Object = MibTableColumn
dot3adAggPortOperConversationCollected = _Dot3adAggPortOperConversationCollected_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5, 1, 2),
    _Dot3adAggPortOperConversationCollected_Type()
)
dot3adAggPortOperConversationCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortOperConversationCollected.setStatus("current")


class _Dot3adAggPortLinkNumberId_Type(Integer32):
    """Custom type dot3adAggPortLinkNumberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortLinkNumberId_Type.__name__ = "Integer32"
_Dot3adAggPortLinkNumberId_Object = MibTableColumn
dot3adAggPortLinkNumberId = _Dot3adAggPortLinkNumberId_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5, 1, 3),
    _Dot3adAggPortLinkNumberId_Type()
)
dot3adAggPortLinkNumberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortLinkNumberId.setStatus("current")


class _Dot3adAggPortPartnerAdminLinkNumberId_Type(Integer32):
    """Custom type dot3adAggPortPartnerAdminLinkNumberId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerAdminLinkNumberId_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerAdminLinkNumberId_Object = MibTableColumn
dot3adAggPortPartnerAdminLinkNumberId = _Dot3adAggPortPartnerAdminLinkNumberId_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5, 1, 4),
    _Dot3adAggPortPartnerAdminLinkNumberId_Type()
)
dot3adAggPortPartnerAdminLinkNumberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminLinkNumberId.setStatus("deprecated")


class _Dot3adAggPortWTRTime_Type(Integer32):
    """Custom type dot3adAggPortWTRTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 12),
        ValueRangeConstraint(100, 100),
    )


_Dot3adAggPortWTRTime_Type.__name__ = "Integer32"
_Dot3adAggPortWTRTime_Object = MibTableColumn
dot3adAggPortWTRTime = _Dot3adAggPortWTRTime_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5, 1, 5),
    _Dot3adAggPortWTRTime_Type()
)
dot3adAggPortWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortWTRTime.setStatus("current")


class _Dot3adAggPortEnableLongPDUXmit_Type(TruthValue):
    """Custom type dot3adAggPortEnableLongPDUXmit based on TruthValue"""


_Dot3adAggPortEnableLongPDUXmit_Object = MibTableColumn
dot3adAggPortEnableLongPDUXmit = _Dot3adAggPortEnableLongPDUXmit_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 5, 1, 6),
    _Dot3adAggPortEnableLongPDUXmit_Type()
)
dot3adAggPortEnableLongPDUXmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortEnableLongPDUXmit.setStatus("current")
_Dot3adAggPortDebugXTable_Object = MibTable
dot3adAggPortDebugXTable = _Dot3adAggPortDebugXTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 6)
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugXTable.setStatus("current")
_Dot3adAggPortDebugXEntry_Object = MibTableRow
dot3adAggPortDebugXEntry = _Dot3adAggPortDebugXEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugXEntry.setStatus("current")
_Dot3adAggPortDebugActorCDSChurnState_Type = ChurnState
_Dot3adAggPortDebugActorCDSChurnState_Object = MibTableColumn
dot3adAggPortDebugActorCDSChurnState = _Dot3adAggPortDebugActorCDSChurnState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 6, 1, 1),
    _Dot3adAggPortDebugActorCDSChurnState_Type()
)
dot3adAggPortDebugActorCDSChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorCDSChurnState.setStatus("current")
_Dot3adAggPortDebugPartnerCDSChurnState_Type = ChurnState
_Dot3adAggPortDebugPartnerCDSChurnState_Object = MibTableColumn
dot3adAggPortDebugPartnerCDSChurnState = _Dot3adAggPortDebugPartnerCDSChurnState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 6, 1, 2),
    _Dot3adAggPortDebugPartnerCDSChurnState_Type()
)
dot3adAggPortDebugPartnerCDSChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerCDSChurnState.setStatus("current")
_Dot3adAggPortDebugActorCDSChurnCount_Type = Counter64
_Dot3adAggPortDebugActorCDSChurnCount_Object = MibTableColumn
dot3adAggPortDebugActorCDSChurnCount = _Dot3adAggPortDebugActorCDSChurnCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 6, 1, 3),
    _Dot3adAggPortDebugActorCDSChurnCount_Type()
)
dot3adAggPortDebugActorCDSChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorCDSChurnCount.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorCDSChurnCount.setUnits("times entered ACTOR_CDS_CHURN")
_Dot3adAggPortDebugPartnerCDSChurnCount_Type = Counter64
_Dot3adAggPortDebugPartnerCDSChurnCount_Object = MibTableColumn
dot3adAggPortDebugPartnerCDSChurnCount = _Dot3adAggPortDebugPartnerCDSChurnCount_Object(
    (1, 2, 840, 10006, 300, 43, 1, 2, 6, 1, 4),
    _Dot3adAggPortDebugPartnerCDSChurnCount_Type()
)
dot3adAggPortDebugPartnerCDSChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerCDSChurnCount.setStatus("current")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerCDSChurnCount.setUnits("times entered PARTNER_CDS_CHURN")
_Dot3adTablesLastChanged_Type = TimeTicks
_Dot3adTablesLastChanged_Object = MibScalar
dot3adTablesLastChanged = _Dot3adTablesLastChanged_Object(
    (1, 2, 840, 10006, 300, 43, 1, 3),
    _Dot3adTablesLastChanged_Type()
)
dot3adTablesLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adTablesLastChanged.setStatus("current")
_Dot3adDrni_ObjectIdentity = ObjectIdentity
dot3adDrni = _Dot3adDrni_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 1, 4)
)
_Dot3adDrniTable_Object = MibTable
dot3adDrniTable = _Dot3adDrniTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot3adDrniTable.setStatus("current")
_Dot3adDrniEntry_Object = MibTableRow
dot3adDrniEntry = _Dot3adDrniEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1)
)
dot3adDrniEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adDrniIndex"),
)
if mibBuilder.loadTexts:
    dot3adDrniEntry.setStatus("current")
_Dot3adDrniIndex_Type = InterfaceIndex
_Dot3adDrniIndex_Object = MibTableColumn
dot3adDrniIndex = _Dot3adDrniIndex_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 1),
    _Dot3adDrniIndex_Type()
)
dot3adDrniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adDrniIndex.setStatus("current")
_Dot3adDrniDescription_Type = SnmpAdminString
_Dot3adDrniDescription_Object = MibTableColumn
dot3adDrniDescription = _Dot3adDrniDescription_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 2),
    _Dot3adDrniDescription_Type()
)
dot3adDrniDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adDrniDescription.setStatus("current")
_Dot3adDrniName_Type = SnmpAdminString
_Dot3adDrniName_Object = MibTableColumn
dot3adDrniName = _Dot3adDrniName_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 3),
    _Dot3adDrniName_Type()
)
dot3adDrniName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniName.setStatus("current")
_Dot3adDrniPortalAddr_Type = MacAddress
_Dot3adDrniPortalAddr_Object = MibTableColumn
dot3adDrniPortalAddr = _Dot3adDrniPortalAddr_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 4),
    _Dot3adDrniPortalAddr_Type()
)
dot3adDrniPortalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniPortalAddr.setStatus("current")
_Dot3adDrniPortalPriority_Type = Integer32
_Dot3adDrniPortalPriority_Object = MibTableColumn
dot3adDrniPortalPriority = _Dot3adDrniPortalPriority_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 5),
    _Dot3adDrniPortalPriority_Type()
)
dot3adDrniPortalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniPortalPriority.setStatus("current")
_Dot3adDrniThreePortalSystem_Type = TruthValue
_Dot3adDrniThreePortalSystem_Object = MibTableColumn
dot3adDrniThreePortalSystem = _Dot3adDrniThreePortalSystem_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 6),
    _Dot3adDrniThreePortalSystem_Type()
)
dot3adDrniThreePortalSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniThreePortalSystem.setStatus("current")


class _Dot3adDrniPortalSystemNumber_Type(Integer32):
    """Custom type dot3adDrniPortalSystemNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Dot3adDrniPortalSystemNumber_Type.__name__ = "Integer32"
_Dot3adDrniPortalSystemNumber_Object = MibTableColumn
dot3adDrniPortalSystemNumber = _Dot3adDrniPortalSystemNumber_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 7),
    _Dot3adDrniPortalSystemNumber_Type()
)
dot3adDrniPortalSystemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniPortalSystemNumber.setStatus("current")
_Dot3adDrniIntraPortalLinkList_Type = PortalLinkList
_Dot3adDrniIntraPortalLinkList_Object = MibTableColumn
dot3adDrniIntraPortalLinkList = _Dot3adDrniIntraPortalLinkList_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 8),
    _Dot3adDrniIntraPortalLinkList_Type()
)
dot3adDrniIntraPortalLinkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniIntraPortalLinkList.setStatus("current")
_Dot3adDrniAggregator_Type = InterfaceIndex
_Dot3adDrniAggregator_Object = MibTableColumn
dot3adDrniAggregator = _Dot3adDrniAggregator_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 9),
    _Dot3adDrniAggregator_Type()
)
dot3adDrniAggregator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniAggregator.setStatus("current")


class _Dot3adDrniNeighborAdminConvGatewayListDigest_Type(OctetString):
    """Custom type dot3adDrniNeighborAdminConvGatewayListDigest based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Dot3adDrniNeighborAdminConvGatewayListDigest_Type.__name__ = "OctetString"
_Dot3adDrniNeighborAdminConvGatewayListDigest_Object = MibTableColumn
dot3adDrniNeighborAdminConvGatewayListDigest = _Dot3adDrniNeighborAdminConvGatewayListDigest_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 10),
    _Dot3adDrniNeighborAdminConvGatewayListDigest_Type()
)
dot3adDrniNeighborAdminConvGatewayListDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniNeighborAdminConvGatewayListDigest.setStatus("current")


class _Dot3adDrniNeighborAdminConvPortListDigest_Type(OctetString):
    """Custom type dot3adDrniNeighborAdminConvPortListDigest based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Dot3adDrniNeighborAdminConvPortListDigest_Type.__name__ = "OctetString"
_Dot3adDrniNeighborAdminConvPortListDigest_Object = MibTableColumn
dot3adDrniNeighborAdminConvPortListDigest = _Dot3adDrniNeighborAdminConvPortListDigest_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 11),
    _Dot3adDrniNeighborAdminConvPortListDigest_Type()
)
dot3adDrniNeighborAdminConvPortListDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniNeighborAdminConvPortListDigest.setStatus("current")


class _Dot3adDrniGatewayAlgorithm_Type(OctetString):
    """Custom type dot3adDrniGatewayAlgorithm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot3adDrniGatewayAlgorithm_Type.__name__ = "OctetString"
_Dot3adDrniGatewayAlgorithm_Object = MibTableColumn
dot3adDrniGatewayAlgorithm = _Dot3adDrniGatewayAlgorithm_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 12),
    _Dot3adDrniGatewayAlgorithm_Type()
)
dot3adDrniGatewayAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniGatewayAlgorithm.setStatus("current")


class _Dot3adDrniNeighborAdminGatewayAlgorithm_Type(OctetString):
    """Custom type dot3adDrniNeighborAdminGatewayAlgorithm based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Dot3adDrniNeighborAdminGatewayAlgorithm_Type.__name__ = "OctetString"
_Dot3adDrniNeighborAdminGatewayAlgorithm_Object = MibTableColumn
dot3adDrniNeighborAdminGatewayAlgorithm = _Dot3adDrniNeighborAdminGatewayAlgorithm_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 13),
    _Dot3adDrniNeighborAdminGatewayAlgorithm_Type()
)
dot3adDrniNeighborAdminGatewayAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniNeighborAdminGatewayAlgorithm.setStatus("current")


class _Dot3adDrniNeighborAdminPortAlgorithm_Type(OctetString):
    """Custom type dot3adDrniNeighborAdminPortAlgorithm based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Dot3adDrniNeighborAdminPortAlgorithm_Type.__name__ = "OctetString"
_Dot3adDrniNeighborAdminPortAlgorithm_Object = MibTableColumn
dot3adDrniNeighborAdminPortAlgorithm = _Dot3adDrniNeighborAdminPortAlgorithm_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 14),
    _Dot3adDrniNeighborAdminPortAlgorithm_Type()
)
dot3adDrniNeighborAdminPortAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniNeighborAdminPortAlgorithm.setStatus("current")
_Dot3adDrniNeighborAdminDRCPState_Type = DrcpState
_Dot3adDrniNeighborAdminDRCPState_Object = MibTableColumn
dot3adDrniNeighborAdminDRCPState = _Dot3adDrniNeighborAdminDRCPState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 15),
    _Dot3adDrniNeighborAdminDRCPState_Type()
)
dot3adDrniNeighborAdminDRCPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniNeighborAdminDRCPState.setStatus("current")


class _Dot3adDrniEncapsulationMethod_Type(OctetString):
    """Custom type dot3adDrniEncapsulationMethod based on OctetString"""
    defaultHexValue = "0080C200"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot3adDrniEncapsulationMethod_Type.__name__ = "OctetString"
_Dot3adDrniEncapsulationMethod_Object = MibTableColumn
dot3adDrniEncapsulationMethod = _Dot3adDrniEncapsulationMethod_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 16),
    _Dot3adDrniEncapsulationMethod_Type()
)
dot3adDrniEncapsulationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniEncapsulationMethod.setStatus("current")


class _Dot3adDrniDRPortConversationPasses_Type(OctetString):
    """Custom type dot3adDrniDRPortConversationPasses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_Dot3adDrniDRPortConversationPasses_Type.__name__ = "OctetString"
_Dot3adDrniDRPortConversationPasses_Object = MibTableColumn
dot3adDrniDRPortConversationPasses = _Dot3adDrniDRPortConversationPasses_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 17),
    _Dot3adDrniDRPortConversationPasses_Type()
)
dot3adDrniDRPortConversationPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adDrniDRPortConversationPasses.setStatus("current")


class _Dot3adDrniDRGatewayConversationPasses_Type(OctetString):
    """Custom type dot3adDrniDRGatewayConversationPasses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_Dot3adDrniDRGatewayConversationPasses_Type.__name__ = "OctetString"
_Dot3adDrniDRGatewayConversationPasses_Object = MibTableColumn
dot3adDrniDRGatewayConversationPasses = _Dot3adDrniDRGatewayConversationPasses_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 18),
    _Dot3adDrniDRGatewayConversationPasses_Type()
)
dot3adDrniDRGatewayConversationPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adDrniDRGatewayConversationPasses.setStatus("current")
_Dot3adDrniPSI_Type = TruthValue
_Dot3adDrniPSI_Object = MibTableColumn
dot3adDrniPSI = _Dot3adDrniPSI_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 19),
    _Dot3adDrniPSI_Type()
)
dot3adDrniPSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adDrniPSI.setStatus("current")


class _Dot3adDrniPortConversationControl_Type(TruthValue):
    """Custom type dot3adDrniPortConversationControl based on TruthValue"""


_Dot3adDrniPortConversationControl_Object = MibTableColumn
dot3adDrniPortConversationControl = _Dot3adDrniPortConversationControl_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 20),
    _Dot3adDrniPortConversationControl_Type()
)
dot3adDrniPortConversationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniPortConversationControl.setStatus("current")


class _Dot3adDrniIntraPortalPortProtocolDA_Type(MacAddress):
    """Custom type dot3adDrniIntraPortalPortProtocolDA based on MacAddress"""
    defaultHexValue = "0180C2000003"


_Dot3adDrniIntraPortalPortProtocolDA_Object = MibTableColumn
dot3adDrniIntraPortalPortProtocolDA = _Dot3adDrniIntraPortalPortProtocolDA_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 1, 1, 21),
    _Dot3adDrniIntraPortalPortProtocolDA_Type()
)
dot3adDrniIntraPortalPortProtocolDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniIntraPortalPortProtocolDA.setStatus("current")
_Dot3adDrniConvAdminGatewayTable_Object = MibTable
dot3adDrniConvAdminGatewayTable = _Dot3adDrniConvAdminGatewayTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dot3adDrniConvAdminGatewayTable.setStatus("current")
_Dot3adDrniConvAdminGatewayEntry_Object = MibTableRow
dot3adDrniConvAdminGatewayEntry = _Dot3adDrniConvAdminGatewayEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 2, 1)
)
dot3adDrniConvAdminGatewayEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adDrniGatewayConversationID"),
    (0, "IEEE8023-LAG-MIB", "dot3adDrniIndex"),
)
if mibBuilder.loadTexts:
    dot3adDrniConvAdminGatewayEntry.setStatus("current")


class _Dot3adDrniGatewayConversationID_Type(Integer32):
    """Custom type dot3adDrniGatewayConversationID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Dot3adDrniGatewayConversationID_Type.__name__ = "Integer32"
_Dot3adDrniGatewayConversationID_Object = MibTableColumn
dot3adDrniGatewayConversationID = _Dot3adDrniGatewayConversationID_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 2, 1, 1),
    _Dot3adDrniGatewayConversationID_Type()
)
dot3adDrniGatewayConversationID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adDrniGatewayConversationID.setStatus("current")
_Dot3adDrniConvAdminGatewayList_Type = DrniConvAdminGatewayList
_Dot3adDrniConvAdminGatewayList_Object = MibTableColumn
dot3adDrniConvAdminGatewayList = _Dot3adDrniConvAdminGatewayList_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 2, 1, 2),
    _Dot3adDrniConvAdminGatewayList_Type()
)
dot3adDrniConvAdminGatewayList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniConvAdminGatewayList.setStatus("current")
_Dot3adDrniIPLEncapMapTable_Object = MibTable
dot3adDrniIPLEncapMapTable = _Dot3adDrniIPLEncapMapTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dot3adDrniIPLEncapMapTable.setStatus("current")
_Dot3adDrniIPLEncapMapEntry_Object = MibTableRow
dot3adDrniIPLEncapMapEntry = _Dot3adDrniIPLEncapMapEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 3, 1)
)
dot3adDrniIPLEncapMapEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adDrniGatewayConversationID"),
    (0, "IEEE8023-LAG-MIB", "dot3adDrniIndex"),
)
if mibBuilder.loadTexts:
    dot3adDrniIPLEncapMapEntry.setStatus("current")
_Dot3adDrniIPLFrameIdValue_Type = Integer32
_Dot3adDrniIPLFrameIdValue_Object = MibTableColumn
dot3adDrniIPLFrameIdValue = _Dot3adDrniIPLFrameIdValue_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 3, 1, 2),
    _Dot3adDrniIPLFrameIdValue_Type()
)
dot3adDrniIPLFrameIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniIPLFrameIdValue.setStatus("current")
_Dot3adDrniNetEncapMapTable_Object = MibTable
dot3adDrniNetEncapMapTable = _Dot3adDrniNetEncapMapTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dot3adDrniNetEncapMapTable.setStatus("current")
_Dot3adDrniNetEncapMapEntry_Object = MibTableRow
dot3adDrniNetEncapMapEntry = _Dot3adDrniNetEncapMapEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 4, 1)
)
dot3adDrniNetEncapMapEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adDrniGatewayConversationID"),
    (0, "IEEE8023-LAG-MIB", "dot3adDrniIndex"),
)
if mibBuilder.loadTexts:
    dot3adDrniNetEncapMapEntry.setStatus("current")
_Dot3adDrniNetFrameIdValue_Type = Integer32
_Dot3adDrniNetFrameIdValue_Object = MibTableColumn
dot3adDrniNetFrameIdValue = _Dot3adDrniNetFrameIdValue_Object(
    (1, 2, 840, 10006, 300, 43, 1, 4, 4, 1, 1),
    _Dot3adDrniNetFrameIdValue_Type()
)
dot3adDrniNetFrameIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adDrniNetFrameIdValue.setStatus("current")
_Dot3adIPP_ObjectIdentity = ObjectIdentity
dot3adIPP = _Dot3adIPP_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 1, 5)
)
_Dot3adIPPAttributeTable_Object = MibTable
dot3adIPPAttributeTable = _Dot3adIPPAttributeTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dot3adIPPAttributeTable.setStatus("current")
_Dot3adIPPAttributeEntry_Object = MibTableRow
dot3adIPPAttributeEntry = _Dot3adIPPAttributeEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1, 1)
)
dot3adIPPAttributeEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adIPPIndex"),
)
if mibBuilder.loadTexts:
    dot3adIPPAttributeEntry.setStatus("current")
_Dot3adIPPIndex_Type = InterfaceIndex
_Dot3adIPPIndex_Object = MibTableColumn
dot3adIPPIndex = _Dot3adIPPIndex_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1, 1, 1),
    _Dot3adIPPIndex_Type()
)
dot3adIPPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adIPPIndex.setStatus("current")


class _Dot3adIPPPortConversationPasses_Type(OctetString):
    """Custom type dot3adIPPPortConversationPasses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_Dot3adIPPPortConversationPasses_Type.__name__ = "OctetString"
_Dot3adIPPPortConversationPasses_Object = MibTableColumn
dot3adIPPPortConversationPasses = _Dot3adIPPPortConversationPasses_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1, 1, 2),
    _Dot3adIPPPortConversationPasses_Type()
)
dot3adIPPPortConversationPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPPortConversationPasses.setStatus("current")


class _Dot3adIPPGatewayConversationDirection_Type(OctetString):
    """Custom type dot3adIPPGatewayConversationDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_Dot3adIPPGatewayConversationDirection_Type.__name__ = "OctetString"
_Dot3adIPPGatewayConversationDirection_Object = MibTableColumn
dot3adIPPGatewayConversationDirection = _Dot3adIPPGatewayConversationDirection_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1, 1, 3),
    _Dot3adIPPGatewayConversationDirection_Type()
)
dot3adIPPGatewayConversationDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPGatewayConversationDirection.setStatus("current")
_Dot3adIPPAdminState_Type = AggState
_Dot3adIPPAdminState_Object = MibTableColumn
dot3adIPPAdminState = _Dot3adIPPAdminState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1, 1, 4),
    _Dot3adIPPAdminState_Type()
)
dot3adIPPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adIPPAdminState.setStatus("current")
_Dot3adIPPOperState_Type = AggState
_Dot3adIPPOperState_Object = MibTableColumn
dot3adIPPOperState = _Dot3adIPPOperState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1, 1, 5),
    _Dot3adIPPOperState_Type()
)
dot3adIPPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPOperState.setStatus("current")
_Dot3adIPPTimeOfLastOperChange_Type = Integer32
_Dot3adIPPTimeOfLastOperChange_Object = MibTableColumn
dot3adIPPTimeOfLastOperChange = _Dot3adIPPTimeOfLastOperChange_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 1, 1, 6),
    _Dot3adIPPTimeOfLastOperChange_Type()
)
dot3adIPPTimeOfLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPTimeOfLastOperChange.setStatus("current")
_Dot3adIPPStatsTable_Object = MibTable
dot3adIPPStatsTable = _Dot3adIPPStatsTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dot3adIPPStatsTable.setStatus("current")
_Dot3adIPPStatsEntry_Object = MibTableRow
dot3adIPPStatsEntry = _Dot3adIPPStatsEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 2, 1)
)
dot3adIPPStatsEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adIPPIndex"),
)
if mibBuilder.loadTexts:
    dot3adIPPStatsEntry.setStatus("current")
_Dot3adIPPStatsDRCPDUsRx_Type = Counter64
_Dot3adIPPStatsDRCPDUsRx_Object = MibTableColumn
dot3adIPPStatsDRCPDUsRx = _Dot3adIPPStatsDRCPDUsRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 2, 1, 1),
    _Dot3adIPPStatsDRCPDUsRx_Type()
)
dot3adIPPStatsDRCPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPStatsDRCPDUsRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3adIPPStatsDRCPDUsRx.setUnits("frames")
_Dot3adIPPStatsIllegalRx_Type = Counter64
_Dot3adIPPStatsIllegalRx_Object = MibTableColumn
dot3adIPPStatsIllegalRx = _Dot3adIPPStatsIllegalRx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 2, 1, 2),
    _Dot3adIPPStatsIllegalRx_Type()
)
dot3adIPPStatsIllegalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPStatsIllegalRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3adIPPStatsIllegalRx.setUnits("frames")
_Dot3adIPPStatsDRCPDUsTx_Type = Counter64
_Dot3adIPPStatsDRCPDUsTx_Object = MibTableColumn
dot3adIPPStatsDRCPDUsTx = _Dot3adIPPStatsDRCPDUsTx_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 2, 1, 3),
    _Dot3adIPPStatsDRCPDUsTx_Type()
)
dot3adIPPStatsDRCPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPStatsDRCPDUsTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3adIPPStatsDRCPDUsTx.setUnits("frames")
_Dot3adIPPDebugTable_Object = MibTable
dot3adIPPDebugTable = _Dot3adIPPDebugTable_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 3)
)
if mibBuilder.loadTexts:
    dot3adIPPDebugTable.setStatus("current")
_Dot3adIPPDebugEntry_Object = MibTableRow
dot3adIPPDebugEntry = _Dot3adIPPDebugEntry_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 3, 1)
)
dot3adIPPDebugEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adIPPIndex"),
)
if mibBuilder.loadTexts:
    dot3adIPPDebugEntry.setStatus("current")


class _Dot3adIPPDebugDRCPRxState_Type(Integer32):
    """Custom type dot3adIPPDebugDRCPRxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("defaulted", 3),
          ("expired", 2),
          ("initialize", 4),
          ("reportToManagement", 5))
    )


_Dot3adIPPDebugDRCPRxState_Type.__name__ = "Integer32"
_Dot3adIPPDebugDRCPRxState_Object = MibTableColumn
dot3adIPPDebugDRCPRxState = _Dot3adIPPDebugDRCPRxState_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 3, 1, 1),
    _Dot3adIPPDebugDRCPRxState_Type()
)
dot3adIPPDebugDRCPRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPDebugDRCPRxState.setStatus("current")
_Dot3adIPPDebugLastRxTime_Type = TimeTicks
_Dot3adIPPDebugLastRxTime_Object = MibTableColumn
dot3adIPPDebugLastRxTime = _Dot3adIPPDebugLastRxTime_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 3, 1, 2),
    _Dot3adIPPDebugLastRxTime_Type()
)
dot3adIPPDebugLastRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPDebugLastRxTime.setStatus("current")
_Dot3adIPPDebugDifferPortalReason_Type = SnmpAdminString
_Dot3adIPPDebugDifferPortalReason_Object = MibTableColumn
dot3adIPPDebugDifferPortalReason = _Dot3adIPPDebugDifferPortalReason_Object(
    (1, 2, 840, 10006, 300, 43, 1, 5, 3, 1, 3),
    _Dot3adIPPDebugDifferPortalReason_Type()
)
dot3adIPPDebugDifferPortalReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adIPPDebugDifferPortalReason.setStatus("current")
_Dot3adAggConformance_ObjectIdentity = ObjectIdentity
dot3adAggConformance = _Dot3adAggConformance_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 2)
)
_Dot3adAggGroups_ObjectIdentity = ObjectIdentity
dot3adAggGroups = _Dot3adAggGroups_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 2, 1)
)
_Dot3adAggCompliances_ObjectIdentity = ObjectIdentity
dot3adAggCompliances = _Dot3adAggCompliances_ObjectIdentity(
    (1, 2, 840, 10006, 300, 43, 2, 2)
)
dot3adAggEntry.registerAugmentions(
    ("IEEE8023-LAG-MIB",
     "dot3adAggXEntry")
)
dot3adAggXEntry.setIndexNames(*dot3adAggEntry.getIndexNames())
dot3adAggPortEntry.registerAugmentions(
    ("IEEE8023-LAG-MIB",
     "dot3adAggPortXEntry")
)
dot3adAggPortXEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
dot3adAggPortEntry.registerAugmentions(
    ("IEEE8023-LAG-MIB",
     "dot3adAggPortSecondXEntry")
)
dot3adAggPortSecondXEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
dot3adAggPortDebugEntry.registerAugmentions(
    ("IEEE8023-LAG-MIB",
     "dot3adAggPortDebugXEntry")
)
dot3adAggPortDebugXEntry.setIndexNames(*dot3adAggPortDebugEntry.getIndexNames())

# Managed Objects groups

dot3adAggGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 1)
)
dot3adAggGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggActorSystemID"),
        ("IEEE8023-LAG-MIB", "dot3adAggActorSystemPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggAggregateOrIndividual"),
        ("IEEE8023-LAG-MIB", "dot3adAggActorAdminKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggMACAddress"),
        ("IEEE8023-LAG-MIB", "dot3adAggActorOperKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerSystemID"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerSystemPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerOperKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggCollectorMaxDelay"))
)
if mibBuilder.loadTexts:
    dot3adAggGroup.setStatus("current")

dot3adAggPortListGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 2)
)
dot3adAggPortListGroup.setObjects(
    ("IEEE8023-LAG-MIB", "dot3adAggPortListPorts")
)
if mibBuilder.loadTexts:
    dot3adAggPortListGroup.setStatus("current")

dot3adAggPortGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 3)
)
dot3adAggPortGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggPortActorSystemPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorSystemID"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorAdminKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorOperKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemID"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemID"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperKey"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortSelectedAggID"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortAttachedAggID"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorPort"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorPortPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPort"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPort"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPortPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPortPriority"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorAdminState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortActorOperState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortAggregateOrIndividual"))
)
if mibBuilder.loadTexts:
    dot3adAggPortGroup.setStatus("current")

dot3adAggPortStatsGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 4)
)
dot3adAggPortStatsGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsRx"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsRx"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsRx"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortStatsUnknownRx"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortStatsIllegalRx"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsTx"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsTx"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsTx"))
)
if mibBuilder.loadTexts:
    dot3adAggPortStatsGroup.setStatus("current")

dot3adAggPortDebugGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 5)
)
dot3adAggPortDebugGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggPortDebugRxState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugLastRxTime"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxReason"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnCount"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnCount"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorSyncTransitionCount"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerSyncTransitionCount"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChangeCount"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChangeCount"))
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugGroup.setStatus("current")

dot3adTablesLastChangedGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 6)
)
dot3adTablesLastChangedGroup.setObjects(
    ("IEEE8023-LAG-MIB", "dot3adTablesLastChanged")
)
if mibBuilder.loadTexts:
    dot3adTablesLastChangedGroup.setStatus("current")

dot3adAggPortProtocolDAGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 7)
)
dot3adAggPortProtocolDAGroup.setObjects(
    ("IEEE8023-LAG-MIB", "dot3adAggPortProtocolDA")
)
if mibBuilder.loadTexts:
    dot3adAggPortProtocolDAGroup.setStatus("current")

dot3adAggXGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 9)
)
dot3adAggXGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggDescription"),
        ("IEEE8023-LAG-MIB", "dot3adAggName"),
        ("IEEE8023-LAG-MIB", "dot3adAggAdminState"),
        ("IEEE8023-LAG-MIB", "dot3adAggOperState"),
        ("IEEE8023-LAG-MIB", "dot3adAggTimeOfLastOperChange"),
        ("IEEE8023-LAG-MIB", "dot3adAggDataRate"),
        ("IEEE8023-LAG-MIB", "dot3adAggFramesTxOK"),
        ("IEEE8023-LAG-MIB", "dot3adAggFramesRxOK"),
        ("IEEE8023-LAG-MIB", "dot3adAggLinkUpDownNotificationEnable"))
)
if mibBuilder.loadTexts:
    dot3adAggXGroup.setStatus("current")

dot3adAggRecommendedGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 10)
)
dot3adAggRecommendedGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggOctetsTxOK"),
        ("IEEE8023-LAG-MIB", "dot3adAggOctetsRxOK"),
        ("IEEE8023-LAG-MIB", "dot3adAggFramesDiscardedOnTx"),
        ("IEEE8023-LAG-MIB", "dot3adAggFramesDiscardedOnRx"),
        ("IEEE8023-LAG-MIB", "dot3adAggFramesWithTxErrors"),
        ("IEEE8023-LAG-MIB", "dot3adAggFramesWithRxErrors"),
        ("IEEE8023-LAG-MIB", "dot3adAggUnknownProtocolFrames"))
)
if mibBuilder.loadTexts:
    dot3adAggRecommendedGroup.setStatus("current")

dot3adAggOptionalGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 11)
)
dot3adAggOptionalGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggMulticastFramesTxOK"),
        ("IEEE8023-LAG-MIB", "dot3adAggMulticastFramesRxOK"),
        ("IEEE8023-LAG-MIB", "dot3adAggBroadcastFramesTxOK"),
        ("IEEE8023-LAG-MIB", "dot3adAggBroadcastFramesRxOK"))
)
if mibBuilder.loadTexts:
    dot3adAggOptionalGroup.setStatus("current")

dot3adPerServiceFrameDistGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 12)
)
dot3adPerServiceFrameDistGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggConversationAdminLinkList"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortAlgorithm"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerAdminPortAlgorithm"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerAdminPortConversationListDigest"),
        ("IEEE8023-LAG-MIB", "dot3adAggAdminDiscardWrongConversation"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerAdminConvServiceMappingDigest"),
        ("IEEE8023-LAG-MIB", "dot3adAggAdminServiceConversationServiceIDList"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortLinkNumberId"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminLinkNumberId"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortOperConversationPasses"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortOperConversationCollected"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortWTRTime"))
)
if mibBuilder.loadTexts:
    dot3adPerServiceFrameDistGroup.setStatus("deprecated")

dot3adAggPortDebugXGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 13)
)
dot3adAggPortDebugXGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorCDSChurnState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerCDSChurnState"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorCDSChurnCount"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerCDSChurnCount"))
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugXGroup.setStatus("current")

dot3adDrniGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 14)
)
dot3adDrniGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adDrniDescription"),
        ("IEEE8023-LAG-MIB", "dot3adDrniName"),
        ("IEEE8023-LAG-MIB", "dot3adDrniPortalAddr"),
        ("IEEE8023-LAG-MIB", "dot3adDrniPortalPriority"),
        ("IEEE8023-LAG-MIB", "dot3adDrniThreePortalSystem"),
        ("IEEE8023-LAG-MIB", "dot3adDrniPortalSystemNumber"),
        ("IEEE8023-LAG-MIB", "dot3adDrniIntraPortalLinkList"),
        ("IEEE8023-LAG-MIB", "dot3adDrniAggregator"),
        ("IEEE8023-LAG-MIB", "dot3adDrniNeighborAdminConvGatewayListDigest"),
        ("IEEE8023-LAG-MIB", "dot3adDrniNeighborAdminConvPortListDigest"),
        ("IEEE8023-LAG-MIB", "dot3adDrniGatewayAlgorithm"),
        ("IEEE8023-LAG-MIB", "dot3adDrniNeighborAdminGatewayAlgorithm"),
        ("IEEE8023-LAG-MIB", "dot3adDrniNeighborAdminPortAlgorithm"),
        ("IEEE8023-LAG-MIB", "dot3adDrniNeighborAdminDRCPState"),
        ("IEEE8023-LAG-MIB", "dot3adDrniEncapsulationMethod"),
        ("IEEE8023-LAG-MIB", "dot3adDrniDRPortConversationPasses"),
        ("IEEE8023-LAG-MIB", "dot3adDrniDRGatewayConversationPasses"),
        ("IEEE8023-LAG-MIB", "dot3adDrniConvAdminGatewayList"),
        ("IEEE8023-LAG-MIB", "dot3adDrniIPLFrameIdValue"),
        ("IEEE8023-LAG-MIB", "dot3adDrniNetFrameIdValue"),
        ("IEEE8023-LAG-MIB", "dot3adDrniPSI"),
        ("IEEE8023-LAG-MIB", "dot3adDrniPortConversationControl"),
        ("IEEE8023-LAG-MIB", "dot3adDrniIntraPortalPortProtocolDA"))
)
if mibBuilder.loadTexts:
    dot3adDrniGroup.setStatus("current")

dot3adIPPGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 15)
)
dot3adIPPGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adIPPPortConversationPasses"),
        ("IEEE8023-LAG-MIB", "dot3adIPPGatewayConversationDirection"),
        ("IEEE8023-LAG-MIB", "dot3adIPPAdminState"),
        ("IEEE8023-LAG-MIB", "dot3adIPPOperState"),
        ("IEEE8023-LAG-MIB", "dot3adIPPTimeOfLastOperChange"))
)
if mibBuilder.loadTexts:
    dot3adIPPGroup.setStatus("current")

dot3adIPPStatsGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 16)
)
dot3adIPPStatsGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adIPPStatsDRCPDUsRx"),
        ("IEEE8023-LAG-MIB", "dot3adIPPStatsIllegalRx"),
        ("IEEE8023-LAG-MIB", "dot3adIPPStatsDRCPDUsTx"))
)
if mibBuilder.loadTexts:
    dot3adIPPStatsGroup.setStatus("current")

dot3adIPPDebugGroup = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 17)
)
dot3adIPPDebugGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adIPPDebugDRCPRxState"),
        ("IEEE8023-LAG-MIB", "dot3adIPPDebugLastRxTime"),
        ("IEEE8023-LAG-MIB", "dot3adIPPDebugDifferPortalReason"))
)
if mibBuilder.loadTexts:
    dot3adIPPDebugGroup.setStatus("current")

dot3adPerServiceFrameDistGroup2 = ObjectGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 18)
)
dot3adPerServiceFrameDistGroup2.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggConversationAdminLinkList"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortAlgorithm"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerAdminPortAlgorithm"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerAdminPortConversationListDigest"),
        ("IEEE8023-LAG-MIB", "dot3adAggAdminDiscardWrongConversation2"),
        ("IEEE8023-LAG-MIB", "dot3adAggPartnerAdminConvServiceMappingDigest"),
        ("IEEE8023-LAG-MIB", "dot3adAggAdminServiceConversationServiceIDList"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortLinkNumberId"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortOperConversationPasses"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortOperConversationCollected"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortWTRTime"),
        ("IEEE8023-LAG-MIB", "dot3adAggPortEnableLongPDUXmit"))
)
if mibBuilder.loadTexts:
    dot3adPerServiceFrameDistGroup2.setStatus("current")


# Notification objects

dot3adAggLinkUpNotification = NotificationType(
    (1, 2, 840, 10006, 300, 43, 0, 1)
)
if mibBuilder.loadTexts:
    dot3adAggLinkUpNotification.setStatus(
        "current"
    )

dot3adAggLinkDownNotification = NotificationType(
    (1, 2, 840, 10006, 300, 43, 0, 2)
)
if mibBuilder.loadTexts:
    dot3adAggLinkDownNotification.setStatus(
        "current"
    )


# Notifications groups

dot3adAggNotificationGroup = NotificationGroup(
    (1, 2, 840, 10006, 300, 43, 2, 1, 8)
)
dot3adAggNotificationGroup.setObjects(
      *(("IEEE8023-LAG-MIB", "dot3adAggLinkUpNotification"),
        ("IEEE8023-LAG-MIB", "dot3adAggLinkDownNotification"))
)
if mibBuilder.loadTexts:
    dot3adAggNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dot3adAggCompliance = ModuleCompliance(
    (1, 2, 840, 10006, 300, 43, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dot3adAggCompliance.setStatus(
        "deprecated"
    )

dot3adAggCompliance2 = ModuleCompliance(
    (1, 2, 840, 10006, 300, 43, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dot3adAggCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8023-LAG-MIB",
    **{"LacpKey": LacpKey,
       "LacpState": LacpState,
       "DrcpState": DrcpState,
       "ChurnState": ChurnState,
       "AggState": AggState,
       "DrniConvAdminGatewayList": DrniConvAdminGatewayList,
       "PortalLinkList": PortalLinkList,
       "ServiceIdList": ServiceIdList,
       "lagMIB": lagMIB,
       "lagMIBNotifications": lagMIBNotifications,
       "dot3adAggLinkUpNotification": dot3adAggLinkUpNotification,
       "dot3adAggLinkDownNotification": dot3adAggLinkDownNotification,
       "lagMIBObjects": lagMIBObjects,
       "dot3adAgg": dot3adAgg,
       "dot3adAggTable": dot3adAggTable,
       "dot3adAggEntry": dot3adAggEntry,
       "dot3adAggIndex": dot3adAggIndex,
       "dot3adAggMACAddress": dot3adAggMACAddress,
       "dot3adAggActorSystemPriority": dot3adAggActorSystemPriority,
       "dot3adAggActorSystemID": dot3adAggActorSystemID,
       "dot3adAggAggregateOrIndividual": dot3adAggAggregateOrIndividual,
       "dot3adAggActorAdminKey": dot3adAggActorAdminKey,
       "dot3adAggActorOperKey": dot3adAggActorOperKey,
       "dot3adAggPartnerSystemID": dot3adAggPartnerSystemID,
       "dot3adAggPartnerSystemPriority": dot3adAggPartnerSystemPriority,
       "dot3adAggPartnerOperKey": dot3adAggPartnerOperKey,
       "dot3adAggCollectorMaxDelay": dot3adAggCollectorMaxDelay,
       "dot3adAggPortListTable": dot3adAggPortListTable,
       "dot3adAggPortListEntry": dot3adAggPortListEntry,
       "dot3adAggPortListPorts": dot3adAggPortListPorts,
       "dot3adAggXTable": dot3adAggXTable,
       "dot3adAggXEntry": dot3adAggXEntry,
       "dot3adAggDescription": dot3adAggDescription,
       "dot3adAggName": dot3adAggName,
       "dot3adAggAdminState": dot3adAggAdminState,
       "dot3adAggOperState": dot3adAggOperState,
       "dot3adAggTimeOfLastOperChange": dot3adAggTimeOfLastOperChange,
       "dot3adAggDataRate": dot3adAggDataRate,
       "dot3adAggOctetsTxOK": dot3adAggOctetsTxOK,
       "dot3adAggOctetsRxOK": dot3adAggOctetsRxOK,
       "dot3adAggFramesTxOK": dot3adAggFramesTxOK,
       "dot3adAggFramesRxOK": dot3adAggFramesRxOK,
       "dot3adAggMulticastFramesTxOK": dot3adAggMulticastFramesTxOK,
       "dot3adAggMulticastFramesRxOK": dot3adAggMulticastFramesRxOK,
       "dot3adAggBroadcastFramesTxOK": dot3adAggBroadcastFramesTxOK,
       "dot3adAggBroadcastFramesRxOK": dot3adAggBroadcastFramesRxOK,
       "dot3adAggFramesDiscardedOnTx": dot3adAggFramesDiscardedOnTx,
       "dot3adAggFramesDiscardedOnRx": dot3adAggFramesDiscardedOnRx,
       "dot3adAggFramesWithTxErrors": dot3adAggFramesWithTxErrors,
       "dot3adAggFramesWithRxErrors": dot3adAggFramesWithRxErrors,
       "dot3adAggUnknownProtocolFrames": dot3adAggUnknownProtocolFrames,
       "dot3adAggLinkUpDownNotificationEnable": dot3adAggLinkUpDownNotificationEnable,
       "dot3adAggPortAlgorithm": dot3adAggPortAlgorithm,
       "dot3adAggPartnerAdminPortAlgorithm": dot3adAggPartnerAdminPortAlgorithm,
       "dot3adAggPartnerAdminPortConversationListDigest": dot3adAggPartnerAdminPortConversationListDigest,
       "dot3adAggAdminDiscardWrongConversation": dot3adAggAdminDiscardWrongConversation,
       "dot3adAggPartnerAdminConvServiceMappingDigest": dot3adAggPartnerAdminConvServiceMappingDigest,
       "dot3adAggAdminDiscardWrongConversation2": dot3adAggAdminDiscardWrongConversation2,
       "dot3adAggConversationAdminLinkTable": dot3adAggConversationAdminLinkTable,
       "dot3adAggConversationAdminLinkEntry": dot3adAggConversationAdminLinkEntry,
       "dot3adAggConversationAdminLinkId": dot3adAggConversationAdminLinkId,
       "dot3adAggConversationAdminLinkList": dot3adAggConversationAdminLinkList,
       "dot3adAggAdminServiceConversationMapTable": dot3adAggAdminServiceConversationMapTable,
       "dot3adAggAdminServiceConversationMapEntry": dot3adAggAdminServiceConversationMapEntry,
       "dot3adAggAdminServiceConversationMapId": dot3adAggAdminServiceConversationMapId,
       "dot3adAggAdminServiceConversationServiceIDList": dot3adAggAdminServiceConversationServiceIDList,
       "dot3adAggPort": dot3adAggPort,
       "dot3adAggPortTable": dot3adAggPortTable,
       "dot3adAggPortEntry": dot3adAggPortEntry,
       "dot3adAggPortIndex": dot3adAggPortIndex,
       "dot3adAggPortActorSystemPriority": dot3adAggPortActorSystemPriority,
       "dot3adAggPortActorSystemID": dot3adAggPortActorSystemID,
       "dot3adAggPortActorAdminKey": dot3adAggPortActorAdminKey,
       "dot3adAggPortActorOperKey": dot3adAggPortActorOperKey,
       "dot3adAggPortPartnerAdminSystemPriority": dot3adAggPortPartnerAdminSystemPriority,
       "dot3adAggPortPartnerOperSystemPriority": dot3adAggPortPartnerOperSystemPriority,
       "dot3adAggPortPartnerAdminSystemID": dot3adAggPortPartnerAdminSystemID,
       "dot3adAggPortPartnerOperSystemID": dot3adAggPortPartnerOperSystemID,
       "dot3adAggPortPartnerAdminKey": dot3adAggPortPartnerAdminKey,
       "dot3adAggPortPartnerOperKey": dot3adAggPortPartnerOperKey,
       "dot3adAggPortSelectedAggID": dot3adAggPortSelectedAggID,
       "dot3adAggPortAttachedAggID": dot3adAggPortAttachedAggID,
       "dot3adAggPortActorPort": dot3adAggPortActorPort,
       "dot3adAggPortActorPortPriority": dot3adAggPortActorPortPriority,
       "dot3adAggPortPartnerAdminPort": dot3adAggPortPartnerAdminPort,
       "dot3adAggPortPartnerOperPort": dot3adAggPortPartnerOperPort,
       "dot3adAggPortPartnerAdminPortPriority": dot3adAggPortPartnerAdminPortPriority,
       "dot3adAggPortPartnerOperPortPriority": dot3adAggPortPartnerOperPortPriority,
       "dot3adAggPortActorAdminState": dot3adAggPortActorAdminState,
       "dot3adAggPortActorOperState": dot3adAggPortActorOperState,
       "dot3adAggPortPartnerAdminState": dot3adAggPortPartnerAdminState,
       "dot3adAggPortPartnerOperState": dot3adAggPortPartnerOperState,
       "dot3adAggPortAggregateOrIndividual": dot3adAggPortAggregateOrIndividual,
       "dot3adAggPortStatsTable": dot3adAggPortStatsTable,
       "dot3adAggPortStatsEntry": dot3adAggPortStatsEntry,
       "dot3adAggPortStatsLACPDUsRx": dot3adAggPortStatsLACPDUsRx,
       "dot3adAggPortStatsMarkerPDUsRx": dot3adAggPortStatsMarkerPDUsRx,
       "dot3adAggPortStatsMarkerResponsePDUsRx": dot3adAggPortStatsMarkerResponsePDUsRx,
       "dot3adAggPortStatsUnknownRx": dot3adAggPortStatsUnknownRx,
       "dot3adAggPortStatsIllegalRx": dot3adAggPortStatsIllegalRx,
       "dot3adAggPortStatsLACPDUsTx": dot3adAggPortStatsLACPDUsTx,
       "dot3adAggPortStatsMarkerPDUsTx": dot3adAggPortStatsMarkerPDUsTx,
       "dot3adAggPortStatsMarkerResponsePDUsTx": dot3adAggPortStatsMarkerResponsePDUsTx,
       "dot3adAggPortDebugTable": dot3adAggPortDebugTable,
       "dot3adAggPortDebugEntry": dot3adAggPortDebugEntry,
       "dot3adAggPortDebugRxState": dot3adAggPortDebugRxState,
       "dot3adAggPortDebugLastRxTime": dot3adAggPortDebugLastRxTime,
       "dot3adAggPortDebugMuxState": dot3adAggPortDebugMuxState,
       "dot3adAggPortDebugMuxReason": dot3adAggPortDebugMuxReason,
       "dot3adAggPortDebugActorChurnState": dot3adAggPortDebugActorChurnState,
       "dot3adAggPortDebugPartnerChurnState": dot3adAggPortDebugPartnerChurnState,
       "dot3adAggPortDebugActorChurnCount": dot3adAggPortDebugActorChurnCount,
       "dot3adAggPortDebugPartnerChurnCount": dot3adAggPortDebugPartnerChurnCount,
       "dot3adAggPortDebugActorSyncTransitionCount": dot3adAggPortDebugActorSyncTransitionCount,
       "dot3adAggPortDebugPartnerSyncTransitionCount": dot3adAggPortDebugPartnerSyncTransitionCount,
       "dot3adAggPortDebugActorChangeCount": dot3adAggPortDebugActorChangeCount,
       "dot3adAggPortDebugPartnerChangeCount": dot3adAggPortDebugPartnerChangeCount,
       "dot3adAggPortXTable": dot3adAggPortXTable,
       "dot3adAggPortXEntry": dot3adAggPortXEntry,
       "dot3adAggPortProtocolDA": dot3adAggPortProtocolDA,
       "dot3adAggPortSecondXTable": dot3adAggPortSecondXTable,
       "dot3adAggPortSecondXEntry": dot3adAggPortSecondXEntry,
       "dot3adAggPortOperConversationPasses": dot3adAggPortOperConversationPasses,
       "dot3adAggPortOperConversationCollected": dot3adAggPortOperConversationCollected,
       "dot3adAggPortLinkNumberId": dot3adAggPortLinkNumberId,
       "dot3adAggPortPartnerAdminLinkNumberId": dot3adAggPortPartnerAdminLinkNumberId,
       "dot3adAggPortWTRTime": dot3adAggPortWTRTime,
       "dot3adAggPortEnableLongPDUXmit": dot3adAggPortEnableLongPDUXmit,
       "dot3adAggPortDebugXTable": dot3adAggPortDebugXTable,
       "dot3adAggPortDebugXEntry": dot3adAggPortDebugXEntry,
       "dot3adAggPortDebugActorCDSChurnState": dot3adAggPortDebugActorCDSChurnState,
       "dot3adAggPortDebugPartnerCDSChurnState": dot3adAggPortDebugPartnerCDSChurnState,
       "dot3adAggPortDebugActorCDSChurnCount": dot3adAggPortDebugActorCDSChurnCount,
       "dot3adAggPortDebugPartnerCDSChurnCount": dot3adAggPortDebugPartnerCDSChurnCount,
       "dot3adTablesLastChanged": dot3adTablesLastChanged,
       "dot3adDrni": dot3adDrni,
       "dot3adDrniTable": dot3adDrniTable,
       "dot3adDrniEntry": dot3adDrniEntry,
       "dot3adDrniIndex": dot3adDrniIndex,
       "dot3adDrniDescription": dot3adDrniDescription,
       "dot3adDrniName": dot3adDrniName,
       "dot3adDrniPortalAddr": dot3adDrniPortalAddr,
       "dot3adDrniPortalPriority": dot3adDrniPortalPriority,
       "dot3adDrniThreePortalSystem": dot3adDrniThreePortalSystem,
       "dot3adDrniPortalSystemNumber": dot3adDrniPortalSystemNumber,
       "dot3adDrniIntraPortalLinkList": dot3adDrniIntraPortalLinkList,
       "dot3adDrniAggregator": dot3adDrniAggregator,
       "dot3adDrniNeighborAdminConvGatewayListDigest": dot3adDrniNeighborAdminConvGatewayListDigest,
       "dot3adDrniNeighborAdminConvPortListDigest": dot3adDrniNeighborAdminConvPortListDigest,
       "dot3adDrniGatewayAlgorithm": dot3adDrniGatewayAlgorithm,
       "dot3adDrniNeighborAdminGatewayAlgorithm": dot3adDrniNeighborAdminGatewayAlgorithm,
       "dot3adDrniNeighborAdminPortAlgorithm": dot3adDrniNeighborAdminPortAlgorithm,
       "dot3adDrniNeighborAdminDRCPState": dot3adDrniNeighborAdminDRCPState,
       "dot3adDrniEncapsulationMethod": dot3adDrniEncapsulationMethod,
       "dot3adDrniDRPortConversationPasses": dot3adDrniDRPortConversationPasses,
       "dot3adDrniDRGatewayConversationPasses": dot3adDrniDRGatewayConversationPasses,
       "dot3adDrniPSI": dot3adDrniPSI,
       "dot3adDrniPortConversationControl": dot3adDrniPortConversationControl,
       "dot3adDrniIntraPortalPortProtocolDA": dot3adDrniIntraPortalPortProtocolDA,
       "dot3adDrniConvAdminGatewayTable": dot3adDrniConvAdminGatewayTable,
       "dot3adDrniConvAdminGatewayEntry": dot3adDrniConvAdminGatewayEntry,
       "dot3adDrniGatewayConversationID": dot3adDrniGatewayConversationID,
       "dot3adDrniConvAdminGatewayList": dot3adDrniConvAdminGatewayList,
       "dot3adDrniIPLEncapMapTable": dot3adDrniIPLEncapMapTable,
       "dot3adDrniIPLEncapMapEntry": dot3adDrniIPLEncapMapEntry,
       "dot3adDrniIPLFrameIdValue": dot3adDrniIPLFrameIdValue,
       "dot3adDrniNetEncapMapTable": dot3adDrniNetEncapMapTable,
       "dot3adDrniNetEncapMapEntry": dot3adDrniNetEncapMapEntry,
       "dot3adDrniNetFrameIdValue": dot3adDrniNetFrameIdValue,
       "dot3adIPP": dot3adIPP,
       "dot3adIPPAttributeTable": dot3adIPPAttributeTable,
       "dot3adIPPAttributeEntry": dot3adIPPAttributeEntry,
       "dot3adIPPIndex": dot3adIPPIndex,
       "dot3adIPPPortConversationPasses": dot3adIPPPortConversationPasses,
       "dot3adIPPGatewayConversationDirection": dot3adIPPGatewayConversationDirection,
       "dot3adIPPAdminState": dot3adIPPAdminState,
       "dot3adIPPOperState": dot3adIPPOperState,
       "dot3adIPPTimeOfLastOperChange": dot3adIPPTimeOfLastOperChange,
       "dot3adIPPStatsTable": dot3adIPPStatsTable,
       "dot3adIPPStatsEntry": dot3adIPPStatsEntry,
       "dot3adIPPStatsDRCPDUsRx": dot3adIPPStatsDRCPDUsRx,
       "dot3adIPPStatsIllegalRx": dot3adIPPStatsIllegalRx,
       "dot3adIPPStatsDRCPDUsTx": dot3adIPPStatsDRCPDUsTx,
       "dot3adIPPDebugTable": dot3adIPPDebugTable,
       "dot3adIPPDebugEntry": dot3adIPPDebugEntry,
       "dot3adIPPDebugDRCPRxState": dot3adIPPDebugDRCPRxState,
       "dot3adIPPDebugLastRxTime": dot3adIPPDebugLastRxTime,
       "dot3adIPPDebugDifferPortalReason": dot3adIPPDebugDifferPortalReason,
       "dot3adAggConformance": dot3adAggConformance,
       "dot3adAggGroups": dot3adAggGroups,
       "dot3adAggGroup": dot3adAggGroup,
       "dot3adAggPortListGroup": dot3adAggPortListGroup,
       "dot3adAggPortGroup": dot3adAggPortGroup,
       "dot3adAggPortStatsGroup": dot3adAggPortStatsGroup,
       "dot3adAggPortDebugGroup": dot3adAggPortDebugGroup,
       "dot3adTablesLastChangedGroup": dot3adTablesLastChangedGroup,
       "dot3adAggPortProtocolDAGroup": dot3adAggPortProtocolDAGroup,
       "dot3adAggNotificationGroup": dot3adAggNotificationGroup,
       "dot3adAggXGroup": dot3adAggXGroup,
       "dot3adAggRecommendedGroup": dot3adAggRecommendedGroup,
       "dot3adAggOptionalGroup": dot3adAggOptionalGroup,
       "dot3adPerServiceFrameDistGroup": dot3adPerServiceFrameDistGroup,
       "dot3adAggPortDebugXGroup": dot3adAggPortDebugXGroup,
       "dot3adDrniGroup": dot3adDrniGroup,
       "dot3adIPPGroup": dot3adIPPGroup,
       "dot3adIPPStatsGroup": dot3adIPPStatsGroup,
       "dot3adIPPDebugGroup": dot3adIPPDebugGroup,
       "dot3adPerServiceFrameDistGroup2": dot3adPerServiceFrameDistGroup2,
       "dot3adAggCompliances": dot3adAggCompliances,
       "dot3adAggCompliance": dot3adAggCompliance,
       "dot3adAggCompliance2": dot3adAggCompliance2}
)
