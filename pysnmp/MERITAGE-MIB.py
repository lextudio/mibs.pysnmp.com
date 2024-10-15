# SNMP MIB module (MERITAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERITAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:58 2024
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

_Meritage_ObjectIdentity = ObjectIdentity
meritage = _Meritage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 32)
)
_MeritageBase_ObjectIdentity = ObjectIdentity
meritageBase = _MeritageBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 32, 1)
)
_MeritageBaseLEDs_Type = OctetString
_MeritageBaseLEDs_Object = MibScalar
meritageBaseLEDs = _MeritageBaseLEDs_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 1),
    _MeritageBaseLEDs_Type()
)
meritageBaseLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseLEDs.setStatus("mandatory")


class _MeritageBaseTemperatureExceed_Type(Integer32):
    """Custom type meritageBaseTemperatureExceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exceeded", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_MeritageBaseTemperatureExceed_Type.__name__ = "Integer32"
_MeritageBaseTemperatureExceed_Object = MibScalar
meritageBaseTemperatureExceed = _MeritageBaseTemperatureExceed_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 2),
    _MeritageBaseTemperatureExceed_Type()
)
meritageBaseTemperatureExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseTemperatureExceed.setStatus("mandatory")


class _MeritageBaseXswitchConfiguration_Type(Integer32):
    """Custom type meritageBaseXswitchConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notSupported", 255),
          ("separated", 2))
    )


_MeritageBaseXswitchConfiguration_Type.__name__ = "Integer32"
_MeritageBaseXswitchConfiguration_Object = MibScalar
meritageBaseXswitchConfiguration = _MeritageBaseXswitchConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 3),
    _MeritageBaseXswitchConfiguration_Type()
)
meritageBaseXswitchConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseXswitchConfiguration.setStatus("mandatory")
_MeritageBaseFaultMask_Type = OctetString
_MeritageBaseFaultMask_Object = MibScalar
meritageBaseFaultMask = _MeritageBaseFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 4),
    _MeritageBaseFaultMask_Type()
)
meritageBaseFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseFaultMask.setStatus("mandatory")
_MeritageBaseFanTable_Object = MibTable
meritageBaseFanTable = _MeritageBaseFanTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 5)
)
if mibBuilder.loadTexts:
    meritageBaseFanTable.setStatus("mandatory")
_MeritageBaseFanEntry_Object = MibTableRow
meritageBaseFanEntry = _MeritageBaseFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 5, 1)
)
meritageBaseFanEntry.setIndexNames(
    (0, "MERITAGE-MIB", "meritageBaseFanId"),
)
if mibBuilder.loadTexts:
    meritageBaseFanEntry.setStatus("mandatory")


class _MeritageBaseFanId_Type(Integer32):
    """Custom type meritageBaseFanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MeritageBaseFanId_Type.__name__ = "Integer32"
_MeritageBaseFanId_Object = MibTableColumn
meritageBaseFanId = _MeritageBaseFanId_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 5, 1, 1),
    _MeritageBaseFanId_Type()
)
meritageBaseFanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseFanId.setStatus("mandatory")


class _MeritageBaseFanActivityStatus_Type(Integer32):
    """Custom type meritageBaseFanActivityStatus based on Integer32"""
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
          ("failed", 2),
          ("none", 3))
    )


_MeritageBaseFanActivityStatus_Type.__name__ = "Integer32"
_MeritageBaseFanActivityStatus_Object = MibTableColumn
meritageBaseFanActivityStatus = _MeritageBaseFanActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 5, 1, 2),
    _MeritageBaseFanActivityStatus_Type()
)
meritageBaseFanActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseFanActivityStatus.setStatus("mandatory")
_MeritageBasePSUTable_Object = MibTable
meritageBasePSUTable = _MeritageBasePSUTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 6)
)
if mibBuilder.loadTexts:
    meritageBasePSUTable.setStatus("mandatory")
_MeritageBasePSUEntry_Object = MibTableRow
meritageBasePSUEntry = _MeritageBasePSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1)
)
meritageBasePSUEntry.setIndexNames(
    (0, "MERITAGE-MIB", "meritageBasePSUId"),
)
if mibBuilder.loadTexts:
    meritageBasePSUEntry.setStatus("mandatory")


class _MeritageBasePSUId_Type(Integer32):
    """Custom type meritageBasePSUId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MeritageBasePSUId_Type.__name__ = "Integer32"
_MeritageBasePSUId_Object = MibTableColumn
meritageBasePSUId = _MeritageBasePSUId_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 1),
    _MeritageBasePSUId_Type()
)
meritageBasePSUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBasePSUId.setStatus("mandatory")


class _MeritageBasePSUType_Type(Integer32):
    """Custom type meritageBasePSUType based on Integer32"""
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
        *(("m-ps1250", 2),
          ("m-ps500", 1),
          ("m-ps800", 3),
          ("m-ps800-dc", 4),
          ("notSupported", 255))
    )


_MeritageBasePSUType_Type.__name__ = "Integer32"
_MeritageBasePSUType_Object = MibTableColumn
meritageBasePSUType = _MeritageBasePSUType_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 2),
    _MeritageBasePSUType_Type()
)
meritageBasePSUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBasePSUType.setStatus("mandatory")


class _MeritageBasePSUHWVersion_Type(DisplayString):
    """Custom type meritageBasePSUHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_MeritageBasePSUHWVersion_Type.__name__ = "DisplayString"
_MeritageBasePSUHWVersion_Object = MibTableColumn
meritageBasePSUHWVersion = _MeritageBasePSUHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 3),
    _MeritageBasePSUHWVersion_Type()
)
meritageBasePSUHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBasePSUHWVersion.setStatus("mandatory")
_MeritageBasePSURatedPower_Type = Integer32
_MeritageBasePSURatedPower_Object = MibTableColumn
meritageBasePSURatedPower = _MeritageBasePSURatedPower_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 4),
    _MeritageBasePSURatedPower_Type()
)
meritageBasePSURatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBasePSURatedPower.setStatus("mandatory")


class _MeritageBasePSUActivityStatus_Type(Integer32):
    """Custom type meritageBasePSUActivityStatus based on Integer32"""
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
          ("failed", 2),
          ("none", 3))
    )


_MeritageBasePSUActivityStatus_Type.__name__ = "Integer32"
_MeritageBasePSUActivityStatus_Object = MibTableColumn
meritageBasePSUActivityStatus = _MeritageBasePSUActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 5),
    _MeritageBasePSUActivityStatus_Type()
)
meritageBasePSUActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBasePSUActivityStatus.setStatus("mandatory")


class _MeritageBaseUpBckplnConfiguration_Type(Integer32):
    """Custom type meritageBaseUpBckplnConfiguration based on Integer32"""
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
        *(("dualDomain", 2),
          ("notInstalled", 3),
          ("notSupported", 255),
          ("singleDomain", 1))
    )


_MeritageBaseUpBckplnConfiguration_Type.__name__ = "Integer32"
_MeritageBaseUpBckplnConfiguration_Object = MibScalar
meritageBaseUpBckplnConfiguration = _MeritageBaseUpBckplnConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 7),
    _MeritageBaseUpBckplnConfiguration_Type()
)
meritageBaseUpBckplnConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseUpBckplnConfiguration.setStatus("mandatory")
_MeritageBaseUpBckplnConfigurationSymbol_Type = DisplayString
_MeritageBaseUpBckplnConfigurationSymbol_Object = MibScalar
meritageBaseUpBckplnConfigurationSymbol = _MeritageBaseUpBckplnConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 1, 8),
    _MeritageBaseUpBckplnConfigurationSymbol_Type()
)
meritageBaseUpBckplnConfigurationSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageBaseUpBckplnConfigurationSymbol.setStatus("mandatory")
_MeritageMSPV_ObjectIdentity = ObjectIdentity
meritageMSPV = _MeritageMSPV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 32, 2)
)


class _MeritageMSPVBackupStatus_Type(Integer32):
    """Custom type meritageMSPVBackupStatus based on Integer32"""
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
        *(("dormant", 1),
          ("failed", 2),
          ("none", 3),
          ("notSupported", 255))
    )


_MeritageMSPVBackupStatus_Type.__name__ = "Integer32"
_MeritageMSPVBackupStatus_Object = MibScalar
meritageMSPVBackupStatus = _MeritageMSPVBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 2, 1),
    _MeritageMSPVBackupStatus_Type()
)
meritageMSPVBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageMSPVBackupStatus.setStatus("mandatory")


class _MeritageMSPVMainPosition_Type(Integer32):
    """Custom type meritageMSPVMainPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mMSPV1", 1),
          ("mMSPV2", 2),
          ("notSupported", 255))
    )


_MeritageMSPVMainPosition_Type.__name__ = "Integer32"
_MeritageMSPVMainPosition_Object = MibScalar
meritageMSPVMainPosition = _MeritageMSPVMainPosition_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 2, 2),
    _MeritageMSPVMainPosition_Type()
)
meritageMSPVMainPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageMSPVMainPosition.setStatus("mandatory")
_MeritageGroup_ObjectIdentity = ObjectIdentity
meritageGroup = _MeritageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 32, 3)
)
_MeritageGroupTable_Object = MibTable
meritageGroupTable = _MeritageGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 3, 1)
)
if mibBuilder.loadTexts:
    meritageGroupTable.setStatus("mandatory")
_MeritageGroupEntry_Object = MibTableRow
meritageGroupEntry = _MeritageGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1)
)
meritageGroupEntry.setIndexNames(
    (0, "MERITAGE-MIB", "meritageGroupIndex"),
)
if mibBuilder.loadTexts:
    meritageGroupEntry.setStatus("mandatory")
_MeritageGroupIndex_Type = Integer32
_MeritageGroupIndex_Object = MibTableColumn
meritageGroupIndex = _MeritageGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1, 1),
    _MeritageGroupIndex_Type()
)
meritageGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageGroupIndex.setStatus("mandatory")


class _MeritageGroupTempExceed_Type(Integer32):
    """Custom type meritageGroupTempExceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exceeded", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_MeritageGroupTempExceed_Type.__name__ = "Integer32"
_MeritageGroupTempExceed_Object = MibTableColumn
meritageGroupTempExceed = _MeritageGroupTempExceed_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1, 2),
    _MeritageGroupTempExceed_Type()
)
meritageGroupTempExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageGroupTempExceed.setStatus("mandatory")
_MeritageGroupLEDsMap_Type = OctetString
_MeritageGroupLEDsMap_Object = MibTableColumn
meritageGroupLEDsMap = _MeritageGroupLEDsMap_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1, 3),
    _MeritageGroupLEDsMap_Type()
)
meritageGroupLEDsMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageGroupLEDsMap.setStatus("mandatory")
_MeritageClock_ObjectIdentity = ObjectIdentity
meritageClock = _MeritageClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 32, 4)
)


class _MeritageClockAdminStatus_Type(Integer32):
    """Custom type meritageClockAdminStatus based on Integer32"""
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


_MeritageClockAdminStatus_Type.__name__ = "Integer32"
_MeritageClockAdminStatus_Object = MibScalar
meritageClockAdminStatus = _MeritageClockAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 4, 1),
    _MeritageClockAdminStatus_Type()
)
meritageClockAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meritageClockAdminStatus.setStatus("mandatory")


class _MeritageClockReset_Type(Integer32):
    """Custom type meritageClockReset based on Integer32"""
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


_MeritageClockReset_Type.__name__ = "Integer32"
_MeritageClockReset_Object = MibScalar
meritageClockReset = _MeritageClockReset_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 4, 2),
    _MeritageClockReset_Type()
)
meritageClockReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meritageClockReset.setStatus("mandatory")
_MeritageClockWTR_Type = Integer32
_MeritageClockWTR_Object = MibScalar
meritageClockWTR = _MeritageClockWTR_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 4, 3),
    _MeritageClockWTR_Type()
)
meritageClockWTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meritageClockWTR.setStatus("mandatory")


class _MeritageClockStatus_Type(Integer32):
    """Custom type meritageClockStatus based on Integer32"""
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
        *(("freeRunning", 3),
          ("holdover", 2),
          ("internal", 4),
          ("locked", 1))
    )


_MeritageClockStatus_Type.__name__ = "Integer32"
_MeritageClockStatus_Object = MibScalar
meritageClockStatus = _MeritageClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 4, 4),
    _MeritageClockStatus_Type()
)
meritageClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageClockStatus.setStatus("mandatory")
_MeritageClockCurrentSource_Type = DisplayString
_MeritageClockCurrentSource_Object = MibScalar
meritageClockCurrentSource = _MeritageClockCurrentSource_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 4, 5),
    _MeritageClockCurrentSource_Type()
)
meritageClockCurrentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageClockCurrentSource.setStatus("mandatory")
_MeritageClockSource_ObjectIdentity = ObjectIdentity
meritageClockSource = _MeritageClockSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 32, 5)
)
_MeritageClockSourceTable_Object = MibTable
meritageClockSourceTable = _MeritageClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 5, 1)
)
if mibBuilder.loadTexts:
    meritageClockSourceTable.setStatus("mandatory")
_MeritageClockSourceEntry_Object = MibTableRow
meritageClockSourceEntry = _MeritageClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1)
)
meritageClockSourceEntry.setIndexNames(
    (0, "MERITAGE-MIB", "meritageClockSourceIndex"),
)
if mibBuilder.loadTexts:
    meritageClockSourceEntry.setStatus("mandatory")
_MeritageClockSourceIndex_Type = Integer32
_MeritageClockSourceIndex_Object = MibTableColumn
meritageClockSourceIndex = _MeritageClockSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 1),
    _MeritageClockSourceIndex_Type()
)
meritageClockSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageClockSourceIndex.setStatus("mandatory")


class _MeritageClockSourceStatus_Type(Integer32):
    """Custom type meritageClockSourceStatus based on Integer32"""
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
        *(("failed", 3),
          ("los", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_MeritageClockSourceStatus_Type.__name__ = "Integer32"
_MeritageClockSourceStatus_Object = MibTableColumn
meritageClockSourceStatus = _MeritageClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 2),
    _MeritageClockSourceStatus_Type()
)
meritageClockSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meritageClockSourceStatus.setStatus("mandatory")


class _MeritageClockSourcePriority_Type(Integer32):
    """Custom type meritageClockSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MeritageClockSourcePriority_Type.__name__ = "Integer32"
_MeritageClockSourcePriority_Object = MibTableColumn
meritageClockSourcePriority = _MeritageClockSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 3),
    _MeritageClockSourcePriority_Type()
)
meritageClockSourcePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meritageClockSourcePriority.setStatus("mandatory")
_MeritageClockSourceConfigPort_Type = DisplayString
_MeritageClockSourceConfigPort_Object = MibTableColumn
meritageClockSourceConfigPort = _MeritageClockSourceConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 4),
    _MeritageClockSourceConfigPort_Type()
)
meritageClockSourceConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meritageClockSourceConfigPort.setStatus("mandatory")


class _MeritageClockSourceFraming_Type(Integer32):
    """Custom type meritageClockSourceFraming based on Integer32"""
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
        *(("ds1-esf", 4),
          ("ds1-sf", 3),
          ("e1-framed", 1),
          ("e1-unframed", 2),
          ("notSupported", 255))
    )


_MeritageClockSourceFraming_Type.__name__ = "Integer32"
_MeritageClockSourceFraming_Object = MibTableColumn
meritageClockSourceFraming = _MeritageClockSourceFraming_Object(
    (1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 5),
    _MeritageClockSourceFraming_Type()
)
meritageClockSourceFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meritageClockSourceFraming.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERITAGE-MIB",
    **{"meritage": meritage,
       "meritageBase": meritageBase,
       "meritageBaseLEDs": meritageBaseLEDs,
       "meritageBaseTemperatureExceed": meritageBaseTemperatureExceed,
       "meritageBaseXswitchConfiguration": meritageBaseXswitchConfiguration,
       "meritageBaseFaultMask": meritageBaseFaultMask,
       "meritageBaseFanTable": meritageBaseFanTable,
       "meritageBaseFanEntry": meritageBaseFanEntry,
       "meritageBaseFanId": meritageBaseFanId,
       "meritageBaseFanActivityStatus": meritageBaseFanActivityStatus,
       "meritageBasePSUTable": meritageBasePSUTable,
       "meritageBasePSUEntry": meritageBasePSUEntry,
       "meritageBasePSUId": meritageBasePSUId,
       "meritageBasePSUType": meritageBasePSUType,
       "meritageBasePSUHWVersion": meritageBasePSUHWVersion,
       "meritageBasePSURatedPower": meritageBasePSURatedPower,
       "meritageBasePSUActivityStatus": meritageBasePSUActivityStatus,
       "meritageBaseUpBckplnConfiguration": meritageBaseUpBckplnConfiguration,
       "meritageBaseUpBckplnConfigurationSymbol": meritageBaseUpBckplnConfigurationSymbol,
       "meritageMSPV": meritageMSPV,
       "meritageMSPVBackupStatus": meritageMSPVBackupStatus,
       "meritageMSPVMainPosition": meritageMSPVMainPosition,
       "meritageGroup": meritageGroup,
       "meritageGroupTable": meritageGroupTable,
       "meritageGroupEntry": meritageGroupEntry,
       "meritageGroupIndex": meritageGroupIndex,
       "meritageGroupTempExceed": meritageGroupTempExceed,
       "meritageGroupLEDsMap": meritageGroupLEDsMap,
       "meritageClock": meritageClock,
       "meritageClockAdminStatus": meritageClockAdminStatus,
       "meritageClockReset": meritageClockReset,
       "meritageClockWTR": meritageClockWTR,
       "meritageClockStatus": meritageClockStatus,
       "meritageClockCurrentSource": meritageClockCurrentSource,
       "meritageClockSource": meritageClockSource,
       "meritageClockSourceTable": meritageClockSourceTable,
       "meritageClockSourceEntry": meritageClockSourceEntry,
       "meritageClockSourceIndex": meritageClockSourceIndex,
       "meritageClockSourceStatus": meritageClockSourceStatus,
       "meritageClockSourcePriority": meritageClockSourcePriority,
       "meritageClockSourceConfigPort": meritageClockSourceConfigPort,
       "meritageClockSourceFraming": meritageClockSourceFraming}
)
