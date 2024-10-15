# SNMP MIB module (ALTEON-TIGON-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-TIGON-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:57 2024
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

(switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "switch")

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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1)
)


class _HwPartNumber_Type(DisplayString):
    """Custom type hwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwPartNumber_Type.__name__ = "DisplayString"
_HwPartNumber_Object = MibScalar
hwPartNumber = _HwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 1),
    _HwPartNumber_Type()
)
hwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPartNumber.setStatus("mandatory")


class _HwRevision_Type(DisplayString):
    """Custom type hwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRevision_Type.__name__ = "DisplayString"
_HwRevision_Object = MibScalar
hwRevision = _HwRevision_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 2),
    _HwRevision_Type()
)
hwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRevision.setStatus("mandatory")


class _HwPowerSupplyStatus_Type(Integer32):
    """Custom type hwPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("ok", 1))
    )


_HwPowerSupplyStatus_Type.__name__ = "Integer32"
_HwPowerSupplyStatus_Object = MibScalar
hwPowerSupplyStatus = _HwPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 3),
    _HwPowerSupplyStatus_Type()
)
hwPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPowerSupplyStatus.setStatus("mandatory")


class _HwRedundantPSPresent_Type(Integer32):
    """Custom type hwRedundantPSPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 3),
          ("present", 4))
    )


_HwRedundantPSPresent_Type.__name__ = "Integer32"
_HwRedundantPSPresent_Object = MibScalar
hwRedundantPSPresent = _HwRedundantPSPresent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 4),
    _HwRedundantPSPresent_Type()
)
hwRedundantPSPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRedundantPSPresent.setStatus("mandatory")


class _HwRedundantPSStatus_Type(Integer32):
    """Custom type hwRedundantPSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("notPresent", 3),
          ("ok", 1))
    )


_HwRedundantPSStatus_Type.__name__ = "Integer32"
_HwRedundantPSStatus_Object = MibScalar
hwRedundantPSStatus = _HwRedundantPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 5),
    _HwRedundantPSStatus_Type()
)
hwRedundantPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRedundantPSStatus.setStatus("mandatory")
_HwSensor1Temp_Type = Integer32
_HwSensor1Temp_Object = MibScalar
hwSensor1Temp = _HwSensor1Temp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 6),
    _HwSensor1Temp_Type()
)
hwSensor1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensor1Temp.setStatus("mandatory")
_HwSensor2Temp_Type = Integer32
_HwSensor2Temp_Object = MibScalar
hwSensor2Temp = _HwSensor2Temp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 7),
    _HwSensor2Temp_Type()
)
hwSensor2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensor2Temp.setStatus("mandatory")
_HwSensor3Temp_Type = Integer32
_HwSensor3Temp_Object = MibScalar
hwSensor3Temp = _HwSensor3Temp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 8),
    _HwSensor3Temp_Type()
)
hwSensor3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensor3Temp.setStatus("mandatory")
_HwSensor4Temp_Type = Integer32
_HwSensor4Temp_Object = MibScalar
hwSensor4Temp = _HwSensor4Temp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 1, 9),
    _HwSensor4Temp_Type()
)
hwSensor4Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensor4Temp.setStatus("mandatory")
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2)
)
_AgGeneral_ObjectIdentity = ObjectIdentity
agGeneral = _AgGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1)
)


class _AgSaveConfiguration_Type(Integer32):
    """Custom type agSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSaveActive", 3),
          ("ok", 1),
          ("saveActive", 2))
    )


_AgSaveConfiguration_Type.__name__ = "Integer32"
_AgSaveConfiguration_Object = MibScalar
agSaveConfiguration = _AgSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 1),
    _AgSaveConfiguration_Type()
)
agSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSaveConfiguration.setStatus("mandatory")


class _AgApplyConfiguration_Type(Integer32):
    """Custom type agApplyConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("other", 1))
    )


_AgApplyConfiguration_Type.__name__ = "Integer32"
_AgApplyConfiguration_Object = MibScalar
agApplyConfiguration = _AgApplyConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 2),
    _AgApplyConfiguration_Type()
)
agApplyConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agApplyConfiguration.setStatus("mandatory")


class _AgApplyPending_Type(Integer32):
    """Custom type agApplyPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyNeeded", 2),
          ("noApplyNeeded", 3))
    )


_AgApplyPending_Type.__name__ = "Integer32"
_AgApplyPending_Object = MibScalar
agApplyPending = _AgApplyPending_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 3),
    _AgApplyPending_Type()
)
agApplyPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyPending.setStatus("mandatory")


class _AgReset_Type(Integer32):
    """Custom type agReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldReset", 2),
          ("other", 1),
          ("warmReset", 3))
    )


_AgReset_Type.__name__ = "Integer32"
_AgReset_Object = MibScalar
agReset = _AgReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 4),
    _AgReset_Type()
)
agReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agReset.setStatus("mandatory")


class _AgConfigForNxtReset_Type(Integer32):
    """Custom type agConfigForNxtReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("backup", 3),
          ("default", 4))
    )


_AgConfigForNxtReset_Type.__name__ = "Integer32"
_AgConfigForNxtReset_Object = MibScalar
agConfigForNxtReset = _AgConfigForNxtReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 5),
    _AgConfigForNxtReset_Type()
)
agConfigForNxtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agConfigForNxtReset.setStatus("mandatory")


class _AgImageForNxtReset_Type(Integer32):
    """Custom type agImageForNxtReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3))
    )


_AgImageForNxtReset_Type.__name__ = "Integer32"
_AgImageForNxtReset_Object = MibScalar
agImageForNxtReset = _AgImageForNxtReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 6),
    _AgImageForNxtReset_Type()
)
agImageForNxtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agImageForNxtReset.setStatus("mandatory")


class _AgSoftwareVersion_Type(DisplayString):
    """Custom type agSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgSoftwareVersion_Type.__name__ = "DisplayString"
_AgSoftwareVersion_Object = MibScalar
agSoftwareVersion = _AgSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 7),
    _AgSoftwareVersion_Type()
)
agSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSoftwareVersion.setStatus("mandatory")


class _AgBootVer_Type(DisplayString):
    """Custom type agBootVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgBootVer_Type.__name__ = "DisplayString"
_AgBootVer_Object = MibScalar
agBootVer = _AgBootVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 8),
    _AgBootVer_Type()
)
agBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agBootVer.setStatus("mandatory")


class _AgImage1Ver_Type(DisplayString):
    """Custom type agImage1Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgImage1Ver_Type.__name__ = "DisplayString"
_AgImage1Ver_Object = MibScalar
agImage1Ver = _AgImage1Ver_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 9),
    _AgImage1Ver_Type()
)
agImage1Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agImage1Ver.setStatus("mandatory")


class _AgImage2Ver_Type(DisplayString):
    """Custom type agImage2Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgImage2Ver_Type.__name__ = "DisplayString"
_AgImage2Ver_Object = MibScalar
agImage2Ver = _AgImage2Ver_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 10),
    _AgImage2Ver_Type()
)
agImage2Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agImage2Ver.setStatus("mandatory")


class _AgRtcDate_Type(DisplayString):
    """Custom type agRtcDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgRtcDate_Type.__name__ = "DisplayString"
_AgRtcDate_Object = MibScalar
agRtcDate = _AgRtcDate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 11),
    _AgRtcDate_Type()
)
agRtcDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRtcDate.setStatus("mandatory")


class _AgRtcTime_Type(DisplayString):
    """Custom type agRtcTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgRtcTime_Type.__name__ = "DisplayString"
_AgRtcTime_Object = MibScalar
agRtcTime = _AgRtcTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 12),
    _AgRtcTime_Type()
)
agRtcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRtcTime.setStatus("mandatory")
_AgTftpServerIpAddr_Type = IpAddress
_AgTftpServerIpAddr_Object = MibScalar
agTftpServerIpAddr = _AgTftpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 13),
    _AgTftpServerIpAddr_Type()
)
agTftpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpServerIpAddr.setStatus("mandatory")


class _AgTftpImageFileName_Type(DisplayString):
    """Custom type agTftpImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpImageFileName_Type.__name__ = "DisplayString"
_AgTftpImageFileName_Object = MibScalar
agTftpImageFileName = _AgTftpImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 14),
    _AgTftpImageFileName_Type()
)
agTftpImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpImageFileName.setStatus("mandatory")


class _AgTftpImage_Type(Integer32):
    """Custom type agTftpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3))
    )


_AgTftpImage_Type.__name__ = "Integer32"
_AgTftpImage_Object = MibScalar
agTftpImage = _AgTftpImage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 15),
    _AgTftpImage_Type()
)
agTftpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpImage.setStatus("mandatory")


class _AgTftpDownload_Type(Integer32):
    """Custom type agTftpDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("other", 1))
    )


_AgTftpDownload_Type.__name__ = "Integer32"
_AgTftpDownload_Object = MibScalar
agTftpDownload = _AgTftpDownload_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 16),
    _AgTftpDownload_Type()
)
agTftpDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpDownload.setStatus("mandatory")


class _AgLastSetErrorReason_Type(DisplayString):
    """Custom type agLastSetErrorReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AgLastSetErrorReason_Type.__name__ = "DisplayString"
_AgLastSetErrorReason_Object = MibScalar
agLastSetErrorReason = _AgLastSetErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 17),
    _AgLastSetErrorReason_Type()
)
agLastSetErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agLastSetErrorReason.setStatus("mandatory")


class _AgTftpServer_Type(DisplayString):
    """Custom type agTftpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgTftpServer_Type.__name__ = "DisplayString"
_AgTftpServer_Object = MibScalar
agTftpServer = _AgTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 18),
    _AgTftpServer_Type()
)
agTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpServer.setStatus("mandatory")


class _AgTftpCfgFileName_Type(DisplayString):
    """Custom type agTftpCfgFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpCfgFileName_Type.__name__ = "DisplayString"
_AgTftpCfgFileName_Object = MibScalar
agTftpCfgFileName = _AgTftpCfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 19),
    _AgTftpCfgFileName_Type()
)
agTftpCfgFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpCfgFileName.setStatus("mandatory")


class _AgTftpDumpFileName_Type(DisplayString):
    """Custom type agTftpDumpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpDumpFileName_Type.__name__ = "DisplayString"
_AgTftpDumpFileName_Object = MibScalar
agTftpDumpFileName = _AgTftpDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 20),
    _AgTftpDumpFileName_Type()
)
agTftpDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpDumpFileName.setStatus("mandatory")


class _AgTftpAction_Type(Integer32):
    """Custom type agTftpAction based on Integer32"""
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
        *(("cfg-get", 3),
          ("cfg-put", 4),
          ("dump-put", 5),
          ("img-get", 2),
          ("other", 1))
    )


_AgTftpAction_Type.__name__ = "Integer32"
_AgTftpAction_Object = MibScalar
agTftpAction = _AgTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 21),
    _AgTftpAction_Type()
)
agTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpAction.setStatus("mandatory")


class _AgTftpLastActionStatus_Type(DisplayString):
    """Custom type agTftpLastActionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpLastActionStatus_Type.__name__ = "DisplayString"
_AgTftpLastActionStatus_Object = MibScalar
agTftpLastActionStatus = _AgTftpLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 22),
    _AgTftpLastActionStatus_Type()
)
agTftpLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTftpLastActionStatus.setStatus("mandatory")


class _AgRevert_Type(Integer32):
    """Custom type agRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("revert", 2))
    )


_AgRevert_Type.__name__ = "Integer32"
_AgRevert_Object = MibScalar
agRevert = _AgRevert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 23),
    _AgRevert_Type()
)
agRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRevert.setStatus("mandatory")


class _AgRevertApply_Type(Integer32):
    """Custom type agRevertApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("revertApply", 2))
    )


_AgRevertApply_Type.__name__ = "Integer32"
_AgRevertApply_Object = MibScalar
agRevertApply = _AgRevertApply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 24),
    _AgRevertApply_Type()
)
agRevertApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRevertApply.setStatus("mandatory")
_AgEnabledSwFeatures_Type = DisplayString
_AgEnabledSwFeatures_Object = MibScalar
agEnabledSwFeatures = _AgEnabledSwFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 25),
    _AgEnabledSwFeatures_Type()
)
agEnabledSwFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledSwFeatures.setStatus("mandatory")


class _AgClrSyslogMsgs_Type(Integer32):
    """Custom type agClrSyslogMsgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_AgClrSyslogMsgs_Type.__name__ = "Integer32"
_AgClrSyslogMsgs_Object = MibScalar
agClrSyslogMsgs = _AgClrSyslogMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 26),
    _AgClrSyslogMsgs_Type()
)
agClrSyslogMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agClrSyslogMsgs.setStatus("mandatory")


class _AgSavePending_Type(Integer32):
    """Custom type agSavePending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSaveNeeded", 2),
          ("saveNeeded", 1))
    )


_AgSavePending_Type.__name__ = "Integer32"
_AgSavePending_Object = MibScalar
agSavePending = _AgSavePending_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 27),
    _AgSavePending_Type()
)
agSavePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSavePending.setStatus("mandatory")


class _AgEnabledGslbKey_Type(Integer32):
    """Custom type agEnabledGslbKey based on Integer32"""
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


_AgEnabledGslbKey_Type.__name__ = "Integer32"
_AgEnabledGslbKey_Object = MibScalar
agEnabledGslbKey = _AgEnabledGslbKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 28),
    _AgEnabledGslbKey_Type()
)
agEnabledGslbKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledGslbKey.setStatus("mandatory")


class _AgEnabledBwmKey_Type(Integer32):
    """Custom type agEnabledBwmKey based on Integer32"""
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


_AgEnabledBwmKey_Type.__name__ = "Integer32"
_AgEnabledBwmKey_Object = MibScalar
agEnabledBwmKey = _AgEnabledBwmKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 29),
    _AgEnabledBwmKey_Type()
)
agEnabledBwmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledBwmKey.setStatus("mandatory")


class _AgSlotNumber_Type(Integer32):
    """Custom type agSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgSlotNumber_Type.__name__ = "Integer32"
_AgSlotNumber_Object = MibScalar
agSlotNumber = _AgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 30),
    _AgSlotNumber_Type()
)
agSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSlotNumber.setStatus("mandatory")


class _AgEnabledRurlKey_Type(Integer32):
    """Custom type agEnabledRurlKey based on Integer32"""
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


_AgEnabledRurlKey_Type.__name__ = "Integer32"
_AgEnabledRurlKey_Object = MibScalar
agEnabledRurlKey = _AgEnabledRurlKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 31),
    _AgEnabledRurlKey_Type()
)
agEnabledRurlKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledRurlKey.setStatus("mandatory")
_AgGeneralConfig_ObjectIdentity = ObjectIdentity
agGeneralConfig = _AgGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2)
)
_AgNewCfgSyslogHost_Type = IpAddress
_AgNewCfgSyslogHost_Object = MibScalar
agNewCfgSyslogHost = _AgNewCfgSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 1),
    _AgNewCfgSyslogHost_Type()
)
agNewCfgSyslogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogHost.setStatus("mandatory")
_AgCurCfgSyslogHost_Type = IpAddress
_AgCurCfgSyslogHost_Object = MibScalar
agCurCfgSyslogHost = _AgCurCfgSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 2),
    _AgCurCfgSyslogHost_Type()
)
agCurCfgSyslogHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogHost.setStatus("mandatory")


class _AgNewCfgBootp_Type(Integer32):
    """Custom type agNewCfgBootp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_AgNewCfgBootp_Type.__name__ = "Integer32"
_AgNewCfgBootp_Object = MibScalar
agNewCfgBootp = _AgNewCfgBootp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 3),
    _AgNewCfgBootp_Type()
)
agNewCfgBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgBootp.setStatus("mandatory")


class _AgCurCfgBootp_Type(Integer32):
    """Custom type agCurCfgBootp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_AgCurCfgBootp_Type.__name__ = "Integer32"
_AgCurCfgBootp_Object = MibScalar
agCurCfgBootp = _AgCurCfgBootp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 4),
    _AgCurCfgBootp_Type()
)
agCurCfgBootp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgBootp.setStatus("mandatory")


class _AgNewCfgSpanningTree_Type(Integer32):
    """Custom type agNewCfgSpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_AgNewCfgSpanningTree_Type.__name__ = "Integer32"
_AgNewCfgSpanningTree_Object = MibScalar
agNewCfgSpanningTree = _AgNewCfgSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 5),
    _AgNewCfgSpanningTree_Type()
)
agNewCfgSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSpanningTree.setStatus("mandatory")


class _AgCurCfgSpanningTree_Type(Integer32):
    """Custom type agCurCfgSpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_AgCurCfgSpanningTree_Type.__name__ = "Integer32"
_AgCurCfgSpanningTree_Object = MibScalar
agCurCfgSpanningTree = _AgCurCfgSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 6),
    _AgCurCfgSpanningTree_Type()
)
agCurCfgSpanningTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSpanningTree.setStatus("mandatory")
_AgTrapHostTableMaxEnt_Type = Integer32
_AgTrapHostTableMaxEnt_Object = MibScalar
agTrapHostTableMaxEnt = _AgTrapHostTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 7),
    _AgTrapHostTableMaxEnt_Type()
)
agTrapHostTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTrapHostTableMaxEnt.setStatus("mandatory")
_AgCurCfgTrapHostTable_Object = MibTable
agCurCfgTrapHostTable = _AgCurCfgTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    agCurCfgTrapHostTable.setStatus("mandatory")
_AgCurCfgTrapHostEntry_Object = MibTableRow
agCurCfgTrapHostEntry = _AgCurCfgTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 8, 1)
)
agCurCfgTrapHostEntry.setIndexNames(
    (0, "ALTEON-TIGON-SWITCH-MIB", "agCurCfgTrapHostIndx"),
)
if mibBuilder.loadTexts:
    agCurCfgTrapHostEntry.setStatus("mandatory")


class _AgCurCfgTrapHostIndx_Type(Integer32):
    """Custom type agCurCfgTrapHostIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgCurCfgTrapHostIndx_Type.__name__ = "Integer32"
_AgCurCfgTrapHostIndx_Object = MibTableColumn
agCurCfgTrapHostIndx = _AgCurCfgTrapHostIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 8, 1, 1),
    _AgCurCfgTrapHostIndx_Type()
)
agCurCfgTrapHostIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostIndx.setStatus("mandatory")
_AgCurCfgTrapHostIpAddr_Type = IpAddress
_AgCurCfgTrapHostIpAddr_Object = MibTableColumn
agCurCfgTrapHostIpAddr = _AgCurCfgTrapHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 8, 1, 2),
    _AgCurCfgTrapHostIpAddr_Type()
)
agCurCfgTrapHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostIpAddr.setStatus("mandatory")


class _AgCurCfgTrapHostCommString_Type(DisplayString):
    """Custom type agCurCfgTrapHostCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgCurCfgTrapHostCommString_Type.__name__ = "DisplayString"
_AgCurCfgTrapHostCommString_Object = MibTableColumn
agCurCfgTrapHostCommString = _AgCurCfgTrapHostCommString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 8, 1, 3),
    _AgCurCfgTrapHostCommString_Type()
)
agCurCfgTrapHostCommString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostCommString.setStatus("mandatory")
_AgNewCfgTrapHostTable_Object = MibTable
agNewCfgTrapHostTable = _AgNewCfgTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    agNewCfgTrapHostTable.setStatus("mandatory")
_AgNewCfgTrapHostEntry_Object = MibTableRow
agNewCfgTrapHostEntry = _AgNewCfgTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 9, 1)
)
agNewCfgTrapHostEntry.setIndexNames(
    (0, "ALTEON-TIGON-SWITCH-MIB", "agNewCfgTrapHostIndx"),
)
if mibBuilder.loadTexts:
    agNewCfgTrapHostEntry.setStatus("mandatory")


class _AgNewCfgTrapHostIndx_Type(Integer32):
    """Custom type agNewCfgTrapHostIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgNewCfgTrapHostIndx_Type.__name__ = "Integer32"
_AgNewCfgTrapHostIndx_Object = MibTableColumn
agNewCfgTrapHostIndx = _AgNewCfgTrapHostIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 9, 1, 1),
    _AgNewCfgTrapHostIndx_Type()
)
agNewCfgTrapHostIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgTrapHostIndx.setStatus("mandatory")
_AgNewCfgTrapHostIpAddr_Type = IpAddress
_AgNewCfgTrapHostIpAddr_Object = MibTableColumn
agNewCfgTrapHostIpAddr = _AgNewCfgTrapHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 9, 1, 2),
    _AgNewCfgTrapHostIpAddr_Type()
)
agNewCfgTrapHostIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTrapHostIpAddr.setStatus("mandatory")


class _AgNewCfgTrapHostCommString_Type(DisplayString):
    """Custom type agNewCfgTrapHostCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgNewCfgTrapHostCommString_Type.__name__ = "DisplayString"
_AgNewCfgTrapHostCommString_Object = MibTableColumn
agNewCfgTrapHostCommString = _AgNewCfgTrapHostCommString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 9, 1, 3),
    _AgNewCfgTrapHostCommString_Type()
)
agNewCfgTrapHostCommString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTrapHostCommString.setStatus("mandatory")


class _AgCurCfgHttpServerPort_Type(Integer32):
    """Custom type agCurCfgHttpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgCurCfgHttpServerPort_Type.__name__ = "Integer32"
_AgCurCfgHttpServerPort_Object = MibScalar
agCurCfgHttpServerPort = _AgCurCfgHttpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 10),
    _AgCurCfgHttpServerPort_Type()
)
agCurCfgHttpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgHttpServerPort.setStatus("mandatory")


class _AgNewCfgHttpServerPort_Type(Integer32):
    """Custom type agNewCfgHttpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgHttpServerPort_Type.__name__ = "Integer32"
_AgNewCfgHttpServerPort_Object = MibScalar
agNewCfgHttpServerPort = _AgNewCfgHttpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 11),
    _AgNewCfgHttpServerPort_Type()
)
agNewCfgHttpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgHttpServerPort.setStatus("mandatory")


class _AgCurCfgLoginBanner_Type(DisplayString):
    """Custom type agCurCfgLoginBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AgCurCfgLoginBanner_Type.__name__ = "DisplayString"
_AgCurCfgLoginBanner_Object = MibScalar
agCurCfgLoginBanner = _AgCurCfgLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 12),
    _AgCurCfgLoginBanner_Type()
)
agCurCfgLoginBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgLoginBanner.setStatus("mandatory")


class _AgNewCfgLoginBanner_Type(DisplayString):
    """Custom type agNewCfgLoginBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AgNewCfgLoginBanner_Type.__name__ = "DisplayString"
_AgNewCfgLoginBanner_Object = MibScalar
agNewCfgLoginBanner = _AgNewCfgLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 13),
    _AgNewCfgLoginBanner_Type()
)
agNewCfgLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgLoginBanner.setStatus("mandatory")
_AgNewCfgSyslog2Host_Type = IpAddress
_AgNewCfgSyslog2Host_Object = MibScalar
agNewCfgSyslog2Host = _AgNewCfgSyslog2Host_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 14),
    _AgNewCfgSyslog2Host_Type()
)
agNewCfgSyslog2Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslog2Host.setStatus("mandatory")
_AgCurCfgSyslog2Host_Type = IpAddress
_AgCurCfgSyslog2Host_Object = MibScalar
agCurCfgSyslog2Host = _AgCurCfgSyslog2Host_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 15),
    _AgCurCfgSyslog2Host_Type()
)
agCurCfgSyslog2Host.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslog2Host.setStatus("mandatory")


class _AgCurCfgSyslogFac_Type(Integer32):
    """Custom type agCurCfgSyslogFac based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_AgCurCfgSyslogFac_Type.__name__ = "Integer32"
_AgCurCfgSyslogFac_Object = MibScalar
agCurCfgSyslogFac = _AgCurCfgSyslogFac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 16),
    _AgCurCfgSyslogFac_Type()
)
agCurCfgSyslogFac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogFac.setStatus("mandatory")


class _AgNewCfgSyslogFac_Type(Integer32):
    """Custom type agNewCfgSyslogFac based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_AgNewCfgSyslogFac_Type.__name__ = "Integer32"
_AgNewCfgSyslogFac_Object = MibScalar
agNewCfgSyslogFac = _AgNewCfgSyslogFac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 17),
    _AgNewCfgSyslogFac_Type()
)
agNewCfgSyslogFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogFac.setStatus("mandatory")


class _AgCurCfgSyslog2Fac_Type(Integer32):
    """Custom type agCurCfgSyslog2Fac based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_AgCurCfgSyslog2Fac_Type.__name__ = "Integer32"
_AgCurCfgSyslog2Fac_Object = MibScalar
agCurCfgSyslog2Fac = _AgCurCfgSyslog2Fac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 18),
    _AgCurCfgSyslog2Fac_Type()
)
agCurCfgSyslog2Fac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslog2Fac.setStatus("mandatory")


class _AgNewCfgSyslog2Fac_Type(Integer32):
    """Custom type agNewCfgSyslog2Fac based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_AgNewCfgSyslog2Fac_Type.__name__ = "Integer32"
_AgNewCfgSyslog2Fac_Object = MibScalar
agNewCfgSyslog2Fac = _AgNewCfgSyslog2Fac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 19),
    _AgNewCfgSyslog2Fac_Type()
)
agNewCfgSyslog2Fac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslog2Fac.setStatus("mandatory")


class _AgCurCfgSmtpHost_Type(DisplayString):
    """Custom type agCurCfgSmtpHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AgCurCfgSmtpHost_Type.__name__ = "DisplayString"
_AgCurCfgSmtpHost_Object = MibScalar
agCurCfgSmtpHost = _AgCurCfgSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 20),
    _AgCurCfgSmtpHost_Type()
)
agCurCfgSmtpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSmtpHost.setStatus("mandatory")


class _AgNewCfgSmtpHost_Type(DisplayString):
    """Custom type agNewCfgSmtpHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AgNewCfgSmtpHost_Type.__name__ = "DisplayString"
_AgNewCfgSmtpHost_Object = MibScalar
agNewCfgSmtpHost = _AgNewCfgSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 21),
    _AgNewCfgSmtpHost_Type()
)
agNewCfgSmtpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSmtpHost.setStatus("mandatory")


class _AgCurCfgConsole_Type(Integer32):
    """Custom type agCurCfgConsole based on Integer32"""
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


_AgCurCfgConsole_Type.__name__ = "Integer32"
_AgCurCfgConsole_Object = MibScalar
agCurCfgConsole = _AgCurCfgConsole_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 22),
    _AgCurCfgConsole_Type()
)
agCurCfgConsole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgConsole.setStatus("mandatory")


class _AgNewCfgConsole_Type(Integer32):
    """Custom type agNewCfgConsole based on Integer32"""
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


_AgNewCfgConsole_Type.__name__ = "Integer32"
_AgNewCfgConsole_Object = MibScalar
agNewCfgConsole = _AgNewCfgConsole_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 23),
    _AgNewCfgConsole_Type()
)
agNewCfgConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgConsole.setStatus("mandatory")
_AgCurCfgMgmtNetwork_Type = IpAddress
_AgCurCfgMgmtNetwork_Object = MibScalar
agCurCfgMgmtNetwork = _AgCurCfgMgmtNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 24),
    _AgCurCfgMgmtNetwork_Type()
)
agCurCfgMgmtNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtNetwork.setStatus("mandatory")
_AgNewCfgMgmtNetwork_Type = IpAddress
_AgNewCfgMgmtNetwork_Object = MibScalar
agNewCfgMgmtNetwork = _AgNewCfgMgmtNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 25),
    _AgNewCfgMgmtNetwork_Type()
)
agNewCfgMgmtNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetwork.setStatus("mandatory")
_AgCurCfgMgmtMask_Type = IpAddress
_AgCurCfgMgmtMask_Object = MibScalar
agCurCfgMgmtMask = _AgCurCfgMgmtMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 26),
    _AgCurCfgMgmtMask_Type()
)
agCurCfgMgmtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtMask.setStatus("mandatory")
_AgNewCfgMgmtMask_Type = IpAddress
_AgNewCfgMgmtMask_Object = MibScalar
agNewCfgMgmtMask = _AgNewCfgMgmtMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 27),
    _AgNewCfgMgmtMask_Type()
)
agNewCfgMgmtMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgMgmtMask.setStatus("mandatory")
_AgNTP_ObjectIdentity = ObjectIdentity
agNTP = _AgNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28)
)
_AgCurCfgNTPServer_Type = IpAddress
_AgCurCfgNTPServer_Object = MibScalar
agCurCfgNTPServer = _AgCurCfgNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 1),
    _AgCurCfgNTPServer_Type()
)
agCurCfgNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPServer.setStatus("mandatory")
_AgNewCfgNTPServer_Type = IpAddress
_AgNewCfgNTPServer_Object = MibScalar
agNewCfgNTPServer = _AgNewCfgNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 2),
    _AgNewCfgNTPServer_Type()
)
agNewCfgNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPServer.setStatus("mandatory")


class _AgCurCfgNTPResyncInterval_Type(Integer32):
    """Custom type agCurCfgNTPResyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2880),
    )


_AgCurCfgNTPResyncInterval_Type.__name__ = "Integer32"
_AgCurCfgNTPResyncInterval_Object = MibScalar
agCurCfgNTPResyncInterval = _AgCurCfgNTPResyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 3),
    _AgCurCfgNTPResyncInterval_Type()
)
agCurCfgNTPResyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPResyncInterval.setStatus("mandatory")


class _AgNewCfgNTPResyncInterval_Type(Integer32):
    """Custom type agNewCfgNTPResyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2880),
    )


_AgNewCfgNTPResyncInterval_Type.__name__ = "Integer32"
_AgNewCfgNTPResyncInterval_Object = MibScalar
agNewCfgNTPResyncInterval = _AgNewCfgNTPResyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 4),
    _AgNewCfgNTPResyncInterval_Type()
)
agNewCfgNTPResyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPResyncInterval.setStatus("mandatory")


class _AgCurCfgNTPTzone_Type(DisplayString):
    """Custom type agCurCfgNTPTzone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AgCurCfgNTPTzone_Type.__name__ = "DisplayString"
_AgCurCfgNTPTzone_Object = MibScalar
agCurCfgNTPTzone = _AgCurCfgNTPTzone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 5),
    _AgCurCfgNTPTzone_Type()
)
agCurCfgNTPTzone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPTzone.setStatus("mandatory")


class _AgNewCfgNTPTzone_Type(DisplayString):
    """Custom type agNewCfgNTPTzone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AgNewCfgNTPTzone_Type.__name__ = "DisplayString"
_AgNewCfgNTPTzone_Object = MibScalar
agNewCfgNTPTzone = _AgNewCfgNTPTzone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 6),
    _AgNewCfgNTPTzone_Type()
)
agNewCfgNTPTzone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPTzone.setStatus("mandatory")


class _AgCurCfgNTPDlight_Type(Integer32):
    """Custom type agCurCfgNTPDlight based on Integer32"""
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


_AgCurCfgNTPDlight_Type.__name__ = "Integer32"
_AgCurCfgNTPDlight_Object = MibScalar
agCurCfgNTPDlight = _AgCurCfgNTPDlight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 7),
    _AgCurCfgNTPDlight_Type()
)
agCurCfgNTPDlight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPDlight.setStatus("mandatory")


class _AgNewCfgNTPDlight_Type(Integer32):
    """Custom type agNewCfgNTPDlight based on Integer32"""
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


_AgNewCfgNTPDlight_Type.__name__ = "Integer32"
_AgNewCfgNTPDlight_Object = MibScalar
agNewCfgNTPDlight = _AgNewCfgNTPDlight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 8),
    _AgNewCfgNTPDlight_Type()
)
agNewCfgNTPDlight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPDlight.setStatus("mandatory")


class _AgCurCfgNTPService_Type(Integer32):
    """Custom type agCurCfgNTPService based on Integer32"""
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


_AgCurCfgNTPService_Type.__name__ = "Integer32"
_AgCurCfgNTPService_Object = MibScalar
agCurCfgNTPService = _AgCurCfgNTPService_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 9),
    _AgCurCfgNTPService_Type()
)
agCurCfgNTPService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPService.setStatus("mandatory")


class _AgNewCfgNTPService_Type(Integer32):
    """Custom type agNewCfgNTPService based on Integer32"""
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


_AgNewCfgNTPService_Type.__name__ = "Integer32"
_AgNewCfgNTPService_Object = MibScalar
agNewCfgNTPService = _AgNewCfgNTPService_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 28, 10),
    _AgNewCfgNTPService_Type()
)
agNewCfgNTPService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPService.setStatus("mandatory")
_AgLog_ObjectIdentity = ObjectIdentity
agLog = _AgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29)
)


class _AgNewCfgSyslogTrapConsole_Type(Integer32):
    """Custom type agNewCfgSyslogTrapConsole based on Integer32"""
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


_AgNewCfgSyslogTrapConsole_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapConsole_Object = MibScalar
agNewCfgSyslogTrapConsole = _AgNewCfgSyslogTrapConsole_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 1),
    _AgNewCfgSyslogTrapConsole_Type()
)
agNewCfgSyslogTrapConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapConsole.setStatus("mandatory")


class _AgCurCfgSyslogTrapConsole_Type(Integer32):
    """Custom type agCurCfgSyslogTrapConsole based on Integer32"""
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


_AgCurCfgSyslogTrapConsole_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapConsole_Object = MibScalar
agCurCfgSyslogTrapConsole = _AgCurCfgSyslogTrapConsole_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 2),
    _AgCurCfgSyslogTrapConsole_Type()
)
agCurCfgSyslogTrapConsole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapConsole.setStatus("mandatory")


class _AgNewCfgSyslogTrapSystem_Type(Integer32):
    """Custom type agNewCfgSyslogTrapSystem based on Integer32"""
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


_AgNewCfgSyslogTrapSystem_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapSystem_Object = MibScalar
agNewCfgSyslogTrapSystem = _AgNewCfgSyslogTrapSystem_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 3),
    _AgNewCfgSyslogTrapSystem_Type()
)
agNewCfgSyslogTrapSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSystem.setStatus("mandatory")


class _AgCurCfgSyslogTrapSystem_Type(Integer32):
    """Custom type agCurCfgSyslogTrapSystem based on Integer32"""
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


_AgCurCfgSyslogTrapSystem_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapSystem_Object = MibScalar
agCurCfgSyslogTrapSystem = _AgCurCfgSyslogTrapSystem_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 4),
    _AgCurCfgSyslogTrapSystem_Type()
)
agCurCfgSyslogTrapSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSystem.setStatus("mandatory")


class _AgNewCfgSyslogTrapMgmt_Type(Integer32):
    """Custom type agNewCfgSyslogTrapMgmt based on Integer32"""
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


_AgNewCfgSyslogTrapMgmt_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapMgmt_Object = MibScalar
agNewCfgSyslogTrapMgmt = _AgNewCfgSyslogTrapMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 5),
    _AgNewCfgSyslogTrapMgmt_Type()
)
agNewCfgSyslogTrapMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapMgmt.setStatus("mandatory")


class _AgCurCfgSyslogTrapMgmt_Type(Integer32):
    """Custom type agCurCfgSyslogTrapMgmt based on Integer32"""
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


_AgCurCfgSyslogTrapMgmt_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapMgmt_Object = MibScalar
agCurCfgSyslogTrapMgmt = _AgCurCfgSyslogTrapMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 6),
    _AgCurCfgSyslogTrapMgmt_Type()
)
agCurCfgSyslogTrapMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapMgmt.setStatus("mandatory")


class _AgNewCfgSyslogTrapCli_Type(Integer32):
    """Custom type agNewCfgSyslogTrapCli based on Integer32"""
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


_AgNewCfgSyslogTrapCli_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapCli_Object = MibScalar
agNewCfgSyslogTrapCli = _AgNewCfgSyslogTrapCli_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 7),
    _AgNewCfgSyslogTrapCli_Type()
)
agNewCfgSyslogTrapCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapCli.setStatus("mandatory")


class _AgCurCfgSyslogTrapCli_Type(Integer32):
    """Custom type agCurCfgSyslogTrapCli based on Integer32"""
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


_AgCurCfgSyslogTrapCli_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapCli_Object = MibScalar
agCurCfgSyslogTrapCli = _AgCurCfgSyslogTrapCli_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 8),
    _AgCurCfgSyslogTrapCli_Type()
)
agCurCfgSyslogTrapCli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapCli.setStatus("mandatory")


class _AgNewCfgSyslogTrapStp_Type(Integer32):
    """Custom type agNewCfgSyslogTrapStp based on Integer32"""
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


_AgNewCfgSyslogTrapStp_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapStp_Object = MibScalar
agNewCfgSyslogTrapStp = _AgNewCfgSyslogTrapStp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 9),
    _AgNewCfgSyslogTrapStp_Type()
)
agNewCfgSyslogTrapStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapStp.setStatus("mandatory")


class _AgCurCfgSyslogTrapStp_Type(Integer32):
    """Custom type agCurCfgSyslogTrapStp based on Integer32"""
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


_AgCurCfgSyslogTrapStp_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapStp_Object = MibScalar
agCurCfgSyslogTrapStp = _AgCurCfgSyslogTrapStp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 10),
    _AgCurCfgSyslogTrapStp_Type()
)
agCurCfgSyslogTrapStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapStp.setStatus("mandatory")


class _AgNewCfgSyslogTrapVlan_Type(Integer32):
    """Custom type agNewCfgSyslogTrapVlan based on Integer32"""
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


_AgNewCfgSyslogTrapVlan_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapVlan_Object = MibScalar
agNewCfgSyslogTrapVlan = _AgNewCfgSyslogTrapVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 11),
    _AgNewCfgSyslogTrapVlan_Type()
)
agNewCfgSyslogTrapVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapVlan.setStatus("mandatory")


class _AgCurCfgSyslogTrapVlan_Type(Integer32):
    """Custom type agCurCfgSyslogTrapVlan based on Integer32"""
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


_AgCurCfgSyslogTrapVlan_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapVlan_Object = MibScalar
agCurCfgSyslogTrapVlan = _AgCurCfgSyslogTrapVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 12),
    _AgCurCfgSyslogTrapVlan_Type()
)
agCurCfgSyslogTrapVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapVlan.setStatus("mandatory")


class _AgNewCfgSyslogTrapSlb_Type(Integer32):
    """Custom type agNewCfgSyslogTrapSlb based on Integer32"""
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


_AgNewCfgSyslogTrapSlb_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapSlb_Object = MibScalar
agNewCfgSyslogTrapSlb = _AgNewCfgSyslogTrapSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 13),
    _AgNewCfgSyslogTrapSlb_Type()
)
agNewCfgSyslogTrapSlb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSlb.setStatus("mandatory")


class _AgCurCfgSyslogTrapSlb_Type(Integer32):
    """Custom type agCurCfgSyslogTrapSlb based on Integer32"""
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


_AgCurCfgSyslogTrapSlb_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapSlb_Object = MibScalar
agCurCfgSyslogTrapSlb = _AgCurCfgSyslogTrapSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 14),
    _AgCurCfgSyslogTrapSlb_Type()
)
agCurCfgSyslogTrapSlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSlb.setStatus("mandatory")


class _AgNewCfgSyslogTrapGslb_Type(Integer32):
    """Custom type agNewCfgSyslogTrapGslb based on Integer32"""
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


_AgNewCfgSyslogTrapGslb_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapGslb_Object = MibScalar
agNewCfgSyslogTrapGslb = _AgNewCfgSyslogTrapGslb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 15),
    _AgNewCfgSyslogTrapGslb_Type()
)
agNewCfgSyslogTrapGslb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapGslb.setStatus("mandatory")


class _AgCurCfgSyslogTrapGslb_Type(Integer32):
    """Custom type agCurCfgSyslogTrapGslb based on Integer32"""
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


_AgCurCfgSyslogTrapGslb_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapGslb_Object = MibScalar
agCurCfgSyslogTrapGslb = _AgCurCfgSyslogTrapGslb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 16),
    _AgCurCfgSyslogTrapGslb_Type()
)
agCurCfgSyslogTrapGslb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapGslb.setStatus("mandatory")


class _AgNewCfgSyslogTrapFilter_Type(Integer32):
    """Custom type agNewCfgSyslogTrapFilter based on Integer32"""
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


_AgNewCfgSyslogTrapFilter_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapFilter_Object = MibScalar
agNewCfgSyslogTrapFilter = _AgNewCfgSyslogTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 17),
    _AgNewCfgSyslogTrapFilter_Type()
)
agNewCfgSyslogTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapFilter.setStatus("mandatory")


class _AgCurCfgSyslogTrapFilter_Type(Integer32):
    """Custom type agCurCfgSyslogTrapFilter based on Integer32"""
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


_AgCurCfgSyslogTrapFilter_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapFilter_Object = MibScalar
agCurCfgSyslogTrapFilter = _AgCurCfgSyslogTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 18),
    _AgCurCfgSyslogTrapFilter_Type()
)
agCurCfgSyslogTrapFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapFilter.setStatus("mandatory")


class _AgNewCfgSyslogTrapSsh_Type(Integer32):
    """Custom type agNewCfgSyslogTrapSsh based on Integer32"""
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


_AgNewCfgSyslogTrapSsh_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapSsh_Object = MibScalar
agNewCfgSyslogTrapSsh = _AgNewCfgSyslogTrapSsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 19),
    _AgNewCfgSyslogTrapSsh_Type()
)
agNewCfgSyslogTrapSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSsh.setStatus("mandatory")


class _AgCurCfgSyslogTrapSsh_Type(Integer32):
    """Custom type agCurCfgSyslogTrapSsh based on Integer32"""
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


_AgCurCfgSyslogTrapSsh_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapSsh_Object = MibScalar
agCurCfgSyslogTrapSsh = _AgCurCfgSyslogTrapSsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 20),
    _AgCurCfgSyslogTrapSsh_Type()
)
agCurCfgSyslogTrapSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSsh.setStatus("mandatory")


class _AgNewCfgSyslogTrapVrrp_Type(Integer32):
    """Custom type agNewCfgSyslogTrapVrrp based on Integer32"""
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


_AgNewCfgSyslogTrapVrrp_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapVrrp_Object = MibScalar
agNewCfgSyslogTrapVrrp = _AgNewCfgSyslogTrapVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 21),
    _AgNewCfgSyslogTrapVrrp_Type()
)
agNewCfgSyslogTrapVrrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapVrrp.setStatus("mandatory")


class _AgCurCfgSyslogTrapVrrp_Type(Integer32):
    """Custom type agCurCfgSyslogTrapVrrp based on Integer32"""
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


_AgCurCfgSyslogTrapVrrp_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapVrrp_Object = MibScalar
agCurCfgSyslogTrapVrrp = _AgCurCfgSyslogTrapVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 22),
    _AgCurCfgSyslogTrapVrrp_Type()
)
agCurCfgSyslogTrapVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapVrrp.setStatus("mandatory")


class _AgNewCfgSyslogTrapBgp_Type(Integer32):
    """Custom type agNewCfgSyslogTrapBgp based on Integer32"""
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


_AgNewCfgSyslogTrapBgp_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapBgp_Object = MibScalar
agNewCfgSyslogTrapBgp = _AgNewCfgSyslogTrapBgp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 23),
    _AgNewCfgSyslogTrapBgp_Type()
)
agNewCfgSyslogTrapBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapBgp.setStatus("mandatory")


class _AgCurCfgSyslogTrapBgp_Type(Integer32):
    """Custom type agCurCfgSyslogTrapBgp based on Integer32"""
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


_AgCurCfgSyslogTrapBgp_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapBgp_Object = MibScalar
agCurCfgSyslogTrapBgp = _AgCurCfgSyslogTrapBgp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 24),
    _AgCurCfgSyslogTrapBgp_Type()
)
agCurCfgSyslogTrapBgp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapBgp.setStatus("mandatory")


class _AgNewCfgSyslogTrapNtp_Type(Integer32):
    """Custom type agNewCfgSyslogTrapNtp based on Integer32"""
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


_AgNewCfgSyslogTrapNtp_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapNtp_Object = MibScalar
agNewCfgSyslogTrapNtp = _AgNewCfgSyslogTrapNtp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 25),
    _AgNewCfgSyslogTrapNtp_Type()
)
agNewCfgSyslogTrapNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapNtp.setStatus("mandatory")


class _AgCurCfgSyslogTrapNtp_Type(Integer32):
    """Custom type agCurCfgSyslogTrapNtp based on Integer32"""
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


_AgCurCfgSyslogTrapNtp_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapNtp_Object = MibScalar
agCurCfgSyslogTrapNtp = _AgCurCfgSyslogTrapNtp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 26),
    _AgCurCfgSyslogTrapNtp_Type()
)
agCurCfgSyslogTrapNtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapNtp.setStatus("mandatory")


class _AgNewCfgSyslogTrapIsd_Type(Integer32):
    """Custom type agNewCfgSyslogTrapIsd based on Integer32"""
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


_AgNewCfgSyslogTrapIsd_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapIsd_Object = MibScalar
agNewCfgSyslogTrapIsd = _AgNewCfgSyslogTrapIsd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 27),
    _AgNewCfgSyslogTrapIsd_Type()
)
agNewCfgSyslogTrapIsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapIsd.setStatus("mandatory")


class _AgCurCfgSyslogTrapIsd_Type(Integer32):
    """Custom type agCurCfgSyslogTrapIsd based on Integer32"""
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


_AgCurCfgSyslogTrapIsd_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapIsd_Object = MibScalar
agCurCfgSyslogTrapIsd = _AgCurCfgSyslogTrapIsd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 28),
    _AgCurCfgSyslogTrapIsd_Type()
)
agCurCfgSyslogTrapIsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapIsd.setStatus("mandatory")


class _AgNewCfgSyslogTrapIp_Type(Integer32):
    """Custom type agNewCfgSyslogTrapIp based on Integer32"""
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


_AgNewCfgSyslogTrapIp_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapIp_Object = MibScalar
agNewCfgSyslogTrapIp = _AgNewCfgSyslogTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 31),
    _AgNewCfgSyslogTrapIp_Type()
)
agNewCfgSyslogTrapIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapIp.setStatus("mandatory")


class _AgCurCfgSyslogTrapIp_Type(Integer32):
    """Custom type agCurCfgSyslogTrapIp based on Integer32"""
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


_AgCurCfgSyslogTrapIp_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapIp_Object = MibScalar
agCurCfgSyslogTrapIp = _AgCurCfgSyslogTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 32),
    _AgCurCfgSyslogTrapIp_Type()
)
agCurCfgSyslogTrapIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapIp.setStatus("mandatory")


class _AgNewCfgSyslogTrapWeb_Type(Integer32):
    """Custom type agNewCfgSyslogTrapWeb based on Integer32"""
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


_AgNewCfgSyslogTrapWeb_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapWeb_Object = MibScalar
agNewCfgSyslogTrapWeb = _AgNewCfgSyslogTrapWeb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 35),
    _AgNewCfgSyslogTrapWeb_Type()
)
agNewCfgSyslogTrapWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapWeb.setStatus("mandatory")


class _AgCurCfgSyslogTrapWeb_Type(Integer32):
    """Custom type agCurCfgSyslogTrapWeb based on Integer32"""
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


_AgCurCfgSyslogTrapWeb_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapWeb_Object = MibScalar
agCurCfgSyslogTrapWeb = _AgCurCfgSyslogTrapWeb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 36),
    _AgCurCfgSyslogTrapWeb_Type()
)
agCurCfgSyslogTrapWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapWeb.setStatus("mandatory")


class _AgNewCfgSyslogTrapSynAtk_Type(Integer32):
    """Custom type agNewCfgSyslogTrapSynAtk based on Integer32"""
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


_AgNewCfgSyslogTrapSynAtk_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapSynAtk_Object = MibScalar
agNewCfgSyslogTrapSynAtk = _AgNewCfgSyslogTrapSynAtk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 37),
    _AgNewCfgSyslogTrapSynAtk_Type()
)
agNewCfgSyslogTrapSynAtk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSynAtk.setStatus("mandatory")


class _AgCurCfgSyslogTrapSynAtk_Type(Integer32):
    """Custom type agCurCfgSyslogTrapSynAtk based on Integer32"""
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


_AgCurCfgSyslogTrapSynAtk_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapSynAtk_Object = MibScalar
agCurCfgSyslogTrapSynAtk = _AgCurCfgSyslogTrapSynAtk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 38),
    _AgCurCfgSyslogTrapSynAtk_Type()
)
agCurCfgSyslogTrapSynAtk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSynAtk.setStatus("mandatory")


class _AgNewCfgSyslogTrapTcpLim_Type(Integer32):
    """Custom type agNewCfgSyslogTrapTcpLim based on Integer32"""
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


_AgNewCfgSyslogTrapTcpLim_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapTcpLim_Object = MibScalar
agNewCfgSyslogTrapTcpLim = _AgNewCfgSyslogTrapTcpLim_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 39),
    _AgNewCfgSyslogTrapTcpLim_Type()
)
agNewCfgSyslogTrapTcpLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapTcpLim.setStatus("mandatory")


class _AgCurCfgSyslogTrapTcpLim_Type(Integer32):
    """Custom type agCurCfgSyslogTrapTcpLim based on Integer32"""
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


_AgCurCfgSyslogTrapTcpLim_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapTcpLim_Object = MibScalar
agCurCfgSyslogTrapTcpLim = _AgCurCfgSyslogTrapTcpLim_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 2, 29, 40),
    _AgCurCfgSyslogTrapTcpLim_Type()
)
agCurCfgSyslogTrapTcpLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapTcpLim.setStatus("mandatory")
_Stats_ObjectIdentity = ObjectIdentity
stats = _Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8)
)
_MemStats_ObjectIdentity = ObjectIdentity
memStats = _MemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12)
)
_MemStatsAllocs_Type = Counter32
_MemStatsAllocs_Object = MibScalar
memStatsAllocs = _MemStatsAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12, 1),
    _MemStatsAllocs_Type()
)
memStatsAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatsAllocs.setStatus("mandatory")
_MemStatsFrees_Type = Counter32
_MemStatsFrees_Object = MibScalar
memStatsFrees = _MemStatsFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12, 2),
    _MemStatsFrees_Type()
)
memStatsFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatsFrees.setStatus("mandatory")
_MemStatsAllocFails_Type = Counter32
_MemStatsAllocFails_Object = MibScalar
memStatsAllocFails = _MemStatsAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12, 3),
    _MemStatsAllocFails_Type()
)
memStatsAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatsAllocFails.setStatus("mandatory")
_MemStatsBytesCurr_Type = Gauge32
_MemStatsBytesCurr_Object = MibScalar
memStatsBytesCurr = _MemStatsBytesCurr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12, 4),
    _MemStatsBytesCurr_Type()
)
memStatsBytesCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatsBytesCurr.setStatus("mandatory")
_MemStatsBytesHiwat_Type = Gauge32
_MemStatsBytesHiwat_Object = MibScalar
memStatsBytesHiwat = _MemStatsBytesHiwat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12, 5),
    _MemStatsBytesHiwat_Type()
)
memStatsBytesHiwat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatsBytesHiwat.setStatus("mandatory")
_MemStatsPoolBytes_Type = Gauge32
_MemStatsPoolBytes_Object = MibScalar
memStatsPoolBytes = _MemStatsPoolBytes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12, 6),
    _MemStatsPoolBytes_Type()
)
memStatsPoolBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatsPoolBytes.setStatus("mandatory")
_MemStatsLargest_Type = Gauge32
_MemStatsLargest_Object = MibScalar
memStatsLargest = _MemStatsLargest_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 12, 7),
    _MemStatsLargest_Type()
)
memStatsLargest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatsLargest.setStatus("mandatory")
_PktStats_ObjectIdentity = ObjectIdentity
pktStats = _PktStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 13)
)
_PktStatsAllocs_Type = Counter32
_PktStatsAllocs_Object = MibScalar
pktStatsAllocs = _PktStatsAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 13, 1),
    _PktStatsAllocs_Type()
)
pktStatsAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsAllocs.setStatus("mandatory")
_PktStatsFrees_Type = Counter32
_PktStatsFrees_Object = MibScalar
pktStatsFrees = _PktStatsFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 13, 2),
    _PktStatsFrees_Type()
)
pktStatsFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsFrees.setStatus("mandatory")
_PktStatsAllocFails_Type = Counter32
_PktStatsAllocFails_Object = MibScalar
pktStatsAllocFails = _PktStatsAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 13, 3),
    _PktStatsAllocFails_Type()
)
pktStatsAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsAllocFails.setStatus("mandatory")
_PktStatsMediums_Type = Counter32
_PktStatsMediums_Object = MibScalar
pktStatsMediums = _PktStatsMediums_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 13, 4),
    _PktStatsMediums_Type()
)
pktStatsMediums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsMediums.setStatus("mandatory")
_PktStatsJumbos_Type = Counter32
_PktStatsJumbos_Object = MibScalar
pktStatsJumbos = _PktStatsJumbos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 13, 5),
    _PktStatsJumbos_Type()
)
pktStatsJumbos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsJumbos.setStatus("mandatory")
_PktStatsSmalls_Type = Counter32
_PktStatsSmalls_Object = MibScalar
pktStatsSmalls = _PktStatsSmalls_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 13, 6),
    _PktStatsSmalls_Type()
)
pktStatsSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsSmalls.setStatus("mandatory")
_MpCpuStats_ObjectIdentity = ObjectIdentity
mpCpuStats = _MpCpuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 16)
)
_MpCpuAStatsUtil1Second_Type = Integer32
_MpCpuAStatsUtil1Second_Object = MibScalar
mpCpuAStatsUtil1Second = _MpCpuAStatsUtil1Second_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 16, 1),
    _MpCpuAStatsUtil1Second_Type()
)
mpCpuAStatsUtil1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuAStatsUtil1Second.setStatus("mandatory")
_MpCpuBStatsUtil1Second_Type = Integer32
_MpCpuBStatsUtil1Second_Object = MibScalar
mpCpuBStatsUtil1Second = _MpCpuBStatsUtil1Second_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 16, 2),
    _MpCpuBStatsUtil1Second_Type()
)
mpCpuBStatsUtil1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuBStatsUtil1Second.setStatus("mandatory")
_MpCpuAStatsUtil4Seconds_Type = Integer32
_MpCpuAStatsUtil4Seconds_Object = MibScalar
mpCpuAStatsUtil4Seconds = _MpCpuAStatsUtil4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 16, 3),
    _MpCpuAStatsUtil4Seconds_Type()
)
mpCpuAStatsUtil4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuAStatsUtil4Seconds.setStatus("mandatory")
_MpCpuBStatsUtil4Seconds_Type = Integer32
_MpCpuBStatsUtil4Seconds_Object = MibScalar
mpCpuBStatsUtil4Seconds = _MpCpuBStatsUtil4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 16, 4),
    _MpCpuBStatsUtil4Seconds_Type()
)
mpCpuBStatsUtil4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuBStatsUtil4Seconds.setStatus("mandatory")
_MpCpuAStatsUtil64Seconds_Type = Integer32
_MpCpuAStatsUtil64Seconds_Object = MibScalar
mpCpuAStatsUtil64Seconds = _MpCpuAStatsUtil64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 16, 5),
    _MpCpuAStatsUtil64Seconds_Type()
)
mpCpuAStatsUtil64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuAStatsUtil64Seconds.setStatus("mandatory")
_MpCpuBStatsUtil64Seconds_Type = Integer32
_MpCpuBStatsUtil64Seconds_Object = MibScalar
mpCpuBStatsUtil64Seconds = _MpCpuBStatsUtil64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 16, 6),
    _MpCpuBStatsUtil64Seconds_Type()
)
mpCpuBStatsUtil64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuBStatsUtil64Seconds.setStatus("mandatory")
_Information_ObjectIdentity = ObjectIdentity
information = _Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9)
)
_AltswitchTraps_ObjectIdentity = ObjectIdentity
altswitchTraps = _AltswitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13)
)
_OperCmds_ObjectIdentity = ObjectIdentity
operCmds = _OperCmds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14)
)
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16)
)
_RadCurCfgPrimaryIpAddr_Type = IpAddress
_RadCurCfgPrimaryIpAddr_Object = MibScalar
radCurCfgPrimaryIpAddr = _RadCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 1),
    _RadCurCfgPrimaryIpAddr_Type()
)
radCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgPrimaryIpAddr.setStatus("mandatory")
_RadNewCfgPrimaryIpAddr_Type = IpAddress
_RadNewCfgPrimaryIpAddr_Object = MibScalar
radNewCfgPrimaryIpAddr = _RadNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 2),
    _RadNewCfgPrimaryIpAddr_Type()
)
radNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgPrimaryIpAddr.setStatus("mandatory")
_RadCurCfgSecondaryIpAddr_Type = IpAddress
_RadCurCfgSecondaryIpAddr_Object = MibScalar
radCurCfgSecondaryIpAddr = _RadCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 3),
    _RadCurCfgSecondaryIpAddr_Type()
)
radCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgSecondaryIpAddr.setStatus("mandatory")
_RadNewCfgSecondaryIpAddr_Type = IpAddress
_RadNewCfgSecondaryIpAddr_Object = MibScalar
radNewCfgSecondaryIpAddr = _RadNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 4),
    _RadNewCfgSecondaryIpAddr_Type()
)
radNewCfgSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgSecondaryIpAddr.setStatus("mandatory")


class _RadCurCfgPort_Type(Integer32):
    """Custom type radCurCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 3000),
    )


_RadCurCfgPort_Type.__name__ = "Integer32"
_RadCurCfgPort_Object = MibScalar
radCurCfgPort = _RadCurCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 5),
    _RadCurCfgPort_Type()
)
radCurCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgPort.setStatus("mandatory")


class _RadNewCfgPort_Type(Integer32):
    """Custom type radNewCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 3000),
    )


_RadNewCfgPort_Type.__name__ = "Integer32"
_RadNewCfgPort_Object = MibScalar
radNewCfgPort = _RadNewCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 6),
    _RadNewCfgPort_Type()
)
radNewCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgPort.setStatus("mandatory")


class _RadCurCfgTimeout_Type(Integer32):
    """Custom type radCurCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadCurCfgTimeout_Type.__name__ = "Integer32"
_RadCurCfgTimeout_Object = MibScalar
radCurCfgTimeout = _RadCurCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 7),
    _RadCurCfgTimeout_Type()
)
radCurCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgTimeout.setStatus("mandatory")


class _RadNewCfgTimeout_Type(Integer32):
    """Custom type radNewCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadNewCfgTimeout_Type.__name__ = "Integer32"
_RadNewCfgTimeout_Object = MibScalar
radNewCfgTimeout = _RadNewCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 8),
    _RadNewCfgTimeout_Type()
)
radNewCfgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgTimeout.setStatus("mandatory")


class _RadCurCfgRetries_Type(Integer32):
    """Custom type radCurCfgRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RadCurCfgRetries_Type.__name__ = "Integer32"
_RadCurCfgRetries_Object = MibScalar
radCurCfgRetries = _RadCurCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 9),
    _RadCurCfgRetries_Type()
)
radCurCfgRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgRetries.setStatus("mandatory")


class _RadNewCfgRetries_Type(Integer32):
    """Custom type radNewCfgRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RadNewCfgRetries_Type.__name__ = "Integer32"
_RadNewCfgRetries_Object = MibScalar
radNewCfgRetries = _RadNewCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 10),
    _RadNewCfgRetries_Type()
)
radNewCfgRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgRetries.setStatus("mandatory")


class _RadCurCfgState_Type(Integer32):
    """Custom type radCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_RadCurCfgState_Type.__name__ = "Integer32"
_RadCurCfgState_Object = MibScalar
radCurCfgState = _RadCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 11),
    _RadCurCfgState_Type()
)
radCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgState.setStatus("mandatory")


class _RadNewCfgState_Type(Integer32):
    """Custom type radNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_RadNewCfgState_Type.__name__ = "Integer32"
_RadNewCfgState_Object = MibScalar
radNewCfgState = _RadNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 12),
    _RadNewCfgState_Type()
)
radNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgState.setStatus("mandatory")


class _RadCurCfgAuthenString_Type(DisplayString):
    """Custom type radCurCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadCurCfgAuthenString_Type.__name__ = "DisplayString"
_RadCurCfgAuthenString_Object = MibScalar
radCurCfgAuthenString = _RadCurCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 13),
    _RadCurCfgAuthenString_Type()
)
radCurCfgAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgAuthenString.setStatus("mandatory")


class _RadNewCfgAuthenString_Type(DisplayString):
    """Custom type radNewCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadNewCfgAuthenString_Type.__name__ = "DisplayString"
_RadNewCfgAuthenString_Object = MibScalar
radNewCfgAuthenString = _RadNewCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 14),
    _RadNewCfgAuthenString_Type()
)
radNewCfgAuthenString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgAuthenString.setStatus("mandatory")


class _RadCurCfgTelnet_Type(Integer32):
    """Custom type radCurCfgTelnet based on Integer32"""
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


_RadCurCfgTelnet_Type.__name__ = "Integer32"
_RadCurCfgTelnet_Object = MibScalar
radCurCfgTelnet = _RadCurCfgTelnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 15),
    _RadCurCfgTelnet_Type()
)
radCurCfgTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgTelnet.setStatus("mandatory")


class _RadNewCfgTelnet_Type(Integer32):
    """Custom type radNewCfgTelnet based on Integer32"""
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


_RadNewCfgTelnet_Type.__name__ = "Integer32"
_RadNewCfgTelnet_Object = MibScalar
radNewCfgTelnet = _RadNewCfgTelnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 16, 16),
    _RadNewCfgTelnet_Type()
)
radNewCfgTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgTelnet.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-TIGON-SWITCH-MIB",
    **{"hardware": hardware,
       "hwPartNumber": hwPartNumber,
       "hwRevision": hwRevision,
       "hwPowerSupplyStatus": hwPowerSupplyStatus,
       "hwRedundantPSPresent": hwRedundantPSPresent,
       "hwRedundantPSStatus": hwRedundantPSStatus,
       "hwSensor1Temp": hwSensor1Temp,
       "hwSensor2Temp": hwSensor2Temp,
       "hwSensor3Temp": hwSensor3Temp,
       "hwSensor4Temp": hwSensor4Temp,
       "agent": agent,
       "agGeneral": agGeneral,
       "agSaveConfiguration": agSaveConfiguration,
       "agApplyConfiguration": agApplyConfiguration,
       "agApplyPending": agApplyPending,
       "agReset": agReset,
       "agConfigForNxtReset": agConfigForNxtReset,
       "agImageForNxtReset": agImageForNxtReset,
       "agSoftwareVersion": agSoftwareVersion,
       "agBootVer": agBootVer,
       "agImage1Ver": agImage1Ver,
       "agImage2Ver": agImage2Ver,
       "agRtcDate": agRtcDate,
       "agRtcTime": agRtcTime,
       "agTftpServerIpAddr": agTftpServerIpAddr,
       "agTftpImageFileName": agTftpImageFileName,
       "agTftpImage": agTftpImage,
       "agTftpDownload": agTftpDownload,
       "agLastSetErrorReason": agLastSetErrorReason,
       "agTftpServer": agTftpServer,
       "agTftpCfgFileName": agTftpCfgFileName,
       "agTftpDumpFileName": agTftpDumpFileName,
       "agTftpAction": agTftpAction,
       "agTftpLastActionStatus": agTftpLastActionStatus,
       "agRevert": agRevert,
       "agRevertApply": agRevertApply,
       "agEnabledSwFeatures": agEnabledSwFeatures,
       "agClrSyslogMsgs": agClrSyslogMsgs,
       "agSavePending": agSavePending,
       "agEnabledGslbKey": agEnabledGslbKey,
       "agEnabledBwmKey": agEnabledBwmKey,
       "agSlotNumber": agSlotNumber,
       "agEnabledRurlKey": agEnabledRurlKey,
       "agGeneralConfig": agGeneralConfig,
       "agNewCfgSyslogHost": agNewCfgSyslogHost,
       "agCurCfgSyslogHost": agCurCfgSyslogHost,
       "agNewCfgBootp": agNewCfgBootp,
       "agCurCfgBootp": agCurCfgBootp,
       "agNewCfgSpanningTree": agNewCfgSpanningTree,
       "agCurCfgSpanningTree": agCurCfgSpanningTree,
       "agTrapHostTableMaxEnt": agTrapHostTableMaxEnt,
       "agCurCfgTrapHostTable": agCurCfgTrapHostTable,
       "agCurCfgTrapHostEntry": agCurCfgTrapHostEntry,
       "agCurCfgTrapHostIndx": agCurCfgTrapHostIndx,
       "agCurCfgTrapHostIpAddr": agCurCfgTrapHostIpAddr,
       "agCurCfgTrapHostCommString": agCurCfgTrapHostCommString,
       "agNewCfgTrapHostTable": agNewCfgTrapHostTable,
       "agNewCfgTrapHostEntry": agNewCfgTrapHostEntry,
       "agNewCfgTrapHostIndx": agNewCfgTrapHostIndx,
       "agNewCfgTrapHostIpAddr": agNewCfgTrapHostIpAddr,
       "agNewCfgTrapHostCommString": agNewCfgTrapHostCommString,
       "agCurCfgHttpServerPort": agCurCfgHttpServerPort,
       "agNewCfgHttpServerPort": agNewCfgHttpServerPort,
       "agCurCfgLoginBanner": agCurCfgLoginBanner,
       "agNewCfgLoginBanner": agNewCfgLoginBanner,
       "agNewCfgSyslog2Host": agNewCfgSyslog2Host,
       "agCurCfgSyslog2Host": agCurCfgSyslog2Host,
       "agCurCfgSyslogFac": agCurCfgSyslogFac,
       "agNewCfgSyslogFac": agNewCfgSyslogFac,
       "agCurCfgSyslog2Fac": agCurCfgSyslog2Fac,
       "agNewCfgSyslog2Fac": agNewCfgSyslog2Fac,
       "agCurCfgSmtpHost": agCurCfgSmtpHost,
       "agNewCfgSmtpHost": agNewCfgSmtpHost,
       "agCurCfgConsole": agCurCfgConsole,
       "agNewCfgConsole": agNewCfgConsole,
       "agCurCfgMgmtNetwork": agCurCfgMgmtNetwork,
       "agNewCfgMgmtNetwork": agNewCfgMgmtNetwork,
       "agCurCfgMgmtMask": agCurCfgMgmtMask,
       "agNewCfgMgmtMask": agNewCfgMgmtMask,
       "agNTP": agNTP,
       "agCurCfgNTPServer": agCurCfgNTPServer,
       "agNewCfgNTPServer": agNewCfgNTPServer,
       "agCurCfgNTPResyncInterval": agCurCfgNTPResyncInterval,
       "agNewCfgNTPResyncInterval": agNewCfgNTPResyncInterval,
       "agCurCfgNTPTzone": agCurCfgNTPTzone,
       "agNewCfgNTPTzone": agNewCfgNTPTzone,
       "agCurCfgNTPDlight": agCurCfgNTPDlight,
       "agNewCfgNTPDlight": agNewCfgNTPDlight,
       "agCurCfgNTPService": agCurCfgNTPService,
       "agNewCfgNTPService": agNewCfgNTPService,
       "agLog": agLog,
       "agNewCfgSyslogTrapConsole": agNewCfgSyslogTrapConsole,
       "agCurCfgSyslogTrapConsole": agCurCfgSyslogTrapConsole,
       "agNewCfgSyslogTrapSystem": agNewCfgSyslogTrapSystem,
       "agCurCfgSyslogTrapSystem": agCurCfgSyslogTrapSystem,
       "agNewCfgSyslogTrapMgmt": agNewCfgSyslogTrapMgmt,
       "agCurCfgSyslogTrapMgmt": agCurCfgSyslogTrapMgmt,
       "agNewCfgSyslogTrapCli": agNewCfgSyslogTrapCli,
       "agCurCfgSyslogTrapCli": agCurCfgSyslogTrapCli,
       "agNewCfgSyslogTrapStp": agNewCfgSyslogTrapStp,
       "agCurCfgSyslogTrapStp": agCurCfgSyslogTrapStp,
       "agNewCfgSyslogTrapVlan": agNewCfgSyslogTrapVlan,
       "agCurCfgSyslogTrapVlan": agCurCfgSyslogTrapVlan,
       "agNewCfgSyslogTrapSlb": agNewCfgSyslogTrapSlb,
       "agCurCfgSyslogTrapSlb": agCurCfgSyslogTrapSlb,
       "agNewCfgSyslogTrapGslb": agNewCfgSyslogTrapGslb,
       "agCurCfgSyslogTrapGslb": agCurCfgSyslogTrapGslb,
       "agNewCfgSyslogTrapFilter": agNewCfgSyslogTrapFilter,
       "agCurCfgSyslogTrapFilter": agCurCfgSyslogTrapFilter,
       "agNewCfgSyslogTrapSsh": agNewCfgSyslogTrapSsh,
       "agCurCfgSyslogTrapSsh": agCurCfgSyslogTrapSsh,
       "agNewCfgSyslogTrapVrrp": agNewCfgSyslogTrapVrrp,
       "agCurCfgSyslogTrapVrrp": agCurCfgSyslogTrapVrrp,
       "agNewCfgSyslogTrapBgp": agNewCfgSyslogTrapBgp,
       "agCurCfgSyslogTrapBgp": agCurCfgSyslogTrapBgp,
       "agNewCfgSyslogTrapNtp": agNewCfgSyslogTrapNtp,
       "agCurCfgSyslogTrapNtp": agCurCfgSyslogTrapNtp,
       "agNewCfgSyslogTrapIsd": agNewCfgSyslogTrapIsd,
       "agCurCfgSyslogTrapIsd": agCurCfgSyslogTrapIsd,
       "agNewCfgSyslogTrapIp": agNewCfgSyslogTrapIp,
       "agCurCfgSyslogTrapIp": agCurCfgSyslogTrapIp,
       "agNewCfgSyslogTrapWeb": agNewCfgSyslogTrapWeb,
       "agCurCfgSyslogTrapWeb": agCurCfgSyslogTrapWeb,
       "agNewCfgSyslogTrapSynAtk": agNewCfgSyslogTrapSynAtk,
       "agCurCfgSyslogTrapSynAtk": agCurCfgSyslogTrapSynAtk,
       "agNewCfgSyslogTrapTcpLim": agNewCfgSyslogTrapTcpLim,
       "agCurCfgSyslogTrapTcpLim": agCurCfgSyslogTrapTcpLim,
       "stats": stats,
       "memStats": memStats,
       "memStatsAllocs": memStatsAllocs,
       "memStatsFrees": memStatsFrees,
       "memStatsAllocFails": memStatsAllocFails,
       "memStatsBytesCurr": memStatsBytesCurr,
       "memStatsBytesHiwat": memStatsBytesHiwat,
       "memStatsPoolBytes": memStatsPoolBytes,
       "memStatsLargest": memStatsLargest,
       "pktStats": pktStats,
       "pktStatsAllocs": pktStatsAllocs,
       "pktStatsFrees": pktStatsFrees,
       "pktStatsAllocFails": pktStatsAllocFails,
       "pktStatsMediums": pktStatsMediums,
       "pktStatsJumbos": pktStatsJumbos,
       "pktStatsSmalls": pktStatsSmalls,
       "mpCpuStats": mpCpuStats,
       "mpCpuAStatsUtil1Second": mpCpuAStatsUtil1Second,
       "mpCpuBStatsUtil1Second": mpCpuBStatsUtil1Second,
       "mpCpuAStatsUtil4Seconds": mpCpuAStatsUtil4Seconds,
       "mpCpuBStatsUtil4Seconds": mpCpuBStatsUtil4Seconds,
       "mpCpuAStatsUtil64Seconds": mpCpuAStatsUtil64Seconds,
       "mpCpuBStatsUtil64Seconds": mpCpuBStatsUtil64Seconds,
       "information": information,
       "altswitchTraps": altswitchTraps,
       "operCmds": operCmds,
       "radius": radius,
       "radCurCfgPrimaryIpAddr": radCurCfgPrimaryIpAddr,
       "radNewCfgPrimaryIpAddr": radNewCfgPrimaryIpAddr,
       "radCurCfgSecondaryIpAddr": radCurCfgSecondaryIpAddr,
       "radNewCfgSecondaryIpAddr": radNewCfgSecondaryIpAddr,
       "radCurCfgPort": radCurCfgPort,
       "radNewCfgPort": radNewCfgPort,
       "radCurCfgTimeout": radCurCfgTimeout,
       "radNewCfgTimeout": radNewCfgTimeout,
       "radCurCfgRetries": radCurCfgRetries,
       "radNewCfgRetries": radNewCfgRetries,
       "radCurCfgState": radCurCfgState,
       "radNewCfgState": radNewCfgState,
       "radCurCfgAuthenString": radCurCfgAuthenString,
       "radNewCfgAuthenString": radNewCfgAuthenString,
       "radCurCfgTelnet": radCurCfgTelnet,
       "radNewCfgTelnet": radNewCfgTelnet}
)
