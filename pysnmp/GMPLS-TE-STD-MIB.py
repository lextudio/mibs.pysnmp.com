# SNMP MIB module (GMPLS-TE-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GMPLS-TE-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:46 2024
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

(IANAGmplsAdminStatusInformationTC,
 IANAGmplsGeneralizedPidTC,
 IANAGmplsLSPEncodingTypeTC,
 IANAGmplsSwitchingTypeTC) = mibBuilder.importSymbols(
    "IANA-GMPLS-TC-MIB",
    "IANAGmplsAdminStatusInformationTC",
    "IANAGmplsGeneralizedPidTC",
    "IANAGmplsLSPEncodingTypeTC",
    "IANAGmplsSwitchingTypeTC")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

(mplsTunnelARHopIndex,
 mplsTunnelARHopListIndex,
 mplsTunnelAdminStatus,
 mplsTunnelCHopIndex,
 mplsTunnelCHopListIndex,
 mplsTunnelEgressLSRId,
 mplsTunnelEntry,
 mplsTunnelGroup,
 mplsTunnelHopIndex,
 mplsTunnelHopListIndex,
 mplsTunnelHopPathOptionIndex,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance,
 mplsTunnelOperStatus,
 mplsTunnelScalarGroup) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelARHopIndex",
    "mplsTunnelARHopListIndex",
    "mplsTunnelAdminStatus",
    "mplsTunnelCHopIndex",
    "mplsTunnelCHopListIndex",
    "mplsTunnelEgressLSRId",
    "mplsTunnelEntry",
    "mplsTunnelGroup",
    "mplsTunnelHopIndex",
    "mplsTunnelHopListIndex",
    "mplsTunnelHopPathOptionIndex",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance",
    "mplsTunnelOperStatus",
    "mplsTunnelScalarGroup")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "zeroDotZero")

(DisplayString,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

gmplsTeStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 13)
)
gmplsTeStdMIB.setRevisions(
        ("2007-02-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GmplsTeNotifications_ObjectIdentity = ObjectIdentity
gmplsTeNotifications = _GmplsTeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 0)
)
_GmplsTeScalars_ObjectIdentity = ObjectIdentity
gmplsTeScalars = _GmplsTeScalars_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 1)
)
_GmplsTunnelsConfigured_Type = Gauge32
_GmplsTunnelsConfigured_Object = MibScalar
gmplsTunnelsConfigured = _GmplsTunnelsConfigured_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 1, 1),
    _GmplsTunnelsConfigured_Type()
)
gmplsTunnelsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelsConfigured.setStatus("current")
_GmplsTunnelsActive_Type = Gauge32
_GmplsTunnelsActive_Object = MibScalar
gmplsTunnelsActive = _GmplsTunnelsActive_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 1, 2),
    _GmplsTunnelsActive_Type()
)
gmplsTunnelsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelsActive.setStatus("current")
_GmplsTeObjects_ObjectIdentity = ObjectIdentity
gmplsTeObjects = _GmplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2)
)
_GmplsTunnelTable_Object = MibTable
gmplsTunnelTable = _GmplsTunnelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1)
)
if mibBuilder.loadTexts:
    gmplsTunnelTable.setStatus("current")
_GmplsTunnelEntry_Object = MibTableRow
gmplsTunnelEntry = _GmplsTunnelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1)
)
gmplsTunnelEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    gmplsTunnelEntry.setStatus("current")


class _GmplsTunnelUnnumIf_Type(TruthValue):
    """Custom type gmplsTunnelUnnumIf based on TruthValue"""


_GmplsTunnelUnnumIf_Object = MibTableColumn
gmplsTunnelUnnumIf = _GmplsTunnelUnnumIf_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 1),
    _GmplsTunnelUnnumIf_Type()
)
gmplsTunnelUnnumIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelUnnumIf.setStatus("current")


class _GmplsTunnelAttributes_Type(Bits):
    """Custom type gmplsTunnelAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("labelRecordingDesired", 0)
    )

_GmplsTunnelAttributes_Type.__name__ = "Bits"
_GmplsTunnelAttributes_Object = MibTableColumn
gmplsTunnelAttributes = _GmplsTunnelAttributes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 2),
    _GmplsTunnelAttributes_Type()
)
gmplsTunnelAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelAttributes.setStatus("current")


class _GmplsTunnelLSPEncoding_Type(IANAGmplsLSPEncodingTypeTC):
    """Custom type gmplsTunnelLSPEncoding based on IANAGmplsLSPEncodingTypeTC"""


_GmplsTunnelLSPEncoding_Object = MibTableColumn
gmplsTunnelLSPEncoding = _GmplsTunnelLSPEncoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 3),
    _GmplsTunnelLSPEncoding_Type()
)
gmplsTunnelLSPEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelLSPEncoding.setStatus("current")


class _GmplsTunnelSwitchingType_Type(IANAGmplsSwitchingTypeTC):
    """Custom type gmplsTunnelSwitchingType based on IANAGmplsSwitchingTypeTC"""


_GmplsTunnelSwitchingType_Object = MibTableColumn
gmplsTunnelSwitchingType = _GmplsTunnelSwitchingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 4),
    _GmplsTunnelSwitchingType_Type()
)
gmplsTunnelSwitchingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelSwitchingType.setStatus("current")


class _GmplsTunnelLinkProtection_Type(Bits):
    """Custom type gmplsTunnelLinkProtection based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("dedicatedOnePlusOne", 4),
          ("dedicatedOneToOne", 3),
          ("enhanced", 5),
          ("extraTraffic", 0),
          ("shared", 2),
          ("unprotected", 1))
    )

_GmplsTunnelLinkProtection_Type.__name__ = "Bits"
_GmplsTunnelLinkProtection_Object = MibTableColumn
gmplsTunnelLinkProtection = _GmplsTunnelLinkProtection_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 5),
    _GmplsTunnelLinkProtection_Type()
)
gmplsTunnelLinkProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelLinkProtection.setStatus("current")


class _GmplsTunnelGPid_Type(IANAGmplsGeneralizedPidTC):
    """Custom type gmplsTunnelGPid based on IANAGmplsGeneralizedPidTC"""


_GmplsTunnelGPid_Object = MibTableColumn
gmplsTunnelGPid = _GmplsTunnelGPid_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 6),
    _GmplsTunnelGPid_Type()
)
gmplsTunnelGPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelGPid.setStatus("current")


class _GmplsTunnelSecondary_Type(TruthValue):
    """Custom type gmplsTunnelSecondary based on TruthValue"""


_GmplsTunnelSecondary_Object = MibTableColumn
gmplsTunnelSecondary = _GmplsTunnelSecondary_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 7),
    _GmplsTunnelSecondary_Type()
)
gmplsTunnelSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelSecondary.setStatus("current")


class _GmplsTunnelDirection_Type(Integer32):
    """Custom type gmplsTunnelDirection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("forward", 0))
    )


_GmplsTunnelDirection_Type.__name__ = "Integer32"
_GmplsTunnelDirection_Object = MibTableColumn
gmplsTunnelDirection = _GmplsTunnelDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 8),
    _GmplsTunnelDirection_Type()
)
gmplsTunnelDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelDirection.setStatus("current")


class _GmplsTunnelPathComp_Type(Integer32):
    """Custom type gmplsTunnelPathComp based on Integer32"""
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
        *(("dynamicFull", 1),
          ("dynamicPartial", 3),
          ("explicit", 2))
    )


_GmplsTunnelPathComp_Type.__name__ = "Integer32"
_GmplsTunnelPathComp_Object = MibTableColumn
gmplsTunnelPathComp = _GmplsTunnelPathComp_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 9),
    _GmplsTunnelPathComp_Type()
)
gmplsTunnelPathComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelPathComp.setStatus("current")


class _GmplsTunnelUpstreamNotifyRecipientType_Type(InetAddressType):
    """Custom type gmplsTunnelUpstreamNotifyRecipientType based on InetAddressType"""


_GmplsTunnelUpstreamNotifyRecipientType_Object = MibTableColumn
gmplsTunnelUpstreamNotifyRecipientType = _GmplsTunnelUpstreamNotifyRecipientType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 10),
    _GmplsTunnelUpstreamNotifyRecipientType_Type()
)
gmplsTunnelUpstreamNotifyRecipientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelUpstreamNotifyRecipientType.setStatus("current")


class _GmplsTunnelUpstreamNotifyRecipient_Type(InetAddress):
    """Custom type gmplsTunnelUpstreamNotifyRecipient based on InetAddress"""
    defaultHexValue = "00000000"


_GmplsTunnelUpstreamNotifyRecipient_Object = MibTableColumn
gmplsTunnelUpstreamNotifyRecipient = _GmplsTunnelUpstreamNotifyRecipient_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 11),
    _GmplsTunnelUpstreamNotifyRecipient_Type()
)
gmplsTunnelUpstreamNotifyRecipient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelUpstreamNotifyRecipient.setStatus("current")


class _GmplsTunnelSendResvNotifyRecipientType_Type(InetAddressType):
    """Custom type gmplsTunnelSendResvNotifyRecipientType based on InetAddressType"""


_GmplsTunnelSendResvNotifyRecipientType_Object = MibTableColumn
gmplsTunnelSendResvNotifyRecipientType = _GmplsTunnelSendResvNotifyRecipientType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 12),
    _GmplsTunnelSendResvNotifyRecipientType_Type()
)
gmplsTunnelSendResvNotifyRecipientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelSendResvNotifyRecipientType.setStatus("current")


class _GmplsTunnelSendResvNotifyRecipient_Type(InetAddress):
    """Custom type gmplsTunnelSendResvNotifyRecipient based on InetAddress"""
    defaultHexValue = "00000000"


_GmplsTunnelSendResvNotifyRecipient_Object = MibTableColumn
gmplsTunnelSendResvNotifyRecipient = _GmplsTunnelSendResvNotifyRecipient_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 13),
    _GmplsTunnelSendResvNotifyRecipient_Type()
)
gmplsTunnelSendResvNotifyRecipient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelSendResvNotifyRecipient.setStatus("current")


class _GmplsTunnelDownstreamNotifyRecipientType_Type(InetAddressType):
    """Custom type gmplsTunnelDownstreamNotifyRecipientType based on InetAddressType"""


_GmplsTunnelDownstreamNotifyRecipientType_Object = MibTableColumn
gmplsTunnelDownstreamNotifyRecipientType = _GmplsTunnelDownstreamNotifyRecipientType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 14),
    _GmplsTunnelDownstreamNotifyRecipientType_Type()
)
gmplsTunnelDownstreamNotifyRecipientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelDownstreamNotifyRecipientType.setStatus("current")


class _GmplsTunnelDownstreamNotifyRecipient_Type(InetAddress):
    """Custom type gmplsTunnelDownstreamNotifyRecipient based on InetAddress"""
    defaultHexValue = "00000000"


_GmplsTunnelDownstreamNotifyRecipient_Object = MibTableColumn
gmplsTunnelDownstreamNotifyRecipient = _GmplsTunnelDownstreamNotifyRecipient_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 15),
    _GmplsTunnelDownstreamNotifyRecipient_Type()
)
gmplsTunnelDownstreamNotifyRecipient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelDownstreamNotifyRecipient.setStatus("current")


class _GmplsTunnelSendPathNotifyRecipientType_Type(InetAddressType):
    """Custom type gmplsTunnelSendPathNotifyRecipientType based on InetAddressType"""


_GmplsTunnelSendPathNotifyRecipientType_Object = MibTableColumn
gmplsTunnelSendPathNotifyRecipientType = _GmplsTunnelSendPathNotifyRecipientType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 16),
    _GmplsTunnelSendPathNotifyRecipientType_Type()
)
gmplsTunnelSendPathNotifyRecipientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelSendPathNotifyRecipientType.setStatus("current")


class _GmplsTunnelSendPathNotifyRecipient_Type(InetAddress):
    """Custom type gmplsTunnelSendPathNotifyRecipient based on InetAddress"""
    defaultHexValue = "00000000"


_GmplsTunnelSendPathNotifyRecipient_Object = MibTableColumn
gmplsTunnelSendPathNotifyRecipient = _GmplsTunnelSendPathNotifyRecipient_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 17),
    _GmplsTunnelSendPathNotifyRecipient_Type()
)
gmplsTunnelSendPathNotifyRecipient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelSendPathNotifyRecipient.setStatus("current")


class _GmplsTunnelAdminStatusFlags_Type(IANAGmplsAdminStatusInformationTC):
    """Custom type gmplsTunnelAdminStatusFlags based on IANAGmplsAdminStatusInformationTC"""
    defaultBinValue = "0"


_GmplsTunnelAdminStatusFlags_Object = MibTableColumn
gmplsTunnelAdminStatusFlags = _GmplsTunnelAdminStatusFlags_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 18),
    _GmplsTunnelAdminStatusFlags_Type()
)
gmplsTunnelAdminStatusFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelAdminStatusFlags.setStatus("current")


class _GmplsTunnelExtraParamsPtr_Type(RowPointer):
    """Custom type gmplsTunnelExtraParamsPtr based on RowPointer"""
    defaultValue = (0, 0)


_GmplsTunnelExtraParamsPtr_Object = MibTableColumn
gmplsTunnelExtraParamsPtr = _GmplsTunnelExtraParamsPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 19),
    _GmplsTunnelExtraParamsPtr_Type()
)
gmplsTunnelExtraParamsPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelExtraParamsPtr.setStatus("current")
_GmplsTunnelHopTable_Object = MibTable
gmplsTunnelHopTable = _GmplsTunnelHopTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2)
)
if mibBuilder.loadTexts:
    gmplsTunnelHopTable.setStatus("current")
_GmplsTunnelHopEntry_Object = MibTableRow
gmplsTunnelHopEntry = _GmplsTunnelHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1)
)
gmplsTunnelHopEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelHopListIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelHopPathOptionIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelHopIndex"),
)
if mibBuilder.loadTexts:
    gmplsTunnelHopEntry.setStatus("current")


class _GmplsTunnelHopLabelStatuses_Type(Bits):
    """Custom type gmplsTunnelHopLabelStatuses based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("forwardPresent", 0),
          ("reversePresent", 1))
    )

_GmplsTunnelHopLabelStatuses_Type.__name__ = "Bits"
_GmplsTunnelHopLabelStatuses_Object = MibTableColumn
gmplsTunnelHopLabelStatuses = _GmplsTunnelHopLabelStatuses_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 1),
    _GmplsTunnelHopLabelStatuses_Type()
)
gmplsTunnelHopLabelStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelHopLabelStatuses.setStatus("current")
_GmplsTunnelHopExplicitForwardLabel_Type = Unsigned32
_GmplsTunnelHopExplicitForwardLabel_Object = MibTableColumn
gmplsTunnelHopExplicitForwardLabel = _GmplsTunnelHopExplicitForwardLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 2),
    _GmplsTunnelHopExplicitForwardLabel_Type()
)
gmplsTunnelHopExplicitForwardLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelHopExplicitForwardLabel.setStatus("current")


class _GmplsTunnelHopExplicitForwardLabelPtr_Type(RowPointer):
    """Custom type gmplsTunnelHopExplicitForwardLabelPtr based on RowPointer"""
    defaultValue = (0, 0)


_GmplsTunnelHopExplicitForwardLabelPtr_Object = MibTableColumn
gmplsTunnelHopExplicitForwardLabelPtr = _GmplsTunnelHopExplicitForwardLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 3),
    _GmplsTunnelHopExplicitForwardLabelPtr_Type()
)
gmplsTunnelHopExplicitForwardLabelPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelHopExplicitForwardLabelPtr.setStatus("current")
_GmplsTunnelHopExplicitReverseLabel_Type = Unsigned32
_GmplsTunnelHopExplicitReverseLabel_Object = MibTableColumn
gmplsTunnelHopExplicitReverseLabel = _GmplsTunnelHopExplicitReverseLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 4),
    _GmplsTunnelHopExplicitReverseLabel_Type()
)
gmplsTunnelHopExplicitReverseLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelHopExplicitReverseLabel.setStatus("current")


class _GmplsTunnelHopExplicitReverseLabelPtr_Type(RowPointer):
    """Custom type gmplsTunnelHopExplicitReverseLabelPtr based on RowPointer"""
    defaultValue = (0, 0)


_GmplsTunnelHopExplicitReverseLabelPtr_Object = MibTableColumn
gmplsTunnelHopExplicitReverseLabelPtr = _GmplsTunnelHopExplicitReverseLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 5),
    _GmplsTunnelHopExplicitReverseLabelPtr_Type()
)
gmplsTunnelHopExplicitReverseLabelPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTunnelHopExplicitReverseLabelPtr.setStatus("current")
_GmplsTunnelARHopTable_Object = MibTable
gmplsTunnelARHopTable = _GmplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3)
)
if mibBuilder.loadTexts:
    gmplsTunnelARHopTable.setStatus("current")
_GmplsTunnelARHopEntry_Object = MibTableRow
gmplsTunnelARHopEntry = _GmplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1)
)
gmplsTunnelARHopEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopListIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    gmplsTunnelARHopEntry.setStatus("current")


class _GmplsTunnelARHopLabelStatuses_Type(Bits):
    """Custom type gmplsTunnelARHopLabelStatuses based on Bits"""
    namedValues = NamedValues(
        *(("forwardGlobal", 2),
          ("forwardPresent", 0),
          ("reverseGlobal", 3),
          ("reversePresent", 1))
    )

_GmplsTunnelARHopLabelStatuses_Type.__name__ = "Bits"
_GmplsTunnelARHopLabelStatuses_Object = MibTableColumn
gmplsTunnelARHopLabelStatuses = _GmplsTunnelARHopLabelStatuses_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 1),
    _GmplsTunnelARHopLabelStatuses_Type()
)
gmplsTunnelARHopLabelStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelARHopLabelStatuses.setStatus("current")
_GmplsTunnelARHopExplicitForwardLabel_Type = Unsigned32
_GmplsTunnelARHopExplicitForwardLabel_Object = MibTableColumn
gmplsTunnelARHopExplicitForwardLabel = _GmplsTunnelARHopExplicitForwardLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 2),
    _GmplsTunnelARHopExplicitForwardLabel_Type()
)
gmplsTunnelARHopExplicitForwardLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelARHopExplicitForwardLabel.setStatus("current")
_GmplsTunnelARHopExplicitForwardLabelPtr_Type = RowPointer
_GmplsTunnelARHopExplicitForwardLabelPtr_Object = MibTableColumn
gmplsTunnelARHopExplicitForwardLabelPtr = _GmplsTunnelARHopExplicitForwardLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 3),
    _GmplsTunnelARHopExplicitForwardLabelPtr_Type()
)
gmplsTunnelARHopExplicitForwardLabelPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelARHopExplicitForwardLabelPtr.setStatus("current")
_GmplsTunnelARHopExplicitReverseLabel_Type = Unsigned32
_GmplsTunnelARHopExplicitReverseLabel_Object = MibTableColumn
gmplsTunnelARHopExplicitReverseLabel = _GmplsTunnelARHopExplicitReverseLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 4),
    _GmplsTunnelARHopExplicitReverseLabel_Type()
)
gmplsTunnelARHopExplicitReverseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelARHopExplicitReverseLabel.setStatus("current")
_GmplsTunnelARHopExplicitReverseLabelPtr_Type = RowPointer
_GmplsTunnelARHopExplicitReverseLabelPtr_Object = MibTableColumn
gmplsTunnelARHopExplicitReverseLabelPtr = _GmplsTunnelARHopExplicitReverseLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 5),
    _GmplsTunnelARHopExplicitReverseLabelPtr_Type()
)
gmplsTunnelARHopExplicitReverseLabelPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelARHopExplicitReverseLabelPtr.setStatus("current")


class _GmplsTunnelARHopProtection_Type(Bits):
    """Custom type gmplsTunnelARHopProtection based on Bits"""
    namedValues = NamedValues(
        *(("localAvailable", 0),
          ("localInUse", 1))
    )

_GmplsTunnelARHopProtection_Type.__name__ = "Bits"
_GmplsTunnelARHopProtection_Object = MibTableColumn
gmplsTunnelARHopProtection = _GmplsTunnelARHopProtection_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 6),
    _GmplsTunnelARHopProtection_Type()
)
gmplsTunnelARHopProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelARHopProtection.setStatus("current")
_GmplsTunnelCHopTable_Object = MibTable
gmplsTunnelCHopTable = _GmplsTunnelCHopTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4)
)
if mibBuilder.loadTexts:
    gmplsTunnelCHopTable.setStatus("current")
_GmplsTunnelCHopEntry_Object = MibTableRow
gmplsTunnelCHopEntry = _GmplsTunnelCHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1)
)
gmplsTunnelCHopEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelCHopListIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelCHopIndex"),
)
if mibBuilder.loadTexts:
    gmplsTunnelCHopEntry.setStatus("current")


class _GmplsTunnelCHopLabelStatuses_Type(Bits):
    """Custom type gmplsTunnelCHopLabelStatuses based on Bits"""
    namedValues = NamedValues(
        *(("forwardPresent", 0),
          ("reversePresent", 1))
    )

_GmplsTunnelCHopLabelStatuses_Type.__name__ = "Bits"
_GmplsTunnelCHopLabelStatuses_Object = MibTableColumn
gmplsTunnelCHopLabelStatuses = _GmplsTunnelCHopLabelStatuses_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 1),
    _GmplsTunnelCHopLabelStatuses_Type()
)
gmplsTunnelCHopLabelStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelCHopLabelStatuses.setStatus("current")
_GmplsTunnelCHopExplicitForwardLabel_Type = Unsigned32
_GmplsTunnelCHopExplicitForwardLabel_Object = MibTableColumn
gmplsTunnelCHopExplicitForwardLabel = _GmplsTunnelCHopExplicitForwardLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 2),
    _GmplsTunnelCHopExplicitForwardLabel_Type()
)
gmplsTunnelCHopExplicitForwardLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelCHopExplicitForwardLabel.setStatus("current")
_GmplsTunnelCHopExplicitForwardLabelPtr_Type = RowPointer
_GmplsTunnelCHopExplicitForwardLabelPtr_Object = MibTableColumn
gmplsTunnelCHopExplicitForwardLabelPtr = _GmplsTunnelCHopExplicitForwardLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 3),
    _GmplsTunnelCHopExplicitForwardLabelPtr_Type()
)
gmplsTunnelCHopExplicitForwardLabelPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelCHopExplicitForwardLabelPtr.setStatus("current")
_GmplsTunnelCHopExplicitReverseLabel_Type = Unsigned32
_GmplsTunnelCHopExplicitReverseLabel_Object = MibTableColumn
gmplsTunnelCHopExplicitReverseLabel = _GmplsTunnelCHopExplicitReverseLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 4),
    _GmplsTunnelCHopExplicitReverseLabel_Type()
)
gmplsTunnelCHopExplicitReverseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelCHopExplicitReverseLabel.setStatus("current")
_GmplsTunnelCHopExplicitReverseLabelPtr_Type = RowPointer
_GmplsTunnelCHopExplicitReverseLabelPtr_Object = MibTableColumn
gmplsTunnelCHopExplicitReverseLabelPtr = _GmplsTunnelCHopExplicitReverseLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 5),
    _GmplsTunnelCHopExplicitReverseLabelPtr_Type()
)
gmplsTunnelCHopExplicitReverseLabelPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelCHopExplicitReverseLabelPtr.setStatus("current")
_GmplsTunnelReversePerfTable_Object = MibTable
gmplsTunnelReversePerfTable = _GmplsTunnelReversePerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5)
)
if mibBuilder.loadTexts:
    gmplsTunnelReversePerfTable.setStatus("current")
_GmplsTunnelReversePerfEntry_Object = MibTableRow
gmplsTunnelReversePerfEntry = _GmplsTunnelReversePerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1)
)
if mibBuilder.loadTexts:
    gmplsTunnelReversePerfEntry.setStatus("current")
_GmplsTunnelReversePerfPackets_Type = Counter32
_GmplsTunnelReversePerfPackets_Object = MibTableColumn
gmplsTunnelReversePerfPackets = _GmplsTunnelReversePerfPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 1),
    _GmplsTunnelReversePerfPackets_Type()
)
gmplsTunnelReversePerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelReversePerfPackets.setStatus("current")
_GmplsTunnelReversePerfHCPackets_Type = Counter64
_GmplsTunnelReversePerfHCPackets_Object = MibTableColumn
gmplsTunnelReversePerfHCPackets = _GmplsTunnelReversePerfHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 2),
    _GmplsTunnelReversePerfHCPackets_Type()
)
gmplsTunnelReversePerfHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelReversePerfHCPackets.setStatus("current")
_GmplsTunnelReversePerfErrors_Type = Counter32
_GmplsTunnelReversePerfErrors_Object = MibTableColumn
gmplsTunnelReversePerfErrors = _GmplsTunnelReversePerfErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 3),
    _GmplsTunnelReversePerfErrors_Type()
)
gmplsTunnelReversePerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelReversePerfErrors.setStatus("current")
_GmplsTunnelReversePerfBytes_Type = Counter32
_GmplsTunnelReversePerfBytes_Object = MibTableColumn
gmplsTunnelReversePerfBytes = _GmplsTunnelReversePerfBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 4),
    _GmplsTunnelReversePerfBytes_Type()
)
gmplsTunnelReversePerfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelReversePerfBytes.setStatus("current")
_GmplsTunnelReversePerfHCBytes_Type = Counter64
_GmplsTunnelReversePerfHCBytes_Object = MibTableColumn
gmplsTunnelReversePerfHCBytes = _GmplsTunnelReversePerfHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 5),
    _GmplsTunnelReversePerfHCBytes_Type()
)
gmplsTunnelReversePerfHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelReversePerfHCBytes.setStatus("current")
_GmplsTunnelErrorTable_Object = MibTable
gmplsTunnelErrorTable = _GmplsTunnelErrorTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6)
)
if mibBuilder.loadTexts:
    gmplsTunnelErrorTable.setStatus("current")
_GmplsTunnelErrorEntry_Object = MibTableRow
gmplsTunnelErrorEntry = _GmplsTunnelErrorEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1)
)
if mibBuilder.loadTexts:
    gmplsTunnelErrorEntry.setStatus("current")


class _GmplsTunnelErrorLastErrorType_Type(Integer32):
    """Custom type gmplsTunnelErrorLastErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("localConfiguration", 4),
          ("localOther", 6),
          ("localResources", 5),
          ("noError", 0),
          ("pathComputation", 3),
          ("protocol", 2),
          ("unknown", 1))
    )


_GmplsTunnelErrorLastErrorType_Type.__name__ = "Integer32"
_GmplsTunnelErrorLastErrorType_Object = MibTableColumn
gmplsTunnelErrorLastErrorType = _GmplsTunnelErrorLastErrorType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 1),
    _GmplsTunnelErrorLastErrorType_Type()
)
gmplsTunnelErrorLastErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorLastErrorType.setStatus("current")
_GmplsTunnelErrorLastTime_Type = TimeStamp
_GmplsTunnelErrorLastTime_Object = MibTableColumn
gmplsTunnelErrorLastTime = _GmplsTunnelErrorLastTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 2),
    _GmplsTunnelErrorLastTime_Type()
)
gmplsTunnelErrorLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorLastTime.setStatus("current")
_GmplsTunnelErrorReporterType_Type = InetAddressType
_GmplsTunnelErrorReporterType_Object = MibTableColumn
gmplsTunnelErrorReporterType = _GmplsTunnelErrorReporterType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 3),
    _GmplsTunnelErrorReporterType_Type()
)
gmplsTunnelErrorReporterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorReporterType.setStatus("current")
_GmplsTunnelErrorReporter_Type = InetAddress
_GmplsTunnelErrorReporter_Object = MibTableColumn
gmplsTunnelErrorReporter = _GmplsTunnelErrorReporter_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 4),
    _GmplsTunnelErrorReporter_Type()
)
gmplsTunnelErrorReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorReporter.setStatus("current")
_GmplsTunnelErrorCode_Type = Unsigned32
_GmplsTunnelErrorCode_Object = MibTableColumn
gmplsTunnelErrorCode = _GmplsTunnelErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 5),
    _GmplsTunnelErrorCode_Type()
)
gmplsTunnelErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorCode.setStatus("current")
_GmplsTunnelErrorSubcode_Type = Unsigned32
_GmplsTunnelErrorSubcode_Object = MibTableColumn
gmplsTunnelErrorSubcode = _GmplsTunnelErrorSubcode_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 6),
    _GmplsTunnelErrorSubcode_Type()
)
gmplsTunnelErrorSubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorSubcode.setStatus("current")


class _GmplsTunnelErrorTLVs_Type(OctetString):
    """Custom type gmplsTunnelErrorTLVs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_GmplsTunnelErrorTLVs_Type.__name__ = "OctetString"
_GmplsTunnelErrorTLVs_Object = MibTableColumn
gmplsTunnelErrorTLVs = _GmplsTunnelErrorTLVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 7),
    _GmplsTunnelErrorTLVs_Type()
)
gmplsTunnelErrorTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorTLVs.setStatus("current")
_GmplsTunnelErrorHelpString_Type = SnmpAdminString
_GmplsTunnelErrorHelpString_Object = MibTableColumn
gmplsTunnelErrorHelpString = _GmplsTunnelErrorHelpString_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 8),
    _GmplsTunnelErrorHelpString_Type()
)
gmplsTunnelErrorHelpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTunnelErrorHelpString.setStatus("current")
_GmplsTeConformance_ObjectIdentity = ObjectIdentity
gmplsTeConformance = _GmplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3)
)
_GmplsTeGroups_ObjectIdentity = ObjectIdentity
gmplsTeGroups = _GmplsTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1)
)
_GmplsTeCompliances_ObjectIdentity = ObjectIdentity
gmplsTeCompliances = _GmplsTeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 2)
)
gmplsTunnelEntry.registerAugmentions(
    ("GMPLS-TE-STD-MIB",
     "gmplsTunnelReversePerfEntry")
)
gmplsTunnelReversePerfEntry.setIndexNames(*gmplsTunnelEntry.getIndexNames())
mplsTunnelEntry.registerAugmentions(
    ("GMPLS-TE-STD-MIB",
     "gmplsTunnelErrorEntry")
)
gmplsTunnelErrorEntry.setIndexNames(*mplsTunnelEntry.getIndexNames())

# Managed Objects groups

gmplsTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 1)
)
gmplsTunnelGroup.setObjects(
      *(("GMPLS-TE-STD-MIB", "gmplsTunnelDirection"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelReversePerfPackets"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelReversePerfHCPackets"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelReversePerfErrors"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelReversePerfBytes"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelReversePerfHCBytes"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorLastErrorType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorLastTime"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorReporterType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorReporter"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorCode"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorSubcode"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorTLVs"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorHelpString"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelUnnumIf"))
)
if mibBuilder.loadTexts:
    gmplsTunnelGroup.setStatus("current")

gmplsTunnelSignaledGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 2)
)
gmplsTunnelSignaledGroup.setObjects(
      *(("GMPLS-TE-STD-MIB", "gmplsTunnelAttributes"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelLSPEncoding"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelSwitchingType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelLinkProtection"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelGPid"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelSecondary"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelPathComp"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelUpstreamNotifyRecipientType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelUpstreamNotifyRecipient"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelSendResvNotifyRecipientType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelSendResvNotifyRecipient"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelDownstreamNotifyRecipientType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelDownstreamNotifyRecipient"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelSendPathNotifyRecipientType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelSendPathNotifyRecipient"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelAdminStatusFlags"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelHopLabelStatuses"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelHopExplicitForwardLabel"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelHopExplicitForwardLabelPtr"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelHopExplicitReverseLabel"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelHopExplicitReverseLabelPtr"))
)
if mibBuilder.loadTexts:
    gmplsTunnelSignaledGroup.setStatus("current")

gmplsTunnelScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 3)
)
gmplsTunnelScalarGroup.setObjects(
      *(("GMPLS-TE-STD-MIB", "gmplsTunnelsConfigured"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelsActive"))
)
if mibBuilder.loadTexts:
    gmplsTunnelScalarGroup.setStatus("current")

gmplsTunnelOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 4)
)
gmplsTunnelOptionalGroup.setObjects(
      *(("GMPLS-TE-STD-MIB", "gmplsTunnelExtraParamsPtr"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelARHopLabelStatuses"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelARHopExplicitForwardLabel"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelARHopExplicitForwardLabelPtr"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelARHopExplicitReverseLabel"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelARHopExplicitReverseLabelPtr"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelARHopProtection"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelCHopLabelStatuses"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelCHopExplicitForwardLabel"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelCHopExplicitForwardLabelPtr"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelCHopExplicitReverseLabel"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelCHopExplicitReverseLabelPtr"))
)
if mibBuilder.loadTexts:
    gmplsTunnelOptionalGroup.setStatus("current")


# Notification objects

gmplsTunnelDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 0, 1)
)
gmplsTunnelDown.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorLastErrorType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorReporterType"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorReporter"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorCode"),
        ("GMPLS-TE-STD-MIB", "gmplsTunnelErrorSubcode"))
)
if mibBuilder.loadTexts:
    gmplsTunnelDown.setStatus(
        "current"
    )


# Notifications groups

gmplsTeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 5)
)
gmplsTeNotificationGroup.setObjects(
    ("GMPLS-TE-STD-MIB", "gmplsTunnelDown")
)
if mibBuilder.loadTexts:
    gmplsTeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

gmplsTeModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 2, 1)
)
if mibBuilder.loadTexts:
    gmplsTeModuleFullCompliance.setStatus(
        "current"
    )

gmplsTeModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 2, 2)
)
if mibBuilder.loadTexts:
    gmplsTeModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GMPLS-TE-STD-MIB",
    **{"gmplsTeStdMIB": gmplsTeStdMIB,
       "gmplsTeNotifications": gmplsTeNotifications,
       "gmplsTunnelDown": gmplsTunnelDown,
       "gmplsTeScalars": gmplsTeScalars,
       "gmplsTunnelsConfigured": gmplsTunnelsConfigured,
       "gmplsTunnelsActive": gmplsTunnelsActive,
       "gmplsTeObjects": gmplsTeObjects,
       "gmplsTunnelTable": gmplsTunnelTable,
       "gmplsTunnelEntry": gmplsTunnelEntry,
       "gmplsTunnelUnnumIf": gmplsTunnelUnnumIf,
       "gmplsTunnelAttributes": gmplsTunnelAttributes,
       "gmplsTunnelLSPEncoding": gmplsTunnelLSPEncoding,
       "gmplsTunnelSwitchingType": gmplsTunnelSwitchingType,
       "gmplsTunnelLinkProtection": gmplsTunnelLinkProtection,
       "gmplsTunnelGPid": gmplsTunnelGPid,
       "gmplsTunnelSecondary": gmplsTunnelSecondary,
       "gmplsTunnelDirection": gmplsTunnelDirection,
       "gmplsTunnelPathComp": gmplsTunnelPathComp,
       "gmplsTunnelUpstreamNotifyRecipientType": gmplsTunnelUpstreamNotifyRecipientType,
       "gmplsTunnelUpstreamNotifyRecipient": gmplsTunnelUpstreamNotifyRecipient,
       "gmplsTunnelSendResvNotifyRecipientType": gmplsTunnelSendResvNotifyRecipientType,
       "gmplsTunnelSendResvNotifyRecipient": gmplsTunnelSendResvNotifyRecipient,
       "gmplsTunnelDownstreamNotifyRecipientType": gmplsTunnelDownstreamNotifyRecipientType,
       "gmplsTunnelDownstreamNotifyRecipient": gmplsTunnelDownstreamNotifyRecipient,
       "gmplsTunnelSendPathNotifyRecipientType": gmplsTunnelSendPathNotifyRecipientType,
       "gmplsTunnelSendPathNotifyRecipient": gmplsTunnelSendPathNotifyRecipient,
       "gmplsTunnelAdminStatusFlags": gmplsTunnelAdminStatusFlags,
       "gmplsTunnelExtraParamsPtr": gmplsTunnelExtraParamsPtr,
       "gmplsTunnelHopTable": gmplsTunnelHopTable,
       "gmplsTunnelHopEntry": gmplsTunnelHopEntry,
       "gmplsTunnelHopLabelStatuses": gmplsTunnelHopLabelStatuses,
       "gmplsTunnelHopExplicitForwardLabel": gmplsTunnelHopExplicitForwardLabel,
       "gmplsTunnelHopExplicitForwardLabelPtr": gmplsTunnelHopExplicitForwardLabelPtr,
       "gmplsTunnelHopExplicitReverseLabel": gmplsTunnelHopExplicitReverseLabel,
       "gmplsTunnelHopExplicitReverseLabelPtr": gmplsTunnelHopExplicitReverseLabelPtr,
       "gmplsTunnelARHopTable": gmplsTunnelARHopTable,
       "gmplsTunnelARHopEntry": gmplsTunnelARHopEntry,
       "gmplsTunnelARHopLabelStatuses": gmplsTunnelARHopLabelStatuses,
       "gmplsTunnelARHopExplicitForwardLabel": gmplsTunnelARHopExplicitForwardLabel,
       "gmplsTunnelARHopExplicitForwardLabelPtr": gmplsTunnelARHopExplicitForwardLabelPtr,
       "gmplsTunnelARHopExplicitReverseLabel": gmplsTunnelARHopExplicitReverseLabel,
       "gmplsTunnelARHopExplicitReverseLabelPtr": gmplsTunnelARHopExplicitReverseLabelPtr,
       "gmplsTunnelARHopProtection": gmplsTunnelARHopProtection,
       "gmplsTunnelCHopTable": gmplsTunnelCHopTable,
       "gmplsTunnelCHopEntry": gmplsTunnelCHopEntry,
       "gmplsTunnelCHopLabelStatuses": gmplsTunnelCHopLabelStatuses,
       "gmplsTunnelCHopExplicitForwardLabel": gmplsTunnelCHopExplicitForwardLabel,
       "gmplsTunnelCHopExplicitForwardLabelPtr": gmplsTunnelCHopExplicitForwardLabelPtr,
       "gmplsTunnelCHopExplicitReverseLabel": gmplsTunnelCHopExplicitReverseLabel,
       "gmplsTunnelCHopExplicitReverseLabelPtr": gmplsTunnelCHopExplicitReverseLabelPtr,
       "gmplsTunnelReversePerfTable": gmplsTunnelReversePerfTable,
       "gmplsTunnelReversePerfEntry": gmplsTunnelReversePerfEntry,
       "gmplsTunnelReversePerfPackets": gmplsTunnelReversePerfPackets,
       "gmplsTunnelReversePerfHCPackets": gmplsTunnelReversePerfHCPackets,
       "gmplsTunnelReversePerfErrors": gmplsTunnelReversePerfErrors,
       "gmplsTunnelReversePerfBytes": gmplsTunnelReversePerfBytes,
       "gmplsTunnelReversePerfHCBytes": gmplsTunnelReversePerfHCBytes,
       "gmplsTunnelErrorTable": gmplsTunnelErrorTable,
       "gmplsTunnelErrorEntry": gmplsTunnelErrorEntry,
       "gmplsTunnelErrorLastErrorType": gmplsTunnelErrorLastErrorType,
       "gmplsTunnelErrorLastTime": gmplsTunnelErrorLastTime,
       "gmplsTunnelErrorReporterType": gmplsTunnelErrorReporterType,
       "gmplsTunnelErrorReporter": gmplsTunnelErrorReporter,
       "gmplsTunnelErrorCode": gmplsTunnelErrorCode,
       "gmplsTunnelErrorSubcode": gmplsTunnelErrorSubcode,
       "gmplsTunnelErrorTLVs": gmplsTunnelErrorTLVs,
       "gmplsTunnelErrorHelpString": gmplsTunnelErrorHelpString,
       "gmplsTeConformance": gmplsTeConformance,
       "gmplsTeGroups": gmplsTeGroups,
       "gmplsTunnelGroup": gmplsTunnelGroup,
       "gmplsTunnelSignaledGroup": gmplsTunnelSignaledGroup,
       "gmplsTunnelScalarGroup": gmplsTunnelScalarGroup,
       "gmplsTunnelOptionalGroup": gmplsTunnelOptionalGroup,
       "gmplsTeNotificationGroup": gmplsTeNotificationGroup,
       "gmplsTeCompliances": gmplsTeCompliances,
       "gmplsTeModuleFullCompliance": gmplsTeModuleFullCompliance,
       "gmplsTeModuleReadOnlyCompliance": gmplsTeModuleReadOnlyCompliance}
)
