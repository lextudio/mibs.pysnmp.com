# SNMP MIB module (Wellfleet-EGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-EGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:11 2024
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

(wfEgpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfEgpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfEgp_ObjectIdentity = ObjectIdentity
wfEgp = _WfEgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1)
)


class _WfEgpDelete_Type(Integer32):
    """Custom type wfEgpDelete based on Integer32"""
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


_WfEgpDelete_Type.__name__ = "Integer32"
_WfEgpDelete_Object = MibScalar
wfEgpDelete = _WfEgpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1, 1),
    _WfEgpDelete_Type()
)
wfEgpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpDelete.setStatus("mandatory")


class _WfEgpDisable_Type(Integer32):
    """Custom type wfEgpDisable based on Integer32"""
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


_WfEgpDisable_Type.__name__ = "Integer32"
_WfEgpDisable_Object = MibScalar
wfEgpDisable = _WfEgpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1, 2),
    _WfEgpDisable_Type()
)
wfEgpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpDisable.setStatus("mandatory")
_WfEgpInMsgs_Type = Counter32
_WfEgpInMsgs_Object = MibScalar
wfEgpInMsgs = _WfEgpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1, 3),
    _WfEgpInMsgs_Type()
)
wfEgpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpInMsgs.setStatus("mandatory")
_WfEgpInErrors_Type = Counter32
_WfEgpInErrors_Object = MibScalar
wfEgpInErrors = _WfEgpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1, 4),
    _WfEgpInErrors_Type()
)
wfEgpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpInErrors.setStatus("mandatory")
_WfEgpOutMsgs_Type = Counter32
_WfEgpOutMsgs_Object = MibScalar
wfEgpOutMsgs = _WfEgpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1, 5),
    _WfEgpOutMsgs_Type()
)
wfEgpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpOutMsgs.setStatus("mandatory")
_WfEgpOutErrors_Type = Counter32
_WfEgpOutErrors_Object = MibScalar
wfEgpOutErrors = _WfEgpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1, 6),
    _WfEgpOutErrors_Type()
)
wfEgpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpOutErrors.setStatus("mandatory")


class _WfEgpLocalAs_Type(Integer32):
    """Custom type wfEgpLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfEgpLocalAs_Type.__name__ = "Integer32"
_WfEgpLocalAs_Object = MibScalar
wfEgpLocalAs = _WfEgpLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 1, 7),
    _WfEgpLocalAs_Type()
)
wfEgpLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpLocalAs.setStatus("mandatory")
_WfEgpNeighTable_Object = MibTable
wfEgpNeighTable = _WfEgpNeighTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    wfEgpNeighTable.setStatus("mandatory")
_WfEgpNeighEntry_Object = MibTableRow
wfEgpNeighEntry = _WfEgpNeighEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1)
)
wfEgpNeighEntry.setIndexNames(
    (0, "Wellfleet-EGP-MIB", "wfEgpNeighAddr"),
)
if mibBuilder.loadTexts:
    wfEgpNeighEntry.setStatus("mandatory")


class _WfEgpNeighState_Type(Integer32):
    """Custom type wfEgpNeighState based on Integer32"""
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
        *(("acquisition", 2),
          ("cease", 5),
          ("down", 3),
          ("idle", 1),
          ("up", 4))
    )


_WfEgpNeighState_Type.__name__ = "Integer32"
_WfEgpNeighState_Object = MibTableColumn
wfEgpNeighState = _WfEgpNeighState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 1),
    _WfEgpNeighState_Type()
)
wfEgpNeighState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighState.setStatus("mandatory")
_WfEgpNeighAddr_Type = IpAddress
_WfEgpNeighAddr_Object = MibTableColumn
wfEgpNeighAddr = _WfEgpNeighAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 2),
    _WfEgpNeighAddr_Type()
)
wfEgpNeighAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighAddr.setStatus("mandatory")
_WfEgpNeighAs_Type = Integer32
_WfEgpNeighAs_Object = MibTableColumn
wfEgpNeighAs = _WfEgpNeighAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 3),
    _WfEgpNeighAs_Type()
)
wfEgpNeighAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighAs.setStatus("mandatory")
_WfEgpNeighInMsgs_Type = Counter32
_WfEgpNeighInMsgs_Object = MibTableColumn
wfEgpNeighInMsgs = _WfEgpNeighInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 4),
    _WfEgpNeighInMsgs_Type()
)
wfEgpNeighInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighInMsgs.setStatus("mandatory")
_WfEgpNeighInErrs_Type = Counter32
_WfEgpNeighInErrs_Object = MibTableColumn
wfEgpNeighInErrs = _WfEgpNeighInErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 5),
    _WfEgpNeighInErrs_Type()
)
wfEgpNeighInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighInErrs.setStatus("mandatory")
_WfEgpNeighOutMsgs_Type = Counter32
_WfEgpNeighOutMsgs_Object = MibTableColumn
wfEgpNeighOutMsgs = _WfEgpNeighOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 6),
    _WfEgpNeighOutMsgs_Type()
)
wfEgpNeighOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighOutMsgs.setStatus("mandatory")
_WfEgpNeighOutErrs_Type = Counter32
_WfEgpNeighOutErrs_Object = MibTableColumn
wfEgpNeighOutErrs = _WfEgpNeighOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 7),
    _WfEgpNeighOutErrs_Type()
)
wfEgpNeighOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighOutErrs.setStatus("mandatory")
_WfEgpNeighInErrMsgs_Type = Counter32
_WfEgpNeighInErrMsgs_Object = MibTableColumn
wfEgpNeighInErrMsgs = _WfEgpNeighInErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 8),
    _WfEgpNeighInErrMsgs_Type()
)
wfEgpNeighInErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighInErrMsgs.setStatus("mandatory")
_WfEgpNeighOutErrMsgs_Type = Counter32
_WfEgpNeighOutErrMsgs_Object = MibTableColumn
wfEgpNeighOutErrMsgs = _WfEgpNeighOutErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 9),
    _WfEgpNeighOutErrMsgs_Type()
)
wfEgpNeighOutErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighOutErrMsgs.setStatus("mandatory")
_WfEgpNeighStateUps_Type = Counter32
_WfEgpNeighStateUps_Object = MibTableColumn
wfEgpNeighStateUps = _WfEgpNeighStateUps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 10),
    _WfEgpNeighStateUps_Type()
)
wfEgpNeighStateUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighStateUps.setStatus("mandatory")
_WfEgpNeighStateDowns_Type = Counter32
_WfEgpNeighStateDowns_Object = MibTableColumn
wfEgpNeighStateDowns = _WfEgpNeighStateDowns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 11),
    _WfEgpNeighStateDowns_Type()
)
wfEgpNeighStateDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighStateDowns.setStatus("mandatory")
_WfEgpNeighIntervalHello_Type = Integer32
_WfEgpNeighIntervalHello_Object = MibTableColumn
wfEgpNeighIntervalHello = _WfEgpNeighIntervalHello_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 12),
    _WfEgpNeighIntervalHello_Type()
)
wfEgpNeighIntervalHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighIntervalHello.setStatus("mandatory")
_WfEgpNeighIntervalPoll_Type = Integer32
_WfEgpNeighIntervalPoll_Object = MibTableColumn
wfEgpNeighIntervalPoll = _WfEgpNeighIntervalPoll_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 13),
    _WfEgpNeighIntervalPoll_Type()
)
wfEgpNeighIntervalPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighIntervalPoll.setStatus("mandatory")


class _WfEgpNeighMode_Type(Integer32):
    """Custom type wfEgpNeighMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_WfEgpNeighMode_Type.__name__ = "Integer32"
_WfEgpNeighMode_Object = MibTableColumn
wfEgpNeighMode = _WfEgpNeighMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 14),
    _WfEgpNeighMode_Type()
)
wfEgpNeighMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighMode.setStatus("mandatory")
_WfEgpNeighEvent_Type = Integer32
_WfEgpNeighEvent_Object = MibTableColumn
wfEgpNeighEvent = _WfEgpNeighEvent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 15),
    _WfEgpNeighEvent_Type()
)
wfEgpNeighEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighEvent.setStatus("mandatory")
_WfEgpNeighBadAsns_Type = Counter32
_WfEgpNeighBadAsns_Object = MibTableColumn
wfEgpNeighBadAsns = _WfEgpNeighBadAsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 16),
    _WfEgpNeighBadAsns_Type()
)
wfEgpNeighBadAsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadAsns.setStatus("mandatory")
_WfEgpNeighBadCodes_Type = Counter32
_WfEgpNeighBadCodes_Object = MibTableColumn
wfEgpNeighBadCodes = _WfEgpNeighBadCodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 17),
    _WfEgpNeighBadCodes_Type()
)
wfEgpNeighBadCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadCodes.setStatus("mandatory")
_WfEgpNeighBadHellos_Type = Counter32
_WfEgpNeighBadHellos_Object = MibTableColumn
wfEgpNeighBadHellos = _WfEgpNeighBadHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 18),
    _WfEgpNeighBadHellos_Type()
)
wfEgpNeighBadHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadHellos.setStatus("mandatory")
_WfEgpNeighBadIHUs_Type = Counter32
_WfEgpNeighBadIHUs_Object = MibTableColumn
wfEgpNeighBadIHUs = _WfEgpNeighBadIHUs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 19),
    _WfEgpNeighBadIHUs_Type()
)
wfEgpNeighBadIHUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadIHUs.setStatus("mandatory")
_WfEgpNeighBadStatuses_Type = Counter32
_WfEgpNeighBadStatuses_Object = MibTableColumn
wfEgpNeighBadStatuses = _WfEgpNeighBadStatuses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 20),
    _WfEgpNeighBadStatuses_Type()
)
wfEgpNeighBadStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadStatuses.setStatus("mandatory")
_WfEgpNeighBadChecksums_Type = Counter32
_WfEgpNeighBadChecksums_Object = MibTableColumn
wfEgpNeighBadChecksums = _WfEgpNeighBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 21),
    _WfEgpNeighBadChecksums_Type()
)
wfEgpNeighBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadChecksums.setStatus("mandatory")
_WfEgpNeighBadTypes_Type = Counter32
_WfEgpNeighBadTypes_Object = MibTableColumn
wfEgpNeighBadTypes = _WfEgpNeighBadTypes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 22),
    _WfEgpNeighBadTypes_Type()
)
wfEgpNeighBadTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadTypes.setStatus("mandatory")
_WfEgpNeighBadVersions_Type = Counter32
_WfEgpNeighBadVersions_Object = MibTableColumn
wfEgpNeighBadVersions = _WfEgpNeighBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 23),
    _WfEgpNeighBadVersions_Type()
)
wfEgpNeighBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighBadVersions.setStatus("mandatory")
_WfEgpNeighCmdOutOfSeqs_Type = Counter32
_WfEgpNeighCmdOutOfSeqs_Object = MibTableColumn
wfEgpNeighCmdOutOfSeqs = _WfEgpNeighCmdOutOfSeqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 24),
    _WfEgpNeighCmdOutOfSeqs_Type()
)
wfEgpNeighCmdOutOfSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighCmdOutOfSeqs.setStatus("mandatory")
_WfEgpNeighCmdRejects_Type = Counter32
_WfEgpNeighCmdRejects_Object = MibTableColumn
wfEgpNeighCmdRejects = _WfEgpNeighCmdRejects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 2, 1, 25),
    _WfEgpNeighCmdRejects_Type()
)
wfEgpNeighCmdRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpNeighCmdRejects.setStatus("mandatory")
_WfEgpCfgNeighTable_Object = MibTable
wfEgpCfgNeighTable = _WfEgpCfgNeighTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3)
)
if mibBuilder.loadTexts:
    wfEgpCfgNeighTable.setStatus("mandatory")
_WfEgpCfgNeighEntry_Object = MibTableRow
wfEgpCfgNeighEntry = _WfEgpCfgNeighEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1)
)
wfEgpCfgNeighEntry.setIndexNames(
    (0, "Wellfleet-EGP-MIB", "wfEgpCfgNeighRemoteAddr"),
)
if mibBuilder.loadTexts:
    wfEgpCfgNeighEntry.setStatus("mandatory")


class _WfEgpCfgNeighDelete_Type(Integer32):
    """Custom type wfEgpCfgNeighDelete based on Integer32"""
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


_WfEgpCfgNeighDelete_Type.__name__ = "Integer32"
_WfEgpCfgNeighDelete_Object = MibTableColumn
wfEgpCfgNeighDelete = _WfEgpCfgNeighDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 1),
    _WfEgpCfgNeighDelete_Type()
)
wfEgpCfgNeighDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpCfgNeighDelete.setStatus("mandatory")


class _WfEgpCfgNeighDisable_Type(Integer32):
    """Custom type wfEgpCfgNeighDisable based on Integer32"""
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


_WfEgpCfgNeighDisable_Type.__name__ = "Integer32"
_WfEgpCfgNeighDisable_Object = MibTableColumn
wfEgpCfgNeighDisable = _WfEgpCfgNeighDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 2),
    _WfEgpCfgNeighDisable_Type()
)
wfEgpCfgNeighDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpCfgNeighDisable.setStatus("mandatory")


class _WfEgpCfgNeighState_Type(Integer32):
    """Custom type wfEgpCfgNeighState based on Integer32"""
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


_WfEgpCfgNeighState_Type.__name__ = "Integer32"
_WfEgpCfgNeighState_Object = MibTableColumn
wfEgpCfgNeighState = _WfEgpCfgNeighState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 3),
    _WfEgpCfgNeighState_Type()
)
wfEgpCfgNeighState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpCfgNeighState.setStatus("mandatory")
_WfEgpCfgNeighLocalAddr_Type = IpAddress
_WfEgpCfgNeighLocalAddr_Object = MibTableColumn
wfEgpCfgNeighLocalAddr = _WfEgpCfgNeighLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 4),
    _WfEgpCfgNeighLocalAddr_Type()
)
wfEgpCfgNeighLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpCfgNeighLocalAddr.setStatus("mandatory")
_WfEgpCfgNeighRemoteAddr_Type = IpAddress
_WfEgpCfgNeighRemoteAddr_Object = MibTableColumn
wfEgpCfgNeighRemoteAddr = _WfEgpCfgNeighRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 5),
    _WfEgpCfgNeighRemoteAddr_Type()
)
wfEgpCfgNeighRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfEgpCfgNeighRemoteAddr.setStatus("mandatory")


class _WfEgpCfgNeighGatewayMode_Type(Integer32):
    """Custom type wfEgpCfgNeighGatewayMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("core", 2),
          ("noncore", 1))
    )


_WfEgpCfgNeighGatewayMode_Type.__name__ = "Integer32"
_WfEgpCfgNeighGatewayMode_Object = MibTableColumn
wfEgpCfgNeighGatewayMode = _WfEgpCfgNeighGatewayMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 6),
    _WfEgpCfgNeighGatewayMode_Type()
)
wfEgpCfgNeighGatewayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpCfgNeighGatewayMode.setStatus("mandatory")


class _WfEgpCfgNeighAcqMode_Type(Integer32):
    """Custom type wfEgpCfgNeighAcqMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_WfEgpCfgNeighAcqMode_Type.__name__ = "Integer32"
_WfEgpCfgNeighAcqMode_Object = MibTableColumn
wfEgpCfgNeighAcqMode = _WfEgpCfgNeighAcqMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 7),
    _WfEgpCfgNeighAcqMode_Type()
)
wfEgpCfgNeighAcqMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpCfgNeighAcqMode.setStatus("mandatory")


class _WfEgpCfgNeighPollMode_Type(Integer32):
    """Custom type wfEgpCfgNeighPollMode based on Integer32"""
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
        *(("active", 1),
          ("both", 3),
          ("passive", 2))
    )


_WfEgpCfgNeighPollMode_Type.__name__ = "Integer32"
_WfEgpCfgNeighPollMode_Object = MibTableColumn
wfEgpCfgNeighPollMode = _WfEgpCfgNeighPollMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 8),
    _WfEgpCfgNeighPollMode_Type()
)
wfEgpCfgNeighPollMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpCfgNeighPollMode.setStatus("mandatory")


class _WfEgpCfgNeighHelloTimer_Type(Integer32):
    """Custom type wfEgpCfgNeighHelloTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_WfEgpCfgNeighHelloTimer_Type.__name__ = "Integer32"
_WfEgpCfgNeighHelloTimer_Object = MibTableColumn
wfEgpCfgNeighHelloTimer = _WfEgpCfgNeighHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 9),
    _WfEgpCfgNeighHelloTimer_Type()
)
wfEgpCfgNeighHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpCfgNeighHelloTimer.setStatus("mandatory")


class _WfEgpCfgNeighPollTimer_Type(Integer32):
    """Custom type wfEgpCfgNeighPollTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 480),
    )


_WfEgpCfgNeighPollTimer_Type.__name__ = "Integer32"
_WfEgpCfgNeighPollTimer_Object = MibTableColumn
wfEgpCfgNeighPollTimer = _WfEgpCfgNeighPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4, 3, 1, 10),
    _WfEgpCfgNeighPollTimer_Type()
)
wfEgpCfgNeighPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEgpCfgNeighPollTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-EGP-MIB",
    **{"wfEgp": wfEgp,
       "wfEgpDelete": wfEgpDelete,
       "wfEgpDisable": wfEgpDisable,
       "wfEgpInMsgs": wfEgpInMsgs,
       "wfEgpInErrors": wfEgpInErrors,
       "wfEgpOutMsgs": wfEgpOutMsgs,
       "wfEgpOutErrors": wfEgpOutErrors,
       "wfEgpLocalAs": wfEgpLocalAs,
       "wfEgpNeighTable": wfEgpNeighTable,
       "wfEgpNeighEntry": wfEgpNeighEntry,
       "wfEgpNeighState": wfEgpNeighState,
       "wfEgpNeighAddr": wfEgpNeighAddr,
       "wfEgpNeighAs": wfEgpNeighAs,
       "wfEgpNeighInMsgs": wfEgpNeighInMsgs,
       "wfEgpNeighInErrs": wfEgpNeighInErrs,
       "wfEgpNeighOutMsgs": wfEgpNeighOutMsgs,
       "wfEgpNeighOutErrs": wfEgpNeighOutErrs,
       "wfEgpNeighInErrMsgs": wfEgpNeighInErrMsgs,
       "wfEgpNeighOutErrMsgs": wfEgpNeighOutErrMsgs,
       "wfEgpNeighStateUps": wfEgpNeighStateUps,
       "wfEgpNeighStateDowns": wfEgpNeighStateDowns,
       "wfEgpNeighIntervalHello": wfEgpNeighIntervalHello,
       "wfEgpNeighIntervalPoll": wfEgpNeighIntervalPoll,
       "wfEgpNeighMode": wfEgpNeighMode,
       "wfEgpNeighEvent": wfEgpNeighEvent,
       "wfEgpNeighBadAsns": wfEgpNeighBadAsns,
       "wfEgpNeighBadCodes": wfEgpNeighBadCodes,
       "wfEgpNeighBadHellos": wfEgpNeighBadHellos,
       "wfEgpNeighBadIHUs": wfEgpNeighBadIHUs,
       "wfEgpNeighBadStatuses": wfEgpNeighBadStatuses,
       "wfEgpNeighBadChecksums": wfEgpNeighBadChecksums,
       "wfEgpNeighBadTypes": wfEgpNeighBadTypes,
       "wfEgpNeighBadVersions": wfEgpNeighBadVersions,
       "wfEgpNeighCmdOutOfSeqs": wfEgpNeighCmdOutOfSeqs,
       "wfEgpNeighCmdRejects": wfEgpNeighCmdRejects,
       "wfEgpCfgNeighTable": wfEgpCfgNeighTable,
       "wfEgpCfgNeighEntry": wfEgpCfgNeighEntry,
       "wfEgpCfgNeighDelete": wfEgpCfgNeighDelete,
       "wfEgpCfgNeighDisable": wfEgpCfgNeighDisable,
       "wfEgpCfgNeighState": wfEgpCfgNeighState,
       "wfEgpCfgNeighLocalAddr": wfEgpCfgNeighLocalAddr,
       "wfEgpCfgNeighRemoteAddr": wfEgpCfgNeighRemoteAddr,
       "wfEgpCfgNeighGatewayMode": wfEgpCfgNeighGatewayMode,
       "wfEgpCfgNeighAcqMode": wfEgpCfgNeighAcqMode,
       "wfEgpCfgNeighPollMode": wfEgpCfgNeighPollMode,
       "wfEgpCfgNeighHelloTimer": wfEgpCfgNeighHelloTimer,
       "wfEgpCfgNeighPollTimer": wfEgpCfgNeighPollTimer}
)
