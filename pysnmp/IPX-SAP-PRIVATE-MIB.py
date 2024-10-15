# SNMP MIB module (IPX-SAP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPX-SAP-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:36 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

(cjnIpxIfIndex,) = mibBuilder.importSymbols(
    "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB",
    "cjnIpxIfIndex")

(NetNumber,
 ServiceType) = mibBuilder.importSymbols(
    "IPX-PRIVATE-MIB",
    "NetNumber",
    "ServiceType")

(FilterPrec,) = mibBuilder.importSymbols(
    "IPX-RIP-PRIVATE-MIB",
    "FilterPrec")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnIpxSap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpxSapGlobalGroup_ObjectIdentity = ObjectIdentity
cjnIpxSapGlobalGroup = _CjnIpxSapGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 1)
)


class _CjnIpxSapEnabled_Type(Integer32):
    """Custom type cjnIpxSapEnabled based on Integer32"""
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


_CjnIpxSapEnabled_Type.__name__ = "Integer32"
_CjnIpxSapEnabled_Object = MibScalar
cjnIpxSapEnabled = _CjnIpxSapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 1, 1),
    _CjnIpxSapEnabled_Type()
)
cjnIpxSapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxSapEnabled.setStatus("current")
_CjnIpxSapNameFilterGroup_ObjectIdentity = ObjectIdentity
cjnIpxSapNameFilterGroup = _CjnIpxSapNameFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2)
)
_CjnIpxSapNameFilterTable_Object = MibTable
cjnIpxSapNameFilterTable = _CjnIpxSapNameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1)
)
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterTable.setStatus("current")
_CjnIpxSapNameFilterEntry_Object = MibTableRow
cjnIpxSapNameFilterEntry = _CjnIpxSapNameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1)
)
cjnIpxSapNameFilterEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
    (0, "IPX-SAP-PRIVATE-MIB", "cjnIpxSapNameFilterPrec"),
)
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterEntry.setStatus("current")
_CjnIpxSapNameFilterPrec_Type = FilterPrec
_CjnIpxSapNameFilterPrec_Object = MibTableColumn
cjnIpxSapNameFilterPrec = _CjnIpxSapNameFilterPrec_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 1),
    _CjnIpxSapNameFilterPrec_Type()
)
cjnIpxSapNameFilterPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterPrec.setStatus("current")
_CjnIpxSapNameFilterRowStatus_Type = RowStatus
_CjnIpxSapNameFilterRowStatus_Object = MibTableColumn
cjnIpxSapNameFilterRowStatus = _CjnIpxSapNameFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 2),
    _CjnIpxSapNameFilterRowStatus_Type()
)
cjnIpxSapNameFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterRowStatus.setStatus("current")


class _CjnIpxSapNameFilterName_Type(OctetString):
    """Custom type cjnIpxSapNameFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_CjnIpxSapNameFilterName_Type.__name__ = "OctetString"
_CjnIpxSapNameFilterName_Object = MibTableColumn
cjnIpxSapNameFilterName = _CjnIpxSapNameFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 3),
    _CjnIpxSapNameFilterName_Type()
)
cjnIpxSapNameFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterName.setStatus("current")
_CjnIpxSapNameFilterType_Type = ServiceType
_CjnIpxSapNameFilterType_Object = MibTableColumn
cjnIpxSapNameFilterType = _CjnIpxSapNameFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 4),
    _CjnIpxSapNameFilterType_Type()
)
cjnIpxSapNameFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterType.setStatus("current")


class _CjnIpxSapNameFilterDirection_Type(Integer32):
    """Custom type cjnIpxSapNameFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_CjnIpxSapNameFilterDirection_Type.__name__ = "Integer32"
_CjnIpxSapNameFilterDirection_Object = MibTableColumn
cjnIpxSapNameFilterDirection = _CjnIpxSapNameFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 5),
    _CjnIpxSapNameFilterDirection_Type()
)
cjnIpxSapNameFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterDirection.setStatus("current")


class _CjnIpxSapNameFilterAction_Type(Integer32):
    """Custom type cjnIpxSapNameFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("filter", 1))
    )


_CjnIpxSapNameFilterAction_Type.__name__ = "Integer32"
_CjnIpxSapNameFilterAction_Object = MibTableColumn
cjnIpxSapNameFilterAction = _CjnIpxSapNameFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 6),
    _CjnIpxSapNameFilterAction_Type()
)
cjnIpxSapNameFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterAction.setStatus("current")
_CjnIpxSapNameFilterHops_Type = Integer32
_CjnIpxSapNameFilterHops_Object = MibTableColumn
cjnIpxSapNameFilterHops = _CjnIpxSapNameFilterHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 7),
    _CjnIpxSapNameFilterHops_Type()
)
cjnIpxSapNameFilterHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNameFilterHops.setStatus("current")
_CjnIpxSapNetFilterGroup_ObjectIdentity = ObjectIdentity
cjnIpxSapNetFilterGroup = _CjnIpxSapNetFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3)
)
_CjnIpxSapNetFilterTable_Object = MibTable
cjnIpxSapNetFilterTable = _CjnIpxSapNetFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1)
)
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterTable.setStatus("current")
_CjnIpxSapNetFilterEntry_Object = MibTableRow
cjnIpxSapNetFilterEntry = _CjnIpxSapNetFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1)
)
cjnIpxSapNetFilterEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
    (0, "IPX-SAP-PRIVATE-MIB", "cjnIpxSapNetFilterPrec"),
)
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterEntry.setStatus("current")
_CjnIpxSapNetFilterPrec_Type = FilterPrec
_CjnIpxSapNetFilterPrec_Object = MibTableColumn
cjnIpxSapNetFilterPrec = _CjnIpxSapNetFilterPrec_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 1),
    _CjnIpxSapNetFilterPrec_Type()
)
cjnIpxSapNetFilterPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterPrec.setStatus("current")
_CjnIpxSapNetFilterRowStatus_Type = RowStatus
_CjnIpxSapNetFilterRowStatus_Object = MibTableColumn
cjnIpxSapNetFilterRowStatus = _CjnIpxSapNetFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 2),
    _CjnIpxSapNetFilterRowStatus_Type()
)
cjnIpxSapNetFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterRowStatus.setStatus("current")
_CjnIpxSapNetFilterNet_Type = NetNumber
_CjnIpxSapNetFilterNet_Object = MibTableColumn
cjnIpxSapNetFilterNet = _CjnIpxSapNetFilterNet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 3),
    _CjnIpxSapNetFilterNet_Type()
)
cjnIpxSapNetFilterNet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterNet.setStatus("current")
_CjnIpxSapNetFilterType_Type = ServiceType
_CjnIpxSapNetFilterType_Object = MibTableColumn
cjnIpxSapNetFilterType = _CjnIpxSapNetFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 4),
    _CjnIpxSapNetFilterType_Type()
)
cjnIpxSapNetFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterType.setStatus("current")


class _CjnIpxSapNetFilterDirection_Type(Integer32):
    """Custom type cjnIpxSapNetFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_CjnIpxSapNetFilterDirection_Type.__name__ = "Integer32"
_CjnIpxSapNetFilterDirection_Object = MibTableColumn
cjnIpxSapNetFilterDirection = _CjnIpxSapNetFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 5),
    _CjnIpxSapNetFilterDirection_Type()
)
cjnIpxSapNetFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterDirection.setStatus("current")


class _CjnIpxSapNetFilterAction_Type(Integer32):
    """Custom type cjnIpxSapNetFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("filter", 1))
    )


_CjnIpxSapNetFilterAction_Type.__name__ = "Integer32"
_CjnIpxSapNetFilterAction_Object = MibTableColumn
cjnIpxSapNetFilterAction = _CjnIpxSapNetFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 6),
    _CjnIpxSapNetFilterAction_Type()
)
cjnIpxSapNetFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterAction.setStatus("current")
_CjnIpxSapNetFilterHops_Type = Integer32
_CjnIpxSapNetFilterHops_Object = MibTableColumn
cjnIpxSapNetFilterHops = _CjnIpxSapNetFilterHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 7),
    _CjnIpxSapNetFilterHops_Type()
)
cjnIpxSapNetFilterHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapNetFilterHops.setStatus("current")
_CjnIpxSapIfGroup_ObjectIdentity = ObjectIdentity
cjnIpxSapIfGroup = _CjnIpxSapIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4)
)
_CjnIpxSapIfTable_Object = MibTable
cjnIpxSapIfTable = _CjnIpxSapIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1)
)
if mibBuilder.loadTexts:
    cjnIpxSapIfTable.setStatus("current")
_CjnIpxSapIfEntry_Object = MibTableRow
cjnIpxSapIfEntry = _CjnIpxSapIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1)
)
cjnIpxSapIfEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIpxSapIfEntry.setStatus("current")
_CjnIpxSapIfRowStatus_Type = RowStatus
_CjnIpxSapIfRowStatus_Object = MibTableColumn
cjnIpxSapIfRowStatus = _CjnIpxSapIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 1),
    _CjnIpxSapIfRowStatus_Type()
)
cjnIpxSapIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfRowStatus.setStatus("current")


class _CjnIpxSapIfInterpacketGap_Type(Integer32):
    """Custom type cjnIpxSapIfInterpacketGap based on Integer32"""
    defaultValue = 1

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


_CjnIpxSapIfInterpacketGap_Type.__name__ = "Integer32"
_CjnIpxSapIfInterpacketGap_Object = MibTableColumn
cjnIpxSapIfInterpacketGap = _CjnIpxSapIfInterpacketGap_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 2),
    _CjnIpxSapIfInterpacketGap_Type()
)
cjnIpxSapIfInterpacketGap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfInterpacketGap.setStatus("current")


class _CjnIpxSapIfUseMaximumPacketSize_Type(Integer32):
    """Custom type cjnIpxSapIfUseMaximumPacketSize based on Integer32"""
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


_CjnIpxSapIfUseMaximumPacketSize_Type.__name__ = "Integer32"
_CjnIpxSapIfUseMaximumPacketSize_Object = MibTableColumn
cjnIpxSapIfUseMaximumPacketSize = _CjnIpxSapIfUseMaximumPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 3),
    _CjnIpxSapIfUseMaximumPacketSize_Type()
)
cjnIpxSapIfUseMaximumPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfUseMaximumPacketSize.setStatus("current")


class _CjnIpxSapIfUpdateInterval_Type(Integer32):
    """Custom type cjnIpxSapIfUpdateInterval based on Integer32"""
    defaultValue = 60


_CjnIpxSapIfUpdateInterval_Object = MibTableColumn
cjnIpxSapIfUpdateInterval = _CjnIpxSapIfUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 4),
    _CjnIpxSapIfUpdateInterval_Type()
)
cjnIpxSapIfUpdateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfUpdateInterval.setStatus("current")


class _CjnIpxSapIfAgeMultiplier_Type(Integer32):
    """Custom type cjnIpxSapIfAgeMultiplier based on Integer32"""
    defaultValue = 3


_CjnIpxSapIfAgeMultiplier_Object = MibTableColumn
cjnIpxSapIfAgeMultiplier = _CjnIpxSapIfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 5),
    _CjnIpxSapIfAgeMultiplier_Type()
)
cjnIpxSapIfAgeMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfAgeMultiplier.setStatus("current")


class _CjnIpxSapIfTriggeredUpdates_Type(Integer32):
    """Custom type cjnIpxSapIfTriggeredUpdates based on Integer32"""
    defaultValue = 1

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


_CjnIpxSapIfTriggeredUpdates_Type.__name__ = "Integer32"
_CjnIpxSapIfTriggeredUpdates_Object = MibTableColumn
cjnIpxSapIfTriggeredUpdates = _CjnIpxSapIfTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 6),
    _CjnIpxSapIfTriggeredUpdates_Type()
)
cjnIpxSapIfTriggeredUpdates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfTriggeredUpdates.setStatus("current")


class _CjnIpxSapIfGetNearestServerReply_Type(Integer32):
    """Custom type cjnIpxSapIfGetNearestServerReply based on Integer32"""
    defaultValue = 1

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


_CjnIpxSapIfGetNearestServerReply_Type.__name__ = "Integer32"
_CjnIpxSapIfGetNearestServerReply_Object = MibTableColumn
cjnIpxSapIfGetNearestServerReply = _CjnIpxSapIfGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 7),
    _CjnIpxSapIfGetNearestServerReply_Type()
)
cjnIpxSapIfGetNearestServerReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfGetNearestServerReply.setStatus("current")


class _CjnIpxSapIfGetNearestServerReplyDelay_Type(Integer32):
    """Custom type cjnIpxSapIfGetNearestServerReplyDelay based on Integer32"""
    defaultValue = 0


_CjnIpxSapIfGetNearestServerReplyDelay_Object = MibTableColumn
cjnIpxSapIfGetNearestServerReplyDelay = _CjnIpxSapIfGetNearestServerReplyDelay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 8),
    _CjnIpxSapIfGetNearestServerReplyDelay_Type()
)
cjnIpxSapIfGetNearestServerReplyDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfGetNearestServerReplyDelay.setStatus("current")


class _CjnIpxSapIfMode_Type(Integer32):
    """Custom type cjnIpxSapIfMode based on Integer32"""
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
        *(("both", 3),
          ("listen", 2),
          ("talk", 1))
    )


_CjnIpxSapIfMode_Type.__name__ = "Integer32"
_CjnIpxSapIfMode_Object = MibTableColumn
cjnIpxSapIfMode = _CjnIpxSapIfMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 9),
    _CjnIpxSapIfMode_Type()
)
cjnIpxSapIfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxSapIfMode.setStatus("current")
_CjnIpxSapIfStatGroup_ObjectIdentity = ObjectIdentity
cjnIpxSapIfStatGroup = _CjnIpxSapIfStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5)
)
_CjnIpxSapIfStatTable_Object = MibTable
cjnIpxSapIfStatTable = _CjnIpxSapIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1)
)
if mibBuilder.loadTexts:
    cjnIpxSapIfStatTable.setStatus("current")
_CjnIpxSapIfStatEntry_Object = MibTableRow
cjnIpxSapIfStatEntry = _CjnIpxSapIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1)
)
cjnIpxSapIfStatEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIpxSapIfStatEntry.setStatus("current")
_CjnIpxSapIfStatTriggeredUpdatesSent_Type = Counter32
_CjnIpxSapIfStatTriggeredUpdatesSent_Object = MibTableColumn
cjnIpxSapIfStatTriggeredUpdatesSent = _CjnIpxSapIfStatTriggeredUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 1),
    _CjnIpxSapIfStatTriggeredUpdatesSent_Type()
)
cjnIpxSapIfStatTriggeredUpdatesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatTriggeredUpdatesSent.setStatus("current")
_CjnIpxSapIfStatPeriodicUpdatesSent_Type = Counter32
_CjnIpxSapIfStatPeriodicUpdatesSent_Object = MibTableColumn
cjnIpxSapIfStatPeriodicUpdatesSent = _CjnIpxSapIfStatPeriodicUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 2),
    _CjnIpxSapIfStatPeriodicUpdatesSent_Type()
)
cjnIpxSapIfStatPeriodicUpdatesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatPeriodicUpdatesSent.setStatus("current")
_CjnIpxSapIfStatGNSResponsesSent_Type = Counter32
_CjnIpxSapIfStatGNSResponsesSent_Object = MibTableColumn
cjnIpxSapIfStatGNSResponsesSent = _CjnIpxSapIfStatGNSResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 3),
    _CjnIpxSapIfStatGNSResponsesSent_Type()
)
cjnIpxSapIfStatGNSResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatGNSResponsesSent.setStatus("current")
_CjnIpxSapIfStatUpdatesReceived_Type = Counter32
_CjnIpxSapIfStatUpdatesReceived_Object = MibTableColumn
cjnIpxSapIfStatUpdatesReceived = _CjnIpxSapIfStatUpdatesReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 4),
    _CjnIpxSapIfStatUpdatesReceived_Type()
)
cjnIpxSapIfStatUpdatesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatUpdatesReceived.setStatus("current")
_CjnIpxSapIfStatRequestsReceived_Type = Counter32
_CjnIpxSapIfStatRequestsReceived_Object = MibTableColumn
cjnIpxSapIfStatRequestsReceived = _CjnIpxSapIfStatRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 5),
    _CjnIpxSapIfStatRequestsReceived_Type()
)
cjnIpxSapIfStatRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatRequestsReceived.setStatus("current")
_CjnIpxSapIfStatGNSRequestsReceived_Type = Counter32
_CjnIpxSapIfStatGNSRequestsReceived_Object = MibTableColumn
cjnIpxSapIfStatGNSRequestsReceived = _CjnIpxSapIfStatGNSRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 6),
    _CjnIpxSapIfStatGNSRequestsReceived_Type()
)
cjnIpxSapIfStatGNSRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatGNSRequestsReceived.setStatus("current")
_CjnIpxSapIfStatBadPacketsReceived_Type = Counter32
_CjnIpxSapIfStatBadPacketsReceived_Object = MibTableColumn
cjnIpxSapIfStatBadPacketsReceived = _CjnIpxSapIfStatBadPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 7),
    _CjnIpxSapIfStatBadPacketsReceived_Type()
)
cjnIpxSapIfStatBadPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatBadPacketsReceived.setStatus("current")


class _CjnIpxSapIfStatsReset_Type(Integer32):
    """Custom type cjnIpxSapIfStatsReset based on Integer32"""
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


_CjnIpxSapIfStatsReset_Type.__name__ = "Integer32"
_CjnIpxSapIfStatsReset_Object = MibScalar
cjnIpxSapIfStatsReset = _CjnIpxSapIfStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 8),
    _CjnIpxSapIfStatsReset_Type()
)
cjnIpxSapIfStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxSapIfStatsReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPX-SAP-PRIVATE-MIB",
    **{"cjnIpxSap": cjnIpxSap,
       "cjnIpxSapGlobalGroup": cjnIpxSapGlobalGroup,
       "cjnIpxSapEnabled": cjnIpxSapEnabled,
       "cjnIpxSapNameFilterGroup": cjnIpxSapNameFilterGroup,
       "cjnIpxSapNameFilterTable": cjnIpxSapNameFilterTable,
       "cjnIpxSapNameFilterEntry": cjnIpxSapNameFilterEntry,
       "cjnIpxSapNameFilterPrec": cjnIpxSapNameFilterPrec,
       "cjnIpxSapNameFilterRowStatus": cjnIpxSapNameFilterRowStatus,
       "cjnIpxSapNameFilterName": cjnIpxSapNameFilterName,
       "cjnIpxSapNameFilterType": cjnIpxSapNameFilterType,
       "cjnIpxSapNameFilterDirection": cjnIpxSapNameFilterDirection,
       "cjnIpxSapNameFilterAction": cjnIpxSapNameFilterAction,
       "cjnIpxSapNameFilterHops": cjnIpxSapNameFilterHops,
       "cjnIpxSapNetFilterGroup": cjnIpxSapNetFilterGroup,
       "cjnIpxSapNetFilterTable": cjnIpxSapNetFilterTable,
       "cjnIpxSapNetFilterEntry": cjnIpxSapNetFilterEntry,
       "cjnIpxSapNetFilterPrec": cjnIpxSapNetFilterPrec,
       "cjnIpxSapNetFilterRowStatus": cjnIpxSapNetFilterRowStatus,
       "cjnIpxSapNetFilterNet": cjnIpxSapNetFilterNet,
       "cjnIpxSapNetFilterType": cjnIpxSapNetFilterType,
       "cjnIpxSapNetFilterDirection": cjnIpxSapNetFilterDirection,
       "cjnIpxSapNetFilterAction": cjnIpxSapNetFilterAction,
       "cjnIpxSapNetFilterHops": cjnIpxSapNetFilterHops,
       "cjnIpxSapIfGroup": cjnIpxSapIfGroup,
       "cjnIpxSapIfTable": cjnIpxSapIfTable,
       "cjnIpxSapIfEntry": cjnIpxSapIfEntry,
       "cjnIpxSapIfRowStatus": cjnIpxSapIfRowStatus,
       "cjnIpxSapIfInterpacketGap": cjnIpxSapIfInterpacketGap,
       "cjnIpxSapIfUseMaximumPacketSize": cjnIpxSapIfUseMaximumPacketSize,
       "cjnIpxSapIfUpdateInterval": cjnIpxSapIfUpdateInterval,
       "cjnIpxSapIfAgeMultiplier": cjnIpxSapIfAgeMultiplier,
       "cjnIpxSapIfTriggeredUpdates": cjnIpxSapIfTriggeredUpdates,
       "cjnIpxSapIfGetNearestServerReply": cjnIpxSapIfGetNearestServerReply,
       "cjnIpxSapIfGetNearestServerReplyDelay": cjnIpxSapIfGetNearestServerReplyDelay,
       "cjnIpxSapIfMode": cjnIpxSapIfMode,
       "cjnIpxSapIfStatGroup": cjnIpxSapIfStatGroup,
       "cjnIpxSapIfStatTable": cjnIpxSapIfStatTable,
       "cjnIpxSapIfStatEntry": cjnIpxSapIfStatEntry,
       "cjnIpxSapIfStatTriggeredUpdatesSent": cjnIpxSapIfStatTriggeredUpdatesSent,
       "cjnIpxSapIfStatPeriodicUpdatesSent": cjnIpxSapIfStatPeriodicUpdatesSent,
       "cjnIpxSapIfStatGNSResponsesSent": cjnIpxSapIfStatGNSResponsesSent,
       "cjnIpxSapIfStatUpdatesReceived": cjnIpxSapIfStatUpdatesReceived,
       "cjnIpxSapIfStatRequestsReceived": cjnIpxSapIfStatRequestsReceived,
       "cjnIpxSapIfStatGNSRequestsReceived": cjnIpxSapIfStatGNSRequestsReceived,
       "cjnIpxSapIfStatBadPacketsReceived": cjnIpxSapIfStatBadPacketsReceived,
       "cjnIpxSapIfStatsReset": cjnIpxSapIfStatsReset}
)
