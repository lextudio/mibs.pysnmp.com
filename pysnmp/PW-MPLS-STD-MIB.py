# SNMP MIB module (PW-MPLS-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PW-MPLS-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:18 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(MplsLdpIdentifier,
 MplsLsrIdentifier,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLdpIdentifier",
    "MplsLsrIdentifier",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

(PwIndexType,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

pwMplsStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 181)
)
pwMplsStdMIB.setRevisions(
        ("2009-06-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PwMplsNotifications_ObjectIdentity = ObjectIdentity
pwMplsNotifications = _PwMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 181, 0)
)
_PwMplsObjects_ObjectIdentity = ObjectIdentity
pwMplsObjects = _PwMplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 181, 1)
)
_PwMplsTable_Object = MibTable
pwMplsTable = _PwMplsTable_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1)
)
if mibBuilder.loadTexts:
    pwMplsTable.setStatus("current")
_PwMplsEntry_Object = MibTableRow
pwMplsEntry = _PwMplsEntry_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1)
)
pwMplsEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwMplsEntry.setStatus("current")


class _PwMplsMplsType_Type(Bits):
    """Custom type pwMplsMplsType based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("mplsNonTe", 1),
          ("mplsTe", 0),
          ("pwOnly", 2))
    )

_PwMplsMplsType_Type.__name__ = "Bits"
_PwMplsMplsType_Object = MibTableColumn
pwMplsMplsType = _PwMplsMplsType_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 1),
    _PwMplsMplsType_Type()
)
pwMplsMplsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsMplsType.setStatus("current")


class _PwMplsExpBitsMode_Type(Integer32):
    """Custom type pwMplsExpBitsMode based on Integer32"""
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
        *(("outerTunnel", 1),
          ("serviceDependant", 3),
          ("specifiedValue", 2))
    )


_PwMplsExpBitsMode_Type.__name__ = "Integer32"
_PwMplsExpBitsMode_Object = MibTableColumn
pwMplsExpBitsMode = _PwMplsExpBitsMode_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 2),
    _PwMplsExpBitsMode_Type()
)
pwMplsExpBitsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsExpBitsMode.setStatus("current")


class _PwMplsExpBits_Type(Unsigned32):
    """Custom type pwMplsExpBits based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PwMplsExpBits_Type.__name__ = "Unsigned32"
_PwMplsExpBits_Object = MibTableColumn
pwMplsExpBits = _PwMplsExpBits_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 3),
    _PwMplsExpBits_Type()
)
pwMplsExpBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsExpBits.setStatus("current")


class _PwMplsTtl_Type(Unsigned32):
    """Custom type pwMplsTtl based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PwMplsTtl_Type.__name__ = "Unsigned32"
_PwMplsTtl_Object = MibTableColumn
pwMplsTtl = _PwMplsTtl_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 4),
    _PwMplsTtl_Type()
)
pwMplsTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsTtl.setStatus("current")
_PwMplsLocalLdpID_Type = MplsLdpIdentifier
_PwMplsLocalLdpID_Object = MibTableColumn
pwMplsLocalLdpID = _PwMplsLocalLdpID_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 5),
    _PwMplsLocalLdpID_Type()
)
pwMplsLocalLdpID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsLocalLdpID.setStatus("current")


class _PwMplsLocalLdpEntityIndex_Type(Unsigned32):
    """Custom type pwMplsLocalLdpEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PwMplsLocalLdpEntityIndex_Type.__name__ = "Unsigned32"
_PwMplsLocalLdpEntityIndex_Object = MibTableColumn
pwMplsLocalLdpEntityIndex = _PwMplsLocalLdpEntityIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 6),
    _PwMplsLocalLdpEntityIndex_Type()
)
pwMplsLocalLdpEntityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsLocalLdpEntityIndex.setStatus("current")
_PwMplsPeerLdpID_Type = MplsLdpIdentifier
_PwMplsPeerLdpID_Object = MibTableColumn
pwMplsPeerLdpID = _PwMplsPeerLdpID_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 7),
    _PwMplsPeerLdpID_Type()
)
pwMplsPeerLdpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsPeerLdpID.setStatus("current")


class _PwMplsStorageType_Type(StorageType):
    """Custom type pwMplsStorageType based on StorageType"""


_PwMplsStorageType_Object = MibTableColumn
pwMplsStorageType = _PwMplsStorageType_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 1, 1, 8),
    _PwMplsStorageType_Type()
)
pwMplsStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsStorageType.setStatus("current")
_PwMplsOutboundTable_Object = MibTable
pwMplsOutboundTable = _PwMplsOutboundTable_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2)
)
if mibBuilder.loadTexts:
    pwMplsOutboundTable.setStatus("current")
_PwMplsOutboundEntry_Object = MibTableRow
pwMplsOutboundEntry = _PwMplsOutboundEntry_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pwMplsOutboundEntry.setStatus("current")
_PwMplsOutboundLsrXcIndex_Type = MplsIndexType
_PwMplsOutboundLsrXcIndex_Object = MibTableColumn
pwMplsOutboundLsrXcIndex = _PwMplsOutboundLsrXcIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1, 1),
    _PwMplsOutboundLsrXcIndex_Type()
)
pwMplsOutboundLsrXcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsOutboundLsrXcIndex.setStatus("current")
_PwMplsOutboundTunnelIndex_Type = MplsTunnelIndex
_PwMplsOutboundTunnelIndex_Object = MibTableColumn
pwMplsOutboundTunnelIndex = _PwMplsOutboundTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1, 2),
    _PwMplsOutboundTunnelIndex_Type()
)
pwMplsOutboundTunnelIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsOutboundTunnelIndex.setStatus("current")
_PwMplsOutboundTunnelInstance_Type = MplsTunnelInstanceIndex
_PwMplsOutboundTunnelInstance_Object = MibTableColumn
pwMplsOutboundTunnelInstance = _PwMplsOutboundTunnelInstance_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1, 3),
    _PwMplsOutboundTunnelInstance_Type()
)
pwMplsOutboundTunnelInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsOutboundTunnelInstance.setStatus("current")
_PwMplsOutboundTunnelLclLSR_Type = MplsLsrIdentifier
_PwMplsOutboundTunnelLclLSR_Object = MibTableColumn
pwMplsOutboundTunnelLclLSR = _PwMplsOutboundTunnelLclLSR_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1, 4),
    _PwMplsOutboundTunnelLclLSR_Type()
)
pwMplsOutboundTunnelLclLSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsOutboundTunnelLclLSR.setStatus("current")
_PwMplsOutboundTunnelPeerLSR_Type = MplsLsrIdentifier
_PwMplsOutboundTunnelPeerLSR_Object = MibTableColumn
pwMplsOutboundTunnelPeerLSR = _PwMplsOutboundTunnelPeerLSR_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1, 5),
    _PwMplsOutboundTunnelPeerLSR_Type()
)
pwMplsOutboundTunnelPeerLSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsOutboundTunnelPeerLSR.setStatus("current")
_PwMplsOutboundIfIndex_Type = InterfaceIndexOrZero
_PwMplsOutboundIfIndex_Object = MibTableColumn
pwMplsOutboundIfIndex = _PwMplsOutboundIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1, 6),
    _PwMplsOutboundIfIndex_Type()
)
pwMplsOutboundIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMplsOutboundIfIndex.setStatus("current")


class _PwMplsOutboundTunnelTypeInUse_Type(Integer32):
    """Custom type pwMplsOutboundTunnelTypeInUse based on Integer32"""
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
        *(("mplsNonTe", 3),
          ("mplsTe", 2),
          ("notYetKnown", 1),
          ("pwOnly", 4))
    )


_PwMplsOutboundTunnelTypeInUse_Type.__name__ = "Integer32"
_PwMplsOutboundTunnelTypeInUse_Object = MibTableColumn
pwMplsOutboundTunnelTypeInUse = _PwMplsOutboundTunnelTypeInUse_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 2, 1, 7),
    _PwMplsOutboundTunnelTypeInUse_Type()
)
pwMplsOutboundTunnelTypeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsOutboundTunnelTypeInUse.setStatus("current")
_PwMplsInboundTable_Object = MibTable
pwMplsInboundTable = _PwMplsInboundTable_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 3)
)
if mibBuilder.loadTexts:
    pwMplsInboundTable.setStatus("current")
_PwMplsInboundEntry_Object = MibTableRow
pwMplsInboundEntry = _PwMplsInboundEntry_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 3, 1)
)
pwMplsInboundEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwMplsInboundEntry.setStatus("current")
_PwMplsInboundXcIndex_Type = MplsIndexType
_PwMplsInboundXcIndex_Object = MibTableColumn
pwMplsInboundXcIndex = _PwMplsInboundXcIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 3, 1, 1),
    _PwMplsInboundXcIndex_Type()
)
pwMplsInboundXcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsInboundXcIndex.setStatus("current")
_PwMplsNonTeMappingTable_Object = MibTable
pwMplsNonTeMappingTable = _PwMplsNonTeMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 4)
)
if mibBuilder.loadTexts:
    pwMplsNonTeMappingTable.setStatus("current")
_PwMplsNonTeMappingEntry_Object = MibTableRow
pwMplsNonTeMappingEntry = _PwMplsNonTeMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 4, 1)
)
pwMplsNonTeMappingEntry.setIndexNames(
    (0, "PW-MPLS-STD-MIB", "pwMplsNonTeMappingDirection"),
    (0, "PW-MPLS-STD-MIB", "pwMplsNonTeMappingXcIndex"),
    (0, "PW-MPLS-STD-MIB", "pwMplsNonTeMappingIfIndex"),
    (0, "PW-MPLS-STD-MIB", "pwMplsNonTeMappingPwIndex"),
)
if mibBuilder.loadTexts:
    pwMplsNonTeMappingEntry.setStatus("current")


class _PwMplsNonTeMappingDirection_Type(Integer32):
    """Custom type pwMplsNonTeMappingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromPsn", 2),
          ("psnBound", 1))
    )


_PwMplsNonTeMappingDirection_Type.__name__ = "Integer32"
_PwMplsNonTeMappingDirection_Object = MibTableColumn
pwMplsNonTeMappingDirection = _PwMplsNonTeMappingDirection_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 4, 1, 1),
    _PwMplsNonTeMappingDirection_Type()
)
pwMplsNonTeMappingDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwMplsNonTeMappingDirection.setStatus("current")
_PwMplsNonTeMappingXcIndex_Type = MplsIndexType
_PwMplsNonTeMappingXcIndex_Object = MibTableColumn
pwMplsNonTeMappingXcIndex = _PwMplsNonTeMappingXcIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 4, 1, 2),
    _PwMplsNonTeMappingXcIndex_Type()
)
pwMplsNonTeMappingXcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwMplsNonTeMappingXcIndex.setStatus("current")
_PwMplsNonTeMappingIfIndex_Type = InterfaceIndexOrZero
_PwMplsNonTeMappingIfIndex_Object = MibTableColumn
pwMplsNonTeMappingIfIndex = _PwMplsNonTeMappingIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 4, 1, 3),
    _PwMplsNonTeMappingIfIndex_Type()
)
pwMplsNonTeMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwMplsNonTeMappingIfIndex.setStatus("current")
_PwMplsNonTeMappingPwIndex_Type = PwIndexType
_PwMplsNonTeMappingPwIndex_Object = MibTableColumn
pwMplsNonTeMappingPwIndex = _PwMplsNonTeMappingPwIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 4, 1, 4),
    _PwMplsNonTeMappingPwIndex_Type()
)
pwMplsNonTeMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsNonTeMappingPwIndex.setStatus("current")
_PwMplsTeMappingTable_Object = MibTable
pwMplsTeMappingTable = _PwMplsTeMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 5)
)
if mibBuilder.loadTexts:
    pwMplsTeMappingTable.setStatus("current")
_PwMplsTeMappingEntry_Object = MibTableRow
pwMplsTeMappingEntry = _PwMplsTeMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 5, 1)
)
pwMplsTeMappingEntry.setIndexNames(
    (0, "PW-MPLS-STD-MIB", "pwMplsTeMappingTunnelIndex"),
    (0, "PW-MPLS-STD-MIB", "pwMplsTeMappingTunnelInstance"),
    (0, "PW-MPLS-STD-MIB", "pwMplsTeMappingTunnelPeerLsrID"),
    (0, "PW-MPLS-STD-MIB", "pwMplsTeMappingTunnelLocalLsrID"),
    (0, "PW-MPLS-STD-MIB", "pwMplsTeMappingPwIndex"),
)
if mibBuilder.loadTexts:
    pwMplsTeMappingEntry.setStatus("current")
_PwMplsTeMappingTunnelIndex_Type = MplsTunnelIndex
_PwMplsTeMappingTunnelIndex_Object = MibTableColumn
pwMplsTeMappingTunnelIndex = _PwMplsTeMappingTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 5, 1, 1),
    _PwMplsTeMappingTunnelIndex_Type()
)
pwMplsTeMappingTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwMplsTeMappingTunnelIndex.setStatus("current")
_PwMplsTeMappingTunnelInstance_Type = MplsTunnelInstanceIndex
_PwMplsTeMappingTunnelInstance_Object = MibTableColumn
pwMplsTeMappingTunnelInstance = _PwMplsTeMappingTunnelInstance_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 5, 1, 2),
    _PwMplsTeMappingTunnelInstance_Type()
)
pwMplsTeMappingTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwMplsTeMappingTunnelInstance.setStatus("current")
_PwMplsTeMappingTunnelPeerLsrID_Type = MplsLsrIdentifier
_PwMplsTeMappingTunnelPeerLsrID_Object = MibTableColumn
pwMplsTeMappingTunnelPeerLsrID = _PwMplsTeMappingTunnelPeerLsrID_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 5, 1, 3),
    _PwMplsTeMappingTunnelPeerLsrID_Type()
)
pwMplsTeMappingTunnelPeerLsrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwMplsTeMappingTunnelPeerLsrID.setStatus("current")
_PwMplsTeMappingTunnelLocalLsrID_Type = MplsLsrIdentifier
_PwMplsTeMappingTunnelLocalLsrID_Object = MibTableColumn
pwMplsTeMappingTunnelLocalLsrID = _PwMplsTeMappingTunnelLocalLsrID_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 5, 1, 4),
    _PwMplsTeMappingTunnelLocalLsrID_Type()
)
pwMplsTeMappingTunnelLocalLsrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwMplsTeMappingTunnelLocalLsrID.setStatus("current")
_PwMplsTeMappingPwIndex_Type = PwIndexType
_PwMplsTeMappingPwIndex_Object = MibTableColumn
pwMplsTeMappingPwIndex = _PwMplsTeMappingPwIndex_Object(
    (1, 3, 6, 1, 2, 1, 181, 1, 5, 1, 5),
    _PwMplsTeMappingPwIndex_Type()
)
pwMplsTeMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMplsTeMappingPwIndex.setStatus("current")
_PwMplsConformance_ObjectIdentity = ObjectIdentity
pwMplsConformance = _PwMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 181, 2)
)
_PwMplsGroups_ObjectIdentity = ObjectIdentity
pwMplsGroups = _PwMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 181, 2, 1)
)
_PwMplsCompliances_ObjectIdentity = ObjectIdentity
pwMplsCompliances = _PwMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 181, 2, 2)
)
pwMplsEntry.registerAugmentions(
    ("PW-MPLS-STD-MIB",
     "pwMplsOutboundEntry")
)
pwMplsOutboundEntry.setIndexNames(*pwMplsEntry.getIndexNames())

# Managed Objects groups

pwMplsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 181, 2, 1, 1)
)
pwMplsGroup.setObjects(
      *(("PW-MPLS-STD-MIB", "pwMplsMplsType"),
        ("PW-MPLS-STD-MIB", "pwMplsExpBitsMode"),
        ("PW-MPLS-STD-MIB", "pwMplsExpBits"),
        ("PW-MPLS-STD-MIB", "pwMplsTtl"),
        ("PW-MPLS-STD-MIB", "pwMplsLocalLdpID"),
        ("PW-MPLS-STD-MIB", "pwMplsLocalLdpEntityIndex"),
        ("PW-MPLS-STD-MIB", "pwMplsPeerLdpID"),
        ("PW-MPLS-STD-MIB", "pwMplsStorageType"))
)
if mibBuilder.loadTexts:
    pwMplsGroup.setStatus("current")

pwMplsOutboundMainGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 181, 2, 1, 2)
)
pwMplsOutboundMainGroup.setObjects(
      *(("PW-MPLS-STD-MIB", "pwMplsOutboundLsrXcIndex"),
        ("PW-MPLS-STD-MIB", "pwMplsOutboundIfIndex"),
        ("PW-MPLS-STD-MIB", "pwMplsOutboundTunnelTypeInUse"))
)
if mibBuilder.loadTexts:
    pwMplsOutboundMainGroup.setStatus("current")

pwMplsOutboundTeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 181, 2, 1, 3)
)
pwMplsOutboundTeGroup.setObjects(
      *(("PW-MPLS-STD-MIB", "pwMplsOutboundTunnelIndex"),
        ("PW-MPLS-STD-MIB", "pwMplsOutboundTunnelInstance"),
        ("PW-MPLS-STD-MIB", "pwMplsOutboundTunnelLclLSR"),
        ("PW-MPLS-STD-MIB", "pwMplsOutboundTunnelPeerLSR"))
)
if mibBuilder.loadTexts:
    pwMplsOutboundTeGroup.setStatus("current")

pwMplsInboundGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 181, 2, 1, 4)
)
pwMplsInboundGroup.setObjects(
    ("PW-MPLS-STD-MIB", "pwMplsInboundXcIndex")
)
if mibBuilder.loadTexts:
    pwMplsInboundGroup.setStatus("current")

pwMplsMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 181, 2, 1, 5)
)
pwMplsMappingGroup.setObjects(
      *(("PW-MPLS-STD-MIB", "pwMplsNonTeMappingPwIndex"),
        ("PW-MPLS-STD-MIB", "pwMplsTeMappingPwIndex"))
)
if mibBuilder.loadTexts:
    pwMplsMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pwMplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 181, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pwMplsModuleFullCompliance.setStatus(
        "current"
    )

pwMplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 181, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pwMplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PW-MPLS-STD-MIB",
    **{"pwMplsStdMIB": pwMplsStdMIB,
       "pwMplsNotifications": pwMplsNotifications,
       "pwMplsObjects": pwMplsObjects,
       "pwMplsTable": pwMplsTable,
       "pwMplsEntry": pwMplsEntry,
       "pwMplsMplsType": pwMplsMplsType,
       "pwMplsExpBitsMode": pwMplsExpBitsMode,
       "pwMplsExpBits": pwMplsExpBits,
       "pwMplsTtl": pwMplsTtl,
       "pwMplsLocalLdpID": pwMplsLocalLdpID,
       "pwMplsLocalLdpEntityIndex": pwMplsLocalLdpEntityIndex,
       "pwMplsPeerLdpID": pwMplsPeerLdpID,
       "pwMplsStorageType": pwMplsStorageType,
       "pwMplsOutboundTable": pwMplsOutboundTable,
       "pwMplsOutboundEntry": pwMplsOutboundEntry,
       "pwMplsOutboundLsrXcIndex": pwMplsOutboundLsrXcIndex,
       "pwMplsOutboundTunnelIndex": pwMplsOutboundTunnelIndex,
       "pwMplsOutboundTunnelInstance": pwMplsOutboundTunnelInstance,
       "pwMplsOutboundTunnelLclLSR": pwMplsOutboundTunnelLclLSR,
       "pwMplsOutboundTunnelPeerLSR": pwMplsOutboundTunnelPeerLSR,
       "pwMplsOutboundIfIndex": pwMplsOutboundIfIndex,
       "pwMplsOutboundTunnelTypeInUse": pwMplsOutboundTunnelTypeInUse,
       "pwMplsInboundTable": pwMplsInboundTable,
       "pwMplsInboundEntry": pwMplsInboundEntry,
       "pwMplsInboundXcIndex": pwMplsInboundXcIndex,
       "pwMplsNonTeMappingTable": pwMplsNonTeMappingTable,
       "pwMplsNonTeMappingEntry": pwMplsNonTeMappingEntry,
       "pwMplsNonTeMappingDirection": pwMplsNonTeMappingDirection,
       "pwMplsNonTeMappingXcIndex": pwMplsNonTeMappingXcIndex,
       "pwMplsNonTeMappingIfIndex": pwMplsNonTeMappingIfIndex,
       "pwMplsNonTeMappingPwIndex": pwMplsNonTeMappingPwIndex,
       "pwMplsTeMappingTable": pwMplsTeMappingTable,
       "pwMplsTeMappingEntry": pwMplsTeMappingEntry,
       "pwMplsTeMappingTunnelIndex": pwMplsTeMappingTunnelIndex,
       "pwMplsTeMappingTunnelInstance": pwMplsTeMappingTunnelInstance,
       "pwMplsTeMappingTunnelPeerLsrID": pwMplsTeMappingTunnelPeerLsrID,
       "pwMplsTeMappingTunnelLocalLsrID": pwMplsTeMappingTunnelLocalLsrID,
       "pwMplsTeMappingPwIndex": pwMplsTeMappingPwIndex,
       "pwMplsConformance": pwMplsConformance,
       "pwMplsGroups": pwMplsGroups,
       "pwMplsGroup": pwMplsGroup,
       "pwMplsOutboundMainGroup": pwMplsOutboundMainGroup,
       "pwMplsOutboundTeGroup": pwMplsOutboundTeGroup,
       "pwMplsInboundGroup": pwMplsInboundGroup,
       "pwMplsMappingGroup": pwMplsMappingGroup,
       "pwMplsCompliances": pwMplsCompliances,
       "pwMplsModuleFullCompliance": pwMplsModuleFullCompliance,
       "pwMplsModuleReadOnlyCompliance": pwMplsModuleReadOnlyCompliance}
)
