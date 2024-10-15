# SNMP MIB module (ACD-ERP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-ERP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:19 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdErp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15)
)
acdErp.setRevisions(
        ("2012-01-11 01:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcdErpVlanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 1),
          ("svlan", 2))
    )



class AcdErpPortStateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("forwarding", 0))
    )



class AcdErpStateType(Integer32, TextualConvention):
    status = "current"
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
        *(("fs", 4),
          ("idle", 1),
          ("ms", 3),
          ("pending", 5),
          ("prot", 2))
    )



class AcdErpPortStatusType(Integer32, TextualConvention):
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
        *(("ok", 1),
          ("sd", 2),
          ("sf", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AcdErpMIBObjects_ObjectIdentity = ObjectIdentity
acdErpMIBObjects = _AcdErpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0)
)
_AcdErpConfig_ObjectIdentity = ObjectIdentity
acdErpConfig = _AcdErpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1)
)
_AcdErpConfigTable_Object = MibTable
acdErpConfigTable = _AcdErpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1)
)
if mibBuilder.loadTexts:
    acdErpConfigTable.setStatus("current")
_AcdErpConfigEntry_Object = MibTableRow
acdErpConfigEntry = _AcdErpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1)
)
acdErpConfigEntry.setIndexNames(
    (0, "ACD-ERP-MIB", "acdErpIndex"),
)
if mibBuilder.loadTexts:
    acdErpConfigEntry.setStatus("current")
_AcdErpIndex_Type = Unsigned32
_AcdErpIndex_Object = MibTableColumn
acdErpIndex = _AcdErpIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 1),
    _AcdErpIndex_Type()
)
acdErpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdErpIndex.setStatus("current")
_AcdErpConfigRowStatus_Type = RowStatus
_AcdErpConfigRowStatus_Object = MibTableColumn
acdErpConfigRowStatus = _AcdErpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 2),
    _AcdErpConfigRowStatus_Type()
)
acdErpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdErpConfigRowStatus.setStatus("current")


class _AcdErpConfigName_Type(DisplayString):
    """Custom type acdErpConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdErpConfigName_Type.__name__ = "DisplayString"
_AcdErpConfigName_Object = MibTableColumn
acdErpConfigName = _AcdErpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 3),
    _AcdErpConfigName_Type()
)
acdErpConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdErpConfigName.setStatus("current")


class _AcdErpConfigRPLRole_Type(DisplayString):
    """Custom type acdErpConfigRPLRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdErpConfigRPLRole_Type.__name__ = "DisplayString"
_AcdErpConfigRPLRole_Object = MibTableColumn
acdErpConfigRPLRole = _AcdErpConfigRPLRole_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 4),
    _AcdErpConfigRPLRole_Type()
)
acdErpConfigRPLRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigRPLRole.setStatus("current")


class _AcdErpConfigRPLPort_Type(Unsigned32):
    """Custom type acdErpConfigRPLPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdErpConfigRPLPort_Type.__name__ = "Unsigned32"
_AcdErpConfigRPLPort_Object = MibTableColumn
acdErpConfigRPLPort = _AcdErpConfigRPLPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 5),
    _AcdErpConfigRPLPort_Type()
)
acdErpConfigRPLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigRPLPort.setStatus("current")


class _AcdErpConfigHoldOffTimer_Type(Unsigned32):
    """Custom type acdErpConfigHoldOffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AcdErpConfigHoldOffTimer_Type.__name__ = "Unsigned32"
_AcdErpConfigHoldOffTimer_Object = MibTableColumn
acdErpConfigHoldOffTimer = _AcdErpConfigHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 6),
    _AcdErpConfigHoldOffTimer_Type()
)
acdErpConfigHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigHoldOffTimer.setStatus("current")


class _AcdErpConfigRevertive_Type(TruthValue):
    """Custom type acdErpConfigRevertive based on TruthValue"""
    defaultValue = 1


_AcdErpConfigRevertive_Object = MibTableColumn
acdErpConfigRevertive = _AcdErpConfigRevertive_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 7),
    _AcdErpConfigRevertive_Type()
)
acdErpConfigRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigRevertive.setStatus("current")


class _AcdErpConfigGuardTimer_Type(Unsigned32):
    """Custom type acdErpConfigGuardTimer based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AcdErpConfigGuardTimer_Type.__name__ = "Unsigned32"
_AcdErpConfigGuardTimer_Object = MibTableColumn
acdErpConfigGuardTimer = _AcdErpConfigGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 8),
    _AcdErpConfigGuardTimer_Type()
)
acdErpConfigGuardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigGuardTimer.setStatus("current")


class _AcdErpConfigWTRTimer_Type(Unsigned32):
    """Custom type acdErpConfigWTRTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AcdErpConfigWTRTimer_Type.__name__ = "Unsigned32"
_AcdErpConfigWTRTimer_Object = MibTableColumn
acdErpConfigWTRTimer = _AcdErpConfigWTRTimer_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 9),
    _AcdErpConfigWTRTimer_Type()
)
acdErpConfigWTRTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigWTRTimer.setStatus("current")


class _AcdErpConfigMDLevel_Type(Unsigned32):
    """Custom type acdErpConfigMDLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdErpConfigMDLevel_Type.__name__ = "Unsigned32"
_AcdErpConfigMDLevel_Object = MibTableColumn
acdErpConfigMDLevel = _AcdErpConfigMDLevel_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 10),
    _AcdErpConfigMDLevel_Type()
)
acdErpConfigMDLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigMDLevel.setStatus("current")


class _AcdErpConfigAPSVid_Type(Unsigned32):
    """Custom type acdErpConfigAPSVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdErpConfigAPSVid_Type.__name__ = "Unsigned32"
_AcdErpConfigAPSVid_Object = MibTableColumn
acdErpConfigAPSVid = _AcdErpConfigAPSVid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 11),
    _AcdErpConfigAPSVid_Type()
)
acdErpConfigAPSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigAPSVid.setStatus("current")


class _AcdErpConfigVids0to1023_Type(OctetString):
    """Custom type acdErpConfigVids0to1023 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpConfigVids0to1023_Type.__name__ = "OctetString"
_AcdErpConfigVids0to1023_Object = MibTableColumn
acdErpConfigVids0to1023 = _AcdErpConfigVids0to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 12),
    _AcdErpConfigVids0to1023_Type()
)
acdErpConfigVids0to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpConfigVids0to1023.setStatus("current")


class _AcdErpConfigVids1024to2047_Type(OctetString):
    """Custom type acdErpConfigVids1024to2047 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpConfigVids1024to2047_Type.__name__ = "OctetString"
_AcdErpConfigVids1024to2047_Object = MibTableColumn
acdErpConfigVids1024to2047 = _AcdErpConfigVids1024to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 13),
    _AcdErpConfigVids1024to2047_Type()
)
acdErpConfigVids1024to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpConfigVids1024to2047.setStatus("current")


class _AcdErpConfigVids2048to3071_Type(OctetString):
    """Custom type acdErpConfigVids2048to3071 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpConfigVids2048to3071_Type.__name__ = "OctetString"
_AcdErpConfigVids2048to3071_Object = MibTableColumn
acdErpConfigVids2048to3071 = _AcdErpConfigVids2048to3071_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 14),
    _AcdErpConfigVids2048to3071_Type()
)
acdErpConfigVids2048to3071.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpConfigVids2048to3071.setStatus("current")


class _AcdErpConfigVids3072to4095_Type(OctetString):
    """Custom type acdErpConfigVids3072to4095 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpConfigVids3072to4095_Type.__name__ = "OctetString"
_AcdErpConfigVids3072to4095_Object = MibTableColumn
acdErpConfigVids3072to4095 = _AcdErpConfigVids3072to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 15),
    _AcdErpConfigVids3072to4095_Type()
)
acdErpConfigVids3072to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpConfigVids3072to4095.setStatus("current")


class _AcdErpConfigLAGPort_Type(DisplayString):
    """Custom type acdErpConfigLAGPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdErpConfigLAGPort_Type.__name__ = "DisplayString"
_AcdErpConfigLAGPort_Object = MibTableColumn
acdErpConfigLAGPort = _AcdErpConfigLAGPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 16),
    _AcdErpConfigLAGPort_Type()
)
acdErpConfigLAGPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigLAGPort.setStatus("current")


class _AcdErpConfigMep0Idx_Type(Unsigned32):
    """Custom type acdErpConfigMep0Idx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AcdErpConfigMep0Idx_Type.__name__ = "Unsigned32"
_AcdErpConfigMep0Idx_Object = MibTableColumn
acdErpConfigMep0Idx = _AcdErpConfigMep0Idx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 17),
    _AcdErpConfigMep0Idx_Type()
)
acdErpConfigMep0Idx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigMep0Idx.setStatus("current")


class _AcdErpConfigMep1Idx_Type(Unsigned32):
    """Custom type acdErpConfigMep1Idx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AcdErpConfigMep1Idx_Type.__name__ = "Unsigned32"
_AcdErpConfigMep1Idx_Object = MibTableColumn
acdErpConfigMep1Idx = _AcdErpConfigMep1Idx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 1, 1, 1, 18),
    _AcdErpConfigMep1Idx_Type()
)
acdErpConfigMep1Idx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdErpConfigMep1Idx.setStatus("current")
_AcdErpCounter_ObjectIdentity = ObjectIdentity
acdErpCounter = _AcdErpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2)
)
_AcdErpCounterTable_Object = MibTable
acdErpCounterTable = _AcdErpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1)
)
if mibBuilder.loadTexts:
    acdErpCounterTable.setStatus("current")
_AcdErpCounterEntry_Object = MibTableRow
acdErpCounterEntry = _AcdErpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1)
)
acdErpCounterEntry.setIndexNames(
    (0, "ACD-ERP-MIB", "acdErpCounterIndex"),
)
if mibBuilder.loadTexts:
    acdErpCounterEntry.setStatus("current")
_AcdErpCounterIndex_Type = Unsigned32
_AcdErpCounterIndex_Object = MibTableColumn
acdErpCounterIndex = _AcdErpCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 1),
    _AcdErpCounterIndex_Type()
)
acdErpCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdErpCounterIndex.setStatus("current")
_AcdErpCounterPort0LocalClear_Type = Unsigned32
_AcdErpCounterPort0LocalClear_Object = MibTableColumn
acdErpCounterPort0LocalClear = _AcdErpCounterPort0LocalClear_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 2),
    _AcdErpCounterPort0LocalClear_Type()
)
acdErpCounterPort0LocalClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0LocalClear.setStatus("current")
_AcdErpCounterPort0LocalFs_Type = Unsigned32
_AcdErpCounterPort0LocalFs_Object = MibTableColumn
acdErpCounterPort0LocalFs = _AcdErpCounterPort0LocalFs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 3),
    _AcdErpCounterPort0LocalFs_Type()
)
acdErpCounterPort0LocalFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0LocalFs.setStatus("current")
_AcdErpCounterPort0LocalSf_Type = Unsigned32
_AcdErpCounterPort0LocalSf_Object = MibTableColumn
acdErpCounterPort0LocalSf = _AcdErpCounterPort0LocalSf_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 4),
    _AcdErpCounterPort0LocalSf_Type()
)
acdErpCounterPort0LocalSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0LocalSf.setStatus("current")
_AcdErpCounterPort0LocalMs_Type = Unsigned32
_AcdErpCounterPort0LocalMs_Object = MibTableColumn
acdErpCounterPort0LocalMs = _AcdErpCounterPort0LocalMs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 5),
    _AcdErpCounterPort0LocalMs_Type()
)
acdErpCounterPort0LocalMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0LocalMs.setStatus("current")
_AcdErpCounterPort0RxAps_Type = Unsigned32
_AcdErpCounterPort0RxAps_Object = MibTableColumn
acdErpCounterPort0RxAps = _AcdErpCounterPort0RxAps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 6),
    _AcdErpCounterPort0RxAps_Type()
)
acdErpCounterPort0RxAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0RxAps.setStatus("current")
_AcdErpCounterPort0RxApsFs_Type = Unsigned32
_AcdErpCounterPort0RxApsFs_Object = MibTableColumn
acdErpCounterPort0RxApsFs = _AcdErpCounterPort0RxApsFs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 7),
    _AcdErpCounterPort0RxApsFs_Type()
)
acdErpCounterPort0RxApsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0RxApsFs.setStatus("current")
_AcdErpCounterPort0RxApsSf_Type = Unsigned32
_AcdErpCounterPort0RxApsSf_Object = MibTableColumn
acdErpCounterPort0RxApsSf = _AcdErpCounterPort0RxApsSf_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 8),
    _AcdErpCounterPort0RxApsSf_Type()
)
acdErpCounterPort0RxApsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0RxApsSf.setStatus("current")
_AcdErpCounterPort0RxApsMs_Type = Unsigned32
_AcdErpCounterPort0RxApsMs_Object = MibTableColumn
acdErpCounterPort0RxApsMs = _AcdErpCounterPort0RxApsMs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 9),
    _AcdErpCounterPort0RxApsMs_Type()
)
acdErpCounterPort0RxApsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0RxApsMs.setStatus("current")
_AcdErpCounterPort0RxApsNrRb_Type = Unsigned32
_AcdErpCounterPort0RxApsNrRb_Object = MibTableColumn
acdErpCounterPort0RxApsNrRb = _AcdErpCounterPort0RxApsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 10),
    _AcdErpCounterPort0RxApsNrRb_Type()
)
acdErpCounterPort0RxApsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0RxApsNrRb.setStatus("current")
_AcdErpCounterPort0RxApsNr_Type = Unsigned32
_AcdErpCounterPort0RxApsNr_Object = MibTableColumn
acdErpCounterPort0RxApsNr = _AcdErpCounterPort0RxApsNr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 11),
    _AcdErpCounterPort0RxApsNr_Type()
)
acdErpCounterPort0RxApsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0RxApsNr.setStatus("current")
_AcdErpCounterPort0TxAps_Type = Unsigned32
_AcdErpCounterPort0TxAps_Object = MibTableColumn
acdErpCounterPort0TxAps = _AcdErpCounterPort0TxAps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 12),
    _AcdErpCounterPort0TxAps_Type()
)
acdErpCounterPort0TxAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0TxAps.setStatus("current")
_AcdErpCounterPort0TxApsFs_Type = Unsigned32
_AcdErpCounterPort0TxApsFs_Object = MibTableColumn
acdErpCounterPort0TxApsFs = _AcdErpCounterPort0TxApsFs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 13),
    _AcdErpCounterPort0TxApsFs_Type()
)
acdErpCounterPort0TxApsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0TxApsFs.setStatus("current")
_AcdErpCounterPort0TxApsSf_Type = Unsigned32
_AcdErpCounterPort0TxApsSf_Object = MibTableColumn
acdErpCounterPort0TxApsSf = _AcdErpCounterPort0TxApsSf_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 14),
    _AcdErpCounterPort0TxApsSf_Type()
)
acdErpCounterPort0TxApsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0TxApsSf.setStatus("current")
_AcdErpCounterPort0TxApsMs_Type = Unsigned32
_AcdErpCounterPort0TxApsMs_Object = MibTableColumn
acdErpCounterPort0TxApsMs = _AcdErpCounterPort0TxApsMs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 15),
    _AcdErpCounterPort0TxApsMs_Type()
)
acdErpCounterPort0TxApsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0TxApsMs.setStatus("current")
_AcdErpCounterPort0TxApsNrRb_Type = Unsigned32
_AcdErpCounterPort0TxApsNrRb_Object = MibTableColumn
acdErpCounterPort0TxApsNrRb = _AcdErpCounterPort0TxApsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 16),
    _AcdErpCounterPort0TxApsNrRb_Type()
)
acdErpCounterPort0TxApsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0TxApsNrRb.setStatus("current")
_AcdErpCounterPort0TxApsNr_Type = Unsigned32
_AcdErpCounterPort0TxApsNr_Object = MibTableColumn
acdErpCounterPort0TxApsNr = _AcdErpCounterPort0TxApsNr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 17),
    _AcdErpCounterPort0TxApsNr_Type()
)
acdErpCounterPort0TxApsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0TxApsNr.setStatus("current")
_AcdErpCounterPort0DropGuard_Type = Unsigned32
_AcdErpCounterPort0DropGuard_Object = MibTableColumn
acdErpCounterPort0DropGuard = _AcdErpCounterPort0DropGuard_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 18),
    _AcdErpCounterPort0DropGuard_Type()
)
acdErpCounterPort0DropGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0DropGuard.setStatus("current")
_AcdErpCounterPort0DropUnknown_Type = Unsigned32
_AcdErpCounterPort0DropUnknown_Object = MibTableColumn
acdErpCounterPort0DropUnknown = _AcdErpCounterPort0DropUnknown_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 19),
    _AcdErpCounterPort0DropUnknown_Type()
)
acdErpCounterPort0DropUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0DropUnknown.setStatus("current")
_AcdErpCounterPort0DropMismatch_Type = Unsigned32
_AcdErpCounterPort0DropMismatch_Object = MibTableColumn
acdErpCounterPort0DropMismatch = _AcdErpCounterPort0DropMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 20),
    _AcdErpCounterPort0DropMismatch_Type()
)
acdErpCounterPort0DropMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort0DropMismatch.setStatus("current")
_AcdErpCounterPort1LocalClear_Type = Unsigned32
_AcdErpCounterPort1LocalClear_Object = MibTableColumn
acdErpCounterPort1LocalClear = _AcdErpCounterPort1LocalClear_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 21),
    _AcdErpCounterPort1LocalClear_Type()
)
acdErpCounterPort1LocalClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1LocalClear.setStatus("current")
_AcdErpCounterPort1LocalFs_Type = Unsigned32
_AcdErpCounterPort1LocalFs_Object = MibTableColumn
acdErpCounterPort1LocalFs = _AcdErpCounterPort1LocalFs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 22),
    _AcdErpCounterPort1LocalFs_Type()
)
acdErpCounterPort1LocalFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1LocalFs.setStatus("current")
_AcdErpCounterPort1LocalSf_Type = Unsigned32
_AcdErpCounterPort1LocalSf_Object = MibTableColumn
acdErpCounterPort1LocalSf = _AcdErpCounterPort1LocalSf_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 23),
    _AcdErpCounterPort1LocalSf_Type()
)
acdErpCounterPort1LocalSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1LocalSf.setStatus("current")
_AcdErpCounterPort1LocalMs_Type = Unsigned32
_AcdErpCounterPort1LocalMs_Object = MibTableColumn
acdErpCounterPort1LocalMs = _AcdErpCounterPort1LocalMs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 24),
    _AcdErpCounterPort1LocalMs_Type()
)
acdErpCounterPort1LocalMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1LocalMs.setStatus("current")
_AcdErpCounterPort1RxAps_Type = Unsigned32
_AcdErpCounterPort1RxAps_Object = MibTableColumn
acdErpCounterPort1RxAps = _AcdErpCounterPort1RxAps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 25),
    _AcdErpCounterPort1RxAps_Type()
)
acdErpCounterPort1RxAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1RxAps.setStatus("current")
_AcdErpCounterPort1RxApsFs_Type = Unsigned32
_AcdErpCounterPort1RxApsFs_Object = MibTableColumn
acdErpCounterPort1RxApsFs = _AcdErpCounterPort1RxApsFs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 26),
    _AcdErpCounterPort1RxApsFs_Type()
)
acdErpCounterPort1RxApsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1RxApsFs.setStatus("current")
_AcdErpCounterPort1RxApsSf_Type = Unsigned32
_AcdErpCounterPort1RxApsSf_Object = MibTableColumn
acdErpCounterPort1RxApsSf = _AcdErpCounterPort1RxApsSf_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 27),
    _AcdErpCounterPort1RxApsSf_Type()
)
acdErpCounterPort1RxApsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1RxApsSf.setStatus("current")
_AcdErpCounterPort1RxApsMs_Type = Unsigned32
_AcdErpCounterPort1RxApsMs_Object = MibTableColumn
acdErpCounterPort1RxApsMs = _AcdErpCounterPort1RxApsMs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 28),
    _AcdErpCounterPort1RxApsMs_Type()
)
acdErpCounterPort1RxApsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1RxApsMs.setStatus("current")
_AcdErpCounterPort1RxApsNrRb_Type = Unsigned32
_AcdErpCounterPort1RxApsNrRb_Object = MibTableColumn
acdErpCounterPort1RxApsNrRb = _AcdErpCounterPort1RxApsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 29),
    _AcdErpCounterPort1RxApsNrRb_Type()
)
acdErpCounterPort1RxApsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1RxApsNrRb.setStatus("current")
_AcdErpCounterPort1RxApsNr_Type = Unsigned32
_AcdErpCounterPort1RxApsNr_Object = MibTableColumn
acdErpCounterPort1RxApsNr = _AcdErpCounterPort1RxApsNr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 30),
    _AcdErpCounterPort1RxApsNr_Type()
)
acdErpCounterPort1RxApsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1RxApsNr.setStatus("current")
_AcdErpCounterPort1TxAps_Type = Unsigned32
_AcdErpCounterPort1TxAps_Object = MibTableColumn
acdErpCounterPort1TxAps = _AcdErpCounterPort1TxAps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 31),
    _AcdErpCounterPort1TxAps_Type()
)
acdErpCounterPort1TxAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1TxAps.setStatus("current")
_AcdErpCounterPort1TxApsFs_Type = Unsigned32
_AcdErpCounterPort1TxApsFs_Object = MibTableColumn
acdErpCounterPort1TxApsFs = _AcdErpCounterPort1TxApsFs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 32),
    _AcdErpCounterPort1TxApsFs_Type()
)
acdErpCounterPort1TxApsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1TxApsFs.setStatus("current")
_AcdErpCounterPort1TxApsSf_Type = Unsigned32
_AcdErpCounterPort1TxApsSf_Object = MibTableColumn
acdErpCounterPort1TxApsSf = _AcdErpCounterPort1TxApsSf_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 33),
    _AcdErpCounterPort1TxApsSf_Type()
)
acdErpCounterPort1TxApsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1TxApsSf.setStatus("current")
_AcdErpCounterPort1TxApsMs_Type = Unsigned32
_AcdErpCounterPort1TxApsMs_Object = MibTableColumn
acdErpCounterPort1TxApsMs = _AcdErpCounterPort1TxApsMs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 34),
    _AcdErpCounterPort1TxApsMs_Type()
)
acdErpCounterPort1TxApsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1TxApsMs.setStatus("current")
_AcdErpCounterPort1TxApsNrRb_Type = Unsigned32
_AcdErpCounterPort1TxApsNrRb_Object = MibTableColumn
acdErpCounterPort1TxApsNrRb = _AcdErpCounterPort1TxApsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 35),
    _AcdErpCounterPort1TxApsNrRb_Type()
)
acdErpCounterPort1TxApsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1TxApsNrRb.setStatus("current")
_AcdErpCounterPort1TxApsNr_Type = Unsigned32
_AcdErpCounterPort1TxApsNr_Object = MibTableColumn
acdErpCounterPort1TxApsNr = _AcdErpCounterPort1TxApsNr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 36),
    _AcdErpCounterPort1TxApsNr_Type()
)
acdErpCounterPort1TxApsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1TxApsNr.setStatus("current")
_AcdErpCounterPort1DropGuard_Type = Unsigned32
_AcdErpCounterPort1DropGuard_Object = MibTableColumn
acdErpCounterPort1DropGuard = _AcdErpCounterPort1DropGuard_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 37),
    _AcdErpCounterPort1DropGuard_Type()
)
acdErpCounterPort1DropGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1DropGuard.setStatus("current")
_AcdErpCounterPort1DropUnknown_Type = Unsigned32
_AcdErpCounterPort1DropUnknown_Object = MibTableColumn
acdErpCounterPort1DropUnknown = _AcdErpCounterPort1DropUnknown_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 38),
    _AcdErpCounterPort1DropUnknown_Type()
)
acdErpCounterPort1DropUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1DropUnknown.setStatus("current")
_AcdErpCounterPort1DropMismatch_Type = Unsigned32
_AcdErpCounterPort1DropMismatch_Object = MibTableColumn
acdErpCounterPort1DropMismatch = _AcdErpCounterPort1DropMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 2, 1, 1, 39),
    _AcdErpCounterPort1DropMismatch_Type()
)
acdErpCounterPort1DropMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpCounterPort1DropMismatch.setStatus("current")
_AcdErpStatus_ObjectIdentity = ObjectIdentity
acdErpStatus = _AcdErpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3)
)
_AcdErpStatusTable_Object = MibTable
acdErpStatusTable = _AcdErpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1)
)
if mibBuilder.loadTexts:
    acdErpStatusTable.setStatus("current")
_AcdErpStatusEntry_Object = MibTableRow
acdErpStatusEntry = _AcdErpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1)
)
acdErpStatusEntry.setIndexNames(
    (0, "ACD-ERP-MIB", "acdErpStatusIdx"),
)
if mibBuilder.loadTexts:
    acdErpStatusEntry.setStatus("current")
_AcdErpStatusIdx_Type = Unsigned32
_AcdErpStatusIdx_Object = MibTableColumn
acdErpStatusIdx = _AcdErpStatusIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 1),
    _AcdErpStatusIdx_Type()
)
acdErpStatusIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdErpStatusIdx.setStatus("current")


class _AcdErpStatusName_Type(DisplayString):
    """Custom type acdErpStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdErpStatusName_Type.__name__ = "DisplayString"
_AcdErpStatusName_Object = MibTableColumn
acdErpStatusName = _AcdErpStatusName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 2),
    _AcdErpStatusName_Type()
)
acdErpStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpStatusName.setStatus("current")
_AcdErpStatusNodeId_Type = MacAddress
_AcdErpStatusNodeId_Object = MibTableColumn
acdErpStatusNodeId = _AcdErpStatusNodeId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 3),
    _AcdErpStatusNodeId_Type()
)
acdErpStatusNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpStatusNodeId.setStatus("current")
_AcdErpStatusRPLNodeId_Type = MacAddress
_AcdErpStatusRPLNodeId_Object = MibTableColumn
acdErpStatusRPLNodeId = _AcdErpStatusRPLNodeId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 4),
    _AcdErpStatusRPLNodeId_Type()
)
acdErpStatusRPLNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpStatusRPLNodeId.setStatus("current")
_AcdErpStatusState_Type = AcdErpStateType
_AcdErpStatusState_Object = MibTableColumn
acdErpStatusState = _AcdErpStatusState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 5),
    _AcdErpStatusState_Type()
)
acdErpStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpStatusState.setStatus("current")
_AcdErpStatusRequestNodeId_Type = MacAddress
_AcdErpStatusRequestNodeId_Object = MibTableColumn
acdErpStatusRequestNodeId = _AcdErpStatusRequestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 6),
    _AcdErpStatusRequestNodeId_Type()
)
acdErpStatusRequestNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpStatusRequestNodeId.setStatus("current")
_AcdErpStatusRequest_Type = Unsigned32
_AcdErpStatusRequest_Object = MibTableColumn
acdErpStatusRequest = _AcdErpStatusRequest_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 7),
    _AcdErpStatusRequest_Type()
)
acdErpStatusRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpStatusRequest.setStatus("current")
_AcdErpPort0Status_Type = AcdErpPortStatusType
_AcdErpPort0Status_Object = MibTableColumn
acdErpPort0Status = _AcdErpPort0Status_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 8),
    _AcdErpPort0Status_Type()
)
acdErpPort0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpPort0Status.setStatus("current")
_AcdErpPort0State_Type = AcdErpPortStateType
_AcdErpPort0State_Object = MibTableColumn
acdErpPort0State = _AcdErpPort0State_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 9),
    _AcdErpPort0State_Type()
)
acdErpPort0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpPort0State.setStatus("current")
_AcdErpPort1Status_Type = AcdErpPortStatusType
_AcdErpPort1Status_Object = MibTableColumn
acdErpPort1Status = _AcdErpPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 10),
    _AcdErpPort1Status_Type()
)
acdErpPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpPort1Status.setStatus("current")
_AcdErpPort1State_Type = AcdErpPortStateType
_AcdErpPort1State_Object = MibTableColumn
acdErpPort1State = _AcdErpPort1State_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 3, 1, 1, 11),
    _AcdErpPort1State_Type()
)
acdErpPort1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpPort1State.setStatus("current")
_AcdErpVlanFdb_ObjectIdentity = ObjectIdentity
acdErpVlanFdb = _AcdErpVlanFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4)
)
_AcdErpVlanFdbTable_Object = MibTable
acdErpVlanFdbTable = _AcdErpVlanFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1)
)
if mibBuilder.loadTexts:
    acdErpVlanFdbTable.setStatus("current")
_AcdErpVlanFdbEntry_Object = MibTableRow
acdErpVlanFdbEntry = _AcdErpVlanFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1)
)
acdErpVlanFdbEntry.setIndexNames(
    (0, "ACD-ERP-MIB", "acdErpVlanFdbIdx"),
)
if mibBuilder.loadTexts:
    acdErpVlanFdbEntry.setStatus("current")
_AcdErpVlanFdbIdx_Type = Unsigned32
_AcdErpVlanFdbIdx_Object = MibTableColumn
acdErpVlanFdbIdx = _AcdErpVlanFdbIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 1),
    _AcdErpVlanFdbIdx_Type()
)
acdErpVlanFdbIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdErpVlanFdbIdx.setStatus("current")


class _AcdErpVlanFdbPort0Vids0to1023_Type(OctetString):
    """Custom type acdErpVlanFdbPort0Vids0to1023 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort0Vids0to1023_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort0Vids0to1023_Object = MibTableColumn
acdErpVlanFdbPort0Vids0to1023 = _AcdErpVlanFdbPort0Vids0to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 2),
    _AcdErpVlanFdbPort0Vids0to1023_Type()
)
acdErpVlanFdbPort0Vids0to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort0Vids0to1023.setStatus("current")


class _AcdErpVlanFdbPort0Vids1024to2047_Type(OctetString):
    """Custom type acdErpVlanFdbPort0Vids1024to2047 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort0Vids1024to2047_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort0Vids1024to2047_Object = MibTableColumn
acdErpVlanFdbPort0Vids1024to2047 = _AcdErpVlanFdbPort0Vids1024to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 3),
    _AcdErpVlanFdbPort0Vids1024to2047_Type()
)
acdErpVlanFdbPort0Vids1024to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort0Vids1024to2047.setStatus("current")


class _AcdErpVlanFdbPort0Vids2048to3071_Type(OctetString):
    """Custom type acdErpVlanFdbPort0Vids2048to3071 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort0Vids2048to3071_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort0Vids2048to3071_Object = MibTableColumn
acdErpVlanFdbPort0Vids2048to3071 = _AcdErpVlanFdbPort0Vids2048to3071_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 4),
    _AcdErpVlanFdbPort0Vids2048to3071_Type()
)
acdErpVlanFdbPort0Vids2048to3071.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort0Vids2048to3071.setStatus("current")


class _AcdErpVlanFdbPort0Vids3072to4095_Type(OctetString):
    """Custom type acdErpVlanFdbPort0Vids3072to4095 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort0Vids3072to4095_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort0Vids3072to4095_Object = MibTableColumn
acdErpVlanFdbPort0Vids3072to4095 = _AcdErpVlanFdbPort0Vids3072to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 5),
    _AcdErpVlanFdbPort0Vids3072to4095_Type()
)
acdErpVlanFdbPort0Vids3072to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort0Vids3072to4095.setStatus("current")


class _AcdErpVlanFdbPort1Vids0to1023_Type(OctetString):
    """Custom type acdErpVlanFdbPort1Vids0to1023 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort1Vids0to1023_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort1Vids0to1023_Object = MibTableColumn
acdErpVlanFdbPort1Vids0to1023 = _AcdErpVlanFdbPort1Vids0to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 6),
    _AcdErpVlanFdbPort1Vids0to1023_Type()
)
acdErpVlanFdbPort1Vids0to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort1Vids0to1023.setStatus("current")


class _AcdErpVlanFdbPort1Vids1024to2047_Type(OctetString):
    """Custom type acdErpVlanFdbPort1Vids1024to2047 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort1Vids1024to2047_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort1Vids1024to2047_Object = MibTableColumn
acdErpVlanFdbPort1Vids1024to2047 = _AcdErpVlanFdbPort1Vids1024to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 7),
    _AcdErpVlanFdbPort1Vids1024to2047_Type()
)
acdErpVlanFdbPort1Vids1024to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort1Vids1024to2047.setStatus("current")


class _AcdErpVlanFdbPort1Vids2048to3071_Type(OctetString):
    """Custom type acdErpVlanFdbPort1Vids2048to3071 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort1Vids2048to3071_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort1Vids2048to3071_Object = MibTableColumn
acdErpVlanFdbPort1Vids2048to3071 = _AcdErpVlanFdbPort1Vids2048to3071_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 8),
    _AcdErpVlanFdbPort1Vids2048to3071_Type()
)
acdErpVlanFdbPort1Vids2048to3071.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort1Vids2048to3071.setStatus("current")


class _AcdErpVlanFdbPort1Vids3072to4095_Type(OctetString):
    """Custom type acdErpVlanFdbPort1Vids3072to4095 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbPort1Vids3072to4095_Type.__name__ = "OctetString"
_AcdErpVlanFdbPort1Vids3072to4095_Object = MibTableColumn
acdErpVlanFdbPort1Vids3072to4095 = _AcdErpVlanFdbPort1Vids3072to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 9),
    _AcdErpVlanFdbPort1Vids3072to4095_Type()
)
acdErpVlanFdbPort1Vids3072to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbPort1Vids3072to4095.setStatus("current")


class _AcdErpVlanFdbFloodingVids0to1023_Type(OctetString):
    """Custom type acdErpVlanFdbFloodingVids0to1023 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFloodingVids0to1023_Type.__name__ = "OctetString"
_AcdErpVlanFdbFloodingVids0to1023_Object = MibTableColumn
acdErpVlanFdbFloodingVids0to1023 = _AcdErpVlanFdbFloodingVids0to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 10),
    _AcdErpVlanFdbFloodingVids0to1023_Type()
)
acdErpVlanFdbFloodingVids0to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFloodingVids0to1023.setStatus("current")


class _AcdErpVlanFdbFloodingVids1024to2047_Type(OctetString):
    """Custom type acdErpVlanFdbFloodingVids1024to2047 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFloodingVids1024to2047_Type.__name__ = "OctetString"
_AcdErpVlanFdbFloodingVids1024to2047_Object = MibTableColumn
acdErpVlanFdbFloodingVids1024to2047 = _AcdErpVlanFdbFloodingVids1024to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 11),
    _AcdErpVlanFdbFloodingVids1024to2047_Type()
)
acdErpVlanFdbFloodingVids1024to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFloodingVids1024to2047.setStatus("current")


class _AcdErpVlanFdbFloodingVids2048to3071_Type(OctetString):
    """Custom type acdErpVlanFdbFloodingVids2048to3071 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFloodingVids2048to3071_Type.__name__ = "OctetString"
_AcdErpVlanFdbFloodingVids2048to3071_Object = MibTableColumn
acdErpVlanFdbFloodingVids2048to3071 = _AcdErpVlanFdbFloodingVids2048to3071_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 12),
    _AcdErpVlanFdbFloodingVids2048to3071_Type()
)
acdErpVlanFdbFloodingVids2048to3071.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFloodingVids2048to3071.setStatus("current")


class _AcdErpVlanFdbFloodingVids3072to4095_Type(OctetString):
    """Custom type acdErpVlanFdbFloodingVids3072to4095 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFloodingVids3072to4095_Type.__name__ = "OctetString"
_AcdErpVlanFdbFloodingVids3072to4095_Object = MibTableColumn
acdErpVlanFdbFloodingVids3072to4095 = _AcdErpVlanFdbFloodingVids3072to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 13),
    _AcdErpVlanFdbFloodingVids3072to4095_Type()
)
acdErpVlanFdbFloodingVids3072to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFloodingVids3072to4095.setStatus("current")


class _AcdErpVlanFdbFlappingVids0to1023_Type(OctetString):
    """Custom type acdErpVlanFdbFlappingVids0to1023 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFlappingVids0to1023_Type.__name__ = "OctetString"
_AcdErpVlanFdbFlappingVids0to1023_Object = MibTableColumn
acdErpVlanFdbFlappingVids0to1023 = _AcdErpVlanFdbFlappingVids0to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 14),
    _AcdErpVlanFdbFlappingVids0to1023_Type()
)
acdErpVlanFdbFlappingVids0to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFlappingVids0to1023.setStatus("current")


class _AcdErpVlanFdbFlappingVids1024to2047_Type(OctetString):
    """Custom type acdErpVlanFdbFlappingVids1024to2047 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFlappingVids1024to2047_Type.__name__ = "OctetString"
_AcdErpVlanFdbFlappingVids1024to2047_Object = MibTableColumn
acdErpVlanFdbFlappingVids1024to2047 = _AcdErpVlanFdbFlappingVids1024to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 15),
    _AcdErpVlanFdbFlappingVids1024to2047_Type()
)
acdErpVlanFdbFlappingVids1024to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFlappingVids1024to2047.setStatus("current")


class _AcdErpVlanFdbFlappingVids2048to3071_Type(OctetString):
    """Custom type acdErpVlanFdbFlappingVids2048to3071 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFlappingVids2048to3071_Type.__name__ = "OctetString"
_AcdErpVlanFdbFlappingVids2048to3071_Object = MibTableColumn
acdErpVlanFdbFlappingVids2048to3071 = _AcdErpVlanFdbFlappingVids2048to3071_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 16),
    _AcdErpVlanFdbFlappingVids2048to3071_Type()
)
acdErpVlanFdbFlappingVids2048to3071.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFlappingVids2048to3071.setStatus("current")


class _AcdErpVlanFdbFlappingVids3072to4095_Type(OctetString):
    """Custom type acdErpVlanFdbFlappingVids3072to4095 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdErpVlanFdbFlappingVids3072to4095_Type.__name__ = "OctetString"
_AcdErpVlanFdbFlappingVids3072to4095_Object = MibTableColumn
acdErpVlanFdbFlappingVids3072to4095 = _AcdErpVlanFdbFlappingVids3072to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 0, 4, 1, 1, 17),
    _AcdErpVlanFdbFlappingVids3072to4095_Type()
)
acdErpVlanFdbFlappingVids3072to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdErpVlanFdbFlappingVids3072to4095.setStatus("current")
_AcdErpConformance_ObjectIdentity = ObjectIdentity
acdErpConformance = _AcdErpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1)
)
_AcdErpCompliances_ObjectIdentity = ObjectIdentity
acdErpCompliances = _AcdErpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1, 1)
)
_AcdErpGroups_ObjectIdentity = ObjectIdentity
acdErpGroups = _AcdErpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1, 2)
)

# Managed Objects groups

acdErpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1, 2, 1)
)
acdErpConfigGroup.setObjects(
      *(("ACD-ERP-MIB", "acdErpConfigRowStatus"),
        ("ACD-ERP-MIB", "acdErpConfigName"),
        ("ACD-ERP-MIB", "acdErpConfigRPLRole"),
        ("ACD-ERP-MIB", "acdErpConfigRPLPort"),
        ("ACD-ERP-MIB", "acdErpConfigHoldOffTimer"),
        ("ACD-ERP-MIB", "acdErpConfigRevertive"),
        ("ACD-ERP-MIB", "acdErpConfigGuardTimer"),
        ("ACD-ERP-MIB", "acdErpConfigWTRTimer"),
        ("ACD-ERP-MIB", "acdErpConfigMDLevel"),
        ("ACD-ERP-MIB", "acdErpConfigAPSVid"),
        ("ACD-ERP-MIB", "acdErpConfigVids0to1023"),
        ("ACD-ERP-MIB", "acdErpConfigVids1024to2047"),
        ("ACD-ERP-MIB", "acdErpConfigVids2048to3071"),
        ("ACD-ERP-MIB", "acdErpConfigVids3072to4095"),
        ("ACD-ERP-MIB", "acdErpConfigLAGPort"),
        ("ACD-ERP-MIB", "acdErpConfigMep0Idx"),
        ("ACD-ERP-MIB", "acdErpConfigMep1Idx"))
)
if mibBuilder.loadTexts:
    acdErpConfigGroup.setStatus("current")

acdErpCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1, 2, 2)
)
acdErpCounterGroup.setObjects(
      *(("ACD-ERP-MIB", "acdErpCounterPort0LocalClear"),
        ("ACD-ERP-MIB", "acdErpCounterPort0LocalFs"),
        ("ACD-ERP-MIB", "acdErpCounterPort0LocalSf"),
        ("ACD-ERP-MIB", "acdErpCounterPort0LocalMs"),
        ("ACD-ERP-MIB", "acdErpCounterPort0RxAps"),
        ("ACD-ERP-MIB", "acdErpCounterPort0RxApsFs"),
        ("ACD-ERP-MIB", "acdErpCounterPort0RxApsSf"),
        ("ACD-ERP-MIB", "acdErpCounterPort0RxApsMs"),
        ("ACD-ERP-MIB", "acdErpCounterPort0RxApsNrRb"),
        ("ACD-ERP-MIB", "acdErpCounterPort0RxApsNr"),
        ("ACD-ERP-MIB", "acdErpCounterPort0TxAps"),
        ("ACD-ERP-MIB", "acdErpCounterPort0TxApsFs"),
        ("ACD-ERP-MIB", "acdErpCounterPort0TxApsSf"),
        ("ACD-ERP-MIB", "acdErpCounterPort0TxApsMs"),
        ("ACD-ERP-MIB", "acdErpCounterPort0TxApsNrRb"),
        ("ACD-ERP-MIB", "acdErpCounterPort0TxApsNr"),
        ("ACD-ERP-MIB", "acdErpCounterPort0DropGuard"),
        ("ACD-ERP-MIB", "acdErpCounterPort0DropUnknown"),
        ("ACD-ERP-MIB", "acdErpCounterPort0DropMismatch"),
        ("ACD-ERP-MIB", "acdErpCounterPort1LocalClear"),
        ("ACD-ERP-MIB", "acdErpCounterPort1LocalFs"),
        ("ACD-ERP-MIB", "acdErpCounterPort1LocalSf"),
        ("ACD-ERP-MIB", "acdErpCounterPort1LocalMs"),
        ("ACD-ERP-MIB", "acdErpCounterPort1RxAps"),
        ("ACD-ERP-MIB", "acdErpCounterPort1RxApsFs"),
        ("ACD-ERP-MIB", "acdErpCounterPort1RxApsSf"),
        ("ACD-ERP-MIB", "acdErpCounterPort1RxApsMs"),
        ("ACD-ERP-MIB", "acdErpCounterPort1RxApsNrRb"),
        ("ACD-ERP-MIB", "acdErpCounterPort1RxApsNr"),
        ("ACD-ERP-MIB", "acdErpCounterPort1TxAps"),
        ("ACD-ERP-MIB", "acdErpCounterPort1TxApsFs"),
        ("ACD-ERP-MIB", "acdErpCounterPort1TxApsSf"),
        ("ACD-ERP-MIB", "acdErpCounterPort1TxApsMs"),
        ("ACD-ERP-MIB", "acdErpCounterPort1TxApsNrRb"),
        ("ACD-ERP-MIB", "acdErpCounterPort1TxApsNr"),
        ("ACD-ERP-MIB", "acdErpCounterPort1DropGuard"),
        ("ACD-ERP-MIB", "acdErpCounterPort1DropUnknown"),
        ("ACD-ERP-MIB", "acdErpCounterPort1DropMismatch"))
)
if mibBuilder.loadTexts:
    acdErpCounterGroup.setStatus("current")

acdErpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1, 2, 3)
)
acdErpStatusGroup.setObjects(
      *(("ACD-ERP-MIB", "acdErpStatusName"),
        ("ACD-ERP-MIB", "acdErpStatusNodeId"),
        ("ACD-ERP-MIB", "acdErpStatusRPLNodeId"),
        ("ACD-ERP-MIB", "acdErpStatusState"),
        ("ACD-ERP-MIB", "acdErpStatusRequestNodeId"),
        ("ACD-ERP-MIB", "acdErpStatusRequest"),
        ("ACD-ERP-MIB", "acdErpPort0Status"),
        ("ACD-ERP-MIB", "acdErpPort0State"),
        ("ACD-ERP-MIB", "acdErpPort1Status"),
        ("ACD-ERP-MIB", "acdErpPort1State"))
)
if mibBuilder.loadTexts:
    acdErpStatusGroup.setStatus("current")

acdErpVlanFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1, 2, 4)
)
acdErpVlanFdbGroup.setObjects(
      *(("ACD-ERP-MIB", "acdErpVlanFdbPort0Vids0to1023"),
        ("ACD-ERP-MIB", "acdErpVlanFdbPort0Vids1024to2047"),
        ("ACD-ERP-MIB", "acdErpVlanFdbPort0Vids2048to3071"),
        ("ACD-ERP-MIB", "acdErpVlanFdbPort0Vids3072to4095"),
        ("ACD-ERP-MIB", "acdErpVlanFdbPort1Vids0to1023"),
        ("ACD-ERP-MIB", "acdErpVlanFdbPort1Vids1024to2047"),
        ("ACD-ERP-MIB", "acdErpVlanFdbPort1Vids2048to3071"),
        ("ACD-ERP-MIB", "acdErpVlanFdbPort1Vids3072to4095"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFloodingVids0to1023"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFloodingVids1024to2047"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFloodingVids2048to3071"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFloodingVids3072to4095"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFlappingVids0to1023"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFlappingVids1024to2047"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFlappingVids2048to3071"),
        ("ACD-ERP-MIB", "acdErpVlanFdbFlappingVids3072to4095"))
)
if mibBuilder.loadTexts:
    acdErpVlanFdbGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdErpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdErpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-ERP-MIB",
    **{"AcdErpVlanType": AcdErpVlanType,
       "AcdErpPortStateType": AcdErpPortStateType,
       "AcdErpStateType": AcdErpStateType,
       "AcdErpPortStatusType": AcdErpPortStatusType,
       "acdErp": acdErp,
       "acdErpMIBObjects": acdErpMIBObjects,
       "acdErpConfig": acdErpConfig,
       "acdErpConfigTable": acdErpConfigTable,
       "acdErpConfigEntry": acdErpConfigEntry,
       "acdErpIndex": acdErpIndex,
       "acdErpConfigRowStatus": acdErpConfigRowStatus,
       "acdErpConfigName": acdErpConfigName,
       "acdErpConfigRPLRole": acdErpConfigRPLRole,
       "acdErpConfigRPLPort": acdErpConfigRPLPort,
       "acdErpConfigHoldOffTimer": acdErpConfigHoldOffTimer,
       "acdErpConfigRevertive": acdErpConfigRevertive,
       "acdErpConfigGuardTimer": acdErpConfigGuardTimer,
       "acdErpConfigWTRTimer": acdErpConfigWTRTimer,
       "acdErpConfigMDLevel": acdErpConfigMDLevel,
       "acdErpConfigAPSVid": acdErpConfigAPSVid,
       "acdErpConfigVids0to1023": acdErpConfigVids0to1023,
       "acdErpConfigVids1024to2047": acdErpConfigVids1024to2047,
       "acdErpConfigVids2048to3071": acdErpConfigVids2048to3071,
       "acdErpConfigVids3072to4095": acdErpConfigVids3072to4095,
       "acdErpConfigLAGPort": acdErpConfigLAGPort,
       "acdErpConfigMep0Idx": acdErpConfigMep0Idx,
       "acdErpConfigMep1Idx": acdErpConfigMep1Idx,
       "acdErpCounter": acdErpCounter,
       "acdErpCounterTable": acdErpCounterTable,
       "acdErpCounterEntry": acdErpCounterEntry,
       "acdErpCounterIndex": acdErpCounterIndex,
       "acdErpCounterPort0LocalClear": acdErpCounterPort0LocalClear,
       "acdErpCounterPort0LocalFs": acdErpCounterPort0LocalFs,
       "acdErpCounterPort0LocalSf": acdErpCounterPort0LocalSf,
       "acdErpCounterPort0LocalMs": acdErpCounterPort0LocalMs,
       "acdErpCounterPort0RxAps": acdErpCounterPort0RxAps,
       "acdErpCounterPort0RxApsFs": acdErpCounterPort0RxApsFs,
       "acdErpCounterPort0RxApsSf": acdErpCounterPort0RxApsSf,
       "acdErpCounterPort0RxApsMs": acdErpCounterPort0RxApsMs,
       "acdErpCounterPort0RxApsNrRb": acdErpCounterPort0RxApsNrRb,
       "acdErpCounterPort0RxApsNr": acdErpCounterPort0RxApsNr,
       "acdErpCounterPort0TxAps": acdErpCounterPort0TxAps,
       "acdErpCounterPort0TxApsFs": acdErpCounterPort0TxApsFs,
       "acdErpCounterPort0TxApsSf": acdErpCounterPort0TxApsSf,
       "acdErpCounterPort0TxApsMs": acdErpCounterPort0TxApsMs,
       "acdErpCounterPort0TxApsNrRb": acdErpCounterPort0TxApsNrRb,
       "acdErpCounterPort0TxApsNr": acdErpCounterPort0TxApsNr,
       "acdErpCounterPort0DropGuard": acdErpCounterPort0DropGuard,
       "acdErpCounterPort0DropUnknown": acdErpCounterPort0DropUnknown,
       "acdErpCounterPort0DropMismatch": acdErpCounterPort0DropMismatch,
       "acdErpCounterPort1LocalClear": acdErpCounterPort1LocalClear,
       "acdErpCounterPort1LocalFs": acdErpCounterPort1LocalFs,
       "acdErpCounterPort1LocalSf": acdErpCounterPort1LocalSf,
       "acdErpCounterPort1LocalMs": acdErpCounterPort1LocalMs,
       "acdErpCounterPort1RxAps": acdErpCounterPort1RxAps,
       "acdErpCounterPort1RxApsFs": acdErpCounterPort1RxApsFs,
       "acdErpCounterPort1RxApsSf": acdErpCounterPort1RxApsSf,
       "acdErpCounterPort1RxApsMs": acdErpCounterPort1RxApsMs,
       "acdErpCounterPort1RxApsNrRb": acdErpCounterPort1RxApsNrRb,
       "acdErpCounterPort1RxApsNr": acdErpCounterPort1RxApsNr,
       "acdErpCounterPort1TxAps": acdErpCounterPort1TxAps,
       "acdErpCounterPort1TxApsFs": acdErpCounterPort1TxApsFs,
       "acdErpCounterPort1TxApsSf": acdErpCounterPort1TxApsSf,
       "acdErpCounterPort1TxApsMs": acdErpCounterPort1TxApsMs,
       "acdErpCounterPort1TxApsNrRb": acdErpCounterPort1TxApsNrRb,
       "acdErpCounterPort1TxApsNr": acdErpCounterPort1TxApsNr,
       "acdErpCounterPort1DropGuard": acdErpCounterPort1DropGuard,
       "acdErpCounterPort1DropUnknown": acdErpCounterPort1DropUnknown,
       "acdErpCounterPort1DropMismatch": acdErpCounterPort1DropMismatch,
       "acdErpStatus": acdErpStatus,
       "acdErpStatusTable": acdErpStatusTable,
       "acdErpStatusEntry": acdErpStatusEntry,
       "acdErpStatusIdx": acdErpStatusIdx,
       "acdErpStatusName": acdErpStatusName,
       "acdErpStatusNodeId": acdErpStatusNodeId,
       "acdErpStatusRPLNodeId": acdErpStatusRPLNodeId,
       "acdErpStatusState": acdErpStatusState,
       "acdErpStatusRequestNodeId": acdErpStatusRequestNodeId,
       "acdErpStatusRequest": acdErpStatusRequest,
       "acdErpPort0Status": acdErpPort0Status,
       "acdErpPort0State": acdErpPort0State,
       "acdErpPort1Status": acdErpPort1Status,
       "acdErpPort1State": acdErpPort1State,
       "acdErpVlanFdb": acdErpVlanFdb,
       "acdErpVlanFdbTable": acdErpVlanFdbTable,
       "acdErpVlanFdbEntry": acdErpVlanFdbEntry,
       "acdErpVlanFdbIdx": acdErpVlanFdbIdx,
       "acdErpVlanFdbPort0Vids0to1023": acdErpVlanFdbPort0Vids0to1023,
       "acdErpVlanFdbPort0Vids1024to2047": acdErpVlanFdbPort0Vids1024to2047,
       "acdErpVlanFdbPort0Vids2048to3071": acdErpVlanFdbPort0Vids2048to3071,
       "acdErpVlanFdbPort0Vids3072to4095": acdErpVlanFdbPort0Vids3072to4095,
       "acdErpVlanFdbPort1Vids0to1023": acdErpVlanFdbPort1Vids0to1023,
       "acdErpVlanFdbPort1Vids1024to2047": acdErpVlanFdbPort1Vids1024to2047,
       "acdErpVlanFdbPort1Vids2048to3071": acdErpVlanFdbPort1Vids2048to3071,
       "acdErpVlanFdbPort1Vids3072to4095": acdErpVlanFdbPort1Vids3072to4095,
       "acdErpVlanFdbFloodingVids0to1023": acdErpVlanFdbFloodingVids0to1023,
       "acdErpVlanFdbFloodingVids1024to2047": acdErpVlanFdbFloodingVids1024to2047,
       "acdErpVlanFdbFloodingVids2048to3071": acdErpVlanFdbFloodingVids2048to3071,
       "acdErpVlanFdbFloodingVids3072to4095": acdErpVlanFdbFloodingVids3072to4095,
       "acdErpVlanFdbFlappingVids0to1023": acdErpVlanFdbFlappingVids0to1023,
       "acdErpVlanFdbFlappingVids1024to2047": acdErpVlanFdbFlappingVids1024to2047,
       "acdErpVlanFdbFlappingVids2048to3071": acdErpVlanFdbFlappingVids2048to3071,
       "acdErpVlanFdbFlappingVids3072to4095": acdErpVlanFdbFlappingVids3072to4095,
       "acdErpConformance": acdErpConformance,
       "acdErpCompliances": acdErpCompliances,
       "acdErpCompliance": acdErpCompliance,
       "acdErpGroups": acdErpGroups,
       "acdErpConfigGroup": acdErpConfigGroup,
       "acdErpCounterGroup": acdErpCounterGroup,
       "acdErpStatusGroup": acdErpStatusGroup,
       "acdErpVlanFdbGroup": acdErpVlanFdbGroup}
)
