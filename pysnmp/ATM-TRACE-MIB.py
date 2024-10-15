# SNMP MIB module (ATM-TRACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-TRACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:04 2024
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

(NetworkEntityNetworkServiceCategory,
 PolicyConstraintIndex,
 ResourcePartitionNetworkServiceCategory) = mibBuilder.importSymbols(
    "ATM-POLICY-CONSTRAINT-MIB",
    "NetworkEntityNetworkServiceCategory",
    "PolicyConstraintIndex",
    "ResourcePartitionNetworkServiceCategory")

(AtmAddr,
 AtmConnCastType,
 AtmConnKind,
 AtmServiceCategory,
 AtmTrafficDescrParamIndex,
 AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr",
    "AtmConnCastType",
    "AtmConnKind",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

(PnniNodeId,
 PnniPortId,
 pnniIfEntry) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "PnniNodeId",
    "PnniPortId",
    "pnniIfEntry")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

atmTraceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1)
)
atmTraceMIB.setRevisions(
        ("2004-02-06 12:00",
         "1900-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CallReference(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class AtmEndPointReference(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )



class AtmTraceRecordIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class AtmTraceOwnerString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfSignalling_ObjectIdentity = ObjectIdentity
atmfSignalling = _AtmfSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9)
)
_AtmfTrace_ObjectIdentity = ObjectIdentity
atmfTrace = _AtmfTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2)
)
_AtmTraceMIBObjects_ObjectIdentity = ObjectIdentity
atmTraceMIBObjects = _AtmTraceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1)
)
_AtmTraceBaseGroup_ObjectIdentity = ObjectIdentity
atmTraceBaseGroup = _AtmTraceBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 1)
)


class _AtmTraceFilterControl_Type(Integer32):
    """Custom type atmTraceFilterControl based on Integer32"""
    defaultValue = 2

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


_AtmTraceFilterControl_Type.__name__ = "Integer32"
_AtmTraceFilterControl_Object = MibScalar
atmTraceFilterControl = _AtmTraceFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 1, 1),
    _AtmTraceFilterControl_Type()
)
atmTraceFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTraceFilterControl.setStatus("current")


class _AtmTraceMaxConcurrentRequests_Type(Integer32):
    """Custom type atmTraceMaxConcurrentRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmTraceMaxConcurrentRequests_Type.__name__ = "Integer32"
_AtmTraceMaxConcurrentRequests_Object = MibScalar
atmTraceMaxConcurrentRequests = _AtmTraceMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 1, 2),
    _AtmTraceMaxConcurrentRequests_Type()
)
atmTraceMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTraceMaxConcurrentRequests.setStatus("current")


class _AtmTraceAvailableRequests_Type(Integer32):
    """Custom type atmTraceAvailableRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmTraceAvailableRequests_Type.__name__ = "Integer32"
_AtmTraceAvailableRequests_Object = MibScalar
atmTraceAvailableRequests = _AtmTraceAvailableRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 1, 3),
    _AtmTraceAvailableRequests_Type()
)
atmTraceAvailableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceAvailableRequests.setStatus("current")


class _AtmTraceTransitListMaximumSize_Type(Integer32):
    """Custom type atmTraceTransitListMaximumSize based on Integer32"""
    defaultValue = 1466

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1466, 65535),
    )


_AtmTraceTransitListMaximumSize_Type.__name__ = "Integer32"
_AtmTraceTransitListMaximumSize_Object = MibScalar
atmTraceTransitListMaximumSize = _AtmTraceTransitListMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 1, 4),
    _AtmTraceTransitListMaximumSize_Type()
)
atmTraceTransitListMaximumSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTraceTransitListMaximumSize.setStatus("current")
if mibBuilder.loadTexts:
    atmTraceTransitListMaximumSize.setUnits("octets")
_AtmTraceConnGroup_ObjectIdentity = ObjectIdentity
atmTraceConnGroup = _AtmTraceConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2)
)
_AtmTraceConnTable_Object = MibTable
atmTraceConnTable = _AtmTraceConnTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmTraceConnTable.setStatus("current")
_AtmTraceConnEntry_Object = MibTableRow
atmTraceConnEntry = _AtmTraceConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1)
)
atmTraceConnEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTraceConnIndex"),
)
if mibBuilder.loadTexts:
    atmTraceConnEntry.setStatus("current")
_AtmTraceConnIndex_Type = Integer32
_AtmTraceConnIndex_Object = MibTableColumn
atmTraceConnIndex = _AtmTraceConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 1),
    _AtmTraceConnIndex_Type()
)
atmTraceConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceConnIndex.setStatus("current")
_AtmTraceConnOwner_Type = AtmTraceOwnerString
_AtmTraceConnOwner_Object = MibTableColumn
atmTraceConnOwner = _AtmTraceConnOwner_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 2),
    _AtmTraceConnOwner_Type()
)
atmTraceConnOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnOwner.setStatus("current")
_AtmTraceConnTraceSourceIf_Type = InterfaceIndex
_AtmTraceConnTraceSourceIf_Object = MibTableColumn
atmTraceConnTraceSourceIf = _AtmTraceConnTraceSourceIf_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 3),
    _AtmTraceConnTraceSourceIf_Type()
)
atmTraceConnTraceSourceIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTraceSourceIf.setStatus("current")


class _AtmTraceConnOrigConnType_Type(Integer32):
    """Custom type atmTraceConnOrigConnType based on Integer32"""
    defaultValue = 2

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
        *(("atmCOBISigConn", 4),
          ("atmVcc", 2),
          ("atmVpc", 3),
          ("frameRelayVc", 5),
          ("other", 1))
    )


_AtmTraceConnOrigConnType_Type.__name__ = "Integer32"
_AtmTraceConnOrigConnType_Object = MibTableColumn
atmTraceConnOrigConnType = _AtmTraceConnOrigConnType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 4),
    _AtmTraceConnOrigConnType_Type()
)
atmTraceConnOrigConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnOrigConnType.setStatus("current")
_AtmTraceConnOrigVpi_Type = AtmVpIdentifier
_AtmTraceConnOrigVpi_Object = MibTableColumn
atmTraceConnOrigVpi = _AtmTraceConnOrigVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 5),
    _AtmTraceConnOrigVpi_Type()
)
atmTraceConnOrigVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnOrigVpi.setStatus("current")
_AtmTraceConnOrigVci_Type = AtmVcIdentifier
_AtmTraceConnOrigVci_Object = MibTableColumn
atmTraceConnOrigVci = _AtmTraceConnOrigVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 6),
    _AtmTraceConnOrigVci_Type()
)
atmTraceConnOrigVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnOrigVci.setStatus("current")
_AtmTraceConnEndPtRef_Type = AtmEndPointReference
_AtmTraceConnEndPtRef_Object = MibTableColumn
atmTraceConnEndPtRef = _AtmTraceConnEndPtRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 7),
    _AtmTraceConnEndPtRef_Type()
)
atmTraceConnEndPtRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnEndPtRef.setStatus("current")
_AtmTraceConnCallRef_Type = CallReference
_AtmTraceConnCallRef_Object = MibTableColumn
atmTraceConnCallRef = _AtmTraceConnCallRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 8),
    _AtmTraceConnCallRef_Type()
)
atmTraceConnCallRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnCallRef.setStatus("current")
_AtmTraceConnOrigDlci_Type = Integer32
_AtmTraceConnOrigDlci_Object = MibTableColumn
atmTraceConnOrigDlci = _AtmTraceConnOrigDlci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 9),
    _AtmTraceConnOrigDlci_Type()
)
atmTraceConnOrigDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnOrigDlci.setStatus("current")


class _AtmTraceConnOrigDirection_Type(Integer32):
    """Custom type atmTraceConnOrigDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AtmTraceConnOrigDirection_Type.__name__ = "Integer32"
_AtmTraceConnOrigDirection_Object = MibTableColumn
atmTraceConnOrigDirection = _AtmTraceConnOrigDirection_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 10),
    _AtmTraceConnOrigDirection_Type()
)
atmTraceConnOrigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnOrigDirection.setStatus("current")


class _AtmTraceConnTraceConnId_Type(TruthValue):
    """Custom type atmTraceConnTraceConnId based on TruthValue"""


_AtmTraceConnTraceConnId_Object = MibTableColumn
atmTraceConnTraceConnId = _AtmTraceConnTraceConnId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 11),
    _AtmTraceConnTraceConnId_Type()
)
atmTraceConnTraceConnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTraceConnId.setStatus("current")


class _AtmTraceConnTraceCallRef_Type(TruthValue):
    """Custom type atmTraceConnTraceCallRef based on TruthValue"""


_AtmTraceConnTraceCallRef_Object = MibTableColumn
atmTraceConnTraceCallRef = _AtmTraceConnTraceCallRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 12),
    _AtmTraceConnTraceCallRef_Type()
)
atmTraceConnTraceCallRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTraceCallRef.setStatus("current")


class _AtmTraceConnPassAlongRequest_Type(TruthValue):
    """Custom type atmTraceConnPassAlongRequest based on TruthValue"""


_AtmTraceConnPassAlongRequest_Object = MibTableColumn
atmTraceConnPassAlongRequest = _AtmTraceConnPassAlongRequest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 13),
    _AtmTraceConnPassAlongRequest_Type()
)
atmTraceConnPassAlongRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnPassAlongRequest.setStatus("current")


class _AtmTraceConnFailTimeout_Type(Integer32):
    """Custom type atmTraceConnFailTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmTraceConnFailTimeout_Type.__name__ = "Integer32"
_AtmTraceConnFailTimeout_Object = MibTableColumn
atmTraceConnFailTimeout = _AtmTraceConnFailTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 14),
    _AtmTraceConnFailTimeout_Type()
)
atmTraceConnFailTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnFailTimeout.setStatus("current")
if mibBuilder.loadTexts:
    atmTraceConnFailTimeout.setUnits("seconds")


class _AtmTraceConnAgeTimeout_Type(Integer32):
    """Custom type atmTraceConnAgeTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AtmTraceConnAgeTimeout_Type.__name__ = "Integer32"
_AtmTraceConnAgeTimeout_Object = MibTableColumn
atmTraceConnAgeTimeout = _AtmTraceConnAgeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 15),
    _AtmTraceConnAgeTimeout_Type()
)
atmTraceConnAgeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnAgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    atmTraceConnAgeTimeout.setUnits("seconds")


class _AtmTraceConnRestart_Type(Integer32):
    """Custom type atmTraceConnRestart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restart", 1))
    )


_AtmTraceConnRestart_Type.__name__ = "Integer32"
_AtmTraceConnRestart_Object = MibTableColumn
atmTraceConnRestart = _AtmTraceConnRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 16),
    _AtmTraceConnRestart_Type()
)
atmTraceConnRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnRestart.setStatus("current")


class _AtmTraceConnTrapOnCompletion_Type(TruthValue):
    """Custom type atmTraceConnTrapOnCompletion based on TruthValue"""


_AtmTraceConnTrapOnCompletion_Object = MibTableColumn
atmTraceConnTrapOnCompletion = _AtmTraceConnTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 17),
    _AtmTraceConnTrapOnCompletion_Type()
)
atmTraceConnTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTrapOnCompletion.setStatus("current")
_AtmTraceConnRecordIndex_Type = AtmTraceRecordIndex
_AtmTraceConnRecordIndex_Object = MibTableColumn
atmTraceConnRecordIndex = _AtmTraceConnRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 18),
    _AtmTraceConnRecordIndex_Type()
)
atmTraceConnRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceConnRecordIndex.setStatus("current")
_AtmTraceConnRowStatus_Type = RowStatus
_AtmTraceConnRowStatus_Object = MibTableColumn
atmTraceConnRowStatus = _AtmTraceConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 19),
    _AtmTraceConnRowStatus_Type()
)
atmTraceConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnRowStatus.setStatus("current")


class _AtmTraceConnTraceNeNsc_Type(TruthValue):
    """Custom type atmTraceConnTraceNeNsc based on TruthValue"""


_AtmTraceConnTraceNeNsc_Object = MibTableColumn
atmTraceConnTraceNeNsc = _AtmTraceConnTraceNeNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 20),
    _AtmTraceConnTraceNeNsc_Type()
)
atmTraceConnTraceNeNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTraceNeNsc.setStatus("current")


class _AtmTraceConnTraceRpNsc_Type(TruthValue):
    """Custom type atmTraceConnTraceRpNsc based on TruthValue"""


_AtmTraceConnTraceRpNsc_Object = MibTableColumn
atmTraceConnTraceRpNsc = _AtmTraceConnTraceRpNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 21),
    _AtmTraceConnTraceRpNsc_Type()
)
atmTraceConnTraceRpNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTraceRpNsc.setStatus("current")


class _AtmTraceConnTraceIncoming_Type(TruthValue):
    """Custom type atmTraceConnTraceIncoming based on TruthValue"""


_AtmTraceConnTraceIncoming_Object = MibTableColumn
atmTraceConnTraceIncoming = _AtmTraceConnTraceIncoming_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 22),
    _AtmTraceConnTraceIncoming_Type()
)
atmTraceConnTraceIncoming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTraceIncoming.setStatus("current")


class _AtmTraceConnTraceLabels_Type(TruthValue):
    """Custom type atmTraceConnTraceLabels based on TruthValue"""


_AtmTraceConnTraceLabels_Object = MibTableColumn
atmTraceConnTraceLabels = _AtmTraceConnTraceLabels_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 2, 1, 1, 23),
    _AtmTraceConnTraceLabels_Type()
)
atmTraceConnTraceLabels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceConnTraceLabels.setStatus("current")
_AtmTracePathTestGroup_ObjectIdentity = ObjectIdentity
atmTracePathTestGroup = _AtmTracePathTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3)
)
_AtmTracePathTestTable_Object = MibTable
atmTracePathTestTable = _AtmTracePathTestTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmTracePathTestTable.setStatus("current")
_AtmTracePathTestEntry_Object = MibTableRow
atmTracePathTestEntry = _AtmTracePathTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1)
)
atmTracePathTestEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTracePathTestIndex"),
)
if mibBuilder.loadTexts:
    atmTracePathTestEntry.setStatus("current")
_AtmTracePathTestIndex_Type = Integer32
_AtmTracePathTestIndex_Object = MibTableColumn
atmTracePathTestIndex = _AtmTracePathTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 1),
    _AtmTracePathTestIndex_Type()
)
atmTracePathTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTracePathTestIndex.setStatus("current")
_AtmTracePathTestOwner_Type = AtmTraceOwnerString
_AtmTracePathTestOwner_Object = MibTableColumn
atmTracePathTestOwner = _AtmTracePathTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 2),
    _AtmTracePathTestOwner_Type()
)
atmTracePathTestOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestOwner.setStatus("current")


class _AtmTracePathTestConnType_Type(Integer32):
    """Custom type atmTracePathTestConnType based on Integer32"""
    defaultValue = 2

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
        *(("atmCOBISigConn", 4),
          ("atmVcc", 2),
          ("atmVpc", 3),
          ("other", 1))
    )


_AtmTracePathTestConnType_Type.__name__ = "Integer32"
_AtmTracePathTestConnType_Object = MibTableColumn
atmTracePathTestConnType = _AtmTracePathTestConnType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 3),
    _AtmTracePathTestConnType_Type()
)
atmTracePathTestConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestConnType.setStatus("current")


class _AtmTracePathTestConnCastType_Type(AtmConnCastType):
    """Custom type atmTracePathTestConnCastType based on AtmConnCastType"""


_AtmTracePathTestConnCastType_Object = MibTableColumn
atmTracePathTestConnCastType = _AtmTracePathTestConnCastType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 4),
    _AtmTracePathTestConnCastType_Type()
)
atmTracePathTestConnCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestConnCastType.setStatus("current")
_AtmTracePathTestTraceSourceIf_Type = InterfaceIndex
_AtmTracePathTestTraceSourceIf_Object = MibTableColumn
atmTracePathTestTraceSourceIf = _AtmTracePathTestTraceSourceIf_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 5),
    _AtmTracePathTestTraceSourceIf_Type()
)
atmTracePathTestTraceSourceIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceSourceIf.setStatus("current")


class _AtmTracePathTestP2MpNewConn_Type(TruthValue):
    """Custom type atmTracePathTestP2MpNewConn based on TruthValue"""


_AtmTracePathTestP2MpNewConn_Object = MibTableColumn
atmTracePathTestP2MpNewConn = _AtmTracePathTestP2MpNewConn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 6),
    _AtmTracePathTestP2MpNewConn_Type()
)
atmTracePathTestP2MpNewConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestP2MpNewConn.setStatus("current")


class _AtmTracePathTestOrigVpi_Type(AtmVpIdentifier):
    """Custom type atmTracePathTestOrigVpi based on AtmVpIdentifier"""
    defaultValue = 0


_AtmTracePathTestOrigVpi_Object = MibTableColumn
atmTracePathTestOrigVpi = _AtmTracePathTestOrigVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 7),
    _AtmTracePathTestOrigVpi_Type()
)
atmTracePathTestOrigVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestOrigVpi.setStatus("current")


class _AtmTracePathTestOrigVci_Type(AtmVcIdentifier):
    """Custom type atmTracePathTestOrigVci based on AtmVcIdentifier"""
    defaultValue = 0


_AtmTracePathTestOrigVci_Object = MibTableColumn
atmTracePathTestOrigVci = _AtmTracePathTestOrigVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 8),
    _AtmTracePathTestOrigVci_Type()
)
atmTracePathTestOrigVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestOrigVci.setStatus("current")
_AtmTracePathTestCalledParty_Type = AtmAddr
_AtmTracePathTestCalledParty_Object = MibTableColumn
atmTracePathTestCalledParty = _AtmTracePathTestCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 9),
    _AtmTracePathTestCalledParty_Type()
)
atmTracePathTestCalledParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestCalledParty.setStatus("current")
_AtmTracePathTestCallingParty_Type = AtmAddr
_AtmTracePathTestCallingParty_Object = MibTableColumn
atmTracePathTestCallingParty = _AtmTracePathTestCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 10),
    _AtmTracePathTestCallingParty_Type()
)
atmTracePathTestCallingParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestCallingParty.setStatus("current")


class _AtmTracePathTestRxTrafDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type atmTracePathTestRxTrafDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 0


_AtmTracePathTestRxTrafDescrIndex_Object = MibTableColumn
atmTracePathTestRxTrafDescrIndex = _AtmTracePathTestRxTrafDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 11),
    _AtmTracePathTestRxTrafDescrIndex_Type()
)
atmTracePathTestRxTrafDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestRxTrafDescrIndex.setStatus("current")


class _AtmTracePathTestTxTrafDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type atmTracePathTestTxTrafDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 0


_AtmTracePathTestTxTrafDescrIndex_Object = MibTableColumn
atmTracePathTestTxTrafDescrIndex = _AtmTracePathTestTxTrafDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 12),
    _AtmTracePathTestTxTrafDescrIndex_Type()
)
atmTracePathTestTxTrafDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTxTrafDescrIndex.setStatus("current")


class _AtmTracePathTestClearCallAtTDest_Type(TruthValue):
    """Custom type atmTracePathTestClearCallAtTDest based on TruthValue"""


_AtmTracePathTestClearCallAtTDest_Object = MibTableColumn
atmTracePathTestClearCallAtTDest = _AtmTracePathTestClearCallAtTDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 13),
    _AtmTracePathTestClearCallAtTDest_Type()
)
atmTracePathTestClearCallAtTDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestClearCallAtTDest.setStatus("current")


class _AtmTracePathTestTraceCrankback_Type(TruthValue):
    """Custom type atmTracePathTestTraceCrankback based on TruthValue"""


_AtmTracePathTestTraceCrankback_Object = MibTableColumn
atmTracePathTestTraceCrankback = _AtmTracePathTestTraceCrankback_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 14),
    _AtmTracePathTestTraceCrankback_Type()
)
atmTracePathTestTraceCrankback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceCrankback.setStatus("current")


class _AtmTracePathTestTraceConnId_Type(TruthValue):
    """Custom type atmTracePathTestTraceConnId based on TruthValue"""


_AtmTracePathTestTraceConnId_Object = MibTableColumn
atmTracePathTestTraceConnId = _AtmTracePathTestTraceConnId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 15),
    _AtmTracePathTestTraceConnId_Type()
)
atmTracePathTestTraceConnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceConnId.setStatus("current")


class _AtmTracePathTestTraceCallRef_Type(TruthValue):
    """Custom type atmTracePathTestTraceCallRef based on TruthValue"""


_AtmTracePathTestTraceCallRef_Object = MibTableColumn
atmTracePathTestTraceCallRef = _AtmTracePathTestTraceCallRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 16),
    _AtmTracePathTestTraceCallRef_Type()
)
atmTracePathTestTraceCallRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceCallRef.setStatus("current")


class _AtmTracePathTestPassAlongRequest_Type(TruthValue):
    """Custom type atmTracePathTestPassAlongRequest based on TruthValue"""


_AtmTracePathTestPassAlongRequest_Object = MibTableColumn
atmTracePathTestPassAlongRequest = _AtmTracePathTestPassAlongRequest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 17),
    _AtmTracePathTestPassAlongRequest_Type()
)
atmTracePathTestPassAlongRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestPassAlongRequest.setStatus("current")


class _AtmTracePathTestAgeTimeout_Type(Integer32):
    """Custom type atmTracePathTestAgeTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AtmTracePathTestAgeTimeout_Type.__name__ = "Integer32"
_AtmTracePathTestAgeTimeout_Object = MibTableColumn
atmTracePathTestAgeTimeout = _AtmTracePathTestAgeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 18),
    _AtmTracePathTestAgeTimeout_Type()
)
atmTracePathTestAgeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestAgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    atmTracePathTestAgeTimeout.setUnits("seconds")


class _AtmTracePathTestRestart_Type(Integer32):
    """Custom type atmTracePathTestRestart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restart", 1))
    )


_AtmTracePathTestRestart_Type.__name__ = "Integer32"
_AtmTracePathTestRestart_Object = MibTableColumn
atmTracePathTestRestart = _AtmTracePathTestRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 19),
    _AtmTracePathTestRestart_Type()
)
atmTracePathTestRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestRestart.setStatus("current")


class _AtmTracePathTestTrapOnCompletion_Type(TruthValue):
    """Custom type atmTracePathTestTrapOnCompletion based on TruthValue"""


_AtmTracePathTestTrapOnCompletion_Object = MibTableColumn
atmTracePathTestTrapOnCompletion = _AtmTracePathTestTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 20),
    _AtmTracePathTestTrapOnCompletion_Type()
)
atmTracePathTestTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTrapOnCompletion.setStatus("current")
_AtmTracePathTestRecordIndex_Type = AtmTraceRecordIndex
_AtmTracePathTestRecordIndex_Object = MibTableColumn
atmTracePathTestRecordIndex = _AtmTracePathTestRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 21),
    _AtmTracePathTestRecordIndex_Type()
)
atmTracePathTestRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTracePathTestRecordIndex.setStatus("current")
_AtmTracePathTestRowStatus_Type = RowStatus
_AtmTracePathTestRowStatus_Object = MibTableColumn
atmTracePathTestRowStatus = _AtmTracePathTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 22),
    _AtmTracePathTestRowStatus_Type()
)
atmTracePathTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestRowStatus.setStatus("current")


class _AtmTracePathTestTraceNeNsc_Type(TruthValue):
    """Custom type atmTracePathTestTraceNeNsc based on TruthValue"""


_AtmTracePathTestTraceNeNsc_Object = MibTableColumn
atmTracePathTestTraceNeNsc = _AtmTracePathTestTraceNeNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 23),
    _AtmTracePathTestTraceNeNsc_Type()
)
atmTracePathTestTraceNeNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceNeNsc.setStatus("current")


class _AtmTracePathTestTraceRpNsc_Type(TruthValue):
    """Custom type atmTracePathTestTraceRpNsc based on TruthValue"""


_AtmTracePathTestTraceRpNsc_Object = MibTableColumn
atmTracePathTestTraceRpNsc = _AtmTracePathTestTraceRpNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 24),
    _AtmTracePathTestTraceRpNsc_Type()
)
atmTracePathTestTraceRpNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceRpNsc.setStatus("current")


class _AtmTracePathTestTraceIncoming_Type(TruthValue):
    """Custom type atmTracePathTestTraceIncoming based on TruthValue"""


_AtmTracePathTestTraceIncoming_Object = MibTableColumn
atmTracePathTestTraceIncoming = _AtmTracePathTestTraceIncoming_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 25),
    _AtmTracePathTestTraceIncoming_Type()
)
atmTracePathTestTraceIncoming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceIncoming.setStatus("current")


class _AtmTracePathTestPolicyConstraint_Type(PolicyConstraintIndex):
    """Custom type atmTracePathTestPolicyConstraint based on PolicyConstraintIndex"""
    defaultValue = 0


_AtmTracePathTestPolicyConstraint_Object = MibTableColumn
atmTracePathTestPolicyConstraint = _AtmTracePathTestPolicyConstraint_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 26),
    _AtmTracePathTestPolicyConstraint_Type()
)
atmTracePathTestPolicyConstraint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestPolicyConstraint.setStatus("current")


class _AtmTracePathTestTraceLabels_Type(TruthValue):
    """Custom type atmTracePathTestTraceLabels based on TruthValue"""


_AtmTracePathTestTraceLabels_Object = MibTableColumn
atmTracePathTestTraceLabels = _AtmTracePathTestTraceLabels_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 3, 1, 1, 27),
    _AtmTracePathTestTraceLabels_Type()
)
atmTracePathTestTraceLabels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTracePathTestTraceLabels.setStatus("current")
_AtmTraceFilterGroup_ObjectIdentity = ObjectIdentity
atmTraceFilterGroup = _AtmTraceFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4)
)
_AtmTraceFilterTable_Object = MibTable
atmTraceFilterTable = _AtmTraceFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    atmTraceFilterTable.setStatus("current")
_AtmTraceFilterEntry_Object = MibTableRow
atmTraceFilterEntry = _AtmTraceFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1)
)
atmTraceFilterEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    atmTraceFilterEntry.setStatus("current")


class _AtmTraceFilterIndex_Type(Integer32):
    """Custom type atmTraceFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AtmTraceFilterIndex_Type.__name__ = "Integer32"
_AtmTraceFilterIndex_Object = MibTableColumn
atmTraceFilterIndex = _AtmTraceFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 1),
    _AtmTraceFilterIndex_Type()
)
atmTraceFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceFilterIndex.setStatus("current")
_AtmTraceFilterOwner_Type = AtmTraceOwnerString
_AtmTraceFilterOwner_Object = MibTableColumn
atmTraceFilterOwner = _AtmTraceFilterOwner_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 2),
    _AtmTraceFilterOwner_Type()
)
atmTraceFilterOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterOwner.setStatus("current")


class _AtmTraceFilterConnKind_Type(Bits):
    """Custom type atmTraceFilterConnKind based on Bits"""
    namedValues = NamedValues(
        *(("atmCOBISigConn", 5),
          ("other", 0),
          ("spvcInitiator", 2),
          ("spvpInitiator", 4),
          ("svcAndSpvcNotInitiator", 1),
          ("svpAndSpvpNotInitiator", 3))
    )

_AtmTraceFilterConnKind_Type.__name__ = "Bits"
_AtmTraceFilterConnKind_Object = MibTableColumn
atmTraceFilterConnKind = _AtmTraceFilterConnKind_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 3),
    _AtmTraceFilterConnKind_Type()
)
atmTraceFilterConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterConnKind.setStatus("current")


class _AtmTraceFilterConnCastType_Type(Bits):
    """Custom type atmTraceFilterConnCastType based on Bits"""
    namedValues = NamedValues(
        *(("p2mp", 1),
          ("p2p", 0))
    )

_AtmTraceFilterConnCastType_Type.__name__ = "Bits"
_AtmTraceFilterConnCastType_Object = MibTableColumn
atmTraceFilterConnCastType = _AtmTraceFilterConnCastType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 4),
    _AtmTraceFilterConnCastType_Type()
)
atmTraceFilterConnCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterConnCastType.setStatus("current")


class _AtmTraceFilterServiceCategory_Type(Bits):
    """Custom type atmTraceFilterServiceCategory based on Bits"""
    namedValues = NamedValues(
        *(("abr", 3),
          ("cbr", 0),
          ("gfr", 5),
          ("nrtVbr", 2),
          ("other", 6),
          ("rtVbr", 1),
          ("ubr", 4))
    )

_AtmTraceFilterServiceCategory_Type.__name__ = "Bits"
_AtmTraceFilterServiceCategory_Object = MibTableColumn
atmTraceFilterServiceCategory = _AtmTraceFilterServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 5),
    _AtmTraceFilterServiceCategory_Type()
)
atmTraceFilterServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterServiceCategory.setStatus("current")


class _AtmTraceFilterInIf_Type(InterfaceIndexOrZero):
    """Custom type atmTraceFilterInIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AtmTraceFilterInIf_Object = MibTableColumn
atmTraceFilterInIf = _AtmTraceFilterInIf_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 6),
    _AtmTraceFilterInIf_Type()
)
atmTraceFilterInIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterInIf.setStatus("current")


class _AtmTraceFilterOutIf_Type(InterfaceIndexOrZero):
    """Custom type atmTraceFilterOutIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AtmTraceFilterOutIf_Object = MibTableColumn
atmTraceFilterOutIf = _AtmTraceFilterOutIf_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 7),
    _AtmTraceFilterOutIf_Type()
)
atmTraceFilterOutIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterOutIf.setStatus("current")
_AtmTraceFilterCallingPartyPrefix_Type = AtmAddr
_AtmTraceFilterCallingPartyPrefix_Object = MibTableColumn
atmTraceFilterCallingPartyPrefix = _AtmTraceFilterCallingPartyPrefix_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 8),
    _AtmTraceFilterCallingPartyPrefix_Type()
)
atmTraceFilterCallingPartyPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterCallingPartyPrefix.setStatus("current")


class _AtmTraceFilterCallingPartyLength_Type(Integer32):
    """Custom type atmTraceFilterCallingPartyLength based on Integer32"""
    defaultValue = 152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_AtmTraceFilterCallingPartyLength_Type.__name__ = "Integer32"
_AtmTraceFilterCallingPartyLength_Object = MibTableColumn
atmTraceFilterCallingPartyLength = _AtmTraceFilterCallingPartyLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 9),
    _AtmTraceFilterCallingPartyLength_Type()
)
atmTraceFilterCallingPartyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterCallingPartyLength.setStatus("current")
_AtmTraceFilterCalledPartyPrefix_Type = AtmAddr
_AtmTraceFilterCalledPartyPrefix_Object = MibTableColumn
atmTraceFilterCalledPartyPrefix = _AtmTraceFilterCalledPartyPrefix_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 10),
    _AtmTraceFilterCalledPartyPrefix_Type()
)
atmTraceFilterCalledPartyPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterCalledPartyPrefix.setStatus("current")


class _AtmTraceFilterCalledPartyLength_Type(Integer32):
    """Custom type atmTraceFilterCalledPartyLength based on Integer32"""
    defaultValue = 152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_AtmTraceFilterCalledPartyLength_Type.__name__ = "Integer32"
_AtmTraceFilterCalledPartyLength_Object = MibTableColumn
atmTraceFilterCalledPartyLength = _AtmTraceFilterCalledPartyLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 11),
    _AtmTraceFilterCalledPartyLength_Type()
)
atmTraceFilterCalledPartyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterCalledPartyLength.setStatus("current")


class _AtmTraceFilterClearCallAtTDest_Type(TruthValue):
    """Custom type atmTraceFilterClearCallAtTDest based on TruthValue"""


_AtmTraceFilterClearCallAtTDest_Object = MibTableColumn
atmTraceFilterClearCallAtTDest = _AtmTraceFilterClearCallAtTDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 12),
    _AtmTraceFilterClearCallAtTDest_Type()
)
atmTraceFilterClearCallAtTDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterClearCallAtTDest.setStatus("current")


class _AtmTraceFilterTraceCrankback_Type(TruthValue):
    """Custom type atmTraceFilterTraceCrankback based on TruthValue"""


_AtmTraceFilterTraceCrankback_Object = MibTableColumn
atmTraceFilterTraceCrankback = _AtmTraceFilterTraceCrankback_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 13),
    _AtmTraceFilterTraceCrankback_Type()
)
atmTraceFilterTraceCrankback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTraceCrankback.setStatus("current")


class _AtmTraceFilterTraceConnId_Type(TruthValue):
    """Custom type atmTraceFilterTraceConnId based on TruthValue"""


_AtmTraceFilterTraceConnId_Object = MibTableColumn
atmTraceFilterTraceConnId = _AtmTraceFilterTraceConnId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 14),
    _AtmTraceFilterTraceConnId_Type()
)
atmTraceFilterTraceConnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTraceConnId.setStatus("current")


class _AtmTraceFilterTraceCallRef_Type(TruthValue):
    """Custom type atmTraceFilterTraceCallRef based on TruthValue"""


_AtmTraceFilterTraceCallRef_Object = MibTableColumn
atmTraceFilterTraceCallRef = _AtmTraceFilterTraceCallRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 15),
    _AtmTraceFilterTraceCallRef_Type()
)
atmTraceFilterTraceCallRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTraceCallRef.setStatus("current")


class _AtmTraceFilterPassAlongRequest_Type(TruthValue):
    """Custom type atmTraceFilterPassAlongRequest based on TruthValue"""


_AtmTraceFilterPassAlongRequest_Object = MibTableColumn
atmTraceFilterPassAlongRequest = _AtmTraceFilterPassAlongRequest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 16),
    _AtmTraceFilterPassAlongRequest_Type()
)
atmTraceFilterPassAlongRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterPassAlongRequest.setStatus("current")


class _AtmTraceFilterMaxRecords_Type(Integer32):
    """Custom type atmTraceFilterMaxRecords based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 214783647),
    )


_AtmTraceFilterMaxRecords_Type.__name__ = "Integer32"
_AtmTraceFilterMaxRecords_Object = MibTableColumn
atmTraceFilterMaxRecords = _AtmTraceFilterMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 17),
    _AtmTraceFilterMaxRecords_Type()
)
atmTraceFilterMaxRecords.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterMaxRecords.setStatus("current")


class _AtmTraceFilterRecordCountDown_Type(Integer32):
    """Custom type atmTraceFilterRecordCountDown based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AtmTraceFilterRecordCountDown_Type.__name__ = "Integer32"
_AtmTraceFilterRecordCountDown_Object = MibTableColumn
atmTraceFilterRecordCountDown = _AtmTraceFilterRecordCountDown_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 18),
    _AtmTraceFilterRecordCountDown_Type()
)
atmTraceFilterRecordCountDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterRecordCountDown.setStatus("current")


class _AtmTraceFilterStopTimeout_Type(Integer32):
    """Custom type atmTraceFilterStopTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AtmTraceFilterStopTimeout_Type.__name__ = "Integer32"
_AtmTraceFilterStopTimeout_Object = MibTableColumn
atmTraceFilterStopTimeout = _AtmTraceFilterStopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 19),
    _AtmTraceFilterStopTimeout_Type()
)
atmTraceFilterStopTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterStopTimeout.setStatus("current")
if mibBuilder.loadTexts:
    atmTraceFilterStopTimeout.setUnits("seconds")


class _AtmTraceFilterAgeTimeout_Type(Integer32):
    """Custom type atmTraceFilterAgeTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AtmTraceFilterAgeTimeout_Type.__name__ = "Integer32"
_AtmTraceFilterAgeTimeout_Object = MibTableColumn
atmTraceFilterAgeTimeout = _AtmTraceFilterAgeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 20),
    _AtmTraceFilterAgeTimeout_Type()
)
atmTraceFilterAgeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterAgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    atmTraceFilterAgeTimeout.setUnits("seconds")


class _AtmTraceFilterPurge_Type(Integer32):
    """Custom type atmTraceFilterPurge based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("purge", 1))
    )


_AtmTraceFilterPurge_Type.__name__ = "Integer32"
_AtmTraceFilterPurge_Object = MibTableColumn
atmTraceFilterPurge = _AtmTraceFilterPurge_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 21),
    _AtmTraceFilterPurge_Type()
)
atmTraceFilterPurge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterPurge.setStatus("current")


class _AtmTraceFilterTrapEnable_Type(TruthValue):
    """Custom type atmTraceFilterTrapEnable based on TruthValue"""


_AtmTraceFilterTrapEnable_Object = MibTableColumn
atmTraceFilterTrapEnable = _AtmTraceFilterTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 22),
    _AtmTraceFilterTrapEnable_Type()
)
atmTraceFilterTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTrapEnable.setStatus("current")
_AtmTraceFilterNumMatches_Type = Counter32
_AtmTraceFilterNumMatches_Object = MibTableColumn
atmTraceFilterNumMatches = _AtmTraceFilterNumMatches_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 23),
    _AtmTraceFilterNumMatches_Type()
)
atmTraceFilterNumMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterNumMatches.setStatus("current")
_AtmTraceFilterRowStatus_Type = RowStatus
_AtmTraceFilterRowStatus_Object = MibTableColumn
atmTraceFilterRowStatus = _AtmTraceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 24),
    _AtmTraceFilterRowStatus_Type()
)
atmTraceFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterRowStatus.setStatus("current")


class _AtmTraceFilterPolicy_Type(TruthValue):
    """Custom type atmTraceFilterPolicy based on TruthValue"""


_AtmTraceFilterPolicy_Object = MibTableColumn
atmTraceFilterPolicy = _AtmTraceFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 25),
    _AtmTraceFilterPolicy_Type()
)
atmTraceFilterPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterPolicy.setStatus("current")


class _AtmTraceFilterTraceNeNsc_Type(TruthValue):
    """Custom type atmTraceFilterTraceNeNsc based on TruthValue"""


_AtmTraceFilterTraceNeNsc_Object = MibTableColumn
atmTraceFilterTraceNeNsc = _AtmTraceFilterTraceNeNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 26),
    _AtmTraceFilterTraceNeNsc_Type()
)
atmTraceFilterTraceNeNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTraceNeNsc.setStatus("current")


class _AtmTraceFilterTraceRpNsc_Type(TruthValue):
    """Custom type atmTraceFilterTraceRpNsc based on TruthValue"""


_AtmTraceFilterTraceRpNsc_Object = MibTableColumn
atmTraceFilterTraceRpNsc = _AtmTraceFilterTraceRpNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 27),
    _AtmTraceFilterTraceRpNsc_Type()
)
atmTraceFilterTraceRpNsc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTraceRpNsc.setStatus("current")


class _AtmTraceFilterTraceIncoming_Type(TruthValue):
    """Custom type atmTraceFilterTraceIncoming based on TruthValue"""


_AtmTraceFilterTraceIncoming_Object = MibTableColumn
atmTraceFilterTraceIncoming = _AtmTraceFilterTraceIncoming_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 28),
    _AtmTraceFilterTraceIncoming_Type()
)
atmTraceFilterTraceIncoming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTraceIncoming.setStatus("current")


class _AtmTraceFilterTraceLabels_Type(TruthValue):
    """Custom type atmTraceFilterTraceLabels based on TruthValue"""


_AtmTraceFilterTraceLabels_Object = MibTableColumn
atmTraceFilterTraceLabels = _AtmTraceFilterTraceLabels_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 1, 1, 29),
    _AtmTraceFilterTraceLabels_Type()
)
atmTraceFilterTraceLabels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTraceFilterTraceLabels.setStatus("current")
_AtmTraceFilterRecordTable_Object = MibTable
atmTraceFilterRecordTable = _AtmTraceFilterRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    atmTraceFilterRecordTable.setStatus("current")
_AtmTraceFilterRecordEntry_Object = MibTableRow
atmTraceFilterRecordEntry = _AtmTraceFilterRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1)
)
atmTraceFilterRecordEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTraceFilterIndex"),
    (0, "ATM-TRACE-MIB", "atmTraceFilterRecordIndex"),
)
if mibBuilder.loadTexts:
    atmTraceFilterRecordEntry.setStatus("current")
_AtmTraceFilterRecordIndex_Type = AtmTraceRecordIndex
_AtmTraceFilterRecordIndex_Object = MibTableColumn
atmTraceFilterRecordIndex = _AtmTraceFilterRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 1),
    _AtmTraceFilterRecordIndex_Type()
)
atmTraceFilterRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceFilterRecordIndex.setStatus("current")
_AtmTraceFilterRecordConnKind_Type = AtmConnKind
_AtmTraceFilterRecordConnKind_Object = MibTableColumn
atmTraceFilterRecordConnKind = _AtmTraceFilterRecordConnKind_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 2),
    _AtmTraceFilterRecordConnKind_Type()
)
atmTraceFilterRecordConnKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterRecordConnKind.setStatus("current")
_AtmTraceFilterRecordConnCastType_Type = AtmConnCastType
_AtmTraceFilterRecordConnCastType_Object = MibTableColumn
atmTraceFilterRecordConnCastType = _AtmTraceFilterRecordConnCastType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 3),
    _AtmTraceFilterRecordConnCastType_Type()
)
atmTraceFilterRecordConnCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterRecordConnCastType.setStatus("current")
_AtmTraceFilterRecordServiceCategory_Type = AtmServiceCategory
_AtmTraceFilterRecordServiceCategory_Object = MibTableColumn
atmTraceFilterRecordServiceCategory = _AtmTraceFilterRecordServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 4),
    _AtmTraceFilterRecordServiceCategory_Type()
)
atmTraceFilterRecordServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterRecordServiceCategory.setStatus("current")
_AtmTraceFilterRecordInIf_Type = InterfaceIndex
_AtmTraceFilterRecordInIf_Object = MibTableColumn
atmTraceFilterRecordInIf = _AtmTraceFilterRecordInIf_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 5),
    _AtmTraceFilterRecordInIf_Type()
)
atmTraceFilterRecordInIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterRecordInIf.setStatus("current")
_AtmTraceFilterRecordOutIf_Type = InterfaceIndexOrZero
_AtmTraceFilterRecordOutIf_Object = MibTableColumn
atmTraceFilterRecordOutIf = _AtmTraceFilterRecordOutIf_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 6),
    _AtmTraceFilterRecordOutIf_Type()
)
atmTraceFilterRecordOutIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterRecordOutIf.setStatus("current")
_AtmTraceFilterRecordCallingParty_Type = AtmAddr
_AtmTraceFilterRecordCallingParty_Object = MibTableColumn
atmTraceFilterRecordCallingParty = _AtmTraceFilterRecordCallingParty_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 7),
    _AtmTraceFilterRecordCallingParty_Type()
)
atmTraceFilterRecordCallingParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterRecordCallingParty.setStatus("current")
_AtmTraceFilterRecordCalledParty_Type = AtmAddr
_AtmTraceFilterRecordCalledParty_Object = MibTableColumn
atmTraceFilterRecordCalledParty = _AtmTraceFilterRecordCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 4, 2, 1, 8),
    _AtmTraceFilterRecordCalledParty_Type()
)
atmTraceFilterRecordCalledParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceFilterRecordCalledParty.setStatus("current")
_AtmTraceRecordGroup_ObjectIdentity = ObjectIdentity
atmTraceRecordGroup = _AtmTraceRecordGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5)
)
_AtmTraceRecordTable_Object = MibTable
atmTraceRecordTable = _AtmTraceRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    atmTraceRecordTable.setStatus("current")
_AtmTraceRecordEntry_Object = MibTableRow
atmTraceRecordEntry = _AtmTraceRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1)
)
atmTraceRecordEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTraceRecordIndex"),
)
if mibBuilder.loadTexts:
    atmTraceRecordEntry.setStatus("current")
_AtmTraceRecordIndex_Type = AtmTraceRecordIndex
_AtmTraceRecordIndex_Object = MibTableColumn
atmTraceRecordIndex = _AtmTraceRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 1),
    _AtmTraceRecordIndex_Type()
)
atmTraceRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceRecordIndex.setStatus("current")


class _AtmTraceRecordStatus_Type(Integer32):
    """Custom type atmTraceRecordStatus based on Integer32"""
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
        *(("traceCompletedNormally", 2),
          ("traceExceededIELengthLimitations", 4),
          ("traceExceededMessageLengthLimitations", 5),
          ("traceInProgress", 1),
          ("traceIncomplete", 3),
          ("traceLackResource", 6))
    )


_AtmTraceRecordStatus_Type.__name__ = "Integer32"
_AtmTraceRecordStatus_Object = MibTableColumn
atmTraceRecordStatus = _AtmTraceRecordStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 2),
    _AtmTraceRecordStatus_Type()
)
atmTraceRecordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordStatus.setStatus("current")


class _AtmTraceRecordCause_Type(Integer32):
    """Custom type atmTraceRecordCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmTraceRecordCause_Type.__name__ = "Integer32"
_AtmTraceRecordCause_Object = MibTableColumn
atmTraceRecordCause = _AtmTraceRecordCause_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 3),
    _AtmTraceRecordCause_Type()
)
atmTraceRecordCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordCause.setStatus("current")


class _AtmTraceRecordDiags_Type(OctetString):
    """Custom type atmTraceRecordDiags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AtmTraceRecordDiags_Type.__name__ = "OctetString"
_AtmTraceRecordDiags_Object = MibTableColumn
atmTraceRecordDiags = _AtmTraceRecordDiags_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 4),
    _AtmTraceRecordDiags_Type()
)
atmTraceRecordDiags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordDiags.setStatus("current")
_AtmTraceRecordTraceSourcePortId_Type = PnniPortId
_AtmTraceRecordTraceSourcePortId_Object = MibTableColumn
atmTraceRecordTraceSourcePortId = _AtmTraceRecordTraceSourcePortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 5),
    _AtmTraceRecordTraceSourcePortId_Type()
)
atmTraceRecordTraceSourcePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceSourcePortId.setStatus("current")
_AtmTraceRecordTraceSourceDlci_Type = Integer32
_AtmTraceRecordTraceSourceDlci_Object = MibTableColumn
atmTraceRecordTraceSourceDlci = _AtmTraceRecordTraceSourceDlci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 6),
    _AtmTraceRecordTraceSourceDlci_Type()
)
atmTraceRecordTraceSourceDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceSourceDlci.setStatus("current")
_AtmTraceRecordTraceDestVpi_Type = AtmVpIdentifier
_AtmTraceRecordTraceDestVpi_Object = MibTableColumn
atmTraceRecordTraceDestVpi = _AtmTraceRecordTraceDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 7),
    _AtmTraceRecordTraceDestVpi_Type()
)
atmTraceRecordTraceDestVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceDestVpi.setStatus("current")
_AtmTraceRecordTraceDestVci_Type = AtmVcIdentifier
_AtmTraceRecordTraceDestVci_Object = MibTableColumn
atmTraceRecordTraceDestVci = _AtmTraceRecordTraceDestVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 8),
    _AtmTraceRecordTraceDestVci_Type()
)
atmTraceRecordTraceDestVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceDestVci.setStatus("current")
_AtmTraceRecordTraceDestCallRef_Type = CallReference
_AtmTraceRecordTraceDestCallRef_Object = MibTableColumn
atmTraceRecordTraceDestCallRef = _AtmTraceRecordTraceDestCallRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 9),
    _AtmTraceRecordTraceDestCallRef_Type()
)
atmTraceRecordTraceDestCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceDestCallRef.setStatus("current")
_AtmTraceRecordTraceDestEndPtRef_Type = AtmEndPointReference
_AtmTraceRecordTraceDestEndPtRef_Object = MibTableColumn
atmTraceRecordTraceDestEndPtRef = _AtmTraceRecordTraceDestEndPtRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 10),
    _AtmTraceRecordTraceDestEndPtRef_Type()
)
atmTraceRecordTraceDestEndPtRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceDestEndPtRef.setStatus("current")
_AtmTraceRecordTraceDestDlci_Type = Integer32
_AtmTraceRecordTraceDestDlci_Object = MibTableColumn
atmTraceRecordTraceDestDlci = _AtmTraceRecordTraceDestDlci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 11),
    _AtmTraceRecordTraceDestDlci_Type()
)
atmTraceRecordTraceDestDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceDestDlci.setStatus("current")
_AtmTraceRecordTimeStamp_Type = TimeStamp
_AtmTraceRecordTimeStamp_Object = MibTableColumn
atmTraceRecordTimeStamp = _AtmTraceRecordTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 12),
    _AtmTraceRecordTimeStamp_Type()
)
atmTraceRecordTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTimeStamp.setStatus("current")
_AtmTraceRecordTraceDestReceiveLabel_Type = MplsLabel
_AtmTraceRecordTraceDestReceiveLabel_Object = MibTableColumn
atmTraceRecordTraceDestReceiveLabel = _AtmTraceRecordTraceDestReceiveLabel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 13),
    _AtmTraceRecordTraceDestReceiveLabel_Type()
)
atmTraceRecordTraceDestReceiveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceDestReceiveLabel.setStatus("current")
_AtmTraceRecordTraceDestTransmitLabel_Type = MplsLabel
_AtmTraceRecordTraceDestTransmitLabel_Object = MibTableColumn
atmTraceRecordTraceDestTransmitLabel = _AtmTraceRecordTraceDestTransmitLabel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 1, 1, 14),
    _AtmTraceRecordTraceDestTransmitLabel_Type()
)
atmTraceRecordTraceDestTransmitLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceRecordTraceDestTransmitLabel.setStatus("current")
_AtmTraceInfoTable_Object = MibTable
atmTraceInfoTable = _AtmTraceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    atmTraceInfoTable.setStatus("current")
_AtmTraceInfoEntry_Object = MibTableRow
atmTraceInfoEntry = _AtmTraceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1)
)
atmTraceInfoEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTraceRecordIndex"),
    (0, "ATM-TRACE-MIB", "atmTraceInfoSequenceIndex"),
)
if mibBuilder.loadTexts:
    atmTraceInfoEntry.setStatus("current")


class _AtmTraceInfoSequenceIndex_Type(Integer32):
    """Custom type atmTraceInfoSequenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AtmTraceInfoSequenceIndex_Type.__name__ = "Integer32"
_AtmTraceInfoSequenceIndex_Object = MibTableColumn
atmTraceInfoSequenceIndex = _AtmTraceInfoSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 1),
    _AtmTraceInfoSequenceIndex_Type()
)
atmTraceInfoSequenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceInfoSequenceIndex.setStatus("current")
_AtmTraceInfoNodeId_Type = PnniNodeId
_AtmTraceInfoNodeId_Object = MibTableColumn
atmTraceInfoNodeId = _AtmTraceInfoNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 2),
    _AtmTraceInfoNodeId_Type()
)
atmTraceInfoNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoNodeId.setStatus("current")
_AtmTraceInfoOutgoingPortId_Type = PnniPortId
_AtmTraceInfoOutgoingPortId_Object = MibTableColumn
atmTraceInfoOutgoingPortId = _AtmTraceInfoOutgoingPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 3),
    _AtmTraceInfoOutgoingPortId_Type()
)
atmTraceInfoOutgoingPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoOutgoingPortId.setStatus("current")
_AtmTraceInfoIncomingVpi_Type = AtmVpIdentifier
_AtmTraceInfoIncomingVpi_Object = MibTableColumn
atmTraceInfoIncomingVpi = _AtmTraceInfoIncomingVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 4),
    _AtmTraceInfoIncomingVpi_Type()
)
atmTraceInfoIncomingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoIncomingVpi.setStatus("current")
_AtmTraceInfoIncomingVci_Type = AtmVcIdentifier
_AtmTraceInfoIncomingVci_Object = MibTableColumn
atmTraceInfoIncomingVci = _AtmTraceInfoIncomingVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 5),
    _AtmTraceInfoIncomingVci_Type()
)
atmTraceInfoIncomingVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoIncomingVci.setStatus("current")
_AtmTraceInfoIncomingCallRef_Type = CallReference
_AtmTraceInfoIncomingCallRef_Object = MibTableColumn
atmTraceInfoIncomingCallRef = _AtmTraceInfoIncomingCallRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 6),
    _AtmTraceInfoIncomingCallRef_Type()
)
atmTraceInfoIncomingCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoIncomingCallRef.setStatus("current")
_AtmTraceInfoIncomingEndPtRef_Type = AtmEndPointReference
_AtmTraceInfoIncomingEndPtRef_Object = MibTableColumn
atmTraceInfoIncomingEndPtRef = _AtmTraceInfoIncomingEndPtRef_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 7),
    _AtmTraceInfoIncomingEndPtRef_Type()
)
atmTraceInfoIncomingEndPtRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoIncomingEndPtRef.setStatus("current")
_AtmTraceInfoRefusalIndicator_Type = TruthValue
_AtmTraceInfoRefusalIndicator_Object = MibTableColumn
atmTraceInfoRefusalIndicator = _AtmTraceInfoRefusalIndicator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 8),
    _AtmTraceInfoRefusalIndicator_Type()
)
atmTraceInfoRefusalIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoRefusalIndicator.setStatus("current")
_AtmTraceInfoCrankBackRcvdAtDest_Type = TruthValue
_AtmTraceInfoCrankBackRcvdAtDest_Object = MibTableColumn
atmTraceInfoCrankBackRcvdAtDest = _AtmTraceInfoCrankBackRcvdAtDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 9),
    _AtmTraceInfoCrankBackRcvdAtDest_Type()
)
atmTraceInfoCrankBackRcvdAtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoCrankBackRcvdAtDest.setStatus("current")
_AtmTraceInfoCrankBackGap_Type = TruthValue
_AtmTraceInfoCrankBackGap_Object = MibTableColumn
atmTraceInfoCrankBackGap = _AtmTraceInfoCrankBackGap_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 10),
    _AtmTraceInfoCrankBackGap_Type()
)
atmTraceInfoCrankBackGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoCrankBackGap.setStatus("current")
_AtmTraceInfoCrankBackIndicator_Type = TruthValue
_AtmTraceInfoCrankBackIndicator_Object = MibTableColumn
atmTraceInfoCrankBackIndicator = _AtmTraceInfoCrankBackIndicator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 11),
    _AtmTraceInfoCrankBackIndicator_Type()
)
atmTraceInfoCrankBackIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoCrankBackIndicator.setStatus("current")


class _AtmTraceInfoCrankBackBlockedTransitType_Type(Integer32):
    """Custom type atmTraceInfoCrankBackBlockedTransitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockedIncomingLink", 1),
          ("blockedNode", 2),
          ("blockedOutgoingLink", 3))
    )


_AtmTraceInfoCrankBackBlockedTransitType_Type.__name__ = "Integer32"
_AtmTraceInfoCrankBackBlockedTransitType_Object = MibTableColumn
atmTraceInfoCrankBackBlockedTransitType = _AtmTraceInfoCrankBackBlockedTransitType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 12),
    _AtmTraceInfoCrankBackBlockedTransitType_Type()
)
atmTraceInfoCrankBackBlockedTransitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoCrankBackBlockedTransitType.setStatus("current")
_AtmTraceInfoCrankBackBlockedTransitInfo_Type = OctetString
_AtmTraceInfoCrankBackBlockedTransitInfo_Object = MibTableColumn
atmTraceInfoCrankBackBlockedTransitInfo = _AtmTraceInfoCrankBackBlockedTransitInfo_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 13),
    _AtmTraceInfoCrankBackBlockedTransitInfo_Type()
)
atmTraceInfoCrankBackBlockedTransitInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoCrankBackBlockedTransitInfo.setStatus("current")
_AtmTraceInfoCrankBackCause_Type = Integer32
_AtmTraceInfoCrankBackCause_Object = MibTableColumn
atmTraceInfoCrankBackCause = _AtmTraceInfoCrankBackCause_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 14),
    _AtmTraceInfoCrankBackCause_Type()
)
atmTraceInfoCrankBackCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoCrankBackCause.setStatus("current")
_AtmTraceInfoReceiveLabel_Type = MplsLabel
_AtmTraceInfoReceiveLabel_Object = MibTableColumn
atmTraceInfoReceiveLabel = _AtmTraceInfoReceiveLabel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 15),
    _AtmTraceInfoReceiveLabel_Type()
)
atmTraceInfoReceiveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoReceiveLabel.setStatus("current")
_AtmTraceInfoTransmitLabel_Type = MplsLabel
_AtmTraceInfoTransmitLabel_Object = MibTableColumn
atmTraceInfoTransmitLabel = _AtmTraceInfoTransmitLabel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 2, 1, 16),
    _AtmTraceInfoTransmitLabel_Type()
)
atmTraceInfoTransmitLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoTransmitLabel.setStatus("current")
_AtmTraceInfoNeNscTable_Object = MibTable
atmTraceInfoNeNscTable = _AtmTraceInfoNeNscTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    atmTraceInfoNeNscTable.setStatus("current")
_AtmTraceInfoNeNscEntry_Object = MibTableRow
atmTraceInfoNeNscEntry = _AtmTraceInfoNeNscEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 3, 1)
)
atmTraceInfoNeNscEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTraceRecordIndex"),
    (0, "ATM-TRACE-MIB", "atmTraceInfoSequenceIndex"),
    (0, "ATM-TRACE-MIB", "atmTraceInfoNeNscInterface"),
    (0, "ATM-TRACE-MIB", "atmTraceInfoNeNscIndex"),
)
if mibBuilder.loadTexts:
    atmTraceInfoNeNscEntry.setStatus("current")


class _AtmTraceInfoNeNscInterface_Type(Integer32):
    """Custom type atmTraceInfoNeNscInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AtmTraceInfoNeNscInterface_Type.__name__ = "Integer32"
_AtmTraceInfoNeNscInterface_Object = MibTableColumn
atmTraceInfoNeNscInterface = _AtmTraceInfoNeNscInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 3, 1, 1),
    _AtmTraceInfoNeNscInterface_Type()
)
atmTraceInfoNeNscInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceInfoNeNscInterface.setStatus("current")


class _AtmTraceInfoNeNscIndex_Type(Integer32):
    """Custom type atmTraceInfoNeNscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_AtmTraceInfoNeNscIndex_Type.__name__ = "Integer32"
_AtmTraceInfoNeNscIndex_Object = MibTableColumn
atmTraceInfoNeNscIndex = _AtmTraceInfoNeNscIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 3, 1, 2),
    _AtmTraceInfoNeNscIndex_Type()
)
atmTraceInfoNeNscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceInfoNeNscIndex.setStatus("current")
_AtmTraceInfoNeNsc_Type = NetworkEntityNetworkServiceCategory
_AtmTraceInfoNeNsc_Object = MibTableColumn
atmTraceInfoNeNsc = _AtmTraceInfoNeNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 3, 1, 3),
    _AtmTraceInfoNeNsc_Type()
)
atmTraceInfoNeNsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoNeNsc.setStatus("current")
_AtmTraceInfoRpNscTable_Object = MibTable
atmTraceInfoRpNscTable = _AtmTraceInfoRpNscTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    atmTraceInfoRpNscTable.setStatus("current")
_AtmTraceInfoRpNscEntry_Object = MibTableRow
atmTraceInfoRpNscEntry = _AtmTraceInfoRpNscEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 4, 1)
)
atmTraceInfoRpNscEntry.setIndexNames(
    (0, "ATM-TRACE-MIB", "atmTraceRecordIndex"),
    (0, "ATM-TRACE-MIB", "atmTraceInfoSequenceIndex"),
    (0, "ATM-TRACE-MIB", "atmTraceInfoRpNscInterface"),
    (0, "ATM-TRACE-MIB", "atmTraceInfoRpNscSequenceIndex"),
)
if mibBuilder.loadTexts:
    atmTraceInfoRpNscEntry.setStatus("current")


class _AtmTraceInfoRpNscInterface_Type(Integer32):
    """Custom type atmTraceInfoRpNscInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AtmTraceInfoRpNscInterface_Type.__name__ = "Integer32"
_AtmTraceInfoRpNscInterface_Object = MibTableColumn
atmTraceInfoRpNscInterface = _AtmTraceInfoRpNscInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 4, 1, 1),
    _AtmTraceInfoRpNscInterface_Type()
)
atmTraceInfoRpNscInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceInfoRpNscInterface.setStatus("current")


class _AtmTraceInfoRpNscSequenceIndex_Type(Integer32):
    """Custom type atmTraceInfoRpNscSequenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_AtmTraceInfoRpNscSequenceIndex_Type.__name__ = "Integer32"
_AtmTraceInfoRpNscSequenceIndex_Object = MibTableColumn
atmTraceInfoRpNscSequenceIndex = _AtmTraceInfoRpNscSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 4, 1, 2),
    _AtmTraceInfoRpNscSequenceIndex_Type()
)
atmTraceInfoRpNscSequenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTraceInfoRpNscSequenceIndex.setStatus("current")
_AtmTraceInfoRpNsc_Type = ResourcePartitionNetworkServiceCategory
_AtmTraceInfoRpNsc_Object = MibTableColumn
atmTraceInfoRpNsc = _AtmTraceInfoRpNsc_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 5, 4, 1, 3),
    _AtmTraceInfoRpNsc_Type()
)
atmTraceInfoRpNsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTraceInfoRpNsc.setStatus("current")
_AtmTraceIfGroup_ObjectIdentity = ObjectIdentity
atmTraceIfGroup = _AtmTraceIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 6)
)
_AtmTraceIfTable_Object = MibTable
atmTraceIfTable = _AtmTraceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    atmTraceIfTable.setStatus("current")
_AtmTraceIfEntry_Object = MibTableRow
atmTraceIfEntry = _AtmTraceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    atmTraceIfEntry.setStatus("current")


class _AtmTraceIfTraceBoundary_Type(TruthValue):
    """Custom type atmTraceIfTraceBoundary based on TruthValue"""


_AtmTraceIfTraceBoundary_Object = MibTableColumn
atmTraceIfTraceBoundary = _AtmTraceIfTraceBoundary_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 1, 6, 1, 1, 1),
    _AtmTraceIfTraceBoundary_Type()
)
atmTraceIfTraceBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTraceIfTraceBoundary.setStatus("current")
_AtmTraceMIBTrapsPrefix_ObjectIdentity = ObjectIdentity
atmTraceMIBTrapsPrefix = _AtmTraceMIBTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 2)
)
_AtmTraceMIBTraps_ObjectIdentity = ObjectIdentity
atmTraceMIBTraps = _AtmTraceMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 2, 0)
)
_AtmTraceMIBConformance_ObjectIdentity = ObjectIdentity
atmTraceMIBConformance = _AtmTraceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3)
)
_AtmTraceMIBCompliances_ObjectIdentity = ObjectIdentity
atmTraceMIBCompliances = _AtmTraceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 1)
)
_AtmTraceMIBGroups_ObjectIdentity = ObjectIdentity
atmTraceMIBGroups = _AtmTraceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2)
)
pnniIfEntry.registerAugmentions(
    ("ATM-TRACE-MIB",
     "atmTraceIfEntry")
)
atmTraceIfEntry.setIndexNames(*pnniIfEntry.getIndexNames())

# Managed Objects groups

atmTraceMIBMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 1)
)
atmTraceMIBMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceMaxConcurrentRequests"),
        ("ATM-TRACE-MIB", "atmTraceAvailableRequests"),
        ("ATM-TRACE-MIB", "atmTraceTransitListMaximumSize"),
        ("ATM-TRACE-MIB", "atmTraceRecordStatus"),
        ("ATM-TRACE-MIB", "atmTraceRecordTraceSourcePortId"),
        ("ATM-TRACE-MIB", "atmTraceRecordTimeStamp"),
        ("ATM-TRACE-MIB", "atmTraceInfoNodeId"),
        ("ATM-TRACE-MIB", "atmTraceInfoOutgoingPortId"),
        ("ATM-TRACE-MIB", "atmTraceInfoRefusalIndicator"))
)
if mibBuilder.loadTexts:
    atmTraceMIBMandatoryGroup.setStatus("current")

atmTraceMIBOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 2)
)
atmTraceMIBOptionalGroup.setObjects(
    ("ATM-TRACE-MIB", "atmTraceRecordTraceSourceDlci")
)
if mibBuilder.loadTexts:
    atmTraceMIBOptionalGroup.setStatus("current")

atmTraceConnAndPathFilterMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 3)
)
atmTraceConnAndPathFilterMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceRecordTraceDestVpi"),
        ("ATM-TRACE-MIB", "atmTraceRecordTraceDestVci"),
        ("ATM-TRACE-MIB", "atmTraceRecordTraceDestCallRef"),
        ("ATM-TRACE-MIB", "atmTraceRecordTraceDestEndPtRef"),
        ("ATM-TRACE-MIB", "atmTraceRecordTraceDestDlci"),
        ("ATM-TRACE-MIB", "atmTraceInfoIncomingVpi"),
        ("ATM-TRACE-MIB", "atmTraceInfoIncomingVci"),
        ("ATM-TRACE-MIB", "atmTraceInfoIncomingCallRef"),
        ("ATM-TRACE-MIB", "atmTraceInfoIncomingEndPtRef"))
)
if mibBuilder.loadTexts:
    atmTraceConnAndPathFilterMandatoryGroup.setStatus("current")

atmTracePathMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 4)
)
atmTracePathMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceRecordCause"),
        ("ATM-TRACE-MIB", "atmTraceRecordDiags"),
        ("ATM-TRACE-MIB", "atmTraceInfoCrankBackRcvdAtDest"),
        ("ATM-TRACE-MIB", "atmTraceInfoCrankBackGap"),
        ("ATM-TRACE-MIB", "atmTraceInfoCrankBackIndicator"),
        ("ATM-TRACE-MIB", "atmTraceInfoCrankBackBlockedTransitType"),
        ("ATM-TRACE-MIB", "atmTraceInfoCrankBackBlockedTransitInfo"),
        ("ATM-TRACE-MIB", "atmTraceInfoCrankBackCause"))
)
if mibBuilder.loadTexts:
    atmTracePathMandatoryGroup.setStatus("current")

atmTraceConnMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 5)
)
atmTraceConnMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceConnOwner"),
        ("ATM-TRACE-MIB", "atmTraceConnTraceSourceIf"),
        ("ATM-TRACE-MIB", "atmTraceConnOrigConnType"),
        ("ATM-TRACE-MIB", "atmTraceConnOrigVpi"),
        ("ATM-TRACE-MIB", "atmTraceConnOrigVci"),
        ("ATM-TRACE-MIB", "atmTraceConnEndPtRef"),
        ("ATM-TRACE-MIB", "atmTraceConnOrigDirection"),
        ("ATM-TRACE-MIB", "atmTraceConnTraceConnId"),
        ("ATM-TRACE-MIB", "atmTraceConnTraceCallRef"),
        ("ATM-TRACE-MIB", "atmTraceConnPassAlongRequest"),
        ("ATM-TRACE-MIB", "atmTraceConnFailTimeout"),
        ("ATM-TRACE-MIB", "atmTraceConnAgeTimeout"),
        ("ATM-TRACE-MIB", "atmTraceConnRestart"),
        ("ATM-TRACE-MIB", "atmTraceConnRecordIndex"),
        ("ATM-TRACE-MIB", "atmTraceConnRowStatus"))
)
if mibBuilder.loadTexts:
    atmTraceConnMandatoryGroup.setStatus("current")

atmTraceConnOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 6)
)
atmTraceConnOptionalGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceConnCallRef"),
        ("ATM-TRACE-MIB", "atmTraceConnOrigDlci"),
        ("ATM-TRACE-MIB", "atmTraceConnTrapOnCompletion"))
)
if mibBuilder.loadTexts:
    atmTraceConnOptionalGroup.setStatus("current")

atmTracePathTestMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 7)
)
atmTracePathTestMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTracePathTestOwner"),
        ("ATM-TRACE-MIB", "atmTracePathTestConnType"),
        ("ATM-TRACE-MIB", "atmTracePathTestConnCastType"),
        ("ATM-TRACE-MIB", "atmTracePathTestTraceSourceIf"),
        ("ATM-TRACE-MIB", "atmTracePathTestP2MpNewConn"),
        ("ATM-TRACE-MIB", "atmTracePathTestOrigVpi"),
        ("ATM-TRACE-MIB", "atmTracePathTestOrigVci"),
        ("ATM-TRACE-MIB", "atmTracePathTestCalledParty"),
        ("ATM-TRACE-MIB", "atmTracePathTestTxTrafDescrIndex"),
        ("ATM-TRACE-MIB", "atmTracePathTestRxTrafDescrIndex"),
        ("ATM-TRACE-MIB", "atmTracePathTestClearCallAtTDest"),
        ("ATM-TRACE-MIB", "atmTracePathTestTraceCrankback"),
        ("ATM-TRACE-MIB", "atmTracePathTestPassAlongRequest"),
        ("ATM-TRACE-MIB", "atmTracePathTestAgeTimeout"),
        ("ATM-TRACE-MIB", "atmTracePathTestRestart"),
        ("ATM-TRACE-MIB", "atmTracePathTestRecordIndex"),
        ("ATM-TRACE-MIB", "atmTracePathTestRowStatus"))
)
if mibBuilder.loadTexts:
    atmTracePathTestMandatoryGroup.setStatus("current")

atmTracePathTestOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 8)
)
atmTracePathTestOptionalGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTracePathTestCallingParty"),
        ("ATM-TRACE-MIB", "atmTracePathTestTraceConnId"),
        ("ATM-TRACE-MIB", "atmTracePathTestTraceCallRef"),
        ("ATM-TRACE-MIB", "atmTracePathTestTrapOnCompletion"))
)
if mibBuilder.loadTexts:
    atmTracePathTestOptionalGroup.setStatus("current")

atmTracePathFilterMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 9)
)
atmTracePathFilterMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceFilterControl"),
        ("ATM-TRACE-MIB", "atmTraceFilterOwner"),
        ("ATM-TRACE-MIB", "atmTraceFilterConnKind"),
        ("ATM-TRACE-MIB", "atmTraceFilterInIf"),
        ("ATM-TRACE-MIB", "atmTraceFilterCalledPartyPrefix"),
        ("ATM-TRACE-MIB", "atmTraceFilterCalledPartyLength"),
        ("ATM-TRACE-MIB", "atmTraceFilterClearCallAtTDest"),
        ("ATM-TRACE-MIB", "atmTraceFilterTraceCrankback"),
        ("ATM-TRACE-MIB", "atmTraceFilterTraceConnId"),
        ("ATM-TRACE-MIB", "atmTraceFilterTraceCallRef"),
        ("ATM-TRACE-MIB", "atmTraceFilterPassAlongRequest"),
        ("ATM-TRACE-MIB", "atmTraceFilterMaxRecords"),
        ("ATM-TRACE-MIB", "atmTraceFilterStopTimeout"),
        ("ATM-TRACE-MIB", "atmTraceFilterAgeTimeout"),
        ("ATM-TRACE-MIB", "atmTraceFilterPurge"),
        ("ATM-TRACE-MIB", "atmTraceFilterNumMatches"),
        ("ATM-TRACE-MIB", "atmTraceFilterRowStatus"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordConnKind"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordConnCastType"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordServiceCategory"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordInIf"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordOutIf"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordCallingParty"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordCalledParty"))
)
if mibBuilder.loadTexts:
    atmTracePathFilterMandatoryGroup.setStatus("current")

atmTracePathFilterOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 10)
)
atmTracePathFilterOptionalGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceFilterConnCastType"),
        ("ATM-TRACE-MIB", "atmTraceFilterServiceCategory"),
        ("ATM-TRACE-MIB", "atmTraceFilterOutIf"),
        ("ATM-TRACE-MIB", "atmTraceFilterCallingPartyPrefix"),
        ("ATM-TRACE-MIB", "atmTraceFilterCallingPartyLength"),
        ("ATM-TRACE-MIB", "atmTraceFilterRecordCountDown"),
        ("ATM-TRACE-MIB", "atmTraceFilterTrapEnable"))
)
if mibBuilder.loadTexts:
    atmTracePathFilterOptionalGroup.setStatus("current")

atmTraceIfOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 11)
)
atmTraceIfOptionalGroup.setObjects(
    ("ATM-TRACE-MIB", "atmTraceIfTraceBoundary")
)
if mibBuilder.loadTexts:
    atmTraceIfOptionalGroup.setStatus("current")

atmTraceConnAndPathFilterPolicyMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 13)
)
atmTraceConnAndPathFilterPolicyMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceInfoNeNsc"),
        ("ATM-TRACE-MIB", "atmTraceInfoRpNsc"))
)
if mibBuilder.loadTexts:
    atmTraceConnAndPathFilterPolicyMandatoryGroup.setStatus("current")

atmTraceConnPolicyMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 14)
)
atmTraceConnPolicyMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceConnTraceNeNsc"),
        ("ATM-TRACE-MIB", "atmTraceConnTraceRpNsc"),
        ("ATM-TRACE-MIB", "atmTraceConnTraceIncoming"))
)
if mibBuilder.loadTexts:
    atmTraceConnPolicyMandatoryGroup.setStatus("current")

atmTracePathTestPolicyMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 15)
)
atmTracePathTestPolicyMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTracePathTestTraceNeNsc"),
        ("ATM-TRACE-MIB", "atmTracePathTestTraceRpNsc"),
        ("ATM-TRACE-MIB", "atmTracePathTestTraceIncoming"))
)
if mibBuilder.loadTexts:
    atmTracePathTestPolicyMandatoryGroup.setStatus("current")

atmTracePathFilterPolicyMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 16)
)
atmTracePathFilterPolicyMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceFilterPolicy"),
        ("ATM-TRACE-MIB", "atmTraceFilterTraceNeNsc"),
        ("ATM-TRACE-MIB", "atmTraceFilterTraceRpNsc"),
        ("ATM-TRACE-MIB", "atmTraceFilterTraceIncoming"))
)
if mibBuilder.loadTexts:
    atmTracePathFilterPolicyMandatoryGroup.setStatus("current")

atmTraceConnAndPathFilterMplsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 17)
)
atmTraceConnAndPathFilterMplsMandatoryGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceRecordTraceDestReceiveLabel"),
        ("ATM-TRACE-MIB", "atmTraceRecordTraceDestTransmitLabel"),
        ("ATM-TRACE-MIB", "atmTraceInfoReceiveLabel"),
        ("ATM-TRACE-MIB", "atmTraceInfoTransmitLabel"))
)
if mibBuilder.loadTexts:
    atmTraceConnAndPathFilterMplsMandatoryGroup.setStatus("current")

atmTraceConnMplsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 18)
)
atmTraceConnMplsMandatoryGroup.setObjects(
    ("ATM-TRACE-MIB", "atmTraceConnTraceLabels")
)
if mibBuilder.loadTexts:
    atmTraceConnMplsMandatoryGroup.setStatus("current")

atmTracePathTestMplsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 19)
)
atmTracePathTestMplsMandatoryGroup.setObjects(
    ("ATM-TRACE-MIB", "atmTracePathTestTraceLabels")
)
if mibBuilder.loadTexts:
    atmTracePathTestMplsMandatoryGroup.setStatus("current")

atmTracePathFilterMplsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 20)
)
atmTracePathFilterMplsMandatoryGroup.setObjects(
    ("ATM-TRACE-MIB", "atmTraceFilterTraceLabels")
)
if mibBuilder.loadTexts:
    atmTracePathFilterMplsMandatoryGroup.setStatus("current")


# Notification objects

atmTraceConnCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 2, 0, 1)
)
atmTraceConnCompletion.setObjects(
    ("ATM-TRACE-MIB", "atmTraceConnRecordIndex")
)
if mibBuilder.loadTexts:
    atmTraceConnCompletion.setStatus(
        "current"
    )

atmTracePathTestCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 2, 0, 2)
)
atmTracePathTestCompletion.setObjects(
    ("ATM-TRACE-MIB", "atmTracePathTestRecordIndex")
)
if mibBuilder.loadTexts:
    atmTracePathTestCompletion.setStatus(
        "current"
    )

atmTracePathFilterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 2, 0, 3)
)
atmTracePathFilterTrap.setObjects(
    ("ATM-TRACE-MIB", "atmTraceFilterRecordConnKind")
)
if mibBuilder.loadTexts:
    atmTracePathFilterTrap.setStatus(
        "current"
    )


# Notifications groups

atmTraceNotificationOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 2, 12)
)
atmTraceNotificationOptionalGroup.setObjects(
      *(("ATM-TRACE-MIB", "atmTraceConnCompletion"),
        ("ATM-TRACE-MIB", "atmTracePathTestCompletion"),
        ("ATM-TRACE-MIB", "atmTracePathFilterTrap"))
)
if mibBuilder.loadTexts:
    atmTraceNotificationOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

atmTraceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    atmTraceMIBCompliance.setStatus(
        "deprecated"
    )

atmTraceMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    atmTraceMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-TRACE-MIB",
    **{"CallReference": CallReference,
       "AtmEndPointReference": AtmEndPointReference,
       "AtmTraceRecordIndex": AtmTraceRecordIndex,
       "AtmTraceOwnerString": AtmTraceOwnerString,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfSignalling": atmfSignalling,
       "atmfTrace": atmfTrace,
       "atmTraceMIB": atmTraceMIB,
       "atmTraceMIBObjects": atmTraceMIBObjects,
       "atmTraceBaseGroup": atmTraceBaseGroup,
       "atmTraceFilterControl": atmTraceFilterControl,
       "atmTraceMaxConcurrentRequests": atmTraceMaxConcurrentRequests,
       "atmTraceAvailableRequests": atmTraceAvailableRequests,
       "atmTraceTransitListMaximumSize": atmTraceTransitListMaximumSize,
       "atmTraceConnGroup": atmTraceConnGroup,
       "atmTraceConnTable": atmTraceConnTable,
       "atmTraceConnEntry": atmTraceConnEntry,
       "atmTraceConnIndex": atmTraceConnIndex,
       "atmTraceConnOwner": atmTraceConnOwner,
       "atmTraceConnTraceSourceIf": atmTraceConnTraceSourceIf,
       "atmTraceConnOrigConnType": atmTraceConnOrigConnType,
       "atmTraceConnOrigVpi": atmTraceConnOrigVpi,
       "atmTraceConnOrigVci": atmTraceConnOrigVci,
       "atmTraceConnEndPtRef": atmTraceConnEndPtRef,
       "atmTraceConnCallRef": atmTraceConnCallRef,
       "atmTraceConnOrigDlci": atmTraceConnOrigDlci,
       "atmTraceConnOrigDirection": atmTraceConnOrigDirection,
       "atmTraceConnTraceConnId": atmTraceConnTraceConnId,
       "atmTraceConnTraceCallRef": atmTraceConnTraceCallRef,
       "atmTraceConnPassAlongRequest": atmTraceConnPassAlongRequest,
       "atmTraceConnFailTimeout": atmTraceConnFailTimeout,
       "atmTraceConnAgeTimeout": atmTraceConnAgeTimeout,
       "atmTraceConnRestart": atmTraceConnRestart,
       "atmTraceConnTrapOnCompletion": atmTraceConnTrapOnCompletion,
       "atmTraceConnRecordIndex": atmTraceConnRecordIndex,
       "atmTraceConnRowStatus": atmTraceConnRowStatus,
       "atmTraceConnTraceNeNsc": atmTraceConnTraceNeNsc,
       "atmTraceConnTraceRpNsc": atmTraceConnTraceRpNsc,
       "atmTraceConnTraceIncoming": atmTraceConnTraceIncoming,
       "atmTraceConnTraceLabels": atmTraceConnTraceLabels,
       "atmTracePathTestGroup": atmTracePathTestGroup,
       "atmTracePathTestTable": atmTracePathTestTable,
       "atmTracePathTestEntry": atmTracePathTestEntry,
       "atmTracePathTestIndex": atmTracePathTestIndex,
       "atmTracePathTestOwner": atmTracePathTestOwner,
       "atmTracePathTestConnType": atmTracePathTestConnType,
       "atmTracePathTestConnCastType": atmTracePathTestConnCastType,
       "atmTracePathTestTraceSourceIf": atmTracePathTestTraceSourceIf,
       "atmTracePathTestP2MpNewConn": atmTracePathTestP2MpNewConn,
       "atmTracePathTestOrigVpi": atmTracePathTestOrigVpi,
       "atmTracePathTestOrigVci": atmTracePathTestOrigVci,
       "atmTracePathTestCalledParty": atmTracePathTestCalledParty,
       "atmTracePathTestCallingParty": atmTracePathTestCallingParty,
       "atmTracePathTestRxTrafDescrIndex": atmTracePathTestRxTrafDescrIndex,
       "atmTracePathTestTxTrafDescrIndex": atmTracePathTestTxTrafDescrIndex,
       "atmTracePathTestClearCallAtTDest": atmTracePathTestClearCallAtTDest,
       "atmTracePathTestTraceCrankback": atmTracePathTestTraceCrankback,
       "atmTracePathTestTraceConnId": atmTracePathTestTraceConnId,
       "atmTracePathTestTraceCallRef": atmTracePathTestTraceCallRef,
       "atmTracePathTestPassAlongRequest": atmTracePathTestPassAlongRequest,
       "atmTracePathTestAgeTimeout": atmTracePathTestAgeTimeout,
       "atmTracePathTestRestart": atmTracePathTestRestart,
       "atmTracePathTestTrapOnCompletion": atmTracePathTestTrapOnCompletion,
       "atmTracePathTestRecordIndex": atmTracePathTestRecordIndex,
       "atmTracePathTestRowStatus": atmTracePathTestRowStatus,
       "atmTracePathTestTraceNeNsc": atmTracePathTestTraceNeNsc,
       "atmTracePathTestTraceRpNsc": atmTracePathTestTraceRpNsc,
       "atmTracePathTestTraceIncoming": atmTracePathTestTraceIncoming,
       "atmTracePathTestPolicyConstraint": atmTracePathTestPolicyConstraint,
       "atmTracePathTestTraceLabels": atmTracePathTestTraceLabels,
       "atmTraceFilterGroup": atmTraceFilterGroup,
       "atmTraceFilterTable": atmTraceFilterTable,
       "atmTraceFilterEntry": atmTraceFilterEntry,
       "atmTraceFilterIndex": atmTraceFilterIndex,
       "atmTraceFilterOwner": atmTraceFilterOwner,
       "atmTraceFilterConnKind": atmTraceFilterConnKind,
       "atmTraceFilterConnCastType": atmTraceFilterConnCastType,
       "atmTraceFilterServiceCategory": atmTraceFilterServiceCategory,
       "atmTraceFilterInIf": atmTraceFilterInIf,
       "atmTraceFilterOutIf": atmTraceFilterOutIf,
       "atmTraceFilterCallingPartyPrefix": atmTraceFilterCallingPartyPrefix,
       "atmTraceFilterCallingPartyLength": atmTraceFilterCallingPartyLength,
       "atmTraceFilterCalledPartyPrefix": atmTraceFilterCalledPartyPrefix,
       "atmTraceFilterCalledPartyLength": atmTraceFilterCalledPartyLength,
       "atmTraceFilterClearCallAtTDest": atmTraceFilterClearCallAtTDest,
       "atmTraceFilterTraceCrankback": atmTraceFilterTraceCrankback,
       "atmTraceFilterTraceConnId": atmTraceFilterTraceConnId,
       "atmTraceFilterTraceCallRef": atmTraceFilterTraceCallRef,
       "atmTraceFilterPassAlongRequest": atmTraceFilterPassAlongRequest,
       "atmTraceFilterMaxRecords": atmTraceFilterMaxRecords,
       "atmTraceFilterRecordCountDown": atmTraceFilterRecordCountDown,
       "atmTraceFilterStopTimeout": atmTraceFilterStopTimeout,
       "atmTraceFilterAgeTimeout": atmTraceFilterAgeTimeout,
       "atmTraceFilterPurge": atmTraceFilterPurge,
       "atmTraceFilterTrapEnable": atmTraceFilterTrapEnable,
       "atmTraceFilterNumMatches": atmTraceFilterNumMatches,
       "atmTraceFilterRowStatus": atmTraceFilterRowStatus,
       "atmTraceFilterPolicy": atmTraceFilterPolicy,
       "atmTraceFilterTraceNeNsc": atmTraceFilterTraceNeNsc,
       "atmTraceFilterTraceRpNsc": atmTraceFilterTraceRpNsc,
       "atmTraceFilterTraceIncoming": atmTraceFilterTraceIncoming,
       "atmTraceFilterTraceLabels": atmTraceFilterTraceLabels,
       "atmTraceFilterRecordTable": atmTraceFilterRecordTable,
       "atmTraceFilterRecordEntry": atmTraceFilterRecordEntry,
       "atmTraceFilterRecordIndex": atmTraceFilterRecordIndex,
       "atmTraceFilterRecordConnKind": atmTraceFilterRecordConnKind,
       "atmTraceFilterRecordConnCastType": atmTraceFilterRecordConnCastType,
       "atmTraceFilterRecordServiceCategory": atmTraceFilterRecordServiceCategory,
       "atmTraceFilterRecordInIf": atmTraceFilterRecordInIf,
       "atmTraceFilterRecordOutIf": atmTraceFilterRecordOutIf,
       "atmTraceFilterRecordCallingParty": atmTraceFilterRecordCallingParty,
       "atmTraceFilterRecordCalledParty": atmTraceFilterRecordCalledParty,
       "atmTraceRecordGroup": atmTraceRecordGroup,
       "atmTraceRecordTable": atmTraceRecordTable,
       "atmTraceRecordEntry": atmTraceRecordEntry,
       "atmTraceRecordIndex": atmTraceRecordIndex,
       "atmTraceRecordStatus": atmTraceRecordStatus,
       "atmTraceRecordCause": atmTraceRecordCause,
       "atmTraceRecordDiags": atmTraceRecordDiags,
       "atmTraceRecordTraceSourcePortId": atmTraceRecordTraceSourcePortId,
       "atmTraceRecordTraceSourceDlci": atmTraceRecordTraceSourceDlci,
       "atmTraceRecordTraceDestVpi": atmTraceRecordTraceDestVpi,
       "atmTraceRecordTraceDestVci": atmTraceRecordTraceDestVci,
       "atmTraceRecordTraceDestCallRef": atmTraceRecordTraceDestCallRef,
       "atmTraceRecordTraceDestEndPtRef": atmTraceRecordTraceDestEndPtRef,
       "atmTraceRecordTraceDestDlci": atmTraceRecordTraceDestDlci,
       "atmTraceRecordTimeStamp": atmTraceRecordTimeStamp,
       "atmTraceRecordTraceDestReceiveLabel": atmTraceRecordTraceDestReceiveLabel,
       "atmTraceRecordTraceDestTransmitLabel": atmTraceRecordTraceDestTransmitLabel,
       "atmTraceInfoTable": atmTraceInfoTable,
       "atmTraceInfoEntry": atmTraceInfoEntry,
       "atmTraceInfoSequenceIndex": atmTraceInfoSequenceIndex,
       "atmTraceInfoNodeId": atmTraceInfoNodeId,
       "atmTraceInfoOutgoingPortId": atmTraceInfoOutgoingPortId,
       "atmTraceInfoIncomingVpi": atmTraceInfoIncomingVpi,
       "atmTraceInfoIncomingVci": atmTraceInfoIncomingVci,
       "atmTraceInfoIncomingCallRef": atmTraceInfoIncomingCallRef,
       "atmTraceInfoIncomingEndPtRef": atmTraceInfoIncomingEndPtRef,
       "atmTraceInfoRefusalIndicator": atmTraceInfoRefusalIndicator,
       "atmTraceInfoCrankBackRcvdAtDest": atmTraceInfoCrankBackRcvdAtDest,
       "atmTraceInfoCrankBackGap": atmTraceInfoCrankBackGap,
       "atmTraceInfoCrankBackIndicator": atmTraceInfoCrankBackIndicator,
       "atmTraceInfoCrankBackBlockedTransitType": atmTraceInfoCrankBackBlockedTransitType,
       "atmTraceInfoCrankBackBlockedTransitInfo": atmTraceInfoCrankBackBlockedTransitInfo,
       "atmTraceInfoCrankBackCause": atmTraceInfoCrankBackCause,
       "atmTraceInfoReceiveLabel": atmTraceInfoReceiveLabel,
       "atmTraceInfoTransmitLabel": atmTraceInfoTransmitLabel,
       "atmTraceInfoNeNscTable": atmTraceInfoNeNscTable,
       "atmTraceInfoNeNscEntry": atmTraceInfoNeNscEntry,
       "atmTraceInfoNeNscInterface": atmTraceInfoNeNscInterface,
       "atmTraceInfoNeNscIndex": atmTraceInfoNeNscIndex,
       "atmTraceInfoNeNsc": atmTraceInfoNeNsc,
       "atmTraceInfoRpNscTable": atmTraceInfoRpNscTable,
       "atmTraceInfoRpNscEntry": atmTraceInfoRpNscEntry,
       "atmTraceInfoRpNscInterface": atmTraceInfoRpNscInterface,
       "atmTraceInfoRpNscSequenceIndex": atmTraceInfoRpNscSequenceIndex,
       "atmTraceInfoRpNsc": atmTraceInfoRpNsc,
       "atmTraceIfGroup": atmTraceIfGroup,
       "atmTraceIfTable": atmTraceIfTable,
       "atmTraceIfEntry": atmTraceIfEntry,
       "atmTraceIfTraceBoundary": atmTraceIfTraceBoundary,
       "atmTraceMIBTrapsPrefix": atmTraceMIBTrapsPrefix,
       "atmTraceMIBTraps": atmTraceMIBTraps,
       "atmTraceConnCompletion": atmTraceConnCompletion,
       "atmTracePathTestCompletion": atmTracePathTestCompletion,
       "atmTracePathFilterTrap": atmTracePathFilterTrap,
       "atmTraceMIBConformance": atmTraceMIBConformance,
       "atmTraceMIBCompliances": atmTraceMIBCompliances,
       "atmTraceMIBCompliance": atmTraceMIBCompliance,
       "atmTraceMIBCompliance2": atmTraceMIBCompliance2,
       "atmTraceMIBGroups": atmTraceMIBGroups,
       "atmTraceMIBMandatoryGroup": atmTraceMIBMandatoryGroup,
       "atmTraceMIBOptionalGroup": atmTraceMIBOptionalGroup,
       "atmTraceConnAndPathFilterMandatoryGroup": atmTraceConnAndPathFilterMandatoryGroup,
       "atmTracePathMandatoryGroup": atmTracePathMandatoryGroup,
       "atmTraceConnMandatoryGroup": atmTraceConnMandatoryGroup,
       "atmTraceConnOptionalGroup": atmTraceConnOptionalGroup,
       "atmTracePathTestMandatoryGroup": atmTracePathTestMandatoryGroup,
       "atmTracePathTestOptionalGroup": atmTracePathTestOptionalGroup,
       "atmTracePathFilterMandatoryGroup": atmTracePathFilterMandatoryGroup,
       "atmTracePathFilterOptionalGroup": atmTracePathFilterOptionalGroup,
       "atmTraceIfOptionalGroup": atmTraceIfOptionalGroup,
       "atmTraceNotificationOptionalGroup": atmTraceNotificationOptionalGroup,
       "atmTraceConnAndPathFilterPolicyMandatoryGroup": atmTraceConnAndPathFilterPolicyMandatoryGroup,
       "atmTraceConnPolicyMandatoryGroup": atmTraceConnPolicyMandatoryGroup,
       "atmTracePathTestPolicyMandatoryGroup": atmTracePathTestPolicyMandatoryGroup,
       "atmTracePathFilterPolicyMandatoryGroup": atmTracePathFilterPolicyMandatoryGroup,
       "atmTraceConnAndPathFilterMplsMandatoryGroup": atmTraceConnAndPathFilterMplsMandatoryGroup,
       "atmTraceConnMplsMandatoryGroup": atmTraceConnMplsMandatoryGroup,
       "atmTracePathTestMplsMandatoryGroup": atmTracePathTestMplsMandatoryGroup,
       "atmTracePathFilterMplsMandatoryGroup": atmTracePathFilterMplsMandatoryGroup}
)
