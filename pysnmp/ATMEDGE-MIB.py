# SNMP MIB module (ATMEDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATMEDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:08 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmEdge_ObjectIdentity = ObjectIdentity
atmEdge = _AtmEdge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 26)
)
_AtmEdgePort_ObjectIdentity = ObjectIdentity
atmEdgePort = _AtmEdgePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 26, 1)
)
_AtmEdgePortTable_Object = MibTable
atmEdgePortTable = _AtmEdgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1)
)
if mibBuilder.loadTexts:
    atmEdgePortTable.setStatus("mandatory")
_AtmEdgePortEntry_Object = MibTableRow
atmEdgePortEntry = _AtmEdgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1)
)
atmEdgePortEntry.setIndexNames(
    (0, "ATMEDGE-MIB", "atmEdgePortGroupId"),
    (0, "ATMEDGE-MIB", "atmEdgePortId"),
)
if mibBuilder.loadTexts:
    atmEdgePortEntry.setStatus("mandatory")


class _AtmEdgePortGroupId_Type(Integer32):
    """Custom type atmEdgePortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmEdgePortGroupId_Type.__name__ = "Integer32"
_AtmEdgePortGroupId_Object = MibTableColumn
atmEdgePortGroupId = _AtmEdgePortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 1),
    _AtmEdgePortGroupId_Type()
)
atmEdgePortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortGroupId.setStatus("mandatory")


class _AtmEdgePortId_Type(Integer32):
    """Custom type atmEdgePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmEdgePortId_Type.__name__ = "Integer32"
_AtmEdgePortId_Object = MibTableColumn
atmEdgePortId = _AtmEdgePortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 2),
    _AtmEdgePortId_Type()
)
atmEdgePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortId.setStatus("mandatory")


class _AtmEdgePortHealthStatus_Type(Integer32):
    """Custom type atmEdgePortHealthStatus based on Integer32"""
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
        *(("atmError", 2),
          ("notSupported", 255),
          ("ok", 1),
          ("sonetLinkError", 3),
          ("sonetRemoteLinkError", 4))
    )


_AtmEdgePortHealthStatus_Type.__name__ = "Integer32"
_AtmEdgePortHealthStatus_Object = MibTableColumn
atmEdgePortHealthStatus = _AtmEdgePortHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 3),
    _AtmEdgePortHealthStatus_Type()
)
atmEdgePortHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortHealthStatus.setStatus("mandatory")


class _AtmEdgePortMACAddr_Type(OctetString):
    """Custom type atmEdgePortMACAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AtmEdgePortMACAddr_Type.__name__ = "OctetString"
_AtmEdgePortMACAddr_Object = MibTableColumn
atmEdgePortMACAddr = _AtmEdgePortMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 4),
    _AtmEdgePortMACAddr_Type()
)
atmEdgePortMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortMACAddr.setStatus("mandatory")


class _AtmEdgePortATMAddr_Type(OctetString):
    """Custom type atmEdgePortATMAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmEdgePortATMAddr_Type.__name__ = "OctetString"
_AtmEdgePortATMAddr_Object = MibTableColumn
atmEdgePortATMAddr = _AtmEdgePortATMAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 5),
    _AtmEdgePortATMAddr_Type()
)
atmEdgePortATMAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortATMAddr.setStatus("mandatory")


class _AtmEdgePortLanType_Type(Integer32):
    """Custom type atmEdgePortLanType based on Integer32"""
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
        *(("ethernet", 1),
          ("notSupported", 255),
          ("token-ring", 2))
    )


_AtmEdgePortLanType_Type.__name__ = "Integer32"
_AtmEdgePortLanType_Object = MibTableColumn
atmEdgePortLanType = _AtmEdgePortLanType_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 6),
    _AtmEdgePortLanType_Type()
)
atmEdgePortLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortLanType.setStatus("mandatory")


class _AtmEdgePortILMIStatus_Type(Integer32):
    """Custom type atmEdgePortILMIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notsupported", 255),
          ("up", 1))
    )


_AtmEdgePortILMIStatus_Type.__name__ = "Integer32"
_AtmEdgePortILMIStatus_Object = MibTableColumn
atmEdgePortILMIStatus = _AtmEdgePortILMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 7),
    _AtmEdgePortILMIStatus_Type()
)
atmEdgePortILMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortILMIStatus.setStatus("mandatory")


class _AtmEdgePortSignalStatus_Type(Integer32):
    """Custom type atmEdgePortSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notsupported", 255),
          ("up", 1))
    )


_AtmEdgePortSignalStatus_Type.__name__ = "Integer32"
_AtmEdgePortSignalStatus_Object = MibTableColumn
atmEdgePortSignalStatus = _AtmEdgePortSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 8),
    _AtmEdgePortSignalStatus_Type()
)
atmEdgePortSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortSignalStatus.setStatus("mandatory")


class _AtmEdgePortActualUNIVersion_Type(Integer32):
    """Custom type atmEdgePortActualUNIVersion based on Integer32"""
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
        *(("notsupported", 255),
          ("uni-30", 2),
          ("uni-31", 3),
          ("uni-40", 4),
          ("unknown", 1))
    )


_AtmEdgePortActualUNIVersion_Type.__name__ = "Integer32"
_AtmEdgePortActualUNIVersion_Object = MibTableColumn
atmEdgePortActualUNIVersion = _AtmEdgePortActualUNIVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 9),
    _AtmEdgePortActualUNIVersion_Type()
)
atmEdgePortActualUNIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortActualUNIVersion.setStatus("mandatory")


class _AtmEdgePortNetworkPrefix_Type(OctetString):
    """Custom type atmEdgePortNetworkPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_AtmEdgePortNetworkPrefix_Type.__name__ = "OctetString"
_AtmEdgePortNetworkPrefix_Object = MibTableColumn
atmEdgePortNetworkPrefix = _AtmEdgePortNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 10),
    _AtmEdgePortNetworkPrefix_Type()
)
atmEdgePortNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEdgePortNetworkPrefix.setStatus("mandatory")


class _AtmEdgePortDormantHealthStatus_Type(Integer32):
    """Custom type atmEdgePortDormantHealthStatus based on Integer32"""
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
        *(("atmError", 2),
          ("notSupported", 255),
          ("ok", 1),
          ("sonetLinkError", 3),
          ("sonetRemoteLinkError", 4))
    )


_AtmEdgePortDormantHealthStatus_Type.__name__ = "Integer32"
_AtmEdgePortDormantHealthStatus_Object = MibTableColumn
atmEdgePortDormantHealthStatus = _AtmEdgePortDormantHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 11),
    _AtmEdgePortDormantHealthStatus_Type()
)
atmEdgePortDormantHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortDormantHealthStatus.setStatus("mandatory")


class _AtmEdgePortRedundancyStatus_Type(Integer32):
    """Custom type atmEdgePortRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("masterNicActive", 1),
          ("notSupported", 255),
          ("secondaryNicActive", 2))
    )


_AtmEdgePortRedundancyStatus_Type.__name__ = "Integer32"
_AtmEdgePortRedundancyStatus_Object = MibTableColumn
atmEdgePortRedundancyStatus = _AtmEdgePortRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 12),
    _AtmEdgePortRedundancyStatus_Type()
)
atmEdgePortRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgePortRedundancyStatus.setStatus("mandatory")
_AtmEdgeGroup_ObjectIdentity = ObjectIdentity
atmEdgeGroup = _AtmEdgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 26, 2)
)
_AtmEdgeGroupTable_Object = MibTable
atmEdgeGroupTable = _AtmEdgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 2, 1)
)
if mibBuilder.loadTexts:
    atmEdgeGroupTable.setStatus("mandatory")
_AtmEdgeGroupEntry_Object = MibTableRow
atmEdgeGroupEntry = _AtmEdgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1)
)
atmEdgeGroupEntry.setIndexNames(
    (0, "ATMEDGE-MIB", "atmEdgeGroupGroupId"),
)
if mibBuilder.loadTexts:
    atmEdgeGroupEntry.setStatus("mandatory")
_AtmEdgeGroupGroupId_Type = Integer32
_AtmEdgeGroupGroupId_Object = MibTableColumn
atmEdgeGroupGroupId = _AtmEdgeGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1, 1),
    _AtmEdgeGroupGroupId_Type()
)
atmEdgeGroupGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgeGroupGroupId.setStatus("mandatory")


class _AtmEdgeGroupWorkState_Type(Integer32):
    """Custom type atmEdgeGroupWorkState based on Integer32"""
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
        *(("boot", 2),
          ("none", 4),
          ("notSupported", 255),
          ("run", 1),
          ("runAndBoot", 3))
    )


_AtmEdgeGroupWorkState_Type.__name__ = "Integer32"
_AtmEdgeGroupWorkState_Object = MibTableColumn
atmEdgeGroupWorkState = _AtmEdgeGroupWorkState_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1, 2),
    _AtmEdgeGroupWorkState_Type()
)
atmEdgeGroupWorkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgeGroupWorkState.setStatus("mandatory")


class _AtmEdgeGroupBITResult_Type(Integer32):
    """Custom type atmEdgeGroupBITResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_AtmEdgeGroupBITResult_Type.__name__ = "Integer32"
_AtmEdgeGroupBITResult_Object = MibTableColumn
atmEdgeGroupBITResult = _AtmEdgeGroupBITResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1, 3),
    _AtmEdgeGroupBITResult_Type()
)
atmEdgeGroupBITResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEdgeGroupBITResult.setStatus("mandatory")
_AtmEdgeAssociation_ObjectIdentity = ObjectIdentity
atmEdgeAssociation = _AtmEdgeAssociation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 26, 3)
)
_AssociationTable_Object = MibTable
associationTable = _AssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1)
)
if mibBuilder.loadTexts:
    associationTable.setStatus("mandatory")
_AssociationEntry_Object = MibTableRow
associationEntry = _AssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1)
)
associationEntry.setIndexNames(
    (0, "ATMEDGE-MIB", "associationSlotIndex"),
    (0, "ATMEDGE-MIB", "associationPortIndex"),
    (0, "ATMEDGE-MIB", "associationIndex"),
)
if mibBuilder.loadTexts:
    associationEntry.setStatus("mandatory")
_AssociationSlotIndex_Type = Integer32
_AssociationSlotIndex_Object = MibTableColumn
associationSlotIndex = _AssociationSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 1),
    _AssociationSlotIndex_Type()
)
associationSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationSlotIndex.setStatus("mandatory")
_AssociationPortIndex_Type = Integer32
_AssociationPortIndex_Object = MibTableColumn
associationPortIndex = _AssociationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 2),
    _AssociationPortIndex_Type()
)
associationPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationPortIndex.setStatus("mandatory")
_AssociationIndex_Type = Integer32
_AssociationIndex_Object = MibTableColumn
associationIndex = _AssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 3),
    _AssociationIndex_Type()
)
associationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationIndex.setStatus("mandatory")


class _AssociationVlan_Type(Integer32):
    """Custom type associationVlan based on Integer32"""
    defaultValue = 0


_AssociationVlan_Object = MibTableColumn
associationVlan = _AssociationVlan_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 4),
    _AssociationVlan_Type()
)
associationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    associationVlan.setStatus("mandatory")
_AssociationElan_Type = DisplayString
_AssociationElan_Object = MibTableColumn
associationElan = _AssociationElan_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 5),
    _AssociationElan_Type()
)
associationElan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    associationElan.setStatus("mandatory")


class _AssociationRowStatus_Type(Integer32):
    """Custom type associationRowStatus based on Integer32"""
    defaultValue = 1

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


_AssociationRowStatus_Type.__name__ = "Integer32"
_AssociationRowStatus_Object = MibTableColumn
associationRowStatus = _AssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 6),
    _AssociationRowStatus_Type()
)
associationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    associationRowStatus.setStatus("mandatory")


class _AssociationIfIndex_Type(Integer32):
    """Custom type associationIfIndex based on Integer32"""
    defaultValue = 0


_AssociationIfIndex_Object = MibTableColumn
associationIfIndex = _AssociationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 7),
    _AssociationIfIndex_Type()
)
associationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationIfIndex.setStatus("mandatory")
_Cti_ObjectIdentity = ObjectIdentity
cti = _Cti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 29)
)
_GenCTIGroup_ObjectIdentity = ObjectIdentity
genCTIGroup = _GenCTIGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 29, 1)
)
_GenCTIGroupTable_Object = MibTable
genCTIGroupTable = _GenCTIGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1)
)
if mibBuilder.loadTexts:
    genCTIGroupTable.setStatus("mandatory")
_GenCTIGroupEntry_Object = MibTableRow
genCTIGroupEntry = _GenCTIGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1)
)
genCTIGroupEntry.setIndexNames(
    (0, "ATMEDGE-MIB", "genCTIGroupId"),
)
if mibBuilder.loadTexts:
    genCTIGroupEntry.setStatus("mandatory")
_GenCTIGroupId_Type = Integer32
_GenCTIGroupId_Object = MibTableColumn
genCTIGroupId = _GenCTIGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 1),
    _GenCTIGroupId_Type()
)
genCTIGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIGroupId.setStatus("mandatory")


class _GenCTIGroupCellLossAlarm_Type(Integer32):
    """Custom type genCTIGroupCellLossAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cellLossAlarm", 2),
          ("ok", 1))
    )


_GenCTIGroupCellLossAlarm_Type.__name__ = "Integer32"
_GenCTIGroupCellLossAlarm_Object = MibTableColumn
genCTIGroupCellLossAlarm = _GenCTIGroupCellLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 2),
    _GenCTIGroupCellLossAlarm_Type()
)
genCTIGroupCellLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIGroupCellLossAlarm.setStatus("mandatory")


class _GenCTIGroupRedunAvailable_Type(Integer32):
    """Custom type genCTIGroupRedunAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRedun", 1),
          ("redunAvailable", 2))
    )


_GenCTIGroupRedunAvailable_Type.__name__ = "Integer32"
_GenCTIGroupRedunAvailable_Object = MibTableColumn
genCTIGroupRedunAvailable = _GenCTIGroupRedunAvailable_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 3),
    _GenCTIGroupRedunAvailable_Type()
)
genCTIGroupRedunAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIGroupRedunAvailable.setStatus("mandatory")


class _GenCTIGroupRedunFlip_Type(Integer32):
    """Custom type genCTIGroupRedunFlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flipFiber", 2),
          ("noFlip", 1))
    )


_GenCTIGroupRedunFlip_Type.__name__ = "Integer32"
_GenCTIGroupRedunFlip_Object = MibTableColumn
genCTIGroupRedunFlip = _GenCTIGroupRedunFlip_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 4),
    _GenCTIGroupRedunFlip_Type()
)
genCTIGroupRedunFlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genCTIGroupRedunFlip.setStatus("mandatory")


class _GenCTIGroupFiberActive_Type(Integer32):
    """Custom type genCTIGroupFiberActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiberActiveA", 1),
          ("fiberActiveB", 2))
    )


_GenCTIGroupFiberActive_Type.__name__ = "Integer32"
_GenCTIGroupFiberActive_Object = MibTableColumn
genCTIGroupFiberActive = _GenCTIGroupFiberActive_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 5),
    _GenCTIGroupFiberActive_Type()
)
genCTIGroupFiberActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIGroupFiberActive.setStatus("mandatory")


class _GenCTIGroupVmuxMaster_Type(Integer32):
    """Custom type genCTIGroupVmuxMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localMaster", 1),
          ("localSlave", 2))
    )


_GenCTIGroupVmuxMaster_Type.__name__ = "Integer32"
_GenCTIGroupVmuxMaster_Object = MibTableColumn
genCTIGroupVmuxMaster = _GenCTIGroupVmuxMaster_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 6),
    _GenCTIGroupVmuxMaster_Type()
)
genCTIGroupVmuxMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIGroupVmuxMaster.setStatus("mandatory")
_GenCTIPortTable_Object = MibTable
genCTIPortTable = _GenCTIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 2)
)
if mibBuilder.loadTexts:
    genCTIPortTable.setStatus("mandatory")
_GenCTIPortEntry_Object = MibTableRow
genCTIPortEntry = _GenCTIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1)
)
genCTIPortEntry.setIndexNames(
    (0, "ATMEDGE-MIB", "genCTIPortGroupId"),
    (0, "ATMEDGE-MIB", "genCTIPortId"),
)
if mibBuilder.loadTexts:
    genCTIPortEntry.setStatus("mandatory")
_GenCTIPortGroupId_Type = Integer32
_GenCTIPortGroupId_Object = MibTableColumn
genCTIPortGroupId = _GenCTIPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 1),
    _GenCTIPortGroupId_Type()
)
genCTIPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIPortGroupId.setStatus("mandatory")
_GenCTIPortId_Type = Integer32
_GenCTIPortId_Object = MibTableColumn
genCTIPortId = _GenCTIPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 2),
    _GenCTIPortId_Type()
)
genCTIPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIPortId.setStatus("mandatory")


class _GenCTIPortSync_Type(Integer32):
    """Custom type genCTIPortSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_GenCTIPortSync_Type.__name__ = "Integer32"
_GenCTIPortSync_Object = MibTableColumn
genCTIPortSync = _GenCTIPortSync_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 3),
    _GenCTIPortSync_Type()
)
genCTIPortSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIPortSync.setStatus("mandatory")


class _GenCTIPortRxAlarm_Type(Integer32):
    """Custom type genCTIPortRxAlarm based on Integer32"""
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
          ("ok", 1),
          ("rxAlarm", 2))
    )


_GenCTIPortRxAlarm_Type.__name__ = "Integer32"
_GenCTIPortRxAlarm_Object = MibTableColumn
genCTIPortRxAlarm = _GenCTIPortRxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 4),
    _GenCTIPortRxAlarm_Type()
)
genCTIPortRxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIPortRxAlarm.setStatus("mandatory")


class _GenCTIPortTxAlarm_Type(Integer32):
    """Custom type genCTIPortTxAlarm based on Integer32"""
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
          ("ok", 1),
          ("txAlarm", 2))
    )


_GenCTIPortTxAlarm_Type.__name__ = "Integer32"
_GenCTIPortTxAlarm_Object = MibTableColumn
genCTIPortTxAlarm = _GenCTIPortTxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 5),
    _GenCTIPortTxAlarm_Type()
)
genCTIPortTxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCTIPortTxAlarm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATMEDGE-MIB",
    **{"atmEdge": atmEdge,
       "atmEdgePort": atmEdgePort,
       "atmEdgePortTable": atmEdgePortTable,
       "atmEdgePortEntry": atmEdgePortEntry,
       "atmEdgePortGroupId": atmEdgePortGroupId,
       "atmEdgePortId": atmEdgePortId,
       "atmEdgePortHealthStatus": atmEdgePortHealthStatus,
       "atmEdgePortMACAddr": atmEdgePortMACAddr,
       "atmEdgePortATMAddr": atmEdgePortATMAddr,
       "atmEdgePortLanType": atmEdgePortLanType,
       "atmEdgePortILMIStatus": atmEdgePortILMIStatus,
       "atmEdgePortSignalStatus": atmEdgePortSignalStatus,
       "atmEdgePortActualUNIVersion": atmEdgePortActualUNIVersion,
       "atmEdgePortNetworkPrefix": atmEdgePortNetworkPrefix,
       "atmEdgePortDormantHealthStatus": atmEdgePortDormantHealthStatus,
       "atmEdgePortRedundancyStatus": atmEdgePortRedundancyStatus,
       "atmEdgeGroup": atmEdgeGroup,
       "atmEdgeGroupTable": atmEdgeGroupTable,
       "atmEdgeGroupEntry": atmEdgeGroupEntry,
       "atmEdgeGroupGroupId": atmEdgeGroupGroupId,
       "atmEdgeGroupWorkState": atmEdgeGroupWorkState,
       "atmEdgeGroupBITResult": atmEdgeGroupBITResult,
       "atmEdgeAssociation": atmEdgeAssociation,
       "associationTable": associationTable,
       "associationEntry": associationEntry,
       "associationSlotIndex": associationSlotIndex,
       "associationPortIndex": associationPortIndex,
       "associationIndex": associationIndex,
       "associationVlan": associationVlan,
       "associationElan": associationElan,
       "associationRowStatus": associationRowStatus,
       "associationIfIndex": associationIfIndex,
       "cti": cti,
       "genCTIGroup": genCTIGroup,
       "genCTIGroupTable": genCTIGroupTable,
       "genCTIGroupEntry": genCTIGroupEntry,
       "genCTIGroupId": genCTIGroupId,
       "genCTIGroupCellLossAlarm": genCTIGroupCellLossAlarm,
       "genCTIGroupRedunAvailable": genCTIGroupRedunAvailable,
       "genCTIGroupRedunFlip": genCTIGroupRedunFlip,
       "genCTIGroupFiberActive": genCTIGroupFiberActive,
       "genCTIGroupVmuxMaster": genCTIGroupVmuxMaster,
       "genCTIPortTable": genCTIPortTable,
       "genCTIPortEntry": genCTIPortEntry,
       "genCTIPortGroupId": genCTIPortGroupId,
       "genCTIPortId": genCTIPortId,
       "genCTIPortSync": genCTIPortSync,
       "genCTIPortRxAlarm": genCTIPortRxAlarm,
       "genCTIPortTxAlarm": genCTIPortTxAlarm}
)
