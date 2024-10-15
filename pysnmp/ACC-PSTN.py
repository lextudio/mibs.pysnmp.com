# SNMP MIB module (ACC-PSTN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-PSTN
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:49 2024
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
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_AccPstn_ObjectIdentity = ObjectIdentity
accPstn = _AccPstn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69)
)
_AccPstnSubTable_Object = MibTable
accPstnSubTable = _AccPstnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1)
)
if mibBuilder.loadTexts:
    accPstnSubTable.setStatus("mandatory")
_AccPstnSubTabEntry_Object = MibTableRow
accPstnSubTabEntry = _AccPstnSubTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1)
)
accPstnSubTabEntry.setIndexNames(
    (0, "ACC-PSTN", "oPstnSubTabDslIndex"),
)
if mibBuilder.loadTexts:
    accPstnSubTabEntry.setStatus("mandatory")
_OPstnSubTabDslIndex_Type = Integer32
_OPstnSubTabDslIndex_Object = MibTableColumn
oPstnSubTabDslIndex = _OPstnSubTabDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 1),
    _OPstnSubTabDslIndex_Type()
)
oPstnSubTabDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnSubTabDslIndex.setStatus("mandatory")


class _OPstnSubTabSigSystem_Type(Integer32):
    """Custom type oPstnSubTabSigSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p7", 2),
          ("r2", 3),
          ("rbs", 1))
    )


_OPstnSubTabSigSystem_Type.__name__ = "Integer32"
_OPstnSubTabSigSystem_Object = MibTableColumn
oPstnSubTabSigSystem = _OPstnSubTabSigSystem_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 2),
    _OPstnSubTabSigSystem_Type()
)
oPstnSubTabSigSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnSubTabSigSystem.setStatus("mandatory")
_OPstnSubTabNumChannels_Type = Integer32
_OPstnSubTabNumChannels_Object = MibTableColumn
oPstnSubTabNumChannels = _OPstnSubTabNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 3),
    _OPstnSubTabNumChannels_Type()
)
oPstnSubTabNumChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnSubTabNumChannels.setStatus("mandatory")


class _OPstnSubTabAdminStatus_Type(Integer32):
    """Custom type oPstnSubTabAdminStatus based on Integer32"""
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


_OPstnSubTabAdminStatus_Type.__name__ = "Integer32"
_OPstnSubTabAdminStatus_Object = MibTableColumn
oPstnSubTabAdminStatus = _OPstnSubTabAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 4),
    _OPstnSubTabAdminStatus_Type()
)
oPstnSubTabAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnSubTabAdminStatus.setStatus("mandatory")


class _OPstnSubTabOperStatus_Type(Integer32):
    """Custom type oPstnSubTabOperStatus based on Integer32"""
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
        *(("cfgpend", 4),
          ("offline", 1),
          ("online", 7),
          ("regpend", 2),
          ("starting", 5),
          ("stopping", 6),
          ("unrpend", 3))
    )


_OPstnSubTabOperStatus_Type.__name__ = "Integer32"
_OPstnSubTabOperStatus_Object = MibTableColumn
oPstnSubTabOperStatus = _OPstnSubTabOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 5),
    _OPstnSubTabOperStatus_Type()
)
oPstnSubTabOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnSubTabOperStatus.setStatus("mandatory")
_OPstnSubTabMsgLevel_Type = Integer32
_OPstnSubTabMsgLevel_Object = MibTableColumn
oPstnSubTabMsgLevel = _OPstnSubTabMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 6),
    _OPstnSubTabMsgLevel_Type()
)
oPstnSubTabMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnSubTabMsgLevel.setStatus("mandatory")


class _OPstnSubTabLastCause_Type(Integer32):
    """Custom type oPstnSubTabLastCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7,
              16,
              17,
              18,
              19,
              21,
              22,
              26,
              27,
              28,
              29,
              30,
              31,
              34,
              38,
              41,
              42,
              43,
              44,
              45,
              47,
              49,
              50,
              52,
              54,
              57,
              58,
              63,
              65,
              66,
              69,
              70,
              79,
              81,
              82,
              83,
              84,
              85,
              86,
              88,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("access-information-discarded", 43),
          ("bearer-capability-not-authorized", 57),
          ("bearer-capability-not-available", 58),
          ("bearer-capability-not-implemented", 65),
          ("call-awarded-being-delivered", 7),
          ("call-identity-in-use", 84),
          ("call-identity-non-existent", 83),
          ("call-rejected", 21),
          ("channel-does-not-exist", 82),
          ("channel-not-implemented", 66),
          ("channel-unacceptable", 6),
          ("ciruit-or-channel-preempted", 45),
          ("destination-out-of-order", 27),
          ("facility-not-implemented", 69),
          ("facility-not-subscribed", 50),
          ("facility-rejected", 29),
          ("incoming-call-barred", 54),
          ("incompatible-destination", 88),
          ("incompatible-or-nonexistent-message", 98),
          ("information-element-length-error", 103),
          ("information-element-not-implemented", 99),
          ("interworking-unspecified", 127),
          ("invalid-call-reference", 81),
          ("invalid-information-element-contents", 100),
          ("invalid-message-unspecified", 95),
          ("invalid-number-format", 28),
          ("invalid-transit-network", 91),
          ("manditory-information-element-missing", 96),
          ("message-incompatible-with-call-state", 101),
          ("message-nonexistent-or-not-implemented", 97),
          ("network-congestion", 42),
          ("network-out-of-order", 38),
          ("no-call-suspended", 85),
          ("no-circuit-or-channel-available", 34),
          ("no-error", 0),
          ("no-route-to-destination", 3),
          ("no-route-to-transit-network", 2),
          ("no-user-responding", 18),
          ("non-selected-user-clearing", 26),
          ("normal-call-clearing", 16),
          ("normal-clearing-unspecified", 31),
          ("number-changed", 22),
          ("outgoing-call-barred", 52),
          ("protocol-error-unspecified", 111),
          ("quality-of-service-unavailable", 49),
          ("requested-channel-not-available", 44),
          ("resources-unavailable", 47),
          ("response-to-status-enquiry", 30),
          ("restricted-digital-information-only", 70),
          ("service-not-available", 63),
          ("service-not-implemented", 79),
          ("suspended-call-cleared", 86),
          ("temporary-failure", 41),
          ("timer-expiration", 102),
          ("unassigned-number", 1),
          ("user-alerted-no-answer", 19),
          ("user-busy", 17))
    )


_OPstnSubTabLastCause_Type.__name__ = "Integer32"
_OPstnSubTabLastCause_Object = MibTableColumn
oPstnSubTabLastCause = _OPstnSubTabLastCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 7),
    _OPstnSubTabLastCause_Type()
)
oPstnSubTabLastCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnSubTabLastCause.setStatus("mandatory")
_OPstnSubTabNumberGroup_Type = Integer32
_OPstnSubTabNumberGroup_Object = MibTableColumn
oPstnSubTabNumberGroup = _OPstnSubTabNumberGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 1, 1, 8),
    _OPstnSubTabNumberGroup_Type()
)
oPstnSubTabNumberGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnSubTabNumberGroup.setStatus("mandatory")
_AccPstnStatTable_Object = MibTable
accPstnStatTable = _AccPstnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2)
)
if mibBuilder.loadTexts:
    accPstnStatTable.setStatus("mandatory")
_AccPstnStatEntry_Object = MibTableRow
accPstnStatEntry = _AccPstnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1)
)
accPstnStatEntry.setIndexNames(
    (0, "ACC-PSTN", "oPstnStatDslIndex"),
)
if mibBuilder.loadTexts:
    accPstnStatEntry.setStatus("mandatory")
_OPstnStatDslIndex_Type = Integer32
_OPstnStatDslIndex_Object = MibTableColumn
oPstnStatDslIndex = _OPstnStatDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1, 1),
    _OPstnStatDslIndex_Type()
)
oPstnStatDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnStatDslIndex.setStatus("mandatory")
_OPstnStatCallsOriginated_Type = Counter32
_OPstnStatCallsOriginated_Object = MibTableColumn
oPstnStatCallsOriginated = _OPstnStatCallsOriginated_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1, 2),
    _OPstnStatCallsOriginated_Type()
)
oPstnStatCallsOriginated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnStatCallsOriginated.setStatus("mandatory")
_OPstnStatCallsOfferred_Type = Counter32
_OPstnStatCallsOfferred_Object = MibTableColumn
oPstnStatCallsOfferred = _OPstnStatCallsOfferred_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1, 3),
    _OPstnStatCallsOfferred_Type()
)
oPstnStatCallsOfferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnStatCallsOfferred.setStatus("mandatory")
_OPstnStatCallsRouted_Type = Counter32
_OPstnStatCallsRouted_Object = MibTableColumn
oPstnStatCallsRouted = _OPstnStatCallsRouted_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1, 4),
    _OPstnStatCallsRouted_Type()
)
oPstnStatCallsRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnStatCallsRouted.setStatus("mandatory")
_OPstnStatCallsAccepted_Type = Counter32
_OPstnStatCallsAccepted_Object = MibTableColumn
oPstnStatCallsAccepted = _OPstnStatCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1, 5),
    _OPstnStatCallsAccepted_Type()
)
oPstnStatCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnStatCallsAccepted.setStatus("mandatory")
_OPstnStatCallsCompleted_Type = Counter32
_OPstnStatCallsCompleted_Object = MibTableColumn
oPstnStatCallsCompleted = _OPstnStatCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1, 6),
    _OPstnStatCallsCompleted_Type()
)
oPstnStatCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnStatCallsCompleted.setStatus("mandatory")
_OPstnStatCallsCleared_Type = Counter32
_OPstnStatCallsCleared_Object = MibTableColumn
oPstnStatCallsCleared = _OPstnStatCallsCleared_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 2, 1, 7),
    _OPstnStatCallsCleared_Type()
)
oPstnStatCallsCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnStatCallsCleared.setStatus("mandatory")
_AccPstnCallTable_Object = MibTable
accPstnCallTable = _AccPstnCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3)
)
if mibBuilder.loadTexts:
    accPstnCallTable.setStatus("mandatory")
_AccPstnCallTableEntry_Object = MibTableRow
accPstnCallTableEntry = _AccPstnCallTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1)
)
accPstnCallTableEntry.setIndexNames(
    (0, "ACC-PSTN", "oPstnCallTabDslIndex"),
)
if mibBuilder.loadTexts:
    accPstnCallTableEntry.setStatus("mandatory")
_OPstnCallTabDslIndex_Type = Integer32
_OPstnCallTabDslIndex_Object = MibTableColumn
oPstnCallTabDslIndex = _OPstnCallTabDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 1),
    _OPstnCallTabDslIndex_Type()
)
oPstnCallTabDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabDslIndex.setStatus("mandatory")
_OPstnCallTabCallId_Type = Integer32
_OPstnCallTabCallId_Object = MibTableColumn
oPstnCallTabCallId = _OPstnCallTabCallId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 2),
    _OPstnCallTabCallId_Type()
)
oPstnCallTabCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabCallId.setStatus("mandatory")


class _OPstnCallTabOrigin_Type(Integer32):
    """Custom type oPstnCallTabOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("none", 1),
          ("outgoing", 3))
    )


_OPstnCallTabOrigin_Type.__name__ = "Integer32"
_OPstnCallTabOrigin_Object = MibTableColumn
oPstnCallTabOrigin = _OPstnCallTabOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 3),
    _OPstnCallTabOrigin_Type()
)
oPstnCallTabOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabOrigin.setStatus("mandatory")
_OPstnCallTabChannel_Type = Integer32
_OPstnCallTabChannel_Object = MibTableColumn
oPstnCallTabChannel = _OPstnCallTabChannel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 4),
    _OPstnCallTabChannel_Type()
)
oPstnCallTabChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabChannel.setStatus("mandatory")
_OPstnCallTabEndpoint_Type = Integer32
_OPstnCallTabEndpoint_Object = MibTableColumn
oPstnCallTabEndpoint = _OPstnCallTabEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 5),
    _OPstnCallTabEndpoint_Type()
)
oPstnCallTabEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabEndpoint.setStatus("mandatory")


class _OPstnCallTabState_Type(Integer32):
    """Custom type oPstnCallTabState based on Integer32"""
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
        *(("answered", 12),
          ("busy", 14),
          ("clearing", 8),
          ("connected", 6),
          ("delivered", 11),
          ("idle", 1),
          ("initiated", 3),
          ("offered", 2),
          ("proceeding", 5),
          ("receiving", 13),
          ("releasing", 7),
          ("ringing", 10),
          ("routing", 9),
          ("sending", 4))
    )


_OPstnCallTabState_Type.__name__ = "Integer32"
_OPstnCallTabState_Object = MibTableColumn
oPstnCallTabState = _OPstnCallTabState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 6),
    _OPstnCallTabState_Type()
)
oPstnCallTabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabState.setStatus("mandatory")


class _OPstnCallTabCause_Type(Integer32):
    """Custom type oPstnCallTabCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7,
              16,
              17,
              18,
              19,
              21,
              22,
              26,
              27,
              28,
              29,
              30,
              31,
              34,
              38,
              41,
              42,
              43,
              44,
              45,
              47,
              49,
              50,
              52,
              54,
              57,
              58,
              63,
              65,
              66,
              69,
              70,
              79,
              81,
              82,
              83,
              84,
              85,
              86,
              88,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("access-information-discarded", 43),
          ("bearer-capability-not-authorized", 57),
          ("bearer-capability-not-available", 58),
          ("bearer-capability-not-implemented", 65),
          ("call-awarded-being-delivered", 7),
          ("call-identity-in-use", 84),
          ("call-identity-non-existent", 83),
          ("call-rejected", 21),
          ("channel-does-not-exist", 82),
          ("channel-not-implemented", 66),
          ("channel-unacceptable", 6),
          ("ciruit-or-channel-preempted", 45),
          ("destination-out-of-order", 27),
          ("facility-not-implemented", 69),
          ("facility-not-subscribed", 50),
          ("facility-rejected", 29),
          ("incoming-call-barred", 54),
          ("incompatible-destination", 88),
          ("incompatible-or-nonexistent-message", 98),
          ("information-element-length-error", 103),
          ("information-element-not-implemented", 99),
          ("interworking-unspecified", 127),
          ("invalid-call-reference", 81),
          ("invalid-information-element-contents", 100),
          ("invalid-message-unspecified", 95),
          ("invalid-number-format", 28),
          ("invalid-transit-network", 91),
          ("manditory-information-element-missing", 96),
          ("message-incompatible-with-call-state", 101),
          ("message-nonexistent-or-not-implemented", 97),
          ("network-congestion", 42),
          ("network-out-of-order", 38),
          ("no-call-suspended", 85),
          ("no-circuit-or-channel-available", 34),
          ("no-error", 0),
          ("no-route-to-destination", 3),
          ("no-route-to-transit-network", 2),
          ("no-user-responding", 18),
          ("non-selected-user-clearing", 26),
          ("normal-call-clearing", 16),
          ("normal-clearing-unspecified", 31),
          ("number-changed", 22),
          ("outgoing-call-barred", 52),
          ("protocol-error-unspecified", 111),
          ("quality-of-service-unavailable", 49),
          ("requested-channel-not-available", 44),
          ("resources-unavailable", 47),
          ("response-to-status-enquiry", 30),
          ("restricted-digital-information-only", 70),
          ("service-not-available", 63),
          ("service-not-implemented", 79),
          ("suspended-call-cleared", 86),
          ("temporary-failure", 41),
          ("timer-expiration", 102),
          ("unassigned-number", 1),
          ("user-alerted-no-answer", 19),
          ("user-busy", 17))
    )


_OPstnCallTabCause_Type.__name__ = "Integer32"
_OPstnCallTabCause_Object = MibTableColumn
oPstnCallTabCause = _OPstnCallTabCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 7),
    _OPstnCallTabCause_Type()
)
oPstnCallTabCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabCause.setStatus("mandatory")
_OPstnCallTabAddress_Type = Integer32
_OPstnCallTabAddress_Object = MibTableColumn
oPstnCallTabAddress = _OPstnCallTabAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 8),
    _OPstnCallTabAddress_Type()
)
oPstnCallTabAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabAddress.setStatus("mandatory")
_OPstnCallTabInfoRate_Type = Integer32
_OPstnCallTabInfoRate_Object = MibTableColumn
oPstnCallTabInfoRate = _OPstnCallTabInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 9),
    _OPstnCallTabInfoRate_Type()
)
oPstnCallTabInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabInfoRate.setStatus("mandatory")


class _OPstnCallTabInfoType_Type(Integer32):
    """Custom type oPstnCallTabInfoType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("audio", 8),
          ("cm56", 2),
          ("cma", 4),
          ("cmd", 1),
          ("cmv", 3),
          ("data", 6),
          ("data56", 7),
          ("rdi", 10),
          ("udi", 9),
          ("voice", 5))
    )


_OPstnCallTabInfoType_Type.__name__ = "Integer32"
_OPstnCallTabInfoType_Object = MibTableColumn
oPstnCallTabInfoType = _OPstnCallTabInfoType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 10),
    _OPstnCallTabInfoType_Type()
)
oPstnCallTabInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabInfoType.setStatus("mandatory")
_OPstnCallTabDuration_Type = Integer32
_OPstnCallTabDuration_Object = MibTableColumn
oPstnCallTabDuration = _OPstnCallTabDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 3, 1, 11),
    _OPstnCallTabDuration_Type()
)
oPstnCallTabDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCallTabDuration.setStatus("mandatory")
_AccPstnChanTable_Object = MibTable
accPstnChanTable = _AccPstnChanTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 4)
)
if mibBuilder.loadTexts:
    accPstnChanTable.setStatus("mandatory")
_AccPstnChanTableEntry_Object = MibTableRow
accPstnChanTableEntry = _AccPstnChanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 4, 1)
)
accPstnChanTableEntry.setIndexNames(
    (0, "ACC-PSTN", "oPstnChanTabDslIndex"),
    (0, "ACC-PSTN", "oPstnChanTabSlotMap"),
)
if mibBuilder.loadTexts:
    accPstnChanTableEntry.setStatus("mandatory")
_OPstnChanTabDslIndex_Type = Integer32
_OPstnChanTabDslIndex_Object = MibTableColumn
oPstnChanTabDslIndex = _OPstnChanTabDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 4, 1, 1),
    _OPstnChanTabDslIndex_Type()
)
oPstnChanTabDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnChanTabDslIndex.setStatus("mandatory")
_OPstnChanTabChannel_Type = Integer32
_OPstnChanTabChannel_Object = MibTableColumn
oPstnChanTabChannel = _OPstnChanTabChannel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 4, 1, 2),
    _OPstnChanTabChannel_Type()
)
oPstnChanTabChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnChanTabChannel.setStatus("mandatory")


class _OPstnChanTabServState_Type(Integer32):
    """Custom type oPstnChanTabServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("maintenance", 2),
          ("out-service", 3))
    )


_OPstnChanTabServState_Type.__name__ = "Integer32"
_OPstnChanTabServState_Object = MibTableColumn
oPstnChanTabServState = _OPstnChanTabServState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 4, 1, 3),
    _OPstnChanTabServState_Type()
)
oPstnChanTabServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnChanTabServState.setStatus("mandatory")


class _OPstnChanTabChanState_Type(Integer32):
    """Custom type oPstnChanTabChanState based on Integer32"""
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
        *(("awarded", 3),
          ("busy", 4),
          ("cnfgerr", 7),
          ("cnfgpend", 6),
          ("idle", 1),
          ("proposed", 2),
          ("reserved", 8),
          ("restart", 5))
    )


_OPstnChanTabChanState_Type.__name__ = "Integer32"
_OPstnChanTabChanState_Object = MibTableColumn
oPstnChanTabChanState = _OPstnChanTabChanState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 4, 1, 4),
    _OPstnChanTabChanState_Type()
)
oPstnChanTabChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnChanTabChanState.setStatus("mandatory")
_OPstnChanTabSlotMap_Type = Integer32
_OPstnChanTabSlotMap_Object = MibTableColumn
oPstnChanTabSlotMap = _OPstnChanTabSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 4, 1, 5),
    _OPstnChanTabSlotMap_Type()
)
oPstnChanTabSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnChanTabSlotMap.setStatus("mandatory")
_AccPstnRBSParamTable_Object = MibTable
accPstnRBSParamTable = _AccPstnRBSParamTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5)
)
if mibBuilder.loadTexts:
    accPstnRBSParamTable.setStatus("mandatory")
_AccPstnRBSParamTableEntry_Object = MibTableRow
accPstnRBSParamTableEntry = _AccPstnRBSParamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1)
)
accPstnRBSParamTableEntry.setIndexNames(
    (0, "ACC-PSTN", "oPstnRbsTabDslIndex"),
)
if mibBuilder.loadTexts:
    accPstnRBSParamTableEntry.setStatus("mandatory")
_OPstnRbsTabDslIndex_Type = Integer32
_OPstnRbsTabDslIndex_Object = MibTableColumn
oPstnRbsTabDslIndex = _OPstnRbsTabDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 1),
    _OPstnRbsTabDslIndex_Type()
)
oPstnRbsTabDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnRbsTabDslIndex.setStatus("mandatory")


class _OPstnRbsTabSuprModeIn_Type(Integer32):
    """Custom type oPstnRbsTabSuprModeIn based on Integer32"""
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
        *(("ddsd", 4),
          ("immediate", 2),
          ("none", 1),
          ("wink", 3))
    )


_OPstnRbsTabSuprModeIn_Type.__name__ = "Integer32"
_OPstnRbsTabSuprModeIn_Object = MibTableColumn
oPstnRbsTabSuprModeIn = _OPstnRbsTabSuprModeIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 2),
    _OPstnRbsTabSuprModeIn_Type()
)
oPstnRbsTabSuprModeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabSuprModeIn.setStatus("mandatory")


class _OPstnRbsTabSuprModeOut_Type(Integer32):
    """Custom type oPstnRbsTabSuprModeOut based on Integer32"""
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
        *(("ddsd", 4),
          ("immediate", 2),
          ("none", 1),
          ("wink", 3))
    )


_OPstnRbsTabSuprModeOut_Type.__name__ = "Integer32"
_OPstnRbsTabSuprModeOut_Object = MibTableColumn
oPstnRbsTabSuprModeOut = _OPstnRbsTabSuprModeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 3),
    _OPstnRbsTabSuprModeOut_Type()
)
oPstnRbsTabSuprModeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabSuprModeOut.setStatus("mandatory")


class _OPstnRbsTabRegnModeIn_Type(Integer32):
    """Custom type oPstnRbsTabRegnModeIn based on Integer32"""
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
        *(("dtmf", 4),
          ("mf", 3),
          ("pulse", 2),
          ("suppress", 1))
    )


_OPstnRbsTabRegnModeIn_Type.__name__ = "Integer32"
_OPstnRbsTabRegnModeIn_Object = MibTableColumn
oPstnRbsTabRegnModeIn = _OPstnRbsTabRegnModeIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 4),
    _OPstnRbsTabRegnModeIn_Type()
)
oPstnRbsTabRegnModeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabRegnModeIn.setStatus("mandatory")


class _OPstnRbsTabRegnModeOut_Type(Integer32):
    """Custom type oPstnRbsTabRegnModeOut based on Integer32"""
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
        *(("dtmf", 4),
          ("mf", 3),
          ("pulse", 2),
          ("suppress", 1))
    )


_OPstnRbsTabRegnModeOut_Type.__name__ = "Integer32"
_OPstnRbsTabRegnModeOut_Object = MibTableColumn
oPstnRbsTabRegnModeOut = _OPstnRbsTabRegnModeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 5),
    _OPstnRbsTabRegnModeOut_Type()
)
oPstnRbsTabRegnModeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabRegnModeOut.setStatus("mandatory")


class _OPstnRbsTabPresModeIn_Type(Integer32):
    """Custom type oPstnRbsTabPresModeIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enbloc", 2),
          ("none", 1),
          ("overlap", 3))
    )


_OPstnRbsTabPresModeIn_Type.__name__ = "Integer32"
_OPstnRbsTabPresModeIn_Object = MibTableColumn
oPstnRbsTabPresModeIn = _OPstnRbsTabPresModeIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 6),
    _OPstnRbsTabPresModeIn_Type()
)
oPstnRbsTabPresModeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabPresModeIn.setStatus("mandatory")


class _OPstnRbsTabPresModeOut_Type(Integer32):
    """Custom type oPstnRbsTabPresModeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enbloc", 2),
          ("none", 1),
          ("overlap", 3))
    )


_OPstnRbsTabPresModeOut_Type.__name__ = "Integer32"
_OPstnRbsTabPresModeOut_Object = MibTableColumn
oPstnRbsTabPresModeOut = _OPstnRbsTabPresModeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 7),
    _OPstnRbsTabPresModeOut_Type()
)
oPstnRbsTabPresModeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabPresModeOut.setStatus("mandatory")


class _OPstnRbsTabGlareAction_Type(Integer32):
    """Custom type oPstnRbsTabGlareAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backoff", 1),
          ("proceed", 2))
    )


_OPstnRbsTabGlareAction_Type.__name__ = "Integer32"
_OPstnRbsTabGlareAction_Object = MibTableColumn
oPstnRbsTabGlareAction = _OPstnRbsTabGlareAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 8),
    _OPstnRbsTabGlareAction_Type()
)
oPstnRbsTabGlareAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabGlareAction.setStatus("mandatory")
_OPstnRbsTabWoddDuration_Type = Integer32
_OPstnRbsTabWoddDuration_Object = MibTableColumn
oPstnRbsTabWoddDuration = _OPstnRbsTabWoddDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 9),
    _OPstnRbsTabWoddDuration_Type()
)
oPstnRbsTabWoddDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabWoddDuration.setStatus("mandatory")
_OPstnRbsTabWsddDetect_Type = Integer32
_OPstnRbsTabWsddDetect_Object = MibTableColumn
oPstnRbsTabWsddDetect = _OPstnRbsTabWsddDetect_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 10),
    _OPstnRbsTabWsddDetect_Type()
)
oPstnRbsTabWsddDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabWsddDetect.setStatus("mandatory")
_OPstnRbsTabWesdDetect_Type = Integer32
_OPstnRbsTabWesdDetect_Object = MibTableColumn
oPstnRbsTabWesdDetect = _OPstnRbsTabWesdDetect_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 11),
    _OPstnRbsTabWesdDetect_Type()
)
oPstnRbsTabWesdDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabWesdDetect.setStatus("mandatory")
_OPstnRbsTabEnblocDigits_Type = Integer32
_OPstnRbsTabEnblocDigits_Object = MibTableColumn
oPstnRbsTabEnblocDigits = _OPstnRbsTabEnblocDigits_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 12),
    _OPstnRbsTabEnblocDigits_Type()
)
oPstnRbsTabEnblocDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabEnblocDigits.setStatus("mandatory")
_OPstnRbsTabEnblocTimeout_Type = Integer32
_OPstnRbsTabEnblocTimeout_Object = MibTableColumn
oPstnRbsTabEnblocTimeout = _OPstnRbsTabEnblocTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 5, 1, 13),
    _OPstnRbsTabEnblocTimeout_Type()
)
oPstnRbsTabEnblocTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnRbsTabEnblocTimeout.setStatus("mandatory")
_AccPstnIntCasSupvParamTable_Object = MibTable
accPstnIntCasSupvParamTable = _AccPstnIntCasSupvParamTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6)
)
if mibBuilder.loadTexts:
    accPstnIntCasSupvParamTable.setStatus("mandatory")
_AccPstnIntCasSupvParamEntry_Object = MibTableRow
accPstnIntCasSupvParamEntry = _AccPstnIntCasSupvParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1)
)
accPstnIntCasSupvParamEntry.setIndexNames(
    (0, "ACC-PSTN", "oPstnCasTabDslIndex"),
)
if mibBuilder.loadTexts:
    accPstnIntCasSupvParamEntry.setStatus("mandatory")
_OPstnCasTabDslIndex_Type = Integer32
_OPstnCasTabDslIndex_Object = MibTableColumn
oPstnCasTabDslIndex = _OPstnCasTabDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 1),
    _OPstnCasTabDslIndex_Type()
)
oPstnCasTabDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oPstnCasTabDslIndex.setStatus("mandatory")


class _OPstnCasTabSupvModeIn_Type(Integer32):
    """Custom type oPstnCasTabSupvModeIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("p7", 3),
          ("r2", 2))
    )


_OPstnCasTabSupvModeIn_Type.__name__ = "Integer32"
_OPstnCasTabSupvModeIn_Object = MibTableColumn
oPstnCasTabSupvModeIn = _OPstnCasTabSupvModeIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 2),
    _OPstnCasTabSupvModeIn_Type()
)
oPstnCasTabSupvModeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvModeIn.setStatus("mandatory")


class _OPstnCasTabSupvModeOut_Type(Integer32):
    """Custom type oPstnCasTabSupvModeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("p7", 3),
          ("r2", 2))
    )


_OPstnCasTabSupvModeOut_Type.__name__ = "Integer32"
_OPstnCasTabSupvModeOut_Object = MibTableColumn
oPstnCasTabSupvModeOut = _OPstnCasTabSupvModeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 3),
    _OPstnCasTabSupvModeOut_Type()
)
oPstnCasTabSupvModeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvModeOut.setStatus("mandatory")


class _OPstnCasTabSupvMask_Type(Integer32):
    """Custom type oPstnCasTabSupvMask based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvMask_Type.__name__ = "Integer32"
_OPstnCasTabSupvMask_Object = MibTableColumn
oPstnCasTabSupvMask = _OPstnCasTabSupvMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 4),
    _OPstnCasTabSupvMask_Type()
)
oPstnCasTabSupvMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvMask.setStatus("mandatory")


class _OPstnCasTabSupvIdlePatt_Type(Integer32):
    """Custom type oPstnCasTabSupvIdlePatt based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvIdlePatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvIdlePatt_Object = MibTableColumn
oPstnCasTabSupvIdlePatt = _OPstnCasTabSupvIdlePatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 5),
    _OPstnCasTabSupvIdlePatt_Type()
)
oPstnCasTabSupvIdlePatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvIdlePatt.setStatus("mandatory")
_OPstnCasTabSupvIdleTime_Type = Integer32
_OPstnCasTabSupvIdleTime_Object = MibTableColumn
oPstnCasTabSupvIdleTime = _OPstnCasTabSupvIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 6),
    _OPstnCasTabSupvIdleTime_Type()
)
oPstnCasTabSupvIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvIdleTime.setStatus("mandatory")


class _OPstnCasTabSupvSeizePatt_Type(Integer32):
    """Custom type oPstnCasTabSupvSeizePatt based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvSeizePatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvSeizePatt_Object = MibTableColumn
oPstnCasTabSupvSeizePatt = _OPstnCasTabSupvSeizePatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 7),
    _OPstnCasTabSupvSeizePatt_Type()
)
oPstnCasTabSupvSeizePatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvSeizePatt.setStatus("mandatory")
_OPstnCasTabSupvSeizeTime_Type = Integer32
_OPstnCasTabSupvSeizeTime_Object = MibTableColumn
oPstnCasTabSupvSeizeTime = _OPstnCasTabSupvSeizeTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 8),
    _OPstnCasTabSupvSeizeTime_Type()
)
oPstnCasTabSupvSeizeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvSeizeTime.setStatus("mandatory")


class _OPstnCasTabSupvSeizeAckPatt_Type(Integer32):
    """Custom type oPstnCasTabSupvSeizeAckPatt based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvSeizeAckPatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvSeizeAckPatt_Object = MibTableColumn
oPstnCasTabSupvSeizeAckPatt = _OPstnCasTabSupvSeizeAckPatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 9),
    _OPstnCasTabSupvSeizeAckPatt_Type()
)
oPstnCasTabSupvSeizeAckPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvSeizeAckPatt.setStatus("mandatory")
_OPstnCasTabSupvSeizeAckTime_Type = Integer32
_OPstnCasTabSupvSeizeAckTime_Object = MibTableColumn
oPstnCasTabSupvSeizeAckTime = _OPstnCasTabSupvSeizeAckTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 10),
    _OPstnCasTabSupvSeizeAckTime_Type()
)
oPstnCasTabSupvSeizeAckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvSeizeAckTime.setStatus("mandatory")


class _OPstnCasTabSupvAnswerPatt_Type(Integer32):
    """Custom type oPstnCasTabSupvAnswerPatt based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvAnswerPatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvAnswerPatt_Object = MibTableColumn
oPstnCasTabSupvAnswerPatt = _OPstnCasTabSupvAnswerPatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 11),
    _OPstnCasTabSupvAnswerPatt_Type()
)
oPstnCasTabSupvAnswerPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvAnswerPatt.setStatus("mandatory")
_OPstnCasTabSupvAnswerTime_Type = Integer32
_OPstnCasTabSupvAnswerTime_Object = MibTableColumn
oPstnCasTabSupvAnswerTime = _OPstnCasTabSupvAnswerTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 12),
    _OPstnCasTabSupvAnswerTime_Type()
)
oPstnCasTabSupvAnswerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvAnswerTime.setStatus("mandatory")


class _OPstnCasTabSupvClrForwPatt_Type(Integer32):
    """Custom type oPstnCasTabSupvClrForwPatt based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvClrForwPatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvClrForwPatt_Object = MibTableColumn
oPstnCasTabSupvClrForwPatt = _OPstnCasTabSupvClrForwPatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 13),
    _OPstnCasTabSupvClrForwPatt_Type()
)
oPstnCasTabSupvClrForwPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvClrForwPatt.setStatus("mandatory")
_OPstnCasTabSupvClrForwTime_Type = Integer32
_OPstnCasTabSupvClrForwTime_Object = MibTableColumn
oPstnCasTabSupvClrForwTime = _OPstnCasTabSupvClrForwTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 14),
    _OPstnCasTabSupvClrForwTime_Type()
)
oPstnCasTabSupvClrForwTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvClrForwTime.setStatus("mandatory")


class _OPstnCasTabSupvClrBackPatt_Type(Integer32):
    """Custom type oPstnCasTabSupvClrBackPatt based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvClrBackPatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvClrBackPatt_Object = MibTableColumn
oPstnCasTabSupvClrBackPatt = _OPstnCasTabSupvClrBackPatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 15),
    _OPstnCasTabSupvClrBackPatt_Type()
)
oPstnCasTabSupvClrBackPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvClrBackPatt.setStatus("mandatory")
_OPstnCasTabSupvClrBackTime_Type = Integer32
_OPstnCasTabSupvClrBackTime_Object = MibTableColumn
oPstnCasTabSupvClrBackTime = _OPstnCasTabSupvClrBackTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 16),
    _OPstnCasTabSupvClrBackTime_Type()
)
oPstnCasTabSupvClrBackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvClrBackTime.setStatus("mandatory")


class _OPstnCasTabSupvBlockPatt_Type(Integer32):
    """Custom type oPstnCasTabSupvBlockPatt based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_OPstnCasTabSupvBlockPatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvBlockPatt_Object = MibTableColumn
oPstnCasTabSupvBlockPatt = _OPstnCasTabSupvBlockPatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 17),
    _OPstnCasTabSupvBlockPatt_Type()
)
oPstnCasTabSupvBlockPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvBlockPatt.setStatus("mandatory")
_OPstnCasTabSupvBlockTime_Type = Integer32
_OPstnCasTabSupvBlockTime_Object = MibTableColumn
oPstnCasTabSupvBlockTime = _OPstnCasTabSupvBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 18),
    _OPstnCasTabSupvBlockTime_Type()
)
oPstnCasTabSupvBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvBlockTime.setStatus("mandatory")


class _OPstnCasTabSupvMetPatt_Type(Integer32):
    """Custom type oPstnCasTabSupvMetPatt based on Integer32"""
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
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16),
          ("disabled", 17))
    )


_OPstnCasTabSupvMetPatt_Type.__name__ = "Integer32"
_OPstnCasTabSupvMetPatt_Object = MibTableColumn
oPstnCasTabSupvMetPatt = _OPstnCasTabSupvMetPatt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 19),
    _OPstnCasTabSupvMetPatt_Type()
)
oPstnCasTabSupvMetPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvMetPatt.setStatus("mandatory")
_OPstnCasTabSupvMetTime_Type = Integer32
_OPstnCasTabSupvMetTime_Object = MibTableColumn
oPstnCasTabSupvMetTime = _OPstnCasTabSupvMetTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 20),
    _OPstnCasTabSupvMetTime_Type()
)
oPstnCasTabSupvMetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvMetTime.setStatus("mandatory")
_OPstnCasTabSupvMetDelay_Type = Integer32
_OPstnCasTabSupvMetDelay_Object = MibTableColumn
oPstnCasTabSupvMetDelay = _OPstnCasTabSupvMetDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 21),
    _OPstnCasTabSupvMetDelay_Type()
)
oPstnCasTabSupvMetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvMetDelay.setStatus("mandatory")
_OPstnCasTabSupvMetOn_Type = Integer32
_OPstnCasTabSupvMetOn_Object = MibTableColumn
oPstnCasTabSupvMetOn = _OPstnCasTabSupvMetOn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 22),
    _OPstnCasTabSupvMetOn_Type()
)
oPstnCasTabSupvMetOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvMetOn.setStatus("mandatory")
_OPstnCasTabSupvMetOff_Type = Integer32
_OPstnCasTabSupvMetOff_Object = MibTableColumn
oPstnCasTabSupvMetOff = _OPstnCasTabSupvMetOff_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 23),
    _OPstnCasTabSupvMetOff_Type()
)
oPstnCasTabSupvMetOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvMetOff.setStatus("mandatory")


class _OPstnCasTabSupvGlare_Type(Integer32):
    """Custom type oPstnCasTabSupvGlare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backoff", 1),
          ("proceed", 2))
    )


_OPstnCasTabSupvGlare_Type.__name__ = "Integer32"
_OPstnCasTabSupvGlare_Object = MibTableColumn
oPstnCasTabSupvGlare = _OPstnCasTabSupvGlare_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 24),
    _OPstnCasTabSupvGlare_Type()
)
oPstnCasTabSupvGlare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabSupvGlare.setStatus("mandatory")


class _OPstnCasTabRegModeIn_Type(Integer32):
    """Custom type oPstnCasTabRegModeIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p7-dtmf", 3),
          ("r2-mf-x", 2),
          ("suppressed", 1))
    )


_OPstnCasTabRegModeIn_Type.__name__ = "Integer32"
_OPstnCasTabRegModeIn_Object = MibTableColumn
oPstnCasTabRegModeIn = _OPstnCasTabRegModeIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 25),
    _OPstnCasTabRegModeIn_Type()
)
oPstnCasTabRegModeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegModeIn.setStatus("mandatory")


class _OPstnCasTabRegModeOut_Type(Integer32):
    """Custom type oPstnCasTabRegModeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p7-dtmf", 3),
          ("r2-mf-x", 2),
          ("suppressed", 1))
    )


_OPstnCasTabRegModeOut_Type.__name__ = "Integer32"
_OPstnCasTabRegModeOut_Object = MibTableColumn
oPstnCasTabRegModeOut = _OPstnCasTabRegModeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 26),
    _OPstnCasTabRegModeOut_Type()
)
oPstnCasTabRegModeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegModeOut.setStatus("mandatory")


class _OPstnCasTabRegComp1Tone_Type(Integer32):
    """Custom type oPstnCasTabRegComp1Tone based on Integer32"""
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
        *(("d1", 1),
          ("d10", 10),
          ("d11", 11),
          ("d12", 12),
          ("d13", 13),
          ("d14", 14),
          ("d15", 15),
          ("d2", 2),
          ("d3", 3),
          ("d4", 4),
          ("d5", 5),
          ("d6", 6),
          ("d7", 7),
          ("d8", 8),
          ("d9", 9),
          ("none", 16))
    )


_OPstnCasTabRegComp1Tone_Type.__name__ = "Integer32"
_OPstnCasTabRegComp1Tone_Object = MibTableColumn
oPstnCasTabRegComp1Tone = _OPstnCasTabRegComp1Tone_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 27),
    _OPstnCasTabRegComp1Tone_Type()
)
oPstnCasTabRegComp1Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegComp1Tone.setStatus("mandatory")
_OPstnCasTabRegComp1On_Type = Integer32
_OPstnCasTabRegComp1On_Object = MibTableColumn
oPstnCasTabRegComp1On = _OPstnCasTabRegComp1On_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 28),
    _OPstnCasTabRegComp1On_Type()
)
oPstnCasTabRegComp1On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegComp1On.setStatus("mandatory")
_OPstnCasTabRegComp1Off_Type = Integer32
_OPstnCasTabRegComp1Off_Object = MibTableColumn
oPstnCasTabRegComp1Off = _OPstnCasTabRegComp1Off_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 29),
    _OPstnCasTabRegComp1Off_Type()
)
oPstnCasTabRegComp1Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegComp1Off.setStatus("mandatory")


class _OPstnCasTabRegComp2Tone_Type(Integer32):
    """Custom type oPstnCasTabRegComp2Tone based on Integer32"""
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
        *(("d1", 1),
          ("d10", 10),
          ("d11", 11),
          ("d12", 12),
          ("d13", 13),
          ("d14", 14),
          ("d15", 15),
          ("d2", 2),
          ("d3", 3),
          ("d4", 4),
          ("d5", 5),
          ("d6", 6),
          ("d7", 7),
          ("d8", 8),
          ("d9", 9),
          ("none", 16))
    )


_OPstnCasTabRegComp2Tone_Type.__name__ = "Integer32"
_OPstnCasTabRegComp2Tone_Object = MibTableColumn
oPstnCasTabRegComp2Tone = _OPstnCasTabRegComp2Tone_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 30),
    _OPstnCasTabRegComp2Tone_Type()
)
oPstnCasTabRegComp2Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegComp2Tone.setStatus("mandatory")
_OPstnCasTabRegComp2On_Type = Integer32
_OPstnCasTabRegComp2On_Object = MibTableColumn
oPstnCasTabRegComp2On = _OPstnCasTabRegComp2On_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 31),
    _OPstnCasTabRegComp2On_Type()
)
oPstnCasTabRegComp2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegComp2On.setStatus("mandatory")
_OPstnCasTabRegComp2Off_Type = Integer32
_OPstnCasTabRegComp2Off_Object = MibTableColumn
oPstnCasTabRegComp2Off = _OPstnCasTabRegComp2Off_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 6, 1, 32),
    _OPstnCasTabRegComp2Off_Type()
)
oPstnCasTabRegComp2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oPstnCasTabRegComp2Off.setStatus("mandatory")
_AccDsprmTraps_ObjectIdentity = ObjectIdentity
accDsprmTraps = _AccDsprmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7)
)
_AccDsprmTrapMsg_Type = DisplayString
_AccDsprmTrapMsg_Object = MibScalar
accDsprmTrapMsg = _AccDsprmTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7, 1),
    _AccDsprmTrapMsg_Type()
)
accDsprmTrapMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDsprmTrapMsg.setStatus("mandatory")
_AccNewLiberty_ObjectIdentity = ObjectIdentity
accNewLiberty = _AccNewLiberty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8)
)
_AccPstnTabSigGen_ObjectIdentity = ObjectIdentity
accPstnTabSigGen = _AccPstnTabSigGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3)
)
_AccPstnTabSigTrace_Type = Integer32
_AccPstnTabSigTrace_Object = MibScalar
accPstnTabSigTrace = _AccPstnTabSigTrace_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 1),
    _AccPstnTabSigTrace_Type()
)
accPstnTabSigTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigTrace.setStatus("mandatory")
_AccPstnTabSigType_ObjectIdentity = ObjectIdentity
accPstnTabSigType = _AccPstnTabSigType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 2)
)


class _AccPstnTabSigInType_Type(Integer32):
    """Custom type accPstnTabSigInType based on Integer32"""
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
        *(("dp", 3),
          ("dtmf", 2),
          ("none", 1),
          ("r2", 4))
    )


_AccPstnTabSigInType_Type.__name__ = "Integer32"
_AccPstnTabSigInType_Object = MibScalar
accPstnTabSigInType = _AccPstnTabSigInType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 2, 1),
    _AccPstnTabSigInType_Type()
)
accPstnTabSigInType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigInType.setStatus("mandatory")


class _AccPstnTabSigOutType_Type(Integer32):
    """Custom type accPstnTabSigOutType based on Integer32"""
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
        *(("dp", 3),
          ("dtmf", 2),
          ("none", 1),
          ("r2", 4))
    )


_AccPstnTabSigOutType_Type.__name__ = "Integer32"
_AccPstnTabSigOutType_Object = MibScalar
accPstnTabSigOutType = _AccPstnTabSigOutType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 2, 2),
    _AccPstnTabSigOutType_Type()
)
accPstnTabSigOutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigOutType.setStatus("mandatory")
_AccPstnEtt_ObjectIdentity = ObjectIdentity
accPstnEtt = _AccPstnEtt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3)
)
_AccR2Sig_ObjectIdentity = ObjectIdentity
accR2Sig = _AccR2Sig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1)
)
_AccR2Sigo_ObjectIdentity = ObjectIdentity
accR2Sigo = _AccR2Sigo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1)
)
_AccPstnTabSigR2CdDig_Type = Integer32
_AccPstnTabSigR2CdDig_Object = MibScalar
accPstnTabSigR2CdDig = _AccPstnTabSigR2CdDig_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 1),
    _AccPstnTabSigR2CdDig_Type()
)
accPstnTabSigR2CdDig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2CdDig.setStatus("mandatory")
_AccPstnTabSigR2CnDig_Type = Integer32
_AccPstnTabSigR2CnDig_Object = MibScalar
accPstnTabSigR2CnDig = _AccPstnTabSigR2CnDig_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 2),
    _AccPstnTabSigR2CnDig_Type()
)
accPstnTabSigR2CnDig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2CnDig.setStatus("mandatory")


class _AccPstnTabSigR2ReqCpc_Type(Integer32):
    """Custom type accPstnTabSigR2ReqCpc based on Integer32"""
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


_AccPstnTabSigR2ReqCpc_Type.__name__ = "Integer32"
_AccPstnTabSigR2ReqCpc_Object = MibScalar
accPstnTabSigR2ReqCpc = _AccPstnTabSigR2ReqCpc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 3),
    _AccPstnTabSigR2ReqCpc_Type()
)
accPstnTabSigR2ReqCpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2ReqCpc.setStatus("mandatory")


class _AccPstnTabSigR2AdMo_Type(Integer32):
    """Custom type accPstnTabSigR2AdMo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groupATable", 2),
          ("groupBTable", 1))
    )


_AccPstnTabSigR2AdMo_Type.__name__ = "Integer32"
_AccPstnTabSigR2AdMo_Object = MibScalar
accPstnTabSigR2AdMo = _AccPstnTabSigR2AdMo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 4),
    _AccPstnTabSigR2AdMo_Type()
)
accPstnTabSigR2AdMo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2AdMo.setStatus("mandatory")


class _AccPstnTabSigR2CdInMode_Type(Integer32):
    """Custom type accPstnTabSigR2CdInMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signaled", 1),
          ("timeout", 2))
    )


_AccPstnTabSigR2CdInMode_Type.__name__ = "Integer32"
_AccPstnTabSigR2CdInMode_Object = MibScalar
accPstnTabSigR2CdInMode = _AccPstnTabSigR2CdInMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 5),
    _AccPstnTabSigR2CdInMode_Type()
)
accPstnTabSigR2CdInMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2CdInMode.setStatus("mandatory")


class _AccPstnTabSigR2CdOutMode_Type(Integer32):
    """Custom type accPstnTabSigR2CdOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signaled", 1),
          ("timeout", 2))
    )


_AccPstnTabSigR2CdOutMode_Type.__name__ = "Integer32"
_AccPstnTabSigR2CdOutMode_Object = MibScalar
accPstnTabSigR2CdOutMode = _AccPstnTabSigR2CdOutMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 6),
    _AccPstnTabSigR2CdOutMode_Type()
)
accPstnTabSigR2CdOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2CdOutMode.setStatus("mandatory")


class _AccPstnTabSigR2CnInMode_Type(Integer32):
    """Custom type accPstnTabSigR2CnInMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signaled", 1),
          ("timeout", 2))
    )


_AccPstnTabSigR2CnInMode_Type.__name__ = "Integer32"
_AccPstnTabSigR2CnInMode_Object = MibScalar
accPstnTabSigR2CnInMode = _AccPstnTabSigR2CnInMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 7),
    _AccPstnTabSigR2CnInMode_Type()
)
accPstnTabSigR2CnInMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2CnInMode.setStatus("mandatory")


class _AccPstnTabSigR2CnOutMode_Type(Integer32):
    """Custom type accPstnTabSigR2CnOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signaled", 1),
          ("timeout", 2))
    )


_AccPstnTabSigR2CnOutMode_Type.__name__ = "Integer32"
_AccPstnTabSigR2CnOutMode_Object = MibScalar
accPstnTabSigR2CnOutMode = _AccPstnTabSigR2CnOutMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 8),
    _AccPstnTabSigR2CnOutMode_Type()
)
accPstnTabSigR2CnOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2CnOutMode.setStatus("mandatory")


class _AccPstnTabSigR2RspInMode_Type(Integer32):
    """Custom type accPstnTabSigR2RspInMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compelled", 1),
          ("noncomp", 3),
          ("semicomp", 2))
    )


_AccPstnTabSigR2RspInMode_Type.__name__ = "Integer32"
_AccPstnTabSigR2RspInMode_Object = MibScalar
accPstnTabSigR2RspInMode = _AccPstnTabSigR2RspInMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 9),
    _AccPstnTabSigR2RspInMode_Type()
)
accPstnTabSigR2RspInMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2RspInMode.setStatus("mandatory")


class _AccPstnTabSigR2RspOutMode_Type(Integer32):
    """Custom type accPstnTabSigR2RspOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compelled", 1),
          ("noncomp", 3),
          ("semicomp", 2))
    )


_AccPstnTabSigR2RspOutMode_Type.__name__ = "Integer32"
_AccPstnTabSigR2RspOutMode_Object = MibScalar
accPstnTabSigR2RspOutMode = _AccPstnTabSigR2RspOutMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 10),
    _AccPstnTabSigR2RspOutMode_Type()
)
accPstnTabSigR2RspOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2RspOutMode.setStatus("mandatory")


class _AccPstnTabSigR2ObCpc_Type(Integer32):
    """Custom type accPstnTabSigR2ObCpc based on Integer32"""
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
        *(("data", 4),
          ("maintenance", 5),
          ("operator", 1),
          ("ordinary", 2),
          ("priority", 3))
    )


_AccPstnTabSigR2ObCpc_Type.__name__ = "Integer32"
_AccPstnTabSigR2ObCpc_Object = MibScalar
accPstnTabSigR2ObCpc = _AccPstnTabSigR2ObCpc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 11),
    _AccPstnTabSigR2ObCpc_Type()
)
accPstnTabSigR2ObCpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2ObCpc.setStatus("mandatory")
_AccPstnTabSigR2ObDflt_Type = Integer32
_AccPstnTabSigR2ObDflt_Object = MibScalar
accPstnTabSigR2ObDflt = _AccPstnTabSigR2ObDflt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 12),
    _AccPstnTabSigR2ObDflt_Type()
)
accPstnTabSigR2ObDflt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2ObDflt.setStatus("mandatory")
_AccPstnTabSigR2ScDur_Type = Integer32
_AccPstnTabSigR2ScDur_Object = MibScalar
accPstnTabSigR2ScDur = _AccPstnTabSigR2ScDur_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 13),
    _AccPstnTabSigR2ScDur_Type()
)
accPstnTabSigR2ScDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2ScDur.setStatus("mandatory")
_AccPstnTabSigR2RspInDur_Type = Integer32
_AccPstnTabSigR2RspInDur_Object = MibScalar
accPstnTabSigR2RspInDur = _AccPstnTabSigR2RspInDur_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 14),
    _AccPstnTabSigR2RspInDur_Type()
)
accPstnTabSigR2RspInDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2RspInDur.setStatus("mandatory")
_AccPstnTabSigR2RspOutDur_Type = Integer32
_AccPstnTabSigR2RspOutDur_Object = MibScalar
accPstnTabSigR2RspOutDur = _AccPstnTabSigR2RspOutDur_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 15),
    _AccPstnTabSigR2RspOutDur_Type()
)
accPstnTabSigR2RspOutDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2RspOutDur.setStatus("mandatory")
_AccPstnTabSigR2InDur_Type = Integer32
_AccPstnTabSigR2InDur_Object = MibScalar
accPstnTabSigR2InDur = _AccPstnTabSigR2InDur_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 16),
    _AccPstnTabSigR2InDur_Type()
)
accPstnTabSigR2InDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2InDur.setStatus("mandatory")
_AccPstnTabSigR2OutDur_Type = Integer32
_AccPstnTabSigR2OutDur_Object = MibScalar
accPstnTabSigR2OutDur = _AccPstnTabSigR2OutDur_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 17),
    _AccPstnTabSigR2OutDur_Type()
)
accPstnTabSigR2OutDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2OutDur.setStatus("mandatory")
_AccPstnTabSigR2InHiPwr_Type = Integer32
_AccPstnTabSigR2InHiPwr_Object = MibScalar
accPstnTabSigR2InHiPwr = _AccPstnTabSigR2InHiPwr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 18),
    _AccPstnTabSigR2InHiPwr_Type()
)
accPstnTabSigR2InHiPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2InHiPwr.setStatus("mandatory")
_AccPstnTabSigR2InLoPwr_Type = Integer32
_AccPstnTabSigR2InLoPwr_Object = MibScalar
accPstnTabSigR2InLoPwr = _AccPstnTabSigR2InLoPwr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 19),
    _AccPstnTabSigR2InLoPwr_Type()
)
accPstnTabSigR2InLoPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2InLoPwr.setStatus("mandatory")
_AccPstnTabSigR2OutHiPwr_Type = Integer32
_AccPstnTabSigR2OutHiPwr_Object = MibScalar
accPstnTabSigR2OutHiPwr = _AccPstnTabSigR2OutHiPwr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 20),
    _AccPstnTabSigR2OutHiPwr_Type()
)
accPstnTabSigR2OutHiPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2OutHiPwr.setStatus("mandatory")
_AccPstnTabSigR2OutLoPwr_Type = Integer32
_AccPstnTabSigR2OutLoPwr_Object = MibScalar
accPstnTabSigR2OutLoPwr = _AccPstnTabSigR2OutLoPwr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 21),
    _AccPstnTabSigR2OutLoPwr_Type()
)
accPstnTabSigR2OutLoPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigR2OutLoPwr.setStatus("mandatory")
_AccPstnTableInt_Type = Integer32
_AccPstnTableInt_Object = MibScalar
accPstnTableInt = _AccPstnTableInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 1, 1, 22),
    _AccPstnTableInt_Type()
)
accPstnTableInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTableInt.setStatus("mandatory")
_AccToneSupoo_ObjectIdentity = ObjectIdentity
accToneSupoo = _AccToneSupoo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2)
)
_AccPstnTable_Type = Integer32
_AccPstnTable_Object = MibScalar
accPstnTable = _AccPstnTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 1),
    _AccPstnTable_Type()
)
accPstnTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTable.setStatus("mandatory")
_AccPstnSignal_Type = Integer32
_AccPstnSignal_Object = MibScalar
accPstnSignal = _AccPstnSignal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 2),
    _AccPstnSignal_Type()
)
accPstnSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnSignal.setStatus("mandatory")


class _AccPstnFwdIntGI_Type(Integer32):
    """Custom type accPstnFwdIntGI based on Integer32"""
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
              200)
        )
    )
    namedValues = NamedValues(
        *(("accessTestEquipment", 13),
          ("delayOperator", 12),
          ("digit0", 10),
          ("digit1", 1),
          ("digit2", 2),
          ("digit3", 3),
          ("digit4", 4),
          ("digit5", 5),
          ("digit6", 6),
          ("digit7", 7),
          ("digit8", 8),
          ("digit9", 9),
          ("endOfInformation", 15),
          ("incomingOperator", 11),
          ("requireHalfEchoSuppressor", 14),
          ("spare", 200))
    )


_AccPstnFwdIntGI_Type.__name__ = "Integer32"
_AccPstnFwdIntGI_Object = MibScalar
accPstnFwdIntGI = _AccPstnFwdIntGI_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 3),
    _AccPstnFwdIntGI_Type()
)
accPstnFwdIntGI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnFwdIntGI.setStatus("mandatory")


class _AccPstnFwdIntGII_Type(Integer32):
    """Custom type accPstnFwdIntGII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              200)
        )
    )
    namedValues = NamedValues(
        *(("internationalDataTrans", 8),
          ("internationalOp", 10),
          ("internationalPrioritySubscriber", 9),
          ("internationalSubscriber", 7),
          ("nationalDataTransmission", 6),
          ("nationalMaintenanceEquipment", 3),
          ("nationalOp", 5),
          ("nationalPrioritySubscriber", 2),
          ("nationalSubscriber", 1),
          ("spare", 200))
    )


_AccPstnFwdIntGII_Type.__name__ = "Integer32"
_AccPstnFwdIntGII_Object = MibScalar
accPstnFwdIntGII = _AccPstnFwdIntGII_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 4),
    _AccPstnFwdIntGII_Type()
)
accPstnFwdIntGII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnFwdIntGII.setStatus("mandatory")


class _AccPstnFwdGenGI_Type(Integer32):
    """Custom type accPstnFwdGenGI based on Integer32"""
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
              200)
        )
    )
    namedValues = NamedValues(
        *(("accessTestEquipment", 13),
          ("delayOperator", 12),
          ("digit0", 10),
          ("digit1", 1),
          ("digit2", 2),
          ("digit3", 3),
          ("digit4", 4),
          ("digit5", 5),
          ("digit6", 6),
          ("digit7", 7),
          ("digit8", 8),
          ("digit9", 9),
          ("endOfInformation", 15),
          ("incomingOperator", 11),
          ("requireHalfEchoSuppressor", 14),
          ("spare", 200))
    )


_AccPstnFwdGenGI_Type.__name__ = "Integer32"
_AccPstnFwdGenGI_Object = MibScalar
accPstnFwdGenGI = _AccPstnFwdGenGI_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 5),
    _AccPstnFwdGenGI_Type()
)
accPstnFwdGenGI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnFwdGenGI.setStatus("mandatory")


class _AccPstnFwdGenGII_Type(Integer32):
    """Custom type accPstnFwdGenGII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              200)
        )
    )
    namedValues = NamedValues(
        *(("internationalDataTrans", 8),
          ("internationalOp", 10),
          ("internationalPrioritySubscriber", 9),
          ("internationalSubscriber", 7),
          ("nationalDataTransmission", 6),
          ("nationalMaintenanceEquipment", 3),
          ("nationalOp", 5),
          ("nationalPrioritySubscriber", 2),
          ("nationalSubscriber", 1),
          ("spare", 200))
    )


_AccPstnFwdGenGII_Type.__name__ = "Integer32"
_AccPstnFwdGenGII_Object = MibScalar
accPstnFwdGenGII = _AccPstnFwdGenGII_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 6),
    _AccPstnFwdGenGII_Type()
)
accPstnFwdGenGII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnFwdGenGII.setStatus("mandatory")


class _AccPstnBckIntGA_Type(Integer32):
    """Custom type accPstnBckIntGA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              200)
        )
    )
    namedValues = NamedValues(
        *(("addCmpltEndSig", 22),
          ("addCmpltRcvB", 19),
          ("congestInt-vacnt", 31),
          ("congestNat", 20),
          ("countryC", 27),
          ("echoSup-sndSigGroup2", 30),
          ("langDig", 28),
          ("natureCirct-sndCallingLn", 29),
          ("snd1stDig", 25),
          ("sndCpc", 21),
          ("sndCpcGoC", 26),
          ("sndDigN1", 18),
          ("sndDigN2", 23),
          ("sndDigN3", 24),
          ("sndNextDig", 17),
          ("spare", 200))
    )


_AccPstnBckIntGA_Type.__name__ = "Integer32"
_AccPstnBckIntGA_Object = MibScalar
accPstnBckIntGA = _AccPstnBckIntGA_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 7),
    _AccPstnBckIntGA_Type()
)
accPstnBckIntGA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnBckIntGA.setStatus("mandatory")


class _AccPstnBckIntGB_Type(Integer32):
    """Custom type accPstnBckIntGB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(18,
              19,
              20,
              21,
              22,
              23,
              24,
              200)
        )
    )
    namedValues = NamedValues(
        *(("congestion", 20),
          ("sendSpecialInformationTone", 18),
          ("spare", 200),
          ("subscriberLineBusy", 19),
          ("subscriberLineFreeCharge", 22),
          ("subscriberLineFreeNoCharge", 23),
          ("subscriberLineOutOfService", 24),
          ("unallocatedNumber", 21))
    )


_AccPstnBckIntGB_Type.__name__ = "Integer32"
_AccPstnBckIntGB_Object = MibScalar
accPstnBckIntGB = _AccPstnBckIntGB_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 8),
    _AccPstnBckIntGB_Type()
)
accPstnBckIntGB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnBckIntGB.setStatus("mandatory")


class _AccPstnBckIntGC_Type(Integer32):
    """Custom type accPstnBckIntGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              18,
              19,
              20,
              21,
              22,
              200)
        )
    )
    namedValues = NamedValues(
        *(("congestionC", 20),
          ("sendFirstCalledDigit", 18),
          ("sendGroupB", 19),
          ("sendNextCalledDigit", 21),
          ("sendNextCallingDigit", 17),
          ("sendSameCalledDigit", 22),
          ("spare", 200))
    )


_AccPstnBckIntGC_Type.__name__ = "Integer32"
_AccPstnBckIntGC_Object = MibScalar
accPstnBckIntGC = _AccPstnBckIntGC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 9),
    _AccPstnBckIntGC_Type()
)
accPstnBckIntGC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnBckIntGC.setStatus("mandatory")


class _AccPstnBckGenGA_Type(Integer32):
    """Custom type accPstnBckGenGA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              200)
        )
    )
    namedValues = NamedValues(
        *(("addCmpltendSig", 22),
          ("addCmpltrcvB", 19),
          ("congestNat", 20),
          ("congestint-vacnt", 31),
          ("countryC", 27),
          ("echoSup-sndSigGroup2", 30),
          ("langDig", 28),
          ("natureCirct-sndCallingLn", 29),
          ("snd1stDig", 25),
          ("sndCpc", 21),
          ("sndCpcGoC", 26),
          ("sndDigN1", 18),
          ("sndDigN2", 23),
          ("sndDigN3", 24),
          ("sndNextDig", 17),
          ("spare", 200))
    )


_AccPstnBckGenGA_Type.__name__ = "Integer32"
_AccPstnBckGenGA_Object = MibScalar
accPstnBckGenGA = _AccPstnBckGenGA_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 10),
    _AccPstnBckGenGA_Type()
)
accPstnBckGenGA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnBckGenGA.setStatus("mandatory")


class _AccPstnBckGenGB_Type(Integer32):
    """Custom type accPstnBckGenGB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(18,
              19,
              20,
              21,
              22,
              23,
              24,
              200)
        )
    )
    namedValues = NamedValues(
        *(("congestion", 20),
          ("sendSpecialInformationTone", 18),
          ("spare", 200),
          ("subscriberLineBusy", 19),
          ("subscriberLineFreeCharge", 22),
          ("subscriberLineFreeNoCharge", 23),
          ("subscriberLineOutOfService", 24),
          ("unallocatedNumber", 21))
    )


_AccPstnBckGenGB_Type.__name__ = "Integer32"
_AccPstnBckGenGB_Object = MibScalar
accPstnBckGenGB = _AccPstnBckGenGB_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 11),
    _AccPstnBckGenGB_Type()
)
accPstnBckGenGB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnBckGenGB.setStatus("mandatory")


class _AccPstnBckGenGC_Type(Integer32):
    """Custom type accPstnBckGenGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              18,
              19,
              20,
              21,
              22,
              200)
        )
    )
    namedValues = NamedValues(
        *(("congestionC", 20),
          ("sendFirstCalledDigit", 18),
          ("sendGroupB", 19),
          ("sendNextCalledDigit", 21),
          ("sendNextCallingDigit", 17),
          ("sendSameCalledDigit", 22),
          ("spare", 200))
    )


_AccPstnBckGenGC_Type.__name__ = "Integer32"
_AccPstnBckGenGC_Object = MibScalar
accPstnBckGenGC = _AccPstnBckGenGC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 12),
    _AccPstnBckGenGC_Type()
)
accPstnBckGenGC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnBckGenGC.setStatus("mandatory")
_AccPstnTableDef_Type = Integer32
_AccPstnTableDef_Object = MibScalar
accPstnTableDef = _AccPstnTableDef_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 13),
    _AccPstnTableDef_Type()
)
accPstnTableDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTableDef.setStatus("mandatory")
_AccPstnDisplayFGTableSet1_Type = Integer32
_AccPstnDisplayFGTableSet1_Object = MibScalar
accPstnDisplayFGTableSet1 = _AccPstnDisplayFGTableSet1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 14),
    _AccPstnDisplayFGTableSet1_Type()
)
accPstnDisplayFGTableSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFGTableSet1.setStatus("mandatory")
_AccPstnDisplayFGTableSet2_Type = Integer32
_AccPstnDisplayFGTableSet2_Object = MibScalar
accPstnDisplayFGTableSet2 = _AccPstnDisplayFGTableSet2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 15),
    _AccPstnDisplayFGTableSet2_Type()
)
accPstnDisplayFGTableSet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFGTableSet2.setStatus("mandatory")
_AccPstnDisplayFGTableSet3_Type = Integer32
_AccPstnDisplayFGTableSet3_Object = MibScalar
accPstnDisplayFGTableSet3 = _AccPstnDisplayFGTableSet3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 16),
    _AccPstnDisplayFGTableSet3_Type()
)
accPstnDisplayFGTableSet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFGTableSet3.setStatus("mandatory")
_AccPstnDisplayFGTableSet4_Type = Integer32
_AccPstnDisplayFGTableSet4_Object = MibScalar
accPstnDisplayFGTableSet4 = _AccPstnDisplayFGTableSet4_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 17),
    _AccPstnDisplayFGTableSet4_Type()
)
accPstnDisplayFGTableSet4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFGTableSet4.setStatus("mandatory")
_AccPstnDisplayFITableSet1_Type = Integer32
_AccPstnDisplayFITableSet1_Object = MibScalar
accPstnDisplayFITableSet1 = _AccPstnDisplayFITableSet1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 18),
    _AccPstnDisplayFITableSet1_Type()
)
accPstnDisplayFITableSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFITableSet1.setStatus("mandatory")
_AccPstnDisplayFITableSet2_Type = Integer32
_AccPstnDisplayFITableSet2_Object = MibScalar
accPstnDisplayFITableSet2 = _AccPstnDisplayFITableSet2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 19),
    _AccPstnDisplayFITableSet2_Type()
)
accPstnDisplayFITableSet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFITableSet2.setStatus("mandatory")
_AccPstnDisplayFITableSet3_Type = Integer32
_AccPstnDisplayFITableSet3_Object = MibScalar
accPstnDisplayFITableSet3 = _AccPstnDisplayFITableSet3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 20),
    _AccPstnDisplayFITableSet3_Type()
)
accPstnDisplayFITableSet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFITableSet3.setStatus("mandatory")
_AccPstnDisplayFITableSet4_Type = Integer32
_AccPstnDisplayFITableSet4_Object = MibScalar
accPstnDisplayFITableSet4 = _AccPstnDisplayFITableSet4_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 21),
    _AccPstnDisplayFITableSet4_Type()
)
accPstnDisplayFITableSet4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayFITableSet4.setStatus("mandatory")
_AccPstnDisplayBGTableSet1_Type = Integer32
_AccPstnDisplayBGTableSet1_Object = MibScalar
accPstnDisplayBGTableSet1 = _AccPstnDisplayBGTableSet1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 22),
    _AccPstnDisplayBGTableSet1_Type()
)
accPstnDisplayBGTableSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBGTableSet1.setStatus("mandatory")
_AccPstnDisplayBGTableSet2_Type = Integer32
_AccPstnDisplayBGTableSet2_Object = MibScalar
accPstnDisplayBGTableSet2 = _AccPstnDisplayBGTableSet2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 23),
    _AccPstnDisplayBGTableSet2_Type()
)
accPstnDisplayBGTableSet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBGTableSet2.setStatus("mandatory")
_AccPstnDisplayBGTableSet3_Type = Integer32
_AccPstnDisplayBGTableSet3_Object = MibScalar
accPstnDisplayBGTableSet3 = _AccPstnDisplayBGTableSet3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 24),
    _AccPstnDisplayBGTableSet3_Type()
)
accPstnDisplayBGTableSet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBGTableSet3.setStatus("mandatory")
_AccPstnDisplayBGTableSet4_Type = Integer32
_AccPstnDisplayBGTableSet4_Object = MibScalar
accPstnDisplayBGTableSet4 = _AccPstnDisplayBGTableSet4_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 25),
    _AccPstnDisplayBGTableSet4_Type()
)
accPstnDisplayBGTableSet4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBGTableSet4.setStatus("mandatory")
_AccPstnDisplayBITableSet1_Type = Integer32
_AccPstnDisplayBITableSet1_Object = MibScalar
accPstnDisplayBITableSet1 = _AccPstnDisplayBITableSet1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 26),
    _AccPstnDisplayBITableSet1_Type()
)
accPstnDisplayBITableSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBITableSet1.setStatus("mandatory")
_AccPstnDisplayBITableSet2_Type = Integer32
_AccPstnDisplayBITableSet2_Object = MibScalar
accPstnDisplayBITableSet2 = _AccPstnDisplayBITableSet2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 27),
    _AccPstnDisplayBITableSet2_Type()
)
accPstnDisplayBITableSet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBITableSet2.setStatus("mandatory")
_AccPstnDisplayBITableSet3_Type = Integer32
_AccPstnDisplayBITableSet3_Object = MibScalar
accPstnDisplayBITableSet3 = _AccPstnDisplayBITableSet3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 28),
    _AccPstnDisplayBITableSet3_Type()
)
accPstnDisplayBITableSet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBITableSet3.setStatus("mandatory")
_AccPstnDisplayBITableSet4_Type = Integer32
_AccPstnDisplayBITableSet4_Object = MibScalar
accPstnDisplayBITableSet4 = _AccPstnDisplayBITableSet4_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 2, 29),
    _AccPstnDisplayBITableSet4_Type()
)
accPstnDisplayBITableSet4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnDisplayBITableSet4.setStatus("mandatory")
_AccPstnTTIndex_Type = Integer32
_AccPstnTTIndex_Object = MibScalar
accPstnTTIndex = _AccPstnTTIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 3, 3),
    _AccPstnTTIndex_Type()
)
accPstnTTIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTTIndex.setStatus("mandatory")
_AccDTMF_ObjectIdentity = ObjectIdentity
accDTMF = _AccDTMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4)
)
_AccDTMFo_ObjectIdentity = ObjectIdentity
accDTMFo = _AccDTMFo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1)
)
_AccDTMFoo_ObjectIdentity = ObjectIdentity
accDTMFoo = _AccDTMFoo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1)
)


class _AccPstnTabSigDtCpEnd_Type(Integer32):
    """Custom type accPstnTabSigDtCpEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ringbackbusy", 2))
    )


_AccPstnTabSigDtCpEnd_Type.__name__ = "Integer32"
_AccPstnTabSigDtCpEnd_Object = MibScalar
accPstnTabSigDtCpEnd = _AccPstnTabSigDtCpEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 1),
    _AccPstnTabSigDtCpEnd_Type()
)
accPstnTabSigDtCpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtCpEnd.setStatus("mandatory")


class _AccPstnTabSigDtCpSt_Type(Integer32):
    """Custom type accPstnTabSigDtCpSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial", 2),
          ("none", 1))
    )


_AccPstnTabSigDtCpSt_Type.__name__ = "Integer32"
_AccPstnTabSigDtCpSt_Object = MibScalar
accPstnTabSigDtCpSt = _AccPstnTabSigDtCpSt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 2),
    _AccPstnTabSigDtCpSt_Type()
)
accPstnTabSigDtCpSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtCpSt.setStatus("mandatory")
_AccPstnTabSigDtCpTo_Type = Integer32
_AccPstnTabSigDtCpTo_Object = MibScalar
accPstnTabSigDtCpTo = _AccPstnTabSigDtCpTo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 3),
    _AccPstnTabSigDtCpTo_Type()
)
accPstnTabSigDtCpTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtCpTo.setStatus("mandatory")
_AccPstnTabSigDtDt_Type = Integer32
_AccPstnTabSigDtDt_Object = MibScalar
accPstnTabSigDtDt = _AccPstnTabSigDtDt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 4),
    _AccPstnTabSigDtDt_Type()
)
accPstnTabSigDtDt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtDt.setStatus("mandatory")


class _AccPstnTabSigDtIbCpSt_Type(Integer32):
    """Custom type accPstnTabSigDtIbCpSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial", 2),
          ("none", 1))
    )


_AccPstnTabSigDtIbCpSt_Type.__name__ = "Integer32"
_AccPstnTabSigDtIbCpSt_Object = MibScalar
accPstnTabSigDtIbCpSt = _AccPstnTabSigDtIbCpSt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 5),
    _AccPstnTabSigDtIbCpSt_Type()
)
accPstnTabSigDtIbCpSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtIbCpSt.setStatus("mandatory")
_AccPstnTabSigDtIbCpTp_Type = Integer32
_AccPstnTabSigDtIbCpTp_Object = MibScalar
accPstnTabSigDtIbCpTp = _AccPstnTabSigDtIbCpTp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 6),
    _AccPstnTabSigDtIbCpTp_Type()
)
accPstnTabSigDtIbCpTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtIbCpTp.setStatus("mandatory")
_AccPstnTabSigDtPm_Type = Integer32
_AccPstnTabSigDtPm_Object = MibScalar
accPstnTabSigDtPm = _AccPstnTabSigDtPm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 7),
    _AccPstnTabSigDtPm_Type()
)
accPstnTabSigDtPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtPm.setStatus("mandatory")
_AccPstnTabSigDtPmCo_Type = Integer32
_AccPstnTabSigDtPmCo_Object = MibScalar
accPstnTabSigDtPmCo = _AccPstnTabSigDtPmCo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 8),
    _AccPstnTabSigDtPmCo_Type()
)
accPstnTabSigDtPmCo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtPmCo.setStatus("mandatory")
_AccPstnTabSigDtSt_Type = Integer32
_AccPstnTabSigDtSt_Object = MibScalar
accPstnTabSigDtSt = _AccPstnTabSigDtSt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 9),
    _AccPstnTabSigDtSt_Type()
)
accPstnTabSigDtSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtSt.setStatus("mandatory")
_AccPstnTabSigDtHiPwr_Type = Integer32
_AccPstnTabSigDtHiPwr_Object = MibScalar
accPstnTabSigDtHiPwr = _AccPstnTabSigDtHiPwr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 10),
    _AccPstnTabSigDtHiPwr_Type()
)
accPstnTabSigDtHiPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtHiPwr.setStatus("mandatory")
_AccPstnTabSigDtLoPwr_Type = Integer32
_AccPstnTabSigDtLoPwr_Object = MibScalar
accPstnTabSigDtLoPwr = _AccPstnTabSigDtLoPwr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 11),
    _AccPstnTabSigDtLoPwr_Type()
)
accPstnTabSigDtLoPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtLoPwr.setStatus("mandatory")
_AccPstnTabSigDtOffTime_Type = Integer32
_AccPstnTabSigDtOffTime_Object = MibScalar
accPstnTabSigDtOffTime = _AccPstnTabSigDtOffTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 12),
    _AccPstnTabSigDtOffTime_Type()
)
accPstnTabSigDtOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtOffTime.setStatus("mandatory")
_AccPstnTabSigDtOnTime_Type = Integer32
_AccPstnTabSigDtOnTime_Object = MibScalar
accPstnTabSigDtOnTime = _AccPstnTabSigDtOnTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 4, 1, 1, 13),
    _AccPstnTabSigDtOnTime_Type()
)
accPstnTabSigDtOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDtOnTime.setStatus("mandatory")
_AccDPSig_ObjectIdentity = ObjectIdentity
accDPSig = _AccDPSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5)
)
_AccDPSigo_ObjectIdentity = ObjectIdentity
accDPSigo = _AccDPSigo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1)
)
_AccDPSigoo_ObjectIdentity = ObjectIdentity
accDPSigoo = _AccDPSigoo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1)
)


class _AccPstnTabSigDpCpEnd_Type(Integer32):
    """Custom type accPstnTabSigDpCpEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ringbackbusy", 2))
    )


_AccPstnTabSigDpCpEnd_Type.__name__ = "Integer32"
_AccPstnTabSigDpCpEnd_Object = MibScalar
accPstnTabSigDpCpEnd = _AccPstnTabSigDpCpEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 1),
    _AccPstnTabSigDpCpEnd_Type()
)
accPstnTabSigDpCpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpCpEnd.setStatus("mandatory")


class _AccPstnTabSigDpCpSt_Type(Integer32):
    """Custom type accPstnTabSigDpCpSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial", 2),
          ("none", 1))
    )


_AccPstnTabSigDpCpSt_Type.__name__ = "Integer32"
_AccPstnTabSigDpCpSt_Object = MibScalar
accPstnTabSigDpCpSt = _AccPstnTabSigDpCpSt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 2),
    _AccPstnTabSigDpCpSt_Type()
)
accPstnTabSigDpCpSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpCpSt.setStatus("mandatory")
_AccPstnTabSigDpCpTo_Type = Integer32
_AccPstnTabSigDpCpTo_Object = MibScalar
accPstnTabSigDpCpTo = _AccPstnTabSigDpCpTo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 3),
    _AccPstnTabSigDpCpTo_Type()
)
accPstnTabSigDpCpTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpCpTo.setStatus("mandatory")
_AccPstnTabSigDpDt_Type = Integer32
_AccPstnTabSigDpDt_Object = MibScalar
accPstnTabSigDpDt = _AccPstnTabSigDpDt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 4),
    _AccPstnTabSigDpDt_Type()
)
accPstnTabSigDpDt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpDt.setStatus("mandatory")
_AccPstnTabSigDpPm_Type = Integer32
_AccPstnTabSigDpPm_Object = MibScalar
accPstnTabSigDpPm = _AccPstnTabSigDpPm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 5),
    _AccPstnTabSigDpPm_Type()
)
accPstnTabSigDpPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpPm.setStatus("mandatory")
_AccPstnTabSigDpPmCo_Type = Integer32
_AccPstnTabSigDpPmCo_Object = MibScalar
accPstnTabSigDpPmCo = _AccPstnTabSigDpPmCo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 6),
    _AccPstnTabSigDpPmCo_Type()
)
accPstnTabSigDpPmCo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpPmCo.setStatus("mandatory")
_AccPstnTabSigDpBrkTime_Type = Integer32
_AccPstnTabSigDpBrkTime_Object = MibScalar
accPstnTabSigDpBrkTime = _AccPstnTabSigDpBrkTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 7),
    _AccPstnTabSigDpBrkTime_Type()
)
accPstnTabSigDpBrkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpBrkTime.setStatus("mandatory")
_AccPstnTabSigDpIdTime_Type = Integer32
_AccPstnTabSigDpIdTime_Object = MibScalar
accPstnTabSigDpIdTime = _AccPstnTabSigDpIdTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 8),
    _AccPstnTabSigDpIdTime_Type()
)
accPstnTabSigDpIdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpIdTime.setStatus("mandatory")
_AccPstnTabSigDpMkTime_Type = Integer32
_AccPstnTabSigDpMkTime_Object = MibScalar
accPstnTabSigDpMkTime = _AccPstnTabSigDpMkTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 9),
    _AccPstnTabSigDpMkTime_Type()
)
accPstnTabSigDpMkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpMkTime.setStatus("mandatory")
_AccPstnTabSigDpSt_Type = Integer32
_AccPstnTabSigDpSt_Object = MibScalar
accPstnTabSigDpSt = _AccPstnTabSigDpSt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 3, 5, 1, 1, 10),
    _AccPstnTabSigDpSt_Type()
)
accPstnTabSigDpSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSigDpSt.setStatus("mandatory")
_AccPstnTabSigGenT_ObjectIdentity = ObjectIdentity
accPstnTabSigGenT = _AccPstnTabSigGenT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4)
)
_AccPstnTabLineTrace_Type = Integer32
_AccPstnTabLineTrace_Object = MibScalar
accPstnTabLineTrace = _AccPstnTabLineTrace_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 1),
    _AccPstnTabLineTrace_Type()
)
accPstnTabLineTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabLineTrace.setStatus("mandatory")


class _AccPstnTabSupType_Type(Integer32):
    """Custom type accPstnTabSupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 2),
          ("none", 3),
          ("r2", 1))
    )


_AccPstnTabSupType_Type.__name__ = "Integer32"
_AccPstnTabSupType_Object = MibScalar
accPstnTabSupType = _AccPstnTabSupType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 2),
    _AccPstnTabSupType_Type()
)
accPstnTabSupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupType.setStatus("mandatory")
_AccPstnSupGen_ObjectIdentity = ObjectIdentity
accPstnSupGen = _AccPstnSupGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4)
)
_AccEMLinSup_ObjectIdentity = ObjectIdentity
accEMLinSup = _AccEMLinSup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1)
)
_AccEMLinSupo_ObjectIdentity = ObjectIdentity
accEMLinSupo = _AccEMLinSupo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1)
)
_AccPstnTabSupEmDsOutStDly_Type = Integer32
_AccPstnTabSupEmDsOutStDly_Object = MibScalar
accPstnTabSupEmDsOutStDly = _AccPstnTabSupEmDsOutStDly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 1),
    _AccPstnTabSupEmDsOutStDly_Type()
)
accPstnTabSupEmDsOutStDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmDsOutStDly.setStatus("mandatory")


class _AccPstnTabSupEmGl_Type(Integer32):
    """Custom type accPstnTabSupEmGl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backoff", 1),
          ("proceed", 2))
    )


_AccPstnTabSupEmGl_Type.__name__ = "Integer32"
_AccPstnTabSupEmGl_Object = MibScalar
accPstnTabSupEmGl = _AccPstnTabSupEmGl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 2),
    _AccPstnTabSupEmGl_Type()
)
accPstnTabSupEmGl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmGl.setStatus("mandatory")
_AccPstnTabSupEmImOutStDly_Type = Integer32
_AccPstnTabSupEmImOutStDly_Object = MibScalar
accPstnTabSupEmImOutStDly = _AccPstnTabSupEmImOutStDly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 3),
    _AccPstnTabSupEmImOutStDly_Type()
)
accPstnTabSupEmImOutStDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmImOutStDly.setStatus("mandatory")
_AccPstnTabSupEmWiInDur_Type = Integer32
_AccPstnTabSupEmWiInDur_Object = MibScalar
accPstnTabSupEmWiInDur = _AccPstnTabSupEmWiInDur_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 4),
    _AccPstnTabSupEmWiInDur_Type()
)
accPstnTabSupEmWiInDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmWiInDur.setStatus("mandatory")
_AccPstnTabSupEmWiOutEndTo_Type = Integer32
_AccPstnTabSupEmWiOutEndTo_Object = MibScalar
accPstnTabSupEmWiOutEndTo = _AccPstnTabSupEmWiOutEndTo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 5),
    _AccPstnTabSupEmWiOutEndTo_Type()
)
accPstnTabSupEmWiOutEndTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmWiOutEndTo.setStatus("mandatory")
_AccPstnTabSupEmWiOutStDly_Type = Integer32
_AccPstnTabSupEmWiOutStDly_Object = MibScalar
accPstnTabSupEmWiOutStDly = _AccPstnTabSupEmWiOutStDly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 6),
    _AccPstnTabSupEmWiOutStDly_Type()
)
accPstnTabSupEmWiOutStDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmWiOutStDly.setStatus("mandatory")
_AccPstnTabSupEmWiOutStTo_Type = Integer32
_AccPstnTabSupEmWiOutStTo_Object = MibScalar
accPstnTabSupEmWiOutStTo = _AccPstnTabSupEmWiOutStTo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 7),
    _AccPstnTabSupEmWiOutStTo_Type()
)
accPstnTabSupEmWiOutStTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmWiOutStTo.setStatus("mandatory")


class _AccPstnTabSupInMode_Type(Integer32):
    """Custom type accPstnTabSupInMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delayed", 3),
          ("immediate", 1),
          ("wink", 2))
    )


_AccPstnTabSupInMode_Type.__name__ = "Integer32"
_AccPstnTabSupInMode_Object = MibScalar
accPstnTabSupInMode = _AccPstnTabSupInMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 8),
    _AccPstnTabSupInMode_Type()
)
accPstnTabSupInMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupInMode.setStatus("mandatory")


class _AccPstnTabSupOutMode_Type(Integer32):
    """Custom type accPstnTabSupOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delayed", 3),
          ("immediate", 1),
          ("wink", 2))
    )


_AccPstnTabSupOutMode_Type.__name__ = "Integer32"
_AccPstnTabSupOutMode_Object = MibScalar
accPstnTabSupOutMode = _AccPstnTabSupOutMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 9),
    _AccPstnTabSupOutMode_Type()
)
accPstnTabSupOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupOutMode.setStatus("mandatory")
_AccPstnTabSupEmDsInDur_Type = Integer32
_AccPstnTabSupEmDsInDur_Object = MibScalar
accPstnTabSupEmDsInDur = _AccPstnTabSupEmDsInDur_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 11),
    _AccPstnTabSupEmDsInDur_Type()
)
accPstnTabSupEmDsInDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmDsInDur.setStatus("mandatory")
_AccPstnTabSupEmDsOutEndTo_Type = Integer32
_AccPstnTabSupEmDsOutEndTo_Object = MibScalar
accPstnTabSupEmDsOutEndTo = _AccPstnTabSupEmDsOutEndTo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 12),
    _AccPstnTabSupEmDsOutEndTo_Type()
)
accPstnTabSupEmDsOutEndTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmDsOutEndTo.setStatus("mandatory")
_AccPstnTabSupEmDsOutStTo_Type = Integer32
_AccPstnTabSupEmDsOutStTo_Object = MibScalar
accPstnTabSupEmDsOutStTo = _AccPstnTabSupEmDsOutStTo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 1, 1, 13),
    _AccPstnTabSupEmDsOutStTo_Type()
)
accPstnTabSupEmDsOutStTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupEmDsOutStTo.setStatus("mandatory")
_AccR2LinSupoo_ObjectIdentity = ObjectIdentity
accR2LinSupoo = _AccR2LinSupoo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3)
)
_AccPstnTabSupR2AnAnsDly_Type = Integer32
_AccPstnTabSupR2AnAnsDly_Object = MibScalar
accPstnTabSupR2AnAnsDly = _AccPstnTabSupR2AnAnsDly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 1),
    _AccPstnTabSupR2AnAnsDly_Type()
)
accPstnTabSupR2AnAnsDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2AnAnsDly.setStatus("mandatory")


class _AccPstnTabSupR2AnInPat_Type(Integer32):
    """Custom type accPstnTabSupR2AnInPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2AnInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2AnInPat_Object = MibScalar
accPstnTabSupR2AnInPat = _AccPstnTabSupR2AnInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 2),
    _AccPstnTabSupR2AnInPat_Type()
)
accPstnTabSupR2AnInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2AnInPat.setStatus("mandatory")


class _AccPstnTabSupR2AnOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2AnOutPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2AnOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2AnOutPat_Object = MibScalar
accPstnTabSupR2AnOutPat = _AccPstnTabSupR2AnOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 3),
    _AccPstnTabSupR2AnOutPat_Type()
)
accPstnTabSupR2AnOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2AnOutPat.setStatus("mandatory")
_AccPstnTabSupR2AnRecTime_Type = Integer32
_AccPstnTabSupR2AnRecTime_Object = MibScalar
accPstnTabSupR2AnRecTime = _AccPstnTabSupR2AnRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 4),
    _AccPstnTabSupR2AnRecTime_Type()
)
accPstnTabSupR2AnRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2AnRecTime.setStatus("mandatory")


class _AccPstnTabSupR2BlInPat_Type(Integer32):
    """Custom type accPstnTabSupR2BlInPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2BlInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2BlInPat_Object = MibScalar
accPstnTabSupR2BlInPat = _AccPstnTabSupR2BlInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 5),
    _AccPstnTabSupR2BlInPat_Type()
)
accPstnTabSupR2BlInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2BlInPat.setStatus("mandatory")


class _AccPstnTabSupR2BlOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2BlOutPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2BlOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2BlOutPat_Object = MibScalar
accPstnTabSupR2BlOutPat = _AccPstnTabSupR2BlOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 6),
    _AccPstnTabSupR2BlOutPat_Type()
)
accPstnTabSupR2BlOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2BlOutPat.setStatus("mandatory")
_AccPstnTabSupR2BlRecTime_Type = Integer32
_AccPstnTabSupR2BlRecTime_Object = MibScalar
accPstnTabSupR2BlRecTime = _AccPstnTabSupR2BlRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 7),
    _AccPstnTabSupR2BlRecTime_Type()
)
accPstnTabSupR2BlRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2BlRecTime.setStatus("mandatory")
_AccPstnTabSupR2CbFcbTime_Type = Integer32
_AccPstnTabSupR2CbFcbTime_Object = MibScalar
accPstnTabSupR2CbFcbTime = _AccPstnTabSupR2CbFcbTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 8),
    _AccPstnTabSupR2CbFcbTime_Type()
)
accPstnTabSupR2CbFcbTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2CbFcbTime.setStatus("mandatory")


class _AccPstnTabSupR2CbInPat_Type(Integer32):
    """Custom type accPstnTabSupR2CbInPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2CbInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2CbInPat_Object = MibScalar
accPstnTabSupR2CbInPat = _AccPstnTabSupR2CbInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 9),
    _AccPstnTabSupR2CbInPat_Type()
)
accPstnTabSupR2CbInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2CbInPat.setStatus("mandatory")


class _AccPstnTabSupR2CbOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2CbOutPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2CbOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2CbOutPat_Object = MibScalar
accPstnTabSupR2CbOutPat = _AccPstnTabSupR2CbOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 10),
    _AccPstnTabSupR2CbOutPat_Type()
)
accPstnTabSupR2CbOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2CbOutPat.setStatus("mandatory")
_AccPstnTabSupR2CbRecTime_Type = Integer32
_AccPstnTabSupR2CbRecTime_Object = MibScalar
accPstnTabSupR2CbRecTime = _AccPstnTabSupR2CbRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 11),
    _AccPstnTabSupR2CbRecTime_Type()
)
accPstnTabSupR2CbRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2CbRecTime.setStatus("mandatory")


class _AccPstnTabSupR2CfInPat_Type(Integer32):
    """Custom type accPstnTabSupR2CfInPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2CfInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2CfInPat_Object = MibScalar
accPstnTabSupR2CfInPat = _AccPstnTabSupR2CfInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 12),
    _AccPstnTabSupR2CfInPat_Type()
)
accPstnTabSupR2CfInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2CfInPat.setStatus("mandatory")


class _AccPstnTabSupR2CfOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2CfOutPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2CfOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2CfOutPat_Object = MibScalar
accPstnTabSupR2CfOutPat = _AccPstnTabSupR2CfOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 13),
    _AccPstnTabSupR2CfOutPat_Type()
)
accPstnTabSupR2CfOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2CfOutPat.setStatus("mandatory")
_AccPstnTabSupR2CfRecTime_Type = Integer32
_AccPstnTabSupR2CfRecTime_Object = MibScalar
accPstnTabSupR2CfRecTime = _AccPstnTabSupR2CfRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 14),
    _AccPstnTabSupR2CfRecTime_Type()
)
accPstnTabSupR2CfRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2CfRecTime.setStatus("mandatory")


class _AccPstnTabSupR2Gl_Type(Integer32):
    """Custom type accPstnTabSupR2Gl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backoff", 1),
          ("proceed", 2))
    )


_AccPstnTabSupR2Gl_Type.__name__ = "Integer32"
_AccPstnTabSupR2Gl_Object = MibScalar
accPstnTabSupR2Gl = _AccPstnTabSupR2Gl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 15),
    _AccPstnTabSupR2Gl_Type()
)
accPstnTabSupR2Gl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2Gl.setStatus("mandatory")


class _AccPstnTabSupR2IdInPat_Type(Integer32):
    """Custom type accPstnTabSupR2IdInPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2IdInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2IdInPat_Object = MibScalar
accPstnTabSupR2IdInPat = _AccPstnTabSupR2IdInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 16),
    _AccPstnTabSupR2IdInPat_Type()
)
accPstnTabSupR2IdInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2IdInPat.setStatus("mandatory")


class _AccPstnTabSupR2IdOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2IdOutPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2IdOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2IdOutPat_Object = MibScalar
accPstnTabSupR2IdOutPat = _AccPstnTabSupR2IdOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 17),
    _AccPstnTabSupR2IdOutPat_Type()
)
accPstnTabSupR2IdOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2IdOutPat.setStatus("mandatory")
_AccPstnTabSupR2IdRecTime_Type = Integer32
_AccPstnTabSupR2IdRecTime_Object = MibScalar
accPstnTabSupR2IdRecTime = _AccPstnTabSupR2IdRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 18),
    _AccPstnTabSupR2IdRecTime_Type()
)
accPstnTabSupR2IdRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2IdRecTime.setStatus("mandatory")


class _AccPstnTabSupR2Mask_Type(Integer32):
    """Custom type accPstnTabSupR2Mask based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2Mask_Type.__name__ = "Integer32"
_AccPstnTabSupR2Mask_Object = MibScalar
accPstnTabSupR2Mask = _AccPstnTabSupR2Mask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 19),
    _AccPstnTabSupR2Mask_Type()
)
accPstnTabSupR2Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2Mask.setStatus("mandatory")


class _AccPstnTabSupR2SaInPat_Type(Integer32):
    """Custom type accPstnTabSupR2SaInPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2SaInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2SaInPat_Object = MibScalar
accPstnTabSupR2SaInPat = _AccPstnTabSupR2SaInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 20),
    _AccPstnTabSupR2SaInPat_Type()
)
accPstnTabSupR2SaInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2SaInPat.setStatus("mandatory")


class _AccPstnTabSupR2SaOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2SaOutPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2SaOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2SaOutPat_Object = MibScalar
accPstnTabSupR2SaOutPat = _AccPstnTabSupR2SaOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 21),
    _AccPstnTabSupR2SaOutPat_Type()
)
accPstnTabSupR2SaOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2SaOutPat.setStatus("mandatory")
_AccPstnTabSupR2SaRecTime_Type = Integer32
_AccPstnTabSupR2SaRecTime_Object = MibScalar
accPstnTabSupR2SaRecTime = _AccPstnTabSupR2SaRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 22),
    _AccPstnTabSupR2SaRecTime_Type()
)
accPstnTabSupR2SaRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2SaRecTime.setStatus("mandatory")


class _AccPstnTabSupR2SzInPat_Type(Integer32):
    """Custom type accPstnTabSupR2SzInPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2SzInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2SzInPat_Object = MibScalar
accPstnTabSupR2SzInPat = _AccPstnTabSupR2SzInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 23),
    _AccPstnTabSupR2SzInPat_Type()
)
accPstnTabSupR2SzInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2SzInPat.setStatus("mandatory")


class _AccPstnTabSupR2SzOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2SzOutPat based on Integer32"""
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
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16))
    )


_AccPstnTabSupR2SzOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2SzOutPat_Object = MibScalar
accPstnTabSupR2SzOutPat = _AccPstnTabSupR2SzOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 24),
    _AccPstnTabSupR2SzOutPat_Type()
)
accPstnTabSupR2SzOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2SzOutPat.setStatus("mandatory")
_AccPstnTabSupR2SzRecTime_Type = Integer32
_AccPstnTabSupR2SzRecTime_Object = MibScalar
accPstnTabSupR2SzRecTime = _AccPstnTabSupR2SzRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 25),
    _AccPstnTabSupR2SzRecTime_Type()
)
accPstnTabSupR2SzRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2SzRecTime.setStatus("mandatory")


class _AccPstnTabSupR2MeInPat_Type(Integer32):
    """Custom type accPstnTabSupR2MeInPat based on Integer32"""
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
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16),
          ("disabled", 17))
    )


_AccPstnTabSupR2MeInPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2MeInPat_Object = MibScalar
accPstnTabSupR2MeInPat = _AccPstnTabSupR2MeInPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 26),
    _AccPstnTabSupR2MeInPat_Type()
)
accPstnTabSupR2MeInPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2MeInPat.setStatus("mandatory")


class _AccPstnTabSupR2MeOutPat_Type(Integer32):
    """Custom type accPstnTabSupR2MeOutPat based on Integer32"""
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
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("b0000", 1),
          ("b0001", 2),
          ("b0010", 3),
          ("b0011", 4),
          ("b0100", 5),
          ("b0101", 6),
          ("b0110", 7),
          ("b0111", 8),
          ("b1000", 9),
          ("b1001", 10),
          ("b1010", 11),
          ("b1011", 12),
          ("b1100", 13),
          ("b1101", 14),
          ("b1110", 15),
          ("b1111", 16),
          ("disabled", 17))
    )


_AccPstnTabSupR2MeOutPat_Type.__name__ = "Integer32"
_AccPstnTabSupR2MeOutPat_Object = MibScalar
accPstnTabSupR2MeOutPat = _AccPstnTabSupR2MeOutPat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 27),
    _AccPstnTabSupR2MeOutPat_Type()
)
accPstnTabSupR2MeOutPat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2MeOutPat.setStatus("mandatory")
_AccPstnTabSupR2MeRecTime_Type = Integer32
_AccPstnTabSupR2MeRecTime_Object = MibScalar
accPstnTabSupR2MeRecTime = _AccPstnTabSupR2MeRecTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 28),
    _AccPstnTabSupR2MeRecTime_Type()
)
accPstnTabSupR2MeRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2MeRecTime.setStatus("mandatory")
_AccPstnTabSupR2MeDly_Type = Integer32
_AccPstnTabSupR2MeDly_Object = MibScalar
accPstnTabSupR2MeDly = _AccPstnTabSupR2MeDly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 29),
    _AccPstnTabSupR2MeDly_Type()
)
accPstnTabSupR2MeDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2MeDly.setStatus("mandatory")
_AccPstnTabSupR2MeOffTime_Type = Integer32
_AccPstnTabSupR2MeOffTime_Object = MibScalar
accPstnTabSupR2MeOffTime = _AccPstnTabSupR2MeOffTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 30),
    _AccPstnTabSupR2MeOffTime_Type()
)
accPstnTabSupR2MeOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2MeOffTime.setStatus("mandatory")
_AccPstnTabSupR2MeOnTime_Type = Integer32
_AccPstnTabSupR2MeOnTime_Object = MibScalar
accPstnTabSupR2MeOnTime = _AccPstnTabSupR2MeOnTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 4, 4, 3, 31),
    _AccPstnTabSupR2MeOnTime_Type()
)
accPstnTabSupR2MeOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabSupR2MeOnTime.setStatus("mandatory")
_AccMisc_ObjectIdentity = ObjectIdentity
accMisc = _AccMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 5)
)
_AccDsprmMessageLevel_Type = Integer32
_AccDsprmMessageLevel_Object = MibScalar
accDsprmMessageLevel = _AccDsprmMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 5, 1),
    _AccDsprmMessageLevel_Type()
)
accDsprmMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDsprmMessageLevel.setStatus("mandatory")
_AccPstnTabPstnDslIndex_Type = Integer32
_AccPstnTabPstnDslIndex_Object = MibScalar
accPstnTabPstnDslIndex = _AccPstnTabPstnDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 5, 2),
    _AccPstnTabPstnDslIndex_Type()
)
accPstnTabPstnDslIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnTabPstnDslIndex.setStatus("mandatory")
_AccPstnOperstatus_Type = Integer32
_AccPstnOperstatus_Object = MibScalar
accPstnOperstatus = _AccPstnOperstatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 8, 5, 3),
    _AccPstnOperstatus_Type()
)
accPstnOperstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPstnOperstatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accDsprmRelnqshFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7, 0, 1)
)
accDsprmRelnqshFailTrap.setObjects(
      *(("ACC-PSTN", "accDsprmTrapMsg"),
        ("IF-MIB", "ifIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDsprmRelnqshFailTrap.setStatus(
        ""
    )

accDsprmLdspNotInUseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7, 0, 2)
)
accDsprmLdspNotInUseTrap.setObjects(
      *(("ACC-PSTN", "accDsprmTrapMsg"),
        ("IF-MIB", "ifIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDsprmLdspNotInUseTrap.setStatus(
        ""
    )

accDsprmCucbErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7, 0, 3)
)
accDsprmCucbErrTrap.setObjects(
      *(("ACC-PSTN", "accDsprmTrapMsg"),
        ("IF-MIB", "ifIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDsprmCucbErrTrap.setStatus(
        ""
    )

accDsprmNoDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7, 0, 4)
)
accDsprmNoDataTrap.setObjects(
      *(("ACC-PSTN", "accDsprmTrapMsg"),
        ("IF-MIB", "ifIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDsprmNoDataTrap.setStatus(
        ""
    )

accDsprmMemAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7, 0, 5)
)
accDsprmMemAllocTrap.setObjects(
      *(("ACC-PSTN", "accDsprmTrapMsg"),
        ("IF-MIB", "ifIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDsprmMemAllocTrap.setStatus(
        ""
    )

accDsprmInvMplTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 69, 7, 0, 6)
)
accDsprmInvMplTrap.setObjects(
      *(("ACC-PSTN", "accDsprmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDsprmInvMplTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-PSTN",
    **{"accPstn": accPstn,
       "accPstnSubTable": accPstnSubTable,
       "accPstnSubTabEntry": accPstnSubTabEntry,
       "oPstnSubTabDslIndex": oPstnSubTabDslIndex,
       "oPstnSubTabSigSystem": oPstnSubTabSigSystem,
       "oPstnSubTabNumChannels": oPstnSubTabNumChannels,
       "oPstnSubTabAdminStatus": oPstnSubTabAdminStatus,
       "oPstnSubTabOperStatus": oPstnSubTabOperStatus,
       "oPstnSubTabMsgLevel": oPstnSubTabMsgLevel,
       "oPstnSubTabLastCause": oPstnSubTabLastCause,
       "oPstnSubTabNumberGroup": oPstnSubTabNumberGroup,
       "accPstnStatTable": accPstnStatTable,
       "accPstnStatEntry": accPstnStatEntry,
       "oPstnStatDslIndex": oPstnStatDslIndex,
       "oPstnStatCallsOriginated": oPstnStatCallsOriginated,
       "oPstnStatCallsOfferred": oPstnStatCallsOfferred,
       "oPstnStatCallsRouted": oPstnStatCallsRouted,
       "oPstnStatCallsAccepted": oPstnStatCallsAccepted,
       "oPstnStatCallsCompleted": oPstnStatCallsCompleted,
       "oPstnStatCallsCleared": oPstnStatCallsCleared,
       "accPstnCallTable": accPstnCallTable,
       "accPstnCallTableEntry": accPstnCallTableEntry,
       "oPstnCallTabDslIndex": oPstnCallTabDslIndex,
       "oPstnCallTabCallId": oPstnCallTabCallId,
       "oPstnCallTabOrigin": oPstnCallTabOrigin,
       "oPstnCallTabChannel": oPstnCallTabChannel,
       "oPstnCallTabEndpoint": oPstnCallTabEndpoint,
       "oPstnCallTabState": oPstnCallTabState,
       "oPstnCallTabCause": oPstnCallTabCause,
       "oPstnCallTabAddress": oPstnCallTabAddress,
       "oPstnCallTabInfoRate": oPstnCallTabInfoRate,
       "oPstnCallTabInfoType": oPstnCallTabInfoType,
       "oPstnCallTabDuration": oPstnCallTabDuration,
       "accPstnChanTable": accPstnChanTable,
       "accPstnChanTableEntry": accPstnChanTableEntry,
       "oPstnChanTabDslIndex": oPstnChanTabDslIndex,
       "oPstnChanTabChannel": oPstnChanTabChannel,
       "oPstnChanTabServState": oPstnChanTabServState,
       "oPstnChanTabChanState": oPstnChanTabChanState,
       "oPstnChanTabSlotMap": oPstnChanTabSlotMap,
       "accPstnRBSParamTable": accPstnRBSParamTable,
       "accPstnRBSParamTableEntry": accPstnRBSParamTableEntry,
       "oPstnRbsTabDslIndex": oPstnRbsTabDslIndex,
       "oPstnRbsTabSuprModeIn": oPstnRbsTabSuprModeIn,
       "oPstnRbsTabSuprModeOut": oPstnRbsTabSuprModeOut,
       "oPstnRbsTabRegnModeIn": oPstnRbsTabRegnModeIn,
       "oPstnRbsTabRegnModeOut": oPstnRbsTabRegnModeOut,
       "oPstnRbsTabPresModeIn": oPstnRbsTabPresModeIn,
       "oPstnRbsTabPresModeOut": oPstnRbsTabPresModeOut,
       "oPstnRbsTabGlareAction": oPstnRbsTabGlareAction,
       "oPstnRbsTabWoddDuration": oPstnRbsTabWoddDuration,
       "oPstnRbsTabWsddDetect": oPstnRbsTabWsddDetect,
       "oPstnRbsTabWesdDetect": oPstnRbsTabWesdDetect,
       "oPstnRbsTabEnblocDigits": oPstnRbsTabEnblocDigits,
       "oPstnRbsTabEnblocTimeout": oPstnRbsTabEnblocTimeout,
       "accPstnIntCasSupvParamTable": accPstnIntCasSupvParamTable,
       "accPstnIntCasSupvParamEntry": accPstnIntCasSupvParamEntry,
       "oPstnCasTabDslIndex": oPstnCasTabDslIndex,
       "oPstnCasTabSupvModeIn": oPstnCasTabSupvModeIn,
       "oPstnCasTabSupvModeOut": oPstnCasTabSupvModeOut,
       "oPstnCasTabSupvMask": oPstnCasTabSupvMask,
       "oPstnCasTabSupvIdlePatt": oPstnCasTabSupvIdlePatt,
       "oPstnCasTabSupvIdleTime": oPstnCasTabSupvIdleTime,
       "oPstnCasTabSupvSeizePatt": oPstnCasTabSupvSeizePatt,
       "oPstnCasTabSupvSeizeTime": oPstnCasTabSupvSeizeTime,
       "oPstnCasTabSupvSeizeAckPatt": oPstnCasTabSupvSeizeAckPatt,
       "oPstnCasTabSupvSeizeAckTime": oPstnCasTabSupvSeizeAckTime,
       "oPstnCasTabSupvAnswerPatt": oPstnCasTabSupvAnswerPatt,
       "oPstnCasTabSupvAnswerTime": oPstnCasTabSupvAnswerTime,
       "oPstnCasTabSupvClrForwPatt": oPstnCasTabSupvClrForwPatt,
       "oPstnCasTabSupvClrForwTime": oPstnCasTabSupvClrForwTime,
       "oPstnCasTabSupvClrBackPatt": oPstnCasTabSupvClrBackPatt,
       "oPstnCasTabSupvClrBackTime": oPstnCasTabSupvClrBackTime,
       "oPstnCasTabSupvBlockPatt": oPstnCasTabSupvBlockPatt,
       "oPstnCasTabSupvBlockTime": oPstnCasTabSupvBlockTime,
       "oPstnCasTabSupvMetPatt": oPstnCasTabSupvMetPatt,
       "oPstnCasTabSupvMetTime": oPstnCasTabSupvMetTime,
       "oPstnCasTabSupvMetDelay": oPstnCasTabSupvMetDelay,
       "oPstnCasTabSupvMetOn": oPstnCasTabSupvMetOn,
       "oPstnCasTabSupvMetOff": oPstnCasTabSupvMetOff,
       "oPstnCasTabSupvGlare": oPstnCasTabSupvGlare,
       "oPstnCasTabRegModeIn": oPstnCasTabRegModeIn,
       "oPstnCasTabRegModeOut": oPstnCasTabRegModeOut,
       "oPstnCasTabRegComp1Tone": oPstnCasTabRegComp1Tone,
       "oPstnCasTabRegComp1On": oPstnCasTabRegComp1On,
       "oPstnCasTabRegComp1Off": oPstnCasTabRegComp1Off,
       "oPstnCasTabRegComp2Tone": oPstnCasTabRegComp2Tone,
       "oPstnCasTabRegComp2On": oPstnCasTabRegComp2On,
       "oPstnCasTabRegComp2Off": oPstnCasTabRegComp2Off,
       "accDsprmTraps": accDsprmTraps,
       "accDsprmRelnqshFailTrap": accDsprmRelnqshFailTrap,
       "accDsprmLdspNotInUseTrap": accDsprmLdspNotInUseTrap,
       "accDsprmCucbErrTrap": accDsprmCucbErrTrap,
       "accDsprmNoDataTrap": accDsprmNoDataTrap,
       "accDsprmMemAllocTrap": accDsprmMemAllocTrap,
       "accDsprmInvMplTrap": accDsprmInvMplTrap,
       "accDsprmTrapMsg": accDsprmTrapMsg,
       "accNewLiberty": accNewLiberty,
       "accPstnTabSigGen": accPstnTabSigGen,
       "accPstnTabSigTrace": accPstnTabSigTrace,
       "accPstnTabSigType": accPstnTabSigType,
       "accPstnTabSigInType": accPstnTabSigInType,
       "accPstnTabSigOutType": accPstnTabSigOutType,
       "accPstnEtt": accPstnEtt,
       "accR2Sig": accR2Sig,
       "accR2Sigo": accR2Sigo,
       "accPstnTabSigR2CdDig": accPstnTabSigR2CdDig,
       "accPstnTabSigR2CnDig": accPstnTabSigR2CnDig,
       "accPstnTabSigR2ReqCpc": accPstnTabSigR2ReqCpc,
       "accPstnTabSigR2AdMo": accPstnTabSigR2AdMo,
       "accPstnTabSigR2CdInMode": accPstnTabSigR2CdInMode,
       "accPstnTabSigR2CdOutMode": accPstnTabSigR2CdOutMode,
       "accPstnTabSigR2CnInMode": accPstnTabSigR2CnInMode,
       "accPstnTabSigR2CnOutMode": accPstnTabSigR2CnOutMode,
       "accPstnTabSigR2RspInMode": accPstnTabSigR2RspInMode,
       "accPstnTabSigR2RspOutMode": accPstnTabSigR2RspOutMode,
       "accPstnTabSigR2ObCpc": accPstnTabSigR2ObCpc,
       "accPstnTabSigR2ObDflt": accPstnTabSigR2ObDflt,
       "accPstnTabSigR2ScDur": accPstnTabSigR2ScDur,
       "accPstnTabSigR2RspInDur": accPstnTabSigR2RspInDur,
       "accPstnTabSigR2RspOutDur": accPstnTabSigR2RspOutDur,
       "accPstnTabSigR2InDur": accPstnTabSigR2InDur,
       "accPstnTabSigR2OutDur": accPstnTabSigR2OutDur,
       "accPstnTabSigR2InHiPwr": accPstnTabSigR2InHiPwr,
       "accPstnTabSigR2InLoPwr": accPstnTabSigR2InLoPwr,
       "accPstnTabSigR2OutHiPwr": accPstnTabSigR2OutHiPwr,
       "accPstnTabSigR2OutLoPwr": accPstnTabSigR2OutLoPwr,
       "accPstnTableInt": accPstnTableInt,
       "accToneSupoo": accToneSupoo,
       "accPstnTable": accPstnTable,
       "accPstnSignal": accPstnSignal,
       "accPstnFwdIntGI": accPstnFwdIntGI,
       "accPstnFwdIntGII": accPstnFwdIntGII,
       "accPstnFwdGenGI": accPstnFwdGenGI,
       "accPstnFwdGenGII": accPstnFwdGenGII,
       "accPstnBckIntGA": accPstnBckIntGA,
       "accPstnBckIntGB": accPstnBckIntGB,
       "accPstnBckIntGC": accPstnBckIntGC,
       "accPstnBckGenGA": accPstnBckGenGA,
       "accPstnBckGenGB": accPstnBckGenGB,
       "accPstnBckGenGC": accPstnBckGenGC,
       "accPstnTableDef": accPstnTableDef,
       "accPstnDisplayFGTableSet1": accPstnDisplayFGTableSet1,
       "accPstnDisplayFGTableSet2": accPstnDisplayFGTableSet2,
       "accPstnDisplayFGTableSet3": accPstnDisplayFGTableSet3,
       "accPstnDisplayFGTableSet4": accPstnDisplayFGTableSet4,
       "accPstnDisplayFITableSet1": accPstnDisplayFITableSet1,
       "accPstnDisplayFITableSet2": accPstnDisplayFITableSet2,
       "accPstnDisplayFITableSet3": accPstnDisplayFITableSet3,
       "accPstnDisplayFITableSet4": accPstnDisplayFITableSet4,
       "accPstnDisplayBGTableSet1": accPstnDisplayBGTableSet1,
       "accPstnDisplayBGTableSet2": accPstnDisplayBGTableSet2,
       "accPstnDisplayBGTableSet3": accPstnDisplayBGTableSet3,
       "accPstnDisplayBGTableSet4": accPstnDisplayBGTableSet4,
       "accPstnDisplayBITableSet1": accPstnDisplayBITableSet1,
       "accPstnDisplayBITableSet2": accPstnDisplayBITableSet2,
       "accPstnDisplayBITableSet3": accPstnDisplayBITableSet3,
       "accPstnDisplayBITableSet4": accPstnDisplayBITableSet4,
       "accPstnTTIndex": accPstnTTIndex,
       "accDTMF": accDTMF,
       "accDTMFo": accDTMFo,
       "accDTMFoo": accDTMFoo,
       "accPstnTabSigDtCpEnd": accPstnTabSigDtCpEnd,
       "accPstnTabSigDtCpSt": accPstnTabSigDtCpSt,
       "accPstnTabSigDtCpTo": accPstnTabSigDtCpTo,
       "accPstnTabSigDtDt": accPstnTabSigDtDt,
       "accPstnTabSigDtIbCpSt": accPstnTabSigDtIbCpSt,
       "accPstnTabSigDtIbCpTp": accPstnTabSigDtIbCpTp,
       "accPstnTabSigDtPm": accPstnTabSigDtPm,
       "accPstnTabSigDtPmCo": accPstnTabSigDtPmCo,
       "accPstnTabSigDtSt": accPstnTabSigDtSt,
       "accPstnTabSigDtHiPwr": accPstnTabSigDtHiPwr,
       "accPstnTabSigDtLoPwr": accPstnTabSigDtLoPwr,
       "accPstnTabSigDtOffTime": accPstnTabSigDtOffTime,
       "accPstnTabSigDtOnTime": accPstnTabSigDtOnTime,
       "accDPSig": accDPSig,
       "accDPSigo": accDPSigo,
       "accDPSigoo": accDPSigoo,
       "accPstnTabSigDpCpEnd": accPstnTabSigDpCpEnd,
       "accPstnTabSigDpCpSt": accPstnTabSigDpCpSt,
       "accPstnTabSigDpCpTo": accPstnTabSigDpCpTo,
       "accPstnTabSigDpDt": accPstnTabSigDpDt,
       "accPstnTabSigDpPm": accPstnTabSigDpPm,
       "accPstnTabSigDpPmCo": accPstnTabSigDpPmCo,
       "accPstnTabSigDpBrkTime": accPstnTabSigDpBrkTime,
       "accPstnTabSigDpIdTime": accPstnTabSigDpIdTime,
       "accPstnTabSigDpMkTime": accPstnTabSigDpMkTime,
       "accPstnTabSigDpSt": accPstnTabSigDpSt,
       "accPstnTabSigGenT": accPstnTabSigGenT,
       "accPstnTabLineTrace": accPstnTabLineTrace,
       "accPstnTabSupType": accPstnTabSupType,
       "accPstnSupGen": accPstnSupGen,
       "accEMLinSup": accEMLinSup,
       "accEMLinSupo": accEMLinSupo,
       "accPstnTabSupEmDsOutStDly": accPstnTabSupEmDsOutStDly,
       "accPstnTabSupEmGl": accPstnTabSupEmGl,
       "accPstnTabSupEmImOutStDly": accPstnTabSupEmImOutStDly,
       "accPstnTabSupEmWiInDur": accPstnTabSupEmWiInDur,
       "accPstnTabSupEmWiOutEndTo": accPstnTabSupEmWiOutEndTo,
       "accPstnTabSupEmWiOutStDly": accPstnTabSupEmWiOutStDly,
       "accPstnTabSupEmWiOutStTo": accPstnTabSupEmWiOutStTo,
       "accPstnTabSupInMode": accPstnTabSupInMode,
       "accPstnTabSupOutMode": accPstnTabSupOutMode,
       "accPstnTabSupEmDsInDur": accPstnTabSupEmDsInDur,
       "accPstnTabSupEmDsOutEndTo": accPstnTabSupEmDsOutEndTo,
       "accPstnTabSupEmDsOutStTo": accPstnTabSupEmDsOutStTo,
       "accR2LinSupoo": accR2LinSupoo,
       "accPstnTabSupR2AnAnsDly": accPstnTabSupR2AnAnsDly,
       "accPstnTabSupR2AnInPat": accPstnTabSupR2AnInPat,
       "accPstnTabSupR2AnOutPat": accPstnTabSupR2AnOutPat,
       "accPstnTabSupR2AnRecTime": accPstnTabSupR2AnRecTime,
       "accPstnTabSupR2BlInPat": accPstnTabSupR2BlInPat,
       "accPstnTabSupR2BlOutPat": accPstnTabSupR2BlOutPat,
       "accPstnTabSupR2BlRecTime": accPstnTabSupR2BlRecTime,
       "accPstnTabSupR2CbFcbTime": accPstnTabSupR2CbFcbTime,
       "accPstnTabSupR2CbInPat": accPstnTabSupR2CbInPat,
       "accPstnTabSupR2CbOutPat": accPstnTabSupR2CbOutPat,
       "accPstnTabSupR2CbRecTime": accPstnTabSupR2CbRecTime,
       "accPstnTabSupR2CfInPat": accPstnTabSupR2CfInPat,
       "accPstnTabSupR2CfOutPat": accPstnTabSupR2CfOutPat,
       "accPstnTabSupR2CfRecTime": accPstnTabSupR2CfRecTime,
       "accPstnTabSupR2Gl": accPstnTabSupR2Gl,
       "accPstnTabSupR2IdInPat": accPstnTabSupR2IdInPat,
       "accPstnTabSupR2IdOutPat": accPstnTabSupR2IdOutPat,
       "accPstnTabSupR2IdRecTime": accPstnTabSupR2IdRecTime,
       "accPstnTabSupR2Mask": accPstnTabSupR2Mask,
       "accPstnTabSupR2SaInPat": accPstnTabSupR2SaInPat,
       "accPstnTabSupR2SaOutPat": accPstnTabSupR2SaOutPat,
       "accPstnTabSupR2SaRecTime": accPstnTabSupR2SaRecTime,
       "accPstnTabSupR2SzInPat": accPstnTabSupR2SzInPat,
       "accPstnTabSupR2SzOutPat": accPstnTabSupR2SzOutPat,
       "accPstnTabSupR2SzRecTime": accPstnTabSupR2SzRecTime,
       "accPstnTabSupR2MeInPat": accPstnTabSupR2MeInPat,
       "accPstnTabSupR2MeOutPat": accPstnTabSupR2MeOutPat,
       "accPstnTabSupR2MeRecTime": accPstnTabSupR2MeRecTime,
       "accPstnTabSupR2MeDly": accPstnTabSupR2MeDly,
       "accPstnTabSupR2MeOffTime": accPstnTabSupR2MeOffTime,
       "accPstnTabSupR2MeOnTime": accPstnTabSupR2MeOnTime,
       "accMisc": accMisc,
       "accDsprmMessageLevel": accDsprmMessageLevel,
       "accPstnTabPstnDslIndex": accPstnTabPstnDslIndex,
       "accPstnOperstatus": accPstnOperstatus}
)
