# SNMP MIB module (Wellfleet-SNMPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SNMPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:06 2024
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

(AutonomousType,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention")

(wfSnmpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSnmpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSnmp_ObjectIdentity = ObjectIdentity
wfSnmp = _WfSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1)
)


class _WfSnmpDisable_Type(Integer32):
    """Custom type wfSnmpDisable based on Integer32"""
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


_WfSnmpDisable_Type.__name__ = "Integer32"
_WfSnmpDisable_Object = MibScalar
wfSnmpDisable = _WfSnmpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 1),
    _WfSnmpDisable_Type()
)
wfSnmpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpDisable.setStatus("mandatory")


class _WfSnmpUseLock_Type(Integer32):
    """Custom type wfSnmpUseLock based on Integer32"""
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


_WfSnmpUseLock_Type.__name__ = "Integer32"
_WfSnmpUseLock_Object = MibScalar
wfSnmpUseLock = _WfSnmpUseLock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 2),
    _WfSnmpUseLock_Type()
)
wfSnmpUseLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpUseLock.setStatus("mandatory")
_WfSnmpLockAddress_Type = IpAddress
_WfSnmpLockAddress_Object = MibScalar
wfSnmpLockAddress = _WfSnmpLockAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 3),
    _WfSnmpLockAddress_Type()
)
wfSnmpLockAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpLockAddress.setStatus("mandatory")


class _WfSnmpLockTimeOut_Type(Integer32):
    """Custom type wfSnmpLockTimeOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfSnmpLockTimeOut_Type.__name__ = "Integer32"
_WfSnmpLockTimeOut_Object = MibScalar
wfSnmpLockTimeOut = _WfSnmpLockTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 4),
    _WfSnmpLockTimeOut_Type()
)
wfSnmpLockTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpLockTimeOut.setStatus("mandatory")


class _WfSnmpAuth_Type(Integer32):
    """Custom type wfSnmpAuth based on Integer32"""
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
        *(("party", 2),
          ("proprietary", 3),
          ("trivial", 1))
    )


_WfSnmpAuth_Type.__name__ = "Integer32"
_WfSnmpAuth_Object = MibScalar
wfSnmpAuth = _WfSnmpAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 5),
    _WfSnmpAuth_Type()
)
wfSnmpAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpAuth.setStatus("mandatory")
_WfSnmpInPkts_Type = Counter32
_WfSnmpInPkts_Object = MibScalar
wfSnmpInPkts = _WfSnmpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 6),
    _WfSnmpInPkts_Type()
)
wfSnmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInPkts.setStatus("mandatory")
_WfSnmpOutPkts_Type = Counter32
_WfSnmpOutPkts_Object = MibScalar
wfSnmpOutPkts = _WfSnmpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 7),
    _WfSnmpOutPkts_Type()
)
wfSnmpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutPkts.setStatus("mandatory")
_WfSnmpInBadVersions_Type = Counter32
_WfSnmpInBadVersions_Object = MibScalar
wfSnmpInBadVersions = _WfSnmpInBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 8),
    _WfSnmpInBadVersions_Type()
)
wfSnmpInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadVersions.setStatus("mandatory")
_WfSnmpInBadCommunityNames_Type = Counter32
_WfSnmpInBadCommunityNames_Object = MibScalar
wfSnmpInBadCommunityNames = _WfSnmpInBadCommunityNames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 9),
    _WfSnmpInBadCommunityNames_Type()
)
wfSnmpInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadCommunityNames.setStatus("mandatory")
_WfSnmpInBadCommunityUses_Type = Counter32
_WfSnmpInBadCommunityUses_Object = MibScalar
wfSnmpInBadCommunityUses = _WfSnmpInBadCommunityUses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 10),
    _WfSnmpInBadCommunityUses_Type()
)
wfSnmpInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadCommunityUses.setStatus("mandatory")
_WfSnmpInASNParseErrs_Type = Counter32
_WfSnmpInASNParseErrs_Object = MibScalar
wfSnmpInASNParseErrs = _WfSnmpInASNParseErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 11),
    _WfSnmpInASNParseErrs_Type()
)
wfSnmpInASNParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInASNParseErrs.setStatus("mandatory")
_WfSnmpInBadTypes_Type = Counter32
_WfSnmpInBadTypes_Object = MibScalar
wfSnmpInBadTypes = _WfSnmpInBadTypes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 12),
    _WfSnmpInBadTypes_Type()
)
wfSnmpInBadTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadTypes.setStatus("mandatory")
_WfSnmpInTooBigs_Type = Counter32
_WfSnmpInTooBigs_Object = MibScalar
wfSnmpInTooBigs = _WfSnmpInTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 13),
    _WfSnmpInTooBigs_Type()
)
wfSnmpInTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTooBigs.setStatus("mandatory")
_WfSnmpInNoSuchNames_Type = Counter32
_WfSnmpInNoSuchNames_Object = MibScalar
wfSnmpInNoSuchNames = _WfSnmpInNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 14),
    _WfSnmpInNoSuchNames_Type()
)
wfSnmpInNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInNoSuchNames.setStatus("mandatory")
_WfSnmpInBadValues_Type = Counter32
_WfSnmpInBadValues_Object = MibScalar
wfSnmpInBadValues = _WfSnmpInBadValues_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 15),
    _WfSnmpInBadValues_Type()
)
wfSnmpInBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadValues.setStatus("mandatory")
_WfSnmpInReadOnlys_Type = Counter32
_WfSnmpInReadOnlys_Object = MibScalar
wfSnmpInReadOnlys = _WfSnmpInReadOnlys_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 16),
    _WfSnmpInReadOnlys_Type()
)
wfSnmpInReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInReadOnlys.setStatus("mandatory")
_WfSnmpInGenErrs_Type = Counter32
_WfSnmpInGenErrs_Object = MibScalar
wfSnmpInGenErrs = _WfSnmpInGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 17),
    _WfSnmpInGenErrs_Type()
)
wfSnmpInGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGenErrs.setStatus("mandatory")
_WfSnmpInTotalReqVars_Type = Counter32
_WfSnmpInTotalReqVars_Object = MibScalar
wfSnmpInTotalReqVars = _WfSnmpInTotalReqVars_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 18),
    _WfSnmpInTotalReqVars_Type()
)
wfSnmpInTotalReqVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTotalReqVars.setStatus("mandatory")
_WfSnmpInTotalSetVars_Type = Counter32
_WfSnmpInTotalSetVars_Object = MibScalar
wfSnmpInTotalSetVars = _WfSnmpInTotalSetVars_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 19),
    _WfSnmpInTotalSetVars_Type()
)
wfSnmpInTotalSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTotalSetVars.setStatus("mandatory")
_WfSnmpInGetRequests_Type = Counter32
_WfSnmpInGetRequests_Object = MibScalar
wfSnmpInGetRequests = _WfSnmpInGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 20),
    _WfSnmpInGetRequests_Type()
)
wfSnmpInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGetRequests.setStatus("mandatory")
_WfSnmpInGetNexts_Type = Counter32
_WfSnmpInGetNexts_Object = MibScalar
wfSnmpInGetNexts = _WfSnmpInGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 21),
    _WfSnmpInGetNexts_Type()
)
wfSnmpInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGetNexts.setStatus("mandatory")
_WfSnmpInSetRequests_Type = Counter32
_WfSnmpInSetRequests_Object = MibScalar
wfSnmpInSetRequests = _WfSnmpInSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 22),
    _WfSnmpInSetRequests_Type()
)
wfSnmpInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInSetRequests.setStatus("mandatory")
_WfSnmpInGetResponses_Type = Counter32
_WfSnmpInGetResponses_Object = MibScalar
wfSnmpInGetResponses = _WfSnmpInGetResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 23),
    _WfSnmpInGetResponses_Type()
)
wfSnmpInGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGetResponses.setStatus("mandatory")
_WfSnmpInTraps_Type = Counter32
_WfSnmpInTraps_Object = MibScalar
wfSnmpInTraps = _WfSnmpInTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 24),
    _WfSnmpInTraps_Type()
)
wfSnmpInTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTraps.setStatus("mandatory")
_WfSnmpOutTooBigs_Type = Counter32
_WfSnmpOutTooBigs_Object = MibScalar
wfSnmpOutTooBigs = _WfSnmpOutTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 25),
    _WfSnmpOutTooBigs_Type()
)
wfSnmpOutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutTooBigs.setStatus("mandatory")
_WfSnmpOutNoSuchNames_Type = Counter32
_WfSnmpOutNoSuchNames_Object = MibScalar
wfSnmpOutNoSuchNames = _WfSnmpOutNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 26),
    _WfSnmpOutNoSuchNames_Type()
)
wfSnmpOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutNoSuchNames.setStatus("mandatory")
_WfSnmpOutBadValues_Type = Counter32
_WfSnmpOutBadValues_Object = MibScalar
wfSnmpOutBadValues = _WfSnmpOutBadValues_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 27),
    _WfSnmpOutBadValues_Type()
)
wfSnmpOutBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutBadValues.setStatus("mandatory")
_WfSnmpOutReadOnlys_Type = Counter32
_WfSnmpOutReadOnlys_Object = MibScalar
wfSnmpOutReadOnlys = _WfSnmpOutReadOnlys_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 28),
    _WfSnmpOutReadOnlys_Type()
)
wfSnmpOutReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutReadOnlys.setStatus("mandatory")
_WfSnmpOutGenErrs_Type = Counter32
_WfSnmpOutGenErrs_Object = MibScalar
wfSnmpOutGenErrs = _WfSnmpOutGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 29),
    _WfSnmpOutGenErrs_Type()
)
wfSnmpOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGenErrs.setStatus("mandatory")
_WfSnmpOutGetRequests_Type = Counter32
_WfSnmpOutGetRequests_Object = MibScalar
wfSnmpOutGetRequests = _WfSnmpOutGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 30),
    _WfSnmpOutGetRequests_Type()
)
wfSnmpOutGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGetRequests.setStatus("mandatory")
_WfSnmpOutGetNexts_Type = Counter32
_WfSnmpOutGetNexts_Object = MibScalar
wfSnmpOutGetNexts = _WfSnmpOutGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 31),
    _WfSnmpOutGetNexts_Type()
)
wfSnmpOutGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGetNexts.setStatus("mandatory")
_WfSnmpOutSetRequests_Type = Counter32
_WfSnmpOutSetRequests_Object = MibScalar
wfSnmpOutSetRequests = _WfSnmpOutSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 32),
    _WfSnmpOutSetRequests_Type()
)
wfSnmpOutSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutSetRequests.setStatus("mandatory")
_WfSnmpOutGetResponses_Type = Counter32
_WfSnmpOutGetResponses_Object = MibScalar
wfSnmpOutGetResponses = _WfSnmpOutGetResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 33),
    _WfSnmpOutGetResponses_Type()
)
wfSnmpOutGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGetResponses.setStatus("mandatory")
_WfSnmpOutTraps_Type = Counter32
_WfSnmpOutTraps_Object = MibScalar
wfSnmpOutTraps = _WfSnmpOutTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 34),
    _WfSnmpOutTraps_Type()
)
wfSnmpOutTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutTraps.setStatus("mandatory")


class _WfSnmpEnableAuthTraps_Type(Integer32):
    """Custom type wfSnmpEnableAuthTraps based on Integer32"""
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


_WfSnmpEnableAuthTraps_Type.__name__ = "Integer32"
_WfSnmpEnableAuthTraps_Object = MibScalar
wfSnmpEnableAuthTraps = _WfSnmpEnableAuthTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 35),
    _WfSnmpEnableAuthTraps_Type()
)
wfSnmpEnableAuthTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpEnableAuthTraps.setStatus("mandatory")


class _WfSnmpTrapDebug_Type(Integer32):
    """Custom type wfSnmpTrapDebug based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapDebug_Type.__name__ = "Integer32"
_WfSnmpTrapDebug_Object = MibScalar
wfSnmpTrapDebug = _WfSnmpTrapDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 36),
    _WfSnmpTrapDebug_Type()
)
wfSnmpTrapDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapDebug.setStatus("obsolete")


class _WfSnmpTrapTrace_Type(Integer32):
    """Custom type wfSnmpTrapTrace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapTrace_Type.__name__ = "Integer32"
_WfSnmpTrapTrace_Object = MibScalar
wfSnmpTrapTrace = _WfSnmpTrapTrace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 37),
    _WfSnmpTrapTrace_Type()
)
wfSnmpTrapTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapTrace.setStatus("obsolete")


class _WfSnmpTrapInfo_Type(Integer32):
    """Custom type wfSnmpTrapInfo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapInfo_Type.__name__ = "Integer32"
_WfSnmpTrapInfo_Object = MibScalar
wfSnmpTrapInfo = _WfSnmpTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 38),
    _WfSnmpTrapInfo_Type()
)
wfSnmpTrapInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapInfo.setStatus("obsolete")


class _WfSnmpTrapWarn_Type(Integer32):
    """Custom type wfSnmpTrapWarn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapWarn_Type.__name__ = "Integer32"
_WfSnmpTrapWarn_Object = MibScalar
wfSnmpTrapWarn = _WfSnmpTrapWarn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 39),
    _WfSnmpTrapWarn_Type()
)
wfSnmpTrapWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapWarn.setStatus("obsolete")


class _WfSnmpTrapFault_Type(Integer32):
    """Custom type wfSnmpTrapFault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapFault_Type.__name__ = "Integer32"
_WfSnmpTrapFault_Object = MibScalar
wfSnmpTrapFault = _WfSnmpTrapFault_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 40),
    _WfSnmpTrapFault_Type()
)
wfSnmpTrapFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapFault.setStatus("obsolete")


class _WfSnmpIpTos_Type(Integer32):
    """Custom type wfSnmpIpTos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reliability", 2))
    )


_WfSnmpIpTos_Type.__name__ = "Integer32"
_WfSnmpIpTos_Object = MibScalar
wfSnmpIpTos = _WfSnmpIpTos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 41),
    _WfSnmpIpTos_Type()
)
wfSnmpIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpIpTos.setStatus("obsolete")


class _WfSnmpPropEncryption_Type(Integer32):
    """Custom type wfSnmpPropEncryption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("others", 2),
          ("wflt", 1))
    )


_WfSnmpPropEncryption_Type.__name__ = "Integer32"
_WfSnmpPropEncryption_Object = MibScalar
wfSnmpPropEncryption = _WfSnmpPropEncryption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 42),
    _WfSnmpPropEncryption_Type()
)
wfSnmpPropEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpPropEncryption.setStatus("mandatory")


class _WfSnmpPDUThreads_Type(Integer32):
    """Custom type wfSnmpPDUThreads based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_WfSnmpPDUThreads_Type.__name__ = "Integer32"
_WfSnmpPDUThreads_Object = MibScalar
wfSnmpPDUThreads = _WfSnmpPDUThreads_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 43),
    _WfSnmpPDUThreads_Type()
)
wfSnmpPDUThreads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpPDUThreads.setStatus("mandatory")
_WfSnmpBusyPDUThreads_Type = Gauge32
_WfSnmpBusyPDUThreads_Object = MibScalar
wfSnmpBusyPDUThreads = _WfSnmpBusyPDUThreads_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 44),
    _WfSnmpBusyPDUThreads_Type()
)
wfSnmpBusyPDUThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpBusyPDUThreads.setStatus("mandatory")


class _WfSnmpLogLevel_Type(Integer32):
    """Custom type wfSnmpLogLevel based on Integer32"""
    defaultValue = 8

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
        *(("apall", 1),
          ("aperror", 2),
          ("aperrwarn", 7),
          ("apnone", 8),
          ("aptrace", 4),
          ("aptraceerr", 5),
          ("aptracewarn", 6),
          ("apwarn", 3))
    )


_WfSnmpLogLevel_Type.__name__ = "Integer32"
_WfSnmpLogLevel_Object = MibScalar
wfSnmpLogLevel = _WfSnmpLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 45),
    _WfSnmpLogLevel_Type()
)
wfSnmpLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpLogLevel.setStatus("mandatory")


class _WfSnmpDelete_Type(Integer32):
    """Custom type wfSnmpDelete based on Integer32"""
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


_WfSnmpDelete_Type.__name__ = "Integer32"
_WfSnmpDelete_Object = MibScalar
wfSnmpDelete = _WfSnmpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 46),
    _WfSnmpDelete_Type()
)
wfSnmpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpDelete.setStatus("mandatory")


class _WfSnmpScopeDelimiter_Type(OctetString):
    """Custom type wfSnmpScopeDelimiter based on OctetString"""
    defaultValue = OctetString("@")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_WfSnmpScopeDelimiter_Type.__name__ = "OctetString"
_WfSnmpScopeDelimiter_Object = MibScalar
wfSnmpScopeDelimiter = _WfSnmpScopeDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 47),
    _WfSnmpScopeDelimiter_Type()
)
wfSnmpScopeDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpScopeDelimiter.setStatus("mandatory")


class _WfSnmpMaxInPktChain_Type(Integer32):
    """Custom type wfSnmpMaxInPktChain based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WfSnmpMaxInPktChain_Type.__name__ = "Integer32"
_WfSnmpMaxInPktChain_Object = MibScalar
wfSnmpMaxInPktChain = _WfSnmpMaxInPktChain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 48),
    _WfSnmpMaxInPktChain_Type()
)
wfSnmpMaxInPktChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMaxInPktChain.setStatus("mandatory")
_WfSnmpCommTable_Object = MibTable
wfSnmpCommTable = _WfSnmpCommTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2)
)
if mibBuilder.loadTexts:
    wfSnmpCommTable.setStatus("mandatory")
_WfSnmpCommEntry_Object = MibTableRow
wfSnmpCommEntry = _WfSnmpCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1)
)
wfSnmpCommEntry.setIndexNames(
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpCommIndex"),
)
if mibBuilder.loadTexts:
    wfSnmpCommEntry.setStatus("mandatory")


class _WfSnmpCommDelete_Type(Integer32):
    """Custom type wfSnmpCommDelete based on Integer32"""
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


_WfSnmpCommDelete_Type.__name__ = "Integer32"
_WfSnmpCommDelete_Object = MibTableColumn
wfSnmpCommDelete = _WfSnmpCommDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 1),
    _WfSnmpCommDelete_Type()
)
wfSnmpCommDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommDelete.setStatus("mandatory")
_WfSnmpCommIndex_Type = Integer32
_WfSnmpCommIndex_Object = MibTableColumn
wfSnmpCommIndex = _WfSnmpCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 2),
    _WfSnmpCommIndex_Type()
)
wfSnmpCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpCommIndex.setStatus("mandatory")
_WfSnmpCommName_Type = DisplayString
_WfSnmpCommName_Object = MibTableColumn
wfSnmpCommName = _WfSnmpCommName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 3),
    _WfSnmpCommName_Type()
)
wfSnmpCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommName.setStatus("mandatory")


class _WfSnmpCommAccess_Type(Integer32):
    """Custom type wfSnmpCommAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_WfSnmpCommAccess_Type.__name__ = "Integer32"
_WfSnmpCommAccess_Object = MibTableColumn
wfSnmpCommAccess = _WfSnmpCommAccess_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 4),
    _WfSnmpCommAccess_Type()
)
wfSnmpCommAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommAccess.setStatus("mandatory")
_WfSnmpCommScopeType_Type = AutonomousType
_WfSnmpCommScopeType_Object = MibTableColumn
wfSnmpCommScopeType = _WfSnmpCommScopeType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 5),
    _WfSnmpCommScopeType_Type()
)
wfSnmpCommScopeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommScopeType.setStatus("mandatory")
_WfSnmpCommViewIndex_Type = Integer32
_WfSnmpCommViewIndex_Object = MibTableColumn
wfSnmpCommViewIndex = _WfSnmpCommViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 6),
    _WfSnmpCommViewIndex_Type()
)
wfSnmpCommViewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommViewIndex.setStatus("mandatory")
_WfSnmpMgrTable_Object = MibTable
wfSnmpMgrTable = _WfSnmpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3)
)
if mibBuilder.loadTexts:
    wfSnmpMgrTable.setStatus("mandatory")
_WfSnmpMgrEntry_Object = MibTableRow
wfSnmpMgrEntry = _WfSnmpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1)
)
wfSnmpMgrEntry.setIndexNames(
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpMgrCommIndex"),
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpMgrAddress"),
)
if mibBuilder.loadTexts:
    wfSnmpMgrEntry.setStatus("mandatory")


class _WfSnmpMgrDelete_Type(Integer32):
    """Custom type wfSnmpMgrDelete based on Integer32"""
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


_WfSnmpMgrDelete_Type.__name__ = "Integer32"
_WfSnmpMgrDelete_Object = MibTableColumn
wfSnmpMgrDelete = _WfSnmpMgrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 1),
    _WfSnmpMgrDelete_Type()
)
wfSnmpMgrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrDelete.setStatus("mandatory")
_WfSnmpMgrCommIndex_Type = Integer32
_WfSnmpMgrCommIndex_Object = MibTableColumn
wfSnmpMgrCommIndex = _WfSnmpMgrCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 2),
    _WfSnmpMgrCommIndex_Type()
)
wfSnmpMgrCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrCommIndex.setStatus("mandatory")
_WfSnmpMgrAddress_Type = IpAddress
_WfSnmpMgrAddress_Object = MibTableColumn
wfSnmpMgrAddress = _WfSnmpMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 3),
    _WfSnmpMgrAddress_Type()
)
wfSnmpMgrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrAddress.setStatus("mandatory")
_WfSnmpMgrName_Type = DisplayString
_WfSnmpMgrName_Object = MibTableColumn
wfSnmpMgrName = _WfSnmpMgrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 4),
    _WfSnmpMgrName_Type()
)
wfSnmpMgrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrName.setStatus("mandatory")


class _WfSnmpMgrTrapPort_Type(Integer32):
    """Custom type wfSnmpMgrTrapPort based on Integer32"""
    defaultValue = 162


_WfSnmpMgrTrapPort_Object = MibTableColumn
wfSnmpMgrTrapPort = _WfSnmpMgrTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 5),
    _WfSnmpMgrTrapPort_Type()
)
wfSnmpMgrTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrTrapPort.setStatus("mandatory")


class _WfSnmpMgrTraps_Type(Integer32):
    """Custom type wfSnmpMgrTraps based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 7),
          ("generic", 2),
          ("none", 1),
          ("specific", 4))
    )


_WfSnmpMgrTraps_Type.__name__ = "Integer32"
_WfSnmpMgrTraps_Object = MibTableColumn
wfSnmpMgrTraps = _WfSnmpMgrTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 6),
    _WfSnmpMgrTraps_Type()
)
wfSnmpMgrTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrTraps.setStatus("mandatory")
_WfSnmpMgrEncrSeed1_Type = Integer32
_WfSnmpMgrEncrSeed1_Object = MibTableColumn
wfSnmpMgrEncrSeed1 = _WfSnmpMgrEncrSeed1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 7),
    _WfSnmpMgrEncrSeed1_Type()
)
wfSnmpMgrEncrSeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrEncrSeed1.setStatus("mandatory")
_WfSnmpMgrEncrSeed2_Type = Integer32
_WfSnmpMgrEncrSeed2_Object = MibTableColumn
wfSnmpMgrEncrSeed2 = _WfSnmpMgrEncrSeed2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 8),
    _WfSnmpMgrEncrSeed2_Type()
)
wfSnmpMgrEncrSeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrEncrSeed2.setStatus("mandatory")
_WfSnmpMgrEncrSeed3_Type = Integer32
_WfSnmpMgrEncrSeed3_Object = MibTableColumn
wfSnmpMgrEncrSeed3 = _WfSnmpMgrEncrSeed3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 9),
    _WfSnmpMgrEncrSeed3_Type()
)
wfSnmpMgrEncrSeed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrEncrSeed3.setStatus("mandatory")
_WfSnmpMgrEncrSeed4_Type = Integer32
_WfSnmpMgrEncrSeed4_Object = MibTableColumn
wfSnmpMgrEncrSeed4 = _WfSnmpMgrEncrSeed4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 10),
    _WfSnmpMgrEncrSeed4_Type()
)
wfSnmpMgrEncrSeed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrEncrSeed4.setStatus("mandatory")
_WfSnmpMgrEncrSeed5_Type = Integer32
_WfSnmpMgrEncrSeed5_Object = MibTableColumn
wfSnmpMgrEncrSeed5 = _WfSnmpMgrEncrSeed5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 11),
    _WfSnmpMgrEncrSeed5_Type()
)
wfSnmpMgrEncrSeed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrEncrSeed5.setStatus("mandatory")


class _WfSnmpMgrCircuitlessTrap_Type(Integer32):
    """Custom type wfSnmpMgrCircuitlessTrap based on Integer32"""
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


_WfSnmpMgrCircuitlessTrap_Type.__name__ = "Integer32"
_WfSnmpMgrCircuitlessTrap_Object = MibTableColumn
wfSnmpMgrCircuitlessTrap = _WfSnmpMgrCircuitlessTrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 12),
    _WfSnmpMgrCircuitlessTrap_Type()
)
wfSnmpMgrCircuitlessTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrCircuitlessTrap.setStatus("mandatory")
_WfSnmpTrapEntityTable_Object = MibTable
wfSnmpTrapEntityTable = _WfSnmpTrapEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5)
)
if mibBuilder.loadTexts:
    wfSnmpTrapEntityTable.setStatus("mandatory")
_WfSnmpTrapEntityEntry_Object = MibTableRow
wfSnmpTrapEntityEntry = _WfSnmpTrapEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1)
)
wfSnmpTrapEntityEntry.setIndexNames(
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEntityNumber"),
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEntitySlot"),
)
if mibBuilder.loadTexts:
    wfSnmpTrapEntityEntry.setStatus("mandatory")


class _WfSnmpTrapEntityDelete_Type(Integer32):
    """Custom type wfSnmpTrapEntityDelete based on Integer32"""
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


_WfSnmpTrapEntityDelete_Type.__name__ = "Integer32"
_WfSnmpTrapEntityDelete_Object = MibTableColumn
wfSnmpTrapEntityDelete = _WfSnmpTrapEntityDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 1),
    _WfSnmpTrapEntityDelete_Type()
)
wfSnmpTrapEntityDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityDelete.setStatus("mandatory")


class _WfSnmpTrapEntityDisable_Type(Integer32):
    """Custom type wfSnmpTrapEntityDisable based on Integer32"""
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


_WfSnmpTrapEntityDisable_Type.__name__ = "Integer32"
_WfSnmpTrapEntityDisable_Object = MibTableColumn
wfSnmpTrapEntityDisable = _WfSnmpTrapEntityDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 2),
    _WfSnmpTrapEntityDisable_Type()
)
wfSnmpTrapEntityDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityDisable.setStatus("mandatory")
_WfSnmpTrapEntityNumber_Type = Integer32
_WfSnmpTrapEntityNumber_Object = MibTableColumn
wfSnmpTrapEntityNumber = _WfSnmpTrapEntityNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 3),
    _WfSnmpTrapEntityNumber_Type()
)
wfSnmpTrapEntityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityNumber.setStatus("mandatory")
_WfSnmpTrapEntitySlot_Type = Integer32
_WfSnmpTrapEntitySlot_Object = MibTableColumn
wfSnmpTrapEntitySlot = _WfSnmpTrapEntitySlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 4),
    _WfSnmpTrapEntitySlot_Type()
)
wfSnmpTrapEntitySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpTrapEntitySlot.setStatus("mandatory")
_WfSnmpTrapEntityName_Type = DisplayString
_WfSnmpTrapEntityName_Object = MibTableColumn
wfSnmpTrapEntityName = _WfSnmpTrapEntityName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 5),
    _WfSnmpTrapEntityName_Type()
)
wfSnmpTrapEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityName.setStatus("mandatory")


class _WfSnmpTrapEntityFault_Type(Integer32):
    """Custom type wfSnmpTrapEntityFault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapEntityFault_Type.__name__ = "Integer32"
_WfSnmpTrapEntityFault_Object = MibTableColumn
wfSnmpTrapEntityFault = _WfSnmpTrapEntityFault_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 6),
    _WfSnmpTrapEntityFault_Type()
)
wfSnmpTrapEntityFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityFault.setStatus("mandatory")


class _WfSnmpTrapEntityWarn_Type(Integer32):
    """Custom type wfSnmpTrapEntityWarn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapEntityWarn_Type.__name__ = "Integer32"
_WfSnmpTrapEntityWarn_Object = MibTableColumn
wfSnmpTrapEntityWarn = _WfSnmpTrapEntityWarn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 7),
    _WfSnmpTrapEntityWarn_Type()
)
wfSnmpTrapEntityWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityWarn.setStatus("mandatory")


class _WfSnmpTrapEntityInfo_Type(Integer32):
    """Custom type wfSnmpTrapEntityInfo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapEntityInfo_Type.__name__ = "Integer32"
_WfSnmpTrapEntityInfo_Object = MibTableColumn
wfSnmpTrapEntityInfo = _WfSnmpTrapEntityInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 8),
    _WfSnmpTrapEntityInfo_Type()
)
wfSnmpTrapEntityInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityInfo.setStatus("mandatory")


class _WfSnmpTrapEntityTrace_Type(Integer32):
    """Custom type wfSnmpTrapEntityTrace based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapEntityTrace_Type.__name__ = "Integer32"
_WfSnmpTrapEntityTrace_Object = MibTableColumn
wfSnmpTrapEntityTrace = _WfSnmpTrapEntityTrace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 9),
    _WfSnmpTrapEntityTrace_Type()
)
wfSnmpTrapEntityTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityTrace.setStatus("mandatory")


class _WfSnmpTrapEntityDebug_Type(Integer32):
    """Custom type wfSnmpTrapEntityDebug based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapEntityDebug_Type.__name__ = "Integer32"
_WfSnmpTrapEntityDebug_Object = MibTableColumn
wfSnmpTrapEntityDebug = _WfSnmpTrapEntityDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 10),
    _WfSnmpTrapEntityDebug_Type()
)
wfSnmpTrapEntityDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEntityDebug.setStatus("mandatory")
_WfSnmpTrapEventTable_Object = MibTable
wfSnmpTrapEventTable = _WfSnmpTrapEventTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6)
)
if mibBuilder.loadTexts:
    wfSnmpTrapEventTable.setStatus("mandatory")
_WfSnmpTrapEventEntry_Object = MibTableRow
wfSnmpTrapEventEntry = _WfSnmpTrapEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1)
)
wfSnmpTrapEventEntry.setIndexNames(
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEventEntity"),
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEventNumber"),
)
if mibBuilder.loadTexts:
    wfSnmpTrapEventEntry.setStatus("mandatory")


class _WfSnmpTrapEventDelete_Type(Integer32):
    """Custom type wfSnmpTrapEventDelete based on Integer32"""
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


_WfSnmpTrapEventDelete_Type.__name__ = "Integer32"
_WfSnmpTrapEventDelete_Object = MibTableColumn
wfSnmpTrapEventDelete = _WfSnmpTrapEventDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 1),
    _WfSnmpTrapEventDelete_Type()
)
wfSnmpTrapEventDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEventDelete.setStatus("mandatory")


class _WfSnmpTrapEventDisable_Type(Integer32):
    """Custom type wfSnmpTrapEventDisable based on Integer32"""
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


_WfSnmpTrapEventDisable_Type.__name__ = "Integer32"
_WfSnmpTrapEventDisable_Object = MibTableColumn
wfSnmpTrapEventDisable = _WfSnmpTrapEventDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 2),
    _WfSnmpTrapEventDisable_Type()
)
wfSnmpTrapEventDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapEventDisable.setStatus("mandatory")
_WfSnmpTrapEventEntity_Type = Integer32
_WfSnmpTrapEventEntity_Object = MibTableColumn
wfSnmpTrapEventEntity = _WfSnmpTrapEventEntity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 3),
    _WfSnmpTrapEventEntity_Type()
)
wfSnmpTrapEventEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpTrapEventEntity.setStatus("mandatory")
_WfSnmpTrapEventNumber_Type = Integer32
_WfSnmpTrapEventNumber_Object = MibTableColumn
wfSnmpTrapEventNumber = _WfSnmpTrapEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 4),
    _WfSnmpTrapEventNumber_Type()
)
wfSnmpTrapEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpTrapEventNumber.setStatus("mandatory")
_WfSnmpTrapEventName_Type = DisplayString
_WfSnmpTrapEventName_Object = MibTableColumn
wfSnmpTrapEventName = _WfSnmpTrapEventName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 5),
    _WfSnmpTrapEventName_Type()
)
wfSnmpTrapEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpTrapEventName.setStatus("mandatory")
_WfSnmpViewTable_Object = MibTable
wfSnmpViewTable = _WfSnmpViewTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7)
)
if mibBuilder.loadTexts:
    wfSnmpViewTable.setStatus("mandatory")
_WfSnmpViewEntry_Object = MibTableRow
wfSnmpViewEntry = _WfSnmpViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1)
)
wfSnmpViewEntry.setIndexNames(
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpViewIndex"),
    (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpViewSubtree"),
)
if mibBuilder.loadTexts:
    wfSnmpViewEntry.setStatus("mandatory")


class _WfSnmpViewDelete_Type(Integer32):
    """Custom type wfSnmpViewDelete based on Integer32"""
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


_WfSnmpViewDelete_Type.__name__ = "Integer32"
_WfSnmpViewDelete_Object = MibTableColumn
wfSnmpViewDelete = _WfSnmpViewDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 1),
    _WfSnmpViewDelete_Type()
)
wfSnmpViewDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpViewDelete.setStatus("mandatory")
_WfSnmpViewIndex_Type = Integer32
_WfSnmpViewIndex_Object = MibTableColumn
wfSnmpViewIndex = _WfSnmpViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 2),
    _WfSnmpViewIndex_Type()
)
wfSnmpViewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpViewIndex.setStatus("mandatory")
_WfSnmpViewSubtree_Type = Integer32
_WfSnmpViewSubtree_Object = MibTableColumn
wfSnmpViewSubtree = _WfSnmpViewSubtree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 3),
    _WfSnmpViewSubtree_Type()
)
wfSnmpViewSubtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpViewSubtree.setStatus("mandatory")
_WfSnmpViewName_Type = DisplayString
_WfSnmpViewName_Object = MibTableColumn
wfSnmpViewName = _WfSnmpViewName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 4),
    _WfSnmpViewName_Type()
)
wfSnmpViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpViewName.setStatus("mandatory")
_WfSnmpViewTree_Type = DisplayString
_WfSnmpViewTree_Object = MibTableColumn
wfSnmpViewTree = _WfSnmpViewTree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 5),
    _WfSnmpViewTree_Type()
)
wfSnmpViewTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpViewTree.setStatus("mandatory")


class _WfSnmpViewType_Type(Integer32):
    """Custom type wfSnmpViewType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_WfSnmpViewType_Type.__name__ = "Integer32"
_WfSnmpViewType_Object = MibTableColumn
wfSnmpViewType = _WfSnmpViewType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 6),
    _WfSnmpViewType_Type()
)
wfSnmpViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpViewType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SNMPEXT-MIB",
    **{"wfSnmp": wfSnmp,
       "wfSnmpDisable": wfSnmpDisable,
       "wfSnmpUseLock": wfSnmpUseLock,
       "wfSnmpLockAddress": wfSnmpLockAddress,
       "wfSnmpLockTimeOut": wfSnmpLockTimeOut,
       "wfSnmpAuth": wfSnmpAuth,
       "wfSnmpInPkts": wfSnmpInPkts,
       "wfSnmpOutPkts": wfSnmpOutPkts,
       "wfSnmpInBadVersions": wfSnmpInBadVersions,
       "wfSnmpInBadCommunityNames": wfSnmpInBadCommunityNames,
       "wfSnmpInBadCommunityUses": wfSnmpInBadCommunityUses,
       "wfSnmpInASNParseErrs": wfSnmpInASNParseErrs,
       "wfSnmpInBadTypes": wfSnmpInBadTypes,
       "wfSnmpInTooBigs": wfSnmpInTooBigs,
       "wfSnmpInNoSuchNames": wfSnmpInNoSuchNames,
       "wfSnmpInBadValues": wfSnmpInBadValues,
       "wfSnmpInReadOnlys": wfSnmpInReadOnlys,
       "wfSnmpInGenErrs": wfSnmpInGenErrs,
       "wfSnmpInTotalReqVars": wfSnmpInTotalReqVars,
       "wfSnmpInTotalSetVars": wfSnmpInTotalSetVars,
       "wfSnmpInGetRequests": wfSnmpInGetRequests,
       "wfSnmpInGetNexts": wfSnmpInGetNexts,
       "wfSnmpInSetRequests": wfSnmpInSetRequests,
       "wfSnmpInGetResponses": wfSnmpInGetResponses,
       "wfSnmpInTraps": wfSnmpInTraps,
       "wfSnmpOutTooBigs": wfSnmpOutTooBigs,
       "wfSnmpOutNoSuchNames": wfSnmpOutNoSuchNames,
       "wfSnmpOutBadValues": wfSnmpOutBadValues,
       "wfSnmpOutReadOnlys": wfSnmpOutReadOnlys,
       "wfSnmpOutGenErrs": wfSnmpOutGenErrs,
       "wfSnmpOutGetRequests": wfSnmpOutGetRequests,
       "wfSnmpOutGetNexts": wfSnmpOutGetNexts,
       "wfSnmpOutSetRequests": wfSnmpOutSetRequests,
       "wfSnmpOutGetResponses": wfSnmpOutGetResponses,
       "wfSnmpOutTraps": wfSnmpOutTraps,
       "wfSnmpEnableAuthTraps": wfSnmpEnableAuthTraps,
       "wfSnmpTrapDebug": wfSnmpTrapDebug,
       "wfSnmpTrapTrace": wfSnmpTrapTrace,
       "wfSnmpTrapInfo": wfSnmpTrapInfo,
       "wfSnmpTrapWarn": wfSnmpTrapWarn,
       "wfSnmpTrapFault": wfSnmpTrapFault,
       "wfSnmpIpTos": wfSnmpIpTos,
       "wfSnmpPropEncryption": wfSnmpPropEncryption,
       "wfSnmpPDUThreads": wfSnmpPDUThreads,
       "wfSnmpBusyPDUThreads": wfSnmpBusyPDUThreads,
       "wfSnmpLogLevel": wfSnmpLogLevel,
       "wfSnmpDelete": wfSnmpDelete,
       "wfSnmpScopeDelimiter": wfSnmpScopeDelimiter,
       "wfSnmpMaxInPktChain": wfSnmpMaxInPktChain,
       "wfSnmpCommTable": wfSnmpCommTable,
       "wfSnmpCommEntry": wfSnmpCommEntry,
       "wfSnmpCommDelete": wfSnmpCommDelete,
       "wfSnmpCommIndex": wfSnmpCommIndex,
       "wfSnmpCommName": wfSnmpCommName,
       "wfSnmpCommAccess": wfSnmpCommAccess,
       "wfSnmpCommScopeType": wfSnmpCommScopeType,
       "wfSnmpCommViewIndex": wfSnmpCommViewIndex,
       "wfSnmpMgrTable": wfSnmpMgrTable,
       "wfSnmpMgrEntry": wfSnmpMgrEntry,
       "wfSnmpMgrDelete": wfSnmpMgrDelete,
       "wfSnmpMgrCommIndex": wfSnmpMgrCommIndex,
       "wfSnmpMgrAddress": wfSnmpMgrAddress,
       "wfSnmpMgrName": wfSnmpMgrName,
       "wfSnmpMgrTrapPort": wfSnmpMgrTrapPort,
       "wfSnmpMgrTraps": wfSnmpMgrTraps,
       "wfSnmpMgrEncrSeed1": wfSnmpMgrEncrSeed1,
       "wfSnmpMgrEncrSeed2": wfSnmpMgrEncrSeed2,
       "wfSnmpMgrEncrSeed3": wfSnmpMgrEncrSeed3,
       "wfSnmpMgrEncrSeed4": wfSnmpMgrEncrSeed4,
       "wfSnmpMgrEncrSeed5": wfSnmpMgrEncrSeed5,
       "wfSnmpMgrCircuitlessTrap": wfSnmpMgrCircuitlessTrap,
       "wfSnmpTrapEntityTable": wfSnmpTrapEntityTable,
       "wfSnmpTrapEntityEntry": wfSnmpTrapEntityEntry,
       "wfSnmpTrapEntityDelete": wfSnmpTrapEntityDelete,
       "wfSnmpTrapEntityDisable": wfSnmpTrapEntityDisable,
       "wfSnmpTrapEntityNumber": wfSnmpTrapEntityNumber,
       "wfSnmpTrapEntitySlot": wfSnmpTrapEntitySlot,
       "wfSnmpTrapEntityName": wfSnmpTrapEntityName,
       "wfSnmpTrapEntityFault": wfSnmpTrapEntityFault,
       "wfSnmpTrapEntityWarn": wfSnmpTrapEntityWarn,
       "wfSnmpTrapEntityInfo": wfSnmpTrapEntityInfo,
       "wfSnmpTrapEntityTrace": wfSnmpTrapEntityTrace,
       "wfSnmpTrapEntityDebug": wfSnmpTrapEntityDebug,
       "wfSnmpTrapEventTable": wfSnmpTrapEventTable,
       "wfSnmpTrapEventEntry": wfSnmpTrapEventEntry,
       "wfSnmpTrapEventDelete": wfSnmpTrapEventDelete,
       "wfSnmpTrapEventDisable": wfSnmpTrapEventDisable,
       "wfSnmpTrapEventEntity": wfSnmpTrapEventEntity,
       "wfSnmpTrapEventNumber": wfSnmpTrapEventNumber,
       "wfSnmpTrapEventName": wfSnmpTrapEventName,
       "wfSnmpViewTable": wfSnmpViewTable,
       "wfSnmpViewEntry": wfSnmpViewEntry,
       "wfSnmpViewDelete": wfSnmpViewDelete,
       "wfSnmpViewIndex": wfSnmpViewIndex,
       "wfSnmpViewSubtree": wfSnmpViewSubtree,
       "wfSnmpViewName": wfSnmpViewName,
       "wfSnmpViewTree": wfSnmpViewTree,
       "wfSnmpViewType": wfSnmpViewType}
)
