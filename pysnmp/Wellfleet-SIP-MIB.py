# SNMP MIB module (Wellfleet-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:04 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfSipGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSipGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSipL2_Object = MibTable
wfSipL2 = _WfSipL2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1)
)
if mibBuilder.loadTexts:
    wfSipL2.setStatus("mandatory")
_WfSipL2Entry_Object = MibTableRow
wfSipL2Entry = _WfSipL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1)
)
wfSipL2Entry.setIndexNames(
    (0, "Wellfleet-SIP-MIB", "wfSipL2Index"),
)
if mibBuilder.loadTexts:
    wfSipL2Entry.setStatus("mandatory")


class _WfSipL2Index_Type(Integer32):
    """Custom type wfSipL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfSipL2Index_Type.__name__ = "Integer32"
_WfSipL2Index_Object = MibTableColumn
wfSipL2Index = _WfSipL2Index_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 1),
    _WfSipL2Index_Type()
)
wfSipL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2Index.setStatus("mandatory")
_WfSipL2ReceivedCounts_Type = Counter32
_WfSipL2ReceivedCounts_Object = MibTableColumn
wfSipL2ReceivedCounts = _WfSipL2ReceivedCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 2),
    _WfSipL2ReceivedCounts_Type()
)
wfSipL2ReceivedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2ReceivedCounts.setStatus("mandatory")
_WfSipL2SentCounts_Type = Counter32
_WfSipL2SentCounts_Object = MibTableColumn
wfSipL2SentCounts = _WfSipL2SentCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 3),
    _WfSipL2SentCounts_Type()
)
wfSipL2SentCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2SentCounts.setStatus("mandatory")
_WfSipHcsOrCRCErrors_Type = Counter32
_WfSipHcsOrCRCErrors_Object = MibTableColumn
wfSipHcsOrCRCErrors = _WfSipHcsOrCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 4),
    _WfSipHcsOrCRCErrors_Type()
)
wfSipHcsOrCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipHcsOrCRCErrors.setStatus("mandatory")
_WfSipL2PayloadLengthErrors_Type = Counter32
_WfSipL2PayloadLengthErrors_Object = MibTableColumn
wfSipL2PayloadLengthErrors = _WfSipL2PayloadLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 5),
    _WfSipL2PayloadLengthErrors_Type()
)
wfSipL2PayloadLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2PayloadLengthErrors.setStatus("mandatory")
_WfSipL2SequenceNumberErrors_Type = Counter32
_WfSipL2SequenceNumberErrors_Object = MibTableColumn
wfSipL2SequenceNumberErrors = _WfSipL2SequenceNumberErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 6),
    _WfSipL2SequenceNumberErrors_Type()
)
wfSipL2SequenceNumberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2SequenceNumberErrors.setStatus("mandatory")
_WfSipL2MidCurrentlyActiveErrors_Type = Counter32
_WfSipL2MidCurrentlyActiveErrors_Object = MibTableColumn
wfSipL2MidCurrentlyActiveErrors = _WfSipL2MidCurrentlyActiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 7),
    _WfSipL2MidCurrentlyActiveErrors_Type()
)
wfSipL2MidCurrentlyActiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2MidCurrentlyActiveErrors.setStatus("mandatory")
_WfSipL2BomOrSSMsMIDErrors_Type = Counter32
_WfSipL2BomOrSSMsMIDErrors_Object = MibTableColumn
wfSipL2BomOrSSMsMIDErrors = _WfSipL2BomOrSSMsMIDErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 8),
    _WfSipL2BomOrSSMsMIDErrors_Type()
)
wfSipL2BomOrSSMsMIDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2BomOrSSMsMIDErrors.setStatus("mandatory")
_WfSipL2EomsMIDErrors_Type = Counter32
_WfSipL2EomsMIDErrors_Object = MibTableColumn
wfSipL2EomsMIDErrors = _WfSipL2EomsMIDErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 9),
    _WfSipL2EomsMIDErrors_Type()
)
wfSipL2EomsMIDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2EomsMIDErrors.setStatus("mandatory")
_WfSipPlcpGroup_ObjectIdentity = ObjectIdentity
wfSipPlcpGroup = _WfSipPlcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2)
)
_WfSipDs1Plcp_Object = MibTable
wfSipDs1Plcp = _WfSipDs1Plcp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1)
)
if mibBuilder.loadTexts:
    wfSipDs1Plcp.setStatus("mandatory")
_WfSipDs1PlcpEntry_Object = MibTableRow
wfSipDs1PlcpEntry = _WfSipDs1PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1)
)
wfSipDs1PlcpEntry.setIndexNames(
    (0, "Wellfleet-SIP-MIB", "wfSipDs1PlcpIndex"),
)
if mibBuilder.loadTexts:
    wfSipDs1PlcpEntry.setStatus("mandatory")


class _WfSipDs1PlcpIndex_Type(Integer32):
    """Custom type wfSipDs1PlcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfSipDs1PlcpIndex_Type.__name__ = "Integer32"
_WfSipDs1PlcpIndex_Object = MibTableColumn
wfSipDs1PlcpIndex = _WfSipDs1PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 1),
    _WfSipDs1PlcpIndex_Type()
)
wfSipDs1PlcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpIndex.setStatus("mandatory")
_WfSipDs1PlcpSEFs_Type = Counter32
_WfSipDs1PlcpSEFs_Object = MibTableColumn
wfSipDs1PlcpSEFs = _WfSipDs1PlcpSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 2),
    _WfSipDs1PlcpSEFs_Type()
)
wfSipDs1PlcpSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpSEFs.setStatus("mandatory")


class _WfSipDs1PlcpAlarmState_Type(Integer32):
    """Custom type wfSipDs1PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incominglof", 3),
          ("noalarm", 1),
          ("receivedfarendalarm", 2))
    )


_WfSipDs1PlcpAlarmState_Type.__name__ = "Integer32"
_WfSipDs1PlcpAlarmState_Object = MibTableColumn
wfSipDs1PlcpAlarmState = _WfSipDs1PlcpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 3),
    _WfSipDs1PlcpAlarmState_Type()
)
wfSipDs1PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpAlarmState.setStatus("mandatory")
_WfSipDs1PlcpUASs_Type = Counter32
_WfSipDs1PlcpUASs_Object = MibTableColumn
wfSipDs1PlcpUASs = _WfSipDs1PlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 4),
    _WfSipDs1PlcpUASs_Type()
)
wfSipDs1PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpUASs.setStatus("mandatory")
_WfSipDs3Plcp_Object = MibTable
wfSipDs3Plcp = _WfSipDs3Plcp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2)
)
if mibBuilder.loadTexts:
    wfSipDs3Plcp.setStatus("mandatory")
_WfSipDs3PlcpEntry_Object = MibTableRow
wfSipDs3PlcpEntry = _WfSipDs3PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1)
)
wfSipDs3PlcpEntry.setIndexNames(
    (0, "Wellfleet-SIP-MIB", "wfSipDs3PlcpIndex"),
)
if mibBuilder.loadTexts:
    wfSipDs3PlcpEntry.setStatus("mandatory")


class _WfSipDs3PlcpIndex_Type(Integer32):
    """Custom type wfSipDs3PlcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfSipDs3PlcpIndex_Type.__name__ = "Integer32"
_WfSipDs3PlcpIndex_Object = MibTableColumn
wfSipDs3PlcpIndex = _WfSipDs3PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 1),
    _WfSipDs3PlcpIndex_Type()
)
wfSipDs3PlcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpIndex.setStatus("mandatory")
_WfSipDs3PlcpSEFs_Type = Counter32
_WfSipDs3PlcpSEFs_Object = MibTableColumn
wfSipDs3PlcpSEFs = _WfSipDs3PlcpSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 2),
    _WfSipDs3PlcpSEFs_Type()
)
wfSipDs3PlcpSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpSEFs.setStatus("mandatory")


class _WfSipDs3PlcpAlarmState_Type(Integer32):
    """Custom type wfSipDs3PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incominglof", 3),
          ("noalarm", 1),
          ("receivedfarendalarm", 2))
    )


_WfSipDs3PlcpAlarmState_Type.__name__ = "Integer32"
_WfSipDs3PlcpAlarmState_Object = MibTableColumn
wfSipDs3PlcpAlarmState = _WfSipDs3PlcpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 3),
    _WfSipDs3PlcpAlarmState_Type()
)
wfSipDs3PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpAlarmState.setStatus("mandatory")
_WfSipDs3PlcpUASs_Type = Counter32
_WfSipDs3PlcpUASs_Object = MibTableColumn
wfSipDs3PlcpUASs = _WfSipDs3PlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 4),
    _WfSipDs3PlcpUASs_Type()
)
wfSipDs3PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpUASs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SIP-MIB",
    **{"wfSipL2": wfSipL2,
       "wfSipL2Entry": wfSipL2Entry,
       "wfSipL2Index": wfSipL2Index,
       "wfSipL2ReceivedCounts": wfSipL2ReceivedCounts,
       "wfSipL2SentCounts": wfSipL2SentCounts,
       "wfSipHcsOrCRCErrors": wfSipHcsOrCRCErrors,
       "wfSipL2PayloadLengthErrors": wfSipL2PayloadLengthErrors,
       "wfSipL2SequenceNumberErrors": wfSipL2SequenceNumberErrors,
       "wfSipL2MidCurrentlyActiveErrors": wfSipL2MidCurrentlyActiveErrors,
       "wfSipL2BomOrSSMsMIDErrors": wfSipL2BomOrSSMsMIDErrors,
       "wfSipL2EomsMIDErrors": wfSipL2EomsMIDErrors,
       "wfSipPlcpGroup": wfSipPlcpGroup,
       "wfSipDs1Plcp": wfSipDs1Plcp,
       "wfSipDs1PlcpEntry": wfSipDs1PlcpEntry,
       "wfSipDs1PlcpIndex": wfSipDs1PlcpIndex,
       "wfSipDs1PlcpSEFs": wfSipDs1PlcpSEFs,
       "wfSipDs1PlcpAlarmState": wfSipDs1PlcpAlarmState,
       "wfSipDs1PlcpUASs": wfSipDs1PlcpUASs,
       "wfSipDs3Plcp": wfSipDs3Plcp,
       "wfSipDs3PlcpEntry": wfSipDs3PlcpEntry,
       "wfSipDs3PlcpIndex": wfSipDs3PlcpIndex,
       "wfSipDs3PlcpSEFs": wfSipDs3PlcpSEFs,
       "wfSipDs3PlcpAlarmState": wfSipDs3PlcpAlarmState,
       "wfSipDs3PlcpUASs": wfSipDs3PlcpUASs}
)
