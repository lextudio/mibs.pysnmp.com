# SNMP MIB module (Wellfleet-ASR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ASR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:46 2024
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

(wfAsrGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAsrGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAsrBase_ObjectIdentity = ObjectIdentity
wfAsrBase = _WfAsrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1)
)


class _WfAsrBaseCreate_Type(Integer32):
    """Custom type wfAsrBaseCreate based on Integer32"""
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


_WfAsrBaseCreate_Type.__name__ = "Integer32"
_WfAsrBaseCreate_Object = MibScalar
wfAsrBaseCreate = _WfAsrBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 1),
    _WfAsrBaseCreate_Type()
)
wfAsrBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrBaseCreate.setStatus("mandatory")


class _WfAsrBaseEnable_Type(Integer32):
    """Custom type wfAsrBaseEnable based on Integer32"""
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


_WfAsrBaseEnable_Type.__name__ = "Integer32"
_WfAsrBaseEnable_Object = MibScalar
wfAsrBaseEnable = _WfAsrBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 2),
    _WfAsrBaseEnable_Type()
)
wfAsrBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrBaseEnable.setStatus("mandatory")


class _WfAsrBaseState_Type(Integer32):
    """Custom type wfAsrBaseState based on Integer32"""
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
          ("notpres", 4),
          ("up", 1))
    )


_WfAsrBaseState_Type.__name__ = "Integer32"
_WfAsrBaseState_Object = MibScalar
wfAsrBaseState = _WfAsrBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 3),
    _WfAsrBaseState_Type()
)
wfAsrBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrBaseState.setStatus("mandatory")


class _WfAsrNextHopRetryLimit_Type(Integer32):
    """Custom type wfAsrNextHopRetryLimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfAsrNextHopRetryLimit_Type.__name__ = "Integer32"
_WfAsrNextHopRetryLimit_Object = MibScalar
wfAsrNextHopRetryLimit = _WfAsrNextHopRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 4),
    _WfAsrNextHopRetryLimit_Type()
)
wfAsrNextHopRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrNextHopRetryLimit.setStatus("mandatory")


class _WfAsrSecureInFilter_Type(Integer32):
    """Custom type wfAsrSecureInFilter based on Integer32"""
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


_WfAsrSecureInFilter_Type.__name__ = "Integer32"
_WfAsrSecureInFilter_Object = MibScalar
wfAsrSecureInFilter = _WfAsrSecureInFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 5),
    _WfAsrSecureInFilter_Type()
)
wfAsrSecureInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrSecureInFilter.setStatus("mandatory")


class _WfAsrSecureInValid_Type(Integer32):
    """Custom type wfAsrSecureInValid based on Integer32"""
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


_WfAsrSecureInValid_Type.__name__ = "Integer32"
_WfAsrSecureInValid_Object = MibScalar
wfAsrSecureInValid = _WfAsrSecureInValid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 6),
    _WfAsrSecureInValid_Type()
)
wfAsrSecureInValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrSecureInValid.setStatus("mandatory")


class _WfAsrHoldDownTimer_Type(Integer32):
    """Custom type wfAsrHoldDownTimer based on Integer32"""
    defaultValue = 5


_WfAsrHoldDownTimer_Object = MibScalar
wfAsrHoldDownTimer = _WfAsrHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 7),
    _WfAsrHoldDownTimer_Type()
)
wfAsrHoldDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrHoldDownTimer.setStatus("mandatory")
_WfAsrActiveSvcs_Type = Counter32
_WfAsrActiveSvcs_Object = MibScalar
wfAsrActiveSvcs = _WfAsrActiveSvcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 8),
    _WfAsrActiveSvcs_Type()
)
wfAsrActiveSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrActiveSvcs.setStatus("mandatory")
_WfAsrFwdTblEntries_Type = Counter32
_WfAsrFwdTblEntries_Object = MibScalar
wfAsrFwdTblEntries = _WfAsrFwdTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 9),
    _WfAsrFwdTblEntries_Type()
)
wfAsrFwdTblEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFwdTblEntries.setStatus("mandatory")
_WfAsrFwdTblSeq_Type = Counter32
_WfAsrFwdTblSeq_Object = MibScalar
wfAsrFwdTblSeq = _WfAsrFwdTblSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 10),
    _WfAsrFwdTblSeq_Type()
)
wfAsrFwdTblSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFwdTblSeq.setStatus("mandatory")


class _WfAsrDnsProxyPort_Type(Integer32):
    """Custom type wfAsrDnsProxyPort based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              500,
              32550)
        )
    )
    namedValues = NamedValues(
        *(("default", 500),
          ("max", 32550),
          ("min", 1))
    )


_WfAsrDnsProxyPort_Type.__name__ = "Integer32"
_WfAsrDnsProxyPort_Object = MibScalar
wfAsrDnsProxyPort = _WfAsrDnsProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 11),
    _WfAsrDnsProxyPort_Type()
)
wfAsrDnsProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrDnsProxyPort.setStatus("mandatory")


class _WfAsrMaxSessions_Type(Integer32):
    """Custom type wfAsrMaxSessions based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            500
        )
    )
    namedValues = NamedValues(
        ("default", 500)
    )


_WfAsrMaxSessions_Type.__name__ = "Integer32"
_WfAsrMaxSessions_Object = MibScalar
wfAsrMaxSessions = _WfAsrMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 12),
    _WfAsrMaxSessions_Type()
)
wfAsrMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrMaxSessions.setStatus("mandatory")


class _WfAsrDebugLevel_Type(Integer32):
    """Custom type wfAsrDebugLevel based on Integer32"""
    defaultValue = 0


_WfAsrDebugLevel_Object = MibScalar
wfAsrDebugLevel = _WfAsrDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 13),
    _WfAsrDebugLevel_Type()
)
wfAsrDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrDebugLevel.setStatus("mandatory")


class _WfAsrUseDynRdiscPref_Type(Integer32):
    """Custom type wfAsrUseDynRdiscPref based on Integer32"""
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


_WfAsrUseDynRdiscPref_Type.__name__ = "Integer32"
_WfAsrUseDynRdiscPref_Object = MibScalar
wfAsrUseDynRdiscPref = _WfAsrUseDynRdiscPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 1, 14),
    _WfAsrUseDynRdiscPref_Type()
)
wfAsrUseDynRdiscPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrUseDynRdiscPref.setStatus("mandatory")
_WfAsrX213PriTable_Object = MibTable
wfAsrX213PriTable = _WfAsrX213PriTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 2)
)
if mibBuilder.loadTexts:
    wfAsrX213PriTable.setStatus("mandatory")
_WfAsrX213PriEntry_Object = MibTableRow
wfAsrX213PriEntry = _WfAsrX213PriEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 2, 1)
)
wfAsrX213PriEntry.setIndexNames(
    (0, "Wellfleet-ASR-MIB", "wfAsrX213PriLowVal"),
    (0, "Wellfleet-ASR-MIB", "wfAsrX213PriHiVal"),
)
if mibBuilder.loadTexts:
    wfAsrX213PriEntry.setStatus("mandatory")


class _WfAsrX213PriDelete_Type(Integer32):
    """Custom type wfAsrX213PriDelete based on Integer32"""
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


_WfAsrX213PriDelete_Type.__name__ = "Integer32"
_WfAsrX213PriDelete_Object = MibTableColumn
wfAsrX213PriDelete = _WfAsrX213PriDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 2, 1, 1),
    _WfAsrX213PriDelete_Type()
)
wfAsrX213PriDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrX213PriDelete.setStatus("mandatory")
_WfAsrX213PriLowVal_Type = Integer32
_WfAsrX213PriLowVal_Object = MibTableColumn
wfAsrX213PriLowVal = _WfAsrX213PriLowVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 2, 1, 2),
    _WfAsrX213PriLowVal_Type()
)
wfAsrX213PriLowVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrX213PriLowVal.setStatus("mandatory")
_WfAsrX213PriHiVal_Type = Integer32
_WfAsrX213PriHiVal_Object = MibTableColumn
wfAsrX213PriHiVal = _WfAsrX213PriHiVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 2, 1, 3),
    _WfAsrX213PriHiVal_Type()
)
wfAsrX213PriHiVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrX213PriHiVal.setStatus("mandatory")
_WfAsrX213PriSwVal_Type = Integer32
_WfAsrX213PriSwVal_Object = MibTableColumn
wfAsrX213PriSwVal = _WfAsrX213PriSwVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 2, 1, 4),
    _WfAsrX213PriSwVal_Type()
)
wfAsrX213PriSwVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrX213PriSwVal.setStatus("mandatory")
_WfAsrRtrPriTable_Object = MibTable
wfAsrRtrPriTable = _WfAsrRtrPriTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 3)
)
if mibBuilder.loadTexts:
    wfAsrRtrPriTable.setStatus("mandatory")
_WfAsrRtrPriEntry_Object = MibTableRow
wfAsrRtrPriEntry = _WfAsrRtrPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 3, 1)
)
wfAsrRtrPriEntry.setIndexNames(
    (0, "Wellfleet-ASR-MIB", "wfAsrRtrPriLowVal"),
    (0, "Wellfleet-ASR-MIB", "wfAsrRtrPriHiVal"),
)
if mibBuilder.loadTexts:
    wfAsrRtrPriEntry.setStatus("mandatory")


class _WfAsrRtrPriDelete_Type(Integer32):
    """Custom type wfAsrRtrPriDelete based on Integer32"""
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


_WfAsrRtrPriDelete_Type.__name__ = "Integer32"
_WfAsrRtrPriDelete_Object = MibTableColumn
wfAsrRtrPriDelete = _WfAsrRtrPriDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 3, 1, 1),
    _WfAsrRtrPriDelete_Type()
)
wfAsrRtrPriDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrRtrPriDelete.setStatus("mandatory")
_WfAsrRtrPriLowVal_Type = Integer32
_WfAsrRtrPriLowVal_Object = MibTableColumn
wfAsrRtrPriLowVal = _WfAsrRtrPriLowVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 3, 1, 2),
    _WfAsrRtrPriLowVal_Type()
)
wfAsrRtrPriLowVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrRtrPriLowVal.setStatus("mandatory")
_WfAsrRtrPriHiVal_Type = Integer32
_WfAsrRtrPriHiVal_Object = MibTableColumn
wfAsrRtrPriHiVal = _WfAsrRtrPriHiVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 3, 1, 3),
    _WfAsrRtrPriHiVal_Type()
)
wfAsrRtrPriHiVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrRtrPriHiVal.setStatus("mandatory")
_WfAsrRtrPriCvtVal_Type = Integer32
_WfAsrRtrPriCvtVal_Object = MibTableColumn
wfAsrRtrPriCvtVal = _WfAsrRtrPriCvtVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 3, 1, 4),
    _WfAsrRtrPriCvtVal_Type()
)
wfAsrRtrPriCvtVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrRtrPriCvtVal.setStatus("mandatory")
_WfAsrMultiHopTable_Object = MibTable
wfAsrMultiHopTable = _WfAsrMultiHopTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 4)
)
if mibBuilder.loadTexts:
    wfAsrMultiHopTable.setStatus("mandatory")
_WfAsrMultiHopEntry_Object = MibTableRow
wfAsrMultiHopEntry = _WfAsrMultiHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 4, 1)
)
wfAsrMultiHopEntry.setIndexNames(
    (0, "Wellfleet-ASR-MIB", "wfAsrMhCircuitNumber"),
    (0, "Wellfleet-ASR-MIB", "wfAsrMhVcid1"),
    (0, "Wellfleet-ASR-MIB", "wfAsrMhVcid2"),
)
if mibBuilder.loadTexts:
    wfAsrMultiHopEntry.setStatus("mandatory")


class _WfAsrMultiHopDelete_Type(Integer32):
    """Custom type wfAsrMultiHopDelete based on Integer32"""
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


_WfAsrMultiHopDelete_Type.__name__ = "Integer32"
_WfAsrMultiHopDelete_Object = MibTableColumn
wfAsrMultiHopDelete = _WfAsrMultiHopDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 4, 1, 1),
    _WfAsrMultiHopDelete_Type()
)
wfAsrMultiHopDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrMultiHopDelete.setStatus("mandatory")
_WfAsrMhCircuitNumber_Type = Integer32
_WfAsrMhCircuitNumber_Object = MibTableColumn
wfAsrMhCircuitNumber = _WfAsrMhCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 4, 1, 2),
    _WfAsrMhCircuitNumber_Type()
)
wfAsrMhCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrMhCircuitNumber.setStatus("mandatory")
_WfAsrMhVcid1_Type = Integer32
_WfAsrMhVcid1_Object = MibTableColumn
wfAsrMhVcid1 = _WfAsrMhVcid1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 4, 1, 3),
    _WfAsrMhVcid1_Type()
)
wfAsrMhVcid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrMhVcid1.setStatus("mandatory")
_WfAsrMhVcid2_Type = Integer32
_WfAsrMhVcid2_Object = MibTableColumn
wfAsrMhVcid2 = _WfAsrMhVcid2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 4, 1, 4),
    _WfAsrMhVcid2_Type()
)
wfAsrMhVcid2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrMhVcid2.setStatus("mandatory")
_WfAsrDirectExceptTable_Object = MibTable
wfAsrDirectExceptTable = _WfAsrDirectExceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5)
)
if mibBuilder.loadTexts:
    wfAsrDirectExceptTable.setStatus("mandatory")
_WfAsrDirectExceptEntry_Object = MibTableRow
wfAsrDirectExceptEntry = _WfAsrDirectExceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5, 1)
)
wfAsrDirectExceptEntry.setIndexNames(
    (0, "Wellfleet-ASR-MIB", "wfAsrServiceProtocol"),
    (0, "Wellfleet-ASR-MIB", "wfAsrServicePort"),
)
if mibBuilder.loadTexts:
    wfAsrDirectExceptEntry.setStatus("mandatory")


class _WfAsrServiceProtocol_Type(Integer32):
    """Custom type wfAsrServiceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_WfAsrServiceProtocol_Type.__name__ = "Integer32"
_WfAsrServiceProtocol_Object = MibTableColumn
wfAsrServiceProtocol = _WfAsrServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5, 1, 1),
    _WfAsrServiceProtocol_Type()
)
wfAsrServiceProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrServiceProtocol.setStatus("mandatory")
_WfAsrServicePort_Type = Integer32
_WfAsrServicePort_Object = MibTableColumn
wfAsrServicePort = _WfAsrServicePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5, 1, 2),
    _WfAsrServicePort_Type()
)
wfAsrServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrServicePort.setStatus("mandatory")
_WfAsrSrcPortLow_Type = Integer32
_WfAsrSrcPortLow_Object = MibTableColumn
wfAsrSrcPortLow = _WfAsrSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5, 1, 3),
    _WfAsrSrcPortLow_Type()
)
wfAsrSrcPortLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrSrcPortLow.setStatus("mandatory")
_WfAsrSrcPortHigh_Type = Integer32
_WfAsrSrcPortHigh_Object = MibTableColumn
wfAsrSrcPortHigh = _WfAsrSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5, 1, 4),
    _WfAsrSrcPortHigh_Type()
)
wfAsrSrcPortHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrSrcPortHigh.setStatus("mandatory")
_WfAsrDestPortLow_Type = Integer32
_WfAsrDestPortLow_Object = MibTableColumn
wfAsrDestPortLow = _WfAsrDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5, 1, 5),
    _WfAsrDestPortLow_Type()
)
wfAsrDestPortLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrDestPortLow.setStatus("mandatory")
_WfAsrDestPortHigh_Type = Integer32
_WfAsrDestPortHigh_Object = MibTableColumn
wfAsrDestPortHigh = _WfAsrDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 5, 1, 6),
    _WfAsrDestPortHigh_Type()
)
wfAsrDestPortHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrDestPortHigh.setStatus("mandatory")
_WfAsrCircuitTable_Object = MibTable
wfAsrCircuitTable = _WfAsrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6)
)
if mibBuilder.loadTexts:
    wfAsrCircuitTable.setStatus("mandatory")
_WfAsrCircuitEntry_Object = MibTableRow
wfAsrCircuitEntry = _WfAsrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1)
)
wfAsrCircuitEntry.setIndexNames(
    (0, "Wellfleet-ASR-MIB", "wfAsrCircuitNumber"),
)
if mibBuilder.loadTexts:
    wfAsrCircuitEntry.setStatus("mandatory")


class _WfAsrCircuitCreate_Type(Integer32):
    """Custom type wfAsrCircuitCreate based on Integer32"""
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


_WfAsrCircuitCreate_Type.__name__ = "Integer32"
_WfAsrCircuitCreate_Object = MibTableColumn
wfAsrCircuitCreate = _WfAsrCircuitCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 1),
    _WfAsrCircuitCreate_Type()
)
wfAsrCircuitCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrCircuitCreate.setStatus("mandatory")


class _WfAsrCircuitEnable_Type(Integer32):
    """Custom type wfAsrCircuitEnable based on Integer32"""
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


_WfAsrCircuitEnable_Type.__name__ = "Integer32"
_WfAsrCircuitEnable_Object = MibTableColumn
wfAsrCircuitEnable = _WfAsrCircuitEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 2),
    _WfAsrCircuitEnable_Type()
)
wfAsrCircuitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrCircuitEnable.setStatus("mandatory")


class _WfAsrCircuitState_Type(Integer32):
    """Custom type wfAsrCircuitState based on Integer32"""
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


_WfAsrCircuitState_Type.__name__ = "Integer32"
_WfAsrCircuitState_Object = MibTableColumn
wfAsrCircuitState = _WfAsrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 3),
    _WfAsrCircuitState_Type()
)
wfAsrCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitState.setStatus("mandatory")
_WfAsrCircuitNumber_Type = Integer32
_WfAsrCircuitNumber_Object = MibTableColumn
wfAsrCircuitNumber = _WfAsrCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 4),
    _WfAsrCircuitNumber_Type()
)
wfAsrCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitNumber.setStatus("mandatory")


class _WfAsrCircuitCallCtrl_Type(Integer32):
    """Custom type wfAsrCircuitCallCtrl based on Integer32"""
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
        *(("inboundandoutbound", 3),
          ("inboundonly", 1),
          ("none", 4),
          ("outboundonly", 2))
    )


_WfAsrCircuitCallCtrl_Type.__name__ = "Integer32"
_WfAsrCircuitCallCtrl_Object = MibTableColumn
wfAsrCircuitCallCtrl = _WfAsrCircuitCallCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 5),
    _WfAsrCircuitCallCtrl_Type()
)
wfAsrCircuitCallCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrCircuitCallCtrl.setStatus("mandatory")
_WfAsrCircuitInReceives_Type = Counter32
_WfAsrCircuitInReceives_Object = MibTableColumn
wfAsrCircuitInReceives = _WfAsrCircuitInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 6),
    _WfAsrCircuitInReceives_Type()
)
wfAsrCircuitInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitInReceives.setStatus("mandatory")
_WfAsrCircuitInDiscards_Type = Counter32
_WfAsrCircuitInDiscards_Object = MibTableColumn
wfAsrCircuitInDiscards = _WfAsrCircuitInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 7),
    _WfAsrCircuitInDiscards_Type()
)
wfAsrCircuitInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitInDiscards.setStatus("mandatory")
_WfAsrCircuitSetupRequests_Type = Counter32
_WfAsrCircuitSetupRequests_Object = MibTableColumn
wfAsrCircuitSetupRequests = _WfAsrCircuitSetupRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 8),
    _WfAsrCircuitSetupRequests_Type()
)
wfAsrCircuitSetupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitSetupRequests.setStatus("mandatory")
_WfAsrCircuitSetupSucc_Type = Counter32
_WfAsrCircuitSetupSucc_Object = MibTableColumn
wfAsrCircuitSetupSucc = _WfAsrCircuitSetupSucc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 9),
    _WfAsrCircuitSetupSucc_Type()
)
wfAsrCircuitSetupSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitSetupSucc.setStatus("mandatory")
_WfAsrCircuitSetupFail_Type = Counter32
_WfAsrCircuitSetupFail_Object = MibTableColumn
wfAsrCircuitSetupFail = _WfAsrCircuitSetupFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 10),
    _WfAsrCircuitSetupFail_Type()
)
wfAsrCircuitSetupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitSetupFail.setStatus("mandatory")
_WfAsrCircuitSVCsEstablished_Type = Counter32
_WfAsrCircuitSVCsEstablished_Object = MibTableColumn
wfAsrCircuitSVCsEstablished = _WfAsrCircuitSVCsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 11),
    _WfAsrCircuitSVCsEstablished_Type()
)
wfAsrCircuitSVCsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrCircuitSVCsEstablished.setStatus("mandatory")
_WfAsrNegativeNHR_Type = Counter32
_WfAsrNegativeNHR_Object = MibTableColumn
wfAsrNegativeNHR = _WfAsrNegativeNHR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 12),
    _WfAsrNegativeNHR_Type()
)
wfAsrNegativeNHR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrNegativeNHR.setStatus("mandatory")
_WfAsrSvcOutboundReqFail_Type = Counter32
_WfAsrSvcOutboundReqFail_Object = MibTableColumn
wfAsrSvcOutboundReqFail = _WfAsrSvcOutboundReqFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 13),
    _WfAsrSvcOutboundReqFail_Type()
)
wfAsrSvcOutboundReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcOutboundReqFail.setStatus("mandatory")
_WfAsrSvcInboundFilterFail_Type = Counter32
_WfAsrSvcInboundFilterFail_Object = MibTableColumn
wfAsrSvcInboundFilterFail = _WfAsrSvcInboundFilterFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 14),
    _WfAsrSvcInboundFilterFail_Type()
)
wfAsrSvcInboundFilterFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcInboundFilterFail.setStatus("mandatory")
_WfAsrSvcInboundCallValFail_Type = Counter32
_WfAsrSvcInboundCallValFail_Object = MibTableColumn
wfAsrSvcInboundCallValFail = _WfAsrSvcInboundCallValFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 6, 1, 15),
    _WfAsrSvcInboundCallValFail_Type()
)
wfAsrSvcInboundCallValFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcInboundCallValFail.setStatus("mandatory")
_WfAsrFiltTable_Object = MibTable
wfAsrFiltTable = _WfAsrFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7)
)
if mibBuilder.loadTexts:
    wfAsrFiltTable.setStatus("mandatory")
_WfAsrFiltEntry_Object = MibTableRow
wfAsrFiltEntry = _WfAsrFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1)
)
wfAsrFiltEntry.setIndexNames(
    (0, "Wellfleet-ASR-MIB", "wfAsrFilterSlot"),
    (0, "Wellfleet-ASR-MIB", "wfAsrDestIpAddr"),
    (0, "Wellfleet-ASR-MIB", "wfAsrDestIpMask"),
    (0, "Wellfleet-ASR-MIB", "wfAsrSourceIpAddr"),
    (0, "Wellfleet-ASR-MIB", "wfAsrSourceIpMask"),
    (0, "Wellfleet-ASR-MIB", "wfAsrDestPortRangeLow"),
    (0, "Wellfleet-ASR-MIB", "wfAsrDestPortRangeHigh"),
    (0, "Wellfleet-ASR-MIB", "wfAsrSourcePortRangeLow"),
    (0, "Wellfleet-ASR-MIB", "wfAsrSourcePortRangeHigh"),
    (0, "Wellfleet-ASR-MIB", "wfAsrIPProtocol"),
)
if mibBuilder.loadTexts:
    wfAsrFiltEntry.setStatus("mandatory")


class _WfAsrFilterCreate_Type(Integer32):
    """Custom type wfAsrFilterCreate based on Integer32"""
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


_WfAsrFilterCreate_Type.__name__ = "Integer32"
_WfAsrFilterCreate_Object = MibTableColumn
wfAsrFilterCreate = _WfAsrFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 1),
    _WfAsrFilterCreate_Type()
)
wfAsrFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrFilterCreate.setStatus("mandatory")
_WfAsrFilterSlot_Type = Integer32
_WfAsrFilterSlot_Object = MibTableColumn
wfAsrFilterSlot = _WfAsrFilterSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 2),
    _WfAsrFilterSlot_Type()
)
wfAsrFilterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFilterSlot.setStatus("mandatory")
_WfAsrDestIpAddr_Type = IpAddress
_WfAsrDestIpAddr_Object = MibTableColumn
wfAsrDestIpAddr = _WfAsrDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 3),
    _WfAsrDestIpAddr_Type()
)
wfAsrDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrDestIpAddr.setStatus("mandatory")
_WfAsrDestIpMask_Type = IpAddress
_WfAsrDestIpMask_Object = MibTableColumn
wfAsrDestIpMask = _WfAsrDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 4),
    _WfAsrDestIpMask_Type()
)
wfAsrDestIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrDestIpMask.setStatus("mandatory")
_WfAsrSourceIpAddr_Type = IpAddress
_WfAsrSourceIpAddr_Object = MibTableColumn
wfAsrSourceIpAddr = _WfAsrSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 5),
    _WfAsrSourceIpAddr_Type()
)
wfAsrSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSourceIpAddr.setStatus("mandatory")
_WfAsrSourceIpMask_Type = IpAddress
_WfAsrSourceIpMask_Object = MibTableColumn
wfAsrSourceIpMask = _WfAsrSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 6),
    _WfAsrSourceIpMask_Type()
)
wfAsrSourceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSourceIpMask.setStatus("mandatory")
_WfAsrDestPortRangeLow_Type = Integer32
_WfAsrDestPortRangeLow_Object = MibTableColumn
wfAsrDestPortRangeLow = _WfAsrDestPortRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 7),
    _WfAsrDestPortRangeLow_Type()
)
wfAsrDestPortRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrDestPortRangeLow.setStatus("mandatory")
_WfAsrDestPortRangeHigh_Type = Integer32
_WfAsrDestPortRangeHigh_Object = MibTableColumn
wfAsrDestPortRangeHigh = _WfAsrDestPortRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 8),
    _WfAsrDestPortRangeHigh_Type()
)
wfAsrDestPortRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrDestPortRangeHigh.setStatus("mandatory")
_WfAsrSourcePortRangeLow_Type = Integer32
_WfAsrSourcePortRangeLow_Object = MibTableColumn
wfAsrSourcePortRangeLow = _WfAsrSourcePortRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 9),
    _WfAsrSourcePortRangeLow_Type()
)
wfAsrSourcePortRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSourcePortRangeLow.setStatus("mandatory")
_WfAsrSourcePortRangeHigh_Type = Integer32
_WfAsrSourcePortRangeHigh_Object = MibTableColumn
wfAsrSourcePortRangeHigh = _WfAsrSourcePortRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 10),
    _WfAsrSourcePortRangeHigh_Type()
)
wfAsrSourcePortRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSourcePortRangeHigh.setStatus("mandatory")
_WfAsrIPProtocol_Type = Integer32
_WfAsrIPProtocol_Object = MibTableColumn
wfAsrIPProtocol = _WfAsrIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 11),
    _WfAsrIPProtocol_Type()
)
wfAsrIPProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrIPProtocol.setStatus("mandatory")
_WfAsrFilterTtl_Type = Integer32
_WfAsrFilterTtl_Object = MibTableColumn
wfAsrFilterTtl = _WfAsrFilterTtl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 12),
    _WfAsrFilterTtl_Type()
)
wfAsrFilterTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFilterTtl.setStatus("mandatory")
_WfAsrFilterType_Type = DisplayString
_WfAsrFilterType_Object = MibTableColumn
wfAsrFilterType = _WfAsrFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 13),
    _WfAsrFilterType_Type()
)
wfAsrFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFilterType.setStatus("mandatory")
_WfAsrSvcCircuitNumber_Type = Integer32
_WfAsrSvcCircuitNumber_Object = MibTableColumn
wfAsrSvcCircuitNumber = _WfAsrSvcCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 14),
    _WfAsrSvcCircuitNumber_Type()
)
wfAsrSvcCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcCircuitNumber.setStatus("mandatory")
_WfAsrSvcVcid1_Type = Integer32
_WfAsrSvcVcid1_Object = MibTableColumn
wfAsrSvcVcid1 = _WfAsrSvcVcid1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 15),
    _WfAsrSvcVcid1_Type()
)
wfAsrSvcVcid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcVcid1.setStatus("mandatory")
_WfAsrSvcVcid2_Type = Integer32
_WfAsrSvcVcid2_Object = MibTableColumn
wfAsrSvcVcid2 = _WfAsrSvcVcid2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 16),
    _WfAsrSvcVcid2_Type()
)
wfAsrSvcVcid2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcVcid2.setStatus("mandatory")
_WfAsrSvcCalledAddr_Type = DisplayString
_WfAsrSvcCalledAddr_Object = MibTableColumn
wfAsrSvcCalledAddr = _WfAsrSvcCalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 17),
    _WfAsrSvcCalledAddr_Type()
)
wfAsrSvcCalledAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcCalledAddr.setStatus("mandatory")
_WfAsrSvcSetupTime_Type = Integer32
_WfAsrSvcSetupTime_Object = MibTableColumn
wfAsrSvcSetupTime = _WfAsrSvcSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 18),
    _WfAsrSvcSetupTime_Type()
)
wfAsrSvcSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcSetupTime.setStatus("mandatory")


class _WfAsrSvcType_Type(Integer32):
    """Custom type wfAsrSvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfAsrSvcType_Type.__name__ = "Integer32"
_WfAsrSvcType_Object = MibTableColumn
wfAsrSvcType = _WfAsrSvcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 19),
    _WfAsrSvcType_Type()
)
wfAsrSvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrSvcType.setStatus("mandatory")
_WfAsrSvcMTU_Type = Integer32
_WfAsrSvcMTU_Object = MibTableColumn
wfAsrSvcMTU = _WfAsrSvcMTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 20),
    _WfAsrSvcMTU_Type()
)
wfAsrSvcMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcMTU.setStatus("mandatory")
_WfAsrSvcRouterPriOut_Type = Integer32
_WfAsrSvcRouterPriOut_Object = MibTableColumn
wfAsrSvcRouterPriOut = _WfAsrSvcRouterPriOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 21),
    _WfAsrSvcRouterPriOut_Type()
)
wfAsrSvcRouterPriOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrSvcRouterPriOut.setStatus("mandatory")
_WfAsrFrSvcCIRIn_Type = Integer32
_WfAsrFrSvcCIRIn_Object = MibTableColumn
wfAsrFrSvcCIRIn = _WfAsrFrSvcCIRIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 22),
    _WfAsrFrSvcCIRIn_Type()
)
wfAsrFrSvcCIRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFrSvcCIRIn.setStatus("mandatory")
_WfAsrFrSvcCIROut_Type = Integer32
_WfAsrFrSvcCIROut_Object = MibTableColumn
wfAsrFrSvcCIROut = _WfAsrFrSvcCIROut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 23),
    _WfAsrFrSvcCIROut_Type()
)
wfAsrFrSvcCIROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFrSvcCIROut.setStatus("mandatory")
_WfAsrFrSvcBCIn_Type = Integer32
_WfAsrFrSvcBCIn_Object = MibTableColumn
wfAsrFrSvcBCIn = _WfAsrFrSvcBCIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 24),
    _WfAsrFrSvcBCIn_Type()
)
wfAsrFrSvcBCIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFrSvcBCIn.setStatus("mandatory")
_WfAsrFrSvcBCOut_Type = Integer32
_WfAsrFrSvcBCOut_Object = MibTableColumn
wfAsrFrSvcBCOut = _WfAsrFrSvcBCOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 25),
    _WfAsrFrSvcBCOut_Type()
)
wfAsrFrSvcBCOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFrSvcBCOut.setStatus("mandatory")
_WfAsrFrSvcBEIn_Type = Integer32
_WfAsrFrSvcBEIn_Object = MibTableColumn
wfAsrFrSvcBEIn = _WfAsrFrSvcBEIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 26),
    _WfAsrFrSvcBEIn_Type()
)
wfAsrFrSvcBEIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFrSvcBEIn.setStatus("mandatory")
_WfAsrFrSvcBEOut_Type = Integer32
_WfAsrFrSvcBEOut_Object = MibTableColumn
wfAsrFrSvcBEOut = _WfAsrFrSvcBEOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 27),
    _WfAsrFrSvcBEOut_Type()
)
wfAsrFrSvcBEOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFrSvcBEOut.setStatus("mandatory")
_WfAsrFrSvcX213Pri_Type = Integer32
_WfAsrFrSvcX213Pri_Object = MibTableColumn
wfAsrFrSvcX213Pri = _WfAsrFrSvcX213Pri_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 28),
    _WfAsrFrSvcX213Pri_Type()
)
wfAsrFrSvcX213Pri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrFrSvcX213Pri.setStatus("mandatory")
_WfAsrAtmSvcPCRIn_Type = Integer32
_WfAsrAtmSvcPCRIn_Object = MibTableColumn
wfAsrAtmSvcPCRIn = _WfAsrAtmSvcPCRIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 29),
    _WfAsrAtmSvcPCRIn_Type()
)
wfAsrAtmSvcPCRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcPCRIn.setStatus("mandatory")
_WfAsrAtmSvcPCROut_Type = Integer32
_WfAsrAtmSvcPCROut_Object = MibTableColumn
wfAsrAtmSvcPCROut = _WfAsrAtmSvcPCROut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 30),
    _WfAsrAtmSvcPCROut_Type()
)
wfAsrAtmSvcPCROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcPCROut.setStatus("mandatory")
_WfAsrAtmSvcSCRIn_Type = Integer32
_WfAsrAtmSvcSCRIn_Object = MibTableColumn
wfAsrAtmSvcSCRIn = _WfAsrAtmSvcSCRIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 31),
    _WfAsrAtmSvcSCRIn_Type()
)
wfAsrAtmSvcSCRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcSCRIn.setStatus("mandatory")
_WfAsrAtmSvcSCROut_Type = Integer32
_WfAsrAtmSvcSCROut_Object = MibTableColumn
wfAsrAtmSvcSCROut = _WfAsrAtmSvcSCROut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 32),
    _WfAsrAtmSvcSCROut_Type()
)
wfAsrAtmSvcSCROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcSCROut.setStatus("mandatory")
_WfAsrAtmSvcMBSIn_Type = Integer32
_WfAsrAtmSvcMBSIn_Object = MibTableColumn
wfAsrAtmSvcMBSIn = _WfAsrAtmSvcMBSIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 33),
    _WfAsrAtmSvcMBSIn_Type()
)
wfAsrAtmSvcMBSIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcMBSIn.setStatus("mandatory")
_WfAsrAtmSvcMBSOut_Type = Integer32
_WfAsrAtmSvcMBSOut_Object = MibTableColumn
wfAsrAtmSvcMBSOut = _WfAsrAtmSvcMBSOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 34),
    _WfAsrAtmSvcMBSOut_Type()
)
wfAsrAtmSvcMBSOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcMBSOut.setStatus("mandatory")
_WfAsrAtmSvcQOSClassIn_Type = Integer32
_WfAsrAtmSvcQOSClassIn_Object = MibTableColumn
wfAsrAtmSvcQOSClassIn = _WfAsrAtmSvcQOSClassIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 35),
    _WfAsrAtmSvcQOSClassIn_Type()
)
wfAsrAtmSvcQOSClassIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcQOSClassIn.setStatus("mandatory")
_WfAsrAtmSvcQOSClassOut_Type = Integer32
_WfAsrAtmSvcQOSClassOut_Object = MibTableColumn
wfAsrAtmSvcQOSClassOut = _WfAsrAtmSvcQOSClassOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 36),
    _WfAsrAtmSvcQOSClassOut_Type()
)
wfAsrAtmSvcQOSClassOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcQOSClassOut.setStatus("mandatory")
_WfAsrAtmSvcCDVTIn_Type = Integer32
_WfAsrAtmSvcCDVTIn_Object = MibTableColumn
wfAsrAtmSvcCDVTIn = _WfAsrAtmSvcCDVTIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 37),
    _WfAsrAtmSvcCDVTIn_Type()
)
wfAsrAtmSvcCDVTIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcCDVTIn.setStatus("mandatory")
_WfAsrAtmSvcCDVTOut_Type = Integer32
_WfAsrAtmSvcCDVTOut_Object = MibTableColumn
wfAsrAtmSvcCDVTOut = _WfAsrAtmSvcCDVTOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 38),
    _WfAsrAtmSvcCDVTOut_Type()
)
wfAsrAtmSvcCDVTOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcCDVTOut.setStatus("mandatory")
_WfAsrAtmSvcCLRIn_Type = Integer32
_WfAsrAtmSvcCLRIn_Object = MibTableColumn
wfAsrAtmSvcCLRIn = _WfAsrAtmSvcCLRIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 39),
    _WfAsrAtmSvcCLRIn_Type()
)
wfAsrAtmSvcCLRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcCLRIn.setStatus("mandatory")
_WfAsrAtmSvcCLROut_Type = Integer32
_WfAsrAtmSvcCLROut_Object = MibTableColumn
wfAsrAtmSvcCLROut = _WfAsrAtmSvcCLROut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 7, 1, 40),
    _WfAsrAtmSvcCLROut_Type()
)
wfAsrAtmSvcCLROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsrAtmSvcCLROut.setStatus("mandatory")
_WfAsrTest_ObjectIdentity = ObjectIdentity
wfAsrTest = _WfAsrTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 8)
)


class _WfAsrTestCreate_Type(Integer32):
    """Custom type wfAsrTestCreate based on Integer32"""
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


_WfAsrTestCreate_Type.__name__ = "Integer32"
_WfAsrTestCreate_Object = MibScalar
wfAsrTestCreate = _WfAsrTestCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 8, 1),
    _WfAsrTestCreate_Type()
)
wfAsrTestCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrTestCreate.setStatus("mandatory")


class _WfAsrTestChangeVal_Type(Integer32):
    """Custom type wfAsrTestChangeVal based on Integer32"""
    defaultValue = 6


_WfAsrTestChangeVal_Object = MibScalar
wfAsrTestChangeVal = _WfAsrTestChangeVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 8, 2),
    _WfAsrTestChangeVal_Type()
)
wfAsrTestChangeVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrTestChangeVal.setStatus("mandatory")
_WfAsrTestDlci_Type = Integer32
_WfAsrTestDlci_Object = MibScalar
wfAsrTestDlci = _WfAsrTestDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 8, 3),
    _WfAsrTestDlci_Type()
)
wfAsrTestDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrTestDlci.setStatus("mandatory")
_WfAsrTestCct_Type = Integer32
_WfAsrTestCct_Object = MibScalar
wfAsrTestCct = _WfAsrTestCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11, 8, 4),
    _WfAsrTestCct_Type()
)
wfAsrTestCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsrTestCct.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ASR-MIB",
    **{"wfAsrBase": wfAsrBase,
       "wfAsrBaseCreate": wfAsrBaseCreate,
       "wfAsrBaseEnable": wfAsrBaseEnable,
       "wfAsrBaseState": wfAsrBaseState,
       "wfAsrNextHopRetryLimit": wfAsrNextHopRetryLimit,
       "wfAsrSecureInFilter": wfAsrSecureInFilter,
       "wfAsrSecureInValid": wfAsrSecureInValid,
       "wfAsrHoldDownTimer": wfAsrHoldDownTimer,
       "wfAsrActiveSvcs": wfAsrActiveSvcs,
       "wfAsrFwdTblEntries": wfAsrFwdTblEntries,
       "wfAsrFwdTblSeq": wfAsrFwdTblSeq,
       "wfAsrDnsProxyPort": wfAsrDnsProxyPort,
       "wfAsrMaxSessions": wfAsrMaxSessions,
       "wfAsrDebugLevel": wfAsrDebugLevel,
       "wfAsrUseDynRdiscPref": wfAsrUseDynRdiscPref,
       "wfAsrX213PriTable": wfAsrX213PriTable,
       "wfAsrX213PriEntry": wfAsrX213PriEntry,
       "wfAsrX213PriDelete": wfAsrX213PriDelete,
       "wfAsrX213PriLowVal": wfAsrX213PriLowVal,
       "wfAsrX213PriHiVal": wfAsrX213PriHiVal,
       "wfAsrX213PriSwVal": wfAsrX213PriSwVal,
       "wfAsrRtrPriTable": wfAsrRtrPriTable,
       "wfAsrRtrPriEntry": wfAsrRtrPriEntry,
       "wfAsrRtrPriDelete": wfAsrRtrPriDelete,
       "wfAsrRtrPriLowVal": wfAsrRtrPriLowVal,
       "wfAsrRtrPriHiVal": wfAsrRtrPriHiVal,
       "wfAsrRtrPriCvtVal": wfAsrRtrPriCvtVal,
       "wfAsrMultiHopTable": wfAsrMultiHopTable,
       "wfAsrMultiHopEntry": wfAsrMultiHopEntry,
       "wfAsrMultiHopDelete": wfAsrMultiHopDelete,
       "wfAsrMhCircuitNumber": wfAsrMhCircuitNumber,
       "wfAsrMhVcid1": wfAsrMhVcid1,
       "wfAsrMhVcid2": wfAsrMhVcid2,
       "wfAsrDirectExceptTable": wfAsrDirectExceptTable,
       "wfAsrDirectExceptEntry": wfAsrDirectExceptEntry,
       "wfAsrServiceProtocol": wfAsrServiceProtocol,
       "wfAsrServicePort": wfAsrServicePort,
       "wfAsrSrcPortLow": wfAsrSrcPortLow,
       "wfAsrSrcPortHigh": wfAsrSrcPortHigh,
       "wfAsrDestPortLow": wfAsrDestPortLow,
       "wfAsrDestPortHigh": wfAsrDestPortHigh,
       "wfAsrCircuitTable": wfAsrCircuitTable,
       "wfAsrCircuitEntry": wfAsrCircuitEntry,
       "wfAsrCircuitCreate": wfAsrCircuitCreate,
       "wfAsrCircuitEnable": wfAsrCircuitEnable,
       "wfAsrCircuitState": wfAsrCircuitState,
       "wfAsrCircuitNumber": wfAsrCircuitNumber,
       "wfAsrCircuitCallCtrl": wfAsrCircuitCallCtrl,
       "wfAsrCircuitInReceives": wfAsrCircuitInReceives,
       "wfAsrCircuitInDiscards": wfAsrCircuitInDiscards,
       "wfAsrCircuitSetupRequests": wfAsrCircuitSetupRequests,
       "wfAsrCircuitSetupSucc": wfAsrCircuitSetupSucc,
       "wfAsrCircuitSetupFail": wfAsrCircuitSetupFail,
       "wfAsrCircuitSVCsEstablished": wfAsrCircuitSVCsEstablished,
       "wfAsrNegativeNHR": wfAsrNegativeNHR,
       "wfAsrSvcOutboundReqFail": wfAsrSvcOutboundReqFail,
       "wfAsrSvcInboundFilterFail": wfAsrSvcInboundFilterFail,
       "wfAsrSvcInboundCallValFail": wfAsrSvcInboundCallValFail,
       "wfAsrFiltTable": wfAsrFiltTable,
       "wfAsrFiltEntry": wfAsrFiltEntry,
       "wfAsrFilterCreate": wfAsrFilterCreate,
       "wfAsrFilterSlot": wfAsrFilterSlot,
       "wfAsrDestIpAddr": wfAsrDestIpAddr,
       "wfAsrDestIpMask": wfAsrDestIpMask,
       "wfAsrSourceIpAddr": wfAsrSourceIpAddr,
       "wfAsrSourceIpMask": wfAsrSourceIpMask,
       "wfAsrDestPortRangeLow": wfAsrDestPortRangeLow,
       "wfAsrDestPortRangeHigh": wfAsrDestPortRangeHigh,
       "wfAsrSourcePortRangeLow": wfAsrSourcePortRangeLow,
       "wfAsrSourcePortRangeHigh": wfAsrSourcePortRangeHigh,
       "wfAsrIPProtocol": wfAsrIPProtocol,
       "wfAsrFilterTtl": wfAsrFilterTtl,
       "wfAsrFilterType": wfAsrFilterType,
       "wfAsrSvcCircuitNumber": wfAsrSvcCircuitNumber,
       "wfAsrSvcVcid1": wfAsrSvcVcid1,
       "wfAsrSvcVcid2": wfAsrSvcVcid2,
       "wfAsrSvcCalledAddr": wfAsrSvcCalledAddr,
       "wfAsrSvcSetupTime": wfAsrSvcSetupTime,
       "wfAsrSvcType": wfAsrSvcType,
       "wfAsrSvcMTU": wfAsrSvcMTU,
       "wfAsrSvcRouterPriOut": wfAsrSvcRouterPriOut,
       "wfAsrFrSvcCIRIn": wfAsrFrSvcCIRIn,
       "wfAsrFrSvcCIROut": wfAsrFrSvcCIROut,
       "wfAsrFrSvcBCIn": wfAsrFrSvcBCIn,
       "wfAsrFrSvcBCOut": wfAsrFrSvcBCOut,
       "wfAsrFrSvcBEIn": wfAsrFrSvcBEIn,
       "wfAsrFrSvcBEOut": wfAsrFrSvcBEOut,
       "wfAsrFrSvcX213Pri": wfAsrFrSvcX213Pri,
       "wfAsrAtmSvcPCRIn": wfAsrAtmSvcPCRIn,
       "wfAsrAtmSvcPCROut": wfAsrAtmSvcPCROut,
       "wfAsrAtmSvcSCRIn": wfAsrAtmSvcSCRIn,
       "wfAsrAtmSvcSCROut": wfAsrAtmSvcSCROut,
       "wfAsrAtmSvcMBSIn": wfAsrAtmSvcMBSIn,
       "wfAsrAtmSvcMBSOut": wfAsrAtmSvcMBSOut,
       "wfAsrAtmSvcQOSClassIn": wfAsrAtmSvcQOSClassIn,
       "wfAsrAtmSvcQOSClassOut": wfAsrAtmSvcQOSClassOut,
       "wfAsrAtmSvcCDVTIn": wfAsrAtmSvcCDVTIn,
       "wfAsrAtmSvcCDVTOut": wfAsrAtmSvcCDVTOut,
       "wfAsrAtmSvcCLRIn": wfAsrAtmSvcCLRIn,
       "wfAsrAtmSvcCLROut": wfAsrAtmSvcCLROut,
       "wfAsrTest": wfAsrTest,
       "wfAsrTestCreate": wfAsrTestCreate,
       "wfAsrTestChangeVal": wfAsrTestChangeVal,
       "wfAsrTestDlci": wfAsrTestDlci,
       "wfAsrTestCct": wfAsrTestCct}
)
