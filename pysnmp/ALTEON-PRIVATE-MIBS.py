# SNMP MIB module (ALTEON-PRIVATE-MIBS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-PRIVATE-MIBS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:55 2024
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

_Alteon_ObjectIdentity = ObjectIdentity
alteon = _Alteon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872)
)
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1)
)
_Private_mibs_ObjectIdentity = ObjectIdentity
private_mibs = _Private_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1)
)
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyNeeded", 2),
          ("noApplyNeeded", 3),
          ("other", 1))
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
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("backup", 3),
          ("default", 4),
          ("other", 1))
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3),
          ("other", 1))
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3),
          ("other", 1))
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
_AgEnabledSwFeatures_Type = DisplayString
_AgEnabledSwFeatures_Object = MibScalar
agEnabledSwFeatures = _AgEnabledSwFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 1, 25),
    _AgEnabledSwFeatures_Type()
)
agEnabledSwFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledSwFeatures.setStatus("mandatory")
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
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
    (0, "ALTEON-PRIVATE-MIBS", "agCurCfgTrapHostIndx"),
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
    (0, "ALTEON-PRIVATE-MIBS", "agNewCfgTrapHostIndx"),
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
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
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
_AgNewCfgHttpServerPort_Type = Integer32
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
_AgPortConfig_ObjectIdentity = ObjectIdentity
agPortConfig = _AgPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3)
)
_AgPortTableMaxEnt_Type = Integer32
_AgPortTableMaxEnt_Object = MibScalar
agPortTableMaxEnt = _AgPortTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 1),
    _AgPortTableMaxEnt_Type()
)
agPortTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortTableMaxEnt.setStatus("mandatory")
_AgPortCurCfgTable_Object = MibTable
agPortCurCfgTable = _AgPortCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    agPortCurCfgTable.setStatus("mandatory")
_AgPortCurCfgTableEntry_Object = MibTableRow
agPortCurCfgTableEntry = _AgPortCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1)
)
agPortCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "agPortCurCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortCurCfgTableEntry.setStatus("mandatory")


class _AgPortCurCfgIndx_Type(Integer32):
    """Custom type agPortCurCfgIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgPortCurCfgIndx_Type.__name__ = "Integer32"
_AgPortCurCfgIndx_Object = MibTableColumn
agPortCurCfgIndx = _AgPortCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 1),
    _AgPortCurCfgIndx_Type()
)
agPortCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgIndx.setStatus("mandatory")


class _AgPortCurCfgPrefLink_Type(Integer32):
    """Custom type agPortCurCfgPrefLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3),
          ("other", 1))
    )


_AgPortCurCfgPrefLink_Type.__name__ = "Integer32"
_AgPortCurCfgPrefLink_Object = MibTableColumn
agPortCurCfgPrefLink = _AgPortCurCfgPrefLink_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 2),
    _AgPortCurCfgPrefLink_Type()
)
agPortCurCfgPrefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPrefLink.setStatus("mandatory")


class _AgPortCurCfgBackLink_Type(Integer32):
    """Custom type agPortCurCfgBackLink based on Integer32"""
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
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3),
          ("none", 4),
          ("other", 1))
    )


_AgPortCurCfgBackLink_Type.__name__ = "Integer32"
_AgPortCurCfgBackLink_Object = MibTableColumn
agPortCurCfgBackLink = _AgPortCurCfgBackLink_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 3),
    _AgPortCurCfgBackLink_Type()
)
agPortCurCfgBackLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgBackLink.setStatus("mandatory")


class _AgPortCurCfgState_Type(Integer32):
    """Custom type agPortCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_AgPortCurCfgState_Type.__name__ = "Integer32"
_AgPortCurCfgState_Object = MibTableColumn
agPortCurCfgState = _AgPortCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 4),
    _AgPortCurCfgState_Type()
)
agPortCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgState.setStatus("mandatory")


class _AgPortCurCfgVlanTag_Type(Integer32):
    """Custom type agPortCurCfgVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tagged", 2),
          ("untagged", 3))
    )


_AgPortCurCfgVlanTag_Type.__name__ = "Integer32"
_AgPortCurCfgVlanTag_Object = MibTableColumn
agPortCurCfgVlanTag = _AgPortCurCfgVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 5),
    _AgPortCurCfgVlanTag_Type()
)
agPortCurCfgVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgVlanTag.setStatus("mandatory")


class _AgPortCurCfgStp_Type(Integer32):
    """Custom type agPortCurCfgStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortCurCfgStp_Type.__name__ = "Integer32"
_AgPortCurCfgStp_Object = MibTableColumn
agPortCurCfgStp = _AgPortCurCfgStp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 6),
    _AgPortCurCfgStp_Type()
)
agPortCurCfgStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgStp.setStatus("mandatory")


class _AgPortCurCfgRmon_Type(Integer32):
    """Custom type agPortCurCfgRmon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortCurCfgRmon_Type.__name__ = "Integer32"
_AgPortCurCfgRmon_Object = MibTableColumn
agPortCurCfgRmon = _AgPortCurCfgRmon_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 7),
    _AgPortCurCfgRmon_Type()
)
agPortCurCfgRmon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgRmon.setStatus("mandatory")
_AgPortCurCfgPVID_Type = Integer32
_AgPortCurCfgPVID_Object = MibTableColumn
agPortCurCfgPVID = _AgPortCurCfgPVID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 8),
    _AgPortCurCfgPVID_Type()
)
agPortCurCfgPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPVID.setStatus("mandatory")


class _AgPortCurCfgFastEthAutoNeg_Type(Integer32):
    """Custom type agPortCurCfgFastEthAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortCurCfgFastEthAutoNeg_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthAutoNeg_Object = MibTableColumn
agPortCurCfgFastEthAutoNeg = _AgPortCurCfgFastEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 9),
    _AgPortCurCfgFastEthAutoNeg_Type()
)
agPortCurCfgFastEthAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthAutoNeg.setStatus("mandatory")


class _AgPortCurCfgFastEthSpeed_Type(Integer32):
    """Custom type agPortCurCfgFastEthSpeed based on Integer32"""
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
        *(("mbs10", 2),
          ("mbs100", 3),
          ("mbs10or100", 4),
          ("other", 1))
    )


_AgPortCurCfgFastEthSpeed_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthSpeed_Object = MibTableColumn
agPortCurCfgFastEthSpeed = _AgPortCurCfgFastEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 10),
    _AgPortCurCfgFastEthSpeed_Type()
)
agPortCurCfgFastEthSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthSpeed.setStatus("mandatory")


class _AgPortCurCfgFastEthMode_Type(Integer32):
    """Custom type agPortCurCfgFastEthMode based on Integer32"""
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
        *(("full-duplex", 2),
          ("full-or-half-duplex", 4),
          ("half-duplex", 3),
          ("other", 1))
    )


_AgPortCurCfgFastEthMode_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthMode_Object = MibTableColumn
agPortCurCfgFastEthMode = _AgPortCurCfgFastEthMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 11),
    _AgPortCurCfgFastEthMode_Type()
)
agPortCurCfgFastEthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthMode.setStatus("mandatory")


class _AgPortCurCfgFastEthFctl_Type(Integer32):
    """Custom type agPortCurCfgFastEthFctl based on Integer32"""
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
        *(("both", 4),
          ("none", 5),
          ("other", 1),
          ("receive", 3),
          ("transmit", 2))
    )


_AgPortCurCfgFastEthFctl_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthFctl_Object = MibTableColumn
agPortCurCfgFastEthFctl = _AgPortCurCfgFastEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 12),
    _AgPortCurCfgFastEthFctl_Type()
)
agPortCurCfgFastEthFctl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthFctl.setStatus("mandatory")


class _AgPortCurCfgGigEthAutoNeg_Type(Integer32):
    """Custom type agPortCurCfgGigEthAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortCurCfgGigEthAutoNeg_Type.__name__ = "Integer32"
_AgPortCurCfgGigEthAutoNeg_Object = MibTableColumn
agPortCurCfgGigEthAutoNeg = _AgPortCurCfgGigEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 13),
    _AgPortCurCfgGigEthAutoNeg_Type()
)
agPortCurCfgGigEthAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthAutoNeg.setStatus("mandatory")


class _AgPortCurCfgGigEthFctl_Type(Integer32):
    """Custom type agPortCurCfgGigEthFctl based on Integer32"""
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
        *(("both", 4),
          ("none", 5),
          ("other", 1),
          ("receive", 3),
          ("transmit", 2))
    )


_AgPortCurCfgGigEthFctl_Type.__name__ = "Integer32"
_AgPortCurCfgGigEthFctl_Object = MibTableColumn
agPortCurCfgGigEthFctl = _AgPortCurCfgGigEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 14),
    _AgPortCurCfgGigEthFctl_Type()
)
agPortCurCfgGigEthFctl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthFctl.setStatus("mandatory")


class _AgPortCurCfgPortName_Type(DisplayString):
    """Custom type agPortCurCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgPortCurCfgPortName_Type.__name__ = "DisplayString"
_AgPortCurCfgPortName_Object = MibTableColumn
agPortCurCfgPortName = _AgPortCurCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 15),
    _AgPortCurCfgPortName_Type()
)
agPortCurCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPortName.setStatus("mandatory")
_AgPortCurCfgBwmContract_Type = Integer32
_AgPortCurCfgBwmContract_Object = MibTableColumn
agPortCurCfgBwmContract = _AgPortCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 16),
    _AgPortCurCfgBwmContract_Type()
)
agPortCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgBwmContract.setStatus("mandatory")


class _AgPortCurCfgDiscardNonIPs_Type(Integer32):
    """Custom type agPortCurCfgDiscardNonIPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_AgPortCurCfgDiscardNonIPs_Type.__name__ = "Integer32"
_AgPortCurCfgDiscardNonIPs_Object = MibTableColumn
agPortCurCfgDiscardNonIPs = _AgPortCurCfgDiscardNonIPs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 17),
    _AgPortCurCfgDiscardNonIPs_Type()
)
agPortCurCfgDiscardNonIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgDiscardNonIPs.setStatus("mandatory")
_AgPortNewCfgTable_Object = MibTable
agPortNewCfgTable = _AgPortNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    agPortNewCfgTable.setStatus("mandatory")
_AgPortNewCfgTableEntry_Object = MibTableRow
agPortNewCfgTableEntry = _AgPortNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1)
)
agPortNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "agPortNewCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortNewCfgTableEntry.setStatus("mandatory")


class _AgPortNewCfgIndx_Type(Integer32):
    """Custom type agPortNewCfgIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgPortNewCfgIndx_Type.__name__ = "Integer32"
_AgPortNewCfgIndx_Object = MibTableColumn
agPortNewCfgIndx = _AgPortNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 1),
    _AgPortNewCfgIndx_Type()
)
agPortNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortNewCfgIndx.setStatus("mandatory")


class _AgPortNewCfgPrefLink_Type(Integer32):
    """Custom type agPortNewCfgPrefLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3),
          ("other", 1))
    )


_AgPortNewCfgPrefLink_Type.__name__ = "Integer32"
_AgPortNewCfgPrefLink_Object = MibTableColumn
agPortNewCfgPrefLink = _AgPortNewCfgPrefLink_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 2),
    _AgPortNewCfgPrefLink_Type()
)
agPortNewCfgPrefLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPrefLink.setStatus("mandatory")


class _AgPortNewCfgBackLink_Type(Integer32):
    """Custom type agPortNewCfgBackLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3),
          ("other", 1))
    )


_AgPortNewCfgBackLink_Type.__name__ = "Integer32"
_AgPortNewCfgBackLink_Object = MibTableColumn
agPortNewCfgBackLink = _AgPortNewCfgBackLink_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 3),
    _AgPortNewCfgBackLink_Type()
)
agPortNewCfgBackLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgBackLink.setStatus("mandatory")


class _AgPortNewCfgState_Type(Integer32):
    """Custom type agPortNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_AgPortNewCfgState_Type.__name__ = "Integer32"
_AgPortNewCfgState_Object = MibTableColumn
agPortNewCfgState = _AgPortNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 4),
    _AgPortNewCfgState_Type()
)
agPortNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgState.setStatus("mandatory")


class _AgPortNewCfgVlanTag_Type(Integer32):
    """Custom type agPortNewCfgVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tagged", 2),
          ("untagged", 3))
    )


_AgPortNewCfgVlanTag_Type.__name__ = "Integer32"
_AgPortNewCfgVlanTag_Object = MibTableColumn
agPortNewCfgVlanTag = _AgPortNewCfgVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 5),
    _AgPortNewCfgVlanTag_Type()
)
agPortNewCfgVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgVlanTag.setStatus("mandatory")


class _AgPortNewCfgStp_Type(Integer32):
    """Custom type agPortNewCfgStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortNewCfgStp_Type.__name__ = "Integer32"
_AgPortNewCfgStp_Object = MibTableColumn
agPortNewCfgStp = _AgPortNewCfgStp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 6),
    _AgPortNewCfgStp_Type()
)
agPortNewCfgStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgStp.setStatus("mandatory")


class _AgPortNewCfgRmon_Type(Integer32):
    """Custom type agPortNewCfgRmon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortNewCfgRmon_Type.__name__ = "Integer32"
_AgPortNewCfgRmon_Object = MibTableColumn
agPortNewCfgRmon = _AgPortNewCfgRmon_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 7),
    _AgPortNewCfgRmon_Type()
)
agPortNewCfgRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgRmon.setStatus("mandatory")
_AgPortNewCfgPVID_Type = Integer32
_AgPortNewCfgPVID_Object = MibTableColumn
agPortNewCfgPVID = _AgPortNewCfgPVID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 8),
    _AgPortNewCfgPVID_Type()
)
agPortNewCfgPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPVID.setStatus("mandatory")


class _AgPortNewCfgFastEthAutoNeg_Type(Integer32):
    """Custom type agPortNewCfgFastEthAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortNewCfgFastEthAutoNeg_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthAutoNeg_Object = MibTableColumn
agPortNewCfgFastEthAutoNeg = _AgPortNewCfgFastEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 9),
    _AgPortNewCfgFastEthAutoNeg_Type()
)
agPortNewCfgFastEthAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthAutoNeg.setStatus("mandatory")


class _AgPortNewCfgFastEthSpeed_Type(Integer32):
    """Custom type agPortNewCfgFastEthSpeed based on Integer32"""
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
        *(("mbs10", 2),
          ("mbs100", 3),
          ("mbs10or100", 4),
          ("other", 1))
    )


_AgPortNewCfgFastEthSpeed_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthSpeed_Object = MibTableColumn
agPortNewCfgFastEthSpeed = _AgPortNewCfgFastEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 10),
    _AgPortNewCfgFastEthSpeed_Type()
)
agPortNewCfgFastEthSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthSpeed.setStatus("mandatory")


class _AgPortNewCfgFastEthMode_Type(Integer32):
    """Custom type agPortNewCfgFastEthMode based on Integer32"""
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
        *(("full-duplex", 2),
          ("full-or-half-duplex", 4),
          ("half-duplex", 3),
          ("other", 1))
    )


_AgPortNewCfgFastEthMode_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthMode_Object = MibTableColumn
agPortNewCfgFastEthMode = _AgPortNewCfgFastEthMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 11),
    _AgPortNewCfgFastEthMode_Type()
)
agPortNewCfgFastEthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthMode.setStatus("mandatory")


class _AgPortNewCfgFastEthFctl_Type(Integer32):
    """Custom type agPortNewCfgFastEthFctl based on Integer32"""
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
        *(("both", 4),
          ("none", 5),
          ("other", 1),
          ("receive", 3),
          ("transmit", 2))
    )


_AgPortNewCfgFastEthFctl_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthFctl_Object = MibTableColumn
agPortNewCfgFastEthFctl = _AgPortNewCfgFastEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 12),
    _AgPortNewCfgFastEthFctl_Type()
)
agPortNewCfgFastEthFctl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthFctl.setStatus("mandatory")


class _AgPortNewCfgGigEthAutoNeg_Type(Integer32):
    """Custom type agPortNewCfgGigEthAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_AgPortNewCfgGigEthAutoNeg_Type.__name__ = "Integer32"
_AgPortNewCfgGigEthAutoNeg_Object = MibTableColumn
agPortNewCfgGigEthAutoNeg = _AgPortNewCfgGigEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 13),
    _AgPortNewCfgGigEthAutoNeg_Type()
)
agPortNewCfgGigEthAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthAutoNeg.setStatus("mandatory")


class _AgPortNewCfgGigEthFctl_Type(Integer32):
    """Custom type agPortNewCfgGigEthFctl based on Integer32"""
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
        *(("both", 4),
          ("none", 5),
          ("other", 1),
          ("receive", 3),
          ("transmit", 2))
    )


_AgPortNewCfgGigEthFctl_Type.__name__ = "Integer32"
_AgPortNewCfgGigEthFctl_Object = MibTableColumn
agPortNewCfgGigEthFctl = _AgPortNewCfgGigEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 14),
    _AgPortNewCfgGigEthFctl_Type()
)
agPortNewCfgGigEthFctl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthFctl.setStatus("mandatory")


class _AgPortNewCfgPortName_Type(DisplayString):
    """Custom type agPortNewCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgPortNewCfgPortName_Type.__name__ = "DisplayString"
_AgPortNewCfgPortName_Object = MibTableColumn
agPortNewCfgPortName = _AgPortNewCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 15),
    _AgPortNewCfgPortName_Type()
)
agPortNewCfgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPortName.setStatus("mandatory")
_AgPortNewCfgBwmContract_Type = Integer32
_AgPortNewCfgBwmContract_Object = MibTableColumn
agPortNewCfgBwmContract = _AgPortNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 16),
    _AgPortNewCfgBwmContract_Type()
)
agPortNewCfgBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgBwmContract.setStatus("mandatory")


class _AgPortNewCfgDiscardNonIPs_Type(Integer32):
    """Custom type agPortNewCfgDiscardNonIPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_AgPortNewCfgDiscardNonIPs_Type.__name__ = "Integer32"
_AgPortNewCfgDiscardNonIPs_Object = MibTableColumn
agPortNewCfgDiscardNonIPs = _AgPortNewCfgDiscardNonIPs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 17),
    _AgPortNewCfgDiscardNonIPs_Type()
)
agPortNewCfgDiscardNonIPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgDiscardNonIPs.setStatus("mandatory")
_Iprouting_ObjectIdentity = ObjectIdentity
iprouting = _Iprouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3)
)
_IpInterfaceTableMax_Type = Integer32
_IpInterfaceTableMax_Object = MibScalar
ipInterfaceTableMax = _IpInterfaceTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 1),
    _IpInterfaceTableMax_Type()
)
ipInterfaceTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceTableMax.setStatus("mandatory")
_IpCurCfgIntfTable_Object = MibTable
ipCurCfgIntfTable = _IpCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgIntfTable.setStatus("mandatory")
_IpCurCfgIntfEntry_Object = MibTableRow
ipCurCfgIntfEntry = _IpCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1)
)
ipCurCfgIntfEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgIntfEntry.setStatus("mandatory")


class _IpCurCfgIntfIndex_Type(Integer32):
    """Custom type ipCurCfgIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IpCurCfgIntfIndex_Type.__name__ = "Integer32"
_IpCurCfgIntfIndex_Object = MibTableColumn
ipCurCfgIntfIndex = _IpCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 1),
    _IpCurCfgIntfIndex_Type()
)
ipCurCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfIndex.setStatus("mandatory")
_IpCurCfgIntfAddr_Type = IpAddress
_IpCurCfgIntfAddr_Object = MibTableColumn
ipCurCfgIntfAddr = _IpCurCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 2),
    _IpCurCfgIntfAddr_Type()
)
ipCurCfgIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfAddr.setStatus("mandatory")
_IpCurCfgIntfMask_Type = IpAddress
_IpCurCfgIntfMask_Object = MibTableColumn
ipCurCfgIntfMask = _IpCurCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 3),
    _IpCurCfgIntfMask_Type()
)
ipCurCfgIntfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfMask.setStatus("mandatory")
_IpCurCfgIntfBroadcast_Type = IpAddress
_IpCurCfgIntfBroadcast_Object = MibTableColumn
ipCurCfgIntfBroadcast = _IpCurCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 4),
    _IpCurCfgIntfBroadcast_Type()
)
ipCurCfgIntfBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfBroadcast.setStatus("mandatory")


class _IpCurCfgIntfVlan_Type(Integer32):
    """Custom type ipCurCfgIntfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpCurCfgIntfVlan_Type.__name__ = "Integer32"
_IpCurCfgIntfVlan_Object = MibTableColumn
ipCurCfgIntfVlan = _IpCurCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 5),
    _IpCurCfgIntfVlan_Type()
)
ipCurCfgIntfVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfVlan.setStatus("mandatory")


class _IpCurCfgIntfState_Type(Integer32):
    """Custom type ipCurCfgIntfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpCurCfgIntfState_Type.__name__ = "Integer32"
_IpCurCfgIntfState_Object = MibTableColumn
ipCurCfgIntfState = _IpCurCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 6),
    _IpCurCfgIntfState_Type()
)
ipCurCfgIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfState.setStatus("mandatory")
_IpNewCfgIntfTable_Object = MibTable
ipNewCfgIntfTable = _IpNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgIntfTable.setStatus("mandatory")
_IpNewCfgIntfEntry_Object = MibTableRow
ipNewCfgIntfEntry = _IpNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1)
)
ipNewCfgIntfEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgIntfEntry.setStatus("mandatory")


class _IpNewCfgIntfIndex_Type(Integer32):
    """Custom type ipNewCfgIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IpNewCfgIntfIndex_Type.__name__ = "Integer32"
_IpNewCfgIntfIndex_Object = MibTableColumn
ipNewCfgIntfIndex = _IpNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 1),
    _IpNewCfgIntfIndex_Type()
)
ipNewCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgIntfIndex.setStatus("mandatory")
_IpNewCfgIntfAddr_Type = IpAddress
_IpNewCfgIntfAddr_Object = MibTableColumn
ipNewCfgIntfAddr = _IpNewCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 2),
    _IpNewCfgIntfAddr_Type()
)
ipNewCfgIntfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfAddr.setStatus("mandatory")
_IpNewCfgIntfMask_Type = IpAddress
_IpNewCfgIntfMask_Object = MibTableColumn
ipNewCfgIntfMask = _IpNewCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 3),
    _IpNewCfgIntfMask_Type()
)
ipNewCfgIntfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfMask.setStatus("mandatory")
_IpNewCfgIntfBroadcast_Type = IpAddress
_IpNewCfgIntfBroadcast_Object = MibTableColumn
ipNewCfgIntfBroadcast = _IpNewCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 4),
    _IpNewCfgIntfBroadcast_Type()
)
ipNewCfgIntfBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfBroadcast.setStatus("mandatory")


class _IpNewCfgIntfVlan_Type(Integer32):
    """Custom type ipNewCfgIntfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpNewCfgIntfVlan_Type.__name__ = "Integer32"
_IpNewCfgIntfVlan_Object = MibTableColumn
ipNewCfgIntfVlan = _IpNewCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 5),
    _IpNewCfgIntfVlan_Type()
)
ipNewCfgIntfVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfVlan.setStatus("mandatory")


class _IpNewCfgIntfState_Type(Integer32):
    """Custom type ipNewCfgIntfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpNewCfgIntfState_Type.__name__ = "Integer32"
_IpNewCfgIntfState_Object = MibTableColumn
ipNewCfgIntfState = _IpNewCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 6),
    _IpNewCfgIntfState_Type()
)
ipNewCfgIntfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfState.setStatus("mandatory")


class _IpNewCfgIntfDelete_Type(Integer32):
    """Custom type ipNewCfgIntfDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_IpNewCfgIntfDelete_Type.__name__ = "Integer32"
_IpNewCfgIntfDelete_Object = MibTableColumn
ipNewCfgIntfDelete = _IpNewCfgIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 7),
    _IpNewCfgIntfDelete_Type()
)
ipNewCfgIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfDelete.setStatus("mandatory")
_IpGatewayTableMax_Type = Integer32
_IpGatewayTableMax_Object = MibScalar
ipGatewayTableMax = _IpGatewayTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 4),
    _IpGatewayTableMax_Type()
)
ipGatewayTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGatewayTableMax.setStatus("mandatory")
_IpCurCfgGwTable_Object = MibTable
ipCurCfgGwTable = _IpCurCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ipCurCfgGwTable.setStatus("mandatory")
_IpCurCfgGwEntry_Object = MibTableRow
ipCurCfgGwEntry = _IpCurCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1)
)
ipCurCfgGwEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgGwEntry.setStatus("mandatory")


class _IpCurCfgGwIndex_Type(Integer32):
    """Custom type ipCurCfgGwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IpCurCfgGwIndex_Type.__name__ = "Integer32"
_IpCurCfgGwIndex_Object = MibTableColumn
ipCurCfgGwIndex = _IpCurCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 1),
    _IpCurCfgGwIndex_Type()
)
ipCurCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwIndex.setStatus("mandatory")
_IpCurCfgGwAddr_Type = IpAddress
_IpCurCfgGwAddr_Object = MibTableColumn
ipCurCfgGwAddr = _IpCurCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 2),
    _IpCurCfgGwAddr_Type()
)
ipCurCfgGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwAddr.setStatus("mandatory")


class _IpCurCfgGwInterval_Type(Integer32):
    """Custom type ipCurCfgGwInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IpCurCfgGwInterval_Type.__name__ = "Integer32"
_IpCurCfgGwInterval_Object = MibTableColumn
ipCurCfgGwInterval = _IpCurCfgGwInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 3),
    _IpCurCfgGwInterval_Type()
)
ipCurCfgGwInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwInterval.setStatus("mandatory")


class _IpCurCfgGwRetry_Type(Integer32):
    """Custom type ipCurCfgGwRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IpCurCfgGwRetry_Type.__name__ = "Integer32"
_IpCurCfgGwRetry_Object = MibTableColumn
ipCurCfgGwRetry = _IpCurCfgGwRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 4),
    _IpCurCfgGwRetry_Type()
)
ipCurCfgGwRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwRetry.setStatus("mandatory")


class _IpCurCfgGwState_Type(Integer32):
    """Custom type ipCurCfgGwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpCurCfgGwState_Type.__name__ = "Integer32"
_IpCurCfgGwState_Object = MibTableColumn
ipCurCfgGwState = _IpCurCfgGwState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 5),
    _IpCurCfgGwState_Type()
)
ipCurCfgGwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwState.setStatus("mandatory")


class _IpCurCfgGwArp_Type(Integer32):
    """Custom type ipCurCfgGwArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpCurCfgGwArp_Type.__name__ = "Integer32"
_IpCurCfgGwArp_Object = MibTableColumn
ipCurCfgGwArp = _IpCurCfgGwArp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 6),
    _IpCurCfgGwArp_Type()
)
ipCurCfgGwArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwArp.setStatus("mandatory")
_IpNewCfgGwTable_Object = MibTable
ipNewCfgGwTable = _IpNewCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ipNewCfgGwTable.setStatus("mandatory")
_IpNewCfgGwEntry_Object = MibTableRow
ipNewCfgGwEntry = _IpNewCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1)
)
ipNewCfgGwEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipNewCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgGwEntry.setStatus("mandatory")


class _IpNewCfgGwIndex_Type(Integer32):
    """Custom type ipNewCfgGwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IpNewCfgGwIndex_Type.__name__ = "Integer32"
_IpNewCfgGwIndex_Object = MibTableColumn
ipNewCfgGwIndex = _IpNewCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 1),
    _IpNewCfgGwIndex_Type()
)
ipNewCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgGwIndex.setStatus("mandatory")
_IpNewCfgGwAddr_Type = IpAddress
_IpNewCfgGwAddr_Object = MibTableColumn
ipNewCfgGwAddr = _IpNewCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 2),
    _IpNewCfgGwAddr_Type()
)
ipNewCfgGwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwAddr.setStatus("mandatory")


class _IpNewCfgGwInterval_Type(Integer32):
    """Custom type ipNewCfgGwInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IpNewCfgGwInterval_Type.__name__ = "Integer32"
_IpNewCfgGwInterval_Object = MibTableColumn
ipNewCfgGwInterval = _IpNewCfgGwInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 3),
    _IpNewCfgGwInterval_Type()
)
ipNewCfgGwInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwInterval.setStatus("mandatory")


class _IpNewCfgGwRetry_Type(Integer32):
    """Custom type ipNewCfgGwRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IpNewCfgGwRetry_Type.__name__ = "Integer32"
_IpNewCfgGwRetry_Object = MibTableColumn
ipNewCfgGwRetry = _IpNewCfgGwRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 4),
    _IpNewCfgGwRetry_Type()
)
ipNewCfgGwRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwRetry.setStatus("mandatory")


class _IpNewCfgGwState_Type(Integer32):
    """Custom type ipNewCfgGwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpNewCfgGwState_Type.__name__ = "Integer32"
_IpNewCfgGwState_Object = MibTableColumn
ipNewCfgGwState = _IpNewCfgGwState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 5),
    _IpNewCfgGwState_Type()
)
ipNewCfgGwState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwState.setStatus("mandatory")


class _IpNewCfgGwDelete_Type(Integer32):
    """Custom type ipNewCfgGwDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_IpNewCfgGwDelete_Type.__name__ = "Integer32"
_IpNewCfgGwDelete_Object = MibTableColumn
ipNewCfgGwDelete = _IpNewCfgGwDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 6),
    _IpNewCfgGwDelete_Type()
)
ipNewCfgGwDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwDelete.setStatus("mandatory")


class _IpNewCfgGwArp_Type(Integer32):
    """Custom type ipNewCfgGwArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpNewCfgGwArp_Type.__name__ = "Integer32"
_IpNewCfgGwArp_Object = MibTableColumn
ipNewCfgGwArp = _IpNewCfgGwArp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 7),
    _IpNewCfgGwArp_Type()
)
ipNewCfgGwArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwArp.setStatus("mandatory")
_IpCurCfgStaticRouteTable_Object = MibTable
ipCurCfgStaticRouteTable = _IpCurCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteTable.setStatus("mandatory")
_IpCurCfgStaticRouteEntry_Object = MibTableRow
ipCurCfgStaticRouteEntry = _IpCurCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1)
)
ipCurCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipCurCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteEntry.setStatus("mandatory")


class _IpCurCfgStaticRouteIndx_Type(Integer32):
    """Custom type ipCurCfgStaticRouteIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IpCurCfgStaticRouteIndx_Type.__name__ = "Integer32"
_IpCurCfgStaticRouteIndx_Object = MibTableColumn
ipCurCfgStaticRouteIndx = _IpCurCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 1),
    _IpCurCfgStaticRouteIndx_Type()
)
ipCurCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteIndx.setStatus("mandatory")
_IpCurCfgStaticRouteDestIp_Type = IpAddress
_IpCurCfgStaticRouteDestIp_Object = MibTableColumn
ipCurCfgStaticRouteDestIp = _IpCurCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 2),
    _IpCurCfgStaticRouteDestIp_Type()
)
ipCurCfgStaticRouteDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteDestIp.setStatus("mandatory")
_IpCurCfgStaticRouteMask_Type = IpAddress
_IpCurCfgStaticRouteMask_Object = MibTableColumn
ipCurCfgStaticRouteMask = _IpCurCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 3),
    _IpCurCfgStaticRouteMask_Type()
)
ipCurCfgStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteMask.setStatus("mandatory")
_IpCurCfgStaticRouteGateway_Type = IpAddress
_IpCurCfgStaticRouteGateway_Object = MibTableColumn
ipCurCfgStaticRouteGateway = _IpCurCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 4),
    _IpCurCfgStaticRouteGateway_Type()
)
ipCurCfgStaticRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteGateway.setStatus("mandatory")
_IpCurCfgStaticRouteInterface_Type = Integer32
_IpCurCfgStaticRouteInterface_Object = MibTableColumn
ipCurCfgStaticRouteInterface = _IpCurCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 5),
    _IpCurCfgStaticRouteInterface_Type()
)
ipCurCfgStaticRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteInterface.setStatus("mandatory")
_IpNewCfgStaticRouteTable_Object = MibTable
ipNewCfgStaticRouteTable = _IpNewCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteTable.setStatus("mandatory")
_IpNewCfgStaticRouteEntry_Object = MibTableRow
ipNewCfgStaticRouteEntry = _IpNewCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1)
)
ipNewCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipNewCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteEntry.setStatus("mandatory")


class _IpNewCfgStaticRouteIndx_Type(Integer32):
    """Custom type ipNewCfgStaticRouteIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IpNewCfgStaticRouteIndx_Type.__name__ = "Integer32"
_IpNewCfgStaticRouteIndx_Object = MibTableColumn
ipNewCfgStaticRouteIndx = _IpNewCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 1),
    _IpNewCfgStaticRouteIndx_Type()
)
ipNewCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteIndx.setStatus("mandatory")
_IpNewCfgStaticRouteDestIp_Type = IpAddress
_IpNewCfgStaticRouteDestIp_Object = MibTableColumn
ipNewCfgStaticRouteDestIp = _IpNewCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 2),
    _IpNewCfgStaticRouteDestIp_Type()
)
ipNewCfgStaticRouteDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteDestIp.setStatus("mandatory")
_IpNewCfgStaticRouteMask_Type = IpAddress
_IpNewCfgStaticRouteMask_Object = MibTableColumn
ipNewCfgStaticRouteMask = _IpNewCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 3),
    _IpNewCfgStaticRouteMask_Type()
)
ipNewCfgStaticRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteMask.setStatus("mandatory")
_IpNewCfgStaticRouteGateway_Type = IpAddress
_IpNewCfgStaticRouteGateway_Object = MibTableColumn
ipNewCfgStaticRouteGateway = _IpNewCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 4),
    _IpNewCfgStaticRouteGateway_Type()
)
ipNewCfgStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteGateway.setStatus("mandatory")


class _IpNewCfgStaticRouteAction_Type(Integer32):
    """Custom type ipNewCfgStaticRouteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_IpNewCfgStaticRouteAction_Type.__name__ = "Integer32"
_IpNewCfgStaticRouteAction_Object = MibTableColumn
ipNewCfgStaticRouteAction = _IpNewCfgStaticRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 5),
    _IpNewCfgStaticRouteAction_Type()
)
ipNewCfgStaticRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteAction.setStatus("mandatory")
_IpNewCfgStaticRouteInterface_Type = Integer32
_IpNewCfgStaticRouteInterface_Object = MibTableColumn
ipNewCfgStaticRouteInterface = _IpNewCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 6),
    _IpNewCfgStaticRouteInterface_Type()
)
ipNewCfgStaticRouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteInterface.setStatus("mandatory")
_IpForward_ObjectIdentity = ObjectIdentity
ipForward = _IpForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9)
)
_RipConfig_ObjectIdentity = ObjectIdentity
ripConfig = _RipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1)
)


class _RipCurCfgSupply_Type(Integer32):
    """Custom type ripCurCfgSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipCurCfgSupply_Type.__name__ = "Integer32"
_RipCurCfgSupply_Object = MibScalar
ripCurCfgSupply = _RipCurCfgSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 1),
    _RipCurCfgSupply_Type()
)
ripCurCfgSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgSupply.setStatus("mandatory")


class _RipNewCfgSupply_Type(Integer32):
    """Custom type ripNewCfgSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipNewCfgSupply_Type.__name__ = "Integer32"
_RipNewCfgSupply_Object = MibScalar
ripNewCfgSupply = _RipNewCfgSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 2),
    _RipNewCfgSupply_Type()
)
ripNewCfgSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgSupply.setStatus("mandatory")


class _RipCurCfgListen_Type(Integer32):
    """Custom type ripCurCfgListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipCurCfgListen_Type.__name__ = "Integer32"
_RipCurCfgListen_Object = MibScalar
ripCurCfgListen = _RipCurCfgListen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 3),
    _RipCurCfgListen_Type()
)
ripCurCfgListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgListen.setStatus("mandatory")


class _RipNewCfgListen_Type(Integer32):
    """Custom type ripNewCfgListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipNewCfgListen_Type.__name__ = "Integer32"
_RipNewCfgListen_Object = MibScalar
ripNewCfgListen = _RipNewCfgListen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 4),
    _RipNewCfgListen_Type()
)
ripNewCfgListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgListen.setStatus("mandatory")


class _RipCurCfgDefListen_Type(Integer32):
    """Custom type ripCurCfgDefListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipCurCfgDefListen_Type.__name__ = "Integer32"
_RipCurCfgDefListen_Object = MibScalar
ripCurCfgDefListen = _RipCurCfgDefListen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 5),
    _RipCurCfgDefListen_Type()
)
ripCurCfgDefListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgDefListen.setStatus("mandatory")


class _RipNewCfgDefListen_Type(Integer32):
    """Custom type ripNewCfgDefListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipNewCfgDefListen_Type.__name__ = "Integer32"
_RipNewCfgDefListen_Object = MibScalar
ripNewCfgDefListen = _RipNewCfgDefListen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 6),
    _RipNewCfgDefListen_Type()
)
ripNewCfgDefListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgDefListen.setStatus("mandatory")


class _RipCurCfgStaticSupply_Type(Integer32):
    """Custom type ripCurCfgStaticSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipCurCfgStaticSupply_Type.__name__ = "Integer32"
_RipCurCfgStaticSupply_Object = MibScalar
ripCurCfgStaticSupply = _RipCurCfgStaticSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 7),
    _RipCurCfgStaticSupply_Type()
)
ripCurCfgStaticSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgStaticSupply.setStatus("mandatory")


class _RipNewCfgStaticSupply_Type(Integer32):
    """Custom type ripNewCfgStaticSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipNewCfgStaticSupply_Type.__name__ = "Integer32"
_RipNewCfgStaticSupply_Object = MibScalar
ripNewCfgStaticSupply = _RipNewCfgStaticSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 8),
    _RipNewCfgStaticSupply_Type()
)
ripNewCfgStaticSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgStaticSupply.setStatus("mandatory")


class _RipCurCfgUpdatePeriod_Type(Integer32):
    """Custom type ripCurCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RipCurCfgUpdatePeriod_Type.__name__ = "Integer32"
_RipCurCfgUpdatePeriod_Object = MibScalar
ripCurCfgUpdatePeriod = _RipCurCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 9),
    _RipCurCfgUpdatePeriod_Type()
)
ripCurCfgUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgUpdatePeriod.setStatus("mandatory")


class _RipNewCfgUpdatePeriod_Type(Integer32):
    """Custom type ripNewCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RipNewCfgUpdatePeriod_Type.__name__ = "Integer32"
_RipNewCfgUpdatePeriod_Object = MibScalar
ripNewCfgUpdatePeriod = _RipNewCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 10),
    _RipNewCfgUpdatePeriod_Type()
)
ripNewCfgUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgUpdatePeriod.setStatus("mandatory")


class _RipCurCfgState_Type(Integer32):
    """Custom type ripCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_RipCurCfgState_Type.__name__ = "Integer32"
_RipCurCfgState_Object = MibScalar
ripCurCfgState = _RipCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 11),
    _RipCurCfgState_Type()
)
ripCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgState.setStatus("mandatory")


class _RipNewCfgState_Type(Integer32):
    """Custom type ripNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_RipNewCfgState_Type.__name__ = "Integer32"
_RipNewCfgState_Object = MibScalar
ripNewCfgState = _RipNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 12),
    _RipNewCfgState_Type()
)
ripNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgState.setStatus("mandatory")


class _RipCurCfgPoisonReverse_Type(Integer32):
    """Custom type ripCurCfgPoisonReverse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipCurCfgPoisonReverse_Type.__name__ = "Integer32"
_RipCurCfgPoisonReverse_Object = MibScalar
ripCurCfgPoisonReverse = _RipCurCfgPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 13),
    _RipCurCfgPoisonReverse_Type()
)
ripCurCfgPoisonReverse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgPoisonReverse.setStatus("mandatory")


class _RipNewCfgPoisonReverse_Type(Integer32):
    """Custom type ripNewCfgPoisonReverse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_RipNewCfgPoisonReverse_Type.__name__ = "Integer32"
_RipNewCfgPoisonReverse_Object = MibScalar
ripNewCfgPoisonReverse = _RipNewCfgPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 14),
    _RipNewCfgPoisonReverse_Type()
)
ripNewCfgPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgPoisonReverse.setStatus("mandatory")
_IpFwdCurCfgPortTable_Object = MibTable
ipFwdCurCfgPortTable = _IpFwdCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    ipFwdCurCfgPortTable.setStatus("mandatory")
_IpFwdCurCfgPortEntry_Object = MibTableRow
ipFwdCurCfgPortEntry = _IpFwdCurCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2, 1)
)
ipFwdCurCfgPortEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipFwdCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    ipFwdCurCfgPortEntry.setStatus("mandatory")
_IpFwdCurCfgPortIndex_Type = Integer32
_IpFwdCurCfgPortIndex_Object = MibTableColumn
ipFwdCurCfgPortIndex = _IpFwdCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2, 1, 1),
    _IpFwdCurCfgPortIndex_Type()
)
ipFwdCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgPortIndex.setStatus("mandatory")


class _IpFwdCurCfgPortState_Type(Integer32):
    """Custom type ipFwdCurCfgPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpFwdCurCfgPortState_Type.__name__ = "Integer32"
_IpFwdCurCfgPortState_Object = MibTableColumn
ipFwdCurCfgPortState = _IpFwdCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2, 1, 2),
    _IpFwdCurCfgPortState_Type()
)
ipFwdCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgPortState.setStatus("mandatory")
_IpFwdNewCfgPortTable_Object = MibTable
ipFwdNewCfgPortTable = _IpFwdNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3)
)
if mibBuilder.loadTexts:
    ipFwdNewCfgPortTable.setStatus("mandatory")
_IpFwdNewCfgPortEntry_Object = MibTableRow
ipFwdNewCfgPortEntry = _IpFwdNewCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3, 1)
)
ipFwdNewCfgPortEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipFwdNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    ipFwdNewCfgPortEntry.setStatus("mandatory")
_IpFwdNewCfgPortIndex_Type = Integer32
_IpFwdNewCfgPortIndex_Object = MibTableColumn
ipFwdNewCfgPortIndex = _IpFwdNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3, 1, 1),
    _IpFwdNewCfgPortIndex_Type()
)
ipFwdNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdNewCfgPortIndex.setStatus("mandatory")


class _IpFwdNewCfgPortState_Type(Integer32):
    """Custom type ipFwdNewCfgPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_IpFwdNewCfgPortState_Type.__name__ = "Integer32"
_IpFwdNewCfgPortState_Object = MibTableColumn
ipFwdNewCfgPortState = _IpFwdNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3, 1, 2),
    _IpFwdNewCfgPortState_Type()
)
ipFwdNewCfgPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgPortState.setStatus("mandatory")
_IpFwdCurCfgLocalSubnet_Type = IpAddress
_IpFwdCurCfgLocalSubnet_Object = MibScalar
ipFwdCurCfgLocalSubnet = _IpFwdCurCfgLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 4),
    _IpFwdCurCfgLocalSubnet_Type()
)
ipFwdCurCfgLocalSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalSubnet.setStatus("mandatory")
_IpFwdNewCfgLocalSubnet_Type = IpAddress
_IpFwdNewCfgLocalSubnet_Object = MibScalar
ipFwdNewCfgLocalSubnet = _IpFwdNewCfgLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 5),
    _IpFwdNewCfgLocalSubnet_Type()
)
ipFwdNewCfgLocalSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalSubnet.setStatus("mandatory")
_IpFwdCurCfgLocalMask_Type = IpAddress
_IpFwdCurCfgLocalMask_Object = MibScalar
ipFwdCurCfgLocalMask = _IpFwdCurCfgLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 6),
    _IpFwdCurCfgLocalMask_Type()
)
ipFwdCurCfgLocalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalMask.setStatus("mandatory")
_IpFwdNewCfgLocalMask_Type = IpAddress
_IpFwdNewCfgLocalMask_Object = MibScalar
ipFwdNewCfgLocalMask = _IpFwdNewCfgLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 7),
    _IpFwdNewCfgLocalMask_Type()
)
ipFwdNewCfgLocalMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalMask.setStatus("mandatory")


class _IpFwdCurCfgState_Type(Integer32):
    """Custom type ipFwdCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_IpFwdCurCfgState_Type.__name__ = "Integer32"
_IpFwdCurCfgState_Object = MibScalar
ipFwdCurCfgState = _IpFwdCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 8),
    _IpFwdCurCfgState_Type()
)
ipFwdCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgState.setStatus("mandatory")


class _IpFwdNewCfgState_Type(Integer32):
    """Custom type ipFwdNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_IpFwdNewCfgState_Type.__name__ = "Integer32"
_IpFwdNewCfgState_Object = MibScalar
ipFwdNewCfgState = _IpFwdNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 9),
    _IpFwdNewCfgState_Type()
)
ipFwdNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgState.setStatus("mandatory")


class _IpFwdCurCfgDirectedBcast_Type(Integer32):
    """Custom type ipFwdCurCfgDirectedBcast based on Integer32"""
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


_IpFwdCurCfgDirectedBcast_Type.__name__ = "Integer32"
_IpFwdCurCfgDirectedBcast_Object = MibScalar
ipFwdCurCfgDirectedBcast = _IpFwdCurCfgDirectedBcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 10),
    _IpFwdCurCfgDirectedBcast_Type()
)
ipFwdCurCfgDirectedBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgDirectedBcast.setStatus("mandatory")


class _IpFwdNewCfgDirectedBcast_Type(Integer32):
    """Custom type ipFwdNewCfgDirectedBcast based on Integer32"""
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


_IpFwdNewCfgDirectedBcast_Type.__name__ = "Integer32"
_IpFwdNewCfgDirectedBcast_Object = MibScalar
ipFwdNewCfgDirectedBcast = _IpFwdNewCfgDirectedBcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 11),
    _IpFwdNewCfgDirectedBcast_Type()
)
ipFwdNewCfgDirectedBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgDirectedBcast.setStatus("mandatory")
_ArpCurCfgReARPPeriod_Type = Integer32
_ArpCurCfgReARPPeriod_Object = MibScalar
arpCurCfgReARPPeriod = _ArpCurCfgReARPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 10),
    _ArpCurCfgReARPPeriod_Type()
)
arpCurCfgReARPPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpCurCfgReARPPeriod.setStatus("mandatory")
_ArpNewCfgReARPPeriod_Type = Integer32
_ArpNewCfgReARPPeriod_Object = MibScalar
arpNewCfgReARPPeriod = _ArpNewCfgReARPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 11),
    _ArpNewCfgReARPPeriod_Type()
)
arpNewCfgReARPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpNewCfgReARPPeriod.setStatus("mandatory")


class _IpCurCfgGwMetric_Type(Integer32):
    """Custom type ipCurCfgGwMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 2),
          ("strict", 1))
    )


_IpCurCfgGwMetric_Type.__name__ = "Integer32"
_IpCurCfgGwMetric_Object = MibScalar
ipCurCfgGwMetric = _IpCurCfgGwMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 12),
    _IpCurCfgGwMetric_Type()
)
ipCurCfgGwMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwMetric.setStatus("mandatory")


class _IpNewCfgGwMetric_Type(Integer32):
    """Custom type ipNewCfgGwMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 2),
          ("strict", 1))
    )


_IpNewCfgGwMetric_Type.__name__ = "Integer32"
_IpNewCfgGwMetric_Object = MibScalar
ipNewCfgGwMetric = _IpNewCfgGwMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 13),
    _IpNewCfgGwMetric_Type()
)
ipNewCfgGwMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwMetric.setStatus("mandatory")
_Vlans_ObjectIdentity = ObjectIdentity
vlans = _Vlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4)
)
_VlanMaxEnt_Type = Integer32
_VlanMaxEnt_Object = MibScalar
vlanMaxEnt = _VlanMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 1),
    _VlanMaxEnt_Type()
)
vlanMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxEnt.setStatus("mandatory")
_VlanCurCfgTable_Object = MibTable
vlanCurCfgTable = _VlanCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    vlanCurCfgTable.setStatus("mandatory")
_VlanCurCfgTableEntry_Object = MibTableRow
vlanCurCfgTableEntry = _VlanCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1)
)
vlanCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vlanCurCfgVlanId"),
)
if mibBuilder.loadTexts:
    vlanCurCfgTableEntry.setStatus("mandatory")


class _VlanCurCfgVlanId_Type(Integer32):
    """Custom type vlanCurCfgVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanCurCfgVlanId_Type.__name__ = "Integer32"
_VlanCurCfgVlanId_Object = MibTableColumn
vlanCurCfgVlanId = _VlanCurCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1, 1),
    _VlanCurCfgVlanId_Type()
)
vlanCurCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgVlanId.setStatus("mandatory")


class _VlanCurCfgVlanName_Type(DisplayString):
    """Custom type vlanCurCfgVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanCurCfgVlanName_Type.__name__ = "DisplayString"
_VlanCurCfgVlanName_Object = MibTableColumn
vlanCurCfgVlanName = _VlanCurCfgVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1, 2),
    _VlanCurCfgVlanName_Type()
)
vlanCurCfgVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgVlanName.setStatus("mandatory")


class _VlanCurCfgPorts_Type(OctetString):
    """Custom type vlanCurCfgPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanCurCfgPorts_Type.__name__ = "OctetString"
_VlanCurCfgPorts_Object = MibTableColumn
vlanCurCfgPorts = _VlanCurCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1, 3),
    _VlanCurCfgPorts_Type()
)
vlanCurCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgPorts.setStatus("mandatory")


class _VlanCurCfgState_Type(Integer32):
    """Custom type vlanCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_VlanCurCfgState_Type.__name__ = "Integer32"
_VlanCurCfgState_Object = MibTableColumn
vlanCurCfgState = _VlanCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1, 4),
    _VlanCurCfgState_Type()
)
vlanCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgState.setStatus("mandatory")


class _VlanCurCfgJumbo_Type(Integer32):
    """Custom type vlanCurCfgJumbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_VlanCurCfgJumbo_Type.__name__ = "Integer32"
_VlanCurCfgJumbo_Object = MibTableColumn
vlanCurCfgJumbo = _VlanCurCfgJumbo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1, 5),
    _VlanCurCfgJumbo_Type()
)
vlanCurCfgJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgJumbo.setStatus("mandatory")
_VlanCurCfgBwmContract_Type = Integer32
_VlanCurCfgBwmContract_Object = MibTableColumn
vlanCurCfgBwmContract = _VlanCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1, 6),
    _VlanCurCfgBwmContract_Type()
)
vlanCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgBwmContract.setStatus("mandatory")
_VlanNewCfgTable_Object = MibTable
vlanNewCfgTable = _VlanNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    vlanNewCfgTable.setStatus("mandatory")
_VlanNewCfgTableEntry_Object = MibTableRow
vlanNewCfgTableEntry = _VlanNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1)
)
vlanNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vlanNewCfgVlanId"),
)
if mibBuilder.loadTexts:
    vlanNewCfgTableEntry.setStatus("mandatory")


class _VlanNewCfgVlanId_Type(Integer32):
    """Custom type vlanNewCfgVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanNewCfgVlanId_Type.__name__ = "Integer32"
_VlanNewCfgVlanId_Object = MibTableColumn
vlanNewCfgVlanId = _VlanNewCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 1),
    _VlanNewCfgVlanId_Type()
)
vlanNewCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNewCfgVlanId.setStatus("mandatory")


class _VlanNewCfgVlanName_Type(DisplayString):
    """Custom type vlanNewCfgVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanNewCfgVlanName_Type.__name__ = "DisplayString"
_VlanNewCfgVlanName_Object = MibTableColumn
vlanNewCfgVlanName = _VlanNewCfgVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 2),
    _VlanNewCfgVlanName_Type()
)
vlanNewCfgVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgVlanName.setStatus("mandatory")


class _VlanNewCfgPorts_Type(OctetString):
    """Custom type vlanNewCfgPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanNewCfgPorts_Type.__name__ = "OctetString"
_VlanNewCfgPorts_Object = MibTableColumn
vlanNewCfgPorts = _VlanNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 3),
    _VlanNewCfgPorts_Type()
)
vlanNewCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNewCfgPorts.setStatus("mandatory")


class _VlanNewCfgState_Type(Integer32):
    """Custom type vlanNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_VlanNewCfgState_Type.__name__ = "Integer32"
_VlanNewCfgState_Object = MibTableColumn
vlanNewCfgState = _VlanNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 4),
    _VlanNewCfgState_Type()
)
vlanNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgState.setStatus("mandatory")


class _VlanNewCfgJumbo_Type(Integer32):
    """Custom type vlanNewCfgJumbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_VlanNewCfgJumbo_Type.__name__ = "Integer32"
_VlanNewCfgJumbo_Object = MibTableColumn
vlanNewCfgJumbo = _VlanNewCfgJumbo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 5),
    _VlanNewCfgJumbo_Type()
)
vlanNewCfgJumbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgJumbo.setStatus("mandatory")
_VlanNewCfgAddPort_Type = Integer32
_VlanNewCfgAddPort_Object = MibTableColumn
vlanNewCfgAddPort = _VlanNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 6),
    _VlanNewCfgAddPort_Type()
)
vlanNewCfgAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgAddPort.setStatus("mandatory")
_VlanNewCfgRemovePort_Type = Integer32
_VlanNewCfgRemovePort_Object = MibTableColumn
vlanNewCfgRemovePort = _VlanNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 7),
    _VlanNewCfgRemovePort_Type()
)
vlanNewCfgRemovePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgRemovePort.setStatus("mandatory")


class _VlanNewCfgDelete_Type(Integer32):
    """Custom type vlanNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_VlanNewCfgDelete_Type.__name__ = "Integer32"
_VlanNewCfgDelete_Object = MibTableColumn
vlanNewCfgDelete = _VlanNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 8),
    _VlanNewCfgDelete_Type()
)
vlanNewCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgDelete.setStatus("mandatory")
_VlanNewCfgBwmContract_Type = Integer32
_VlanNewCfgBwmContract_Object = MibTableColumn
vlanNewCfgBwmContract = _VlanNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 9),
    _VlanNewCfgBwmContract_Type()
)
vlanNewCfgBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgBwmContract.setStatus("mandatory")
_Serverloadbalance_ObjectIdentity = ObjectIdentity
serverloadbalance = _Serverloadbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5)
)
_SlbRealServerMaxSize_Type = Integer32
_SlbRealServerMaxSize_Object = MibScalar
slbRealServerMaxSize = _SlbRealServerMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 1),
    _SlbRealServerMaxSize_Type()
)
slbRealServerMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerMaxSize.setStatus("mandatory")
_SlbCurCfgRealServerTable_Object = MibTable
slbCurCfgRealServerTable = _SlbCurCfgRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgRealServerTable.setStatus("mandatory")
_SlbCurCfgRealServerEntry_Object = MibTableRow
slbCurCfgRealServerEntry = _SlbCurCfgRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1)
)
slbCurCfgRealServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgRealServerEntry.setStatus("mandatory")
_SlbCurCfgRealServerIndex_Type = Integer32
_SlbCurCfgRealServerIndex_Object = MibTableColumn
slbCurCfgRealServerIndex = _SlbCurCfgRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 1),
    _SlbCurCfgRealServerIndex_Type()
)
slbCurCfgRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIndex.setStatus("mandatory")
_SlbCurCfgRealServerIpAddr_Type = IpAddress
_SlbCurCfgRealServerIpAddr_Object = MibTableColumn
slbCurCfgRealServerIpAddr = _SlbCurCfgRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 2),
    _SlbCurCfgRealServerIpAddr_Type()
)
slbCurCfgRealServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIpAddr.setStatus("mandatory")


class _SlbCurCfgRealServerWeight_Type(Integer32):
    """Custom type slbCurCfgRealServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbCurCfgRealServerWeight_Type.__name__ = "Integer32"
_SlbCurCfgRealServerWeight_Object = MibTableColumn
slbCurCfgRealServerWeight = _SlbCurCfgRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 3),
    _SlbCurCfgRealServerWeight_Type()
)
slbCurCfgRealServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerWeight.setStatus("mandatory")


class _SlbCurCfgRealServerMaxConns_Type(Integer32):
    """Custom type slbCurCfgRealServerMaxConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_SlbCurCfgRealServerMaxConns_Type.__name__ = "Integer32"
_SlbCurCfgRealServerMaxConns_Object = MibTableColumn
slbCurCfgRealServerMaxConns = _SlbCurCfgRealServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 4),
    _SlbCurCfgRealServerMaxConns_Type()
)
slbCurCfgRealServerMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerMaxConns.setStatus("mandatory")


class _SlbCurCfgRealServerTimeOut_Type(Integer32):
    """Custom type slbCurCfgRealServerTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_SlbCurCfgRealServerTimeOut_Type.__name__ = "Integer32"
_SlbCurCfgRealServerTimeOut_Object = MibTableColumn
slbCurCfgRealServerTimeOut = _SlbCurCfgRealServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 5),
    _SlbCurCfgRealServerTimeOut_Type()
)
slbCurCfgRealServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerTimeOut.setStatus("mandatory")


class _SlbCurCfgRealServerBackUp_Type(Integer32):
    """Custom type slbCurCfgRealServerBackUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_SlbCurCfgRealServerBackUp_Type.__name__ = "Integer32"
_SlbCurCfgRealServerBackUp_Object = MibTableColumn
slbCurCfgRealServerBackUp = _SlbCurCfgRealServerBackUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 6),
    _SlbCurCfgRealServerBackUp_Type()
)
slbCurCfgRealServerBackUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerBackUp.setStatus("mandatory")


class _SlbCurCfgRealServerPingInterval_Type(Integer32):
    """Custom type slbCurCfgRealServerPingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SlbCurCfgRealServerPingInterval_Type.__name__ = "Integer32"
_SlbCurCfgRealServerPingInterval_Object = MibTableColumn
slbCurCfgRealServerPingInterval = _SlbCurCfgRealServerPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 7),
    _SlbCurCfgRealServerPingInterval_Type()
)
slbCurCfgRealServerPingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerPingInterval.setStatus("mandatory")


class _SlbCurCfgRealServerFailRetry_Type(Integer32):
    """Custom type slbCurCfgRealServerFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgRealServerFailRetry_Type.__name__ = "Integer32"
_SlbCurCfgRealServerFailRetry_Object = MibTableColumn
slbCurCfgRealServerFailRetry = _SlbCurCfgRealServerFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 8),
    _SlbCurCfgRealServerFailRetry_Type()
)
slbCurCfgRealServerFailRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerFailRetry.setStatus("mandatory")


class _SlbCurCfgRealServerSuccRetry_Type(Integer32):
    """Custom type slbCurCfgRealServerSuccRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgRealServerSuccRetry_Type.__name__ = "Integer32"
_SlbCurCfgRealServerSuccRetry_Object = MibTableColumn
slbCurCfgRealServerSuccRetry = _SlbCurCfgRealServerSuccRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 9),
    _SlbCurCfgRealServerSuccRetry_Type()
)
slbCurCfgRealServerSuccRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerSuccRetry.setStatus("mandatory")


class _SlbCurCfgRealServerState_Type(Integer32):
    """Custom type slbCurCfgRealServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbCurCfgRealServerState_Type.__name__ = "Integer32"
_SlbCurCfgRealServerState_Object = MibTableColumn
slbCurCfgRealServerState = _SlbCurCfgRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 10),
    _SlbCurCfgRealServerState_Type()
)
slbCurCfgRealServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerState.setStatus("mandatory")


class _SlbCurCfgRealServerType_Type(Integer32):
    """Custom type slbCurCfgRealServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-server", 1),
          ("remote-server", 2))
    )


_SlbCurCfgRealServerType_Type.__name__ = "Integer32"
_SlbCurCfgRealServerType_Object = MibTableColumn
slbCurCfgRealServerType = _SlbCurCfgRealServerType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 11),
    _SlbCurCfgRealServerType_Type()
)
slbCurCfgRealServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerType.setStatus("mandatory")


class _SlbCurCfgRealServerName_Type(DisplayString):
    """Custom type slbCurCfgRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SlbCurCfgRealServerName_Type.__name__ = "DisplayString"
_SlbCurCfgRealServerName_Object = MibTableColumn
slbCurCfgRealServerName = _SlbCurCfgRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 12),
    _SlbCurCfgRealServerName_Type()
)
slbCurCfgRealServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerName.setStatus("mandatory")
_SlbCurCfgRealServerUrlBmap_Type = OctetString
_SlbCurCfgRealServerUrlBmap_Object = MibTableColumn
slbCurCfgRealServerUrlBmap = _SlbCurCfgRealServerUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 13),
    _SlbCurCfgRealServerUrlBmap_Type()
)
slbCurCfgRealServerUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerUrlBmap.setStatus("mandatory")


class _SlbCurCfgRealServerCookie_Type(Integer32):
    """Custom type slbCurCfgRealServerCookie based on Integer32"""
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


_SlbCurCfgRealServerCookie_Type.__name__ = "Integer32"
_SlbCurCfgRealServerCookie_Object = MibTableColumn
slbCurCfgRealServerCookie = _SlbCurCfgRealServerCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 14),
    _SlbCurCfgRealServerCookie_Type()
)
slbCurCfgRealServerCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerCookie.setStatus("mandatory")


class _SlbCurCfgRealServerExcludeStr_Type(Integer32):
    """Custom type slbCurCfgRealServerExcludeStr based on Integer32"""
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


_SlbCurCfgRealServerExcludeStr_Type.__name__ = "Integer32"
_SlbCurCfgRealServerExcludeStr_Object = MibTableColumn
slbCurCfgRealServerExcludeStr = _SlbCurCfgRealServerExcludeStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 15),
    _SlbCurCfgRealServerExcludeStr_Type()
)
slbCurCfgRealServerExcludeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerExcludeStr.setStatus("mandatory")


class _SlbCurCfgRealServerSubmac_Type(Integer32):
    """Custom type slbCurCfgRealServerSubmac based on Integer32"""
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


_SlbCurCfgRealServerSubmac_Type.__name__ = "Integer32"
_SlbCurCfgRealServerSubmac_Object = MibTableColumn
slbCurCfgRealServerSubmac = _SlbCurCfgRealServerSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 16),
    _SlbCurCfgRealServerSubmac_Type()
)
slbCurCfgRealServerSubmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerSubmac.setStatus("mandatory")
_SlbNewCfgRealServerTable_Object = MibTable
slbNewCfgRealServerTable = _SlbNewCfgRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgRealServerTable.setStatus("mandatory")
_SlbNewCfgRealServerEntry_Object = MibTableRow
slbNewCfgRealServerEntry = _SlbNewCfgRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1)
)
slbNewCfgRealServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgRealServerEntry.setStatus("mandatory")
_SlbNewCfgRealServerIndex_Type = Integer32
_SlbNewCfgRealServerIndex_Object = MibTableColumn
slbNewCfgRealServerIndex = _SlbNewCfgRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 1),
    _SlbNewCfgRealServerIndex_Type()
)
slbNewCfgRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIndex.setStatus("mandatory")
_SlbNewCfgRealServerIpAddr_Type = IpAddress
_SlbNewCfgRealServerIpAddr_Object = MibTableColumn
slbNewCfgRealServerIpAddr = _SlbNewCfgRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 2),
    _SlbNewCfgRealServerIpAddr_Type()
)
slbNewCfgRealServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIpAddr.setStatus("mandatory")


class _SlbNewCfgRealServerWeight_Type(Integer32):
    """Custom type slbNewCfgRealServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbNewCfgRealServerWeight_Type.__name__ = "Integer32"
_SlbNewCfgRealServerWeight_Object = MibTableColumn
slbNewCfgRealServerWeight = _SlbNewCfgRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 3),
    _SlbNewCfgRealServerWeight_Type()
)
slbNewCfgRealServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerWeight.setStatus("mandatory")


class _SlbNewCfgRealServerMaxConns_Type(Integer32):
    """Custom type slbNewCfgRealServerMaxConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_SlbNewCfgRealServerMaxConns_Type.__name__ = "Integer32"
_SlbNewCfgRealServerMaxConns_Object = MibTableColumn
slbNewCfgRealServerMaxConns = _SlbNewCfgRealServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 4),
    _SlbNewCfgRealServerMaxConns_Type()
)
slbNewCfgRealServerMaxConns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerMaxConns.setStatus("mandatory")


class _SlbNewCfgRealServerTimeOut_Type(Integer32):
    """Custom type slbNewCfgRealServerTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_SlbNewCfgRealServerTimeOut_Type.__name__ = "Integer32"
_SlbNewCfgRealServerTimeOut_Object = MibTableColumn
slbNewCfgRealServerTimeOut = _SlbNewCfgRealServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 5),
    _SlbNewCfgRealServerTimeOut_Type()
)
slbNewCfgRealServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerTimeOut.setStatus("mandatory")


class _SlbNewCfgRealServerBackUp_Type(Integer32):
    """Custom type slbNewCfgRealServerBackUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_SlbNewCfgRealServerBackUp_Type.__name__ = "Integer32"
_SlbNewCfgRealServerBackUp_Object = MibTableColumn
slbNewCfgRealServerBackUp = _SlbNewCfgRealServerBackUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 6),
    _SlbNewCfgRealServerBackUp_Type()
)
slbNewCfgRealServerBackUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerBackUp.setStatus("mandatory")


class _SlbNewCfgRealServerPingInterval_Type(Integer32):
    """Custom type slbNewCfgRealServerPingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SlbNewCfgRealServerPingInterval_Type.__name__ = "Integer32"
_SlbNewCfgRealServerPingInterval_Object = MibTableColumn
slbNewCfgRealServerPingInterval = _SlbNewCfgRealServerPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 7),
    _SlbNewCfgRealServerPingInterval_Type()
)
slbNewCfgRealServerPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerPingInterval.setStatus("mandatory")


class _SlbNewCfgRealServerFailRetry_Type(Integer32):
    """Custom type slbNewCfgRealServerFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgRealServerFailRetry_Type.__name__ = "Integer32"
_SlbNewCfgRealServerFailRetry_Object = MibTableColumn
slbNewCfgRealServerFailRetry = _SlbNewCfgRealServerFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 8),
    _SlbNewCfgRealServerFailRetry_Type()
)
slbNewCfgRealServerFailRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerFailRetry.setStatus("mandatory")


class _SlbNewCfgRealServerSuccRetry_Type(Integer32):
    """Custom type slbNewCfgRealServerSuccRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgRealServerSuccRetry_Type.__name__ = "Integer32"
_SlbNewCfgRealServerSuccRetry_Object = MibTableColumn
slbNewCfgRealServerSuccRetry = _SlbNewCfgRealServerSuccRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 9),
    _SlbNewCfgRealServerSuccRetry_Type()
)
slbNewCfgRealServerSuccRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerSuccRetry.setStatus("mandatory")


class _SlbNewCfgRealServerState_Type(Integer32):
    """Custom type slbNewCfgRealServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbNewCfgRealServerState_Type.__name__ = "Integer32"
_SlbNewCfgRealServerState_Object = MibTableColumn
slbNewCfgRealServerState = _SlbNewCfgRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 10),
    _SlbNewCfgRealServerState_Type()
)
slbNewCfgRealServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerState.setStatus("mandatory")


class _SlbNewCfgRealServerDelete_Type(Integer32):
    """Custom type slbNewCfgRealServerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgRealServerDelete_Type.__name__ = "Integer32"
_SlbNewCfgRealServerDelete_Object = MibTableColumn
slbNewCfgRealServerDelete = _SlbNewCfgRealServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 11),
    _SlbNewCfgRealServerDelete_Type()
)
slbNewCfgRealServerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerDelete.setStatus("mandatory")


class _SlbNewCfgRealServerType_Type(Integer32):
    """Custom type slbNewCfgRealServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-server", 1),
          ("remote-server", 2))
    )


_SlbNewCfgRealServerType_Type.__name__ = "Integer32"
_SlbNewCfgRealServerType_Object = MibTableColumn
slbNewCfgRealServerType = _SlbNewCfgRealServerType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 12),
    _SlbNewCfgRealServerType_Type()
)
slbNewCfgRealServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerType.setStatus("mandatory")


class _SlbNewCfgRealServerName_Type(DisplayString):
    """Custom type slbNewCfgRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SlbNewCfgRealServerName_Type.__name__ = "DisplayString"
_SlbNewCfgRealServerName_Object = MibTableColumn
slbNewCfgRealServerName = _SlbNewCfgRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 13),
    _SlbNewCfgRealServerName_Type()
)
slbNewCfgRealServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerName.setStatus("mandatory")
_SlbNewCfgRealServerUrlBmap_Type = OctetString
_SlbNewCfgRealServerUrlBmap_Object = MibTableColumn
slbNewCfgRealServerUrlBmap = _SlbNewCfgRealServerUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 14),
    _SlbNewCfgRealServerUrlBmap_Type()
)
slbNewCfgRealServerUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServerUrlBmap.setStatus("mandatory")
_SlbNewCfgRealServerAddUrl_Type = Integer32
_SlbNewCfgRealServerAddUrl_Object = MibTableColumn
slbNewCfgRealServerAddUrl = _SlbNewCfgRealServerAddUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 15),
    _SlbNewCfgRealServerAddUrl_Type()
)
slbNewCfgRealServerAddUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerAddUrl.setStatus("mandatory")
_SlbNewCfgRealServerRemUrl_Type = Integer32
_SlbNewCfgRealServerRemUrl_Object = MibTableColumn
slbNewCfgRealServerRemUrl = _SlbNewCfgRealServerRemUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 16),
    _SlbNewCfgRealServerRemUrl_Type()
)
slbNewCfgRealServerRemUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerRemUrl.setStatus("mandatory")


class _SlbNewCfgRealServerCookie_Type(Integer32):
    """Custom type slbNewCfgRealServerCookie based on Integer32"""
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


_SlbNewCfgRealServerCookie_Type.__name__ = "Integer32"
_SlbNewCfgRealServerCookie_Object = MibTableColumn
slbNewCfgRealServerCookie = _SlbNewCfgRealServerCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 17),
    _SlbNewCfgRealServerCookie_Type()
)
slbNewCfgRealServerCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerCookie.setStatus("mandatory")


class _SlbNewCfgRealServerExcludeStr_Type(Integer32):
    """Custom type slbNewCfgRealServerExcludeStr based on Integer32"""
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


_SlbNewCfgRealServerExcludeStr_Type.__name__ = "Integer32"
_SlbNewCfgRealServerExcludeStr_Object = MibTableColumn
slbNewCfgRealServerExcludeStr = _SlbNewCfgRealServerExcludeStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 18),
    _SlbNewCfgRealServerExcludeStr_Type()
)
slbNewCfgRealServerExcludeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerExcludeStr.setStatus("mandatory")


class _SlbNewCfgRealServerSubmac_Type(Integer32):
    """Custom type slbNewCfgRealServerSubmac based on Integer32"""
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


_SlbNewCfgRealServerSubmac_Type.__name__ = "Integer32"
_SlbNewCfgRealServerSubmac_Object = MibTableColumn
slbNewCfgRealServerSubmac = _SlbNewCfgRealServerSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 19),
    _SlbNewCfgRealServerSubmac_Type()
)
slbNewCfgRealServerSubmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerSubmac.setStatus("mandatory")
_SlbVirtServerTableMaxSize_Type = Integer32
_SlbVirtServerTableMaxSize_Object = MibScalar
slbVirtServerTableMaxSize = _SlbVirtServerTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 4),
    _SlbVirtServerTableMaxSize_Type()
)
slbVirtServerTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServerTableMaxSize.setStatus("mandatory")
_SlbCurCfgVirtServerTable_Object = MibTable
slbCurCfgVirtServerTable = _SlbCurCfgVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServerTable.setStatus("mandatory")
_SlbCurCfgVirtualServerEntry_Object = MibTableRow
slbCurCfgVirtualServerEntry = _SlbCurCfgVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1)
)
slbCurCfgVirtualServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgVirtServerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgVirtualServerEntry.setStatus("mandatory")
_SlbCurCfgVirtServerIndex_Type = Integer32
_SlbCurCfgVirtServerIndex_Object = MibTableColumn
slbCurCfgVirtServerIndex = _SlbCurCfgVirtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 1),
    _SlbCurCfgVirtServerIndex_Type()
)
slbCurCfgVirtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIndex.setStatus("mandatory")
_SlbCurCfgVirtServerIpAddress_Type = IpAddress
_SlbCurCfgVirtServerIpAddress_Object = MibTableColumn
slbCurCfgVirtServerIpAddress = _SlbCurCfgVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 2),
    _SlbCurCfgVirtServerIpAddress_Type()
)
slbCurCfgVirtServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIpAddress.setStatus("mandatory")


class _SlbCurCfgVirtServerLayer3Only_Type(Integer32):
    """Custom type slbCurCfgVirtServerLayer3Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("layer3Only", 1))
    )


_SlbCurCfgVirtServerLayer3Only_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerLayer3Only_Object = MibTableColumn
slbCurCfgVirtServerLayer3Only = _SlbCurCfgVirtServerLayer3Only_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 3),
    _SlbCurCfgVirtServerLayer3Only_Type()
)
slbCurCfgVirtServerLayer3Only.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerLayer3Only.setStatus("mandatory")


class _SlbCurCfgVirtServerState_Type(Integer32):
    """Custom type slbCurCfgVirtServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbCurCfgVirtServerState_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerState_Object = MibTableColumn
slbCurCfgVirtServerState = _SlbCurCfgVirtServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 4),
    _SlbCurCfgVirtServerState_Type()
)
slbCurCfgVirtServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerState.setStatus("mandatory")


class _SlbCurCfgVirtServerDname_Type(DisplayString):
    """Custom type slbCurCfgVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbCurCfgVirtServerDname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerDname_Object = MibTableColumn
slbCurCfgVirtServerDname = _SlbCurCfgVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 5),
    _SlbCurCfgVirtServerDname_Type()
)
slbCurCfgVirtServerDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerDname.setStatus("mandatory")


class _SlbCurCfgVirtServerCname_Type(DisplayString):
    """Custom type slbCurCfgVirtServerCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlbCurCfgVirtServerCname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerCname_Object = MibTableColumn
slbCurCfgVirtServerCname = _SlbCurCfgVirtServerCname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 6),
    _SlbCurCfgVirtServerCname_Type()
)
slbCurCfgVirtServerCname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerCname.setStatus("mandatory")


class _SlbCurCfgVirtServerCoffset_Type(Integer32):
    """Custom type slbCurCfgVirtServerCoffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlbCurCfgVirtServerCoffset_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerCoffset_Object = MibTableColumn
slbCurCfgVirtServerCoffset = _SlbCurCfgVirtServerCoffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 7),
    _SlbCurCfgVirtServerCoffset_Type()
)
slbCurCfgVirtServerCoffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerCoffset.setStatus("mandatory")


class _SlbCurCfgVirtServerClength_Type(Integer32):
    """Custom type slbCurCfgVirtServerClength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlbCurCfgVirtServerClength_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerClength_Object = MibTableColumn
slbCurCfgVirtServerClength = _SlbCurCfgVirtServerClength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 8),
    _SlbCurCfgVirtServerClength_Type()
)
slbCurCfgVirtServerClength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerClength.setStatus("mandatory")


class _SlbCurCfgVirtServerUriCookie_Type(Integer32):
    """Custom type slbCurCfgVirtServerUriCookie based on Integer32"""
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


_SlbCurCfgVirtServerUriCookie_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerUriCookie_Object = MibTableColumn
slbCurCfgVirtServerUriCookie = _SlbCurCfgVirtServerUriCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 9),
    _SlbCurCfgVirtServerUriCookie_Type()
)
slbCurCfgVirtServerUriCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerUriCookie.setStatus("mandatory")


class _SlbCurCfgVirtServerFtpParsing_Type(Integer32):
    """Custom type slbCurCfgVirtServerFtpParsing based on Integer32"""
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


_SlbCurCfgVirtServerFtpParsing_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerFtpParsing_Object = MibTableColumn
slbCurCfgVirtServerFtpParsing = _SlbCurCfgVirtServerFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 10),
    _SlbCurCfgVirtServerFtpParsing_Type()
)
slbCurCfgVirtServerFtpParsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerFtpParsing.setStatus("mandatory")


class _SlbCurCfgVirtServerUrlHashLen_Type(Integer32):
    """Custom type slbCurCfgVirtServerUrlHashLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbCurCfgVirtServerUrlHashLen_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerUrlHashLen_Object = MibTableColumn
slbCurCfgVirtServerUrlHashLen = _SlbCurCfgVirtServerUrlHashLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 11),
    _SlbCurCfgVirtServerUrlHashLen_Type()
)
slbCurCfgVirtServerUrlHashLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerUrlHashLen.setStatus("mandatory")


class _SlbCurCfgVirtServerHttpHdrName_Type(DisplayString):
    """Custom type slbCurCfgVirtServerHttpHdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgVirtServerHttpHdrName_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerHttpHdrName_Object = MibTableColumn
slbCurCfgVirtServerHttpHdrName = _SlbCurCfgVirtServerHttpHdrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 12),
    _SlbCurCfgVirtServerHttpHdrName_Type()
)
slbCurCfgVirtServerHttpHdrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerHttpHdrName.setStatus("mandatory")
_SlbCurCfgVirtServerBwmContract_Type = Integer32
_SlbCurCfgVirtServerBwmContract_Object = MibTableColumn
slbCurCfgVirtServerBwmContract = _SlbCurCfgVirtServerBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 13),
    _SlbCurCfgVirtServerBwmContract_Type()
)
slbCurCfgVirtServerBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerBwmContract.setStatus("mandatory")
_SlbNewCfgVirtServerTable_Object = MibTable
slbNewCfgVirtServerTable = _SlbNewCfgVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServerTable.setStatus("mandatory")
_SlbNewCfgVirtualServerEntry_Object = MibTableRow
slbNewCfgVirtualServerEntry = _SlbNewCfgVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1)
)
slbNewCfgVirtualServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgVirtServerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgVirtualServerEntry.setStatus("mandatory")
_SlbNewCfgVirtServerIndex_Type = Integer32
_SlbNewCfgVirtServerIndex_Object = MibTableColumn
slbNewCfgVirtServerIndex = _SlbNewCfgVirtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 1),
    _SlbNewCfgVirtServerIndex_Type()
)
slbNewCfgVirtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIndex.setStatus("mandatory")
_SlbNewCfgVirtServerIpAddress_Type = IpAddress
_SlbNewCfgVirtServerIpAddress_Object = MibTableColumn
slbNewCfgVirtServerIpAddress = _SlbNewCfgVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 2),
    _SlbNewCfgVirtServerIpAddress_Type()
)
slbNewCfgVirtServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIpAddress.setStatus("mandatory")


class _SlbNewCfgVirtServerLayer3Only_Type(Integer32):
    """Custom type slbNewCfgVirtServerLayer3Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("layer3Only", 1))
    )


_SlbNewCfgVirtServerLayer3Only_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerLayer3Only_Object = MibTableColumn
slbNewCfgVirtServerLayer3Only = _SlbNewCfgVirtServerLayer3Only_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 3),
    _SlbNewCfgVirtServerLayer3Only_Type()
)
slbNewCfgVirtServerLayer3Only.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerLayer3Only.setStatus("mandatory")


class _SlbNewCfgVirtServerState_Type(Integer32):
    """Custom type slbNewCfgVirtServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbNewCfgVirtServerState_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerState_Object = MibTableColumn
slbNewCfgVirtServerState = _SlbNewCfgVirtServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 4),
    _SlbNewCfgVirtServerState_Type()
)
slbNewCfgVirtServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerState.setStatus("mandatory")


class _SlbNewCfgVirtServerDelete_Type(Integer32):
    """Custom type slbNewCfgVirtServerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgVirtServerDelete_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerDelete_Object = MibTableColumn
slbNewCfgVirtServerDelete = _SlbNewCfgVirtServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 5),
    _SlbNewCfgVirtServerDelete_Type()
)
slbNewCfgVirtServerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerDelete.setStatus("mandatory")


class _SlbNewCfgVirtServerDname_Type(DisplayString):
    """Custom type slbNewCfgVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbNewCfgVirtServerDname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerDname_Object = MibTableColumn
slbNewCfgVirtServerDname = _SlbNewCfgVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 6),
    _SlbNewCfgVirtServerDname_Type()
)
slbNewCfgVirtServerDname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerDname.setStatus("mandatory")


class _SlbNewCfgVirtServerCname_Type(DisplayString):
    """Custom type slbNewCfgVirtServerCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlbNewCfgVirtServerCname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerCname_Object = MibTableColumn
slbNewCfgVirtServerCname = _SlbNewCfgVirtServerCname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 7),
    _SlbNewCfgVirtServerCname_Type()
)
slbNewCfgVirtServerCname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerCname.setStatus("mandatory")


class _SlbNewCfgVirtServerCoffset_Type(Integer32):
    """Custom type slbNewCfgVirtServerCoffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlbNewCfgVirtServerCoffset_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerCoffset_Object = MibTableColumn
slbNewCfgVirtServerCoffset = _SlbNewCfgVirtServerCoffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 8),
    _SlbNewCfgVirtServerCoffset_Type()
)
slbNewCfgVirtServerCoffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerCoffset.setStatus("mandatory")


class _SlbNewCfgVirtServerClength_Type(Integer32):
    """Custom type slbNewCfgVirtServerClength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlbNewCfgVirtServerClength_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerClength_Object = MibTableColumn
slbNewCfgVirtServerClength = _SlbNewCfgVirtServerClength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 9),
    _SlbNewCfgVirtServerClength_Type()
)
slbNewCfgVirtServerClength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerClength.setStatus("mandatory")


class _SlbNewCfgVirtServerUriCookie_Type(Integer32):
    """Custom type slbNewCfgVirtServerUriCookie based on Integer32"""
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


_SlbNewCfgVirtServerUriCookie_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerUriCookie_Object = MibTableColumn
slbNewCfgVirtServerUriCookie = _SlbNewCfgVirtServerUriCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 10),
    _SlbNewCfgVirtServerUriCookie_Type()
)
slbNewCfgVirtServerUriCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerUriCookie.setStatus("mandatory")


class _SlbNewCfgVirtServerFtpParsing_Type(Integer32):
    """Custom type slbNewCfgVirtServerFtpParsing based on Integer32"""
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


_SlbNewCfgVirtServerFtpParsing_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerFtpParsing_Object = MibTableColumn
slbNewCfgVirtServerFtpParsing = _SlbNewCfgVirtServerFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 11),
    _SlbNewCfgVirtServerFtpParsing_Type()
)
slbNewCfgVirtServerFtpParsing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerFtpParsing.setStatus("mandatory")


class _SlbNewCfgVirtServerUrlHashLen_Type(Integer32):
    """Custom type slbNewCfgVirtServerUrlHashLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbNewCfgVirtServerUrlHashLen_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerUrlHashLen_Object = MibTableColumn
slbNewCfgVirtServerUrlHashLen = _SlbNewCfgVirtServerUrlHashLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 12),
    _SlbNewCfgVirtServerUrlHashLen_Type()
)
slbNewCfgVirtServerUrlHashLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerUrlHashLen.setStatus("mandatory")


class _SlbNewCfgVirtServerHttpHdrName_Type(DisplayString):
    """Custom type slbNewCfgVirtServerHttpHdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgVirtServerHttpHdrName_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerHttpHdrName_Object = MibTableColumn
slbNewCfgVirtServerHttpHdrName = _SlbNewCfgVirtServerHttpHdrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 13),
    _SlbNewCfgVirtServerHttpHdrName_Type()
)
slbNewCfgVirtServerHttpHdrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerHttpHdrName.setStatus("mandatory")
_SlbNewCfgVirtServerBwmContract_Type = Integer32
_SlbNewCfgVirtServerBwmContract_Object = MibTableColumn
slbNewCfgVirtServerBwmContract = _SlbNewCfgVirtServerBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 14),
    _SlbNewCfgVirtServerBwmContract_Type()
)
slbNewCfgVirtServerBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerBwmContract.setStatus("mandatory")
_SlbCurCfgVirtServicesTable_Object = MibTable
slbCurCfgVirtServicesTable = _SlbCurCfgVirtServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServicesTable.setStatus("mandatory")
_SlbCurCfgVirtServicesEntry_Object = MibTableRow
slbCurCfgVirtServicesEntry = _SlbCurCfgVirtServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1)
)
slbCurCfgVirtServicesEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgVirtServIndex"),
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgVirtServiceIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServicesEntry.setStatus("mandatory")
_SlbCurCfgVirtServIndex_Type = Integer32
_SlbCurCfgVirtServIndex_Object = MibTableColumn
slbCurCfgVirtServIndex = _SlbCurCfgVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 1),
    _SlbCurCfgVirtServIndex_Type()
)
slbCurCfgVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServIndex.setStatus("mandatory")
_SlbCurCfgVirtServiceIndex_Type = Integer32
_SlbCurCfgVirtServiceIndex_Object = MibTableColumn
slbCurCfgVirtServiceIndex = _SlbCurCfgVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 2),
    _SlbCurCfgVirtServiceIndex_Type()
)
slbCurCfgVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceIndex.setStatus("mandatory")
_SlbCurCfgVirtServiceVirtPort_Type = Integer32
_SlbCurCfgVirtServiceVirtPort_Object = MibTableColumn
slbCurCfgVirtServiceVirtPort = _SlbCurCfgVirtServiceVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 3),
    _SlbCurCfgVirtServiceVirtPort_Type()
)
slbCurCfgVirtServiceVirtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceVirtPort.setStatus("mandatory")
_SlbCurCfgVirtServiceRealGroup_Type = Integer32
_SlbCurCfgVirtServiceRealGroup_Object = MibTableColumn
slbCurCfgVirtServiceRealGroup = _SlbCurCfgVirtServiceRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 4),
    _SlbCurCfgVirtServiceRealGroup_Type()
)
slbCurCfgVirtServiceRealGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRealGroup.setStatus("mandatory")
_SlbCurCfgVirtServiceRealPort_Type = Integer32
_SlbCurCfgVirtServiceRealPort_Object = MibTableColumn
slbCurCfgVirtServiceRealPort = _SlbCurCfgVirtServiceRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 5),
    _SlbCurCfgVirtServiceRealPort_Type()
)
slbCurCfgVirtServiceRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRealPort.setStatus("mandatory")


class _SlbCurCfgVirtServiceUDPBalance_Type(Integer32):
    """Custom type slbCurCfgVirtServiceUDPBalance based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1),
          ("stateless", 4))
    )


_SlbCurCfgVirtServiceUDPBalance_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceUDPBalance_Object = MibTableColumn
slbCurCfgVirtServiceUDPBalance = _SlbCurCfgVirtServiceUDPBalance_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 6),
    _SlbCurCfgVirtServiceUDPBalance_Type()
)
slbCurCfgVirtServiceUDPBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceUDPBalance.setStatus("mandatory")


class _SlbCurCfgVirtServicePBind_Type(Integer32):
    """Custom type slbCurCfgVirtServicePBind based on Integer32"""
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
        *(("cookie", 5),
          ("disabled", 3),
          ("enabled", 2),
          ("other", 1),
          ("sessid", 4))
    )


_SlbCurCfgVirtServicePBind_Type.__name__ = "Integer32"
_SlbCurCfgVirtServicePBind_Object = MibTableColumn
slbCurCfgVirtServicePBind = _SlbCurCfgVirtServicePBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 7),
    _SlbCurCfgVirtServicePBind_Type()
)
slbCurCfgVirtServicePBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServicePBind.setStatus("mandatory")


class _SlbCurCfgVirtServiceHname_Type(DisplayString):
    """Custom type slbCurCfgVirtServiceHname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SlbCurCfgVirtServiceHname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServiceHname_Object = MibTableColumn
slbCurCfgVirtServiceHname = _SlbCurCfgVirtServiceHname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 8),
    _SlbCurCfgVirtServiceHname_Type()
)
slbCurCfgVirtServiceHname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHname.setStatus("mandatory")


class _SlbCurCfgVirtServiceHttpSlb_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpSlb based on Integer32"""
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
        *(("browser", 6),
          ("cookie", 4),
          ("disabled", 1),
          ("host", 5),
          ("others", 7),
          ("urlhash", 3),
          ("urlslb", 2))
    )


_SlbCurCfgVirtServiceHttpSlb_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpSlb_Object = MibTableColumn
slbCurCfgVirtServiceHttpSlb = _SlbCurCfgVirtServiceHttpSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 9),
    _SlbCurCfgVirtServiceHttpSlb_Type()
)
slbCurCfgVirtServiceHttpSlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpSlb.setStatus("mandatory")
_SlbCurCfgVirtServiceBwmContract_Type = Integer32
_SlbCurCfgVirtServiceBwmContract_Object = MibTableColumn
slbCurCfgVirtServiceBwmContract = _SlbCurCfgVirtServiceBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 10),
    _SlbCurCfgVirtServiceBwmContract_Type()
)
slbCurCfgVirtServiceBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceBwmContract.setStatus("mandatory")


class _SlbCurCfgVirtServiceDirServerRtn_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDirServerRtn based on Integer32"""
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


_SlbCurCfgVirtServiceDirServerRtn_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDirServerRtn_Object = MibTableColumn
slbCurCfgVirtServiceDirServerRtn = _SlbCurCfgVirtServiceDirServerRtn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 11),
    _SlbCurCfgVirtServiceDirServerRtn_Type()
)
slbCurCfgVirtServiceDirServerRtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDirServerRtn.setStatus("mandatory")
_SlbNewCfgVirtServicesTable_Object = MibTable
slbNewCfgVirtServicesTable = _SlbNewCfgVirtServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServicesTable.setStatus("mandatory")
_SlbNewCfgVirtServicesEntry_Object = MibTableRow
slbNewCfgVirtServicesEntry = _SlbNewCfgVirtServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1)
)
slbNewCfgVirtServicesEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgVirtServIndex"),
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgVirtServiceIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServicesEntry.setStatus("mandatory")
_SlbNewCfgVirtServIndex_Type = Integer32
_SlbNewCfgVirtServIndex_Object = MibTableColumn
slbNewCfgVirtServIndex = _SlbNewCfgVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 1),
    _SlbNewCfgVirtServIndex_Type()
)
slbNewCfgVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServIndex.setStatus("mandatory")
_SlbNewCfgVirtServiceIndex_Type = Integer32
_SlbNewCfgVirtServiceIndex_Object = MibTableColumn
slbNewCfgVirtServiceIndex = _SlbNewCfgVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 2),
    _SlbNewCfgVirtServiceIndex_Type()
)
slbNewCfgVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceIndex.setStatus("mandatory")
_SlbNewCfgVirtServiceVirtPort_Type = Integer32
_SlbNewCfgVirtServiceVirtPort_Object = MibTableColumn
slbNewCfgVirtServiceVirtPort = _SlbNewCfgVirtServiceVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 3),
    _SlbNewCfgVirtServiceVirtPort_Type()
)
slbNewCfgVirtServiceVirtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceVirtPort.setStatus("mandatory")
_SlbNewCfgVirtServiceRealGroup_Type = Integer32
_SlbNewCfgVirtServiceRealGroup_Object = MibTableColumn
slbNewCfgVirtServiceRealGroup = _SlbNewCfgVirtServiceRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 4),
    _SlbNewCfgVirtServiceRealGroup_Type()
)
slbNewCfgVirtServiceRealGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRealGroup.setStatus("mandatory")
_SlbNewCfgVirtServiceRealPort_Type = Integer32
_SlbNewCfgVirtServiceRealPort_Object = MibTableColumn
slbNewCfgVirtServiceRealPort = _SlbNewCfgVirtServiceRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 5),
    _SlbNewCfgVirtServiceRealPort_Type()
)
slbNewCfgVirtServiceRealPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRealPort.setStatus("mandatory")


class _SlbNewCfgVirtServiceUDPBalance_Type(Integer32):
    """Custom type slbNewCfgVirtServiceUDPBalance based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1),
          ("stateless", 4))
    )


_SlbNewCfgVirtServiceUDPBalance_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceUDPBalance_Object = MibTableColumn
slbNewCfgVirtServiceUDPBalance = _SlbNewCfgVirtServiceUDPBalance_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 6),
    _SlbNewCfgVirtServiceUDPBalance_Type()
)
slbNewCfgVirtServiceUDPBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceUDPBalance.setStatus("mandatory")


class _SlbNewCfgVirtServicePBind_Type(Integer32):
    """Custom type slbNewCfgVirtServicePBind based on Integer32"""
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
        *(("cookie", 5),
          ("disabled", 3),
          ("enabled", 2),
          ("other", 1),
          ("sessid", 4))
    )


_SlbNewCfgVirtServicePBind_Type.__name__ = "Integer32"
_SlbNewCfgVirtServicePBind_Object = MibTableColumn
slbNewCfgVirtServicePBind = _SlbNewCfgVirtServicePBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 7),
    _SlbNewCfgVirtServicePBind_Type()
)
slbNewCfgVirtServicePBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServicePBind.setStatus("mandatory")


class _SlbNewCfgVirtServiceHname_Type(DisplayString):
    """Custom type slbNewCfgVirtServiceHname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SlbNewCfgVirtServiceHname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServiceHname_Object = MibTableColumn
slbNewCfgVirtServiceHname = _SlbNewCfgVirtServiceHname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 8),
    _SlbNewCfgVirtServiceHname_Type()
)
slbNewCfgVirtServiceHname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHname.setStatus("mandatory")


class _SlbNewCfgVirtServiceHttpSlb_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpSlb based on Integer32"""
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
        *(("browser", 6),
          ("cookie", 4),
          ("disabled", 1),
          ("host", 5),
          ("others", 7),
          ("urlhash", 3),
          ("urlslb", 2))
    )


_SlbNewCfgVirtServiceHttpSlb_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpSlb_Object = MibTableColumn
slbNewCfgVirtServiceHttpSlb = _SlbNewCfgVirtServiceHttpSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 9),
    _SlbNewCfgVirtServiceHttpSlb_Type()
)
slbNewCfgVirtServiceHttpSlb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpSlb.setStatus("mandatory")
_SlbNewCfgVirtServiceBwmContract_Type = Integer32
_SlbNewCfgVirtServiceBwmContract_Object = MibTableColumn
slbNewCfgVirtServiceBwmContract = _SlbNewCfgVirtServiceBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 10),
    _SlbNewCfgVirtServiceBwmContract_Type()
)
slbNewCfgVirtServiceBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceBwmContract.setStatus("mandatory")


class _SlbNewCfgVirtServiceDirServerRtn_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDirServerRtn based on Integer32"""
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


_SlbNewCfgVirtServiceDirServerRtn_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDirServerRtn_Object = MibTableColumn
slbNewCfgVirtServiceDirServerRtn = _SlbNewCfgVirtServiceDirServerRtn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 11),
    _SlbNewCfgVirtServiceDirServerRtn_Type()
)
slbNewCfgVirtServiceDirServerRtn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDirServerRtn.setStatus("mandatory")


class _SlbNewCfgVirtServiceDelete_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgVirtServiceDelete_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDelete_Object = MibTableColumn
slbNewCfgVirtServiceDelete = _SlbNewCfgVirtServiceDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 12),
    _SlbNewCfgVirtServiceDelete_Type()
)
slbNewCfgVirtServiceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDelete.setStatus("mandatory")
_SlbGroupTableMaxSize_Type = Integer32
_SlbGroupTableMaxSize_Object = MibScalar
slbGroupTableMaxSize = _SlbGroupTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 9),
    _SlbGroupTableMaxSize_Type()
)
slbGroupTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbGroupTableMaxSize.setStatus("mandatory")
_SlbCurCfgGroupTable_Object = MibTable
slbCurCfgGroupTable = _SlbCurCfgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10)
)
if mibBuilder.loadTexts:
    slbCurCfgGroupTable.setStatus("mandatory")
_SlbCurCfgGroupEntry_Object = MibTableRow
slbCurCfgGroupEntry = _SlbCurCfgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1)
)
slbCurCfgGroupEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgGroupIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgGroupEntry.setStatus("mandatory")
_SlbCurCfgGroupIndex_Type = Integer32
_SlbCurCfgGroupIndex_Object = MibTableColumn
slbCurCfgGroupIndex = _SlbCurCfgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 1),
    _SlbCurCfgGroupIndex_Type()
)
slbCurCfgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupIndex.setStatus("mandatory")


class _SlbCurCfgGroupRealServers_Type(OctetString):
    """Custom type slbCurCfgGroupRealServers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbCurCfgGroupRealServers_Type.__name__ = "OctetString"
_SlbCurCfgGroupRealServers_Object = MibTableColumn
slbCurCfgGroupRealServers = _SlbCurCfgGroupRealServers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 2),
    _SlbCurCfgGroupRealServers_Type()
)
slbCurCfgGroupRealServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealServers.setStatus("mandatory")


class _SlbCurCfgGroupMetric_Type(Integer32):
    """Custom type slbCurCfgGroupMetric based on Integer32"""
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
        *(("hash", 4),
          ("leastConnections", 2),
          ("minMisses", 3),
          ("roundRobin", 1))
    )


_SlbCurCfgGroupMetric_Type.__name__ = "Integer32"
_SlbCurCfgGroupMetric_Object = MibTableColumn
slbCurCfgGroupMetric = _SlbCurCfgGroupMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 3),
    _SlbCurCfgGroupMetric_Type()
)
slbCurCfgGroupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupMetric.setStatus("mandatory")


class _SlbCurCfgGroupBackupServer_Type(Integer32):
    """Custom type slbCurCfgGroupBackupServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_SlbCurCfgGroupBackupServer_Type.__name__ = "Integer32"
_SlbCurCfgGroupBackupServer_Object = MibTableColumn
slbCurCfgGroupBackupServer = _SlbCurCfgGroupBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 4),
    _SlbCurCfgGroupBackupServer_Type()
)
slbCurCfgGroupBackupServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupBackupServer.setStatus("mandatory")


class _SlbCurCfgGroupHealthCheckUrl_Type(DisplayString):
    """Custom type slbCurCfgGroupHealthCheckUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgGroupHealthCheckUrl_Type.__name__ = "DisplayString"
_SlbCurCfgGroupHealthCheckUrl_Object = MibTableColumn
slbCurCfgGroupHealthCheckUrl = _SlbCurCfgGroupHealthCheckUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 5),
    _SlbCurCfgGroupHealthCheckUrl_Type()
)
slbCurCfgGroupHealthCheckUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupHealthCheckUrl.setStatus("mandatory")


class _SlbCurCfgGroupHealthCheckLayer_Type(Integer32):
    """Custom type slbCurCfgGroupHealthCheckLayer based on Integer32"""
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
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dns", 4),
          ("ftp", 8),
          ("http", 3),
          ("icmp", 1),
          ("imap", 9),
          ("nntp", 7),
          ("pop3", 6),
          ("radius", 10),
          ("script1", 12),
          ("script2", 13),
          ("script3", 14),
          ("script4", 15),
          ("script5", 16),
          ("script6", 17),
          ("script7", 18),
          ("script8", 19),
          ("smtp", 5),
          ("sslh", 11),
          ("tcp", 2))
    )


_SlbCurCfgGroupHealthCheckLayer_Type.__name__ = "Integer32"
_SlbCurCfgGroupHealthCheckLayer_Object = MibTableColumn
slbCurCfgGroupHealthCheckLayer = _SlbCurCfgGroupHealthCheckLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 6),
    _SlbCurCfgGroupHealthCheckLayer_Type()
)
slbCurCfgGroupHealthCheckLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupHealthCheckLayer.setStatus("mandatory")


class _SlbCurCfgGroupName_Type(DisplayString):
    """Custom type slbCurCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SlbCurCfgGroupName_Type.__name__ = "DisplayString"
_SlbCurCfgGroupName_Object = MibTableColumn
slbCurCfgGroupName = _SlbCurCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 7),
    _SlbCurCfgGroupName_Type()
)
slbCurCfgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupName.setStatus("mandatory")


class _SlbCurCfgGroupRealThreshold_Type(Integer32):
    """Custom type slbCurCfgGroupRealThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbCurCfgGroupRealThreshold_Type.__name__ = "Integer32"
_SlbCurCfgGroupRealThreshold_Object = MibTableColumn
slbCurCfgGroupRealThreshold = _SlbCurCfgGroupRealThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 8),
    _SlbCurCfgGroupRealThreshold_Type()
)
slbCurCfgGroupRealThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealThreshold.setStatus("mandatory")


class _SlbCurCfgGroupBackupGroup_Type(Integer32):
    """Custom type slbCurCfgGroupBackupGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_SlbCurCfgGroupBackupGroup_Type.__name__ = "Integer32"
_SlbCurCfgGroupBackupGroup_Object = MibTableColumn
slbCurCfgGroupBackupGroup = _SlbCurCfgGroupBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 9),
    _SlbCurCfgGroupBackupGroup_Type()
)
slbCurCfgGroupBackupGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupBackupGroup.setStatus("mandatory")
_SlbNewCfgGroupTable_Object = MibTable
slbNewCfgGroupTable = _SlbNewCfgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11)
)
if mibBuilder.loadTexts:
    slbNewCfgGroupTable.setStatus("mandatory")
_SlbNewCfgGroupEntry_Object = MibTableRow
slbNewCfgGroupEntry = _SlbNewCfgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1)
)
slbNewCfgGroupEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgGroupIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgGroupEntry.setStatus("mandatory")
_SlbNewCfgGroupIndex_Type = Integer32
_SlbNewCfgGroupIndex_Object = MibTableColumn
slbNewCfgGroupIndex = _SlbNewCfgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 1),
    _SlbNewCfgGroupIndex_Type()
)
slbNewCfgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgGroupIndex.setStatus("mandatory")


class _SlbNewCfgGroupRealServers_Type(OctetString):
    """Custom type slbNewCfgGroupRealServers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbNewCfgGroupRealServers_Type.__name__ = "OctetString"
_SlbNewCfgGroupRealServers_Object = MibTableColumn
slbNewCfgGroupRealServers = _SlbNewCfgGroupRealServers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 2),
    _SlbNewCfgGroupRealServers_Type()
)
slbNewCfgGroupRealServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealServers.setStatus("mandatory")
_SlbNewCfgGroupAddServer_Type = Integer32
_SlbNewCfgGroupAddServer_Object = MibTableColumn
slbNewCfgGroupAddServer = _SlbNewCfgGroupAddServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 3),
    _SlbNewCfgGroupAddServer_Type()
)
slbNewCfgGroupAddServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupAddServer.setStatus("mandatory")
_SlbNewCfgGroupRemoveServer_Type = Integer32
_SlbNewCfgGroupRemoveServer_Object = MibTableColumn
slbNewCfgGroupRemoveServer = _SlbNewCfgGroupRemoveServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 4),
    _SlbNewCfgGroupRemoveServer_Type()
)
slbNewCfgGroupRemoveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupRemoveServer.setStatus("mandatory")


class _SlbNewCfgGroupMetric_Type(Integer32):
    """Custom type slbNewCfgGroupMetric based on Integer32"""
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
        *(("hash", 4),
          ("leastConnections", 2),
          ("minMisses", 3),
          ("roundRobin", 1))
    )


_SlbNewCfgGroupMetric_Type.__name__ = "Integer32"
_SlbNewCfgGroupMetric_Object = MibTableColumn
slbNewCfgGroupMetric = _SlbNewCfgGroupMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 5),
    _SlbNewCfgGroupMetric_Type()
)
slbNewCfgGroupMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupMetric.setStatus("mandatory")


class _SlbNewCfgGroupBackupServer_Type(Integer32):
    """Custom type slbNewCfgGroupBackupServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_SlbNewCfgGroupBackupServer_Type.__name__ = "Integer32"
_SlbNewCfgGroupBackupServer_Object = MibTableColumn
slbNewCfgGroupBackupServer = _SlbNewCfgGroupBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 6),
    _SlbNewCfgGroupBackupServer_Type()
)
slbNewCfgGroupBackupServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupBackupServer.setStatus("mandatory")


class _SlbNewCfgGroupDelete_Type(Integer32):
    """Custom type slbNewCfgGroupDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgGroupDelete_Type.__name__ = "Integer32"
_SlbNewCfgGroupDelete_Object = MibTableColumn
slbNewCfgGroupDelete = _SlbNewCfgGroupDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 7),
    _SlbNewCfgGroupDelete_Type()
)
slbNewCfgGroupDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupDelete.setStatus("mandatory")


class _SlbNewCfgGroupHealthCheckUrl_Type(DisplayString):
    """Custom type slbNewCfgGroupHealthCheckUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgGroupHealthCheckUrl_Type.__name__ = "DisplayString"
_SlbNewCfgGroupHealthCheckUrl_Object = MibTableColumn
slbNewCfgGroupHealthCheckUrl = _SlbNewCfgGroupHealthCheckUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 8),
    _SlbNewCfgGroupHealthCheckUrl_Type()
)
slbNewCfgGroupHealthCheckUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupHealthCheckUrl.setStatus("mandatory")


class _SlbNewCfgGroupHealthCheckLayer_Type(Integer32):
    """Custom type slbNewCfgGroupHealthCheckLayer based on Integer32"""
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
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dns", 4),
          ("ftp", 8),
          ("http", 3),
          ("icmp", 1),
          ("imap", 9),
          ("nntp", 7),
          ("pop3", 6),
          ("radius", 10),
          ("script1", 12),
          ("script2", 13),
          ("script3", 14),
          ("script4", 15),
          ("script5", 16),
          ("script6", 17),
          ("script7", 18),
          ("script8", 19),
          ("smtp", 5),
          ("sslh", 11),
          ("tcp", 2))
    )


_SlbNewCfgGroupHealthCheckLayer_Type.__name__ = "Integer32"
_SlbNewCfgGroupHealthCheckLayer_Object = MibTableColumn
slbNewCfgGroupHealthCheckLayer = _SlbNewCfgGroupHealthCheckLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 9),
    _SlbNewCfgGroupHealthCheckLayer_Type()
)
slbNewCfgGroupHealthCheckLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupHealthCheckLayer.setStatus("mandatory")


class _SlbNewCfgGroupName_Type(DisplayString):
    """Custom type slbNewCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SlbNewCfgGroupName_Type.__name__ = "DisplayString"
_SlbNewCfgGroupName_Object = MibTableColumn
slbNewCfgGroupName = _SlbNewCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 10),
    _SlbNewCfgGroupName_Type()
)
slbNewCfgGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupName.setStatus("mandatory")


class _SlbNewCfgGroupRealThreshold_Type(Integer32):
    """Custom type slbNewCfgGroupRealThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbNewCfgGroupRealThreshold_Type.__name__ = "Integer32"
_SlbNewCfgGroupRealThreshold_Object = MibTableColumn
slbNewCfgGroupRealThreshold = _SlbNewCfgGroupRealThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 11),
    _SlbNewCfgGroupRealThreshold_Type()
)
slbNewCfgGroupRealThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealThreshold.setStatus("mandatory")


class _SlbNewCfgGroupBackupGroup_Type(Integer32):
    """Custom type slbNewCfgGroupBackupGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_SlbNewCfgGroupBackupGroup_Type.__name__ = "Integer32"
_SlbNewCfgGroupBackupGroup_Object = MibTableColumn
slbNewCfgGroupBackupGroup = _SlbNewCfgGroupBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 12),
    _SlbNewCfgGroupBackupGroup_Type()
)
slbNewCfgGroupBackupGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupBackupGroup.setStatus("mandatory")
_SlbCurCfgPortTable_Object = MibTable
slbCurCfgPortTable = _SlbCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12)
)
if mibBuilder.loadTexts:
    slbCurCfgPortTable.setStatus("mandatory")
_SlbCurCfgPortEntry_Object = MibTableRow
slbCurCfgPortEntry = _SlbCurCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1)
)
slbCurCfgPortEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgPortEntry.setStatus("mandatory")
_SlbCurCfgPortIndex_Type = Integer32
_SlbCurCfgPortIndex_Object = MibTableColumn
slbCurCfgPortIndex = _SlbCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 1),
    _SlbCurCfgPortIndex_Type()
)
slbCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortIndex.setStatus("mandatory")
_SlbCurCfgPortProxyIpAddr_Type = IpAddress
_SlbCurCfgPortProxyIpAddr_Object = MibTableColumn
slbCurCfgPortProxyIpAddr = _SlbCurCfgPortProxyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 2),
    _SlbCurCfgPortProxyIpAddr_Type()
)
slbCurCfgPortProxyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortProxyIpAddr.setStatus("mandatory")


class _SlbCurCfgPortSlbState_Type(Integer32):
    """Custom type slbCurCfgPortSlbState based on Integer32"""
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
        *(("client", 2),
          ("client-server", 4),
          ("failOver", 5),
          ("failOver-stanby", 6),
          ("none", 1),
          ("server", 3))
    )


_SlbCurCfgPortSlbState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbState_Object = MibTableColumn
slbCurCfgPortSlbState = _SlbCurCfgPortSlbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 3),
    _SlbCurCfgPortSlbState_Type()
)
slbCurCfgPortSlbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbState.setStatus("mandatory")


class _SlbCurCfgPortSlbHotStandby_Type(Integer32):
    """Custom type slbCurCfgPortSlbHotStandby based on Integer32"""
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


_SlbCurCfgPortSlbHotStandby_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbHotStandby_Object = MibTableColumn
slbCurCfgPortSlbHotStandby = _SlbCurCfgPortSlbHotStandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 4),
    _SlbCurCfgPortSlbHotStandby_Type()
)
slbCurCfgPortSlbHotStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbHotStandby.setStatus("mandatory")


class _SlbCurCfgPortSlbInterSwitch_Type(Integer32):
    """Custom type slbCurCfgPortSlbInterSwitch based on Integer32"""
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


_SlbCurCfgPortSlbInterSwitch_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbInterSwitch_Object = MibTableColumn
slbCurCfgPortSlbInterSwitch = _SlbCurCfgPortSlbInterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 5),
    _SlbCurCfgPortSlbInterSwitch_Type()
)
slbCurCfgPortSlbInterSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbInterSwitch.setStatus("mandatory")


class _SlbCurCfgPortSlbPipState_Type(Integer32):
    """Custom type slbCurCfgPortSlbPipState based on Integer32"""
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


_SlbCurCfgPortSlbPipState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbPipState_Object = MibTableColumn
slbCurCfgPortSlbPipState = _SlbCurCfgPortSlbPipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 6),
    _SlbCurCfgPortSlbPipState_Type()
)
slbCurCfgPortSlbPipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbPipState.setStatus("mandatory")
_SlbNewCfgPortTable_Object = MibTable
slbNewCfgPortTable = _SlbNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13)
)
if mibBuilder.loadTexts:
    slbNewCfgPortTable.setStatus("mandatory")
_SlbNewCfgPortEntry_Object = MibTableRow
slbNewCfgPortEntry = _SlbNewCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1)
)
slbNewCfgPortEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgPortEntry.setStatus("mandatory")
_SlbNewCfgPortIndex_Type = Integer32
_SlbNewCfgPortIndex_Object = MibTableColumn
slbNewCfgPortIndex = _SlbNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 1),
    _SlbNewCfgPortIndex_Type()
)
slbNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgPortIndex.setStatus("mandatory")
_SlbNewCfgPortProxyIpAddr_Type = IpAddress
_SlbNewCfgPortProxyIpAddr_Object = MibTableColumn
slbNewCfgPortProxyIpAddr = _SlbNewCfgPortProxyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 2),
    _SlbNewCfgPortProxyIpAddr_Type()
)
slbNewCfgPortProxyIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortProxyIpAddr.setStatus("mandatory")


class _SlbNewCfgPortSlbState_Type(Integer32):
    """Custom type slbNewCfgPortSlbState based on Integer32"""
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
        *(("client", 2),
          ("client-server", 4),
          ("failOver", 5),
          ("failOver-stanby", 6),
          ("none", 1),
          ("server", 3))
    )


_SlbNewCfgPortSlbState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbState_Object = MibTableColumn
slbNewCfgPortSlbState = _SlbNewCfgPortSlbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 3),
    _SlbNewCfgPortSlbState_Type()
)
slbNewCfgPortSlbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbState.setStatus("mandatory")


class _SlbNewCfgPortSlbHotStandby_Type(Integer32):
    """Custom type slbNewCfgPortSlbHotStandby based on Integer32"""
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


_SlbNewCfgPortSlbHotStandby_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbHotStandby_Object = MibTableColumn
slbNewCfgPortSlbHotStandby = _SlbNewCfgPortSlbHotStandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 4),
    _SlbNewCfgPortSlbHotStandby_Type()
)
slbNewCfgPortSlbHotStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbHotStandby.setStatus("mandatory")


class _SlbNewCfgPortSlbInterSwitch_Type(Integer32):
    """Custom type slbNewCfgPortSlbInterSwitch based on Integer32"""
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


_SlbNewCfgPortSlbInterSwitch_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbInterSwitch_Object = MibTableColumn
slbNewCfgPortSlbInterSwitch = _SlbNewCfgPortSlbInterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 5),
    _SlbNewCfgPortSlbInterSwitch_Type()
)
slbNewCfgPortSlbInterSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbInterSwitch.setStatus("mandatory")


class _SlbNewCfgPortSlbPipState_Type(Integer32):
    """Custom type slbNewCfgPortSlbPipState based on Integer32"""
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


_SlbNewCfgPortSlbPipState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbPipState_Object = MibTableColumn
slbNewCfgPortSlbPipState = _SlbNewCfgPortSlbPipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 6),
    _SlbNewCfgPortSlbPipState_Type()
)
slbNewCfgPortSlbPipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbPipState.setStatus("mandatory")
_SlbCurCfgImask_Type = IpAddress
_SlbCurCfgImask_Object = MibScalar
slbCurCfgImask = _SlbCurCfgImask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 14),
    _SlbCurCfgImask_Type()
)
slbCurCfgImask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgImask.setStatus("mandatory")
_SlbNewCfgImask_Type = IpAddress
_SlbNewCfgImask_Object = MibScalar
slbNewCfgImask = _SlbNewCfgImask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 15),
    _SlbNewCfgImask_Type()
)
slbNewCfgImask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgImask.setStatus("mandatory")
_Slbfailover_ObjectIdentity = ObjectIdentity
slbfailover = _Slbfailover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16)
)
_SlbCurCfgFailOverTable_Object = MibTable
slbCurCfgFailOverTable = _SlbCurCfgFailOverTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1)
)
if mibBuilder.loadTexts:
    slbCurCfgFailOverTable.setStatus("mandatory")
_SlbCurCfgFailOverTblEntry_Object = MibTableRow
slbCurCfgFailOverTblEntry = _SlbCurCfgFailOverTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1)
)
slbCurCfgFailOverTblEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgFailOverIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgFailOverTblEntry.setStatus("mandatory")
_SlbCurCfgFailOverIndex_Type = Integer32
_SlbCurCfgFailOverIndex_Object = MibTableColumn
slbCurCfgFailOverIndex = _SlbCurCfgFailOverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 1),
    _SlbCurCfgFailOverIndex_Type()
)
slbCurCfgFailOverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverIndex.setStatus("mandatory")
_SlbCurCfgFailOverPrimaryIp_Type = IpAddress
_SlbCurCfgFailOverPrimaryIp_Object = MibTableColumn
slbCurCfgFailOverPrimaryIp = _SlbCurCfgFailOverPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 2),
    _SlbCurCfgFailOverPrimaryIp_Type()
)
slbCurCfgFailOverPrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverPrimaryIp.setStatus("mandatory")
_SlbCurCfgFailOverSecondaryIp_Type = IpAddress
_SlbCurCfgFailOverSecondaryIp_Object = MibTableColumn
slbCurCfgFailOverSecondaryIp = _SlbCurCfgFailOverSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 3),
    _SlbCurCfgFailOverSecondaryIp_Type()
)
slbCurCfgFailOverSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverSecondaryIp.setStatus("mandatory")


class _SlbCurCfgFailOverSilenceInterval_Type(Integer32):
    """Custom type slbCurCfgFailOverSilenceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_SlbCurCfgFailOverSilenceInterval_Type.__name__ = "Integer32"
_SlbCurCfgFailOverSilenceInterval_Object = MibTableColumn
slbCurCfgFailOverSilenceInterval = _SlbCurCfgFailOverSilenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 4),
    _SlbCurCfgFailOverSilenceInterval_Type()
)
slbCurCfgFailOverSilenceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverSilenceInterval.setStatus("mandatory")


class _SlbCurCfgFailOverState_Type(Integer32):
    """Custom type slbCurCfgFailOverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbCurCfgFailOverState_Type.__name__ = "Integer32"
_SlbCurCfgFailOverState_Object = MibTableColumn
slbCurCfgFailOverState = _SlbCurCfgFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 5),
    _SlbCurCfgFailOverState_Type()
)
slbCurCfgFailOverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverState.setStatus("mandatory")


class _SlbCurCfgFailOverRouteSupply_Type(Integer32):
    """Custom type slbCurCfgFailOverRouteSupply based on Integer32"""
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


_SlbCurCfgFailOverRouteSupply_Type.__name__ = "Integer32"
_SlbCurCfgFailOverRouteSupply_Object = MibTableColumn
slbCurCfgFailOverRouteSupply = _SlbCurCfgFailOverRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 6),
    _SlbCurCfgFailOverRouteSupply_Type()
)
slbCurCfgFailOverRouteSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverRouteSupply.setStatus("mandatory")
_SlbNewCfgFailOverTable_Object = MibTable
slbNewCfgFailOverTable = _SlbNewCfgFailOverTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2)
)
if mibBuilder.loadTexts:
    slbNewCfgFailOverTable.setStatus("mandatory")
_SlbNewCfgFailOverTblEntry_Object = MibTableRow
slbNewCfgFailOverTblEntry = _SlbNewCfgFailOverTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1)
)
slbNewCfgFailOverTblEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgFailOverIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgFailOverTblEntry.setStatus("mandatory")
_SlbNewCfgFailOverIndex_Type = Integer32
_SlbNewCfgFailOverIndex_Object = MibTableColumn
slbNewCfgFailOverIndex = _SlbNewCfgFailOverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 1),
    _SlbNewCfgFailOverIndex_Type()
)
slbNewCfgFailOverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgFailOverIndex.setStatus("mandatory")
_SlbNewCfgFailOverPrimaryIp_Type = IpAddress
_SlbNewCfgFailOverPrimaryIp_Object = MibTableColumn
slbNewCfgFailOverPrimaryIp = _SlbNewCfgFailOverPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 2),
    _SlbNewCfgFailOverPrimaryIp_Type()
)
slbNewCfgFailOverPrimaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverPrimaryIp.setStatus("mandatory")
_SlbNewCfgFailOverSecondaryIp_Type = IpAddress
_SlbNewCfgFailOverSecondaryIp_Object = MibTableColumn
slbNewCfgFailOverSecondaryIp = _SlbNewCfgFailOverSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 3),
    _SlbNewCfgFailOverSecondaryIp_Type()
)
slbNewCfgFailOverSecondaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverSecondaryIp.setStatus("mandatory")


class _SlbNewCfgFailOverSilenceInterval_Type(Integer32):
    """Custom type slbNewCfgFailOverSilenceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_SlbNewCfgFailOverSilenceInterval_Type.__name__ = "Integer32"
_SlbNewCfgFailOverSilenceInterval_Object = MibTableColumn
slbNewCfgFailOverSilenceInterval = _SlbNewCfgFailOverSilenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 4),
    _SlbNewCfgFailOverSilenceInterval_Type()
)
slbNewCfgFailOverSilenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverSilenceInterval.setStatus("mandatory")


class _SlbNewCfgFailOverState_Type(Integer32):
    """Custom type slbNewCfgFailOverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbNewCfgFailOverState_Type.__name__ = "Integer32"
_SlbNewCfgFailOverState_Object = MibTableColumn
slbNewCfgFailOverState = _SlbNewCfgFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 5),
    _SlbNewCfgFailOverState_Type()
)
slbNewCfgFailOverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverState.setStatus("mandatory")


class _SlbNewCfgFailOverRouteSupply_Type(Integer32):
    """Custom type slbNewCfgFailOverRouteSupply based on Integer32"""
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


_SlbNewCfgFailOverRouteSupply_Type.__name__ = "Integer32"
_SlbNewCfgFailOverRouteSupply_Object = MibTableColumn
slbNewCfgFailOverRouteSupply = _SlbNewCfgFailOverRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 6),
    _SlbNewCfgFailOverRouteSupply_Type()
)
slbNewCfgFailOverRouteSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgFailOverRouteSupply.setStatus("mandatory")


class _SlbCurCfgGlobalControl_Type(Integer32):
    """Custom type slbCurCfgGlobalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbCurCfgGlobalControl_Type.__name__ = "Integer32"
_SlbCurCfgGlobalControl_Object = MibScalar
slbCurCfgGlobalControl = _SlbCurCfgGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 17),
    _SlbCurCfgGlobalControl_Type()
)
slbCurCfgGlobalControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGlobalControl.setStatus("mandatory")


class _SlbNewCfgGlobalControl_Type(Integer32):
    """Custom type slbNewCfgGlobalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SlbNewCfgGlobalControl_Type.__name__ = "Integer32"
_SlbNewCfgGlobalControl_Object = MibScalar
slbNewCfgGlobalControl = _SlbNewCfgGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 18),
    _SlbNewCfgGlobalControl_Type()
)
slbNewCfgGlobalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGlobalControl.setStatus("mandatory")
_SlbCurCfgMnet_Type = IpAddress
_SlbCurCfgMnet_Object = MibScalar
slbCurCfgMnet = _SlbCurCfgMnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 19),
    _SlbCurCfgMnet_Type()
)
slbCurCfgMnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMnet.setStatus("mandatory")
_SlbNewCfgMnet_Type = IpAddress
_SlbNewCfgMnet_Object = MibScalar
slbNewCfgMnet = _SlbNewCfgMnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 20),
    _SlbNewCfgMnet_Type()
)
slbNewCfgMnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMnet.setStatus("mandatory")
_SlbCurCfgMmask_Type = IpAddress
_SlbCurCfgMmask_Object = MibScalar
slbCurCfgMmask = _SlbCurCfgMmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 21),
    _SlbCurCfgMmask_Type()
)
slbCurCfgMmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMmask.setStatus("mandatory")
_SlbNewCfgMmask_Type = IpAddress
_SlbNewCfgMmask_Object = MibScalar
slbNewCfgMmask = _SlbNewCfgMmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 22),
    _SlbNewCfgMmask_Type()
)
slbNewCfgMmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMmask.setStatus("mandatory")


class _SlbCurCfgRadiusAuthenString_Type(DisplayString):
    """Custom type slbCurCfgRadiusAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgRadiusAuthenString_Type.__name__ = "DisplayString"
_SlbCurCfgRadiusAuthenString_Object = MibScalar
slbCurCfgRadiusAuthenString = _SlbCurCfgRadiusAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 23),
    _SlbCurCfgRadiusAuthenString_Type()
)
slbCurCfgRadiusAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRadiusAuthenString.setStatus("mandatory")


class _SlbNewCfgRadiusAuthenString_Type(DisplayString):
    """Custom type slbNewCfgRadiusAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgRadiusAuthenString_Type.__name__ = "DisplayString"
_SlbNewCfgRadiusAuthenString_Object = MibScalar
slbNewCfgRadiusAuthenString = _SlbNewCfgRadiusAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 24),
    _SlbNewCfgRadiusAuthenString_Type()
)
slbNewCfgRadiusAuthenString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRadiusAuthenString.setStatus("mandatory")


class _SlbCurCfgDirectMode_Type(Integer32):
    """Custom type slbCurCfgDirectMode based on Integer32"""
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


_SlbCurCfgDirectMode_Type.__name__ = "Integer32"
_SlbCurCfgDirectMode_Object = MibScalar
slbCurCfgDirectMode = _SlbCurCfgDirectMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 25),
    _SlbCurCfgDirectMode_Type()
)
slbCurCfgDirectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDirectMode.setStatus("mandatory")


class _SlbNewCfgDirectMode_Type(Integer32):
    """Custom type slbNewCfgDirectMode based on Integer32"""
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


_SlbNewCfgDirectMode_Type.__name__ = "Integer32"
_SlbNewCfgDirectMode_Object = MibScalar
slbNewCfgDirectMode = _SlbNewCfgDirectMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 26),
    _SlbNewCfgDirectMode_Type()
)
slbNewCfgDirectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgDirectMode.setStatus("mandatory")
_SlbUrl_ObjectIdentity = ObjectIdentity
slbUrl = _SlbUrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27)
)
_SlbUrlRedir_ObjectIdentity = ObjectIdentity
slbUrlRedir = _SlbUrlRedir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1)
)
_SlbCurCfgUrlExpTable_Object = MibTable
slbCurCfgUrlExpTable = _SlbCurCfgUrlExpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlExpTable.setStatus("mandatory")
_SlbCurCfgUrlExpTableEntry_Object = MibTableRow
slbCurCfgUrlExpTableEntry = _SlbCurCfgUrlExpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1, 1)
)
slbCurCfgUrlExpTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgUrlExpIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlExpTableEntry.setStatus("mandatory")
_SlbCurCfgUrlExpIndex_Type = Integer32
_SlbCurCfgUrlExpIndex_Object = MibTableColumn
slbCurCfgUrlExpIndex = _SlbCurCfgUrlExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1, 1, 1),
    _SlbCurCfgUrlExpIndex_Type()
)
slbCurCfgUrlExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlExpIndex.setStatus("mandatory")


class _SlbCurCfgUrlExpression_Type(DisplayString):
    """Custom type slbCurCfgUrlExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SlbCurCfgUrlExpression_Type.__name__ = "DisplayString"
_SlbCurCfgUrlExpression_Object = MibTableColumn
slbCurCfgUrlExpression = _SlbCurCfgUrlExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1, 1, 2),
    _SlbCurCfgUrlExpression_Type()
)
slbCurCfgUrlExpression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlExpression.setStatus("mandatory")
_SlbNewCfgUrlExpTable_Object = MibTable
slbNewCfgUrlExpTable = _SlbNewCfgUrlExpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlExpTable.setStatus("mandatory")
_SlbNewCfgUrlExpTableEntry_Object = MibTableRow
slbNewCfgUrlExpTableEntry = _SlbNewCfgUrlExpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1)
)
slbNewCfgUrlExpTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgUrlExpIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlExpTableEntry.setStatus("mandatory")
_SlbNewCfgUrlExpIndex_Type = Integer32
_SlbNewCfgUrlExpIndex_Object = MibTableColumn
slbNewCfgUrlExpIndex = _SlbNewCfgUrlExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1, 1),
    _SlbNewCfgUrlExpIndex_Type()
)
slbNewCfgUrlExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlExpIndex.setStatus("mandatory")


class _SlbNewCfgUrlExpression_Type(DisplayString):
    """Custom type slbNewCfgUrlExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SlbNewCfgUrlExpression_Type.__name__ = "DisplayString"
_SlbNewCfgUrlExpression_Object = MibTableColumn
slbNewCfgUrlExpression = _SlbNewCfgUrlExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1, 2),
    _SlbNewCfgUrlExpression_Type()
)
slbNewCfgUrlExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlExpression.setStatus("mandatory")


class _SlbNewCfgUrlExpDelete_Type(Integer32):
    """Custom type slbNewCfgUrlExpDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgUrlExpDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlExpDelete_Object = MibTableColumn
slbNewCfgUrlExpDelete = _SlbNewCfgUrlExpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1, 3),
    _SlbNewCfgUrlExpDelete_Type()
)
slbNewCfgUrlExpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlExpDelete.setStatus("mandatory")


class _SlbCurCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNonGetOrigSrv based on Integer32"""
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


_SlbCurCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNonGetOrigSrv = _SlbCurCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 3),
    _SlbCurCfgUrlRedirNonGetOrigSrv_Type()
)
slbCurCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNonGetOrigSrv.setStatus("mandatory")


class _SlbNewCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNonGetOrigSrv based on Integer32"""
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


_SlbNewCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNonGetOrigSrv = _SlbNewCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 4),
    _SlbNewCfgUrlRedirNonGetOrigSrv_Type()
)
slbNewCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNonGetOrigSrv.setStatus("mandatory")


class _SlbCurCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirCookieOrigSrv based on Integer32"""
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


_SlbCurCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbCurCfgUrlRedirCookieOrigSrv = _SlbCurCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 5),
    _SlbCurCfgUrlRedirCookieOrigSrv_Type()
)
slbCurCfgUrlRedirCookieOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirCookieOrigSrv.setStatus("mandatory")


class _SlbNewCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirCookieOrigSrv based on Integer32"""
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


_SlbNewCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbNewCfgUrlRedirCookieOrigSrv = _SlbNewCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 6),
    _SlbNewCfgUrlRedirCookieOrigSrv_Type()
)
slbNewCfgUrlRedirCookieOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirCookieOrigSrv.setStatus("mandatory")


class _SlbCurCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNoCacheOrigSrv based on Integer32"""
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


_SlbCurCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNoCacheOrigSrv = _SlbCurCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 7),
    _SlbCurCfgUrlRedirNoCacheOrigSrv_Type()
)
slbCurCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNoCacheOrigSrv.setStatus("mandatory")


class _SlbNewCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNoCacheOrigSrv based on Integer32"""
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


_SlbNewCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNoCacheOrigSrv = _SlbNewCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 8),
    _SlbNewCfgUrlRedirNoCacheOrigSrv_Type()
)
slbNewCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNoCacheOrigSrv.setStatus("mandatory")
_SlbCurCfgUrlRedirUriHashLength_Type = Integer32
_SlbCurCfgUrlRedirUriHashLength_Object = MibScalar
slbCurCfgUrlRedirUriHashLength = _SlbCurCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 9),
    _SlbCurCfgUrlRedirUriHashLength_Type()
)
slbCurCfgUrlRedirUriHashLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirUriHashLength.setStatus("mandatory")
_SlbNewCfgUrlRedirUriHashLength_Type = Integer32
_SlbNewCfgUrlRedirUriHashLength_Object = MibScalar
slbNewCfgUrlRedirUriHashLength = _SlbNewCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 10),
    _SlbNewCfgUrlRedirUriHashLength_Type()
)
slbNewCfgUrlRedirUriHashLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirUriHashLength.setStatus("mandatory")


class _SlbCurCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbCurCfgUrlRedirHeader based on Integer32"""
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


_SlbCurCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirHeader_Object = MibScalar
slbCurCfgUrlRedirHeader = _SlbCurCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 11),
    _SlbCurCfgUrlRedirHeader_Type()
)
slbCurCfgUrlRedirHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeader.setStatus("mandatory")


class _SlbNewCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbNewCfgUrlRedirHeader based on Integer32"""
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


_SlbNewCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirHeader_Object = MibScalar
slbNewCfgUrlRedirHeader = _SlbNewCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 12),
    _SlbNewCfgUrlRedirHeader_Type()
)
slbNewCfgUrlRedirHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeader.setStatus("mandatory")
_SlbCurCfgUrlRedirHeaderName_Type = DisplayString
_SlbCurCfgUrlRedirHeaderName_Object = MibScalar
slbCurCfgUrlRedirHeaderName = _SlbCurCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 13),
    _SlbCurCfgUrlRedirHeaderName_Type()
)
slbCurCfgUrlRedirHeaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeaderName.setStatus("mandatory")
_SlbNewCfgUrlRedirHeaderName_Type = DisplayString
_SlbNewCfgUrlRedirHeaderName_Object = MibScalar
slbNewCfgUrlRedirHeaderName = _SlbNewCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 14),
    _SlbNewCfgUrlRedirHeaderName_Type()
)
slbNewCfgUrlRedirHeaderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeaderName.setStatus("mandatory")
_SlbUrlBalance_ObjectIdentity = ObjectIdentity
slbUrlBalance = _SlbUrlBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2)
)
_SlbCurCfgUrlLbPathTable_Object = MibTable
slbCurCfgUrlLbPathTable = _SlbCurCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTable.setStatus("mandatory")
_SlbCurCfgUrlLbPathTableEntry_Object = MibTableRow
slbCurCfgUrlLbPathTableEntry = _SlbCurCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1, 1)
)
slbCurCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTableEntry.setStatus("mandatory")
_SlbCurCfgUrlLbPathIndex_Type = Integer32
_SlbCurCfgUrlLbPathIndex_Object = MibTableColumn
slbCurCfgUrlLbPathIndex = _SlbCurCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1, 1, 1),
    _SlbCurCfgUrlLbPathIndex_Type()
)
slbCurCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathIndex.setStatus("mandatory")


class _SlbCurCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlbCurCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathString_Object = MibTableColumn
slbCurCfgUrlLbPathString = _SlbCurCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1, 1, 2),
    _SlbCurCfgUrlLbPathString_Type()
)
slbCurCfgUrlLbPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathString.setStatus("mandatory")
_SlbNewCfgUrlLbPathTable_Object = MibTable
slbNewCfgUrlLbPathTable = _SlbNewCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTable.setStatus("mandatory")
_SlbNewCfgUrlLbPathTableEntry_Object = MibTableRow
slbNewCfgUrlLbPathTableEntry = _SlbNewCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1)
)
slbNewCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTableEntry.setStatus("mandatory")
_SlbNewCfgUrlLbPathIndex_Type = Integer32
_SlbNewCfgUrlLbPathIndex_Object = MibTableColumn
slbNewCfgUrlLbPathIndex = _SlbNewCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1, 1),
    _SlbNewCfgUrlLbPathIndex_Type()
)
slbNewCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathIndex.setStatus("mandatory")


class _SlbNewCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlbNewCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathString_Object = MibTableColumn
slbNewCfgUrlLbPathString = _SlbNewCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1, 2),
    _SlbNewCfgUrlLbPathString_Type()
)
slbNewCfgUrlLbPathString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathString.setStatus("mandatory")


class _SlbNewCfgUrlLbPathDelete_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgUrlLbPathDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathDelete_Object = MibTableColumn
slbNewCfgUrlLbPathDelete = _SlbNewCfgUrlLbPathDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1, 3),
    _SlbNewCfgUrlLbPathDelete_Type()
)
slbNewCfgUrlLbPathDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDelete.setStatus("mandatory")
_SlbCurCfgUrlLbErrorMsg_Type = DisplayString
_SlbCurCfgUrlLbErrorMsg_Object = MibScalar
slbCurCfgUrlLbErrorMsg = _SlbCurCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 3),
    _SlbCurCfgUrlLbErrorMsg_Type()
)
slbCurCfgUrlLbErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbErrorMsg.setStatus("mandatory")
_SlbNewCfgUrlLbErrorMsg_Type = DisplayString
_SlbNewCfgUrlLbErrorMsg_Object = MibScalar
slbNewCfgUrlLbErrorMsg = _SlbNewCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 4),
    _SlbNewCfgUrlLbErrorMsg_Type()
)
slbNewCfgUrlLbErrorMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbErrorMsg.setStatus("mandatory")
_SlbCurCfgPmask_Type = IpAddress
_SlbCurCfgPmask_Object = MibScalar
slbCurCfgPmask = _SlbCurCfgPmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 28),
    _SlbCurCfgPmask_Type()
)
slbCurCfgPmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPmask.setStatus("mandatory")
_SlbNewCfgPmask_Type = IpAddress
_SlbNewCfgPmask_Object = MibScalar
slbNewCfgPmask = _SlbNewCfgPmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 29),
    _SlbNewCfgPmask_Type()
)
slbNewCfgPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPmask.setStatus("mandatory")


class _SlbCurCfgGrace_Type(Integer32):
    """Custom type slbCurCfgGrace based on Integer32"""
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


_SlbCurCfgGrace_Type.__name__ = "Integer32"
_SlbCurCfgGrace_Object = MibScalar
slbCurCfgGrace = _SlbCurCfgGrace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 30),
    _SlbCurCfgGrace_Type()
)
slbCurCfgGrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGrace.setStatus("mandatory")


class _SlbNewCfgGrace_Type(Integer32):
    """Custom type slbNewCfgGrace based on Integer32"""
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


_SlbNewCfgGrace_Type.__name__ = "Integer32"
_SlbNewCfgGrace_Object = MibScalar
slbNewCfgGrace = _SlbNewCfgGrace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 31),
    _SlbNewCfgGrace_Type()
)
slbNewCfgGrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGrace.setStatus("mandatory")
_SlbCurCfgPeerTable_Object = MibTable
slbCurCfgPeerTable = _SlbCurCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32)
)
if mibBuilder.loadTexts:
    slbCurCfgPeerTable.setStatus("mandatory")
_SlbCurCfgPeerEntry_Object = MibTableRow
slbCurCfgPeerEntry = _SlbCurCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1)
)
slbCurCfgPeerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgPeerEntry.setStatus("mandatory")
_SlbCurCfgPeerIndex_Type = Integer32
_SlbCurCfgPeerIndex_Object = MibTableColumn
slbCurCfgPeerIndex = _SlbCurCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1, 1),
    _SlbCurCfgPeerIndex_Type()
)
slbCurCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerIndex.setStatus("mandatory")
_SlbCurCfgPeerIpAddr_Type = IpAddress
_SlbCurCfgPeerIpAddr_Object = MibTableColumn
slbCurCfgPeerIpAddr = _SlbCurCfgPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1, 2),
    _SlbCurCfgPeerIpAddr_Type()
)
slbCurCfgPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerIpAddr.setStatus("mandatory")


class _SlbCurCfgPeerState_Type(Integer32):
    """Custom type slbCurCfgPeerState based on Integer32"""
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


_SlbCurCfgPeerState_Type.__name__ = "Integer32"
_SlbCurCfgPeerState_Object = MibTableColumn
slbCurCfgPeerState = _SlbCurCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1, 3),
    _SlbCurCfgPeerState_Type()
)
slbCurCfgPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerState.setStatus("mandatory")
_SlbNewCfgPeerTable_Object = MibTable
slbNewCfgPeerTable = _SlbNewCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33)
)
if mibBuilder.loadTexts:
    slbNewCfgPeerTable.setStatus("mandatory")
_SlbNewCfgPeerEntry_Object = MibTableRow
slbNewCfgPeerEntry = _SlbNewCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1)
)
slbNewCfgPeerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbNewCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgPeerEntry.setStatus("mandatory")
_SlbNewCfgPeerIndex_Type = Integer32
_SlbNewCfgPeerIndex_Object = MibTableColumn
slbNewCfgPeerIndex = _SlbNewCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 1),
    _SlbNewCfgPeerIndex_Type()
)
slbNewCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgPeerIndex.setStatus("mandatory")
_SlbNewCfgPeerIpAddr_Type = IpAddress
_SlbNewCfgPeerIpAddr_Object = MibTableColumn
slbNewCfgPeerIpAddr = _SlbNewCfgPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 2),
    _SlbNewCfgPeerIpAddr_Type()
)
slbNewCfgPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPeerIpAddr.setStatus("mandatory")


class _SlbNewCfgPeerState_Type(Integer32):
    """Custom type slbNewCfgPeerState based on Integer32"""
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


_SlbNewCfgPeerState_Type.__name__ = "Integer32"
_SlbNewCfgPeerState_Object = MibTableColumn
slbNewCfgPeerState = _SlbNewCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 3),
    _SlbNewCfgPeerState_Type()
)
slbNewCfgPeerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPeerState.setStatus("mandatory")


class _SlbNewCfgPeerDelete_Type(Integer32):
    """Custom type slbNewCfgPeerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgPeerDelete_Type.__name__ = "Integer32"
_SlbNewCfgPeerDelete_Object = MibTableColumn
slbNewCfgPeerDelete = _SlbNewCfgPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 4),
    _SlbNewCfgPeerDelete_Type()
)
slbNewCfgPeerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPeerDelete.setStatus("mandatory")


class _SlbCurCfgSyncFilt_Type(Integer32):
    """Custom type slbCurCfgSyncFilt based on Integer32"""
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


_SlbCurCfgSyncFilt_Type.__name__ = "Integer32"
_SlbCurCfgSyncFilt_Object = MibScalar
slbCurCfgSyncFilt = _SlbCurCfgSyncFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 34),
    _SlbCurCfgSyncFilt_Type()
)
slbCurCfgSyncFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncFilt.setStatus("mandatory")


class _SlbNewCfgSyncFilt_Type(Integer32):
    """Custom type slbNewCfgSyncFilt based on Integer32"""
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


_SlbNewCfgSyncFilt_Type.__name__ = "Integer32"
_SlbNewCfgSyncFilt_Object = MibScalar
slbNewCfgSyncFilt = _SlbNewCfgSyncFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 35),
    _SlbNewCfgSyncFilt_Type()
)
slbNewCfgSyncFilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncFilt.setStatus("mandatory")


class _SlbCurCfgSyncPort_Type(Integer32):
    """Custom type slbCurCfgSyncPort based on Integer32"""
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


_SlbCurCfgSyncPort_Type.__name__ = "Integer32"
_SlbCurCfgSyncPort_Object = MibScalar
slbCurCfgSyncPort = _SlbCurCfgSyncPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 36),
    _SlbCurCfgSyncPort_Type()
)
slbCurCfgSyncPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncPort.setStatus("mandatory")


class _SlbNewCfgSyncPort_Type(Integer32):
    """Custom type slbNewCfgSyncPort based on Integer32"""
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


_SlbNewCfgSyncPort_Type.__name__ = "Integer32"
_SlbNewCfgSyncPort_Object = MibScalar
slbNewCfgSyncPort = _SlbNewCfgSyncPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 37),
    _SlbNewCfgSyncPort_Type()
)
slbNewCfgSyncPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncPort.setStatus("mandatory")


class _SlbCurCfgSyncVrrp_Type(Integer32):
    """Custom type slbCurCfgSyncVrrp based on Integer32"""
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


_SlbCurCfgSyncVrrp_Type.__name__ = "Integer32"
_SlbCurCfgSyncVrrp_Object = MibScalar
slbCurCfgSyncVrrp = _SlbCurCfgSyncVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 38),
    _SlbCurCfgSyncVrrp_Type()
)
slbCurCfgSyncVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncVrrp.setStatus("mandatory")


class _SlbNewCfgSyncVrrp_Type(Integer32):
    """Custom type slbNewCfgSyncVrrp based on Integer32"""
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


_SlbNewCfgSyncVrrp_Type.__name__ = "Integer32"
_SlbNewCfgSyncVrrp_Object = MibScalar
slbNewCfgSyncVrrp = _SlbNewCfgSyncVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 39),
    _SlbNewCfgSyncVrrp_Type()
)
slbNewCfgSyncVrrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncVrrp.setStatus("mandatory")


class _SlbCurCfgSyncPip_Type(Integer32):
    """Custom type slbCurCfgSyncPip based on Integer32"""
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


_SlbCurCfgSyncPip_Type.__name__ = "Integer32"
_SlbCurCfgSyncPip_Object = MibScalar
slbCurCfgSyncPip = _SlbCurCfgSyncPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 40),
    _SlbCurCfgSyncPip_Type()
)
slbCurCfgSyncPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncPip.setStatus("mandatory")


class _SlbNewCfgSyncPip_Type(Integer32):
    """Custom type slbNewCfgSyncPip based on Integer32"""
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


_SlbNewCfgSyncPip_Type.__name__ = "Integer32"
_SlbNewCfgSyncPip_Object = MibScalar
slbNewCfgSyncPip = _SlbNewCfgSyncPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 41),
    _SlbNewCfgSyncPip_Type()
)
slbNewCfgSyncPip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncPip.setStatus("mandatory")


class _SlbCurCfgVirtMatrixArch_Type(Integer32):
    """Custom type slbCurCfgVirtMatrixArch based on Integer32"""
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


_SlbCurCfgVirtMatrixArch_Type.__name__ = "Integer32"
_SlbCurCfgVirtMatrixArch_Object = MibScalar
slbCurCfgVirtMatrixArch = _SlbCurCfgVirtMatrixArch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 42),
    _SlbCurCfgVirtMatrixArch_Type()
)
slbCurCfgVirtMatrixArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtMatrixArch.setStatus("mandatory")


class _SlbNewCfgVirtMatrixArch_Type(Integer32):
    """Custom type slbNewCfgVirtMatrixArch based on Integer32"""
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


_SlbNewCfgVirtMatrixArch_Type.__name__ = "Integer32"
_SlbNewCfgVirtMatrixArch_Object = MibScalar
slbNewCfgVirtMatrixArch = _SlbNewCfgVirtMatrixArch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 43),
    _SlbNewCfgVirtMatrixArch_Type()
)
slbNewCfgVirtMatrixArch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtMatrixArch.setStatus("mandatory")
_Portmirroring_ObjectIdentity = ObjectIdentity
portmirroring = _Portmirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6)
)
_PmCurCfgMonitoringPort_Type = Integer32
_PmCurCfgMonitoringPort_Object = MibScalar
pmCurCfgMonitoringPort = _PmCurCfgMonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 1),
    _PmCurCfgMonitoringPort_Type()
)
pmCurCfgMonitoringPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgMonitoringPort.setStatus("mandatory")
_PmNewCfgMonitoringPort_Type = Integer32
_PmNewCfgMonitoringPort_Object = MibScalar
pmNewCfgMonitoringPort = _PmNewCfgMonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 2),
    _PmNewCfgMonitoringPort_Type()
)
pmNewCfgMonitoringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgMonitoringPort.setStatus("mandatory")
_PmCurCfgMirroredPort_Type = Integer32
_PmCurCfgMirroredPort_Object = MibScalar
pmCurCfgMirroredPort = _PmCurCfgMirroredPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 3),
    _PmCurCfgMirroredPort_Type()
)
pmCurCfgMirroredPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgMirroredPort.setStatus("mandatory")
_PmNewCfgMirroredPort_Type = Integer32
_PmNewCfgMirroredPort_Object = MibScalar
pmNewCfgMirroredPort = _PmNewCfgMirroredPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 4),
    _PmNewCfgMirroredPort_Type()
)
pmNewCfgMirroredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgMirroredPort.setStatus("mandatory")


class _PmCurCfgMonitoredTraffic_Type(Integer32):
    """Custom type pmCurCfgMonitoredTraffic based on Integer32"""
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
        *(("both", 5),
          ("none", 2),
          ("other", 1),
          ("received", 3),
          ("transmitted", 4))
    )


_PmCurCfgMonitoredTraffic_Type.__name__ = "Integer32"
_PmCurCfgMonitoredTraffic_Object = MibScalar
pmCurCfgMonitoredTraffic = _PmCurCfgMonitoredTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 5),
    _PmCurCfgMonitoredTraffic_Type()
)
pmCurCfgMonitoredTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgMonitoredTraffic.setStatus("mandatory")


class _PmNewCfgMonitoredTraffic_Type(Integer32):
    """Custom type pmNewCfgMonitoredTraffic based on Integer32"""
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
        *(("both", 5),
          ("none", 2),
          ("other", 1),
          ("received", 3),
          ("transmitted", 4))
    )


_PmNewCfgMonitoredTraffic_Type.__name__ = "Integer32"
_PmNewCfgMonitoredTraffic_Object = MibScalar
pmNewCfgMonitoredTraffic = _PmNewCfgMonitoredTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 6),
    _PmNewCfgMonitoredTraffic_Type()
)
pmNewCfgMonitoredTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgMonitoredTraffic.setStatus("mandatory")


class _PmCurCfgState_Type(Integer32):
    """Custom type pmCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_PmCurCfgState_Type.__name__ = "Integer32"
_PmCurCfgState_Object = MibScalar
pmCurCfgState = _PmCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 7),
    _PmCurCfgState_Type()
)
pmCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgState.setStatus("mandatory")


class _PmNewCfgState_Type(Integer32):
    """Custom type pmNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_PmNewCfgState_Type.__name__ = "Integer32"
_PmNewCfgState_Object = MibScalar
pmNewCfgState = _PmNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 8),
    _PmNewCfgState_Type()
)
pmNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgState.setStatus("mandatory")
_Trunkgroup_ObjectIdentity = ObjectIdentity
trunkgroup = _Trunkgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7)
)
_TrunkGroupTableMaxSize_Type = Integer32
_TrunkGroupTableMaxSize_Object = MibScalar
trunkGroupTableMaxSize = _TrunkGroupTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 1),
    _TrunkGroupTableMaxSize_Type()
)
trunkGroupTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupTableMaxSize.setStatus("mandatory")
_TrunkGroupCurCfgTable_Object = MibTable
trunkGroupCurCfgTable = _TrunkGroupCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    trunkGroupCurCfgTable.setStatus("mandatory")
_TrunkGroupCurCfgTableEntry_Object = MibTableRow
trunkGroupCurCfgTableEntry = _TrunkGroupCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 2, 1)
)
trunkGroupCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "trunkGroupCurCfgIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupCurCfgTableEntry.setStatus("mandatory")
_TrunkGroupCurCfgIndex_Type = Integer32
_TrunkGroupCurCfgIndex_Object = MibTableColumn
trunkGroupCurCfgIndex = _TrunkGroupCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 2, 1, 1),
    _TrunkGroupCurCfgIndex_Type()
)
trunkGroupCurCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgIndex.setStatus("mandatory")


class _TrunkGroupCurCfgPorts_Type(OctetString):
    """Custom type trunkGroupCurCfgPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TrunkGroupCurCfgPorts_Type.__name__ = "OctetString"
_TrunkGroupCurCfgPorts_Object = MibTableColumn
trunkGroupCurCfgPorts = _TrunkGroupCurCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 2, 1, 2),
    _TrunkGroupCurCfgPorts_Type()
)
trunkGroupCurCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgPorts.setStatus("mandatory")


class _TrunkGroupCurCfgState_Type(Integer32):
    """Custom type trunkGroupCurCfgState based on Integer32"""
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


_TrunkGroupCurCfgState_Type.__name__ = "Integer32"
_TrunkGroupCurCfgState_Object = MibTableColumn
trunkGroupCurCfgState = _TrunkGroupCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 2, 1, 3),
    _TrunkGroupCurCfgState_Type()
)
trunkGroupCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgState.setStatus("mandatory")
_TrunkGroupCurCfgBwmContract_Type = Integer32
_TrunkGroupCurCfgBwmContract_Object = MibTableColumn
trunkGroupCurCfgBwmContract = _TrunkGroupCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 2, 1, 4),
    _TrunkGroupCurCfgBwmContract_Type()
)
trunkGroupCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgBwmContract.setStatus("mandatory")
_TrunkGroupNewCfgTable_Object = MibTable
trunkGroupNewCfgTable = _TrunkGroupNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    trunkGroupNewCfgTable.setStatus("mandatory")
_TrunkGroupNewCfgTableEntry_Object = MibTableRow
trunkGroupNewCfgTableEntry = _TrunkGroupNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1)
)
trunkGroupNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "trunkGroupNewCfgIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupNewCfgTableEntry.setStatus("mandatory")
_TrunkGroupNewCfgIndex_Type = Integer32
_TrunkGroupNewCfgIndex_Object = MibTableColumn
trunkGroupNewCfgIndex = _TrunkGroupNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1, 1),
    _TrunkGroupNewCfgIndex_Type()
)
trunkGroupNewCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupNewCfgIndex.setStatus("mandatory")


class _TrunkGroupNewCfgPorts_Type(OctetString):
    """Custom type trunkGroupNewCfgPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TrunkGroupNewCfgPorts_Type.__name__ = "OctetString"
_TrunkGroupNewCfgPorts_Object = MibTableColumn
trunkGroupNewCfgPorts = _TrunkGroupNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1, 2),
    _TrunkGroupNewCfgPorts_Type()
)
trunkGroupNewCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupNewCfgPorts.setStatus("mandatory")
_TrunkGroupNewCfgAddPort_Type = Integer32
_TrunkGroupNewCfgAddPort_Object = MibTableColumn
trunkGroupNewCfgAddPort = _TrunkGroupNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1, 3),
    _TrunkGroupNewCfgAddPort_Type()
)
trunkGroupNewCfgAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGroupNewCfgAddPort.setStatus("mandatory")
_TrunkGroupNewCfgRemovePort_Type = Integer32
_TrunkGroupNewCfgRemovePort_Object = MibTableColumn
trunkGroupNewCfgRemovePort = _TrunkGroupNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1, 4),
    _TrunkGroupNewCfgRemovePort_Type()
)
trunkGroupNewCfgRemovePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGroupNewCfgRemovePort.setStatus("mandatory")


class _TrunkGroupNewCfgState_Type(Integer32):
    """Custom type trunkGroupNewCfgState based on Integer32"""
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


_TrunkGroupNewCfgState_Type.__name__ = "Integer32"
_TrunkGroupNewCfgState_Object = MibTableColumn
trunkGroupNewCfgState = _TrunkGroupNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1, 5),
    _TrunkGroupNewCfgState_Type()
)
trunkGroupNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGroupNewCfgState.setStatus("mandatory")


class _TrunkGroupNewCfgDelete_Type(Integer32):
    """Custom type trunkGroupNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_TrunkGroupNewCfgDelete_Type.__name__ = "Integer32"
_TrunkGroupNewCfgDelete_Object = MibTableColumn
trunkGroupNewCfgDelete = _TrunkGroupNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1, 6),
    _TrunkGroupNewCfgDelete_Type()
)
trunkGroupNewCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGroupNewCfgDelete.setStatus("mandatory")
_TrunkGroupNewCfgBwmContract_Type = Integer32
_TrunkGroupNewCfgBwmContract_Object = MibTableColumn
trunkGroupNewCfgBwmContract = _TrunkGroupNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 7, 3, 1, 7),
    _TrunkGroupNewCfgBwmContract_Type()
)
trunkGroupNewCfgBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGroupNewCfgBwmContract.setStatus("mandatory")
_Stats_ObjectIdentity = ObjectIdentity
stats = _Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8)
)
_RipStats_ObjectIdentity = ObjectIdentity
ripStats = _RipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1)
)
_RipStatInPkts_Type = Counter32
_RipStatInPkts_Object = MibScalar
ripStatInPkts = _RipStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1, 1),
    _RipStatInPkts_Type()
)
ripStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInPkts.setStatus("mandatory")
_RipStatOutPkts_Type = Counter32
_RipStatOutPkts_Object = MibScalar
ripStatOutPkts = _RipStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1, 2),
    _RipStatOutPkts_Type()
)
ripStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutPkts.setStatus("mandatory")
_RipStatInErrorPkts_Type = Counter32
_RipStatInErrorPkts_Object = MibScalar
ripStatInErrorPkts = _RipStatInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1, 3),
    _RipStatInErrorPkts_Type()
)
ripStatInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInErrorPkts.setStatus("mandatory")
_SlbStats_ObjectIdentity = ObjectIdentity
slbStats = _SlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2)
)
_SlbStatPortMaintTable_Object = MibTable
slbStatPortMaintTable = _SlbStatPortMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    slbStatPortMaintTable.setStatus("mandatory")
_SlbStatPortMaintEntry_Object = MibTableRow
slbStatPortMaintEntry = _SlbStatPortMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1)
)
slbStatPortMaintEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbStatPortMaintPortIndex"),
)
if mibBuilder.loadTexts:
    slbStatPortMaintEntry.setStatus("mandatory")
_SlbStatPortMaintPortIndex_Type = Integer32
_SlbStatPortMaintPortIndex_Object = MibTableColumn
slbStatPortMaintPortIndex = _SlbStatPortMaintPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 1),
    _SlbStatPortMaintPortIndex_Type()
)
slbStatPortMaintPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintPortIndex.setStatus("mandatory")
_SlbStatPortMaintCurBindings_Type = Gauge32
_SlbStatPortMaintCurBindings_Object = MibTableColumn
slbStatPortMaintCurBindings = _SlbStatPortMaintCurBindings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 2),
    _SlbStatPortMaintCurBindings_Type()
)
slbStatPortMaintCurBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintCurBindings.setStatus("mandatory")
_SlbStatPortMaintBindingFails_Type = Counter32
_SlbStatPortMaintBindingFails_Object = MibTableColumn
slbStatPortMaintBindingFails = _SlbStatPortMaintBindingFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 3),
    _SlbStatPortMaintBindingFails_Type()
)
slbStatPortMaintBindingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintBindingFails.setStatus("mandatory")
_SlbStatPortMaintNonTcpFrames_Type = Counter32
_SlbStatPortMaintNonTcpFrames_Object = MibTableColumn
slbStatPortMaintNonTcpFrames = _SlbStatPortMaintNonTcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 4),
    _SlbStatPortMaintNonTcpFrames_Type()
)
slbStatPortMaintNonTcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintNonTcpFrames.setStatus("mandatory")
_SlbStatPortMaintTcpFragments_Type = Counter32
_SlbStatPortMaintTcpFragments_Object = MibTableColumn
slbStatPortMaintTcpFragments = _SlbStatPortMaintTcpFragments_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 5),
    _SlbStatPortMaintTcpFragments_Type()
)
slbStatPortMaintTcpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintTcpFragments.setStatus("mandatory")
_SlbStatPortMaintUdpDatagrams_Type = Counter32
_SlbStatPortMaintUdpDatagrams_Object = MibTableColumn
slbStatPortMaintUdpDatagrams = _SlbStatPortMaintUdpDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 6),
    _SlbStatPortMaintUdpDatagrams_Type()
)
slbStatPortMaintUdpDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintUdpDatagrams.setStatus("mandatory")
_SlbStatPortMaintIncorrectVIPs_Type = Counter32
_SlbStatPortMaintIncorrectVIPs_Object = MibTableColumn
slbStatPortMaintIncorrectVIPs = _SlbStatPortMaintIncorrectVIPs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 7),
    _SlbStatPortMaintIncorrectVIPs_Type()
)
slbStatPortMaintIncorrectVIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintIncorrectVIPs.setStatus("mandatory")
_SlbStatPortMaintIncorrectVports_Type = Counter32
_SlbStatPortMaintIncorrectVports_Object = MibTableColumn
slbStatPortMaintIncorrectVports = _SlbStatPortMaintIncorrectVports_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 8),
    _SlbStatPortMaintIncorrectVports_Type()
)
slbStatPortMaintIncorrectVports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintIncorrectVports.setStatus("mandatory")
_SlbStatPortMaintRealServerNoAvails_Type = Counter32
_SlbStatPortMaintRealServerNoAvails_Object = MibTableColumn
slbStatPortMaintRealServerNoAvails = _SlbStatPortMaintRealServerNoAvails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 9),
    _SlbStatPortMaintRealServerNoAvails_Type()
)
slbStatPortMaintRealServerNoAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintRealServerNoAvails.setStatus("mandatory")
_SlbStatPortMaintFilteredDeniedFrames_Type = Counter32
_SlbStatPortMaintFilteredDeniedFrames_Object = MibTableColumn
slbStatPortMaintFilteredDeniedFrames = _SlbStatPortMaintFilteredDeniedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 10),
    _SlbStatPortMaintFilteredDeniedFrames_Type()
)
slbStatPortMaintFilteredDeniedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintFilteredDeniedFrames.setStatus("mandatory")
_SlbStatPortRealServerTable_Object = MibTable
slbStatPortRealServerTable = _SlbStatPortRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    slbStatPortRealServerTable.setStatus("mandatory")
_SlbStatPortRealServerEntry_Object = MibTableRow
slbStatPortRealServerEntry = _SlbStatPortRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1)
)
slbStatPortRealServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbStatPortRealServerPortIndex"),
    (0, "ALTEON-PRIVATE-MIBS", "slbStatPortRealServerServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatPortRealServerEntry.setStatus("mandatory")
_SlbStatPortRealServerPortIndex_Type = Integer32
_SlbStatPortRealServerPortIndex_Object = MibTableColumn
slbStatPortRealServerPortIndex = _SlbStatPortRealServerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 1),
    _SlbStatPortRealServerPortIndex_Type()
)
slbStatPortRealServerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerPortIndex.setStatus("mandatory")
_SlbStatPortRealServerServerIndex_Type = Integer32
_SlbStatPortRealServerServerIndex_Object = MibTableColumn
slbStatPortRealServerServerIndex = _SlbStatPortRealServerServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 2),
    _SlbStatPortRealServerServerIndex_Type()
)
slbStatPortRealServerServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerServerIndex.setStatus("mandatory")
_SlbStatPortRealServerCurrSessions_Type = Gauge32
_SlbStatPortRealServerCurrSessions_Object = MibTableColumn
slbStatPortRealServerCurrSessions = _SlbStatPortRealServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 3),
    _SlbStatPortRealServerCurrSessions_Type()
)
slbStatPortRealServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerCurrSessions.setStatus("mandatory")
_SlbStatPortRealServerTotalSessions_Type = Counter32
_SlbStatPortRealServerTotalSessions_Object = MibTableColumn
slbStatPortRealServerTotalSessions = _SlbStatPortRealServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 4),
    _SlbStatPortRealServerTotalSessions_Type()
)
slbStatPortRealServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerTotalSessions.setStatus("mandatory")
_SlbStatPortRealServerHCOctets_Type = Counter64
_SlbStatPortRealServerHCOctets_Object = MibTableColumn
slbStatPortRealServerHCOctets = _SlbStatPortRealServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 5),
    _SlbStatPortRealServerHCOctets_Type()
)
slbStatPortRealServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerHCOctets.setStatus("mandatory")
_SlbStatPortRealServerHCOctetsLow32_Type = Counter32
_SlbStatPortRealServerHCOctetsLow32_Object = MibTableColumn
slbStatPortRealServerHCOctetsLow32 = _SlbStatPortRealServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 6),
    _SlbStatPortRealServerHCOctetsLow32_Type()
)
slbStatPortRealServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerHCOctetsLow32.setStatus("mandatory")
_SlbStatPortRealServerHCOctetsHigh32_Type = Counter32
_SlbStatPortRealServerHCOctetsHigh32_Object = MibTableColumn
slbStatPortRealServerHCOctetsHigh32 = _SlbStatPortRealServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 7),
    _SlbStatPortRealServerHCOctetsHigh32_Type()
)
slbStatPortRealServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerHCOctetsHigh32.setStatus("mandatory")
_SlbStatMaintBackupServActs_Type = Counter32
_SlbStatMaintBackupServActs_Object = MibScalar
slbStatMaintBackupServActs = _SlbStatMaintBackupServActs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 3),
    _SlbStatMaintBackupServActs_Type()
)
slbStatMaintBackupServActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintBackupServActs.setStatus("mandatory")
_SlbStatMaintOverflowServActs_Type = Counter32
_SlbStatMaintOverflowServActs_Object = MibScalar
slbStatMaintOverflowServActs = _SlbStatMaintOverflowServActs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 4),
    _SlbStatMaintOverflowServActs_Type()
)
slbStatMaintOverflowServActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintOverflowServActs.setStatus("mandatory")
_SlbStatRServerTable_Object = MibTable
slbStatRServerTable = _SlbStatRServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5)
)
if mibBuilder.loadTexts:
    slbStatRServerTable.setStatus("mandatory")
_SlbStatRServerEntry_Object = MibTableRow
slbStatRServerEntry = _SlbStatRServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1)
)
slbStatRServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbStatRServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatRServerEntry.setStatus("mandatory")
_SlbStatRServerIndex_Type = Integer32
_SlbStatRServerIndex_Object = MibTableColumn
slbStatRServerIndex = _SlbStatRServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 1),
    _SlbStatRServerIndex_Type()
)
slbStatRServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerIndex.setStatus("mandatory")
_SlbStatRServerCurrSessions_Type = Gauge32
_SlbStatRServerCurrSessions_Object = MibTableColumn
slbStatRServerCurrSessions = _SlbStatRServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 2),
    _SlbStatRServerCurrSessions_Type()
)
slbStatRServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerCurrSessions.setStatus("mandatory")
_SlbStatRServerTotalSessions_Type = Counter32
_SlbStatRServerTotalSessions_Object = MibTableColumn
slbStatRServerTotalSessions = _SlbStatRServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 3),
    _SlbStatRServerTotalSessions_Type()
)
slbStatRServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerTotalSessions.setStatus("mandatory")
_SlbStatRServerFailures_Type = Counter32
_SlbStatRServerFailures_Object = MibTableColumn
slbStatRServerFailures = _SlbStatRServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 4),
    _SlbStatRServerFailures_Type()
)
slbStatRServerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerFailures.setStatus("mandatory")
_SlbStatRServerHighestSessions_Type = Counter32
_SlbStatRServerHighestSessions_Object = MibTableColumn
slbStatRServerHighestSessions = _SlbStatRServerHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 5),
    _SlbStatRServerHighestSessions_Type()
)
slbStatRServerHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHighestSessions.setStatus("mandatory")
_SlbStatRServerHCOctets_Type = Counter64
_SlbStatRServerHCOctets_Object = MibTableColumn
slbStatRServerHCOctets = _SlbStatRServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 6),
    _SlbStatRServerHCOctets_Type()
)
slbStatRServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctets.setStatus("mandatory")
_SlbStatRServerHCOctetsLow32_Type = Counter32
_SlbStatRServerHCOctetsLow32_Object = MibTableColumn
slbStatRServerHCOctetsLow32 = _SlbStatRServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 7),
    _SlbStatRServerHCOctetsLow32_Type()
)
slbStatRServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctetsLow32.setStatus("mandatory")
_SlbStatRServerHCOctetsHigh32_Type = Counter32
_SlbStatRServerHCOctetsHigh32_Object = MibTableColumn
slbStatRServerHCOctetsHigh32 = _SlbStatRServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 8),
    _SlbStatRServerHCOctetsHigh32_Type()
)
slbStatRServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctetsHigh32.setStatus("mandatory")
_SlbStatGroupTable_Object = MibTable
slbStatGroupTable = _SlbStatGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6)
)
if mibBuilder.loadTexts:
    slbStatGroupTable.setStatus("mandatory")
_SlbStatGroupEntry_Object = MibTableRow
slbStatGroupEntry = _SlbStatGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1)
)
slbStatGroupEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbStatGroupIndex"),
)
if mibBuilder.loadTexts:
    slbStatGroupEntry.setStatus("mandatory")
_SlbStatGroupIndex_Type = Integer32
_SlbStatGroupIndex_Object = MibTableColumn
slbStatGroupIndex = _SlbStatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 1),
    _SlbStatGroupIndex_Type()
)
slbStatGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupIndex.setStatus("mandatory")
_SlbStatGroupCurrSessions_Type = Gauge32
_SlbStatGroupCurrSessions_Object = MibTableColumn
slbStatGroupCurrSessions = _SlbStatGroupCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 2),
    _SlbStatGroupCurrSessions_Type()
)
slbStatGroupCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupCurrSessions.setStatus("mandatory")
_SlbStatGroupTotalSessions_Type = Counter32
_SlbStatGroupTotalSessions_Object = MibTableColumn
slbStatGroupTotalSessions = _SlbStatGroupTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 3),
    _SlbStatGroupTotalSessions_Type()
)
slbStatGroupTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupTotalSessions.setStatus("mandatory")
_SlbStatGroupHighestSessions_Type = Counter32
_SlbStatGroupHighestSessions_Object = MibTableColumn
slbStatGroupHighestSessions = _SlbStatGroupHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 4),
    _SlbStatGroupHighestSessions_Type()
)
slbStatGroupHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHighestSessions.setStatus("mandatory")
_SlbStatGroupHCOctets_Type = Counter64
_SlbStatGroupHCOctets_Object = MibTableColumn
slbStatGroupHCOctets = _SlbStatGroupHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 5),
    _SlbStatGroupHCOctets_Type()
)
slbStatGroupHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctets.setStatus("mandatory")
_SlbStatGroupHCOctetsLow32_Type = Counter32
_SlbStatGroupHCOctetsLow32_Object = MibTableColumn
slbStatGroupHCOctetsLow32 = _SlbStatGroupHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 6),
    _SlbStatGroupHCOctetsLow32_Type()
)
slbStatGroupHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctetsLow32.setStatus("mandatory")
_SlbStatGroupHCOctetsHigh32_Type = Counter32
_SlbStatGroupHCOctetsHigh32_Object = MibTableColumn
slbStatGroupHCOctetsHigh32 = _SlbStatGroupHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 7),
    _SlbStatGroupHCOctetsHigh32_Type()
)
slbStatGroupHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctetsHigh32.setStatus("mandatory")
_SlbStatVServerTable_Object = MibTable
slbStatVServerTable = _SlbStatVServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7)
)
if mibBuilder.loadTexts:
    slbStatVServerTable.setStatus("mandatory")
_SlbStatVServerEntry_Object = MibTableRow
slbStatVServerEntry = _SlbStatVServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1)
)
slbStatVServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbStatVServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatVServerEntry.setStatus("mandatory")
_SlbStatVServerIndex_Type = Integer32
_SlbStatVServerIndex_Object = MibTableColumn
slbStatVServerIndex = _SlbStatVServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 1),
    _SlbStatVServerIndex_Type()
)
slbStatVServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerIndex.setStatus("mandatory")
_SlbStatVServerCurrSessions_Type = Gauge32
_SlbStatVServerCurrSessions_Object = MibTableColumn
slbStatVServerCurrSessions = _SlbStatVServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 2),
    _SlbStatVServerCurrSessions_Type()
)
slbStatVServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerCurrSessions.setStatus("mandatory")
_SlbStatVServerTotalSessions_Type = Counter32
_SlbStatVServerTotalSessions_Object = MibTableColumn
slbStatVServerTotalSessions = _SlbStatVServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 3),
    _SlbStatVServerTotalSessions_Type()
)
slbStatVServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerTotalSessions.setStatus("mandatory")
_SlbStatVServerHighestSessions_Type = Counter32
_SlbStatVServerHighestSessions_Object = MibTableColumn
slbStatVServerHighestSessions = _SlbStatVServerHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 4),
    _SlbStatVServerHighestSessions_Type()
)
slbStatVServerHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHighestSessions.setStatus("mandatory")
_SlbStatVServerHCOctets_Type = Counter64
_SlbStatVServerHCOctets_Object = MibTableColumn
slbStatVServerHCOctets = _SlbStatVServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 5),
    _SlbStatVServerHCOctets_Type()
)
slbStatVServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctets.setStatus("mandatory")
_SlbStatVServerHCOctetsLow32_Type = Counter32
_SlbStatVServerHCOctetsLow32_Object = MibTableColumn
slbStatVServerHCOctetsLow32 = _SlbStatVServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 6),
    _SlbStatVServerHCOctetsLow32_Type()
)
slbStatVServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctetsLow32.setStatus("mandatory")
_SlbStatVServerHCOctetsHigh32_Type = Counter32
_SlbStatVServerHCOctetsHigh32_Object = MibTableColumn
slbStatVServerHCOctetsHigh32 = _SlbStatVServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 7),
    _SlbStatVServerHCOctetsHigh32_Type()
)
slbStatVServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctetsHigh32.setStatus("mandatory")
_SlbStatVServerHeaderHits_Type = Counter32
_SlbStatVServerHeaderHits_Object = MibTableColumn
slbStatVServerHeaderHits = _SlbStatVServerHeaderHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 8),
    _SlbStatVServerHeaderHits_Type()
)
slbStatVServerHeaderHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderHits.setStatus("mandatory")
_SlbStatVServerHeaderMisses_Type = Counter32
_SlbStatVServerHeaderMisses_Object = MibTableColumn
slbStatVServerHeaderMisses = _SlbStatVServerHeaderMisses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 9),
    _SlbStatVServerHeaderMisses_Type()
)
slbStatVServerHeaderMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderMisses.setStatus("mandatory")
_SlbStatVServerHeaderTotalSessions_Type = Counter32
_SlbStatVServerHeaderTotalSessions_Object = MibTableColumn
slbStatVServerHeaderTotalSessions = _SlbStatVServerHeaderTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 10),
    _SlbStatVServerHeaderTotalSessions_Type()
)
slbStatVServerHeaderTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderTotalSessions.setStatus("mandatory")
_ArpStats_ObjectIdentity = ObjectIdentity
arpStats = _ArpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3)
)
_ArpStatEntries_Type = Gauge32
_ArpStatEntries_Object = MibScalar
arpStatEntries = _ArpStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3, 1),
    _ArpStatEntries_Type()
)
arpStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatEntries.setStatus("mandatory")
_ArpStatHighWater_Type = Gauge32
_ArpStatHighWater_Object = MibScalar
arpStatHighWater = _ArpStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3, 2),
    _ArpStatHighWater_Type()
)
arpStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatHighWater.setStatus("mandatory")
_ArpStatMaxEntries_Type = Gauge32
_ArpStatMaxEntries_Object = MibScalar
arpStatMaxEntries = _ArpStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3, 3),
    _ArpStatMaxEntries_Type()
)
arpStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatMaxEntries.setStatus("mandatory")
_RouteStats_ObjectIdentity = ObjectIdentity
routeStats = _RouteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4)
)
_RouteStatEntries_Type = Gauge32
_RouteStatEntries_Object = MibScalar
routeStatEntries = _RouteStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4, 1),
    _RouteStatEntries_Type()
)
routeStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatEntries.setStatus("mandatory")
_RouteStatHighWater_Type = Gauge32
_RouteStatHighWater_Object = MibScalar
routeStatHighWater = _RouteStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4, 2),
    _RouteStatHighWater_Type()
)
routeStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatHighWater.setStatus("mandatory")
_RouteStatMaxEntries_Type = Gauge32
_RouteStatMaxEntries_Object = MibScalar
routeStatMaxEntries = _RouteStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4, 3),
    _RouteStatMaxEntries_Type()
)
routeStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatMaxEntries.setStatus("mandatory")
_DnsStats_ObjectIdentity = ObjectIdentity
dnsStats = _DnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 5)
)
_DnsStatInGoodDnsRequests_Type = Counter32
_DnsStatInGoodDnsRequests_Object = MibScalar
dnsStatInGoodDnsRequests = _DnsStatInGoodDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 5, 1),
    _DnsStatInGoodDnsRequests_Type()
)
dnsStatInGoodDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInGoodDnsRequests.setStatus("mandatory")
_DnsStatInBadDnsRequests_Type = Counter32
_DnsStatInBadDnsRequests_Object = MibScalar
dnsStatInBadDnsRequests = _DnsStatInBadDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 5, 2),
    _DnsStatInBadDnsRequests_Type()
)
dnsStatInBadDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInBadDnsRequests.setStatus("mandatory")
_FilterStats_ObjectIdentity = ObjectIdentity
filterStats = _FilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6)
)
_FltStatTable_Object = MibTable
fltStatTable = _FltStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1)
)
if mibBuilder.loadTexts:
    fltStatTable.setStatus("mandatory")
_FltStatTableEntry_Object = MibTableRow
fltStatTableEntry = _FltStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1, 1)
)
fltStatTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "fltStatFltIndex"),
)
if mibBuilder.loadTexts:
    fltStatTableEntry.setStatus("mandatory")
_FltStatFltIndex_Type = Integer32
_FltStatFltIndex_Object = MibTableColumn
fltStatFltIndex = _FltStatFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1, 1, 1),
    _FltStatFltIndex_Type()
)
fltStatFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatFltIndex.setStatus("mandatory")
_FltStatFltFirings_Type = Counter32
_FltStatFltFirings_Object = MibTableColumn
fltStatFltFirings = _FltStatFltFirings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1, 1, 2),
    _FltStatFltFirings_Type()
)
fltStatFltFirings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatFltFirings.setStatus("mandatory")
_GslbStats_ObjectIdentity = ObjectIdentity
gslbStats = _GslbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7)
)
_GslbStatRemRealServerTable_Object = MibTable
gslbStatRemRealServerTable = _GslbStatRemRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1)
)
if mibBuilder.loadTexts:
    gslbStatRemRealServerTable.setStatus("mandatory")
_GslbStatRemRealServerEntry_Object = MibTableRow
gslbStatRemRealServerEntry = _GslbStatRemRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1)
)
gslbStatRemRealServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "gslbStatRemRealServerIndex"),
)
if mibBuilder.loadTexts:
    gslbStatRemRealServerEntry.setStatus("mandatory")
_GslbStatRemRealServerIndex_Type = Integer32
_GslbStatRemRealServerIndex_Object = MibTableColumn
gslbStatRemRealServerIndex = _GslbStatRemRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1, 1),
    _GslbStatRemRealServerIndex_Type()
)
gslbStatRemRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerIndex.setStatus("mandatory")
_GslbStatRemRealServerDnsHandoffs_Type = Counter32
_GslbStatRemRealServerDnsHandoffs_Object = MibTableColumn
gslbStatRemRealServerDnsHandoffs = _GslbStatRemRealServerDnsHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1, 2),
    _GslbStatRemRealServerDnsHandoffs_Type()
)
gslbStatRemRealServerDnsHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerDnsHandoffs.setStatus("mandatory")
_GslbStatRemRealServerHttpRedirs_Type = Counter32
_GslbStatRemRealServerHttpRedirs_Object = MibTableColumn
gslbStatRemRealServerHttpRedirs = _GslbStatRemRealServerHttpRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1, 3),
    _GslbStatRemRealServerHttpRedirs_Type()
)
gslbStatRemRealServerHttpRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerHttpRedirs.setStatus("mandatory")
_GslbMaintStats_ObjectIdentity = ObjectIdentity
gslbMaintStats = _GslbMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 8)
)
_GslbStatMaintInGoodSiteUpdates_Type = Counter32
_GslbStatMaintInGoodSiteUpdates_Object = MibScalar
gslbStatMaintInGoodSiteUpdates = _GslbStatMaintInGoodSiteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 8, 1),
    _GslbStatMaintInGoodSiteUpdates_Type()
)
gslbStatMaintInGoodSiteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInGoodSiteUpdates.setStatus("mandatory")
_GslbStatMaintInBadSiteUpdates_Type = Counter32
_GslbStatMaintInBadSiteUpdates_Object = MibScalar
gslbStatMaintInBadSiteUpdates = _GslbStatMaintInBadSiteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 8, 2),
    _GslbStatMaintInBadSiteUpdates_Type()
)
gslbStatMaintInBadSiteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInBadSiteUpdates.setStatus("mandatory")
_VrrpStats_ObjectIdentity = ObjectIdentity
vrrpStats = _VrrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9)
)
_VrrpStatInAdvers_Type = Counter32
_VrrpStatInAdvers_Object = MibScalar
vrrpStatInAdvers = _VrrpStatInAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9, 1),
    _VrrpStatInAdvers_Type()
)
vrrpStatInAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatInAdvers.setStatus("mandatory")
_VrrpStatOutAdvers_Type = Counter32
_VrrpStatOutAdvers_Object = MibScalar
vrrpStatOutAdvers = _VrrpStatOutAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9, 2),
    _VrrpStatOutAdvers_Type()
)
vrrpStatOutAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutAdvers.setStatus("mandatory")
_VrrpStatOutBadAdvers_Type = Counter32
_VrrpStatOutBadAdvers_Object = MibScalar
vrrpStatOutBadAdvers = _VrrpStatOutBadAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9, 3),
    _VrrpStatOutBadAdvers_Type()
)
vrrpStatOutBadAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutBadAdvers.setStatus("mandatory")
_UrlStats_ObjectIdentity = ObjectIdentity
urlStats = _UrlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10)
)
_UrlRedirStats_ObjectIdentity = ObjectIdentity
urlRedirStats = _UrlRedirStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1)
)
_UrlStatRedRedirs_Type = Counter32
_UrlStatRedRedirs_Object = MibScalar
urlStatRedRedirs = _UrlStatRedRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 1),
    _UrlStatRedRedirs_Type()
)
urlStatRedRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRedirs.setStatus("mandatory")
_UrlStatRedOrigSrvs_Type = Counter32
_UrlStatRedOrigSrvs_Object = MibScalar
urlStatRedOrigSrvs = _UrlStatRedOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 2),
    _UrlStatRedOrigSrvs_Type()
)
urlStatRedOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedOrigSrvs.setStatus("mandatory")
_UrlStatRedNonGets_Type = Counter32
_UrlStatRedNonGets_Object = MibScalar
urlStatRedNonGets = _UrlStatRedNonGets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 3),
    _UrlStatRedNonGets_Type()
)
urlStatRedNonGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNonGets.setStatus("mandatory")
_UrlStatRedCookie_Type = Counter32
_UrlStatRedCookie_Object = MibScalar
urlStatRedCookie = _UrlStatRedCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 4),
    _UrlStatRedCookie_Type()
)
urlStatRedCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedCookie.setStatus("mandatory")
_UrlStatRedNoCache_Type = Counter32
_UrlStatRedNoCache_Object = MibScalar
urlStatRedNoCache = _UrlStatRedNoCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 5),
    _UrlStatRedNoCache_Type()
)
urlStatRedNoCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNoCache.setStatus("mandatory")
_UrlSlbStats_ObjectIdentity = ObjectIdentity
urlSlbStats = _UrlSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2)
)
_UrlStatSlbPathTable_Object = MibTable
urlStatSlbPathTable = _UrlStatSlbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1)
)
if mibBuilder.loadTexts:
    urlStatSlbPathTable.setStatus("mandatory")
_UrlStatSlbPathTableEntry_Object = MibTableRow
urlStatSlbPathTableEntry = _UrlStatSlbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1, 1)
)
urlStatSlbPathTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbCurCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    urlStatSlbPathTableEntry.setStatus("mandatory")
_UrlStatSlbPathIndex_Type = Integer32
_UrlStatSlbPathIndex_Object = MibTableColumn
urlStatSlbPathIndex = _UrlStatSlbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1, 1, 1),
    _UrlStatSlbPathIndex_Type()
)
urlStatSlbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathIndex.setStatus("mandatory")
_UrlStatSlbPathHits_Type = Counter32
_UrlStatSlbPathHits_Object = MibTableColumn
urlStatSlbPathHits = _UrlStatSlbPathHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1, 1, 2),
    _UrlStatSlbPathHits_Type()
)
urlStatSlbPathHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathHits.setStatus("mandatory")
_TcpStats_ObjectIdentity = ObjectIdentity
tcpStats = _TcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 11)
)
_TcpStatCurConns_Type = Gauge32
_TcpStatCurConns_Object = MibScalar
tcpStatCurConns = _TcpStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 11, 1),
    _TcpStatCurConns_Type()
)
tcpStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpStatCurConns.setStatus("mandatory")
_TcpStatHalfOpens_Type = Gauge32
_TcpStatHalfOpens_Object = MibScalar
tcpStatHalfOpens = _TcpStatHalfOpens_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 11, 2),
    _TcpStatHalfOpens_Type()
)
tcpStatHalfOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpStatHalfOpens.setStatus("mandatory")
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
_FtpStats_ObjectIdentity = ObjectIdentity
ftpStats = _FtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14)
)
_FtpSlbStats_ObjectIdentity = ObjectIdentity
ftpSlbStats = _FtpSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14, 1)
)
_FtpSlbStatTotal_Type = Counter32
_FtpSlbStatTotal_Object = MibScalar
ftpSlbStatTotal = _FtpSlbStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14, 1, 1),
    _FtpSlbStatTotal_Type()
)
ftpSlbStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpSlbStatTotal.setStatus("mandatory")
_FtpNatStatTotal_Type = Counter32
_FtpNatStatTotal_Object = MibScalar
ftpNatStatTotal = _FtpNatStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14, 1, 2),
    _FtpNatStatTotal_Type()
)
ftpNatStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpNatStatTotal.setStatus("mandatory")
_BwmStats_ObjectIdentity = ObjectIdentity
bwmStats = _BwmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15)
)
_BwmStatTcTable_Object = MibTable
bwmStatTcTable = _BwmStatTcTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1)
)
if mibBuilder.loadTexts:
    bwmStatTcTable.setStatus("mandatory")
_BwmStatTcEntry_Object = MibTableRow
bwmStatTcEntry = _BwmStatTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1)
)
bwmStatTcEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmStatTcContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatTcEntry.setStatus("mandatory")
_BwmStatTcContractIndex_Type = Integer32
_BwmStatTcContractIndex_Object = MibTableColumn
bwmStatTcContractIndex = _BwmStatTcContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 1),
    _BwmStatTcContractIndex_Type()
)
bwmStatTcContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcContractIndex.setStatus("mandatory")


class _BwmStatTcName_Type(DisplayString):
    """Custom type bwmStatTcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BwmStatTcName_Type.__name__ = "DisplayString"
_BwmStatTcName_Object = MibTableColumn
bwmStatTcName = _BwmStatTcName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 2),
    _BwmStatTcName_Type()
)
bwmStatTcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcName.setStatus("mandatory")
_BwmStatTcOutoct_Type = Counter32
_BwmStatTcOutoct_Object = MibTableColumn
bwmStatTcOutoct = _BwmStatTcOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 3),
    _BwmStatTcOutoct_Type()
)
bwmStatTcOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcOutoct.setStatus("mandatory")
_BwmStatTcOutdisoct_Type = Counter32
_BwmStatTcOutdisoct_Object = MibTableColumn
bwmStatTcOutdisoct = _BwmStatTcOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 4),
    _BwmStatTcOutdisoct_Type()
)
bwmStatTcOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcOutdisoct.setStatus("mandatory")
_BwmStatTcBufferUsed_Type = Counter32
_BwmStatTcBufferUsed_Object = MibTableColumn
bwmStatTcBufferUsed = _BwmStatTcBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 5),
    _BwmStatTcBufferUsed_Type()
)
bwmStatTcBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcBufferUsed.setStatus("mandatory")
_BwmStatTcBufferMax_Type = Counter32
_BwmStatTcBufferMax_Object = MibTableColumn
bwmStatTcBufferMax = _BwmStatTcBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 6),
    _BwmStatTcBufferMax_Type()
)
bwmStatTcBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcBufferMax.setStatus("mandatory")
_BwmStatTcrTable_Object = MibTable
bwmStatTcrTable = _BwmStatTcrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2)
)
if mibBuilder.loadTexts:
    bwmStatTcrTable.setStatus("mandatory")
_BwmStatTcrEntry_Object = MibTableRow
bwmStatTcrEntry = _BwmStatTcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1)
)
bwmStatTcrEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmStatTcrContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatTcrEntry.setStatus("mandatory")
_BwmStatTcrContractIndex_Type = Integer32
_BwmStatTcrContractIndex_Object = MibTableColumn
bwmStatTcrContractIndex = _BwmStatTcrContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 1),
    _BwmStatTcrContractIndex_Type()
)
bwmStatTcrContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrContractIndex.setStatus("mandatory")


class _BwmStatTcrName_Type(DisplayString):
    """Custom type bwmStatTcrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BwmStatTcrName_Type.__name__ = "DisplayString"
_BwmStatTcrName_Object = MibTableColumn
bwmStatTcrName = _BwmStatTcrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 2),
    _BwmStatTcrName_Type()
)
bwmStatTcrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrName.setStatus("mandatory")
_BwmStatTcrRate_Type = Integer32
_BwmStatTcrRate_Object = MibTableColumn
bwmStatTcrRate = _BwmStatTcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 3),
    _BwmStatTcrRate_Type()
)
bwmStatTcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrRate.setStatus("mandatory")
_BwmStatTcrOutoct_Type = Counter32
_BwmStatTcrOutoct_Object = MibTableColumn
bwmStatTcrOutoct = _BwmStatTcrOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 4),
    _BwmStatTcrOutoct_Type()
)
bwmStatTcrOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrOutoct.setStatus("mandatory")
_BwmStatTcrOutdisoct_Type = Counter32
_BwmStatTcrOutdisoct_Object = MibTableColumn
bwmStatTcrOutdisoct = _BwmStatTcrOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 5),
    _BwmStatTcrOutdisoct_Type()
)
bwmStatTcrOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrOutdisoct.setStatus("mandatory")
_BwmStatTcrBufferUsed_Type = Counter32
_BwmStatTcrBufferUsed_Object = MibTableColumn
bwmStatTcrBufferUsed = _BwmStatTcrBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 6),
    _BwmStatTcrBufferUsed_Type()
)
bwmStatTcrBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrBufferUsed.setStatus("mandatory")
_BwmStatTcrBufferMax_Type = Counter32
_BwmStatTcrBufferMax_Object = MibTableColumn
bwmStatTcrBufferMax = _BwmStatTcrBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 7),
    _BwmStatTcrBufferMax_Type()
)
bwmStatTcrBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrBufferMax.setStatus("mandatory")
_BwmStatSpTcTable_Object = MibTable
bwmStatSpTcTable = _BwmStatSpTcTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3)
)
if mibBuilder.loadTexts:
    bwmStatSpTcTable.setStatus("mandatory")
_BwmStatSpTcEntry_Object = MibTableRow
bwmStatSpTcEntry = _BwmStatSpTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1)
)
bwmStatSpTcEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmStatSpTcPortIndex"),
    (0, "ALTEON-PRIVATE-MIBS", "bwmStatSpTcContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatSpTcEntry.setStatus("mandatory")
_BwmStatSpTcPortIndex_Type = Integer32
_BwmStatSpTcPortIndex_Object = MibTableColumn
bwmStatSpTcPortIndex = _BwmStatSpTcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 1),
    _BwmStatSpTcPortIndex_Type()
)
bwmStatSpTcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcPortIndex.setStatus("mandatory")
_BwmStatSpTcContractIndex_Type = Integer32
_BwmStatSpTcContractIndex_Object = MibTableColumn
bwmStatSpTcContractIndex = _BwmStatSpTcContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 2),
    _BwmStatSpTcContractIndex_Type()
)
bwmStatSpTcContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcContractIndex.setStatus("mandatory")


class _BwmStatSpTcName_Type(DisplayString):
    """Custom type bwmStatSpTcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BwmStatSpTcName_Type.__name__ = "DisplayString"
_BwmStatSpTcName_Object = MibTableColumn
bwmStatSpTcName = _BwmStatSpTcName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 3),
    _BwmStatSpTcName_Type()
)
bwmStatSpTcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcName.setStatus("mandatory")
_BwmStatSpTcOutoct_Type = Counter32
_BwmStatSpTcOutoct_Object = MibTableColumn
bwmStatSpTcOutoct = _BwmStatSpTcOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 4),
    _BwmStatSpTcOutoct_Type()
)
bwmStatSpTcOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcOutoct.setStatus("mandatory")
_BwmStatSpTcOutdisoct_Type = Counter32
_BwmStatSpTcOutdisoct_Object = MibTableColumn
bwmStatSpTcOutdisoct = _BwmStatSpTcOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 5),
    _BwmStatSpTcOutdisoct_Type()
)
bwmStatSpTcOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcOutdisoct.setStatus("mandatory")
_BwmStatSpTcBufferUsed_Type = Counter32
_BwmStatSpTcBufferUsed_Object = MibTableColumn
bwmStatSpTcBufferUsed = _BwmStatSpTcBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 6),
    _BwmStatSpTcBufferUsed_Type()
)
bwmStatSpTcBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcBufferUsed.setStatus("mandatory")
_BwmStatSpTcBufferMax_Type = Counter32
_BwmStatSpTcBufferMax_Object = MibTableColumn
bwmStatSpTcBufferMax = _BwmStatSpTcBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 7),
    _BwmStatSpTcBufferMax_Type()
)
bwmStatSpTcBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcBufferMax.setStatus("mandatory")
_BwmStatSpTcrTable_Object = MibTable
bwmStatSpTcrTable = _BwmStatSpTcrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4)
)
if mibBuilder.loadTexts:
    bwmStatSpTcrTable.setStatus("mandatory")
_BwmStatSpTcrEntry_Object = MibTableRow
bwmStatSpTcrEntry = _BwmStatSpTcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1)
)
bwmStatSpTcrEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmStatSpTcrPortIndex"),
    (0, "ALTEON-PRIVATE-MIBS", "bwmStatSpTcrContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatSpTcrEntry.setStatus("mandatory")
_BwmStatSpTcrPortIndex_Type = Integer32
_BwmStatSpTcrPortIndex_Object = MibTableColumn
bwmStatSpTcrPortIndex = _BwmStatSpTcrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 1),
    _BwmStatSpTcrPortIndex_Type()
)
bwmStatSpTcrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrPortIndex.setStatus("mandatory")
_BwmStatSpTcrContractIndex_Type = Integer32
_BwmStatSpTcrContractIndex_Object = MibTableColumn
bwmStatSpTcrContractIndex = _BwmStatSpTcrContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 2),
    _BwmStatSpTcrContractIndex_Type()
)
bwmStatSpTcrContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrContractIndex.setStatus("mandatory")


class _BwmStatSpTcrName_Type(DisplayString):
    """Custom type bwmStatSpTcrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BwmStatSpTcrName_Type.__name__ = "DisplayString"
_BwmStatSpTcrName_Object = MibTableColumn
bwmStatSpTcrName = _BwmStatSpTcrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 3),
    _BwmStatSpTcrName_Type()
)
bwmStatSpTcrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrName.setStatus("mandatory")
_BwmStatSpTcrRate_Type = Integer32
_BwmStatSpTcrRate_Object = MibTableColumn
bwmStatSpTcrRate = _BwmStatSpTcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 4),
    _BwmStatSpTcrRate_Type()
)
bwmStatSpTcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrRate.setStatus("mandatory")
_BwmStatSpTcrOutoct_Type = Counter32
_BwmStatSpTcrOutoct_Object = MibTableColumn
bwmStatSpTcrOutoct = _BwmStatSpTcrOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 5),
    _BwmStatSpTcrOutoct_Type()
)
bwmStatSpTcrOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrOutoct.setStatus("mandatory")
_BwmStatSpTcrOutdisoct_Type = Counter32
_BwmStatSpTcrOutdisoct_Object = MibTableColumn
bwmStatSpTcrOutdisoct = _BwmStatSpTcrOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 6),
    _BwmStatSpTcrOutdisoct_Type()
)
bwmStatSpTcrOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrOutdisoct.setStatus("mandatory")
_BwmStatSpTcrBufferUsed_Type = Counter32
_BwmStatSpTcrBufferUsed_Object = MibTableColumn
bwmStatSpTcrBufferUsed = _BwmStatSpTcrBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 7),
    _BwmStatSpTcrBufferUsed_Type()
)
bwmStatSpTcrBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrBufferUsed.setStatus("mandatory")
_BwmStatSpTcrBufferMax_Type = Counter32
_BwmStatSpTcrBufferMax_Object = MibTableColumn
bwmStatSpTcrBufferMax = _BwmStatSpTcrBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 8),
    _BwmStatSpTcrBufferMax_Type()
)
bwmStatSpTcrBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrBufferMax.setStatus("mandatory")
_Information_ObjectIdentity = ObjectIdentity
information = _Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9)
)
_Port_info_ObjectIdentity = ObjectIdentity
port_info = _Port_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1)
)
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("mandatory")
_PortInfoTableEntry_Object = MibTableRow
portInfoTableEntry = _PortInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1)
)
portInfoTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "portInfoIndx"),
)
if mibBuilder.loadTexts:
    portInfoTableEntry.setStatus("mandatory")


class _PortInfoIndx_Type(Integer32):
    """Custom type portInfoIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortInfoIndx_Type.__name__ = "Integer32"
_PortInfoIndx_Object = MibTableColumn
portInfoIndx = _PortInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 1),
    _PortInfoIndx_Type()
)
portInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoIndx.setStatus("mandatory")


class _PortInfoSpeed_Type(Integer32):
    """Custom type portInfoSpeed based on Integer32"""
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
        *(("mbs10", 2),
          ("mbs100", 3),
          ("mbs1000", 4),
          ("other", 1))
    )


_PortInfoSpeed_Type.__name__ = "Integer32"
_PortInfoSpeed_Object = MibTableColumn
portInfoSpeed = _PortInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 2),
    _PortInfoSpeed_Type()
)
portInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSpeed.setStatus("mandatory")


class _PortInfoMode_Type(Integer32):
    """Custom type portInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 3),
          ("other", 1))
    )


_PortInfoMode_Type.__name__ = "Integer32"
_PortInfoMode_Object = MibTableColumn
portInfoMode = _PortInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 3),
    _PortInfoMode_Type()
)
portInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoMode.setStatus("mandatory")


class _PortInfoFlowCtrl_Type(Integer32):
    """Custom type portInfoFlowCtrl based on Integer32"""
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
        *(("both", 4),
          ("none", 5),
          ("other", 1),
          ("receive", 3),
          ("transmit", 2))
    )


_PortInfoFlowCtrl_Type.__name__ = "Integer32"
_PortInfoFlowCtrl_Object = MibTableColumn
portInfoFlowCtrl = _PortInfoFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 4),
    _PortInfoFlowCtrl_Type()
)
portInfoFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoFlowCtrl.setStatus("mandatory")


class _PortInfoLink_Type(Integer32):
    """Custom type portInfoLink based on Integer32"""
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
        *(("disabled", 3),
          ("down", 2),
          ("inoperative", 4),
          ("up", 1))
    )


_PortInfoLink_Type.__name__ = "Integer32"
_PortInfoLink_Object = MibTableColumn
portInfoLink = _PortInfoLink_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 5),
    _PortInfoLink_Type()
)
portInfoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoLink.setStatus("mandatory")
_Slb_info_ObjectIdentity = ObjectIdentity
slb_info = _Slb_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2)
)
_SlbFailOverInfoTable_Object = MibTable
slbFailOverInfoTable = _SlbFailOverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    slbFailOverInfoTable.setStatus("mandatory")
_SlbFailOverInfoEntry_Object = MibTableRow
slbFailOverInfoEntry = _SlbFailOverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1)
)
slbFailOverInfoEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbFailOverInfoIndex"),
)
if mibBuilder.loadTexts:
    slbFailOverInfoEntry.setStatus("mandatory")
_SlbFailOverInfoIndex_Type = Integer32
_SlbFailOverInfoIndex_Object = MibTableColumn
slbFailOverInfoIndex = _SlbFailOverInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 1),
    _SlbFailOverInfoIndex_Type()
)
slbFailOverInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoIndex.setStatus("mandatory")
_SlbFailOverInfoPrimaryIp_Type = IpAddress
_SlbFailOverInfoPrimaryIp_Object = MibTableColumn
slbFailOverInfoPrimaryIp = _SlbFailOverInfoPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 2),
    _SlbFailOverInfoPrimaryIp_Type()
)
slbFailOverInfoPrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoPrimaryIp.setStatus("mandatory")


class _SlbFailOverInfoPrimaryStatus_Type(Integer32):
    """Custom type slbFailOverInfoPrimaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SlbFailOverInfoPrimaryStatus_Type.__name__ = "Integer32"
_SlbFailOverInfoPrimaryStatus_Object = MibTableColumn
slbFailOverInfoPrimaryStatus = _SlbFailOverInfoPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 3),
    _SlbFailOverInfoPrimaryStatus_Type()
)
slbFailOverInfoPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoPrimaryStatus.setStatus("mandatory")


class _SlbFailOverInfoPrimaryState_Type(Integer32):
    """Custom type slbFailOverInfoPrimaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_SlbFailOverInfoPrimaryState_Type.__name__ = "Integer32"
_SlbFailOverInfoPrimaryState_Object = MibTableColumn
slbFailOverInfoPrimaryState = _SlbFailOverInfoPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 4),
    _SlbFailOverInfoPrimaryState_Type()
)
slbFailOverInfoPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoPrimaryState.setStatus("mandatory")
_SlbFailOverInfoSecondaryIp_Type = IpAddress
_SlbFailOverInfoSecondaryIp_Object = MibTableColumn
slbFailOverInfoSecondaryIp = _SlbFailOverInfoSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 5),
    _SlbFailOverInfoSecondaryIp_Type()
)
slbFailOverInfoSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoSecondaryIp.setStatus("mandatory")


class _SlbFailOverInfoSecondaryStatus_Type(Integer32):
    """Custom type slbFailOverInfoSecondaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SlbFailOverInfoSecondaryStatus_Type.__name__ = "Integer32"
_SlbFailOverInfoSecondaryStatus_Object = MibTableColumn
slbFailOverInfoSecondaryStatus = _SlbFailOverInfoSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 6),
    _SlbFailOverInfoSecondaryStatus_Type()
)
slbFailOverInfoSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoSecondaryStatus.setStatus("mandatory")


class _SlbFailOverInfoSecondaryState_Type(Integer32):
    """Custom type slbFailOverInfoSecondaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_SlbFailOverInfoSecondaryState_Type.__name__ = "Integer32"
_SlbFailOverInfoSecondaryState_Object = MibTableColumn
slbFailOverInfoSecondaryState = _SlbFailOverInfoSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 7),
    _SlbFailOverInfoSecondaryState_Type()
)
slbFailOverInfoSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoSecondaryState.setStatus("mandatory")
_SlbRealServerInfoTable_Object = MibTable
slbRealServerInfoTable = _SlbRealServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    slbRealServerInfoTable.setStatus("mandatory")
_SlbRealServerInfoEntry_Object = MibTableRow
slbRealServerInfoEntry = _SlbRealServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1)
)
slbRealServerInfoEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "slbRealServerInfoIndex"),
)
if mibBuilder.loadTexts:
    slbRealServerInfoEntry.setStatus("mandatory")
_SlbRealServerInfoIndex_Type = Integer32
_SlbRealServerInfoIndex_Object = MibTableColumn
slbRealServerInfoIndex = _SlbRealServerInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 1),
    _SlbRealServerInfoIndex_Type()
)
slbRealServerInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoIndex.setStatus("mandatory")
_SlbRealServerInfoIpAddr_Type = IpAddress
_SlbRealServerInfoIpAddr_Object = MibTableColumn
slbRealServerInfoIpAddr = _SlbRealServerInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 2),
    _SlbRealServerInfoIpAddr_Type()
)
slbRealServerInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoIpAddr.setStatus("mandatory")
_SlbRealServerMacAddr_Type = PhysAddress
_SlbRealServerMacAddr_Object = MibTableColumn
slbRealServerMacAddr = _SlbRealServerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 3),
    _SlbRealServerMacAddr_Type()
)
slbRealServerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerMacAddr.setStatus("mandatory")
_SlbRealServerInfoSwitchPort_Type = Integer32
_SlbRealServerInfoSwitchPort_Object = MibTableColumn
slbRealServerInfoSwitchPort = _SlbRealServerInfoSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 4),
    _SlbRealServerInfoSwitchPort_Type()
)
slbRealServerInfoSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoSwitchPort.setStatus("mandatory")


class _SlbRealServerInfoHealthLayer_Type(Integer32):
    """Custom type slbRealServerInfoHealthLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer3", 2),
          ("layer4", 3),
          ("other", 1))
    )


_SlbRealServerInfoHealthLayer_Type.__name__ = "Integer32"
_SlbRealServerInfoHealthLayer_Object = MibTableColumn
slbRealServerInfoHealthLayer = _SlbRealServerInfoHealthLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 5),
    _SlbRealServerInfoHealthLayer_Type()
)
slbRealServerInfoHealthLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoHealthLayer.setStatus("mandatory")


class _SlbRealServerInfoOverflow_Type(Integer32):
    """Custom type slbRealServerInfoOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-overflow", 2),
          ("overflow", 1))
    )


_SlbRealServerInfoOverflow_Type.__name__ = "Integer32"
_SlbRealServerInfoOverflow_Object = MibTableColumn
slbRealServerInfoOverflow = _SlbRealServerInfoOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 6),
    _SlbRealServerInfoOverflow_Type()
)
slbRealServerInfoOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoOverflow.setStatus("mandatory")


class _SlbRealServerInfoState_Type(Integer32):
    """Custom type slbRealServerInfoState based on Integer32"""
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
        *(("disabled", 4),
          ("failed", 3),
          ("other", 1),
          ("running", 2))
    )


_SlbRealServerInfoState_Type.__name__ = "Integer32"
_SlbRealServerInfoState_Object = MibTableColumn
slbRealServerInfoState = _SlbRealServerInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 7),
    _SlbRealServerInfoState_Type()
)
slbRealServerInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoState.setStatus("mandatory")
_Ip_info_ObjectIdentity = ObjectIdentity
ip_info = _Ip_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3)
)
_IpRouteInfoTable_Object = MibTable
ipRouteInfoTable = _IpRouteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    ipRouteInfoTable.setStatus("mandatory")
_IpRouteInfoEntry_Object = MibTableRow
ipRouteInfoEntry = _IpRouteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1)
)
ipRouteInfoEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "ipRouteInfoIndx"),
)
if mibBuilder.loadTexts:
    ipRouteInfoEntry.setStatus("mandatory")
_IpRouteInfoIndx_Type = Integer32
_IpRouteInfoIndx_Object = MibTableColumn
ipRouteInfoIndx = _IpRouteInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 1),
    _IpRouteInfoIndx_Type()
)
ipRouteInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoIndx.setStatus("mandatory")
_IpRouteInfoDestIp_Type = IpAddress
_IpRouteInfoDestIp_Object = MibTableColumn
ipRouteInfoDestIp = _IpRouteInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 2),
    _IpRouteInfoDestIp_Type()
)
ipRouteInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoDestIp.setStatus("mandatory")
_IpRouteInfoMask_Type = IpAddress
_IpRouteInfoMask_Object = MibTableColumn
ipRouteInfoMask = _IpRouteInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 3),
    _IpRouteInfoMask_Type()
)
ipRouteInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoMask.setStatus("mandatory")
_IpRouteInfoGateway_Type = IpAddress
_IpRouteInfoGateway_Object = MibTableColumn
ipRouteInfoGateway = _IpRouteInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 4),
    _IpRouteInfoGateway_Type()
)
ipRouteInfoGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoGateway.setStatus("mandatory")


class _IpRouteInfoTag_Type(Integer32):
    """Custom type ipRouteInfoTag based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("addr", 5),
          ("broadcast", 7),
          ("fixed", 1),
          ("icmp", 2),
          ("martian", 8),
          ("multicast", 9),
          ("rip", 6),
          ("snmp", 4),
          ("static", 3))
    )


_IpRouteInfoTag_Type.__name__ = "Integer32"
_IpRouteInfoTag_Object = MibTableColumn
ipRouteInfoTag = _IpRouteInfoTag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 5),
    _IpRouteInfoTag_Type()
)
ipRouteInfoTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoTag.setStatus("mandatory")


class _IpRouteInfoType_Type(Integer32):
    """Custom type ipRouteInfoType based on Integer32"""
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
        *(("broadcast", 4),
          ("direct", 2),
          ("indirect", 1),
          ("local", 3),
          ("martian", 5),
          ("multicast", 6),
          ("other", 7))
    )


_IpRouteInfoType_Type.__name__ = "Integer32"
_IpRouteInfoType_Object = MibTableColumn
ipRouteInfoType = _IpRouteInfoType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 6),
    _IpRouteInfoType_Type()
)
ipRouteInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoType.setStatus("mandatory")
_IpRouteInfoInterface_Type = Integer32
_IpRouteInfoInterface_Object = MibTableColumn
ipRouteInfoInterface = _IpRouteInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 7),
    _IpRouteInfoInterface_Type()
)
ipRouteInfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoInterface.setStatus("mandatory")
_ArpInfoTable_Object = MibTable
arpInfoTable = _ArpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    arpInfoTable.setStatus("mandatory")
_ArpInfoEntry_Object = MibTableRow
arpInfoEntry = _ArpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1)
)
arpInfoEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "arpInfoDestIp"),
)
if mibBuilder.loadTexts:
    arpInfoEntry.setStatus("mandatory")
_ArpInfoDestIp_Type = IpAddress
_ArpInfoDestIp_Object = MibTableColumn
arpInfoDestIp = _ArpInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 1),
    _ArpInfoDestIp_Type()
)
arpInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoDestIp.setStatus("mandatory")
_ArpInfoMacAddr_Type = PhysAddress
_ArpInfoMacAddr_Object = MibTableColumn
arpInfoMacAddr = _ArpInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 2),
    _ArpInfoMacAddr_Type()
)
arpInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoMacAddr.setStatus("mandatory")
_ArpInfoVLAN_Type = Integer32
_ArpInfoVLAN_Object = MibTableColumn
arpInfoVLAN = _ArpInfoVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 3),
    _ArpInfoVLAN_Type()
)
arpInfoVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoVLAN.setStatus("mandatory")
_ArpInfoSrcPort_Type = Integer32
_ArpInfoSrcPort_Object = MibTableColumn
arpInfoSrcPort = _ArpInfoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 4),
    _ArpInfoSrcPort_Type()
)
arpInfoSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoSrcPort.setStatus("mandatory")
_ArpInfoRefPorts_Type = Integer32
_ArpInfoRefPorts_Object = MibTableColumn
arpInfoRefPorts = _ArpInfoRefPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 5),
    _ArpInfoRefPorts_Type()
)
arpInfoRefPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoRefPorts.setStatus("mandatory")


class _ArpInfoFlag_Type(Integer32):
    """Custom type arpInfoFlag based on Integer32"""
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
        *(("clear", 1),
          ("indirect", 4),
          ("permanent", 3),
          ("unresolved", 2))
    )


_ArpInfoFlag_Type.__name__ = "Integer32"
_ArpInfoFlag_Object = MibTableColumn
arpInfoFlag = _ArpInfoFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 6),
    _ArpInfoFlag_Type()
)
arpInfoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoFlag.setStatus("mandatory")
_Vrrp_info_ObjectIdentity = ObjectIdentity
vrrp_info = _Vrrp_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4)
)
_VrrpInfoVirtRtrTable_Object = MibTable
vrrpInfoVirtRtrTable = _VrrpInfoVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTable.setStatus("mandatory")
_VrrpInfoVirtRtrTableEntry_Object = MibTableRow
vrrpInfoVirtRtrTableEntry = _VrrpInfoVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1)
)
vrrpInfoVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vrrpInfoVirtRtrIndex"),
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTableEntry.setStatus("mandatory")
_VrrpInfoVirtRtrIndex_Type = Integer32
_VrrpInfoVirtRtrIndex_Object = MibTableColumn
vrrpInfoVirtRtrIndex = _VrrpInfoVirtRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1, 1),
    _VrrpInfoVirtRtrIndex_Type()
)
vrrpInfoVirtRtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrIndex.setStatus("mandatory")


class _VrrpInfoVirtRtrState_Type(Integer32):
    """Custom type vrrpInfoVirtRtrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("init", 1),
          ("master", 2))
    )


_VrrpInfoVirtRtrState_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrState_Object = MibTableColumn
vrrpInfoVirtRtrState = _VrrpInfoVirtRtrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1, 2),
    _VrrpInfoVirtRtrState_Type()
)
vrrpInfoVirtRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrState.setStatus("mandatory")
_Filtering_ObjectIdentity = ObjectIdentity
filtering = _Filtering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10)
)
_FltCfgTableMaxSize_Type = Integer32
_FltCfgTableMaxSize_Object = MibScalar
fltCfgTableMaxSize = _FltCfgTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 1),
    _FltCfgTableMaxSize_Type()
)
fltCfgTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCfgTableMaxSize.setStatus("mandatory")
_FltCurCfgTable_Object = MibTable
fltCurCfgTable = _FltCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    fltCurCfgTable.setStatus("mandatory")
_FltCurCfgTableEntry_Object = MibTableRow
fltCurCfgTableEntry = _FltCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1)
)
fltCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "fltCurCfgIndx"),
)
if mibBuilder.loadTexts:
    fltCurCfgTableEntry.setStatus("mandatory")
_FltCurCfgIndx_Type = Integer32
_FltCurCfgIndx_Object = MibTableColumn
fltCurCfgIndx = _FltCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 1),
    _FltCurCfgIndx_Type()
)
fltCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIndx.setStatus("mandatory")
_FltCurCfgSrcIp_Type = IpAddress
_FltCurCfgSrcIp_Object = MibTableColumn
fltCurCfgSrcIp = _FltCurCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 2),
    _FltCurCfgSrcIp_Type()
)
fltCurCfgSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIp.setStatus("mandatory")
_FltCurCfgSrcIpMask_Type = IpAddress
_FltCurCfgSrcIpMask_Object = MibTableColumn
fltCurCfgSrcIpMask = _FltCurCfgSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 3),
    _FltCurCfgSrcIpMask_Type()
)
fltCurCfgSrcIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIpMask.setStatus("mandatory")
_FltCurCfgDstIp_Type = IpAddress
_FltCurCfgDstIp_Object = MibTableColumn
fltCurCfgDstIp = _FltCurCfgDstIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 4),
    _FltCurCfgDstIp_Type()
)
fltCurCfgDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIp.setStatus("mandatory")
_FltCurCfgDstIpMask_Type = IpAddress
_FltCurCfgDstIpMask_Object = MibTableColumn
fltCurCfgDstIpMask = _FltCurCfgDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 5),
    _FltCurCfgDstIpMask_Type()
)
fltCurCfgDstIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIpMask.setStatus("mandatory")
_FltCurCfgProtocol_Type = Integer32
_FltCurCfgProtocol_Object = MibTableColumn
fltCurCfgProtocol = _FltCurCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 6),
    _FltCurCfgProtocol_Type()
)
fltCurCfgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgProtocol.setStatus("mandatory")
_FltCurCfgRangeHighSrcPort_Type = Integer32
_FltCurCfgRangeHighSrcPort_Object = MibTableColumn
fltCurCfgRangeHighSrcPort = _FltCurCfgRangeHighSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 7),
    _FltCurCfgRangeHighSrcPort_Type()
)
fltCurCfgRangeHighSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeHighSrcPort.setStatus("mandatory")
_FltCurCfgRangeLowSrcPort_Type = Integer32
_FltCurCfgRangeLowSrcPort_Object = MibTableColumn
fltCurCfgRangeLowSrcPort = _FltCurCfgRangeLowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 8),
    _FltCurCfgRangeLowSrcPort_Type()
)
fltCurCfgRangeLowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeLowSrcPort.setStatus("mandatory")
_FltCurCfgRangeLowDstPort_Type = Integer32
_FltCurCfgRangeLowDstPort_Object = MibTableColumn
fltCurCfgRangeLowDstPort = _FltCurCfgRangeLowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 9),
    _FltCurCfgRangeLowDstPort_Type()
)
fltCurCfgRangeLowDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeLowDstPort.setStatus("mandatory")
_FltCurCfgRangeHighDstPort_Type = Integer32
_FltCurCfgRangeHighDstPort_Object = MibTableColumn
fltCurCfgRangeHighDstPort = _FltCurCfgRangeHighDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 10),
    _FltCurCfgRangeHighDstPort_Type()
)
fltCurCfgRangeHighDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeHighDstPort.setStatus("mandatory")


class _FltCurCfgAction_Type(Integer32):
    """Custom type fltCurCfgAction based on Integer32"""
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
        *(("allow", 1),
          ("deny", 2),
          ("nat", 4),
          ("redirect", 3))
    )


_FltCurCfgAction_Type.__name__ = "Integer32"
_FltCurCfgAction_Object = MibTableColumn
fltCurCfgAction = _FltCurCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 11),
    _FltCurCfgAction_Type()
)
fltCurCfgAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAction.setStatus("mandatory")
_FltCurCfgRedirPort_Type = Integer32
_FltCurCfgRedirPort_Object = MibTableColumn
fltCurCfgRedirPort = _FltCurCfgRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 12),
    _FltCurCfgRedirPort_Type()
)
fltCurCfgRedirPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRedirPort.setStatus("mandatory")
_FltCurCfgRedirGroup_Type = Integer32
_FltCurCfgRedirGroup_Object = MibTableColumn
fltCurCfgRedirGroup = _FltCurCfgRedirGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 13),
    _FltCurCfgRedirGroup_Type()
)
fltCurCfgRedirGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRedirGroup.setStatus("mandatory")


class _FltCurCfgLog_Type(Integer32):
    """Custom type fltCurCfgLog based on Integer32"""
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


_FltCurCfgLog_Type.__name__ = "Integer32"
_FltCurCfgLog_Object = MibTableColumn
fltCurCfgLog = _FltCurCfgLog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 14),
    _FltCurCfgLog_Type()
)
fltCurCfgLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLog.setStatus("mandatory")


class _FltCurCfgState_Type(Integer32):
    """Custom type fltCurCfgState based on Integer32"""
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


_FltCurCfgState_Type.__name__ = "Integer32"
_FltCurCfgState_Object = MibTableColumn
fltCurCfgState = _FltCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 15),
    _FltCurCfgState_Type()
)
fltCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgState.setStatus("mandatory")


class _FltCurCfgNat_Type(Integer32):
    """Custom type fltCurCfgNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-address", 1),
          ("source-address", 2))
    )


_FltCurCfgNat_Type.__name__ = "Integer32"
_FltCurCfgNat_Object = MibTableColumn
fltCurCfgNat = _FltCurCfgNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 16),
    _FltCurCfgNat_Type()
)
fltCurCfgNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgNat.setStatus("mandatory")


class _FltCurCfgCache_Type(Integer32):
    """Custom type fltCurCfgCache based on Integer32"""
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


_FltCurCfgCache_Type.__name__ = "Integer32"
_FltCurCfgCache_Object = MibTableColumn
fltCurCfgCache = _FltCurCfgCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 17),
    _FltCurCfgCache_Type()
)
fltCurCfgCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgCache.setStatus("mandatory")


class _FltCurCfgInvert_Type(Integer32):
    """Custom type fltCurCfgInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert-off", 2),
          ("invert-on", 1))
    )


_FltCurCfgInvert_Type.__name__ = "Integer32"
_FltCurCfgInvert_Object = MibTableColumn
fltCurCfgInvert = _FltCurCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 18),
    _FltCurCfgInvert_Type()
)
fltCurCfgInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgInvert.setStatus("mandatory")


class _FltCurCfgClientProxy_Type(Integer32):
    """Custom type fltCurCfgClientProxy based on Integer32"""
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


_FltCurCfgClientProxy_Type.__name__ = "Integer32"
_FltCurCfgClientProxy_Object = MibTableColumn
fltCurCfgClientProxy = _FltCurCfgClientProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 19),
    _FltCurCfgClientProxy_Type()
)
fltCurCfgClientProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgClientProxy.setStatus("mandatory")


class _FltCurCfgTcpAck_Type(Integer32):
    """Custom type fltCurCfgTcpAck based on Integer32"""
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


_FltCurCfgTcpAck_Type.__name__ = "Integer32"
_FltCurCfgTcpAck_Object = MibTableColumn
fltCurCfgTcpAck = _FltCurCfgTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 20),
    _FltCurCfgTcpAck_Type()
)
fltCurCfgTcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTcpAck.setStatus("mandatory")


class _FltCurCfgUrlRedir_Type(Integer32):
    """Custom type fltCurCfgUrlRedir based on Integer32"""
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


_FltCurCfgUrlRedir_Type.__name__ = "Integer32"
_FltCurCfgUrlRedir_Object = MibTableColumn
fltCurCfgUrlRedir = _FltCurCfgUrlRedir_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 21),
    _FltCurCfgUrlRedir_Type()
)
fltCurCfgUrlRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlRedir.setStatus("mandatory")
_FltCurCfgSrcMac_Type = PhysAddress
_FltCurCfgSrcMac_Object = MibTableColumn
fltCurCfgSrcMac = _FltCurCfgSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 22),
    _FltCurCfgSrcMac_Type()
)
fltCurCfgSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcMac.setStatus("mandatory")
_FltCurCfgDstMac_Type = PhysAddress
_FltCurCfgDstMac_Object = MibTableColumn
fltCurCfgDstMac = _FltCurCfgDstMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 23),
    _FltCurCfgDstMac_Type()
)
fltCurCfgDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstMac.setStatus("mandatory")


class _FltCurCfgFtpNatActive_Type(Integer32):
    """Custom type fltCurCfgFtpNatActive based on Integer32"""
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


_FltCurCfgFtpNatActive_Type.__name__ = "Integer32"
_FltCurCfgFtpNatActive_Object = MibTableColumn
fltCurCfgFtpNatActive = _FltCurCfgFtpNatActive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 24),
    _FltCurCfgFtpNatActive_Type()
)
fltCurCfgFtpNatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgFtpNatActive.setStatus("mandatory")


class _FltCurCfgAclTcpUrg_Type(Integer32):
    """Custom type fltCurCfgAclTcpUrg based on Integer32"""
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


_FltCurCfgAclTcpUrg_Type.__name__ = "Integer32"
_FltCurCfgAclTcpUrg_Object = MibTableColumn
fltCurCfgAclTcpUrg = _FltCurCfgAclTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 25),
    _FltCurCfgAclTcpUrg_Type()
)
fltCurCfgAclTcpUrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpUrg.setStatus("mandatory")


class _FltCurCfgAclTcpAck_Type(Integer32):
    """Custom type fltCurCfgAclTcpAck based on Integer32"""
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


_FltCurCfgAclTcpAck_Type.__name__ = "Integer32"
_FltCurCfgAclTcpAck_Object = MibTableColumn
fltCurCfgAclTcpAck = _FltCurCfgAclTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 26),
    _FltCurCfgAclTcpAck_Type()
)
fltCurCfgAclTcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpAck.setStatus("mandatory")


class _FltCurCfgAclTcpPsh_Type(Integer32):
    """Custom type fltCurCfgAclTcpPsh based on Integer32"""
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


_FltCurCfgAclTcpPsh_Type.__name__ = "Integer32"
_FltCurCfgAclTcpPsh_Object = MibTableColumn
fltCurCfgAclTcpPsh = _FltCurCfgAclTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 27),
    _FltCurCfgAclTcpPsh_Type()
)
fltCurCfgAclTcpPsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpPsh.setStatus("mandatory")


class _FltCurCfgAclTcpRst_Type(Integer32):
    """Custom type fltCurCfgAclTcpRst based on Integer32"""
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


_FltCurCfgAclTcpRst_Type.__name__ = "Integer32"
_FltCurCfgAclTcpRst_Object = MibTableColumn
fltCurCfgAclTcpRst = _FltCurCfgAclTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 28),
    _FltCurCfgAclTcpRst_Type()
)
fltCurCfgAclTcpRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpRst.setStatus("mandatory")


class _FltCurCfgAclTcpSyn_Type(Integer32):
    """Custom type fltCurCfgAclTcpSyn based on Integer32"""
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


_FltCurCfgAclTcpSyn_Type.__name__ = "Integer32"
_FltCurCfgAclTcpSyn_Object = MibTableColumn
fltCurCfgAclTcpSyn = _FltCurCfgAclTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 29),
    _FltCurCfgAclTcpSyn_Type()
)
fltCurCfgAclTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpSyn.setStatus("mandatory")


class _FltCurCfgAclTcpFin_Type(Integer32):
    """Custom type fltCurCfgAclTcpFin based on Integer32"""
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


_FltCurCfgAclTcpFin_Type.__name__ = "Integer32"
_FltCurCfgAclTcpFin_Object = MibTableColumn
fltCurCfgAclTcpFin = _FltCurCfgAclTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 30),
    _FltCurCfgAclTcpFin_Type()
)
fltCurCfgAclTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpFin.setStatus("mandatory")
_FltCurCfgAclIcmp_Type = Integer32
_FltCurCfgAclIcmp_Object = MibTableColumn
fltCurCfgAclIcmp = _FltCurCfgAclIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 31),
    _FltCurCfgAclIcmp_Type()
)
fltCurCfgAclIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIcmp.setStatus("mandatory")


class _FltCurCfgAclIpOption_Type(Integer32):
    """Custom type fltCurCfgAclIpOption based on Integer32"""
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
        *(("any", 1),
          ("loose", 4),
          ("rroute", 2),
          ("strict", 5),
          ("tstamp", 3))
    )


_FltCurCfgAclIpOption_Type.__name__ = "Integer32"
_FltCurCfgAclIpOption_Object = MibTableColumn
fltCurCfgAclIpOption = _FltCurCfgAclIpOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 32),
    _FltCurCfgAclIpOption_Type()
)
fltCurCfgAclIpOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpOption.setStatus("mandatory")
_FltCurCfgBwmContract_Type = Integer32
_FltCurCfgBwmContract_Object = MibTableColumn
fltCurCfgBwmContract = _FltCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 33),
    _FltCurCfgBwmContract_Type()
)
fltCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgBwmContract.setStatus("mandatory")


class _FltCurCfgAclIpTos_Type(Integer32):
    """Custom type fltCurCfgAclIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTos_Type.__name__ = "Integer32"
_FltCurCfgAclIpTos_Object = MibTableColumn
fltCurCfgAclIpTos = _FltCurCfgAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 34),
    _FltCurCfgAclIpTos_Type()
)
fltCurCfgAclIpTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTos.setStatus("mandatory")


class _FltCurCfgAclIpTosMask_Type(Integer32):
    """Custom type fltCurCfgAclIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTosMask_Type.__name__ = "Integer32"
_FltCurCfgAclIpTosMask_Object = MibTableColumn
fltCurCfgAclIpTosMask = _FltCurCfgAclIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 35),
    _FltCurCfgAclIpTosMask_Type()
)
fltCurCfgAclIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTosMask.setStatus("mandatory")


class _FltCurCfgAclIpTosNew_Type(Integer32):
    """Custom type fltCurCfgAclIpTosNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTosNew_Type.__name__ = "Integer32"
_FltCurCfgAclIpTosNew_Object = MibTableColumn
fltCurCfgAclIpTosNew = _FltCurCfgAclIpTosNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 36),
    _FltCurCfgAclIpTosNew_Type()
)
fltCurCfgAclIpTosNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTosNew.setStatus("mandatory")


class _FltCurCfgFwlb_Type(Integer32):
    """Custom type fltCurCfgFwlb based on Integer32"""
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


_FltCurCfgFwlb_Type.__name__ = "Integer32"
_FltCurCfgFwlb_Object = MibTableColumn
fltCurCfgFwlb = _FltCurCfgFwlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 37),
    _FltCurCfgFwlb_Type()
)
fltCurCfgFwlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgFwlb.setStatus("mandatory")
_FltNewCfgTable_Object = MibTable
fltNewCfgTable = _FltNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    fltNewCfgTable.setStatus("mandatory")
_FltNewCfgTableEntry_Object = MibTableRow
fltNewCfgTableEntry = _FltNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1)
)
fltNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "fltNewCfgIndx"),
)
if mibBuilder.loadTexts:
    fltNewCfgTableEntry.setStatus("mandatory")
_FltNewCfgIndx_Type = Integer32
_FltNewCfgIndx_Object = MibTableColumn
fltNewCfgIndx = _FltNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 1),
    _FltNewCfgIndx_Type()
)
fltNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgIndx.setStatus("mandatory")
_FltNewCfgSrcIp_Type = IpAddress
_FltNewCfgSrcIp_Object = MibTableColumn
fltNewCfgSrcIp = _FltNewCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 2),
    _FltNewCfgSrcIp_Type()
)
fltNewCfgSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgSrcIp.setStatus("mandatory")
_FltNewCfgSrcIpMask_Type = IpAddress
_FltNewCfgSrcIpMask_Object = MibTableColumn
fltNewCfgSrcIpMask = _FltNewCfgSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 3),
    _FltNewCfgSrcIpMask_Type()
)
fltNewCfgSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgSrcIpMask.setStatus("mandatory")
_FltNewCfgDstIp_Type = IpAddress
_FltNewCfgDstIp_Object = MibTableColumn
fltNewCfgDstIp = _FltNewCfgDstIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 4),
    _FltNewCfgDstIp_Type()
)
fltNewCfgDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDstIp.setStatus("mandatory")
_FltNewCfgDstIpMask_Type = IpAddress
_FltNewCfgDstIpMask_Object = MibTableColumn
fltNewCfgDstIpMask = _FltNewCfgDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 5),
    _FltNewCfgDstIpMask_Type()
)
fltNewCfgDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDstIpMask.setStatus("mandatory")
_FltNewCfgProtocol_Type = Integer32
_FltNewCfgProtocol_Object = MibTableColumn
fltNewCfgProtocol = _FltNewCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 6),
    _FltNewCfgProtocol_Type()
)
fltNewCfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgProtocol.setStatus("mandatory")
_FltNewCfgRangeHighSrcPort_Type = Integer32
_FltNewCfgRangeHighSrcPort_Object = MibTableColumn
fltNewCfgRangeHighSrcPort = _FltNewCfgRangeHighSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 7),
    _FltNewCfgRangeHighSrcPort_Type()
)
fltNewCfgRangeHighSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeHighSrcPort.setStatus("mandatory")
_FltNewCfgRangeLowSrcPort_Type = Integer32
_FltNewCfgRangeLowSrcPort_Object = MibTableColumn
fltNewCfgRangeLowSrcPort = _FltNewCfgRangeLowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 8),
    _FltNewCfgRangeLowSrcPort_Type()
)
fltNewCfgRangeLowSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeLowSrcPort.setStatus("mandatory")
_FltNewCfgRangeLowDstPort_Type = Integer32
_FltNewCfgRangeLowDstPort_Object = MibTableColumn
fltNewCfgRangeLowDstPort = _FltNewCfgRangeLowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 9),
    _FltNewCfgRangeLowDstPort_Type()
)
fltNewCfgRangeLowDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeLowDstPort.setStatus("mandatory")
_FltNewCfgRangeHighDstPort_Type = Integer32
_FltNewCfgRangeHighDstPort_Object = MibTableColumn
fltNewCfgRangeHighDstPort = _FltNewCfgRangeHighDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 10),
    _FltNewCfgRangeHighDstPort_Type()
)
fltNewCfgRangeHighDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeHighDstPort.setStatus("mandatory")


class _FltNewCfgAction_Type(Integer32):
    """Custom type fltNewCfgAction based on Integer32"""
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
        *(("allow", 1),
          ("deny", 2),
          ("nat", 4),
          ("redirect", 3))
    )


_FltNewCfgAction_Type.__name__ = "Integer32"
_FltNewCfgAction_Object = MibTableColumn
fltNewCfgAction = _FltNewCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 11),
    _FltNewCfgAction_Type()
)
fltNewCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAction.setStatus("mandatory")
_FltNewCfgRedirPort_Type = Integer32
_FltNewCfgRedirPort_Object = MibTableColumn
fltNewCfgRedirPort = _FltNewCfgRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 12),
    _FltNewCfgRedirPort_Type()
)
fltNewCfgRedirPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRedirPort.setStatus("mandatory")
_FltNewCfgRedirGroup_Type = Integer32
_FltNewCfgRedirGroup_Object = MibTableColumn
fltNewCfgRedirGroup = _FltNewCfgRedirGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 13),
    _FltNewCfgRedirGroup_Type()
)
fltNewCfgRedirGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRedirGroup.setStatus("mandatory")


class _FltNewCfgLog_Type(Integer32):
    """Custom type fltNewCfgLog based on Integer32"""
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


_FltNewCfgLog_Type.__name__ = "Integer32"
_FltNewCfgLog_Object = MibTableColumn
fltNewCfgLog = _FltNewCfgLog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 14),
    _FltNewCfgLog_Type()
)
fltNewCfgLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgLog.setStatus("mandatory")


class _FltNewCfgState_Type(Integer32):
    """Custom type fltNewCfgState based on Integer32"""
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


_FltNewCfgState_Type.__name__ = "Integer32"
_FltNewCfgState_Object = MibTableColumn
fltNewCfgState = _FltNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 15),
    _FltNewCfgState_Type()
)
fltNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgState.setStatus("mandatory")


class _FltNewCfgDelete_Type(Integer32):
    """Custom type fltNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_FltNewCfgDelete_Type.__name__ = "Integer32"
_FltNewCfgDelete_Object = MibTableColumn
fltNewCfgDelete = _FltNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 16),
    _FltNewCfgDelete_Type()
)
fltNewCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDelete.setStatus("mandatory")


class _FltNewCfgNat_Type(Integer32):
    """Custom type fltNewCfgNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-address", 1),
          ("source-address", 2))
    )


_FltNewCfgNat_Type.__name__ = "Integer32"
_FltNewCfgNat_Object = MibTableColumn
fltNewCfgNat = _FltNewCfgNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 17),
    _FltNewCfgNat_Type()
)
fltNewCfgNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgNat.setStatus("mandatory")


class _FltNewCfgCache_Type(Integer32):
    """Custom type fltNewCfgCache based on Integer32"""
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


_FltNewCfgCache_Type.__name__ = "Integer32"
_FltNewCfgCache_Object = MibTableColumn
fltNewCfgCache = _FltNewCfgCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 18),
    _FltNewCfgCache_Type()
)
fltNewCfgCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgCache.setStatus("mandatory")


class _FltNewCfgInvert_Type(Integer32):
    """Custom type fltNewCfgInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert-off", 2),
          ("invert-on", 1))
    )


_FltNewCfgInvert_Type.__name__ = "Integer32"
_FltNewCfgInvert_Object = MibTableColumn
fltNewCfgInvert = _FltNewCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 19),
    _FltNewCfgInvert_Type()
)
fltNewCfgInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgInvert.setStatus("mandatory")


class _FltNewCfgClientProxy_Type(Integer32):
    """Custom type fltNewCfgClientProxy based on Integer32"""
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


_FltNewCfgClientProxy_Type.__name__ = "Integer32"
_FltNewCfgClientProxy_Object = MibTableColumn
fltNewCfgClientProxy = _FltNewCfgClientProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 20),
    _FltNewCfgClientProxy_Type()
)
fltNewCfgClientProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgClientProxy.setStatus("mandatory")


class _FltNewCfgTcpAck_Type(Integer32):
    """Custom type fltNewCfgTcpAck based on Integer32"""
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


_FltNewCfgTcpAck_Type.__name__ = "Integer32"
_FltNewCfgTcpAck_Object = MibTableColumn
fltNewCfgTcpAck = _FltNewCfgTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 21),
    _FltNewCfgTcpAck_Type()
)
fltNewCfgTcpAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgTcpAck.setStatus("mandatory")


class _FltNewCfgUrlRedir_Type(Integer32):
    """Custom type fltNewCfgUrlRedir based on Integer32"""
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


_FltNewCfgUrlRedir_Type.__name__ = "Integer32"
_FltNewCfgUrlRedir_Object = MibTableColumn
fltNewCfgUrlRedir = _FltNewCfgUrlRedir_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 22),
    _FltNewCfgUrlRedir_Type()
)
fltNewCfgUrlRedir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgUrlRedir.setStatus("mandatory")
_FltNewCfgSrcMac_Type = PhysAddress
_FltNewCfgSrcMac_Object = MibTableColumn
fltNewCfgSrcMac = _FltNewCfgSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 23),
    _FltNewCfgSrcMac_Type()
)
fltNewCfgSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgSrcMac.setStatus("mandatory")
_FltNewCfgDstMac_Type = PhysAddress
_FltNewCfgDstMac_Object = MibTableColumn
fltNewCfgDstMac = _FltNewCfgDstMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 24),
    _FltNewCfgDstMac_Type()
)
fltNewCfgDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDstMac.setStatus("mandatory")


class _FltNewCfgFtpNatActive_Type(Integer32):
    """Custom type fltNewCfgFtpNatActive based on Integer32"""
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


_FltNewCfgFtpNatActive_Type.__name__ = "Integer32"
_FltNewCfgFtpNatActive_Object = MibTableColumn
fltNewCfgFtpNatActive = _FltNewCfgFtpNatActive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 25),
    _FltNewCfgFtpNatActive_Type()
)
fltNewCfgFtpNatActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgFtpNatActive.setStatus("mandatory")


class _FltNewCfgAclTcpUrg_Type(Integer32):
    """Custom type fltNewCfgAclTcpUrg based on Integer32"""
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


_FltNewCfgAclTcpUrg_Type.__name__ = "Integer32"
_FltNewCfgAclTcpUrg_Object = MibTableColumn
fltNewCfgAclTcpUrg = _FltNewCfgAclTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 26),
    _FltNewCfgAclTcpUrg_Type()
)
fltNewCfgAclTcpUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpUrg.setStatus("mandatory")


class _FltNewCfgAclTcpAck_Type(Integer32):
    """Custom type fltNewCfgAclTcpAck based on Integer32"""
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


_FltNewCfgAclTcpAck_Type.__name__ = "Integer32"
_FltNewCfgAclTcpAck_Object = MibTableColumn
fltNewCfgAclTcpAck = _FltNewCfgAclTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 27),
    _FltNewCfgAclTcpAck_Type()
)
fltNewCfgAclTcpAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpAck.setStatus("mandatory")


class _FltNewCfgAclTcpPsh_Type(Integer32):
    """Custom type fltNewCfgAclTcpPsh based on Integer32"""
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


_FltNewCfgAclTcpPsh_Type.__name__ = "Integer32"
_FltNewCfgAclTcpPsh_Object = MibTableColumn
fltNewCfgAclTcpPsh = _FltNewCfgAclTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 28),
    _FltNewCfgAclTcpPsh_Type()
)
fltNewCfgAclTcpPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpPsh.setStatus("mandatory")


class _FltNewCfgAclTcpRst_Type(Integer32):
    """Custom type fltNewCfgAclTcpRst based on Integer32"""
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


_FltNewCfgAclTcpRst_Type.__name__ = "Integer32"
_FltNewCfgAclTcpRst_Object = MibTableColumn
fltNewCfgAclTcpRst = _FltNewCfgAclTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 29),
    _FltNewCfgAclTcpRst_Type()
)
fltNewCfgAclTcpRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpRst.setStatus("mandatory")


class _FltNewCfgAclTcpSyn_Type(Integer32):
    """Custom type fltNewCfgAclTcpSyn based on Integer32"""
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


_FltNewCfgAclTcpSyn_Type.__name__ = "Integer32"
_FltNewCfgAclTcpSyn_Object = MibTableColumn
fltNewCfgAclTcpSyn = _FltNewCfgAclTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 30),
    _FltNewCfgAclTcpSyn_Type()
)
fltNewCfgAclTcpSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpSyn.setStatus("mandatory")


class _FltNewCfgAclTcpFin_Type(Integer32):
    """Custom type fltNewCfgAclTcpFin based on Integer32"""
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


_FltNewCfgAclTcpFin_Type.__name__ = "Integer32"
_FltNewCfgAclTcpFin_Object = MibTableColumn
fltNewCfgAclTcpFin = _FltNewCfgAclTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 31),
    _FltNewCfgAclTcpFin_Type()
)
fltNewCfgAclTcpFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpFin.setStatus("mandatory")
_FltNewCfgAclIcmp_Type = Integer32
_FltNewCfgAclIcmp_Object = MibTableColumn
fltNewCfgAclIcmp = _FltNewCfgAclIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 32),
    _FltNewCfgAclIcmp_Type()
)
fltNewCfgAclIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIcmp.setStatus("mandatory")


class _FltNewCfgAclIpOption_Type(Integer32):
    """Custom type fltNewCfgAclIpOption based on Integer32"""
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
        *(("any", 1),
          ("loose", 4),
          ("rroute", 2),
          ("strict", 5),
          ("tstamp", 3))
    )


_FltNewCfgAclIpOption_Type.__name__ = "Integer32"
_FltNewCfgAclIpOption_Object = MibTableColumn
fltNewCfgAclIpOption = _FltNewCfgAclIpOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 33),
    _FltNewCfgAclIpOption_Type()
)
fltNewCfgAclIpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpOption.setStatus("mandatory")
_FltNewCfgBwmContract_Type = Integer32
_FltNewCfgBwmContract_Object = MibTableColumn
fltNewCfgBwmContract = _FltNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 34),
    _FltNewCfgBwmContract_Type()
)
fltNewCfgBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgBwmContract.setStatus("mandatory")


class _FltNewCfgAclIpTos_Type(Integer32):
    """Custom type fltNewCfgAclIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTos_Type.__name__ = "Integer32"
_FltNewCfgAclIpTos_Object = MibTableColumn
fltNewCfgAclIpTos = _FltNewCfgAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 35),
    _FltNewCfgAclIpTos_Type()
)
fltNewCfgAclIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTos.setStatus("mandatory")


class _FltNewCfgAclIpTosMask_Type(Integer32):
    """Custom type fltNewCfgAclIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTosMask_Type.__name__ = "Integer32"
_FltNewCfgAclIpTosMask_Object = MibTableColumn
fltNewCfgAclIpTosMask = _FltNewCfgAclIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 36),
    _FltNewCfgAclIpTosMask_Type()
)
fltNewCfgAclIpTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTosMask.setStatus("mandatory")


class _FltNewCfgAclIpTosNew_Type(Integer32):
    """Custom type fltNewCfgAclIpTosNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTosNew_Type.__name__ = "Integer32"
_FltNewCfgAclIpTosNew_Object = MibTableColumn
fltNewCfgAclIpTosNew = _FltNewCfgAclIpTosNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 37),
    _FltNewCfgAclIpTosNew_Type()
)
fltNewCfgAclIpTosNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTosNew.setStatus("mandatory")


class _FltNewCfgFwlb_Type(Integer32):
    """Custom type fltNewCfgFwlb based on Integer32"""
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


_FltNewCfgFwlb_Type.__name__ = "Integer32"
_FltNewCfgFwlb_Object = MibTableColumn
fltNewCfgFwlb = _FltNewCfgFwlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 38),
    _FltNewCfgFwlb_Type()
)
fltNewCfgFwlb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgFwlb.setStatus("mandatory")
_FltCurCfgPortTable_Object = MibTable
fltCurCfgPortTable = _FltCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4)
)
if mibBuilder.loadTexts:
    fltCurCfgPortTable.setStatus("mandatory")
_FltCurCfgPortTableEntry_Object = MibTableRow
fltCurCfgPortTableEntry = _FltCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1)
)
fltCurCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "fltCurCfgPortIndx"),
)
if mibBuilder.loadTexts:
    fltCurCfgPortTableEntry.setStatus("mandatory")
_FltCurCfgPortIndx_Type = Integer32
_FltCurCfgPortIndx_Object = MibTableColumn
fltCurCfgPortIndx = _FltCurCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1, 1),
    _FltCurCfgPortIndx_Type()
)
fltCurCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortIndx.setStatus("mandatory")


class _FltCurCfgPortState_Type(Integer32):
    """Custom type fltCurCfgPortState based on Integer32"""
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


_FltCurCfgPortState_Type.__name__ = "Integer32"
_FltCurCfgPortState_Object = MibTableColumn
fltCurCfgPortState = _FltCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1, 2),
    _FltCurCfgPortState_Type()
)
fltCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortState.setStatus("mandatory")


class _FltCurCfgPortFiltBmap_Type(OctetString):
    """Custom type fltCurCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FltCurCfgPortFiltBmap_Type.__name__ = "OctetString"
_FltCurCfgPortFiltBmap_Object = MibTableColumn
fltCurCfgPortFiltBmap = _FltCurCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1, 3),
    _FltCurCfgPortFiltBmap_Type()
)
fltCurCfgPortFiltBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortFiltBmap.setStatus("mandatory")
_FltNewCfgPortTable_Object = MibTable
fltNewCfgPortTable = _FltNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5)
)
if mibBuilder.loadTexts:
    fltNewCfgPortTable.setStatus("mandatory")
_FltNewCfgPortTableEntry_Object = MibTableRow
fltNewCfgPortTableEntry = _FltNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1)
)
fltNewCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "fltNewCfgPortIndx"),
)
if mibBuilder.loadTexts:
    fltNewCfgPortTableEntry.setStatus("mandatory")
_FltNewCfgPortIndx_Type = Integer32
_FltNewCfgPortIndx_Object = MibTableColumn
fltNewCfgPortIndx = _FltNewCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 1),
    _FltNewCfgPortIndx_Type()
)
fltNewCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgPortIndx.setStatus("mandatory")


class _FltNewCfgPortState_Type(Integer32):
    """Custom type fltNewCfgPortState based on Integer32"""
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


_FltNewCfgPortState_Type.__name__ = "Integer32"
_FltNewCfgPortState_Object = MibTableColumn
fltNewCfgPortState = _FltNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 2),
    _FltNewCfgPortState_Type()
)
fltNewCfgPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgPortState.setStatus("mandatory")


class _FltNewCfgPortFiltBmap_Type(OctetString):
    """Custom type fltNewCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FltNewCfgPortFiltBmap_Type.__name__ = "OctetString"
_FltNewCfgPortFiltBmap_Object = MibTableColumn
fltNewCfgPortFiltBmap = _FltNewCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 3),
    _FltNewCfgPortFiltBmap_Type()
)
fltNewCfgPortFiltBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgPortFiltBmap.setStatus("mandatory")
_FltNewCfgPortAddFiltRule_Type = Integer32
_FltNewCfgPortAddFiltRule_Object = MibTableColumn
fltNewCfgPortAddFiltRule = _FltNewCfgPortAddFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 4),
    _FltNewCfgPortAddFiltRule_Type()
)
fltNewCfgPortAddFiltRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgPortAddFiltRule.setStatus("mandatory")
_FltNewCfgPortRemFiltRule_Type = Integer32
_FltNewCfgPortRemFiltRule_Object = MibTableColumn
fltNewCfgPortRemFiltRule = _FltNewCfgPortRemFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 5),
    _FltNewCfgPortRemFiltRule_Type()
)
fltNewCfgPortRemFiltRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgPortRemFiltRule.setStatus("mandatory")
_GlobalSLB_ObjectIdentity = ObjectIdentity
globalSLB = _GlobalSLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11)
)
_GslbGeneral_ObjectIdentity = ObjectIdentity
gslbGeneral = _GslbGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1)
)


class _GslbCurCfgGenState_Type(Integer32):
    """Custom type gslbCurCfgGenState based on Integer32"""
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


_GslbCurCfgGenState_Type.__name__ = "Integer32"
_GslbCurCfgGenState_Object = MibScalar
gslbCurCfgGenState = _GslbCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 1),
    _GslbCurCfgGenState_Type()
)
gslbCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenState.setStatus("mandatory")


class _GslbNewCfgGenState_Type(Integer32):
    """Custom type gslbNewCfgGenState based on Integer32"""
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


_GslbNewCfgGenState_Type.__name__ = "Integer32"
_GslbNewCfgGenState_Object = MibScalar
gslbNewCfgGenState = _GslbNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 2),
    _GslbNewCfgGenState_Type()
)
gslbNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenState.setStatus("mandatory")


class _GslbCurCfgGenDnsHandoff_Type(Integer32):
    """Custom type gslbCurCfgGenDnsHandoff based on Integer32"""
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


_GslbCurCfgGenDnsHandoff_Type.__name__ = "Integer32"
_GslbCurCfgGenDnsHandoff_Object = MibScalar
gslbCurCfgGenDnsHandoff = _GslbCurCfgGenDnsHandoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 3),
    _GslbCurCfgGenDnsHandoff_Type()
)
gslbCurCfgGenDnsHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenDnsHandoff.setStatus("mandatory")


class _GslbNewCfgGenDnsHandoff_Type(Integer32):
    """Custom type gslbNewCfgGenDnsHandoff based on Integer32"""
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


_GslbNewCfgGenDnsHandoff_Type.__name__ = "Integer32"
_GslbNewCfgGenDnsHandoff_Object = MibScalar
gslbNewCfgGenDnsHandoff = _GslbNewCfgGenDnsHandoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 4),
    _GslbNewCfgGenDnsHandoff_Type()
)
gslbNewCfgGenDnsHandoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenDnsHandoff.setStatus("mandatory")


class _GslbCurCfgGenDnsTTL_Type(Integer32):
    """Custom type gslbCurCfgGenDnsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_GslbCurCfgGenDnsTTL_Type.__name__ = "Integer32"
_GslbCurCfgGenDnsTTL_Object = MibScalar
gslbCurCfgGenDnsTTL = _GslbCurCfgGenDnsTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 5),
    _GslbCurCfgGenDnsTTL_Type()
)
gslbCurCfgGenDnsTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenDnsTTL.setStatus("mandatory")


class _GslbNewCfgGenDnsTTL_Type(Integer32):
    """Custom type gslbNewCfgGenDnsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_GslbNewCfgGenDnsTTL_Type.__name__ = "Integer32"
_GslbNewCfgGenDnsTTL_Object = MibScalar
gslbNewCfgGenDnsTTL = _GslbNewCfgGenDnsTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 6),
    _GslbNewCfgGenDnsTTL_Type()
)
gslbNewCfgGenDnsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenDnsTTL.setStatus("mandatory")


class _GslbCurCfgGenHttpRedirect_Type(Integer32):
    """Custom type gslbCurCfgGenHttpRedirect based on Integer32"""
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


_GslbCurCfgGenHttpRedirect_Type.__name__ = "Integer32"
_GslbCurCfgGenHttpRedirect_Object = MibScalar
gslbCurCfgGenHttpRedirect = _GslbCurCfgGenHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 7),
    _GslbCurCfgGenHttpRedirect_Type()
)
gslbCurCfgGenHttpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenHttpRedirect.setStatus("mandatory")


class _GslbNewCfgGenHttpRedirect_Type(Integer32):
    """Custom type gslbNewCfgGenHttpRedirect based on Integer32"""
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


_GslbNewCfgGenHttpRedirect_Type.__name__ = "Integer32"
_GslbNewCfgGenHttpRedirect_Object = MibScalar
gslbNewCfgGenHttpRedirect = _GslbNewCfgGenHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 8),
    _GslbNewCfgGenHttpRedirect_Type()
)
gslbNewCfgGenHttpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenHttpRedirect.setStatus("mandatory")


class _GslbCurCfgGenRemSiteUpdateInterval_Type(Integer32):
    """Custom type gslbCurCfgGenRemSiteUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_GslbCurCfgGenRemSiteUpdateInterval_Type.__name__ = "Integer32"
_GslbCurCfgGenRemSiteUpdateInterval_Object = MibScalar
gslbCurCfgGenRemSiteUpdateInterval = _GslbCurCfgGenRemSiteUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 9),
    _GslbCurCfgGenRemSiteUpdateInterval_Type()
)
gslbCurCfgGenRemSiteUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenRemSiteUpdateInterval.setStatus("mandatory")


class _GslbNewCfgGenRemSiteUpdateInterval_Type(Integer32):
    """Custom type gslbNewCfgGenRemSiteUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_GslbNewCfgGenRemSiteUpdateInterval_Type.__name__ = "Integer32"
_GslbNewCfgGenRemSiteUpdateInterval_Object = MibScalar
gslbNewCfgGenRemSiteUpdateInterval = _GslbNewCfgGenRemSiteUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 10),
    _GslbNewCfgGenRemSiteUpdateInterval_Type()
)
gslbNewCfgGenRemSiteUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenRemSiteUpdateInterval.setStatus("mandatory")


class _GslbCurCfgGenDnsLocalPref_Type(Integer32):
    """Custom type gslbCurCfgGenDnsLocalPref based on Integer32"""
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


_GslbCurCfgGenDnsLocalPref_Type.__name__ = "Integer32"
_GslbCurCfgGenDnsLocalPref_Object = MibScalar
gslbCurCfgGenDnsLocalPref = _GslbCurCfgGenDnsLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 11),
    _GslbCurCfgGenDnsLocalPref_Type()
)
gslbCurCfgGenDnsLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenDnsLocalPref.setStatus("mandatory")


class _GslbNewCfgGenDnsLocalPref_Type(Integer32):
    """Custom type gslbNewCfgGenDnsLocalPref based on Integer32"""
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


_GslbNewCfgGenDnsLocalPref_Type.__name__ = "Integer32"
_GslbNewCfgGenDnsLocalPref_Object = MibScalar
gslbNewCfgGenDnsLocalPref = _GslbNewCfgGenDnsLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 12),
    _GslbNewCfgGenDnsLocalPref_Type()
)
gslbNewCfgGenDnsLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenDnsLocalPref.setStatus("mandatory")


class _GslbCurCfgGenMinco_Type(Integer32):
    """Custom type gslbCurCfgGenMinco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbCurCfgGenMinco_Type.__name__ = "Integer32"
_GslbCurCfgGenMinco_Object = MibScalar
gslbCurCfgGenMinco = _GslbCurCfgGenMinco_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 13),
    _GslbCurCfgGenMinco_Type()
)
gslbCurCfgGenMinco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenMinco.setStatus("mandatory")


class _GslbNewCfgGenMinco_Type(Integer32):
    """Custom type gslbNewCfgGenMinco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbNewCfgGenMinco_Type.__name__ = "Integer32"
_GslbNewCfgGenMinco_Object = MibScalar
gslbNewCfgGenMinco = _GslbNewCfgGenMinco_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 14),
    _GslbNewCfgGenMinco_Type()
)
gslbNewCfgGenMinco.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenMinco.setStatus("mandatory")


class _GslbCurCfgGenOne_Type(Integer32):
    """Custom type gslbCurCfgGenOne based on Integer32"""
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


_GslbCurCfgGenOne_Type.__name__ = "Integer32"
_GslbCurCfgGenOne_Object = MibScalar
gslbCurCfgGenOne = _GslbCurCfgGenOne_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 15),
    _GslbCurCfgGenOne_Type()
)
gslbCurCfgGenOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenOne.setStatus("mandatory")


class _GslbNewCfgGenOne_Type(Integer32):
    """Custom type gslbNewCfgGenOne based on Integer32"""
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


_GslbNewCfgGenOne_Type.__name__ = "Integer32"
_GslbNewCfgGenOne_Object = MibScalar
gslbNewCfgGenOne = _GslbNewCfgGenOne_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 16),
    _GslbNewCfgGenOne_Type()
)
gslbNewCfgGenOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenOne.setStatus("mandatory")


class _GslbCurCfgGenUsern_Type(Integer32):
    """Custom type gslbCurCfgGenUsern based on Integer32"""
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


_GslbCurCfgGenUsern_Type.__name__ = "Integer32"
_GslbCurCfgGenUsern_Object = MibScalar
gslbCurCfgGenUsern = _GslbCurCfgGenUsern_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 17),
    _GslbCurCfgGenUsern_Type()
)
gslbCurCfgGenUsern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenUsern.setStatus("mandatory")


class _GslbNewCfgGenUsern_Type(Integer32):
    """Custom type gslbNewCfgGenUsern based on Integer32"""
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


_GslbNewCfgGenUsern_Type.__name__ = "Integer32"
_GslbNewCfgGenUsern_Object = MibScalar
gslbNewCfgGenUsern = _GslbNewCfgGenUsern_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 18),
    _GslbNewCfgGenUsern_Type()
)
gslbNewCfgGenUsern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenUsern.setStatus("mandatory")


class _GslbCurCfgGenGeo_Type(Integer32):
    """Custom type gslbCurCfgGenGeo based on Integer32"""
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


_GslbCurCfgGenGeo_Type.__name__ = "Integer32"
_GslbCurCfgGenGeo_Object = MibScalar
gslbCurCfgGenGeo = _GslbCurCfgGenGeo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 19),
    _GslbCurCfgGenGeo_Type()
)
gslbCurCfgGenGeo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenGeo.setStatus("mandatory")


class _GslbNewCfgGenGeo_Type(Integer32):
    """Custom type gslbNewCfgGenGeo based on Integer32"""
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


_GslbNewCfgGenGeo_Type.__name__ = "Integer32"
_GslbNewCfgGenGeo_Object = MibScalar
gslbNewCfgGenGeo = _GslbNewCfgGenGeo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 20),
    _GslbNewCfgGenGeo_Type()
)
gslbNewCfgGenGeo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenGeo.setStatus("mandatory")
_GslbDNS_ObjectIdentity = ObjectIdentity
gslbDNS = _GslbDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2)
)
_DnsCurCfgPrimaryIpAddr_Type = IpAddress
_DnsCurCfgPrimaryIpAddr_Object = MibScalar
dnsCurCfgPrimaryIpAddr = _DnsCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 1),
    _DnsCurCfgPrimaryIpAddr_Type()
)
dnsCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgPrimaryIpAddr.setStatus("mandatory")
_DnsNewCfgPrimaryIpAddr_Type = IpAddress
_DnsNewCfgPrimaryIpAddr_Object = MibScalar
dnsNewCfgPrimaryIpAddr = _DnsNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 2),
    _DnsNewCfgPrimaryIpAddr_Type()
)
dnsNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgPrimaryIpAddr.setStatus("mandatory")
_DnsCurCfgSecondaryIpAddr_Type = IpAddress
_DnsCurCfgSecondaryIpAddr_Object = MibScalar
dnsCurCfgSecondaryIpAddr = _DnsCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 3),
    _DnsCurCfgSecondaryIpAddr_Type()
)
dnsCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgSecondaryIpAddr.setStatus("mandatory")
_DnsNewCfgSecondaryIpAddr_Type = IpAddress
_DnsNewCfgSecondaryIpAddr_Object = MibScalar
dnsNewCfgSecondaryIpAddr = _DnsNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 4),
    _DnsNewCfgSecondaryIpAddr_Type()
)
dnsNewCfgSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgSecondaryIpAddr.setStatus("mandatory")
_DnsCurCfgDomainName_Type = DisplayString
_DnsCurCfgDomainName_Object = MibScalar
dnsCurCfgDomainName = _DnsCurCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 5),
    _DnsCurCfgDomainName_Type()
)
dnsCurCfgDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgDomainName.setStatus("mandatory")
_DnsNewCfgDomainName_Type = DisplayString
_DnsNewCfgDomainName_Object = MibScalar
dnsNewCfgDomainName = _DnsNewCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 6),
    _DnsNewCfgDomainName_Type()
)
dnsNewCfgDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgDomainName.setStatus("mandatory")
_GslbSites_ObjectIdentity = ObjectIdentity
gslbSites = _GslbSites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3)
)
_GslbRemSiteTableMaxSize_Type = Integer32
_GslbRemSiteTableMaxSize_Object = MibScalar
gslbRemSiteTableMaxSize = _GslbRemSiteTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 1),
    _GslbRemSiteTableMaxSize_Type()
)
gslbRemSiteTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbRemSiteTableMaxSize.setStatus("mandatory")
_GslbCurCfgRemSiteTable_Object = MibTable
gslbCurCfgRemSiteTable = _GslbCurCfgRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteTable.setStatus("mandatory")
_GslbCurCfgRemSiteTableEntry_Object = MibTableRow
gslbCurCfgRemSiteTableEntry = _GslbCurCfgRemSiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1)
)
gslbCurCfgRemSiteTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "gslbCurCfgRemSiteIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteTableEntry.setStatus("mandatory")
_GslbCurCfgRemSiteIndx_Type = Integer32
_GslbCurCfgRemSiteIndx_Object = MibTableColumn
gslbCurCfgRemSiteIndx = _GslbCurCfgRemSiteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 1),
    _GslbCurCfgRemSiteIndx_Type()
)
gslbCurCfgRemSiteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteIndx.setStatus("mandatory")
_GslbCurCfgRemSitePrimaryIp_Type = IpAddress
_GslbCurCfgRemSitePrimaryIp_Object = MibTableColumn
gslbCurCfgRemSitePrimaryIp = _GslbCurCfgRemSitePrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 2),
    _GslbCurCfgRemSitePrimaryIp_Type()
)
gslbCurCfgRemSitePrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSitePrimaryIp.setStatus("mandatory")
_GslbCurCfgRemSiteSecondaryIp_Type = IpAddress
_GslbCurCfgRemSiteSecondaryIp_Object = MibTableColumn
gslbCurCfgRemSiteSecondaryIp = _GslbCurCfgRemSiteSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 3),
    _GslbCurCfgRemSiteSecondaryIp_Type()
)
gslbCurCfgRemSiteSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteSecondaryIp.setStatus("mandatory")


class _GslbCurCfgRemSiteState_Type(Integer32):
    """Custom type gslbCurCfgRemSiteState based on Integer32"""
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


_GslbCurCfgRemSiteState_Type.__name__ = "Integer32"
_GslbCurCfgRemSiteState_Object = MibTableColumn
gslbCurCfgRemSiteState = _GslbCurCfgRemSiteState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 4),
    _GslbCurCfgRemSiteState_Type()
)
gslbCurCfgRemSiteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteState.setStatus("mandatory")


class _GslbCurCfgRemSiteUpdate_Type(Integer32):
    """Custom type gslbCurCfgRemSiteUpdate based on Integer32"""
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


_GslbCurCfgRemSiteUpdate_Type.__name__ = "Integer32"
_GslbCurCfgRemSiteUpdate_Object = MibTableColumn
gslbCurCfgRemSiteUpdate = _GslbCurCfgRemSiteUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 5),
    _GslbCurCfgRemSiteUpdate_Type()
)
gslbCurCfgRemSiteUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteUpdate.setStatus("mandatory")
_GslbNewCfgRemSiteTable_Object = MibTable
gslbNewCfgRemSiteTable = _GslbNewCfgRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteTable.setStatus("mandatory")
_GslbNewCfgRemSiteTableEntry_Object = MibTableRow
gslbNewCfgRemSiteTableEntry = _GslbNewCfgRemSiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1)
)
gslbNewCfgRemSiteTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "gslbNewCfgRemSiteIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteTableEntry.setStatus("mandatory")
_GslbNewCfgRemSiteIndx_Type = Integer32
_GslbNewCfgRemSiteIndx_Object = MibTableColumn
gslbNewCfgRemSiteIndx = _GslbNewCfgRemSiteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 1),
    _GslbNewCfgRemSiteIndx_Type()
)
gslbNewCfgRemSiteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteIndx.setStatus("mandatory")
_GslbNewCfgRemSitePrimaryIp_Type = IpAddress
_GslbNewCfgRemSitePrimaryIp_Object = MibTableColumn
gslbNewCfgRemSitePrimaryIp = _GslbNewCfgRemSitePrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 2),
    _GslbNewCfgRemSitePrimaryIp_Type()
)
gslbNewCfgRemSitePrimaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSitePrimaryIp.setStatus("mandatory")
_GslbNewCfgRemSiteSecondaryIp_Type = IpAddress
_GslbNewCfgRemSiteSecondaryIp_Object = MibTableColumn
gslbNewCfgRemSiteSecondaryIp = _GslbNewCfgRemSiteSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 3),
    _GslbNewCfgRemSiteSecondaryIp_Type()
)
gslbNewCfgRemSiteSecondaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteSecondaryIp.setStatus("mandatory")


class _GslbNewCfgRemSiteState_Type(Integer32):
    """Custom type gslbNewCfgRemSiteState based on Integer32"""
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


_GslbNewCfgRemSiteState_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteState_Object = MibTableColumn
gslbNewCfgRemSiteState = _GslbNewCfgRemSiteState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 4),
    _GslbNewCfgRemSiteState_Type()
)
gslbNewCfgRemSiteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteState.setStatus("mandatory")


class _GslbNewCfgRemSiteUpdate_Type(Integer32):
    """Custom type gslbNewCfgRemSiteUpdate based on Integer32"""
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


_GslbNewCfgRemSiteUpdate_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteUpdate_Object = MibTableColumn
gslbNewCfgRemSiteUpdate = _GslbNewCfgRemSiteUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 5),
    _GslbNewCfgRemSiteUpdate_Type()
)
gslbNewCfgRemSiteUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteUpdate.setStatus("mandatory")
_GslbLookup_ObjectIdentity = ObjectIdentity
gslbLookup = _GslbLookup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4)
)


class _GslbCurCfgGenLookups_Type(Integer32):
    """Custom type gslbCurCfgGenLookups based on Integer32"""
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


_GslbCurCfgGenLookups_Type.__name__ = "Integer32"
_GslbCurCfgGenLookups_Object = MibScalar
gslbCurCfgGenLookups = _GslbCurCfgGenLookups_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 1),
    _GslbCurCfgGenLookups_Type()
)
gslbCurCfgGenLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookups.setStatus("mandatory")


class _GslbNewCfgGenLookups_Type(Integer32):
    """Custom type gslbNewCfgGenLookups based on Integer32"""
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


_GslbNewCfgGenLookups_Type.__name__ = "Integer32"
_GslbNewCfgGenLookups_Object = MibScalar
gslbNewCfgGenLookups = _GslbNewCfgGenLookups_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 2),
    _GslbNewCfgGenLookups_Type()
)
gslbNewCfgGenLookups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookups.setStatus("mandatory")
_GslbCurCfgGenLookupDname_Type = DisplayString
_GslbCurCfgGenLookupDname_Object = MibScalar
gslbCurCfgGenLookupDname = _GslbCurCfgGenLookupDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 3),
    _GslbCurCfgGenLookupDname_Type()
)
gslbCurCfgGenLookupDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookupDname.setStatus("mandatory")
_GslbNewCfgGenLookupDname_Type = DisplayString
_GslbNewCfgGenLookupDname_Object = MibScalar
gslbNewCfgGenLookupDname = _GslbNewCfgGenLookupDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 4),
    _GslbNewCfgGenLookupDname_Type()
)
gslbNewCfgGenLookupDname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookupDname.setStatus("mandatory")
_GslbNetwork_ObjectIdentity = ObjectIdentity
gslbNetwork = _GslbNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5)
)
_GslbNetworkTableMaxSize_Type = Integer32
_GslbNetworkTableMaxSize_Object = MibScalar
gslbNetworkTableMaxSize = _GslbNetworkTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 1),
    _GslbNetworkTableMaxSize_Type()
)
gslbNetworkTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNetworkTableMaxSize.setStatus("mandatory")
_GslbCurCfgNetworkTable_Object = MibTable
gslbCurCfgNetworkTable = _GslbCurCfgNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2)
)
if mibBuilder.loadTexts:
    gslbCurCfgNetworkTable.setStatus("mandatory")
_GslbCurCfgNetworkTableEntry_Object = MibTableRow
gslbCurCfgNetworkTableEntry = _GslbCurCfgNetworkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1)
)
gslbCurCfgNetworkTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "gslbCurCfgNetworkIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgNetworkTableEntry.setStatus("mandatory")
_GslbCurCfgNetworkIndx_Type = Integer32
_GslbCurCfgNetworkIndx_Object = MibTableColumn
gslbCurCfgNetworkIndx = _GslbCurCfgNetworkIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 1),
    _GslbCurCfgNetworkIndx_Type()
)
gslbCurCfgNetworkIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkIndx.setStatus("mandatory")
_GslbCurCfgNetworkSourceIp_Type = IpAddress
_GslbCurCfgNetworkSourceIp_Object = MibTableColumn
gslbCurCfgNetworkSourceIp = _GslbCurCfgNetworkSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 2),
    _GslbCurCfgNetworkSourceIp_Type()
)
gslbCurCfgNetworkSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkSourceIp.setStatus("mandatory")
_GslbCurCfgNetworkNetMask_Type = IpAddress
_GslbCurCfgNetworkNetMask_Object = MibTableColumn
gslbCurCfgNetworkNetMask = _GslbCurCfgNetworkNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 3),
    _GslbCurCfgNetworkNetMask_Type()
)
gslbCurCfgNetworkNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkNetMask.setStatus("mandatory")
_GslbCurCfgNetworkVip1_Type = IpAddress
_GslbCurCfgNetworkVip1_Object = MibTableColumn
gslbCurCfgNetworkVip1 = _GslbCurCfgNetworkVip1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 4),
    _GslbCurCfgNetworkVip1_Type()
)
gslbCurCfgNetworkVip1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkVip1.setStatus("mandatory")
_GslbCurCfgNetworkVip2_Type = IpAddress
_GslbCurCfgNetworkVip2_Object = MibTableColumn
gslbCurCfgNetworkVip2 = _GslbCurCfgNetworkVip2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 5),
    _GslbCurCfgNetworkVip2_Type()
)
gslbCurCfgNetworkVip2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkVip2.setStatus("mandatory")
_GslbNewCfgNetworkTable_Object = MibTable
gslbNewCfgNetworkTable = _GslbNewCfgNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3)
)
if mibBuilder.loadTexts:
    gslbNewCfgNetworkTable.setStatus("mandatory")
_GslbNewCfgNetworkTableEntry_Object = MibTableRow
gslbNewCfgNetworkTableEntry = _GslbNewCfgNetworkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1)
)
gslbNewCfgNetworkTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "gslbNewCfgNetworkIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgNetworkTableEntry.setStatus("mandatory")
_GslbNewCfgNetworkIndx_Type = Integer32
_GslbNewCfgNetworkIndx_Object = MibTableColumn
gslbNewCfgNetworkIndx = _GslbNewCfgNetworkIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 1),
    _GslbNewCfgNetworkIndx_Type()
)
gslbNewCfgNetworkIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkIndx.setStatus("mandatory")
_GslbNewCfgNetworkSourceIp_Type = IpAddress
_GslbNewCfgNetworkSourceIp_Object = MibTableColumn
gslbNewCfgNetworkSourceIp = _GslbNewCfgNetworkSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 2),
    _GslbNewCfgNetworkSourceIp_Type()
)
gslbNewCfgNetworkSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkSourceIp.setStatus("mandatory")
_GslbNewCfgNetworkNetMask_Type = IpAddress
_GslbNewCfgNetworkNetMask_Object = MibTableColumn
gslbNewCfgNetworkNetMask = _GslbNewCfgNetworkNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 3),
    _GslbNewCfgNetworkNetMask_Type()
)
gslbNewCfgNetworkNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkNetMask.setStatus("mandatory")
_GslbNewCfgNetworkVip1_Type = IpAddress
_GslbNewCfgNetworkVip1_Object = MibTableColumn
gslbNewCfgNetworkVip1 = _GslbNewCfgNetworkVip1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 4),
    _GslbNewCfgNetworkVip1_Type()
)
gslbNewCfgNetworkVip1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkVip1.setStatus("mandatory")
_GslbNewCfgNetworkVip2_Type = IpAddress
_GslbNewCfgNetworkVip2_Object = MibTableColumn
gslbNewCfgNetworkVip2 = _GslbNewCfgNetworkVip2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 5),
    _GslbNewCfgNetworkVip2_Type()
)
gslbNewCfgNetworkVip2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkVip2.setStatus("mandatory")


class _GslbNewCfgNetworkDelete_Type(Integer32):
    """Custom type gslbNewCfgNetworkDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_GslbNewCfgNetworkDelete_Type.__name__ = "Integer32"
_GslbNewCfgNetworkDelete_Object = MibTableColumn
gslbNewCfgNetworkDelete = _GslbNewCfgNetworkDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 12),
    _GslbNewCfgNetworkDelete_Type()
)
gslbNewCfgNetworkDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkDelete.setStatus("mandatory")


class _GslbCurCfgGenExternal_Type(Integer32):
    """Custom type gslbCurCfgGenExternal based on Integer32"""
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


_GslbCurCfgGenExternal_Type.__name__ = "Integer32"
_GslbCurCfgGenExternal_Object = MibScalar
gslbCurCfgGenExternal = _GslbCurCfgGenExternal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 6),
    _GslbCurCfgGenExternal_Type()
)
gslbCurCfgGenExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenExternal.setStatus("mandatory")


class _GslbNewCfgGenExternal_Type(Integer32):
    """Custom type gslbNewCfgGenExternal based on Integer32"""
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


_GslbNewCfgGenExternal_Type.__name__ = "Integer32"
_GslbNewCfgGenExternal_Object = MibScalar
gslbNewCfgGenExternal = _GslbNewCfgGenExternal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 7),
    _GslbNewCfgGenExternal_Type()
)
gslbNewCfgGenExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenExternal.setStatus("mandatory")
_GslbCurCfgGenEip_Type = IpAddress
_GslbCurCfgGenEip_Object = MibScalar
gslbCurCfgGenEip = _GslbCurCfgGenEip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 8),
    _GslbCurCfgGenEip_Type()
)
gslbCurCfgGenEip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenEip.setStatus("mandatory")
_GslbNewCfgGenEip_Type = IpAddress
_GslbNewCfgGenEip_Object = MibScalar
gslbNewCfgGenEip = _GslbNewCfgGenEip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 9),
    _GslbNewCfgGenEip_Type()
)
gslbNewCfgGenEip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenEip.setStatus("mandatory")


class _GslbCurCfgGenLookupPort_Type(Integer32):
    """Custom type gslbCurCfgGenLookupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8100, 9999),
    )


_GslbCurCfgGenLookupPort_Type.__name__ = "Integer32"
_GslbCurCfgGenLookupPort_Object = MibScalar
gslbCurCfgGenLookupPort = _GslbCurCfgGenLookupPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 10),
    _GslbCurCfgGenLookupPort_Type()
)
gslbCurCfgGenLookupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookupPort.setStatus("mandatory")


class _GslbNewCfgGenLookupPort_Type(Integer32):
    """Custom type gslbNewCfgGenLookupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8100, 9999),
    )


_GslbNewCfgGenLookupPort_Type.__name__ = "Integer32"
_GslbNewCfgGenLookupPort_Object = MibScalar
gslbNewCfgGenLookupPort = _GslbNewCfgGenLookupPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 11),
    _GslbNewCfgGenLookupPort_Type()
)
gslbNewCfgGenLookupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookupPort.setStatus("mandatory")


class _GslbCurCfgGenLookupTimeout_Type(Integer32):
    """Custom type gslbCurCfgGenLookupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GslbCurCfgGenLookupTimeout_Type.__name__ = "Integer32"
_GslbCurCfgGenLookupTimeout_Object = MibScalar
gslbCurCfgGenLookupTimeout = _GslbCurCfgGenLookupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 12),
    _GslbCurCfgGenLookupTimeout_Type()
)
gslbCurCfgGenLookupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookupTimeout.setStatus("mandatory")


class _GslbNewCfgGenLookupTimeout_Type(Integer32):
    """Custom type gslbNewCfgGenLookupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GslbNewCfgGenLookupTimeout_Type.__name__ = "Integer32"
_GslbNewCfgGenLookupTimeout_Object = MibScalar
gslbNewCfgGenLookupTimeout = _GslbNewCfgGenLookupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 13),
    _GslbNewCfgGenLookupTimeout_Type()
)
gslbNewCfgGenLookupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookupTimeout.setStatus("mandatory")
_DynamicSLB_ObjectIdentity = ObjectIdentity
dynamicSLB = _DynamicSLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12)
)
_DynSLBRealServerTable_Object = MibTable
dynSLBRealServerTable = _DynSLBRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    dynSLBRealServerTable.setStatus("mandatory")
_DynSLBRealServerEntry_Object = MibTableRow
dynSLBRealServerEntry = _DynSLBRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1)
)
dynSLBRealServerEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "dynSLBRealServerIpAddr"),
    (0, "ALTEON-PRIVATE-MIBS", "dynSLBRealServerPortNum"),
)
if mibBuilder.loadTexts:
    dynSLBRealServerEntry.setStatus("mandatory")
_DynSLBRealServerIpAddr_Type = IpAddress
_DynSLBRealServerIpAddr_Object = MibTableColumn
dynSLBRealServerIpAddr = _DynSLBRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1, 1),
    _DynSLBRealServerIpAddr_Type()
)
dynSLBRealServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynSLBRealServerIpAddr.setStatus("mandatory")
_DynSLBRealServerPortNum_Type = Integer32
_DynSLBRealServerPortNum_Object = MibTableColumn
dynSLBRealServerPortNum = _DynSLBRealServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1, 2),
    _DynSLBRealServerPortNum_Type()
)
dynSLBRealServerPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynSLBRealServerPortNum.setStatus("mandatory")
_DynSLBRealServerWeight_Type = Integer32
_DynSLBRealServerWeight_Object = MibTableColumn
dynSLBRealServerWeight = _DynSLBRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1, 3),
    _DynSLBRealServerWeight_Type()
)
dynSLBRealServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynSLBRealServerWeight.setStatus("mandatory")
_AltswitchTraps_ObjectIdentity = ObjectIdentity
altswitchTraps = _AltswitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13)
)
_OperCmds_ObjectIdentity = ObjectIdentity
operCmds = _OperCmds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14)
)
_OperSlbPortTable_Object = MibTable
operSlbPortTable = _OperSlbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    operSlbPortTable.setStatus("mandatory")
_OperSlbPortEntry_Object = MibTableRow
operSlbPortEntry = _OperSlbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1, 1)
)
operSlbPortEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "operSlbPortIndex"),
)
if mibBuilder.loadTexts:
    operSlbPortEntry.setStatus("mandatory")
_OperSlbPortIndex_Type = Integer32
_OperSlbPortIndex_Object = MibTableColumn
operSlbPortIndex = _OperSlbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1, 1, 1),
    _OperSlbPortIndex_Type()
)
operSlbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operSlbPortIndex.setStatus("mandatory")


class _OperSlbPortClrSessionTab_Type(Integer32):
    """Custom type operSlbPortClrSessionTab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_OperSlbPortClrSessionTab_Type.__name__ = "Integer32"
_OperSlbPortClrSessionTab_Object = MibTableColumn
operSlbPortClrSessionTab = _OperSlbPortClrSessionTab_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1, 1, 2),
    _OperSlbPortClrSessionTab_Type()
)
operSlbPortClrSessionTab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operSlbPortClrSessionTab.setStatus("mandatory")
_Vrrp_ObjectIdentity = ObjectIdentity
vrrp = _Vrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15)
)
_VrrpGeneral_ObjectIdentity = ObjectIdentity
vrrpGeneral = _VrrpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1)
)


class _VrrpCurCfgGenState_Type(Integer32):
    """Custom type vrrpCurCfgGenState based on Integer32"""
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


_VrrpCurCfgGenState_Type.__name__ = "Integer32"
_VrrpCurCfgGenState_Object = MibScalar
vrrpCurCfgGenState = _VrrpCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 1),
    _VrrpCurCfgGenState_Type()
)
vrrpCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenState.setStatus("mandatory")


class _VrrpNewCfgGenState_Type(Integer32):
    """Custom type vrrpNewCfgGenState based on Integer32"""
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


_VrrpNewCfgGenState_Type.__name__ = "Integer32"
_VrrpNewCfgGenState_Object = MibScalar
vrrpNewCfgGenState = _VrrpNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 2),
    _VrrpNewCfgGenState_Type()
)
vrrpNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenState.setStatus("mandatory")


class _VrrpCurCfgGenTckVirtRtrInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckVirtRtrInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckVirtRtrInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckVirtRtrInc_Object = MibScalar
vrrpCurCfgGenTckVirtRtrInc = _VrrpCurCfgGenTckVirtRtrInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 3),
    _VrrpCurCfgGenTckVirtRtrInc_Type()
)
vrrpCurCfgGenTckVirtRtrInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckVirtRtrInc.setStatus("mandatory")


class _VrrpNewCfgGenTckVirtRtrInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckVirtRtrInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckVirtRtrInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckVirtRtrInc_Object = MibScalar
vrrpNewCfgGenTckVirtRtrInc = _VrrpNewCfgGenTckVirtRtrInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 4),
    _VrrpNewCfgGenTckVirtRtrInc_Type()
)
vrrpNewCfgGenTckVirtRtrInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckVirtRtrInc.setStatus("mandatory")


class _VrrpCurCfgGenTckIpIntfInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckIpIntfInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckIpIntfInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckIpIntfInc_Object = MibScalar
vrrpCurCfgGenTckIpIntfInc = _VrrpCurCfgGenTckIpIntfInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 5),
    _VrrpCurCfgGenTckIpIntfInc_Type()
)
vrrpCurCfgGenTckIpIntfInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckIpIntfInc.setStatus("mandatory")


class _VrrpNewCfgGenTckIpIntfInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckIpIntfInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckIpIntfInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckIpIntfInc_Object = MibScalar
vrrpNewCfgGenTckIpIntfInc = _VrrpNewCfgGenTckIpIntfInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 6),
    _VrrpNewCfgGenTckIpIntfInc_Type()
)
vrrpNewCfgGenTckIpIntfInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckIpIntfInc.setStatus("mandatory")


class _VrrpCurCfgGenTckVlanPortInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckVlanPortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckVlanPortInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckVlanPortInc_Object = MibScalar
vrrpCurCfgGenTckVlanPortInc = _VrrpCurCfgGenTckVlanPortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 7),
    _VrrpCurCfgGenTckVlanPortInc_Type()
)
vrrpCurCfgGenTckVlanPortInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckVlanPortInc.setStatus("mandatory")


class _VrrpNewCfgGenTckVlanPortInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckVlanPortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckVlanPortInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckVlanPortInc_Object = MibScalar
vrrpNewCfgGenTckVlanPortInc = _VrrpNewCfgGenTckVlanPortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 8),
    _VrrpNewCfgGenTckVlanPortInc_Type()
)
vrrpNewCfgGenTckVlanPortInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckVlanPortInc.setStatus("mandatory")


class _VrrpCurCfgGenTckL4PortInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckL4PortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckL4PortInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckL4PortInc_Object = MibScalar
vrrpCurCfgGenTckL4PortInc = _VrrpCurCfgGenTckL4PortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 9),
    _VrrpCurCfgGenTckL4PortInc_Type()
)
vrrpCurCfgGenTckL4PortInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckL4PortInc.setStatus("mandatory")


class _VrrpNewCfgGenTckL4PortInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckL4PortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckL4PortInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckL4PortInc_Object = MibScalar
vrrpNewCfgGenTckL4PortInc = _VrrpNewCfgGenTckL4PortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 10),
    _VrrpNewCfgGenTckL4PortInc_Type()
)
vrrpNewCfgGenTckL4PortInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckL4PortInc.setStatus("mandatory")


class _VrrpCurCfgGenTckRServerInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckRServerInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckRServerInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckRServerInc_Object = MibScalar
vrrpCurCfgGenTckRServerInc = _VrrpCurCfgGenTckRServerInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 11),
    _VrrpCurCfgGenTckRServerInc_Type()
)
vrrpCurCfgGenTckRServerInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckRServerInc.setStatus("mandatory")


class _VrrpNewCfgGenTckRServerInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckRServerInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckRServerInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckRServerInc_Object = MibScalar
vrrpNewCfgGenTckRServerInc = _VrrpNewCfgGenTckRServerInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 12),
    _VrrpNewCfgGenTckRServerInc_Type()
)
vrrpNewCfgGenTckRServerInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckRServerInc.setStatus("mandatory")


class _VrrpCurCfgGenTckHsrpInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckHsrpInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckHsrpInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckHsrpInc_Object = MibScalar
vrrpCurCfgGenTckHsrpInc = _VrrpCurCfgGenTckHsrpInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 13),
    _VrrpCurCfgGenTckHsrpInc_Type()
)
vrrpCurCfgGenTckHsrpInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckHsrpInc.setStatus("mandatory")


class _VrrpNewCfgGenTckHsrpInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckHsrpInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckHsrpInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckHsrpInc_Object = MibScalar
vrrpNewCfgGenTckHsrpInc = _VrrpNewCfgGenTckHsrpInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 14),
    _VrrpNewCfgGenTckHsrpInc_Type()
)
vrrpNewCfgGenTckHsrpInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckHsrpInc.setStatus("mandatory")


class _VrrpCurCfgGenHotstandby_Type(Integer32):
    """Custom type vrrpCurCfgGenHotstandby based on Integer32"""
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


_VrrpCurCfgGenHotstandby_Type.__name__ = "Integer32"
_VrrpCurCfgGenHotstandby_Object = MibScalar
vrrpCurCfgGenHotstandby = _VrrpCurCfgGenHotstandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 15),
    _VrrpCurCfgGenHotstandby_Type()
)
vrrpCurCfgGenHotstandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenHotstandby.setStatus("mandatory")


class _VrrpNewCfgGenHotstandby_Type(Integer32):
    """Custom type vrrpNewCfgGenHotstandby based on Integer32"""
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


_VrrpNewCfgGenHotstandby_Type.__name__ = "Integer32"
_VrrpNewCfgGenHotstandby_Object = MibScalar
vrrpNewCfgGenHotstandby = _VrrpNewCfgGenHotstandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 16),
    _VrrpNewCfgGenHotstandby_Type()
)
vrrpNewCfgGenHotstandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenHotstandby.setStatus("mandatory")
_VrrpCurCfgVirtRtrTable_Object = MibTable
vrrpCurCfgVirtRtrTable = _VrrpCurCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTable.setStatus("mandatory")
_VrrpCurCfgVirtRtrTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrTableEntry = _VrrpCurCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1)
)
vrrpCurCfgVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vrrpCurCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTableEntry.setStatus("mandatory")
_VrrpCurCfgVirtRtrIndx_Type = Integer32
_VrrpCurCfgVirtRtrIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrIndx = _VrrpCurCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 1),
    _VrrpCurCfgVirtRtrIndx_Type()
)
vrrpCurCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIndx.setStatus("mandatory")


class _VrrpCurCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrID_Object = MibTableColumn
vrrpCurCfgVirtRtrID = _VrrpCurCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 2),
    _VrrpCurCfgVirtRtrID_Type()
)
vrrpCurCfgVirtRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrID.setStatus("mandatory")
_VrrpCurCfgVirtRtrAddr_Type = IpAddress
_VrrpCurCfgVirtRtrAddr_Object = MibTableColumn
vrrpCurCfgVirtRtrAddr = _VrrpCurCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 3),
    _VrrpCurCfgVirtRtrAddr_Type()
)
vrrpCurCfgVirtRtrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrAddr.setStatus("mandatory")
_VrrpCurCfgVirtRtrIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrIfIndex = _VrrpCurCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 4),
    _VrrpCurCfgVirtRtrIfIndex_Type()
)
vrrpCurCfgVirtRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIfIndex.setStatus("mandatory")


class _VrrpCurCfgVirtRtrInterval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrInterval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrInterval_Object = MibTableColumn
vrrpCurCfgVirtRtrInterval = _VrrpCurCfgVirtRtrInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 5),
    _VrrpCurCfgVirtRtrInterval_Type()
)
vrrpCurCfgVirtRtrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrInterval.setStatus("mandatory")


class _VrrpCurCfgVirtRtrPriority_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpCurCfgVirtRtrPriority_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrPriority_Object = MibTableColumn
vrrpCurCfgVirtRtrPriority = _VrrpCurCfgVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 6),
    _VrrpCurCfgVirtRtrPriority_Type()
)
vrrpCurCfgVirtRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrPriority.setStatus("mandatory")


class _VrrpCurCfgVirtRtrPreempt_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrPreempt based on Integer32"""
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


_VrrpCurCfgVirtRtrPreempt_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrPreempt_Object = MibTableColumn
vrrpCurCfgVirtRtrPreempt = _VrrpCurCfgVirtRtrPreempt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 7),
    _VrrpCurCfgVirtRtrPreempt_Type()
)
vrrpCurCfgVirtRtrPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrPreempt.setStatus("mandatory")


class _VrrpCurCfgVirtRtrState_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrState based on Integer32"""
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


_VrrpCurCfgVirtRtrState_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrState_Object = MibTableColumn
vrrpCurCfgVirtRtrState = _VrrpCurCfgVirtRtrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 8),
    _VrrpCurCfgVirtRtrState_Type()
)
vrrpCurCfgVirtRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrState.setStatus("mandatory")


class _VrrpCurCfgVirtRtrSharing_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrSharing based on Integer32"""
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


_VrrpCurCfgVirtRtrSharing_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrSharing_Object = MibTableColumn
vrrpCurCfgVirtRtrSharing = _VrrpCurCfgVirtRtrSharing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 9),
    _VrrpCurCfgVirtRtrSharing_Type()
)
vrrpCurCfgVirtRtrSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrSharing.setStatus("mandatory")


class _VrrpCurCfgVirtRtrTckVirtRtr_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckVirtRtr based on Integer32"""
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


_VrrpCurCfgVirtRtrTckVirtRtr_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckVirtRtr_Object = MibTableColumn
vrrpCurCfgVirtRtrTckVirtRtr = _VrrpCurCfgVirtRtrTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 10),
    _VrrpCurCfgVirtRtrTckVirtRtr_Type()
)
vrrpCurCfgVirtRtrTckVirtRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckVirtRtr.setStatus("mandatory")


class _VrrpCurCfgVirtRtrTckIpIntf_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckIpIntf based on Integer32"""
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


_VrrpCurCfgVirtRtrTckIpIntf_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckIpIntf_Object = MibTableColumn
vrrpCurCfgVirtRtrTckIpIntf = _VrrpCurCfgVirtRtrTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 11),
    _VrrpCurCfgVirtRtrTckIpIntf_Type()
)
vrrpCurCfgVirtRtrTckIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckIpIntf.setStatus("mandatory")


class _VrrpCurCfgVirtRtrTckVlanPort_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckVlanPort based on Integer32"""
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


_VrrpCurCfgVirtRtrTckVlanPort_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckVlanPort_Object = MibTableColumn
vrrpCurCfgVirtRtrTckVlanPort = _VrrpCurCfgVirtRtrTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 12),
    _VrrpCurCfgVirtRtrTckVlanPort_Type()
)
vrrpCurCfgVirtRtrTckVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckVlanPort.setStatus("mandatory")


class _VrrpCurCfgVirtRtrTckL4Port_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckL4Port based on Integer32"""
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


_VrrpCurCfgVirtRtrTckL4Port_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckL4Port_Object = MibTableColumn
vrrpCurCfgVirtRtrTckL4Port = _VrrpCurCfgVirtRtrTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 13),
    _VrrpCurCfgVirtRtrTckL4Port_Type()
)
vrrpCurCfgVirtRtrTckL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckL4Port.setStatus("mandatory")


class _VrrpCurCfgVirtRtrTckRServer_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckRServer based on Integer32"""
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


_VrrpCurCfgVirtRtrTckRServer_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckRServer_Object = MibTableColumn
vrrpCurCfgVirtRtrTckRServer = _VrrpCurCfgVirtRtrTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 14),
    _VrrpCurCfgVirtRtrTckRServer_Type()
)
vrrpCurCfgVirtRtrTckRServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckRServer.setStatus("mandatory")


class _VrrpCurCfgVirtRtrTckHsrp_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckHsrp based on Integer32"""
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


_VrrpCurCfgVirtRtrTckHsrp_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckHsrp_Object = MibTableColumn
vrrpCurCfgVirtRtrTckHsrp = _VrrpCurCfgVirtRtrTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 15),
    _VrrpCurCfgVirtRtrTckHsrp_Type()
)
vrrpCurCfgVirtRtrTckHsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckHsrp.setStatus("mandatory")
_VrrpNewCfgVirtRtrTable_Object = MibTable
vrrpNewCfgVirtRtrTable = _VrrpNewCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTable.setStatus("mandatory")
_VrrpNewCfgVirtRtrTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrTableEntry = _VrrpNewCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1)
)
vrrpNewCfgVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vrrpNewCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTableEntry.setStatus("mandatory")
_VrrpNewCfgVirtRtrIndx_Type = Integer32
_VrrpNewCfgVirtRtrIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrIndx = _VrrpNewCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 1),
    _VrrpNewCfgVirtRtrIndx_Type()
)
vrrpNewCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIndx.setStatus("mandatory")


class _VrrpNewCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrID_Object = MibTableColumn
vrrpNewCfgVirtRtrID = _VrrpNewCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 2),
    _VrrpNewCfgVirtRtrID_Type()
)
vrrpNewCfgVirtRtrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrID.setStatus("mandatory")
_VrrpNewCfgVirtRtrAddr_Type = IpAddress
_VrrpNewCfgVirtRtrAddr_Object = MibTableColumn
vrrpNewCfgVirtRtrAddr = _VrrpNewCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 3),
    _VrrpNewCfgVirtRtrAddr_Type()
)
vrrpNewCfgVirtRtrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrAddr.setStatus("mandatory")
_VrrpNewCfgVirtRtrIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrIfIndex = _VrrpNewCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 4),
    _VrrpNewCfgVirtRtrIfIndex_Type()
)
vrrpNewCfgVirtRtrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIfIndex.setStatus("mandatory")


class _VrrpNewCfgVirtRtrInterval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrInterval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrInterval_Object = MibTableColumn
vrrpNewCfgVirtRtrInterval = _VrrpNewCfgVirtRtrInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 5),
    _VrrpNewCfgVirtRtrInterval_Type()
)
vrrpNewCfgVirtRtrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrInterval.setStatus("mandatory")


class _VrrpNewCfgVirtRtrPriority_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpNewCfgVirtRtrPriority_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrPriority_Object = MibTableColumn
vrrpNewCfgVirtRtrPriority = _VrrpNewCfgVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 6),
    _VrrpNewCfgVirtRtrPriority_Type()
)
vrrpNewCfgVirtRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrPriority.setStatus("mandatory")


class _VrrpNewCfgVirtRtrPreempt_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrPreempt based on Integer32"""
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


_VrrpNewCfgVirtRtrPreempt_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrPreempt_Object = MibTableColumn
vrrpNewCfgVirtRtrPreempt = _VrrpNewCfgVirtRtrPreempt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 7),
    _VrrpNewCfgVirtRtrPreempt_Type()
)
vrrpNewCfgVirtRtrPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrPreempt.setStatus("mandatory")


class _VrrpNewCfgVirtRtrState_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrState based on Integer32"""
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


_VrrpNewCfgVirtRtrState_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrState_Object = MibTableColumn
vrrpNewCfgVirtRtrState = _VrrpNewCfgVirtRtrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 8),
    _VrrpNewCfgVirtRtrState_Type()
)
vrrpNewCfgVirtRtrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrState.setStatus("mandatory")


class _VrrpNewCfgVirtRtrDelete_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_VrrpNewCfgVirtRtrDelete_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrDelete_Object = MibTableColumn
vrrpNewCfgVirtRtrDelete = _VrrpNewCfgVirtRtrDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 9),
    _VrrpNewCfgVirtRtrDelete_Type()
)
vrrpNewCfgVirtRtrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrDelete.setStatus("mandatory")


class _VrrpNewCfgVirtRtrSharing_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrSharing based on Integer32"""
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


_VrrpNewCfgVirtRtrSharing_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrSharing_Object = MibTableColumn
vrrpNewCfgVirtRtrSharing = _VrrpNewCfgVirtRtrSharing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 10),
    _VrrpNewCfgVirtRtrSharing_Type()
)
vrrpNewCfgVirtRtrSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrSharing.setStatus("mandatory")


class _VrrpNewCfgVirtRtrTckVirtRtr_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckVirtRtr based on Integer32"""
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


_VrrpNewCfgVirtRtrTckVirtRtr_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckVirtRtr_Object = MibTableColumn
vrrpNewCfgVirtRtrTckVirtRtr = _VrrpNewCfgVirtRtrTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 11),
    _VrrpNewCfgVirtRtrTckVirtRtr_Type()
)
vrrpNewCfgVirtRtrTckVirtRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckVirtRtr.setStatus("mandatory")


class _VrrpNewCfgVirtRtrTckIpIntf_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckIpIntf based on Integer32"""
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


_VrrpNewCfgVirtRtrTckIpIntf_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckIpIntf_Object = MibTableColumn
vrrpNewCfgVirtRtrTckIpIntf = _VrrpNewCfgVirtRtrTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 12),
    _VrrpNewCfgVirtRtrTckIpIntf_Type()
)
vrrpNewCfgVirtRtrTckIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckIpIntf.setStatus("mandatory")


class _VrrpNewCfgVirtRtrTckVlanPort_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckVlanPort based on Integer32"""
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


_VrrpNewCfgVirtRtrTckVlanPort_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckVlanPort_Object = MibTableColumn
vrrpNewCfgVirtRtrTckVlanPort = _VrrpNewCfgVirtRtrTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 13),
    _VrrpNewCfgVirtRtrTckVlanPort_Type()
)
vrrpNewCfgVirtRtrTckVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckVlanPort.setStatus("mandatory")


class _VrrpNewCfgVirtRtrTckL4Port_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckL4Port based on Integer32"""
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


_VrrpNewCfgVirtRtrTckL4Port_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckL4Port_Object = MibTableColumn
vrrpNewCfgVirtRtrTckL4Port = _VrrpNewCfgVirtRtrTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 14),
    _VrrpNewCfgVirtRtrTckL4Port_Type()
)
vrrpNewCfgVirtRtrTckL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckL4Port.setStatus("mandatory")


class _VrrpNewCfgVirtRtrTckRServer_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckRServer based on Integer32"""
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


_VrrpNewCfgVirtRtrTckRServer_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckRServer_Object = MibTableColumn
vrrpNewCfgVirtRtrTckRServer = _VrrpNewCfgVirtRtrTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 15),
    _VrrpNewCfgVirtRtrTckRServer_Type()
)
vrrpNewCfgVirtRtrTckRServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckRServer.setStatus("mandatory")


class _VrrpNewCfgVirtRtrTckHsrp_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckHsrp based on Integer32"""
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


_VrrpNewCfgVirtRtrTckHsrp_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckHsrp_Object = MibTableColumn
vrrpNewCfgVirtRtrTckHsrp = _VrrpNewCfgVirtRtrTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 16),
    _VrrpNewCfgVirtRtrTckHsrp_Type()
)
vrrpNewCfgVirtRtrTckHsrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckHsrp.setStatus("mandatory")
_VrrpCurCfgIfTable_Object = MibTable
vrrpCurCfgIfTable = _VrrpCurCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4)
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTable.setStatus("mandatory")
_VrrpCurCfgIfTableEntry_Object = MibTableRow
vrrpCurCfgIfTableEntry = _VrrpCurCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1)
)
vrrpCurCfgIfTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vrrpCurCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTableEntry.setStatus("mandatory")
_VrrpCurCfgIfIndx_Type = Integer32
_VrrpCurCfgIfIndx_Object = MibTableColumn
vrrpCurCfgIfIndx = _VrrpCurCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1, 1),
    _VrrpCurCfgIfIndx_Type()
)
vrrpCurCfgIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfIndx.setStatus("mandatory")


class _VrrpCurCfgIfAuthType_Type(Integer32):
    """Custom type vrrpCurCfgIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple-text-password", 2))
    )


_VrrpCurCfgIfAuthType_Type.__name__ = "Integer32"
_VrrpCurCfgIfAuthType_Object = MibTableColumn
vrrpCurCfgIfAuthType = _VrrpCurCfgIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1, 2),
    _VrrpCurCfgIfAuthType_Type()
)
vrrpCurCfgIfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfAuthType.setStatus("mandatory")


class _VrrpCurCfgIfPasswd_Type(DisplayString):
    """Custom type vrrpCurCfgIfPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrrpCurCfgIfPasswd_Type.__name__ = "DisplayString"
_VrrpCurCfgIfPasswd_Object = MibTableColumn
vrrpCurCfgIfPasswd = _VrrpCurCfgIfPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1, 3),
    _VrrpCurCfgIfPasswd_Type()
)
vrrpCurCfgIfPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfPasswd.setStatus("mandatory")
_VrrpNewCfgIfTable_Object = MibTable
vrrpNewCfgIfTable = _VrrpNewCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5)
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTable.setStatus("mandatory")
_VrrpNewCfgIfTableEntry_Object = MibTableRow
vrrpNewCfgIfTableEntry = _VrrpNewCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1)
)
vrrpNewCfgIfTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vrrpNewCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTableEntry.setStatus("mandatory")
_VrrpNewCfgIfIndx_Type = Integer32
_VrrpNewCfgIfIndx_Object = MibTableColumn
vrrpNewCfgIfIndx = _VrrpNewCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 1),
    _VrrpNewCfgIfIndx_Type()
)
vrrpNewCfgIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgIfIndx.setStatus("mandatory")


class _VrrpNewCfgIfAuthType_Type(Integer32):
    """Custom type vrrpNewCfgIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple-text-password", 2))
    )


_VrrpNewCfgIfAuthType_Type.__name__ = "Integer32"
_VrrpNewCfgIfAuthType_Object = MibTableColumn
vrrpNewCfgIfAuthType = _VrrpNewCfgIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 2),
    _VrrpNewCfgIfAuthType_Type()
)
vrrpNewCfgIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgIfAuthType.setStatus("mandatory")


class _VrrpNewCfgIfPasswd_Type(DisplayString):
    """Custom type vrrpNewCfgIfPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrrpNewCfgIfPasswd_Type.__name__ = "DisplayString"
_VrrpNewCfgIfPasswd_Object = MibTableColumn
vrrpNewCfgIfPasswd = _VrrpNewCfgIfPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 3),
    _VrrpNewCfgIfPasswd_Type()
)
vrrpNewCfgIfPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgIfPasswd.setStatus("mandatory")


class _VrrpNewCfgIfDelete_Type(Integer32):
    """Custom type vrrpNewCfgIfDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_VrrpNewCfgIfDelete_Type.__name__ = "Integer32"
_VrrpNewCfgIfDelete_Object = MibTableColumn
vrrpNewCfgIfDelete = _VrrpNewCfgIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 4),
    _VrrpNewCfgIfDelete_Type()
)
vrrpNewCfgIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgIfDelete.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpTable_Object = MibTable
vrrpCurCfgVirtRtrGrpTable = _VrrpCurCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTable.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrGrpTableEntry = _VrrpCurCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1)
)
vrrpCurCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vrrpCurCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTableEntry.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpIndx_Type = Integer32
_VrrpCurCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIndx = _VrrpCurCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 1),
    _VrrpCurCfgVirtRtrGrpIndx_Type()
)
vrrpCurCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIndx.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpID_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpID = _VrrpCurCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 2),
    _VrrpCurCfgVirtRtrGrpID_Type()
)
vrrpCurCfgVirtRtrGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpID.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIfIndex = _VrrpCurCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 3),
    _VrrpCurCfgVirtRtrGrpIfIndex_Type()
)
vrrpCurCfgVirtRtrGrpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIfIndex.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpInterval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrGrpInterval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpInterval_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpInterval = _VrrpCurCfgVirtRtrGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 4),
    _VrrpCurCfgVirtRtrGrpInterval_Type()
)
vrrpCurCfgVirtRtrGrpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpInterval.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpPriority_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpCurCfgVirtRtrGrpPriority_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpPriority_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpPriority = _VrrpCurCfgVirtRtrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 5),
    _VrrpCurCfgVirtRtrGrpPriority_Type()
)
vrrpCurCfgVirtRtrGrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpPriority.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpPreempt_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpPreempt based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpPreempt_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpPreempt_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpPreempt = _VrrpCurCfgVirtRtrGrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 6),
    _VrrpCurCfgVirtRtrGrpPreempt_Type()
)
vrrpCurCfgVirtRtrGrpPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpPreempt.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpState_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpState based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpState_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpState_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpState = _VrrpCurCfgVirtRtrGrpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 7),
    _VrrpCurCfgVirtRtrGrpState_Type()
)
vrrpCurCfgVirtRtrGrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpState.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpSharing_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpSharing based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpSharing_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpSharing_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpSharing = _VrrpCurCfgVirtRtrGrpSharing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 8),
    _VrrpCurCfgVirtRtrGrpSharing_Type()
)
vrrpCurCfgVirtRtrGrpSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpSharing.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpTckVirtRtr_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckVirtRtr based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckVirtRtr_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckVirtRtr_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckVirtRtr = _VrrpCurCfgVirtRtrGrpTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 9),
    _VrrpCurCfgVirtRtrGrpTckVirtRtr_Type()
)
vrrpCurCfgVirtRtrGrpTckVirtRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckVirtRtr.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpTckIpIntf_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckIpIntf based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckIpIntf_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckIpIntf_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckIpIntf = _VrrpCurCfgVirtRtrGrpTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 10),
    _VrrpCurCfgVirtRtrGrpTckIpIntf_Type()
)
vrrpCurCfgVirtRtrGrpTckIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckIpIntf.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpTckVlanPort_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckVlanPort based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckVlanPort_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckVlanPort_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckVlanPort = _VrrpCurCfgVirtRtrGrpTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 11),
    _VrrpCurCfgVirtRtrGrpTckVlanPort_Type()
)
vrrpCurCfgVirtRtrGrpTckVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckVlanPort.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpTckL4Port_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckL4Port based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckL4Port_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckL4Port_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckL4Port = _VrrpCurCfgVirtRtrGrpTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 12),
    _VrrpCurCfgVirtRtrGrpTckL4Port_Type()
)
vrrpCurCfgVirtRtrGrpTckL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckL4Port.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpTckRServer_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckRServer based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckRServer_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckRServer_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckRServer = _VrrpCurCfgVirtRtrGrpTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 13),
    _VrrpCurCfgVirtRtrGrpTckRServer_Type()
)
vrrpCurCfgVirtRtrGrpTckRServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckRServer.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpTckHsrp_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckHsrp based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckHsrp_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckHsrp_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckHsrp = _VrrpCurCfgVirtRtrGrpTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 14),
    _VrrpCurCfgVirtRtrGrpTckHsrp_Type()
)
vrrpCurCfgVirtRtrGrpTckHsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckHsrp.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpTable_Object = MibTable
vrrpNewCfgVirtRtrGrpTable = _VrrpNewCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTable.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrGrpTableEntry = _VrrpNewCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1)
)
vrrpNewCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "vrrpNewCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTableEntry.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpIndx_Type = Integer32
_VrrpNewCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIndx = _VrrpNewCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 1),
    _VrrpNewCfgVirtRtrGrpIndx_Type()
)
vrrpNewCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIndx.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpID_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpID = _VrrpNewCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 2),
    _VrrpNewCfgVirtRtrGrpID_Type()
)
vrrpNewCfgVirtRtrGrpID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpID.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIfIndex = _VrrpNewCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 3),
    _VrrpNewCfgVirtRtrGrpIfIndex_Type()
)
vrrpNewCfgVirtRtrGrpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIfIndex.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpInterval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrGrpInterval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpInterval_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpInterval = _VrrpNewCfgVirtRtrGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 4),
    _VrrpNewCfgVirtRtrGrpInterval_Type()
)
vrrpNewCfgVirtRtrGrpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpInterval.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpPriority_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpNewCfgVirtRtrGrpPriority_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpPriority_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpPriority = _VrrpNewCfgVirtRtrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 5),
    _VrrpNewCfgVirtRtrGrpPriority_Type()
)
vrrpNewCfgVirtRtrGrpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpPriority.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpPreempt_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpPreempt based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpPreempt_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpPreempt_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpPreempt = _VrrpNewCfgVirtRtrGrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 6),
    _VrrpNewCfgVirtRtrGrpPreempt_Type()
)
vrrpNewCfgVirtRtrGrpPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpPreempt.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpState_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpState based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpState_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpState_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpState = _VrrpNewCfgVirtRtrGrpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 7),
    _VrrpNewCfgVirtRtrGrpState_Type()
)
vrrpNewCfgVirtRtrGrpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpState.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpDelete_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_VrrpNewCfgVirtRtrGrpDelete_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpDelete_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpDelete = _VrrpNewCfgVirtRtrGrpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 8),
    _VrrpNewCfgVirtRtrGrpDelete_Type()
)
vrrpNewCfgVirtRtrGrpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpDelete.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpSharing_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpSharing based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpSharing_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpSharing_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpSharing = _VrrpNewCfgVirtRtrGrpSharing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 9),
    _VrrpNewCfgVirtRtrGrpSharing_Type()
)
vrrpNewCfgVirtRtrGrpSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpSharing.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpTckVirtRtr_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckVirtRtr based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckVirtRtr_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckVirtRtr_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckVirtRtr = _VrrpNewCfgVirtRtrGrpTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 10),
    _VrrpNewCfgVirtRtrGrpTckVirtRtr_Type()
)
vrrpNewCfgVirtRtrGrpTckVirtRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckVirtRtr.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpTckIpIntf_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckIpIntf based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckIpIntf_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckIpIntf_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckIpIntf = _VrrpNewCfgVirtRtrGrpTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 11),
    _VrrpNewCfgVirtRtrGrpTckIpIntf_Type()
)
vrrpNewCfgVirtRtrGrpTckIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckIpIntf.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpTckVlanPort_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckVlanPort based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckVlanPort_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckVlanPort_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckVlanPort = _VrrpNewCfgVirtRtrGrpTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 12),
    _VrrpNewCfgVirtRtrGrpTckVlanPort_Type()
)
vrrpNewCfgVirtRtrGrpTckVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckVlanPort.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpTckL4Port_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckL4Port based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckL4Port_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckL4Port_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckL4Port = _VrrpNewCfgVirtRtrGrpTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 13),
    _VrrpNewCfgVirtRtrGrpTckL4Port_Type()
)
vrrpNewCfgVirtRtrGrpTckL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckL4Port.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpTckRServer_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckRServer based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckRServer_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckRServer_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckRServer = _VrrpNewCfgVirtRtrGrpTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 14),
    _VrrpNewCfgVirtRtrGrpTckRServer_Type()
)
vrrpNewCfgVirtRtrGrpTckRServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckRServer.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpTckHsrp_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckHsrp based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckHsrp_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckHsrp_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckHsrp = _VrrpNewCfgVirtRtrGrpTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 15),
    _VrrpNewCfgVirtRtrGrpTckHsrp_Type()
)
vrrpNewCfgVirtRtrGrpTckHsrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckHsrp.setStatus("mandatory")
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
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
_Bwm_ObjectIdentity = ObjectIdentity
bwm = _Bwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17)
)
_BwmGeneralConfig_ObjectIdentity = ObjectIdentity
bwmGeneralConfig = _BwmGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1)
)


class _BwmCurCfgGenState_Type(Integer32):
    """Custom type bwmCurCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_BwmCurCfgGenState_Type.__name__ = "Integer32"
_BwmCurCfgGenState_Object = MibScalar
bwmCurCfgGenState = _BwmCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 1),
    _BwmCurCfgGenState_Type()
)
bwmCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenState.setStatus("mandatory")


class _BwmNewCfgGenState_Type(Integer32):
    """Custom type bwmNewCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_BwmNewCfgGenState_Type.__name__ = "Integer32"
_BwmNewCfgGenState_Object = MibScalar
bwmNewCfgGenState = _BwmNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 2),
    _BwmNewCfgGenState_Type()
)
bwmNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenState.setStatus("mandatory")


class _BwmCurCfgGenEnforcePolicy_Type(Integer32):
    """Custom type bwmCurCfgGenEnforcePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmCurCfgGenEnforcePolicy_Type.__name__ = "Integer32"
_BwmCurCfgGenEnforcePolicy_Object = MibScalar
bwmCurCfgGenEnforcePolicy = _BwmCurCfgGenEnforcePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 3),
    _BwmCurCfgGenEnforcePolicy_Type()
)
bwmCurCfgGenEnforcePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenEnforcePolicy.setStatus("mandatory")


class _BwmNewCfgGenEnforcePolicy_Type(Integer32):
    """Custom type bwmNewCfgGenEnforcePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmNewCfgGenEnforcePolicy_Type.__name__ = "Integer32"
_BwmNewCfgGenEnforcePolicy_Object = MibScalar
bwmNewCfgGenEnforcePolicy = _BwmNewCfgGenEnforcePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 4),
    _BwmNewCfgGenEnforcePolicy_Type()
)
bwmNewCfgGenEnforcePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenEnforcePolicy.setStatus("mandatory")


class _BwmCurCfgGenSmtpUser_Type(DisplayString):
    """Custom type bwmCurCfgGenSmtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BwmCurCfgGenSmtpUser_Type.__name__ = "DisplayString"
_BwmCurCfgGenSmtpUser_Object = MibScalar
bwmCurCfgGenSmtpUser = _BwmCurCfgGenSmtpUser_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 5),
    _BwmCurCfgGenSmtpUser_Type()
)
bwmCurCfgGenSmtpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenSmtpUser.setStatus("mandatory")


class _BwmNewCfgGenSmtpUser_Type(DisplayString):
    """Custom type bwmNewCfgGenSmtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BwmNewCfgGenSmtpUser_Type.__name__ = "DisplayString"
_BwmNewCfgGenSmtpUser_Object = MibScalar
bwmNewCfgGenSmtpUser = _BwmNewCfgGenSmtpUser_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 6),
    _BwmNewCfgGenSmtpUser_Type()
)
bwmNewCfgGenSmtpUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenSmtpUser.setStatus("mandatory")
_BwmPolicyConfig_ObjectIdentity = ObjectIdentity
bwmPolicyConfig = _BwmPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2)
)
_BwmPolicyTableMaxEnt_Type = Integer32
_BwmPolicyTableMaxEnt_Object = MibScalar
bwmPolicyTableMaxEnt = _BwmPolicyTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 1),
    _BwmPolicyTableMaxEnt_Type()
)
bwmPolicyTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmPolicyTableMaxEnt.setStatus("mandatory")
_BwmCurCfgPolicyTable_Object = MibTable
bwmCurCfgPolicyTable = _BwmCurCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTable.setStatus("mandatory")
_BwmCurCfgPolicyTableEntry_Object = MibTableRow
bwmCurCfgPolicyTableEntry = _BwmCurCfgPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1)
)
bwmCurCfgPolicyTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmCurCfgPolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTableEntry.setStatus("mandatory")


class _BwmCurCfgPolicyIndx_Type(Integer32):
    """Custom type bwmCurCfgPolicyIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwmCurCfgPolicyIndx_Type.__name__ = "Integer32"
_BwmCurCfgPolicyIndx_Object = MibTableColumn
bwmCurCfgPolicyIndx = _BwmCurCfgPolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 1),
    _BwmCurCfgPolicyIndx_Type()
)
bwmCurCfgPolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyIndx.setStatus("mandatory")


class _BwmCurCfgPolicyTosIn_Type(Integer32):
    """Custom type bwmCurCfgPolicyTosIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmCurCfgPolicyTosIn_Type.__name__ = "Integer32"
_BwmCurCfgPolicyTosIn_Object = MibTableColumn
bwmCurCfgPolicyTosIn = _BwmCurCfgPolicyTosIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 2),
    _BwmCurCfgPolicyTosIn_Type()
)
bwmCurCfgPolicyTosIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTosIn.setStatus("mandatory")


class _BwmCurCfgPolicyTosOut_Type(Integer32):
    """Custom type bwmCurCfgPolicyTosOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmCurCfgPolicyTosOut_Type.__name__ = "Integer32"
_BwmCurCfgPolicyTosOut_Object = MibTableColumn
bwmCurCfgPolicyTosOut = _BwmCurCfgPolicyTosOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 3),
    _BwmCurCfgPolicyTosOut_Type()
)
bwmCurCfgPolicyTosOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTosOut.setStatus("mandatory")


class _BwmCurCfgPolicyHard_Type(DisplayString):
    """Custom type bwmCurCfgPolicyHard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BwmCurCfgPolicyHard_Type.__name__ = "DisplayString"
_BwmCurCfgPolicyHard_Object = MibTableColumn
bwmCurCfgPolicyHard = _BwmCurCfgPolicyHard_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 4),
    _BwmCurCfgPolicyHard_Type()
)
bwmCurCfgPolicyHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyHard.setStatus("mandatory")


class _BwmCurCfgPolicySoft_Type(DisplayString):
    """Custom type bwmCurCfgPolicySoft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BwmCurCfgPolicySoft_Type.__name__ = "DisplayString"
_BwmCurCfgPolicySoft_Object = MibTableColumn
bwmCurCfgPolicySoft = _BwmCurCfgPolicySoft_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 5),
    _BwmCurCfgPolicySoft_Type()
)
bwmCurCfgPolicySoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicySoft.setStatus("mandatory")


class _BwmCurCfgPolicyResv_Type(DisplayString):
    """Custom type bwmCurCfgPolicyResv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BwmCurCfgPolicyResv_Type.__name__ = "DisplayString"
_BwmCurCfgPolicyResv_Object = MibTableColumn
bwmCurCfgPolicyResv = _BwmCurCfgPolicyResv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 6),
    _BwmCurCfgPolicyResv_Type()
)
bwmCurCfgPolicyResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyResv.setStatus("mandatory")


class _BwmCurCfgPolicyBuffer_Type(Integer32):
    """Custom type bwmCurCfgPolicyBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 512000),
    )


_BwmCurCfgPolicyBuffer_Type.__name__ = "Integer32"
_BwmCurCfgPolicyBuffer_Object = MibTableColumn
bwmCurCfgPolicyBuffer = _BwmCurCfgPolicyBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 7),
    _BwmCurCfgPolicyBuffer_Type()
)
bwmCurCfgPolicyBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyBuffer.setStatus("mandatory")
_BwmNewCfgPolicyTable_Object = MibTable
bwmNewCfgPolicyTable = _BwmNewCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTable.setStatus("mandatory")
_BwmNewCfgPolicyTableEntry_Object = MibTableRow
bwmNewCfgPolicyTableEntry = _BwmNewCfgPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1)
)
bwmNewCfgPolicyTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmNewCfgPolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTableEntry.setStatus("mandatory")


class _BwmNewCfgPolicyIndx_Type(Integer32):
    """Custom type bwmNewCfgPolicyIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwmNewCfgPolicyIndx_Type.__name__ = "Integer32"
_BwmNewCfgPolicyIndx_Object = MibTableColumn
bwmNewCfgPolicyIndx = _BwmNewCfgPolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 1),
    _BwmNewCfgPolicyIndx_Type()
)
bwmNewCfgPolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyIndx.setStatus("mandatory")


class _BwmNewCfgPolicyTosIn_Type(Integer32):
    """Custom type bwmNewCfgPolicyTosIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmNewCfgPolicyTosIn_Type.__name__ = "Integer32"
_BwmNewCfgPolicyTosIn_Object = MibTableColumn
bwmNewCfgPolicyTosIn = _BwmNewCfgPolicyTosIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 2),
    _BwmNewCfgPolicyTosIn_Type()
)
bwmNewCfgPolicyTosIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTosIn.setStatus("mandatory")


class _BwmNewCfgPolicyTosOut_Type(Integer32):
    """Custom type bwmNewCfgPolicyTosOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmNewCfgPolicyTosOut_Type.__name__ = "Integer32"
_BwmNewCfgPolicyTosOut_Object = MibTableColumn
bwmNewCfgPolicyTosOut = _BwmNewCfgPolicyTosOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 3),
    _BwmNewCfgPolicyTosOut_Type()
)
bwmNewCfgPolicyTosOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTosOut.setStatus("mandatory")


class _BwmNewCfgPolicyHard_Type(DisplayString):
    """Custom type bwmNewCfgPolicyHard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicyHard_Type.__name__ = "DisplayString"
_BwmNewCfgPolicyHard_Object = MibTableColumn
bwmNewCfgPolicyHard = _BwmNewCfgPolicyHard_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 4),
    _BwmNewCfgPolicyHard_Type()
)
bwmNewCfgPolicyHard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyHard.setStatus("mandatory")


class _BwmNewCfgPolicySoft_Type(DisplayString):
    """Custom type bwmNewCfgPolicySoft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicySoft_Type.__name__ = "DisplayString"
_BwmNewCfgPolicySoft_Object = MibTableColumn
bwmNewCfgPolicySoft = _BwmNewCfgPolicySoft_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 5),
    _BwmNewCfgPolicySoft_Type()
)
bwmNewCfgPolicySoft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicySoft.setStatus("mandatory")


class _BwmNewCfgPolicyResv_Type(DisplayString):
    """Custom type bwmNewCfgPolicyResv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicyResv_Type.__name__ = "DisplayString"
_BwmNewCfgPolicyResv_Object = MibTableColumn
bwmNewCfgPolicyResv = _BwmNewCfgPolicyResv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 6),
    _BwmNewCfgPolicyResv_Type()
)
bwmNewCfgPolicyResv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyResv.setStatus("mandatory")


class _BwmNewCfgPolicyBuffer_Type(Integer32):
    """Custom type bwmNewCfgPolicyBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 512000),
    )


_BwmNewCfgPolicyBuffer_Type.__name__ = "Integer32"
_BwmNewCfgPolicyBuffer_Object = MibTableColumn
bwmNewCfgPolicyBuffer = _BwmNewCfgPolicyBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 7),
    _BwmNewCfgPolicyBuffer_Type()
)
bwmNewCfgPolicyBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyBuffer.setStatus("mandatory")
_BwmContractConfig_ObjectIdentity = ObjectIdentity
bwmContractConfig = _BwmContractConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3)
)
_BwmContractTableMaxEnt_Type = Integer32
_BwmContractTableMaxEnt_Object = MibScalar
bwmContractTableMaxEnt = _BwmContractTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 1),
    _BwmContractTableMaxEnt_Type()
)
bwmContractTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContractTableMaxEnt.setStatus("mandatory")
_BwmCurCfgContractTable_Object = MibTable
bwmCurCfgContractTable = _BwmCurCfgContractTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgContractTable.setStatus("mandatory")
_BwmCurCfgContractTableEntry_Object = MibTableRow
bwmCurCfgContractTableEntry = _BwmCurCfgContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1)
)
bwmCurCfgContractTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmCurCfgContractIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgContractTableEntry.setStatus("mandatory")


class _BwmCurCfgContractIndx_Type(Integer32):
    """Custom type bwmCurCfgContractIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmCurCfgContractIndx_Type.__name__ = "Integer32"
_BwmCurCfgContractIndx_Object = MibTableColumn
bwmCurCfgContractIndx = _BwmCurCfgContractIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 1),
    _BwmCurCfgContractIndx_Type()
)
bwmCurCfgContractIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractIndx.setStatus("mandatory")


class _BwmCurCfgContractName_Type(DisplayString):
    """Custom type bwmCurCfgContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BwmCurCfgContractName_Type.__name__ = "DisplayString"
_BwmCurCfgContractName_Object = MibTableColumn
bwmCurCfgContractName = _BwmCurCfgContractName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 2),
    _BwmCurCfgContractName_Type()
)
bwmCurCfgContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractName.setStatus("mandatory")


class _BwmCurCfgContractState_Type(Integer32):
    """Custom type bwmCurCfgContractState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmCurCfgContractState_Type.__name__ = "Integer32"
_BwmCurCfgContractState_Object = MibTableColumn
bwmCurCfgContractState = _BwmCurCfgContractState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 3),
    _BwmCurCfgContractState_Type()
)
bwmCurCfgContractState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractState.setStatus("mandatory")


class _BwmCurCfgContractPolicy_Type(Integer32):
    """Custom type bwmCurCfgContractPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwmCurCfgContractPolicy_Type.__name__ = "Integer32"
_BwmCurCfgContractPolicy_Object = MibTableColumn
bwmCurCfgContractPolicy = _BwmCurCfgContractPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 4),
    _BwmCurCfgContractPolicy_Type()
)
bwmCurCfgContractPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractPolicy.setStatus("mandatory")


class _BwmCurCfgContractPrec_Type(Integer32):
    """Custom type bwmCurCfgContractPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmCurCfgContractPrec_Type.__name__ = "Integer32"
_BwmCurCfgContractPrec_Object = MibTableColumn
bwmCurCfgContractPrec = _BwmCurCfgContractPrec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 5),
    _BwmCurCfgContractPrec_Type()
)
bwmCurCfgContractPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractPrec.setStatus("mandatory")


class _BwmCurCfgContractUseTos_Type(Integer32):
    """Custom type bwmCurCfgContractUseTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmCurCfgContractUseTos_Type.__name__ = "Integer32"
_BwmCurCfgContractUseTos_Object = MibTableColumn
bwmCurCfgContractUseTos = _BwmCurCfgContractUseTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 6),
    _BwmCurCfgContractUseTos_Type()
)
bwmCurCfgContractUseTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractUseTos.setStatus("mandatory")


class _BwmCurCfgContractHistory_Type(Integer32):
    """Custom type bwmCurCfgContractHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmCurCfgContractHistory_Type.__name__ = "Integer32"
_BwmCurCfgContractHistory_Object = MibTableColumn
bwmCurCfgContractHistory = _BwmCurCfgContractHistory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 7),
    _BwmCurCfgContractHistory_Type()
)
bwmCurCfgContractHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractHistory.setStatus("mandatory")
_BwmNewCfgContractTable_Object = MibTable
bwmNewCfgContractTable = _BwmNewCfgContractTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgContractTable.setStatus("mandatory")
_BwmNewCfgContractTableEntry_Object = MibTableRow
bwmNewCfgContractTableEntry = _BwmNewCfgContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1)
)
bwmNewCfgContractTableEntry.setIndexNames(
    (0, "ALTEON-PRIVATE-MIBS", "bwmNewCfgContractIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgContractTableEntry.setStatus("mandatory")


class _BwmNewCfgContractIndx_Type(Integer32):
    """Custom type bwmNewCfgContractIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmNewCfgContractIndx_Type.__name__ = "Integer32"
_BwmNewCfgContractIndx_Object = MibTableColumn
bwmNewCfgContractIndx = _BwmNewCfgContractIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 1),
    _BwmNewCfgContractIndx_Type()
)
bwmNewCfgContractIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContractIndx.setStatus("mandatory")


class _BwmNewCfgContractName_Type(DisplayString):
    """Custom type bwmNewCfgContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BwmNewCfgContractName_Type.__name__ = "DisplayString"
_BwmNewCfgContractName_Object = MibTableColumn
bwmNewCfgContractName = _BwmNewCfgContractName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 2),
    _BwmNewCfgContractName_Type()
)
bwmNewCfgContractName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractName.setStatus("mandatory")


class _BwmNewCfgContractState_Type(Integer32):
    """Custom type bwmNewCfgContractState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmNewCfgContractState_Type.__name__ = "Integer32"
_BwmNewCfgContractState_Object = MibTableColumn
bwmNewCfgContractState = _BwmNewCfgContractState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 3),
    _BwmNewCfgContractState_Type()
)
bwmNewCfgContractState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractState.setStatus("mandatory")


class _BwmNewCfgContractPolicy_Type(Integer32):
    """Custom type bwmNewCfgContractPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwmNewCfgContractPolicy_Type.__name__ = "Integer32"
_BwmNewCfgContractPolicy_Object = MibTableColumn
bwmNewCfgContractPolicy = _BwmNewCfgContractPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 4),
    _BwmNewCfgContractPolicy_Type()
)
bwmNewCfgContractPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractPolicy.setStatus("mandatory")


class _BwmNewCfgContractDelete_Type(Integer32):
    """Custom type bwmNewCfgContractDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_BwmNewCfgContractDelete_Type.__name__ = "Integer32"
_BwmNewCfgContractDelete_Object = MibTableColumn
bwmNewCfgContractDelete = _BwmNewCfgContractDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 5),
    _BwmNewCfgContractDelete_Type()
)
bwmNewCfgContractDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractDelete.setStatus("mandatory")


class _BwmNewCfgContractPrec_Type(Integer32):
    """Custom type bwmNewCfgContractPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmNewCfgContractPrec_Type.__name__ = "Integer32"
_BwmNewCfgContractPrec_Object = MibTableColumn
bwmNewCfgContractPrec = _BwmNewCfgContractPrec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 6),
    _BwmNewCfgContractPrec_Type()
)
bwmNewCfgContractPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractPrec.setStatus("mandatory")


class _BwmNewCfgContractUseTos_Type(Integer32):
    """Custom type bwmNewCfgContractUseTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmNewCfgContractUseTos_Type.__name__ = "Integer32"
_BwmNewCfgContractUseTos_Object = MibTableColumn
bwmNewCfgContractUseTos = _BwmNewCfgContractUseTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 7),
    _BwmNewCfgContractUseTos_Type()
)
bwmNewCfgContractUseTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractUseTos.setStatus("mandatory")


class _BwmNewCfgContractHistory_Type(Integer32):
    """Custom type bwmNewCfgContractHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_BwmNewCfgContractHistory_Type.__name__ = "Integer32"
_BwmNewCfgContractHistory_Object = MibTableColumn
bwmNewCfgContractHistory = _BwmNewCfgContractHistory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 8),
    _BwmNewCfgContractHistory_Type()
)
bwmNewCfgContractHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractHistory.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-PRIVATE-MIBS",
    **{"alteon": alteon,
       "registration": registration,
       "private-mibs": private_mibs,
       "switch": switch,
       "hardware": hardware,
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
       "agEnabledSwFeatures": agEnabledSwFeatures,
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
       "agPortConfig": agPortConfig,
       "agPortTableMaxEnt": agPortTableMaxEnt,
       "agPortCurCfgTable": agPortCurCfgTable,
       "agPortCurCfgTableEntry": agPortCurCfgTableEntry,
       "agPortCurCfgIndx": agPortCurCfgIndx,
       "agPortCurCfgPrefLink": agPortCurCfgPrefLink,
       "agPortCurCfgBackLink": agPortCurCfgBackLink,
       "agPortCurCfgState": agPortCurCfgState,
       "agPortCurCfgVlanTag": agPortCurCfgVlanTag,
       "agPortCurCfgStp": agPortCurCfgStp,
       "agPortCurCfgRmon": agPortCurCfgRmon,
       "agPortCurCfgPVID": agPortCurCfgPVID,
       "agPortCurCfgFastEthAutoNeg": agPortCurCfgFastEthAutoNeg,
       "agPortCurCfgFastEthSpeed": agPortCurCfgFastEthSpeed,
       "agPortCurCfgFastEthMode": agPortCurCfgFastEthMode,
       "agPortCurCfgFastEthFctl": agPortCurCfgFastEthFctl,
       "agPortCurCfgGigEthAutoNeg": agPortCurCfgGigEthAutoNeg,
       "agPortCurCfgGigEthFctl": agPortCurCfgGigEthFctl,
       "agPortCurCfgPortName": agPortCurCfgPortName,
       "agPortCurCfgBwmContract": agPortCurCfgBwmContract,
       "agPortCurCfgDiscardNonIPs": agPortCurCfgDiscardNonIPs,
       "agPortNewCfgTable": agPortNewCfgTable,
       "agPortNewCfgTableEntry": agPortNewCfgTableEntry,
       "agPortNewCfgIndx": agPortNewCfgIndx,
       "agPortNewCfgPrefLink": agPortNewCfgPrefLink,
       "agPortNewCfgBackLink": agPortNewCfgBackLink,
       "agPortNewCfgState": agPortNewCfgState,
       "agPortNewCfgVlanTag": agPortNewCfgVlanTag,
       "agPortNewCfgStp": agPortNewCfgStp,
       "agPortNewCfgRmon": agPortNewCfgRmon,
       "agPortNewCfgPVID": agPortNewCfgPVID,
       "agPortNewCfgFastEthAutoNeg": agPortNewCfgFastEthAutoNeg,
       "agPortNewCfgFastEthSpeed": agPortNewCfgFastEthSpeed,
       "agPortNewCfgFastEthMode": agPortNewCfgFastEthMode,
       "agPortNewCfgFastEthFctl": agPortNewCfgFastEthFctl,
       "agPortNewCfgGigEthAutoNeg": agPortNewCfgGigEthAutoNeg,
       "agPortNewCfgGigEthFctl": agPortNewCfgGigEthFctl,
       "agPortNewCfgPortName": agPortNewCfgPortName,
       "agPortNewCfgBwmContract": agPortNewCfgBwmContract,
       "agPortNewCfgDiscardNonIPs": agPortNewCfgDiscardNonIPs,
       "iprouting": iprouting,
       "ipInterfaceTableMax": ipInterfaceTableMax,
       "ipCurCfgIntfTable": ipCurCfgIntfTable,
       "ipCurCfgIntfEntry": ipCurCfgIntfEntry,
       "ipCurCfgIntfIndex": ipCurCfgIntfIndex,
       "ipCurCfgIntfAddr": ipCurCfgIntfAddr,
       "ipCurCfgIntfMask": ipCurCfgIntfMask,
       "ipCurCfgIntfBroadcast": ipCurCfgIntfBroadcast,
       "ipCurCfgIntfVlan": ipCurCfgIntfVlan,
       "ipCurCfgIntfState": ipCurCfgIntfState,
       "ipNewCfgIntfTable": ipNewCfgIntfTable,
       "ipNewCfgIntfEntry": ipNewCfgIntfEntry,
       "ipNewCfgIntfIndex": ipNewCfgIntfIndex,
       "ipNewCfgIntfAddr": ipNewCfgIntfAddr,
       "ipNewCfgIntfMask": ipNewCfgIntfMask,
       "ipNewCfgIntfBroadcast": ipNewCfgIntfBroadcast,
       "ipNewCfgIntfVlan": ipNewCfgIntfVlan,
       "ipNewCfgIntfState": ipNewCfgIntfState,
       "ipNewCfgIntfDelete": ipNewCfgIntfDelete,
       "ipGatewayTableMax": ipGatewayTableMax,
       "ipCurCfgGwTable": ipCurCfgGwTable,
       "ipCurCfgGwEntry": ipCurCfgGwEntry,
       "ipCurCfgGwIndex": ipCurCfgGwIndex,
       "ipCurCfgGwAddr": ipCurCfgGwAddr,
       "ipCurCfgGwInterval": ipCurCfgGwInterval,
       "ipCurCfgGwRetry": ipCurCfgGwRetry,
       "ipCurCfgGwState": ipCurCfgGwState,
       "ipCurCfgGwArp": ipCurCfgGwArp,
       "ipNewCfgGwTable": ipNewCfgGwTable,
       "ipNewCfgGwEntry": ipNewCfgGwEntry,
       "ipNewCfgGwIndex": ipNewCfgGwIndex,
       "ipNewCfgGwAddr": ipNewCfgGwAddr,
       "ipNewCfgGwInterval": ipNewCfgGwInterval,
       "ipNewCfgGwRetry": ipNewCfgGwRetry,
       "ipNewCfgGwState": ipNewCfgGwState,
       "ipNewCfgGwDelete": ipNewCfgGwDelete,
       "ipNewCfgGwArp": ipNewCfgGwArp,
       "ipCurCfgStaticRouteTable": ipCurCfgStaticRouteTable,
       "ipCurCfgStaticRouteEntry": ipCurCfgStaticRouteEntry,
       "ipCurCfgStaticRouteIndx": ipCurCfgStaticRouteIndx,
       "ipCurCfgStaticRouteDestIp": ipCurCfgStaticRouteDestIp,
       "ipCurCfgStaticRouteMask": ipCurCfgStaticRouteMask,
       "ipCurCfgStaticRouteGateway": ipCurCfgStaticRouteGateway,
       "ipCurCfgStaticRouteInterface": ipCurCfgStaticRouteInterface,
       "ipNewCfgStaticRouteTable": ipNewCfgStaticRouteTable,
       "ipNewCfgStaticRouteEntry": ipNewCfgStaticRouteEntry,
       "ipNewCfgStaticRouteIndx": ipNewCfgStaticRouteIndx,
       "ipNewCfgStaticRouteDestIp": ipNewCfgStaticRouteDestIp,
       "ipNewCfgStaticRouteMask": ipNewCfgStaticRouteMask,
       "ipNewCfgStaticRouteGateway": ipNewCfgStaticRouteGateway,
       "ipNewCfgStaticRouteAction": ipNewCfgStaticRouteAction,
       "ipNewCfgStaticRouteInterface": ipNewCfgStaticRouteInterface,
       "ipForward": ipForward,
       "ripConfig": ripConfig,
       "ripCurCfgSupply": ripCurCfgSupply,
       "ripNewCfgSupply": ripNewCfgSupply,
       "ripCurCfgListen": ripCurCfgListen,
       "ripNewCfgListen": ripNewCfgListen,
       "ripCurCfgDefListen": ripCurCfgDefListen,
       "ripNewCfgDefListen": ripNewCfgDefListen,
       "ripCurCfgStaticSupply": ripCurCfgStaticSupply,
       "ripNewCfgStaticSupply": ripNewCfgStaticSupply,
       "ripCurCfgUpdatePeriod": ripCurCfgUpdatePeriod,
       "ripNewCfgUpdatePeriod": ripNewCfgUpdatePeriod,
       "ripCurCfgState": ripCurCfgState,
       "ripNewCfgState": ripNewCfgState,
       "ripCurCfgPoisonReverse": ripCurCfgPoisonReverse,
       "ripNewCfgPoisonReverse": ripNewCfgPoisonReverse,
       "ipFwdCurCfgPortTable": ipFwdCurCfgPortTable,
       "ipFwdCurCfgPortEntry": ipFwdCurCfgPortEntry,
       "ipFwdCurCfgPortIndex": ipFwdCurCfgPortIndex,
       "ipFwdCurCfgPortState": ipFwdCurCfgPortState,
       "ipFwdNewCfgPortTable": ipFwdNewCfgPortTable,
       "ipFwdNewCfgPortEntry": ipFwdNewCfgPortEntry,
       "ipFwdNewCfgPortIndex": ipFwdNewCfgPortIndex,
       "ipFwdNewCfgPortState": ipFwdNewCfgPortState,
       "ipFwdCurCfgLocalSubnet": ipFwdCurCfgLocalSubnet,
       "ipFwdNewCfgLocalSubnet": ipFwdNewCfgLocalSubnet,
       "ipFwdCurCfgLocalMask": ipFwdCurCfgLocalMask,
       "ipFwdNewCfgLocalMask": ipFwdNewCfgLocalMask,
       "ipFwdCurCfgState": ipFwdCurCfgState,
       "ipFwdNewCfgState": ipFwdNewCfgState,
       "ipFwdCurCfgDirectedBcast": ipFwdCurCfgDirectedBcast,
       "ipFwdNewCfgDirectedBcast": ipFwdNewCfgDirectedBcast,
       "arpCurCfgReARPPeriod": arpCurCfgReARPPeriod,
       "arpNewCfgReARPPeriod": arpNewCfgReARPPeriod,
       "ipCurCfgGwMetric": ipCurCfgGwMetric,
       "ipNewCfgGwMetric": ipNewCfgGwMetric,
       "vlans": vlans,
       "vlanMaxEnt": vlanMaxEnt,
       "vlanCurCfgTable": vlanCurCfgTable,
       "vlanCurCfgTableEntry": vlanCurCfgTableEntry,
       "vlanCurCfgVlanId": vlanCurCfgVlanId,
       "vlanCurCfgVlanName": vlanCurCfgVlanName,
       "vlanCurCfgPorts": vlanCurCfgPorts,
       "vlanCurCfgState": vlanCurCfgState,
       "vlanCurCfgJumbo": vlanCurCfgJumbo,
       "vlanCurCfgBwmContract": vlanCurCfgBwmContract,
       "vlanNewCfgTable": vlanNewCfgTable,
       "vlanNewCfgTableEntry": vlanNewCfgTableEntry,
       "vlanNewCfgVlanId": vlanNewCfgVlanId,
       "vlanNewCfgVlanName": vlanNewCfgVlanName,
       "vlanNewCfgPorts": vlanNewCfgPorts,
       "vlanNewCfgState": vlanNewCfgState,
       "vlanNewCfgJumbo": vlanNewCfgJumbo,
       "vlanNewCfgAddPort": vlanNewCfgAddPort,
       "vlanNewCfgRemovePort": vlanNewCfgRemovePort,
       "vlanNewCfgDelete": vlanNewCfgDelete,
       "vlanNewCfgBwmContract": vlanNewCfgBwmContract,
       "serverloadbalance": serverloadbalance,
       "slbRealServerMaxSize": slbRealServerMaxSize,
       "slbCurCfgRealServerTable": slbCurCfgRealServerTable,
       "slbCurCfgRealServerEntry": slbCurCfgRealServerEntry,
       "slbCurCfgRealServerIndex": slbCurCfgRealServerIndex,
       "slbCurCfgRealServerIpAddr": slbCurCfgRealServerIpAddr,
       "slbCurCfgRealServerWeight": slbCurCfgRealServerWeight,
       "slbCurCfgRealServerMaxConns": slbCurCfgRealServerMaxConns,
       "slbCurCfgRealServerTimeOut": slbCurCfgRealServerTimeOut,
       "slbCurCfgRealServerBackUp": slbCurCfgRealServerBackUp,
       "slbCurCfgRealServerPingInterval": slbCurCfgRealServerPingInterval,
       "slbCurCfgRealServerFailRetry": slbCurCfgRealServerFailRetry,
       "slbCurCfgRealServerSuccRetry": slbCurCfgRealServerSuccRetry,
       "slbCurCfgRealServerState": slbCurCfgRealServerState,
       "slbCurCfgRealServerType": slbCurCfgRealServerType,
       "slbCurCfgRealServerName": slbCurCfgRealServerName,
       "slbCurCfgRealServerUrlBmap": slbCurCfgRealServerUrlBmap,
       "slbCurCfgRealServerCookie": slbCurCfgRealServerCookie,
       "slbCurCfgRealServerExcludeStr": slbCurCfgRealServerExcludeStr,
       "slbCurCfgRealServerSubmac": slbCurCfgRealServerSubmac,
       "slbNewCfgRealServerTable": slbNewCfgRealServerTable,
       "slbNewCfgRealServerEntry": slbNewCfgRealServerEntry,
       "slbNewCfgRealServerIndex": slbNewCfgRealServerIndex,
       "slbNewCfgRealServerIpAddr": slbNewCfgRealServerIpAddr,
       "slbNewCfgRealServerWeight": slbNewCfgRealServerWeight,
       "slbNewCfgRealServerMaxConns": slbNewCfgRealServerMaxConns,
       "slbNewCfgRealServerTimeOut": slbNewCfgRealServerTimeOut,
       "slbNewCfgRealServerBackUp": slbNewCfgRealServerBackUp,
       "slbNewCfgRealServerPingInterval": slbNewCfgRealServerPingInterval,
       "slbNewCfgRealServerFailRetry": slbNewCfgRealServerFailRetry,
       "slbNewCfgRealServerSuccRetry": slbNewCfgRealServerSuccRetry,
       "slbNewCfgRealServerState": slbNewCfgRealServerState,
       "slbNewCfgRealServerDelete": slbNewCfgRealServerDelete,
       "slbNewCfgRealServerType": slbNewCfgRealServerType,
       "slbNewCfgRealServerName": slbNewCfgRealServerName,
       "slbNewCfgRealServerUrlBmap": slbNewCfgRealServerUrlBmap,
       "slbNewCfgRealServerAddUrl": slbNewCfgRealServerAddUrl,
       "slbNewCfgRealServerRemUrl": slbNewCfgRealServerRemUrl,
       "slbNewCfgRealServerCookie": slbNewCfgRealServerCookie,
       "slbNewCfgRealServerExcludeStr": slbNewCfgRealServerExcludeStr,
       "slbNewCfgRealServerSubmac": slbNewCfgRealServerSubmac,
       "slbVirtServerTableMaxSize": slbVirtServerTableMaxSize,
       "slbCurCfgVirtServerTable": slbCurCfgVirtServerTable,
       "slbCurCfgVirtualServerEntry": slbCurCfgVirtualServerEntry,
       "slbCurCfgVirtServerIndex": slbCurCfgVirtServerIndex,
       "slbCurCfgVirtServerIpAddress": slbCurCfgVirtServerIpAddress,
       "slbCurCfgVirtServerLayer3Only": slbCurCfgVirtServerLayer3Only,
       "slbCurCfgVirtServerState": slbCurCfgVirtServerState,
       "slbCurCfgVirtServerDname": slbCurCfgVirtServerDname,
       "slbCurCfgVirtServerCname": slbCurCfgVirtServerCname,
       "slbCurCfgVirtServerCoffset": slbCurCfgVirtServerCoffset,
       "slbCurCfgVirtServerClength": slbCurCfgVirtServerClength,
       "slbCurCfgVirtServerUriCookie": slbCurCfgVirtServerUriCookie,
       "slbCurCfgVirtServerFtpParsing": slbCurCfgVirtServerFtpParsing,
       "slbCurCfgVirtServerUrlHashLen": slbCurCfgVirtServerUrlHashLen,
       "slbCurCfgVirtServerHttpHdrName": slbCurCfgVirtServerHttpHdrName,
       "slbCurCfgVirtServerBwmContract": slbCurCfgVirtServerBwmContract,
       "slbNewCfgVirtServerTable": slbNewCfgVirtServerTable,
       "slbNewCfgVirtualServerEntry": slbNewCfgVirtualServerEntry,
       "slbNewCfgVirtServerIndex": slbNewCfgVirtServerIndex,
       "slbNewCfgVirtServerIpAddress": slbNewCfgVirtServerIpAddress,
       "slbNewCfgVirtServerLayer3Only": slbNewCfgVirtServerLayer3Only,
       "slbNewCfgVirtServerState": slbNewCfgVirtServerState,
       "slbNewCfgVirtServerDelete": slbNewCfgVirtServerDelete,
       "slbNewCfgVirtServerDname": slbNewCfgVirtServerDname,
       "slbNewCfgVirtServerCname": slbNewCfgVirtServerCname,
       "slbNewCfgVirtServerCoffset": slbNewCfgVirtServerCoffset,
       "slbNewCfgVirtServerClength": slbNewCfgVirtServerClength,
       "slbNewCfgVirtServerUriCookie": slbNewCfgVirtServerUriCookie,
       "slbNewCfgVirtServerFtpParsing": slbNewCfgVirtServerFtpParsing,
       "slbNewCfgVirtServerUrlHashLen": slbNewCfgVirtServerUrlHashLen,
       "slbNewCfgVirtServerHttpHdrName": slbNewCfgVirtServerHttpHdrName,
       "slbNewCfgVirtServerBwmContract": slbNewCfgVirtServerBwmContract,
       "slbCurCfgVirtServicesTable": slbCurCfgVirtServicesTable,
       "slbCurCfgVirtServicesEntry": slbCurCfgVirtServicesEntry,
       "slbCurCfgVirtServIndex": slbCurCfgVirtServIndex,
       "slbCurCfgVirtServiceIndex": slbCurCfgVirtServiceIndex,
       "slbCurCfgVirtServiceVirtPort": slbCurCfgVirtServiceVirtPort,
       "slbCurCfgVirtServiceRealGroup": slbCurCfgVirtServiceRealGroup,
       "slbCurCfgVirtServiceRealPort": slbCurCfgVirtServiceRealPort,
       "slbCurCfgVirtServiceUDPBalance": slbCurCfgVirtServiceUDPBalance,
       "slbCurCfgVirtServicePBind": slbCurCfgVirtServicePBind,
       "slbCurCfgVirtServiceHname": slbCurCfgVirtServiceHname,
       "slbCurCfgVirtServiceHttpSlb": slbCurCfgVirtServiceHttpSlb,
       "slbCurCfgVirtServiceBwmContract": slbCurCfgVirtServiceBwmContract,
       "slbCurCfgVirtServiceDirServerRtn": slbCurCfgVirtServiceDirServerRtn,
       "slbNewCfgVirtServicesTable": slbNewCfgVirtServicesTable,
       "slbNewCfgVirtServicesEntry": slbNewCfgVirtServicesEntry,
       "slbNewCfgVirtServIndex": slbNewCfgVirtServIndex,
       "slbNewCfgVirtServiceIndex": slbNewCfgVirtServiceIndex,
       "slbNewCfgVirtServiceVirtPort": slbNewCfgVirtServiceVirtPort,
       "slbNewCfgVirtServiceRealGroup": slbNewCfgVirtServiceRealGroup,
       "slbNewCfgVirtServiceRealPort": slbNewCfgVirtServiceRealPort,
       "slbNewCfgVirtServiceUDPBalance": slbNewCfgVirtServiceUDPBalance,
       "slbNewCfgVirtServicePBind": slbNewCfgVirtServicePBind,
       "slbNewCfgVirtServiceHname": slbNewCfgVirtServiceHname,
       "slbNewCfgVirtServiceHttpSlb": slbNewCfgVirtServiceHttpSlb,
       "slbNewCfgVirtServiceBwmContract": slbNewCfgVirtServiceBwmContract,
       "slbNewCfgVirtServiceDirServerRtn": slbNewCfgVirtServiceDirServerRtn,
       "slbNewCfgVirtServiceDelete": slbNewCfgVirtServiceDelete,
       "slbGroupTableMaxSize": slbGroupTableMaxSize,
       "slbCurCfgGroupTable": slbCurCfgGroupTable,
       "slbCurCfgGroupEntry": slbCurCfgGroupEntry,
       "slbCurCfgGroupIndex": slbCurCfgGroupIndex,
       "slbCurCfgGroupRealServers": slbCurCfgGroupRealServers,
       "slbCurCfgGroupMetric": slbCurCfgGroupMetric,
       "slbCurCfgGroupBackupServer": slbCurCfgGroupBackupServer,
       "slbCurCfgGroupHealthCheckUrl": slbCurCfgGroupHealthCheckUrl,
       "slbCurCfgGroupHealthCheckLayer": slbCurCfgGroupHealthCheckLayer,
       "slbCurCfgGroupName": slbCurCfgGroupName,
       "slbCurCfgGroupRealThreshold": slbCurCfgGroupRealThreshold,
       "slbCurCfgGroupBackupGroup": slbCurCfgGroupBackupGroup,
       "slbNewCfgGroupTable": slbNewCfgGroupTable,
       "slbNewCfgGroupEntry": slbNewCfgGroupEntry,
       "slbNewCfgGroupIndex": slbNewCfgGroupIndex,
       "slbNewCfgGroupRealServers": slbNewCfgGroupRealServers,
       "slbNewCfgGroupAddServer": slbNewCfgGroupAddServer,
       "slbNewCfgGroupRemoveServer": slbNewCfgGroupRemoveServer,
       "slbNewCfgGroupMetric": slbNewCfgGroupMetric,
       "slbNewCfgGroupBackupServer": slbNewCfgGroupBackupServer,
       "slbNewCfgGroupDelete": slbNewCfgGroupDelete,
       "slbNewCfgGroupHealthCheckUrl": slbNewCfgGroupHealthCheckUrl,
       "slbNewCfgGroupHealthCheckLayer": slbNewCfgGroupHealthCheckLayer,
       "slbNewCfgGroupName": slbNewCfgGroupName,
       "slbNewCfgGroupRealThreshold": slbNewCfgGroupRealThreshold,
       "slbNewCfgGroupBackupGroup": slbNewCfgGroupBackupGroup,
       "slbCurCfgPortTable": slbCurCfgPortTable,
       "slbCurCfgPortEntry": slbCurCfgPortEntry,
       "slbCurCfgPortIndex": slbCurCfgPortIndex,
       "slbCurCfgPortProxyIpAddr": slbCurCfgPortProxyIpAddr,
       "slbCurCfgPortSlbState": slbCurCfgPortSlbState,
       "slbCurCfgPortSlbHotStandby": slbCurCfgPortSlbHotStandby,
       "slbCurCfgPortSlbInterSwitch": slbCurCfgPortSlbInterSwitch,
       "slbCurCfgPortSlbPipState": slbCurCfgPortSlbPipState,
       "slbNewCfgPortTable": slbNewCfgPortTable,
       "slbNewCfgPortEntry": slbNewCfgPortEntry,
       "slbNewCfgPortIndex": slbNewCfgPortIndex,
       "slbNewCfgPortProxyIpAddr": slbNewCfgPortProxyIpAddr,
       "slbNewCfgPortSlbState": slbNewCfgPortSlbState,
       "slbNewCfgPortSlbHotStandby": slbNewCfgPortSlbHotStandby,
       "slbNewCfgPortSlbInterSwitch": slbNewCfgPortSlbInterSwitch,
       "slbNewCfgPortSlbPipState": slbNewCfgPortSlbPipState,
       "slbCurCfgImask": slbCurCfgImask,
       "slbNewCfgImask": slbNewCfgImask,
       "slbfailover": slbfailover,
       "slbCurCfgFailOverTable": slbCurCfgFailOverTable,
       "slbCurCfgFailOverTblEntry": slbCurCfgFailOverTblEntry,
       "slbCurCfgFailOverIndex": slbCurCfgFailOverIndex,
       "slbCurCfgFailOverPrimaryIp": slbCurCfgFailOverPrimaryIp,
       "slbCurCfgFailOverSecondaryIp": slbCurCfgFailOverSecondaryIp,
       "slbCurCfgFailOverSilenceInterval": slbCurCfgFailOverSilenceInterval,
       "slbCurCfgFailOverState": slbCurCfgFailOverState,
       "slbCurCfgFailOverRouteSupply": slbCurCfgFailOverRouteSupply,
       "slbNewCfgFailOverTable": slbNewCfgFailOverTable,
       "slbNewCfgFailOverTblEntry": slbNewCfgFailOverTblEntry,
       "slbNewCfgFailOverIndex": slbNewCfgFailOverIndex,
       "slbNewCfgFailOverPrimaryIp": slbNewCfgFailOverPrimaryIp,
       "slbNewCfgFailOverSecondaryIp": slbNewCfgFailOverSecondaryIp,
       "slbNewCfgFailOverSilenceInterval": slbNewCfgFailOverSilenceInterval,
       "slbNewCfgFailOverState": slbNewCfgFailOverState,
       "slbNewCfgFailOverRouteSupply": slbNewCfgFailOverRouteSupply,
       "slbCurCfgGlobalControl": slbCurCfgGlobalControl,
       "slbNewCfgGlobalControl": slbNewCfgGlobalControl,
       "slbCurCfgMnet": slbCurCfgMnet,
       "slbNewCfgMnet": slbNewCfgMnet,
       "slbCurCfgMmask": slbCurCfgMmask,
       "slbNewCfgMmask": slbNewCfgMmask,
       "slbCurCfgRadiusAuthenString": slbCurCfgRadiusAuthenString,
       "slbNewCfgRadiusAuthenString": slbNewCfgRadiusAuthenString,
       "slbCurCfgDirectMode": slbCurCfgDirectMode,
       "slbNewCfgDirectMode": slbNewCfgDirectMode,
       "slbUrl": slbUrl,
       "slbUrlRedir": slbUrlRedir,
       "slbCurCfgUrlExpTable": slbCurCfgUrlExpTable,
       "slbCurCfgUrlExpTableEntry": slbCurCfgUrlExpTableEntry,
       "slbCurCfgUrlExpIndex": slbCurCfgUrlExpIndex,
       "slbCurCfgUrlExpression": slbCurCfgUrlExpression,
       "slbNewCfgUrlExpTable": slbNewCfgUrlExpTable,
       "slbNewCfgUrlExpTableEntry": slbNewCfgUrlExpTableEntry,
       "slbNewCfgUrlExpIndex": slbNewCfgUrlExpIndex,
       "slbNewCfgUrlExpression": slbNewCfgUrlExpression,
       "slbNewCfgUrlExpDelete": slbNewCfgUrlExpDelete,
       "slbCurCfgUrlRedirNonGetOrigSrv": slbCurCfgUrlRedirNonGetOrigSrv,
       "slbNewCfgUrlRedirNonGetOrigSrv": slbNewCfgUrlRedirNonGetOrigSrv,
       "slbCurCfgUrlRedirCookieOrigSrv": slbCurCfgUrlRedirCookieOrigSrv,
       "slbNewCfgUrlRedirCookieOrigSrv": slbNewCfgUrlRedirCookieOrigSrv,
       "slbCurCfgUrlRedirNoCacheOrigSrv": slbCurCfgUrlRedirNoCacheOrigSrv,
       "slbNewCfgUrlRedirNoCacheOrigSrv": slbNewCfgUrlRedirNoCacheOrigSrv,
       "slbCurCfgUrlRedirUriHashLength": slbCurCfgUrlRedirUriHashLength,
       "slbNewCfgUrlRedirUriHashLength": slbNewCfgUrlRedirUriHashLength,
       "slbCurCfgUrlRedirHeader": slbCurCfgUrlRedirHeader,
       "slbNewCfgUrlRedirHeader": slbNewCfgUrlRedirHeader,
       "slbCurCfgUrlRedirHeaderName": slbCurCfgUrlRedirHeaderName,
       "slbNewCfgUrlRedirHeaderName": slbNewCfgUrlRedirHeaderName,
       "slbUrlBalance": slbUrlBalance,
       "slbCurCfgUrlLbPathTable": slbCurCfgUrlLbPathTable,
       "slbCurCfgUrlLbPathTableEntry": slbCurCfgUrlLbPathTableEntry,
       "slbCurCfgUrlLbPathIndex": slbCurCfgUrlLbPathIndex,
       "slbCurCfgUrlLbPathString": slbCurCfgUrlLbPathString,
       "slbNewCfgUrlLbPathTable": slbNewCfgUrlLbPathTable,
       "slbNewCfgUrlLbPathTableEntry": slbNewCfgUrlLbPathTableEntry,
       "slbNewCfgUrlLbPathIndex": slbNewCfgUrlLbPathIndex,
       "slbNewCfgUrlLbPathString": slbNewCfgUrlLbPathString,
       "slbNewCfgUrlLbPathDelete": slbNewCfgUrlLbPathDelete,
       "slbCurCfgUrlLbErrorMsg": slbCurCfgUrlLbErrorMsg,
       "slbNewCfgUrlLbErrorMsg": slbNewCfgUrlLbErrorMsg,
       "slbCurCfgPmask": slbCurCfgPmask,
       "slbNewCfgPmask": slbNewCfgPmask,
       "slbCurCfgGrace": slbCurCfgGrace,
       "slbNewCfgGrace": slbNewCfgGrace,
       "slbCurCfgPeerTable": slbCurCfgPeerTable,
       "slbCurCfgPeerEntry": slbCurCfgPeerEntry,
       "slbCurCfgPeerIndex": slbCurCfgPeerIndex,
       "slbCurCfgPeerIpAddr": slbCurCfgPeerIpAddr,
       "slbCurCfgPeerState": slbCurCfgPeerState,
       "slbNewCfgPeerTable": slbNewCfgPeerTable,
       "slbNewCfgPeerEntry": slbNewCfgPeerEntry,
       "slbNewCfgPeerIndex": slbNewCfgPeerIndex,
       "slbNewCfgPeerIpAddr": slbNewCfgPeerIpAddr,
       "slbNewCfgPeerState": slbNewCfgPeerState,
       "slbNewCfgPeerDelete": slbNewCfgPeerDelete,
       "slbCurCfgSyncFilt": slbCurCfgSyncFilt,
       "slbNewCfgSyncFilt": slbNewCfgSyncFilt,
       "slbCurCfgSyncPort": slbCurCfgSyncPort,
       "slbNewCfgSyncPort": slbNewCfgSyncPort,
       "slbCurCfgSyncVrrp": slbCurCfgSyncVrrp,
       "slbNewCfgSyncVrrp": slbNewCfgSyncVrrp,
       "slbCurCfgSyncPip": slbCurCfgSyncPip,
       "slbNewCfgSyncPip": slbNewCfgSyncPip,
       "slbCurCfgVirtMatrixArch": slbCurCfgVirtMatrixArch,
       "slbNewCfgVirtMatrixArch": slbNewCfgVirtMatrixArch,
       "portmirroring": portmirroring,
       "pmCurCfgMonitoringPort": pmCurCfgMonitoringPort,
       "pmNewCfgMonitoringPort": pmNewCfgMonitoringPort,
       "pmCurCfgMirroredPort": pmCurCfgMirroredPort,
       "pmNewCfgMirroredPort": pmNewCfgMirroredPort,
       "pmCurCfgMonitoredTraffic": pmCurCfgMonitoredTraffic,
       "pmNewCfgMonitoredTraffic": pmNewCfgMonitoredTraffic,
       "pmCurCfgState": pmCurCfgState,
       "pmNewCfgState": pmNewCfgState,
       "trunkgroup": trunkgroup,
       "trunkGroupTableMaxSize": trunkGroupTableMaxSize,
       "trunkGroupCurCfgTable": trunkGroupCurCfgTable,
       "trunkGroupCurCfgTableEntry": trunkGroupCurCfgTableEntry,
       "trunkGroupCurCfgIndex": trunkGroupCurCfgIndex,
       "trunkGroupCurCfgPorts": trunkGroupCurCfgPorts,
       "trunkGroupCurCfgState": trunkGroupCurCfgState,
       "trunkGroupCurCfgBwmContract": trunkGroupCurCfgBwmContract,
       "trunkGroupNewCfgTable": trunkGroupNewCfgTable,
       "trunkGroupNewCfgTableEntry": trunkGroupNewCfgTableEntry,
       "trunkGroupNewCfgIndex": trunkGroupNewCfgIndex,
       "trunkGroupNewCfgPorts": trunkGroupNewCfgPorts,
       "trunkGroupNewCfgAddPort": trunkGroupNewCfgAddPort,
       "trunkGroupNewCfgRemovePort": trunkGroupNewCfgRemovePort,
       "trunkGroupNewCfgState": trunkGroupNewCfgState,
       "trunkGroupNewCfgDelete": trunkGroupNewCfgDelete,
       "trunkGroupNewCfgBwmContract": trunkGroupNewCfgBwmContract,
       "stats": stats,
       "ripStats": ripStats,
       "ripStatInPkts": ripStatInPkts,
       "ripStatOutPkts": ripStatOutPkts,
       "ripStatInErrorPkts": ripStatInErrorPkts,
       "slbStats": slbStats,
       "slbStatPortMaintTable": slbStatPortMaintTable,
       "slbStatPortMaintEntry": slbStatPortMaintEntry,
       "slbStatPortMaintPortIndex": slbStatPortMaintPortIndex,
       "slbStatPortMaintCurBindings": slbStatPortMaintCurBindings,
       "slbStatPortMaintBindingFails": slbStatPortMaintBindingFails,
       "slbStatPortMaintNonTcpFrames": slbStatPortMaintNonTcpFrames,
       "slbStatPortMaintTcpFragments": slbStatPortMaintTcpFragments,
       "slbStatPortMaintUdpDatagrams": slbStatPortMaintUdpDatagrams,
       "slbStatPortMaintIncorrectVIPs": slbStatPortMaintIncorrectVIPs,
       "slbStatPortMaintIncorrectVports": slbStatPortMaintIncorrectVports,
       "slbStatPortMaintRealServerNoAvails": slbStatPortMaintRealServerNoAvails,
       "slbStatPortMaintFilteredDeniedFrames": slbStatPortMaintFilteredDeniedFrames,
       "slbStatPortRealServerTable": slbStatPortRealServerTable,
       "slbStatPortRealServerEntry": slbStatPortRealServerEntry,
       "slbStatPortRealServerPortIndex": slbStatPortRealServerPortIndex,
       "slbStatPortRealServerServerIndex": slbStatPortRealServerServerIndex,
       "slbStatPortRealServerCurrSessions": slbStatPortRealServerCurrSessions,
       "slbStatPortRealServerTotalSessions": slbStatPortRealServerTotalSessions,
       "slbStatPortRealServerHCOctets": slbStatPortRealServerHCOctets,
       "slbStatPortRealServerHCOctetsLow32": slbStatPortRealServerHCOctetsLow32,
       "slbStatPortRealServerHCOctetsHigh32": slbStatPortRealServerHCOctetsHigh32,
       "slbStatMaintBackupServActs": slbStatMaintBackupServActs,
       "slbStatMaintOverflowServActs": slbStatMaintOverflowServActs,
       "slbStatRServerTable": slbStatRServerTable,
       "slbStatRServerEntry": slbStatRServerEntry,
       "slbStatRServerIndex": slbStatRServerIndex,
       "slbStatRServerCurrSessions": slbStatRServerCurrSessions,
       "slbStatRServerTotalSessions": slbStatRServerTotalSessions,
       "slbStatRServerFailures": slbStatRServerFailures,
       "slbStatRServerHighestSessions": slbStatRServerHighestSessions,
       "slbStatRServerHCOctets": slbStatRServerHCOctets,
       "slbStatRServerHCOctetsLow32": slbStatRServerHCOctetsLow32,
       "slbStatRServerHCOctetsHigh32": slbStatRServerHCOctetsHigh32,
       "slbStatGroupTable": slbStatGroupTable,
       "slbStatGroupEntry": slbStatGroupEntry,
       "slbStatGroupIndex": slbStatGroupIndex,
       "slbStatGroupCurrSessions": slbStatGroupCurrSessions,
       "slbStatGroupTotalSessions": slbStatGroupTotalSessions,
       "slbStatGroupHighestSessions": slbStatGroupHighestSessions,
       "slbStatGroupHCOctets": slbStatGroupHCOctets,
       "slbStatGroupHCOctetsLow32": slbStatGroupHCOctetsLow32,
       "slbStatGroupHCOctetsHigh32": slbStatGroupHCOctetsHigh32,
       "slbStatVServerTable": slbStatVServerTable,
       "slbStatVServerEntry": slbStatVServerEntry,
       "slbStatVServerIndex": slbStatVServerIndex,
       "slbStatVServerCurrSessions": slbStatVServerCurrSessions,
       "slbStatVServerTotalSessions": slbStatVServerTotalSessions,
       "slbStatVServerHighestSessions": slbStatVServerHighestSessions,
       "slbStatVServerHCOctets": slbStatVServerHCOctets,
       "slbStatVServerHCOctetsLow32": slbStatVServerHCOctetsLow32,
       "slbStatVServerHCOctetsHigh32": slbStatVServerHCOctetsHigh32,
       "slbStatVServerHeaderHits": slbStatVServerHeaderHits,
       "slbStatVServerHeaderMisses": slbStatVServerHeaderMisses,
       "slbStatVServerHeaderTotalSessions": slbStatVServerHeaderTotalSessions,
       "arpStats": arpStats,
       "arpStatEntries": arpStatEntries,
       "arpStatHighWater": arpStatHighWater,
       "arpStatMaxEntries": arpStatMaxEntries,
       "routeStats": routeStats,
       "routeStatEntries": routeStatEntries,
       "routeStatHighWater": routeStatHighWater,
       "routeStatMaxEntries": routeStatMaxEntries,
       "dnsStats": dnsStats,
       "dnsStatInGoodDnsRequests": dnsStatInGoodDnsRequests,
       "dnsStatInBadDnsRequests": dnsStatInBadDnsRequests,
       "filterStats": filterStats,
       "fltStatTable": fltStatTable,
       "fltStatTableEntry": fltStatTableEntry,
       "fltStatFltIndex": fltStatFltIndex,
       "fltStatFltFirings": fltStatFltFirings,
       "gslbStats": gslbStats,
       "gslbStatRemRealServerTable": gslbStatRemRealServerTable,
       "gslbStatRemRealServerEntry": gslbStatRemRealServerEntry,
       "gslbStatRemRealServerIndex": gslbStatRemRealServerIndex,
       "gslbStatRemRealServerDnsHandoffs": gslbStatRemRealServerDnsHandoffs,
       "gslbStatRemRealServerHttpRedirs": gslbStatRemRealServerHttpRedirs,
       "gslbMaintStats": gslbMaintStats,
       "gslbStatMaintInGoodSiteUpdates": gslbStatMaintInGoodSiteUpdates,
       "gslbStatMaintInBadSiteUpdates": gslbStatMaintInBadSiteUpdates,
       "vrrpStats": vrrpStats,
       "vrrpStatInAdvers": vrrpStatInAdvers,
       "vrrpStatOutAdvers": vrrpStatOutAdvers,
       "vrrpStatOutBadAdvers": vrrpStatOutBadAdvers,
       "urlStats": urlStats,
       "urlRedirStats": urlRedirStats,
       "urlStatRedRedirs": urlStatRedRedirs,
       "urlStatRedOrigSrvs": urlStatRedOrigSrvs,
       "urlStatRedNonGets": urlStatRedNonGets,
       "urlStatRedCookie": urlStatRedCookie,
       "urlStatRedNoCache": urlStatRedNoCache,
       "urlSlbStats": urlSlbStats,
       "urlStatSlbPathTable": urlStatSlbPathTable,
       "urlStatSlbPathTableEntry": urlStatSlbPathTableEntry,
       "urlStatSlbPathIndex": urlStatSlbPathIndex,
       "urlStatSlbPathHits": urlStatSlbPathHits,
       "tcpStats": tcpStats,
       "tcpStatCurConns": tcpStatCurConns,
       "tcpStatHalfOpens": tcpStatHalfOpens,
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
       "ftpStats": ftpStats,
       "ftpSlbStats": ftpSlbStats,
       "ftpSlbStatTotal": ftpSlbStatTotal,
       "ftpNatStatTotal": ftpNatStatTotal,
       "bwmStats": bwmStats,
       "bwmStatTcTable": bwmStatTcTable,
       "bwmStatTcEntry": bwmStatTcEntry,
       "bwmStatTcContractIndex": bwmStatTcContractIndex,
       "bwmStatTcName": bwmStatTcName,
       "bwmStatTcOutoct": bwmStatTcOutoct,
       "bwmStatTcOutdisoct": bwmStatTcOutdisoct,
       "bwmStatTcBufferUsed": bwmStatTcBufferUsed,
       "bwmStatTcBufferMax": bwmStatTcBufferMax,
       "bwmStatTcrTable": bwmStatTcrTable,
       "bwmStatTcrEntry": bwmStatTcrEntry,
       "bwmStatTcrContractIndex": bwmStatTcrContractIndex,
       "bwmStatTcrName": bwmStatTcrName,
       "bwmStatTcrRate": bwmStatTcrRate,
       "bwmStatTcrOutoct": bwmStatTcrOutoct,
       "bwmStatTcrOutdisoct": bwmStatTcrOutdisoct,
       "bwmStatTcrBufferUsed": bwmStatTcrBufferUsed,
       "bwmStatTcrBufferMax": bwmStatTcrBufferMax,
       "bwmStatSpTcTable": bwmStatSpTcTable,
       "bwmStatSpTcEntry": bwmStatSpTcEntry,
       "bwmStatSpTcPortIndex": bwmStatSpTcPortIndex,
       "bwmStatSpTcContractIndex": bwmStatSpTcContractIndex,
       "bwmStatSpTcName": bwmStatSpTcName,
       "bwmStatSpTcOutoct": bwmStatSpTcOutoct,
       "bwmStatSpTcOutdisoct": bwmStatSpTcOutdisoct,
       "bwmStatSpTcBufferUsed": bwmStatSpTcBufferUsed,
       "bwmStatSpTcBufferMax": bwmStatSpTcBufferMax,
       "bwmStatSpTcrTable": bwmStatSpTcrTable,
       "bwmStatSpTcrEntry": bwmStatSpTcrEntry,
       "bwmStatSpTcrPortIndex": bwmStatSpTcrPortIndex,
       "bwmStatSpTcrContractIndex": bwmStatSpTcrContractIndex,
       "bwmStatSpTcrName": bwmStatSpTcrName,
       "bwmStatSpTcrRate": bwmStatSpTcrRate,
       "bwmStatSpTcrOutoct": bwmStatSpTcrOutoct,
       "bwmStatSpTcrOutdisoct": bwmStatSpTcrOutdisoct,
       "bwmStatSpTcrBufferUsed": bwmStatSpTcrBufferUsed,
       "bwmStatSpTcrBufferMax": bwmStatSpTcrBufferMax,
       "information": information,
       "port-info": port_info,
       "portInfoTable": portInfoTable,
       "portInfoTableEntry": portInfoTableEntry,
       "portInfoIndx": portInfoIndx,
       "portInfoSpeed": portInfoSpeed,
       "portInfoMode": portInfoMode,
       "portInfoFlowCtrl": portInfoFlowCtrl,
       "portInfoLink": portInfoLink,
       "slb-info": slb_info,
       "slbFailOverInfoTable": slbFailOverInfoTable,
       "slbFailOverInfoEntry": slbFailOverInfoEntry,
       "slbFailOverInfoIndex": slbFailOverInfoIndex,
       "slbFailOverInfoPrimaryIp": slbFailOverInfoPrimaryIp,
       "slbFailOverInfoPrimaryStatus": slbFailOverInfoPrimaryStatus,
       "slbFailOverInfoPrimaryState": slbFailOverInfoPrimaryState,
       "slbFailOverInfoSecondaryIp": slbFailOverInfoSecondaryIp,
       "slbFailOverInfoSecondaryStatus": slbFailOverInfoSecondaryStatus,
       "slbFailOverInfoSecondaryState": slbFailOverInfoSecondaryState,
       "slbRealServerInfoTable": slbRealServerInfoTable,
       "slbRealServerInfoEntry": slbRealServerInfoEntry,
       "slbRealServerInfoIndex": slbRealServerInfoIndex,
       "slbRealServerInfoIpAddr": slbRealServerInfoIpAddr,
       "slbRealServerMacAddr": slbRealServerMacAddr,
       "slbRealServerInfoSwitchPort": slbRealServerInfoSwitchPort,
       "slbRealServerInfoHealthLayer": slbRealServerInfoHealthLayer,
       "slbRealServerInfoOverflow": slbRealServerInfoOverflow,
       "slbRealServerInfoState": slbRealServerInfoState,
       "ip-info": ip_info,
       "ipRouteInfoTable": ipRouteInfoTable,
       "ipRouteInfoEntry": ipRouteInfoEntry,
       "ipRouteInfoIndx": ipRouteInfoIndx,
       "ipRouteInfoDestIp": ipRouteInfoDestIp,
       "ipRouteInfoMask": ipRouteInfoMask,
       "ipRouteInfoGateway": ipRouteInfoGateway,
       "ipRouteInfoTag": ipRouteInfoTag,
       "ipRouteInfoType": ipRouteInfoType,
       "ipRouteInfoInterface": ipRouteInfoInterface,
       "arpInfoTable": arpInfoTable,
       "arpInfoEntry": arpInfoEntry,
       "arpInfoDestIp": arpInfoDestIp,
       "arpInfoMacAddr": arpInfoMacAddr,
       "arpInfoVLAN": arpInfoVLAN,
       "arpInfoSrcPort": arpInfoSrcPort,
       "arpInfoRefPorts": arpInfoRefPorts,
       "arpInfoFlag": arpInfoFlag,
       "vrrp-info": vrrp_info,
       "vrrpInfoVirtRtrTable": vrrpInfoVirtRtrTable,
       "vrrpInfoVirtRtrTableEntry": vrrpInfoVirtRtrTableEntry,
       "vrrpInfoVirtRtrIndex": vrrpInfoVirtRtrIndex,
       "vrrpInfoVirtRtrState": vrrpInfoVirtRtrState,
       "filtering": filtering,
       "fltCfgTableMaxSize": fltCfgTableMaxSize,
       "fltCurCfgTable": fltCurCfgTable,
       "fltCurCfgTableEntry": fltCurCfgTableEntry,
       "fltCurCfgIndx": fltCurCfgIndx,
       "fltCurCfgSrcIp": fltCurCfgSrcIp,
       "fltCurCfgSrcIpMask": fltCurCfgSrcIpMask,
       "fltCurCfgDstIp": fltCurCfgDstIp,
       "fltCurCfgDstIpMask": fltCurCfgDstIpMask,
       "fltCurCfgProtocol": fltCurCfgProtocol,
       "fltCurCfgRangeHighSrcPort": fltCurCfgRangeHighSrcPort,
       "fltCurCfgRangeLowSrcPort": fltCurCfgRangeLowSrcPort,
       "fltCurCfgRangeLowDstPort": fltCurCfgRangeLowDstPort,
       "fltCurCfgRangeHighDstPort": fltCurCfgRangeHighDstPort,
       "fltCurCfgAction": fltCurCfgAction,
       "fltCurCfgRedirPort": fltCurCfgRedirPort,
       "fltCurCfgRedirGroup": fltCurCfgRedirGroup,
       "fltCurCfgLog": fltCurCfgLog,
       "fltCurCfgState": fltCurCfgState,
       "fltCurCfgNat": fltCurCfgNat,
       "fltCurCfgCache": fltCurCfgCache,
       "fltCurCfgInvert": fltCurCfgInvert,
       "fltCurCfgClientProxy": fltCurCfgClientProxy,
       "fltCurCfgTcpAck": fltCurCfgTcpAck,
       "fltCurCfgUrlRedir": fltCurCfgUrlRedir,
       "fltCurCfgSrcMac": fltCurCfgSrcMac,
       "fltCurCfgDstMac": fltCurCfgDstMac,
       "fltCurCfgFtpNatActive": fltCurCfgFtpNatActive,
       "fltCurCfgAclTcpUrg": fltCurCfgAclTcpUrg,
       "fltCurCfgAclTcpAck": fltCurCfgAclTcpAck,
       "fltCurCfgAclTcpPsh": fltCurCfgAclTcpPsh,
       "fltCurCfgAclTcpRst": fltCurCfgAclTcpRst,
       "fltCurCfgAclTcpSyn": fltCurCfgAclTcpSyn,
       "fltCurCfgAclTcpFin": fltCurCfgAclTcpFin,
       "fltCurCfgAclIcmp": fltCurCfgAclIcmp,
       "fltCurCfgAclIpOption": fltCurCfgAclIpOption,
       "fltCurCfgBwmContract": fltCurCfgBwmContract,
       "fltCurCfgAclIpTos": fltCurCfgAclIpTos,
       "fltCurCfgAclIpTosMask": fltCurCfgAclIpTosMask,
       "fltCurCfgAclIpTosNew": fltCurCfgAclIpTosNew,
       "fltCurCfgFwlb": fltCurCfgFwlb,
       "fltNewCfgTable": fltNewCfgTable,
       "fltNewCfgTableEntry": fltNewCfgTableEntry,
       "fltNewCfgIndx": fltNewCfgIndx,
       "fltNewCfgSrcIp": fltNewCfgSrcIp,
       "fltNewCfgSrcIpMask": fltNewCfgSrcIpMask,
       "fltNewCfgDstIp": fltNewCfgDstIp,
       "fltNewCfgDstIpMask": fltNewCfgDstIpMask,
       "fltNewCfgProtocol": fltNewCfgProtocol,
       "fltNewCfgRangeHighSrcPort": fltNewCfgRangeHighSrcPort,
       "fltNewCfgRangeLowSrcPort": fltNewCfgRangeLowSrcPort,
       "fltNewCfgRangeLowDstPort": fltNewCfgRangeLowDstPort,
       "fltNewCfgRangeHighDstPort": fltNewCfgRangeHighDstPort,
       "fltNewCfgAction": fltNewCfgAction,
       "fltNewCfgRedirPort": fltNewCfgRedirPort,
       "fltNewCfgRedirGroup": fltNewCfgRedirGroup,
       "fltNewCfgLog": fltNewCfgLog,
       "fltNewCfgState": fltNewCfgState,
       "fltNewCfgDelete": fltNewCfgDelete,
       "fltNewCfgNat": fltNewCfgNat,
       "fltNewCfgCache": fltNewCfgCache,
       "fltNewCfgInvert": fltNewCfgInvert,
       "fltNewCfgClientProxy": fltNewCfgClientProxy,
       "fltNewCfgTcpAck": fltNewCfgTcpAck,
       "fltNewCfgUrlRedir": fltNewCfgUrlRedir,
       "fltNewCfgSrcMac": fltNewCfgSrcMac,
       "fltNewCfgDstMac": fltNewCfgDstMac,
       "fltNewCfgFtpNatActive": fltNewCfgFtpNatActive,
       "fltNewCfgAclTcpUrg": fltNewCfgAclTcpUrg,
       "fltNewCfgAclTcpAck": fltNewCfgAclTcpAck,
       "fltNewCfgAclTcpPsh": fltNewCfgAclTcpPsh,
       "fltNewCfgAclTcpRst": fltNewCfgAclTcpRst,
       "fltNewCfgAclTcpSyn": fltNewCfgAclTcpSyn,
       "fltNewCfgAclTcpFin": fltNewCfgAclTcpFin,
       "fltNewCfgAclIcmp": fltNewCfgAclIcmp,
       "fltNewCfgAclIpOption": fltNewCfgAclIpOption,
       "fltNewCfgBwmContract": fltNewCfgBwmContract,
       "fltNewCfgAclIpTos": fltNewCfgAclIpTos,
       "fltNewCfgAclIpTosMask": fltNewCfgAclIpTosMask,
       "fltNewCfgAclIpTosNew": fltNewCfgAclIpTosNew,
       "fltNewCfgFwlb": fltNewCfgFwlb,
       "fltCurCfgPortTable": fltCurCfgPortTable,
       "fltCurCfgPortTableEntry": fltCurCfgPortTableEntry,
       "fltCurCfgPortIndx": fltCurCfgPortIndx,
       "fltCurCfgPortState": fltCurCfgPortState,
       "fltCurCfgPortFiltBmap": fltCurCfgPortFiltBmap,
       "fltNewCfgPortTable": fltNewCfgPortTable,
       "fltNewCfgPortTableEntry": fltNewCfgPortTableEntry,
       "fltNewCfgPortIndx": fltNewCfgPortIndx,
       "fltNewCfgPortState": fltNewCfgPortState,
       "fltNewCfgPortFiltBmap": fltNewCfgPortFiltBmap,
       "fltNewCfgPortAddFiltRule": fltNewCfgPortAddFiltRule,
       "fltNewCfgPortRemFiltRule": fltNewCfgPortRemFiltRule,
       "globalSLB": globalSLB,
       "gslbGeneral": gslbGeneral,
       "gslbCurCfgGenState": gslbCurCfgGenState,
       "gslbNewCfgGenState": gslbNewCfgGenState,
       "gslbCurCfgGenDnsHandoff": gslbCurCfgGenDnsHandoff,
       "gslbNewCfgGenDnsHandoff": gslbNewCfgGenDnsHandoff,
       "gslbCurCfgGenDnsTTL": gslbCurCfgGenDnsTTL,
       "gslbNewCfgGenDnsTTL": gslbNewCfgGenDnsTTL,
       "gslbCurCfgGenHttpRedirect": gslbCurCfgGenHttpRedirect,
       "gslbNewCfgGenHttpRedirect": gslbNewCfgGenHttpRedirect,
       "gslbCurCfgGenRemSiteUpdateInterval": gslbCurCfgGenRemSiteUpdateInterval,
       "gslbNewCfgGenRemSiteUpdateInterval": gslbNewCfgGenRemSiteUpdateInterval,
       "gslbCurCfgGenDnsLocalPref": gslbCurCfgGenDnsLocalPref,
       "gslbNewCfgGenDnsLocalPref": gslbNewCfgGenDnsLocalPref,
       "gslbCurCfgGenMinco": gslbCurCfgGenMinco,
       "gslbNewCfgGenMinco": gslbNewCfgGenMinco,
       "gslbCurCfgGenOne": gslbCurCfgGenOne,
       "gslbNewCfgGenOne": gslbNewCfgGenOne,
       "gslbCurCfgGenUsern": gslbCurCfgGenUsern,
       "gslbNewCfgGenUsern": gslbNewCfgGenUsern,
       "gslbCurCfgGenGeo": gslbCurCfgGenGeo,
       "gslbNewCfgGenGeo": gslbNewCfgGenGeo,
       "gslbDNS": gslbDNS,
       "dnsCurCfgPrimaryIpAddr": dnsCurCfgPrimaryIpAddr,
       "dnsNewCfgPrimaryIpAddr": dnsNewCfgPrimaryIpAddr,
       "dnsCurCfgSecondaryIpAddr": dnsCurCfgSecondaryIpAddr,
       "dnsNewCfgSecondaryIpAddr": dnsNewCfgSecondaryIpAddr,
       "dnsCurCfgDomainName": dnsCurCfgDomainName,
       "dnsNewCfgDomainName": dnsNewCfgDomainName,
       "gslbSites": gslbSites,
       "gslbRemSiteTableMaxSize": gslbRemSiteTableMaxSize,
       "gslbCurCfgRemSiteTable": gslbCurCfgRemSiteTable,
       "gslbCurCfgRemSiteTableEntry": gslbCurCfgRemSiteTableEntry,
       "gslbCurCfgRemSiteIndx": gslbCurCfgRemSiteIndx,
       "gslbCurCfgRemSitePrimaryIp": gslbCurCfgRemSitePrimaryIp,
       "gslbCurCfgRemSiteSecondaryIp": gslbCurCfgRemSiteSecondaryIp,
       "gslbCurCfgRemSiteState": gslbCurCfgRemSiteState,
       "gslbCurCfgRemSiteUpdate": gslbCurCfgRemSiteUpdate,
       "gslbNewCfgRemSiteTable": gslbNewCfgRemSiteTable,
       "gslbNewCfgRemSiteTableEntry": gslbNewCfgRemSiteTableEntry,
       "gslbNewCfgRemSiteIndx": gslbNewCfgRemSiteIndx,
       "gslbNewCfgRemSitePrimaryIp": gslbNewCfgRemSitePrimaryIp,
       "gslbNewCfgRemSiteSecondaryIp": gslbNewCfgRemSiteSecondaryIp,
       "gslbNewCfgRemSiteState": gslbNewCfgRemSiteState,
       "gslbNewCfgRemSiteUpdate": gslbNewCfgRemSiteUpdate,
       "gslbLookup": gslbLookup,
       "gslbCurCfgGenLookups": gslbCurCfgGenLookups,
       "gslbNewCfgGenLookups": gslbNewCfgGenLookups,
       "gslbCurCfgGenLookupDname": gslbCurCfgGenLookupDname,
       "gslbNewCfgGenLookupDname": gslbNewCfgGenLookupDname,
       "gslbNetwork": gslbNetwork,
       "gslbNetworkTableMaxSize": gslbNetworkTableMaxSize,
       "gslbCurCfgNetworkTable": gslbCurCfgNetworkTable,
       "gslbCurCfgNetworkTableEntry": gslbCurCfgNetworkTableEntry,
       "gslbCurCfgNetworkIndx": gslbCurCfgNetworkIndx,
       "gslbCurCfgNetworkSourceIp": gslbCurCfgNetworkSourceIp,
       "gslbCurCfgNetworkNetMask": gslbCurCfgNetworkNetMask,
       "gslbCurCfgNetworkVip1": gslbCurCfgNetworkVip1,
       "gslbCurCfgNetworkVip2": gslbCurCfgNetworkVip2,
       "gslbNewCfgNetworkTable": gslbNewCfgNetworkTable,
       "gslbNewCfgNetworkTableEntry": gslbNewCfgNetworkTableEntry,
       "gslbNewCfgNetworkIndx": gslbNewCfgNetworkIndx,
       "gslbNewCfgNetworkSourceIp": gslbNewCfgNetworkSourceIp,
       "gslbNewCfgNetworkNetMask": gslbNewCfgNetworkNetMask,
       "gslbNewCfgNetworkVip1": gslbNewCfgNetworkVip1,
       "gslbNewCfgNetworkVip2": gslbNewCfgNetworkVip2,
       "gslbNewCfgNetworkDelete": gslbNewCfgNetworkDelete,
       "gslbCurCfgGenExternal": gslbCurCfgGenExternal,
       "gslbNewCfgGenExternal": gslbNewCfgGenExternal,
       "gslbCurCfgGenEip": gslbCurCfgGenEip,
       "gslbNewCfgGenEip": gslbNewCfgGenEip,
       "gslbCurCfgGenLookupPort": gslbCurCfgGenLookupPort,
       "gslbNewCfgGenLookupPort": gslbNewCfgGenLookupPort,
       "gslbCurCfgGenLookupTimeout": gslbCurCfgGenLookupTimeout,
       "gslbNewCfgGenLookupTimeout": gslbNewCfgGenLookupTimeout,
       "dynamicSLB": dynamicSLB,
       "dynSLBRealServerTable": dynSLBRealServerTable,
       "dynSLBRealServerEntry": dynSLBRealServerEntry,
       "dynSLBRealServerIpAddr": dynSLBRealServerIpAddr,
       "dynSLBRealServerPortNum": dynSLBRealServerPortNum,
       "dynSLBRealServerWeight": dynSLBRealServerWeight,
       "altswitchTraps": altswitchTraps,
       "operCmds": operCmds,
       "operSlbPortTable": operSlbPortTable,
       "operSlbPortEntry": operSlbPortEntry,
       "operSlbPortIndex": operSlbPortIndex,
       "operSlbPortClrSessionTab": operSlbPortClrSessionTab,
       "vrrp": vrrp,
       "vrrpGeneral": vrrpGeneral,
       "vrrpCurCfgGenState": vrrpCurCfgGenState,
       "vrrpNewCfgGenState": vrrpNewCfgGenState,
       "vrrpCurCfgGenTckVirtRtrInc": vrrpCurCfgGenTckVirtRtrInc,
       "vrrpNewCfgGenTckVirtRtrInc": vrrpNewCfgGenTckVirtRtrInc,
       "vrrpCurCfgGenTckIpIntfInc": vrrpCurCfgGenTckIpIntfInc,
       "vrrpNewCfgGenTckIpIntfInc": vrrpNewCfgGenTckIpIntfInc,
       "vrrpCurCfgGenTckVlanPortInc": vrrpCurCfgGenTckVlanPortInc,
       "vrrpNewCfgGenTckVlanPortInc": vrrpNewCfgGenTckVlanPortInc,
       "vrrpCurCfgGenTckL4PortInc": vrrpCurCfgGenTckL4PortInc,
       "vrrpNewCfgGenTckL4PortInc": vrrpNewCfgGenTckL4PortInc,
       "vrrpCurCfgGenTckRServerInc": vrrpCurCfgGenTckRServerInc,
       "vrrpNewCfgGenTckRServerInc": vrrpNewCfgGenTckRServerInc,
       "vrrpCurCfgGenTckHsrpInc": vrrpCurCfgGenTckHsrpInc,
       "vrrpNewCfgGenTckHsrpInc": vrrpNewCfgGenTckHsrpInc,
       "vrrpCurCfgGenHotstandby": vrrpCurCfgGenHotstandby,
       "vrrpNewCfgGenHotstandby": vrrpNewCfgGenHotstandby,
       "vrrpCurCfgVirtRtrTable": vrrpCurCfgVirtRtrTable,
       "vrrpCurCfgVirtRtrTableEntry": vrrpCurCfgVirtRtrTableEntry,
       "vrrpCurCfgVirtRtrIndx": vrrpCurCfgVirtRtrIndx,
       "vrrpCurCfgVirtRtrID": vrrpCurCfgVirtRtrID,
       "vrrpCurCfgVirtRtrAddr": vrrpCurCfgVirtRtrAddr,
       "vrrpCurCfgVirtRtrIfIndex": vrrpCurCfgVirtRtrIfIndex,
       "vrrpCurCfgVirtRtrInterval": vrrpCurCfgVirtRtrInterval,
       "vrrpCurCfgVirtRtrPriority": vrrpCurCfgVirtRtrPriority,
       "vrrpCurCfgVirtRtrPreempt": vrrpCurCfgVirtRtrPreempt,
       "vrrpCurCfgVirtRtrState": vrrpCurCfgVirtRtrState,
       "vrrpCurCfgVirtRtrSharing": vrrpCurCfgVirtRtrSharing,
       "vrrpCurCfgVirtRtrTckVirtRtr": vrrpCurCfgVirtRtrTckVirtRtr,
       "vrrpCurCfgVirtRtrTckIpIntf": vrrpCurCfgVirtRtrTckIpIntf,
       "vrrpCurCfgVirtRtrTckVlanPort": vrrpCurCfgVirtRtrTckVlanPort,
       "vrrpCurCfgVirtRtrTckL4Port": vrrpCurCfgVirtRtrTckL4Port,
       "vrrpCurCfgVirtRtrTckRServer": vrrpCurCfgVirtRtrTckRServer,
       "vrrpCurCfgVirtRtrTckHsrp": vrrpCurCfgVirtRtrTckHsrp,
       "vrrpNewCfgVirtRtrTable": vrrpNewCfgVirtRtrTable,
       "vrrpNewCfgVirtRtrTableEntry": vrrpNewCfgVirtRtrTableEntry,
       "vrrpNewCfgVirtRtrIndx": vrrpNewCfgVirtRtrIndx,
       "vrrpNewCfgVirtRtrID": vrrpNewCfgVirtRtrID,
       "vrrpNewCfgVirtRtrAddr": vrrpNewCfgVirtRtrAddr,
       "vrrpNewCfgVirtRtrIfIndex": vrrpNewCfgVirtRtrIfIndex,
       "vrrpNewCfgVirtRtrInterval": vrrpNewCfgVirtRtrInterval,
       "vrrpNewCfgVirtRtrPriority": vrrpNewCfgVirtRtrPriority,
       "vrrpNewCfgVirtRtrPreempt": vrrpNewCfgVirtRtrPreempt,
       "vrrpNewCfgVirtRtrState": vrrpNewCfgVirtRtrState,
       "vrrpNewCfgVirtRtrDelete": vrrpNewCfgVirtRtrDelete,
       "vrrpNewCfgVirtRtrSharing": vrrpNewCfgVirtRtrSharing,
       "vrrpNewCfgVirtRtrTckVirtRtr": vrrpNewCfgVirtRtrTckVirtRtr,
       "vrrpNewCfgVirtRtrTckIpIntf": vrrpNewCfgVirtRtrTckIpIntf,
       "vrrpNewCfgVirtRtrTckVlanPort": vrrpNewCfgVirtRtrTckVlanPort,
       "vrrpNewCfgVirtRtrTckL4Port": vrrpNewCfgVirtRtrTckL4Port,
       "vrrpNewCfgVirtRtrTckRServer": vrrpNewCfgVirtRtrTckRServer,
       "vrrpNewCfgVirtRtrTckHsrp": vrrpNewCfgVirtRtrTckHsrp,
       "vrrpCurCfgIfTable": vrrpCurCfgIfTable,
       "vrrpCurCfgIfTableEntry": vrrpCurCfgIfTableEntry,
       "vrrpCurCfgIfIndx": vrrpCurCfgIfIndx,
       "vrrpCurCfgIfAuthType": vrrpCurCfgIfAuthType,
       "vrrpCurCfgIfPasswd": vrrpCurCfgIfPasswd,
       "vrrpNewCfgIfTable": vrrpNewCfgIfTable,
       "vrrpNewCfgIfTableEntry": vrrpNewCfgIfTableEntry,
       "vrrpNewCfgIfIndx": vrrpNewCfgIfIndx,
       "vrrpNewCfgIfAuthType": vrrpNewCfgIfAuthType,
       "vrrpNewCfgIfPasswd": vrrpNewCfgIfPasswd,
       "vrrpNewCfgIfDelete": vrrpNewCfgIfDelete,
       "vrrpCurCfgVirtRtrGrpTable": vrrpCurCfgVirtRtrGrpTable,
       "vrrpCurCfgVirtRtrGrpTableEntry": vrrpCurCfgVirtRtrGrpTableEntry,
       "vrrpCurCfgVirtRtrGrpIndx": vrrpCurCfgVirtRtrGrpIndx,
       "vrrpCurCfgVirtRtrGrpID": vrrpCurCfgVirtRtrGrpID,
       "vrrpCurCfgVirtRtrGrpIfIndex": vrrpCurCfgVirtRtrGrpIfIndex,
       "vrrpCurCfgVirtRtrGrpInterval": vrrpCurCfgVirtRtrGrpInterval,
       "vrrpCurCfgVirtRtrGrpPriority": vrrpCurCfgVirtRtrGrpPriority,
       "vrrpCurCfgVirtRtrGrpPreempt": vrrpCurCfgVirtRtrGrpPreempt,
       "vrrpCurCfgVirtRtrGrpState": vrrpCurCfgVirtRtrGrpState,
       "vrrpCurCfgVirtRtrGrpSharing": vrrpCurCfgVirtRtrGrpSharing,
       "vrrpCurCfgVirtRtrGrpTckVirtRtr": vrrpCurCfgVirtRtrGrpTckVirtRtr,
       "vrrpCurCfgVirtRtrGrpTckIpIntf": vrrpCurCfgVirtRtrGrpTckIpIntf,
       "vrrpCurCfgVirtRtrGrpTckVlanPort": vrrpCurCfgVirtRtrGrpTckVlanPort,
       "vrrpCurCfgVirtRtrGrpTckL4Port": vrrpCurCfgVirtRtrGrpTckL4Port,
       "vrrpCurCfgVirtRtrGrpTckRServer": vrrpCurCfgVirtRtrGrpTckRServer,
       "vrrpCurCfgVirtRtrGrpTckHsrp": vrrpCurCfgVirtRtrGrpTckHsrp,
       "vrrpNewCfgVirtRtrGrpTable": vrrpNewCfgVirtRtrGrpTable,
       "vrrpNewCfgVirtRtrGrpTableEntry": vrrpNewCfgVirtRtrGrpTableEntry,
       "vrrpNewCfgVirtRtrGrpIndx": vrrpNewCfgVirtRtrGrpIndx,
       "vrrpNewCfgVirtRtrGrpID": vrrpNewCfgVirtRtrGrpID,
       "vrrpNewCfgVirtRtrGrpIfIndex": vrrpNewCfgVirtRtrGrpIfIndex,
       "vrrpNewCfgVirtRtrGrpInterval": vrrpNewCfgVirtRtrGrpInterval,
       "vrrpNewCfgVirtRtrGrpPriority": vrrpNewCfgVirtRtrGrpPriority,
       "vrrpNewCfgVirtRtrGrpPreempt": vrrpNewCfgVirtRtrGrpPreempt,
       "vrrpNewCfgVirtRtrGrpState": vrrpNewCfgVirtRtrGrpState,
       "vrrpNewCfgVirtRtrGrpDelete": vrrpNewCfgVirtRtrGrpDelete,
       "vrrpNewCfgVirtRtrGrpSharing": vrrpNewCfgVirtRtrGrpSharing,
       "vrrpNewCfgVirtRtrGrpTckVirtRtr": vrrpNewCfgVirtRtrGrpTckVirtRtr,
       "vrrpNewCfgVirtRtrGrpTckIpIntf": vrrpNewCfgVirtRtrGrpTckIpIntf,
       "vrrpNewCfgVirtRtrGrpTckVlanPort": vrrpNewCfgVirtRtrGrpTckVlanPort,
       "vrrpNewCfgVirtRtrGrpTckL4Port": vrrpNewCfgVirtRtrGrpTckL4Port,
       "vrrpNewCfgVirtRtrGrpTckRServer": vrrpNewCfgVirtRtrGrpTckRServer,
       "vrrpNewCfgVirtRtrGrpTckHsrp": vrrpNewCfgVirtRtrGrpTckHsrp,
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
       "bwm": bwm,
       "bwmGeneralConfig": bwmGeneralConfig,
       "bwmCurCfgGenState": bwmCurCfgGenState,
       "bwmNewCfgGenState": bwmNewCfgGenState,
       "bwmCurCfgGenEnforcePolicy": bwmCurCfgGenEnforcePolicy,
       "bwmNewCfgGenEnforcePolicy": bwmNewCfgGenEnforcePolicy,
       "bwmCurCfgGenSmtpUser": bwmCurCfgGenSmtpUser,
       "bwmNewCfgGenSmtpUser": bwmNewCfgGenSmtpUser,
       "bwmPolicyConfig": bwmPolicyConfig,
       "bwmPolicyTableMaxEnt": bwmPolicyTableMaxEnt,
       "bwmCurCfgPolicyTable": bwmCurCfgPolicyTable,
       "bwmCurCfgPolicyTableEntry": bwmCurCfgPolicyTableEntry,
       "bwmCurCfgPolicyIndx": bwmCurCfgPolicyIndx,
       "bwmCurCfgPolicyTosIn": bwmCurCfgPolicyTosIn,
       "bwmCurCfgPolicyTosOut": bwmCurCfgPolicyTosOut,
       "bwmCurCfgPolicyHard": bwmCurCfgPolicyHard,
       "bwmCurCfgPolicySoft": bwmCurCfgPolicySoft,
       "bwmCurCfgPolicyResv": bwmCurCfgPolicyResv,
       "bwmCurCfgPolicyBuffer": bwmCurCfgPolicyBuffer,
       "bwmNewCfgPolicyTable": bwmNewCfgPolicyTable,
       "bwmNewCfgPolicyTableEntry": bwmNewCfgPolicyTableEntry,
       "bwmNewCfgPolicyIndx": bwmNewCfgPolicyIndx,
       "bwmNewCfgPolicyTosIn": bwmNewCfgPolicyTosIn,
       "bwmNewCfgPolicyTosOut": bwmNewCfgPolicyTosOut,
       "bwmNewCfgPolicyHard": bwmNewCfgPolicyHard,
       "bwmNewCfgPolicySoft": bwmNewCfgPolicySoft,
       "bwmNewCfgPolicyResv": bwmNewCfgPolicyResv,
       "bwmNewCfgPolicyBuffer": bwmNewCfgPolicyBuffer,
       "bwmContractConfig": bwmContractConfig,
       "bwmContractTableMaxEnt": bwmContractTableMaxEnt,
       "bwmCurCfgContractTable": bwmCurCfgContractTable,
       "bwmCurCfgContractTableEntry": bwmCurCfgContractTableEntry,
       "bwmCurCfgContractIndx": bwmCurCfgContractIndx,
       "bwmCurCfgContractName": bwmCurCfgContractName,
       "bwmCurCfgContractState": bwmCurCfgContractState,
       "bwmCurCfgContractPolicy": bwmCurCfgContractPolicy,
       "bwmCurCfgContractPrec": bwmCurCfgContractPrec,
       "bwmCurCfgContractUseTos": bwmCurCfgContractUseTos,
       "bwmCurCfgContractHistory": bwmCurCfgContractHistory,
       "bwmNewCfgContractTable": bwmNewCfgContractTable,
       "bwmNewCfgContractTableEntry": bwmNewCfgContractTableEntry,
       "bwmNewCfgContractIndx": bwmNewCfgContractIndx,
       "bwmNewCfgContractName": bwmNewCfgContractName,
       "bwmNewCfgContractState": bwmNewCfgContractState,
       "bwmNewCfgContractPolicy": bwmNewCfgContractPolicy,
       "bwmNewCfgContractDelete": bwmNewCfgContractDelete,
       "bwmNewCfgContractPrec": bwmNewCfgContractPrec,
       "bwmNewCfgContractUseTos": bwmNewCfgContractUseTos,
       "bwmNewCfgContractHistory": bwmNewCfgContractHistory}
)
