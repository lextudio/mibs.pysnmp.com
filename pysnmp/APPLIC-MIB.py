# SNMP MIB module (APPLIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPLIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:51 2024
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(historyControlIndex,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "historyControlIndex")

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

_LntLanSwitch_ObjectIdentity = ObjectIdentity
lntLanSwitch = _LntLanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19)
)
_Lse_ObjectIdentity = ObjectIdentity
lse = _Lse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 1)
)
_LseGroupTable_Object = MibTable
lseGroupTable = _LseGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1)
)
if mibBuilder.loadTexts:
    lseGroupTable.setStatus("mandatory")
_LseGroupEntry_Object = MibTableRow
lseGroupEntry = _LseGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1)
)
lseGroupEntry.setIndexNames(
    (0, "APPLIC-MIB", "lseGroupId"),
)
if mibBuilder.loadTexts:
    lseGroupEntry.setStatus("mandatory")
_LseGroupId_Type = Integer32
_LseGroupId_Object = MibTableColumn
lseGroupId = _LseGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 1),
    _LseGroupId_Type()
)
lseGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseGroupId.setStatus("mandatory")


class _LseGroupFastOpen_Type(Integer32):
    """Custom type lseGroupFastOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupFastOpen_Type.__name__ = "Integer32"
_LseGroupFastOpen_Object = MibTableColumn
lseGroupFastOpen = _LseGroupFastOpen_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 2),
    _LseGroupFastOpen_Type()
)
lseGroupFastOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupFastOpen.setStatus("mandatory")


class _LseGroup10MSqlt_Type(Integer32):
    """Custom type lseGroup10MSqlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroup10MSqlt_Type.__name__ = "Integer32"
_LseGroup10MSqlt_Object = MibTableColumn
lseGroup10MSqlt = _LseGroup10MSqlt_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 3),
    _LseGroup10MSqlt_Type()
)
lseGroup10MSqlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroup10MSqlt.setStatus("mandatory")


class _LseGroupSmartSqlt_Type(Integer32):
    """Custom type lseGroupSmartSqlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupSmartSqlt_Type.__name__ = "Integer32"
_LseGroupSmartSqlt_Object = MibTableColumn
lseGroupSmartSqlt = _LseGroupSmartSqlt_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 4),
    _LseGroupSmartSqlt_Type()
)
lseGroupSmartSqlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupSmartSqlt.setStatus("deprecated")


class _LseGroupCParameter_Type(Integer32):
    """Custom type lseGroupCParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_LseGroupCParameter_Type.__name__ = "Integer32"
_LseGroupCParameter_Object = MibTableColumn
lseGroupCParameter = _LseGroupCParameter_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 5),
    _LseGroupCParameter_Type()
)
lseGroupCParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupCParameter.setStatus("mandatory")


class _LseGroupIPGJamLength_Type(Integer32):
    """Custom type lseGroupIPGJamLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 124),
    )


_LseGroupIPGJamLength_Type.__name__ = "Integer32"
_LseGroupIPGJamLength_Object = MibTableColumn
lseGroupIPGJamLength = _LseGroupIPGJamLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 6),
    _LseGroupIPGJamLength_Type()
)
lseGroupIPGJamLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupIPGJamLength.setStatus("mandatory")


class _LseGroupJamLength_Type(Integer32):
    """Custom type lseGroupJamLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 120),
    )


_LseGroupJamLength_Type.__name__ = "Integer32"
_LseGroupJamLength_Object = MibTableColumn
lseGroupJamLength = _LseGroupJamLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 7),
    _LseGroupJamLength_Type()
)
lseGroupJamLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupJamLength.setStatus("mandatory")


class _LseGroupDataBlinderLength_Type(Integer32):
    """Custom type lseGroupDataBlinderLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_LseGroupDataBlinderLength_Type.__name__ = "Integer32"
_LseGroupDataBlinderLength_Object = MibTableColumn
lseGroupDataBlinderLength = _LseGroupDataBlinderLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 8),
    _LseGroupDataBlinderLength_Type()
)
lseGroupDataBlinderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupDataBlinderLength.setStatus("mandatory")


class _LseGroupIPGDataLength_Type(Integer32):
    """Custom type lseGroupIPGDataLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 124),
    )


_LseGroupIPGDataLength_Type.__name__ = "Integer32"
_LseGroupIPGDataLength_Object = MibTableColumn
lseGroupIPGDataLength = _LseGroupIPGDataLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 9),
    _LseGroupIPGDataLength_Type()
)
lseGroupIPGDataLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupIPGDataLength.setStatus("mandatory")


class _LseGroupActiveMonitor_Type(Integer32):
    """Custom type lseGroupActiveMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupActiveMonitor_Type.__name__ = "Integer32"
_LseGroupActiveMonitor_Object = MibTableColumn
lseGroupActiveMonitor = _LseGroupActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 10),
    _LseGroupActiveMonitor_Type()
)
lseGroupActiveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseGroupActiveMonitor.setStatus("mandatory")


class _LseGroupBackbone12_Type(Integer32):
    """Custom type lseGroupBackbone12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupBackbone12_Type.__name__ = "Integer32"
_LseGroupBackbone12_Object = MibTableColumn
lseGroupBackbone12 = _LseGroupBackbone12_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 11),
    _LseGroupBackbone12_Type()
)
lseGroupBackbone12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupBackbone12.setStatus("mandatory")


class _LseGroupSetDefaults_Type(Integer32):
    """Custom type lseGroupSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupSetDefaults_Type.__name__ = "Integer32"
_LseGroupSetDefaults_Object = MibTableColumn
lseGroupSetDefaults = _LseGroupSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 12),
    _LseGroupSetDefaults_Type()
)
lseGroupSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupSetDefaults.setStatus("mandatory")


class _LseGroupBackbone34_Type(Integer32):
    """Custom type lseGroupBackbone34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupBackbone34_Type.__name__ = "Integer32"
_LseGroupBackbone34_Object = MibTableColumn
lseGroupBackbone34 = _LseGroupBackbone34_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 13),
    _LseGroupBackbone34_Type()
)
lseGroupBackbone34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupBackbone34.setStatus("mandatory")


class _LseGroupBackboneRedun12_Type(Integer32):
    """Custom type lseGroupBackboneRedun12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupBackboneRedun12_Type.__name__ = "Integer32"
_LseGroupBackboneRedun12_Object = MibTableColumn
lseGroupBackboneRedun12 = _LseGroupBackboneRedun12_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 14),
    _LseGroupBackboneRedun12_Type()
)
lseGroupBackboneRedun12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupBackboneRedun12.setStatus("mandatory")


class _LseGroupBackoffFromJam_Type(Integer32):
    """Custom type lseGroupBackoffFromJam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupBackoffFromJam_Type.__name__ = "Integer32"
_LseGroupBackoffFromJam_Object = MibTableColumn
lseGroupBackoffFromJam = _LseGroupBackoffFromJam_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 15),
    _LseGroupBackoffFromJam_Type()
)
lseGroupBackoffFromJam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupBackoffFromJam.setStatus("mandatory")


class _LseGroupCAMClear_Type(Integer32):
    """Custom type lseGroupCAMClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupCAMClear_Type.__name__ = "Integer32"
_LseGroupCAMClear_Object = MibTableColumn
lseGroupCAMClear = _LseGroupCAMClear_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 16),
    _LseGroupCAMClear_Type()
)
lseGroupCAMClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupCAMClear.setStatus("mandatory")


class _LseGroupJamPrevent_Type(Integer32):
    """Custom type lseGroupJamPrevent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupJamPrevent_Type.__name__ = "Integer32"
_LseGroupJamPrevent_Object = MibTableColumn
lseGroupJamPrevent = _LseGroupJamPrevent_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 17),
    _LseGroupJamPrevent_Type()
)
lseGroupJamPrevent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupJamPrevent.setStatus("mandatory")


class _LseGroupNormOpCl_Type(Integer32):
    """Custom type lseGroupNormOpCl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notSupported", 255),
          ("open", 1))
    )


_LseGroupNormOpCl_Type.__name__ = "Integer32"
_LseGroupNormOpCl_Object = MibTableColumn
lseGroupNormOpCl = _LseGroupNormOpCl_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 18),
    _LseGroupNormOpCl_Type()
)
lseGroupNormOpCl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupNormOpCl.setStatus("mandatory")


class _LseGroupNormOpDelay_Type(Integer32):
    """Custom type lseGroupNormOpDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_LseGroupNormOpDelay_Type.__name__ = "Integer32"
_LseGroupNormOpDelay_Object = MibTableColumn
lseGroupNormOpDelay = _LseGroupNormOpDelay_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 19),
    _LseGroupNormOpDelay_Type()
)
lseGroupNormOpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupNormOpDelay.setStatus("mandatory")


class _LseGroupAutoPartitionEnable_Type(Integer32):
    """Custom type lseGroupAutoPartitionEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_LseGroupAutoPartitionEnable_Type.__name__ = "Integer32"
_LseGroupAutoPartitionEnable_Object = MibTableColumn
lseGroupAutoPartitionEnable = _LseGroupAutoPartitionEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 20),
    _LseGroupAutoPartitionEnable_Type()
)
lseGroupAutoPartitionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupAutoPartitionEnable.setStatus("mandatory")


class _LseGroupWorkState_Type(Integer32):
    """Custom type lseGroupWorkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("boot", 2),
          ("none", 4),
          ("notSupported", 255),
          ("run", 1),
          ("runAndBoot", 3))
    )


_LseGroupWorkState_Type.__name__ = "Integer32"
_LseGroupWorkState_Object = MibTableColumn
lseGroupWorkState = _LseGroupWorkState_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 21),
    _LseGroupWorkState_Type()
)
lseGroupWorkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseGroupWorkState.setStatus("mandatory")


class _LseGroupBITResult_Type(Integer32):
    """Custom type lseGroupBITResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_LseGroupBITResult_Type.__name__ = "Integer32"
_LseGroupBITResult_Object = MibTableColumn
lseGroupBITResult = _LseGroupBITResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 22),
    _LseGroupBITResult_Type()
)
lseGroupBITResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseGroupBITResult.setStatus("mandatory")


class _LseGroupAssignSlots_Type(OctetString):
    """Custom type lseGroupAssignSlots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LseGroupAssignSlots_Type.__name__ = "OctetString"
_LseGroupAssignSlots_Object = MibTableColumn
lseGroupAssignSlots = _LseGroupAssignSlots_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 23),
    _LseGroupAssignSlots_Type()
)
lseGroupAssignSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupAssignSlots.setStatus("mandatory")
_LseGroupHSBMonStatus_Type = Integer32
_LseGroupHSBMonStatus_Object = MibTableColumn
lseGroupHSBMonStatus = _LseGroupHSBMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 24),
    _LseGroupHSBMonStatus_Type()
)
lseGroupHSBMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseGroupHSBMonStatus.setStatus("mandatory")


class _LseGroupEnableHSBReset_Type(Integer32):
    """Custom type lseGroupEnableHSBReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_LseGroupEnableHSBReset_Type.__name__ = "Integer32"
_LseGroupEnableHSBReset_Object = MibTableColumn
lseGroupEnableHSBReset = _LseGroupEnableHSBReset_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 1, 1, 25),
    _LseGroupEnableHSBReset_Type()
)
lseGroupEnableHSBReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupEnableHSBReset.setStatus("mandatory")
_LseIntPort_ObjectIdentity = ObjectIdentity
lseIntPort = _LseIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2)
)
_LseIntPortTable_Object = MibTable
lseIntPortTable = _LseIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lseIntPortTable.setStatus("mandatory")
_LseIntPortEntry_Object = MibTableRow
lseIntPortEntry = _LseIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1)
)
lseIntPortEntry.setIndexNames(
    (0, "APPLIC-MIB", "lseIntPortGroupId"),
    (0, "APPLIC-MIB", "lseIntPortId"),
)
if mibBuilder.loadTexts:
    lseIntPortEntry.setStatus("mandatory")


class _LseIntPortGroupId_Type(Integer32):
    """Custom type lseIntPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortGroupId_Type.__name__ = "Integer32"
_LseIntPortGroupId_Object = MibTableColumn
lseIntPortGroupId = _LseIntPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 1),
    _LseIntPortGroupId_Type()
)
lseIntPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortGroupId.setStatus("mandatory")


class _LseIntPortId_Type(Integer32):
    """Custom type lseIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortId_Type.__name__ = "Integer32"
_LseIntPortId_Object = MibTableColumn
lseIntPortId = _LseIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 2),
    _LseIntPortId_Type()
)
lseIntPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortId.setStatus("mandatory")


class _LseIntPortIOMode_Type(Integer32):
    """Custom type lseIntPortIOMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortIOMode_Type.__name__ = "Integer32"
_LseIntPortIOMode_Object = MibTableColumn
lseIntPortIOMode = _LseIntPortIOMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 3),
    _LseIntPortIOMode_Type()
)
lseIntPortIOMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortIOMode.setStatus("mandatory")


class _LseIntPortResetSwitchCAM_Type(Integer32):
    """Custom type lseIntPortResetSwitchCAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortResetSwitchCAM_Type.__name__ = "Integer32"
_LseIntPortResetSwitchCAM_Object = MibTableColumn
lseIntPortResetSwitchCAM = _LseIntPortResetSwitchCAM_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 4),
    _LseIntPortResetSwitchCAM_Type()
)
lseIntPortResetSwitchCAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortResetSwitchCAM.setStatus("mandatory")


class _LseIntPortVideoPacket_Type(Integer32):
    """Custom type lseIntPortVideoPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortVideoPacket_Type.__name__ = "Integer32"
_LseIntPortVideoPacket_Object = MibTableColumn
lseIntPortVideoPacket = _LseIntPortVideoPacket_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 5),
    _LseIntPortVideoPacket_Type()
)
lseIntPortVideoPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortVideoPacket.setStatus("mandatory")


class _LseIntPortPriorityStateMachine_Type(Integer32):
    """Custom type lseIntPortPriorityStateMachine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortPriorityStateMachine_Type.__name__ = "Integer32"
_LseIntPortPriorityStateMachine_Object = MibTableColumn
lseIntPortPriorityStateMachine = _LseIntPortPriorityStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 6),
    _LseIntPortPriorityStateMachine_Type()
)
lseIntPortPriorityStateMachine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortPriorityStateMachine.setStatus("mandatory")


class _LseIntPortActiveBroadcastPriority_Type(Integer32):
    """Custom type lseIntPortActiveBroadcastPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortActiveBroadcastPriority_Type.__name__ = "Integer32"
_LseIntPortActiveBroadcastPriority_Object = MibTableColumn
lseIntPortActiveBroadcastPriority = _LseIntPortActiveBroadcastPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 7),
    _LseIntPortActiveBroadcastPriority_Type()
)
lseIntPortActiveBroadcastPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortActiveBroadcastPriority.setStatus("mandatory")


class _LseIntPortPriorityLevel_Type(Integer32):
    """Custom type lseIntPortPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("default", 5),
          ("mngrTerminal", 6),
          ("multicast", 2),
          ("notSupported", 255),
          ("regular", 4),
          ("video", 3))
    )


_LseIntPortPriorityLevel_Type.__name__ = "Integer32"
_LseIntPortPriorityLevel_Object = MibTableColumn
lseIntPortPriorityLevel = _LseIntPortPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 8),
    _LseIntPortPriorityLevel_Type()
)
lseIntPortPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortPriorityLevel.setStatus("mandatory")


class _LseIntPortSuperPriorityEnable_Type(Integer32):
    """Custom type lseIntPortSuperPriorityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortSuperPriorityEnable_Type.__name__ = "Integer32"
_LseIntPortSuperPriorityEnable_Object = MibTableColumn
lseIntPortSuperPriorityEnable = _LseIntPortSuperPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 9),
    _LseIntPortSuperPriorityEnable_Type()
)
lseIntPortSuperPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortSuperPriorityEnable.setStatus("mandatory")


class _LseIntPortRoutingMode_Type(Integer32):
    """Custom type lseIntPortRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allPackets", 4),
          ("dst-port", 3),
          ("generic", 1),
          ("net", 2),
          ("notSupported", 255))
    )


_LseIntPortRoutingMode_Type.__name__ = "Integer32"
_LseIntPortRoutingMode_Object = MibTableColumn
lseIntPortRoutingMode = _LseIntPortRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 10),
    _LseIntPortRoutingMode_Type()
)
lseIntPortRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRoutingMode.setStatus("mandatory")


class _LseIntPortGlobal_Type(Integer32):
    """Custom type lseIntPortGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortGlobal_Type.__name__ = "Integer32"
_LseIntPortGlobal_Object = MibTableColumn
lseIntPortGlobal = _LseIntPortGlobal_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 11),
    _LseIntPortGlobal_Type()
)
lseIntPortGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortGlobal.setStatus("mandatory")


class _LseIntPortLearnIOCAM_Type(Integer32):
    """Custom type lseIntPortLearnIOCAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortLearnIOCAM_Type.__name__ = "Integer32"
_LseIntPortLearnIOCAM_Object = MibTableColumn
lseIntPortLearnIOCAM = _LseIntPortLearnIOCAM_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 12),
    _LseIntPortLearnIOCAM_Type()
)
lseIntPortLearnIOCAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortLearnIOCAM.setStatus("mandatory")


class _LseIntPortSecurity_Type(Integer32):
    """Custom type lseIntPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortSecurity_Type.__name__ = "Integer32"
_LseIntPortSecurity_Object = MibTableColumn
lseIntPortSecurity = _LseIntPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 13),
    _LseIntPortSecurity_Type()
)
lseIntPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortSecurity.setStatus("mandatory")


class _LseIntPortIgnoreBusy_Type(Integer32):
    """Custom type lseIntPortIgnoreBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortIgnoreBusy_Type.__name__ = "Integer32"
_LseIntPortIgnoreBusy_Object = MibTableColumn
lseIntPortIgnoreBusy = _LseIntPortIgnoreBusy_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 14),
    _LseIntPortIgnoreBusy_Type()
)
lseIntPortIgnoreBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortIgnoreBusy.setStatus("mandatory")


class _LseIntPortRetryPriorityLevel1_Type(Integer32):
    """Custom type lseIntPortRetryPriorityLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LseIntPortRetryPriorityLevel1_Type.__name__ = "Integer32"
_LseIntPortRetryPriorityLevel1_Object = MibTableColumn
lseIntPortRetryPriorityLevel1 = _LseIntPortRetryPriorityLevel1_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 15),
    _LseIntPortRetryPriorityLevel1_Type()
)
lseIntPortRetryPriorityLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRetryPriorityLevel1.setStatus("mandatory")


class _LseIntPortRetryPriorityLevel2_Type(Integer32):
    """Custom type lseIntPortRetryPriorityLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LseIntPortRetryPriorityLevel2_Type.__name__ = "Integer32"
_LseIntPortRetryPriorityLevel2_Object = MibTableColumn
lseIntPortRetryPriorityLevel2 = _LseIntPortRetryPriorityLevel2_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 16),
    _LseIntPortRetryPriorityLevel2_Type()
)
lseIntPortRetryPriorityLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRetryPriorityLevel2.setStatus("mandatory")


class _LseIntPortRetryPriorityLevel3_Type(Integer32):
    """Custom type lseIntPortRetryPriorityLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LseIntPortRetryPriorityLevel3_Type.__name__ = "Integer32"
_LseIntPortRetryPriorityLevel3_Object = MibTableColumn
lseIntPortRetryPriorityLevel3 = _LseIntPortRetryPriorityLevel3_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 17),
    _LseIntPortRetryPriorityLevel3_Type()
)
lseIntPortRetryPriorityLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRetryPriorityLevel3.setStatus("mandatory")


class _LseIntPortIgnoreProtocolType_Type(Integer32):
    """Custom type lseIntPortIgnoreProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("not-ignore", 2),
          ("notSupported", 255))
    )


_LseIntPortIgnoreProtocolType_Type.__name__ = "Integer32"
_LseIntPortIgnoreProtocolType_Object = MibTableColumn
lseIntPortIgnoreProtocolType = _LseIntPortIgnoreProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 18),
    _LseIntPortIgnoreProtocolType_Type()
)
lseIntPortIgnoreProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortIgnoreProtocolType.setStatus("mandatory")
_LseIntPortCompanyMAC_Type = OctetString
_LseIntPortCompanyMAC_Object = MibTableColumn
lseIntPortCompanyMAC = _LseIntPortCompanyMAC_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 19),
    _LseIntPortCompanyMAC_Type()
)
lseIntPortCompanyMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortCompanyMAC.setStatus("mandatory")


class _LseIntPortTxSafetyZone_Type(Integer32):
    """Custom type lseIntPortTxSafetyZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 510),
    )


_LseIntPortTxSafetyZone_Type.__name__ = "Integer32"
_LseIntPortTxSafetyZone_Object = MibTableColumn
lseIntPortTxSafetyZone = _LseIntPortTxSafetyZone_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 20),
    _LseIntPortTxSafetyZone_Type()
)
lseIntPortTxSafetyZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortTxSafetyZone.setStatus("mandatory")


class _LseIntPortRxSafetyZone_Type(Integer32):
    """Custom type lseIntPortRxSafetyZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 510),
    )


_LseIntPortRxSafetyZone_Type.__name__ = "Integer32"
_LseIntPortRxSafetyZone_Object = MibTableColumn
lseIntPortRxSafetyZone = _LseIntPortRxSafetyZone_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 21),
    _LseIntPortRxSafetyZone_Type()
)
lseIntPortRxSafetyZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRxSafetyZone.setStatus("mandatory")


class _LseIntPortTxBurstLength_Type(Integer32):
    """Custom type lseIntPortTxBurstLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 510),
    )


_LseIntPortTxBurstLength_Type.__name__ = "Integer32"
_LseIntPortTxBurstLength_Object = MibTableColumn
lseIntPortTxBurstLength = _LseIntPortTxBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 22),
    _LseIntPortTxBurstLength_Type()
)
lseIntPortTxBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortTxBurstLength.setStatus("mandatory")


class _LseIntPortSecurityIntruder_Type(Integer32):
    """Custom type lseIntPortSecurityIntruder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortSecurityIntruder_Type.__name__ = "Integer32"
_LseIntPortSecurityIntruder_Object = MibTableColumn
lseIntPortSecurityIntruder = _LseIntPortSecurityIntruder_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 23),
    _LseIntPortSecurityIntruder_Type()
)
lseIntPortSecurityIntruder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortSecurityIntruder.setStatus("mandatory")


class _LseIntPortJabber_Type(Integer32):
    """Custom type lseIntPortJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortJabber_Type.__name__ = "Integer32"
_LseIntPortJabber_Object = MibTableColumn
lseIntPortJabber = _LseIntPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 24),
    _LseIntPortJabber_Type()
)
lseIntPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortJabber.setStatus("mandatory")


class _LseIntPortCAM_Type(OctetString):
    """Custom type lseIntPortCAM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_LseIntPortCAM_Type.__name__ = "OctetString"
_LseIntPortCAM_Object = MibTableColumn
lseIntPortCAM = _LseIntPortCAM_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 25),
    _LseIntPortCAM_Type()
)
lseIntPortCAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortCAM.setStatus("mandatory")


class _LseIntPortVideoStateMachine_Type(Integer32):
    """Custom type lseIntPortVideoStateMachine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortVideoStateMachine_Type.__name__ = "Integer32"
_LseIntPortVideoStateMachine_Object = MibTableColumn
lseIntPortVideoStateMachine = _LseIntPortVideoStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 26),
    _LseIntPortVideoStateMachine_Type()
)
lseIntPortVideoStateMachine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortVideoStateMachine.setStatus("mandatory")


class _LseIntPortTransmitWeight_Type(Integer32):
    """Custom type lseIntPortTransmitWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LseIntPortTransmitWeight_Type.__name__ = "Integer32"
_LseIntPortTransmitWeight_Object = MibTableColumn
lseIntPortTransmitWeight = _LseIntPortTransmitWeight_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 27),
    _LseIntPortTransmitWeight_Type()
)
lseIntPortTransmitWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortTransmitWeight.setStatus("mandatory")


class _LseIntPortSuperPriority_Type(Integer32):
    """Custom type lseIntPortSuperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortSuperPriority_Type.__name__ = "Integer32"
_LseIntPortSuperPriority_Object = MibTableColumn
lseIntPortSuperPriority = _LseIntPortSuperPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 28),
    _LseIntPortSuperPriority_Type()
)
lseIntPortSuperPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortSuperPriority.setStatus("mandatory")
_LseIntPortAlignment_Type = Counter32
_LseIntPortAlignment_Object = MibTableColumn
lseIntPortAlignment = _LseIntPortAlignment_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 29),
    _LseIntPortAlignment_Type()
)
lseIntPortAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortAlignment.setStatus("mandatory")
_LseIntPortRxReject_Type = Counter32
_LseIntPortRxReject_Object = MibTableColumn
lseIntPortRxReject = _LseIntPortRxReject_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 30),
    _LseIntPortRxReject_Type()
)
lseIntPortRxReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortRxReject.setStatus("obsolete")
_LseIntPortTxReject_Type = Counter32
_LseIntPortTxReject_Object = MibTableColumn
lseIntPortTxReject = _LseIntPortTxReject_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 31),
    _LseIntPortTxReject_Type()
)
lseIntPortTxReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortTxReject.setStatus("obsolete")
_LseIntPortRxEmpty0_Type = Integer32
_LseIntPortRxEmpty0_Object = MibTableColumn
lseIntPortRxEmpty0 = _LseIntPortRxEmpty0_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 32),
    _LseIntPortRxEmpty0_Type()
)
lseIntPortRxEmpty0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRxEmpty0.setStatus("mandatory")
_LseIntPortRxEmpty1_Type = Integer32
_LseIntPortRxEmpty1_Object = MibTableColumn
lseIntPortRxEmpty1 = _LseIntPortRxEmpty1_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 33),
    _LseIntPortRxEmpty1_Type()
)
lseIntPortRxEmpty1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRxEmpty1.setStatus("mandatory")
_LseIntPortRxEmpty2_Type = Integer32
_LseIntPortRxEmpty2_Object = MibTableColumn
lseIntPortRxEmpty2 = _LseIntPortRxEmpty2_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 34),
    _LseIntPortRxEmpty2_Type()
)
lseIntPortRxEmpty2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRxEmpty2.setStatus("mandatory")


class _LseIntPortSuperNetNumber_Type(Integer32):
    """Custom type lseIntPortSuperNetNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_LseIntPortSuperNetNumber_Type.__name__ = "Integer32"
_LseIntPortSuperNetNumber_Object = MibTableColumn
lseIntPortSuperNetNumber = _LseIntPortSuperNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 35),
    _LseIntPortSuperNetNumber_Type()
)
lseIntPortSuperNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortSuperNetNumber.setStatus("mandatory")


class _LseIntPortGlobalSuperNet_Type(Integer32):
    """Custom type lseIntPortGlobalSuperNet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortGlobalSuperNet_Type.__name__ = "Integer32"
_LseIntPortGlobalSuperNet_Object = MibTableColumn
lseIntPortGlobalSuperNet = _LseIntPortGlobalSuperNet_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 36),
    _LseIntPortGlobalSuperNet_Type()
)
lseIntPortGlobalSuperNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortGlobalSuperNet.setStatus("mandatory")
_LseIntPortMACAddress_Type = OctetString
_LseIntPortMACAddress_Object = MibTableColumn
lseIntPortMACAddress = _LseIntPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 37),
    _LseIntPortMACAddress_Type()
)
lseIntPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortMACAddress.setStatus("mandatory")


class _LseIntPortIgnoreRoutingMode_Type(Integer32):
    """Custom type lseIntPortIgnoreRoutingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("notIgnore", 2),
          ("notSupported", 255))
    )


_LseIntPortIgnoreRoutingMode_Type.__name__ = "Integer32"
_LseIntPortIgnoreRoutingMode_Object = MibTableColumn
lseIntPortIgnoreRoutingMode = _LseIntPortIgnoreRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 38),
    _LseIntPortIgnoreRoutingMode_Type()
)
lseIntPortIgnoreRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortIgnoreRoutingMode.setStatus("mandatory")
_LseIntPortCAMLastChange_Type = TimeTicks
_LseIntPortCAMLastChange_Object = MibTableColumn
lseIntPortCAMLastChange = _LseIntPortCAMLastChange_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 39),
    _LseIntPortCAMLastChange_Type()
)
lseIntPortCAMLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortCAMLastChange.setStatus("mandatory")
_LseIntPortCopiedPort_Type = Integer32
_LseIntPortCopiedPort_Object = MibTableColumn
lseIntPortCopiedPort = _LseIntPortCopiedPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 40),
    _LseIntPortCopiedPort_Type()
)
lseIntPortCopiedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortCopiedPort.setStatus("mandatory")


class _LseIntPortBroadcastBehavior_Type(Integer32):
    """Custom type lseIntPortBroadcastBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notSupported", 255),
          ("receiveAll", 3),
          ("selective", 2))
    )


_LseIntPortBroadcastBehavior_Type.__name__ = "Integer32"
_LseIntPortBroadcastBehavior_Object = MibTableColumn
lseIntPortBroadcastBehavior = _LseIntPortBroadcastBehavior_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 41),
    _LseIntPortBroadcastBehavior_Type()
)
lseIntPortBroadcastBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortBroadcastBehavior.setStatus("mandatory")


class _LseIntPortFilteringMethod_Type(Integer32):
    """Custom type lseIntPortFilteringMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("group", 4),
          ("notSupported", 255),
          ("source", 1),
          ("sourceOrDestination", 3))
    )


_LseIntPortFilteringMethod_Type.__name__ = "Integer32"
_LseIntPortFilteringMethod_Object = MibTableColumn
lseIntPortFilteringMethod = _LseIntPortFilteringMethod_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 42),
    _LseIntPortFilteringMethod_Type()
)
lseIntPortFilteringMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortFilteringMethod.setStatus("mandatory")


class _LseIntPortSetFilter_Type(OctetString):
    """Custom type lseIntPortSetFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 452),
    )


_LseIntPortSetFilter_Type.__name__ = "OctetString"
_LseIntPortSetFilter_Object = MibTableColumn
lseIntPortSetFilter = _LseIntPortSetFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 43),
    _LseIntPortSetFilter_Type()
)
lseIntPortSetFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortSetFilter.setStatus("mandatory")


class _LseIntPortRemoveFilter_Type(OctetString):
    """Custom type lseIntPortRemoveFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 452),
    )


_LseIntPortRemoveFilter_Type.__name__ = "OctetString"
_LseIntPortRemoveFilter_Object = MibTableColumn
lseIntPortRemoveFilter = _LseIntPortRemoveFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 44),
    _LseIntPortRemoveFilter_Type()
)
lseIntPortRemoveFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRemoveFilter.setStatus("mandatory")


class _LseIntPortClearFilter_Type(Integer32):
    """Custom type lseIntPortClearFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("idle", 1),
          ("notSupported", 255))
    )


_LseIntPortClearFilter_Type.__name__ = "Integer32"
_LseIntPortClearFilter_Object = MibTableColumn
lseIntPortClearFilter = _LseIntPortClearFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 45),
    _LseIntPortClearFilter_Type()
)
lseIntPortClearFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortClearFilter.setStatus("mandatory")
_LseIntPortMonitorMissedEvents_Type = Counter32
_LseIntPortMonitorMissedEvents_Object = MibTableColumn
lseIntPortMonitorMissedEvents = _LseIntPortMonitorMissedEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 1, 1, 46),
    _LseIntPortMonitorMissedEvents_Type()
)
lseIntPortMonitorMissedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortMonitorMissedEvents.setStatus("mandatory")
_LseIntPortMACAdd_ObjectIdentity = ObjectIdentity
lseIntPortMACAdd = _LseIntPortMACAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 2)
)
_LseIntPortMACAddTable_Object = MibTable
lseIntPortMACAddTable = _LseIntPortMACAddTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lseIntPortMACAddTable.setStatus("mandatory")
_LseIntPortMACAddEntry_Object = MibTableRow
lseIntPortMACAddEntry = _LseIntPortMACAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 2, 1, 1)
)
lseIntPortMACAddEntry.setIndexNames(
    (0, "APPLIC-MIB", "lseIntPortMACAddGroupId"),
    (0, "APPLIC-MIB", "lseIntPortMACAddPortId"),
    (0, "APPLIC-MIB", "lseIntPortMACAddLAId"),
)
if mibBuilder.loadTexts:
    lseIntPortMACAddEntry.setStatus("mandatory")


class _LseIntPortMACAddGroupId_Type(Integer32):
    """Custom type lseIntPortMACAddGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortMACAddGroupId_Type.__name__ = "Integer32"
_LseIntPortMACAddGroupId_Object = MibTableColumn
lseIntPortMACAddGroupId = _LseIntPortMACAddGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 2, 1, 1, 1),
    _LseIntPortMACAddGroupId_Type()
)
lseIntPortMACAddGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortMACAddGroupId.setStatus("mandatory")


class _LseIntPortMACAddPortId_Type(Integer32):
    """Custom type lseIntPortMACAddPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortMACAddPortId_Type.__name__ = "Integer32"
_LseIntPortMACAddPortId_Object = MibTableColumn
lseIntPortMACAddPortId = _LseIntPortMACAddPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 2, 1, 1, 2),
    _LseIntPortMACAddPortId_Type()
)
lseIntPortMACAddPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortMACAddPortId.setStatus("mandatory")
_LseIntPortMACAddLAId_Type = Integer32
_LseIntPortMACAddLAId_Object = MibTableColumn
lseIntPortMACAddLAId = _LseIntPortMACAddLAId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 2, 1, 1, 3),
    _LseIntPortMACAddLAId_Type()
)
lseIntPortMACAddLAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortMACAddLAId.setStatus("mandatory")


class _LseIntPortMACAddList_Type(OctetString):
    """Custom type lseIntPortMACAddList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 452),
    )


_LseIntPortMACAddList_Type.__name__ = "OctetString"
_LseIntPortMACAddList_Object = MibTableColumn
lseIntPortMACAddList = _LseIntPortMACAddList_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 2, 1, 1, 4),
    _LseIntPortMACAddList_Type()
)
lseIntPortMACAddList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortMACAddList.setStatus("mandatory")
_LseIntPortFilter_ObjectIdentity = ObjectIdentity
lseIntPortFilter = _LseIntPortFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 3)
)
_LseIntPortFilterTable_Object = MibTable
lseIntPortFilterTable = _LseIntPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lseIntPortFilterTable.setStatus("mandatory")
_LseIntPortFilterEntry_Object = MibTableRow
lseIntPortFilterEntry = _LseIntPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 3, 1, 1)
)
lseIntPortFilterEntry.setIndexNames(
    (0, "APPLIC-MIB", "lseIntPortFilterGroupId"),
    (0, "APPLIC-MIB", "lseIntPortFilterPortId"),
    (0, "APPLIC-MIB", "lseIntPortFilterLAId"),
)
if mibBuilder.loadTexts:
    lseIntPortFilterEntry.setStatus("mandatory")


class _LseIntPortFilterGroupId_Type(Integer32):
    """Custom type lseIntPortFilterGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortFilterGroupId_Type.__name__ = "Integer32"
_LseIntPortFilterGroupId_Object = MibTableColumn
lseIntPortFilterGroupId = _LseIntPortFilterGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 3, 1, 1, 1),
    _LseIntPortFilterGroupId_Type()
)
lseIntPortFilterGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortFilterGroupId.setStatus("mandatory")


class _LseIntPortFilterPortId_Type(Integer32):
    """Custom type lseIntPortFilterPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortFilterPortId_Type.__name__ = "Integer32"
_LseIntPortFilterPortId_Object = MibTableColumn
lseIntPortFilterPortId = _LseIntPortFilterPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 3, 1, 1, 2),
    _LseIntPortFilterPortId_Type()
)
lseIntPortFilterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortFilterPortId.setStatus("mandatory")
_LseIntPortFilterLAId_Type = Integer32
_LseIntPortFilterLAId_Object = MibTableColumn
lseIntPortFilterLAId = _LseIntPortFilterLAId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 3, 1, 1, 3),
    _LseIntPortFilterLAId_Type()
)
lseIntPortFilterLAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortFilterLAId.setStatus("mandatory")


class _LseIntPortFilterList_Type(OctetString):
    """Custom type lseIntPortFilterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 452),
    )


_LseIntPortFilterList_Type.__name__ = "OctetString"
_LseIntPortFilterList_Object = MibTableColumn
lseIntPortFilterList = _LseIntPortFilterList_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 2, 3, 1, 1, 4),
    _LseIntPortFilterList_Type()
)
lseIntPortFilterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortFilterList.setStatus("mandatory")
_LsePort_ObjectIdentity = ObjectIdentity
lsePort = _LsePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 3)
)
_LsePortTable_Object = MibTable
lsePortTable = _LsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lsePortTable.setStatus("mandatory")
_LsePortEntry_Object = MibTableRow
lsePortEntry = _LsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 3, 1, 1)
)
lsePortEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsePortGroupId"),
    (0, "APPLIC-MIB", "lsePortId"),
)
if mibBuilder.loadTexts:
    lsePortEntry.setStatus("mandatory")


class _LsePortGroupId_Type(Integer32):
    """Custom type lsePortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LsePortGroupId_Type.__name__ = "Integer32"
_LsePortGroupId_Object = MibTableColumn
lsePortGroupId = _LsePortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 3, 1, 1, 1),
    _LsePortGroupId_Type()
)
lsePortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsePortGroupId.setStatus("mandatory")


class _LsePortId_Type(Integer32):
    """Custom type lsePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LsePortId_Type.__name__ = "Integer32"
_LsePortId_Object = MibTableColumn
lsePortId = _LsePortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 3, 1, 1, 2),
    _LsePortId_Type()
)
lsePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsePortId.setStatus("mandatory")


class _LsePortPolarity_Type(Integer32):
    """Custom type lsePortPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LsePortPolarity_Type.__name__ = "Integer32"
_LsePortPolarity_Object = MibTableColumn
lsePortPolarity = _LsePortPolarity_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 3, 1, 1, 3),
    _LsePortPolarity_Type()
)
lsePortPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsePortPolarity.setStatus("mandatory")


class _LsePortBackboneStatus_Type(Integer32):
    """Custom type lsePortBackboneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_LsePortBackboneStatus_Type.__name__ = "Integer32"
_LsePortBackboneStatus_Object = MibTableColumn
lsePortBackboneStatus = _LsePortBackboneStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 1, 3, 1, 1, 4),
    _LsePortBackboneStatus_Type()
)
lsePortBackboneStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsePortBackboneStatus.setStatus("mandatory")
_Lhs_ObjectIdentity = ObjectIdentity
lhs = _Lhs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 2)
)
_LhsGroupTable_Object = MibTable
lhsGroupTable = _LhsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 1)
)
if mibBuilder.loadTexts:
    lhsGroupTable.setStatus("mandatory")
_LhsGroupEntry_Object = MibTableRow
lhsGroupEntry = _LhsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 1, 1)
)
lhsGroupEntry.setIndexNames(
    (0, "APPLIC-MIB", "lhsGroupId"),
)
if mibBuilder.loadTexts:
    lhsGroupEntry.setStatus("mandatory")
_LhsGroupId_Type = Integer32
_LhsGroupId_Object = MibTableColumn
lhsGroupId = _LhsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 1, 1, 1),
    _LhsGroupId_Type()
)
lhsGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsGroupId.setStatus("mandatory")
_LhsGroupMainSWVersion_Type = DisplayString
_LhsGroupMainSWVersion_Object = MibTableColumn
lhsGroupMainSWVersion = _LhsGroupMainSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 1, 1, 2),
    _LhsGroupMainSWVersion_Type()
)
lhsGroupMainSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsGroupMainSWVersion.setStatus("mandatory")


class _LhsGroupProtocolType_Type(Integer32):
    """Custom type lhsGroupProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("ethernet-tokenring", 4),
          ("notSupported", 255),
          ("other", 1),
          ("tokenring", 3))
    )


_LhsGroupProtocolType_Type.__name__ = "Integer32"
_LhsGroupProtocolType_Object = MibTableColumn
lhsGroupProtocolType = _LhsGroupProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 1, 1, 3),
    _LhsGroupProtocolType_Type()
)
lhsGroupProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lhsGroupProtocolType.setStatus("mandatory")
_LhsPortTable_Object = MibTable
lhsPortTable = _LhsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2)
)
if mibBuilder.loadTexts:
    lhsPortTable.setStatus("mandatory")
_LhsPortEntry_Object = MibTableRow
lhsPortEntry = _LhsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1)
)
lhsPortEntry.setIndexNames(
    (0, "APPLIC-MIB", "lhsPortGroupId"),
    (0, "APPLIC-MIB", "lhsPortId"),
)
if mibBuilder.loadTexts:
    lhsPortEntry.setStatus("mandatory")
_LhsPortGroupId_Type = Integer32
_LhsPortGroupId_Object = MibTableColumn
lhsPortGroupId = _LhsPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 1),
    _LhsPortGroupId_Type()
)
lhsPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsPortGroupId.setStatus("mandatory")
_LhsPortId_Type = Integer32
_LhsPortId_Object = MibTableColumn
lhsPortId = _LhsPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 2),
    _LhsPortId_Type()
)
lhsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsPortId.setStatus("mandatory")
_LhsTxUCast_Type = Counter32
_LhsTxUCast_Object = MibTableColumn
lhsTxUCast = _LhsTxUCast_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 3),
    _LhsTxUCast_Type()
)
lhsTxUCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsTxUCast.setStatus("mandatory")
_LhsTxBCast_Type = Counter32
_LhsTxBCast_Object = MibTableColumn
lhsTxBCast = _LhsTxBCast_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 4),
    _LhsTxBCast_Type()
)
lhsTxBCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsTxBCast.setStatus("mandatory")
_LhsTxMCast_Type = Counter32
_LhsTxMCast_Object = MibTableColumn
lhsTxMCast = _LhsTxMCast_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 5),
    _LhsTxMCast_Type()
)
lhsTxMCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsTxMCast.setStatus("mandatory")
_LhsTxUrunErr_Type = Counter32
_LhsTxUrunErr_Object = MibTableColumn
lhsTxUrunErr = _LhsTxUrunErr_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 6),
    _LhsTxUrunErr_Type()
)
lhsTxUrunErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsTxUrunErr.setStatus("mandatory")
_LhsTxParErr_Type = Counter32
_LhsTxParErr_Object = MibTableColumn
lhsTxParErr = _LhsTxParErr_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 7),
    _LhsTxParErr_Type()
)
lhsTxParErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsTxParErr.setStatus("mandatory")
_LhsRxUCast_Type = Counter32
_LhsRxUCast_Object = MibTableColumn
lhsRxUCast = _LhsRxUCast_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 8),
    _LhsRxUCast_Type()
)
lhsRxUCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsRxUCast.setStatus("mandatory")
_LhsRxBCast_Type = Counter32
_LhsRxBCast_Object = MibTableColumn
lhsRxBCast = _LhsRxBCast_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 9),
    _LhsRxBCast_Type()
)
lhsRxBCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsRxBCast.setStatus("mandatory")
_LhsRxMCast_Type = Counter32
_LhsRxMCast_Object = MibTableColumn
lhsRxMCast = _LhsRxMCast_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 10),
    _LhsRxMCast_Type()
)
lhsRxMCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsRxMCast.setStatus("mandatory")
_LhsRxOrunErr_Type = Counter32
_LhsRxOrunErr_Object = MibTableColumn
lhsRxOrunErr = _LhsRxOrunErr_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 11),
    _LhsRxOrunErr_Type()
)
lhsRxOrunErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsRxOrunErr.setStatus("mandatory")
_LhsRxParErr_Type = Counter32
_LhsRxParErr_Object = MibTableColumn
lhsRxParErr = _LhsRxParErr_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 12),
    _LhsRxParErr_Type()
)
lhsRxParErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsRxParErr.setStatus("mandatory")
_LhsRxRscErr_Type = Counter32
_LhsRxRscErr_Object = MibTableColumn
lhsRxRscErr = _LhsRxRscErr_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 13),
    _LhsRxRscErr_Type()
)
lhsRxRscErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsRxRscErr.setStatus("mandatory")
_LhsRxBadTypeErr_Type = Counter32
_LhsRxBadTypeErr_Object = MibTableColumn
lhsRxBadTypeErr = _LhsRxBadTypeErr_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 14),
    _LhsRxBadTypeErr_Type()
)
lhsRxBadTypeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsRxBadTypeErr.setStatus("mandatory")


class _LhsLinkStatus_Type(Integer32):
    """Custom type lhsLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("linkFailure", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_LhsLinkStatus_Type.__name__ = "Integer32"
_LhsLinkStatus_Object = MibTableColumn
lhsLinkStatus = _LhsLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 2, 2, 1, 15),
    _LhsLinkStatus_Type()
)
lhsLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhsLinkStatus.setStatus("mandatory")
_LsMonitor_ObjectIdentity = ObjectIdentity
lsMonitor = _LsMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 3)
)


class _LsMonitorResourceAllocation_Type(Integer32):
    """Custom type lsMonitorResourceAllocation based on Integer32"""
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
        *(("hostMatrix", 4),
          ("hostStats", 2),
          ("none", 1),
          ("portExtendedStats", 3))
    )


_LsMonitorResourceAllocation_Type.__name__ = "Integer32"
_LsMonitorResourceAllocation_Object = MibScalar
lsMonitorResourceAllocation = _LsMonitorResourceAllocation_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 1),
    _LsMonitorResourceAllocation_Type()
)
lsMonitorResourceAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsMonitorResourceAllocation.setStatus("mandatory")
_LsBusStats_ObjectIdentity = ObjectIdentity
lsBusStats = _LsBusStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2)
)
_LsBusStatsDropEvents_Type = Counter32
_LsBusStatsDropEvents_Object = MibScalar
lsBusStatsDropEvents = _LsBusStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 1),
    _LsBusStatsDropEvents_Type()
)
lsBusStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsDropEvents.setStatus("mandatory")
_LsBusStatsPkts_Type = Counter32
_LsBusStatsPkts_Object = MibScalar
lsBusStatsPkts = _LsBusStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 2),
    _LsBusStatsPkts_Type()
)
lsBusStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsPkts.setStatus("mandatory")
_LsBusStatsOctets_Type = Counter32
_LsBusStatsOctets_Object = MibScalar
lsBusStatsOctets = _LsBusStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 3),
    _LsBusStatsOctets_Type()
)
lsBusStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsOctets.setStatus("mandatory")
_LsBusStatsUtilization_Type = Integer32
_LsBusStatsUtilization_Object = MibScalar
lsBusStatsUtilization = _LsBusStatsUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 4),
    _LsBusStatsUtilization_Type()
)
lsBusStatsUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsUtilization.setStatus("mandatory")
_LsBusStatsEthBroadcastPkts_Type = Counter32
_LsBusStatsEthBroadcastPkts_Object = MibScalar
lsBusStatsEthBroadcastPkts = _LsBusStatsEthBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 5),
    _LsBusStatsEthBroadcastPkts_Type()
)
lsBusStatsEthBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsEthBroadcastPkts.setStatus("mandatory")
_LsBusStatsMulticastPkts_Type = Counter32
_LsBusStatsMulticastPkts_Object = MibScalar
lsBusStatsMulticastPkts = _LsBusStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 6),
    _LsBusStatsMulticastPkts_Type()
)
lsBusStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsMulticastPkts.setStatus("mandatory")
_LsBusStatsGoodEthPkts_Type = Counter32
_LsBusStatsGoodEthPkts_Object = MibScalar
lsBusStatsGoodEthPkts = _LsBusStatsGoodEthPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 7),
    _LsBusStatsGoodEthPkts_Type()
)
lsBusStatsGoodEthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsGoodEthPkts.setStatus("mandatory")
_LsBusStatsGoodEthOctets_Type = Counter32
_LsBusStatsGoodEthOctets_Object = MibScalar
lsBusStatsGoodEthOctets = _LsBusStatsGoodEthOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 8),
    _LsBusStatsGoodEthOctets_Type()
)
lsBusStatsGoodEthOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsGoodEthOctets.setStatus("mandatory")
_LsBusStatsBadEthPkts_Type = Counter32
_LsBusStatsBadEthPkts_Object = MibScalar
lsBusStatsBadEthPkts = _LsBusStatsBadEthPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 9),
    _LsBusStatsBadEthPkts_Type()
)
lsBusStatsBadEthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsBadEthPkts.setStatus("mandatory")
_LsBusStatsBadEthOctets_Type = Counter32
_LsBusStatsBadEthOctets_Object = MibScalar
lsBusStatsBadEthOctets = _LsBusStatsBadEthOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 10),
    _LsBusStatsBadEthOctets_Type()
)
lsBusStatsBadEthOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsBadEthOctets.setStatus("mandatory")
_LsBusStatsNonEthPkts_Type = Counter32
_LsBusStatsNonEthPkts_Object = MibScalar
lsBusStatsNonEthPkts = _LsBusStatsNonEthPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 11),
    _LsBusStatsNonEthPkts_Type()
)
lsBusStatsNonEthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsNonEthPkts.setStatus("mandatory")
_LsBusStatsNonEthOctets_Type = Counter32
_LsBusStatsNonEthOctets_Object = MibScalar
lsBusStatsNonEthOctets = _LsBusStatsNonEthOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 12),
    _LsBusStatsNonEthOctets_Type()
)
lsBusStatsNonEthOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsNonEthOctets.setStatus("mandatory")
_LsBusStatsPriorityTable_Object = MibTable
lsBusStatsPriorityTable = _LsBusStatsPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 13)
)
if mibBuilder.loadTexts:
    lsBusStatsPriorityTable.setStatus("mandatory")
_LsBusStatsPriorityEntry_Object = MibTableRow
lsBusStatsPriorityEntry = _LsBusStatsPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 13, 1)
)
lsBusStatsPriorityEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsBusStatsPriorityIndex"),
)
if mibBuilder.loadTexts:
    lsBusStatsPriorityEntry.setStatus("mandatory")


class _LsBusStatsPriorityIndex_Type(Integer32):
    """Custom type lsBusStatsPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LsBusStatsPriorityIndex_Type.__name__ = "Integer32"
_LsBusStatsPriorityIndex_Object = MibTableColumn
lsBusStatsPriorityIndex = _LsBusStatsPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 13, 1, 1),
    _LsBusStatsPriorityIndex_Type()
)
lsBusStatsPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsPriorityIndex.setStatus("mandatory")
_LsBusStatsPriorityPkts_Type = Counter32
_LsBusStatsPriorityPkts_Object = MibTableColumn
lsBusStatsPriorityPkts = _LsBusStatsPriorityPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 13, 1, 2),
    _LsBusStatsPriorityPkts_Type()
)
lsBusStatsPriorityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsPriorityPkts.setStatus("mandatory")
_LsBusStatsPriorityOctets_Type = Counter32
_LsBusStatsPriorityOctets_Object = MibTableColumn
lsBusStatsPriorityOctets = _LsBusStatsPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 13, 1, 3),
    _LsBusStatsPriorityOctets_Type()
)
lsBusStatsPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsPriorityOctets.setStatus("mandatory")


class _LsBusStatsVirtualNetList_Type(OctetString):
    """Custom type lsBusStatsVirtualNetList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LsBusStatsVirtualNetList_Type.__name__ = "OctetString"
_LsBusStatsVirtualNetList_Object = MibScalar
lsBusStatsVirtualNetList = _LsBusStatsVirtualNetList_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 14),
    _LsBusStatsVirtualNetList_Type()
)
lsBusStatsVirtualNetList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsVirtualNetList.setStatus("mandatory")
_LsBusStatsVirtualNetTable_Object = MibTable
lsBusStatsVirtualNetTable = _LsBusStatsVirtualNetTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 15)
)
if mibBuilder.loadTexts:
    lsBusStatsVirtualNetTable.setStatus("mandatory")
_LsBusStatsVirtualNetEntry_Object = MibTableRow
lsBusStatsVirtualNetEntry = _LsBusStatsVirtualNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 15, 1)
)
lsBusStatsVirtualNetEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsBusStatsVirtualNet"),
)
if mibBuilder.loadTexts:
    lsBusStatsVirtualNetEntry.setStatus("mandatory")
_LsBusStatsVirtualNet_Type = Integer32
_LsBusStatsVirtualNet_Object = MibTableColumn
lsBusStatsVirtualNet = _LsBusStatsVirtualNet_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 15, 1, 1),
    _LsBusStatsVirtualNet_Type()
)
lsBusStatsVirtualNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsVirtualNet.setStatus("mandatory")
_LsBusStatsVirtualNetPackets_Type = Counter32
_LsBusStatsVirtualNetPackets_Object = MibTableColumn
lsBusStatsVirtualNetPackets = _LsBusStatsVirtualNetPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 15, 1, 2),
    _LsBusStatsVirtualNetPackets_Type()
)
lsBusStatsVirtualNetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsVirtualNetPackets.setStatus("mandatory")
_LsBusStatsVirtualNetOctets_Type = Counter32
_LsBusStatsVirtualNetOctets_Object = MibTableColumn
lsBusStatsVirtualNetOctets = _LsBusStatsVirtualNetOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 2, 15, 1, 3),
    _LsBusStatsVirtualNetOctets_Type()
)
lsBusStatsVirtualNetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBusStatsVirtualNetOctets.setStatus("mandatory")
_LsPortStats_ObjectIdentity = ObjectIdentity
lsPortStats = _LsPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3)
)
_LsPortControlTable_Object = MibTable
lsPortControlTable = _LsPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lsPortControlTable.setStatus("mandatory")
_LsPortControlEntry_Object = MibTableRow
lsPortControlEntry = _LsPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1, 1)
)
lsPortControlEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsPortControlIndex"),
)
if mibBuilder.loadTexts:
    lsPortControlEntry.setStatus("mandatory")


class _LsPortControlIndex_Type(Integer32):
    """Custom type lsPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LsPortControlIndex_Type.__name__ = "Integer32"
_LsPortControlIndex_Object = MibTableColumn
lsPortControlIndex = _LsPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1, 1, 1),
    _LsPortControlIndex_Type()
)
lsPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortControlIndex.setStatus("mandatory")
_LsPortControlDataSource_Type = ObjectIdentifier
_LsPortControlDataSource_Object = MibTableColumn
lsPortControlDataSource = _LsPortControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1, 1, 2),
    _LsPortControlDataSource_Type()
)
lsPortControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPortControlDataSource.setStatus("mandatory")
_LsPortControlTableSize_Type = Integer32
_LsPortControlTableSize_Object = MibTableColumn
lsPortControlTableSize = _LsPortControlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1, 1, 3),
    _LsPortControlTableSize_Type()
)
lsPortControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortControlTableSize.setStatus("mandatory")
_LsPortControlLastDeleteTime_Type = TimeTicks
_LsPortControlLastDeleteTime_Object = MibTableColumn
lsPortControlLastDeleteTime = _LsPortControlLastDeleteTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1, 1, 4),
    _LsPortControlLastDeleteTime_Type()
)
lsPortControlLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortControlLastDeleteTime.setStatus("mandatory")
_LsPortControlOwner_Type = DisplayString
_LsPortControlOwner_Object = MibTableColumn
lsPortControlOwner = _LsPortControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1, 1, 5),
    _LsPortControlOwner_Type()
)
lsPortControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPortControlOwner.setStatus("mandatory")


class _LsPortControlStatus_Type(Integer32):
    """Custom type lsPortControlStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_LsPortControlStatus_Type.__name__ = "Integer32"
_LsPortControlStatus_Object = MibTableColumn
lsPortControlStatus = _LsPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 1, 1, 6),
    _LsPortControlStatus_Type()
)
lsPortControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPortControlStatus.setStatus("mandatory")
_LsPortFilterTable_Object = MibTable
lsPortFilterTable = _LsPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 2)
)
if mibBuilder.loadTexts:
    lsPortFilterTable.setStatus("mandatory")
_LsPortFilterEntry_Object = MibTableRow
lsPortFilterEntry = _LsPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 2, 1)
)
lsPortFilterEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsPortFilter"),
)
if mibBuilder.loadTexts:
    lsPortFilterEntry.setStatus("mandatory")
_LsPortFilter_Type = Integer32
_LsPortFilter_Object = MibTableColumn
lsPortFilter = _LsPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 2, 1, 1),
    _LsPortFilter_Type()
)
lsPortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortFilter.setStatus("mandatory")


class _LsPortFilterStatus_Type(Integer32):
    """Custom type lsPortFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 4),
          ("valid", 1))
    )


_LsPortFilterStatus_Type.__name__ = "Integer32"
_LsPortFilterStatus_Object = MibTableColumn
lsPortFilterStatus = _LsPortFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 2, 1, 2),
    _LsPortFilterStatus_Type()
)
lsPortFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPortFilterStatus.setStatus("mandatory")


class _LsPortFilterTableClear_Type(Integer32):
    """Custom type lsPortFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("idle", 1))
    )


_LsPortFilterTableClear_Type.__name__ = "Integer32"
_LsPortFilterTableClear_Object = MibScalar
lsPortFilterTableClear = _LsPortFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 3),
    _LsPortFilterTableClear_Type()
)
lsPortFilterTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPortFilterTableClear.setStatus("mandatory")
_LsPortTable_Object = MibTable
lsPortTable = _LsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4)
)
if mibBuilder.loadTexts:
    lsPortTable.setStatus("mandatory")
_LsPortEntry_Object = MibTableRow
lsPortEntry = _LsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1)
)
lsPortEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsPortNumber"),
)
if mibBuilder.loadTexts:
    lsPortEntry.setStatus("mandatory")
_LsPortNumber_Type = Integer32
_LsPortNumber_Object = MibTableColumn
lsPortNumber = _LsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1, 1),
    _LsPortNumber_Type()
)
lsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortNumber.setStatus("mandatory")
_LsPortInPkts_Type = Counter32
_LsPortInPkts_Object = MibTableColumn
lsPortInPkts = _LsPortInPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1, 2),
    _LsPortInPkts_Type()
)
lsPortInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInPkts.setStatus("mandatory")
_LsPortInFCSErrors_Type = Counter32
_LsPortInFCSErrors_Object = MibTableColumn
lsPortInFCSErrors = _LsPortInFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1, 3),
    _LsPortInFCSErrors_Type()
)
lsPortInFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInFCSErrors.setStatus("mandatory")
_LsPortInTooLongPkts_Type = Counter32
_LsPortInTooLongPkts_Object = MibTableColumn
lsPortInTooLongPkts = _LsPortInTooLongPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1, 4),
    _LsPortInTooLongPkts_Type()
)
lsPortInTooLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInTooLongPkts.setStatus("mandatory")
_LsPortInOctets_Type = Counter32
_LsPortInOctets_Object = MibTableColumn
lsPortInOctets = _LsPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1, 5),
    _LsPortInOctets_Type()
)
lsPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInOctets.setStatus("mandatory")
_LsPortInTotalErrors_Type = Counter32
_LsPortInTotalErrors_Object = MibTableColumn
lsPortInTotalErrors = _LsPortInTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1, 6),
    _LsPortInTotalErrors_Type()
)
lsPortInTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInTotalErrors.setStatus("mandatory")
_LsPortInCollisions_Type = Counter32
_LsPortInCollisions_Object = MibTableColumn
lsPortInCollisions = _LsPortInCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 4, 1, 7),
    _LsPortInCollisions_Type()
)
lsPortInCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInCollisions.setStatus("mandatory")


class _LsPortExtendedReportingList_Type(OctetString):
    """Custom type lsPortExtendedReportingList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LsPortExtendedReportingList_Type.__name__ = "OctetString"
_LsPortExtendedReportingList_Object = MibScalar
lsPortExtendedReportingList = _LsPortExtendedReportingList_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 5),
    _LsPortExtendedReportingList_Type()
)
lsPortExtendedReportingList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortExtendedReportingList.setStatus("mandatory")
_LsPortExtendedStatsTable_Object = MibTable
lsPortExtendedStatsTable = _LsPortExtendedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6)
)
if mibBuilder.loadTexts:
    lsPortExtendedStatsTable.setStatus("mandatory")
_LsPortExtendedStatsEntry_Object = MibTableRow
lsPortExtendedStatsEntry = _LsPortExtendedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6, 1)
)
lsPortExtendedStatsEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsPortExtendedStatsNumber"),
)
if mibBuilder.loadTexts:
    lsPortExtendedStatsEntry.setStatus("mandatory")
_LsPortExtendedStatsNumber_Type = Integer32
_LsPortExtendedStatsNumber_Object = MibTableColumn
lsPortExtendedStatsNumber = _LsPortExtendedStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6, 1, 1),
    _LsPortExtendedStatsNumber_Type()
)
lsPortExtendedStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortExtendedStatsNumber.setStatus("mandatory")


class _LsPortCreationOrder_Type(Integer32):
    """Custom type lsPortCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LsPortCreationOrder_Type.__name__ = "Integer32"
_LsPortCreationOrder_Object = MibTableColumn
lsPortCreationOrder = _LsPortCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6, 1, 2),
    _LsPortCreationOrder_Type()
)
lsPortCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortCreationOrder.setStatus("mandatory")


class _LsPortIndex_Type(Integer32):
    """Custom type lsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LsPortIndex_Type.__name__ = "Integer32"
_LsPortIndex_Object = MibTableColumn
lsPortIndex = _LsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6, 1, 3),
    _LsPortIndex_Type()
)
lsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortIndex.setStatus("mandatory")
_LsPortOutPkts_Type = Counter32
_LsPortOutPkts_Object = MibTableColumn
lsPortOutPkts = _LsPortOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6, 1, 4),
    _LsPortOutPkts_Type()
)
lsPortOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortOutPkts.setStatus("mandatory")
_LsPortInBroadcastPkts_Type = Counter32
_LsPortInBroadcastPkts_Object = MibTableColumn
lsPortInBroadcastPkts = _LsPortInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6, 1, 5),
    _LsPortInBroadcastPkts_Type()
)
lsPortInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInBroadcastPkts.setStatus("mandatory")
_LsPortInMulticastPkts_Type = Counter32
_LsPortInMulticastPkts_Object = MibTableColumn
lsPortInMulticastPkts = _LsPortInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 3, 6, 1, 6),
    _LsPortInMulticastPkts_Type()
)
lsPortInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortInMulticastPkts.setStatus("mandatory")
_LsHostFilterTable_Object = MibTable
lsHostFilterTable = _LsHostFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 4)
)
if mibBuilder.loadTexts:
    lsHostFilterTable.setStatus("mandatory")
_LsHostFilterEntry_Object = MibTableRow
lsHostFilterEntry = _LsHostFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 4, 1)
)
lsHostFilterEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsHostFilterAddress"),
)
if mibBuilder.loadTexts:
    lsHostFilterEntry.setStatus("mandatory")
_LsHostFilterAddress_Type = OctetString
_LsHostFilterAddress_Object = MibTableColumn
lsHostFilterAddress = _LsHostFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 4, 1, 1),
    _LsHostFilterAddress_Type()
)
lsHostFilterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHostFilterAddress.setStatus("mandatory")


class _LsHostFilterStatus_Type(Integer32):
    """Custom type lsHostFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 4),
          ("valid", 1))
    )


_LsHostFilterStatus_Type.__name__ = "Integer32"
_LsHostFilterStatus_Object = MibTableColumn
lsHostFilterStatus = _LsHostFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 4, 1, 2),
    _LsHostFilterStatus_Type()
)
lsHostFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsHostFilterStatus.setStatus("mandatory")


class _LsHostFilterTableClear_Type(Integer32):
    """Custom type lsHostFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("idle", 1))
    )


_LsHostFilterTableClear_Type.__name__ = "Integer32"
_LsHostFilterTableClear_Object = MibScalar
lsHostFilterTableClear = _LsHostFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 5),
    _LsHostFilterTableClear_Type()
)
lsHostFilterTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsHostFilterTableClear.setStatus("mandatory")
_LsHostPortFilterTable_Object = MibTable
lsHostPortFilterTable = _LsHostPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 6)
)
if mibBuilder.loadTexts:
    lsHostPortFilterTable.setStatus("mandatory")
_LsHostPortFilterEntry_Object = MibTableRow
lsHostPortFilterEntry = _LsHostPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 6, 1)
)
lsHostPortFilterEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsHostPortFilter"),
)
if mibBuilder.loadTexts:
    lsHostPortFilterEntry.setStatus("mandatory")
_LsHostPortFilter_Type = Integer32
_LsHostPortFilter_Object = MibTableColumn
lsHostPortFilter = _LsHostPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 6, 1, 1),
    _LsHostPortFilter_Type()
)
lsHostPortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHostPortFilter.setStatus("mandatory")


class _LsHostPortFilterStatus_Type(Integer32):
    """Custom type lsHostPortFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 4),
          ("valid", 1))
    )


_LsHostPortFilterStatus_Type.__name__ = "Integer32"
_LsHostPortFilterStatus_Object = MibTableColumn
lsHostPortFilterStatus = _LsHostPortFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 6, 1, 2),
    _LsHostPortFilterStatus_Type()
)
lsHostPortFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsHostPortFilterStatus.setStatus("mandatory")


class _LsHostPortFilterTableClear_Type(Integer32):
    """Custom type lsHostPortFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("idle", 1))
    )


_LsHostPortFilterTableClear_Type.__name__ = "Integer32"
_LsHostPortFilterTableClear_Object = MibScalar
lsHostPortFilterTableClear = _LsHostPortFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 7),
    _LsHostPortFilterTableClear_Type()
)
lsHostPortFilterTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsHostPortFilterTableClear.setStatus("mandatory")
_LsMatrixFilterTable_Object = MibTable
lsMatrixFilterTable = _LsMatrixFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 8)
)
if mibBuilder.loadTexts:
    lsMatrixFilterTable.setStatus("mandatory")
_LsMatrixFilterEntry_Object = MibTableRow
lsMatrixFilterEntry = _LsMatrixFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 8, 1)
)
lsMatrixFilterEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsMatrixFilterAddress"),
)
if mibBuilder.loadTexts:
    lsMatrixFilterEntry.setStatus("mandatory")
_LsMatrixFilterAddress_Type = OctetString
_LsMatrixFilterAddress_Object = MibTableColumn
lsMatrixFilterAddress = _LsMatrixFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 8, 1, 1),
    _LsMatrixFilterAddress_Type()
)
lsMatrixFilterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsMatrixFilterAddress.setStatus("mandatory")


class _LsMatrixFilterStatus_Type(Integer32):
    """Custom type lsMatrixFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 4),
          ("valid", 1))
    )


_LsMatrixFilterStatus_Type.__name__ = "Integer32"
_LsMatrixFilterStatus_Object = MibTableColumn
lsMatrixFilterStatus = _LsMatrixFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 8, 1, 2),
    _LsMatrixFilterStatus_Type()
)
lsMatrixFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsMatrixFilterStatus.setStatus("mandatory")


class _LsMatrixFilterTableClear_Type(Integer32):
    """Custom type lsMatrixFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("idle", 1))
    )


_LsMatrixFilterTableClear_Type.__name__ = "Integer32"
_LsMatrixFilterTableClear_Object = MibScalar
lsMatrixFilterTableClear = _LsMatrixFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 9),
    _LsMatrixFilterTableClear_Type()
)
lsMatrixFilterTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsMatrixFilterTableClear.setStatus("mandatory")
_LsHostTimePortCorrTable_Object = MibTable
lsHostTimePortCorrTable = _LsHostTimePortCorrTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 10)
)
if mibBuilder.loadTexts:
    lsHostTimePortCorrTable.setStatus("mandatory")
_LsHostTimePortCorrEntry_Object = MibTableRow
lsHostTimePortCorrEntry = _LsHostTimePortCorrEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 10, 1)
)
lsHostTimePortCorrEntry.setIndexNames(
    (0, "APPLIC-MIB", "hostTimeIndex"),
    (0, "APPLIC-MIB", "hostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    lsHostTimePortCorrEntry.setStatus("mandatory")
_HostTimeAddress_Type = OctetString
_HostTimeAddress_Object = MibTableColumn
hostTimeAddress = _HostTimeAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 10, 1, 1),
    _HostTimeAddress_Type()
)
hostTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeAddress.setStatus("mandatory")


class _HostTimeCreationOrder_Type(Integer32):
    """Custom type hostTimeCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeCreationOrder_Type.__name__ = "Integer32"
_HostTimeCreationOrder_Object = MibTableColumn
hostTimeCreationOrder = _HostTimeCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 10, 1, 2),
    _HostTimeCreationOrder_Type()
)
hostTimeCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeCreationOrder.setStatus("mandatory")


class _HostTimeIndex_Type(Integer32):
    """Custom type hostTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeIndex_Type.__name__ = "Integer32"
_HostTimeIndex_Object = MibTableColumn
hostTimeIndex = _HostTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 10, 1, 3),
    _HostTimeIndex_Type()
)
hostTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeIndex.setStatus("mandatory")
_HostTimePortConnection_Type = Integer32
_HostTimePortConnection_Object = MibTableColumn
hostTimePortConnection = _HostTimePortConnection_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 10, 1, 4),
    _HostTimePortConnection_Type()
)
hostTimePortConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimePortConnection.setStatus("mandatory")
_LsHistoryTable_Object = MibTable
lsHistoryTable = _LsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11)
)
if mibBuilder.loadTexts:
    lsHistoryTable.setStatus("mandatory")
_LsHistoryEntry_Object = MibTableRow
lsHistoryEntry = _LsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1)
)
lsHistoryEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsHistoryIndex"),
    (0, "APPLIC-MIB", "lsHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    lsHistoryEntry.setStatus("mandatory")
_LsHistoryIndex_Type = Integer32
_LsHistoryIndex_Object = MibTableColumn
lsHistoryIndex = _LsHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 1),
    _LsHistoryIndex_Type()
)
lsHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryIndex.setStatus("mandatory")


class _LsHistorySampleIndex_Type(Integer32):
    """Custom type lsHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LsHistorySampleIndex_Type.__name__ = "Integer32"
_LsHistorySampleIndex_Object = MibTableColumn
lsHistorySampleIndex = _LsHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 2),
    _LsHistorySampleIndex_Type()
)
lsHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistorySampleIndex.setStatus("mandatory")
_LsHistoryIntervalTime_Type = TimeTicks
_LsHistoryIntervalTime_Object = MibTableColumn
lsHistoryIntervalTime = _LsHistoryIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 3),
    _LsHistoryIntervalTime_Type()
)
lsHistoryIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryIntervalTime.setStatus("mandatory")
_LsHistoryStatsDropEvents_Type = Counter32
_LsHistoryStatsDropEvents_Object = MibTableColumn
lsHistoryStatsDropEvents = _LsHistoryStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 4),
    _LsHistoryStatsDropEvents_Type()
)
lsHistoryStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsDropEvents.setStatus("mandatory")
_LsHistoryStatsPkts_Type = Counter32
_LsHistoryStatsPkts_Object = MibTableColumn
lsHistoryStatsPkts = _LsHistoryStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 5),
    _LsHistoryStatsPkts_Type()
)
lsHistoryStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPkts.setStatus("mandatory")
_LsHistoryStatsOctets_Type = Counter32
_LsHistoryStatsOctets_Object = MibTableColumn
lsHistoryStatsOctets = _LsHistoryStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 6),
    _LsHistoryStatsOctets_Type()
)
lsHistoryStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsOctets.setStatus("mandatory")
_LsHistoryStatsEthBroadcastPkts_Type = Counter32
_LsHistoryStatsEthBroadcastPkts_Object = MibTableColumn
lsHistoryStatsEthBroadcastPkts = _LsHistoryStatsEthBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 7),
    _LsHistoryStatsEthBroadcastPkts_Type()
)
lsHistoryStatsEthBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsEthBroadcastPkts.setStatus("mandatory")
_LsHistoryStatsEthMulticastPkts_Type = Counter32
_LsHistoryStatsEthMulticastPkts_Object = MibTableColumn
lsHistoryStatsEthMulticastPkts = _LsHistoryStatsEthMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 8),
    _LsHistoryStatsEthMulticastPkts_Type()
)
lsHistoryStatsEthMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsEthMulticastPkts.setStatus("mandatory")
_LsHistoryStatsGoodEthPkts_Type = Counter32
_LsHistoryStatsGoodEthPkts_Object = MibTableColumn
lsHistoryStatsGoodEthPkts = _LsHistoryStatsGoodEthPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 9),
    _LsHistoryStatsGoodEthPkts_Type()
)
lsHistoryStatsGoodEthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsGoodEthPkts.setStatus("mandatory")
_LsHistoryStatsGoodEthOctets_Type = Counter32
_LsHistoryStatsGoodEthOctets_Object = MibTableColumn
lsHistoryStatsGoodEthOctets = _LsHistoryStatsGoodEthOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 10),
    _LsHistoryStatsGoodEthOctets_Type()
)
lsHistoryStatsGoodEthOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsGoodEthOctets.setStatus("mandatory")
_LsHistoryStatsBadEthPkts_Type = Counter32
_LsHistoryStatsBadEthPkts_Object = MibTableColumn
lsHistoryStatsBadEthPkts = _LsHistoryStatsBadEthPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 11),
    _LsHistoryStatsBadEthPkts_Type()
)
lsHistoryStatsBadEthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsBadEthPkts.setStatus("mandatory")
_LsHistoryStatsBadEthOctets_Type = Counter32
_LsHistoryStatsBadEthOctets_Object = MibTableColumn
lsHistoryStatsBadEthOctets = _LsHistoryStatsBadEthOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 12),
    _LsHistoryStatsBadEthOctets_Type()
)
lsHistoryStatsBadEthOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsBadEthOctets.setStatus("mandatory")
_LsHistoryStatsNonEthPkts_Type = Counter32
_LsHistoryStatsNonEthPkts_Object = MibTableColumn
lsHistoryStatsNonEthPkts = _LsHistoryStatsNonEthPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 13),
    _LsHistoryStatsNonEthPkts_Type()
)
lsHistoryStatsNonEthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsNonEthPkts.setStatus("mandatory")
_LsHistoryStatsNonEthOctets_Type = Counter32
_LsHistoryStatsNonEthOctets_Object = MibTableColumn
lsHistoryStatsNonEthOctets = _LsHistoryStatsNonEthOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 14),
    _LsHistoryStatsNonEthOctets_Type()
)
lsHistoryStatsNonEthOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsNonEthOctets.setStatus("mandatory")
_LsHistoryStatsPriority1Pkts_Type = Counter32
_LsHistoryStatsPriority1Pkts_Object = MibTableColumn
lsHistoryStatsPriority1Pkts = _LsHistoryStatsPriority1Pkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 15),
    _LsHistoryStatsPriority1Pkts_Type()
)
lsHistoryStatsPriority1Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority1Pkts.setStatus("mandatory")
_LsHistoryStatsPriority1Octets_Type = Counter32
_LsHistoryStatsPriority1Octets_Object = MibTableColumn
lsHistoryStatsPriority1Octets = _LsHistoryStatsPriority1Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 16),
    _LsHistoryStatsPriority1Octets_Type()
)
lsHistoryStatsPriority1Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority1Octets.setStatus("mandatory")
_LsHistoryStatsPriority2Pkts_Type = Counter32
_LsHistoryStatsPriority2Pkts_Object = MibTableColumn
lsHistoryStatsPriority2Pkts = _LsHistoryStatsPriority2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 17),
    _LsHistoryStatsPriority2Pkts_Type()
)
lsHistoryStatsPriority2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority2Pkts.setStatus("mandatory")
_LsHistoryStatsPriority2Octets_Type = Counter32
_LsHistoryStatsPriority2Octets_Object = MibTableColumn
lsHistoryStatsPriority2Octets = _LsHistoryStatsPriority2Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 18),
    _LsHistoryStatsPriority2Octets_Type()
)
lsHistoryStatsPriority2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority2Octets.setStatus("mandatory")
_LsHistoryStatsPriority3Pkts_Type = Counter32
_LsHistoryStatsPriority3Pkts_Object = MibTableColumn
lsHistoryStatsPriority3Pkts = _LsHistoryStatsPriority3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 19),
    _LsHistoryStatsPriority3Pkts_Type()
)
lsHistoryStatsPriority3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority3Pkts.setStatus("mandatory")
_LsHistoryStatsPriority3Octets_Type = Counter32
_LsHistoryStatsPriority3Octets_Object = MibTableColumn
lsHistoryStatsPriority3Octets = _LsHistoryStatsPriority3Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 20),
    _LsHistoryStatsPriority3Octets_Type()
)
lsHistoryStatsPriority3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority3Octets.setStatus("mandatory")
_LsHistoryStatsPriority4Pkts_Type = Counter32
_LsHistoryStatsPriority4Pkts_Object = MibTableColumn
lsHistoryStatsPriority4Pkts = _LsHistoryStatsPriority4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 21),
    _LsHistoryStatsPriority4Pkts_Type()
)
lsHistoryStatsPriority4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority4Pkts.setStatus("mandatory")
_LsHistoryStatsPriority4Octets_Type = Counter32
_LsHistoryStatsPriority4Octets_Object = MibTableColumn
lsHistoryStatsPriority4Octets = _LsHistoryStatsPriority4Octets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 22),
    _LsHistoryStatsPriority4Octets_Type()
)
lsHistoryStatsPriority4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryStatsPriority4Octets.setStatus("mandatory")


class _LsHistoryBusUtilization_Type(Integer32):
    """Custom type lsHistoryBusUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LsHistoryBusUtilization_Type.__name__ = "Integer32"
_LsHistoryBusUtilization_Object = MibTableColumn
lsHistoryBusUtilization = _LsHistoryBusUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 3, 11, 1, 23),
    _LsHistoryBusUtilization_Type()
)
lsHistoryBusUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsHistoryBusUtilization.setStatus("mandatory")
_Lst_ObjectIdentity = ObjectIdentity
lst = _Lst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 4)
)
_LstIntPort_ObjectIdentity = ObjectIdentity
lstIntPort = _LstIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1)
)
_LstIntPortTable_Object = MibTable
lstIntPortTable = _LstIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lstIntPortTable.setStatus("mandatory")
_LstIntPortEntry_Object = MibTableRow
lstIntPortEntry = _LstIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1)
)
lstIntPortEntry.setIndexNames(
    (0, "APPLIC-MIB", "lstIntPortGroupId"),
    (0, "APPLIC-MIB", "lstIntPortId"),
)
if mibBuilder.loadTexts:
    lstIntPortEntry.setStatus("mandatory")


class _LstIntPortGroupId_Type(Integer32):
    """Custom type lstIntPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LstIntPortGroupId_Type.__name__ = "Integer32"
_LstIntPortGroupId_Object = MibTableColumn
lstIntPortGroupId = _LstIntPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 1),
    _LstIntPortGroupId_Type()
)
lstIntPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortGroupId.setStatus("mandatory")


class _LstIntPortId_Type(Integer32):
    """Custom type lstIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LstIntPortId_Type.__name__ = "Integer32"
_LstIntPortId_Object = MibTableColumn
lstIntPortId = _LstIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 2),
    _LstIntPortId_Type()
)
lstIntPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortId.setStatus("mandatory")


class _LstIntPortSidebandMode_Type(Integer32):
    """Custom type lstIntPortSidebandMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LstIntPortSidebandMode_Type.__name__ = "Integer32"
_LstIntPortSidebandMode_Object = MibTableColumn
lstIntPortSidebandMode = _LstIntPortSidebandMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 3),
    _LstIntPortSidebandMode_Type()
)
lstIntPortSidebandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortSidebandMode.setStatus("mandatory")
_LstIntPortTotalOctets_Type = Counter32
_LstIntPortTotalOctets_Object = MibTableColumn
lstIntPortTotalOctets = _LstIntPortTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 4),
    _LstIntPortTotalOctets_Type()
)
lstIntPortTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortTotalOctets.setStatus("mandatory")


class _LstIntPortTotalTraffic_Type(Integer32):
    """Custom type lstIntPortTotalTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LstIntPortTotalTraffic_Type.__name__ = "Integer32"
_LstIntPortTotalTraffic_Object = MibTableColumn
lstIntPortTotalTraffic = _LstIntPortTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 5),
    _LstIntPortTotalTraffic_Type()
)
lstIntPortTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortTotalTraffic.setStatus("mandatory")
_LstIntPortLocalOctets_Type = Counter32
_LstIntPortLocalOctets_Object = MibTableColumn
lstIntPortLocalOctets = _LstIntPortLocalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 6),
    _LstIntPortLocalOctets_Type()
)
lstIntPortLocalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortLocalOctets.setStatus("mandatory")


class _LstIntPortLocalTraffic_Type(Integer32):
    """Custom type lstIntPortLocalTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LstIntPortLocalTraffic_Type.__name__ = "Integer32"
_LstIntPortLocalTraffic_Object = MibTableColumn
lstIntPortLocalTraffic = _LstIntPortLocalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 7),
    _LstIntPortLocalTraffic_Type()
)
lstIntPortLocalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortLocalTraffic.setStatus("mandatory")
_LstIntPortInOctets_Type = Counter32
_LstIntPortInOctets_Object = MibTableColumn
lstIntPortInOctets = _LstIntPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 8),
    _LstIntPortInOctets_Type()
)
lstIntPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortInOctets.setStatus("mandatory")


class _LstIntPortInTraffic_Type(Integer32):
    """Custom type lstIntPortInTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LstIntPortInTraffic_Type.__name__ = "Integer32"
_LstIntPortInTraffic_Object = MibTableColumn
lstIntPortInTraffic = _LstIntPortInTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 9),
    _LstIntPortInTraffic_Type()
)
lstIntPortInTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortInTraffic.setStatus("mandatory")
_LstIntPortOutOctets_Type = Counter32
_LstIntPortOutOctets_Object = MibTableColumn
lstIntPortOutOctets = _LstIntPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 10),
    _LstIntPortOutOctets_Type()
)
lstIntPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortOutOctets.setStatus("mandatory")


class _LstIntPortOutTraffic_Type(Integer32):
    """Custom type lstIntPortOutTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LstIntPortOutTraffic_Type.__name__ = "Integer32"
_LstIntPortOutTraffic_Object = MibTableColumn
lstIntPortOutTraffic = _LstIntPortOutTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 11),
    _LstIntPortOutTraffic_Type()
)
lstIntPortOutTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortOutTraffic.setStatus("mandatory")
_LstIntPortTotalFrames_Type = Counter32
_LstIntPortTotalFrames_Object = MibTableColumn
lstIntPortTotalFrames = _LstIntPortTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 12),
    _LstIntPortTotalFrames_Type()
)
lstIntPortTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortTotalFrames.setStatus("mandatory")
_LstIntPortLostFrames_Type = Counter32
_LstIntPortLostFrames_Object = MibTableColumn
lstIntPortLostFrames = _LstIntPortLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 13),
    _LstIntPortLostFrames_Type()
)
lstIntPortLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortLostFrames.setStatus("mandatory")
_LstIntPortClaimFrames_Type = Counter32
_LstIntPortClaimFrames_Object = MibTableColumn
lstIntPortClaimFrames = _LstIntPortClaimFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 16),
    _LstIntPortClaimFrames_Type()
)
lstIntPortClaimFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortClaimFrames.setStatus("mandatory")
_LstIntPortPurgeFrames_Type = Counter32
_LstIntPortPurgeFrames_Object = MibTableColumn
lstIntPortPurgeFrames = _LstIntPortPurgeFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 17),
    _LstIntPortPurgeFrames_Type()
)
lstIntPortPurgeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortPurgeFrames.setStatus("mandatory")


class _LstIntPortNormallyCloseOpen_Type(Integer32):
    """Custom type lstIntPortNormallyCloseOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normallyClose", 1),
          ("normallyOpen", 2),
          ("notSupported", 255))
    )


_LstIntPortNormallyCloseOpen_Type.__name__ = "Integer32"
_LstIntPortNormallyCloseOpen_Object = MibTableColumn
lstIntPortNormallyCloseOpen = _LstIntPortNormallyCloseOpen_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 18),
    _LstIntPortNormallyCloseOpen_Type()
)
lstIntPortNormallyCloseOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortNormallyCloseOpen.setStatus("mandatory")


class _LstIntPortSlicingEnable_Type(Integer32):
    """Custom type lstIntPortSlicingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LstIntPortSlicingEnable_Type.__name__ = "Integer32"
_LstIntPortSlicingEnable_Object = MibTableColumn
lstIntPortSlicingEnable = _LstIntPortSlicingEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 19),
    _LstIntPortSlicingEnable_Type()
)
lstIntPortSlicingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortSlicingEnable.setStatus("mandatory")
_LstIntPortSliceLength_Type = Integer32
_LstIntPortSliceLength_Object = MibTableColumn
lstIntPortSliceLength = _LstIntPortSliceLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 20),
    _LstIntPortSliceLength_Type()
)
lstIntPortSliceLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortSliceLength.setStatus("mandatory")


class _LstIntPortUNAddr_Type(OctetString):
    """Custom type lstIntPortUNAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LstIntPortUNAddr_Type.__name__ = "OctetString"
_LstIntPortUNAddr_Object = MibTableColumn
lstIntPortUNAddr = _LstIntPortUNAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 21),
    _LstIntPortUNAddr_Type()
)
lstIntPortUNAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortUNAddr.setStatus("mandatory")


class _LstIntPortMACAddress_Type(OctetString):
    """Custom type lstIntPortMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LstIntPortMACAddress_Type.__name__ = "OctetString"
_LstIntPortMACAddress_Object = MibTableColumn
lstIntPortMACAddress = _LstIntPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 22),
    _LstIntPortMACAddress_Type()
)
lstIntPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIntPortMACAddress.setStatus("mandatory")


class _LstIntPortSMPTransmitEnable_Type(Integer32):
    """Custom type lstIntPortSMPTransmitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LstIntPortSMPTransmitEnable_Type.__name__ = "Integer32"
_LstIntPortSMPTransmitEnable_Object = MibTableColumn
lstIntPortSMPTransmitEnable = _LstIntPortSMPTransmitEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 23),
    _LstIntPortSMPTransmitEnable_Type()
)
lstIntPortSMPTransmitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortSMPTransmitEnable.setStatus("mandatory")


class _LstIntPortIPGLength_Type(Integer32):
    """Custom type lstIntPortIPGLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LstIntPortIPGLength_Type.__name__ = "Integer32"
_LstIntPortIPGLength_Object = MibTableColumn
lstIntPortIPGLength = _LstIntPortIPGLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 24),
    _LstIntPortIPGLength_Type()
)
lstIntPortIPGLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortIPGLength.setStatus("mandatory")


class _LstIntPortBPDummyWindow_Type(Integer32):
    """Custom type lstIntPortBPDummyWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LstIntPortBPDummyWindow_Type.__name__ = "Integer32"
_LstIntPortBPDummyWindow_Object = MibTableColumn
lstIntPortBPDummyWindow = _LstIntPortBPDummyWindow_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 25),
    _LstIntPortBPDummyWindow_Type()
)
lstIntPortBPDummyWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortBPDummyWindow.setStatus("mandatory")
_LstIntPortBPTokenWindow_Type = Integer32
_LstIntPortBPTokenWindow_Object = MibTableColumn
lstIntPortBPTokenWindow = _LstIntPortBPTokenWindow_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 26),
    _LstIntPortBPTokenWindow_Type()
)
lstIntPortBPTokenWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortBPTokenWindow.setStatus("mandatory")
_LstIntPortTransmitWindow_Type = Integer32
_LstIntPortTransmitWindow_Object = MibTableColumn
lstIntPortTransmitWindow = _LstIntPortTransmitWindow_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 27),
    _LstIntPortTransmitWindow_Type()
)
lstIntPortTransmitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortTransmitWindow.setStatus("mandatory")


class _LstIntPortBlockingPriority_Type(Integer32):
    """Custom type lstIntPortBlockingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LstIntPortBlockingPriority_Type.__name__ = "Integer32"
_LstIntPortBlockingPriority_Object = MibTableColumn
lstIntPortBlockingPriority = _LstIntPortBlockingPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 28),
    _LstIntPortBlockingPriority_Type()
)
lstIntPortBlockingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortBlockingPriority.setStatus("mandatory")


class _LstIntPortNormalPriority_Type(Integer32):
    """Custom type lstIntPortNormalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LstIntPortNormalPriority_Type.__name__ = "Integer32"
_LstIntPortNormalPriority_Object = MibTableColumn
lstIntPortNormalPriority = _LstIntPortNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 29),
    _LstIntPortNormalPriority_Type()
)
lstIntPortNormalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortNormalPriority.setStatus("mandatory")


class _LstIntPortDummyMV_Type(Integer32):
    """Custom type lstIntPortDummyMV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LstIntPortDummyMV_Type.__name__ = "Integer32"
_LstIntPortDummyMV_Object = MibTableColumn
lstIntPortDummyMV = _LstIntPortDummyMV_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 30),
    _LstIntPortDummyMV_Type()
)
lstIntPortDummyMV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortDummyMV.setStatus("mandatory")
_LstIntPortTxConsecutiveBusiesThresh_Type = Integer32
_LstIntPortTxConsecutiveBusiesThresh_Object = MibTableColumn
lstIntPortTxConsecutiveBusiesThresh = _LstIntPortTxConsecutiveBusiesThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 31),
    _LstIntPortTxConsecutiveBusiesThresh_Type()
)
lstIntPortTxConsecutiveBusiesThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortTxConsecutiveBusiesThresh.setStatus("mandatory")
_LstIntPortTxBufFullThresh_Type = Integer32
_LstIntPortTxBufFullThresh_Object = MibTableColumn
lstIntPortTxBufFullThresh = _LstIntPortTxBufFullThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 32),
    _LstIntPortTxBufFullThresh_Type()
)
lstIntPortTxBufFullThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortTxBufFullThresh.setStatus("mandatory")
_LstIntPortRxEmpty0_Type = Integer32
_LstIntPortRxEmpty0_Object = MibTableColumn
lstIntPortRxEmpty0 = _LstIntPortRxEmpty0_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 33),
    _LstIntPortRxEmpty0_Type()
)
lstIntPortRxEmpty0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortRxEmpty0.setStatus("mandatory")
_LstIntPortRxEmpty1_Type = Integer32
_LstIntPortRxEmpty1_Object = MibTableColumn
lstIntPortRxEmpty1 = _LstIntPortRxEmpty1_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 34),
    _LstIntPortRxEmpty1_Type()
)
lstIntPortRxEmpty1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortRxEmpty1.setStatus("mandatory")
_LstIntPortRxEmpty2_Type = Integer32
_LstIntPortRxEmpty2_Object = MibTableColumn
lstIntPortRxEmpty2 = _LstIntPortRxEmpty2_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 35),
    _LstIntPortRxEmpty2_Type()
)
lstIntPortRxEmpty2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortRxEmpty2.setStatus("mandatory")
_LstIntPortRxFull_Type = Integer32
_LstIntPortRxFull_Object = MibTableColumn
lstIntPortRxFull = _LstIntPortRxFull_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 36),
    _LstIntPortRxFull_Type()
)
lstIntPortRxFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortRxFull.setStatus("mandatory")


class _LstIntPortBPEnable_Type(Integer32):
    """Custom type lstIntPortBPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_LstIntPortBPEnable_Type.__name__ = "Integer32"
_LstIntPortBPEnable_Object = MibTableColumn
lstIntPortBPEnable = _LstIntPortBPEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 37),
    _LstIntPortBPEnable_Type()
)
lstIntPortBPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortBPEnable.setStatus("mandatory")


class _LstIntPortRouteSideband_Type(Integer32):
    """Custom type lstIntPortRouteSideband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LstIntPortRouteSideband_Type.__name__ = "Integer32"
_LstIntPortRouteSideband_Object = MibTableColumn
lstIntPortRouteSideband = _LstIntPortRouteSideband_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 4, 1, 1, 1, 38),
    _LstIntPortRouteSideband_Type()
)
lstIntPortRouteSideband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lstIntPortRouteSideband.setStatus("mandatory")
_LseWANTable_Object = MibTable
lseWANTable = _LseWANTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 5)
)
if mibBuilder.loadTexts:
    lseWANTable.setStatus("mandatory")
_LseWANEntry_Object = MibTableRow
lseWANEntry = _LseWANEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 5, 1)
)
lseWANEntry.setIndexNames(
    (0, "APPLIC-MIB", "lseWANGroupId"),
    (0, "APPLIC-MIB", "lseWANPortId"),
)
if mibBuilder.loadTexts:
    lseWANEntry.setStatus("mandatory")
_LseWANGroupId_Type = Integer32
_LseWANGroupId_Object = MibTableColumn
lseWANGroupId = _LseWANGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 5, 1, 1),
    _LseWANGroupId_Type()
)
lseWANGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseWANGroupId.setStatus("mandatory")
_LseWANPortId_Type = Integer32
_LseWANPortId_Object = MibTableColumn
lseWANPortId = _LseWANPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 5, 1, 2),
    _LseWANPortId_Type()
)
lseWANPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseWANPortId.setStatus("mandatory")


class _LseWANConnection_Type(Integer32):
    """Custom type lseWANConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_LseWANConnection_Type.__name__ = "Integer32"
_LseWANConnection_Object = MibTableColumn
lseWANConnection = _LseWANConnection_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 5, 1, 3),
    _LseWANConnection_Type()
)
lseWANConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseWANConnection.setStatus("mandatory")
_LsVNChange_ObjectIdentity = ObjectIdentity
lsVNChange = _LsVNChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 6)
)


class _LsVNChangeMACAddress_Type(OctetString):
    """Custom type lsVNChangeMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LsVNChangeMACAddress_Type.__name__ = "OctetString"
_LsVNChangeMACAddress_Object = MibScalar
lsVNChangeMACAddress = _LsVNChangeMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 6, 1),
    _LsVNChangeMACAddress_Type()
)
lsVNChangeMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsVNChangeMACAddress.setStatus("mandatory")


class _LsVNChangeDetected_Type(Integer32):
    """Custom type lsVNChangeDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_LsVNChangeDetected_Type.__name__ = "Integer32"
_LsVNChangeDetected_Object = MibScalar
lsVNChangeDetected = _LsVNChangeDetected_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 6, 2),
    _LsVNChangeDetected_Type()
)
lsVNChangeDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsVNChangeDetected.setStatus("mandatory")


class _LsVNChangeExpected_Type(Integer32):
    """Custom type lsVNChangeExpected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_LsVNChangeExpected_Type.__name__ = "Integer32"
_LsVNChangeExpected_Object = MibScalar
lsVNChangeExpected = _LsVNChangeExpected_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 6, 3),
    _LsVNChangeExpected_Type()
)
lsVNChangeExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsVNChangeExpected.setStatus("mandatory")
_LsVNChangeGroup_Type = Integer32
_LsVNChangeGroup_Object = MibScalar
lsVNChangeGroup = _LsVNChangeGroup_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 6, 4),
    _LsVNChangeGroup_Type()
)
lsVNChangeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsVNChangeGroup.setStatus("mandatory")
_LsVNChangePort_Type = Integer32
_LsVNChangePort_Object = MibScalar
lsVNChangePort = _LsVNChangePort_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 6, 5),
    _LsVNChangePort_Type()
)
lsVNChangePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsVNChangePort.setStatus("mandatory")
_VnsPacket_ObjectIdentity = ObjectIdentity
vnsPacket = _VnsPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 7)
)
_VnsPacketTable_Object = MibTable
vnsPacketTable = _VnsPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1)
)
if mibBuilder.loadTexts:
    vnsPacketTable.setStatus("mandatory")
_VnsPacketEntry_Object = MibTableRow
vnsPacketEntry = _VnsPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1)
)
vnsPacketEntry.setIndexNames(
    (0, "APPLIC-MIB", "vnsPacketMACAddress"),
)
if mibBuilder.loadTexts:
    vnsPacketEntry.setStatus("mandatory")


class _VnsPacketMACAddress_Type(OctetString):
    """Custom type vnsPacketMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VnsPacketMACAddress_Type.__name__ = "OctetString"
_VnsPacketMACAddress_Object = MibTableColumn
vnsPacketMACAddress = _VnsPacketMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 1),
    _VnsPacketMACAddress_Type()
)
vnsPacketMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketMACAddress.setStatus("mandatory")


class _VnsPacketProtocolTypeMask_Type(OctetString):
    """Custom type vnsPacketProtocolTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VnsPacketProtocolTypeMask_Type.__name__ = "OctetString"
_VnsPacketProtocolTypeMask_Object = MibTableColumn
vnsPacketProtocolTypeMask = _VnsPacketProtocolTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 2),
    _VnsPacketProtocolTypeMask_Type()
)
vnsPacketProtocolTypeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketProtocolTypeMask.setStatus("mandatory")
_VnsPacketIPAddress_Type = IpAddress
_VnsPacketIPAddress_Object = MibTableColumn
vnsPacketIPAddress = _VnsPacketIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 3),
    _VnsPacketIPAddress_Type()
)
vnsPacketIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketIPAddress.setStatus("mandatory")
_VnsPacketIPNetMask_Type = IpAddress
_VnsPacketIPNetMask_Object = MibTableColumn
vnsPacketIPNetMask = _VnsPacketIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 4),
    _VnsPacketIPNetMask_Type()
)
vnsPacketIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketIPNetMask.setStatus("mandatory")


class _VnsPacketIPXnetwork_Type(OctetString):
    """Custom type vnsPacketIPXnetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VnsPacketIPXnetwork_Type.__name__ = "OctetString"
_VnsPacketIPXnetwork_Object = MibTableColumn
vnsPacketIPXnetwork = _VnsPacketIPXnetwork_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 5),
    _VnsPacketIPXnetwork_Type()
)
vnsPacketIPXnetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketIPXnetwork.setStatus("mandatory")


class _VnsPacketStationType_Type(Integer32):
    """Custom type vnsPacketStationType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("notSupported", 255),
          ("server", 3),
          ("unknown", 1))
    )


_VnsPacketStationType_Type.__name__ = "Integer32"
_VnsPacketStationType_Object = MibTableColumn
vnsPacketStationType = _VnsPacketStationType_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 6),
    _VnsPacketStationType_Type()
)
vnsPacketStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketStationType.setStatus("mandatory")


class _VnsPacketPortGroupId_Type(Integer32):
    """Custom type vnsPacketPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VnsPacketPortGroupId_Type.__name__ = "Integer32"
_VnsPacketPortGroupId_Object = MibTableColumn
vnsPacketPortGroupId = _VnsPacketPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 7),
    _VnsPacketPortGroupId_Type()
)
vnsPacketPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketPortGroupId.setStatus("mandatory")


class _VnsPacketPortId_Type(Integer32):
    """Custom type vnsPacketPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VnsPacketPortId_Type.__name__ = "Integer32"
_VnsPacketPortId_Object = MibTableColumn
vnsPacketPortId = _VnsPacketPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 8),
    _VnsPacketPortId_Type()
)
vnsPacketPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketPortId.setStatus("mandatory")


class _VnsPacketBackbonePort_Type(Integer32):
    """Custom type vnsPacketBackbonePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backbone", 2),
          ("noBackbone", 3),
          ("notSupported", 255),
          ("unknown", 1))
    )


_VnsPacketBackbonePort_Type.__name__ = "Integer32"
_VnsPacketBackbonePort_Object = MibTableColumn
vnsPacketBackbonePort = _VnsPacketBackbonePort_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 9),
    _VnsPacketBackbonePort_Type()
)
vnsPacketBackbonePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketBackbonePort.setStatus("mandatory")
_VnsPacketExpectedVLAN_Type = Integer32
_VnsPacketExpectedVLAN_Object = MibTableColumn
vnsPacketExpectedVLAN = _VnsPacketExpectedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 10),
    _VnsPacketExpectedVLAN_Type()
)
vnsPacketExpectedVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketExpectedVLAN.setStatus("mandatory")
_VnsPacketDetectedVLAN_Type = Integer32
_VnsPacketDetectedVLAN_Object = MibTableColumn
vnsPacketDetectedVLAN = _VnsPacketDetectedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 11),
    _VnsPacketDetectedVLAN_Type()
)
vnsPacketDetectedVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketDetectedVLAN.setStatus("mandatory")
_VnsPacketBoxAgentIP_Type = IpAddress
_VnsPacketBoxAgentIP_Object = MibTableColumn
vnsPacketBoxAgentIP = _VnsPacketBoxAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 12),
    _VnsPacketBoxAgentIP_Type()
)
vnsPacketBoxAgentIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketBoxAgentIP.setStatus("mandatory")
_LntTopology_ObjectIdentity = ObjectIdentity
lntTopology = _LntTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 23)
)


class _TopDiscovery_Type(Integer32):
    """Custom type topDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("macFind", 3),
          ("notSupported", 255),
          ("swBackboneMsgMonitor", 4),
          ("topoMessages", 2))
    )


_TopDiscovery_Type.__name__ = "Integer32"
_TopDiscovery_Object = MibScalar
topDiscovery = _TopDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 1),
    _TopDiscovery_Type()
)
topDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topDiscovery.setStatus("mandatory")


class _TopDiscoveryTimeOut_Type(Integer32):
    """Custom type topDiscoveryTimeOut based on Integer32"""
    defaultValue = 3


_TopDiscoveryTimeOut_Object = MibScalar
topDiscoveryTimeOut = _TopDiscoveryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 2),
    _TopDiscoveryTimeOut_Type()
)
topDiscoveryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topDiscoveryTimeOut.setStatus("mandatory")
_EthTop_ObjectIdentity = ObjectIdentity
ethTop = _EthTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 23, 3)
)


class _EthTopDiscoveryTx_Type(Integer32):
    """Custom type ethTopDiscoveryTx based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("txAckMsg", 4),
          ("txBridgeMsg", 3),
          ("txInterhubMsg", 2))
    )


_EthTopDiscoveryTx_Type.__name__ = "Integer32"
_EthTopDiscoveryTx_Object = MibScalar
ethTopDiscoveryTx = _EthTopDiscoveryTx_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 1),
    _EthTopDiscoveryTx_Type()
)
ethTopDiscoveryTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTopDiscoveryTx.setStatus("mandatory")


class _EthTopClearMessageResult_Type(Integer32):
    """Custom type ethTopClearMessageResult based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("idle", 1))
    )


_EthTopClearMessageResult_Type.__name__ = "Integer32"
_EthTopClearMessageResult_Object = MibScalar
ethTopClearMessageResult = _EthTopClearMessageResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 2),
    _EthTopClearMessageResult_Type()
)
ethTopClearMessageResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTopClearMessageResult.setStatus("mandatory")
_EthTopNumOfMessageResults_Type = Integer32
_EthTopNumOfMessageResults_Object = MibScalar
ethTopNumOfMessageResults = _EthTopNumOfMessageResults_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 3),
    _EthTopNumOfMessageResults_Type()
)
ethTopNumOfMessageResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTopNumOfMessageResults.setStatus("mandatory")
_EthTopMessageResultTable_Object = MibTable
ethTopMessageResultTable = _EthTopMessageResultTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 4)
)
if mibBuilder.loadTexts:
    ethTopMessageResultTable.setStatus("mandatory")
_EthTopMessageResultEntry_Object = MibTableRow
ethTopMessageResultEntry = _EthTopMessageResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 4, 1)
)
ethTopMessageResultEntry.setIndexNames(
    (0, "APPLIC-MIB", "ethTopMessageResultId"),
)
if mibBuilder.loadTexts:
    ethTopMessageResultEntry.setStatus("mandatory")
_EthTopMessageResultId_Type = Integer32
_EthTopMessageResultId_Object = MibTableColumn
ethTopMessageResultId = _EthTopMessageResultId_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 4, 1, 1),
    _EthTopMessageResultId_Type()
)
ethTopMessageResultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTopMessageResultId.setStatus("mandatory")


class _EthTopMessageResult_Type(OctetString):
    """Custom type ethTopMessageResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 440),
    )


_EthTopMessageResult_Type.__name__ = "OctetString"
_EthTopMessageResult_Object = MibTableColumn
ethTopMessageResult = _EthTopMessageResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 4, 1, 2),
    _EthTopMessageResult_Type()
)
ethTopMessageResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTopMessageResult.setStatus("mandatory")


class _EthTopMACFindList_Type(OctetString):
    """Custom type ethTopMACFindList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_EthTopMACFindList_Type.__name__ = "OctetString"
_EthTopMACFindList_Object = MibScalar
ethTopMACFindList = _EthTopMACFindList_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 5),
    _EthTopMACFindList_Type()
)
ethTopMACFindList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTopMACFindList.setStatus("mandatory")
_EthTopMACFindResultTable_Object = MibTable
ethTopMACFindResultTable = _EthTopMACFindResultTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 6)
)
if mibBuilder.loadTexts:
    ethTopMACFindResultTable.setStatus("mandatory")
_EthTopMACFindResultEntry_Object = MibTableRow
ethTopMACFindResultEntry = _EthTopMACFindResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 6, 1)
)
ethTopMACFindResultEntry.setIndexNames(
    (0, "APPLIC-MIB", "ethTopMACFindBus"),
)
if mibBuilder.loadTexts:
    ethTopMACFindResultEntry.setStatus("mandatory")
_EthTopMACFindBus_Type = Integer32
_EthTopMACFindBus_Object = MibTableColumn
ethTopMACFindBus = _EthTopMACFindBus_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 6, 1, 1),
    _EthTopMACFindBus_Type()
)
ethTopMACFindBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTopMACFindBus.setStatus("mandatory")


class _EthTopMACFindResult_Type(OctetString):
    """Custom type ethTopMACFindResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_EthTopMACFindResult_Type.__name__ = "OctetString"
_EthTopMACFindResult_Object = MibTableColumn
ethTopMACFindResult = _EthTopMACFindResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 6, 1, 2),
    _EthTopMACFindResult_Type()
)
ethTopMACFindResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTopMACFindResult.setStatus("mandatory")
_EthTopLSATable_Object = MibTable
ethTopLSATable = _EthTopLSATable_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 7)
)
if mibBuilder.loadTexts:
    ethTopLSATable.setStatus("mandatory")
_EthTopLSAEntry_Object = MibTableRow
ethTopLSAEntry = _EthTopLSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 7, 1)
)
ethTopLSAEntry.setIndexNames(
    (0, "APPLIC-MIB", "ethTopLSAId"),
)
if mibBuilder.loadTexts:
    ethTopLSAEntry.setStatus("mandatory")
_EthTopLSAId_Type = Integer32
_EthTopLSAId_Object = MibTableColumn
ethTopLSAId = _EthTopLSAId_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 7, 1, 1),
    _EthTopLSAId_Type()
)
ethTopLSAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTopLSAId.setStatus("mandatory")


class _EthTopLSA_Type(OctetString):
    """Custom type ethTopLSA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(384, 384),
    )


_EthTopLSA_Type.__name__ = "OctetString"
_EthTopLSA_Object = MibTableColumn
ethTopLSA = _EthTopLSA_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 7, 1, 2),
    _EthTopLSA_Type()
)
ethTopLSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTopLSA.setStatus("mandatory")
_EthTopAddressTable_Object = MibTable
ethTopAddressTable = _EthTopAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 8)
)
if mibBuilder.loadTexts:
    ethTopAddressTable.setStatus("mandatory")
_EthTopAddressEntry_Object = MibTableRow
ethTopAddressEntry = _EthTopAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 8, 1)
)
ethTopAddressEntry.setIndexNames(
    (0, "APPLIC-MIB", "ethTopBus"),
)
if mibBuilder.loadTexts:
    ethTopAddressEntry.setStatus("mandatory")
_EthTopBus_Type = Integer32
_EthTopBus_Object = MibTableColumn
ethTopBus = _EthTopBus_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 8, 1, 1),
    _EthTopBus_Type()
)
ethTopBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTopBus.setStatus("mandatory")


class _EthTopAddress_Type(OctetString):
    """Custom type ethTopAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EthTopAddress_Type.__name__ = "OctetString"
_EthTopAddress_Object = MibTableColumn
ethTopAddress = _EthTopAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 8, 1, 2),
    _EthTopAddress_Type()
)
ethTopAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTopAddress.setStatus("mandatory")


class _EthTopHSBMonitor_Type(Integer32):
    """Custom type ethTopHSBMonitor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("notSupported", 255),
          ("startMonitor", 2))
    )


_EthTopHSBMonitor_Type.__name__ = "Integer32"
_EthTopHSBMonitor_Object = MibScalar
ethTopHSBMonitor = _EthTopHSBMonitor_Object(
    (1, 3, 6, 1, 4, 1, 81, 23, 3, 9),
    _EthTopHSBMonitor_Type()
)
ethTopHSBMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTopHSBMonitor.setStatus("mandatory")
_Smon_ObjectIdentity = ObjectIdentity
smon = _Smon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30)
)
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 1)
)
_AlarmMonitorStatusTable_Object = MibTable
alarmMonitorStatusTable = _AlarmMonitorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 1, 1)
)
if mibBuilder.loadTexts:
    alarmMonitorStatusTable.setStatus("mandatory")
_AlarmMonitorStatusEntry_Object = MibTableRow
alarmMonitorStatusEntry = _AlarmMonitorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 1, 1, 1)
)
alarmMonitorStatusEntry.setIndexNames(
    (0, "APPLIC-MIB", "alarmMonitorStatusIndex"),
)
if mibBuilder.loadTexts:
    alarmMonitorStatusEntry.setStatus("mandatory")


class _AlarmMonitorStatusIndex_Type(Integer32):
    """Custom type alarmMonitorStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlarmMonitorStatusIndex_Type.__name__ = "Integer32"
_AlarmMonitorStatusIndex_Object = MibTableColumn
alarmMonitorStatusIndex = _AlarmMonitorStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 1, 1, 1, 1),
    _AlarmMonitorStatusIndex_Type()
)
alarmMonitorStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMonitorStatusIndex.setStatus("mandatory")


class _AlarmMonitorStatus_Type(Integer32):
    """Custom type alarmMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmState", 2),
          ("ok", 1))
    )


_AlarmMonitorStatus_Type.__name__ = "Integer32"
_AlarmMonitorStatus_Object = MibTableColumn
alarmMonitorStatus = _AlarmMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 1, 1, 1, 2),
    _AlarmMonitorStatus_Type()
)
alarmMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMonitorStatus.setStatus("mandatory")


class _AlarmUtilitiesCommand_Type(Integer32):
    """Custom type alarmUtilitiesCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 2),
          ("idle", 1),
          ("notSupported", 255))
    )


_AlarmUtilitiesCommand_Type.__name__ = "Integer32"
_AlarmUtilitiesCommand_Object = MibScalar
alarmUtilitiesCommand = _AlarmUtilitiesCommand_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 1, 2),
    _AlarmUtilitiesCommand_Type()
)
alarmUtilitiesCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmUtilitiesCommand.setStatus("mandatory")
_PortHistory_ObjectIdentity = ObjectIdentity
portHistory = _PortHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 3)
)
_PortHistoryExtendedControlTable_Object = MibTable
portHistoryExtendedControlTable = _PortHistoryExtendedControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 1)
)
if mibBuilder.loadTexts:
    portHistoryExtendedControlTable.setStatus("mandatory")
_PortHistoryExtendedControlEntry_Object = MibTableRow
portHistoryExtendedControlEntry = _PortHistoryExtendedControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 1, 1)
)
portHistoryExtendedControlEntry.setIndexNames(
    (0, "RMON-MIB", "historyControlIndex"),
)
if mibBuilder.loadTexts:
    portHistoryExtendedControlEntry.setStatus("mandatory")
_PortHistoryExtendedControlCreateTime_Type = TimeTicks
_PortHistoryExtendedControlCreateTime_Object = MibTableColumn
portHistoryExtendedControlCreateTime = _PortHistoryExtendedControlCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 1, 1, 1),
    _PortHistoryExtendedControlCreateTime_Type()
)
portHistoryExtendedControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistoryExtendedControlCreateTime.setStatus("mandatory")
_PortHistoryExtendedControlLastBucketIndex_Type = Integer32
_PortHistoryExtendedControlLastBucketIndex_Object = MibTableColumn
portHistoryExtendedControlLastBucketIndex = _PortHistoryExtendedControlLastBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 1, 1, 2),
    _PortHistoryExtendedControlLastBucketIndex_Type()
)
portHistoryExtendedControlLastBucketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistoryExtendedControlLastBucketIndex.setStatus("mandatory")


class _PortHistoryExtendedControlNumberOfBuckets_Type(Integer32):
    """Custom type portHistoryExtendedControlNumberOfBuckets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortHistoryExtendedControlNumberOfBuckets_Type.__name__ = "Integer32"
_PortHistoryExtendedControlNumberOfBuckets_Object = MibTableColumn
portHistoryExtendedControlNumberOfBuckets = _PortHistoryExtendedControlNumberOfBuckets_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 1, 1, 3),
    _PortHistoryExtendedControlNumberOfBuckets_Type()
)
portHistoryExtendedControlNumberOfBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistoryExtendedControlNumberOfBuckets.setStatus("mandatory")
_PortHistoryExtendedControlName_Type = DisplayString
_PortHistoryExtendedControlName_Object = MibTableColumn
portHistoryExtendedControlName = _PortHistoryExtendedControlName_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 1, 1, 4),
    _PortHistoryExtendedControlName_Type()
)
portHistoryExtendedControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portHistoryExtendedControlName.setStatus("mandatory")
_LsPortHistoryTable_Object = MibTable
lsPortHistoryTable = _LsPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2)
)
if mibBuilder.loadTexts:
    lsPortHistoryTable.setStatus("mandatory")
_LsPortHistoryEntry_Object = MibTableRow
lsPortHistoryEntry = _LsPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1)
)
lsPortHistoryEntry.setIndexNames(
    (0, "APPLIC-MIB", "lsPortHistoryIndex"),
    (0, "APPLIC-MIB", "lsPortHistorySampleIndex"),
    (0, "APPLIC-MIB", "lsPortNumber"),
)
if mibBuilder.loadTexts:
    lsPortHistoryEntry.setStatus("mandatory")


class _LsPortHistoryIndex_Type(Integer32):
    """Custom type lsPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LsPortHistoryIndex_Type.__name__ = "Integer32"
_LsPortHistoryIndex_Object = MibTableColumn
lsPortHistoryIndex = _LsPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1, 1),
    _LsPortHistoryIndex_Type()
)
lsPortHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortHistoryIndex.setStatus("mandatory")


class _LsPortHistorySampleIndex_Type(Integer32):
    """Custom type lsPortHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LsPortHistorySampleIndex_Type.__name__ = "Integer32"
_LsPortHistorySampleIndex_Object = MibTableColumn
lsPortHistorySampleIndex = _LsPortHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1, 2),
    _LsPortHistorySampleIndex_Type()
)
lsPortHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortHistorySampleIndex.setStatus("mandatory")
_LsPortHistoryIntervalTime_Type = TimeTicks
_LsPortHistoryIntervalTime_Object = MibTableColumn
lsPortHistoryIntervalTime = _LsPortHistoryIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1, 3),
    _LsPortHistoryIntervalTime_Type()
)
lsPortHistoryIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortHistoryIntervalTime.setStatus("mandatory")
_LsPortHistoryBoxConfiguration_Type = OctetString
_LsPortHistoryBoxConfiguration_Object = MibTableColumn
lsPortHistoryBoxConfiguration = _LsPortHistoryBoxConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1, 4),
    _LsPortHistoryBoxConfiguration_Type()
)
lsPortHistoryBoxConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortHistoryBoxConfiguration.setStatus("mandatory")
_LsPortHistoryPkts_Type = Counter32
_LsPortHistoryPkts_Object = MibTableColumn
lsPortHistoryPkts = _LsPortHistoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1, 5),
    _LsPortHistoryPkts_Type()
)
lsPortHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortHistoryPkts.setStatus("mandatory")
_LsPortHistoryCollisions_Type = Counter32
_LsPortHistoryCollisions_Object = MibTableColumn
lsPortHistoryCollisions = _LsPortHistoryCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1, 6),
    _LsPortHistoryCollisions_Type()
)
lsPortHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortHistoryCollisions.setStatus("mandatory")
_LsPortHistoryTotalErrors_Type = Counter32
_LsPortHistoryTotalErrors_Object = MibTableColumn
lsPortHistoryTotalErrors = _LsPortHistoryTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 2, 1, 7),
    _LsPortHistoryTotalErrors_Type()
)
lsPortHistoryTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPortHistoryTotalErrors.setStatus("mandatory")
_ScPortHistoryTable_Object = MibTable
scPortHistoryTable = _ScPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3)
)
if mibBuilder.loadTexts:
    scPortHistoryTable.setStatus("mandatory")
_ScPortHistoryEntry_Object = MibTableRow
scPortHistoryEntry = _ScPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1)
)
scPortHistoryEntry.setIndexNames(
    (0, "APPLIC-MIB", "scPortHistoryIndex"),
    (0, "APPLIC-MIB", "scPortHistorySampleIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    scPortHistoryEntry.setStatus("mandatory")


class _ScPortHistoryIndex_Type(Integer32):
    """Custom type scPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ScPortHistoryIndex_Type.__name__ = "Integer32"
_ScPortHistoryIndex_Object = MibTableColumn
scPortHistoryIndex = _ScPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 1),
    _ScPortHistoryIndex_Type()
)
scPortHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryIndex.setStatus("mandatory")


class _ScPortHistorySampleIndex_Type(Integer32):
    """Custom type scPortHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScPortHistorySampleIndex_Type.__name__ = "Integer32"
_ScPortHistorySampleIndex_Object = MibTableColumn
scPortHistorySampleIndex = _ScPortHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 2),
    _ScPortHistorySampleIndex_Type()
)
scPortHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistorySampleIndex.setStatus("mandatory")
_ScPortHistoryIntervalTime_Type = TimeTicks
_ScPortHistoryIntervalTime_Object = MibTableColumn
scPortHistoryIntervalTime = _ScPortHistoryIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 3),
    _ScPortHistoryIntervalTime_Type()
)
scPortHistoryIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryIntervalTime.setStatus("mandatory")
_ScPortHistoryBoxConfiguration_Type = OctetString
_ScPortHistoryBoxConfiguration_Object = MibTableColumn
scPortHistoryBoxConfiguration = _ScPortHistoryBoxConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 4),
    _ScPortHistoryBoxConfiguration_Type()
)
scPortHistoryBoxConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryBoxConfiguration.setStatus("mandatory")
_ScPortHistoryGoodPktsRec_Type = Counter32
_ScPortHistoryGoodPktsRec_Object = MibTableColumn
scPortHistoryGoodPktsRec = _ScPortHistoryGoodPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 5),
    _ScPortHistoryGoodPktsRec_Type()
)
scPortHistoryGoodPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryGoodPktsRec.setStatus("mandatory")
_ScPortHistoryGoodNonUnicastPktsRec_Type = Counter32
_ScPortHistoryGoodNonUnicastPktsRec_Object = MibTableColumn
scPortHistoryGoodNonUnicastPktsRec = _ScPortHistoryGoodNonUnicastPktsRec_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 6),
    _ScPortHistoryGoodNonUnicastPktsRec_Type()
)
scPortHistoryGoodNonUnicastPktsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryGoodNonUnicastPktsRec.setStatus("mandatory")
_ScPortHistoryCollisions_Type = Counter32
_ScPortHistoryCollisions_Object = MibTableColumn
scPortHistoryCollisions = _ScPortHistoryCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 7),
    _ScPortHistoryCollisions_Type()
)
scPortHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryCollisions.setStatus("mandatory")
_ScPortHistoryBadPkts_Type = Counter32
_ScPortHistoryBadPkts_Object = MibTableColumn
scPortHistoryBadPkts = _ScPortHistoryBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 8),
    _ScPortHistoryBadPkts_Type()
)
scPortHistoryBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryBadPkts.setStatus("mandatory")
_ScPortHistoryGoodPktsSent_Type = Counter32
_ScPortHistoryGoodPktsSent_Object = MibTableColumn
scPortHistoryGoodPktsSent = _ScPortHistoryGoodPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 3, 1, 9),
    _ScPortHistoryGoodPktsSent_Type()
)
scPortHistoryGoodPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scPortHistoryGoodPktsSent.setStatus("mandatory")


class _PortHistoryMemoryAvailability_Type(Integer32):
    """Custom type portHistoryMemoryAvailability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("limited1", 2),
          ("limited2", 3),
          ("notSupported", 255),
          ("standard", 1))
    )


_PortHistoryMemoryAvailability_Type.__name__ = "Integer32"
_PortHistoryMemoryAvailability_Object = MibScalar
portHistoryMemoryAvailability = _PortHistoryMemoryAvailability_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 3, 4),
    _PortHistoryMemoryAvailability_Type()
)
portHistoryMemoryAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistoryMemoryAvailability.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPLIC-MIB",
    **{"lntLanSwitch": lntLanSwitch,
       "lse": lse,
       "lseGroupTable": lseGroupTable,
       "lseGroupEntry": lseGroupEntry,
       "lseGroupId": lseGroupId,
       "lseGroupFastOpen": lseGroupFastOpen,
       "lseGroup10MSqlt": lseGroup10MSqlt,
       "lseGroupSmartSqlt": lseGroupSmartSqlt,
       "lseGroupCParameter": lseGroupCParameter,
       "lseGroupIPGJamLength": lseGroupIPGJamLength,
       "lseGroupJamLength": lseGroupJamLength,
       "lseGroupDataBlinderLength": lseGroupDataBlinderLength,
       "lseGroupIPGDataLength": lseGroupIPGDataLength,
       "lseGroupActiveMonitor": lseGroupActiveMonitor,
       "lseGroupBackbone12": lseGroupBackbone12,
       "lseGroupSetDefaults": lseGroupSetDefaults,
       "lseGroupBackbone34": lseGroupBackbone34,
       "lseGroupBackboneRedun12": lseGroupBackboneRedun12,
       "lseGroupBackoffFromJam": lseGroupBackoffFromJam,
       "lseGroupCAMClear": lseGroupCAMClear,
       "lseGroupJamPrevent": lseGroupJamPrevent,
       "lseGroupNormOpCl": lseGroupNormOpCl,
       "lseGroupNormOpDelay": lseGroupNormOpDelay,
       "lseGroupAutoPartitionEnable": lseGroupAutoPartitionEnable,
       "lseGroupWorkState": lseGroupWorkState,
       "lseGroupBITResult": lseGroupBITResult,
       "lseGroupAssignSlots": lseGroupAssignSlots,
       "lseGroupHSBMonStatus": lseGroupHSBMonStatus,
       "lseGroupEnableHSBReset": lseGroupEnableHSBReset,
       "lseIntPort": lseIntPort,
       "lseIntPortTable": lseIntPortTable,
       "lseIntPortEntry": lseIntPortEntry,
       "lseIntPortGroupId": lseIntPortGroupId,
       "lseIntPortId": lseIntPortId,
       "lseIntPortIOMode": lseIntPortIOMode,
       "lseIntPortResetSwitchCAM": lseIntPortResetSwitchCAM,
       "lseIntPortVideoPacket": lseIntPortVideoPacket,
       "lseIntPortPriorityStateMachine": lseIntPortPriorityStateMachine,
       "lseIntPortActiveBroadcastPriority": lseIntPortActiveBroadcastPriority,
       "lseIntPortPriorityLevel": lseIntPortPriorityLevel,
       "lseIntPortSuperPriorityEnable": lseIntPortSuperPriorityEnable,
       "lseIntPortRoutingMode": lseIntPortRoutingMode,
       "lseIntPortGlobal": lseIntPortGlobal,
       "lseIntPortLearnIOCAM": lseIntPortLearnIOCAM,
       "lseIntPortSecurity": lseIntPortSecurity,
       "lseIntPortIgnoreBusy": lseIntPortIgnoreBusy,
       "lseIntPortRetryPriorityLevel1": lseIntPortRetryPriorityLevel1,
       "lseIntPortRetryPriorityLevel2": lseIntPortRetryPriorityLevel2,
       "lseIntPortRetryPriorityLevel3": lseIntPortRetryPriorityLevel3,
       "lseIntPortIgnoreProtocolType": lseIntPortIgnoreProtocolType,
       "lseIntPortCompanyMAC": lseIntPortCompanyMAC,
       "lseIntPortTxSafetyZone": lseIntPortTxSafetyZone,
       "lseIntPortRxSafetyZone": lseIntPortRxSafetyZone,
       "lseIntPortTxBurstLength": lseIntPortTxBurstLength,
       "lseIntPortSecurityIntruder": lseIntPortSecurityIntruder,
       "lseIntPortJabber": lseIntPortJabber,
       "lseIntPortCAM": lseIntPortCAM,
       "lseIntPortVideoStateMachine": lseIntPortVideoStateMachine,
       "lseIntPortTransmitWeight": lseIntPortTransmitWeight,
       "lseIntPortSuperPriority": lseIntPortSuperPriority,
       "lseIntPortAlignment": lseIntPortAlignment,
       "lseIntPortRxReject": lseIntPortRxReject,
       "lseIntPortTxReject": lseIntPortTxReject,
       "lseIntPortRxEmpty0": lseIntPortRxEmpty0,
       "lseIntPortRxEmpty1": lseIntPortRxEmpty1,
       "lseIntPortRxEmpty2": lseIntPortRxEmpty2,
       "lseIntPortSuperNetNumber": lseIntPortSuperNetNumber,
       "lseIntPortGlobalSuperNet": lseIntPortGlobalSuperNet,
       "lseIntPortMACAddress": lseIntPortMACAddress,
       "lseIntPortIgnoreRoutingMode": lseIntPortIgnoreRoutingMode,
       "lseIntPortCAMLastChange": lseIntPortCAMLastChange,
       "lseIntPortCopiedPort": lseIntPortCopiedPort,
       "lseIntPortBroadcastBehavior": lseIntPortBroadcastBehavior,
       "lseIntPortFilteringMethod": lseIntPortFilteringMethod,
       "lseIntPortSetFilter": lseIntPortSetFilter,
       "lseIntPortRemoveFilter": lseIntPortRemoveFilter,
       "lseIntPortClearFilter": lseIntPortClearFilter,
       "lseIntPortMonitorMissedEvents": lseIntPortMonitorMissedEvents,
       "lseIntPortMACAdd": lseIntPortMACAdd,
       "lseIntPortMACAddTable": lseIntPortMACAddTable,
       "lseIntPortMACAddEntry": lseIntPortMACAddEntry,
       "lseIntPortMACAddGroupId": lseIntPortMACAddGroupId,
       "lseIntPortMACAddPortId": lseIntPortMACAddPortId,
       "lseIntPortMACAddLAId": lseIntPortMACAddLAId,
       "lseIntPortMACAddList": lseIntPortMACAddList,
       "lseIntPortFilter": lseIntPortFilter,
       "lseIntPortFilterTable": lseIntPortFilterTable,
       "lseIntPortFilterEntry": lseIntPortFilterEntry,
       "lseIntPortFilterGroupId": lseIntPortFilterGroupId,
       "lseIntPortFilterPortId": lseIntPortFilterPortId,
       "lseIntPortFilterLAId": lseIntPortFilterLAId,
       "lseIntPortFilterList": lseIntPortFilterList,
       "lsePort": lsePort,
       "lsePortTable": lsePortTable,
       "lsePortEntry": lsePortEntry,
       "lsePortGroupId": lsePortGroupId,
       "lsePortId": lsePortId,
       "lsePortPolarity": lsePortPolarity,
       "lsePortBackboneStatus": lsePortBackboneStatus,
       "lhs": lhs,
       "lhsGroupTable": lhsGroupTable,
       "lhsGroupEntry": lhsGroupEntry,
       "lhsGroupId": lhsGroupId,
       "lhsGroupMainSWVersion": lhsGroupMainSWVersion,
       "lhsGroupProtocolType": lhsGroupProtocolType,
       "lhsPortTable": lhsPortTable,
       "lhsPortEntry": lhsPortEntry,
       "lhsPortGroupId": lhsPortGroupId,
       "lhsPortId": lhsPortId,
       "lhsTxUCast": lhsTxUCast,
       "lhsTxBCast": lhsTxBCast,
       "lhsTxMCast": lhsTxMCast,
       "lhsTxUrunErr": lhsTxUrunErr,
       "lhsTxParErr": lhsTxParErr,
       "lhsRxUCast": lhsRxUCast,
       "lhsRxBCast": lhsRxBCast,
       "lhsRxMCast": lhsRxMCast,
       "lhsRxOrunErr": lhsRxOrunErr,
       "lhsRxParErr": lhsRxParErr,
       "lhsRxRscErr": lhsRxRscErr,
       "lhsRxBadTypeErr": lhsRxBadTypeErr,
       "lhsLinkStatus": lhsLinkStatus,
       "lsMonitor": lsMonitor,
       "lsMonitorResourceAllocation": lsMonitorResourceAllocation,
       "lsBusStats": lsBusStats,
       "lsBusStatsDropEvents": lsBusStatsDropEvents,
       "lsBusStatsPkts": lsBusStatsPkts,
       "lsBusStatsOctets": lsBusStatsOctets,
       "lsBusStatsUtilization": lsBusStatsUtilization,
       "lsBusStatsEthBroadcastPkts": lsBusStatsEthBroadcastPkts,
       "lsBusStatsMulticastPkts": lsBusStatsMulticastPkts,
       "lsBusStatsGoodEthPkts": lsBusStatsGoodEthPkts,
       "lsBusStatsGoodEthOctets": lsBusStatsGoodEthOctets,
       "lsBusStatsBadEthPkts": lsBusStatsBadEthPkts,
       "lsBusStatsBadEthOctets": lsBusStatsBadEthOctets,
       "lsBusStatsNonEthPkts": lsBusStatsNonEthPkts,
       "lsBusStatsNonEthOctets": lsBusStatsNonEthOctets,
       "lsBusStatsPriorityTable": lsBusStatsPriorityTable,
       "lsBusStatsPriorityEntry": lsBusStatsPriorityEntry,
       "lsBusStatsPriorityIndex": lsBusStatsPriorityIndex,
       "lsBusStatsPriorityPkts": lsBusStatsPriorityPkts,
       "lsBusStatsPriorityOctets": lsBusStatsPriorityOctets,
       "lsBusStatsVirtualNetList": lsBusStatsVirtualNetList,
       "lsBusStatsVirtualNetTable": lsBusStatsVirtualNetTable,
       "lsBusStatsVirtualNetEntry": lsBusStatsVirtualNetEntry,
       "lsBusStatsVirtualNet": lsBusStatsVirtualNet,
       "lsBusStatsVirtualNetPackets": lsBusStatsVirtualNetPackets,
       "lsBusStatsVirtualNetOctets": lsBusStatsVirtualNetOctets,
       "lsPortStats": lsPortStats,
       "lsPortControlTable": lsPortControlTable,
       "lsPortControlEntry": lsPortControlEntry,
       "lsPortControlIndex": lsPortControlIndex,
       "lsPortControlDataSource": lsPortControlDataSource,
       "lsPortControlTableSize": lsPortControlTableSize,
       "lsPortControlLastDeleteTime": lsPortControlLastDeleteTime,
       "lsPortControlOwner": lsPortControlOwner,
       "lsPortControlStatus": lsPortControlStatus,
       "lsPortFilterTable": lsPortFilterTable,
       "lsPortFilterEntry": lsPortFilterEntry,
       "lsPortFilter": lsPortFilter,
       "lsPortFilterStatus": lsPortFilterStatus,
       "lsPortFilterTableClear": lsPortFilterTableClear,
       "lsPortTable": lsPortTable,
       "lsPortEntry": lsPortEntry,
       "lsPortNumber": lsPortNumber,
       "lsPortInPkts": lsPortInPkts,
       "lsPortInFCSErrors": lsPortInFCSErrors,
       "lsPortInTooLongPkts": lsPortInTooLongPkts,
       "lsPortInOctets": lsPortInOctets,
       "lsPortInTotalErrors": lsPortInTotalErrors,
       "lsPortInCollisions": lsPortInCollisions,
       "lsPortExtendedReportingList": lsPortExtendedReportingList,
       "lsPortExtendedStatsTable": lsPortExtendedStatsTable,
       "lsPortExtendedStatsEntry": lsPortExtendedStatsEntry,
       "lsPortExtendedStatsNumber": lsPortExtendedStatsNumber,
       "lsPortCreationOrder": lsPortCreationOrder,
       "lsPortIndex": lsPortIndex,
       "lsPortOutPkts": lsPortOutPkts,
       "lsPortInBroadcastPkts": lsPortInBroadcastPkts,
       "lsPortInMulticastPkts": lsPortInMulticastPkts,
       "lsHostFilterTable": lsHostFilterTable,
       "lsHostFilterEntry": lsHostFilterEntry,
       "lsHostFilterAddress": lsHostFilterAddress,
       "lsHostFilterStatus": lsHostFilterStatus,
       "lsHostFilterTableClear": lsHostFilterTableClear,
       "lsHostPortFilterTable": lsHostPortFilterTable,
       "lsHostPortFilterEntry": lsHostPortFilterEntry,
       "lsHostPortFilter": lsHostPortFilter,
       "lsHostPortFilterStatus": lsHostPortFilterStatus,
       "lsHostPortFilterTableClear": lsHostPortFilterTableClear,
       "lsMatrixFilterTable": lsMatrixFilterTable,
       "lsMatrixFilterEntry": lsMatrixFilterEntry,
       "lsMatrixFilterAddress": lsMatrixFilterAddress,
       "lsMatrixFilterStatus": lsMatrixFilterStatus,
       "lsMatrixFilterTableClear": lsMatrixFilterTableClear,
       "lsHostTimePortCorrTable": lsHostTimePortCorrTable,
       "lsHostTimePortCorrEntry": lsHostTimePortCorrEntry,
       "hostTimeAddress": hostTimeAddress,
       "hostTimeCreationOrder": hostTimeCreationOrder,
       "hostTimeIndex": hostTimeIndex,
       "hostTimePortConnection": hostTimePortConnection,
       "lsHistoryTable": lsHistoryTable,
       "lsHistoryEntry": lsHistoryEntry,
       "lsHistoryIndex": lsHistoryIndex,
       "lsHistorySampleIndex": lsHistorySampleIndex,
       "lsHistoryIntervalTime": lsHistoryIntervalTime,
       "lsHistoryStatsDropEvents": lsHistoryStatsDropEvents,
       "lsHistoryStatsPkts": lsHistoryStatsPkts,
       "lsHistoryStatsOctets": lsHistoryStatsOctets,
       "lsHistoryStatsEthBroadcastPkts": lsHistoryStatsEthBroadcastPkts,
       "lsHistoryStatsEthMulticastPkts": lsHistoryStatsEthMulticastPkts,
       "lsHistoryStatsGoodEthPkts": lsHistoryStatsGoodEthPkts,
       "lsHistoryStatsGoodEthOctets": lsHistoryStatsGoodEthOctets,
       "lsHistoryStatsBadEthPkts": lsHistoryStatsBadEthPkts,
       "lsHistoryStatsBadEthOctets": lsHistoryStatsBadEthOctets,
       "lsHistoryStatsNonEthPkts": lsHistoryStatsNonEthPkts,
       "lsHistoryStatsNonEthOctets": lsHistoryStatsNonEthOctets,
       "lsHistoryStatsPriority1Pkts": lsHistoryStatsPriority1Pkts,
       "lsHistoryStatsPriority1Octets": lsHistoryStatsPriority1Octets,
       "lsHistoryStatsPriority2Pkts": lsHistoryStatsPriority2Pkts,
       "lsHistoryStatsPriority2Octets": lsHistoryStatsPriority2Octets,
       "lsHistoryStatsPriority3Pkts": lsHistoryStatsPriority3Pkts,
       "lsHistoryStatsPriority3Octets": lsHistoryStatsPriority3Octets,
       "lsHistoryStatsPriority4Pkts": lsHistoryStatsPriority4Pkts,
       "lsHistoryStatsPriority4Octets": lsHistoryStatsPriority4Octets,
       "lsHistoryBusUtilization": lsHistoryBusUtilization,
       "lst": lst,
       "lstIntPort": lstIntPort,
       "lstIntPortTable": lstIntPortTable,
       "lstIntPortEntry": lstIntPortEntry,
       "lstIntPortGroupId": lstIntPortGroupId,
       "lstIntPortId": lstIntPortId,
       "lstIntPortSidebandMode": lstIntPortSidebandMode,
       "lstIntPortTotalOctets": lstIntPortTotalOctets,
       "lstIntPortTotalTraffic": lstIntPortTotalTraffic,
       "lstIntPortLocalOctets": lstIntPortLocalOctets,
       "lstIntPortLocalTraffic": lstIntPortLocalTraffic,
       "lstIntPortInOctets": lstIntPortInOctets,
       "lstIntPortInTraffic": lstIntPortInTraffic,
       "lstIntPortOutOctets": lstIntPortOutOctets,
       "lstIntPortOutTraffic": lstIntPortOutTraffic,
       "lstIntPortTotalFrames": lstIntPortTotalFrames,
       "lstIntPortLostFrames": lstIntPortLostFrames,
       "lstIntPortClaimFrames": lstIntPortClaimFrames,
       "lstIntPortPurgeFrames": lstIntPortPurgeFrames,
       "lstIntPortNormallyCloseOpen": lstIntPortNormallyCloseOpen,
       "lstIntPortSlicingEnable": lstIntPortSlicingEnable,
       "lstIntPortSliceLength": lstIntPortSliceLength,
       "lstIntPortUNAddr": lstIntPortUNAddr,
       "lstIntPortMACAddress": lstIntPortMACAddress,
       "lstIntPortSMPTransmitEnable": lstIntPortSMPTransmitEnable,
       "lstIntPortIPGLength": lstIntPortIPGLength,
       "lstIntPortBPDummyWindow": lstIntPortBPDummyWindow,
       "lstIntPortBPTokenWindow": lstIntPortBPTokenWindow,
       "lstIntPortTransmitWindow": lstIntPortTransmitWindow,
       "lstIntPortBlockingPriority": lstIntPortBlockingPriority,
       "lstIntPortNormalPriority": lstIntPortNormalPriority,
       "lstIntPortDummyMV": lstIntPortDummyMV,
       "lstIntPortTxConsecutiveBusiesThresh": lstIntPortTxConsecutiveBusiesThresh,
       "lstIntPortTxBufFullThresh": lstIntPortTxBufFullThresh,
       "lstIntPortRxEmpty0": lstIntPortRxEmpty0,
       "lstIntPortRxEmpty1": lstIntPortRxEmpty1,
       "lstIntPortRxEmpty2": lstIntPortRxEmpty2,
       "lstIntPortRxFull": lstIntPortRxFull,
       "lstIntPortBPEnable": lstIntPortBPEnable,
       "lstIntPortRouteSideband": lstIntPortRouteSideband,
       "lseWANTable": lseWANTable,
       "lseWANEntry": lseWANEntry,
       "lseWANGroupId": lseWANGroupId,
       "lseWANPortId": lseWANPortId,
       "lseWANConnection": lseWANConnection,
       "lsVNChange": lsVNChange,
       "lsVNChangeMACAddress": lsVNChangeMACAddress,
       "lsVNChangeDetected": lsVNChangeDetected,
       "lsVNChangeExpected": lsVNChangeExpected,
       "lsVNChangeGroup": lsVNChangeGroup,
       "lsVNChangePort": lsVNChangePort,
       "vnsPacket": vnsPacket,
       "vnsPacketTable": vnsPacketTable,
       "vnsPacketEntry": vnsPacketEntry,
       "vnsPacketMACAddress": vnsPacketMACAddress,
       "vnsPacketProtocolTypeMask": vnsPacketProtocolTypeMask,
       "vnsPacketIPAddress": vnsPacketIPAddress,
       "vnsPacketIPNetMask": vnsPacketIPNetMask,
       "vnsPacketIPXnetwork": vnsPacketIPXnetwork,
       "vnsPacketStationType": vnsPacketStationType,
       "vnsPacketPortGroupId": vnsPacketPortGroupId,
       "vnsPacketPortId": vnsPacketPortId,
       "vnsPacketBackbonePort": vnsPacketBackbonePort,
       "vnsPacketExpectedVLAN": vnsPacketExpectedVLAN,
       "vnsPacketDetectedVLAN": vnsPacketDetectedVLAN,
       "vnsPacketBoxAgentIP": vnsPacketBoxAgentIP,
       "lntTopology": lntTopology,
       "topDiscovery": topDiscovery,
       "topDiscoveryTimeOut": topDiscoveryTimeOut,
       "ethTop": ethTop,
       "ethTopDiscoveryTx": ethTopDiscoveryTx,
       "ethTopClearMessageResult": ethTopClearMessageResult,
       "ethTopNumOfMessageResults": ethTopNumOfMessageResults,
       "ethTopMessageResultTable": ethTopMessageResultTable,
       "ethTopMessageResultEntry": ethTopMessageResultEntry,
       "ethTopMessageResultId": ethTopMessageResultId,
       "ethTopMessageResult": ethTopMessageResult,
       "ethTopMACFindList": ethTopMACFindList,
       "ethTopMACFindResultTable": ethTopMACFindResultTable,
       "ethTopMACFindResultEntry": ethTopMACFindResultEntry,
       "ethTopMACFindBus": ethTopMACFindBus,
       "ethTopMACFindResult": ethTopMACFindResult,
       "ethTopLSATable": ethTopLSATable,
       "ethTopLSAEntry": ethTopLSAEntry,
       "ethTopLSAId": ethTopLSAId,
       "ethTopLSA": ethTopLSA,
       "ethTopAddressTable": ethTopAddressTable,
       "ethTopAddressEntry": ethTopAddressEntry,
       "ethTopBus": ethTopBus,
       "ethTopAddress": ethTopAddress,
       "ethTopHSBMonitor": ethTopHSBMonitor,
       "smon": smon,
       "alarms": alarms,
       "alarmMonitorStatusTable": alarmMonitorStatusTable,
       "alarmMonitorStatusEntry": alarmMonitorStatusEntry,
       "alarmMonitorStatusIndex": alarmMonitorStatusIndex,
       "alarmMonitorStatus": alarmMonitorStatus,
       "alarmUtilitiesCommand": alarmUtilitiesCommand,
       "portHistory": portHistory,
       "portHistoryExtendedControlTable": portHistoryExtendedControlTable,
       "portHistoryExtendedControlEntry": portHistoryExtendedControlEntry,
       "portHistoryExtendedControlCreateTime": portHistoryExtendedControlCreateTime,
       "portHistoryExtendedControlLastBucketIndex": portHistoryExtendedControlLastBucketIndex,
       "portHistoryExtendedControlNumberOfBuckets": portHistoryExtendedControlNumberOfBuckets,
       "portHistoryExtendedControlName": portHistoryExtendedControlName,
       "lsPortHistoryTable": lsPortHistoryTable,
       "lsPortHistoryEntry": lsPortHistoryEntry,
       "lsPortHistoryIndex": lsPortHistoryIndex,
       "lsPortHistorySampleIndex": lsPortHistorySampleIndex,
       "lsPortHistoryIntervalTime": lsPortHistoryIntervalTime,
       "lsPortHistoryBoxConfiguration": lsPortHistoryBoxConfiguration,
       "lsPortHistoryPkts": lsPortHistoryPkts,
       "lsPortHistoryCollisions": lsPortHistoryCollisions,
       "lsPortHistoryTotalErrors": lsPortHistoryTotalErrors,
       "scPortHistoryTable": scPortHistoryTable,
       "scPortHistoryEntry": scPortHistoryEntry,
       "scPortHistoryIndex": scPortHistoryIndex,
       "scPortHistorySampleIndex": scPortHistorySampleIndex,
       "scPortHistoryIntervalTime": scPortHistoryIntervalTime,
       "scPortHistoryBoxConfiguration": scPortHistoryBoxConfiguration,
       "scPortHistoryGoodPktsRec": scPortHistoryGoodPktsRec,
       "scPortHistoryGoodNonUnicastPktsRec": scPortHistoryGoodNonUnicastPktsRec,
       "scPortHistoryCollisions": scPortHistoryCollisions,
       "scPortHistoryBadPkts": scPortHistoryBadPkts,
       "scPortHistoryGoodPktsSent": scPortHistoryGoodPktsSent,
       "portHistoryMemoryAvailability": portHistoryMemoryAvailability}
)
