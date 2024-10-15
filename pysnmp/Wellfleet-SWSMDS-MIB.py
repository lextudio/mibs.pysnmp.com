# SNMP MIB module (Wellfleet-SWSMDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SWSMDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:10 2024
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

(wfSmdsSwGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSmdsSwGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSmdsSwSubTable_Object = MibTable
wfSmdsSwSubTable = _WfSmdsSwSubTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1)
)
if mibBuilder.loadTexts:
    wfSmdsSwSubTable.setStatus("mandatory")
_WfSmdsSwSubEntry_Object = MibTableRow
wfSmdsSwSubEntry = _WfSmdsSwSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1)
)
wfSmdsSwSubEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwSubCct"),
)
if mibBuilder.loadTexts:
    wfSmdsSwSubEntry.setStatus("mandatory")


class _WfSmdsSwSubDelete_Type(Integer32):
    """Custom type wfSmdsSwSubDelete based on Integer32"""
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


_WfSmdsSwSubDelete_Type.__name__ = "Integer32"
_WfSmdsSwSubDelete_Object = MibTableColumn
wfSmdsSwSubDelete = _WfSmdsSwSubDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 1),
    _WfSmdsSwSubDelete_Type()
)
wfSmdsSwSubDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubDelete.setStatus("mandatory")


class _WfSmdsSwSubDisable_Type(Integer32):
    """Custom type wfSmdsSwSubDisable based on Integer32"""
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


_WfSmdsSwSubDisable_Type.__name__ = "Integer32"
_WfSmdsSwSubDisable_Object = MibTableColumn
wfSmdsSwSubDisable = _WfSmdsSwSubDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 2),
    _WfSmdsSwSubDisable_Type()
)
wfSmdsSwSubDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubDisable.setStatus("mandatory")


class _WfSmdsSwSubState_Type(Integer32):
    """Custom type wfSmdsSwSubState based on Integer32"""
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


_WfSmdsSwSubState_Type.__name__ = "Integer32"
_WfSmdsSwSubState_Object = MibTableColumn
wfSmdsSwSubState = _WfSmdsSwSubState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 3),
    _WfSmdsSwSubState_Type()
)
wfSmdsSwSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubState.setStatus("mandatory")


class _WfSmdsSwSubCct_Type(Integer32):
    """Custom type wfSmdsSwSubCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfSmdsSwSubCct_Type.__name__ = "Integer32"
_WfSmdsSwSubCct_Object = MibTableColumn
wfSmdsSwSubCct = _WfSmdsSwSubCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 4),
    _WfSmdsSwSubCct_Type()
)
wfSmdsSwSubCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubCct.setStatus("mandatory")


class _WfSmdsSwSubDisableHrtbtPoll_Type(Integer32):
    """Custom type wfSmdsSwSubDisableHrtbtPoll based on Integer32"""
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


_WfSmdsSwSubDisableHrtbtPoll_Type.__name__ = "Integer32"
_WfSmdsSwSubDisableHrtbtPoll_Object = MibTableColumn
wfSmdsSwSubDisableHrtbtPoll = _WfSmdsSwSubDisableHrtbtPoll_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 5),
    _WfSmdsSwSubDisableHrtbtPoll_Type()
)
wfSmdsSwSubDisableHrtbtPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubDisableHrtbtPoll.setStatus("mandatory")


class _WfSmdsSwSubHrtbtPollAddr_Type(Integer32):
    """Custom type wfSmdsSwSubHrtbtPollAddr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpe", 1),
          ("net", 2))
    )


_WfSmdsSwSubHrtbtPollAddr_Type.__name__ = "Integer32"
_WfSmdsSwSubHrtbtPollAddr_Object = MibTableColumn
wfSmdsSwSubHrtbtPollAddr = _WfSmdsSwSubHrtbtPollAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 6),
    _WfSmdsSwSubHrtbtPollAddr_Type()
)
wfSmdsSwSubHrtbtPollAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubHrtbtPollAddr.setStatus("mandatory")


class _WfSmdsSwSubHrtbtPollInterval_Type(Integer32):
    """Custom type wfSmdsSwSubHrtbtPollInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 2147483647),
    )


_WfSmdsSwSubHrtbtPollInterval_Type.__name__ = "Integer32"
_WfSmdsSwSubHrtbtPollInterval_Object = MibTableColumn
wfSmdsSwSubHrtbtPollInterval = _WfSmdsSwSubHrtbtPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 7),
    _WfSmdsSwSubHrtbtPollInterval_Type()
)
wfSmdsSwSubHrtbtPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubHrtbtPollInterval.setStatus("mandatory")


class _WfSmdsSwSubHrtbtPollDownCount_Type(Integer32):
    """Custom type wfSmdsSwSubHrtbtPollDownCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfSmdsSwSubHrtbtPollDownCount_Type.__name__ = "Integer32"
_WfSmdsSwSubHrtbtPollDownCount_Object = MibTableColumn
wfSmdsSwSubHrtbtPollDownCount = _WfSmdsSwSubHrtbtPollDownCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 8),
    _WfSmdsSwSubHrtbtPollDownCount_Type()
)
wfSmdsSwSubHrtbtPollDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubHrtbtPollDownCount.setStatus("mandatory")


class _WfSmdsSwSubDisableNetMgmt_Type(Integer32):
    """Custom type wfSmdsSwSubDisableNetMgmt based on Integer32"""
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


_WfSmdsSwSubDisableNetMgmt_Type.__name__ = "Integer32"
_WfSmdsSwSubDisableNetMgmt_Object = MibTableColumn
wfSmdsSwSubDisableNetMgmt = _WfSmdsSwSubDisableNetMgmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 9),
    _WfSmdsSwSubDisableNetMgmt_Type()
)
wfSmdsSwSubDisableNetMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubDisableNetMgmt.setStatus("mandatory")


class _WfSmdsSwSubInterfaceType_Type(Integer32):
    """Custom type wfSmdsSwSubInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sni", 1),
          ("ssi", 2))
    )


_WfSmdsSwSubInterfaceType_Type.__name__ = "Integer32"
_WfSmdsSwSubInterfaceType_Object = MibTableColumn
wfSmdsSwSubInterfaceType = _WfSmdsSwSubInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 10),
    _WfSmdsSwSubInterfaceType_Type()
)
wfSmdsSwSubInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubInterfaceType.setStatus("mandatory")
_WfSmdsSwSubInterfaceIndex_Type = Integer32
_WfSmdsSwSubInterfaceIndex_Object = MibTableColumn
wfSmdsSwSubInterfaceIndex = _WfSmdsSwSubInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 11),
    _WfSmdsSwSubInterfaceIndex_Type()
)
wfSmdsSwSubInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubInterfaceIndex.setStatus("mandatory")


class _WfSmdsSwSubDisableL3PduChecks_Type(Integer32):
    """Custom type wfSmdsSwSubDisableL3PduChecks based on Integer32"""
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


_WfSmdsSwSubDisableL3PduChecks_Type.__name__ = "Integer32"
_WfSmdsSwSubDisableL3PduChecks_Object = MibTableColumn
wfSmdsSwSubDisableL3PduChecks = _WfSmdsSwSubDisableL3PduChecks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 12),
    _WfSmdsSwSubDisableL3PduChecks_Type()
)
wfSmdsSwSubDisableL3PduChecks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubDisableL3PduChecks.setStatus("mandatory")


class _WfSmdsSwSubDisableUsageGeneration_Type(Integer32):
    """Custom type wfSmdsSwSubDisableUsageGeneration based on Integer32"""
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


_WfSmdsSwSubDisableUsageGeneration_Type.__name__ = "Integer32"
_WfSmdsSwSubDisableUsageGeneration_Object = MibTableColumn
wfSmdsSwSubDisableUsageGeneration = _WfSmdsSwSubDisableUsageGeneration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 13),
    _WfSmdsSwSubDisableUsageGeneration_Type()
)
wfSmdsSwSubDisableUsageGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubDisableUsageGeneration.setStatus("mandatory")


class _WfSmdsSwSubDisableMIR_Type(Integer32):
    """Custom type wfSmdsSwSubDisableMIR based on Integer32"""
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


_WfSmdsSwSubDisableMIR_Type.__name__ = "Integer32"
_WfSmdsSwSubDisableMIR_Object = MibTableColumn
wfSmdsSwSubDisableMIR = _WfSmdsSwSubDisableMIR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 14),
    _WfSmdsSwSubDisableMIR_Type()
)
wfSmdsSwSubDisableMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubDisableMIR.setStatus("mandatory")
_WfSmdsSwSubUnassignedSAs_Type = Counter32
_WfSmdsSwSubUnassignedSAs_Object = MibTableColumn
wfSmdsSwSubUnassignedSAs = _WfSmdsSwSubUnassignedSAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 15),
    _WfSmdsSwSubUnassignedSAs_Type()
)
wfSmdsSwSubUnassignedSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubUnassignedSAs.setStatus("mandatory")
_WfSmdsSwSubSAScreenViolations_Type = Counter32
_WfSmdsSwSubSAScreenViolations_Object = MibTableColumn
wfSmdsSwSubSAScreenViolations = _WfSmdsSwSubSAScreenViolations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 16),
    _WfSmdsSwSubSAScreenViolations_Type()
)
wfSmdsSwSubSAScreenViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSAScreenViolations.setStatus("mandatory")
_WfSmdsSwSubDAScreenViolations_Type = Counter32
_WfSmdsSwSubDAScreenViolations_Object = MibTableColumn
wfSmdsSwSubDAScreenViolations = _WfSmdsSwSubDAScreenViolations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 17),
    _WfSmdsSwSubDAScreenViolations_Type()
)
wfSmdsSwSubDAScreenViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubDAScreenViolations.setStatus("mandatory")
_WfSmdsSwSubNumPDUExceededMIR_Type = Counter32
_WfSmdsSwSubNumPDUExceededMIR_Object = MibTableColumn
wfSmdsSwSubNumPDUExceededMIR = _WfSmdsSwSubNumPDUExceededMIR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 18),
    _WfSmdsSwSubNumPDUExceededMIR_Type()
)
wfSmdsSwSubNumPDUExceededMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubNumPDUExceededMIR.setStatus("mandatory")
_WfSmdsSwSubSipL3ReceivedIAs_Type = Counter32
_WfSmdsSwSubSipL3ReceivedIAs_Object = MibTableColumn
wfSmdsSwSubSipL3ReceivedIAs = _WfSmdsSwSubSipL3ReceivedIAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 19),
    _WfSmdsSwSubSipL3ReceivedIAs_Type()
)
wfSmdsSwSubSipL3ReceivedIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3ReceivedIAs.setStatus("mandatory")
_WfSmdsSwSubSipL3ReceivedGAs_Type = Counter32
_WfSmdsSwSubSipL3ReceivedGAs_Object = MibTableColumn
wfSmdsSwSubSipL3ReceivedGAs = _WfSmdsSwSubSipL3ReceivedGAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 20),
    _WfSmdsSwSubSipL3ReceivedGAs_Type()
)
wfSmdsSwSubSipL3ReceivedGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3ReceivedGAs.setStatus("mandatory")
_WfSmdsSwSubSipL3UnrecIAs_Type = Counter32
_WfSmdsSwSubSipL3UnrecIAs_Object = MibTableColumn
wfSmdsSwSubSipL3UnrecIAs = _WfSmdsSwSubSipL3UnrecIAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 21),
    _WfSmdsSwSubSipL3UnrecIAs_Type()
)
wfSmdsSwSubSipL3UnrecIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3UnrecIAs.setStatus("mandatory")
_WfSmdsSwSubSipL3UnrecGAs_Type = Counter32
_WfSmdsSwSubSipL3UnrecGAs_Object = MibTableColumn
wfSmdsSwSubSipL3UnrecGAs = _WfSmdsSwSubSipL3UnrecGAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 22),
    _WfSmdsSwSubSipL3UnrecGAs_Type()
)
wfSmdsSwSubSipL3UnrecGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3UnrecGAs.setStatus("mandatory")
_WfSmdsSwSubSipL3SentIAs_Type = Counter32
_WfSmdsSwSubSipL3SentIAs_Object = MibTableColumn
wfSmdsSwSubSipL3SentIAs = _WfSmdsSwSubSipL3SentIAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 23),
    _WfSmdsSwSubSipL3SentIAs_Type()
)
wfSmdsSwSubSipL3SentIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3SentIAs.setStatus("mandatory")
_WfSmdsSwSubSipL3SentGAs_Type = Counter32
_WfSmdsSwSubSipL3SentGAs_Object = MibTableColumn
wfSmdsSwSubSipL3SentGAs = _WfSmdsSwSubSipL3SentGAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 24),
    _WfSmdsSwSubSipL3SentGAs_Type()
)
wfSmdsSwSubSipL3SentGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3SentGAs.setStatus("mandatory")
_WfSmdsSwSubSipL3Errors_Type = Counter32
_WfSmdsSwSubSipL3Errors_Object = MibTableColumn
wfSmdsSwSubSipL3Errors = _WfSmdsSwSubSipL3Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 25),
    _WfSmdsSwSubSipL3Errors_Type()
)
wfSmdsSwSubSipL3Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3Errors.setStatus("mandatory")
_WfSmdsSwSubSipL3InvAddrTypes_Type = Counter32
_WfSmdsSwSubSipL3InvAddrTypes_Object = MibTableColumn
wfSmdsSwSubSipL3InvAddrTypes = _WfSmdsSwSubSipL3InvAddrTypes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 26),
    _WfSmdsSwSubSipL3InvAddrTypes_Type()
)
wfSmdsSwSubSipL3InvAddrTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3InvAddrTypes.setStatus("mandatory")


class _WfSmdsSwSubSipL3VersionSupport_Type(Integer32):
    """Custom type wfSmdsSwSubSipL3VersionSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version", 1)
    )


_WfSmdsSwSubSipL3VersionSupport_Type.__name__ = "Integer32"
_WfSmdsSwSubSipL3VersionSupport_Object = MibTableColumn
wfSmdsSwSubSipL3VersionSupport = _WfSmdsSwSubSipL3VersionSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 27),
    _WfSmdsSwSubSipL3VersionSupport_Type()
)
wfSmdsSwSubSipL3VersionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSipL3VersionSupport.setStatus("mandatory")
_WfSmdsSwSubSAScrnViolationOccur_Type = OctetString
_WfSmdsSwSubSAScrnViolationOccur_Object = MibTableColumn
wfSmdsSwSubSAScrnViolationOccur = _WfSmdsSwSubSAScrnViolationOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 28),
    _WfSmdsSwSubSAScrnViolationOccur_Type()
)
wfSmdsSwSubSAScrnViolationOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSAScrnViolationOccur.setStatus("mandatory")
_WfSmdsSwSubDAScrnViolationOccur_Type = OctetString
_WfSmdsSwSubDAScrnViolationOccur_Object = MibTableColumn
wfSmdsSwSubDAScrnViolationOccur = _WfSmdsSwSubDAScrnViolationOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 29),
    _WfSmdsSwSubDAScrnViolationOccur_Type()
)
wfSmdsSwSubDAScrnViolationOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubDAScrnViolationOccur.setStatus("mandatory")
_WfSmdsSwSubUnassignedSAOccur_Type = OctetString
_WfSmdsSwSubUnassignedSAOccur_Object = MibTableColumn
wfSmdsSwSubUnassignedSAOccur = _WfSmdsSwSubUnassignedSAOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 30),
    _WfSmdsSwSubUnassignedSAOccur_Type()
)
wfSmdsSwSubUnassignedSAOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubUnassignedSAOccur.setStatus("mandatory")
_WfSmdsSwSubSAErrorOccur_Type = OctetString
_WfSmdsSwSubSAErrorOccur_Object = MibTableColumn
wfSmdsSwSubSAErrorOccur = _WfSmdsSwSubSAErrorOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 31),
    _WfSmdsSwSubSAErrorOccur_Type()
)
wfSmdsSwSubSAErrorOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubSAErrorOccur.setStatus("mandatory")
_WfSmdsSwSubDAErrorOccur_Type = OctetString
_WfSmdsSwSubDAErrorOccur_Object = MibTableColumn
wfSmdsSwSubDAErrorOccur = _WfSmdsSwSubDAErrorOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 32),
    _WfSmdsSwSubDAErrorOccur_Type()
)
wfSmdsSwSubDAErrorOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubDAErrorOccur.setStatus("mandatory")
_WfSmdsSwSubInvalidBASizeOccur_Type = OctetString
_WfSmdsSwSubInvalidBASizeOccur_Object = MibTableColumn
wfSmdsSwSubInvalidBASizeOccur = _WfSmdsSwSubInvalidBASizeOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 33),
    _WfSmdsSwSubInvalidBASizeOccur_Type()
)
wfSmdsSwSubInvalidBASizeOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInvalidBASizeOccur.setStatus("mandatory")
_WfSmdsSwSubInvalidHELenOccur_Type = OctetString
_WfSmdsSwSubInvalidHELenOccur_Object = MibTableColumn
wfSmdsSwSubInvalidHELenOccur = _WfSmdsSwSubInvalidHELenOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 34),
    _WfSmdsSwSubInvalidHELenOccur_Type()
)
wfSmdsSwSubInvalidHELenOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInvalidHELenOccur.setStatus("mandatory")
_WfSmdsSwSubInvalidHEVerOccur_Type = OctetString
_WfSmdsSwSubInvalidHEVerOccur_Object = MibTableColumn
wfSmdsSwSubInvalidHEVerOccur = _WfSmdsSwSubInvalidHEVerOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 35),
    _WfSmdsSwSubInvalidHEVerOccur_Type()
)
wfSmdsSwSubInvalidHEVerOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInvalidHEVerOccur.setStatus("mandatory")
_WfSmdsSwSubInvalidHECarOccur_Type = OctetString
_WfSmdsSwSubInvalidHECarOccur_Object = MibTableColumn
wfSmdsSwSubInvalidHECarOccur = _WfSmdsSwSubInvalidHECarOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 36),
    _WfSmdsSwSubInvalidHECarOccur_Type()
)
wfSmdsSwSubInvalidHECarOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInvalidHECarOccur.setStatus("mandatory")
_WfSmdsSwSubInvalidHEPadOccur_Type = OctetString
_WfSmdsSwSubInvalidHEPadOccur_Object = MibTableColumn
wfSmdsSwSubInvalidHEPadOccur = _WfSmdsSwSubInvalidHEPadOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 37),
    _WfSmdsSwSubInvalidHEPadOccur_Type()
)
wfSmdsSwSubInvalidHEPadOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInvalidHEPadOccur.setStatus("mandatory")
_WfSmdsSwSubBEtagOccur_Type = OctetString
_WfSmdsSwSubBEtagOccur_Object = MibTableColumn
wfSmdsSwSubBEtagOccur = _WfSmdsSwSubBEtagOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 38),
    _WfSmdsSwSubBEtagOccur_Type()
)
wfSmdsSwSubBEtagOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubBEtagOccur.setStatus("mandatory")
_WfSmdsSwSubBAsizeNELenOccur_Type = OctetString
_WfSmdsSwSubBAsizeNELenOccur_Object = MibTableColumn
wfSmdsSwSubBAsizeNELenOccur = _WfSmdsSwSubBAsizeNELenOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 39),
    _WfSmdsSwSubBAsizeNELenOccur_Type()
)
wfSmdsSwSubBAsizeNELenOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubBAsizeNELenOccur.setStatus("mandatory")
_WfSmdsSwSubIncorrectLenOccur_Type = OctetString
_WfSmdsSwSubIncorrectLenOccur_Object = MibTableColumn
wfSmdsSwSubIncorrectLenOccur = _WfSmdsSwSubIncorrectLenOccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 40),
    _WfSmdsSwSubIncorrectLenOccur_Type()
)
wfSmdsSwSubIncorrectLenOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubIncorrectLenOccur.setStatus("mandatory")
_WfSmdsSwSubExceededMIROccur_Type = OctetString
_WfSmdsSwSubExceededMIROccur_Object = MibTableColumn
wfSmdsSwSubExceededMIROccur = _WfSmdsSwSubExceededMIROccur_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 41),
    _WfSmdsSwSubExceededMIROccur_Type()
)
wfSmdsSwSubExceededMIROccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubExceededMIROccur.setStatus("mandatory")


class _WfSmdsSwSubInBandMgmtDisable_Type(Integer32):
    """Custom type wfSmdsSwSubInBandMgmtDisable based on Integer32"""
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


_WfSmdsSwSubInBandMgmtDisable_Type.__name__ = "Integer32"
_WfSmdsSwSubInBandMgmtDisable_Object = MibTableColumn
wfSmdsSwSubInBandMgmtDisable = _WfSmdsSwSubInBandMgmtDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 42),
    _WfSmdsSwSubInBandMgmtDisable_Type()
)
wfSmdsSwSubInBandMgmtDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubInBandMgmtDisable.setStatus("mandatory")
_WfSmdsSwSubInBandMgmtLocalAddr_Type = OctetString
_WfSmdsSwSubInBandMgmtLocalAddr_Object = MibTableColumn
wfSmdsSwSubInBandMgmtLocalAddr = _WfSmdsSwSubInBandMgmtLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 43),
    _WfSmdsSwSubInBandMgmtLocalAddr_Type()
)
wfSmdsSwSubInBandMgmtLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSubInBandMgmtLocalAddr.setStatus("mandatory")
_WfSmdsSwSubInBandMgmtReceivedPDUs_Type = Counter32
_WfSmdsSwSubInBandMgmtReceivedPDUs_Object = MibTableColumn
wfSmdsSwSubInBandMgmtReceivedPDUs = _WfSmdsSwSubInBandMgmtReceivedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 44),
    _WfSmdsSwSubInBandMgmtReceivedPDUs_Type()
)
wfSmdsSwSubInBandMgmtReceivedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInBandMgmtReceivedPDUs.setStatus("mandatory")
_WfSmdsSwSubInBandMgmtSentPDUs_Type = Counter32
_WfSmdsSwSubInBandMgmtSentPDUs_Object = MibTableColumn
wfSmdsSwSubInBandMgmtSentPDUs = _WfSmdsSwSubInBandMgmtSentPDUs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 45),
    _WfSmdsSwSubInBandMgmtSentPDUs_Type()
)
wfSmdsSwSubInBandMgmtSentPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInBandMgmtSentPDUs.setStatus("mandatory")
_WfSmdsSwSubInBandMgmtMaxLenErrors_Type = Counter32
_WfSmdsSwSubInBandMgmtMaxLenErrors_Object = MibTableColumn
wfSmdsSwSubInBandMgmtMaxLenErrors = _WfSmdsSwSubInBandMgmtMaxLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 46),
    _WfSmdsSwSubInBandMgmtMaxLenErrors_Type()
)
wfSmdsSwSubInBandMgmtMaxLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInBandMgmtMaxLenErrors.setStatus("mandatory")
_WfSmdsSwSubInBandMgmtEncapsErrors_Type = Counter32
_WfSmdsSwSubInBandMgmtEncapsErrors_Object = MibTableColumn
wfSmdsSwSubInBandMgmtEncapsErrors = _WfSmdsSwSubInBandMgmtEncapsErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 47),
    _WfSmdsSwSubInBandMgmtEncapsErrors_Type()
)
wfSmdsSwSubInBandMgmtEncapsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubInBandMgmtEncapsErrors.setStatus("mandatory")
_WfSmdsSwSubGAPartialResolve_Type = Counter32
_WfSmdsSwSubGAPartialResolve_Object = MibTableColumn
wfSmdsSwSubGAPartialResolve = _WfSmdsSwSubGAPartialResolve_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 48),
    _WfSmdsSwSubGAPartialResolve_Type()
)
wfSmdsSwSubGAPartialResolve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubGAPartialResolve.setStatus("mandatory")
_WfSmdsSwSubDANotOnSni_Type = Counter32
_WfSmdsSwSubDANotOnSni_Object = MibTableColumn
wfSmdsSwSubDANotOnSni = _WfSmdsSwSubDANotOnSni_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 1, 1, 49),
    _WfSmdsSwSubDANotOnSni_Type()
)
wfSmdsSwSubDANotOnSni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSubDANotOnSni.setStatus("mandatory")
_WfSmdsSwEndpTable_Object = MibTable
wfSmdsSwEndpTable = _WfSmdsSwEndpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 2)
)
if mibBuilder.loadTexts:
    wfSmdsSwEndpTable.setStatus("mandatory")
_WfSmdsSwEndpEntry_Object = MibTableRow
wfSmdsSwEndpEntry = _WfSmdsSwEndpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 2, 1)
)
wfSmdsSwEndpEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwEndpE164AddrHigh"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwEndpE164AddrDelta"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwEndpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfSmdsSwEndpEntry.setStatus("mandatory")


class _WfSmdsSwEndpDelete_Type(Integer32):
    """Custom type wfSmdsSwEndpDelete based on Integer32"""
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


_WfSmdsSwEndpDelete_Type.__name__ = "Integer32"
_WfSmdsSwEndpDelete_Object = MibTableColumn
wfSmdsSwEndpDelete = _WfSmdsSwEndpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 2, 1, 1),
    _WfSmdsSwEndpDelete_Type()
)
wfSmdsSwEndpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwEndpDelete.setStatus("mandatory")


class _WfSmdsSwEndpE164AddrHigh_Type(OctetString):
    """Custom type wfSmdsSwEndpE164AddrHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwEndpE164AddrHigh_Type.__name__ = "OctetString"
_WfSmdsSwEndpE164AddrHigh_Object = MibTableColumn
wfSmdsSwEndpE164AddrHigh = _WfSmdsSwEndpE164AddrHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 2, 1, 2),
    _WfSmdsSwEndpE164AddrHigh_Type()
)
wfSmdsSwEndpE164AddrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwEndpE164AddrHigh.setStatus("mandatory")


class _WfSmdsSwEndpE164AddrDelta_Type(OctetString):
    """Custom type wfSmdsSwEndpE164AddrDelta based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwEndpE164AddrDelta_Type.__name__ = "OctetString"
_WfSmdsSwEndpE164AddrDelta_Object = MibTableColumn
wfSmdsSwEndpE164AddrDelta = _WfSmdsSwEndpE164AddrDelta_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 2, 1, 3),
    _WfSmdsSwEndpE164AddrDelta_Type()
)
wfSmdsSwEndpE164AddrDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwEndpE164AddrDelta.setStatus("mandatory")
_WfSmdsSwEndpInterfaceIndex_Type = Integer32
_WfSmdsSwEndpInterfaceIndex_Object = MibTableColumn
wfSmdsSwEndpInterfaceIndex = _WfSmdsSwEndpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 2, 1, 4),
    _WfSmdsSwEndpInterfaceIndex_Type()
)
wfSmdsSwEndpInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwEndpInterfaceIndex.setStatus("mandatory")
_WfSmdsSwInterfaceTable_Object = MibTable
wfSmdsSwInterfaceTable = _WfSmdsSwInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3)
)
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceTable.setStatus("mandatory")
_WfSmdsSwInterfaceEntry_Object = MibTableRow
wfSmdsSwInterfaceEntry = _WfSmdsSwInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3, 1)
)
wfSmdsSwInterfaceEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwInterfaceType"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceEntry.setStatus("mandatory")


class _WfSmdsSwInterfaceDelete_Type(Integer32):
    """Custom type wfSmdsSwInterfaceDelete based on Integer32"""
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


_WfSmdsSwInterfaceDelete_Type.__name__ = "Integer32"
_WfSmdsSwInterfaceDelete_Object = MibTableColumn
wfSmdsSwInterfaceDelete = _WfSmdsSwInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3, 1, 1),
    _WfSmdsSwInterfaceDelete_Type()
)
wfSmdsSwInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceDelete.setStatus("mandatory")


class _WfSmdsSwInterfaceType_Type(Integer32):
    """Custom type wfSmdsSwInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sni", 1),
          ("ssi", 2))
    )


_WfSmdsSwInterfaceType_Type.__name__ = "Integer32"
_WfSmdsSwInterfaceType_Object = MibTableColumn
wfSmdsSwInterfaceType = _WfSmdsSwInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3, 1, 2),
    _WfSmdsSwInterfaceType_Type()
)
wfSmdsSwInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceType.setStatus("mandatory")
_WfSmdsSwInterfaceIndex_Type = Integer32
_WfSmdsSwInterfaceIndex_Object = MibTableColumn
wfSmdsSwInterfaceIndex = _WfSmdsSwInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3, 1, 3),
    _WfSmdsSwInterfaceIndex_Type()
)
wfSmdsSwInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceIndex.setStatus("mandatory")
_WfSmdsSwInterfaceIpAddr_Type = IpAddress
_WfSmdsSwInterfaceIpAddr_Object = MibTableColumn
wfSmdsSwInterfaceIpAddr = _WfSmdsSwInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3, 1, 4),
    _WfSmdsSwInterfaceIpAddr_Type()
)
wfSmdsSwInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceIpAddr.setStatus("mandatory")
_WfSmdsSwInterfaceMIR_Type = Integer32
_WfSmdsSwInterfaceMIR_Object = MibTableColumn
wfSmdsSwInterfaceMIR = _WfSmdsSwInterfaceMIR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3, 1, 5),
    _WfSmdsSwInterfaceMIR_Type()
)
wfSmdsSwInterfaceMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceMIR.setStatus("mandatory")
_WfSmdsSwInterfaceCurrentRate_Type = Integer32
_WfSmdsSwInterfaceCurrentRate_Object = MibTableColumn
wfSmdsSwInterfaceCurrentRate = _WfSmdsSwInterfaceCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 3, 1, 6),
    _WfSmdsSwInterfaceCurrentRate_Type()
)
wfSmdsSwInterfaceCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwInterfaceCurrentRate.setStatus("mandatory")
_WfSmdsSwAssocScrnTable_Object = MibTable
wfSmdsSwAssocScrnTable = _WfSmdsSwAssocScrnTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 4)
)
if mibBuilder.loadTexts:
    wfSmdsSwAssocScrnTable.setStatus("mandatory")
_WfSmdsSwAssocScrnEntry_Object = MibTableRow
wfSmdsSwAssocScrnEntry = _WfSmdsSwAssocScrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 4, 1)
)
wfSmdsSwAssocScrnEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwAssocScrnSniIndex"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwAssocScrnAddrInd"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwAssocScrnIndivIndex"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwAssocScrnGrpIndex"),
)
if mibBuilder.loadTexts:
    wfSmdsSwAssocScrnEntry.setStatus("mandatory")


class _WfSmdsSwAssocScrnDelete_Type(Integer32):
    """Custom type wfSmdsSwAssocScrnDelete based on Integer32"""
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


_WfSmdsSwAssocScrnDelete_Type.__name__ = "Integer32"
_WfSmdsSwAssocScrnDelete_Object = MibTableColumn
wfSmdsSwAssocScrnDelete = _WfSmdsSwAssocScrnDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 4, 1, 1),
    _WfSmdsSwAssocScrnDelete_Type()
)
wfSmdsSwAssocScrnDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwAssocScrnDelete.setStatus("mandatory")
_WfSmdsSwAssocScrnSniIndex_Type = Integer32
_WfSmdsSwAssocScrnSniIndex_Object = MibTableColumn
wfSmdsSwAssocScrnSniIndex = _WfSmdsSwAssocScrnSniIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 4, 1, 2),
    _WfSmdsSwAssocScrnSniIndex_Type()
)
wfSmdsSwAssocScrnSniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwAssocScrnSniIndex.setStatus("mandatory")


class _WfSmdsSwAssocScrnAddrInd_Type(OctetString):
    """Custom type wfSmdsSwAssocScrnAddrInd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwAssocScrnAddrInd_Type.__name__ = "OctetString"
_WfSmdsSwAssocScrnAddrInd_Object = MibTableColumn
wfSmdsSwAssocScrnAddrInd = _WfSmdsSwAssocScrnAddrInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 4, 1, 3),
    _WfSmdsSwAssocScrnAddrInd_Type()
)
wfSmdsSwAssocScrnAddrInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwAssocScrnAddrInd.setStatus("mandatory")


class _WfSmdsSwAssocScrnIndivIndex_Type(Integer32):
    """Custom type wfSmdsSwAssocScrnIndivIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfSmdsSwAssocScrnIndivIndex_Type.__name__ = "Integer32"
_WfSmdsSwAssocScrnIndivIndex_Object = MibTableColumn
wfSmdsSwAssocScrnIndivIndex = _WfSmdsSwAssocScrnIndivIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 4, 1, 4),
    _WfSmdsSwAssocScrnIndivIndex_Type()
)
wfSmdsSwAssocScrnIndivIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwAssocScrnIndivIndex.setStatus("mandatory")


class _WfSmdsSwAssocScrnGrpIndex_Type(Integer32):
    """Custom type wfSmdsSwAssocScrnGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfSmdsSwAssocScrnGrpIndex_Type.__name__ = "Integer32"
_WfSmdsSwAssocScrnGrpIndex_Object = MibTableColumn
wfSmdsSwAssocScrnGrpIndex = _WfSmdsSwAssocScrnGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 4, 1, 5),
    _WfSmdsSwAssocScrnGrpIndex_Type()
)
wfSmdsSwAssocScrnGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwAssocScrnGrpIndex.setStatus("mandatory")
_WfSmdsSwIAScrnTable_Object = MibTable
wfSmdsSwIAScrnTable = _WfSmdsSwIAScrnTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 5)
)
if mibBuilder.loadTexts:
    wfSmdsSwIAScrnTable.setStatus("mandatory")
_WfSmdsSwIAScrnEntry_Object = MibTableRow
wfSmdsSwIAScrnEntry = _WfSmdsSwIAScrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 5, 1)
)
wfSmdsSwIAScrnEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwIAScrnSniIndex"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwIAScrnIndex"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwIAScrnAddr"),
)
if mibBuilder.loadTexts:
    wfSmdsSwIAScrnEntry.setStatus("mandatory")


class _WfSmdsSwIAScrnDelete_Type(Integer32):
    """Custom type wfSmdsSwIAScrnDelete based on Integer32"""
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


_WfSmdsSwIAScrnDelete_Type.__name__ = "Integer32"
_WfSmdsSwIAScrnDelete_Object = MibTableColumn
wfSmdsSwIAScrnDelete = _WfSmdsSwIAScrnDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 5, 1, 1),
    _WfSmdsSwIAScrnDelete_Type()
)
wfSmdsSwIAScrnDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwIAScrnDelete.setStatus("mandatory")
_WfSmdsSwIAScrnSniIndex_Type = Integer32
_WfSmdsSwIAScrnSniIndex_Object = MibTableColumn
wfSmdsSwIAScrnSniIndex = _WfSmdsSwIAScrnSniIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 5, 1, 2),
    _WfSmdsSwIAScrnSniIndex_Type()
)
wfSmdsSwIAScrnSniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwIAScrnSniIndex.setStatus("mandatory")


class _WfSmdsSwIAScrnIndex_Type(Integer32):
    """Custom type wfSmdsSwIAScrnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfSmdsSwIAScrnIndex_Type.__name__ = "Integer32"
_WfSmdsSwIAScrnIndex_Object = MibTableColumn
wfSmdsSwIAScrnIndex = _WfSmdsSwIAScrnIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 5, 1, 3),
    _WfSmdsSwIAScrnIndex_Type()
)
wfSmdsSwIAScrnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwIAScrnIndex.setStatus("mandatory")


class _WfSmdsSwIAScrnAddr_Type(OctetString):
    """Custom type wfSmdsSwIAScrnAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwIAScrnAddr_Type.__name__ = "OctetString"
_WfSmdsSwIAScrnAddr_Object = MibTableColumn
wfSmdsSwIAScrnAddr = _WfSmdsSwIAScrnAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 5, 1, 4),
    _WfSmdsSwIAScrnAddr_Type()
)
wfSmdsSwIAScrnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwIAScrnAddr.setStatus("mandatory")
_WfSmdsSwGAScrnTable_Object = MibTable
wfSmdsSwGAScrnTable = _WfSmdsSwGAScrnTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 6)
)
if mibBuilder.loadTexts:
    wfSmdsSwGAScrnTable.setStatus("mandatory")
_WfSmdsSwGAScrnEntry_Object = MibTableRow
wfSmdsSwGAScrnEntry = _WfSmdsSwGAScrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 6, 1)
)
wfSmdsSwGAScrnEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwGAScrnSniIndex"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwGAScrnIndex"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwGAScrnAddr"),
)
if mibBuilder.loadTexts:
    wfSmdsSwGAScrnEntry.setStatus("mandatory")


class _WfSmdsSwGAScrnDelete_Type(Integer32):
    """Custom type wfSmdsSwGAScrnDelete based on Integer32"""
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


_WfSmdsSwGAScrnDelete_Type.__name__ = "Integer32"
_WfSmdsSwGAScrnDelete_Object = MibTableColumn
wfSmdsSwGAScrnDelete = _WfSmdsSwGAScrnDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 6, 1, 1),
    _WfSmdsSwGAScrnDelete_Type()
)
wfSmdsSwGAScrnDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwGAScrnDelete.setStatus("mandatory")
_WfSmdsSwGAScrnSniIndex_Type = Integer32
_WfSmdsSwGAScrnSniIndex_Object = MibTableColumn
wfSmdsSwGAScrnSniIndex = _WfSmdsSwGAScrnSniIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 6, 1, 2),
    _WfSmdsSwGAScrnSniIndex_Type()
)
wfSmdsSwGAScrnSniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwGAScrnSniIndex.setStatus("mandatory")


class _WfSmdsSwGAScrnIndex_Type(Integer32):
    """Custom type wfSmdsSwGAScrnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WfSmdsSwGAScrnIndex_Type.__name__ = "Integer32"
_WfSmdsSwGAScrnIndex_Object = MibTableColumn
wfSmdsSwGAScrnIndex = _WfSmdsSwGAScrnIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 6, 1, 3),
    _WfSmdsSwGAScrnIndex_Type()
)
wfSmdsSwGAScrnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwGAScrnIndex.setStatus("mandatory")


class _WfSmdsSwGAScrnAddr_Type(OctetString):
    """Custom type wfSmdsSwGAScrnAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwGAScrnAddr_Type.__name__ = "OctetString"
_WfSmdsSwGAScrnAddr_Object = MibTableColumn
wfSmdsSwGAScrnAddr = _WfSmdsSwGAScrnAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 6, 1, 4),
    _WfSmdsSwGAScrnAddr_Type()
)
wfSmdsSwGAScrnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwGAScrnAddr.setStatus("mandatory")
_WfSmdsSwGATable_Object = MibTable
wfSmdsSwGATable = _WfSmdsSwGATable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 7)
)
if mibBuilder.loadTexts:
    wfSmdsSwGATable.setStatus("mandatory")
_WfSmdsSwGAEntry_Object = MibTableRow
wfSmdsSwGAEntry = _WfSmdsSwGAEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 7, 1)
)
wfSmdsSwGAEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwGASSI"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwGAGroupAddress"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwGAGroupMember"),
)
if mibBuilder.loadTexts:
    wfSmdsSwGAEntry.setStatus("mandatory")


class _WfSmdsSwGADelete_Type(Integer32):
    """Custom type wfSmdsSwGADelete based on Integer32"""
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


_WfSmdsSwGADelete_Type.__name__ = "Integer32"
_WfSmdsSwGADelete_Object = MibTableColumn
wfSmdsSwGADelete = _WfSmdsSwGADelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 7, 1, 1),
    _WfSmdsSwGADelete_Type()
)
wfSmdsSwGADelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwGADelete.setStatus("mandatory")
_WfSmdsSwGASSI_Type = Integer32
_WfSmdsSwGASSI_Object = MibTableColumn
wfSmdsSwGASSI = _WfSmdsSwGASSI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 7, 1, 2),
    _WfSmdsSwGASSI_Type()
)
wfSmdsSwGASSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwGASSI.setStatus("mandatory")


class _WfSmdsSwGAGroupAddress_Type(OctetString):
    """Custom type wfSmdsSwGAGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwGAGroupAddress_Type.__name__ = "OctetString"
_WfSmdsSwGAGroupAddress_Object = MibTableColumn
wfSmdsSwGAGroupAddress = _WfSmdsSwGAGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 7, 1, 3),
    _WfSmdsSwGAGroupAddress_Type()
)
wfSmdsSwGAGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwGAGroupAddress.setStatus("mandatory")


class _WfSmdsSwGAGroupMember_Type(OctetString):
    """Custom type wfSmdsSwGAGroupMember based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwGAGroupMember_Type.__name__ = "OctetString"
_WfSmdsSwGAGroupMember_Object = MibTableColumn
wfSmdsSwGAGroupMember = _WfSmdsSwGAGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 7, 1, 4),
    _WfSmdsSwGAGroupMember_Type()
)
wfSmdsSwGAGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwGAGroupMember.setStatus("mandatory")
_WfSmdsSwCurUsageTable_Object = MibTable
wfSmdsSwCurUsageTable = _WfSmdsSwCurUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8)
)
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageTable.setStatus("mandatory")
_WfSmdsSwCurUsageEntry_Object = MibTableRow
wfSmdsSwCurUsageEntry = _WfSmdsSwCurUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1)
)
wfSmdsSwCurUsageEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwCurUsageSni"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwCurUsageDestAddr"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwCurUsageSrcAddr"),
)
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageEntry.setStatus("mandatory")


class _WfSmdsSwCurUsageDelete_Type(Integer32):
    """Custom type wfSmdsSwCurUsageDelete based on Integer32"""
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


_WfSmdsSwCurUsageDelete_Type.__name__ = "Integer32"
_WfSmdsSwCurUsageDelete_Object = MibTableColumn
wfSmdsSwCurUsageDelete = _WfSmdsSwCurUsageDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 1),
    _WfSmdsSwCurUsageDelete_Type()
)
wfSmdsSwCurUsageDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageDelete.setStatus("obsolete")


class _WfSmdsSwCurUsageSni_Type(Integer32):
    """Custom type wfSmdsSwCurUsageSni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfSmdsSwCurUsageSni_Type.__name__ = "Integer32"
_WfSmdsSwCurUsageSni_Object = MibTableColumn
wfSmdsSwCurUsageSni = _WfSmdsSwCurUsageSni_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 2),
    _WfSmdsSwCurUsageSni_Type()
)
wfSmdsSwCurUsageSni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageSni.setStatus("mandatory")


class _WfSmdsSwCurUsageDestAddr_Type(OctetString):
    """Custom type wfSmdsSwCurUsageDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwCurUsageDestAddr_Type.__name__ = "OctetString"
_WfSmdsSwCurUsageDestAddr_Object = MibTableColumn
wfSmdsSwCurUsageDestAddr = _WfSmdsSwCurUsageDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 3),
    _WfSmdsSwCurUsageDestAddr_Type()
)
wfSmdsSwCurUsageDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageDestAddr.setStatus("mandatory")


class _WfSmdsSwCurUsageSrcAddr_Type(OctetString):
    """Custom type wfSmdsSwCurUsageSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwCurUsageSrcAddr_Type.__name__ = "OctetString"
_WfSmdsSwCurUsageSrcAddr_Object = MibTableColumn
wfSmdsSwCurUsageSrcAddr = _WfSmdsSwCurUsageSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 4),
    _WfSmdsSwCurUsageSrcAddr_Type()
)
wfSmdsSwCurUsageSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageSrcAddr.setStatus("mandatory")
_WfSmdsSwCurUsageGrpIndAddr_Type = OctetString
_WfSmdsSwCurUsageGrpIndAddr_Object = MibTableColumn
wfSmdsSwCurUsageGrpIndAddr = _WfSmdsSwCurUsageGrpIndAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 5),
    _WfSmdsSwCurUsageGrpIndAddr_Type()
)
wfSmdsSwCurUsageGrpIndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageGrpIndAddr.setStatus("mandatory")
_WfSmdsSwCurUsageNumL3Pdu_Type = Counter32
_WfSmdsSwCurUsageNumL3Pdu_Object = MibTableColumn
wfSmdsSwCurUsageNumL3Pdu = _WfSmdsSwCurUsageNumL3Pdu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 6),
    _WfSmdsSwCurUsageNumL3Pdu_Type()
)
wfSmdsSwCurUsageNumL3Pdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageNumL3Pdu.setStatus("mandatory")
_WfSmdsSwCurUsageNumOctet_Type = Counter32
_WfSmdsSwCurUsageNumOctet_Object = MibTableColumn
wfSmdsSwCurUsageNumOctet = _WfSmdsSwCurUsageNumOctet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 7),
    _WfSmdsSwCurUsageNumOctet_Type()
)
wfSmdsSwCurUsageNumOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageNumOctet.setStatus("mandatory")


class _WfSmdsSwCurUsageToBeDeleted_Type(Integer32):
    """Custom type wfSmdsSwCurUsageToBeDeleted based on Integer32"""
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


_WfSmdsSwCurUsageToBeDeleted_Type.__name__ = "Integer32"
_WfSmdsSwCurUsageToBeDeleted_Object = MibTableColumn
wfSmdsSwCurUsageToBeDeleted = _WfSmdsSwCurUsageToBeDeleted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 8, 1, 8),
    _WfSmdsSwCurUsageToBeDeleted_Type()
)
wfSmdsSwCurUsageToBeDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwCurUsageToBeDeleted.setStatus("mandatory")
_WfSmdsSwUsage_ObjectIdentity = ObjectIdentity
wfSmdsSwUsage = _WfSmdsSwUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9)
)


class _WfSmdsSwUsageEnable_Type(Integer32):
    """Custom type wfSmdsSwUsageEnable based on Integer32"""
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


_WfSmdsSwUsageEnable_Type.__name__ = "Integer32"
_WfSmdsSwUsageEnable_Object = MibScalar
wfSmdsSwUsageEnable = _WfSmdsSwUsageEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 1),
    _WfSmdsSwUsageEnable_Type()
)
wfSmdsSwUsageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageEnable.setStatus("mandatory")


class _WfSmdsSwUsageVolume_Type(Integer32):
    """Custom type wfSmdsSwUsageVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfSmdsSwUsageVolume_Type.__name__ = "Integer32"
_WfSmdsSwUsageVolume_Object = MibScalar
wfSmdsSwUsageVolume = _WfSmdsSwUsageVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 2),
    _WfSmdsSwUsageVolume_Type()
)
wfSmdsSwUsageVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageVolume.setStatus("mandatory")


class _WfSmdsSwUsageVolumeBackup_Type(Integer32):
    """Custom type wfSmdsSwUsageVolumeBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfSmdsSwUsageVolumeBackup_Type.__name__ = "Integer32"
_WfSmdsSwUsageVolumeBackup_Object = MibScalar
wfSmdsSwUsageVolumeBackup = _WfSmdsSwUsageVolumeBackup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 3),
    _WfSmdsSwUsageVolumeBackup_Type()
)
wfSmdsSwUsageVolumeBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageVolumeBackup.setStatus("mandatory")
_WfSmdsSwUsageDirectory_Type = DisplayString
_WfSmdsSwUsageDirectory_Object = MibScalar
wfSmdsSwUsageDirectory = _WfSmdsSwUsageDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 4),
    _WfSmdsSwUsageDirectory_Type()
)
wfSmdsSwUsageDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageDirectory.setStatus("mandatory")
_WfSmdsSwUsageFilePrefix_Type = DisplayString
_WfSmdsSwUsageFilePrefix_Object = MibScalar
wfSmdsSwUsageFilePrefix = _WfSmdsSwUsageFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 5),
    _WfSmdsSwUsageFilePrefix_Type()
)
wfSmdsSwUsageFilePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageFilePrefix.setStatus("mandatory")


class _WfSmdsSwUsageTimerInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageTimerInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfSmdsSwUsageTimerInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageTimerInterval_Object = MibScalar
wfSmdsSwUsageTimerInterval = _WfSmdsSwUsageTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 6),
    _WfSmdsSwUsageTimerInterval_Type()
)
wfSmdsSwUsageTimerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageTimerInterval.setStatus("mandatory")


class _WfSmdsSwUsageUpdateInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageUpdateInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageUpdateInterval_Object = MibScalar
wfSmdsSwUsageUpdateInterval = _WfSmdsSwUsageUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 7),
    _WfSmdsSwUsageUpdateInterval_Type()
)
wfSmdsSwUsageUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageUpdateInterval.setStatus("mandatory")


class _WfSmdsSwUsageStoreInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageStoreInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageStoreInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageStoreInterval_Object = MibScalar
wfSmdsSwUsageStoreInterval = _WfSmdsSwUsageStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 8),
    _WfSmdsSwUsageStoreInterval_Type()
)
wfSmdsSwUsageStoreInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageStoreInterval.setStatus("mandatory")


class _WfSmdsSwUsageFlushInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageFlushInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageFlushInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageFlushInterval_Object = MibScalar
wfSmdsSwUsageFlushInterval = _WfSmdsSwUsageFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 9),
    _WfSmdsSwUsageFlushInterval_Type()
)
wfSmdsSwUsageFlushInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageFlushInterval.setStatus("mandatory")


class _WfSmdsSwUsageCleanupInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageCleanupInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageCleanupInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageCleanupInterval_Object = MibScalar
wfSmdsSwUsageCleanupInterval = _WfSmdsSwUsageCleanupInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 10),
    _WfSmdsSwUsageCleanupInterval_Type()
)
wfSmdsSwUsageCleanupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCleanupInterval.setStatus("mandatory")
_WfSmdsSwUsageLocalTimeZone_Type = Integer32
_WfSmdsSwUsageLocalTimeZone_Object = MibScalar
wfSmdsSwUsageLocalTimeZone = _WfSmdsSwUsageLocalTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 11),
    _WfSmdsSwUsageLocalTimeZone_Type()
)
wfSmdsSwUsageLocalTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageLocalTimeZone.setStatus("mandatory")
_WfSmdsSwUsageUpdateTimeStamp_Type = TimeTicks
_WfSmdsSwUsageUpdateTimeStamp_Object = MibScalar
wfSmdsSwUsageUpdateTimeStamp = _WfSmdsSwUsageUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 12),
    _WfSmdsSwUsageUpdateTimeStamp_Type()
)
wfSmdsSwUsageUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageUpdateTimeStamp.setStatus("mandatory")
_WfSmdsSwUsageStoreTimeStamp_Type = TimeTicks
_WfSmdsSwUsageStoreTimeStamp_Object = MibScalar
wfSmdsSwUsageStoreTimeStamp = _WfSmdsSwUsageStoreTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 13),
    _WfSmdsSwUsageStoreTimeStamp_Type()
)
wfSmdsSwUsageStoreTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageStoreTimeStamp.setStatus("mandatory")
_WfSmdsSwUsageFlushTimeStamp_Type = TimeTicks
_WfSmdsSwUsageFlushTimeStamp_Object = MibScalar
wfSmdsSwUsageFlushTimeStamp = _WfSmdsSwUsageFlushTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 14),
    _WfSmdsSwUsageFlushTimeStamp_Type()
)
wfSmdsSwUsageFlushTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageFlushTimeStamp.setStatus("mandatory")
_WfSmdsSwUsageCleanupTimeStamp_Type = TimeTicks
_WfSmdsSwUsageCleanupTimeStamp_Object = MibScalar
wfSmdsSwUsageCleanupTimeStamp = _WfSmdsSwUsageCleanupTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 15),
    _WfSmdsSwUsageCleanupTimeStamp_Type()
)
wfSmdsSwUsageCleanupTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCleanupTimeStamp.setStatus("mandatory")
_WfSmdsSwUsageUpdateData_Type = Integer32
_WfSmdsSwUsageUpdateData_Object = MibScalar
wfSmdsSwUsageUpdateData = _WfSmdsSwUsageUpdateData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 16),
    _WfSmdsSwUsageUpdateData_Type()
)
wfSmdsSwUsageUpdateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageUpdateData.setStatus("mandatory")
_WfSmdsSwUsageStoreData_Type = Integer32
_WfSmdsSwUsageStoreData_Object = MibScalar
wfSmdsSwUsageStoreData = _WfSmdsSwUsageStoreData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 17),
    _WfSmdsSwUsageStoreData_Type()
)
wfSmdsSwUsageStoreData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageStoreData.setStatus("mandatory")
_WfSmdsSwUsageFlushData_Type = Integer32
_WfSmdsSwUsageFlushData_Object = MibScalar
wfSmdsSwUsageFlushData = _WfSmdsSwUsageFlushData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 18),
    _WfSmdsSwUsageFlushData_Type()
)
wfSmdsSwUsageFlushData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageFlushData.setStatus("mandatory")
_WfSmdsSwUsageFileCleanup_Type = Integer32
_WfSmdsSwUsageFileCleanup_Object = MibScalar
wfSmdsSwUsageFileCleanup = _WfSmdsSwUsageFileCleanup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 19),
    _WfSmdsSwUsageFileCleanup_Type()
)
wfSmdsSwUsageFileCleanup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageFileCleanup.setStatus("mandatory")


class _WfSmdsSwUsageState_Type(Integer32):
    """Custom type wfSmdsSwUsageState based on Integer32"""
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


_WfSmdsSwUsageState_Type.__name__ = "Integer32"
_WfSmdsSwUsageState_Object = MibScalar
wfSmdsSwUsageState = _WfSmdsSwUsageState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 20),
    _WfSmdsSwUsageState_Type()
)
wfSmdsSwUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageState.setStatus("mandatory")


class _WfSmdsSwUsageCurVolume_Type(Integer32):
    """Custom type wfSmdsSwUsageCurVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfSmdsSwUsageCurVolume_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurVolume_Object = MibScalar
wfSmdsSwUsageCurVolume = _WfSmdsSwUsageCurVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 21),
    _WfSmdsSwUsageCurVolume_Type()
)
wfSmdsSwUsageCurVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurVolume.setStatus("mandatory")


class _WfSmdsSwUsageCurVolumeBackup_Type(Integer32):
    """Custom type wfSmdsSwUsageCurVolumeBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfSmdsSwUsageCurVolumeBackup_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurVolumeBackup_Object = MibScalar
wfSmdsSwUsageCurVolumeBackup = _WfSmdsSwUsageCurVolumeBackup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 22),
    _WfSmdsSwUsageCurVolumeBackup_Type()
)
wfSmdsSwUsageCurVolumeBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurVolumeBackup.setStatus("mandatory")
_WfSmdsSwUsageCurDirectory_Type = DisplayString
_WfSmdsSwUsageCurDirectory_Object = MibScalar
wfSmdsSwUsageCurDirectory = _WfSmdsSwUsageCurDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 23),
    _WfSmdsSwUsageCurDirectory_Type()
)
wfSmdsSwUsageCurDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurDirectory.setStatus("mandatory")
_WfSmdsSwUsageCurFilePrefix_Type = DisplayString
_WfSmdsSwUsageCurFilePrefix_Object = MibScalar
wfSmdsSwUsageCurFilePrefix = _WfSmdsSwUsageCurFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 24),
    _WfSmdsSwUsageCurFilePrefix_Type()
)
wfSmdsSwUsageCurFilePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurFilePrefix.setStatus("mandatory")


class _WfSmdsSwUsageCurTimerInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageCurTimerInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfSmdsSwUsageCurTimerInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurTimerInterval_Object = MibScalar
wfSmdsSwUsageCurTimerInterval = _WfSmdsSwUsageCurTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 25),
    _WfSmdsSwUsageCurTimerInterval_Type()
)
wfSmdsSwUsageCurTimerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurTimerInterval.setStatus("mandatory")


class _WfSmdsSwUsageCurUpdateInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageCurUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageCurUpdateInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurUpdateInterval_Object = MibScalar
wfSmdsSwUsageCurUpdateInterval = _WfSmdsSwUsageCurUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 26),
    _WfSmdsSwUsageCurUpdateInterval_Type()
)
wfSmdsSwUsageCurUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurUpdateInterval.setStatus("mandatory")


class _WfSmdsSwUsageCurStoreInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageCurStoreInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageCurStoreInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurStoreInterval_Object = MibScalar
wfSmdsSwUsageCurStoreInterval = _WfSmdsSwUsageCurStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 27),
    _WfSmdsSwUsageCurStoreInterval_Type()
)
wfSmdsSwUsageCurStoreInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurStoreInterval.setStatus("mandatory")


class _WfSmdsSwUsageCurFlushInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageCurFlushInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageCurFlushInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurFlushInterval_Object = MibScalar
wfSmdsSwUsageCurFlushInterval = _WfSmdsSwUsageCurFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 28),
    _WfSmdsSwUsageCurFlushInterval_Type()
)
wfSmdsSwUsageCurFlushInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurFlushInterval.setStatus("mandatory")


class _WfSmdsSwUsageCurCleanupInterval_Type(Integer32):
    """Custom type wfSmdsSwUsageCurCleanupInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsSwUsageCurCleanupInterval_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurCleanupInterval_Object = MibScalar
wfSmdsSwUsageCurCleanupInterval = _WfSmdsSwUsageCurCleanupInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 29),
    _WfSmdsSwUsageCurCleanupInterval_Type()
)
wfSmdsSwUsageCurCleanupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurCleanupInterval.setStatus("mandatory")


class _WfSmdsSwUsageDebug_Type(Integer32):
    """Custom type wfSmdsSwUsageDebug based on Integer32"""
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


_WfSmdsSwUsageDebug_Type.__name__ = "Integer32"
_WfSmdsSwUsageDebug_Object = MibScalar
wfSmdsSwUsageDebug = _WfSmdsSwUsageDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 30),
    _WfSmdsSwUsageDebug_Type()
)
wfSmdsSwUsageDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwUsageDebug.setStatus("mandatory")


class _WfSmdsSwUsageCurDebug_Type(Integer32):
    """Custom type wfSmdsSwUsageCurDebug based on Integer32"""
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


_WfSmdsSwUsageCurDebug_Type.__name__ = "Integer32"
_WfSmdsSwUsageCurDebug_Object = MibScalar
wfSmdsSwUsageCurDebug = _WfSmdsSwUsageCurDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 31),
    _WfSmdsSwUsageCurDebug_Type()
)
wfSmdsSwUsageCurDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageCurDebug.setStatus("mandatory")
_WfSmdsSwUsageSwitchId_Type = Integer32
_WfSmdsSwUsageSwitchId_Object = MibScalar
wfSmdsSwUsageSwitchId = _WfSmdsSwUsageSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 32),
    _WfSmdsSwUsageSwitchId_Type()
)
wfSmdsSwUsageSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageSwitchId.setStatus("mandatory")
_WfSmdsSwUsageNumEntries_Type = Integer32
_WfSmdsSwUsageNumEntries_Object = MibScalar
wfSmdsSwUsageNumEntries = _WfSmdsSwUsageNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 9, 33),
    _WfSmdsSwUsageNumEntries_Type()
)
wfSmdsSwUsageNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageNumEntries.setStatus("mandatory")
_WfSmdsSwUsageTable_Object = MibTable
wfSmdsSwUsageTable = _WfSmdsSwUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10)
)
if mibBuilder.loadTexts:
    wfSmdsSwUsageTable.setStatus("mandatory")
_WfSmdsSwUsageEntry_Object = MibTableRow
wfSmdsSwUsageEntry = _WfSmdsSwUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1)
)
wfSmdsSwUsageEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwUsageSni"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwUsageDestAddr"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwUsageSrcAddr"),
)
if mibBuilder.loadTexts:
    wfSmdsSwUsageEntry.setStatus("mandatory")


class _WfSmdsSwUsageDelete_Type(Integer32):
    """Custom type wfSmdsSwUsageDelete based on Integer32"""
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


_WfSmdsSwUsageDelete_Type.__name__ = "Integer32"
_WfSmdsSwUsageDelete_Object = MibTableColumn
wfSmdsSwUsageDelete = _WfSmdsSwUsageDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 1),
    _WfSmdsSwUsageDelete_Type()
)
wfSmdsSwUsageDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageDelete.setStatus("mandatory")
_WfSmdsSwUsageSni_Type = Integer32
_WfSmdsSwUsageSni_Object = MibTableColumn
wfSmdsSwUsageSni = _WfSmdsSwUsageSni_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 2),
    _WfSmdsSwUsageSni_Type()
)
wfSmdsSwUsageSni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageSni.setStatus("mandatory")


class _WfSmdsSwUsageDestAddr_Type(OctetString):
    """Custom type wfSmdsSwUsageDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwUsageDestAddr_Type.__name__ = "OctetString"
_WfSmdsSwUsageDestAddr_Object = MibTableColumn
wfSmdsSwUsageDestAddr = _WfSmdsSwUsageDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 3),
    _WfSmdsSwUsageDestAddr_Type()
)
wfSmdsSwUsageDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageDestAddr.setStatus("mandatory")


class _WfSmdsSwUsageSrcAddr_Type(OctetString):
    """Custom type wfSmdsSwUsageSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfSmdsSwUsageSrcAddr_Type.__name__ = "OctetString"
_WfSmdsSwUsageSrcAddr_Object = MibTableColumn
wfSmdsSwUsageSrcAddr = _WfSmdsSwUsageSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 4),
    _WfSmdsSwUsageSrcAddr_Type()
)
wfSmdsSwUsageSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageSrcAddr.setStatus("mandatory")
_WfSmdsSwUsageStartTimeStampHigh_Type = Integer32
_WfSmdsSwUsageStartTimeStampHigh_Object = MibTableColumn
wfSmdsSwUsageStartTimeStampHigh = _WfSmdsSwUsageStartTimeStampHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 5),
    _WfSmdsSwUsageStartTimeStampHigh_Type()
)
wfSmdsSwUsageStartTimeStampHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageStartTimeStampHigh.setStatus("mandatory")
_WfSmdsSwUsageStartTimeStampLow_Type = Integer32
_WfSmdsSwUsageStartTimeStampLow_Object = MibTableColumn
wfSmdsSwUsageStartTimeStampLow = _WfSmdsSwUsageStartTimeStampLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 6),
    _WfSmdsSwUsageStartTimeStampLow_Type()
)
wfSmdsSwUsageStartTimeStampLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageStartTimeStampLow.setStatus("mandatory")
_WfSmdsSwUsageEndTimeStampHigh_Type = Integer32
_WfSmdsSwUsageEndTimeStampHigh_Object = MibTableColumn
wfSmdsSwUsageEndTimeStampHigh = _WfSmdsSwUsageEndTimeStampHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 7),
    _WfSmdsSwUsageEndTimeStampHigh_Type()
)
wfSmdsSwUsageEndTimeStampHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageEndTimeStampHigh.setStatus("mandatory")
_WfSmdsSwUsageEndTimeStampLow_Type = Integer32
_WfSmdsSwUsageEndTimeStampLow_Object = MibTableColumn
wfSmdsSwUsageEndTimeStampLow = _WfSmdsSwUsageEndTimeStampLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 8),
    _WfSmdsSwUsageEndTimeStampLow_Type()
)
wfSmdsSwUsageEndTimeStampLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageEndTimeStampLow.setStatus("mandatory")
_WfSmdsSwUsageSentL3PduHigh_Type = Integer32
_WfSmdsSwUsageSentL3PduHigh_Object = MibTableColumn
wfSmdsSwUsageSentL3PduHigh = _WfSmdsSwUsageSentL3PduHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 9),
    _WfSmdsSwUsageSentL3PduHigh_Type()
)
wfSmdsSwUsageSentL3PduHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageSentL3PduHigh.setStatus("mandatory")
_WfSmdsSwUsageSentL3PduLow_Type = Integer32
_WfSmdsSwUsageSentL3PduLow_Object = MibTableColumn
wfSmdsSwUsageSentL3PduLow = _WfSmdsSwUsageSentL3PduLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 10),
    _WfSmdsSwUsageSentL3PduLow_Type()
)
wfSmdsSwUsageSentL3PduLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageSentL3PduLow.setStatus("mandatory")
_WfSmdsSwUsageSentOctetHigh_Type = Integer32
_WfSmdsSwUsageSentOctetHigh_Object = MibTableColumn
wfSmdsSwUsageSentOctetHigh = _WfSmdsSwUsageSentOctetHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 11),
    _WfSmdsSwUsageSentOctetHigh_Type()
)
wfSmdsSwUsageSentOctetHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageSentOctetHigh.setStatus("mandatory")
_WfSmdsSwUsageSentOctetLow_Type = Integer32
_WfSmdsSwUsageSentOctetLow_Object = MibTableColumn
wfSmdsSwUsageSentOctetLow = _WfSmdsSwUsageSentOctetLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 12),
    _WfSmdsSwUsageSentOctetLow_Type()
)
wfSmdsSwUsageSentOctetLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageSentOctetLow.setStatus("mandatory")
_WfSmdsSwUsageLastL3PduHigh_Type = Integer32
_WfSmdsSwUsageLastL3PduHigh_Object = MibTableColumn
wfSmdsSwUsageLastL3PduHigh = _WfSmdsSwUsageLastL3PduHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 13),
    _WfSmdsSwUsageLastL3PduHigh_Type()
)
wfSmdsSwUsageLastL3PduHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageLastL3PduHigh.setStatus("mandatory")
_WfSmdsSwUsageLastL3PduLow_Type = Integer32
_WfSmdsSwUsageLastL3PduLow_Object = MibTableColumn
wfSmdsSwUsageLastL3PduLow = _WfSmdsSwUsageLastL3PduLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 14),
    _WfSmdsSwUsageLastL3PduLow_Type()
)
wfSmdsSwUsageLastL3PduLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageLastL3PduLow.setStatus("mandatory")
_WfSmdsSwUsageLastOctetHigh_Type = Integer32
_WfSmdsSwUsageLastOctetHigh_Object = MibTableColumn
wfSmdsSwUsageLastOctetHigh = _WfSmdsSwUsageLastOctetHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 15),
    _WfSmdsSwUsageLastOctetHigh_Type()
)
wfSmdsSwUsageLastOctetHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageLastOctetHigh.setStatus("mandatory")
_WfSmdsSwUsageLastOctetLow_Type = Integer32
_WfSmdsSwUsageLastOctetLow_Object = MibTableColumn
wfSmdsSwUsageLastOctetLow = _WfSmdsSwUsageLastOctetLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 16),
    _WfSmdsSwUsageLastOctetLow_Type()
)
wfSmdsSwUsageLastOctetLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageLastOctetLow.setStatus("mandatory")
_WfSmdsSwUsageGrpIndAddr_Type = OctetString
_WfSmdsSwUsageGrpIndAddr_Object = MibTableColumn
wfSmdsSwUsageGrpIndAddr = _WfSmdsSwUsageGrpIndAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 10, 1, 17),
    _WfSmdsSwUsageGrpIndAddr_Type()
)
wfSmdsSwUsageGrpIndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwUsageGrpIndAddr.setStatus("mandatory")
_WfSmdsSwSsiSniTable_Object = MibTable
wfSmdsSwSsiSniTable = _WfSmdsSwSsiSniTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 11)
)
if mibBuilder.loadTexts:
    wfSmdsSwSsiSniTable.setStatus("mandatory")
_WfSmdsSwSsiSniEntry_Object = MibTableRow
wfSmdsSwSsiSniEntry = _WfSmdsSwSsiSniEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 11, 1)
)
wfSmdsSwSsiSniEntry.setIndexNames(
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwSsiSniSSI"),
    (0, "Wellfleet-SWSMDS-MIB", "wfSmdsSwSsiSniSNI"),
)
if mibBuilder.loadTexts:
    wfSmdsSwSsiSniEntry.setStatus("mandatory")


class _WfSmdsSwSsiSniDelete_Type(Integer32):
    """Custom type wfSmdsSwSsiSniDelete based on Integer32"""
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


_WfSmdsSwSsiSniDelete_Type.__name__ = "Integer32"
_WfSmdsSwSsiSniDelete_Object = MibTableColumn
wfSmdsSwSsiSniDelete = _WfSmdsSwSsiSniDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 11, 1, 1),
    _WfSmdsSwSsiSniDelete_Type()
)
wfSmdsSwSsiSniDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsSwSsiSniDelete.setStatus("mandatory")
_WfSmdsSwSsiSniSSI_Type = Integer32
_WfSmdsSwSsiSniSSI_Object = MibTableColumn
wfSmdsSwSsiSniSSI = _WfSmdsSwSsiSniSSI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 11, 1, 2),
    _WfSmdsSwSsiSniSSI_Type()
)
wfSmdsSwSsiSniSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSsiSniSSI.setStatus("mandatory")
_WfSmdsSwSsiSniSNI_Type = Integer32
_WfSmdsSwSsiSniSNI_Object = MibTableColumn
wfSmdsSwSsiSniSNI = _WfSmdsSwSsiSniSNI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7, 11, 1, 3),
    _WfSmdsSwSsiSniSNI_Type()
)
wfSmdsSwSsiSniSNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsSwSsiSniSNI.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SWSMDS-MIB",
    **{"wfSmdsSwSubTable": wfSmdsSwSubTable,
       "wfSmdsSwSubEntry": wfSmdsSwSubEntry,
       "wfSmdsSwSubDelete": wfSmdsSwSubDelete,
       "wfSmdsSwSubDisable": wfSmdsSwSubDisable,
       "wfSmdsSwSubState": wfSmdsSwSubState,
       "wfSmdsSwSubCct": wfSmdsSwSubCct,
       "wfSmdsSwSubDisableHrtbtPoll": wfSmdsSwSubDisableHrtbtPoll,
       "wfSmdsSwSubHrtbtPollAddr": wfSmdsSwSubHrtbtPollAddr,
       "wfSmdsSwSubHrtbtPollInterval": wfSmdsSwSubHrtbtPollInterval,
       "wfSmdsSwSubHrtbtPollDownCount": wfSmdsSwSubHrtbtPollDownCount,
       "wfSmdsSwSubDisableNetMgmt": wfSmdsSwSubDisableNetMgmt,
       "wfSmdsSwSubInterfaceType": wfSmdsSwSubInterfaceType,
       "wfSmdsSwSubInterfaceIndex": wfSmdsSwSubInterfaceIndex,
       "wfSmdsSwSubDisableL3PduChecks": wfSmdsSwSubDisableL3PduChecks,
       "wfSmdsSwSubDisableUsageGeneration": wfSmdsSwSubDisableUsageGeneration,
       "wfSmdsSwSubDisableMIR": wfSmdsSwSubDisableMIR,
       "wfSmdsSwSubUnassignedSAs": wfSmdsSwSubUnassignedSAs,
       "wfSmdsSwSubSAScreenViolations": wfSmdsSwSubSAScreenViolations,
       "wfSmdsSwSubDAScreenViolations": wfSmdsSwSubDAScreenViolations,
       "wfSmdsSwSubNumPDUExceededMIR": wfSmdsSwSubNumPDUExceededMIR,
       "wfSmdsSwSubSipL3ReceivedIAs": wfSmdsSwSubSipL3ReceivedIAs,
       "wfSmdsSwSubSipL3ReceivedGAs": wfSmdsSwSubSipL3ReceivedGAs,
       "wfSmdsSwSubSipL3UnrecIAs": wfSmdsSwSubSipL3UnrecIAs,
       "wfSmdsSwSubSipL3UnrecGAs": wfSmdsSwSubSipL3UnrecGAs,
       "wfSmdsSwSubSipL3SentIAs": wfSmdsSwSubSipL3SentIAs,
       "wfSmdsSwSubSipL3SentGAs": wfSmdsSwSubSipL3SentGAs,
       "wfSmdsSwSubSipL3Errors": wfSmdsSwSubSipL3Errors,
       "wfSmdsSwSubSipL3InvAddrTypes": wfSmdsSwSubSipL3InvAddrTypes,
       "wfSmdsSwSubSipL3VersionSupport": wfSmdsSwSubSipL3VersionSupport,
       "wfSmdsSwSubSAScrnViolationOccur": wfSmdsSwSubSAScrnViolationOccur,
       "wfSmdsSwSubDAScrnViolationOccur": wfSmdsSwSubDAScrnViolationOccur,
       "wfSmdsSwSubUnassignedSAOccur": wfSmdsSwSubUnassignedSAOccur,
       "wfSmdsSwSubSAErrorOccur": wfSmdsSwSubSAErrorOccur,
       "wfSmdsSwSubDAErrorOccur": wfSmdsSwSubDAErrorOccur,
       "wfSmdsSwSubInvalidBASizeOccur": wfSmdsSwSubInvalidBASizeOccur,
       "wfSmdsSwSubInvalidHELenOccur": wfSmdsSwSubInvalidHELenOccur,
       "wfSmdsSwSubInvalidHEVerOccur": wfSmdsSwSubInvalidHEVerOccur,
       "wfSmdsSwSubInvalidHECarOccur": wfSmdsSwSubInvalidHECarOccur,
       "wfSmdsSwSubInvalidHEPadOccur": wfSmdsSwSubInvalidHEPadOccur,
       "wfSmdsSwSubBEtagOccur": wfSmdsSwSubBEtagOccur,
       "wfSmdsSwSubBAsizeNELenOccur": wfSmdsSwSubBAsizeNELenOccur,
       "wfSmdsSwSubIncorrectLenOccur": wfSmdsSwSubIncorrectLenOccur,
       "wfSmdsSwSubExceededMIROccur": wfSmdsSwSubExceededMIROccur,
       "wfSmdsSwSubInBandMgmtDisable": wfSmdsSwSubInBandMgmtDisable,
       "wfSmdsSwSubInBandMgmtLocalAddr": wfSmdsSwSubInBandMgmtLocalAddr,
       "wfSmdsSwSubInBandMgmtReceivedPDUs": wfSmdsSwSubInBandMgmtReceivedPDUs,
       "wfSmdsSwSubInBandMgmtSentPDUs": wfSmdsSwSubInBandMgmtSentPDUs,
       "wfSmdsSwSubInBandMgmtMaxLenErrors": wfSmdsSwSubInBandMgmtMaxLenErrors,
       "wfSmdsSwSubInBandMgmtEncapsErrors": wfSmdsSwSubInBandMgmtEncapsErrors,
       "wfSmdsSwSubGAPartialResolve": wfSmdsSwSubGAPartialResolve,
       "wfSmdsSwSubDANotOnSni": wfSmdsSwSubDANotOnSni,
       "wfSmdsSwEndpTable": wfSmdsSwEndpTable,
       "wfSmdsSwEndpEntry": wfSmdsSwEndpEntry,
       "wfSmdsSwEndpDelete": wfSmdsSwEndpDelete,
       "wfSmdsSwEndpE164AddrHigh": wfSmdsSwEndpE164AddrHigh,
       "wfSmdsSwEndpE164AddrDelta": wfSmdsSwEndpE164AddrDelta,
       "wfSmdsSwEndpInterfaceIndex": wfSmdsSwEndpInterfaceIndex,
       "wfSmdsSwInterfaceTable": wfSmdsSwInterfaceTable,
       "wfSmdsSwInterfaceEntry": wfSmdsSwInterfaceEntry,
       "wfSmdsSwInterfaceDelete": wfSmdsSwInterfaceDelete,
       "wfSmdsSwInterfaceType": wfSmdsSwInterfaceType,
       "wfSmdsSwInterfaceIndex": wfSmdsSwInterfaceIndex,
       "wfSmdsSwInterfaceIpAddr": wfSmdsSwInterfaceIpAddr,
       "wfSmdsSwInterfaceMIR": wfSmdsSwInterfaceMIR,
       "wfSmdsSwInterfaceCurrentRate": wfSmdsSwInterfaceCurrentRate,
       "wfSmdsSwAssocScrnTable": wfSmdsSwAssocScrnTable,
       "wfSmdsSwAssocScrnEntry": wfSmdsSwAssocScrnEntry,
       "wfSmdsSwAssocScrnDelete": wfSmdsSwAssocScrnDelete,
       "wfSmdsSwAssocScrnSniIndex": wfSmdsSwAssocScrnSniIndex,
       "wfSmdsSwAssocScrnAddrInd": wfSmdsSwAssocScrnAddrInd,
       "wfSmdsSwAssocScrnIndivIndex": wfSmdsSwAssocScrnIndivIndex,
       "wfSmdsSwAssocScrnGrpIndex": wfSmdsSwAssocScrnGrpIndex,
       "wfSmdsSwIAScrnTable": wfSmdsSwIAScrnTable,
       "wfSmdsSwIAScrnEntry": wfSmdsSwIAScrnEntry,
       "wfSmdsSwIAScrnDelete": wfSmdsSwIAScrnDelete,
       "wfSmdsSwIAScrnSniIndex": wfSmdsSwIAScrnSniIndex,
       "wfSmdsSwIAScrnIndex": wfSmdsSwIAScrnIndex,
       "wfSmdsSwIAScrnAddr": wfSmdsSwIAScrnAddr,
       "wfSmdsSwGAScrnTable": wfSmdsSwGAScrnTable,
       "wfSmdsSwGAScrnEntry": wfSmdsSwGAScrnEntry,
       "wfSmdsSwGAScrnDelete": wfSmdsSwGAScrnDelete,
       "wfSmdsSwGAScrnSniIndex": wfSmdsSwGAScrnSniIndex,
       "wfSmdsSwGAScrnIndex": wfSmdsSwGAScrnIndex,
       "wfSmdsSwGAScrnAddr": wfSmdsSwGAScrnAddr,
       "wfSmdsSwGATable": wfSmdsSwGATable,
       "wfSmdsSwGAEntry": wfSmdsSwGAEntry,
       "wfSmdsSwGADelete": wfSmdsSwGADelete,
       "wfSmdsSwGASSI": wfSmdsSwGASSI,
       "wfSmdsSwGAGroupAddress": wfSmdsSwGAGroupAddress,
       "wfSmdsSwGAGroupMember": wfSmdsSwGAGroupMember,
       "wfSmdsSwCurUsageTable": wfSmdsSwCurUsageTable,
       "wfSmdsSwCurUsageEntry": wfSmdsSwCurUsageEntry,
       "wfSmdsSwCurUsageDelete": wfSmdsSwCurUsageDelete,
       "wfSmdsSwCurUsageSni": wfSmdsSwCurUsageSni,
       "wfSmdsSwCurUsageDestAddr": wfSmdsSwCurUsageDestAddr,
       "wfSmdsSwCurUsageSrcAddr": wfSmdsSwCurUsageSrcAddr,
       "wfSmdsSwCurUsageGrpIndAddr": wfSmdsSwCurUsageGrpIndAddr,
       "wfSmdsSwCurUsageNumL3Pdu": wfSmdsSwCurUsageNumL3Pdu,
       "wfSmdsSwCurUsageNumOctet": wfSmdsSwCurUsageNumOctet,
       "wfSmdsSwCurUsageToBeDeleted": wfSmdsSwCurUsageToBeDeleted,
       "wfSmdsSwUsage": wfSmdsSwUsage,
       "wfSmdsSwUsageEnable": wfSmdsSwUsageEnable,
       "wfSmdsSwUsageVolume": wfSmdsSwUsageVolume,
       "wfSmdsSwUsageVolumeBackup": wfSmdsSwUsageVolumeBackup,
       "wfSmdsSwUsageDirectory": wfSmdsSwUsageDirectory,
       "wfSmdsSwUsageFilePrefix": wfSmdsSwUsageFilePrefix,
       "wfSmdsSwUsageTimerInterval": wfSmdsSwUsageTimerInterval,
       "wfSmdsSwUsageUpdateInterval": wfSmdsSwUsageUpdateInterval,
       "wfSmdsSwUsageStoreInterval": wfSmdsSwUsageStoreInterval,
       "wfSmdsSwUsageFlushInterval": wfSmdsSwUsageFlushInterval,
       "wfSmdsSwUsageCleanupInterval": wfSmdsSwUsageCleanupInterval,
       "wfSmdsSwUsageLocalTimeZone": wfSmdsSwUsageLocalTimeZone,
       "wfSmdsSwUsageUpdateTimeStamp": wfSmdsSwUsageUpdateTimeStamp,
       "wfSmdsSwUsageStoreTimeStamp": wfSmdsSwUsageStoreTimeStamp,
       "wfSmdsSwUsageFlushTimeStamp": wfSmdsSwUsageFlushTimeStamp,
       "wfSmdsSwUsageCleanupTimeStamp": wfSmdsSwUsageCleanupTimeStamp,
       "wfSmdsSwUsageUpdateData": wfSmdsSwUsageUpdateData,
       "wfSmdsSwUsageStoreData": wfSmdsSwUsageStoreData,
       "wfSmdsSwUsageFlushData": wfSmdsSwUsageFlushData,
       "wfSmdsSwUsageFileCleanup": wfSmdsSwUsageFileCleanup,
       "wfSmdsSwUsageState": wfSmdsSwUsageState,
       "wfSmdsSwUsageCurVolume": wfSmdsSwUsageCurVolume,
       "wfSmdsSwUsageCurVolumeBackup": wfSmdsSwUsageCurVolumeBackup,
       "wfSmdsSwUsageCurDirectory": wfSmdsSwUsageCurDirectory,
       "wfSmdsSwUsageCurFilePrefix": wfSmdsSwUsageCurFilePrefix,
       "wfSmdsSwUsageCurTimerInterval": wfSmdsSwUsageCurTimerInterval,
       "wfSmdsSwUsageCurUpdateInterval": wfSmdsSwUsageCurUpdateInterval,
       "wfSmdsSwUsageCurStoreInterval": wfSmdsSwUsageCurStoreInterval,
       "wfSmdsSwUsageCurFlushInterval": wfSmdsSwUsageCurFlushInterval,
       "wfSmdsSwUsageCurCleanupInterval": wfSmdsSwUsageCurCleanupInterval,
       "wfSmdsSwUsageDebug": wfSmdsSwUsageDebug,
       "wfSmdsSwUsageCurDebug": wfSmdsSwUsageCurDebug,
       "wfSmdsSwUsageSwitchId": wfSmdsSwUsageSwitchId,
       "wfSmdsSwUsageNumEntries": wfSmdsSwUsageNumEntries,
       "wfSmdsSwUsageTable": wfSmdsSwUsageTable,
       "wfSmdsSwUsageEntry": wfSmdsSwUsageEntry,
       "wfSmdsSwUsageDelete": wfSmdsSwUsageDelete,
       "wfSmdsSwUsageSni": wfSmdsSwUsageSni,
       "wfSmdsSwUsageDestAddr": wfSmdsSwUsageDestAddr,
       "wfSmdsSwUsageSrcAddr": wfSmdsSwUsageSrcAddr,
       "wfSmdsSwUsageStartTimeStampHigh": wfSmdsSwUsageStartTimeStampHigh,
       "wfSmdsSwUsageStartTimeStampLow": wfSmdsSwUsageStartTimeStampLow,
       "wfSmdsSwUsageEndTimeStampHigh": wfSmdsSwUsageEndTimeStampHigh,
       "wfSmdsSwUsageEndTimeStampLow": wfSmdsSwUsageEndTimeStampLow,
       "wfSmdsSwUsageSentL3PduHigh": wfSmdsSwUsageSentL3PduHigh,
       "wfSmdsSwUsageSentL3PduLow": wfSmdsSwUsageSentL3PduLow,
       "wfSmdsSwUsageSentOctetHigh": wfSmdsSwUsageSentOctetHigh,
       "wfSmdsSwUsageSentOctetLow": wfSmdsSwUsageSentOctetLow,
       "wfSmdsSwUsageLastL3PduHigh": wfSmdsSwUsageLastL3PduHigh,
       "wfSmdsSwUsageLastL3PduLow": wfSmdsSwUsageLastL3PduLow,
       "wfSmdsSwUsageLastOctetHigh": wfSmdsSwUsageLastOctetHigh,
       "wfSmdsSwUsageLastOctetLow": wfSmdsSwUsageLastOctetLow,
       "wfSmdsSwUsageGrpIndAddr": wfSmdsSwUsageGrpIndAddr,
       "wfSmdsSwSsiSniTable": wfSmdsSwSsiSniTable,
       "wfSmdsSwSsiSniEntry": wfSmdsSwSsiSniEntry,
       "wfSmdsSwSsiSniDelete": wfSmdsSwSsiSniDelete,
       "wfSmdsSwSsiSniSSI": wfSmdsSwSsiSniSSI,
       "wfSmdsSwSsiSniSNI": wfSmdsSwSsiSniSNI}
)
