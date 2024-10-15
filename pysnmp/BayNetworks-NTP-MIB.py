# SNMP MIB module (BayNetworks-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BayNetworks-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:21 2024
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

(wfNtpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfNtpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfNtpEntryTable_Object = MibTable
wfNtpEntryTable = _WfNtpEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1)
)
if mibBuilder.loadTexts:
    wfNtpEntryTable.setStatus("mandatory")
_WfNtpEntry_Object = MibTableRow
wfNtpEntry = _WfNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1)
)
wfNtpEntry.setIndexNames(
    (0, "BayNetworks-NTP-MIB", "wfNtpIndex"),
)
if mibBuilder.loadTexts:
    wfNtpEntry.setStatus("mandatory")
_WfNtpIndex_Type = Integer32
_WfNtpIndex_Object = MibTableColumn
wfNtpIndex = _WfNtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 1),
    _WfNtpIndex_Type()
)
wfNtpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpIndex.setStatus("mandatory")


class _WfNtpDelete_Type(Integer32):
    """Custom type wfNtpDelete based on Integer32"""
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


_WfNtpDelete_Type.__name__ = "Integer32"
_WfNtpDelete_Object = MibTableColumn
wfNtpDelete = _WfNtpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 2),
    _WfNtpDelete_Type()
)
wfNtpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpDelete.setStatus("mandatory")


class _WfNtpDisable_Type(Integer32):
    """Custom type wfNtpDisable based on Integer32"""
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


_WfNtpDisable_Type.__name__ = "Integer32"
_WfNtpDisable_Object = MibTableColumn
wfNtpDisable = _WfNtpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 3),
    _WfNtpDisable_Type()
)
wfNtpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpDisable.setStatus("mandatory")


class _WfNtpMode_Type(Integer32):
    """Custom type wfNtpMode based on Integer32"""
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
        *(("bclient", 2),
          ("client", 1),
          ("mclient", 3))
    )


_WfNtpMode_Type.__name__ = "Integer32"
_WfNtpMode_Object = MibTableColumn
wfNtpMode = _WfNtpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 4),
    _WfNtpMode_Type()
)
wfNtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpMode.setStatus("mandatory")
_WfNtpDebugFlag_Type = Gauge32
_WfNtpDebugFlag_Object = MibTableColumn
wfNtpDebugFlag = _WfNtpDebugFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 5),
    _WfNtpDebugFlag_Type()
)
wfNtpDebugFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpDebugFlag.setStatus("mandatory")


class _WfNtpState_Type(Integer32):
    """Custom type wfNtpState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfNtpState_Type.__name__ = "Integer32"
_WfNtpState_Object = MibTableColumn
wfNtpState = _WfNtpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 6),
    _WfNtpState_Type()
)
wfNtpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpState.setStatus("mandatory")
_WfNtpVersion_Type = Integer32
_WfNtpVersion_Object = MibTableColumn
wfNtpVersion = _WfNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 7),
    _WfNtpVersion_Type()
)
wfNtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpVersion.setStatus("mandatory")


class _WfNtpStratum_Type(Integer32):
    """Custom type wfNtpStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfNtpStratum_Type.__name__ = "Integer32"
_WfNtpStratum_Object = MibTableColumn
wfNtpStratum = _WfNtpStratum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 8),
    _WfNtpStratum_Type()
)
wfNtpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpStratum.setStatus("mandatory")
_WfNtpRootDelay_Type = Integer32
_WfNtpRootDelay_Object = MibTableColumn
wfNtpRootDelay = _WfNtpRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 9),
    _WfNtpRootDelay_Type()
)
wfNtpRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpRootDelay.setStatus("mandatory")
_WfNtpReferenceId_Type = IpAddress
_WfNtpReferenceId_Object = MibTableColumn
wfNtpReferenceId = _WfNtpReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 10),
    _WfNtpReferenceId_Type()
)
wfNtpReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpReferenceId.setStatus("mandatory")
_WfNtpClockPrec_Type = Integer32
_WfNtpClockPrec_Object = MibTableColumn
wfNtpClockPrec = _WfNtpClockPrec_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 11),
    _WfNtpClockPrec_Type()
)
wfNtpClockPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpClockPrec.setStatus("mandatory")


class _WfNtpLeapHappened_Type(Integer32):
    """Custom type wfNtpLeapHappened based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WfNtpLeapHappened_Type.__name__ = "Integer32"
_WfNtpLeapHappened_Object = MibTableColumn
wfNtpLeapHappened = _WfNtpLeapHappened_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 12),
    _WfNtpLeapHappened_Type()
)
wfNtpLeapHappened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpLeapHappened.setStatus("mandatory")
_WfNtpLeapTime_Type = TimeTicks
_WfNtpLeapTime_Object = MibTableColumn
wfNtpLeapTime = _WfNtpLeapTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 13),
    _WfNtpLeapTime_Type()
)
wfNtpLeapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpLeapTime.setStatus("mandatory")
_WfNtpUpdateTimer_Type = Integer32
_WfNtpUpdateTimer_Object = MibTableColumn
wfNtpUpdateTimer = _WfNtpUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 1, 1, 14),
    _WfNtpUpdateTimer_Type()
)
wfNtpUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpUpdateTimer.setStatus("mandatory")
_WfNtpAccessTable_Object = MibTable
wfNtpAccessTable = _WfNtpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 2)
)
if mibBuilder.loadTexts:
    wfNtpAccessTable.setStatus("mandatory")
_WfNtpAccessEntry_Object = MibTableRow
wfNtpAccessEntry = _WfNtpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 2, 1)
)
wfNtpAccessEntry.setIndexNames(
    (0, "BayNetworks-NTP-MIB", "wfNtpAccessIpAddr"),
)
if mibBuilder.loadTexts:
    wfNtpAccessEntry.setStatus("mandatory")


class _WfNtpAccessDelete_Type(Integer32):
    """Custom type wfNtpAccessDelete based on Integer32"""
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


_WfNtpAccessDelete_Type.__name__ = "Integer32"
_WfNtpAccessDelete_Object = MibTableColumn
wfNtpAccessDelete = _WfNtpAccessDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 2, 1, 1),
    _WfNtpAccessDelete_Type()
)
wfNtpAccessDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpAccessDelete.setStatus("mandatory")


class _WfNtpAccessFilterType_Type(Integer32):
    """Custom type wfNtpAccessFilterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prefer", 2),
          ("restrict", 1))
    )


_WfNtpAccessFilterType_Type.__name__ = "Integer32"
_WfNtpAccessFilterType_Object = MibTableColumn
wfNtpAccessFilterType = _WfNtpAccessFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 2, 1, 2),
    _WfNtpAccessFilterType_Type()
)
wfNtpAccessFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpAccessFilterType.setStatus("mandatory")
_WfNtpAccessIpAddr_Type = IpAddress
_WfNtpAccessIpAddr_Object = MibTableColumn
wfNtpAccessIpAddr = _WfNtpAccessIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 2, 1, 3),
    _WfNtpAccessIpAddr_Type()
)
wfNtpAccessIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpAccessIpAddr.setStatus("mandatory")
_WfNtpAccessIpMask_Type = IpAddress
_WfNtpAccessIpMask_Object = MibTableColumn
wfNtpAccessIpMask = _WfNtpAccessIpMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 2, 1, 4),
    _WfNtpAccessIpMask_Type()
)
wfNtpAccessIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpAccessIpMask.setStatus("mandatory")
_WfNtpPeerTable_Object = MibTable
wfNtpPeerTable = _WfNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3)
)
if mibBuilder.loadTexts:
    wfNtpPeerTable.setStatus("mandatory")
_WfNtpPeerEntry_Object = MibTableRow
wfNtpPeerEntry = _WfNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1)
)
wfNtpPeerEntry.setIndexNames(
    (0, "BayNetworks-NTP-MIB", "wfNtpPeerIpAddress"),
)
if mibBuilder.loadTexts:
    wfNtpPeerEntry.setStatus("mandatory")


class _WfNtpPeerDelete_Type(Integer32):
    """Custom type wfNtpPeerDelete based on Integer32"""
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


_WfNtpPeerDelete_Type.__name__ = "Integer32"
_WfNtpPeerDelete_Object = MibTableColumn
wfNtpPeerDelete = _WfNtpPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 1),
    _WfNtpPeerDelete_Type()
)
wfNtpPeerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpPeerDelete.setStatus("mandatory")
_WfNtpPeerState_Type = Gauge32
_WfNtpPeerState_Object = MibTableColumn
wfNtpPeerState = _WfNtpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 2),
    _WfNtpPeerState_Type()
)
wfNtpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerState.setStatus("mandatory")


class _WfNtpCfgPeerMode_Type(Integer32):
    """Custom type wfNtpCfgPeerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("peer", 2),
          ("server", 1))
    )


_WfNtpCfgPeerMode_Type.__name__ = "Integer32"
_WfNtpCfgPeerMode_Object = MibTableColumn
wfNtpCfgPeerMode = _WfNtpCfgPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 3),
    _WfNtpCfgPeerMode_Type()
)
wfNtpCfgPeerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpCfgPeerMode.setStatus("mandatory")


class _WfNtpPeerMode_Type(Integer32):
    """Custom type wfNtpPeerMode based on Integer32"""
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
        *(("broadcast", 5),
          ("client", 3),
          ("ntpctrl", 6),
          ("server", 4),
          ("symmetrica", 1),
          ("symmetricp", 2))
    )


_WfNtpPeerMode_Type.__name__ = "Integer32"
_WfNtpPeerMode_Object = MibTableColumn
wfNtpPeerMode = _WfNtpPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 4),
    _WfNtpPeerMode_Type()
)
wfNtpPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerMode.setStatus("mandatory")


class _WfNtpPeerHostMode_Type(Integer32):
    """Custom type wfNtpPeerHostMode based on Integer32"""
    defaultValue = 3

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
        *(("broadcast", 5),
          ("client", 3),
          ("ntpctrl", 6),
          ("server", 4),
          ("symmetrica", 1),
          ("symmetricp", 2))
    )


_WfNtpPeerHostMode_Type.__name__ = "Integer32"
_WfNtpPeerHostMode_Object = MibTableColumn
wfNtpPeerHostMode = _WfNtpPeerHostMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 5),
    _WfNtpPeerHostMode_Type()
)
wfNtpPeerHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpPeerHostMode.setStatus("mandatory")
_WfNtpPeerIpAddress_Type = IpAddress
_WfNtpPeerIpAddress_Object = MibTableColumn
wfNtpPeerIpAddress = _WfNtpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 6),
    _WfNtpPeerIpAddress_Type()
)
wfNtpPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerIpAddress.setStatus("mandatory")
_WfNtpSourceIpAddress_Type = IpAddress
_WfNtpSourceIpAddress_Object = MibTableColumn
wfNtpSourceIpAddress = _WfNtpSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 7),
    _WfNtpSourceIpAddress_Type()
)
wfNtpSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpSourceIpAddress.setStatus("mandatory")


class _WfNtpPeerPref_Type(Integer32):
    """Custom type wfNtpPeerPref based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WfNtpPeerPref_Type.__name__ = "Integer32"
_WfNtpPeerPref_Object = MibTableColumn
wfNtpPeerPref = _WfNtpPeerPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 8),
    _WfNtpPeerPref_Type()
)
wfNtpPeerPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNtpPeerPref.setStatus("mandatory")
_WfNtpPeerRefId_Type = IpAddress
_WfNtpPeerRefId_Object = MibTableColumn
wfNtpPeerRefId = _WfNtpPeerRefId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 9),
    _WfNtpPeerRefId_Type()
)
wfNtpPeerRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerRefId.setStatus("mandatory")


class _WfNtpPeerVersion_Type(Integer32):
    """Custom type wfNtpPeerVersion based on Integer32"""
    defaultValue = 3


_WfNtpPeerVersion_Object = MibTableColumn
wfNtpPeerVersion = _WfNtpPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 10),
    _WfNtpPeerVersion_Type()
)
wfNtpPeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerVersion.setStatus("mandatory")
_WfNtpPeerPrecision_Type = Integer32
_WfNtpPeerPrecision_Object = MibTableColumn
wfNtpPeerPrecision = _WfNtpPeerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 11),
    _WfNtpPeerPrecision_Type()
)
wfNtpPeerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerPrecision.setStatus("mandatory")


class _WfNtpPeerStratum_Type(Integer32):
    """Custom type wfNtpPeerStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfNtpPeerStratum_Type.__name__ = "Integer32"
_WfNtpPeerStratum_Object = MibTableColumn
wfNtpPeerStratum = _WfNtpPeerStratum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 12),
    _WfNtpPeerStratum_Type()
)
wfNtpPeerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerStratum.setStatus("mandatory")
_WfNtpPeerRootDelay_Type = Integer32
_WfNtpPeerRootDelay_Object = MibTableColumn
wfNtpPeerRootDelay = _WfNtpPeerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 13),
    _WfNtpPeerRootDelay_Type()
)
wfNtpPeerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerRootDelay.setStatus("mandatory")
_WfNtpPeerDispersion_Type = Gauge32
_WfNtpPeerDispersion_Object = MibTableColumn
wfNtpPeerDispersion = _WfNtpPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 14),
    _WfNtpPeerDispersion_Type()
)
wfNtpPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerDispersion.setStatus("mandatory")
_WfNtpPeerOffset_Type = Gauge32
_WfNtpPeerOffset_Object = MibTableColumn
wfNtpPeerOffset = _WfNtpPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 15),
    _WfNtpPeerOffset_Type()
)
wfNtpPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerOffset.setStatus("mandatory")
_WfNtpPeerPolls_Type = Counter32
_WfNtpPeerPolls_Object = MibTableColumn
wfNtpPeerPolls = _WfNtpPeerPolls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 16),
    _WfNtpPeerPolls_Type()
)
wfNtpPeerPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerPolls.setStatus("mandatory")
_WfNtpPeerFrameReceives_Type = Counter32
_WfNtpPeerFrameReceives_Object = MibTableColumn
wfNtpPeerFrameReceives = _WfNtpPeerFrameReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17, 3, 1, 17),
    _WfNtpPeerFrameReceives_Type()
)
wfNtpPeerFrameReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNtpPeerFrameReceives.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BayNetworks-NTP-MIB",
    **{"wfNtpEntryTable": wfNtpEntryTable,
       "wfNtpEntry": wfNtpEntry,
       "wfNtpIndex": wfNtpIndex,
       "wfNtpDelete": wfNtpDelete,
       "wfNtpDisable": wfNtpDisable,
       "wfNtpMode": wfNtpMode,
       "wfNtpDebugFlag": wfNtpDebugFlag,
       "wfNtpState": wfNtpState,
       "wfNtpVersion": wfNtpVersion,
       "wfNtpStratum": wfNtpStratum,
       "wfNtpRootDelay": wfNtpRootDelay,
       "wfNtpReferenceId": wfNtpReferenceId,
       "wfNtpClockPrec": wfNtpClockPrec,
       "wfNtpLeapHappened": wfNtpLeapHappened,
       "wfNtpLeapTime": wfNtpLeapTime,
       "wfNtpUpdateTimer": wfNtpUpdateTimer,
       "wfNtpAccessTable": wfNtpAccessTable,
       "wfNtpAccessEntry": wfNtpAccessEntry,
       "wfNtpAccessDelete": wfNtpAccessDelete,
       "wfNtpAccessFilterType": wfNtpAccessFilterType,
       "wfNtpAccessIpAddr": wfNtpAccessIpAddr,
       "wfNtpAccessIpMask": wfNtpAccessIpMask,
       "wfNtpPeerTable": wfNtpPeerTable,
       "wfNtpPeerEntry": wfNtpPeerEntry,
       "wfNtpPeerDelete": wfNtpPeerDelete,
       "wfNtpPeerState": wfNtpPeerState,
       "wfNtpCfgPeerMode": wfNtpCfgPeerMode,
       "wfNtpPeerMode": wfNtpPeerMode,
       "wfNtpPeerHostMode": wfNtpPeerHostMode,
       "wfNtpPeerIpAddress": wfNtpPeerIpAddress,
       "wfNtpSourceIpAddress": wfNtpSourceIpAddress,
       "wfNtpPeerPref": wfNtpPeerPref,
       "wfNtpPeerRefId": wfNtpPeerRefId,
       "wfNtpPeerVersion": wfNtpPeerVersion,
       "wfNtpPeerPrecision": wfNtpPeerPrecision,
       "wfNtpPeerStratum": wfNtpPeerStratum,
       "wfNtpPeerRootDelay": wfNtpPeerRootDelay,
       "wfNtpPeerDispersion": wfNtpPeerDispersion,
       "wfNtpPeerOffset": wfNtpPeerOffset,
       "wfNtpPeerPolls": wfNtpPeerPolls,
       "wfNtpPeerFrameReceives": wfNtpPeerFrameReceives}
)
