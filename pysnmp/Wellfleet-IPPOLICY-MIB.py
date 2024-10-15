# SNMP MIB module (Wellfleet-IPPOLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IPPOLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:28 2024
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

(wfIpPolicyGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpPolicyGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpRipAcceptTable_Object = MibTable
wfIpRipAcceptTable = _WfIpRipAcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    wfIpRipAcceptTable.setStatus("mandatory")
_WfIpRipAcceptEntry_Object = MibTableRow
wfIpRipAcceptEntry = _WfIpRipAcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1)
)
wfIpRipAcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpRipAcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpRipAcceptEntry.setStatus("mandatory")


class _WfIpRipAcceptDelete_Type(Integer32):
    """Custom type wfIpRipAcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRipAcceptDelete_Type.__name__ = "Integer32"
_WfIpRipAcceptDelete_Object = MibTableColumn
wfIpRipAcceptDelete = _WfIpRipAcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 1),
    _WfIpRipAcceptDelete_Type()
)
wfIpRipAcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptDelete.setStatus("mandatory")


class _WfIpRipAcceptDisable_Type(Integer32):
    """Custom type wfIpRipAcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpRipAcceptDisable_Type.__name__ = "Integer32"
_WfIpRipAcceptDisable_Object = MibTableColumn
wfIpRipAcceptDisable = _WfIpRipAcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 2),
    _WfIpRipAcceptDisable_Type()
)
wfIpRipAcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptDisable.setStatus("mandatory")
_WfIpRipAcceptIndex_Type = Integer32
_WfIpRipAcceptIndex_Object = MibTableColumn
wfIpRipAcceptIndex = _WfIpRipAcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 3),
    _WfIpRipAcceptIndex_Type()
)
wfIpRipAcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRipAcceptIndex.setStatus("mandatory")
_WfIpRipAcceptName_Type = DisplayString
_WfIpRipAcceptName_Object = MibTableColumn
wfIpRipAcceptName = _WfIpRipAcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 4),
    _WfIpRipAcceptName_Type()
)
wfIpRipAcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptName.setStatus("mandatory")
_WfIpRipAcceptNetworks_Type = OctetString
_WfIpRipAcceptNetworks_Object = MibTableColumn
wfIpRipAcceptNetworks = _WfIpRipAcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 5),
    _WfIpRipAcceptNetworks_Type()
)
wfIpRipAcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptNetworks.setStatus("mandatory")


class _WfIpRipAcceptAction_Type(Integer32):
    """Custom type wfIpRipAcceptAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpRipAcceptAction_Type.__name__ = "Integer32"
_WfIpRipAcceptAction_Object = MibTableColumn
wfIpRipAcceptAction = _WfIpRipAcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 6),
    _WfIpRipAcceptAction_Type()
)
wfIpRipAcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptAction.setStatus("mandatory")


class _WfIpRipAcceptPreference_Type(Integer32):
    """Custom type wfIpRipAcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpRipAcceptPreference_Type.__name__ = "Integer32"
_WfIpRipAcceptPreference_Object = MibTableColumn
wfIpRipAcceptPreference = _WfIpRipAcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 7),
    _WfIpRipAcceptPreference_Type()
)
wfIpRipAcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptPreference.setStatus("mandatory")
_WfIpRipAcceptPrecedence_Type = Integer32
_WfIpRipAcceptPrecedence_Object = MibTableColumn
wfIpRipAcceptPrecedence = _WfIpRipAcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 8),
    _WfIpRipAcceptPrecedence_Type()
)
wfIpRipAcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptPrecedence.setStatus("mandatory")
_WfIpRipAcceptInject_Type = OctetString
_WfIpRipAcceptInject_Object = MibTableColumn
wfIpRipAcceptInject = _WfIpRipAcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 9),
    _WfIpRipAcceptInject_Type()
)
wfIpRipAcceptInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRipAcceptInject.setStatus("mandatory")
_WfIpRipAcceptGateway_Type = OctetString
_WfIpRipAcceptGateway_Object = MibTableColumn
wfIpRipAcceptGateway = _WfIpRipAcceptGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 10),
    _WfIpRipAcceptGateway_Type()
)
wfIpRipAcceptGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptGateway.setStatus("mandatory")
_WfIpRipAcceptInterface_Type = OctetString
_WfIpRipAcceptInterface_Object = MibTableColumn
wfIpRipAcceptInterface = _WfIpRipAcceptInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 11),
    _WfIpRipAcceptInterface_Type()
)
wfIpRipAcceptInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptInterface.setStatus("mandatory")
_WfIpRipAcceptApplyMask_Type = IpAddress
_WfIpRipAcceptApplyMask_Object = MibTableColumn
wfIpRipAcceptApplyMask = _WfIpRipAcceptApplyMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 1, 1, 12),
    _WfIpRipAcceptApplyMask_Type()
)
wfIpRipAcceptApplyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAcceptApplyMask.setStatus("mandatory")
_WfIpRipAnnounceTable_Object = MibTable
wfIpRipAnnounceTable = _WfIpRipAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2)
)
if mibBuilder.loadTexts:
    wfIpRipAnnounceTable.setStatus("mandatory")
_WfIpRipAnnounceEntry_Object = MibTableRow
wfIpRipAnnounceEntry = _WfIpRipAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1)
)
wfIpRipAnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpRipAnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpRipAnnounceEntry.setStatus("mandatory")


class _WfIpRipAnnounceDelete_Type(Integer32):
    """Custom type wfIpRipAnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRipAnnounceDelete_Type.__name__ = "Integer32"
_WfIpRipAnnounceDelete_Object = MibTableColumn
wfIpRipAnnounceDelete = _WfIpRipAnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 1),
    _WfIpRipAnnounceDelete_Type()
)
wfIpRipAnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceDelete.setStatus("mandatory")


class _WfIpRipAnnounceDisable_Type(Integer32):
    """Custom type wfIpRipAnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpRipAnnounceDisable_Type.__name__ = "Integer32"
_WfIpRipAnnounceDisable_Object = MibTableColumn
wfIpRipAnnounceDisable = _WfIpRipAnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 2),
    _WfIpRipAnnounceDisable_Type()
)
wfIpRipAnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceDisable.setStatus("mandatory")
_WfIpRipAnnounceIndex_Type = Integer32
_WfIpRipAnnounceIndex_Object = MibTableColumn
wfIpRipAnnounceIndex = _WfIpRipAnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 3),
    _WfIpRipAnnounceIndex_Type()
)
wfIpRipAnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRipAnnounceIndex.setStatus("mandatory")
_WfIpRipAnnounceName_Type = DisplayString
_WfIpRipAnnounceName_Object = MibTableColumn
wfIpRipAnnounceName = _WfIpRipAnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 4),
    _WfIpRipAnnounceName_Type()
)
wfIpRipAnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceName.setStatus("mandatory")
_WfIpRipAnnounceNetworks_Type = OctetString
_WfIpRipAnnounceNetworks_Object = MibTableColumn
wfIpRipAnnounceNetworks = _WfIpRipAnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 5),
    _WfIpRipAnnounceNetworks_Type()
)
wfIpRipAnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceNetworks.setStatus("mandatory")


class _WfIpRipAnnounceAction_Type(Integer32):
    """Custom type wfIpRipAnnounceAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpRipAnnounceAction_Type.__name__ = "Integer32"
_WfIpRipAnnounceAction_Object = MibTableColumn
wfIpRipAnnounceAction = _WfIpRipAnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 6),
    _WfIpRipAnnounceAction_Type()
)
wfIpRipAnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceAction.setStatus("mandatory")
_WfIpRipAnnouncePrecedence_Type = Integer32
_WfIpRipAnnouncePrecedence_Object = MibTableColumn
wfIpRipAnnouncePrecedence = _WfIpRipAnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 7),
    _WfIpRipAnnouncePrecedence_Type()
)
wfIpRipAnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnouncePrecedence.setStatus("mandatory")


class _WfIpRipAnnounceRouteSource_Type(Integer32):
    """Custom type wfIpRipAnnounceRouteSource based on Integer32"""
    defaultValue = 63


_WfIpRipAnnounceRouteSource_Object = MibTableColumn
wfIpRipAnnounceRouteSource = _WfIpRipAnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 8),
    _WfIpRipAnnounceRouteSource_Type()
)
wfIpRipAnnounceRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceRouteSource.setStatus("mandatory")


class _WfIpRipAnnounceExtRouteSource_Type(Integer32):
    """Custom type wfIpRipAnnounceExtRouteSource based on Integer32"""
    defaultValue = 63


_WfIpRipAnnounceExtRouteSource_Object = MibTableColumn
wfIpRipAnnounceExtRouteSource = _WfIpRipAnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 9),
    _WfIpRipAnnounceExtRouteSource_Type()
)
wfIpRipAnnounceExtRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceExtRouteSource.setStatus("mandatory")
_WfIpRipAnnounceAdvertise_Type = OctetString
_WfIpRipAnnounceAdvertise_Object = MibTableColumn
wfIpRipAnnounceAdvertise = _WfIpRipAnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 10),
    _WfIpRipAnnounceAdvertise_Type()
)
wfIpRipAnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceAdvertise.setStatus("mandatory")
_WfIpRipAnnounceRipGateway_Type = OctetString
_WfIpRipAnnounceRipGateway_Object = MibTableColumn
wfIpRipAnnounceRipGateway = _WfIpRipAnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 11),
    _WfIpRipAnnounceRipGateway_Type()
)
wfIpRipAnnounceRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceRipGateway.setStatus("mandatory")
_WfIpRipAnnounceRipInterface_Type = OctetString
_WfIpRipAnnounceRipInterface_Object = MibTableColumn
wfIpRipAnnounceRipInterface = _WfIpRipAnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 12),
    _WfIpRipAnnounceRipInterface_Type()
)
wfIpRipAnnounceRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceRipInterface.setStatus("mandatory")
_WfIpRipAnnounceOspfRouterId_Type = OctetString
_WfIpRipAnnounceOspfRouterId_Object = MibTableColumn
wfIpRipAnnounceOspfRouterId = _WfIpRipAnnounceOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 13),
    _WfIpRipAnnounceOspfRouterId_Type()
)
wfIpRipAnnounceOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceOspfRouterId.setStatus("mandatory")


class _WfIpRipAnnounceOspfType_Type(Integer32):
    """Custom type wfIpRipAnnounceOspfType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpRipAnnounceOspfType_Type.__name__ = "Integer32"
_WfIpRipAnnounceOspfType_Object = MibTableColumn
wfIpRipAnnounceOspfType = _WfIpRipAnnounceOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 14),
    _WfIpRipAnnounceOspfType_Type()
)
wfIpRipAnnounceOspfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceOspfType.setStatus("mandatory")
_WfIpRipAnnounceOspfTag_Type = OctetString
_WfIpRipAnnounceOspfTag_Object = MibTableColumn
wfIpRipAnnounceOspfTag = _WfIpRipAnnounceOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 15),
    _WfIpRipAnnounceOspfTag_Type()
)
wfIpRipAnnounceOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceOspfTag.setStatus("mandatory")
_WfIpRipAnnounceEgpPeer_Type = OctetString
_WfIpRipAnnounceEgpPeer_Object = MibTableColumn
wfIpRipAnnounceEgpPeer = _WfIpRipAnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 16),
    _WfIpRipAnnounceEgpPeer_Type()
)
wfIpRipAnnounceEgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceEgpPeer.setStatus("mandatory")
_WfIpRipAnnounceEgpPeerAs_Type = OctetString
_WfIpRipAnnounceEgpPeerAs_Object = MibTableColumn
wfIpRipAnnounceEgpPeerAs = _WfIpRipAnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 17),
    _WfIpRipAnnounceEgpPeerAs_Type()
)
wfIpRipAnnounceEgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceEgpPeerAs.setStatus("mandatory")
_WfIpRipAnnounceEgpGateway_Type = OctetString
_WfIpRipAnnounceEgpGateway_Object = MibTableColumn
wfIpRipAnnounceEgpGateway = _WfIpRipAnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 18),
    _WfIpRipAnnounceEgpGateway_Type()
)
wfIpRipAnnounceEgpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceEgpGateway.setStatus("mandatory")
_WfIpRipAnnounceBgpPeer_Type = OctetString
_WfIpRipAnnounceBgpPeer_Object = MibTableColumn
wfIpRipAnnounceBgpPeer = _WfIpRipAnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 19),
    _WfIpRipAnnounceBgpPeer_Type()
)
wfIpRipAnnounceBgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceBgpPeer.setStatus("mandatory")
_WfIpRipAnnounceBgpPeerAs_Type = OctetString
_WfIpRipAnnounceBgpPeerAs_Object = MibTableColumn
wfIpRipAnnounceBgpPeerAs = _WfIpRipAnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 20),
    _WfIpRipAnnounceBgpPeerAs_Type()
)
wfIpRipAnnounceBgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceBgpPeerAs.setStatus("mandatory")
_WfIpRipAnnounceBgpNextHop_Type = OctetString
_WfIpRipAnnounceBgpNextHop_Object = MibTableColumn
wfIpRipAnnounceBgpNextHop = _WfIpRipAnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 21),
    _WfIpRipAnnounceBgpNextHop_Type()
)
wfIpRipAnnounceBgpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceBgpNextHop.setStatus("mandatory")
_WfIpRipAnnounceInterface_Type = OctetString
_WfIpRipAnnounceInterface_Object = MibTableColumn
wfIpRipAnnounceInterface = _WfIpRipAnnounceInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 22),
    _WfIpRipAnnounceInterface_Type()
)
wfIpRipAnnounceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceInterface.setStatus("mandatory")


class _WfIpRipAnnounceRipMetric_Type(Integer32):
    """Custom type wfIpRipAnnounceRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfIpRipAnnounceRipMetric_Type.__name__ = "Integer32"
_WfIpRipAnnounceRipMetric_Object = MibTableColumn
wfIpRipAnnounceRipMetric = _WfIpRipAnnounceRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 2, 1, 23),
    _WfIpRipAnnounceRipMetric_Type()
)
wfIpRipAnnounceRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRipAnnounceRipMetric.setStatus("mandatory")
_WfIpOspfAcceptTable_Object = MibTable
wfIpOspfAcceptTable = _WfIpOspfAcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    wfIpOspfAcceptTable.setStatus("mandatory")
_WfIpOspfAcceptEntry_Object = MibTableRow
wfIpOspfAcceptEntry = _WfIpOspfAcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1)
)
wfIpOspfAcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpOspfAcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpOspfAcceptEntry.setStatus("mandatory")


class _WfIpOspfAcceptDelete_Type(Integer32):
    """Custom type wfIpOspfAcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpOspfAcceptDelete_Type.__name__ = "Integer32"
_WfIpOspfAcceptDelete_Object = MibTableColumn
wfIpOspfAcceptDelete = _WfIpOspfAcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 1),
    _WfIpOspfAcceptDelete_Type()
)
wfIpOspfAcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptDelete.setStatus("mandatory")


class _WfIpOspfAcceptDisable_Type(Integer32):
    """Custom type wfIpOspfAcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpOspfAcceptDisable_Type.__name__ = "Integer32"
_WfIpOspfAcceptDisable_Object = MibTableColumn
wfIpOspfAcceptDisable = _WfIpOspfAcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 2),
    _WfIpOspfAcceptDisable_Type()
)
wfIpOspfAcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptDisable.setStatus("mandatory")
_WfIpOspfAcceptIndex_Type = Integer32
_WfIpOspfAcceptIndex_Object = MibTableColumn
wfIpOspfAcceptIndex = _WfIpOspfAcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 3),
    _WfIpOspfAcceptIndex_Type()
)
wfIpOspfAcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpOspfAcceptIndex.setStatus("mandatory")
_WfIpOspfAcceptName_Type = DisplayString
_WfIpOspfAcceptName_Object = MibTableColumn
wfIpOspfAcceptName = _WfIpOspfAcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 4),
    _WfIpOspfAcceptName_Type()
)
wfIpOspfAcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptName.setStatus("mandatory")
_WfIpOspfAcceptNetworks_Type = OctetString
_WfIpOspfAcceptNetworks_Object = MibTableColumn
wfIpOspfAcceptNetworks = _WfIpOspfAcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 5),
    _WfIpOspfAcceptNetworks_Type()
)
wfIpOspfAcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptNetworks.setStatus("mandatory")


class _WfIpOspfAcceptAction_Type(Integer32):
    """Custom type wfIpOspfAcceptAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpOspfAcceptAction_Type.__name__ = "Integer32"
_WfIpOspfAcceptAction_Object = MibTableColumn
wfIpOspfAcceptAction = _WfIpOspfAcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 6),
    _WfIpOspfAcceptAction_Type()
)
wfIpOspfAcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptAction.setStatus("mandatory")


class _WfIpOspfAcceptPreference_Type(Integer32):
    """Custom type wfIpOspfAcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpOspfAcceptPreference_Type.__name__ = "Integer32"
_WfIpOspfAcceptPreference_Object = MibTableColumn
wfIpOspfAcceptPreference = _WfIpOspfAcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 7),
    _WfIpOspfAcceptPreference_Type()
)
wfIpOspfAcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptPreference.setStatus("mandatory")
_WfIpOspfAcceptPrecedence_Type = Integer32
_WfIpOspfAcceptPrecedence_Object = MibTableColumn
wfIpOspfAcceptPrecedence = _WfIpOspfAcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 8),
    _WfIpOspfAcceptPrecedence_Type()
)
wfIpOspfAcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptPrecedence.setStatus("mandatory")
_WfIpOspfAcceptInject_Type = OctetString
_WfIpOspfAcceptInject_Object = MibTableColumn
wfIpOspfAcceptInject = _WfIpOspfAcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 9),
    _WfIpOspfAcceptInject_Type()
)
wfIpOspfAcceptInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpOspfAcceptInject.setStatus("mandatory")


class _WfIpOspfAcceptType_Type(Integer32):
    """Custom type wfIpOspfAcceptType based on Integer32"""
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
        *(("any", 3),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpOspfAcceptType_Type.__name__ = "Integer32"
_WfIpOspfAcceptType_Object = MibTableColumn
wfIpOspfAcceptType = _WfIpOspfAcceptType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 10),
    _WfIpOspfAcceptType_Type()
)
wfIpOspfAcceptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptType.setStatus("mandatory")
_WfIpOspfAcceptTag_Type = OctetString
_WfIpOspfAcceptTag_Object = MibTableColumn
wfIpOspfAcceptTag = _WfIpOspfAcceptTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 3, 1, 11),
    _WfIpOspfAcceptTag_Type()
)
wfIpOspfAcceptTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAcceptTag.setStatus("mandatory")
_WfIpOspfAnnounceTable_Object = MibTable
wfIpOspfAnnounceTable = _WfIpOspfAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4)
)
if mibBuilder.loadTexts:
    wfIpOspfAnnounceTable.setStatus("mandatory")
_WfIpOspfAnnounceEntry_Object = MibTableRow
wfIpOspfAnnounceEntry = _WfIpOspfAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1)
)
wfIpOspfAnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpOspfAnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpOspfAnnounceEntry.setStatus("mandatory")


class _WfIpOspfAnnounceDelete_Type(Integer32):
    """Custom type wfIpOspfAnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpOspfAnnounceDelete_Type.__name__ = "Integer32"
_WfIpOspfAnnounceDelete_Object = MibTableColumn
wfIpOspfAnnounceDelete = _WfIpOspfAnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 1),
    _WfIpOspfAnnounceDelete_Type()
)
wfIpOspfAnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceDelete.setStatus("mandatory")


class _WfIpOspfAnnounceDisable_Type(Integer32):
    """Custom type wfIpOspfAnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpOspfAnnounceDisable_Type.__name__ = "Integer32"
_WfIpOspfAnnounceDisable_Object = MibTableColumn
wfIpOspfAnnounceDisable = _WfIpOspfAnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 2),
    _WfIpOspfAnnounceDisable_Type()
)
wfIpOspfAnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceDisable.setStatus("mandatory")
_WfIpOspfAnnounceIndex_Type = Integer32
_WfIpOspfAnnounceIndex_Object = MibTableColumn
wfIpOspfAnnounceIndex = _WfIpOspfAnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 3),
    _WfIpOspfAnnounceIndex_Type()
)
wfIpOspfAnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceIndex.setStatus("mandatory")
_WfIpOspfAnnounceName_Type = DisplayString
_WfIpOspfAnnounceName_Object = MibTableColumn
wfIpOspfAnnounceName = _WfIpOspfAnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 4),
    _WfIpOspfAnnounceName_Type()
)
wfIpOspfAnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceName.setStatus("mandatory")
_WfIpOspfAnnounceNetworks_Type = OctetString
_WfIpOspfAnnounceNetworks_Object = MibTableColumn
wfIpOspfAnnounceNetworks = _WfIpOspfAnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 5),
    _WfIpOspfAnnounceNetworks_Type()
)
wfIpOspfAnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceNetworks.setStatus("mandatory")


class _WfIpOspfAnnounceAction_Type(Integer32):
    """Custom type wfIpOspfAnnounceAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpOspfAnnounceAction_Type.__name__ = "Integer32"
_WfIpOspfAnnounceAction_Object = MibTableColumn
wfIpOspfAnnounceAction = _WfIpOspfAnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 6),
    _WfIpOspfAnnounceAction_Type()
)
wfIpOspfAnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceAction.setStatus("mandatory")
_WfIpOspfAnnouncePrecedence_Type = Integer32
_WfIpOspfAnnouncePrecedence_Object = MibTableColumn
wfIpOspfAnnouncePrecedence = _WfIpOspfAnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 7),
    _WfIpOspfAnnouncePrecedence_Type()
)
wfIpOspfAnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnouncePrecedence.setStatus("mandatory")


class _WfIpOspfAnnounceRouteSource_Type(Integer32):
    """Custom type wfIpOspfAnnounceRouteSource based on Integer32"""
    defaultValue = 63


_WfIpOspfAnnounceRouteSource_Object = MibTableColumn
wfIpOspfAnnounceRouteSource = _WfIpOspfAnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 8),
    _WfIpOspfAnnounceRouteSource_Type()
)
wfIpOspfAnnounceRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceRouteSource.setStatus("mandatory")


class _WfIpOspfAnnounceExtRouteSource_Type(Integer32):
    """Custom type wfIpOspfAnnounceExtRouteSource based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            63
        )
    )
    namedValues = NamedValues(
        ("any", 63)
    )


_WfIpOspfAnnounceExtRouteSource_Type.__name__ = "Integer32"
_WfIpOspfAnnounceExtRouteSource_Object = MibTableColumn
wfIpOspfAnnounceExtRouteSource = _WfIpOspfAnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 9),
    _WfIpOspfAnnounceExtRouteSource_Type()
)
wfIpOspfAnnounceExtRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceExtRouteSource.setStatus("mandatory")
_WfIpOspfAnnounceAdvertise_Type = OctetString
_WfIpOspfAnnounceAdvertise_Object = MibTableColumn
wfIpOspfAnnounceAdvertise = _WfIpOspfAnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 10),
    _WfIpOspfAnnounceAdvertise_Type()
)
wfIpOspfAnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceAdvertise.setStatus("mandatory")
_WfIpOspfAnnounceRipGateway_Type = OctetString
_WfIpOspfAnnounceRipGateway_Object = MibTableColumn
wfIpOspfAnnounceRipGateway = _WfIpOspfAnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 11),
    _WfIpOspfAnnounceRipGateway_Type()
)
wfIpOspfAnnounceRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceRipGateway.setStatus("mandatory")
_WfIpOspfAnnounceRipInterface_Type = OctetString
_WfIpOspfAnnounceRipInterface_Object = MibTableColumn
wfIpOspfAnnounceRipInterface = _WfIpOspfAnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 12),
    _WfIpOspfAnnounceRipInterface_Type()
)
wfIpOspfAnnounceRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceRipInterface.setStatus("mandatory")
_WfIpOspfAnnounceOspfRouterId_Type = OctetString
_WfIpOspfAnnounceOspfRouterId_Object = MibTableColumn
wfIpOspfAnnounceOspfRouterId = _WfIpOspfAnnounceOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 13),
    _WfIpOspfAnnounceOspfRouterId_Type()
)
wfIpOspfAnnounceOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceOspfRouterId.setStatus("mandatory")


class _WfIpOspfAnnounceOspfType_Type(Integer32):
    """Custom type wfIpOspfAnnounceOspfType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpOspfAnnounceOspfType_Type.__name__ = "Integer32"
_WfIpOspfAnnounceOspfType_Object = MibTableColumn
wfIpOspfAnnounceOspfType = _WfIpOspfAnnounceOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 14),
    _WfIpOspfAnnounceOspfType_Type()
)
wfIpOspfAnnounceOspfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceOspfType.setStatus("mandatory")
_WfIpOspfAnnounceOspfTag_Type = OctetString
_WfIpOspfAnnounceOspfTag_Object = MibTableColumn
wfIpOspfAnnounceOspfTag = _WfIpOspfAnnounceOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 15),
    _WfIpOspfAnnounceOspfTag_Type()
)
wfIpOspfAnnounceOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceOspfTag.setStatus("mandatory")
_WfIpOspfAnnounceEgpPeer_Type = OctetString
_WfIpOspfAnnounceEgpPeer_Object = MibTableColumn
wfIpOspfAnnounceEgpPeer = _WfIpOspfAnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 16),
    _WfIpOspfAnnounceEgpPeer_Type()
)
wfIpOspfAnnounceEgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceEgpPeer.setStatus("mandatory")
_WfIpOspfAnnounceEgpPeerAs_Type = OctetString
_WfIpOspfAnnounceEgpPeerAs_Object = MibTableColumn
wfIpOspfAnnounceEgpPeerAs = _WfIpOspfAnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 17),
    _WfIpOspfAnnounceEgpPeerAs_Type()
)
wfIpOspfAnnounceEgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceEgpPeerAs.setStatus("mandatory")
_WfIpOspfAnnounceEgpGateway_Type = OctetString
_WfIpOspfAnnounceEgpGateway_Object = MibTableColumn
wfIpOspfAnnounceEgpGateway = _WfIpOspfAnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 18),
    _WfIpOspfAnnounceEgpGateway_Type()
)
wfIpOspfAnnounceEgpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceEgpGateway.setStatus("mandatory")
_WfIpOspfAnnounceBgpPeer_Type = OctetString
_WfIpOspfAnnounceBgpPeer_Object = MibTableColumn
wfIpOspfAnnounceBgpPeer = _WfIpOspfAnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 19),
    _WfIpOspfAnnounceBgpPeer_Type()
)
wfIpOspfAnnounceBgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceBgpPeer.setStatus("mandatory")
_WfIpOspfAnnounceBgpPeerAs_Type = OctetString
_WfIpOspfAnnounceBgpPeerAs_Object = MibTableColumn
wfIpOspfAnnounceBgpPeerAs = _WfIpOspfAnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 20),
    _WfIpOspfAnnounceBgpPeerAs_Type()
)
wfIpOspfAnnounceBgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceBgpPeerAs.setStatus("mandatory")
_WfIpOspfAnnounceBgpNextHop_Type = OctetString
_WfIpOspfAnnounceBgpNextHop_Object = MibTableColumn
wfIpOspfAnnounceBgpNextHop = _WfIpOspfAnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 21),
    _WfIpOspfAnnounceBgpNextHop_Type()
)
wfIpOspfAnnounceBgpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceBgpNextHop.setStatus("mandatory")


class _WfIpOspfAnnounceType_Type(Integer32):
    """Custom type wfIpOspfAnnounceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_WfIpOspfAnnounceType_Type.__name__ = "Integer32"
_WfIpOspfAnnounceType_Object = MibTableColumn
wfIpOspfAnnounceType = _WfIpOspfAnnounceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 22),
    _WfIpOspfAnnounceType_Type()
)
wfIpOspfAnnounceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceType.setStatus("mandatory")
_WfIpOspfAnnounceTag_Type = Integer32
_WfIpOspfAnnounceTag_Object = MibTableColumn
wfIpOspfAnnounceTag = _WfIpOspfAnnounceTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 23),
    _WfIpOspfAnnounceTag_Type()
)
wfIpOspfAnnounceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceTag.setStatus("mandatory")


class _WfIpOspfAnnounceAutoTag_Type(Integer32):
    """Custom type wfIpOspfAnnounceAutoTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("wf", 3))
    )


_WfIpOspfAnnounceAutoTag_Type.__name__ = "Integer32"
_WfIpOspfAnnounceAutoTag_Object = MibTableColumn
wfIpOspfAnnounceAutoTag = _WfIpOspfAnnounceAutoTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 24),
    _WfIpOspfAnnounceAutoTag_Type()
)
wfIpOspfAnnounceAutoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceAutoTag.setStatus("mandatory")
_WfIpOspfAnnounceMetric_Type = Integer32
_WfIpOspfAnnounceMetric_Object = MibTableColumn
wfIpOspfAnnounceMetric = _WfIpOspfAnnounceMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 25),
    _WfIpOspfAnnounceMetric_Type()
)
wfIpOspfAnnounceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceMetric.setStatus("mandatory")


class _WfIpOspfAnnounceNssaPropagate_Type(Integer32):
    """Custom type wfIpOspfAnnounceNssaPropagate based on Integer32"""
    defaultValue = 2

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


_WfIpOspfAnnounceNssaPropagate_Type.__name__ = "Integer32"
_WfIpOspfAnnounceNssaPropagate_Object = MibTableColumn
wfIpOspfAnnounceNssaPropagate = _WfIpOspfAnnounceNssaPropagate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 4, 1, 26),
    _WfIpOspfAnnounceNssaPropagate_Type()
)
wfIpOspfAnnounceNssaPropagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfAnnounceNssaPropagate.setStatus("mandatory")
_WfIpEgpAcceptTable_Object = MibTable
wfIpEgpAcceptTable = _WfIpEgpAcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5)
)
if mibBuilder.loadTexts:
    wfIpEgpAcceptTable.setStatus("mandatory")
_WfIpEgpAcceptEntry_Object = MibTableRow
wfIpEgpAcceptEntry = _WfIpEgpAcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1)
)
wfIpEgpAcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpEgpAcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpEgpAcceptEntry.setStatus("mandatory")


class _WfIpEgpAcceptDelete_Type(Integer32):
    """Custom type wfIpEgpAcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpEgpAcceptDelete_Type.__name__ = "Integer32"
_WfIpEgpAcceptDelete_Object = MibTableColumn
wfIpEgpAcceptDelete = _WfIpEgpAcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 1),
    _WfIpEgpAcceptDelete_Type()
)
wfIpEgpAcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptDelete.setStatus("mandatory")


class _WfIpEgpAcceptDisable_Type(Integer32):
    """Custom type wfIpEgpAcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpEgpAcceptDisable_Type.__name__ = "Integer32"
_WfIpEgpAcceptDisable_Object = MibTableColumn
wfIpEgpAcceptDisable = _WfIpEgpAcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 2),
    _WfIpEgpAcceptDisable_Type()
)
wfIpEgpAcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptDisable.setStatus("mandatory")
_WfIpEgpAcceptIndex_Type = Integer32
_WfIpEgpAcceptIndex_Object = MibTableColumn
wfIpEgpAcceptIndex = _WfIpEgpAcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 3),
    _WfIpEgpAcceptIndex_Type()
)
wfIpEgpAcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpEgpAcceptIndex.setStatus("mandatory")
_WfIpEgpAcceptName_Type = DisplayString
_WfIpEgpAcceptName_Object = MibTableColumn
wfIpEgpAcceptName = _WfIpEgpAcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 4),
    _WfIpEgpAcceptName_Type()
)
wfIpEgpAcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptName.setStatus("mandatory")
_WfIpEgpAcceptNetworks_Type = OctetString
_WfIpEgpAcceptNetworks_Object = MibTableColumn
wfIpEgpAcceptNetworks = _WfIpEgpAcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 5),
    _WfIpEgpAcceptNetworks_Type()
)
wfIpEgpAcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptNetworks.setStatus("mandatory")


class _WfIpEgpAcceptAction_Type(Integer32):
    """Custom type wfIpEgpAcceptAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpEgpAcceptAction_Type.__name__ = "Integer32"
_WfIpEgpAcceptAction_Object = MibTableColumn
wfIpEgpAcceptAction = _WfIpEgpAcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 6),
    _WfIpEgpAcceptAction_Type()
)
wfIpEgpAcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptAction.setStatus("mandatory")


class _WfIpEgpAcceptPreference_Type(Integer32):
    """Custom type wfIpEgpAcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpEgpAcceptPreference_Type.__name__ = "Integer32"
_WfIpEgpAcceptPreference_Object = MibTableColumn
wfIpEgpAcceptPreference = _WfIpEgpAcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 7),
    _WfIpEgpAcceptPreference_Type()
)
wfIpEgpAcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptPreference.setStatus("mandatory")
_WfIpEgpAcceptPrecedence_Type = Integer32
_WfIpEgpAcceptPrecedence_Object = MibTableColumn
wfIpEgpAcceptPrecedence = _WfIpEgpAcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 8),
    _WfIpEgpAcceptPrecedence_Type()
)
wfIpEgpAcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptPrecedence.setStatus("mandatory")
_WfIpEgpAcceptInject_Type = OctetString
_WfIpEgpAcceptInject_Object = MibTableColumn
wfIpEgpAcceptInject = _WfIpEgpAcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 9),
    _WfIpEgpAcceptInject_Type()
)
wfIpEgpAcceptInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpEgpAcceptInject.setStatus("mandatory")
_WfIpEgpAcceptPeer_Type = OctetString
_WfIpEgpAcceptPeer_Object = MibTableColumn
wfIpEgpAcceptPeer = _WfIpEgpAcceptPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 10),
    _WfIpEgpAcceptPeer_Type()
)
wfIpEgpAcceptPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptPeer.setStatus("mandatory")
_WfIpEgpAcceptAs_Type = OctetString
_WfIpEgpAcceptAs_Object = MibTableColumn
wfIpEgpAcceptAs = _WfIpEgpAcceptAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 11),
    _WfIpEgpAcceptAs_Type()
)
wfIpEgpAcceptAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptAs.setStatus("mandatory")
_WfIpEgpAcceptGateway_Type = OctetString
_WfIpEgpAcceptGateway_Object = MibTableColumn
wfIpEgpAcceptGateway = _WfIpEgpAcceptGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 5, 1, 12),
    _WfIpEgpAcceptGateway_Type()
)
wfIpEgpAcceptGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAcceptGateway.setStatus("mandatory")
_WfIpEgpAnnounceTable_Object = MibTable
wfIpEgpAnnounceTable = _WfIpEgpAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6)
)
if mibBuilder.loadTexts:
    wfIpEgpAnnounceTable.setStatus("mandatory")
_WfIpEgpAnnounceEntry_Object = MibTableRow
wfIpEgpAnnounceEntry = _WfIpEgpAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1)
)
wfIpEgpAnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpEgpAnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpEgpAnnounceEntry.setStatus("mandatory")


class _WfIpEgpAnnounceDelete_Type(Integer32):
    """Custom type wfIpEgpAnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpEgpAnnounceDelete_Type.__name__ = "Integer32"
_WfIpEgpAnnounceDelete_Object = MibTableColumn
wfIpEgpAnnounceDelete = _WfIpEgpAnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 1),
    _WfIpEgpAnnounceDelete_Type()
)
wfIpEgpAnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceDelete.setStatus("mandatory")


class _WfIpEgpAnnounceDisable_Type(Integer32):
    """Custom type wfIpEgpAnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpEgpAnnounceDisable_Type.__name__ = "Integer32"
_WfIpEgpAnnounceDisable_Object = MibTableColumn
wfIpEgpAnnounceDisable = _WfIpEgpAnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 2),
    _WfIpEgpAnnounceDisable_Type()
)
wfIpEgpAnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceDisable.setStatus("mandatory")
_WfIpEgpAnnounceIndex_Type = Integer32
_WfIpEgpAnnounceIndex_Object = MibTableColumn
wfIpEgpAnnounceIndex = _WfIpEgpAnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 3),
    _WfIpEgpAnnounceIndex_Type()
)
wfIpEgpAnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceIndex.setStatus("mandatory")
_WfIpEgpAnnounceName_Type = DisplayString
_WfIpEgpAnnounceName_Object = MibTableColumn
wfIpEgpAnnounceName = _WfIpEgpAnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 4),
    _WfIpEgpAnnounceName_Type()
)
wfIpEgpAnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceName.setStatus("mandatory")
_WfIpEgpAnnounceNetworks_Type = OctetString
_WfIpEgpAnnounceNetworks_Object = MibTableColumn
wfIpEgpAnnounceNetworks = _WfIpEgpAnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 5),
    _WfIpEgpAnnounceNetworks_Type()
)
wfIpEgpAnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceNetworks.setStatus("mandatory")


class _WfIpEgpAnnounceAction_Type(Integer32):
    """Custom type wfIpEgpAnnounceAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpEgpAnnounceAction_Type.__name__ = "Integer32"
_WfIpEgpAnnounceAction_Object = MibTableColumn
wfIpEgpAnnounceAction = _WfIpEgpAnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 6),
    _WfIpEgpAnnounceAction_Type()
)
wfIpEgpAnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceAction.setStatus("mandatory")
_WfIpEgpAnnouncePrecedence_Type = Integer32
_WfIpEgpAnnouncePrecedence_Object = MibTableColumn
wfIpEgpAnnouncePrecedence = _WfIpEgpAnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 7),
    _WfIpEgpAnnouncePrecedence_Type()
)
wfIpEgpAnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnouncePrecedence.setStatus("mandatory")


class _WfIpEgpAnnounceRouteSource_Type(Integer32):
    """Custom type wfIpEgpAnnounceRouteSource based on Integer32"""
    defaultValue = 63


_WfIpEgpAnnounceRouteSource_Object = MibTableColumn
wfIpEgpAnnounceRouteSource = _WfIpEgpAnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 8),
    _WfIpEgpAnnounceRouteSource_Type()
)
wfIpEgpAnnounceRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceRouteSource.setStatus("mandatory")


class _WfIpEgpAnnounceExtRouteSource_Type(Integer32):
    """Custom type wfIpEgpAnnounceExtRouteSource based on Integer32"""
    defaultValue = 63


_WfIpEgpAnnounceExtRouteSource_Object = MibTableColumn
wfIpEgpAnnounceExtRouteSource = _WfIpEgpAnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 9),
    _WfIpEgpAnnounceExtRouteSource_Type()
)
wfIpEgpAnnounceExtRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceExtRouteSource.setStatus("mandatory")
_WfIpEgpAnnounceAdvertise_Type = OctetString
_WfIpEgpAnnounceAdvertise_Object = MibTableColumn
wfIpEgpAnnounceAdvertise = _WfIpEgpAnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 10),
    _WfIpEgpAnnounceAdvertise_Type()
)
wfIpEgpAnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceAdvertise.setStatus("mandatory")
_WfIpEgpAnnounceRipGateway_Type = OctetString
_WfIpEgpAnnounceRipGateway_Object = MibTableColumn
wfIpEgpAnnounceRipGateway = _WfIpEgpAnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 11),
    _WfIpEgpAnnounceRipGateway_Type()
)
wfIpEgpAnnounceRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceRipGateway.setStatus("mandatory")
_WfIpEgpAnnounceRipInterface_Type = OctetString
_WfIpEgpAnnounceRipInterface_Object = MibTableColumn
wfIpEgpAnnounceRipInterface = _WfIpEgpAnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 12),
    _WfIpEgpAnnounceRipInterface_Type()
)
wfIpEgpAnnounceRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceRipInterface.setStatus("mandatory")
_WfIpEgpAnnounceOspfRouterId_Type = OctetString
_WfIpEgpAnnounceOspfRouterId_Object = MibTableColumn
wfIpEgpAnnounceOspfRouterId = _WfIpEgpAnnounceOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 13),
    _WfIpEgpAnnounceOspfRouterId_Type()
)
wfIpEgpAnnounceOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceOspfRouterId.setStatus("mandatory")


class _WfIpEgpAnnounceOspfType_Type(Integer32):
    """Custom type wfIpEgpAnnounceOspfType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpEgpAnnounceOspfType_Type.__name__ = "Integer32"
_WfIpEgpAnnounceOspfType_Object = MibTableColumn
wfIpEgpAnnounceOspfType = _WfIpEgpAnnounceOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 14),
    _WfIpEgpAnnounceOspfType_Type()
)
wfIpEgpAnnounceOspfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceOspfType.setStatus("mandatory")
_WfIpEgpAnnounceOspfTag_Type = OctetString
_WfIpEgpAnnounceOspfTag_Object = MibTableColumn
wfIpEgpAnnounceOspfTag = _WfIpEgpAnnounceOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 15),
    _WfIpEgpAnnounceOspfTag_Type()
)
wfIpEgpAnnounceOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceOspfTag.setStatus("mandatory")
_WfIpEgpAnnounceEgpPeer_Type = OctetString
_WfIpEgpAnnounceEgpPeer_Object = MibTableColumn
wfIpEgpAnnounceEgpPeer = _WfIpEgpAnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 16),
    _WfIpEgpAnnounceEgpPeer_Type()
)
wfIpEgpAnnounceEgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceEgpPeer.setStatus("mandatory")
_WfIpEgpAnnounceEgpPeerAs_Type = OctetString
_WfIpEgpAnnounceEgpPeerAs_Object = MibTableColumn
wfIpEgpAnnounceEgpPeerAs = _WfIpEgpAnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 17),
    _WfIpEgpAnnounceEgpPeerAs_Type()
)
wfIpEgpAnnounceEgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceEgpPeerAs.setStatus("mandatory")
_WfIpEgpAnnounceEgpGateway_Type = OctetString
_WfIpEgpAnnounceEgpGateway_Object = MibTableColumn
wfIpEgpAnnounceEgpGateway = _WfIpEgpAnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 18),
    _WfIpEgpAnnounceEgpGateway_Type()
)
wfIpEgpAnnounceEgpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceEgpGateway.setStatus("mandatory")
_WfIpEgpAnnounceBgpPeer_Type = OctetString
_WfIpEgpAnnounceBgpPeer_Object = MibTableColumn
wfIpEgpAnnounceBgpPeer = _WfIpEgpAnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 19),
    _WfIpEgpAnnounceBgpPeer_Type()
)
wfIpEgpAnnounceBgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceBgpPeer.setStatus("mandatory")
_WfIpEgpAnnounceBgpPeerAs_Type = OctetString
_WfIpEgpAnnounceBgpPeerAs_Object = MibTableColumn
wfIpEgpAnnounceBgpPeerAs = _WfIpEgpAnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 20),
    _WfIpEgpAnnounceBgpPeerAs_Type()
)
wfIpEgpAnnounceBgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceBgpPeerAs.setStatus("mandatory")
_WfIpEgpAnnounceBgpNextHop_Type = OctetString
_WfIpEgpAnnounceBgpNextHop_Object = MibTableColumn
wfIpEgpAnnounceBgpNextHop = _WfIpEgpAnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 21),
    _WfIpEgpAnnounceBgpNextHop_Type()
)
wfIpEgpAnnounceBgpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceBgpNextHop.setStatus("mandatory")
_WfIpEgpAnnouncePeer_Type = OctetString
_WfIpEgpAnnouncePeer_Object = MibTableColumn
wfIpEgpAnnouncePeer = _WfIpEgpAnnouncePeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 22),
    _WfIpEgpAnnouncePeer_Type()
)
wfIpEgpAnnouncePeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnouncePeer.setStatus("mandatory")
_WfIpEgpAnnounceInterface_Type = OctetString
_WfIpEgpAnnounceInterface_Object = MibTableColumn
wfIpEgpAnnounceInterface = _WfIpEgpAnnounceInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 23),
    _WfIpEgpAnnounceInterface_Type()
)
wfIpEgpAnnounceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceInterface.setStatus("mandatory")


class _WfIpEgpAnnounceMetric_Type(Integer32):
    """Custom type wfIpEgpAnnounceMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpEgpAnnounceMetric_Type.__name__ = "Integer32"
_WfIpEgpAnnounceMetric_Object = MibTableColumn
wfIpEgpAnnounceMetric = _WfIpEgpAnnounceMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 6, 1, 24),
    _WfIpEgpAnnounceMetric_Type()
)
wfIpEgpAnnounceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpEgpAnnounceMetric.setStatus("mandatory")
_WfIpBgp3AcceptTable_Object = MibTable
wfIpBgp3AcceptTable = _WfIpBgp3AcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7)
)
if mibBuilder.loadTexts:
    wfIpBgp3AcceptTable.setStatus("mandatory")
_WfIpBgp3AcceptEntry_Object = MibTableRow
wfIpBgp3AcceptEntry = _WfIpBgp3AcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1)
)
wfIpBgp3AcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpBgp3AcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpBgp3AcceptEntry.setStatus("mandatory")


class _WfIpBgp3AcceptDelete_Type(Integer32):
    """Custom type wfIpBgp3AcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpBgp3AcceptDelete_Type.__name__ = "Integer32"
_WfIpBgp3AcceptDelete_Object = MibTableColumn
wfIpBgp3AcceptDelete = _WfIpBgp3AcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 1),
    _WfIpBgp3AcceptDelete_Type()
)
wfIpBgp3AcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptDelete.setStatus("mandatory")


class _WfIpBgp3AcceptDisable_Type(Integer32):
    """Custom type wfIpBgp3AcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpBgp3AcceptDisable_Type.__name__ = "Integer32"
_WfIpBgp3AcceptDisable_Object = MibTableColumn
wfIpBgp3AcceptDisable = _WfIpBgp3AcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 2),
    _WfIpBgp3AcceptDisable_Type()
)
wfIpBgp3AcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptDisable.setStatus("mandatory")
_WfIpBgp3AcceptIndex_Type = Integer32
_WfIpBgp3AcceptIndex_Object = MibTableColumn
wfIpBgp3AcceptIndex = _WfIpBgp3AcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 3),
    _WfIpBgp3AcceptIndex_Type()
)
wfIpBgp3AcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptIndex.setStatus("mandatory")
_WfIpBgp3AcceptName_Type = DisplayString
_WfIpBgp3AcceptName_Object = MibTableColumn
wfIpBgp3AcceptName = _WfIpBgp3AcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 4),
    _WfIpBgp3AcceptName_Type()
)
wfIpBgp3AcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptName.setStatus("mandatory")
_WfIpBgp3AcceptNetworks_Type = OctetString
_WfIpBgp3AcceptNetworks_Object = MibTableColumn
wfIpBgp3AcceptNetworks = _WfIpBgp3AcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 5),
    _WfIpBgp3AcceptNetworks_Type()
)
wfIpBgp3AcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptNetworks.setStatus("mandatory")


class _WfIpBgp3AcceptAction_Type(Integer32):
    """Custom type wfIpBgp3AcceptAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpBgp3AcceptAction_Type.__name__ = "Integer32"
_WfIpBgp3AcceptAction_Object = MibTableColumn
wfIpBgp3AcceptAction = _WfIpBgp3AcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 6),
    _WfIpBgp3AcceptAction_Type()
)
wfIpBgp3AcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptAction.setStatus("mandatory")


class _WfIpBgp3AcceptPreference_Type(Integer32):
    """Custom type wfIpBgp3AcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpBgp3AcceptPreference_Type.__name__ = "Integer32"
_WfIpBgp3AcceptPreference_Object = MibTableColumn
wfIpBgp3AcceptPreference = _WfIpBgp3AcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 7),
    _WfIpBgp3AcceptPreference_Type()
)
wfIpBgp3AcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptPreference.setStatus("mandatory")
_WfIpBgp3AcceptPrecedence_Type = Integer32
_WfIpBgp3AcceptPrecedence_Object = MibTableColumn
wfIpBgp3AcceptPrecedence = _WfIpBgp3AcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 8),
    _WfIpBgp3AcceptPrecedence_Type()
)
wfIpBgp3AcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptPrecedence.setStatus("mandatory")
_WfIpBgp3AcceptInject_Type = OctetString
_WfIpBgp3AcceptInject_Object = MibTableColumn
wfIpBgp3AcceptInject = _WfIpBgp3AcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 9),
    _WfIpBgp3AcceptInject_Type()
)
wfIpBgp3AcceptInject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptInject.setStatus("mandatory")
_WfIpBgp3AcceptPeerAs_Type = OctetString
_WfIpBgp3AcceptPeerAs_Object = MibTableColumn
wfIpBgp3AcceptPeerAs = _WfIpBgp3AcceptPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 10),
    _WfIpBgp3AcceptPeerAs_Type()
)
wfIpBgp3AcceptPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptPeerAs.setStatus("mandatory")
_WfIpBgp3AcceptPeerAddress_Type = OctetString
_WfIpBgp3AcceptPeerAddress_Object = MibTableColumn
wfIpBgp3AcceptPeerAddress = _WfIpBgp3AcceptPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 11),
    _WfIpBgp3AcceptPeerAddress_Type()
)
wfIpBgp3AcceptPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptPeerAddress.setStatus("mandatory")
_WfIpBgp3AcceptOrigAs_Type = OctetString
_WfIpBgp3AcceptOrigAs_Object = MibTableColumn
wfIpBgp3AcceptOrigAs = _WfIpBgp3AcceptOrigAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 12),
    _WfIpBgp3AcceptOrigAs_Type()
)
wfIpBgp3AcceptOrigAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptOrigAs.setStatus("mandatory")


class _WfIpBgp3AcceptRouteOrigin_Type(Integer32):
    """Custom type wfIpBgp3AcceptRouteOrigin based on Integer32"""
    defaultValue = 7

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
        *(("any", 7),
          ("egp", 2),
          ("igp", 1),
          ("igporegp", 3),
          ("incomplete", 4),
          ("incompleteoregp", 6),
          ("incompleteorigp", 5))
    )


_WfIpBgp3AcceptRouteOrigin_Type.__name__ = "Integer32"
_WfIpBgp3AcceptRouteOrigin_Object = MibTableColumn
wfIpBgp3AcceptRouteOrigin = _WfIpBgp3AcceptRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 13),
    _WfIpBgp3AcceptRouteOrigin_Type()
)
wfIpBgp3AcceptRouteOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptRouteOrigin.setStatus("mandatory")


class _WfIpBgp3AcceptBgp3Preference_Type(Integer32):
    """Custom type wfIpBgp3AcceptBgp3Preference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfIpBgp3AcceptBgp3Preference_Type.__name__ = "Integer32"
_WfIpBgp3AcceptBgp3Preference_Object = MibTableColumn
wfIpBgp3AcceptBgp3Preference = _WfIpBgp3AcceptBgp3Preference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 14),
    _WfIpBgp3AcceptBgp3Preference_Type()
)
wfIpBgp3AcceptBgp3Preference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptBgp3Preference.setStatus("mandatory")


class _WfIpBgp3AcceptAsWeightClass_Type(Integer32):
    """Custom type wfIpBgp3AcceptAsWeightClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5),
          ("class6", 6),
          ("class7", 7),
          ("class8", 8))
    )


_WfIpBgp3AcceptAsWeightClass_Type.__name__ = "Integer32"
_WfIpBgp3AcceptAsWeightClass_Object = MibTableColumn
wfIpBgp3AcceptAsWeightClass = _WfIpBgp3AcceptAsWeightClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 15),
    _WfIpBgp3AcceptAsWeightClass_Type()
)
wfIpBgp3AcceptAsWeightClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptAsWeightClass.setStatus("mandatory")
_WfIpBgp3AcceptCommunityMatch_Type = OctetString
_WfIpBgp3AcceptCommunityMatch_Object = MibTableColumn
wfIpBgp3AcceptCommunityMatch = _WfIpBgp3AcceptCommunityMatch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 7, 1, 16),
    _WfIpBgp3AcceptCommunityMatch_Type()
)
wfIpBgp3AcceptCommunityMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AcceptCommunityMatch.setStatus("mandatory")
_WfIpBgp3AnnounceTable_Object = MibTable
wfIpBgp3AnnounceTable = _WfIpBgp3AnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8)
)
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceTable.setStatus("mandatory")
_WfIpBgp3AnnounceEntry_Object = MibTableRow
wfIpBgp3AnnounceEntry = _WfIpBgp3AnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1)
)
wfIpBgp3AnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpBgp3AnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceEntry.setStatus("mandatory")


class _WfIpBgp3AnnounceDelete_Type(Integer32):
    """Custom type wfIpBgp3AnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpBgp3AnnounceDelete_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceDelete_Object = MibTableColumn
wfIpBgp3AnnounceDelete = _WfIpBgp3AnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 1),
    _WfIpBgp3AnnounceDelete_Type()
)
wfIpBgp3AnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceDelete.setStatus("mandatory")


class _WfIpBgp3AnnounceDisable_Type(Integer32):
    """Custom type wfIpBgp3AnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpBgp3AnnounceDisable_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceDisable_Object = MibTableColumn
wfIpBgp3AnnounceDisable = _WfIpBgp3AnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 2),
    _WfIpBgp3AnnounceDisable_Type()
)
wfIpBgp3AnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceDisable.setStatus("mandatory")
_WfIpBgp3AnnounceIndex_Type = Integer32
_WfIpBgp3AnnounceIndex_Object = MibTableColumn
wfIpBgp3AnnounceIndex = _WfIpBgp3AnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 3),
    _WfIpBgp3AnnounceIndex_Type()
)
wfIpBgp3AnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceIndex.setStatus("mandatory")
_WfIpBgp3AnnounceName_Type = DisplayString
_WfIpBgp3AnnounceName_Object = MibTableColumn
wfIpBgp3AnnounceName = _WfIpBgp3AnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 4),
    _WfIpBgp3AnnounceName_Type()
)
wfIpBgp3AnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceName.setStatus("mandatory")
_WfIpBgp3AnnounceNetworks_Type = OctetString
_WfIpBgp3AnnounceNetworks_Object = MibTableColumn
wfIpBgp3AnnounceNetworks = _WfIpBgp3AnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 5),
    _WfIpBgp3AnnounceNetworks_Type()
)
wfIpBgp3AnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceNetworks.setStatus("mandatory")


class _WfIpBgp3AnnounceAction_Type(Integer32):
    """Custom type wfIpBgp3AnnounceAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpBgp3AnnounceAction_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceAction_Object = MibTableColumn
wfIpBgp3AnnounceAction = _WfIpBgp3AnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 6),
    _WfIpBgp3AnnounceAction_Type()
)
wfIpBgp3AnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceAction.setStatus("mandatory")
_WfIpBgp3AnnouncePrecedence_Type = Integer32
_WfIpBgp3AnnouncePrecedence_Object = MibTableColumn
wfIpBgp3AnnouncePrecedence = _WfIpBgp3AnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 7),
    _WfIpBgp3AnnouncePrecedence_Type()
)
wfIpBgp3AnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnouncePrecedence.setStatus("mandatory")


class _WfIpBgp3AnnounceRouteSource_Type(Integer32):
    """Custom type wfIpBgp3AnnounceRouteSource based on Integer32"""
    defaultValue = 63


_WfIpBgp3AnnounceRouteSource_Object = MibTableColumn
wfIpBgp3AnnounceRouteSource = _WfIpBgp3AnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 8),
    _WfIpBgp3AnnounceRouteSource_Type()
)
wfIpBgp3AnnounceRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceRouteSource.setStatus("mandatory")


class _WfIpBgp3AnnounceExtRouteSource_Type(Integer32):
    """Custom type wfIpBgp3AnnounceExtRouteSource based on Integer32"""
    defaultValue = 63


_WfIpBgp3AnnounceExtRouteSource_Object = MibTableColumn
wfIpBgp3AnnounceExtRouteSource = _WfIpBgp3AnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 9),
    _WfIpBgp3AnnounceExtRouteSource_Type()
)
wfIpBgp3AnnounceExtRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceExtRouteSource.setStatus("mandatory")
_WfIpBgp3AnnounceAdvertise_Type = OctetString
_WfIpBgp3AnnounceAdvertise_Object = MibTableColumn
wfIpBgp3AnnounceAdvertise = _WfIpBgp3AnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 10),
    _WfIpBgp3AnnounceAdvertise_Type()
)
wfIpBgp3AnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceAdvertise.setStatus("mandatory")
_WfIpBgp3AnnounceRipGateway_Type = OctetString
_WfIpBgp3AnnounceRipGateway_Object = MibTableColumn
wfIpBgp3AnnounceRipGateway = _WfIpBgp3AnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 11),
    _WfIpBgp3AnnounceRipGateway_Type()
)
wfIpBgp3AnnounceRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceRipGateway.setStatus("mandatory")
_WfIpBgp3AnnounceRipInterface_Type = OctetString
_WfIpBgp3AnnounceRipInterface_Object = MibTableColumn
wfIpBgp3AnnounceRipInterface = _WfIpBgp3AnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 12),
    _WfIpBgp3AnnounceRipInterface_Type()
)
wfIpBgp3AnnounceRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceRipInterface.setStatus("mandatory")
_WfIpBgp3AnnounceOspfRouterId_Type = OctetString
_WfIpBgp3AnnounceOspfRouterId_Object = MibTableColumn
wfIpBgp3AnnounceOspfRouterId = _WfIpBgp3AnnounceOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 13),
    _WfIpBgp3AnnounceOspfRouterId_Type()
)
wfIpBgp3AnnounceOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceOspfRouterId.setStatus("mandatory")


class _WfIpBgp3AnnounceOspfType_Type(Integer32):
    """Custom type wfIpBgp3AnnounceOspfType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpBgp3AnnounceOspfType_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceOspfType_Object = MibTableColumn
wfIpBgp3AnnounceOspfType = _WfIpBgp3AnnounceOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 14),
    _WfIpBgp3AnnounceOspfType_Type()
)
wfIpBgp3AnnounceOspfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceOspfType.setStatus("mandatory")
_WfIpBgp3AnnounceOspfTag_Type = OctetString
_WfIpBgp3AnnounceOspfTag_Object = MibTableColumn
wfIpBgp3AnnounceOspfTag = _WfIpBgp3AnnounceOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 15),
    _WfIpBgp3AnnounceOspfTag_Type()
)
wfIpBgp3AnnounceOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceOspfTag.setStatus("mandatory")
_WfIpBgp3AnnounceEgpPeer_Type = OctetString
_WfIpBgp3AnnounceEgpPeer_Object = MibTableColumn
wfIpBgp3AnnounceEgpPeer = _WfIpBgp3AnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 16),
    _WfIpBgp3AnnounceEgpPeer_Type()
)
wfIpBgp3AnnounceEgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceEgpPeer.setStatus("mandatory")
_WfIpBgp3AnnounceEgpPeerAs_Type = OctetString
_WfIpBgp3AnnounceEgpPeerAs_Object = MibTableColumn
wfIpBgp3AnnounceEgpPeerAs = _WfIpBgp3AnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 17),
    _WfIpBgp3AnnounceEgpPeerAs_Type()
)
wfIpBgp3AnnounceEgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceEgpPeerAs.setStatus("mandatory")
_WfIpBgp3AnnounceEgpGateway_Type = OctetString
_WfIpBgp3AnnounceEgpGateway_Object = MibTableColumn
wfIpBgp3AnnounceEgpGateway = _WfIpBgp3AnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 18),
    _WfIpBgp3AnnounceEgpGateway_Type()
)
wfIpBgp3AnnounceEgpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceEgpGateway.setStatus("mandatory")
_WfIpBgp3AnnounceBgpPeer_Type = OctetString
_WfIpBgp3AnnounceBgpPeer_Object = MibTableColumn
wfIpBgp3AnnounceBgpPeer = _WfIpBgp3AnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 19),
    _WfIpBgp3AnnounceBgpPeer_Type()
)
wfIpBgp3AnnounceBgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceBgpPeer.setStatus("mandatory")
_WfIpBgp3AnnounceBgpPeerAs_Type = OctetString
_WfIpBgp3AnnounceBgpPeerAs_Object = MibTableColumn
wfIpBgp3AnnounceBgpPeerAs = _WfIpBgp3AnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 20),
    _WfIpBgp3AnnounceBgpPeerAs_Type()
)
wfIpBgp3AnnounceBgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceBgpPeerAs.setStatus("mandatory")
_WfIpBgp3AnnounceBgpNextHop_Type = OctetString
_WfIpBgp3AnnounceBgpNextHop_Object = MibTableColumn
wfIpBgp3AnnounceBgpNextHop = _WfIpBgp3AnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 21),
    _WfIpBgp3AnnounceBgpNextHop_Type()
)
wfIpBgp3AnnounceBgpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceBgpNextHop.setStatus("mandatory")
_WfIpBgp3AnnouncePeerAs_Type = OctetString
_WfIpBgp3AnnouncePeerAs_Object = MibTableColumn
wfIpBgp3AnnouncePeerAs = _WfIpBgp3AnnouncePeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 22),
    _WfIpBgp3AnnouncePeerAs_Type()
)
wfIpBgp3AnnouncePeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnouncePeerAs.setStatus("mandatory")
_WfIpBgp3AnnouncePeer_Type = OctetString
_WfIpBgp3AnnouncePeer_Object = MibTableColumn
wfIpBgp3AnnouncePeer = _WfIpBgp3AnnouncePeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 23),
    _WfIpBgp3AnnouncePeer_Type()
)
wfIpBgp3AnnouncePeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnouncePeer.setStatus("mandatory")


class _WfIpBgp3AnnounceUseMetric_Type(Integer32):
    """Custom type wfIpBgp3AnnounceUseMetric based on Integer32"""
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
        *(("none", 1),
          ("originating", 3),
          ("specified", 2))
    )


_WfIpBgp3AnnounceUseMetric_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceUseMetric_Object = MibTableColumn
wfIpBgp3AnnounceUseMetric = _WfIpBgp3AnnounceUseMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 24),
    _WfIpBgp3AnnounceUseMetric_Type()
)
wfIpBgp3AnnounceUseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceUseMetric.setStatus("mandatory")


class _WfIpBgp3AnnounceInterAsMetric_Type(Integer32):
    """Custom type wfIpBgp3AnnounceInterAsMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIpBgp3AnnounceInterAsMetric_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceInterAsMetric_Object = MibTableColumn
wfIpBgp3AnnounceInterAsMetric = _WfIpBgp3AnnounceInterAsMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 25),
    _WfIpBgp3AnnounceInterAsMetric_Type()
)
wfIpBgp3AnnounceInterAsMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceInterAsMetric.setStatus("mandatory")


class _WfIpBgp3AnnounceOrigin_Type(Integer32):
    """Custom type wfIpBgp3AnnounceOrigin based on Integer32"""
    defaultValue = 4

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
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3),
          ("none", 4))
    )


_WfIpBgp3AnnounceOrigin_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceOrigin_Object = MibTableColumn
wfIpBgp3AnnounceOrigin = _WfIpBgp3AnnounceOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 26),
    _WfIpBgp3AnnounceOrigin_Type()
)
wfIpBgp3AnnounceOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceOrigin.setStatus("mandatory")
_WfIpBgp3AnnounceAsPath_Type = OctetString
_WfIpBgp3AnnounceAsPath_Object = MibTableColumn
wfIpBgp3AnnounceAsPath = _WfIpBgp3AnnounceAsPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 27),
    _WfIpBgp3AnnounceAsPath_Type()
)
wfIpBgp3AnnounceAsPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceAsPath.setStatus("mandatory")
_WfIpBgp3AnnounceNextHop_Type = IpAddress
_WfIpBgp3AnnounceNextHop_Object = MibTableColumn
wfIpBgp3AnnounceNextHop = _WfIpBgp3AnnounceNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 28),
    _WfIpBgp3AnnounceNextHop_Type()
)
wfIpBgp3AnnounceNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceNextHop.setStatus("mandatory")
_WfIpBgp3AnnounceCommunity_Type = OctetString
_WfIpBgp3AnnounceCommunity_Object = MibTableColumn
wfIpBgp3AnnounceCommunity = _WfIpBgp3AnnounceCommunity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 29),
    _WfIpBgp3AnnounceCommunity_Type()
)
wfIpBgp3AnnounceCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceCommunity.setStatus("mandatory")


class _WfIpBgp3AnnounceCommunityAction_Type(Integer32):
    """Custom type wfIpBgp3AnnounceCommunityAction based on Integer32"""
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
        *(("append", 3),
          ("as-is", 1),
          ("remove", 2),
          ("replace", 4))
    )


_WfIpBgp3AnnounceCommunityAction_Type.__name__ = "Integer32"
_WfIpBgp3AnnounceCommunityAction_Object = MibTableColumn
wfIpBgp3AnnounceCommunityAction = _WfIpBgp3AnnounceCommunityAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 30),
    _WfIpBgp3AnnounceCommunityAction_Type()
)
wfIpBgp3AnnounceCommunityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceCommunityAction.setStatus("mandatory")
_WfIpBgp3AnnounceCommunityMatch_Type = OctetString
_WfIpBgp3AnnounceCommunityMatch_Object = MibTableColumn
wfIpBgp3AnnounceCommunityMatch = _WfIpBgp3AnnounceCommunityMatch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 8, 1, 31),
    _WfIpBgp3AnnounceCommunityMatch_Type()
)
wfIpBgp3AnnounceCommunityMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp3AnnounceCommunityMatch.setStatus("mandatory")
_WfIpBgp4AcceptTable_Object = MibTable
wfIpBgp4AcceptTable = _WfIpBgp4AcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9)
)
if mibBuilder.loadTexts:
    wfIpBgp4AcceptTable.setStatus("mandatory")
_WfIpBgp4AcceptEntry_Object = MibTableRow
wfIpBgp4AcceptEntry = _WfIpBgp4AcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1)
)
wfIpBgp4AcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpBgp4AcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpBgp4AcceptEntry.setStatus("mandatory")


class _WfIpBgp4AcceptDelete_Type(Integer32):
    """Custom type wfIpBgp4AcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpBgp4AcceptDelete_Type.__name__ = "Integer32"
_WfIpBgp4AcceptDelete_Object = MibTableColumn
wfIpBgp4AcceptDelete = _WfIpBgp4AcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 1),
    _WfIpBgp4AcceptDelete_Type()
)
wfIpBgp4AcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptDelete.setStatus("mandatory")


class _WfIpBgp4AcceptDisable_Type(Integer32):
    """Custom type wfIpBgp4AcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpBgp4AcceptDisable_Type.__name__ = "Integer32"
_WfIpBgp4AcceptDisable_Object = MibTableColumn
wfIpBgp4AcceptDisable = _WfIpBgp4AcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 2),
    _WfIpBgp4AcceptDisable_Type()
)
wfIpBgp4AcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptDisable.setStatus("mandatory")
_WfIpBgp4AcceptIndex_Type = Integer32
_WfIpBgp4AcceptIndex_Object = MibTableColumn
wfIpBgp4AcceptIndex = _WfIpBgp4AcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 3),
    _WfIpBgp4AcceptIndex_Type()
)
wfIpBgp4AcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptIndex.setStatus("mandatory")
_WfIpBgp4AcceptName_Type = DisplayString
_WfIpBgp4AcceptName_Object = MibTableColumn
wfIpBgp4AcceptName = _WfIpBgp4AcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 4),
    _WfIpBgp4AcceptName_Type()
)
wfIpBgp4AcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptName.setStatus("mandatory")
_WfIpBgp4AcceptNetworks_Type = OctetString
_WfIpBgp4AcceptNetworks_Object = MibTableColumn
wfIpBgp4AcceptNetworks = _WfIpBgp4AcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 5),
    _WfIpBgp4AcceptNetworks_Type()
)
wfIpBgp4AcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptNetworks.setStatus("mandatory")


class _WfIpBgp4AcceptAction_Type(Integer32):
    """Custom type wfIpBgp4AcceptAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpBgp4AcceptAction_Type.__name__ = "Integer32"
_WfIpBgp4AcceptAction_Object = MibTableColumn
wfIpBgp4AcceptAction = _WfIpBgp4AcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 6),
    _WfIpBgp4AcceptAction_Type()
)
wfIpBgp4AcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptAction.setStatus("mandatory")


class _WfIpBgp4AcceptPreference_Type(Integer32):
    """Custom type wfIpBgp4AcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpBgp4AcceptPreference_Type.__name__ = "Integer32"
_WfIpBgp4AcceptPreference_Object = MibTableColumn
wfIpBgp4AcceptPreference = _WfIpBgp4AcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 7),
    _WfIpBgp4AcceptPreference_Type()
)
wfIpBgp4AcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptPreference.setStatus("mandatory")
_WfIpBgp4AcceptPrecedence_Type = Integer32
_WfIpBgp4AcceptPrecedence_Object = MibTableColumn
wfIpBgp4AcceptPrecedence = _WfIpBgp4AcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 8),
    _WfIpBgp4AcceptPrecedence_Type()
)
wfIpBgp4AcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptPrecedence.setStatus("mandatory")
_WfIpBgp4AcceptInject_Type = OctetString
_WfIpBgp4AcceptInject_Object = MibTableColumn
wfIpBgp4AcceptInject = _WfIpBgp4AcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 9),
    _WfIpBgp4AcceptInject_Type()
)
wfIpBgp4AcceptInject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptInject.setStatus("mandatory")
_WfIpBgp4AcceptPeerAs_Type = OctetString
_WfIpBgp4AcceptPeerAs_Object = MibTableColumn
wfIpBgp4AcceptPeerAs = _WfIpBgp4AcceptPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 10),
    _WfIpBgp4AcceptPeerAs_Type()
)
wfIpBgp4AcceptPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptPeerAs.setStatus("mandatory")
_WfIpBgp4AcceptPeerAddress_Type = OctetString
_WfIpBgp4AcceptPeerAddress_Object = MibTableColumn
wfIpBgp4AcceptPeerAddress = _WfIpBgp4AcceptPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 11),
    _WfIpBgp4AcceptPeerAddress_Type()
)
wfIpBgp4AcceptPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptPeerAddress.setStatus("mandatory")
_WfIpBgp4AcceptOrigAs_Type = OctetString
_WfIpBgp4AcceptOrigAs_Object = MibTableColumn
wfIpBgp4AcceptOrigAs = _WfIpBgp4AcceptOrigAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 12),
    _WfIpBgp4AcceptOrigAs_Type()
)
wfIpBgp4AcceptOrigAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptOrigAs.setStatus("mandatory")


class _WfIpBgp4AcceptRouteOrigin_Type(Integer32):
    """Custom type wfIpBgp4AcceptRouteOrigin based on Integer32"""
    defaultValue = 7

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
        *(("any", 7),
          ("egp", 2),
          ("igp", 1),
          ("igporegp", 3),
          ("incomplete", 4),
          ("incompleteoregp", 6),
          ("incompleteorigp", 5))
    )


_WfIpBgp4AcceptRouteOrigin_Type.__name__ = "Integer32"
_WfIpBgp4AcceptRouteOrigin_Object = MibTableColumn
wfIpBgp4AcceptRouteOrigin = _WfIpBgp4AcceptRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 13),
    _WfIpBgp4AcceptRouteOrigin_Type()
)
wfIpBgp4AcceptRouteOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptRouteOrigin.setStatus("mandatory")
_WfIpBgp4AcceptAggrAs_Type = OctetString
_WfIpBgp4AcceptAggrAs_Object = MibTableColumn
wfIpBgp4AcceptAggrAs = _WfIpBgp4AcceptAggrAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 14),
    _WfIpBgp4AcceptAggrAs_Type()
)
wfIpBgp4AcceptAggrAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptAggrAs.setStatus("mandatory")
_WfIpBgp4AcceptAggrRouter_Type = OctetString
_WfIpBgp4AcceptAggrRouter_Object = MibTableColumn
wfIpBgp4AcceptAggrRouter = _WfIpBgp4AcceptAggrRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 15),
    _WfIpBgp4AcceptAggrRouter_Type()
)
wfIpBgp4AcceptAggrRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptAggrRouter.setStatus("mandatory")
_WfIpBgp4AcceptLocalPref_Type = Integer32
_WfIpBgp4AcceptLocalPref_Object = MibTableColumn
wfIpBgp4AcceptLocalPref = _WfIpBgp4AcceptLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 16),
    _WfIpBgp4AcceptLocalPref_Type()
)
wfIpBgp4AcceptLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptLocalPref.setStatus("mandatory")


class _WfIpBgp4AcceptBgp4Preference_Type(Integer32):
    """Custom type wfIpBgp4AcceptBgp4Preference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfIpBgp4AcceptBgp4Preference_Type.__name__ = "Integer32"
_WfIpBgp4AcceptBgp4Preference_Object = MibTableColumn
wfIpBgp4AcceptBgp4Preference = _WfIpBgp4AcceptBgp4Preference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 17),
    _WfIpBgp4AcceptBgp4Preference_Type()
)
wfIpBgp4AcceptBgp4Preference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptBgp4Preference.setStatus("mandatory")


class _WfIpBgp4AcceptAsWeightClass_Type(Integer32):
    """Custom type wfIpBgp4AcceptAsWeightClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5),
          ("class6", 6),
          ("class7", 7),
          ("class8", 8))
    )


_WfIpBgp4AcceptAsWeightClass_Type.__name__ = "Integer32"
_WfIpBgp4AcceptAsWeightClass_Object = MibTableColumn
wfIpBgp4AcceptAsWeightClass = _WfIpBgp4AcceptAsWeightClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 18),
    _WfIpBgp4AcceptAsWeightClass_Type()
)
wfIpBgp4AcceptAsWeightClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptAsWeightClass.setStatus("mandatory")
_WfIpBgp4AcceptAsPatternMatch_Type = DisplayString
_WfIpBgp4AcceptAsPatternMatch_Object = MibTableColumn
wfIpBgp4AcceptAsPatternMatch = _WfIpBgp4AcceptAsPatternMatch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 19),
    _WfIpBgp4AcceptAsPatternMatch_Type()
)
wfIpBgp4AcceptAsPatternMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptAsPatternMatch.setStatus("mandatory")
_WfIpBgp4AcceptCommunityMatch_Type = OctetString
_WfIpBgp4AcceptCommunityMatch_Object = MibTableColumn
wfIpBgp4AcceptCommunityMatch = _WfIpBgp4AcceptCommunityMatch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 20),
    _WfIpBgp4AcceptCommunityMatch_Type()
)
wfIpBgp4AcceptCommunityMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptCommunityMatch.setStatus("mandatory")


class _WfIpBgp4AcceptUseMultiExitDisc_Type(Integer32):
    """Custom type wfIpBgp4AcceptUseMultiExitDisc based on Integer32"""
    defaultValue = 1

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
        *(("delete", 4),
          ("generate", 3),
          ("override", 2),
          ("passthru", 1))
    )


_WfIpBgp4AcceptUseMultiExitDisc_Type.__name__ = "Integer32"
_WfIpBgp4AcceptUseMultiExitDisc_Object = MibTableColumn
wfIpBgp4AcceptUseMultiExitDisc = _WfIpBgp4AcceptUseMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 21),
    _WfIpBgp4AcceptUseMultiExitDisc_Type()
)
wfIpBgp4AcceptUseMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptUseMultiExitDisc.setStatus("mandatory")


class _WfIpBgp4AcceptMultiExitDisc_Type(Integer32):
    """Custom type wfIpBgp4AcceptMultiExitDisc based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_WfIpBgp4AcceptMultiExitDisc_Type.__name__ = "Integer32"
_WfIpBgp4AcceptMultiExitDisc_Object = MibTableColumn
wfIpBgp4AcceptMultiExitDisc = _WfIpBgp4AcceptMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 22),
    _WfIpBgp4AcceptMultiExitDisc_Type()
)
wfIpBgp4AcceptMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptMultiExitDisc.setStatus("mandatory")
_WfIpBgp4AcceptAsPrepend_Type = OctetString
_WfIpBgp4AcceptAsPrepend_Object = MibTableColumn
wfIpBgp4AcceptAsPrepend = _WfIpBgp4AcceptAsPrepend_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 23),
    _WfIpBgp4AcceptAsPrepend_Type()
)
wfIpBgp4AcceptAsPrepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptAsPrepend.setStatus("mandatory")
_WfIpBgp4AcceptCommunity_Type = OctetString
_WfIpBgp4AcceptCommunity_Object = MibTableColumn
wfIpBgp4AcceptCommunity = _WfIpBgp4AcceptCommunity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 24),
    _WfIpBgp4AcceptCommunity_Type()
)
wfIpBgp4AcceptCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptCommunity.setStatus("mandatory")


class _WfIpBgp4AcceptCommunityAction_Type(Integer32):
    """Custom type wfIpBgp4AcceptCommunityAction based on Integer32"""
    defaultValue = 1

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
        *(("append", 3),
          ("as-is", 1),
          ("remove", 2),
          ("replace", 4))
    )


_WfIpBgp4AcceptCommunityAction_Type.__name__ = "Integer32"
_WfIpBgp4AcceptCommunityAction_Object = MibTableColumn
wfIpBgp4AcceptCommunityAction = _WfIpBgp4AcceptCommunityAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 25),
    _WfIpBgp4AcceptCommunityAction_Type()
)
wfIpBgp4AcceptCommunityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptCommunityAction.setStatus("mandatory")


class _WfIpBgp4AcceptRFDampeningEnable_Type(Integer32):
    """Custom type wfIpBgp4AcceptRFDampeningEnable based on Integer32"""
    defaultValue = 2

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


_WfIpBgp4AcceptRFDampeningEnable_Type.__name__ = "Integer32"
_WfIpBgp4AcceptRFDampeningEnable_Object = MibTableColumn
wfIpBgp4AcceptRFDampeningEnable = _WfIpBgp4AcceptRFDampeningEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 26),
    _WfIpBgp4AcceptRFDampeningEnable_Type()
)
wfIpBgp4AcceptRFDampeningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptRFDampeningEnable.setStatus("mandatory")


class _WfIpBgp4AcceptRFDampeningTemplate_Type(Integer32):
    """Custom type wfIpBgp4AcceptRFDampeningTemplate based on Integer32"""
    defaultValue = 1


_WfIpBgp4AcceptRFDampeningTemplate_Object = MibTableColumn
wfIpBgp4AcceptRFDampeningTemplate = _WfIpBgp4AcceptRFDampeningTemplate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 9, 1, 27),
    _WfIpBgp4AcceptRFDampeningTemplate_Type()
)
wfIpBgp4AcceptRFDampeningTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AcceptRFDampeningTemplate.setStatus("mandatory")
_WfIpBgp4AnnounceTable_Object = MibTable
wfIpBgp4AnnounceTable = _WfIpBgp4AnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10)
)
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceTable.setStatus("mandatory")
_WfIpBgp4AnnounceEntry_Object = MibTableRow
wfIpBgp4AnnounceEntry = _WfIpBgp4AnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1)
)
wfIpBgp4AnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpBgp4AnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceEntry.setStatus("mandatory")


class _WfIpBgp4AnnounceDelete_Type(Integer32):
    """Custom type wfIpBgp4AnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpBgp4AnnounceDelete_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceDelete_Object = MibTableColumn
wfIpBgp4AnnounceDelete = _WfIpBgp4AnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 1),
    _WfIpBgp4AnnounceDelete_Type()
)
wfIpBgp4AnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceDelete.setStatus("mandatory")


class _WfIpBgp4AnnounceDisable_Type(Integer32):
    """Custom type wfIpBgp4AnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpBgp4AnnounceDisable_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceDisable_Object = MibTableColumn
wfIpBgp4AnnounceDisable = _WfIpBgp4AnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 2),
    _WfIpBgp4AnnounceDisable_Type()
)
wfIpBgp4AnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceDisable.setStatus("mandatory")
_WfIpBgp4AnnounceIndex_Type = Integer32
_WfIpBgp4AnnounceIndex_Object = MibTableColumn
wfIpBgp4AnnounceIndex = _WfIpBgp4AnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 3),
    _WfIpBgp4AnnounceIndex_Type()
)
wfIpBgp4AnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceIndex.setStatus("mandatory")
_WfIpBgp4AnnounceName_Type = DisplayString
_WfIpBgp4AnnounceName_Object = MibTableColumn
wfIpBgp4AnnounceName = _WfIpBgp4AnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 4),
    _WfIpBgp4AnnounceName_Type()
)
wfIpBgp4AnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceName.setStatus("mandatory")
_WfIpBgp4AnnounceNetworks_Type = OctetString
_WfIpBgp4AnnounceNetworks_Object = MibTableColumn
wfIpBgp4AnnounceNetworks = _WfIpBgp4AnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 5),
    _WfIpBgp4AnnounceNetworks_Type()
)
wfIpBgp4AnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceNetworks.setStatus("mandatory")


class _WfIpBgp4AnnounceAction_Type(Integer32):
    """Custom type wfIpBgp4AnnounceAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpBgp4AnnounceAction_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceAction_Object = MibTableColumn
wfIpBgp4AnnounceAction = _WfIpBgp4AnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 6),
    _WfIpBgp4AnnounceAction_Type()
)
wfIpBgp4AnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceAction.setStatus("mandatory")
_WfIpBgp4AnnouncePrecedence_Type = Integer32
_WfIpBgp4AnnouncePrecedence_Object = MibTableColumn
wfIpBgp4AnnouncePrecedence = _WfIpBgp4AnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 7),
    _WfIpBgp4AnnouncePrecedence_Type()
)
wfIpBgp4AnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnouncePrecedence.setStatus("mandatory")


class _WfIpBgp4AnnounceRouteSource_Type(Integer32):
    """Custom type wfIpBgp4AnnounceRouteSource based on Integer32"""
    defaultValue = 63


_WfIpBgp4AnnounceRouteSource_Object = MibTableColumn
wfIpBgp4AnnounceRouteSource = _WfIpBgp4AnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 8),
    _WfIpBgp4AnnounceRouteSource_Type()
)
wfIpBgp4AnnounceRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceRouteSource.setStatus("mandatory")


class _WfIpBgp4AnnounceExtRouteSource_Type(Integer32):
    """Custom type wfIpBgp4AnnounceExtRouteSource based on Integer32"""
    defaultValue = 63


_WfIpBgp4AnnounceExtRouteSource_Object = MibTableColumn
wfIpBgp4AnnounceExtRouteSource = _WfIpBgp4AnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 9),
    _WfIpBgp4AnnounceExtRouteSource_Type()
)
wfIpBgp4AnnounceExtRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceExtRouteSource.setStatus("mandatory")
_WfIpBgp4AnnounceAdvertise_Type = OctetString
_WfIpBgp4AnnounceAdvertise_Object = MibTableColumn
wfIpBgp4AnnounceAdvertise = _WfIpBgp4AnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 10),
    _WfIpBgp4AnnounceAdvertise_Type()
)
wfIpBgp4AnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceAdvertise.setStatus("mandatory")
_WfIpBgp4AnnounceRipGateway_Type = OctetString
_WfIpBgp4AnnounceRipGateway_Object = MibTableColumn
wfIpBgp4AnnounceRipGateway = _WfIpBgp4AnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 11),
    _WfIpBgp4AnnounceRipGateway_Type()
)
wfIpBgp4AnnounceRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceRipGateway.setStatus("mandatory")
_WfIpBgp4AnnounceRipInterface_Type = OctetString
_WfIpBgp4AnnounceRipInterface_Object = MibTableColumn
wfIpBgp4AnnounceRipInterface = _WfIpBgp4AnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 12),
    _WfIpBgp4AnnounceRipInterface_Type()
)
wfIpBgp4AnnounceRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceRipInterface.setStatus("mandatory")
_WfIpBgp4AnnounceOspfRouterId_Type = OctetString
_WfIpBgp4AnnounceOspfRouterId_Object = MibTableColumn
wfIpBgp4AnnounceOspfRouterId = _WfIpBgp4AnnounceOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 13),
    _WfIpBgp4AnnounceOspfRouterId_Type()
)
wfIpBgp4AnnounceOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceOspfRouterId.setStatus("mandatory")


class _WfIpBgp4AnnounceOspfType_Type(Integer32):
    """Custom type wfIpBgp4AnnounceOspfType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpBgp4AnnounceOspfType_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceOspfType_Object = MibTableColumn
wfIpBgp4AnnounceOspfType = _WfIpBgp4AnnounceOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 14),
    _WfIpBgp4AnnounceOspfType_Type()
)
wfIpBgp4AnnounceOspfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceOspfType.setStatus("mandatory")
_WfIpBgp4AnnounceOspfTag_Type = OctetString
_WfIpBgp4AnnounceOspfTag_Object = MibTableColumn
wfIpBgp4AnnounceOspfTag = _WfIpBgp4AnnounceOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 15),
    _WfIpBgp4AnnounceOspfTag_Type()
)
wfIpBgp4AnnounceOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceOspfTag.setStatus("mandatory")
_WfIpBgp4AnnounceEgpPeer_Type = OctetString
_WfIpBgp4AnnounceEgpPeer_Object = MibTableColumn
wfIpBgp4AnnounceEgpPeer = _WfIpBgp4AnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 16),
    _WfIpBgp4AnnounceEgpPeer_Type()
)
wfIpBgp4AnnounceEgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceEgpPeer.setStatus("mandatory")
_WfIpBgp4AnnounceEgpPeerAs_Type = OctetString
_WfIpBgp4AnnounceEgpPeerAs_Object = MibTableColumn
wfIpBgp4AnnounceEgpPeerAs = _WfIpBgp4AnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 17),
    _WfIpBgp4AnnounceEgpPeerAs_Type()
)
wfIpBgp4AnnounceEgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceEgpPeerAs.setStatus("mandatory")
_WfIpBgp4AnnounceEgpGateway_Type = OctetString
_WfIpBgp4AnnounceEgpGateway_Object = MibTableColumn
wfIpBgp4AnnounceEgpGateway = _WfIpBgp4AnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 18),
    _WfIpBgp4AnnounceEgpGateway_Type()
)
wfIpBgp4AnnounceEgpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceEgpGateway.setStatus("mandatory")
_WfIpBgp4AnnounceBgpPeer_Type = OctetString
_WfIpBgp4AnnounceBgpPeer_Object = MibTableColumn
wfIpBgp4AnnounceBgpPeer = _WfIpBgp4AnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 19),
    _WfIpBgp4AnnounceBgpPeer_Type()
)
wfIpBgp4AnnounceBgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceBgpPeer.setStatus("mandatory")
_WfIpBgp4AnnounceBgpPeerAs_Type = OctetString
_WfIpBgp4AnnounceBgpPeerAs_Object = MibTableColumn
wfIpBgp4AnnounceBgpPeerAs = _WfIpBgp4AnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 20),
    _WfIpBgp4AnnounceBgpPeerAs_Type()
)
wfIpBgp4AnnounceBgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceBgpPeerAs.setStatus("mandatory")
_WfIpBgp4AnnounceBgpNextHop_Type = OctetString
_WfIpBgp4AnnounceBgpNextHop_Object = MibTableColumn
wfIpBgp4AnnounceBgpNextHop = _WfIpBgp4AnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 21),
    _WfIpBgp4AnnounceBgpNextHop_Type()
)
wfIpBgp4AnnounceBgpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceBgpNextHop.setStatus("mandatory")
_WfIpBgp4AnnouncePeerAs_Type = OctetString
_WfIpBgp4AnnouncePeerAs_Object = MibTableColumn
wfIpBgp4AnnouncePeerAs = _WfIpBgp4AnnouncePeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 22),
    _WfIpBgp4AnnouncePeerAs_Type()
)
wfIpBgp4AnnouncePeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnouncePeerAs.setStatus("mandatory")
_WfIpBgp4AnnouncePeer_Type = OctetString
_WfIpBgp4AnnouncePeer_Object = MibTableColumn
wfIpBgp4AnnouncePeer = _WfIpBgp4AnnouncePeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 23),
    _WfIpBgp4AnnouncePeer_Type()
)
wfIpBgp4AnnouncePeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnouncePeer.setStatus("mandatory")


class _WfIpBgp4AnnounceUseMultiExitDisc_Type(Integer32):
    """Custom type wfIpBgp4AnnounceUseMultiExitDisc based on Integer32"""
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
        *(("none", 1),
          ("originating", 3),
          ("specified", 2))
    )


_WfIpBgp4AnnounceUseMultiExitDisc_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceUseMultiExitDisc_Object = MibTableColumn
wfIpBgp4AnnounceUseMultiExitDisc = _WfIpBgp4AnnounceUseMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 24),
    _WfIpBgp4AnnounceUseMultiExitDisc_Type()
)
wfIpBgp4AnnounceUseMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceUseMultiExitDisc.setStatus("mandatory")


class _WfIpBgp4AnnounceMultiExitDisc_Type(Integer32):
    """Custom type wfIpBgp4AnnounceMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIpBgp4AnnounceMultiExitDisc_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceMultiExitDisc_Object = MibTableColumn
wfIpBgp4AnnounceMultiExitDisc = _WfIpBgp4AnnounceMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 25),
    _WfIpBgp4AnnounceMultiExitDisc_Type()
)
wfIpBgp4AnnounceMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceMultiExitDisc.setStatus("mandatory")


class _WfIpBgp4AnnounceOrigin_Type(Integer32):
    """Custom type wfIpBgp4AnnounceOrigin based on Integer32"""
    defaultValue = 4

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
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3),
          ("none", 4))
    )


_WfIpBgp4AnnounceOrigin_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceOrigin_Object = MibTableColumn
wfIpBgp4AnnounceOrigin = _WfIpBgp4AnnounceOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 26),
    _WfIpBgp4AnnounceOrigin_Type()
)
wfIpBgp4AnnounceOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceOrigin.setStatus("mandatory")
_WfIpBgp4AnnounceAsPath_Type = OctetString
_WfIpBgp4AnnounceAsPath_Object = MibTableColumn
wfIpBgp4AnnounceAsPath = _WfIpBgp4AnnounceAsPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 27),
    _WfIpBgp4AnnounceAsPath_Type()
)
wfIpBgp4AnnounceAsPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceAsPath.setStatus("mandatory")


class _WfIpBgp4AnnounceLocalPrefOverride_Type(Integer32):
    """Custom type wfIpBgp4AnnounceLocalPrefOverride based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfIpBgp4AnnounceLocalPrefOverride_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceLocalPrefOverride_Object = MibTableColumn
wfIpBgp4AnnounceLocalPrefOverride = _WfIpBgp4AnnounceLocalPrefOverride_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 28),
    _WfIpBgp4AnnounceLocalPrefOverride_Type()
)
wfIpBgp4AnnounceLocalPrefOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceLocalPrefOverride.setStatus("mandatory")
_WfIpBgp4AnnounceLocalPref_Type = Integer32
_WfIpBgp4AnnounceLocalPref_Object = MibTableColumn
wfIpBgp4AnnounceLocalPref = _WfIpBgp4AnnounceLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 29),
    _WfIpBgp4AnnounceLocalPref_Type()
)
wfIpBgp4AnnounceLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceLocalPref.setStatus("mandatory")
_WfIpBgp4AnnounceNextHop_Type = IpAddress
_WfIpBgp4AnnounceNextHop_Object = MibTableColumn
wfIpBgp4AnnounceNextHop = _WfIpBgp4AnnounceNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 30),
    _WfIpBgp4AnnounceNextHop_Type()
)
wfIpBgp4AnnounceNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceNextHop.setStatus("mandatory")


class _WfIpBgp4AnnounceAtomic_Type(Integer32):
    """Custom type wfIpBgp4AnnounceAtomic based on Integer32"""
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
        *(("default", 1),
          ("force", 2),
          ("ignore", 3))
    )


_WfIpBgp4AnnounceAtomic_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceAtomic_Object = MibTableColumn
wfIpBgp4AnnounceAtomic = _WfIpBgp4AnnounceAtomic_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 31),
    _WfIpBgp4AnnounceAtomic_Type()
)
wfIpBgp4AnnounceAtomic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceAtomic.setStatus("mandatory")
_WfIpBgp4AnnounceAsPatternMatch_Type = DisplayString
_WfIpBgp4AnnounceAsPatternMatch_Object = MibTableColumn
wfIpBgp4AnnounceAsPatternMatch = _WfIpBgp4AnnounceAsPatternMatch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 32),
    _WfIpBgp4AnnounceAsPatternMatch_Type()
)
wfIpBgp4AnnounceAsPatternMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceAsPatternMatch.setStatus("mandatory")
_WfIpBgp4AnnounceCommunity_Type = OctetString
_WfIpBgp4AnnounceCommunity_Object = MibTableColumn
wfIpBgp4AnnounceCommunity = _WfIpBgp4AnnounceCommunity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 33),
    _WfIpBgp4AnnounceCommunity_Type()
)
wfIpBgp4AnnounceCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceCommunity.setStatus("mandatory")


class _WfIpBgp4AnnounceCommunityAction_Type(Integer32):
    """Custom type wfIpBgp4AnnounceCommunityAction based on Integer32"""
    defaultValue = 1

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
        *(("append", 3),
          ("as-is", 1),
          ("remove", 2),
          ("replace", 4))
    )


_WfIpBgp4AnnounceCommunityAction_Type.__name__ = "Integer32"
_WfIpBgp4AnnounceCommunityAction_Object = MibTableColumn
wfIpBgp4AnnounceCommunityAction = _WfIpBgp4AnnounceCommunityAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 34),
    _WfIpBgp4AnnounceCommunityAction_Type()
)
wfIpBgp4AnnounceCommunityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceCommunityAction.setStatus("mandatory")
_WfIpBgp4AnnounceCommunityMatch_Type = OctetString
_WfIpBgp4AnnounceCommunityMatch_Object = MibTableColumn
wfIpBgp4AnnounceCommunityMatch = _WfIpBgp4AnnounceCommunityMatch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 35),
    _WfIpBgp4AnnounceCommunityMatch_Type()
)
wfIpBgp4AnnounceCommunityMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceCommunityMatch.setStatus("mandatory")
_WfIpBgp4AnnounceAsPrepend_Type = OctetString
_WfIpBgp4AnnounceAsPrepend_Object = MibTableColumn
wfIpBgp4AnnounceAsPrepend = _WfIpBgp4AnnounceAsPrepend_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 10, 1, 36),
    _WfIpBgp4AnnounceAsPrepend_Type()
)
wfIpBgp4AnnounceAsPrepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBgp4AnnounceAsPrepend.setStatus("mandatory")
_WfIpIgmpGroupPolicyTable_Object = MibTable
wfIpIgmpGroupPolicyTable = _WfIpIgmpGroupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11)
)
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyTable.setStatus("mandatory")
_WfIpIgmpGroupPolicyEntry_Object = MibTableRow
wfIpIgmpGroupPolicyEntry = _WfIpIgmpGroupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1)
)
wfIpIgmpGroupPolicyEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpIgmpGroupPolicyIndex"),
)
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyEntry.setStatus("mandatory")


class _WfIpIgmpGroupPolicyDelete_Type(Integer32):
    """Custom type wfIpIgmpGroupPolicyDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpIgmpGroupPolicyDelete_Type.__name__ = "Integer32"
_WfIpIgmpGroupPolicyDelete_Object = MibTableColumn
wfIpIgmpGroupPolicyDelete = _WfIpIgmpGroupPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 1),
    _WfIpIgmpGroupPolicyDelete_Type()
)
wfIpIgmpGroupPolicyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyDelete.setStatus("mandatory")


class _WfIpIgmpGroupPolicyDisable_Type(Integer32):
    """Custom type wfIpIgmpGroupPolicyDisable based on Integer32"""
    defaultValue = 1

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


_WfIpIgmpGroupPolicyDisable_Type.__name__ = "Integer32"
_WfIpIgmpGroupPolicyDisable_Object = MibTableColumn
wfIpIgmpGroupPolicyDisable = _WfIpIgmpGroupPolicyDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 2),
    _WfIpIgmpGroupPolicyDisable_Type()
)
wfIpIgmpGroupPolicyDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyDisable.setStatus("mandatory")
_WfIpIgmpGroupPolicyIndex_Type = Integer32
_WfIpIgmpGroupPolicyIndex_Object = MibTableColumn
wfIpIgmpGroupPolicyIndex = _WfIpIgmpGroupPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 3),
    _WfIpIgmpGroupPolicyIndex_Type()
)
wfIpIgmpGroupPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyIndex.setStatus("mandatory")
_WfIpIgmpGroupPolicyName_Type = DisplayString
_WfIpIgmpGroupPolicyName_Object = MibTableColumn
wfIpIgmpGroupPolicyName = _WfIpIgmpGroupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 4),
    _WfIpIgmpGroupPolicyName_Type()
)
wfIpIgmpGroupPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyName.setStatus("mandatory")
_WfIpIgmpGroupPolicySources_Type = OctetString
_WfIpIgmpGroupPolicySources_Object = MibTableColumn
wfIpIgmpGroupPolicySources = _WfIpIgmpGroupPolicySources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 5),
    _WfIpIgmpGroupPolicySources_Type()
)
wfIpIgmpGroupPolicySources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicySources.setStatus("mandatory")


class _WfIpIgmpGroupPolicyAction_Type(Integer32):
    """Custom type wfIpIgmpGroupPolicyAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpIgmpGroupPolicyAction_Type.__name__ = "Integer32"
_WfIpIgmpGroupPolicyAction_Object = MibTableColumn
wfIpIgmpGroupPolicyAction = _WfIpIgmpGroupPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 6),
    _WfIpIgmpGroupPolicyAction_Type()
)
wfIpIgmpGroupPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyAction.setStatus("mandatory")


class _WfIpIgmpGroupPolicyPreference_Type(Integer32):
    """Custom type wfIpIgmpGroupPolicyPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpIgmpGroupPolicyPreference_Type.__name__ = "Integer32"
_WfIpIgmpGroupPolicyPreference_Object = MibTableColumn
wfIpIgmpGroupPolicyPreference = _WfIpIgmpGroupPolicyPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 7),
    _WfIpIgmpGroupPolicyPreference_Type()
)
wfIpIgmpGroupPolicyPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyPreference.setStatus("mandatory")
_WfIpIgmpGroupPolicyPrecedence_Type = Integer32
_WfIpIgmpGroupPolicyPrecedence_Object = MibTableColumn
wfIpIgmpGroupPolicyPrecedence = _WfIpIgmpGroupPolicyPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 8),
    _WfIpIgmpGroupPolicyPrecedence_Type()
)
wfIpIgmpGroupPolicyPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyPrecedence.setStatus("mandatory")
_WfIpIgmpGroupPolicyInject_Type = OctetString
_WfIpIgmpGroupPolicyInject_Object = MibTableColumn
wfIpIgmpGroupPolicyInject = _WfIpIgmpGroupPolicyInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 9),
    _WfIpIgmpGroupPolicyInject_Type()
)
wfIpIgmpGroupPolicyInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyInject.setStatus("mandatory")
_WfIpIgmpGroupPolicyGroups_Type = OctetString
_WfIpIgmpGroupPolicyGroups_Object = MibTableColumn
wfIpIgmpGroupPolicyGroups = _WfIpIgmpGroupPolicyGroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 10),
    _WfIpIgmpGroupPolicyGroups_Type()
)
wfIpIgmpGroupPolicyGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyGroups.setStatus("mandatory")
_WfIpIgmpGroupPolicyCircuits_Type = OctetString
_WfIpIgmpGroupPolicyCircuits_Object = MibTableColumn
wfIpIgmpGroupPolicyCircuits = _WfIpIgmpGroupPolicyCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 11),
    _WfIpIgmpGroupPolicyCircuits_Type()
)
wfIpIgmpGroupPolicyCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicyCircuits.setStatus("mandatory")
_WfIpIgmpGroupPolicySenders_Type = OctetString
_WfIpIgmpGroupPolicySenders_Object = MibTableColumn
wfIpIgmpGroupPolicySenders = _WfIpIgmpGroupPolicySenders_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 11, 1, 12),
    _WfIpIgmpGroupPolicySenders_Type()
)
wfIpIgmpGroupPolicySenders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIgmpGroupPolicySenders.setStatus("mandatory")
_WfMTMStaticFwdTable_Object = MibTable
wfMTMStaticFwdTable = _WfMTMStaticFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12)
)
if mibBuilder.loadTexts:
    wfMTMStaticFwdTable.setStatus("obsolete")
_WfMTMStaticFwdEntry_Object = MibTableRow
wfMTMStaticFwdEntry = _WfMTMStaticFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1)
)
wfMTMStaticFwdEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfMTMStaticFwdIndex"),
)
if mibBuilder.loadTexts:
    wfMTMStaticFwdEntry.setStatus("obsolete")


class _WfMTMStaticFwdDelete_Type(Integer32):
    """Custom type wfMTMStaticFwdDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfMTMStaticFwdDelete_Type.__name__ = "Integer32"
_WfMTMStaticFwdDelete_Object = MibTableColumn
wfMTMStaticFwdDelete = _WfMTMStaticFwdDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 1),
    _WfMTMStaticFwdDelete_Type()
)
wfMTMStaticFwdDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdDelete.setStatus("obsolete")


class _WfMTMStaticFwdDisable_Type(Integer32):
    """Custom type wfMTMStaticFwdDisable based on Integer32"""
    defaultValue = 1

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


_WfMTMStaticFwdDisable_Type.__name__ = "Integer32"
_WfMTMStaticFwdDisable_Object = MibTableColumn
wfMTMStaticFwdDisable = _WfMTMStaticFwdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 2),
    _WfMTMStaticFwdDisable_Type()
)
wfMTMStaticFwdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdDisable.setStatus("obsolete")
_WfMTMStaticFwdIndex_Type = Integer32
_WfMTMStaticFwdIndex_Object = MibTableColumn
wfMTMStaticFwdIndex = _WfMTMStaticFwdIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 3),
    _WfMTMStaticFwdIndex_Type()
)
wfMTMStaticFwdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMTMStaticFwdIndex.setStatus("obsolete")
_WfMTMStaticFwdName_Type = DisplayString
_WfMTMStaticFwdName_Object = MibTableColumn
wfMTMStaticFwdName = _WfMTMStaticFwdName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 4),
    _WfMTMStaticFwdName_Type()
)
wfMTMStaticFwdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdName.setStatus("obsolete")
_WfMTMStaticFwdGroups_Type = OctetString
_WfMTMStaticFwdGroups_Object = MibTableColumn
wfMTMStaticFwdGroups = _WfMTMStaticFwdGroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 5),
    _WfMTMStaticFwdGroups_Type()
)
wfMTMStaticFwdGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdGroups.setStatus("obsolete")
_WfMTMStaticFwdAction_Type = Integer32
_WfMTMStaticFwdAction_Object = MibTableColumn
wfMTMStaticFwdAction = _WfMTMStaticFwdAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 6),
    _WfMTMStaticFwdAction_Type()
)
wfMTMStaticFwdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMTMStaticFwdAction.setStatus("obsolete")


class _WfMTMStaticFwdPreference_Type(Integer32):
    """Custom type wfMTMStaticFwdPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfMTMStaticFwdPreference_Type.__name__ = "Integer32"
_WfMTMStaticFwdPreference_Object = MibTableColumn
wfMTMStaticFwdPreference = _WfMTMStaticFwdPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 7),
    _WfMTMStaticFwdPreference_Type()
)
wfMTMStaticFwdPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdPreference.setStatus("obsolete")
_WfMTMStaticFwdPrecedence_Type = Integer32
_WfMTMStaticFwdPrecedence_Object = MibTableColumn
wfMTMStaticFwdPrecedence = _WfMTMStaticFwdPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 8),
    _WfMTMStaticFwdPrecedence_Type()
)
wfMTMStaticFwdPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdPrecedence.setStatus("obsolete")
_WfMTMStaticFwdInject_Type = OctetString
_WfMTMStaticFwdInject_Object = MibTableColumn
wfMTMStaticFwdInject = _WfMTMStaticFwdInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 9),
    _WfMTMStaticFwdInject_Type()
)
wfMTMStaticFwdInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMTMStaticFwdInject.setStatus("obsolete")
_WfMTMStaticFwdSources_Type = OctetString
_WfMTMStaticFwdSources_Object = MibTableColumn
wfMTMStaticFwdSources = _WfMTMStaticFwdSources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 10),
    _WfMTMStaticFwdSources_Type()
)
wfMTMStaticFwdSources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdSources.setStatus("obsolete")
_WfMTMStaticFwdInCircuits_Type = OctetString
_WfMTMStaticFwdInCircuits_Object = MibTableColumn
wfMTMStaticFwdInCircuits = _WfMTMStaticFwdInCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 11),
    _WfMTMStaticFwdInCircuits_Type()
)
wfMTMStaticFwdInCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdInCircuits.setStatus("obsolete")
_WfMTMStaticFwdOutCircuits_Type = OctetString
_WfMTMStaticFwdOutCircuits_Object = MibTableColumn
wfMTMStaticFwdOutCircuits = _WfMTMStaticFwdOutCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 12),
    _WfMTMStaticFwdOutCircuits_Type()
)
wfMTMStaticFwdOutCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdOutCircuits.setStatus("obsolete")


class _WfMTMStaticFwdMode_Type(Integer32):
    """Custom type wfMTMStaticFwdMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamictostatic", 4),
          ("static", 2),
          ("statictodynamic", 3))
    )


_WfMTMStaticFwdMode_Type.__name__ = "Integer32"
_WfMTMStaticFwdMode_Object = MibTableColumn
wfMTMStaticFwdMode = _WfMTMStaticFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 12, 1, 13),
    _WfMTMStaticFwdMode_Type()
)
wfMTMStaticFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticFwdMode.setStatus("obsolete")
_WfIpMospfAcceptTable_Object = MibTable
wfIpMospfAcceptTable = _WfIpMospfAcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13)
)
if mibBuilder.loadTexts:
    wfIpMospfAcceptTable.setStatus("mandatory")
_WfIpMospfAcceptEntry_Object = MibTableRow
wfIpMospfAcceptEntry = _WfIpMospfAcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1)
)
wfIpMospfAcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpMospfAcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpMospfAcceptEntry.setStatus("mandatory")


class _WfIpMospfAcceptDelete_Type(Integer32):
    """Custom type wfIpMospfAcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpMospfAcceptDelete_Type.__name__ = "Integer32"
_WfIpMospfAcceptDelete_Object = MibTableColumn
wfIpMospfAcceptDelete = _WfIpMospfAcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 1),
    _WfIpMospfAcceptDelete_Type()
)
wfIpMospfAcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptDelete.setStatus("mandatory")


class _WfIpMospfAcceptDisable_Type(Integer32):
    """Custom type wfIpMospfAcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpMospfAcceptDisable_Type.__name__ = "Integer32"
_WfIpMospfAcceptDisable_Object = MibTableColumn
wfIpMospfAcceptDisable = _WfIpMospfAcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 2),
    _WfIpMospfAcceptDisable_Type()
)
wfIpMospfAcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptDisable.setStatus("mandatory")
_WfIpMospfAcceptIndex_Type = Integer32
_WfIpMospfAcceptIndex_Object = MibTableColumn
wfIpMospfAcceptIndex = _WfIpMospfAcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 3),
    _WfIpMospfAcceptIndex_Type()
)
wfIpMospfAcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAcceptIndex.setStatus("mandatory")
_WfIpMospfAcceptName_Type = DisplayString
_WfIpMospfAcceptName_Object = MibTableColumn
wfIpMospfAcceptName = _WfIpMospfAcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 4),
    _WfIpMospfAcceptName_Type()
)
wfIpMospfAcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptName.setStatus("mandatory")
_WfIpMospfAcceptNetworks_Type = OctetString
_WfIpMospfAcceptNetworks_Object = MibTableColumn
wfIpMospfAcceptNetworks = _WfIpMospfAcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 5),
    _WfIpMospfAcceptNetworks_Type()
)
wfIpMospfAcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptNetworks.setStatus("mandatory")


class _WfIpMospfAcceptAction_Type(Integer32):
    """Custom type wfIpMospfAcceptAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpMospfAcceptAction_Type.__name__ = "Integer32"
_WfIpMospfAcceptAction_Object = MibTableColumn
wfIpMospfAcceptAction = _WfIpMospfAcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 6),
    _WfIpMospfAcceptAction_Type()
)
wfIpMospfAcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptAction.setStatus("mandatory")


class _WfIpMospfAcceptPreference_Type(Integer32):
    """Custom type wfIpMospfAcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpMospfAcceptPreference_Type.__name__ = "Integer32"
_WfIpMospfAcceptPreference_Object = MibTableColumn
wfIpMospfAcceptPreference = _WfIpMospfAcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 7),
    _WfIpMospfAcceptPreference_Type()
)
wfIpMospfAcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptPreference.setStatus("mandatory")
_WfIpMospfAcceptPrecedence_Type = Integer32
_WfIpMospfAcceptPrecedence_Object = MibTableColumn
wfIpMospfAcceptPrecedence = _WfIpMospfAcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 8),
    _WfIpMospfAcceptPrecedence_Type()
)
wfIpMospfAcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptPrecedence.setStatus("mandatory")
_WfIpMospfAcceptInject_Type = OctetString
_WfIpMospfAcceptInject_Object = MibTableColumn
wfIpMospfAcceptInject = _WfIpMospfAcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 9),
    _WfIpMospfAcceptInject_Type()
)
wfIpMospfAcceptInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAcceptInject.setStatus("mandatory")
_WfIpMospfAcceptGateway_Type = OctetString
_WfIpMospfAcceptGateway_Object = MibTableColumn
wfIpMospfAcceptGateway = _WfIpMospfAcceptGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 10),
    _WfIpMospfAcceptGateway_Type()
)
wfIpMospfAcceptGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptGateway.setStatus("mandatory")
_WfIpMospfAcceptInterface_Type = OctetString
_WfIpMospfAcceptInterface_Object = MibTableColumn
wfIpMospfAcceptInterface = _WfIpMospfAcceptInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 11),
    _WfIpMospfAcceptInterface_Type()
)
wfIpMospfAcceptInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptInterface.setStatus("mandatory")
_WfIpMospfAcceptApplyMask_Type = IpAddress
_WfIpMospfAcceptApplyMask_Object = MibTableColumn
wfIpMospfAcceptApplyMask = _WfIpMospfAcceptApplyMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 13, 1, 12),
    _WfIpMospfAcceptApplyMask_Type()
)
wfIpMospfAcceptApplyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAcceptApplyMask.setStatus("mandatory")
_WfIpMospfAnnounceTable_Object = MibTable
wfIpMospfAnnounceTable = _WfIpMospfAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14)
)
if mibBuilder.loadTexts:
    wfIpMospfAnnounceTable.setStatus("mandatory")
_WfIpMospfAnnounceEntry_Object = MibTableRow
wfIpMospfAnnounceEntry = _WfIpMospfAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1)
)
wfIpMospfAnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpMospfAnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpMospfAnnounceEntry.setStatus("mandatory")


class _WfIpMospfAnnounceDelete_Type(Integer32):
    """Custom type wfIpMospfAnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpMospfAnnounceDelete_Type.__name__ = "Integer32"
_WfIpMospfAnnounceDelete_Object = MibTableColumn
wfIpMospfAnnounceDelete = _WfIpMospfAnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 1),
    _WfIpMospfAnnounceDelete_Type()
)
wfIpMospfAnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceDelete.setStatus("mandatory")


class _WfIpMospfAnnounceDisable_Type(Integer32):
    """Custom type wfIpMospfAnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpMospfAnnounceDisable_Type.__name__ = "Integer32"
_WfIpMospfAnnounceDisable_Object = MibTableColumn
wfIpMospfAnnounceDisable = _WfIpMospfAnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 2),
    _WfIpMospfAnnounceDisable_Type()
)
wfIpMospfAnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceDisable.setStatus("mandatory")
_WfIpMospfAnnounceIndex_Type = Integer32
_WfIpMospfAnnounceIndex_Object = MibTableColumn
wfIpMospfAnnounceIndex = _WfIpMospfAnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 3),
    _WfIpMospfAnnounceIndex_Type()
)
wfIpMospfAnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceIndex.setStatus("mandatory")
_WfIpMospfAnnounceName_Type = DisplayString
_WfIpMospfAnnounceName_Object = MibTableColumn
wfIpMospfAnnounceName = _WfIpMospfAnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 4),
    _WfIpMospfAnnounceName_Type()
)
wfIpMospfAnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceName.setStatus("mandatory")
_WfIpMospfAnnounceNetworks_Type = OctetString
_WfIpMospfAnnounceNetworks_Object = MibTableColumn
wfIpMospfAnnounceNetworks = _WfIpMospfAnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 5),
    _WfIpMospfAnnounceNetworks_Type()
)
wfIpMospfAnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceNetworks.setStatus("mandatory")


class _WfIpMospfAnnounceAction_Type(Integer32):
    """Custom type wfIpMospfAnnounceAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpMospfAnnounceAction_Type.__name__ = "Integer32"
_WfIpMospfAnnounceAction_Object = MibTableColumn
wfIpMospfAnnounceAction = _WfIpMospfAnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 6),
    _WfIpMospfAnnounceAction_Type()
)
wfIpMospfAnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceAction.setStatus("mandatory")
_WfIpMospfAnnouncePrecedence_Type = Integer32
_WfIpMospfAnnouncePrecedence_Object = MibTableColumn
wfIpMospfAnnouncePrecedence = _WfIpMospfAnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 7),
    _WfIpMospfAnnouncePrecedence_Type()
)
wfIpMospfAnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAnnouncePrecedence.setStatus("mandatory")
_WfIpMospfAnnounceRouteSource_Type = Integer32
_WfIpMospfAnnounceRouteSource_Object = MibTableColumn
wfIpMospfAnnounceRouteSource = _WfIpMospfAnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 8),
    _WfIpMospfAnnounceRouteSource_Type()
)
wfIpMospfAnnounceRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceRouteSource.setStatus("mandatory")
_WfIpMospfAnnounceExtRouteSource_Type = Integer32
_WfIpMospfAnnounceExtRouteSource_Object = MibTableColumn
wfIpMospfAnnounceExtRouteSource = _WfIpMospfAnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 9),
    _WfIpMospfAnnounceExtRouteSource_Type()
)
wfIpMospfAnnounceExtRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceExtRouteSource.setStatus("mandatory")
_WfIpMospfAnnounceAdvertise_Type = OctetString
_WfIpMospfAnnounceAdvertise_Object = MibTableColumn
wfIpMospfAnnounceAdvertise = _WfIpMospfAnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 10),
    _WfIpMospfAnnounceAdvertise_Type()
)
wfIpMospfAnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceAdvertise.setStatus("mandatory")
_WfIpMospfAnnounceRipGateway_Type = OctetString
_WfIpMospfAnnounceRipGateway_Object = MibTableColumn
wfIpMospfAnnounceRipGateway = _WfIpMospfAnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 11),
    _WfIpMospfAnnounceRipGateway_Type()
)
wfIpMospfAnnounceRipGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceRipGateway.setStatus("mandatory")
_WfIpMospfAnnounceRipInterface_Type = OctetString
_WfIpMospfAnnounceRipInterface_Object = MibTableColumn
wfIpMospfAnnounceRipInterface = _WfIpMospfAnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 12),
    _WfIpMospfAnnounceRipInterface_Type()
)
wfIpMospfAnnounceRipInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceRipInterface.setStatus("mandatory")
_WfIpMospfAnnounceOspfRouterId_Type = OctetString
_WfIpMospfAnnounceOspfRouterId_Object = MibTableColumn
wfIpMospfAnnounceOspfRouterId = _WfIpMospfAnnounceOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 13),
    _WfIpMospfAnnounceOspfRouterId_Type()
)
wfIpMospfAnnounceOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceOspfRouterId.setStatus("mandatory")


class _WfIpMospfAnnounceOspfType_Type(Integer32):
    """Custom type wfIpMospfAnnounceOspfType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpMospfAnnounceOspfType_Type.__name__ = "Integer32"
_WfIpMospfAnnounceOspfType_Object = MibTableColumn
wfIpMospfAnnounceOspfType = _WfIpMospfAnnounceOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 14),
    _WfIpMospfAnnounceOspfType_Type()
)
wfIpMospfAnnounceOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceOspfType.setStatus("mandatory")
_WfIpMospfAnnounceOspfTag_Type = OctetString
_WfIpMospfAnnounceOspfTag_Object = MibTableColumn
wfIpMospfAnnounceOspfTag = _WfIpMospfAnnounceOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 15),
    _WfIpMospfAnnounceOspfTag_Type()
)
wfIpMospfAnnounceOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceOspfTag.setStatus("mandatory")
_WfIpMospfAnnounceEgpPeer_Type = OctetString
_WfIpMospfAnnounceEgpPeer_Object = MibTableColumn
wfIpMospfAnnounceEgpPeer = _WfIpMospfAnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 16),
    _WfIpMospfAnnounceEgpPeer_Type()
)
wfIpMospfAnnounceEgpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceEgpPeer.setStatus("mandatory")
_WfIpMospfAnnounceEgpPeerAs_Type = OctetString
_WfIpMospfAnnounceEgpPeerAs_Object = MibTableColumn
wfIpMospfAnnounceEgpPeerAs = _WfIpMospfAnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 17),
    _WfIpMospfAnnounceEgpPeerAs_Type()
)
wfIpMospfAnnounceEgpPeerAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceEgpPeerAs.setStatus("mandatory")
_WfIpMospfAnnounceEgpGateway_Type = OctetString
_WfIpMospfAnnounceEgpGateway_Object = MibTableColumn
wfIpMospfAnnounceEgpGateway = _WfIpMospfAnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 18),
    _WfIpMospfAnnounceEgpGateway_Type()
)
wfIpMospfAnnounceEgpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceEgpGateway.setStatus("mandatory")
_WfIpMospfAnnounceBgpPeer_Type = OctetString
_WfIpMospfAnnounceBgpPeer_Object = MibTableColumn
wfIpMospfAnnounceBgpPeer = _WfIpMospfAnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 19),
    _WfIpMospfAnnounceBgpPeer_Type()
)
wfIpMospfAnnounceBgpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceBgpPeer.setStatus("mandatory")
_WfIpMospfAnnounceBgpPeerAs_Type = OctetString
_WfIpMospfAnnounceBgpPeerAs_Object = MibTableColumn
wfIpMospfAnnounceBgpPeerAs = _WfIpMospfAnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 20),
    _WfIpMospfAnnounceBgpPeerAs_Type()
)
wfIpMospfAnnounceBgpPeerAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceBgpPeerAs.setStatus("mandatory")
_WfIpMospfAnnounceBgpNextHop_Type = OctetString
_WfIpMospfAnnounceBgpNextHop_Object = MibTableColumn
wfIpMospfAnnounceBgpNextHop = _WfIpMospfAnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 14, 1, 21),
    _WfIpMospfAnnounceBgpNextHop_Type()
)
wfIpMospfAnnounceBgpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpMospfAnnounceBgpNextHop.setStatus("mandatory")
_WfIpDvmrpAcceptTable_Object = MibTable
wfIpDvmrpAcceptTable = _WfIpDvmrpAcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15)
)
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptTable.setStatus("mandatory")
_WfIpDvmrpAcceptEntry_Object = MibTableRow
wfIpDvmrpAcceptEntry = _WfIpDvmrpAcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1)
)
wfIpDvmrpAcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpDvmrpAcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptEntry.setStatus("mandatory")


class _WfIpDvmrpAcceptDelete_Type(Integer32):
    """Custom type wfIpDvmrpAcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpDvmrpAcceptDelete_Type.__name__ = "Integer32"
_WfIpDvmrpAcceptDelete_Object = MibTableColumn
wfIpDvmrpAcceptDelete = _WfIpDvmrpAcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 1),
    _WfIpDvmrpAcceptDelete_Type()
)
wfIpDvmrpAcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptDelete.setStatus("mandatory")


class _WfIpDvmrpAcceptDisable_Type(Integer32):
    """Custom type wfIpDvmrpAcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpDvmrpAcceptDisable_Type.__name__ = "Integer32"
_WfIpDvmrpAcceptDisable_Object = MibTableColumn
wfIpDvmrpAcceptDisable = _WfIpDvmrpAcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 2),
    _WfIpDvmrpAcceptDisable_Type()
)
wfIpDvmrpAcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptDisable.setStatus("mandatory")
_WfIpDvmrpAcceptIndex_Type = Integer32
_WfIpDvmrpAcceptIndex_Object = MibTableColumn
wfIpDvmrpAcceptIndex = _WfIpDvmrpAcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 3),
    _WfIpDvmrpAcceptIndex_Type()
)
wfIpDvmrpAcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptIndex.setStatus("mandatory")
_WfIpDvmrpAcceptName_Type = DisplayString
_WfIpDvmrpAcceptName_Object = MibTableColumn
wfIpDvmrpAcceptName = _WfIpDvmrpAcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 4),
    _WfIpDvmrpAcceptName_Type()
)
wfIpDvmrpAcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptName.setStatus("mandatory")
_WfIpDvmrpAcceptNetworks_Type = OctetString
_WfIpDvmrpAcceptNetworks_Object = MibTableColumn
wfIpDvmrpAcceptNetworks = _WfIpDvmrpAcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 5),
    _WfIpDvmrpAcceptNetworks_Type()
)
wfIpDvmrpAcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptNetworks.setStatus("mandatory")


class _WfIpDvmrpAcceptAction_Type(Integer32):
    """Custom type wfIpDvmrpAcceptAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpDvmrpAcceptAction_Type.__name__ = "Integer32"
_WfIpDvmrpAcceptAction_Object = MibTableColumn
wfIpDvmrpAcceptAction = _WfIpDvmrpAcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 6),
    _WfIpDvmrpAcceptAction_Type()
)
wfIpDvmrpAcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptAction.setStatus("mandatory")


class _WfIpDvmrpAcceptPreference_Type(Integer32):
    """Custom type wfIpDvmrpAcceptPreference based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpDvmrpAcceptPreference_Type.__name__ = "Integer32"
_WfIpDvmrpAcceptPreference_Object = MibTableColumn
wfIpDvmrpAcceptPreference = _WfIpDvmrpAcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 7),
    _WfIpDvmrpAcceptPreference_Type()
)
wfIpDvmrpAcceptPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptPreference.setStatus("mandatory")
_WfIpDvmrpAcceptPrecedence_Type = Integer32
_WfIpDvmrpAcceptPrecedence_Object = MibTableColumn
wfIpDvmrpAcceptPrecedence = _WfIpDvmrpAcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 8),
    _WfIpDvmrpAcceptPrecedence_Type()
)
wfIpDvmrpAcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptPrecedence.setStatus("mandatory")
_WfIpDvmrpAcceptInject_Type = OctetString
_WfIpDvmrpAcceptInject_Object = MibTableColumn
wfIpDvmrpAcceptInject = _WfIpDvmrpAcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 9),
    _WfIpDvmrpAcceptInject_Type()
)
wfIpDvmrpAcceptInject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptInject.setStatus("mandatory")
_WfIpDvmrpAcceptGateway_Type = OctetString
_WfIpDvmrpAcceptGateway_Object = MibTableColumn
wfIpDvmrpAcceptGateway = _WfIpDvmrpAcceptGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 10),
    _WfIpDvmrpAcceptGateway_Type()
)
wfIpDvmrpAcceptGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptGateway.setStatus("mandatory")
_WfIpDvmrpAcceptInterface_Type = OctetString
_WfIpDvmrpAcceptInterface_Object = MibTableColumn
wfIpDvmrpAcceptInterface = _WfIpDvmrpAcceptInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 11),
    _WfIpDvmrpAcceptInterface_Type()
)
wfIpDvmrpAcceptInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptInterface.setStatus("mandatory")
_WfIpDvmrpAcceptApplyMask_Type = IpAddress
_WfIpDvmrpAcceptApplyMask_Object = MibTableColumn
wfIpDvmrpAcceptApplyMask = _WfIpDvmrpAcceptApplyMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 12),
    _WfIpDvmrpAcceptApplyMask_Type()
)
wfIpDvmrpAcceptApplyMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptApplyMask.setStatus("mandatory")
_WfIpDvmrpAcceptTunnels_Type = OctetString
_WfIpDvmrpAcceptTunnels_Object = MibTableColumn
wfIpDvmrpAcceptTunnels = _WfIpDvmrpAcceptTunnels_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 13),
    _WfIpDvmrpAcceptTunnels_Type()
)
wfIpDvmrpAcceptTunnels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptTunnels.setStatus("mandatory")


class _WfIpDvmrpAcceptInjectMetric_Type(Integer32):
    """Custom type wfIpDvmrpAcceptInjectMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WfIpDvmrpAcceptInjectMetric_Type.__name__ = "Integer32"
_WfIpDvmrpAcceptInjectMetric_Object = MibTableColumn
wfIpDvmrpAcceptInjectMetric = _WfIpDvmrpAcceptInjectMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 15, 1, 14),
    _WfIpDvmrpAcceptInjectMetric_Type()
)
wfIpDvmrpAcceptInjectMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAcceptInjectMetric.setStatus("mandatory")
_WfIpDvmrpAnnounceTable_Object = MibTable
wfIpDvmrpAnnounceTable = _WfIpDvmrpAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16)
)
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceTable.setStatus("mandatory")
_WfIpDvmrpAnnounceEntry_Object = MibTableRow
wfIpDvmrpAnnounceEntry = _WfIpDvmrpAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1)
)
wfIpDvmrpAnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpDvmrpAnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceEntry.setStatus("mandatory")


class _WfIpDvmrpAnnounceDelete_Type(Integer32):
    """Custom type wfIpDvmrpAnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpDvmrpAnnounceDelete_Type.__name__ = "Integer32"
_WfIpDvmrpAnnounceDelete_Object = MibTableColumn
wfIpDvmrpAnnounceDelete = _WfIpDvmrpAnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 1),
    _WfIpDvmrpAnnounceDelete_Type()
)
wfIpDvmrpAnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceDelete.setStatus("mandatory")


class _WfIpDvmrpAnnounceDisable_Type(Integer32):
    """Custom type wfIpDvmrpAnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpDvmrpAnnounceDisable_Type.__name__ = "Integer32"
_WfIpDvmrpAnnounceDisable_Object = MibTableColumn
wfIpDvmrpAnnounceDisable = _WfIpDvmrpAnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 2),
    _WfIpDvmrpAnnounceDisable_Type()
)
wfIpDvmrpAnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceDisable.setStatus("mandatory")
_WfIpDvmrpAnnounceIndex_Type = Integer32
_WfIpDvmrpAnnounceIndex_Object = MibTableColumn
wfIpDvmrpAnnounceIndex = _WfIpDvmrpAnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 3),
    _WfIpDvmrpAnnounceIndex_Type()
)
wfIpDvmrpAnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceIndex.setStatus("mandatory")
_WfIpDvmrpAnnounceName_Type = DisplayString
_WfIpDvmrpAnnounceName_Object = MibTableColumn
wfIpDvmrpAnnounceName = _WfIpDvmrpAnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 4),
    _WfIpDvmrpAnnounceName_Type()
)
wfIpDvmrpAnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceName.setStatus("mandatory")
_WfIpDvmrpAnnounceNetworks_Type = OctetString
_WfIpDvmrpAnnounceNetworks_Object = MibTableColumn
wfIpDvmrpAnnounceNetworks = _WfIpDvmrpAnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 5),
    _WfIpDvmrpAnnounceNetworks_Type()
)
wfIpDvmrpAnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceNetworks.setStatus("mandatory")


class _WfIpDvmrpAnnounceAction_Type(Integer32):
    """Custom type wfIpDvmrpAnnounceAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpDvmrpAnnounceAction_Type.__name__ = "Integer32"
_WfIpDvmrpAnnounceAction_Object = MibTableColumn
wfIpDvmrpAnnounceAction = _WfIpDvmrpAnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 6),
    _WfIpDvmrpAnnounceAction_Type()
)
wfIpDvmrpAnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceAction.setStatus("mandatory")
_WfIpDvmrpAnnouncePrecedence_Type = Integer32
_WfIpDvmrpAnnouncePrecedence_Object = MibTableColumn
wfIpDvmrpAnnouncePrecedence = _WfIpDvmrpAnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 7),
    _WfIpDvmrpAnnouncePrecedence_Type()
)
wfIpDvmrpAnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnouncePrecedence.setStatus("mandatory")
_WfIpDvmrpAnnounceRouteSource_Type = Integer32
_WfIpDvmrpAnnounceRouteSource_Object = MibTableColumn
wfIpDvmrpAnnounceRouteSource = _WfIpDvmrpAnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 8),
    _WfIpDvmrpAnnounceRouteSource_Type()
)
wfIpDvmrpAnnounceRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceRouteSource.setStatus("mandatory")
_WfIpDvmrpAnnounceExtRouteSource_Type = Integer32
_WfIpDvmrpAnnounceExtRouteSource_Object = MibTableColumn
wfIpDvmrpAnnounceExtRouteSource = _WfIpDvmrpAnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 9),
    _WfIpDvmrpAnnounceExtRouteSource_Type()
)
wfIpDvmrpAnnounceExtRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceExtRouteSource.setStatus("mandatory")
_WfIpDvmrpAnnounceAdvertise_Type = OctetString
_WfIpDvmrpAnnounceAdvertise_Object = MibTableColumn
wfIpDvmrpAnnounceAdvertise = _WfIpDvmrpAnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 10),
    _WfIpDvmrpAnnounceAdvertise_Type()
)
wfIpDvmrpAnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceAdvertise.setStatus("mandatory")
_WfIpDvmrpAnnounceRipGateway_Type = OctetString
_WfIpDvmrpAnnounceRipGateway_Object = MibTableColumn
wfIpDvmrpAnnounceRipGateway = _WfIpDvmrpAnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 11),
    _WfIpDvmrpAnnounceRipGateway_Type()
)
wfIpDvmrpAnnounceRipGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceRipGateway.setStatus("mandatory")
_WfIpDvmrpAnnounceRipInterface_Type = OctetString
_WfIpDvmrpAnnounceRipInterface_Object = MibTableColumn
wfIpDvmrpAnnounceRipInterface = _WfIpDvmrpAnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 12),
    _WfIpDvmrpAnnounceRipInterface_Type()
)
wfIpDvmrpAnnounceRipInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceRipInterface.setStatus("mandatory")
_WfIpDvmrpAnnounceOspfRouterId_Type = OctetString
_WfIpDvmrpAnnounceOspfRouterId_Object = MibTableColumn
wfIpDvmrpAnnounceOspfRouterId = _WfIpDvmrpAnnounceOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 13),
    _WfIpDvmrpAnnounceOspfRouterId_Type()
)
wfIpDvmrpAnnounceOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceOspfRouterId.setStatus("mandatory")


class _WfIpDvmrpAnnounceOspfType_Type(Integer32):
    """Custom type wfIpDvmrpAnnounceOspfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpDvmrpAnnounceOspfType_Type.__name__ = "Integer32"
_WfIpDvmrpAnnounceOspfType_Object = MibTableColumn
wfIpDvmrpAnnounceOspfType = _WfIpDvmrpAnnounceOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 14),
    _WfIpDvmrpAnnounceOspfType_Type()
)
wfIpDvmrpAnnounceOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceOspfType.setStatus("mandatory")
_WfIpDvmrpAnnounceOspfTag_Type = OctetString
_WfIpDvmrpAnnounceOspfTag_Object = MibTableColumn
wfIpDvmrpAnnounceOspfTag = _WfIpDvmrpAnnounceOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 15),
    _WfIpDvmrpAnnounceOspfTag_Type()
)
wfIpDvmrpAnnounceOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceOspfTag.setStatus("mandatory")
_WfIpDvmrpAnnounceEgpPeer_Type = OctetString
_WfIpDvmrpAnnounceEgpPeer_Object = MibTableColumn
wfIpDvmrpAnnounceEgpPeer = _WfIpDvmrpAnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 16),
    _WfIpDvmrpAnnounceEgpPeer_Type()
)
wfIpDvmrpAnnounceEgpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceEgpPeer.setStatus("mandatory")
_WfIpDvmrpAnnounceEgpPeerAs_Type = OctetString
_WfIpDvmrpAnnounceEgpPeerAs_Object = MibTableColumn
wfIpDvmrpAnnounceEgpPeerAs = _WfIpDvmrpAnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 17),
    _WfIpDvmrpAnnounceEgpPeerAs_Type()
)
wfIpDvmrpAnnounceEgpPeerAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceEgpPeerAs.setStatus("mandatory")
_WfIpDvmrpAnnounceEgpGateway_Type = OctetString
_WfIpDvmrpAnnounceEgpGateway_Object = MibTableColumn
wfIpDvmrpAnnounceEgpGateway = _WfIpDvmrpAnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 18),
    _WfIpDvmrpAnnounceEgpGateway_Type()
)
wfIpDvmrpAnnounceEgpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceEgpGateway.setStatus("mandatory")
_WfIpDvmrpAnnounceBgpPeer_Type = OctetString
_WfIpDvmrpAnnounceBgpPeer_Object = MibTableColumn
wfIpDvmrpAnnounceBgpPeer = _WfIpDvmrpAnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 19),
    _WfIpDvmrpAnnounceBgpPeer_Type()
)
wfIpDvmrpAnnounceBgpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceBgpPeer.setStatus("mandatory")
_WfIpDvmrpAnnounceBgpPeerAs_Type = OctetString
_WfIpDvmrpAnnounceBgpPeerAs_Object = MibTableColumn
wfIpDvmrpAnnounceBgpPeerAs = _WfIpDvmrpAnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 20),
    _WfIpDvmrpAnnounceBgpPeerAs_Type()
)
wfIpDvmrpAnnounceBgpPeerAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceBgpPeerAs.setStatus("mandatory")
_WfIpDvmrpAnnounceBgpNextHop_Type = OctetString
_WfIpDvmrpAnnounceBgpNextHop_Object = MibTableColumn
wfIpDvmrpAnnounceBgpNextHop = _WfIpDvmrpAnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 21),
    _WfIpDvmrpAnnounceBgpNextHop_Type()
)
wfIpDvmrpAnnounceBgpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceBgpNextHop.setStatus("mandatory")
_WfIpDvmrpAnnounceCircuits_Type = OctetString
_WfIpDvmrpAnnounceCircuits_Object = MibTableColumn
wfIpDvmrpAnnounceCircuits = _WfIpDvmrpAnnounceCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 22),
    _WfIpDvmrpAnnounceCircuits_Type()
)
wfIpDvmrpAnnounceCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceCircuits.setStatus("obsolete")
_WfIpDvmrpAnnounceTunnels_Type = OctetString
_WfIpDvmrpAnnounceTunnels_Object = MibTableColumn
wfIpDvmrpAnnounceTunnels = _WfIpDvmrpAnnounceTunnels_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 23),
    _WfIpDvmrpAnnounceTunnels_Type()
)
wfIpDvmrpAnnounceTunnels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceTunnels.setStatus("mandatory")


class _WfIpDvmrpAnnounceMetric_Type(Integer32):
    """Custom type wfIpDvmrpAnnounceMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_WfIpDvmrpAnnounceMetric_Type.__name__ = "Integer32"
_WfIpDvmrpAnnounceMetric_Object = MibTableColumn
wfIpDvmrpAnnounceMetric = _WfIpDvmrpAnnounceMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 24),
    _WfIpDvmrpAnnounceMetric_Type()
)
wfIpDvmrpAnnounceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceMetric.setStatus("mandatory")
_WfIpDvmrpAnnounceInterface_Type = OctetString
_WfIpDvmrpAnnounceInterface_Object = MibTableColumn
wfIpDvmrpAnnounceInterface = _WfIpDvmrpAnnounceInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 16, 1, 25),
    _WfIpDvmrpAnnounceInterface_Type()
)
wfIpDvmrpAnnounceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpAnnounceInterface.setStatus("mandatory")
_WfIpDvmrpInjectRtTable_Object = MibTable
wfIpDvmrpInjectRtTable = _WfIpDvmrpInjectRtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17)
)
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtTable.setStatus("mandatory")
_WfIpDvmrpInjectRtEntry_Object = MibTableRow
wfIpDvmrpInjectRtEntry = _WfIpDvmrpInjectRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1)
)
wfIpDvmrpInjectRtEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpDvmrpInjectRtIndex"),
)
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtEntry.setStatus("mandatory")


class _WfIpDvmrpInjectRtDelete_Type(Integer32):
    """Custom type wfIpDvmrpInjectRtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpDvmrpInjectRtDelete_Type.__name__ = "Integer32"
_WfIpDvmrpInjectRtDelete_Object = MibTableColumn
wfIpDvmrpInjectRtDelete = _WfIpDvmrpInjectRtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 1),
    _WfIpDvmrpInjectRtDelete_Type()
)
wfIpDvmrpInjectRtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtDelete.setStatus("mandatory")


class _WfIpDvmrpInjectRtDisable_Type(Integer32):
    """Custom type wfIpDvmrpInjectRtDisable based on Integer32"""
    defaultValue = 1

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


_WfIpDvmrpInjectRtDisable_Type.__name__ = "Integer32"
_WfIpDvmrpInjectRtDisable_Object = MibTableColumn
wfIpDvmrpInjectRtDisable = _WfIpDvmrpInjectRtDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 2),
    _WfIpDvmrpInjectRtDisable_Type()
)
wfIpDvmrpInjectRtDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtDisable.setStatus("mandatory")
_WfIpDvmrpInjectRtIndex_Type = Integer32
_WfIpDvmrpInjectRtIndex_Object = MibTableColumn
wfIpDvmrpInjectRtIndex = _WfIpDvmrpInjectRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 3),
    _WfIpDvmrpInjectRtIndex_Type()
)
wfIpDvmrpInjectRtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtIndex.setStatus("mandatory")
_WfIpDvmrpInjectRtName_Type = DisplayString
_WfIpDvmrpInjectRtName_Object = MibTableColumn
wfIpDvmrpInjectRtName = _WfIpDvmrpInjectRtName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 4),
    _WfIpDvmrpInjectRtName_Type()
)
wfIpDvmrpInjectRtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtName.setStatus("mandatory")
_WfIpDvmrpInjectRtNetworks_Type = OctetString
_WfIpDvmrpInjectRtNetworks_Object = MibTableColumn
wfIpDvmrpInjectRtNetworks = _WfIpDvmrpInjectRtNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 5),
    _WfIpDvmrpInjectRtNetworks_Type()
)
wfIpDvmrpInjectRtNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtNetworks.setStatus("mandatory")


class _WfIpDvmrpInjectRtAction_Type(Integer32):
    """Custom type wfIpDvmrpInjectRtAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpDvmrpInjectRtAction_Type.__name__ = "Integer32"
_WfIpDvmrpInjectRtAction_Object = MibTableColumn
wfIpDvmrpInjectRtAction = _WfIpDvmrpInjectRtAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 6),
    _WfIpDvmrpInjectRtAction_Type()
)
wfIpDvmrpInjectRtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtAction.setStatus("mandatory")


class _WfIpDvmrpInjectRtPreference_Type(Integer32):
    """Custom type wfIpDvmrpInjectRtPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpDvmrpInjectRtPreference_Type.__name__ = "Integer32"
_WfIpDvmrpInjectRtPreference_Object = MibTableColumn
wfIpDvmrpInjectRtPreference = _WfIpDvmrpInjectRtPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 7),
    _WfIpDvmrpInjectRtPreference_Type()
)
wfIpDvmrpInjectRtPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtPreference.setStatus("mandatory")
_WfIpDvmrpInjectRtPrecedence_Type = Integer32
_WfIpDvmrpInjectRtPrecedence_Object = MibTableColumn
wfIpDvmrpInjectRtPrecedence = _WfIpDvmrpInjectRtPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 8),
    _WfIpDvmrpInjectRtPrecedence_Type()
)
wfIpDvmrpInjectRtPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtPrecedence.setStatus("mandatory")
_WfIpDvmrpInjectRtInject_Type = OctetString
_WfIpDvmrpInjectRtInject_Object = MibTableColumn
wfIpDvmrpInjectRtInject = _WfIpDvmrpInjectRtInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 9),
    _WfIpDvmrpInjectRtInject_Type()
)
wfIpDvmrpInjectRtInject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtInject.setStatus("mandatory")
_WfIpDvmrpInjectRtInInterface_Type = OctetString
_WfIpDvmrpInjectRtInInterface_Object = MibTableColumn
wfIpDvmrpInjectRtInInterface = _WfIpDvmrpInjectRtInInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 10),
    _WfIpDvmrpInjectRtInInterface_Type()
)
wfIpDvmrpInjectRtInInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtInInterface.setStatus("mandatory")


class _WfIpDvmrpInjectRtType_Type(Integer32):
    """Custom type wfIpDvmrpInjectRtType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("best-route", 2),
          ("both", 6),
          ("ospf", 4))
    )


_WfIpDvmrpInjectRtType_Type.__name__ = "Integer32"
_WfIpDvmrpInjectRtType_Object = MibTableColumn
wfIpDvmrpInjectRtType = _WfIpDvmrpInjectRtType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 11),
    _WfIpDvmrpInjectRtType_Type()
)
wfIpDvmrpInjectRtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtType.setStatus("mandatory")


class _WfIpDvmrpInjectRtMetric_Type(Integer32):
    """Custom type wfIpDvmrpInjectRtMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WfIpDvmrpInjectRtMetric_Type.__name__ = "Integer32"
_WfIpDvmrpInjectRtMetric_Object = MibTableColumn
wfIpDvmrpInjectRtMetric = _WfIpDvmrpInjectRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 17, 1, 12),
    _WfIpDvmrpInjectRtMetric_Type()
)
wfIpDvmrpInjectRtMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpDvmrpInjectRtMetric.setStatus("mandatory")
_WfIpIisisAcceptTable_Object = MibTable
wfIpIisisAcceptTable = _WfIpIisisAcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18)
)
if mibBuilder.loadTexts:
    wfIpIisisAcceptTable.setStatus("mandatory")
_WfIpIisisAcceptEntry_Object = MibTableRow
wfIpIisisAcceptEntry = _WfIpIisisAcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1)
)
wfIpIisisAcceptEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpIisisAcceptIndex"),
)
if mibBuilder.loadTexts:
    wfIpIisisAcceptEntry.setStatus("mandatory")


class _WfIpIisisAcceptDelete_Type(Integer32):
    """Custom type wfIpIisisAcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpIisisAcceptDelete_Type.__name__ = "Integer32"
_WfIpIisisAcceptDelete_Object = MibTableColumn
wfIpIisisAcceptDelete = _WfIpIisisAcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 1),
    _WfIpIisisAcceptDelete_Type()
)
wfIpIisisAcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptDelete.setStatus("mandatory")


class _WfIpIisisAcceptDisable_Type(Integer32):
    """Custom type wfIpIisisAcceptDisable based on Integer32"""
    defaultValue = 1

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


_WfIpIisisAcceptDisable_Type.__name__ = "Integer32"
_WfIpIisisAcceptDisable_Object = MibTableColumn
wfIpIisisAcceptDisable = _WfIpIisisAcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 2),
    _WfIpIisisAcceptDisable_Type()
)
wfIpIisisAcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptDisable.setStatus("mandatory")
_WfIpIisisAcceptIndex_Type = Integer32
_WfIpIisisAcceptIndex_Object = MibTableColumn
wfIpIisisAcceptIndex = _WfIpIisisAcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 3),
    _WfIpIisisAcceptIndex_Type()
)
wfIpIisisAcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIisisAcceptIndex.setStatus("mandatory")
_WfIpIisisAcceptName_Type = DisplayString
_WfIpIisisAcceptName_Object = MibTableColumn
wfIpIisisAcceptName = _WfIpIisisAcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 4),
    _WfIpIisisAcceptName_Type()
)
wfIpIisisAcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptName.setStatus("mandatory")
_WfIpIisisAcceptNetworks_Type = OctetString
_WfIpIisisAcceptNetworks_Object = MibTableColumn
wfIpIisisAcceptNetworks = _WfIpIisisAcceptNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 5),
    _WfIpIisisAcceptNetworks_Type()
)
wfIpIisisAcceptNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptNetworks.setStatus("mandatory")


class _WfIpIisisAcceptAction_Type(Integer32):
    """Custom type wfIpIisisAcceptAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpIisisAcceptAction_Type.__name__ = "Integer32"
_WfIpIisisAcceptAction_Object = MibTableColumn
wfIpIisisAcceptAction = _WfIpIisisAcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 6),
    _WfIpIisisAcceptAction_Type()
)
wfIpIisisAcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptAction.setStatus("mandatory")


class _WfIpIisisAcceptPreference_Type(Integer32):
    """Custom type wfIpIisisAcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpIisisAcceptPreference_Type.__name__ = "Integer32"
_WfIpIisisAcceptPreference_Object = MibTableColumn
wfIpIisisAcceptPreference = _WfIpIisisAcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 7),
    _WfIpIisisAcceptPreference_Type()
)
wfIpIisisAcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptPreference.setStatus("mandatory")
_WfIpIisisAcceptPrecedence_Type = Integer32
_WfIpIisisAcceptPrecedence_Object = MibTableColumn
wfIpIisisAcceptPrecedence = _WfIpIisisAcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 8),
    _WfIpIisisAcceptPrecedence_Type()
)
wfIpIisisAcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptPrecedence.setStatus("mandatory")
_WfIpIisisAcceptInject_Type = OctetString
_WfIpIisisAcceptInject_Object = MibTableColumn
wfIpIisisAcceptInject = _WfIpIisisAcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 9),
    _WfIpIisisAcceptInject_Type()
)
wfIpIisisAcceptInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIisisAcceptInject.setStatus("mandatory")


class _WfIpIisisAcceptType_Type(Integer32):
    """Custom type wfIpIisisAcceptType based on Integer32"""
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
        *(("any", 3),
          ("external", 2),
          ("internal", 1))
    )


_WfIpIisisAcceptType_Type.__name__ = "Integer32"
_WfIpIisisAcceptType_Object = MibTableColumn
wfIpIisisAcceptType = _WfIpIisisAcceptType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 18, 1, 10),
    _WfIpIisisAcceptType_Type()
)
wfIpIisisAcceptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAcceptType.setStatus("mandatory")
_WfIpIisisAnnounceTable_Object = MibTable
wfIpIisisAnnounceTable = _WfIpIisisAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19)
)
if mibBuilder.loadTexts:
    wfIpIisisAnnounceTable.setStatus("mandatory")
_WfIpIisisAnnounceEntry_Object = MibTableRow
wfIpIisisAnnounceEntry = _WfIpIisisAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1)
)
wfIpIisisAnnounceEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfIpIisisAnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfIpIisisAnnounceEntry.setStatus("mandatory")


class _WfIpIisisAnnounceDelete_Type(Integer32):
    """Custom type wfIpIisisAnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpIisisAnnounceDelete_Type.__name__ = "Integer32"
_WfIpIisisAnnounceDelete_Object = MibTableColumn
wfIpIisisAnnounceDelete = _WfIpIisisAnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 1),
    _WfIpIisisAnnounceDelete_Type()
)
wfIpIisisAnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceDelete.setStatus("mandatory")


class _WfIpIisisAnnounceDisable_Type(Integer32):
    """Custom type wfIpIisisAnnounceDisable based on Integer32"""
    defaultValue = 1

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


_WfIpIisisAnnounceDisable_Type.__name__ = "Integer32"
_WfIpIisisAnnounceDisable_Object = MibTableColumn
wfIpIisisAnnounceDisable = _WfIpIisisAnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 2),
    _WfIpIisisAnnounceDisable_Type()
)
wfIpIisisAnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceDisable.setStatus("mandatory")
_WfIpIisisAnnounceIndex_Type = Integer32
_WfIpIisisAnnounceIndex_Object = MibTableColumn
wfIpIisisAnnounceIndex = _WfIpIisisAnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 3),
    _WfIpIisisAnnounceIndex_Type()
)
wfIpIisisAnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceIndex.setStatus("mandatory")
_WfIpIisisAnnounceName_Type = DisplayString
_WfIpIisisAnnounceName_Object = MibTableColumn
wfIpIisisAnnounceName = _WfIpIisisAnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 4),
    _WfIpIisisAnnounceName_Type()
)
wfIpIisisAnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceName.setStatus("mandatory")
_WfIpIisisAnnounceNetworks_Type = OctetString
_WfIpIisisAnnounceNetworks_Object = MibTableColumn
wfIpIisisAnnounceNetworks = _WfIpIisisAnnounceNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 5),
    _WfIpIisisAnnounceNetworks_Type()
)
wfIpIisisAnnounceNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceNetworks.setStatus("mandatory")


class _WfIpIisisAnnounceAction_Type(Integer32):
    """Custom type wfIpIisisAnnounceAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfIpIisisAnnounceAction_Type.__name__ = "Integer32"
_WfIpIisisAnnounceAction_Object = MibTableColumn
wfIpIisisAnnounceAction = _WfIpIisisAnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 6),
    _WfIpIisisAnnounceAction_Type()
)
wfIpIisisAnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceAction.setStatus("mandatory")
_WfIpIisisAnnouncePrecedence_Type = Integer32
_WfIpIisisAnnouncePrecedence_Object = MibTableColumn
wfIpIisisAnnouncePrecedence = _WfIpIisisAnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 7),
    _WfIpIisisAnnouncePrecedence_Type()
)
wfIpIisisAnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnouncePrecedence.setStatus("mandatory")


class _WfIpIisisAnnounceRouteSource_Type(Integer32):
    """Custom type wfIpIisisAnnounceRouteSource based on Integer32"""
    defaultValue = 63


_WfIpIisisAnnounceRouteSource_Object = MibTableColumn
wfIpIisisAnnounceRouteSource = _WfIpIisisAnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 8),
    _WfIpIisisAnnounceRouteSource_Type()
)
wfIpIisisAnnounceRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceRouteSource.setStatus("mandatory")


class _WfIpIisisAnnounceExtRouteSource_Type(Integer32):
    """Custom type wfIpIisisAnnounceExtRouteSource based on Integer32"""
    defaultValue = 63


_WfIpIisisAnnounceExtRouteSource_Object = MibTableColumn
wfIpIisisAnnounceExtRouteSource = _WfIpIisisAnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 9),
    _WfIpIisisAnnounceExtRouteSource_Type()
)
wfIpIisisAnnounceExtRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceExtRouteSource.setStatus("mandatory")
_WfIpIisisAnnounceAdvertise_Type = OctetString
_WfIpIisisAnnounceAdvertise_Object = MibTableColumn
wfIpIisisAnnounceAdvertise = _WfIpIisisAnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 10),
    _WfIpIisisAnnounceAdvertise_Type()
)
wfIpIisisAnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceAdvertise.setStatus("mandatory")
_WfIpIisisAnnounceRipGateway_Type = OctetString
_WfIpIisisAnnounceRipGateway_Object = MibTableColumn
wfIpIisisAnnounceRipGateway = _WfIpIisisAnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 11),
    _WfIpIisisAnnounceRipGateway_Type()
)
wfIpIisisAnnounceRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceRipGateway.setStatus("mandatory")
_WfIpIisisAnnounceRipInterface_Type = OctetString
_WfIpIisisAnnounceRipInterface_Object = MibTableColumn
wfIpIisisAnnounceRipInterface = _WfIpIisisAnnounceRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 12),
    _WfIpIisisAnnounceRipInterface_Type()
)
wfIpIisisAnnounceRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceRipInterface.setStatus("mandatory")
_WfIpIisisAnnounceIisisRouterId_Type = OctetString
_WfIpIisisAnnounceIisisRouterId_Object = MibTableColumn
wfIpIisisAnnounceIisisRouterId = _WfIpIisisAnnounceIisisRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 13),
    _WfIpIisisAnnounceIisisRouterId_Type()
)
wfIpIisisAnnounceIisisRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceIisisRouterId.setStatus("mandatory")


class _WfIpIisisAnnounceIisisType_Type(Integer32):
    """Custom type wfIpIisisAnnounceIisisType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("external", 3),
          ("internal", 4),
          ("type1", 1),
          ("type2", 2))
    )


_WfIpIisisAnnounceIisisType_Type.__name__ = "Integer32"
_WfIpIisisAnnounceIisisType_Object = MibTableColumn
wfIpIisisAnnounceIisisType = _WfIpIisisAnnounceIisisType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 14),
    _WfIpIisisAnnounceIisisType_Type()
)
wfIpIisisAnnounceIisisType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceIisisType.setStatus("mandatory")
_WfIpIisisAnnounceIisisTag_Type = OctetString
_WfIpIisisAnnounceIisisTag_Object = MibTableColumn
wfIpIisisAnnounceIisisTag = _WfIpIisisAnnounceIisisTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 15),
    _WfIpIisisAnnounceIisisTag_Type()
)
wfIpIisisAnnounceIisisTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceIisisTag.setStatus("mandatory")
_WfIpIisisAnnounceEgpPeer_Type = OctetString
_WfIpIisisAnnounceEgpPeer_Object = MibTableColumn
wfIpIisisAnnounceEgpPeer = _WfIpIisisAnnounceEgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 16),
    _WfIpIisisAnnounceEgpPeer_Type()
)
wfIpIisisAnnounceEgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceEgpPeer.setStatus("mandatory")
_WfIpIisisAnnounceEgpPeerAs_Type = OctetString
_WfIpIisisAnnounceEgpPeerAs_Object = MibTableColumn
wfIpIisisAnnounceEgpPeerAs = _WfIpIisisAnnounceEgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 17),
    _WfIpIisisAnnounceEgpPeerAs_Type()
)
wfIpIisisAnnounceEgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceEgpPeerAs.setStatus("mandatory")
_WfIpIisisAnnounceEgpGateway_Type = OctetString
_WfIpIisisAnnounceEgpGateway_Object = MibTableColumn
wfIpIisisAnnounceEgpGateway = _WfIpIisisAnnounceEgpGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 18),
    _WfIpIisisAnnounceEgpGateway_Type()
)
wfIpIisisAnnounceEgpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceEgpGateway.setStatus("mandatory")
_WfIpIisisAnnounceBgpPeer_Type = OctetString
_WfIpIisisAnnounceBgpPeer_Object = MibTableColumn
wfIpIisisAnnounceBgpPeer = _WfIpIisisAnnounceBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 19),
    _WfIpIisisAnnounceBgpPeer_Type()
)
wfIpIisisAnnounceBgpPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceBgpPeer.setStatus("mandatory")
_WfIpIisisAnnounceBgpPeerAs_Type = OctetString
_WfIpIisisAnnounceBgpPeerAs_Object = MibTableColumn
wfIpIisisAnnounceBgpPeerAs = _WfIpIisisAnnounceBgpPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 20),
    _WfIpIisisAnnounceBgpPeerAs_Type()
)
wfIpIisisAnnounceBgpPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceBgpPeerAs.setStatus("mandatory")
_WfIpIisisAnnounceBgpNextHop_Type = OctetString
_WfIpIisisAnnounceBgpNextHop_Object = MibTableColumn
wfIpIisisAnnounceBgpNextHop = _WfIpIisisAnnounceBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 21),
    _WfIpIisisAnnounceBgpNextHop_Type()
)
wfIpIisisAnnounceBgpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceBgpNextHop.setStatus("mandatory")


class _WfIpIisisAnnounceType_Type(Integer32):
    """Custom type wfIpIisisAnnounceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_WfIpIisisAnnounceType_Type.__name__ = "Integer32"
_WfIpIisisAnnounceType_Object = MibTableColumn
wfIpIisisAnnounceType = _WfIpIisisAnnounceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 22),
    _WfIpIisisAnnounceType_Type()
)
wfIpIisisAnnounceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceType.setStatus("mandatory")
_WfIpIisisAnnounceTag_Type = Integer32
_WfIpIisisAnnounceTag_Object = MibTableColumn
wfIpIisisAnnounceTag = _WfIpIisisAnnounceTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 23),
    _WfIpIisisAnnounceTag_Type()
)
wfIpIisisAnnounceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceTag.setStatus("mandatory")


class _WfIpIisisAnnounceAutoTag_Type(Integer32):
    """Custom type wfIpIisisAnnounceAutoTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("wf", 3))
    )


_WfIpIisisAnnounceAutoTag_Type.__name__ = "Integer32"
_WfIpIisisAnnounceAutoTag_Object = MibTableColumn
wfIpIisisAnnounceAutoTag = _WfIpIisisAnnounceAutoTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 24),
    _WfIpIisisAnnounceAutoTag_Type()
)
wfIpIisisAnnounceAutoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceAutoTag.setStatus("mandatory")
_WfIpIisisAnnounceMetric_Type = Integer32
_WfIpIisisAnnounceMetric_Object = MibTableColumn
wfIpIisisAnnounceMetric = _WfIpIisisAnnounceMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 19, 1, 25),
    _WfIpIisisAnnounceMetric_Type()
)
wfIpIisisAnnounceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIisisAnnounceMetric.setStatus("mandatory")
_WfMTMStaticForwardTable_Object = MibTable
wfMTMStaticForwardTable = _WfMTMStaticForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20)
)
if mibBuilder.loadTexts:
    wfMTMStaticForwardTable.setStatus("mandatory")
_WfMTMStaticForwardEntry_Object = MibTableRow
wfMTMStaticForwardEntry = _WfMTMStaticForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1)
)
wfMTMStaticForwardEntry.setIndexNames(
    (0, "Wellfleet-IPPOLICY-MIB", "wfMTMStaticForwardIndex"),
)
if mibBuilder.loadTexts:
    wfMTMStaticForwardEntry.setStatus("mandatory")


class _WfMTMStaticForwardDelete_Type(Integer32):
    """Custom type wfMTMStaticForwardDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfMTMStaticForwardDelete_Type.__name__ = "Integer32"
_WfMTMStaticForwardDelete_Object = MibTableColumn
wfMTMStaticForwardDelete = _WfMTMStaticForwardDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 1),
    _WfMTMStaticForwardDelete_Type()
)
wfMTMStaticForwardDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardDelete.setStatus("mandatory")


class _WfMTMStaticForwardDisable_Type(Integer32):
    """Custom type wfMTMStaticForwardDisable based on Integer32"""
    defaultValue = 1

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


_WfMTMStaticForwardDisable_Type.__name__ = "Integer32"
_WfMTMStaticForwardDisable_Object = MibTableColumn
wfMTMStaticForwardDisable = _WfMTMStaticForwardDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 2),
    _WfMTMStaticForwardDisable_Type()
)
wfMTMStaticForwardDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardDisable.setStatus("mandatory")
_WfMTMStaticForwardIndex_Type = Integer32
_WfMTMStaticForwardIndex_Object = MibTableColumn
wfMTMStaticForwardIndex = _WfMTMStaticForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 3),
    _WfMTMStaticForwardIndex_Type()
)
wfMTMStaticForwardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMTMStaticForwardIndex.setStatus("mandatory")
_WfMTMStaticForwardName_Type = DisplayString
_WfMTMStaticForwardName_Object = MibTableColumn
wfMTMStaticForwardName = _WfMTMStaticForwardName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 4),
    _WfMTMStaticForwardName_Type()
)
wfMTMStaticForwardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardName.setStatus("mandatory")
_WfMTMStaticForwardGroups_Type = OctetString
_WfMTMStaticForwardGroups_Object = MibTableColumn
wfMTMStaticForwardGroups = _WfMTMStaticForwardGroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 5),
    _WfMTMStaticForwardGroups_Type()
)
wfMTMStaticForwardGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardGroups.setStatus("mandatory")
_WfMTMStaticForwardAction_Type = Integer32
_WfMTMStaticForwardAction_Object = MibTableColumn
wfMTMStaticForwardAction = _WfMTMStaticForwardAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 6),
    _WfMTMStaticForwardAction_Type()
)
wfMTMStaticForwardAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMTMStaticForwardAction.setStatus("mandatory")


class _WfMTMStaticForwardPreference_Type(Integer32):
    """Custom type wfMTMStaticForwardPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfMTMStaticForwardPreference_Type.__name__ = "Integer32"
_WfMTMStaticForwardPreference_Object = MibTableColumn
wfMTMStaticForwardPreference = _WfMTMStaticForwardPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 7),
    _WfMTMStaticForwardPreference_Type()
)
wfMTMStaticForwardPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardPreference.setStatus("mandatory")
_WfMTMStaticForwardPrecedence_Type = Integer32
_WfMTMStaticForwardPrecedence_Object = MibTableColumn
wfMTMStaticForwardPrecedence = _WfMTMStaticForwardPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 8),
    _WfMTMStaticForwardPrecedence_Type()
)
wfMTMStaticForwardPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardPrecedence.setStatus("mandatory")
_WfMTMStaticForwardInject_Type = OctetString
_WfMTMStaticForwardInject_Object = MibTableColumn
wfMTMStaticForwardInject = _WfMTMStaticForwardInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 9),
    _WfMTMStaticForwardInject_Type()
)
wfMTMStaticForwardInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMTMStaticForwardInject.setStatus("mandatory")
_WfMTMStaticForwardSources_Type = OctetString
_WfMTMStaticForwardSources_Object = MibTableColumn
wfMTMStaticForwardSources = _WfMTMStaticForwardSources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 10),
    _WfMTMStaticForwardSources_Type()
)
wfMTMStaticForwardSources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardSources.setStatus("mandatory")
_WfMTMStaticForwardInCircuits_Type = OctetString
_WfMTMStaticForwardInCircuits_Object = MibTableColumn
wfMTMStaticForwardInCircuits = _WfMTMStaticForwardInCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 11),
    _WfMTMStaticForwardInCircuits_Type()
)
wfMTMStaticForwardInCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardInCircuits.setStatus("mandatory")
_WfMTMStaticForwardOutCircuits_Type = OctetString
_WfMTMStaticForwardOutCircuits_Object = MibTableColumn
wfMTMStaticForwardOutCircuits = _WfMTMStaticForwardOutCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 12),
    _WfMTMStaticForwardOutCircuits_Type()
)
wfMTMStaticForwardOutCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardOutCircuits.setStatus("mandatory")


class _WfMTMStaticForwardMode_Type(Integer32):
    """Custom type wfMTMStaticForwardMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamictostatic", 4),
          ("static", 2),
          ("statictodynamic", 3))
    )


_WfMTMStaticForwardMode_Type.__name__ = "Integer32"
_WfMTMStaticForwardMode_Object = MibTableColumn
wfMTMStaticForwardMode = _WfMTMStaticForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6, 20, 1, 13),
    _WfMTMStaticForwardMode_Type()
)
wfMTMStaticForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMTMStaticForwardMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IPPOLICY-MIB",
    **{"wfIpRipAcceptTable": wfIpRipAcceptTable,
       "wfIpRipAcceptEntry": wfIpRipAcceptEntry,
       "wfIpRipAcceptDelete": wfIpRipAcceptDelete,
       "wfIpRipAcceptDisable": wfIpRipAcceptDisable,
       "wfIpRipAcceptIndex": wfIpRipAcceptIndex,
       "wfIpRipAcceptName": wfIpRipAcceptName,
       "wfIpRipAcceptNetworks": wfIpRipAcceptNetworks,
       "wfIpRipAcceptAction": wfIpRipAcceptAction,
       "wfIpRipAcceptPreference": wfIpRipAcceptPreference,
       "wfIpRipAcceptPrecedence": wfIpRipAcceptPrecedence,
       "wfIpRipAcceptInject": wfIpRipAcceptInject,
       "wfIpRipAcceptGateway": wfIpRipAcceptGateway,
       "wfIpRipAcceptInterface": wfIpRipAcceptInterface,
       "wfIpRipAcceptApplyMask": wfIpRipAcceptApplyMask,
       "wfIpRipAnnounceTable": wfIpRipAnnounceTable,
       "wfIpRipAnnounceEntry": wfIpRipAnnounceEntry,
       "wfIpRipAnnounceDelete": wfIpRipAnnounceDelete,
       "wfIpRipAnnounceDisable": wfIpRipAnnounceDisable,
       "wfIpRipAnnounceIndex": wfIpRipAnnounceIndex,
       "wfIpRipAnnounceName": wfIpRipAnnounceName,
       "wfIpRipAnnounceNetworks": wfIpRipAnnounceNetworks,
       "wfIpRipAnnounceAction": wfIpRipAnnounceAction,
       "wfIpRipAnnouncePrecedence": wfIpRipAnnouncePrecedence,
       "wfIpRipAnnounceRouteSource": wfIpRipAnnounceRouteSource,
       "wfIpRipAnnounceExtRouteSource": wfIpRipAnnounceExtRouteSource,
       "wfIpRipAnnounceAdvertise": wfIpRipAnnounceAdvertise,
       "wfIpRipAnnounceRipGateway": wfIpRipAnnounceRipGateway,
       "wfIpRipAnnounceRipInterface": wfIpRipAnnounceRipInterface,
       "wfIpRipAnnounceOspfRouterId": wfIpRipAnnounceOspfRouterId,
       "wfIpRipAnnounceOspfType": wfIpRipAnnounceOspfType,
       "wfIpRipAnnounceOspfTag": wfIpRipAnnounceOspfTag,
       "wfIpRipAnnounceEgpPeer": wfIpRipAnnounceEgpPeer,
       "wfIpRipAnnounceEgpPeerAs": wfIpRipAnnounceEgpPeerAs,
       "wfIpRipAnnounceEgpGateway": wfIpRipAnnounceEgpGateway,
       "wfIpRipAnnounceBgpPeer": wfIpRipAnnounceBgpPeer,
       "wfIpRipAnnounceBgpPeerAs": wfIpRipAnnounceBgpPeerAs,
       "wfIpRipAnnounceBgpNextHop": wfIpRipAnnounceBgpNextHop,
       "wfIpRipAnnounceInterface": wfIpRipAnnounceInterface,
       "wfIpRipAnnounceRipMetric": wfIpRipAnnounceRipMetric,
       "wfIpOspfAcceptTable": wfIpOspfAcceptTable,
       "wfIpOspfAcceptEntry": wfIpOspfAcceptEntry,
       "wfIpOspfAcceptDelete": wfIpOspfAcceptDelete,
       "wfIpOspfAcceptDisable": wfIpOspfAcceptDisable,
       "wfIpOspfAcceptIndex": wfIpOspfAcceptIndex,
       "wfIpOspfAcceptName": wfIpOspfAcceptName,
       "wfIpOspfAcceptNetworks": wfIpOspfAcceptNetworks,
       "wfIpOspfAcceptAction": wfIpOspfAcceptAction,
       "wfIpOspfAcceptPreference": wfIpOspfAcceptPreference,
       "wfIpOspfAcceptPrecedence": wfIpOspfAcceptPrecedence,
       "wfIpOspfAcceptInject": wfIpOspfAcceptInject,
       "wfIpOspfAcceptType": wfIpOspfAcceptType,
       "wfIpOspfAcceptTag": wfIpOspfAcceptTag,
       "wfIpOspfAnnounceTable": wfIpOspfAnnounceTable,
       "wfIpOspfAnnounceEntry": wfIpOspfAnnounceEntry,
       "wfIpOspfAnnounceDelete": wfIpOspfAnnounceDelete,
       "wfIpOspfAnnounceDisable": wfIpOspfAnnounceDisable,
       "wfIpOspfAnnounceIndex": wfIpOspfAnnounceIndex,
       "wfIpOspfAnnounceName": wfIpOspfAnnounceName,
       "wfIpOspfAnnounceNetworks": wfIpOspfAnnounceNetworks,
       "wfIpOspfAnnounceAction": wfIpOspfAnnounceAction,
       "wfIpOspfAnnouncePrecedence": wfIpOspfAnnouncePrecedence,
       "wfIpOspfAnnounceRouteSource": wfIpOspfAnnounceRouteSource,
       "wfIpOspfAnnounceExtRouteSource": wfIpOspfAnnounceExtRouteSource,
       "wfIpOspfAnnounceAdvertise": wfIpOspfAnnounceAdvertise,
       "wfIpOspfAnnounceRipGateway": wfIpOspfAnnounceRipGateway,
       "wfIpOspfAnnounceRipInterface": wfIpOspfAnnounceRipInterface,
       "wfIpOspfAnnounceOspfRouterId": wfIpOspfAnnounceOspfRouterId,
       "wfIpOspfAnnounceOspfType": wfIpOspfAnnounceOspfType,
       "wfIpOspfAnnounceOspfTag": wfIpOspfAnnounceOspfTag,
       "wfIpOspfAnnounceEgpPeer": wfIpOspfAnnounceEgpPeer,
       "wfIpOspfAnnounceEgpPeerAs": wfIpOspfAnnounceEgpPeerAs,
       "wfIpOspfAnnounceEgpGateway": wfIpOspfAnnounceEgpGateway,
       "wfIpOspfAnnounceBgpPeer": wfIpOspfAnnounceBgpPeer,
       "wfIpOspfAnnounceBgpPeerAs": wfIpOspfAnnounceBgpPeerAs,
       "wfIpOspfAnnounceBgpNextHop": wfIpOspfAnnounceBgpNextHop,
       "wfIpOspfAnnounceType": wfIpOspfAnnounceType,
       "wfIpOspfAnnounceTag": wfIpOspfAnnounceTag,
       "wfIpOspfAnnounceAutoTag": wfIpOspfAnnounceAutoTag,
       "wfIpOspfAnnounceMetric": wfIpOspfAnnounceMetric,
       "wfIpOspfAnnounceNssaPropagate": wfIpOspfAnnounceNssaPropagate,
       "wfIpEgpAcceptTable": wfIpEgpAcceptTable,
       "wfIpEgpAcceptEntry": wfIpEgpAcceptEntry,
       "wfIpEgpAcceptDelete": wfIpEgpAcceptDelete,
       "wfIpEgpAcceptDisable": wfIpEgpAcceptDisable,
       "wfIpEgpAcceptIndex": wfIpEgpAcceptIndex,
       "wfIpEgpAcceptName": wfIpEgpAcceptName,
       "wfIpEgpAcceptNetworks": wfIpEgpAcceptNetworks,
       "wfIpEgpAcceptAction": wfIpEgpAcceptAction,
       "wfIpEgpAcceptPreference": wfIpEgpAcceptPreference,
       "wfIpEgpAcceptPrecedence": wfIpEgpAcceptPrecedence,
       "wfIpEgpAcceptInject": wfIpEgpAcceptInject,
       "wfIpEgpAcceptPeer": wfIpEgpAcceptPeer,
       "wfIpEgpAcceptAs": wfIpEgpAcceptAs,
       "wfIpEgpAcceptGateway": wfIpEgpAcceptGateway,
       "wfIpEgpAnnounceTable": wfIpEgpAnnounceTable,
       "wfIpEgpAnnounceEntry": wfIpEgpAnnounceEntry,
       "wfIpEgpAnnounceDelete": wfIpEgpAnnounceDelete,
       "wfIpEgpAnnounceDisable": wfIpEgpAnnounceDisable,
       "wfIpEgpAnnounceIndex": wfIpEgpAnnounceIndex,
       "wfIpEgpAnnounceName": wfIpEgpAnnounceName,
       "wfIpEgpAnnounceNetworks": wfIpEgpAnnounceNetworks,
       "wfIpEgpAnnounceAction": wfIpEgpAnnounceAction,
       "wfIpEgpAnnouncePrecedence": wfIpEgpAnnouncePrecedence,
       "wfIpEgpAnnounceRouteSource": wfIpEgpAnnounceRouteSource,
       "wfIpEgpAnnounceExtRouteSource": wfIpEgpAnnounceExtRouteSource,
       "wfIpEgpAnnounceAdvertise": wfIpEgpAnnounceAdvertise,
       "wfIpEgpAnnounceRipGateway": wfIpEgpAnnounceRipGateway,
       "wfIpEgpAnnounceRipInterface": wfIpEgpAnnounceRipInterface,
       "wfIpEgpAnnounceOspfRouterId": wfIpEgpAnnounceOspfRouterId,
       "wfIpEgpAnnounceOspfType": wfIpEgpAnnounceOspfType,
       "wfIpEgpAnnounceOspfTag": wfIpEgpAnnounceOspfTag,
       "wfIpEgpAnnounceEgpPeer": wfIpEgpAnnounceEgpPeer,
       "wfIpEgpAnnounceEgpPeerAs": wfIpEgpAnnounceEgpPeerAs,
       "wfIpEgpAnnounceEgpGateway": wfIpEgpAnnounceEgpGateway,
       "wfIpEgpAnnounceBgpPeer": wfIpEgpAnnounceBgpPeer,
       "wfIpEgpAnnounceBgpPeerAs": wfIpEgpAnnounceBgpPeerAs,
       "wfIpEgpAnnounceBgpNextHop": wfIpEgpAnnounceBgpNextHop,
       "wfIpEgpAnnouncePeer": wfIpEgpAnnouncePeer,
       "wfIpEgpAnnounceInterface": wfIpEgpAnnounceInterface,
       "wfIpEgpAnnounceMetric": wfIpEgpAnnounceMetric,
       "wfIpBgp3AcceptTable": wfIpBgp3AcceptTable,
       "wfIpBgp3AcceptEntry": wfIpBgp3AcceptEntry,
       "wfIpBgp3AcceptDelete": wfIpBgp3AcceptDelete,
       "wfIpBgp3AcceptDisable": wfIpBgp3AcceptDisable,
       "wfIpBgp3AcceptIndex": wfIpBgp3AcceptIndex,
       "wfIpBgp3AcceptName": wfIpBgp3AcceptName,
       "wfIpBgp3AcceptNetworks": wfIpBgp3AcceptNetworks,
       "wfIpBgp3AcceptAction": wfIpBgp3AcceptAction,
       "wfIpBgp3AcceptPreference": wfIpBgp3AcceptPreference,
       "wfIpBgp3AcceptPrecedence": wfIpBgp3AcceptPrecedence,
       "wfIpBgp3AcceptInject": wfIpBgp3AcceptInject,
       "wfIpBgp3AcceptPeerAs": wfIpBgp3AcceptPeerAs,
       "wfIpBgp3AcceptPeerAddress": wfIpBgp3AcceptPeerAddress,
       "wfIpBgp3AcceptOrigAs": wfIpBgp3AcceptOrigAs,
       "wfIpBgp3AcceptRouteOrigin": wfIpBgp3AcceptRouteOrigin,
       "wfIpBgp3AcceptBgp3Preference": wfIpBgp3AcceptBgp3Preference,
       "wfIpBgp3AcceptAsWeightClass": wfIpBgp3AcceptAsWeightClass,
       "wfIpBgp3AcceptCommunityMatch": wfIpBgp3AcceptCommunityMatch,
       "wfIpBgp3AnnounceTable": wfIpBgp3AnnounceTable,
       "wfIpBgp3AnnounceEntry": wfIpBgp3AnnounceEntry,
       "wfIpBgp3AnnounceDelete": wfIpBgp3AnnounceDelete,
       "wfIpBgp3AnnounceDisable": wfIpBgp3AnnounceDisable,
       "wfIpBgp3AnnounceIndex": wfIpBgp3AnnounceIndex,
       "wfIpBgp3AnnounceName": wfIpBgp3AnnounceName,
       "wfIpBgp3AnnounceNetworks": wfIpBgp3AnnounceNetworks,
       "wfIpBgp3AnnounceAction": wfIpBgp3AnnounceAction,
       "wfIpBgp3AnnouncePrecedence": wfIpBgp3AnnouncePrecedence,
       "wfIpBgp3AnnounceRouteSource": wfIpBgp3AnnounceRouteSource,
       "wfIpBgp3AnnounceExtRouteSource": wfIpBgp3AnnounceExtRouteSource,
       "wfIpBgp3AnnounceAdvertise": wfIpBgp3AnnounceAdvertise,
       "wfIpBgp3AnnounceRipGateway": wfIpBgp3AnnounceRipGateway,
       "wfIpBgp3AnnounceRipInterface": wfIpBgp3AnnounceRipInterface,
       "wfIpBgp3AnnounceOspfRouterId": wfIpBgp3AnnounceOspfRouterId,
       "wfIpBgp3AnnounceOspfType": wfIpBgp3AnnounceOspfType,
       "wfIpBgp3AnnounceOspfTag": wfIpBgp3AnnounceOspfTag,
       "wfIpBgp3AnnounceEgpPeer": wfIpBgp3AnnounceEgpPeer,
       "wfIpBgp3AnnounceEgpPeerAs": wfIpBgp3AnnounceEgpPeerAs,
       "wfIpBgp3AnnounceEgpGateway": wfIpBgp3AnnounceEgpGateway,
       "wfIpBgp3AnnounceBgpPeer": wfIpBgp3AnnounceBgpPeer,
       "wfIpBgp3AnnounceBgpPeerAs": wfIpBgp3AnnounceBgpPeerAs,
       "wfIpBgp3AnnounceBgpNextHop": wfIpBgp3AnnounceBgpNextHop,
       "wfIpBgp3AnnouncePeerAs": wfIpBgp3AnnouncePeerAs,
       "wfIpBgp3AnnouncePeer": wfIpBgp3AnnouncePeer,
       "wfIpBgp3AnnounceUseMetric": wfIpBgp3AnnounceUseMetric,
       "wfIpBgp3AnnounceInterAsMetric": wfIpBgp3AnnounceInterAsMetric,
       "wfIpBgp3AnnounceOrigin": wfIpBgp3AnnounceOrigin,
       "wfIpBgp3AnnounceAsPath": wfIpBgp3AnnounceAsPath,
       "wfIpBgp3AnnounceNextHop": wfIpBgp3AnnounceNextHop,
       "wfIpBgp3AnnounceCommunity": wfIpBgp3AnnounceCommunity,
       "wfIpBgp3AnnounceCommunityAction": wfIpBgp3AnnounceCommunityAction,
       "wfIpBgp3AnnounceCommunityMatch": wfIpBgp3AnnounceCommunityMatch,
       "wfIpBgp4AcceptTable": wfIpBgp4AcceptTable,
       "wfIpBgp4AcceptEntry": wfIpBgp4AcceptEntry,
       "wfIpBgp4AcceptDelete": wfIpBgp4AcceptDelete,
       "wfIpBgp4AcceptDisable": wfIpBgp4AcceptDisable,
       "wfIpBgp4AcceptIndex": wfIpBgp4AcceptIndex,
       "wfIpBgp4AcceptName": wfIpBgp4AcceptName,
       "wfIpBgp4AcceptNetworks": wfIpBgp4AcceptNetworks,
       "wfIpBgp4AcceptAction": wfIpBgp4AcceptAction,
       "wfIpBgp4AcceptPreference": wfIpBgp4AcceptPreference,
       "wfIpBgp4AcceptPrecedence": wfIpBgp4AcceptPrecedence,
       "wfIpBgp4AcceptInject": wfIpBgp4AcceptInject,
       "wfIpBgp4AcceptPeerAs": wfIpBgp4AcceptPeerAs,
       "wfIpBgp4AcceptPeerAddress": wfIpBgp4AcceptPeerAddress,
       "wfIpBgp4AcceptOrigAs": wfIpBgp4AcceptOrigAs,
       "wfIpBgp4AcceptRouteOrigin": wfIpBgp4AcceptRouteOrigin,
       "wfIpBgp4AcceptAggrAs": wfIpBgp4AcceptAggrAs,
       "wfIpBgp4AcceptAggrRouter": wfIpBgp4AcceptAggrRouter,
       "wfIpBgp4AcceptLocalPref": wfIpBgp4AcceptLocalPref,
       "wfIpBgp4AcceptBgp4Preference": wfIpBgp4AcceptBgp4Preference,
       "wfIpBgp4AcceptAsWeightClass": wfIpBgp4AcceptAsWeightClass,
       "wfIpBgp4AcceptAsPatternMatch": wfIpBgp4AcceptAsPatternMatch,
       "wfIpBgp4AcceptCommunityMatch": wfIpBgp4AcceptCommunityMatch,
       "wfIpBgp4AcceptUseMultiExitDisc": wfIpBgp4AcceptUseMultiExitDisc,
       "wfIpBgp4AcceptMultiExitDisc": wfIpBgp4AcceptMultiExitDisc,
       "wfIpBgp4AcceptAsPrepend": wfIpBgp4AcceptAsPrepend,
       "wfIpBgp4AcceptCommunity": wfIpBgp4AcceptCommunity,
       "wfIpBgp4AcceptCommunityAction": wfIpBgp4AcceptCommunityAction,
       "wfIpBgp4AcceptRFDampeningEnable": wfIpBgp4AcceptRFDampeningEnable,
       "wfIpBgp4AcceptRFDampeningTemplate": wfIpBgp4AcceptRFDampeningTemplate,
       "wfIpBgp4AnnounceTable": wfIpBgp4AnnounceTable,
       "wfIpBgp4AnnounceEntry": wfIpBgp4AnnounceEntry,
       "wfIpBgp4AnnounceDelete": wfIpBgp4AnnounceDelete,
       "wfIpBgp4AnnounceDisable": wfIpBgp4AnnounceDisable,
       "wfIpBgp4AnnounceIndex": wfIpBgp4AnnounceIndex,
       "wfIpBgp4AnnounceName": wfIpBgp4AnnounceName,
       "wfIpBgp4AnnounceNetworks": wfIpBgp4AnnounceNetworks,
       "wfIpBgp4AnnounceAction": wfIpBgp4AnnounceAction,
       "wfIpBgp4AnnouncePrecedence": wfIpBgp4AnnouncePrecedence,
       "wfIpBgp4AnnounceRouteSource": wfIpBgp4AnnounceRouteSource,
       "wfIpBgp4AnnounceExtRouteSource": wfIpBgp4AnnounceExtRouteSource,
       "wfIpBgp4AnnounceAdvertise": wfIpBgp4AnnounceAdvertise,
       "wfIpBgp4AnnounceRipGateway": wfIpBgp4AnnounceRipGateway,
       "wfIpBgp4AnnounceRipInterface": wfIpBgp4AnnounceRipInterface,
       "wfIpBgp4AnnounceOspfRouterId": wfIpBgp4AnnounceOspfRouterId,
       "wfIpBgp4AnnounceOspfType": wfIpBgp4AnnounceOspfType,
       "wfIpBgp4AnnounceOspfTag": wfIpBgp4AnnounceOspfTag,
       "wfIpBgp4AnnounceEgpPeer": wfIpBgp4AnnounceEgpPeer,
       "wfIpBgp4AnnounceEgpPeerAs": wfIpBgp4AnnounceEgpPeerAs,
       "wfIpBgp4AnnounceEgpGateway": wfIpBgp4AnnounceEgpGateway,
       "wfIpBgp4AnnounceBgpPeer": wfIpBgp4AnnounceBgpPeer,
       "wfIpBgp4AnnounceBgpPeerAs": wfIpBgp4AnnounceBgpPeerAs,
       "wfIpBgp4AnnounceBgpNextHop": wfIpBgp4AnnounceBgpNextHop,
       "wfIpBgp4AnnouncePeerAs": wfIpBgp4AnnouncePeerAs,
       "wfIpBgp4AnnouncePeer": wfIpBgp4AnnouncePeer,
       "wfIpBgp4AnnounceUseMultiExitDisc": wfIpBgp4AnnounceUseMultiExitDisc,
       "wfIpBgp4AnnounceMultiExitDisc": wfIpBgp4AnnounceMultiExitDisc,
       "wfIpBgp4AnnounceOrigin": wfIpBgp4AnnounceOrigin,
       "wfIpBgp4AnnounceAsPath": wfIpBgp4AnnounceAsPath,
       "wfIpBgp4AnnounceLocalPrefOverride": wfIpBgp4AnnounceLocalPrefOverride,
       "wfIpBgp4AnnounceLocalPref": wfIpBgp4AnnounceLocalPref,
       "wfIpBgp4AnnounceNextHop": wfIpBgp4AnnounceNextHop,
       "wfIpBgp4AnnounceAtomic": wfIpBgp4AnnounceAtomic,
       "wfIpBgp4AnnounceAsPatternMatch": wfIpBgp4AnnounceAsPatternMatch,
       "wfIpBgp4AnnounceCommunity": wfIpBgp4AnnounceCommunity,
       "wfIpBgp4AnnounceCommunityAction": wfIpBgp4AnnounceCommunityAction,
       "wfIpBgp4AnnounceCommunityMatch": wfIpBgp4AnnounceCommunityMatch,
       "wfIpBgp4AnnounceAsPrepend": wfIpBgp4AnnounceAsPrepend,
       "wfIpIgmpGroupPolicyTable": wfIpIgmpGroupPolicyTable,
       "wfIpIgmpGroupPolicyEntry": wfIpIgmpGroupPolicyEntry,
       "wfIpIgmpGroupPolicyDelete": wfIpIgmpGroupPolicyDelete,
       "wfIpIgmpGroupPolicyDisable": wfIpIgmpGroupPolicyDisable,
       "wfIpIgmpGroupPolicyIndex": wfIpIgmpGroupPolicyIndex,
       "wfIpIgmpGroupPolicyName": wfIpIgmpGroupPolicyName,
       "wfIpIgmpGroupPolicySources": wfIpIgmpGroupPolicySources,
       "wfIpIgmpGroupPolicyAction": wfIpIgmpGroupPolicyAction,
       "wfIpIgmpGroupPolicyPreference": wfIpIgmpGroupPolicyPreference,
       "wfIpIgmpGroupPolicyPrecedence": wfIpIgmpGroupPolicyPrecedence,
       "wfIpIgmpGroupPolicyInject": wfIpIgmpGroupPolicyInject,
       "wfIpIgmpGroupPolicyGroups": wfIpIgmpGroupPolicyGroups,
       "wfIpIgmpGroupPolicyCircuits": wfIpIgmpGroupPolicyCircuits,
       "wfIpIgmpGroupPolicySenders": wfIpIgmpGroupPolicySenders,
       "wfMTMStaticFwdTable": wfMTMStaticFwdTable,
       "wfMTMStaticFwdEntry": wfMTMStaticFwdEntry,
       "wfMTMStaticFwdDelete": wfMTMStaticFwdDelete,
       "wfMTMStaticFwdDisable": wfMTMStaticFwdDisable,
       "wfMTMStaticFwdIndex": wfMTMStaticFwdIndex,
       "wfMTMStaticFwdName": wfMTMStaticFwdName,
       "wfMTMStaticFwdGroups": wfMTMStaticFwdGroups,
       "wfMTMStaticFwdAction": wfMTMStaticFwdAction,
       "wfMTMStaticFwdPreference": wfMTMStaticFwdPreference,
       "wfMTMStaticFwdPrecedence": wfMTMStaticFwdPrecedence,
       "wfMTMStaticFwdInject": wfMTMStaticFwdInject,
       "wfMTMStaticFwdSources": wfMTMStaticFwdSources,
       "wfMTMStaticFwdInCircuits": wfMTMStaticFwdInCircuits,
       "wfMTMStaticFwdOutCircuits": wfMTMStaticFwdOutCircuits,
       "wfMTMStaticFwdMode": wfMTMStaticFwdMode,
       "wfIpMospfAcceptTable": wfIpMospfAcceptTable,
       "wfIpMospfAcceptEntry": wfIpMospfAcceptEntry,
       "wfIpMospfAcceptDelete": wfIpMospfAcceptDelete,
       "wfIpMospfAcceptDisable": wfIpMospfAcceptDisable,
       "wfIpMospfAcceptIndex": wfIpMospfAcceptIndex,
       "wfIpMospfAcceptName": wfIpMospfAcceptName,
       "wfIpMospfAcceptNetworks": wfIpMospfAcceptNetworks,
       "wfIpMospfAcceptAction": wfIpMospfAcceptAction,
       "wfIpMospfAcceptPreference": wfIpMospfAcceptPreference,
       "wfIpMospfAcceptPrecedence": wfIpMospfAcceptPrecedence,
       "wfIpMospfAcceptInject": wfIpMospfAcceptInject,
       "wfIpMospfAcceptGateway": wfIpMospfAcceptGateway,
       "wfIpMospfAcceptInterface": wfIpMospfAcceptInterface,
       "wfIpMospfAcceptApplyMask": wfIpMospfAcceptApplyMask,
       "wfIpMospfAnnounceTable": wfIpMospfAnnounceTable,
       "wfIpMospfAnnounceEntry": wfIpMospfAnnounceEntry,
       "wfIpMospfAnnounceDelete": wfIpMospfAnnounceDelete,
       "wfIpMospfAnnounceDisable": wfIpMospfAnnounceDisable,
       "wfIpMospfAnnounceIndex": wfIpMospfAnnounceIndex,
       "wfIpMospfAnnounceName": wfIpMospfAnnounceName,
       "wfIpMospfAnnounceNetworks": wfIpMospfAnnounceNetworks,
       "wfIpMospfAnnounceAction": wfIpMospfAnnounceAction,
       "wfIpMospfAnnouncePrecedence": wfIpMospfAnnouncePrecedence,
       "wfIpMospfAnnounceRouteSource": wfIpMospfAnnounceRouteSource,
       "wfIpMospfAnnounceExtRouteSource": wfIpMospfAnnounceExtRouteSource,
       "wfIpMospfAnnounceAdvertise": wfIpMospfAnnounceAdvertise,
       "wfIpMospfAnnounceRipGateway": wfIpMospfAnnounceRipGateway,
       "wfIpMospfAnnounceRipInterface": wfIpMospfAnnounceRipInterface,
       "wfIpMospfAnnounceOspfRouterId": wfIpMospfAnnounceOspfRouterId,
       "wfIpMospfAnnounceOspfType": wfIpMospfAnnounceOspfType,
       "wfIpMospfAnnounceOspfTag": wfIpMospfAnnounceOspfTag,
       "wfIpMospfAnnounceEgpPeer": wfIpMospfAnnounceEgpPeer,
       "wfIpMospfAnnounceEgpPeerAs": wfIpMospfAnnounceEgpPeerAs,
       "wfIpMospfAnnounceEgpGateway": wfIpMospfAnnounceEgpGateway,
       "wfIpMospfAnnounceBgpPeer": wfIpMospfAnnounceBgpPeer,
       "wfIpMospfAnnounceBgpPeerAs": wfIpMospfAnnounceBgpPeerAs,
       "wfIpMospfAnnounceBgpNextHop": wfIpMospfAnnounceBgpNextHop,
       "wfIpDvmrpAcceptTable": wfIpDvmrpAcceptTable,
       "wfIpDvmrpAcceptEntry": wfIpDvmrpAcceptEntry,
       "wfIpDvmrpAcceptDelete": wfIpDvmrpAcceptDelete,
       "wfIpDvmrpAcceptDisable": wfIpDvmrpAcceptDisable,
       "wfIpDvmrpAcceptIndex": wfIpDvmrpAcceptIndex,
       "wfIpDvmrpAcceptName": wfIpDvmrpAcceptName,
       "wfIpDvmrpAcceptNetworks": wfIpDvmrpAcceptNetworks,
       "wfIpDvmrpAcceptAction": wfIpDvmrpAcceptAction,
       "wfIpDvmrpAcceptPreference": wfIpDvmrpAcceptPreference,
       "wfIpDvmrpAcceptPrecedence": wfIpDvmrpAcceptPrecedence,
       "wfIpDvmrpAcceptInject": wfIpDvmrpAcceptInject,
       "wfIpDvmrpAcceptGateway": wfIpDvmrpAcceptGateway,
       "wfIpDvmrpAcceptInterface": wfIpDvmrpAcceptInterface,
       "wfIpDvmrpAcceptApplyMask": wfIpDvmrpAcceptApplyMask,
       "wfIpDvmrpAcceptTunnels": wfIpDvmrpAcceptTunnels,
       "wfIpDvmrpAcceptInjectMetric": wfIpDvmrpAcceptInjectMetric,
       "wfIpDvmrpAnnounceTable": wfIpDvmrpAnnounceTable,
       "wfIpDvmrpAnnounceEntry": wfIpDvmrpAnnounceEntry,
       "wfIpDvmrpAnnounceDelete": wfIpDvmrpAnnounceDelete,
       "wfIpDvmrpAnnounceDisable": wfIpDvmrpAnnounceDisable,
       "wfIpDvmrpAnnounceIndex": wfIpDvmrpAnnounceIndex,
       "wfIpDvmrpAnnounceName": wfIpDvmrpAnnounceName,
       "wfIpDvmrpAnnounceNetworks": wfIpDvmrpAnnounceNetworks,
       "wfIpDvmrpAnnounceAction": wfIpDvmrpAnnounceAction,
       "wfIpDvmrpAnnouncePrecedence": wfIpDvmrpAnnouncePrecedence,
       "wfIpDvmrpAnnounceRouteSource": wfIpDvmrpAnnounceRouteSource,
       "wfIpDvmrpAnnounceExtRouteSource": wfIpDvmrpAnnounceExtRouteSource,
       "wfIpDvmrpAnnounceAdvertise": wfIpDvmrpAnnounceAdvertise,
       "wfIpDvmrpAnnounceRipGateway": wfIpDvmrpAnnounceRipGateway,
       "wfIpDvmrpAnnounceRipInterface": wfIpDvmrpAnnounceRipInterface,
       "wfIpDvmrpAnnounceOspfRouterId": wfIpDvmrpAnnounceOspfRouterId,
       "wfIpDvmrpAnnounceOspfType": wfIpDvmrpAnnounceOspfType,
       "wfIpDvmrpAnnounceOspfTag": wfIpDvmrpAnnounceOspfTag,
       "wfIpDvmrpAnnounceEgpPeer": wfIpDvmrpAnnounceEgpPeer,
       "wfIpDvmrpAnnounceEgpPeerAs": wfIpDvmrpAnnounceEgpPeerAs,
       "wfIpDvmrpAnnounceEgpGateway": wfIpDvmrpAnnounceEgpGateway,
       "wfIpDvmrpAnnounceBgpPeer": wfIpDvmrpAnnounceBgpPeer,
       "wfIpDvmrpAnnounceBgpPeerAs": wfIpDvmrpAnnounceBgpPeerAs,
       "wfIpDvmrpAnnounceBgpNextHop": wfIpDvmrpAnnounceBgpNextHop,
       "wfIpDvmrpAnnounceCircuits": wfIpDvmrpAnnounceCircuits,
       "wfIpDvmrpAnnounceTunnels": wfIpDvmrpAnnounceTunnels,
       "wfIpDvmrpAnnounceMetric": wfIpDvmrpAnnounceMetric,
       "wfIpDvmrpAnnounceInterface": wfIpDvmrpAnnounceInterface,
       "wfIpDvmrpInjectRtTable": wfIpDvmrpInjectRtTable,
       "wfIpDvmrpInjectRtEntry": wfIpDvmrpInjectRtEntry,
       "wfIpDvmrpInjectRtDelete": wfIpDvmrpInjectRtDelete,
       "wfIpDvmrpInjectRtDisable": wfIpDvmrpInjectRtDisable,
       "wfIpDvmrpInjectRtIndex": wfIpDvmrpInjectRtIndex,
       "wfIpDvmrpInjectRtName": wfIpDvmrpInjectRtName,
       "wfIpDvmrpInjectRtNetworks": wfIpDvmrpInjectRtNetworks,
       "wfIpDvmrpInjectRtAction": wfIpDvmrpInjectRtAction,
       "wfIpDvmrpInjectRtPreference": wfIpDvmrpInjectRtPreference,
       "wfIpDvmrpInjectRtPrecedence": wfIpDvmrpInjectRtPrecedence,
       "wfIpDvmrpInjectRtInject": wfIpDvmrpInjectRtInject,
       "wfIpDvmrpInjectRtInInterface": wfIpDvmrpInjectRtInInterface,
       "wfIpDvmrpInjectRtType": wfIpDvmrpInjectRtType,
       "wfIpDvmrpInjectRtMetric": wfIpDvmrpInjectRtMetric,
       "wfIpIisisAcceptTable": wfIpIisisAcceptTable,
       "wfIpIisisAcceptEntry": wfIpIisisAcceptEntry,
       "wfIpIisisAcceptDelete": wfIpIisisAcceptDelete,
       "wfIpIisisAcceptDisable": wfIpIisisAcceptDisable,
       "wfIpIisisAcceptIndex": wfIpIisisAcceptIndex,
       "wfIpIisisAcceptName": wfIpIisisAcceptName,
       "wfIpIisisAcceptNetworks": wfIpIisisAcceptNetworks,
       "wfIpIisisAcceptAction": wfIpIisisAcceptAction,
       "wfIpIisisAcceptPreference": wfIpIisisAcceptPreference,
       "wfIpIisisAcceptPrecedence": wfIpIisisAcceptPrecedence,
       "wfIpIisisAcceptInject": wfIpIisisAcceptInject,
       "wfIpIisisAcceptType": wfIpIisisAcceptType,
       "wfIpIisisAnnounceTable": wfIpIisisAnnounceTable,
       "wfIpIisisAnnounceEntry": wfIpIisisAnnounceEntry,
       "wfIpIisisAnnounceDelete": wfIpIisisAnnounceDelete,
       "wfIpIisisAnnounceDisable": wfIpIisisAnnounceDisable,
       "wfIpIisisAnnounceIndex": wfIpIisisAnnounceIndex,
       "wfIpIisisAnnounceName": wfIpIisisAnnounceName,
       "wfIpIisisAnnounceNetworks": wfIpIisisAnnounceNetworks,
       "wfIpIisisAnnounceAction": wfIpIisisAnnounceAction,
       "wfIpIisisAnnouncePrecedence": wfIpIisisAnnouncePrecedence,
       "wfIpIisisAnnounceRouteSource": wfIpIisisAnnounceRouteSource,
       "wfIpIisisAnnounceExtRouteSource": wfIpIisisAnnounceExtRouteSource,
       "wfIpIisisAnnounceAdvertise": wfIpIisisAnnounceAdvertise,
       "wfIpIisisAnnounceRipGateway": wfIpIisisAnnounceRipGateway,
       "wfIpIisisAnnounceRipInterface": wfIpIisisAnnounceRipInterface,
       "wfIpIisisAnnounceIisisRouterId": wfIpIisisAnnounceIisisRouterId,
       "wfIpIisisAnnounceIisisType": wfIpIisisAnnounceIisisType,
       "wfIpIisisAnnounceIisisTag": wfIpIisisAnnounceIisisTag,
       "wfIpIisisAnnounceEgpPeer": wfIpIisisAnnounceEgpPeer,
       "wfIpIisisAnnounceEgpPeerAs": wfIpIisisAnnounceEgpPeerAs,
       "wfIpIisisAnnounceEgpGateway": wfIpIisisAnnounceEgpGateway,
       "wfIpIisisAnnounceBgpPeer": wfIpIisisAnnounceBgpPeer,
       "wfIpIisisAnnounceBgpPeerAs": wfIpIisisAnnounceBgpPeerAs,
       "wfIpIisisAnnounceBgpNextHop": wfIpIisisAnnounceBgpNextHop,
       "wfIpIisisAnnounceType": wfIpIisisAnnounceType,
       "wfIpIisisAnnounceTag": wfIpIisisAnnounceTag,
       "wfIpIisisAnnounceAutoTag": wfIpIisisAnnounceAutoTag,
       "wfIpIisisAnnounceMetric": wfIpIisisAnnounceMetric,
       "wfMTMStaticForwardTable": wfMTMStaticForwardTable,
       "wfMTMStaticForwardEntry": wfMTMStaticForwardEntry,
       "wfMTMStaticForwardDelete": wfMTMStaticForwardDelete,
       "wfMTMStaticForwardDisable": wfMTMStaticForwardDisable,
       "wfMTMStaticForwardIndex": wfMTMStaticForwardIndex,
       "wfMTMStaticForwardName": wfMTMStaticForwardName,
       "wfMTMStaticForwardGroups": wfMTMStaticForwardGroups,
       "wfMTMStaticForwardAction": wfMTMStaticForwardAction,
       "wfMTMStaticForwardPreference": wfMTMStaticForwardPreference,
       "wfMTMStaticForwardPrecedence": wfMTMStaticForwardPrecedence,
       "wfMTMStaticForwardInject": wfMTMStaticForwardInject,
       "wfMTMStaticForwardSources": wfMTMStaticForwardSources,
       "wfMTMStaticForwardInCircuits": wfMTMStaticForwardInCircuits,
       "wfMTMStaticForwardOutCircuits": wfMTMStaticForwardOutCircuits,
       "wfMTMStaticForwardMode": wfMTMStaticForwardMode}
)
