# SNMP MIB module (ACC-SERVICEPROFILE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-SERVICEPROFILE
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:00 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccServiceProfile_ObjectIdentity = ObjectIdentity
accServiceProfile = _AccServiceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65)
)
_AccServiceProfileTable_Object = MibTable
accServiceProfileTable = _AccServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1)
)
if mibBuilder.loadTexts:
    accServiceProfileTable.setStatus("mandatory")
_AccServiceProfileEntry_Object = MibTableRow
accServiceProfileEntry = _AccServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1)
)
accServiceProfileEntry.setIndexNames(
    (0, "ACC-SERVICEPROFILE", "accServiceProfileName"),
)
if mibBuilder.loadTexts:
    accServiceProfileEntry.setStatus("mandatory")
_AccServiceProfileName_Type = DisplayString
_AccServiceProfileName_Object = MibTableColumn
accServiceProfileName = _AccServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 1),
    _AccServiceProfileName_Type()
)
accServiceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileName.setStatus("mandatory")


class _AccServiceProfileType_Type(Integer32):
    """Custom type accServiceProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdnr", 2),
          ("mpbr", 1))
    )


_AccServiceProfileType_Type.__name__ = "Integer32"
_AccServiceProfileType_Object = MibTableColumn
accServiceProfileType = _AccServiceProfileType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 2),
    _AccServiceProfileType_Type()
)
accServiceProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileType.setStatus("mandatory")


class _AccServiceProfileAdminState_Type(Integer32):
    """Custom type accServiceProfileAdminState based on Integer32"""
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
          ("drained", 3),
          ("enabled", 1))
    )


_AccServiceProfileAdminState_Type.__name__ = "Integer32"
_AccServiceProfileAdminState_Object = MibTableColumn
accServiceProfileAdminState = _AccServiceProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 3),
    _AccServiceProfileAdminState_Type()
)
accServiceProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileAdminState.setStatus("mandatory")


class _AccServiceProfileMsgLevel_Type(Integer32):
    """Custom type accServiceProfileMsgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccServiceProfileMsgLevel_Type.__name__ = "Integer32"
_AccServiceProfileMsgLevel_Object = MibTableColumn
accServiceProfileMsgLevel = _AccServiceProfileMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 4),
    _AccServiceProfileMsgLevel_Type()
)
accServiceProfileMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileMsgLevel.setStatus("mandatory")


class _AccServiceProfilePppDefault_Type(Integer32):
    """Custom type accServiceProfilePppDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factory", 1),
          ("override", 2))
    )


_AccServiceProfilePppDefault_Type.__name__ = "Integer32"
_AccServiceProfilePppDefault_Object = MibTableColumn
accServiceProfilePppDefault = _AccServiceProfilePppDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 5),
    _AccServiceProfilePppDefault_Type()
)
accServiceProfilePppDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfilePppDefault.setStatus("obsolete")


class _AccServiceProfileAuthMethod_Type(Integer32):
    """Custom type accServiceProfileAuthMethod based on Integer32"""
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
        *(("chap", 3),
          ("chap-or-pap", 4),
          ("login", 5),
          ("none", 1),
          ("pap", 2),
          ("token-chap", 6))
    )


_AccServiceProfileAuthMethod_Type.__name__ = "Integer32"
_AccServiceProfileAuthMethod_Object = MibTableColumn
accServiceProfileAuthMethod = _AccServiceProfileAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 6),
    _AccServiceProfileAuthMethod_Type()
)
accServiceProfileAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileAuthMethod.setStatus("mandatory")


class _AccServiceProfilePortLimit_Type(Integer32):
    """Custom type accServiceProfilePortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccServiceProfilePortLimit_Type.__name__ = "Integer32"
_AccServiceProfilePortLimit_Object = MibTableColumn
accServiceProfilePortLimit = _AccServiceProfilePortLimit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 7),
    _AccServiceProfilePortLimit_Type()
)
accServiceProfilePortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfilePortLimit.setStatus("mandatory")
_AccServiceProfileAccessPart_Type = DisplayString
_AccServiceProfileAccessPart_Object = MibTableColumn
accServiceProfileAccessPart = _AccServiceProfileAccessPart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 8),
    _AccServiceProfileAccessPart_Type()
)
accServiceProfileAccessPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileAccessPart.setStatus("mandatory")
_AccServiceProfileModemPool_Type = DisplayString
_AccServiceProfileModemPool_Object = MibTableColumn
accServiceProfileModemPool = _AccServiceProfileModemPool_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 9),
    _AccServiceProfileModemPool_Type()
)
accServiceProfileModemPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileModemPool.setStatus("mandatory")


class _AccServiceProfileEntryStatus_Type(Integer32):
    """Custom type accServiceProfileEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccServiceProfileEntryStatus_Type.__name__ = "Integer32"
_AccServiceProfileEntryStatus_Object = MibTableColumn
accServiceProfileEntryStatus = _AccServiceProfileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 10),
    _AccServiceProfileEntryStatus_Type()
)
accServiceProfileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileEntryStatus.setStatus("mandatory")
_AccServiceProfileBusyCount_Type = Gauge32
_AccServiceProfileBusyCount_Object = MibTableColumn
accServiceProfileBusyCount = _AccServiceProfileBusyCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 11),
    _AccServiceProfileBusyCount_Type()
)
accServiceProfileBusyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileBusyCount.setStatus("mandatory")
_AccServiceProfileNumAccepts_Type = Counter32
_AccServiceProfileNumAccepts_Object = MibTableColumn
accServiceProfileNumAccepts = _AccServiceProfileNumAccepts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 12),
    _AccServiceProfileNumAccepts_Type()
)
accServiceProfileNumAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileNumAccepts.setStatus("mandatory")
_AccServiceProfileNumRejects_Type = Counter32
_AccServiceProfileNumRejects_Object = MibTableColumn
accServiceProfileNumRejects = _AccServiceProfileNumRejects_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 13),
    _AccServiceProfileNumRejects_Type()
)
accServiceProfileNumRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileNumRejects.setStatus("mandatory")
_AccServiceProfileNumActive_Type = Gauge32
_AccServiceProfileNumActive_Object = MibTableColumn
accServiceProfileNumActive = _AccServiceProfileNumActive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 14),
    _AccServiceProfileNumActive_Type()
)
accServiceProfileNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileNumActive.setStatus("mandatory")


class _AccServiceProfileNumberGroup_Type(Integer32):
    """Custom type accServiceProfileNumberGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AccServiceProfileNumberGroup_Type.__name__ = "Integer32"
_AccServiceProfileNumberGroup_Object = MibTableColumn
accServiceProfileNumberGroup = _AccServiceProfileNumberGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 15),
    _AccServiceProfileNumberGroup_Type()
)
accServiceProfileNumberGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileNumberGroup.setStatus("mandatory")


class _AccServiceProfilePppMru_Type(Integer32):
    """Custom type accServiceProfilePppMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4500),
    )


_AccServiceProfilePppMru_Type.__name__ = "Integer32"
_AccServiceProfilePppMru_Object = MibTableColumn
accServiceProfilePppMru = _AccServiceProfilePppMru_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 16),
    _AccServiceProfilePppMru_Type()
)
accServiceProfilePppMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfilePppMru.setStatus("mandatory")


class _AccServiceProfileMlpppMrru_Type(Integer32):
    """Custom type accServiceProfileMlpppMrru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4500),
    )


_AccServiceProfileMlpppMrru_Type.__name__ = "Integer32"
_AccServiceProfileMlpppMrru_Object = MibTableColumn
accServiceProfileMlpppMrru = _AccServiceProfileMlpppMrru_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 17),
    _AccServiceProfileMlpppMrru_Type()
)
accServiceProfileMlpppMrru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileMlpppMrru.setStatus("mandatory")


class _AccServiceProfileMlxState_Type(Integer32):
    """Custom type accServiceProfileMlxState based on Integer32"""
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


_AccServiceProfileMlxState_Type.__name__ = "Integer32"
_AccServiceProfileMlxState_Object = MibTableColumn
accServiceProfileMlxState = _AccServiceProfileMlxState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 18),
    _AccServiceProfileMlxState_Type()
)
accServiceProfileMlxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileMlxState.setStatus("obsolete")
_AccServiceProfileWelcomeMessage_Type = DisplayString
_AccServiceProfileWelcomeMessage_Object = MibTableColumn
accServiceProfileWelcomeMessage = _AccServiceProfileWelcomeMessage_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 19),
    _AccServiceProfileWelcomeMessage_Type()
)
accServiceProfileWelcomeMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileWelcomeMessage.setStatus("mandatory")
_AccServiceProfileLoginPrompt_Type = DisplayString
_AccServiceProfileLoginPrompt_Object = MibTableColumn
accServiceProfileLoginPrompt = _AccServiceProfileLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 20),
    _AccServiceProfileLoginPrompt_Type()
)
accServiceProfileLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileLoginPrompt.setStatus("mandatory")
_AccServiceProfilePasswordPrompt_Type = DisplayString
_AccServiceProfilePasswordPrompt_Object = MibTableColumn
accServiceProfilePasswordPrompt = _AccServiceProfilePasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 21),
    _AccServiceProfilePasswordPrompt_Type()
)
accServiceProfilePasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfilePasswordPrompt.setStatus("mandatory")
_AccServiceProfileServicePrompt_Type = DisplayString
_AccServiceProfileServicePrompt_Object = MibTableColumn
accServiceProfileServicePrompt = _AccServiceProfileServicePrompt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 22),
    _AccServiceProfileServicePrompt_Type()
)
accServiceProfileServicePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileServicePrompt.setStatus("mandatory")
_AccServiceProfileLoginTimeout_Type = TimeTicks
_AccServiceProfileLoginTimeout_Object = MibTableColumn
accServiceProfileLoginTimeout = _AccServiceProfileLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 23),
    _AccServiceProfileLoginTimeout_Type()
)
accServiceProfileLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileLoginTimeout.setStatus("mandatory")


class _AccServiceProfileAuthPreference_Type(Integer32):
    """Custom type accServiceProfileAuthPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_AccServiceProfileAuthPreference_Type.__name__ = "Integer32"
_AccServiceProfileAuthPreference_Object = MibTableColumn
accServiceProfileAuthPreference = _AccServiceProfileAuthPreference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 24),
    _AccServiceProfileAuthPreference_Type()
)
accServiceProfileAuthPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileAuthPreference.setStatus("mandatory")


class _AccServiceProfileAccountingOptn_Type(Integer32):
    """Custom type accServiceProfileAccountingOptn based on Integer32"""
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


_AccServiceProfileAccountingOptn_Type.__name__ = "Integer32"
_AccServiceProfileAccountingOptn_Object = MibTableColumn
accServiceProfileAccountingOptn = _AccServiceProfileAccountingOptn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 25),
    _AccServiceProfileAccountingOptn_Type()
)
accServiceProfileAccountingOptn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileAccountingOptn.setStatus("mandatory")


class _AccServiceProfileBandwidthMgmt_Type(Integer32):
    """Custom type accServiceProfileBandwidthMgmt based on Integer32"""
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
        *(("any", 4),
          ("bacp", 1),
          ("default", 3),
          ("mlx", 2))
    )


_AccServiceProfileBandwidthMgmt_Type.__name__ = "Integer32"
_AccServiceProfileBandwidthMgmt_Object = MibTableColumn
accServiceProfileBandwidthMgmt = _AccServiceProfileBandwidthMgmt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 26),
    _AccServiceProfileBandwidthMgmt_Type()
)
accServiceProfileBandwidthMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfileBandwidthMgmt.setStatus("mandatory")


class _AccServiceProfilePppIpComp_Type(Integer32):
    """Custom type accServiceProfilePppIpComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vjhc", 2))
    )


_AccServiceProfilePppIpComp_Type.__name__ = "Integer32"
_AccServiceProfilePppIpComp_Object = MibTableColumn
accServiceProfilePppIpComp = _AccServiceProfilePppIpComp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 1, 1, 27),
    _AccServiceProfilePppIpComp_Type()
)
accServiceProfilePppIpComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accServiceProfilePppIpComp.setStatus("mandatory")
_AccServiceProfilePortTable_Object = MibTable
accServiceProfilePortTable = _AccServiceProfilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 2)
)
if mibBuilder.loadTexts:
    accServiceProfilePortTable.setStatus("mandatory")
_AccServiceProfilePortEntry_Object = MibTableRow
accServiceProfilePortEntry = _AccServiceProfilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 2, 1)
)
accServiceProfilePortEntry.setIndexNames(
    (0, "ACC-SERVICEPROFILE", "accServiceProfileIfIndex"),
)
if mibBuilder.loadTexts:
    accServiceProfilePortEntry.setStatus("mandatory")


class _AccServiceProfileIfIndex_Type(Integer32):
    """Custom type accServiceProfileIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccServiceProfileIfIndex_Type.__name__ = "Integer32"
_AccServiceProfileIfIndex_Object = MibTableColumn
accServiceProfileIfIndex = _AccServiceProfileIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 2, 1, 1),
    _AccServiceProfileIfIndex_Type()
)
accServiceProfileIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileIfIndex.setStatus("mandatory")
_AccServiceProfileConfiguredName_Type = DisplayString
_AccServiceProfileConfiguredName_Object = MibTableColumn
accServiceProfileConfiguredName = _AccServiceProfileConfiguredName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 2, 1, 2),
    _AccServiceProfileConfiguredName_Type()
)
accServiceProfileConfiguredName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileConfiguredName.setStatus("mandatory")
_AccServiceProfileActiveName_Type = DisplayString
_AccServiceProfileActiveName_Object = MibTableColumn
accServiceProfileActiveName = _AccServiceProfileActiveName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 2, 1, 3),
    _AccServiceProfileActiveName_Type()
)
accServiceProfileActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileActiveName.setStatus("mandatory")


class _AccServiceProfileActiveType_Type(Integer32):
    """Custom type accServiceProfileActiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdnr", 3),
          ("inactive", 1),
          ("mpbr", 2))
    )


_AccServiceProfileActiveType_Type.__name__ = "Integer32"
_AccServiceProfileActiveType_Object = MibTableColumn
accServiceProfileActiveType = _AccServiceProfileActiveType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 65, 2, 1, 4),
    _AccServiceProfileActiveType_Type()
)
accServiceProfileActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accServiceProfileActiveType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-SERVICEPROFILE",
    **{"accServiceProfile": accServiceProfile,
       "accServiceProfileTable": accServiceProfileTable,
       "accServiceProfileEntry": accServiceProfileEntry,
       "accServiceProfileName": accServiceProfileName,
       "accServiceProfileType": accServiceProfileType,
       "accServiceProfileAdminState": accServiceProfileAdminState,
       "accServiceProfileMsgLevel": accServiceProfileMsgLevel,
       "accServiceProfilePppDefault": accServiceProfilePppDefault,
       "accServiceProfileAuthMethod": accServiceProfileAuthMethod,
       "accServiceProfilePortLimit": accServiceProfilePortLimit,
       "accServiceProfileAccessPart": accServiceProfileAccessPart,
       "accServiceProfileModemPool": accServiceProfileModemPool,
       "accServiceProfileEntryStatus": accServiceProfileEntryStatus,
       "accServiceProfileBusyCount": accServiceProfileBusyCount,
       "accServiceProfileNumAccepts": accServiceProfileNumAccepts,
       "accServiceProfileNumRejects": accServiceProfileNumRejects,
       "accServiceProfileNumActive": accServiceProfileNumActive,
       "accServiceProfileNumberGroup": accServiceProfileNumberGroup,
       "accServiceProfilePppMru": accServiceProfilePppMru,
       "accServiceProfileMlpppMrru": accServiceProfileMlpppMrru,
       "accServiceProfileMlxState": accServiceProfileMlxState,
       "accServiceProfileWelcomeMessage": accServiceProfileWelcomeMessage,
       "accServiceProfileLoginPrompt": accServiceProfileLoginPrompt,
       "accServiceProfilePasswordPrompt": accServiceProfilePasswordPrompt,
       "accServiceProfileServicePrompt": accServiceProfileServicePrompt,
       "accServiceProfileLoginTimeout": accServiceProfileLoginTimeout,
       "accServiceProfileAuthPreference": accServiceProfileAuthPreference,
       "accServiceProfileAccountingOptn": accServiceProfileAccountingOptn,
       "accServiceProfileBandwidthMgmt": accServiceProfileBandwidthMgmt,
       "accServiceProfilePppIpComp": accServiceProfilePppIpComp,
       "accServiceProfilePortTable": accServiceProfilePortTable,
       "accServiceProfilePortEntry": accServiceProfilePortEntry,
       "accServiceProfileIfIndex": accServiceProfileIfIndex,
       "accServiceProfileConfiguredName": accServiceProfileConfiguredName,
       "accServiceProfileActiveName": accServiceProfileActiveName,
       "accServiceProfileActiveType": accServiceProfileActiveType}
)
