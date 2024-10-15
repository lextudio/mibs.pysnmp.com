# SNMP MIB module (Wellfleet-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:53 2024
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

(wfPimGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfPimGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfPim_ObjectIdentity = ObjectIdentity
wfPim = _WfPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1)
)


class _WfPimDelete_Type(Integer32):
    """Custom type wfPimDelete based on Integer32"""
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


_WfPimDelete_Type.__name__ = "Integer32"
_WfPimDelete_Object = MibScalar
wfPimDelete = _WfPimDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 1),
    _WfPimDelete_Type()
)
wfPimDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimDelete.setStatus("mandatory")


class _WfPimDisable_Type(Integer32):
    """Custom type wfPimDisable based on Integer32"""
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


_WfPimDisable_Type.__name__ = "Integer32"
_WfPimDisable_Object = MibScalar
wfPimDisable = _WfPimDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 2),
    _WfPimDisable_Type()
)
wfPimDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimDisable.setStatus("mandatory")


class _WfPimState_Type(Integer32):
    """Custom type wfPimState based on Integer32"""
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


_WfPimState_Type.__name__ = "Integer32"
_WfPimState_Object = MibScalar
wfPimState = _WfPimState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 3),
    _WfPimState_Type()
)
wfPimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimState.setStatus("mandatory")


class _WfPimInfoWarning_Type(Integer32):
    """Custom type wfPimInfoWarning based on Integer32"""
    defaultValue = 0


_WfPimInfoWarning_Object = MibScalar
wfPimInfoWarning = _WfPimInfoWarning_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 4),
    _WfPimInfoWarning_Type()
)
wfPimInfoWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimInfoWarning.setStatus("mandatory")


class _WfPimDebug_Type(Integer32):
    """Custom type wfPimDebug based on Integer32"""
    defaultValue = 0


_WfPimDebug_Object = MibScalar
wfPimDebug = _WfPimDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 5),
    _WfPimDebug_Type()
)
wfPimDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimDebug.setStatus("mandatory")


class _WfPimTrace_Type(Integer32):
    """Custom type wfPimTrace based on Integer32"""
    defaultValue = 0


_WfPimTrace_Object = MibScalar
wfPimTrace = _WfPimTrace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 6),
    _WfPimTrace_Type()
)
wfPimTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimTrace.setStatus("mandatory")
_WfPimTotalCacheEntries_Type = Integer32
_WfPimTotalCacheEntries_Object = MibScalar
wfPimTotalCacheEntries = _WfPimTotalCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 7),
    _WfPimTotalCacheEntries_Type()
)
wfPimTotalCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimTotalCacheEntries.setStatus("mandatory")


class _WfPimJoinPruneInterval_Type(Integer32):
    """Custom type wfPimJoinPruneInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 18724),
    )


_WfPimJoinPruneInterval_Type.__name__ = "Integer32"
_WfPimJoinPruneInterval_Object = MibScalar
wfPimJoinPruneInterval = _WfPimJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 8),
    _WfPimJoinPruneInterval_Type()
)
wfPimJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimJoinPruneInterval.setStatus("mandatory")


class _WfPimLastHopDataThresholdDisable_Type(Integer32):
    """Custom type wfPimLastHopDataThresholdDisable based on Integer32"""
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


_WfPimLastHopDataThresholdDisable_Type.__name__ = "Integer32"
_WfPimLastHopDataThresholdDisable_Object = MibScalar
wfPimLastHopDataThresholdDisable = _WfPimLastHopDataThresholdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 9),
    _WfPimLastHopDataThresholdDisable_Type()
)
wfPimLastHopDataThresholdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimLastHopDataThresholdDisable.setStatus("mandatory")


class _WfPimLastHopDataThreshold_Type(Integer32):
    """Custom type wfPimLastHopDataThreshold based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfPimLastHopDataThreshold_Type.__name__ = "Integer32"
_WfPimLastHopDataThreshold_Object = MibScalar
wfPimLastHopDataThreshold = _WfPimLastHopDataThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 10),
    _WfPimLastHopDataThreshold_Type()
)
wfPimLastHopDataThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimLastHopDataThreshold.setStatus("mandatory")


class _WfPimRPDataThresholdDisable_Type(Integer32):
    """Custom type wfPimRPDataThresholdDisable based on Integer32"""
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


_WfPimRPDataThresholdDisable_Type.__name__ = "Integer32"
_WfPimRPDataThresholdDisable_Object = MibScalar
wfPimRPDataThresholdDisable = _WfPimRPDataThresholdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 11),
    _WfPimRPDataThresholdDisable_Type()
)
wfPimRPDataThresholdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimRPDataThresholdDisable.setStatus("mandatory")


class _WfPimRPDataThreshold_Type(Integer32):
    """Custom type wfPimRPDataThreshold based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfPimRPDataThreshold_Type.__name__ = "Integer32"
_WfPimRPDataThreshold_Object = MibScalar
wfPimRPDataThreshold = _WfPimRPDataThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 12),
    _WfPimRPDataThreshold_Type()
)
wfPimRPDataThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimRPDataThreshold.setStatus("mandatory")


class _WfPimThresholdSampleInterval_Type(Integer32):
    """Custom type wfPimThresholdSampleInterval based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 300),
    )


_WfPimThresholdSampleInterval_Type.__name__ = "Integer32"
_WfPimThresholdSampleInterval_Object = MibScalar
wfPimThresholdSampleInterval = _WfPimThresholdSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 13),
    _WfPimThresholdSampleInterval_Type()
)
wfPimThresholdSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimThresholdSampleInterval.setStatus("mandatory")


class _WfPimPMBREnable_Type(Integer32):
    """Custom type wfPimPMBREnable based on Integer32"""
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


_WfPimPMBREnable_Type.__name__ = "Integer32"
_WfPimPMBREnable_Object = MibScalar
wfPimPMBREnable = _WfPimPMBREnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 14),
    _WfPimPMBREnable_Type()
)
wfPimPMBREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimPMBREnable.setStatus("mandatory")


class _WfPimHelloOptionGenIdDisable_Type(Integer32):
    """Custom type wfPimHelloOptionGenIdDisable based on Integer32"""
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


_WfPimHelloOptionGenIdDisable_Type.__name__ = "Integer32"
_WfPimHelloOptionGenIdDisable_Object = MibScalar
wfPimHelloOptionGenIdDisable = _WfPimHelloOptionGenIdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 15),
    _WfPimHelloOptionGenIdDisable_Type()
)
wfPimHelloOptionGenIdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimHelloOptionGenIdDisable.setStatus("mandatory")
_WfPimBSRAddress_Type = IpAddress
_WfPimBSRAddress_Object = MibScalar
wfPimBSRAddress = _WfPimBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 16),
    _WfPimBSRAddress_Type()
)
wfPimBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimBSRAddress.setStatus("mandatory")


class _WfPimBSRPriority_Type(Integer32):
    """Custom type wfPimBSRPriority based on Integer32"""
    defaultValue = 1


_WfPimBSRPriority_Object = MibScalar
wfPimBSRPriority = _WfPimBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 17),
    _WfPimBSRPriority_Type()
)
wfPimBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimBSRPriority.setStatus("mandatory")
_WfPimBSRHoldTime_Type = Integer32
_WfPimBSRHoldTime_Object = MibScalar
wfPimBSRHoldTime = _WfPimBSRHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 18),
    _WfPimBSRHoldTime_Type()
)
wfPimBSRHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimBSRHoldTime.setStatus("mandatory")


class _WfPimBSRHashMaskLen_Type(Integer32):
    """Custom type wfPimBSRHashMaskLen based on Integer32"""
    defaultValue = 30


_WfPimBSRHashMaskLen_Object = MibScalar
wfPimBSRHashMaskLen = _WfPimBSRHashMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 19),
    _WfPimBSRHashMaskLen_Type()
)
wfPimBSRHashMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimBSRHashMaskLen.setStatus("mandatory")


class _WfPimCBSREnable_Type(Integer32):
    """Custom type wfPimCBSREnable based on Integer32"""
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


_WfPimCBSREnable_Type.__name__ = "Integer32"
_WfPimCBSREnable_Object = MibScalar
wfPimCBSREnable = _WfPimCBSREnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 20),
    _WfPimCBSREnable_Type()
)
wfPimCBSREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCBSREnable.setStatus("mandatory")
_WfPimCBSRAddress_Type = IpAddress
_WfPimCBSRAddress_Object = MibScalar
wfPimCBSRAddress = _WfPimCBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 21),
    _WfPimCBSRAddress_Type()
)
wfPimCBSRAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCBSRAddress.setStatus("mandatory")


class _WfPimCBSRPriority_Type(Integer32):
    """Custom type wfPimCBSRPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfPimCBSRPriority_Type.__name__ = "Integer32"
_WfPimCBSRPriority_Object = MibScalar
wfPimCBSRPriority = _WfPimCBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 22),
    _WfPimCBSRPriority_Type()
)
wfPimCBSRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCBSRPriority.setStatus("mandatory")


class _WfPimCBSRInterval_Type(Integer32):
    """Custom type wfPimCBSRInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32757),
    )


_WfPimCBSRInterval_Type.__name__ = "Integer32"
_WfPimCBSRInterval_Object = MibScalar
wfPimCBSRInterval = _WfPimCBSRInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 23),
    _WfPimCBSRInterval_Type()
)
wfPimCBSRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCBSRInterval.setStatus("mandatory")


class _WfPimCBSRHashMaskLen_Type(Integer32):
    """Custom type wfPimCBSRHashMaskLen based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_WfPimCBSRHashMaskLen_Type.__name__ = "Integer32"
_WfPimCBSRHashMaskLen_Object = MibScalar
wfPimCBSRHashMaskLen = _WfPimCBSRHashMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 24),
    _WfPimCBSRHashMaskLen_Type()
)
wfPimCBSRHashMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCBSRHashMaskLen.setStatus("mandatory")


class _WfPimCRPEnable_Type(Integer32):
    """Custom type wfPimCRPEnable based on Integer32"""
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


_WfPimCRPEnable_Type.__name__ = "Integer32"
_WfPimCRPEnable_Object = MibScalar
wfPimCRPEnable = _WfPimCRPEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 25),
    _WfPimCRPEnable_Type()
)
wfPimCRPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCRPEnable.setStatus("mandatory")
_WfPimCRPAddress_Type = IpAddress
_WfPimCRPAddress_Object = MibScalar
wfPimCRPAddress = _WfPimCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 26),
    _WfPimCRPAddress_Type()
)
wfPimCRPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCRPAddress.setStatus("mandatory")


class _WfPimCRPPriority_Type(Integer32):
    """Custom type wfPimCRPPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfPimCRPPriority_Type.__name__ = "Integer32"
_WfPimCRPPriority_Object = MibScalar
wfPimCRPPriority = _WfPimCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 27),
    _WfPimCRPPriority_Type()
)
wfPimCRPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCRPPriority.setStatus("mandatory")
_WfPimCRPGrPrefix_Type = OctetString
_WfPimCRPGrPrefix_Object = MibScalar
wfPimCRPGrPrefix = _WfPimCRPGrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 28),
    _WfPimCRPGrPrefix_Type()
)
wfPimCRPGrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCRPGrPrefix.setStatus("mandatory")


class _WfPimCRPAdvInterval_Type(Integer32):
    """Custom type wfPimCRPAdvInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 26214),
    )


_WfPimCRPAdvInterval_Type.__name__ = "Integer32"
_WfPimCRPAdvInterval_Object = MibScalar
wfPimCRPAdvInterval = _WfPimCRPAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 29),
    _WfPimCRPAdvInterval_Type()
)
wfPimCRPAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCRPAdvInterval.setStatus("mandatory")
_WfPimCRPHoldTime_Type = Integer32
_WfPimCRPHoldTime_Object = MibScalar
wfPimCRPHoldTime = _WfPimCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 30),
    _WfPimCRPHoldTime_Type()
)
wfPimCRPHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimCRPHoldTime.setStatus("mandatory")


class _WfPimRPRcvRegisterCacheTimeout_Type(Integer32):
    """Custom type wfPimRPRcvRegisterCacheTimeout based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WfPimRPRcvRegisterCacheTimeout_Type.__name__ = "Integer32"
_WfPimRPRcvRegisterCacheTimeout_Object = MibScalar
wfPimRPRcvRegisterCacheTimeout = _WfPimRPRcvRegisterCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 31),
    _WfPimRPRcvRegisterCacheTimeout_Type()
)
wfPimRPRcvRegisterCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimRPRcvRegisterCacheTimeout.setStatus("mandatory")


class _WfPimRPRegisterDisable_Type(Integer32):
    """Custom type wfPimRPRegisterDisable based on Integer32"""
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


_WfPimRPRegisterDisable_Type.__name__ = "Integer32"
_WfPimRPRegisterDisable_Object = MibScalar
wfPimRPRegisterDisable = _WfPimRPRegisterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 32),
    _WfPimRPRegisterDisable_Type()
)
wfPimRPRegisterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimRPRegisterDisable.setStatus("mandatory")


class _WfPimRegisterSuppressTimeout_Type(Integer32):
    """Custom type wfPimRegisterSuppressTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WfPimRegisterSuppressTimeout_Type.__name__ = "Integer32"
_WfPimRegisterSuppressTimeout_Object = MibScalar
wfPimRegisterSuppressTimeout = _WfPimRegisterSuppressTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 33),
    _WfPimRegisterSuppressTimeout_Type()
)
wfPimRegisterSuppressTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimRegisterSuppressTimeout.setStatus("mandatory")


class _WfPimProbeTime_Type(Integer32):
    """Custom type wfPimProbeTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfPimProbeTime_Type.__name__ = "Integer32"
_WfPimProbeTime_Object = MibScalar
wfPimProbeTime = _WfPimProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 34),
    _WfPimProbeTime_Type()
)
wfPimProbeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimProbeTime.setStatus("mandatory")


class _WfPimCiscoCompatibilityEnable_Type(Integer32):
    """Custom type wfPimCiscoCompatibilityEnable based on Integer32"""
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


_WfPimCiscoCompatibilityEnable_Type.__name__ = "Integer32"
_WfPimCiscoCompatibilityEnable_Object = MibScalar
wfPimCiscoCompatibilityEnable = _WfPimCiscoCompatibilityEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 35),
    _WfPimCiscoCompatibilityEnable_Type()
)
wfPimCiscoCompatibilityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimCiscoCompatibilityEnable.setStatus("obsolete")


class _WfPimRfcComplianceDisable_Type(Integer32):
    """Custom type wfPimRfcComplianceDisable based on Integer32"""
    defaultValue = 0


_WfPimRfcComplianceDisable_Object = MibScalar
wfPimRfcComplianceDisable = _WfPimRfcComplianceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 1, 36),
    _WfPimRfcComplianceDisable_Type()
)
wfPimRfcComplianceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimRfcComplianceDisable.setStatus("mandatory")
_WfPimIfTable_Object = MibTable
wfPimIfTable = _WfPimIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2)
)
if mibBuilder.loadTexts:
    wfPimIfTable.setStatus("mandatory")
_WfPimIfEntry_Object = MibTableRow
wfPimIfEntry = _WfPimIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1)
)
wfPimIfEntry.setIndexNames(
    (0, "Wellfleet-PIM-MIB", "wfPimIfCct"),
)
if mibBuilder.loadTexts:
    wfPimIfEntry.setStatus("mandatory")


class _WfPimIfDelete_Type(Integer32):
    """Custom type wfPimIfDelete based on Integer32"""
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


_WfPimIfDelete_Type.__name__ = "Integer32"
_WfPimIfDelete_Object = MibTableColumn
wfPimIfDelete = _WfPimIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 1),
    _WfPimIfDelete_Type()
)
wfPimIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfDelete.setStatus("mandatory")


class _WfPimIfDisable_Type(Integer32):
    """Custom type wfPimIfDisable based on Integer32"""
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


_WfPimIfDisable_Type.__name__ = "Integer32"
_WfPimIfDisable_Object = MibTableColumn
wfPimIfDisable = _WfPimIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 2),
    _WfPimIfDisable_Type()
)
wfPimIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfDisable.setStatus("mandatory")


class _WfPimIfState_Type(Integer32):
    """Custom type wfPimIfState based on Integer32"""
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


_WfPimIfState_Type.__name__ = "Integer32"
_WfPimIfState_Object = MibTableColumn
wfPimIfState = _WfPimIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 3),
    _WfPimIfState_Type()
)
wfPimIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfState.setStatus("mandatory")
_WfPimIfCct_Type = Integer32
_WfPimIfCct_Object = MibTableColumn
wfPimIfCct = _WfPimIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 4),
    _WfPimIfCct_Type()
)
wfPimIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfCct.setStatus("mandatory")
_WfPimIfIpAddress_Type = IpAddress
_WfPimIfIpAddress_Object = MibTableColumn
wfPimIfIpAddress = _WfPimIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 5),
    _WfPimIfIpAddress_Type()
)
wfPimIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfIpAddress.setStatus("mandatory")
_WfPimIfIpMask_Type = IpAddress
_WfPimIfIpMask_Object = MibTableColumn
wfPimIfIpMask = _WfPimIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 6),
    _WfPimIfIpMask_Type()
)
wfPimIfIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfIpMask.setStatus("mandatory")


class _WfPimIfHelloInterval_Type(Integer32):
    """Custom type wfPimIfHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfPimIfHelloInterval_Type.__name__ = "Integer32"
_WfPimIfHelloInterval_Object = MibTableColumn
wfPimIfHelloInterval = _WfPimIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 7),
    _WfPimIfHelloInterval_Type()
)
wfPimIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfHelloInterval.setStatus("mandatory")


class _WfPimIfMode_Type(Integer32):
    """Custom type wfPimIfMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_WfPimIfMode_Type.__name__ = "Integer32"
_WfPimIfMode_Object = MibTableColumn
wfPimIfMode = _WfPimIfMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 8),
    _WfPimIfMode_Type()
)
wfPimIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfMode.setStatus("mandatory")


class _WfPimIfCacheTimeOut_Type(Integer32):
    """Custom type wfPimIfCacheTimeOut based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_WfPimIfCacheTimeOut_Type.__name__ = "Integer32"
_WfPimIfCacheTimeOut_Object = MibTableColumn
wfPimIfCacheTimeOut = _WfPimIfCacheTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 9),
    _WfPimIfCacheTimeOut_Type()
)
wfPimIfCacheTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfCacheTimeOut.setStatus("mandatory")


class _WfPimIfDefaultGlobalJoinPruneIntervalDisable_Type(Integer32):
    """Custom type wfPimIfDefaultGlobalJoinPruneIntervalDisable based on Integer32"""
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


_WfPimIfDefaultGlobalJoinPruneIntervalDisable_Type.__name__ = "Integer32"
_WfPimIfDefaultGlobalJoinPruneIntervalDisable_Object = MibTableColumn
wfPimIfDefaultGlobalJoinPruneIntervalDisable = _WfPimIfDefaultGlobalJoinPruneIntervalDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 10),
    _WfPimIfDefaultGlobalJoinPruneIntervalDisable_Type()
)
wfPimIfDefaultGlobalJoinPruneIntervalDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfDefaultGlobalJoinPruneIntervalDisable.setStatus("mandatory")


class _WfPimIfJoinPruneInterval_Type(Integer32):
    """Custom type wfPimIfJoinPruneInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 18724),
    )


_WfPimIfJoinPruneInterval_Type.__name__ = "Integer32"
_WfPimIfJoinPruneInterval_Object = MibTableColumn
wfPimIfJoinPruneInterval = _WfPimIfJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 11),
    _WfPimIfJoinPruneInterval_Type()
)
wfPimIfJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfJoinPruneInterval.setStatus("mandatory")


class _WfPimIfDownstreamIgmpRelayEnable_Type(Integer32):
    """Custom type wfPimIfDownstreamIgmpRelayEnable based on Integer32"""
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


_WfPimIfDownstreamIgmpRelayEnable_Type.__name__ = "Integer32"
_WfPimIfDownstreamIgmpRelayEnable_Object = MibTableColumn
wfPimIfDownstreamIgmpRelayEnable = _WfPimIfDownstreamIgmpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 12),
    _WfPimIfDownstreamIgmpRelayEnable_Type()
)
wfPimIfDownstreamIgmpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfDownstreamIgmpRelayEnable.setStatus("mandatory")


class _WfPimIfLocalDRPriority_Type(Integer32):
    """Custom type wfPimIfLocalDRPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfPimIfLocalDRPriority_Type.__name__ = "Integer32"
_WfPimIfLocalDRPriority_Object = MibTableColumn
wfPimIfLocalDRPriority = _WfPimIfLocalDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 13),
    _WfPimIfLocalDRPriority_Type()
)
wfPimIfLocalDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfLocalDRPriority.setStatus("mandatory")
_WfPimIfDR_Type = IpAddress
_WfPimIfDR_Object = MibTableColumn
wfPimIfDR = _WfPimIfDR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 14),
    _WfPimIfDR_Type()
)
wfPimIfDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfDR.setStatus("mandatory")


class _WfPimIfDRPriority_Type(Integer32):
    """Custom type wfPimIfDRPriority based on Integer32"""
    defaultValue = 1


_WfPimIfDRPriority_Object = MibTableColumn
wfPimIfDRPriority = _WfPimIfDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 15),
    _WfPimIfDRPriority_Type()
)
wfPimIfDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfDRPriority.setStatus("mandatory")
_WfPimIfInHellos_Type = Integer32
_WfPimIfInHellos_Object = MibTableColumn
wfPimIfInHellos = _WfPimIfInHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 16),
    _WfPimIfInHellos_Type()
)
wfPimIfInHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInHellos.setStatus("mandatory")
_WfPimIfOutHellos_Type = Integer32
_WfPimIfOutHellos_Object = MibTableColumn
wfPimIfOutHellos = _WfPimIfOutHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 17),
    _WfPimIfOutHellos_Type()
)
wfPimIfOutHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutHellos.setStatus("mandatory")
_WfPimIfInPrunes_Type = Integer32
_WfPimIfInPrunes_Object = MibTableColumn
wfPimIfInPrunes = _WfPimIfInPrunes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 18),
    _WfPimIfInPrunes_Type()
)
wfPimIfInPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInPrunes.setStatus("mandatory")
_WfPimIfOutPrunes_Type = Integer32
_WfPimIfOutPrunes_Object = MibTableColumn
wfPimIfOutPrunes = _WfPimIfOutPrunes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 19),
    _WfPimIfOutPrunes_Type()
)
wfPimIfOutPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutPrunes.setStatus("mandatory")
_WfPimIfInGrafts_Type = Integer32
_WfPimIfInGrafts_Object = MibTableColumn
wfPimIfInGrafts = _WfPimIfInGrafts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 20),
    _WfPimIfInGrafts_Type()
)
wfPimIfInGrafts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInGrafts.setStatus("mandatory")
_WfPimIfOutGrafts_Type = Integer32
_WfPimIfOutGrafts_Object = MibTableColumn
wfPimIfOutGrafts = _WfPimIfOutGrafts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 21),
    _WfPimIfOutGrafts_Type()
)
wfPimIfOutGrafts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutGrafts.setStatus("mandatory")
_WfPimIfInCRPAdvs_Type = Integer32
_WfPimIfInCRPAdvs_Object = MibTableColumn
wfPimIfInCRPAdvs = _WfPimIfInCRPAdvs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 22),
    _WfPimIfInCRPAdvs_Type()
)
wfPimIfInCRPAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInCRPAdvs.setStatus("mandatory")
_WfPimIfOutCRPAdvs_Type = Integer32
_WfPimIfOutCRPAdvs_Object = MibTableColumn
wfPimIfOutCRPAdvs = _WfPimIfOutCRPAdvs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 23),
    _WfPimIfOutCRPAdvs_Type()
)
wfPimIfOutCRPAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutCRPAdvs.setStatus("mandatory")
_WfPimIfInRPSets_Type = Integer32
_WfPimIfInRPSets_Object = MibTableColumn
wfPimIfInRPSets = _WfPimIfInRPSets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 24),
    _WfPimIfInRPSets_Type()
)
wfPimIfInRPSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInRPSets.setStatus("mandatory")
_WfPimIfOutRPSets_Type = Integer32
_WfPimIfOutRPSets_Object = MibTableColumn
wfPimIfOutRPSets = _WfPimIfOutRPSets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 25),
    _WfPimIfOutRPSets_Type()
)
wfPimIfOutRPSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutRPSets.setStatus("mandatory")
_WfPimIfInRegisters_Type = Integer32
_WfPimIfInRegisters_Object = MibTableColumn
wfPimIfInRegisters = _WfPimIfInRegisters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 26),
    _WfPimIfInRegisters_Type()
)
wfPimIfInRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInRegisters.setStatus("mandatory")
_WfPimIfOutRegisters_Type = Integer32
_WfPimIfOutRegisters_Object = MibTableColumn
wfPimIfOutRegisters = _WfPimIfOutRegisters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 27),
    _WfPimIfOutRegisters_Type()
)
wfPimIfOutRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutRegisters.setStatus("mandatory")
_WfPimIfInRegStop_Type = Integer32
_WfPimIfInRegStop_Object = MibTableColumn
wfPimIfInRegStop = _WfPimIfInRegStop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 28),
    _WfPimIfInRegStop_Type()
)
wfPimIfInRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInRegStop.setStatus("mandatory")
_WfPimIfOutRegStop_Type = Integer32
_WfPimIfOutRegStop_Object = MibTableColumn
wfPimIfOutRegStop = _WfPimIfOutRegStop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 29),
    _WfPimIfOutRegStop_Type()
)
wfPimIfOutRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutRegStop.setStatus("mandatory")
_WfPimIfInJoinPrunes_Type = Integer32
_WfPimIfInJoinPrunes_Object = MibTableColumn
wfPimIfInJoinPrunes = _WfPimIfInJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 30),
    _WfPimIfInJoinPrunes_Type()
)
wfPimIfInJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfInJoinPrunes.setStatus("mandatory")
_WfPimIfOutJoinPrunes_Type = Integer32
_WfPimIfOutJoinPrunes_Object = MibTableColumn
wfPimIfOutJoinPrunes = _WfPimIfOutJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 31),
    _WfPimIfOutJoinPrunes_Type()
)
wfPimIfOutJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimIfOutJoinPrunes.setStatus("mandatory")


class _WfPimIfBootstrapBorder_Type(Integer32):
    """Custom type wfPimIfBootstrapBorder based on Integer32"""
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


_WfPimIfBootstrapBorder_Type.__name__ = "Integer32"
_WfPimIfBootstrapBorder_Object = MibTableColumn
wfPimIfBootstrapBorder = _WfPimIfBootstrapBorder_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 2, 1, 32),
    _WfPimIfBootstrapBorder_Type()
)
wfPimIfBootstrapBorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimIfBootstrapBorder.setStatus("mandatory")
_WfPimNeighborTable_Object = MibTable
wfPimNeighborTable = _WfPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3)
)
if mibBuilder.loadTexts:
    wfPimNeighborTable.setStatus("mandatory")
_WfPimNeighborEntry_Object = MibTableRow
wfPimNeighborEntry = _WfPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3, 1)
)
wfPimNeighborEntry.setIndexNames(
    (0, "Wellfleet-PIM-MIB", "wfPimNeighborAddress"),
)
if mibBuilder.loadTexts:
    wfPimNeighborEntry.setStatus("mandatory")
_WfPimNeighborAddress_Type = IpAddress
_WfPimNeighborAddress_Object = MibTableColumn
wfPimNeighborAddress = _WfPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3, 1, 1),
    _WfPimNeighborAddress_Type()
)
wfPimNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimNeighborAddress.setStatus("mandatory")
_WfPimNeighborCct_Type = Integer32
_WfPimNeighborCct_Object = MibTableColumn
wfPimNeighborCct = _WfPimNeighborCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3, 1, 2),
    _WfPimNeighborCct_Type()
)
wfPimNeighborCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimNeighborCct.setStatus("mandatory")
_WfPimNeighborUpTime_Type = Integer32
_WfPimNeighborUpTime_Object = MibTableColumn
wfPimNeighborUpTime = _WfPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3, 1, 3),
    _WfPimNeighborUpTime_Type()
)
wfPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimNeighborUpTime.setStatus("mandatory")
_WfPimNeighborExpiryTime_Type = Integer32
_WfPimNeighborExpiryTime_Object = MibTableColumn
wfPimNeighborExpiryTime = _WfPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3, 1, 4),
    _WfPimNeighborExpiryTime_Type()
)
wfPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimNeighborExpiryTime.setStatus("mandatory")
_WfPimNeighboringRouterGenId_Type = Integer32
_WfPimNeighboringRouterGenId_Object = MibTableColumn
wfPimNeighboringRouterGenId = _WfPimNeighboringRouterGenId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3, 1, 5),
    _WfPimNeighboringRouterGenId_Type()
)
wfPimNeighboringRouterGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimNeighboringRouterGenId.setStatus("mandatory")
_WfPimNeighboringRouterDRPriority_Type = Integer32
_WfPimNeighboringRouterDRPriority_Object = MibTableColumn
wfPimNeighboringRouterDRPriority = _WfPimNeighboringRouterDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14, 3, 1, 6),
    _WfPimNeighboringRouterDRPriority_Type()
)
wfPimNeighboringRouterDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPimNeighboringRouterDRPriority.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-PIM-MIB",
    **{"wfPim": wfPim,
       "wfPimDelete": wfPimDelete,
       "wfPimDisable": wfPimDisable,
       "wfPimState": wfPimState,
       "wfPimInfoWarning": wfPimInfoWarning,
       "wfPimDebug": wfPimDebug,
       "wfPimTrace": wfPimTrace,
       "wfPimTotalCacheEntries": wfPimTotalCacheEntries,
       "wfPimJoinPruneInterval": wfPimJoinPruneInterval,
       "wfPimLastHopDataThresholdDisable": wfPimLastHopDataThresholdDisable,
       "wfPimLastHopDataThreshold": wfPimLastHopDataThreshold,
       "wfPimRPDataThresholdDisable": wfPimRPDataThresholdDisable,
       "wfPimRPDataThreshold": wfPimRPDataThreshold,
       "wfPimThresholdSampleInterval": wfPimThresholdSampleInterval,
       "wfPimPMBREnable": wfPimPMBREnable,
       "wfPimHelloOptionGenIdDisable": wfPimHelloOptionGenIdDisable,
       "wfPimBSRAddress": wfPimBSRAddress,
       "wfPimBSRPriority": wfPimBSRPriority,
       "wfPimBSRHoldTime": wfPimBSRHoldTime,
       "wfPimBSRHashMaskLen": wfPimBSRHashMaskLen,
       "wfPimCBSREnable": wfPimCBSREnable,
       "wfPimCBSRAddress": wfPimCBSRAddress,
       "wfPimCBSRPriority": wfPimCBSRPriority,
       "wfPimCBSRInterval": wfPimCBSRInterval,
       "wfPimCBSRHashMaskLen": wfPimCBSRHashMaskLen,
       "wfPimCRPEnable": wfPimCRPEnable,
       "wfPimCRPAddress": wfPimCRPAddress,
       "wfPimCRPPriority": wfPimCRPPriority,
       "wfPimCRPGrPrefix": wfPimCRPGrPrefix,
       "wfPimCRPAdvInterval": wfPimCRPAdvInterval,
       "wfPimCRPHoldTime": wfPimCRPHoldTime,
       "wfPimRPRcvRegisterCacheTimeout": wfPimRPRcvRegisterCacheTimeout,
       "wfPimRPRegisterDisable": wfPimRPRegisterDisable,
       "wfPimRegisterSuppressTimeout": wfPimRegisterSuppressTimeout,
       "wfPimProbeTime": wfPimProbeTime,
       "wfPimCiscoCompatibilityEnable": wfPimCiscoCompatibilityEnable,
       "wfPimRfcComplianceDisable": wfPimRfcComplianceDisable,
       "wfPimIfTable": wfPimIfTable,
       "wfPimIfEntry": wfPimIfEntry,
       "wfPimIfDelete": wfPimIfDelete,
       "wfPimIfDisable": wfPimIfDisable,
       "wfPimIfState": wfPimIfState,
       "wfPimIfCct": wfPimIfCct,
       "wfPimIfIpAddress": wfPimIfIpAddress,
       "wfPimIfIpMask": wfPimIfIpMask,
       "wfPimIfHelloInterval": wfPimIfHelloInterval,
       "wfPimIfMode": wfPimIfMode,
       "wfPimIfCacheTimeOut": wfPimIfCacheTimeOut,
       "wfPimIfDefaultGlobalJoinPruneIntervalDisable": wfPimIfDefaultGlobalJoinPruneIntervalDisable,
       "wfPimIfJoinPruneInterval": wfPimIfJoinPruneInterval,
       "wfPimIfDownstreamIgmpRelayEnable": wfPimIfDownstreamIgmpRelayEnable,
       "wfPimIfLocalDRPriority": wfPimIfLocalDRPriority,
       "wfPimIfDR": wfPimIfDR,
       "wfPimIfDRPriority": wfPimIfDRPriority,
       "wfPimIfInHellos": wfPimIfInHellos,
       "wfPimIfOutHellos": wfPimIfOutHellos,
       "wfPimIfInPrunes": wfPimIfInPrunes,
       "wfPimIfOutPrunes": wfPimIfOutPrunes,
       "wfPimIfInGrafts": wfPimIfInGrafts,
       "wfPimIfOutGrafts": wfPimIfOutGrafts,
       "wfPimIfInCRPAdvs": wfPimIfInCRPAdvs,
       "wfPimIfOutCRPAdvs": wfPimIfOutCRPAdvs,
       "wfPimIfInRPSets": wfPimIfInRPSets,
       "wfPimIfOutRPSets": wfPimIfOutRPSets,
       "wfPimIfInRegisters": wfPimIfInRegisters,
       "wfPimIfOutRegisters": wfPimIfOutRegisters,
       "wfPimIfInRegStop": wfPimIfInRegStop,
       "wfPimIfOutRegStop": wfPimIfOutRegStop,
       "wfPimIfInJoinPrunes": wfPimIfInJoinPrunes,
       "wfPimIfOutJoinPrunes": wfPimIfOutJoinPrunes,
       "wfPimIfBootstrapBorder": wfPimIfBootstrapBorder,
       "wfPimNeighborTable": wfPimNeighborTable,
       "wfPimNeighborEntry": wfPimNeighborEntry,
       "wfPimNeighborAddress": wfPimNeighborAddress,
       "wfPimNeighborCct": wfPimNeighborCct,
       "wfPimNeighborUpTime": wfPimNeighborUpTime,
       "wfPimNeighborExpiryTime": wfPimNeighborExpiryTime,
       "wfPimNeighboringRouterGenId": wfPimNeighboringRouterGenId,
       "wfPimNeighboringRouterDRPriority": wfPimNeighboringRouterDRPriority}
)
