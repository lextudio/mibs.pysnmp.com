# SNMP MIB module (NMS-MEAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-MEAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:02 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsMEAPS_ObjectIdentity = ObjectIdentity
nmsMEAPS = _NmsMEAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234)
)
_NmsMEAPSDomains_Type = Integer32
_NmsMEAPSDomains_Object = MibScalar
nmsMEAPSDomains = _NmsMEAPSDomains_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 1),
    _NmsMEAPSDomains_Type()
)
nmsMEAPSDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSDomains.setStatus("mandatory")
_NmsMEAPSPduRx_Type = Integer32
_NmsMEAPSPduRx_Object = MibScalar
nmsMEAPSPduRx = _NmsMEAPSPduRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 2),
    _NmsMEAPSPduRx_Type()
)
nmsMEAPSPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSPduRx.setStatus("mandatory")
_NmsMEAPSPduTx_Type = Integer32
_NmsMEAPSPduTx_Object = MibScalar
nmsMEAPSPduTx = _NmsMEAPSPduTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 3),
    _NmsMEAPSPduTx_Type()
)
nmsMEAPSPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSPduTx.setStatus("mandatory")
_NmsMEAPSDomainTable_Object = MibTable
nmsMEAPSDomainTable = _NmsMEAPSDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 4)
)
if mibBuilder.loadTexts:
    nmsMEAPSDomainTable.setStatus("mandatory")
_NmsMEAPSDomainTableEntry_Object = MibTableRow
nmsMEAPSDomainTableEntry = _NmsMEAPSDomainTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 4, 1)
)
nmsMEAPSDomainTableEntry.setIndexNames(
    (0, "NMS-MEAPS-MIB", "nmsMEAPSDomainID"),
)
if mibBuilder.loadTexts:
    nmsMEAPSDomainTableEntry.setStatus("mandatory")
_NmsMEAPSDomainID_Type = Integer32
_NmsMEAPSDomainID_Object = MibTableColumn
nmsMEAPSDomainID = _NmsMEAPSDomainID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 4, 1, 1),
    _NmsMEAPSDomainID_Type()
)
nmsMEAPSDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSDomainID.setStatus("mandatory")
_NmsMEAPSRings_Type = Integer32
_NmsMEAPSRings_Object = MibTableColumn
nmsMEAPSRings = _NmsMEAPSRings_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 4, 1, 2),
    _NmsMEAPSRings_Type()
)
nmsMEAPSRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRings.setStatus("mandatory")


class _NmsMEAPSRowStatus_Type(Integer32):
    """Custom type nmsMEAPSRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("running", 2))
    )


_NmsMEAPSRowStatus_Type.__name__ = "Integer32"
_NmsMEAPSRowStatus_Object = MibTableColumn
nmsMEAPSRowStatus = _NmsMEAPSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 4, 1, 3),
    _NmsMEAPSRowStatus_Type()
)
nmsMEAPSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsMEAPSRowStatus.setStatus("mandatory")
_NmsMEAPSRingTable_Object = MibTable
nmsMEAPSRingTable = _NmsMEAPSRingTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5)
)
if mibBuilder.loadTexts:
    nmsMEAPSRingTable.setStatus("mandatory")
_NmsMEAPSRingTableEntry_Object = MibTableRow
nmsMEAPSRingTableEntry = _NmsMEAPSRingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1)
)
nmsMEAPSRingTableEntry.setIndexNames(
    (0, "NMS-MEAPS-MIB", "nmsMEAPSRingID"),
)
if mibBuilder.loadTexts:
    nmsMEAPSRingTableEntry.setStatus("mandatory")
_NmsMEAPSRingID_Type = Integer32
_NmsMEAPSRingID_Object = MibTableColumn
nmsMEAPSRingID = _NmsMEAPSRingID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 1),
    _NmsMEAPSRingID_Type()
)
nmsMEAPSRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingID.setStatus("mandatory")


class _NmsMEAPSRingLevel_Type(Integer32):
    """Custom type nmsMEAPSRingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("majorRing", 1),
          ("subRing", 2),
          ("unknown", 0))
    )


_NmsMEAPSRingLevel_Type.__name__ = "Integer32"
_NmsMEAPSRingLevel_Object = MibTableColumn
nmsMEAPSRingLevel = _NmsMEAPSRingLevel_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 2),
    _NmsMEAPSRingLevel_Type()
)
nmsMEAPSRingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingLevel.setStatus("mandatory")


class _NmsMEAPSRingNodeType_Type(Integer32):
    """Custom type nmsMEAPSRingNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("assistantNode", 4),
          ("edgeNode", 3),
          ("masterNode", 1),
          ("transitNode", 2),
          ("unknown", 0))
    )


_NmsMEAPSRingNodeType_Type.__name__ = "Integer32"
_NmsMEAPSRingNodeType_Object = MibTableColumn
nmsMEAPSRingNodeType = _NmsMEAPSRingNodeType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 3),
    _NmsMEAPSRingNodeType_Type()
)
nmsMEAPSRingNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingNodeType.setStatus("mandatory")
_NmsMEAPSRingControlVlanMajor_Type = Integer32
_NmsMEAPSRingControlVlanMajor_Object = MibTableColumn
nmsMEAPSRingControlVlanMajor = _NmsMEAPSRingControlVlanMajor_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 4),
    _NmsMEAPSRingControlVlanMajor_Type()
)
nmsMEAPSRingControlVlanMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingControlVlanMajor.setStatus("mandatory")
_NmsMEAPSRingControlVlanSub_Type = Integer32
_NmsMEAPSRingControlVlanSub_Object = MibTableColumn
nmsMEAPSRingControlVlanSub = _NmsMEAPSRingControlVlanSub_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 5),
    _NmsMEAPSRingControlVlanSub_Type()
)
nmsMEAPSRingControlVlanSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingControlVlanSub.setStatus("mandatory")
_NmsMEAPSRingPorts_Type = Integer32
_NmsMEAPSRingPorts_Object = MibTableColumn
nmsMEAPSRingPorts = _NmsMEAPSRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 6),
    _NmsMEAPSRingPorts_Type()
)
nmsMEAPSRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPorts.setStatus("mandatory")


class _NmsMEAPSRingState_Type(Integer32):
    """Custom type nmsMEAPSRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("ringFault", 2),
          ("unknown", 0))
    )


_NmsMEAPSRingState_Type.__name__ = "Integer32"
_NmsMEAPSRingState_Object = MibTableColumn
nmsMEAPSRingState = _NmsMEAPSRingState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 7),
    _NmsMEAPSRingState_Type()
)
nmsMEAPSRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingState.setStatus("mandatory")


class _NmsMEAPSRingHealthCheck_Type(Integer32):
    """Custom type nmsMEAPSRingHealthCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NmsMEAPSRingHealthCheck_Type.__name__ = "Integer32"
_NmsMEAPSRingHealthCheck_Object = MibTableColumn
nmsMEAPSRingHealthCheck = _NmsMEAPSRingHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 8),
    _NmsMEAPSRingHealthCheck_Type()
)
nmsMEAPSRingHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingHealthCheck.setStatus("mandatory")
_NmsMEAPSRingHelloTime_Type = Integer32
_NmsMEAPSRingHelloTime_Object = MibTableColumn
nmsMEAPSRingHelloTime = _NmsMEAPSRingHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 9),
    _NmsMEAPSRingHelloTime_Type()
)
nmsMEAPSRingHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingHelloTime.setStatus("mandatory")
_NmsMEAPSRingFailTime_Type = Integer32
_NmsMEAPSRingFailTime_Object = MibTableColumn
nmsMEAPSRingFailTime = _NmsMEAPSRingFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 10),
    _NmsMEAPSRingFailTime_Type()
)
nmsMEAPSRingFailTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingFailTime.setStatus("mandatory")
_NmsMEAPSRingPreforwardTime_Type = Integer32
_NmsMEAPSRingPreforwardTime_Object = MibTableColumn
nmsMEAPSRingPreforwardTime = _NmsMEAPSRingPreforwardTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 11),
    _NmsMEAPSRingPreforwardTime_Type()
)
nmsMEAPSRingPreforwardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingPreforwardTime.setStatus("mandatory")
_NmsMEAPSRingEdgeHelloTime_Type = Integer32
_NmsMEAPSRingEdgeHelloTime_Object = MibTableColumn
nmsMEAPSRingEdgeHelloTime = _NmsMEAPSRingEdgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 12),
    _NmsMEAPSRingEdgeHelloTime_Type()
)
nmsMEAPSRingEdgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingEdgeHelloTime.setStatus("mandatory")
_NmsMEAPSRingEdgeFailTime_Type = Integer32
_NmsMEAPSRingEdgeFailTime_Object = MibTableColumn
nmsMEAPSRingEdgeFailTime = _NmsMEAPSRingEdgeFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 13),
    _NmsMEAPSRingEdgeFailTime_Type()
)
nmsMEAPSRingEdgeFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingEdgeFailTime.setStatus("mandatory")


class _NmsMEAPSRingAdminStatus_Type(Integer32):
    """Custom type nmsMEAPSRingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("running", 2))
    )


_NmsMEAPSRingAdminStatus_Type.__name__ = "Integer32"
_NmsMEAPSRingAdminStatus_Object = MibTableColumn
nmsMEAPSRingAdminStatus = _NmsMEAPSRingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 14),
    _NmsMEAPSRingAdminStatus_Type()
)
nmsMEAPSRingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsMEAPSRingAdminStatus.setStatus("mandatory")
_NmsMEAPSRingPrimaryPort_Type = Integer32
_NmsMEAPSRingPrimaryPort_Object = MibTableColumn
nmsMEAPSRingPrimaryPort = _NmsMEAPSRingPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 15),
    _NmsMEAPSRingPrimaryPort_Type()
)
nmsMEAPSRingPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingPrimaryPort.setStatus("mandatory")


class _NmsMEAPSRingPrimaryPortState_Type(Integer32):
    """Custom type nmsMEAPSRingPrimaryPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("edgepreforwarding", 4),
          ("forwarding", 1),
          ("preforwarding", 2),
          ("unknown", 0))
    )


_NmsMEAPSRingPrimaryPortState_Type.__name__ = "Integer32"
_NmsMEAPSRingPrimaryPortState_Object = MibTableColumn
nmsMEAPSRingPrimaryPortState = _NmsMEAPSRingPrimaryPortState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 16),
    _NmsMEAPSRingPrimaryPortState_Type()
)
nmsMEAPSRingPrimaryPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPrimaryPortState.setStatus("mandatory")


class _NmsMEAPSRingPrimaryPortStatus_Type(Integer32):
    """Custom type nmsMEAPSRingPrimaryPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1))
    )


_NmsMEAPSRingPrimaryPortStatus_Type.__name__ = "Integer32"
_NmsMEAPSRingPrimaryPortStatus_Object = MibTableColumn
nmsMEAPSRingPrimaryPortStatus = _NmsMEAPSRingPrimaryPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 17),
    _NmsMEAPSRingPrimaryPortStatus_Type()
)
nmsMEAPSRingPrimaryPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPrimaryPortStatus.setStatus("mandatory")
_NmsMEAPSRingSecondaryPort_Type = Integer32
_NmsMEAPSRingSecondaryPort_Object = MibTableColumn
nmsMEAPSRingSecondaryPort = _NmsMEAPSRingSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 18),
    _NmsMEAPSRingSecondaryPort_Type()
)
nmsMEAPSRingSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsMEAPSRingSecondaryPort.setStatus("mandatory")


class _NmsMEAPSRingSecondaryPortState_Type(Integer32):
    """Custom type nmsMEAPSRingSecondaryPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("edgepreforwarding", 4),
          ("forwarding", 1),
          ("preforwarding", 2),
          ("unknown", 0))
    )


_NmsMEAPSRingSecondaryPortState_Type.__name__ = "Integer32"
_NmsMEAPSRingSecondaryPortState_Object = MibTableColumn
nmsMEAPSRingSecondaryPortState = _NmsMEAPSRingSecondaryPortState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 19),
    _NmsMEAPSRingSecondaryPortState_Type()
)
nmsMEAPSRingSecondaryPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingSecondaryPortState.setStatus("mandatory")


class _NmsMEAPSRingSecondaryPortStatus_Type(Integer32):
    """Custom type nmsMEAPSRingSecondaryPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1))
    )


_NmsMEAPSRingSecondaryPortStatus_Type.__name__ = "Integer32"
_NmsMEAPSRingSecondaryPortStatus_Object = MibTableColumn
nmsMEAPSRingSecondaryPortStatus = _NmsMEAPSRingSecondaryPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 5, 1, 20),
    _NmsMEAPSRingSecondaryPortStatus_Type()
)
nmsMEAPSRingSecondaryPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingSecondaryPortStatus.setStatus("mandatory")
_NmsMEAPSRingPortTable_Object = MibTable
nmsMEAPSRingPortTable = _NmsMEAPSRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6)
)
if mibBuilder.loadTexts:
    nmsMEAPSRingPortTable.setStatus("mandatory")
_NmsMEAPSRingPortTableEntry_Object = MibTableRow
nmsMEAPSRingPortTableEntry = _NmsMEAPSRingPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1)
)
nmsMEAPSRingPortTableEntry.setIndexNames(
    (0, "NMS-MEAPS-MIB", "nmsMEAPSRingPortRingID"),
    (0, "NMS-MEAPS-MIB", "nmsMEAPSRingPort"),
)
if mibBuilder.loadTexts:
    nmsMEAPSRingPortTableEntry.setStatus("mandatory")
_NmsMEAPSRingPortRingID_Type = Integer32
_NmsMEAPSRingPortRingID_Object = MibTableColumn
nmsMEAPSRingPortRingID = _NmsMEAPSRingPortRingID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 1),
    _NmsMEAPSRingPortRingID_Type()
)
nmsMEAPSRingPortRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPortRingID.setStatus("mandatory")
_NmsMEAPSRingPort_Type = Integer32
_NmsMEAPSRingPort_Object = MibTableColumn
nmsMEAPSRingPort = _NmsMEAPSRingPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 2),
    _NmsMEAPSRingPort_Type()
)
nmsMEAPSRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPort.setStatus("mandatory")


class _NmsMEAPSRingPortType_Type(Integer32):
    """Custom type nmsMEAPSRingPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("commonPort", 4),
          ("edgePort", 5),
          ("primaryPort", 1),
          ("secondaryPort", 2),
          ("transitPort", 3),
          ("unknown", 0))
    )


_NmsMEAPSRingPortType_Type.__name__ = "Integer32"
_NmsMEAPSRingPortType_Object = MibTableColumn
nmsMEAPSRingPortType = _NmsMEAPSRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 3),
    _NmsMEAPSRingPortType_Type()
)
nmsMEAPSRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPortType.setStatus("mandatory")


class _NmsMEAPSRingPortState_Type(Integer32):
    """Custom type nmsMEAPSRingPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("edgepreforwarding", 4),
          ("forwarding", 1),
          ("preforwarding", 2),
          ("unknown", 0))
    )


_NmsMEAPSRingPortState_Type.__name__ = "Integer32"
_NmsMEAPSRingPortState_Object = MibTableColumn
nmsMEAPSRingPortState = _NmsMEAPSRingPortState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 4),
    _NmsMEAPSRingPortState_Type()
)
nmsMEAPSRingPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPortState.setStatus("mandatory")
_NmsMEAPSRingPortForwards_Type = Integer32
_NmsMEAPSRingPortForwards_Object = MibTableColumn
nmsMEAPSRingPortForwards = _NmsMEAPSRingPortForwards_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 5),
    _NmsMEAPSRingPortForwards_Type()
)
nmsMEAPSRingPortForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPortForwards.setStatus("mandatory")
_NmsMEAPSRingPortRx_Type = Integer32
_NmsMEAPSRingPortRx_Object = MibTableColumn
nmsMEAPSRingPortRx = _NmsMEAPSRingPortRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 6),
    _NmsMEAPSRingPortRx_Type()
)
nmsMEAPSRingPortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPortRx.setStatus("mandatory")
_NmsMEAPSRingPortTx_Type = Integer32
_NmsMEAPSRingPortTx_Object = MibTableColumn
nmsMEAPSRingPortTx = _NmsMEAPSRingPortTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 7),
    _NmsMEAPSRingPortTx_Type()
)
nmsMEAPSRingPortTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPortTx.setStatus("mandatory")


class _NmsMEAPSRingPortStatus_Type(Integer32):
    """Custom type nmsMEAPSRingPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1))
    )


_NmsMEAPSRingPortStatus_Type.__name__ = "Integer32"
_NmsMEAPSRingPortStatus_Object = MibTableColumn
nmsMEAPSRingPortStatus = _NmsMEAPSRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 6, 1, 8),
    _NmsMEAPSRingPortStatus_Type()
)
nmsMEAPSRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMEAPSRingPortStatus.setStatus("mandatory")
_NmsMEAPSRingNotifications_ObjectIdentity = ObjectIdentity
nmsMEAPSRingNotifications = _NmsMEAPSRingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 7)
)

# Managed Objects groups


# Notification objects

nmsMEAPSRingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 234, 7, 1)
)
nmsMEAPSRingNotification.setObjects(
      *(("NMS-MEAPS-MIB", "nmsMEAPSRingID"),
        ("NMS-MEAPS-MIB", "nmsMEAPSRingNodeType"),
        ("NMS-MEAPS-MIB", "nmsMEAPSRingState"))
)
if mibBuilder.loadTexts:
    nmsMEAPSRingNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-MEAPS-MIB",
    **{"nmsMEAPS": nmsMEAPS,
       "nmsMEAPSDomains": nmsMEAPSDomains,
       "nmsMEAPSPduRx": nmsMEAPSPduRx,
       "nmsMEAPSPduTx": nmsMEAPSPduTx,
       "nmsMEAPSDomainTable": nmsMEAPSDomainTable,
       "nmsMEAPSDomainTableEntry": nmsMEAPSDomainTableEntry,
       "nmsMEAPSDomainID": nmsMEAPSDomainID,
       "nmsMEAPSRings": nmsMEAPSRings,
       "nmsMEAPSRowStatus": nmsMEAPSRowStatus,
       "nmsMEAPSRingTable": nmsMEAPSRingTable,
       "nmsMEAPSRingTableEntry": nmsMEAPSRingTableEntry,
       "nmsMEAPSRingID": nmsMEAPSRingID,
       "nmsMEAPSRingLevel": nmsMEAPSRingLevel,
       "nmsMEAPSRingNodeType": nmsMEAPSRingNodeType,
       "nmsMEAPSRingControlVlanMajor": nmsMEAPSRingControlVlanMajor,
       "nmsMEAPSRingControlVlanSub": nmsMEAPSRingControlVlanSub,
       "nmsMEAPSRingPorts": nmsMEAPSRingPorts,
       "nmsMEAPSRingState": nmsMEAPSRingState,
       "nmsMEAPSRingHealthCheck": nmsMEAPSRingHealthCheck,
       "nmsMEAPSRingHelloTime": nmsMEAPSRingHelloTime,
       "nmsMEAPSRingFailTime": nmsMEAPSRingFailTime,
       "nmsMEAPSRingPreforwardTime": nmsMEAPSRingPreforwardTime,
       "nmsMEAPSRingEdgeHelloTime": nmsMEAPSRingEdgeHelloTime,
       "nmsMEAPSRingEdgeFailTime": nmsMEAPSRingEdgeFailTime,
       "nmsMEAPSRingAdminStatus": nmsMEAPSRingAdminStatus,
       "nmsMEAPSRingPrimaryPort": nmsMEAPSRingPrimaryPort,
       "nmsMEAPSRingPrimaryPortState": nmsMEAPSRingPrimaryPortState,
       "nmsMEAPSRingPrimaryPortStatus": nmsMEAPSRingPrimaryPortStatus,
       "nmsMEAPSRingSecondaryPort": nmsMEAPSRingSecondaryPort,
       "nmsMEAPSRingSecondaryPortState": nmsMEAPSRingSecondaryPortState,
       "nmsMEAPSRingSecondaryPortStatus": nmsMEAPSRingSecondaryPortStatus,
       "nmsMEAPSRingPortTable": nmsMEAPSRingPortTable,
       "nmsMEAPSRingPortTableEntry": nmsMEAPSRingPortTableEntry,
       "nmsMEAPSRingPortRingID": nmsMEAPSRingPortRingID,
       "nmsMEAPSRingPort": nmsMEAPSRingPort,
       "nmsMEAPSRingPortType": nmsMEAPSRingPortType,
       "nmsMEAPSRingPortState": nmsMEAPSRingPortState,
       "nmsMEAPSRingPortForwards": nmsMEAPSRingPortForwards,
       "nmsMEAPSRingPortRx": nmsMEAPSRingPortRx,
       "nmsMEAPSRingPortTx": nmsMEAPSRingPortTx,
       "nmsMEAPSRingPortStatus": nmsMEAPSRingPortStatus,
       "nmsMEAPSRingNotifications": nmsMEAPSRingNotifications,
       "nmsMEAPSRingNotification": nmsMEAPSRingNotification}
)
