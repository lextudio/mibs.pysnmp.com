# SNMP MIB module (Wellfleet-BOOTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-BOOTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:53 2024
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

(wfBootpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBootpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBootpClientGroup_ObjectIdentity = ObjectIdentity
wfBootpClientGroup = _WfBootpClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1)
)
_WfBootpClientIntfTable_Object = MibTable
wfBootpClientIntfTable = _WfBootpClientIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    wfBootpClientIntfTable.setStatus("mandatory")
_WfBootpClientIntfEntry_Object = MibTableRow
wfBootpClientIntfEntry = _WfBootpClientIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1)
)
wfBootpClientIntfEntry.setIndexNames(
    (0, "Wellfleet-BOOTP-MIB", "wfBootpClientIntfAddress"),
    (0, "Wellfleet-BOOTP-MIB", "wfBootpClientIntfDlci"),
)
if mibBuilder.loadTexts:
    wfBootpClientIntfEntry.setStatus("mandatory")


class _WfBootpClientIntfDelete_Type(Integer32):
    """Custom type wfBootpClientIntfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfBootpClientIntfDelete_Type.__name__ = "Integer32"
_WfBootpClientIntfDelete_Object = MibTableColumn
wfBootpClientIntfDelete = _WfBootpClientIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1, 1),
    _WfBootpClientIntfDelete_Type()
)
wfBootpClientIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpClientIntfDelete.setStatus("mandatory")
_WfBootpClientIntfDlci_Type = Integer32
_WfBootpClientIntfDlci_Object = MibTableColumn
wfBootpClientIntfDlci = _WfBootpClientIntfDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1, 2),
    _WfBootpClientIntfDlci_Type()
)
wfBootpClientIntfDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpClientIntfDlci.setStatus("mandatory")
_WfBootpClientIntfAddress_Type = IpAddress
_WfBootpClientIntfAddress_Object = MibTableColumn
wfBootpClientIntfAddress = _WfBootpClientIntfAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 1, 1, 1, 3),
    _WfBootpClientIntfAddress_Type()
)
wfBootpClientIntfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpClientIntfAddress.setStatus("mandatory")
_WfBootpServerGroup_ObjectIdentity = ObjectIdentity
wfBootpServerGroup = _WfBootpServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 2)
)
_WfBootpRelayAgentGroup_ObjectIdentity = ObjectIdentity
wfBootpRelayAgentGroup = _WfBootpRelayAgentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3)
)
_WfBootpRelayIntfTable_Object = MibTable
wfBootpRelayIntfTable = _WfBootpRelayIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1)
)
if mibBuilder.loadTexts:
    wfBootpRelayIntfTable.setStatus("mandatory")
_WfBootpRelayIntfEntry_Object = MibTableRow
wfBootpRelayIntfEntry = _WfBootpRelayIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1)
)
wfBootpRelayIntfEntry.setIndexNames(
    (0, "Wellfleet-BOOTP-MIB", "wfBootpRelayIntfAddress"),
)
if mibBuilder.loadTexts:
    wfBootpRelayIntfEntry.setStatus("mandatory")


class _WfBootpRelayIntfDelete_Type(Integer32):
    """Custom type wfBootpRelayIntfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfBootpRelayIntfDelete_Type.__name__ = "Integer32"
_WfBootpRelayIntfDelete_Object = MibTableColumn
wfBootpRelayIntfDelete = _WfBootpRelayIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 1),
    _WfBootpRelayIntfDelete_Type()
)
wfBootpRelayIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfDelete.setStatus("mandatory")


class _WfBootpRelayIntfDisable_Type(Integer32):
    """Custom type wfBootpRelayIntfDisable based on Integer32"""
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


_WfBootpRelayIntfDisable_Type.__name__ = "Integer32"
_WfBootpRelayIntfDisable_Object = MibTableColumn
wfBootpRelayIntfDisable = _WfBootpRelayIntfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 2),
    _WfBootpRelayIntfDisable_Type()
)
wfBootpRelayIntfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfDisable.setStatus("mandatory")


class _WfBootpRelayIntfState_Type(Integer32):
    """Custom type wfBootpRelayIntfState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfBootpRelayIntfState_Type.__name__ = "Integer32"
_WfBootpRelayIntfState_Object = MibTableColumn
wfBootpRelayIntfState = _WfBootpRelayIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 3),
    _WfBootpRelayIntfState_Type()
)
wfBootpRelayIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfState.setStatus("mandatory")
_WfBootpRelayIntfAddress_Type = IpAddress
_WfBootpRelayIntfAddress_Object = MibTableColumn
wfBootpRelayIntfAddress = _WfBootpRelayIntfAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 4),
    _WfBootpRelayIntfAddress_Type()
)
wfBootpRelayIntfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfAddress.setStatus("mandatory")


class _WfBootpRelayIntfHops_Type(Integer32):
    """Custom type wfBootpRelayIntfHops based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfBootpRelayIntfHops_Type.__name__ = "Integer32"
_WfBootpRelayIntfHops_Object = MibTableColumn
wfBootpRelayIntfHops = _WfBootpRelayIntfHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 5),
    _WfBootpRelayIntfHops_Type()
)
wfBootpRelayIntfHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfHops.setStatus("mandatory")


class _WfBootpRelayIntfSeconds_Type(Integer32):
    """Custom type wfBootpRelayIntfSeconds based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfBootpRelayIntfSeconds_Type.__name__ = "Integer32"
_WfBootpRelayIntfSeconds_Object = MibTableColumn
wfBootpRelayIntfSeconds = _WfBootpRelayIntfSeconds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 6),
    _WfBootpRelayIntfSeconds_Type()
)
wfBootpRelayIntfSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfSeconds.setStatus("mandatory")
_WfBootpRelayIntfOpDrops_Type = Counter32
_WfBootpRelayIntfOpDrops_Object = MibTableColumn
wfBootpRelayIntfOpDrops = _WfBootpRelayIntfOpDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 7),
    _WfBootpRelayIntfOpDrops_Type()
)
wfBootpRelayIntfOpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfOpDrops.setStatus("mandatory")
_WfBootpRelayIntfRequests_Type = Counter32
_WfBootpRelayIntfRequests_Object = MibTableColumn
wfBootpRelayIntfRequests = _WfBootpRelayIntfRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 8),
    _WfBootpRelayIntfRequests_Type()
)
wfBootpRelayIntfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfRequests.setStatus("mandatory")
_WfBootpRelayIntfTranReqs_Type = Counter32
_WfBootpRelayIntfTranReqs_Object = MibTableColumn
wfBootpRelayIntfTranReqs = _WfBootpRelayIntfTranReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 9),
    _WfBootpRelayIntfTranReqs_Type()
)
wfBootpRelayIntfTranReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfTranReqs.setStatus("mandatory")
_WfBootpRelayIntfHopsDrops_Type = Counter32
_WfBootpRelayIntfHopsDrops_Object = MibTableColumn
wfBootpRelayIntfHopsDrops = _WfBootpRelayIntfHopsDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 10),
    _WfBootpRelayIntfHopsDrops_Type()
)
wfBootpRelayIntfHopsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfHopsDrops.setStatus("mandatory")
_WfBootpRelayIntfBcastDrops_Type = Counter32
_WfBootpRelayIntfBcastDrops_Object = MibTableColumn
wfBootpRelayIntfBcastDrops = _WfBootpRelayIntfBcastDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 11),
    _WfBootpRelayIntfBcastDrops_Type()
)
wfBootpRelayIntfBcastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfBcastDrops.setStatus("mandatory")
_WfBootpRelayIntfSecDrops_Type = Counter32
_WfBootpRelayIntfSecDrops_Object = MibTableColumn
wfBootpRelayIntfSecDrops = _WfBootpRelayIntfSecDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 12),
    _WfBootpRelayIntfSecDrops_Type()
)
wfBootpRelayIntfSecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfSecDrops.setStatus("mandatory")
_WfBootpRelayIntfReplies_Type = Counter32
_WfBootpRelayIntfReplies_Object = MibTableColumn
wfBootpRelayIntfReplies = _WfBootpRelayIntfReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 13),
    _WfBootpRelayIntfReplies_Type()
)
wfBootpRelayIntfReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfReplies.setStatus("mandatory")
_WfBootpRelayIntfGiaddrDrops_Type = Counter32
_WfBootpRelayIntfGiaddrDrops_Object = MibTableColumn
wfBootpRelayIntfGiaddrDrops = _WfBootpRelayIntfGiaddrDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 14),
    _WfBootpRelayIntfGiaddrDrops_Type()
)
wfBootpRelayIntfGiaddrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfGiaddrDrops.setStatus("mandatory")
_WfBootpRelayIntfResrcDrops_Type = Counter32
_WfBootpRelayIntfResrcDrops_Object = MibTableColumn
wfBootpRelayIntfResrcDrops = _WfBootpRelayIntfResrcDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 15),
    _WfBootpRelayIntfResrcDrops_Type()
)
wfBootpRelayIntfResrcDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfResrcDrops.setStatus("mandatory")


class _WfBootpRelayIntfPassThroughMode_Type(Integer32):
    """Custom type wfBootpRelayIntfPassThroughMode based on Integer32"""
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
        *(("bootp", 1),
          ("bootp-dhcp", 2),
          ("dhcp", 3))
    )


_WfBootpRelayIntfPassThroughMode_Type.__name__ = "Integer32"
_WfBootpRelayIntfPassThroughMode_Object = MibTableColumn
wfBootpRelayIntfPassThroughMode = _WfBootpRelayIntfPassThroughMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 16),
    _WfBootpRelayIntfPassThroughMode_Type()
)
wfBootpRelayIntfPassThroughMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfPassThroughMode.setStatus("mandatory")
_WfBootpRelayIntfUdpSktDrops_Type = Counter32
_WfBootpRelayIntfUdpSktDrops_Object = MibTableColumn
wfBootpRelayIntfUdpSktDrops = _WfBootpRelayIntfUdpSktDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 17),
    _WfBootpRelayIntfUdpSktDrops_Type()
)
wfBootpRelayIntfUdpSktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfUdpSktDrops.setStatus("mandatory")
_WfBootpRelayIntfTooShortDrops_Type = Counter32
_WfBootpRelayIntfTooShortDrops_Object = MibTableColumn
wfBootpRelayIntfTooShortDrops = _WfBootpRelayIntfTooShortDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 18),
    _WfBootpRelayIntfTooShortDrops_Type()
)
wfBootpRelayIntfTooShortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfTooShortDrops.setStatus("mandatory")
_WfBootpRelayIntfFltrDrops_Type = Counter32
_WfBootpRelayIntfFltrDrops_Object = MibTableColumn
wfBootpRelayIntfFltrDrops = _WfBootpRelayIntfFltrDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 19),
    _WfBootpRelayIntfFltrDrops_Type()
)
wfBootpRelayIntfFltrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfFltrDrops.setStatus("mandatory")


class _WfBootpRelayIntfPri_Type(Integer32):
    """Custom type wfBootpRelayIntfPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfBootpRelayIntfPri_Type.__name__ = "Integer32"
_WfBootpRelayIntfPri_Object = MibTableColumn
wfBootpRelayIntfPri = _WfBootpRelayIntfPri_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 20),
    _WfBootpRelayIntfPri_Type()
)
wfBootpRelayIntfPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfPri.setStatus("mandatory")


class _WfBootpRelayIntfDhcpSvrDsbl_Type(Integer32):
    """Custom type wfBootpRelayIntfDhcpSvrDsbl based on Integer32"""
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


_WfBootpRelayIntfDhcpSvrDsbl_Type.__name__ = "Integer32"
_WfBootpRelayIntfDhcpSvrDsbl_Object = MibTableColumn
wfBootpRelayIntfDhcpSvrDsbl = _WfBootpRelayIntfDhcpSvrDsbl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 21),
    _WfBootpRelayIntfDhcpSvrDsbl_Type()
)
wfBootpRelayIntfDhcpSvrDsbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfDhcpSvrDsbl.setStatus("mandatory")
_WfBootpRelayIntfDhcpSvDnDrps_Type = Counter32
_WfBootpRelayIntfDhcpSvDnDrps_Object = MibTableColumn
wfBootpRelayIntfDhcpSvDnDrps = _WfBootpRelayIntfDhcpSvDnDrps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 22),
    _WfBootpRelayIntfDhcpSvDnDrps_Type()
)
wfBootpRelayIntfDhcpSvDnDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfDhcpSvDnDrps.setStatus("mandatory")


class _WfBootpRelayIntfArpCache_Type(Integer32):
    """Custom type wfBootpRelayIntfArpCache based on Integer32"""
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


_WfBootpRelayIntfArpCache_Type.__name__ = "Integer32"
_WfBootpRelayIntfArpCache_Object = MibTableColumn
wfBootpRelayIntfArpCache = _WfBootpRelayIntfArpCache_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 23),
    _WfBootpRelayIntfArpCache_Type()
)
wfBootpRelayIntfArpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfArpCache.setStatus("mandatory")


class _WfBootpRelayIntfBufLimit_Type(Integer32):
    """Custom type wfBootpRelayIntfBufLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1000),
    )


_WfBootpRelayIntfBufLimit_Type.__name__ = "Integer32"
_WfBootpRelayIntfBufLimit_Object = MibTableColumn
wfBootpRelayIntfBufLimit = _WfBootpRelayIntfBufLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 24),
    _WfBootpRelayIntfBufLimit_Type()
)
wfBootpRelayIntfBufLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayIntfBufLimit.setStatus("mandatory")
_WfBootpRelayIntfBufDrops_Type = Counter32
_WfBootpRelayIntfBufDrops_Object = MibTableColumn
wfBootpRelayIntfBufDrops = _WfBootpRelayIntfBufDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 1, 1, 25),
    _WfBootpRelayIntfBufDrops_Type()
)
wfBootpRelayIntfBufDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayIntfBufDrops.setStatus("mandatory")
_WfBootpRelayFwdTable_Object = MibTable
wfBootpRelayFwdTable = _WfBootpRelayFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2)
)
if mibBuilder.loadTexts:
    wfBootpRelayFwdTable.setStatus("mandatory")
_WfBootpRelayFwdEntry_Object = MibTableRow
wfBootpRelayFwdEntry = _WfBootpRelayFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1)
)
wfBootpRelayFwdEntry.setIndexNames(
    (0, "Wellfleet-BOOTP-MIB", "wfBootpRelayFwdAgentIntf"),
    (0, "Wellfleet-BOOTP-MIB", "wfBootpRelayFwdOutIntf"),
)
if mibBuilder.loadTexts:
    wfBootpRelayFwdEntry.setStatus("mandatory")


class _WfBootpRelayFwdDelete_Type(Integer32):
    """Custom type wfBootpRelayFwdDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfBootpRelayFwdDelete_Type.__name__ = "Integer32"
_WfBootpRelayFwdDelete_Object = MibTableColumn
wfBootpRelayFwdDelete = _WfBootpRelayFwdDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 1),
    _WfBootpRelayFwdDelete_Type()
)
wfBootpRelayFwdDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayFwdDelete.setStatus("mandatory")


class _WfBootpRelayFwdDisable_Type(Integer32):
    """Custom type wfBootpRelayFwdDisable based on Integer32"""
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


_WfBootpRelayFwdDisable_Type.__name__ = "Integer32"
_WfBootpRelayFwdDisable_Object = MibTableColumn
wfBootpRelayFwdDisable = _WfBootpRelayFwdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 2),
    _WfBootpRelayFwdDisable_Type()
)
wfBootpRelayFwdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayFwdDisable.setStatus("mandatory")
_WfBootpRelayFwdAgentIntf_Type = IpAddress
_WfBootpRelayFwdAgentIntf_Object = MibTableColumn
wfBootpRelayFwdAgentIntf = _WfBootpRelayFwdAgentIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 3),
    _WfBootpRelayFwdAgentIntf_Type()
)
wfBootpRelayFwdAgentIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayFwdAgentIntf.setStatus("mandatory")
_WfBootpRelayFwdOutIntf_Type = IpAddress
_WfBootpRelayFwdOutIntf_Object = MibTableColumn
wfBootpRelayFwdOutIntf = _WfBootpRelayFwdOutIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 4),
    _WfBootpRelayFwdOutIntf_Type()
)
wfBootpRelayFwdOutIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayFwdOutIntf.setStatus("mandatory")


class _WfBootpRelayFwdPassThroughMode_Type(Integer32):
    """Custom type wfBootpRelayFwdPassThroughMode based on Integer32"""
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
        *(("bootp", 1),
          ("bootp-dhcp", 2),
          ("dhcp", 3))
    )


_WfBootpRelayFwdPassThroughMode_Type.__name__ = "Integer32"
_WfBootpRelayFwdPassThroughMode_Object = MibTableColumn
wfBootpRelayFwdPassThroughMode = _WfBootpRelayFwdPassThroughMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 5),
    _WfBootpRelayFwdPassThroughMode_Type()
)
wfBootpRelayFwdPassThroughMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayFwdPassThroughMode.setStatus("mandatory")
_WfBootpRelayFwdOutReqPkts_Type = Counter32
_WfBootpRelayFwdOutReqPkts_Object = MibTableColumn
wfBootpRelayFwdOutReqPkts = _WfBootpRelayFwdOutReqPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 2, 1, 6),
    _WfBootpRelayFwdOutReqPkts_Type()
)
wfBootpRelayFwdOutReqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayFwdOutReqPkts.setStatus("mandatory")
_WfBootpRelayPrefServTable_Object = MibTable
wfBootpRelayPrefServTable = _WfBootpRelayPrefServTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3)
)
if mibBuilder.loadTexts:
    wfBootpRelayPrefServTable.setStatus("mandatory")
_WfBootpRelayPrefServEntry_Object = MibTableRow
wfBootpRelayPrefServEntry = _WfBootpRelayPrefServEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1)
)
wfBootpRelayPrefServEntry.setIndexNames(
    (0, "Wellfleet-BOOTP-MIB", "wfBootpRelayPrefServAgentAddress"),
    (0, "Wellfleet-BOOTP-MIB", "wfBootpRelayPrefServTargetAddress"),
)
if mibBuilder.loadTexts:
    wfBootpRelayPrefServEntry.setStatus("mandatory")


class _WfBootpRelayPrefServDelete_Type(Integer32):
    """Custom type wfBootpRelayPrefServDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfBootpRelayPrefServDelete_Type.__name__ = "Integer32"
_WfBootpRelayPrefServDelete_Object = MibTableColumn
wfBootpRelayPrefServDelete = _WfBootpRelayPrefServDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 1),
    _WfBootpRelayPrefServDelete_Type()
)
wfBootpRelayPrefServDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayPrefServDelete.setStatus("mandatory")


class _WfBootpRelayPrefServDisable_Type(Integer32):
    """Custom type wfBootpRelayPrefServDisable based on Integer32"""
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


_WfBootpRelayPrefServDisable_Type.__name__ = "Integer32"
_WfBootpRelayPrefServDisable_Object = MibTableColumn
wfBootpRelayPrefServDisable = _WfBootpRelayPrefServDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 2),
    _WfBootpRelayPrefServDisable_Type()
)
wfBootpRelayPrefServDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayPrefServDisable.setStatus("mandatory")
_WfBootpRelayPrefServAgentAddress_Type = IpAddress
_WfBootpRelayPrefServAgentAddress_Object = MibTableColumn
wfBootpRelayPrefServAgentAddress = _WfBootpRelayPrefServAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 3),
    _WfBootpRelayPrefServAgentAddress_Type()
)
wfBootpRelayPrefServAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayPrefServAgentAddress.setStatus("mandatory")
_WfBootpRelayPrefServTargetAddress_Type = IpAddress
_WfBootpRelayPrefServTargetAddress_Object = MibTableColumn
wfBootpRelayPrefServTargetAddress = _WfBootpRelayPrefServTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 4),
    _WfBootpRelayPrefServTargetAddress_Type()
)
wfBootpRelayPrefServTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayPrefServTargetAddress.setStatus("mandatory")
_WfBootpRelayPrefServTargetName_Type = DisplayString
_WfBootpRelayPrefServTargetName_Object = MibTableColumn
wfBootpRelayPrefServTargetName = _WfBootpRelayPrefServTargetName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 5),
    _WfBootpRelayPrefServTargetName_Type()
)
wfBootpRelayPrefServTargetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayPrefServTargetName.setStatus("mandatory")


class _WfBootpRelayPrefServRequestMode_Type(Integer32):
    """Custom type wfBootpRelayPrefServRequestMode based on Integer32"""
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
        *(("bootp", 1),
          ("bootp-dhcp", 2),
          ("dhcp", 3))
    )


_WfBootpRelayPrefServRequestMode_Type.__name__ = "Integer32"
_WfBootpRelayPrefServRequestMode_Object = MibTableColumn
wfBootpRelayPrefServRequestMode = _WfBootpRelayPrefServRequestMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 6),
    _WfBootpRelayPrefServRequestMode_Type()
)
wfBootpRelayPrefServRequestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBootpRelayPrefServRequestMode.setStatus("mandatory")
_WfBootpRelayPrefServOutReqPkts_Type = Counter32
_WfBootpRelayPrefServOutReqPkts_Object = MibTableColumn
wfBootpRelayPrefServOutReqPkts = _WfBootpRelayPrefServOutReqPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8, 3, 3, 1, 7),
    _WfBootpRelayPrefServOutReqPkts_Type()
)
wfBootpRelayPrefServOutReqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBootpRelayPrefServOutReqPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-BOOTP-MIB",
    **{"wfBootpClientGroup": wfBootpClientGroup,
       "wfBootpClientIntfTable": wfBootpClientIntfTable,
       "wfBootpClientIntfEntry": wfBootpClientIntfEntry,
       "wfBootpClientIntfDelete": wfBootpClientIntfDelete,
       "wfBootpClientIntfDlci": wfBootpClientIntfDlci,
       "wfBootpClientIntfAddress": wfBootpClientIntfAddress,
       "wfBootpServerGroup": wfBootpServerGroup,
       "wfBootpRelayAgentGroup": wfBootpRelayAgentGroup,
       "wfBootpRelayIntfTable": wfBootpRelayIntfTable,
       "wfBootpRelayIntfEntry": wfBootpRelayIntfEntry,
       "wfBootpRelayIntfDelete": wfBootpRelayIntfDelete,
       "wfBootpRelayIntfDisable": wfBootpRelayIntfDisable,
       "wfBootpRelayIntfState": wfBootpRelayIntfState,
       "wfBootpRelayIntfAddress": wfBootpRelayIntfAddress,
       "wfBootpRelayIntfHops": wfBootpRelayIntfHops,
       "wfBootpRelayIntfSeconds": wfBootpRelayIntfSeconds,
       "wfBootpRelayIntfOpDrops": wfBootpRelayIntfOpDrops,
       "wfBootpRelayIntfRequests": wfBootpRelayIntfRequests,
       "wfBootpRelayIntfTranReqs": wfBootpRelayIntfTranReqs,
       "wfBootpRelayIntfHopsDrops": wfBootpRelayIntfHopsDrops,
       "wfBootpRelayIntfBcastDrops": wfBootpRelayIntfBcastDrops,
       "wfBootpRelayIntfSecDrops": wfBootpRelayIntfSecDrops,
       "wfBootpRelayIntfReplies": wfBootpRelayIntfReplies,
       "wfBootpRelayIntfGiaddrDrops": wfBootpRelayIntfGiaddrDrops,
       "wfBootpRelayIntfResrcDrops": wfBootpRelayIntfResrcDrops,
       "wfBootpRelayIntfPassThroughMode": wfBootpRelayIntfPassThroughMode,
       "wfBootpRelayIntfUdpSktDrops": wfBootpRelayIntfUdpSktDrops,
       "wfBootpRelayIntfTooShortDrops": wfBootpRelayIntfTooShortDrops,
       "wfBootpRelayIntfFltrDrops": wfBootpRelayIntfFltrDrops,
       "wfBootpRelayIntfPri": wfBootpRelayIntfPri,
       "wfBootpRelayIntfDhcpSvrDsbl": wfBootpRelayIntfDhcpSvrDsbl,
       "wfBootpRelayIntfDhcpSvDnDrps": wfBootpRelayIntfDhcpSvDnDrps,
       "wfBootpRelayIntfArpCache": wfBootpRelayIntfArpCache,
       "wfBootpRelayIntfBufLimit": wfBootpRelayIntfBufLimit,
       "wfBootpRelayIntfBufDrops": wfBootpRelayIntfBufDrops,
       "wfBootpRelayFwdTable": wfBootpRelayFwdTable,
       "wfBootpRelayFwdEntry": wfBootpRelayFwdEntry,
       "wfBootpRelayFwdDelete": wfBootpRelayFwdDelete,
       "wfBootpRelayFwdDisable": wfBootpRelayFwdDisable,
       "wfBootpRelayFwdAgentIntf": wfBootpRelayFwdAgentIntf,
       "wfBootpRelayFwdOutIntf": wfBootpRelayFwdOutIntf,
       "wfBootpRelayFwdPassThroughMode": wfBootpRelayFwdPassThroughMode,
       "wfBootpRelayFwdOutReqPkts": wfBootpRelayFwdOutReqPkts,
       "wfBootpRelayPrefServTable": wfBootpRelayPrefServTable,
       "wfBootpRelayPrefServEntry": wfBootpRelayPrefServEntry,
       "wfBootpRelayPrefServDelete": wfBootpRelayPrefServDelete,
       "wfBootpRelayPrefServDisable": wfBootpRelayPrefServDisable,
       "wfBootpRelayPrefServAgentAddress": wfBootpRelayPrefServAgentAddress,
       "wfBootpRelayPrefServTargetAddress": wfBootpRelayPrefServTargetAddress,
       "wfBootpRelayPrefServTargetName": wfBootpRelayPrefServTargetName,
       "wfBootpRelayPrefServRequestMode": wfBootpRelayPrefServRequestMode,
       "wfBootpRelayPrefServOutReqPkts": wfBootpRelayPrefServOutReqPkts}
)
