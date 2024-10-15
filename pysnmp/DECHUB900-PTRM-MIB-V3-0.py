# SNMP MIB module (DECHUB900-PTRM-MIB-V3-0) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECHUB900-PTRM-MIB-V3-0
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:42 2024
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
 enterprises,
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
    "enterprises",
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

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecHub900_ObjectIdentity = ObjectIdentity
decHub900 = _DecHub900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11)
)
_Ptrm_ObjectIdentity = ObjectIdentity
ptrm = _Ptrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3)
)
_PtrmBase_ObjectIdentity = ObjectIdentity
ptrmBase = _PtrmBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 1)
)


class _PtrmBaseForceSpeed_Type(Integer32):
    """Custom type ptrmBaseForceSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("force-16Mbps", 3),
          ("force-4Mbps", 2),
          ("notForced", 1))
    )


_PtrmBaseForceSpeed_Type.__name__ = "Integer32"
_PtrmBaseForceSpeed_Object = MibScalar
ptrmBaseForceSpeed = _PtrmBaseForceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 1, 2),
    _PtrmBaseForceSpeed_Type()
)
ptrmBaseForceSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptrmBaseForceSpeed.setStatus("mandatory")


class _PtrmBaseSpeed_Type(Integer32):
    """Custom type ptrmBaseSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoBauding", 1),
          ("speed-16Mbps", 3),
          ("speed-4Mbps", 2))
    )


_PtrmBaseSpeed_Type.__name__ = "Integer32"
_PtrmBaseSpeed_Object = MibScalar
ptrmBaseSpeed = _PtrmBaseSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 1, 3),
    _PtrmBaseSpeed_Type()
)
ptrmBaseSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmBaseSpeed.setStatus("mandatory")


class _PtrmBaseNumLobes_Type(Integer32):
    """Custom type ptrmBaseNumLobes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PtrmBaseNumLobes_Type.__name__ = "Integer32"
_PtrmBaseNumLobes_Object = MibScalar
ptrmBaseNumLobes = _PtrmBaseNumLobes_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 1, 4),
    _PtrmBaseNumLobes_Type()
)
ptrmBaseNumLobes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmBaseNumLobes.setStatus("mandatory")
_PtrmTrunkTable_Object = MibTable
ptrmTrunkTable = _PtrmTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2)
)
if mibBuilder.loadTexts:
    ptrmTrunkTable.setStatus("mandatory")
_PtrmTrunkEntry_Object = MibTableRow
ptrmTrunkEntry = _PtrmTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1)
)
ptrmTrunkEntry.setIndexNames(
    (0, "DECHUB900-PTRM-MIB-V3-0", "ptrmTrunkType"),
)
if mibBuilder.loadTexts:
    ptrmTrunkEntry.setStatus("mandatory")


class _PtrmTrunkType_Type(Integer32):
    """Custom type ptrmTrunkType based on Integer32"""
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
        *(("copperRingIn", 1),
          ("copperRingOut", 2),
          ("fiberRingIn", 5),
          ("fiberRingOut", 6),
          ("hubA", 3),
          ("hubB", 4))
    )


_PtrmTrunkType_Type.__name__ = "Integer32"
_PtrmTrunkType_Object = MibTableColumn
ptrmTrunkType = _PtrmTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 1),
    _PtrmTrunkType_Type()
)
ptrmTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmTrunkType.setStatus("mandatory")


class _PtrmTrunkOperStatus_Type(Integer32):
    """Custom type ptrmTrunkOperStatus based on Integer32"""
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
        *(("badSpeed", 4),
          ("inserted", 1),
          ("notPresent", 3),
          ("wrapped", 2))
    )


_PtrmTrunkOperStatus_Type.__name__ = "Integer32"
_PtrmTrunkOperStatus_Object = MibTableColumn
ptrmTrunkOperStatus = _PtrmTrunkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 2),
    _PtrmTrunkOperStatus_Type()
)
ptrmTrunkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmTrunkOperStatus.setStatus("mandatory")


class _PtrmTrunkAdminStatus_Type(Integer32):
    """Custom type ptrmTrunkAdminStatus based on Integer32"""
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


_PtrmTrunkAdminStatus_Type.__name__ = "Integer32"
_PtrmTrunkAdminStatus_Object = MibTableColumn
ptrmTrunkAdminStatus = _PtrmTrunkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 3),
    _PtrmTrunkAdminStatus_Type()
)
ptrmTrunkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptrmTrunkAdminStatus.setStatus("mandatory")


class _PtrmTrunkMedia_Type(Integer32):
    """Custom type ptrmTrunkMedia based on Integer32"""
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
        *(("fiberMedia", 5),
          ("hubDirect", 6),
          ("hubTCU", 7),
          ("ibmMedia", 4),
          ("otherMedia", 1),
          ("stpMedia", 3),
          ("utpMedia", 2))
    )


_PtrmTrunkMedia_Type.__name__ = "Integer32"
_PtrmTrunkMedia_Object = MibTableColumn
ptrmTrunkMedia = _PtrmTrunkMedia_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 4),
    _PtrmTrunkMedia_Type()
)
ptrmTrunkMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmTrunkMedia.setStatus("mandatory")


class _PtrmTrunkAutoWrapEnable_Type(Integer32):
    """Custom type ptrmTrunkAutoWrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("off", 2),
          ("on", 1))
    )


_PtrmTrunkAutoWrapEnable_Type.__name__ = "Integer32"
_PtrmTrunkAutoWrapEnable_Object = MibTableColumn
ptrmTrunkAutoWrapEnable = _PtrmTrunkAutoWrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 5),
    _PtrmTrunkAutoWrapEnable_Type()
)
ptrmTrunkAutoWrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptrmTrunkAutoWrapEnable.setStatus("mandatory")


class _PtrmTrunkAutoPartitionStatus_Type(Integer32):
    """Custom type ptrmTrunkAutoPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_PtrmTrunkAutoPartitionStatus_Type.__name__ = "Integer32"
_PtrmTrunkAutoPartitionStatus_Object = MibTableColumn
ptrmTrunkAutoPartitionStatus = _PtrmTrunkAutoPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 6),
    _PtrmTrunkAutoPartitionStatus_Type()
)
ptrmTrunkAutoPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmTrunkAutoPartitionStatus.setStatus("mandatory")


class _PtrmTrunkDetectedSpeed_Type(Integer32):
    """Custom type ptrmTrunkDetectedSpeed based on Integer32"""
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
        *(("invalid", 1),
          ("notApplicable", 4),
          ("speed-16Mbps", 3),
          ("speed-4Mbps", 2))
    )


_PtrmTrunkDetectedSpeed_Type.__name__ = "Integer32"
_PtrmTrunkDetectedSpeed_Object = MibTableColumn
ptrmTrunkDetectedSpeed = _PtrmTrunkDetectedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 7),
    _PtrmTrunkDetectedSpeed_Type()
)
ptrmTrunkDetectedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmTrunkDetectedSpeed.setStatus("mandatory")


class _PtrmTrunkPhantomDrive_Type(Integer32):
    """Custom type ptrmTrunkPhantomDrive based on Integer32"""
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
        *(("driveReceive", 3),
          ("noDrive", 2),
          ("notApplicable", 1),
          ("wireFault", 4))
    )


_PtrmTrunkPhantomDrive_Type.__name__ = "Integer32"
_PtrmTrunkPhantomDrive_Object = MibTableColumn
ptrmTrunkPhantomDrive = _PtrmTrunkPhantomDrive_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 8),
    _PtrmTrunkPhantomDrive_Type()
)
ptrmTrunkPhantomDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmTrunkPhantomDrive.setStatus("mandatory")


class _PtrmTrunkPhantomDetect_Type(Integer32):
    """Custom type ptrmTrunkPhantomDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detectPhantom", 3),
          ("noDetectPhantom", 2),
          ("notApplicable", 1))
    )


_PtrmTrunkPhantomDetect_Type.__name__ = "Integer32"
_PtrmTrunkPhantomDetect_Object = MibTableColumn
ptrmTrunkPhantomDetect = _PtrmTrunkPhantomDetect_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 2, 1, 9),
    _PtrmTrunkPhantomDetect_Type()
)
ptrmTrunkPhantomDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmTrunkPhantomDetect.setStatus("mandatory")
_PtrmLobeTable_Object = MibTable
ptrmLobeTable = _PtrmLobeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3)
)
if mibBuilder.loadTexts:
    ptrmLobeTable.setStatus("mandatory")
_PtrmLobeEntry_Object = MibTableRow
ptrmLobeEntry = _PtrmLobeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1)
)
ptrmLobeEntry.setIndexNames(
    (0, "DECHUB900-PTRM-MIB-V3-0", "ptrmLobeIndex"),
)
if mibBuilder.loadTexts:
    ptrmLobeEntry.setStatus("mandatory")


class _PtrmLobeIndex_Type(Integer32):
    """Custom type ptrmLobeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PtrmLobeIndex_Type.__name__ = "Integer32"
_PtrmLobeIndex_Object = MibTableColumn
ptrmLobeIndex = _PtrmLobeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 1),
    _PtrmLobeIndex_Type()
)
ptrmLobeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmLobeIndex.setStatus("mandatory")


class _PtrmLobeOperStatus_Type(Integer32):
    """Custom type ptrmLobeOperStatus based on Integer32"""
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
        *(("badSpeed", 4),
          ("inserted", 1),
          ("notPresent", 3),
          ("wrapped", 2))
    )


_PtrmLobeOperStatus_Type.__name__ = "Integer32"
_PtrmLobeOperStatus_Object = MibTableColumn
ptrmLobeOperStatus = _PtrmLobeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 2),
    _PtrmLobeOperStatus_Type()
)
ptrmLobeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmLobeOperStatus.setStatus("mandatory")


class _PtrmLobeAdminStatus_Type(Integer32):
    """Custom type ptrmLobeAdminStatus based on Integer32"""
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


_PtrmLobeAdminStatus_Type.__name__ = "Integer32"
_PtrmLobeAdminStatus_Object = MibTableColumn
ptrmLobeAdminStatus = _PtrmLobeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 3),
    _PtrmLobeAdminStatus_Type()
)
ptrmLobeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptrmLobeAdminStatus.setStatus("mandatory")


class _PtrmLobeMedia_Type(Integer32):
    """Custom type ptrmLobeMedia based on Integer32"""
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
        *(("fiberMedia", 5),
          ("ibmMedia", 4),
          ("otherMedia", 1),
          ("stpMedia", 3),
          ("utpMedia", 2))
    )


_PtrmLobeMedia_Type.__name__ = "Integer32"
_PtrmLobeMedia_Object = MibTableColumn
ptrmLobeMedia = _PtrmLobeMedia_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 4),
    _PtrmLobeMedia_Type()
)
ptrmLobeMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmLobeMedia.setStatus("mandatory")


class _PtrmLobeAutoWrapEnable_Type(Integer32):
    """Custom type ptrmLobeAutoWrapEnable based on Integer32"""
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


_PtrmLobeAutoWrapEnable_Type.__name__ = "Integer32"
_PtrmLobeAutoWrapEnable_Object = MibTableColumn
ptrmLobeAutoWrapEnable = _PtrmLobeAutoWrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 5),
    _PtrmLobeAutoWrapEnable_Type()
)
ptrmLobeAutoWrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptrmLobeAutoWrapEnable.setStatus("mandatory")


class _PtrmLobeAutoPartitionStatus_Type(Integer32):
    """Custom type ptrmLobeAutoPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_PtrmLobeAutoPartitionStatus_Type.__name__ = "Integer32"
_PtrmLobeAutoPartitionStatus_Object = MibTableColumn
ptrmLobeAutoPartitionStatus = _PtrmLobeAutoPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 6),
    _PtrmLobeAutoPartitionStatus_Type()
)
ptrmLobeAutoPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmLobeAutoPartitionStatus.setStatus("mandatory")


class _PtrmLobeDetectedSpeed_Type(Integer32):
    """Custom type ptrmLobeDetectedSpeed based on Integer32"""
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
        *(("invalid", 1),
          ("notApplicable", 4),
          ("speed-16Mbps", 3),
          ("speed-4Mbps", 2))
    )


_PtrmLobeDetectedSpeed_Type.__name__ = "Integer32"
_PtrmLobeDetectedSpeed_Object = MibTableColumn
ptrmLobeDetectedSpeed = _PtrmLobeDetectedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 7),
    _PtrmLobeDetectedSpeed_Type()
)
ptrmLobeDetectedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmLobeDetectedSpeed.setStatus("mandatory")


class _PtrmLobePhantomDrive_Type(Integer32):
    """Custom type ptrmLobePhantomDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("notApplicable", 1)
    )


_PtrmLobePhantomDrive_Type.__name__ = "Integer32"
_PtrmLobePhantomDrive_Object = MibTableColumn
ptrmLobePhantomDrive = _PtrmLobePhantomDrive_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 8),
    _PtrmLobePhantomDrive_Type()
)
ptrmLobePhantomDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmLobePhantomDrive.setStatus("mandatory")


class _PtrmLobePhantomDetect_Type(Integer32):
    """Custom type ptrmLobePhantomDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detectPhantom", 3),
          ("noDetectPhantom", 2),
          ("notApplicable", 1))
    )


_PtrmLobePhantomDetect_Type.__name__ = "Integer32"
_PtrmLobePhantomDetect_Object = MibTableColumn
ptrmLobePhantomDetect = _PtrmLobePhantomDetect_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 3, 1, 9),
    _PtrmLobePhantomDetect_Type()
)
ptrmLobePhantomDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmLobePhantomDetect.setStatus("mandatory")
_PtrmMacTable_Object = MibTable
ptrmMacTable = _PtrmMacTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 4)
)
if mibBuilder.loadTexts:
    ptrmMacTable.setStatus("mandatory")
_PtrmMacEntry_Object = MibTableRow
ptrmMacEntry = _PtrmMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 4, 1)
)
ptrmMacEntry.setIndexNames(
    (0, "DECHUB900-PTRM-MIB-V3-0", "ptrmMacIndex"),
)
if mibBuilder.loadTexts:
    ptrmMacEntry.setStatus("mandatory")


class _PtrmMacIndex_Type(Integer32):
    """Custom type ptrmMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PtrmMacIndex_Type.__name__ = "Integer32"
_PtrmMacIndex_Object = MibTableColumn
ptrmMacIndex = _PtrmMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 4, 1, 1),
    _PtrmMacIndex_Type()
)
ptrmMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmMacIndex.setStatus("mandatory")
_PtrmMacRingInterface_Type = Integer32
_PtrmMacRingInterface_Object = MibTableColumn
ptrmMacRingInterface = _PtrmMacRingInterface_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 4, 1, 2),
    _PtrmMacRingInterface_Type()
)
ptrmMacRingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmMacRingInterface.setStatus("mandatory")


class _PtrmMacAddress_Type(OctetString):
    """Custom type ptrmMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PtrmMacAddress_Type.__name__ = "OctetString"
_PtrmMacAddress_Object = MibTableColumn
ptrmMacAddress = _PtrmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 4, 1, 3),
    _PtrmMacAddress_Type()
)
ptrmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmMacAddress.setStatus("mandatory")


class _PtrmMacPosition_Type(Integer32):
    """Custom type ptrmMacPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PtrmMacPosition_Type.__name__ = "Integer32"
_PtrmMacPosition_Object = MibTableColumn
ptrmMacPosition = _PtrmMacPosition_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 4, 1, 4),
    _PtrmMacPosition_Type()
)
ptrmMacPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmMacPosition.setStatus("mandatory")
_PtrmMultiBp_ObjectIdentity = ObjectIdentity
ptrmMultiBp = _PtrmMultiBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5)
)
_PtrmNumBackplanePorts_Type = Integer32
_PtrmNumBackplanePorts_Object = MibScalar
ptrmNumBackplanePorts = _PtrmNumBackplanePorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5, 1),
    _PtrmNumBackplanePorts_Type()
)
ptrmNumBackplanePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmNumBackplanePorts.setStatus("mandatory")
_PtrmNumLobePorts_Type = Integer32
_PtrmNumLobePorts_Object = MibScalar
ptrmNumLobePorts = _PtrmNumLobePorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5, 2),
    _PtrmNumLobePorts_Type()
)
ptrmNumLobePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmNumLobePorts.setStatus("mandatory")
_PtrmMultiBpPortTable_Object = MibTable
ptrmMultiBpPortTable = _PtrmMultiBpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5, 3)
)
if mibBuilder.loadTexts:
    ptrmMultiBpPortTable.setStatus("mandatory")
_PtrmMultiBpPortEntry_Object = MibTableRow
ptrmMultiBpPortEntry = _PtrmMultiBpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5, 3, 1)
)
ptrmMultiBpPortEntry.setIndexNames(
    (0, "DECHUB900-PTRM-MIB-V3-0", "ptrmMultiBpPortIndex"),
)
if mibBuilder.loadTexts:
    ptrmMultiBpPortEntry.setStatus("mandatory")
_PtrmMultiBpPortIndex_Type = Integer32
_PtrmMultiBpPortIndex_Object = MibTableColumn
ptrmMultiBpPortIndex = _PtrmMultiBpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5, 3, 1, 1),
    _PtrmMultiBpPortIndex_Type()
)
ptrmMultiBpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmMultiBpPortIndex.setStatus("mandatory")


class _PtrmMultiBpPortSpeed_Type(Integer32):
    """Custom type ptrmMultiBpPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-16Mbps", 3),
          ("speed-4Mbps", 2))
    )


_PtrmMultiBpPortSpeed_Type.__name__ = "Integer32"
_PtrmMultiBpPortSpeed_Object = MibTableColumn
ptrmMultiBpPortSpeed = _PtrmMultiBpPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5, 3, 1, 2),
    _PtrmMultiBpPortSpeed_Type()
)
ptrmMultiBpPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptrmMultiBpPortSpeed.setStatus("mandatory")


class _PtrmMultiBpPortForceSpeed_Type(Integer32):
    """Custom type ptrmMultiBpPortForceSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("force-16Mbps", 3),
          ("force-4Mbps", 2),
          ("notForced", 1))
    )


_PtrmMultiBpPortForceSpeed_Type.__name__ = "Integer32"
_PtrmMultiBpPortForceSpeed_Object = MibTableColumn
ptrmMultiBpPortForceSpeed = _PtrmMultiBpPortForceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 3, 5, 3, 1, 3),
    _PtrmMultiBpPortForceSpeed_Type()
)
ptrmMultiBpPortForceSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptrmMultiBpPortForceSpeed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECHUB900-PTRM-MIB-V3-0",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decHub900": decHub900,
       "ptrm": ptrm,
       "ptrmBase": ptrmBase,
       "ptrmBaseForceSpeed": ptrmBaseForceSpeed,
       "ptrmBaseSpeed": ptrmBaseSpeed,
       "ptrmBaseNumLobes": ptrmBaseNumLobes,
       "ptrmTrunkTable": ptrmTrunkTable,
       "ptrmTrunkEntry": ptrmTrunkEntry,
       "ptrmTrunkType": ptrmTrunkType,
       "ptrmTrunkOperStatus": ptrmTrunkOperStatus,
       "ptrmTrunkAdminStatus": ptrmTrunkAdminStatus,
       "ptrmTrunkMedia": ptrmTrunkMedia,
       "ptrmTrunkAutoWrapEnable": ptrmTrunkAutoWrapEnable,
       "ptrmTrunkAutoPartitionStatus": ptrmTrunkAutoPartitionStatus,
       "ptrmTrunkDetectedSpeed": ptrmTrunkDetectedSpeed,
       "ptrmTrunkPhantomDrive": ptrmTrunkPhantomDrive,
       "ptrmTrunkPhantomDetect": ptrmTrunkPhantomDetect,
       "ptrmLobeTable": ptrmLobeTable,
       "ptrmLobeEntry": ptrmLobeEntry,
       "ptrmLobeIndex": ptrmLobeIndex,
       "ptrmLobeOperStatus": ptrmLobeOperStatus,
       "ptrmLobeAdminStatus": ptrmLobeAdminStatus,
       "ptrmLobeMedia": ptrmLobeMedia,
       "ptrmLobeAutoWrapEnable": ptrmLobeAutoWrapEnable,
       "ptrmLobeAutoPartitionStatus": ptrmLobeAutoPartitionStatus,
       "ptrmLobeDetectedSpeed": ptrmLobeDetectedSpeed,
       "ptrmLobePhantomDrive": ptrmLobePhantomDrive,
       "ptrmLobePhantomDetect": ptrmLobePhantomDetect,
       "ptrmMacTable": ptrmMacTable,
       "ptrmMacEntry": ptrmMacEntry,
       "ptrmMacIndex": ptrmMacIndex,
       "ptrmMacRingInterface": ptrmMacRingInterface,
       "ptrmMacAddress": ptrmMacAddress,
       "ptrmMacPosition": ptrmMacPosition,
       "ptrmMultiBp": ptrmMultiBp,
       "ptrmNumBackplanePorts": ptrmNumBackplanePorts,
       "ptrmNumLobePorts": ptrmNumLobePorts,
       "ptrmMultiBpPortTable": ptrmMultiBpPortTable,
       "ptrmMultiBpPortEntry": ptrmMultiBpPortEntry,
       "ptrmMultiBpPortIndex": ptrmMultiBpPortIndex,
       "ptrmMultiBpPortSpeed": ptrmMultiBpPortSpeed,
       "ptrmMultiBpPortForceSpeed": ptrmMultiBpPortForceSpeed}
)
