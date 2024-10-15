# SNMP MIB module (CISCO-IETF-PW-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PW-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:58 2024
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

(cpwVcIndex,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-MIB",
    "cpwVcIndex")

(CpwVcIndexType,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-TC-MIB",
    "CpwVcIndexType")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(MplsLdpIdentifier,
 MplsLsrIdentifier,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLdpIdentifier",
    "MplsLsrIdentifier",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

cpwVcMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 107)
)
cpwVcMplsMIB.setRevisions(
        ("2003-02-26 12:00",
         "2002-06-02 12:00",
         "2002-01-29 12:00",
         "2001-07-11 12:00",
         "2001-07-11 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpwVcMplsNotifications_ObjectIdentity = ObjectIdentity
cpwVcMplsNotifications = _CpwVcMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 0)
)
_CpwVcMplsNotifyPrefix_ObjectIdentity = ObjectIdentity
cpwVcMplsNotifyPrefix = _CpwVcMplsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 0, 0)
)
_CpwVcMplsObjects_ObjectIdentity = ObjectIdentity
cpwVcMplsObjects = _CpwVcMplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1)
)
_CpwVcMplsTable_Object = MibTable
cpwVcMplsTable = _CpwVcMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1)
)
if mibBuilder.loadTexts:
    cpwVcMplsTable.setStatus("current")
_CpwVcMplsEntry_Object = MibTableRow
cpwVcMplsEntry = _CpwVcMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1)
)
cpwVcMplsEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcMplsEntry.setStatus("current")


class _CpwVcMplsMplsType_Type(Bits):
    """Custom type cpwVcMplsMplsType based on Bits"""
    namedValues = NamedValues(
        *(("mplsNonTe", 1),
          ("mplsTe", 0),
          ("vcOnly", 2))
    )

_CpwVcMplsMplsType_Type.__name__ = "Bits"
_CpwVcMplsMplsType_Object = MibTableColumn
cpwVcMplsMplsType = _CpwVcMplsMplsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 1),
    _CpwVcMplsMplsType_Type()
)
cpwVcMplsMplsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcMplsMplsType.setStatus("current")


class _CpwVcMplsExpBitsMode_Type(Integer32):
    """Custom type cpwVcMplsExpBitsMode based on Integer32"""
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


_CpwVcMplsExpBitsMode_Type.__name__ = "Integer32"
_CpwVcMplsExpBitsMode_Object = MibTableColumn
cpwVcMplsExpBitsMode = _CpwVcMplsExpBitsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 2),
    _CpwVcMplsExpBitsMode_Type()
)
cpwVcMplsExpBitsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcMplsExpBitsMode.setStatus("current")


class _CpwVcMplsExpBits_Type(Unsigned32):
    """Custom type cpwVcMplsExpBits based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CpwVcMplsExpBits_Type.__name__ = "Unsigned32"
_CpwVcMplsExpBits_Object = MibTableColumn
cpwVcMplsExpBits = _CpwVcMplsExpBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 3),
    _CpwVcMplsExpBits_Type()
)
cpwVcMplsExpBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcMplsExpBits.setStatus("current")


class _CpwVcMplsTtl_Type(Unsigned32):
    """Custom type cpwVcMplsTtl based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpwVcMplsTtl_Type.__name__ = "Unsigned32"
_CpwVcMplsTtl_Object = MibTableColumn
cpwVcMplsTtl = _CpwVcMplsTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 4),
    _CpwVcMplsTtl_Type()
)
cpwVcMplsTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcMplsTtl.setStatus("current")
_CpwVcMplsLocalLdpID_Type = MplsLdpIdentifier
_CpwVcMplsLocalLdpID_Object = MibTableColumn
cpwVcMplsLocalLdpID = _CpwVcMplsLocalLdpID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 5),
    _CpwVcMplsLocalLdpID_Type()
)
cpwVcMplsLocalLdpID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcMplsLocalLdpID.setStatus("current")
_CpwVcMplsLocalLdpEntityID_Type = Unsigned32
_CpwVcMplsLocalLdpEntityID_Object = MibTableColumn
cpwVcMplsLocalLdpEntityID = _CpwVcMplsLocalLdpEntityID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 6),
    _CpwVcMplsLocalLdpEntityID_Type()
)
cpwVcMplsLocalLdpEntityID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcMplsLocalLdpEntityID.setStatus("current")
_CpwVcMplsPeerLdpID_Type = MplsLdpIdentifier
_CpwVcMplsPeerLdpID_Object = MibTableColumn
cpwVcMplsPeerLdpID = _CpwVcMplsPeerLdpID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 7),
    _CpwVcMplsPeerLdpID_Type()
)
cpwVcMplsPeerLdpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcMplsPeerLdpID.setStatus("current")
_CpwVcMplsStorageType_Type = StorageType
_CpwVcMplsStorageType_Object = MibTableColumn
cpwVcMplsStorageType = _CpwVcMplsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 8),
    _CpwVcMplsStorageType_Type()
)
cpwVcMplsStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcMplsStorageType.setStatus("current")


class _CpwVcMplsOutboundIndexNext_Type(Unsigned32):
    """Custom type cpwVcMplsOutboundIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpwVcMplsOutboundIndexNext_Type.__name__ = "Unsigned32"
_CpwVcMplsOutboundIndexNext_Object = MibScalar
cpwVcMplsOutboundIndexNext = _CpwVcMplsOutboundIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 2),
    _CpwVcMplsOutboundIndexNext_Type()
)
cpwVcMplsOutboundIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundIndexNext.setStatus("current")
_CpwVcMplsOutboundTable_Object = MibTable
cpwVcMplsOutboundTable = _CpwVcMplsOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3)
)
if mibBuilder.loadTexts:
    cpwVcMplsOutboundTable.setStatus("current")
_CpwVcMplsOutboundEntry_Object = MibTableRow
cpwVcMplsOutboundEntry = _CpwVcMplsOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1)
)
cpwVcMplsOutboundEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundIndex"),
)
if mibBuilder.loadTexts:
    cpwVcMplsOutboundEntry.setStatus("current")


class _CpwVcMplsOutboundIndex_Type(Unsigned32):
    """Custom type cpwVcMplsOutboundIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpwVcMplsOutboundIndex_Type.__name__ = "Unsigned32"
_CpwVcMplsOutboundIndex_Object = MibTableColumn
cpwVcMplsOutboundIndex = _CpwVcMplsOutboundIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 1),
    _CpwVcMplsOutboundIndex_Type()
)
cpwVcMplsOutboundIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundIndex.setStatus("current")
_CpwVcMplsOutboundLsrXcIndex_Type = Unsigned32
_CpwVcMplsOutboundLsrXcIndex_Object = MibTableColumn
cpwVcMplsOutboundLsrXcIndex = _CpwVcMplsOutboundLsrXcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 2),
    _CpwVcMplsOutboundLsrXcIndex_Type()
)
cpwVcMplsOutboundLsrXcIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundLsrXcIndex.setStatus("current")
_CpwVcMplsOutboundTunnelIndex_Type = MplsTunnelIndex
_CpwVcMplsOutboundTunnelIndex_Object = MibTableColumn
cpwVcMplsOutboundTunnelIndex = _CpwVcMplsOutboundTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 3),
    _CpwVcMplsOutboundTunnelIndex_Type()
)
cpwVcMplsOutboundTunnelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundTunnelIndex.setStatus("current")
_CpwVcMplsOutboundTunnelInstance_Type = MplsTunnelInstanceIndex
_CpwVcMplsOutboundTunnelInstance_Object = MibTableColumn
cpwVcMplsOutboundTunnelInstance = _CpwVcMplsOutboundTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 4),
    _CpwVcMplsOutboundTunnelInstance_Type()
)
cpwVcMplsOutboundTunnelInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundTunnelInstance.setStatus("current")
_CpwVcMplsOutboundTunnelLclLSR_Type = MplsLsrIdentifier
_CpwVcMplsOutboundTunnelLclLSR_Object = MibTableColumn
cpwVcMplsOutboundTunnelLclLSR = _CpwVcMplsOutboundTunnelLclLSR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 5),
    _CpwVcMplsOutboundTunnelLclLSR_Type()
)
cpwVcMplsOutboundTunnelLclLSR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundTunnelLclLSR.setStatus("current")
_CpwVcMplsOutboundTunnelPeerLSR_Type = MplsLsrIdentifier
_CpwVcMplsOutboundTunnelPeerLSR_Object = MibTableColumn
cpwVcMplsOutboundTunnelPeerLSR = _CpwVcMplsOutboundTunnelPeerLSR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 6),
    _CpwVcMplsOutboundTunnelPeerLSR_Type()
)
cpwVcMplsOutboundTunnelPeerLSR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundTunnelPeerLSR.setStatus("current")
_CpwVcMplsOutboundIfIndex_Type = InterfaceIndexOrZero
_CpwVcMplsOutboundIfIndex_Object = MibTableColumn
cpwVcMplsOutboundIfIndex = _CpwVcMplsOutboundIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 7),
    _CpwVcMplsOutboundIfIndex_Type()
)
cpwVcMplsOutboundIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundIfIndex.setStatus("current")
_CpwVcMplsOutboundRowStatus_Type = RowStatus
_CpwVcMplsOutboundRowStatus_Object = MibTableColumn
cpwVcMplsOutboundRowStatus = _CpwVcMplsOutboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 8),
    _CpwVcMplsOutboundRowStatus_Type()
)
cpwVcMplsOutboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundRowStatus.setStatus("current")
_CpwVcMplsOutboundStorageType_Type = StorageType
_CpwVcMplsOutboundStorageType_Object = MibTableColumn
cpwVcMplsOutboundStorageType = _CpwVcMplsOutboundStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 9),
    _CpwVcMplsOutboundStorageType_Type()
)
cpwVcMplsOutboundStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsOutboundStorageType.setStatus("current")


class _CpwVcMplsInboundIndexNext_Type(Unsigned32):
    """Custom type cpwVcMplsInboundIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpwVcMplsInboundIndexNext_Type.__name__ = "Unsigned32"
_CpwVcMplsInboundIndexNext_Object = MibScalar
cpwVcMplsInboundIndexNext = _CpwVcMplsInboundIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 4),
    _CpwVcMplsInboundIndexNext_Type()
)
cpwVcMplsInboundIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcMplsInboundIndexNext.setStatus("current")
_CpwVcMplsInboundTable_Object = MibTable
cpwVcMplsInboundTable = _CpwVcMplsInboundTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5)
)
if mibBuilder.loadTexts:
    cpwVcMplsInboundTable.setStatus("current")
_CpwVcMplsInboundEntry_Object = MibTableRow
cpwVcMplsInboundEntry = _CpwVcMplsInboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1)
)
cpwVcMplsInboundEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundIndex"),
)
if mibBuilder.loadTexts:
    cpwVcMplsInboundEntry.setStatus("current")


class _CpwVcMplsInboundIndex_Type(Unsigned32):
    """Custom type cpwVcMplsInboundIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpwVcMplsInboundIndex_Type.__name__ = "Unsigned32"
_CpwVcMplsInboundIndex_Object = MibTableColumn
cpwVcMplsInboundIndex = _CpwVcMplsInboundIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 1),
    _CpwVcMplsInboundIndex_Type()
)
cpwVcMplsInboundIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsInboundIndex.setStatus("current")
_CpwVcMplsInboundLsrXcIndex_Type = Unsigned32
_CpwVcMplsInboundLsrXcIndex_Object = MibTableColumn
cpwVcMplsInboundLsrXcIndex = _CpwVcMplsInboundLsrXcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 2),
    _CpwVcMplsInboundLsrXcIndex_Type()
)
cpwVcMplsInboundLsrXcIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundLsrXcIndex.setStatus("current")
_CpwVcMplsInboundTunnelIndex_Type = MplsTunnelIndex
_CpwVcMplsInboundTunnelIndex_Object = MibTableColumn
cpwVcMplsInboundTunnelIndex = _CpwVcMplsInboundTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 3),
    _CpwVcMplsInboundTunnelIndex_Type()
)
cpwVcMplsInboundTunnelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundTunnelIndex.setStatus("current")
_CpwVcMplsInboundTunnelInstance_Type = MplsTunnelInstanceIndex
_CpwVcMplsInboundTunnelInstance_Object = MibTableColumn
cpwVcMplsInboundTunnelInstance = _CpwVcMplsInboundTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 4),
    _CpwVcMplsInboundTunnelInstance_Type()
)
cpwVcMplsInboundTunnelInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundTunnelInstance.setStatus("current")
_CpwVcMplsInboundTunnelLclLSR_Type = MplsLsrIdentifier
_CpwVcMplsInboundTunnelLclLSR_Object = MibTableColumn
cpwVcMplsInboundTunnelLclLSR = _CpwVcMplsInboundTunnelLclLSR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 5),
    _CpwVcMplsInboundTunnelLclLSR_Type()
)
cpwVcMplsInboundTunnelLclLSR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundTunnelLclLSR.setStatus("current")
_CpwVcMplsInboundTunnelPeerLSR_Type = MplsLsrIdentifier
_CpwVcMplsInboundTunnelPeerLSR_Object = MibTableColumn
cpwVcMplsInboundTunnelPeerLSR = _CpwVcMplsInboundTunnelPeerLSR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 6),
    _CpwVcMplsInboundTunnelPeerLSR_Type()
)
cpwVcMplsInboundTunnelPeerLSR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundTunnelPeerLSR.setStatus("current")
_CpwVcMplsInboundIfIndex_Type = InterfaceIndexOrZero
_CpwVcMplsInboundIfIndex_Object = MibTableColumn
cpwVcMplsInboundIfIndex = _CpwVcMplsInboundIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 7),
    _CpwVcMplsInboundIfIndex_Type()
)
cpwVcMplsInboundIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundIfIndex.setStatus("current")
_CpwVcMplsInboundRowStatus_Type = RowStatus
_CpwVcMplsInboundRowStatus_Object = MibTableColumn
cpwVcMplsInboundRowStatus = _CpwVcMplsInboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 8),
    _CpwVcMplsInboundRowStatus_Type()
)
cpwVcMplsInboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundRowStatus.setStatus("current")
_CpwVcMplsInboundStorageType_Type = StorageType
_CpwVcMplsInboundStorageType_Object = MibTableColumn
cpwVcMplsInboundStorageType = _CpwVcMplsInboundStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 9),
    _CpwVcMplsInboundStorageType_Type()
)
cpwVcMplsInboundStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcMplsInboundStorageType.setStatus("current")
_CpwVcMplsNonTeMappingTable_Object = MibTable
cpwVcMplsNonTeMappingTable = _CpwVcMplsNonTeMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6)
)
if mibBuilder.loadTexts:
    cpwVcMplsNonTeMappingTable.setStatus("current")
_CpwVcMplsNonTeMappingEntry_Object = MibTableRow
cpwVcMplsNonTeMappingEntry = _CpwVcMplsNonTeMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1)
)
cpwVcMplsNonTeMappingEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingTunnelDirection"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingXcTunnelIndex"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingIfIndex"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcMplsNonTeMappingEntry.setStatus("current")


class _CpwVcMplsNonTeMappingTunnelDirection_Type(Integer32):
    """Custom type cpwVcMplsNonTeMappingTunnelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 2),
          ("outbound", 1))
    )


_CpwVcMplsNonTeMappingTunnelDirection_Type.__name__ = "Integer32"
_CpwVcMplsNonTeMappingTunnelDirection_Object = MibTableColumn
cpwVcMplsNonTeMappingTunnelDirection = _CpwVcMplsNonTeMappingTunnelDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 1),
    _CpwVcMplsNonTeMappingTunnelDirection_Type()
)
cpwVcMplsNonTeMappingTunnelDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsNonTeMappingTunnelDirection.setStatus("current")


class _CpwVcMplsNonTeMappingXcTunnelIndex_Type(Unsigned32):
    """Custom type cpwVcMplsNonTeMappingXcTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpwVcMplsNonTeMappingXcTunnelIndex_Type.__name__ = "Unsigned32"
_CpwVcMplsNonTeMappingXcTunnelIndex_Object = MibTableColumn
cpwVcMplsNonTeMappingXcTunnelIndex = _CpwVcMplsNonTeMappingXcTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 2),
    _CpwVcMplsNonTeMappingXcTunnelIndex_Type()
)
cpwVcMplsNonTeMappingXcTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsNonTeMappingXcTunnelIndex.setStatus("current")
_CpwVcMplsNonTeMappingIfIndex_Type = InterfaceIndexOrZero
_CpwVcMplsNonTeMappingIfIndex_Object = MibTableColumn
cpwVcMplsNonTeMappingIfIndex = _CpwVcMplsNonTeMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 3),
    _CpwVcMplsNonTeMappingIfIndex_Type()
)
cpwVcMplsNonTeMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsNonTeMappingIfIndex.setStatus("current")
_CpwVcMplsNonTeMappingVcIndex_Type = CpwVcIndexType
_CpwVcMplsNonTeMappingVcIndex_Object = MibTableColumn
cpwVcMplsNonTeMappingVcIndex = _CpwVcMplsNonTeMappingVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 4),
    _CpwVcMplsNonTeMappingVcIndex_Type()
)
cpwVcMplsNonTeMappingVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcMplsNonTeMappingVcIndex.setStatus("current")
_CpwVcMplsTeMappingTable_Object = MibTable
cpwVcMplsTeMappingTable = _CpwVcMplsTeMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7)
)
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingTable.setStatus("current")
_CpwVcMplsTeMappingEntry_Object = MibTableRow
cpwVcMplsTeMappingEntry = _CpwVcMplsTeMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1)
)
cpwVcMplsTeMappingEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelDirection"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelIndex"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelInstance"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelPeerLsrID"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelLocalLsrID"),
    (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingEntry.setStatus("current")


class _CpwVcMplsTeMappingTunnelDirection_Type(Integer32):
    """Custom type cpwVcMplsTeMappingTunnelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 2),
          ("outbound", 1))
    )


_CpwVcMplsTeMappingTunnelDirection_Type.__name__ = "Integer32"
_CpwVcMplsTeMappingTunnelDirection_Object = MibTableColumn
cpwVcMplsTeMappingTunnelDirection = _CpwVcMplsTeMappingTunnelDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 1),
    _CpwVcMplsTeMappingTunnelDirection_Type()
)
cpwVcMplsTeMappingTunnelDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingTunnelDirection.setStatus("current")
_CpwVcMplsTeMappingTunnelIndex_Type = MplsTunnelIndex
_CpwVcMplsTeMappingTunnelIndex_Object = MibTableColumn
cpwVcMplsTeMappingTunnelIndex = _CpwVcMplsTeMappingTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 2),
    _CpwVcMplsTeMappingTunnelIndex_Type()
)
cpwVcMplsTeMappingTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingTunnelIndex.setStatus("current")
_CpwVcMplsTeMappingTunnelInstance_Type = MplsTunnelInstanceIndex
_CpwVcMplsTeMappingTunnelInstance_Object = MibTableColumn
cpwVcMplsTeMappingTunnelInstance = _CpwVcMplsTeMappingTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 3),
    _CpwVcMplsTeMappingTunnelInstance_Type()
)
cpwVcMplsTeMappingTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingTunnelInstance.setStatus("current")
_CpwVcMplsTeMappingTunnelPeerLsrID_Type = MplsLsrIdentifier
_CpwVcMplsTeMappingTunnelPeerLsrID_Object = MibTableColumn
cpwVcMplsTeMappingTunnelPeerLsrID = _CpwVcMplsTeMappingTunnelPeerLsrID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 4),
    _CpwVcMplsTeMappingTunnelPeerLsrID_Type()
)
cpwVcMplsTeMappingTunnelPeerLsrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingTunnelPeerLsrID.setStatus("current")
_CpwVcMplsTeMappingTunnelLocalLsrID_Type = MplsLsrIdentifier
_CpwVcMplsTeMappingTunnelLocalLsrID_Object = MibTableColumn
cpwVcMplsTeMappingTunnelLocalLsrID = _CpwVcMplsTeMappingTunnelLocalLsrID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 5),
    _CpwVcMplsTeMappingTunnelLocalLsrID_Type()
)
cpwVcMplsTeMappingTunnelLocalLsrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingTunnelLocalLsrID.setStatus("current")
_CpwVcMplsTeMappingVcIndex_Type = CpwVcIndexType
_CpwVcMplsTeMappingVcIndex_Object = MibTableColumn
cpwVcMplsTeMappingVcIndex = _CpwVcMplsTeMappingVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 6),
    _CpwVcMplsTeMappingVcIndex_Type()
)
cpwVcMplsTeMappingVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcMplsTeMappingVcIndex.setStatus("current")
_CpwVcMplsConformance_ObjectIdentity = ObjectIdentity
cpwVcMplsConformance = _CpwVcMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2)
)
_CpwVcMplsGroups_ObjectIdentity = ObjectIdentity
cpwVcMplsGroups = _CpwVcMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1)
)
_CpwVcMplsCompliances_ObjectIdentity = ObjectIdentity
cpwVcMplsCompliances = _CpwVcMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 2)
)

# Managed Objects groups

cpwVcMplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 1)
)
cpwVcMplsGroup.setObjects(
      *(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsMplsType"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsExpBitsMode"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsExpBits"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTtl"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsLocalLdpID"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsLocalLdpEntityID"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsPeerLdpID"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsStorageType"))
)
if mibBuilder.loadTexts:
    cpwVcMplsGroup.setStatus("current")

cpwVcMplsOutboundGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 2)
)
cpwVcMplsOutboundGroup.setObjects(
      *(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundIndexNext"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundLsrXcIndex"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelIndex"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelInstance"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelLclLSR"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelPeerLSR"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundIfIndex"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundRowStatus"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundStorageType"))
)
if mibBuilder.loadTexts:
    cpwVcMplsOutboundGroup.setStatus("current")

cpwVcMplsInboundGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 3)
)
cpwVcMplsInboundGroup.setObjects(
      *(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundIndexNext"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundLsrXcIndex"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelIndex"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelInstance"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelLclLSR"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelPeerLSR"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundIfIndex"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundRowStatus"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundStorageType"))
)
if mibBuilder.loadTexts:
    cpwVcMplsInboundGroup.setStatus("current")

cpwVcMplsMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 4)
)
cpwVcMplsMappingGroup.setObjects(
      *(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingVcIndex"),
        ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingVcIndex"))
)
if mibBuilder.loadTexts:
    cpwVcMplsMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpwMplsModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpwMplsModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-MPLS-MIB",
    **{"cpwVcMplsMIB": cpwVcMplsMIB,
       "cpwVcMplsNotifications": cpwVcMplsNotifications,
       "cpwVcMplsNotifyPrefix": cpwVcMplsNotifyPrefix,
       "cpwVcMplsObjects": cpwVcMplsObjects,
       "cpwVcMplsTable": cpwVcMplsTable,
       "cpwVcMplsEntry": cpwVcMplsEntry,
       "cpwVcMplsMplsType": cpwVcMplsMplsType,
       "cpwVcMplsExpBitsMode": cpwVcMplsExpBitsMode,
       "cpwVcMplsExpBits": cpwVcMplsExpBits,
       "cpwVcMplsTtl": cpwVcMplsTtl,
       "cpwVcMplsLocalLdpID": cpwVcMplsLocalLdpID,
       "cpwVcMplsLocalLdpEntityID": cpwVcMplsLocalLdpEntityID,
       "cpwVcMplsPeerLdpID": cpwVcMplsPeerLdpID,
       "cpwVcMplsStorageType": cpwVcMplsStorageType,
       "cpwVcMplsOutboundIndexNext": cpwVcMplsOutboundIndexNext,
       "cpwVcMplsOutboundTable": cpwVcMplsOutboundTable,
       "cpwVcMplsOutboundEntry": cpwVcMplsOutboundEntry,
       "cpwVcMplsOutboundIndex": cpwVcMplsOutboundIndex,
       "cpwVcMplsOutboundLsrXcIndex": cpwVcMplsOutboundLsrXcIndex,
       "cpwVcMplsOutboundTunnelIndex": cpwVcMplsOutboundTunnelIndex,
       "cpwVcMplsOutboundTunnelInstance": cpwVcMplsOutboundTunnelInstance,
       "cpwVcMplsOutboundTunnelLclLSR": cpwVcMplsOutboundTunnelLclLSR,
       "cpwVcMplsOutboundTunnelPeerLSR": cpwVcMplsOutboundTunnelPeerLSR,
       "cpwVcMplsOutboundIfIndex": cpwVcMplsOutboundIfIndex,
       "cpwVcMplsOutboundRowStatus": cpwVcMplsOutboundRowStatus,
       "cpwVcMplsOutboundStorageType": cpwVcMplsOutboundStorageType,
       "cpwVcMplsInboundIndexNext": cpwVcMplsInboundIndexNext,
       "cpwVcMplsInboundTable": cpwVcMplsInboundTable,
       "cpwVcMplsInboundEntry": cpwVcMplsInboundEntry,
       "cpwVcMplsInboundIndex": cpwVcMplsInboundIndex,
       "cpwVcMplsInboundLsrXcIndex": cpwVcMplsInboundLsrXcIndex,
       "cpwVcMplsInboundTunnelIndex": cpwVcMplsInboundTunnelIndex,
       "cpwVcMplsInboundTunnelInstance": cpwVcMplsInboundTunnelInstance,
       "cpwVcMplsInboundTunnelLclLSR": cpwVcMplsInboundTunnelLclLSR,
       "cpwVcMplsInboundTunnelPeerLSR": cpwVcMplsInboundTunnelPeerLSR,
       "cpwVcMplsInboundIfIndex": cpwVcMplsInboundIfIndex,
       "cpwVcMplsInboundRowStatus": cpwVcMplsInboundRowStatus,
       "cpwVcMplsInboundStorageType": cpwVcMplsInboundStorageType,
       "cpwVcMplsNonTeMappingTable": cpwVcMplsNonTeMappingTable,
       "cpwVcMplsNonTeMappingEntry": cpwVcMplsNonTeMappingEntry,
       "cpwVcMplsNonTeMappingTunnelDirection": cpwVcMplsNonTeMappingTunnelDirection,
       "cpwVcMplsNonTeMappingXcTunnelIndex": cpwVcMplsNonTeMappingXcTunnelIndex,
       "cpwVcMplsNonTeMappingIfIndex": cpwVcMplsNonTeMappingIfIndex,
       "cpwVcMplsNonTeMappingVcIndex": cpwVcMplsNonTeMappingVcIndex,
       "cpwVcMplsTeMappingTable": cpwVcMplsTeMappingTable,
       "cpwVcMplsTeMappingEntry": cpwVcMplsTeMappingEntry,
       "cpwVcMplsTeMappingTunnelDirection": cpwVcMplsTeMappingTunnelDirection,
       "cpwVcMplsTeMappingTunnelIndex": cpwVcMplsTeMappingTunnelIndex,
       "cpwVcMplsTeMappingTunnelInstance": cpwVcMplsTeMappingTunnelInstance,
       "cpwVcMplsTeMappingTunnelPeerLsrID": cpwVcMplsTeMappingTunnelPeerLsrID,
       "cpwVcMplsTeMappingTunnelLocalLsrID": cpwVcMplsTeMappingTunnelLocalLsrID,
       "cpwVcMplsTeMappingVcIndex": cpwVcMplsTeMappingVcIndex,
       "cpwVcMplsConformance": cpwVcMplsConformance,
       "cpwVcMplsGroups": cpwVcMplsGroups,
       "cpwVcMplsGroup": cpwVcMplsGroup,
       "cpwVcMplsOutboundGroup": cpwVcMplsOutboundGroup,
       "cpwVcMplsInboundGroup": cpwVcMplsInboundGroup,
       "cpwVcMplsMappingGroup": cpwVcMplsMappingGroup,
       "cpwVcMplsCompliances": cpwVcMplsCompliances,
       "cpwMplsModuleCompliance": cpwMplsModuleCompliance}
)
