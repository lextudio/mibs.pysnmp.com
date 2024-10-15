# SNMP MIB module (Nortel-Magellan-Passport-DpnTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DpnTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:39 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint1,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint1",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpnGate_ObjectIdentity = ObjectIdentity
dpnGate = _DpnGate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61)
)
_DpnGateRowStatusTable_Object = MibTable
dpnGateRowStatusTable = _DpnGateRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1)
)
if mibBuilder.loadTexts:
    dpnGateRowStatusTable.setStatus("mandatory")
_DpnGateRowStatusEntry_Object = MibTableRow
dpnGateRowStatusEntry = _DpnGateRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1)
)
dpnGateRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateRowStatusEntry.setStatus("mandatory")
_DpnGateRowStatus_Type = RowStatus
_DpnGateRowStatus_Object = MibTableColumn
dpnGateRowStatus = _DpnGateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 1),
    _DpnGateRowStatus_Type()
)
dpnGateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateRowStatus.setStatus("mandatory")
_DpnGateComponentName_Type = DisplayString
_DpnGateComponentName_Object = MibTableColumn
dpnGateComponentName = _DpnGateComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 2),
    _DpnGateComponentName_Type()
)
dpnGateComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateComponentName.setStatus("mandatory")
_DpnGateStorageType_Type = StorageType
_DpnGateStorageType_Object = MibTableColumn
dpnGateStorageType = _DpnGateStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 4),
    _DpnGateStorageType_Type()
)
dpnGateStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateStorageType.setStatus("mandatory")


class _DpnGateIndex_Type(Integer32):
    """Custom type dpnGateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpnGateIndex_Type.__name__ = "Integer32"
_DpnGateIndex_Object = MibTableColumn
dpnGateIndex = _DpnGateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 1, 1, 10),
    _DpnGateIndex_Type()
)
dpnGateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpnGateIndex.setStatus("mandatory")
_DpnGateFwdStats_ObjectIdentity = ObjectIdentity
dpnGateFwdStats = _DpnGateFwdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3)
)
_DpnGateFwdStatsRowStatusTable_Object = MibTable
dpnGateFwdStatsRowStatusTable = _DpnGateFwdStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1)
)
if mibBuilder.loadTexts:
    dpnGateFwdStatsRowStatusTable.setStatus("mandatory")
_DpnGateFwdStatsRowStatusEntry_Object = MibTableRow
dpnGateFwdStatsRowStatusEntry = _DpnGateFwdStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1)
)
dpnGateFwdStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFwdStatsRowStatusEntry.setStatus("mandatory")
_DpnGateFwdStatsRowStatus_Type = RowStatus
_DpnGateFwdStatsRowStatus_Object = MibTableColumn
dpnGateFwdStatsRowStatus = _DpnGateFwdStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 1),
    _DpnGateFwdStatsRowStatus_Type()
)
dpnGateFwdStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFwdStatsRowStatus.setStatus("mandatory")
_DpnGateFwdStatsComponentName_Type = DisplayString
_DpnGateFwdStatsComponentName_Object = MibTableColumn
dpnGateFwdStatsComponentName = _DpnGateFwdStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 2),
    _DpnGateFwdStatsComponentName_Type()
)
dpnGateFwdStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFwdStatsComponentName.setStatus("mandatory")
_DpnGateFwdStatsStorageType_Type = StorageType
_DpnGateFwdStatsStorageType_Object = MibTableColumn
dpnGateFwdStatsStorageType = _DpnGateFwdStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 4),
    _DpnGateFwdStatsStorageType_Type()
)
dpnGateFwdStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFwdStatsStorageType.setStatus("mandatory")
_DpnGateFwdStatsIndex_Type = NonReplicated
_DpnGateFwdStatsIndex_Object = MibTableColumn
dpnGateFwdStatsIndex = _DpnGateFwdStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 1, 1, 10),
    _DpnGateFwdStatsIndex_Type()
)
dpnGateFwdStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpnGateFwdStatsIndex.setStatus("mandatory")
_DpnGateFwdStatsOperTable_Object = MibTable
dpnGateFwdStatsOperTable = _DpnGateFwdStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10)
)
if mibBuilder.loadTexts:
    dpnGateFwdStatsOperTable.setStatus("mandatory")
_DpnGateFwdStatsOperEntry_Object = MibTableRow
dpnGateFwdStatsOperEntry = _DpnGateFwdStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1)
)
dpnGateFwdStatsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFwdStatsOperEntry.setStatus("mandatory")
_DpnGateFwdStatsFwdPktFromIf_Type = PassportCounter64
_DpnGateFwdStatsFwdPktFromIf_Object = MibTableColumn
dpnGateFwdStatsFwdPktFromIf = _DpnGateFwdStatsFwdPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1, 1),
    _DpnGateFwdStatsFwdPktFromIf_Type()
)
dpnGateFwdStatsFwdPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFwdStatsFwdPktFromIf.setStatus("mandatory")
_DpnGateFwdStatsFwdDiscUnforwardFromIf_Type = PassportCounter64
_DpnGateFwdStatsFwdDiscUnforwardFromIf_Object = MibTableColumn
dpnGateFwdStatsFwdDiscUnforwardFromIf = _DpnGateFwdStatsFwdDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1, 2),
    _DpnGateFwdStatsFwdDiscUnforwardFromIf_Type()
)
dpnGateFwdStatsFwdDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFwdStatsFwdDiscUnforwardFromIf.setStatus("mandatory")
_DpnGateFwdStatsFwdOctetFromIf_Type = PassportCounter64
_DpnGateFwdStatsFwdOctetFromIf_Object = MibTableColumn
dpnGateFwdStatsFwdOctetFromIf = _DpnGateFwdStatsFwdOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 3, 10, 1, 3),
    _DpnGateFwdStatsFwdOctetFromIf_Type()
)
dpnGateFwdStatsFwdOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFwdStatsFwdOctetFromIf.setStatus("mandatory")
_DpnGateIfEntryTable_Object = MibTable
dpnGateIfEntryTable = _DpnGateIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100)
)
if mibBuilder.loadTexts:
    dpnGateIfEntryTable.setStatus("mandatory")
_DpnGateIfEntryEntry_Object = MibTableRow
dpnGateIfEntryEntry = _DpnGateIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100, 1)
)
dpnGateIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateIfEntryEntry.setStatus("mandatory")


class _DpnGateIfAdminStatus_Type(Integer32):
    """Custom type dpnGateIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_DpnGateIfAdminStatus_Type.__name__ = "Integer32"
_DpnGateIfAdminStatus_Object = MibTableColumn
dpnGateIfAdminStatus = _DpnGateIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100, 1, 1),
    _DpnGateIfAdminStatus_Type()
)
dpnGateIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateIfAdminStatus.setStatus("mandatory")


class _DpnGateIfIndex_Type(InterfaceIndex):
    """Custom type dpnGateIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DpnGateIfIndex_Type.__name__ = "InterfaceIndex"
_DpnGateIfIndex_Object = MibTableColumn
dpnGateIfIndex = _DpnGateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 100, 1, 2),
    _DpnGateIfIndex_Type()
)
dpnGateIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateIfIndex.setStatus("mandatory")
_DpnGateProvTable_Object = MibTable
dpnGateProvTable = _DpnGateProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101)
)
if mibBuilder.loadTexts:
    dpnGateProvTable.setStatus("mandatory")
_DpnGateProvEntry_Object = MibTableRow
dpnGateProvEntry = _DpnGateProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1)
)
dpnGateProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateProvEntry.setStatus("mandatory")


class _DpnGateExpectedRemoteNamsId_Type(Unsigned32):
    """Custom type dpnGateExpectedRemoteNamsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpnGateExpectedRemoteNamsId_Type.__name__ = "Unsigned32"
_DpnGateExpectedRemoteNamsId_Object = MibTableColumn
dpnGateExpectedRemoteNamsId = _DpnGateExpectedRemoteNamsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1, 1),
    _DpnGateExpectedRemoteNamsId_Type()
)
dpnGateExpectedRemoteNamsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateExpectedRemoteNamsId.setStatus("mandatory")


class _DpnGateRemoteValidationAction_Type(Integer32):
    """Custom type dpnGateRemoteValidationAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("continue", 0),
          ("disable", 1))
    )


_DpnGateRemoteValidationAction_Type.__name__ = "Integer32"
_DpnGateRemoteValidationAction_Object = MibTableColumn
dpnGateRemoteValidationAction = _DpnGateRemoteValidationAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1, 2),
    _DpnGateRemoteValidationAction_Type()
)
dpnGateRemoteValidationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateRemoteValidationAction.setStatus("mandatory")


class _DpnGateLinkType_Type(Integer32):
    """Custom type dpnGateLinkType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 0),
          ("dialIn", 3))
    )


_DpnGateLinkType_Type.__name__ = "Integer32"
_DpnGateLinkType_Object = MibTableColumn
dpnGateLinkType = _DpnGateLinkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 101, 1, 3),
    _DpnGateLinkType_Type()
)
dpnGateLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateLinkType.setStatus("mandatory")
_DpnGateOverridesTable_Object = MibTable
dpnGateOverridesTable = _DpnGateOverridesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102)
)
if mibBuilder.loadTexts:
    dpnGateOverridesTable.setStatus("mandatory")
_DpnGateOverridesEntry_Object = MibTableRow
dpnGateOverridesEntry = _DpnGateOverridesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1)
)
dpnGateOverridesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateOverridesEntry.setStatus("mandatory")


class _DpnGateOverrideTransmitSpeed_Type(Gauge32):
    """Custom type dpnGateOverrideTransmitSpeed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 4294967295),
    )


_DpnGateOverrideTransmitSpeed_Type.__name__ = "Gauge32"
_DpnGateOverrideTransmitSpeed_Object = MibTableColumn
dpnGateOverrideTransmitSpeed = _DpnGateOverrideTransmitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1, 1),
    _DpnGateOverrideTransmitSpeed_Type()
)
dpnGateOverrideTransmitSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateOverrideTransmitSpeed.setStatus("mandatory")


class _DpnGateOldOverrideRoundTripDelay_Type(Gauge32):
    """Custom type dpnGateOldOverrideRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_DpnGateOldOverrideRoundTripDelay_Type.__name__ = "Gauge32"
_DpnGateOldOverrideRoundTripDelay_Object = MibTableColumn
dpnGateOldOverrideRoundTripDelay = _DpnGateOldOverrideRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1, 2),
    _DpnGateOldOverrideRoundTripDelay_Type()
)
dpnGateOldOverrideRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateOldOverrideRoundTripDelay.setStatus("obsolete")


class _DpnGateOverrideRoundTripUsec_Type(FixedPoint1):
    """Custom type dpnGateOverrideRoundTripUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_DpnGateOverrideRoundTripUsec_Type.__name__ = "FixedPoint1"
_DpnGateOverrideRoundTripUsec_Object = MibTableColumn
dpnGateOverrideRoundTripUsec = _DpnGateOverrideRoundTripUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 102, 1, 3),
    _DpnGateOverrideRoundTripUsec_Type()
)
dpnGateOverrideRoundTripUsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateOverrideRoundTripUsec.setStatus("mandatory")
_DpnGateStateTable_Object = MibTable
dpnGateStateTable = _DpnGateStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103)
)
if mibBuilder.loadTexts:
    dpnGateStateTable.setStatus("mandatory")
_DpnGateStateEntry_Object = MibTableRow
dpnGateStateEntry = _DpnGateStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1)
)
dpnGateStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateStateEntry.setStatus("mandatory")


class _DpnGateAdminState_Type(Integer32):
    """Custom type dpnGateAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_DpnGateAdminState_Type.__name__ = "Integer32"
_DpnGateAdminState_Object = MibTableColumn
dpnGateAdminState = _DpnGateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 1),
    _DpnGateAdminState_Type()
)
dpnGateAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateAdminState.setStatus("mandatory")


class _DpnGateOperationalState_Type(Integer32):
    """Custom type dpnGateOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DpnGateOperationalState_Type.__name__ = "Integer32"
_DpnGateOperationalState_Object = MibTableColumn
dpnGateOperationalState = _DpnGateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 2),
    _DpnGateOperationalState_Type()
)
dpnGateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateOperationalState.setStatus("mandatory")


class _DpnGateUsageState_Type(Integer32):
    """Custom type dpnGateUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_DpnGateUsageState_Type.__name__ = "Integer32"
_DpnGateUsageState_Object = MibTableColumn
dpnGateUsageState = _DpnGateUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 3),
    _DpnGateUsageState_Type()
)
dpnGateUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUsageState.setStatus("mandatory")


class _DpnGateAvailabilityStatus_Type(OctetString):
    """Custom type dpnGateAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DpnGateAvailabilityStatus_Type.__name__ = "OctetString"
_DpnGateAvailabilityStatus_Object = MibTableColumn
dpnGateAvailabilityStatus = _DpnGateAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 4),
    _DpnGateAvailabilityStatus_Type()
)
dpnGateAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateAvailabilityStatus.setStatus("mandatory")


class _DpnGateProceduralStatus_Type(OctetString):
    """Custom type dpnGateProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateProceduralStatus_Type.__name__ = "OctetString"
_DpnGateProceduralStatus_Object = MibTableColumn
dpnGateProceduralStatus = _DpnGateProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 5),
    _DpnGateProceduralStatus_Type()
)
dpnGateProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateProceduralStatus.setStatus("mandatory")


class _DpnGateControlStatus_Type(OctetString):
    """Custom type dpnGateControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateControlStatus_Type.__name__ = "OctetString"
_DpnGateControlStatus_Object = MibTableColumn
dpnGateControlStatus = _DpnGateControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 6),
    _DpnGateControlStatus_Type()
)
dpnGateControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateControlStatus.setStatus("mandatory")


class _DpnGateAlarmStatus_Type(OctetString):
    """Custom type dpnGateAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateAlarmStatus_Type.__name__ = "OctetString"
_DpnGateAlarmStatus_Object = MibTableColumn
dpnGateAlarmStatus = _DpnGateAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 7),
    _DpnGateAlarmStatus_Type()
)
dpnGateAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateAlarmStatus.setStatus("mandatory")


class _DpnGateStandbyStatus_Type(Integer32):
    """Custom type dpnGateStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_DpnGateStandbyStatus_Type.__name__ = "Integer32"
_DpnGateStandbyStatus_Object = MibTableColumn
dpnGateStandbyStatus = _DpnGateStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 8),
    _DpnGateStandbyStatus_Type()
)
dpnGateStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateStandbyStatus.setStatus("mandatory")


class _DpnGateUnknownStatus_Type(Integer32):
    """Custom type dpnGateUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DpnGateUnknownStatus_Type.__name__ = "Integer32"
_DpnGateUnknownStatus_Object = MibTableColumn
dpnGateUnknownStatus = _DpnGateUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 103, 1, 9),
    _DpnGateUnknownStatus_Type()
)
dpnGateUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUnknownStatus.setStatus("mandatory")
_DpnGateOperStatusTable_Object = MibTable
dpnGateOperStatusTable = _DpnGateOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 104)
)
if mibBuilder.loadTexts:
    dpnGateOperStatusTable.setStatus("mandatory")
_DpnGateOperStatusEntry_Object = MibTableRow
dpnGateOperStatusEntry = _DpnGateOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 104, 1)
)
dpnGateOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateOperStatusEntry.setStatus("mandatory")


class _DpnGateSnmpOperStatus_Type(Integer32):
    """Custom type dpnGateSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_DpnGateSnmpOperStatus_Type.__name__ = "Integer32"
_DpnGateSnmpOperStatus_Object = MibTableColumn
dpnGateSnmpOperStatus = _DpnGateSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 104, 1, 1),
    _DpnGateSnmpOperStatus_Type()
)
dpnGateSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateSnmpOperStatus.setStatus("mandatory")
_DpnGateOperTable_Object = MibTable
dpnGateOperTable = _DpnGateOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105)
)
if mibBuilder.loadTexts:
    dpnGateOperTable.setStatus("mandatory")
_DpnGateOperEntry_Object = MibTableRow
dpnGateOperEntry = _DpnGateOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1)
)
dpnGateOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateOperEntry.setStatus("mandatory")


class _DpnGateRemoteComponentName_Type(AsciiString):
    """Custom type dpnGateRemoteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 26),
    )


_DpnGateRemoteComponentName_Type.__name__ = "AsciiString"
_DpnGateRemoteComponentName_Object = MibTableColumn
dpnGateRemoteComponentName = _DpnGateRemoteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 1),
    _DpnGateRemoteComponentName_Type()
)
dpnGateRemoteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateRemoteComponentName.setStatus("mandatory")


class _DpnGateRemoteNamsMnemonic_Type(AsciiString):
    """Custom type dpnGateRemoteNamsMnemonic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_DpnGateRemoteNamsMnemonic_Type.__name__ = "AsciiString"
_DpnGateRemoteNamsMnemonic_Object = MibTableColumn
dpnGateRemoteNamsMnemonic = _DpnGateRemoteNamsMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 2),
    _DpnGateRemoteNamsMnemonic_Type()
)
dpnGateRemoteNamsMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateRemoteNamsMnemonic.setStatus("mandatory")


class _DpnGateLinkMode_Type(Integer32):
    """Custom type dpnGateLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkLink", 1),
          ("trunk", 0),
          ("unknown", 2))
    )


_DpnGateLinkMode_Type.__name__ = "Integer32"
_DpnGateLinkMode_Object = MibTableColumn
dpnGateLinkMode = _DpnGateLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 3),
    _DpnGateLinkMode_Type()
)
dpnGateLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateLinkMode.setStatus("mandatory")


class _DpnGateActivateReason_Type(Integer32):
    """Custom type dpnGateActivateReason based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bwod", 5),
          ("dbnl", 2),
          ("dedicated", 0),
          ("dialIn", 3),
          ("dnl", 1),
          ("unknown", 15))
    )


_DpnGateActivateReason_Type.__name__ = "Integer32"
_DpnGateActivateReason_Object = MibTableColumn
dpnGateActivateReason = _DpnGateActivateReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 105, 1, 4),
    _DpnGateActivateReason_Type()
)
dpnGateActivateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateActivateReason.setStatus("mandatory")
_DpnGateTransportTable_Object = MibTable
dpnGateTransportTable = _DpnGateTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106)
)
if mibBuilder.loadTexts:
    dpnGateTransportTable.setStatus("mandatory")
_DpnGateTransportEntry_Object = MibTableRow
dpnGateTransportEntry = _DpnGateTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1)
)
dpnGateTransportEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateTransportEntry.setStatus("mandatory")


class _DpnGateMeasuredSpeedToIf_Type(Gauge32):
    """Custom type dpnGateMeasuredSpeedToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DpnGateMeasuredSpeedToIf_Type.__name__ = "Gauge32"
_DpnGateMeasuredSpeedToIf_Object = MibTableColumn
dpnGateMeasuredSpeedToIf = _DpnGateMeasuredSpeedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 1),
    _DpnGateMeasuredSpeedToIf_Type()
)
dpnGateMeasuredSpeedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateMeasuredSpeedToIf.setStatus("mandatory")


class _DpnGateMeasuredRoundTripDelay_Type(Gauge32):
    """Custom type dpnGateMeasuredRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_DpnGateMeasuredRoundTripDelay_Type.__name__ = "Gauge32"
_DpnGateMeasuredRoundTripDelay_Object = MibTableColumn
dpnGateMeasuredRoundTripDelay = _DpnGateMeasuredRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 2),
    _DpnGateMeasuredRoundTripDelay_Type()
)
dpnGateMeasuredRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateMeasuredRoundTripDelay.setStatus("obsolete")


class _DpnGateMaxTxUnit_Type(Gauge32):
    """Custom type dpnGateMaxTxUnit based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpnGateMaxTxUnit_Type.__name__ = "Gauge32"
_DpnGateMaxTxUnit_Object = MibTableColumn
dpnGateMaxTxUnit = _DpnGateMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 3),
    _DpnGateMaxTxUnit_Type()
)
dpnGateMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateMaxTxUnit.setStatus("mandatory")


class _DpnGateMeasuredRoundTripDelayUsec_Type(FixedPoint1):
    """Custom type dpnGateMeasuredRoundTripDelayUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_DpnGateMeasuredRoundTripDelayUsec_Type.__name__ = "FixedPoint1"
_DpnGateMeasuredRoundTripDelayUsec_Object = MibTableColumn
dpnGateMeasuredRoundTripDelayUsec = _DpnGateMeasuredRoundTripDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 106, 1, 4),
    _DpnGateMeasuredRoundTripDelayUsec_Type()
)
dpnGateMeasuredRoundTripDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateMeasuredRoundTripDelayUsec.setStatus("mandatory")
_DpnGateStatsTable_Object = MibTable
dpnGateStatsTable = _DpnGateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107)
)
if mibBuilder.loadTexts:
    dpnGateStatsTable.setStatus("mandatory")
_DpnGateStatsEntry_Object = MibTableRow
dpnGateStatsEntry = _DpnGateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1)
)
dpnGateStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
)
if mibBuilder.loadTexts:
    dpnGateStatsEntry.setStatus("mandatory")
_DpnGatePktFromIf_Type = PassportCounter64
_DpnGatePktFromIf_Object = MibTableColumn
dpnGatePktFromIf = _DpnGatePktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 1),
    _DpnGatePktFromIf_Type()
)
dpnGatePktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGatePktFromIf.setStatus("mandatory")
_DpnGateTrunkPktFromIf_Type = Counter32
_DpnGateTrunkPktFromIf_Object = MibTableColumn
dpnGateTrunkPktFromIf = _DpnGateTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 2),
    _DpnGateTrunkPktFromIf_Type()
)
dpnGateTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateTrunkPktFromIf.setStatus("mandatory")
_DpnGateTrunkPktToIf_Type = Counter32
_DpnGateTrunkPktToIf_Object = MibTableColumn
dpnGateTrunkPktToIf = _DpnGateTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 3),
    _DpnGateTrunkPktToIf_Type()
)
dpnGateTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateTrunkPktToIf.setStatus("mandatory")
_DpnGateDiscardUnforward_Type = PassportCounter64
_DpnGateDiscardUnforward_Object = MibTableColumn
dpnGateDiscardUnforward = _DpnGateDiscardUnforward_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 4),
    _DpnGateDiscardUnforward_Type()
)
dpnGateDiscardUnforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateDiscardUnforward.setStatus("mandatory")
_DpnGateDiscardTrunkPktFromIf_Type = Counter32
_DpnGateDiscardTrunkPktFromIf_Object = MibTableColumn
dpnGateDiscardTrunkPktFromIf = _DpnGateDiscardTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 5),
    _DpnGateDiscardTrunkPktFromIf_Type()
)
dpnGateDiscardTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateDiscardTrunkPktFromIf.setStatus("mandatory")
_DpnGateStagingAttempts_Type = Counter32
_DpnGateStagingAttempts_Object = MibTableColumn
dpnGateStagingAttempts = _DpnGateStagingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 6),
    _DpnGateStagingAttempts_Type()
)
dpnGateStagingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateStagingAttempts.setStatus("mandatory")
_DpnGateDiscardTrunkPktToIf_Type = Counter32
_DpnGateDiscardTrunkPktToIf_Object = MibTableColumn
dpnGateDiscardTrunkPktToIf = _DpnGateDiscardTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 107, 1, 7),
    _DpnGateDiscardTrunkPktToIf_Type()
)
dpnGateDiscardTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateDiscardTrunkPktToIf.setStatus("mandatory")
_DpnTrunksMIB_ObjectIdentity = ObjectIdentity
dpnTrunksMIB = _DpnTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40)
)
_DpnTrunksGroup_ObjectIdentity = ObjectIdentity
dpnTrunksGroup = _DpnTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1)
)
_DpnTrunksGroupBE_ObjectIdentity = ObjectIdentity
dpnTrunksGroupBE = _DpnTrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1, 5)
)
_DpnTrunksGroupBE01_ObjectIdentity = ObjectIdentity
dpnTrunksGroupBE01 = _DpnTrunksGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1, 5, 2)
)
_DpnTrunksGroupBE01A_ObjectIdentity = ObjectIdentity
dpnTrunksGroupBE01A = _DpnTrunksGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 1, 5, 2, 2)
)
_DpnTrunksCapabilities_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilities = _DpnTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3)
)
_DpnTrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilitiesBE = _DpnTrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3, 5)
)
_DpnTrunksCapabilitiesBE01_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilitiesBE01 = _DpnTrunksCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3, 5, 2)
)
_DpnTrunksCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilitiesBE01A = _DpnTrunksCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 40, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DpnTrunksMIB",
    **{"dpnGate": dpnGate,
       "dpnGateRowStatusTable": dpnGateRowStatusTable,
       "dpnGateRowStatusEntry": dpnGateRowStatusEntry,
       "dpnGateRowStatus": dpnGateRowStatus,
       "dpnGateComponentName": dpnGateComponentName,
       "dpnGateStorageType": dpnGateStorageType,
       "dpnGateIndex": dpnGateIndex,
       "dpnGateFwdStats": dpnGateFwdStats,
       "dpnGateFwdStatsRowStatusTable": dpnGateFwdStatsRowStatusTable,
       "dpnGateFwdStatsRowStatusEntry": dpnGateFwdStatsRowStatusEntry,
       "dpnGateFwdStatsRowStatus": dpnGateFwdStatsRowStatus,
       "dpnGateFwdStatsComponentName": dpnGateFwdStatsComponentName,
       "dpnGateFwdStatsStorageType": dpnGateFwdStatsStorageType,
       "dpnGateFwdStatsIndex": dpnGateFwdStatsIndex,
       "dpnGateFwdStatsOperTable": dpnGateFwdStatsOperTable,
       "dpnGateFwdStatsOperEntry": dpnGateFwdStatsOperEntry,
       "dpnGateFwdStatsFwdPktFromIf": dpnGateFwdStatsFwdPktFromIf,
       "dpnGateFwdStatsFwdDiscUnforwardFromIf": dpnGateFwdStatsFwdDiscUnforwardFromIf,
       "dpnGateFwdStatsFwdOctetFromIf": dpnGateFwdStatsFwdOctetFromIf,
       "dpnGateIfEntryTable": dpnGateIfEntryTable,
       "dpnGateIfEntryEntry": dpnGateIfEntryEntry,
       "dpnGateIfAdminStatus": dpnGateIfAdminStatus,
       "dpnGateIfIndex": dpnGateIfIndex,
       "dpnGateProvTable": dpnGateProvTable,
       "dpnGateProvEntry": dpnGateProvEntry,
       "dpnGateExpectedRemoteNamsId": dpnGateExpectedRemoteNamsId,
       "dpnGateRemoteValidationAction": dpnGateRemoteValidationAction,
       "dpnGateLinkType": dpnGateLinkType,
       "dpnGateOverridesTable": dpnGateOverridesTable,
       "dpnGateOverridesEntry": dpnGateOverridesEntry,
       "dpnGateOverrideTransmitSpeed": dpnGateOverrideTransmitSpeed,
       "dpnGateOldOverrideRoundTripDelay": dpnGateOldOverrideRoundTripDelay,
       "dpnGateOverrideRoundTripUsec": dpnGateOverrideRoundTripUsec,
       "dpnGateStateTable": dpnGateStateTable,
       "dpnGateStateEntry": dpnGateStateEntry,
       "dpnGateAdminState": dpnGateAdminState,
       "dpnGateOperationalState": dpnGateOperationalState,
       "dpnGateUsageState": dpnGateUsageState,
       "dpnGateAvailabilityStatus": dpnGateAvailabilityStatus,
       "dpnGateProceduralStatus": dpnGateProceduralStatus,
       "dpnGateControlStatus": dpnGateControlStatus,
       "dpnGateAlarmStatus": dpnGateAlarmStatus,
       "dpnGateStandbyStatus": dpnGateStandbyStatus,
       "dpnGateUnknownStatus": dpnGateUnknownStatus,
       "dpnGateOperStatusTable": dpnGateOperStatusTable,
       "dpnGateOperStatusEntry": dpnGateOperStatusEntry,
       "dpnGateSnmpOperStatus": dpnGateSnmpOperStatus,
       "dpnGateOperTable": dpnGateOperTable,
       "dpnGateOperEntry": dpnGateOperEntry,
       "dpnGateRemoteComponentName": dpnGateRemoteComponentName,
       "dpnGateRemoteNamsMnemonic": dpnGateRemoteNamsMnemonic,
       "dpnGateLinkMode": dpnGateLinkMode,
       "dpnGateActivateReason": dpnGateActivateReason,
       "dpnGateTransportTable": dpnGateTransportTable,
       "dpnGateTransportEntry": dpnGateTransportEntry,
       "dpnGateMeasuredSpeedToIf": dpnGateMeasuredSpeedToIf,
       "dpnGateMeasuredRoundTripDelay": dpnGateMeasuredRoundTripDelay,
       "dpnGateMaxTxUnit": dpnGateMaxTxUnit,
       "dpnGateMeasuredRoundTripDelayUsec": dpnGateMeasuredRoundTripDelayUsec,
       "dpnGateStatsTable": dpnGateStatsTable,
       "dpnGateStatsEntry": dpnGateStatsEntry,
       "dpnGatePktFromIf": dpnGatePktFromIf,
       "dpnGateTrunkPktFromIf": dpnGateTrunkPktFromIf,
       "dpnGateTrunkPktToIf": dpnGateTrunkPktToIf,
       "dpnGateDiscardUnforward": dpnGateDiscardUnforward,
       "dpnGateDiscardTrunkPktFromIf": dpnGateDiscardTrunkPktFromIf,
       "dpnGateStagingAttempts": dpnGateStagingAttempts,
       "dpnGateDiscardTrunkPktToIf": dpnGateDiscardTrunkPktToIf,
       "dpnTrunksMIB": dpnTrunksMIB,
       "dpnTrunksGroup": dpnTrunksGroup,
       "dpnTrunksGroupBE": dpnTrunksGroupBE,
       "dpnTrunksGroupBE01": dpnTrunksGroupBE01,
       "dpnTrunksGroupBE01A": dpnTrunksGroupBE01A,
       "dpnTrunksCapabilities": dpnTrunksCapabilities,
       "dpnTrunksCapabilitiesBE": dpnTrunksCapabilitiesBE,
       "dpnTrunksCapabilitiesBE01": dpnTrunksCapabilitiesBE01,
       "dpnTrunksCapabilitiesBE01A": dpnTrunksCapabilitiesBE01A}
)
