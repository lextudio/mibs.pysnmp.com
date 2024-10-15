# SNMP MIB module (Nortel-MsCarrier-MscPassport-DpnTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DpnTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:16 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint1,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint1",
    "NonReplicated",
    "PassportCounter64")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscDpnGate_ObjectIdentity = ObjectIdentity
mscDpnGate = _MscDpnGate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61)
)
_MscDpnGateRowStatusTable_Object = MibTable
mscDpnGateRowStatusTable = _MscDpnGateRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 1)
)
if mibBuilder.loadTexts:
    mscDpnGateRowStatusTable.setStatus("mandatory")
_MscDpnGateRowStatusEntry_Object = MibTableRow
mscDpnGateRowStatusEntry = _MscDpnGateRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 1, 1)
)
mscDpnGateRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateRowStatusEntry.setStatus("mandatory")
_MscDpnGateRowStatus_Type = RowStatus
_MscDpnGateRowStatus_Object = MibTableColumn
mscDpnGateRowStatus = _MscDpnGateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 1, 1, 1),
    _MscDpnGateRowStatus_Type()
)
mscDpnGateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateRowStatus.setStatus("mandatory")
_MscDpnGateComponentName_Type = DisplayString
_MscDpnGateComponentName_Object = MibTableColumn
mscDpnGateComponentName = _MscDpnGateComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 1, 1, 2),
    _MscDpnGateComponentName_Type()
)
mscDpnGateComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateComponentName.setStatus("mandatory")
_MscDpnGateStorageType_Type = StorageType
_MscDpnGateStorageType_Object = MibTableColumn
mscDpnGateStorageType = _MscDpnGateStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 1, 1, 4),
    _MscDpnGateStorageType_Type()
)
mscDpnGateStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateStorageType.setStatus("mandatory")


class _MscDpnGateIndex_Type(Integer32):
    """Custom type mscDpnGateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscDpnGateIndex_Type.__name__ = "Integer32"
_MscDpnGateIndex_Object = MibTableColumn
mscDpnGateIndex = _MscDpnGateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 1, 1, 10),
    _MscDpnGateIndex_Type()
)
mscDpnGateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDpnGateIndex.setStatus("mandatory")
_MscDpnGateFwdStats_ObjectIdentity = ObjectIdentity
mscDpnGateFwdStats = _MscDpnGateFwdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3)
)
_MscDpnGateFwdStatsRowStatusTable_Object = MibTable
mscDpnGateFwdStatsRowStatusTable = _MscDpnGateFwdStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 1)
)
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsRowStatusTable.setStatus("mandatory")
_MscDpnGateFwdStatsRowStatusEntry_Object = MibTableRow
mscDpnGateFwdStatsRowStatusEntry = _MscDpnGateFwdStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 1, 1)
)
mscDpnGateFwdStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsRowStatusEntry.setStatus("mandatory")
_MscDpnGateFwdStatsRowStatus_Type = RowStatus
_MscDpnGateFwdStatsRowStatus_Object = MibTableColumn
mscDpnGateFwdStatsRowStatus = _MscDpnGateFwdStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 1, 1, 1),
    _MscDpnGateFwdStatsRowStatus_Type()
)
mscDpnGateFwdStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsRowStatus.setStatus("mandatory")
_MscDpnGateFwdStatsComponentName_Type = DisplayString
_MscDpnGateFwdStatsComponentName_Object = MibTableColumn
mscDpnGateFwdStatsComponentName = _MscDpnGateFwdStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 1, 1, 2),
    _MscDpnGateFwdStatsComponentName_Type()
)
mscDpnGateFwdStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsComponentName.setStatus("mandatory")
_MscDpnGateFwdStatsStorageType_Type = StorageType
_MscDpnGateFwdStatsStorageType_Object = MibTableColumn
mscDpnGateFwdStatsStorageType = _MscDpnGateFwdStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 1, 1, 4),
    _MscDpnGateFwdStatsStorageType_Type()
)
mscDpnGateFwdStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsStorageType.setStatus("mandatory")
_MscDpnGateFwdStatsIndex_Type = NonReplicated
_MscDpnGateFwdStatsIndex_Object = MibTableColumn
mscDpnGateFwdStatsIndex = _MscDpnGateFwdStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 1, 1, 10),
    _MscDpnGateFwdStatsIndex_Type()
)
mscDpnGateFwdStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsIndex.setStatus("mandatory")
_MscDpnGateFwdStatsOperTable_Object = MibTable
mscDpnGateFwdStatsOperTable = _MscDpnGateFwdStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 10)
)
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsOperTable.setStatus("mandatory")
_MscDpnGateFwdStatsOperEntry_Object = MibTableRow
mscDpnGateFwdStatsOperEntry = _MscDpnGateFwdStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 10, 1)
)
mscDpnGateFwdStatsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateFwdStatsIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsOperEntry.setStatus("mandatory")
_MscDpnGateFwdStatsFwdPktFromIf_Type = PassportCounter64
_MscDpnGateFwdStatsFwdPktFromIf_Object = MibTableColumn
mscDpnGateFwdStatsFwdPktFromIf = _MscDpnGateFwdStatsFwdPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 10, 1, 1),
    _MscDpnGateFwdStatsFwdPktFromIf_Type()
)
mscDpnGateFwdStatsFwdPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsFwdPktFromIf.setStatus("mandatory")
_MscDpnGateFwdStatsFwdDiscUnforwardFromIf_Type = PassportCounter64
_MscDpnGateFwdStatsFwdDiscUnforwardFromIf_Object = MibTableColumn
mscDpnGateFwdStatsFwdDiscUnforwardFromIf = _MscDpnGateFwdStatsFwdDiscUnforwardFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 10, 1, 2),
    _MscDpnGateFwdStatsFwdDiscUnforwardFromIf_Type()
)
mscDpnGateFwdStatsFwdDiscUnforwardFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsFwdDiscUnforwardFromIf.setStatus("mandatory")
_MscDpnGateFwdStatsFwdOctetFromIf_Type = PassportCounter64
_MscDpnGateFwdStatsFwdOctetFromIf_Object = MibTableColumn
mscDpnGateFwdStatsFwdOctetFromIf = _MscDpnGateFwdStatsFwdOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 3, 10, 1, 3),
    _MscDpnGateFwdStatsFwdOctetFromIf_Type()
)
mscDpnGateFwdStatsFwdOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFwdStatsFwdOctetFromIf.setStatus("mandatory")
_MscDpnGateIfEntryTable_Object = MibTable
mscDpnGateIfEntryTable = _MscDpnGateIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 100)
)
if mibBuilder.loadTexts:
    mscDpnGateIfEntryTable.setStatus("mandatory")
_MscDpnGateIfEntryEntry_Object = MibTableRow
mscDpnGateIfEntryEntry = _MscDpnGateIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 100, 1)
)
mscDpnGateIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateIfEntryEntry.setStatus("mandatory")


class _MscDpnGateIfAdminStatus_Type(Integer32):
    """Custom type mscDpnGateIfAdminStatus based on Integer32"""
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


_MscDpnGateIfAdminStatus_Type.__name__ = "Integer32"
_MscDpnGateIfAdminStatus_Object = MibTableColumn
mscDpnGateIfAdminStatus = _MscDpnGateIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 100, 1, 1),
    _MscDpnGateIfAdminStatus_Type()
)
mscDpnGateIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateIfAdminStatus.setStatus("mandatory")


class _MscDpnGateIfIndex_Type(InterfaceIndex):
    """Custom type mscDpnGateIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscDpnGateIfIndex_Type.__name__ = "InterfaceIndex"
_MscDpnGateIfIndex_Object = MibTableColumn
mscDpnGateIfIndex = _MscDpnGateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 100, 1, 2),
    _MscDpnGateIfIndex_Type()
)
mscDpnGateIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateIfIndex.setStatus("mandatory")
_MscDpnGateProvTable_Object = MibTable
mscDpnGateProvTable = _MscDpnGateProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 101)
)
if mibBuilder.loadTexts:
    mscDpnGateProvTable.setStatus("mandatory")
_MscDpnGateProvEntry_Object = MibTableRow
mscDpnGateProvEntry = _MscDpnGateProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 101, 1)
)
mscDpnGateProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateProvEntry.setStatus("mandatory")


class _MscDpnGateExpectedRemoteNamsId_Type(Unsigned32):
    """Custom type mscDpnGateExpectedRemoteNamsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscDpnGateExpectedRemoteNamsId_Type.__name__ = "Unsigned32"
_MscDpnGateExpectedRemoteNamsId_Object = MibTableColumn
mscDpnGateExpectedRemoteNamsId = _MscDpnGateExpectedRemoteNamsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 101, 1, 1),
    _MscDpnGateExpectedRemoteNamsId_Type()
)
mscDpnGateExpectedRemoteNamsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateExpectedRemoteNamsId.setStatus("mandatory")


class _MscDpnGateRemoteValidationAction_Type(Integer32):
    """Custom type mscDpnGateRemoteValidationAction based on Integer32"""
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


_MscDpnGateRemoteValidationAction_Type.__name__ = "Integer32"
_MscDpnGateRemoteValidationAction_Object = MibTableColumn
mscDpnGateRemoteValidationAction = _MscDpnGateRemoteValidationAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 101, 1, 2),
    _MscDpnGateRemoteValidationAction_Type()
)
mscDpnGateRemoteValidationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateRemoteValidationAction.setStatus("mandatory")


class _MscDpnGateLinkType_Type(Integer32):
    """Custom type mscDpnGateLinkType based on Integer32"""
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


_MscDpnGateLinkType_Type.__name__ = "Integer32"
_MscDpnGateLinkType_Object = MibTableColumn
mscDpnGateLinkType = _MscDpnGateLinkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 101, 1, 3),
    _MscDpnGateLinkType_Type()
)
mscDpnGateLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateLinkType.setStatus("mandatory")
_MscDpnGateOverridesTable_Object = MibTable
mscDpnGateOverridesTable = _MscDpnGateOverridesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 102)
)
if mibBuilder.loadTexts:
    mscDpnGateOverridesTable.setStatus("mandatory")
_MscDpnGateOverridesEntry_Object = MibTableRow
mscDpnGateOverridesEntry = _MscDpnGateOverridesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 102, 1)
)
mscDpnGateOverridesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateOverridesEntry.setStatus("mandatory")


class _MscDpnGateOverrideTransmitSpeed_Type(Gauge32):
    """Custom type mscDpnGateOverrideTransmitSpeed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 4294967295),
    )


_MscDpnGateOverrideTransmitSpeed_Type.__name__ = "Gauge32"
_MscDpnGateOverrideTransmitSpeed_Object = MibTableColumn
mscDpnGateOverrideTransmitSpeed = _MscDpnGateOverrideTransmitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 102, 1, 1),
    _MscDpnGateOverrideTransmitSpeed_Type()
)
mscDpnGateOverrideTransmitSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateOverrideTransmitSpeed.setStatus("mandatory")


class _MscDpnGateOldOverrideRoundTripDelay_Type(Gauge32):
    """Custom type mscDpnGateOldOverrideRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_MscDpnGateOldOverrideRoundTripDelay_Type.__name__ = "Gauge32"
_MscDpnGateOldOverrideRoundTripDelay_Object = MibTableColumn
mscDpnGateOldOverrideRoundTripDelay = _MscDpnGateOldOverrideRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 102, 1, 2),
    _MscDpnGateOldOverrideRoundTripDelay_Type()
)
mscDpnGateOldOverrideRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateOldOverrideRoundTripDelay.setStatus("obsolete")


class _MscDpnGateOverrideRoundTripUsec_Type(FixedPoint1):
    """Custom type mscDpnGateOverrideRoundTripUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_MscDpnGateOverrideRoundTripUsec_Type.__name__ = "FixedPoint1"
_MscDpnGateOverrideRoundTripUsec_Object = MibTableColumn
mscDpnGateOverrideRoundTripUsec = _MscDpnGateOverrideRoundTripUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 102, 1, 3),
    _MscDpnGateOverrideRoundTripUsec_Type()
)
mscDpnGateOverrideRoundTripUsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateOverrideRoundTripUsec.setStatus("mandatory")
_MscDpnGateStateTable_Object = MibTable
mscDpnGateStateTable = _MscDpnGateStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103)
)
if mibBuilder.loadTexts:
    mscDpnGateStateTable.setStatus("mandatory")
_MscDpnGateStateEntry_Object = MibTableRow
mscDpnGateStateEntry = _MscDpnGateStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1)
)
mscDpnGateStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateStateEntry.setStatus("mandatory")


class _MscDpnGateAdminState_Type(Integer32):
    """Custom type mscDpnGateAdminState based on Integer32"""
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


_MscDpnGateAdminState_Type.__name__ = "Integer32"
_MscDpnGateAdminState_Object = MibTableColumn
mscDpnGateAdminState = _MscDpnGateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 1),
    _MscDpnGateAdminState_Type()
)
mscDpnGateAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateAdminState.setStatus("mandatory")


class _MscDpnGateOperationalState_Type(Integer32):
    """Custom type mscDpnGateOperationalState based on Integer32"""
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


_MscDpnGateOperationalState_Type.__name__ = "Integer32"
_MscDpnGateOperationalState_Object = MibTableColumn
mscDpnGateOperationalState = _MscDpnGateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 2),
    _MscDpnGateOperationalState_Type()
)
mscDpnGateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateOperationalState.setStatus("mandatory")


class _MscDpnGateUsageState_Type(Integer32):
    """Custom type mscDpnGateUsageState based on Integer32"""
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


_MscDpnGateUsageState_Type.__name__ = "Integer32"
_MscDpnGateUsageState_Object = MibTableColumn
mscDpnGateUsageState = _MscDpnGateUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 3),
    _MscDpnGateUsageState_Type()
)
mscDpnGateUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUsageState.setStatus("mandatory")


class _MscDpnGateAvailabilityStatus_Type(OctetString):
    """Custom type mscDpnGateAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscDpnGateAvailabilityStatus_Type.__name__ = "OctetString"
_MscDpnGateAvailabilityStatus_Object = MibTableColumn
mscDpnGateAvailabilityStatus = _MscDpnGateAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 4),
    _MscDpnGateAvailabilityStatus_Type()
)
mscDpnGateAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateAvailabilityStatus.setStatus("mandatory")


class _MscDpnGateProceduralStatus_Type(OctetString):
    """Custom type mscDpnGateProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateProceduralStatus_Type.__name__ = "OctetString"
_MscDpnGateProceduralStatus_Object = MibTableColumn
mscDpnGateProceduralStatus = _MscDpnGateProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 5),
    _MscDpnGateProceduralStatus_Type()
)
mscDpnGateProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateProceduralStatus.setStatus("mandatory")


class _MscDpnGateControlStatus_Type(OctetString):
    """Custom type mscDpnGateControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateControlStatus_Type.__name__ = "OctetString"
_MscDpnGateControlStatus_Object = MibTableColumn
mscDpnGateControlStatus = _MscDpnGateControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 6),
    _MscDpnGateControlStatus_Type()
)
mscDpnGateControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateControlStatus.setStatus("mandatory")


class _MscDpnGateAlarmStatus_Type(OctetString):
    """Custom type mscDpnGateAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateAlarmStatus_Type.__name__ = "OctetString"
_MscDpnGateAlarmStatus_Object = MibTableColumn
mscDpnGateAlarmStatus = _MscDpnGateAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 7),
    _MscDpnGateAlarmStatus_Type()
)
mscDpnGateAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateAlarmStatus.setStatus("mandatory")


class _MscDpnGateStandbyStatus_Type(Integer32):
    """Custom type mscDpnGateStandbyStatus based on Integer32"""
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


_MscDpnGateStandbyStatus_Type.__name__ = "Integer32"
_MscDpnGateStandbyStatus_Object = MibTableColumn
mscDpnGateStandbyStatus = _MscDpnGateStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 8),
    _MscDpnGateStandbyStatus_Type()
)
mscDpnGateStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateStandbyStatus.setStatus("mandatory")


class _MscDpnGateUnknownStatus_Type(Integer32):
    """Custom type mscDpnGateUnknownStatus based on Integer32"""
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


_MscDpnGateUnknownStatus_Type.__name__ = "Integer32"
_MscDpnGateUnknownStatus_Object = MibTableColumn
mscDpnGateUnknownStatus = _MscDpnGateUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 103, 1, 9),
    _MscDpnGateUnknownStatus_Type()
)
mscDpnGateUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUnknownStatus.setStatus("mandatory")
_MscDpnGateOperStatusTable_Object = MibTable
mscDpnGateOperStatusTable = _MscDpnGateOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 104)
)
if mibBuilder.loadTexts:
    mscDpnGateOperStatusTable.setStatus("mandatory")
_MscDpnGateOperStatusEntry_Object = MibTableRow
mscDpnGateOperStatusEntry = _MscDpnGateOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 104, 1)
)
mscDpnGateOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateOperStatusEntry.setStatus("mandatory")


class _MscDpnGateSnmpOperStatus_Type(Integer32):
    """Custom type mscDpnGateSnmpOperStatus based on Integer32"""
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


_MscDpnGateSnmpOperStatus_Type.__name__ = "Integer32"
_MscDpnGateSnmpOperStatus_Object = MibTableColumn
mscDpnGateSnmpOperStatus = _MscDpnGateSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 104, 1, 1),
    _MscDpnGateSnmpOperStatus_Type()
)
mscDpnGateSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateSnmpOperStatus.setStatus("mandatory")
_MscDpnGateOperTable_Object = MibTable
mscDpnGateOperTable = _MscDpnGateOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 105)
)
if mibBuilder.loadTexts:
    mscDpnGateOperTable.setStatus("mandatory")
_MscDpnGateOperEntry_Object = MibTableRow
mscDpnGateOperEntry = _MscDpnGateOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 105, 1)
)
mscDpnGateOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateOperEntry.setStatus("mandatory")


class _MscDpnGateRemoteComponentName_Type(AsciiString):
    """Custom type mscDpnGateRemoteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 26),
    )


_MscDpnGateRemoteComponentName_Type.__name__ = "AsciiString"
_MscDpnGateRemoteComponentName_Object = MibTableColumn
mscDpnGateRemoteComponentName = _MscDpnGateRemoteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 105, 1, 1),
    _MscDpnGateRemoteComponentName_Type()
)
mscDpnGateRemoteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateRemoteComponentName.setStatus("mandatory")


class _MscDpnGateRemoteNamsMnemonic_Type(AsciiString):
    """Custom type mscDpnGateRemoteNamsMnemonic based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscDpnGateRemoteNamsMnemonic_Type.__name__ = "AsciiString"
_MscDpnGateRemoteNamsMnemonic_Object = MibTableColumn
mscDpnGateRemoteNamsMnemonic = _MscDpnGateRemoteNamsMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 105, 1, 2),
    _MscDpnGateRemoteNamsMnemonic_Type()
)
mscDpnGateRemoteNamsMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateRemoteNamsMnemonic.setStatus("mandatory")


class _MscDpnGateLinkMode_Type(Integer32):
    """Custom type mscDpnGateLinkMode based on Integer32"""
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


_MscDpnGateLinkMode_Type.__name__ = "Integer32"
_MscDpnGateLinkMode_Object = MibTableColumn
mscDpnGateLinkMode = _MscDpnGateLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 105, 1, 3),
    _MscDpnGateLinkMode_Type()
)
mscDpnGateLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateLinkMode.setStatus("mandatory")


class _MscDpnGateActivateReason_Type(Integer32):
    """Custom type mscDpnGateActivateReason based on Integer32"""
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


_MscDpnGateActivateReason_Type.__name__ = "Integer32"
_MscDpnGateActivateReason_Object = MibTableColumn
mscDpnGateActivateReason = _MscDpnGateActivateReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 105, 1, 4),
    _MscDpnGateActivateReason_Type()
)
mscDpnGateActivateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateActivateReason.setStatus("mandatory")
_MscDpnGateTransportTable_Object = MibTable
mscDpnGateTransportTable = _MscDpnGateTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 106)
)
if mibBuilder.loadTexts:
    mscDpnGateTransportTable.setStatus("mandatory")
_MscDpnGateTransportEntry_Object = MibTableRow
mscDpnGateTransportEntry = _MscDpnGateTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 106, 1)
)
mscDpnGateTransportEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateTransportEntry.setStatus("mandatory")


class _MscDpnGateMeasuredSpeedToIf_Type(Gauge32):
    """Custom type mscDpnGateMeasuredSpeedToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDpnGateMeasuredSpeedToIf_Type.__name__ = "Gauge32"
_MscDpnGateMeasuredSpeedToIf_Object = MibTableColumn
mscDpnGateMeasuredSpeedToIf = _MscDpnGateMeasuredSpeedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 106, 1, 1),
    _MscDpnGateMeasuredSpeedToIf_Type()
)
mscDpnGateMeasuredSpeedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateMeasuredSpeedToIf.setStatus("mandatory")


class _MscDpnGateMeasuredRoundTripDelay_Type(Gauge32):
    """Custom type mscDpnGateMeasuredRoundTripDelay based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_MscDpnGateMeasuredRoundTripDelay_Type.__name__ = "Gauge32"
_MscDpnGateMeasuredRoundTripDelay_Object = MibTableColumn
mscDpnGateMeasuredRoundTripDelay = _MscDpnGateMeasuredRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 106, 1, 2),
    _MscDpnGateMeasuredRoundTripDelay_Type()
)
mscDpnGateMeasuredRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateMeasuredRoundTripDelay.setStatus("obsolete")


class _MscDpnGateMaxTxUnit_Type(Gauge32):
    """Custom type mscDpnGateMaxTxUnit based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscDpnGateMaxTxUnit_Type.__name__ = "Gauge32"
_MscDpnGateMaxTxUnit_Object = MibTableColumn
mscDpnGateMaxTxUnit = _MscDpnGateMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 106, 1, 3),
    _MscDpnGateMaxTxUnit_Type()
)
mscDpnGateMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateMaxTxUnit.setStatus("mandatory")


class _MscDpnGateMeasuredRoundTripDelayUsec_Type(FixedPoint1):
    """Custom type mscDpnGateMeasuredRoundTripDelayUsec based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_MscDpnGateMeasuredRoundTripDelayUsec_Type.__name__ = "FixedPoint1"
_MscDpnGateMeasuredRoundTripDelayUsec_Object = MibTableColumn
mscDpnGateMeasuredRoundTripDelayUsec = _MscDpnGateMeasuredRoundTripDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 106, 1, 4),
    _MscDpnGateMeasuredRoundTripDelayUsec_Type()
)
mscDpnGateMeasuredRoundTripDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateMeasuredRoundTripDelayUsec.setStatus("mandatory")
_MscDpnGateStatsTable_Object = MibTable
mscDpnGateStatsTable = _MscDpnGateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107)
)
if mibBuilder.loadTexts:
    mscDpnGateStatsTable.setStatus("mandatory")
_MscDpnGateStatsEntry_Object = MibTableRow
mscDpnGateStatsEntry = _MscDpnGateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1)
)
mscDpnGateStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateStatsEntry.setStatus("mandatory")
_MscDpnGatePktFromIf_Type = PassportCounter64
_MscDpnGatePktFromIf_Object = MibTableColumn
mscDpnGatePktFromIf = _MscDpnGatePktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1, 1),
    _MscDpnGatePktFromIf_Type()
)
mscDpnGatePktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGatePktFromIf.setStatus("mandatory")
_MscDpnGateTrunkPktFromIf_Type = Counter32
_MscDpnGateTrunkPktFromIf_Object = MibTableColumn
mscDpnGateTrunkPktFromIf = _MscDpnGateTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1, 2),
    _MscDpnGateTrunkPktFromIf_Type()
)
mscDpnGateTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateTrunkPktFromIf.setStatus("mandatory")
_MscDpnGateTrunkPktToIf_Type = Counter32
_MscDpnGateTrunkPktToIf_Object = MibTableColumn
mscDpnGateTrunkPktToIf = _MscDpnGateTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1, 3),
    _MscDpnGateTrunkPktToIf_Type()
)
mscDpnGateTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateTrunkPktToIf.setStatus("mandatory")
_MscDpnGateDiscardUnforward_Type = PassportCounter64
_MscDpnGateDiscardUnforward_Object = MibTableColumn
mscDpnGateDiscardUnforward = _MscDpnGateDiscardUnforward_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1, 4),
    _MscDpnGateDiscardUnforward_Type()
)
mscDpnGateDiscardUnforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateDiscardUnforward.setStatus("mandatory")
_MscDpnGateDiscardTrunkPktFromIf_Type = Counter32
_MscDpnGateDiscardTrunkPktFromIf_Object = MibTableColumn
mscDpnGateDiscardTrunkPktFromIf = _MscDpnGateDiscardTrunkPktFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1, 5),
    _MscDpnGateDiscardTrunkPktFromIf_Type()
)
mscDpnGateDiscardTrunkPktFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateDiscardTrunkPktFromIf.setStatus("mandatory")
_MscDpnGateStagingAttempts_Type = Counter32
_MscDpnGateStagingAttempts_Object = MibTableColumn
mscDpnGateStagingAttempts = _MscDpnGateStagingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1, 6),
    _MscDpnGateStagingAttempts_Type()
)
mscDpnGateStagingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateStagingAttempts.setStatus("mandatory")
_MscDpnGateDiscardTrunkPktToIf_Type = Counter32
_MscDpnGateDiscardTrunkPktToIf_Object = MibTableColumn
mscDpnGateDiscardTrunkPktToIf = _MscDpnGateDiscardTrunkPktToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 107, 1, 7),
    _MscDpnGateDiscardTrunkPktToIf_Type()
)
mscDpnGateDiscardTrunkPktToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateDiscardTrunkPktToIf.setStatus("mandatory")
_DpnTrunksMIB_ObjectIdentity = ObjectIdentity
dpnTrunksMIB = _DpnTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40)
)
_DpnTrunksGroup_ObjectIdentity = ObjectIdentity
dpnTrunksGroup = _DpnTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 1)
)
_DpnTrunksGroupCA_ObjectIdentity = ObjectIdentity
dpnTrunksGroupCA = _DpnTrunksGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 1, 1)
)
_DpnTrunksGroupCA02_ObjectIdentity = ObjectIdentity
dpnTrunksGroupCA02 = _DpnTrunksGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 1, 1, 3)
)
_DpnTrunksGroupCA02A_ObjectIdentity = ObjectIdentity
dpnTrunksGroupCA02A = _DpnTrunksGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 1, 1, 3, 2)
)
_DpnTrunksCapabilities_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilities = _DpnTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 3)
)
_DpnTrunksCapabilitiesCA_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilitiesCA = _DpnTrunksCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 3, 1)
)
_DpnTrunksCapabilitiesCA02_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilitiesCA02 = _DpnTrunksCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 3, 1, 3)
)
_DpnTrunksCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
dpnTrunksCapabilitiesCA02A = _DpnTrunksCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 40, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DpnTrunksMIB",
    **{"mscDpnGate": mscDpnGate,
       "mscDpnGateRowStatusTable": mscDpnGateRowStatusTable,
       "mscDpnGateRowStatusEntry": mscDpnGateRowStatusEntry,
       "mscDpnGateRowStatus": mscDpnGateRowStatus,
       "mscDpnGateComponentName": mscDpnGateComponentName,
       "mscDpnGateStorageType": mscDpnGateStorageType,
       "mscDpnGateIndex": mscDpnGateIndex,
       "mscDpnGateFwdStats": mscDpnGateFwdStats,
       "mscDpnGateFwdStatsRowStatusTable": mscDpnGateFwdStatsRowStatusTable,
       "mscDpnGateFwdStatsRowStatusEntry": mscDpnGateFwdStatsRowStatusEntry,
       "mscDpnGateFwdStatsRowStatus": mscDpnGateFwdStatsRowStatus,
       "mscDpnGateFwdStatsComponentName": mscDpnGateFwdStatsComponentName,
       "mscDpnGateFwdStatsStorageType": mscDpnGateFwdStatsStorageType,
       "mscDpnGateFwdStatsIndex": mscDpnGateFwdStatsIndex,
       "mscDpnGateFwdStatsOperTable": mscDpnGateFwdStatsOperTable,
       "mscDpnGateFwdStatsOperEntry": mscDpnGateFwdStatsOperEntry,
       "mscDpnGateFwdStatsFwdPktFromIf": mscDpnGateFwdStatsFwdPktFromIf,
       "mscDpnGateFwdStatsFwdDiscUnforwardFromIf": mscDpnGateFwdStatsFwdDiscUnforwardFromIf,
       "mscDpnGateFwdStatsFwdOctetFromIf": mscDpnGateFwdStatsFwdOctetFromIf,
       "mscDpnGateIfEntryTable": mscDpnGateIfEntryTable,
       "mscDpnGateIfEntryEntry": mscDpnGateIfEntryEntry,
       "mscDpnGateIfAdminStatus": mscDpnGateIfAdminStatus,
       "mscDpnGateIfIndex": mscDpnGateIfIndex,
       "mscDpnGateProvTable": mscDpnGateProvTable,
       "mscDpnGateProvEntry": mscDpnGateProvEntry,
       "mscDpnGateExpectedRemoteNamsId": mscDpnGateExpectedRemoteNamsId,
       "mscDpnGateRemoteValidationAction": mscDpnGateRemoteValidationAction,
       "mscDpnGateLinkType": mscDpnGateLinkType,
       "mscDpnGateOverridesTable": mscDpnGateOverridesTable,
       "mscDpnGateOverridesEntry": mscDpnGateOverridesEntry,
       "mscDpnGateOverrideTransmitSpeed": mscDpnGateOverrideTransmitSpeed,
       "mscDpnGateOldOverrideRoundTripDelay": mscDpnGateOldOverrideRoundTripDelay,
       "mscDpnGateOverrideRoundTripUsec": mscDpnGateOverrideRoundTripUsec,
       "mscDpnGateStateTable": mscDpnGateStateTable,
       "mscDpnGateStateEntry": mscDpnGateStateEntry,
       "mscDpnGateAdminState": mscDpnGateAdminState,
       "mscDpnGateOperationalState": mscDpnGateOperationalState,
       "mscDpnGateUsageState": mscDpnGateUsageState,
       "mscDpnGateAvailabilityStatus": mscDpnGateAvailabilityStatus,
       "mscDpnGateProceduralStatus": mscDpnGateProceduralStatus,
       "mscDpnGateControlStatus": mscDpnGateControlStatus,
       "mscDpnGateAlarmStatus": mscDpnGateAlarmStatus,
       "mscDpnGateStandbyStatus": mscDpnGateStandbyStatus,
       "mscDpnGateUnknownStatus": mscDpnGateUnknownStatus,
       "mscDpnGateOperStatusTable": mscDpnGateOperStatusTable,
       "mscDpnGateOperStatusEntry": mscDpnGateOperStatusEntry,
       "mscDpnGateSnmpOperStatus": mscDpnGateSnmpOperStatus,
       "mscDpnGateOperTable": mscDpnGateOperTable,
       "mscDpnGateOperEntry": mscDpnGateOperEntry,
       "mscDpnGateRemoteComponentName": mscDpnGateRemoteComponentName,
       "mscDpnGateRemoteNamsMnemonic": mscDpnGateRemoteNamsMnemonic,
       "mscDpnGateLinkMode": mscDpnGateLinkMode,
       "mscDpnGateActivateReason": mscDpnGateActivateReason,
       "mscDpnGateTransportTable": mscDpnGateTransportTable,
       "mscDpnGateTransportEntry": mscDpnGateTransportEntry,
       "mscDpnGateMeasuredSpeedToIf": mscDpnGateMeasuredSpeedToIf,
       "mscDpnGateMeasuredRoundTripDelay": mscDpnGateMeasuredRoundTripDelay,
       "mscDpnGateMaxTxUnit": mscDpnGateMaxTxUnit,
       "mscDpnGateMeasuredRoundTripDelayUsec": mscDpnGateMeasuredRoundTripDelayUsec,
       "mscDpnGateStatsTable": mscDpnGateStatsTable,
       "mscDpnGateStatsEntry": mscDpnGateStatsEntry,
       "mscDpnGatePktFromIf": mscDpnGatePktFromIf,
       "mscDpnGateTrunkPktFromIf": mscDpnGateTrunkPktFromIf,
       "mscDpnGateTrunkPktToIf": mscDpnGateTrunkPktToIf,
       "mscDpnGateDiscardUnforward": mscDpnGateDiscardUnforward,
       "mscDpnGateDiscardTrunkPktFromIf": mscDpnGateDiscardTrunkPktFromIf,
       "mscDpnGateStagingAttempts": mscDpnGateStagingAttempts,
       "mscDpnGateDiscardTrunkPktToIf": mscDpnGateDiscardTrunkPktToIf,
       "dpnTrunksMIB": dpnTrunksMIB,
       "dpnTrunksGroup": dpnTrunksGroup,
       "dpnTrunksGroupCA": dpnTrunksGroupCA,
       "dpnTrunksGroupCA02": dpnTrunksGroupCA02,
       "dpnTrunksGroupCA02A": dpnTrunksGroupCA02A,
       "dpnTrunksCapabilities": dpnTrunksCapabilities,
       "dpnTrunksCapabilitiesCA": dpnTrunksCapabilitiesCA,
       "dpnTrunksCapabilitiesCA02": dpnTrunksCapabilitiesCA02,
       "dpnTrunksCapabilitiesCA02A": dpnTrunksCapabilitiesCA02A}
)
