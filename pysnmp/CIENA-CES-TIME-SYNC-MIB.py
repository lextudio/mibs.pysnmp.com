# SNMP MIB module (CIENA-CES-TIME-SYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-TIME-SYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:07 2024
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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


# MODULE-IDENTITY

cienaCesTimeSyncMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28)
)
cienaCesTimeSyncMIB.setRevisions(
        ("2012-06-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SsmStratumLevel(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 6),
          ("dus", 15),
          ("prc", 2),
          ("prov", 16),
          ("prs", 7),
          ("sec", 5),
          ("smc", 13),
          ("ssua", 3),
          ("ssub", 4),
          ("st2", 9),
          ("st3", 12),
          ("st3e", 11),
          ("st4", 14),
          ("stu", 8),
          ("tnc", 10),
          ("unknown", 1))
    )



class SyncInterfaceProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits", 2),
          ("synce", 3),
          ("unknown", 1))
    )



class SyncBITSSignalMode(Integer32, TextualConvention):
    status = "current"
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
        *(("mode2048khz", 5),
          ("mode6312khz", 7),
          ("mode64kcc", 6),
          ("modee1", 3),
          ("modej1", 4),
          ("modet1", 2),
          ("modeunknown", 1))
    )



class SyncBITSSignalFormat(Integer32, TextualConvention):
    status = "current"
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
        *(("cas", 2),
          ("cascrc", 3),
          ("esf", 4),
          ("fas", 5),
          ("fascrc", 6),
          ("sf", 7),
          ("unknown", 1))
    )



class SyncBITSSignalEncoding(Integer32, TextualConvention):
    status = "current"
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
        *(("ami", 3),
          ("b8zs", 2),
          ("hdb3", 4),
          ("unknown", 1))
    )



class SyncRefOperationalStatus(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("alarmindicationsignal", 6),
          ("hardwarefault", 7),
          ("hardwarenotconfigured", 8),
          ("linkflap", 14),
          ("loopbackrx", 13),
          ("loopbacktx", 12),
          ("lossofframe", 5),
          ("lossofsignal", 4),
          ("notauthenticated", 11),
          ("qlbelowthreshold", 9),
          ("rxtimeout", 10),
          ("selected", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesTimeSyncMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncMIBObjects = _CienaCesTimeSyncMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1)
)
_CienaCesTimeSyncObjects_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncObjects = _CienaCesTimeSyncObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1)
)
_CienaCesSyncAdminState_Type = CienaGlobalState
_CienaCesSyncAdminState_Object = MibScalar
cienaCesSyncAdminState = _CienaCesSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 1),
    _CienaCesSyncAdminState_Type()
)
cienaCesSyncAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncAdminState.setStatus("current")


class _CienaCesSyncOptionType_Type(Integer32):
    """Custom type cienaCesSyncOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("option1", 2),
          ("option2", 3),
          ("unknown", 1))
    )


_CienaCesSyncOptionType_Type.__name__ = "Integer32"
_CienaCesSyncOptionType_Object = MibScalar
cienaCesSyncOptionType = _CienaCesSyncOptionType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 2),
    _CienaCesSyncOptionType_Type()
)
cienaCesSyncOptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncOptionType.setStatus("current")


class _CienaCesSyncRevertiveMode_Type(Integer32):
    """Custom type cienaCesSyncRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 3),
          ("revertive", 2),
          ("unknown", 1))
    )


_CienaCesSyncRevertiveMode_Type.__name__ = "Integer32"
_CienaCesSyncRevertiveMode_Object = MibScalar
cienaCesSyncRevertiveMode = _CienaCesSyncRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 3),
    _CienaCesSyncRevertiveMode_Type()
)
cienaCesSyncRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncRevertiveMode.setStatus("current")
_CienaCesSyncWaitToRestoreTimer_Type = Unsigned32
_CienaCesSyncWaitToRestoreTimer_Object = MibScalar
cienaCesSyncWaitToRestoreTimer = _CienaCesSyncWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 4),
    _CienaCesSyncWaitToRestoreTimer_Type()
)
cienaCesSyncWaitToRestoreTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncWaitToRestoreTimer.setStatus("current")
_CienaCesSyncInputProtectionGroupTable_Object = MibTable
cienaCesSyncInputProtectionGroupTable = _CienaCesSyncInputProtectionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionGroupTable.setStatus("current")
_CienaCesSyncInputProtectionGroupEntry_Object = MibTableRow
cienaCesSyncInputProtectionGroupEntry = _CienaCesSyncInputProtectionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1)
)
cienaCesSyncInputProtectionGroupEntry.setIndexNames(
    (0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGEntityId"),
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionGroupEntry.setStatus("current")


class _CienaCesInputPGEntityId_Type(Integer32):
    """Custom type cienaCesInputPGEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesInputPGEntityId_Type.__name__ = "Integer32"
_CienaCesInputPGEntityId_Object = MibTableColumn
cienaCesInputPGEntityId = _CienaCesInputPGEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 1),
    _CienaCesInputPGEntityId_Type()
)
cienaCesInputPGEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInputPGEntityId.setStatus("current")


class _CienaCesInputPGEntityName_Type(DisplayString):
    """Custom type cienaCesInputPGEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGEntityName_Type.__name__ = "DisplayString"
_CienaCesInputPGEntityName_Object = MibTableColumn
cienaCesInputPGEntityName = _CienaCesInputPGEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 2),
    _CienaCesInputPGEntityName_Type()
)
cienaCesInputPGEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGEntityName.setStatus("current")


class _CienaCesInputPGPreferredReference_Type(DisplayString):
    """Custom type cienaCesInputPGPreferredReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGPreferredReference_Type.__name__ = "DisplayString"
_CienaCesInputPGPreferredReference_Object = MibTableColumn
cienaCesInputPGPreferredReference = _CienaCesInputPGPreferredReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 3),
    _CienaCesInputPGPreferredReference_Type()
)
cienaCesInputPGPreferredReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGPreferredReference.setStatus("current")


class _CienaCesInputPGSelectedReference_Type(DisplayString):
    """Custom type cienaCesInputPGSelectedReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGSelectedReference_Type.__name__ = "DisplayString"
_CienaCesInputPGSelectedReference_Object = MibTableColumn
cienaCesInputPGSelectedReference = _CienaCesInputPGSelectedReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 4),
    _CienaCesInputPGSelectedReference_Type()
)
cienaCesInputPGSelectedReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGSelectedReference.setStatus("current")


class _CienaCesInputPGForcedReference_Type(DisplayString):
    """Custom type cienaCesInputPGForcedReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGForcedReference_Type.__name__ = "DisplayString"
_CienaCesInputPGForcedReference_Object = MibTableColumn
cienaCesInputPGForcedReference = _CienaCesInputPGForcedReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 5),
    _CienaCesInputPGForcedReference_Type()
)
cienaCesInputPGForcedReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGForcedReference.setStatus("current")
_CienaCesInputPGThresholdQualityLevel_Type = SsmStratumLevel
_CienaCesInputPGThresholdQualityLevel_Object = MibTableColumn
cienaCesInputPGThresholdQualityLevel = _CienaCesInputPGThresholdQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 6),
    _CienaCesInputPGThresholdQualityLevel_Type()
)
cienaCesInputPGThresholdQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGThresholdQualityLevel.setStatus("current")
_CienaCesInputPGState_Type = CienaGlobalState
_CienaCesInputPGState_Object = MibTableColumn
cienaCesInputPGState = _CienaCesInputPGState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 7),
    _CienaCesInputPGState_Type()
)
cienaCesInputPGState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGState.setStatus("current")


class _CienaCesInputPGStateDuration_Type(DisplayString):
    """Custom type cienaCesInputPGStateDuration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGStateDuration_Type.__name__ = "DisplayString"
_CienaCesInputPGStateDuration_Object = MibTableColumn
cienaCesInputPGStateDuration = _CienaCesInputPGStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 8),
    _CienaCesInputPGStateDuration_Type()
)
cienaCesInputPGStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGStateDuration.setStatus("current")
_CienaCesInputPGReferenceSwitchCount_Type = Unsigned32
_CienaCesInputPGReferenceSwitchCount_Object = MibTableColumn
cienaCesInputPGReferenceSwitchCount = _CienaCesInputPGReferenceSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 9),
    _CienaCesInputPGReferenceSwitchCount_Type()
)
cienaCesInputPGReferenceSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGReferenceSwitchCount.setStatus("current")


class _CienaCesInputPGOperationalStatus_Type(Integer32):
    """Custom type cienaCesInputPGOperationalStatus based on Integer32"""
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
        *(("acquiringlock", 5),
          ("freerun", 2),
          ("holdover", 3),
          ("locked", 4),
          ("unknown", 1))
    )


_CienaCesInputPGOperationalStatus_Type.__name__ = "Integer32"
_CienaCesInputPGOperationalStatus_Object = MibTableColumn
cienaCesInputPGOperationalStatus = _CienaCesInputPGOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 10),
    _CienaCesInputPGOperationalStatus_Type()
)
cienaCesInputPGOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGOperationalStatus.setStatus("current")
_CienaCesSyncInputProtectionUnitTable_Object = MibTable
cienaCesSyncInputProtectionUnitTable = _CienaCesSyncInputProtectionUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionUnitTable.setStatus("current")
_CienaCesSyncInputProtectionUnitEntry_Object = MibTableRow
cienaCesSyncInputProtectionUnitEntry = _CienaCesSyncInputProtectionUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1)
)
cienaCesSyncInputProtectionUnitEntry.setIndexNames(
    (0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUEntityId"),
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionUnitEntry.setStatus("current")


class _CienaCesInputPUEntityId_Type(Integer32):
    """Custom type cienaCesInputPUEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CienaCesInputPUEntityId_Type.__name__ = "Integer32"
_CienaCesInputPUEntityId_Object = MibTableColumn
cienaCesInputPUEntityId = _CienaCesInputPUEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 1),
    _CienaCesInputPUEntityId_Type()
)
cienaCesInputPUEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInputPUEntityId.setStatus("current")


class _CienaCesInputPUEntityName_Type(DisplayString):
    """Custom type cienaCesInputPUEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPUEntityName_Type.__name__ = "DisplayString"
_CienaCesInputPUEntityName_Object = MibTableColumn
cienaCesInputPUEntityName = _CienaCesInputPUEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 2),
    _CienaCesInputPUEntityName_Type()
)
cienaCesInputPUEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUEntityName.setStatus("current")


class _CienaCesInputPUPGEntityName_Type(DisplayString):
    """Custom type cienaCesInputPUPGEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPUPGEntityName_Type.__name__ = "DisplayString"
_CienaCesInputPUPGEntityName_Object = MibTableColumn
cienaCesInputPUPGEntityName = _CienaCesInputPUPGEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 3),
    _CienaCesInputPUPGEntityName_Type()
)
cienaCesInputPUPGEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUPGEntityName.setStatus("current")


class _CienaCesInputPUTimingInterfaceName_Type(DisplayString):
    """Custom type cienaCesInputPUTimingInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPUTimingInterfaceName_Type.__name__ = "DisplayString"
_CienaCesInputPUTimingInterfaceName_Object = MibTableColumn
cienaCesInputPUTimingInterfaceName = _CienaCesInputPUTimingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 4),
    _CienaCesInputPUTimingInterfaceName_Type()
)
cienaCesInputPUTimingInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUTimingInterfaceName.setStatus("current")
_CienaCesInputPUTimingInterfaceProtocol_Type = SyncInterfaceProtocol
_CienaCesInputPUTimingInterfaceProtocol_Object = MibTableColumn
cienaCesInputPUTimingInterfaceProtocol = _CienaCesInputPUTimingInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 5),
    _CienaCesInputPUTimingInterfaceProtocol_Type()
)
cienaCesInputPUTimingInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUTimingInterfaceProtocol.setStatus("current")
_CienaCesInputPUUserPriority_Type = Unsigned32
_CienaCesInputPUUserPriority_Object = MibTableColumn
cienaCesInputPUUserPriority = _CienaCesInputPUUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 6),
    _CienaCesInputPUUserPriority_Type()
)
cienaCesInputPUUserPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUUserPriority.setStatus("current")
_CienaCesInputPUOperationalQL_Type = SsmStratumLevel
_CienaCesInputPUOperationalQL_Object = MibTableColumn
cienaCesInputPUOperationalQL = _CienaCesInputPUOperationalQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 7),
    _CienaCesInputPUOperationalQL_Type()
)
cienaCesInputPUOperationalQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUOperationalQL.setStatus("current")
_CienaCesInputPUForcedQL_Type = SsmStratumLevel
_CienaCesInputPUForcedQL_Object = MibTableColumn
cienaCesInputPUForcedQL = _CienaCesInputPUForcedQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 8),
    _CienaCesInputPUForcedQL_Type()
)
cienaCesInputPUForcedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUForcedQL.setStatus("current")
_CienaCesInputPUReceivedQL_Type = SsmStratumLevel
_CienaCesInputPUReceivedQL_Object = MibTableColumn
cienaCesInputPUReceivedQL = _CienaCesInputPUReceivedQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 9),
    _CienaCesInputPUReceivedQL_Type()
)
cienaCesInputPUReceivedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUReceivedQL.setStatus("current")


class _CienaCesInputPUSsmEnabled_Type(Integer32):
    """Custom type cienaCesInputPUSsmEnabled based on Integer32"""
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
          ("enabled", 3),
          ("unknown", 1))
    )


_CienaCesInputPUSsmEnabled_Type.__name__ = "Integer32"
_CienaCesInputPUSsmEnabled_Object = MibTableColumn
cienaCesInputPUSsmEnabled = _CienaCesInputPUSsmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 10),
    _CienaCesInputPUSsmEnabled_Type()
)
cienaCesInputPUSsmEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUSsmEnabled.setStatus("current")
_CienaCesInputPUOperationalStatus_Type = SyncRefOperationalStatus
_CienaCesInputPUOperationalStatus_Object = MibTableColumn
cienaCesInputPUOperationalStatus = _CienaCesInputPUOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 11),
    _CienaCesInputPUOperationalStatus_Type()
)
cienaCesInputPUOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUOperationalStatus.setStatus("current")
_CienaCesInputPUBITSSignalMode_Type = SyncBITSSignalMode
_CienaCesInputPUBITSSignalMode_Object = MibTableColumn
cienaCesInputPUBITSSignalMode = _CienaCesInputPUBITSSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 12),
    _CienaCesInputPUBITSSignalMode_Type()
)
cienaCesInputPUBITSSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUBITSSignalMode.setStatus("current")
_CienaCesInputPUBITSSignalFormat_Type = SyncBITSSignalFormat
_CienaCesInputPUBITSSignalFormat_Object = MibTableColumn
cienaCesInputPUBITSSignalFormat = _CienaCesInputPUBITSSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 13),
    _CienaCesInputPUBITSSignalFormat_Type()
)
cienaCesInputPUBITSSignalFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUBITSSignalFormat.setStatus("current")
_CienaCesInputPUBITSSignalEncoding_Type = SyncBITSSignalEncoding
_CienaCesInputPUBITSSignalEncoding_Object = MibTableColumn
cienaCesInputPUBITSSignalEncoding = _CienaCesInputPUBITSSignalEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 14),
    _CienaCesInputPUBITSSignalEncoding_Type()
)
cienaCesInputPUBITSSignalEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUBITSSignalEncoding.setStatus("current")
_CienaCesSyncOutputTable_Object = MibTable
cienaCesSyncOutputTable = _CienaCesSyncOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesSyncOutputTable.setStatus("current")
_CienaCesSyncOutputEntry_Object = MibTableRow
cienaCesSyncOutputEntry = _CienaCesSyncOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1)
)
cienaCesSyncOutputEntry.setIndexNames(
    (0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesOutputEntityId"),
)
if mibBuilder.loadTexts:
    cienaCesSyncOutputEntry.setStatus("current")


class _CienaCesOutputEntityId_Type(Integer32):
    """Custom type cienaCesOutputEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CienaCesOutputEntityId_Type.__name__ = "Integer32"
_CienaCesOutputEntityId_Object = MibTableColumn
cienaCesOutputEntityId = _CienaCesOutputEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 1),
    _CienaCesOutputEntityId_Type()
)
cienaCesOutputEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOutputEntityId.setStatus("current")


class _CienaCesOutputEntityName_Type(DisplayString):
    """Custom type cienaCesOutputEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesOutputEntityName_Type.__name__ = "DisplayString"
_CienaCesOutputEntityName_Object = MibTableColumn
cienaCesOutputEntityName = _CienaCesOutputEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 2),
    _CienaCesOutputEntityName_Type()
)
cienaCesOutputEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputEntityName.setStatus("current")


class _CienaCesOutputTimingInterfaceName_Type(DisplayString):
    """Custom type cienaCesOutputTimingInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesOutputTimingInterfaceName_Type.__name__ = "DisplayString"
_CienaCesOutputTimingInterfaceName_Object = MibTableColumn
cienaCesOutputTimingInterfaceName = _CienaCesOutputTimingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 3),
    _CienaCesOutputTimingInterfaceName_Type()
)
cienaCesOutputTimingInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputTimingInterfaceName.setStatus("current")
_CienaCesOutputTimingInterfaceProtocol_Type = SyncInterfaceProtocol
_CienaCesOutputTimingInterfaceProtocol_Object = MibTableColumn
cienaCesOutputTimingInterfaceProtocol = _CienaCesOutputTimingInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 4),
    _CienaCesOutputTimingInterfaceProtocol_Type()
)
cienaCesOutputTimingInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputTimingInterfaceProtocol.setStatus("current")
_CienaCesOutputOperationalQL_Type = SsmStratumLevel
_CienaCesOutputOperationalQL_Object = MibTableColumn
cienaCesOutputOperationalQL = _CienaCesOutputOperationalQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 5),
    _CienaCesOutputOperationalQL_Type()
)
cienaCesOutputOperationalQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputOperationalQL.setStatus("current")
_CienaCesOutputOperationalStatus_Type = SyncRefOperationalStatus
_CienaCesOutputOperationalStatus_Object = MibTableColumn
cienaCesOutputOperationalStatus = _CienaCesOutputOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 6),
    _CienaCesOutputOperationalStatus_Type()
)
cienaCesOutputOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputOperationalStatus.setStatus("current")
_CienaCesOutputBITSSignalMode_Type = SyncBITSSignalMode
_CienaCesOutputBITSSignalMode_Object = MibTableColumn
cienaCesOutputBITSSignalMode = _CienaCesOutputBITSSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 7),
    _CienaCesOutputBITSSignalMode_Type()
)
cienaCesOutputBITSSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalMode.setStatus("current")
_CienaCesOutputBITSSignalFormat_Type = SyncBITSSignalFormat
_CienaCesOutputBITSSignalFormat_Object = MibTableColumn
cienaCesOutputBITSSignalFormat = _CienaCesOutputBITSSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 8),
    _CienaCesOutputBITSSignalFormat_Type()
)
cienaCesOutputBITSSignalFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalFormat.setStatus("current")
_CienaCesOutputBITSSignalEncoding_Type = SyncBITSSignalEncoding
_CienaCesOutputBITSSignalEncoding_Object = MibTableColumn
cienaCesOutputBITSSignalEncoding = _CienaCesOutputBITSSignalEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 9),
    _CienaCesOutputBITSSignalEncoding_Type()
)
cienaCesOutputBITSSignalEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalEncoding.setStatus("current")


class _CienaCesOutputBITSSignalLineBuildout_Type(Integer32):
    """Custom type cienaCesOutputBITSSignalLineBuildout based on Integer32"""
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
        *(("lbo133", 2),
          ("lbo266", 3),
          ("lbo399", 4),
          ("lbo533", 5),
          ("lbo655", 6),
          ("unknown", 1))
    )


_CienaCesOutputBITSSignalLineBuildout_Type.__name__ = "Integer32"
_CienaCesOutputBITSSignalLineBuildout_Object = MibTableColumn
cienaCesOutputBITSSignalLineBuildout = _CienaCesOutputBITSSignalLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 10),
    _CienaCesOutputBITSSignalLineBuildout_Type()
)
cienaCesOutputBITSSignalLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalLineBuildout.setStatus("current")


class _CienaCesOutputBITSSignalSsmLocation_Type(Integer32):
    """Custom type cienaCesOutputBITSSignalSsmLocation based on Integer32"""
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
        *(("sa4", 2),
          ("sa5", 3),
          ("sa6", 4),
          ("sa7", 5),
          ("unknown", 1))
    )


_CienaCesOutputBITSSignalSsmLocation_Type.__name__ = "Integer32"
_CienaCesOutputBITSSignalSsmLocation_Object = MibTableColumn
cienaCesOutputBITSSignalSsmLocation = _CienaCesOutputBITSSignalSsmLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 11),
    _CienaCesOutputBITSSignalSsmLocation_Type()
)
cienaCesOutputBITSSignalSsmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalSsmLocation.setStatus("current")
_CienaCesTimeSyncMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncMIBNotificationPrefix = _CienaCesTimeSyncMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28)
)
_CienaCesTimeSyncMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncMIBNotifications = _CienaCesTimeSyncMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0)
)

# Managed Objects groups


# Notification objects

cienaCesSyncInputPUStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0, 1)
)
cienaCesSyncInputPUStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUEntityName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUPGEntityName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUTimingInterfaceName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUTimingInterfaceProtocol"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUOperationalStatus"))
)
if mibBuilder.loadTexts:
    cienaCesSyncInputPUStateChangeNotification.setStatus(
        "current"
    )

cienaCesSyncInputProtectionGroupStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0, 2)
)
cienaCesSyncInputProtectionGroupStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGEntityName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGOperationalStatus"))
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionGroupStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-TIME-SYNC-MIB",
    **{"SsmStratumLevel": SsmStratumLevel,
       "SyncInterfaceProtocol": SyncInterfaceProtocol,
       "SyncBITSSignalMode": SyncBITSSignalMode,
       "SyncBITSSignalFormat": SyncBITSSignalFormat,
       "SyncBITSSignalEncoding": SyncBITSSignalEncoding,
       "SyncRefOperationalStatus": SyncRefOperationalStatus,
       "cienaCesTimeSyncMIB": cienaCesTimeSyncMIB,
       "cienaCesTimeSyncMIBObjects": cienaCesTimeSyncMIBObjects,
       "cienaCesTimeSyncObjects": cienaCesTimeSyncObjects,
       "cienaCesSyncAdminState": cienaCesSyncAdminState,
       "cienaCesSyncOptionType": cienaCesSyncOptionType,
       "cienaCesSyncRevertiveMode": cienaCesSyncRevertiveMode,
       "cienaCesSyncWaitToRestoreTimer": cienaCesSyncWaitToRestoreTimer,
       "cienaCesSyncInputProtectionGroupTable": cienaCesSyncInputProtectionGroupTable,
       "cienaCesSyncInputProtectionGroupEntry": cienaCesSyncInputProtectionGroupEntry,
       "cienaCesInputPGEntityId": cienaCesInputPGEntityId,
       "cienaCesInputPGEntityName": cienaCesInputPGEntityName,
       "cienaCesInputPGPreferredReference": cienaCesInputPGPreferredReference,
       "cienaCesInputPGSelectedReference": cienaCesInputPGSelectedReference,
       "cienaCesInputPGForcedReference": cienaCesInputPGForcedReference,
       "cienaCesInputPGThresholdQualityLevel": cienaCesInputPGThresholdQualityLevel,
       "cienaCesInputPGState": cienaCesInputPGState,
       "cienaCesInputPGStateDuration": cienaCesInputPGStateDuration,
       "cienaCesInputPGReferenceSwitchCount": cienaCesInputPGReferenceSwitchCount,
       "cienaCesInputPGOperationalStatus": cienaCesInputPGOperationalStatus,
       "cienaCesSyncInputProtectionUnitTable": cienaCesSyncInputProtectionUnitTable,
       "cienaCesSyncInputProtectionUnitEntry": cienaCesSyncInputProtectionUnitEntry,
       "cienaCesInputPUEntityId": cienaCesInputPUEntityId,
       "cienaCesInputPUEntityName": cienaCesInputPUEntityName,
       "cienaCesInputPUPGEntityName": cienaCesInputPUPGEntityName,
       "cienaCesInputPUTimingInterfaceName": cienaCesInputPUTimingInterfaceName,
       "cienaCesInputPUTimingInterfaceProtocol": cienaCesInputPUTimingInterfaceProtocol,
       "cienaCesInputPUUserPriority": cienaCesInputPUUserPriority,
       "cienaCesInputPUOperationalQL": cienaCesInputPUOperationalQL,
       "cienaCesInputPUForcedQL": cienaCesInputPUForcedQL,
       "cienaCesInputPUReceivedQL": cienaCesInputPUReceivedQL,
       "cienaCesInputPUSsmEnabled": cienaCesInputPUSsmEnabled,
       "cienaCesInputPUOperationalStatus": cienaCesInputPUOperationalStatus,
       "cienaCesInputPUBITSSignalMode": cienaCesInputPUBITSSignalMode,
       "cienaCesInputPUBITSSignalFormat": cienaCesInputPUBITSSignalFormat,
       "cienaCesInputPUBITSSignalEncoding": cienaCesInputPUBITSSignalEncoding,
       "cienaCesSyncOutputTable": cienaCesSyncOutputTable,
       "cienaCesSyncOutputEntry": cienaCesSyncOutputEntry,
       "cienaCesOutputEntityId": cienaCesOutputEntityId,
       "cienaCesOutputEntityName": cienaCesOutputEntityName,
       "cienaCesOutputTimingInterfaceName": cienaCesOutputTimingInterfaceName,
       "cienaCesOutputTimingInterfaceProtocol": cienaCesOutputTimingInterfaceProtocol,
       "cienaCesOutputOperationalQL": cienaCesOutputOperationalQL,
       "cienaCesOutputOperationalStatus": cienaCesOutputOperationalStatus,
       "cienaCesOutputBITSSignalMode": cienaCesOutputBITSSignalMode,
       "cienaCesOutputBITSSignalFormat": cienaCesOutputBITSSignalFormat,
       "cienaCesOutputBITSSignalEncoding": cienaCesOutputBITSSignalEncoding,
       "cienaCesOutputBITSSignalLineBuildout": cienaCesOutputBITSSignalLineBuildout,
       "cienaCesOutputBITSSignalSsmLocation": cienaCesOutputBITSSignalSsmLocation,
       "cienaCesTimeSyncMIBNotificationPrefix": cienaCesTimeSyncMIBNotificationPrefix,
       "cienaCesTimeSyncMIBNotifications": cienaCesTimeSyncMIBNotifications,
       "cienaCesSyncInputPUStateChangeNotification": cienaCesSyncInputPUStateChangeNotification,
       "cienaCesSyncInputProtectionGroupStateChangeNotification": cienaCesSyncInputProtectionGroupStateChangeNotification}
)
