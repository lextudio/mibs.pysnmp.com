# SNMP MIB module (BLADETYPE2-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADETYPE2-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:05 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(hpSwitchBladeType2_Mgmt,) = mibBuilder.importSymbols(
    "HP-SWITCH-PL-MIB",
    "hpSwitchBladeType2-Mgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentConfig_ObjectIdentity = ObjectIdentity
agentConfig = _AgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1)
)
_AgSystem_ObjectIdentity = ObjectIdentity
agSystem = _AgSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1)
)


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 2),
    _AgApplyConfiguration_Type()
)
agApplyConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agApplyConfiguration.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 3),
    _AgSavePending_Type()
)
agSavePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSavePending.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 4),
    _AgSaveConfiguration_Type()
)
agSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSaveConfiguration.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 5),
    _AgRevert_Type()
)
agRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRevert.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 6),
    _AgRevertApply_Type()
)
agRevertApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRevertApply.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 7),
    _AgReset_Type()
)
agReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agReset.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 8),
    _AgConfigForNxtReset_Type()
)
agConfigForNxtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agConfigForNxtReset.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 9),
    _AgImageForNxtReset_Type()
)
agImageForNxtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agImageForNxtReset.setStatus("current")


class _AgSoftwareVersion_Type(DisplayString):
    """Custom type agSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgSoftwareVersion_Type.__name__ = "DisplayString"
_AgSoftwareVersion_Object = MibScalar
agSoftwareVersion = _AgSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 10),
    _AgSoftwareVersion_Type()
)
agSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSoftwareVersion.setStatus("current")


class _AgBootVer_Type(DisplayString):
    """Custom type agBootVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgBootVer_Type.__name__ = "DisplayString"
_AgBootVer_Object = MibScalar
agBootVer = _AgBootVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 11),
    _AgBootVer_Type()
)
agBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agBootVer.setStatus("current")


class _AgImage1Ver_Type(DisplayString):
    """Custom type agImage1Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgImage1Ver_Type.__name__ = "DisplayString"
_AgImage1Ver_Object = MibScalar
agImage1Ver = _AgImage1Ver_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 12),
    _AgImage1Ver_Type()
)
agImage1Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agImage1Ver.setStatus("current")


class _AgImage2Ver_Type(DisplayString):
    """Custom type agImage2Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgImage2Ver_Type.__name__ = "DisplayString"
_AgImage2Ver_Object = MibScalar
agImage2Ver = _AgImage2Ver_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 13),
    _AgImage2Ver_Type()
)
agImage2Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agImage2Ver.setStatus("current")


class _AgRtcDate_Type(DisplayString):
    """Custom type agRtcDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgRtcDate_Type.__name__ = "DisplayString"
_AgRtcDate_Object = MibScalar
agRtcDate = _AgRtcDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 14),
    _AgRtcDate_Type()
)
agRtcDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRtcDate.setStatus("current")


class _AgRtcTime_Type(DisplayString):
    """Custom type agRtcTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgRtcTime_Type.__name__ = "DisplayString"
_AgRtcTime_Object = MibScalar
agRtcTime = _AgRtcTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 15),
    _AgRtcTime_Type()
)
agRtcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agRtcTime.setStatus("current")


class _AgLastSetErrorReason_Type(DisplayString):
    """Custom type agLastSetErrorReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgLastSetErrorReason_Type.__name__ = "DisplayString"
_AgLastSetErrorReason_Object = MibScalar
agLastSetErrorReason = _AgLastSetErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 16),
    _AgLastSetErrorReason_Type()
)
agLastSetErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agLastSetErrorReason.setStatus("current")


class _AgCurCfgHttpServerPort_Type(Integer32):
    """Custom type agCurCfgHttpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgCurCfgHttpServerPort_Type.__name__ = "Integer32"
_AgCurCfgHttpServerPort_Object = MibScalar
agCurCfgHttpServerPort = _AgCurCfgHttpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 17),
    _AgCurCfgHttpServerPort_Type()
)
agCurCfgHttpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgHttpServerPort.setStatus("current")


class _AgNewCfgHttpServerPort_Type(Integer32):
    """Custom type agNewCfgHttpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgHttpServerPort_Type.__name__ = "Integer32"
_AgNewCfgHttpServerPort_Object = MibScalar
agNewCfgHttpServerPort = _AgNewCfgHttpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 18),
    _AgNewCfgHttpServerPort_Type()
)
agNewCfgHttpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgHttpServerPort.setStatus("current")


class _AgCurCfgLoginBanner_Type(DisplayString):
    """Custom type agCurCfgLoginBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AgCurCfgLoginBanner_Type.__name__ = "DisplayString"
_AgCurCfgLoginBanner_Object = MibScalar
agCurCfgLoginBanner = _AgCurCfgLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 19),
    _AgCurCfgLoginBanner_Type()
)
agCurCfgLoginBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgLoginBanner.setStatus("current")


class _AgNewCfgLoginBanner_Type(DisplayString):
    """Custom type agNewCfgLoginBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AgNewCfgLoginBanner_Type.__name__ = "DisplayString"
_AgNewCfgLoginBanner_Object = MibScalar
agNewCfgLoginBanner = _AgNewCfgLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 20),
    _AgNewCfgLoginBanner_Type()
)
agNewCfgLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgLoginBanner.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 23),
    _AgCurCfgConsole_Type()
)
agCurCfgConsole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgConsole.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 24),
    _AgNewCfgConsole_Type()
)
agNewCfgConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgConsole.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 29),
    _AgCurCfgBootp_Type()
)
agCurCfgBootp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgBootp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 30),
    _AgNewCfgBootp_Type()
)
agNewCfgBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgBootp.setStatus("current")


class _AgSlotNumber_Type(Integer32):
    """Custom type agSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgSlotNumber_Type.__name__ = "Integer32"
_AgSlotNumber_Object = MibScalar
agSlotNumber = _AgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 31),
    _AgSlotNumber_Type()
)
agSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSlotNumber.setStatus("current")


class _AgCurCfgSnmpTimeout_Type(Integer32):
    """Custom type agCurCfgSnmpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgCurCfgSnmpTimeout_Type.__name__ = "Integer32"
_AgCurCfgSnmpTimeout_Object = MibScalar
agCurCfgSnmpTimeout = _AgCurCfgSnmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 32),
    _AgCurCfgSnmpTimeout_Type()
)
agCurCfgSnmpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSnmpTimeout.setStatus("current")


class _AgNewCfgSnmpTimeout_Type(Integer32):
    """Custom type agNewCfgSnmpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgNewCfgSnmpTimeout_Type.__name__ = "Integer32"
_AgNewCfgSnmpTimeout_Object = MibScalar
agNewCfgSnmpTimeout = _AgNewCfgSnmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 33),
    _AgNewCfgSnmpTimeout_Type()
)
agNewCfgSnmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSnmpTimeout.setStatus("current")


class _AgCurCfgTelnetServerPort_Type(Integer32):
    """Custom type agCurCfgTelnetServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgCurCfgTelnetServerPort_Type.__name__ = "Integer32"
_AgCurCfgTelnetServerPort_Object = MibScalar
agCurCfgTelnetServerPort = _AgCurCfgTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 34),
    _AgCurCfgTelnetServerPort_Type()
)
agCurCfgTelnetServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTelnetServerPort.setStatus("current")


class _AgNewCfgTelnetServerPort_Type(Integer32):
    """Custom type agNewCfgTelnetServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgTelnetServerPort_Type.__name__ = "Integer32"
_AgNewCfgTelnetServerPort_Object = MibScalar
agNewCfgTelnetServerPort = _AgNewCfgTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 35),
    _AgNewCfgTelnetServerPort_Type()
)
agNewCfgTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTelnetServerPort.setStatus("current")


class _AgClearFlashDump_Type(Integer32):
    """Custom type agClearFlashDump based on Integer32"""
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


_AgClearFlashDump_Type.__name__ = "Integer32"
_AgClearFlashDump_Object = MibScalar
agClearFlashDump = _AgClearFlashDump_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 36),
    _AgClearFlashDump_Type()
)
agClearFlashDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agClearFlashDump.setStatus("current")


class _AgRackId_Type(DisplayString):
    """Custom type agRackId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AgRackId_Type.__name__ = "DisplayString"
_AgRackId_Object = MibScalar
agRackId = _AgRackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 37),
    _AgRackId_Type()
)
agRackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRackId.setStatus("current")


class _AgChassis_Type(DisplayString):
    """Custom type agChassis based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AgChassis_Type.__name__ = "DisplayString"
_AgChassis_Object = MibScalar
agChassis = _AgChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 38),
    _AgChassis_Type()
)
agChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agChassis.setStatus("current")


class _AgCurCfgTftpServerPort_Type(Integer32):
    """Custom type agCurCfgTftpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgCurCfgTftpServerPort_Type.__name__ = "Integer32"
_AgCurCfgTftpServerPort_Object = MibScalar
agCurCfgTftpServerPort = _AgCurCfgTftpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 39),
    _AgCurCfgTftpServerPort_Type()
)
agCurCfgTftpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTftpServerPort.setStatus("current")


class _AgNewCfgTftpServerPort_Type(Integer32):
    """Custom type agNewCfgTftpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgTftpServerPort_Type.__name__ = "Integer32"
_AgNewCfgTftpServerPort_Object = MibScalar
agNewCfgTftpServerPort = _AgNewCfgTftpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 40),
    _AgNewCfgTftpServerPort_Type()
)
agNewCfgTftpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTftpServerPort.setStatus("current")


class _AgCurCfgHttpsServerPort_Type(Integer32):
    """Custom type agCurCfgHttpsServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgCurCfgHttpsServerPort_Type.__name__ = "Integer32"
_AgCurCfgHttpsServerPort_Object = MibScalar
agCurCfgHttpsServerPort = _AgCurCfgHttpsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 49),
    _AgCurCfgHttpsServerPort_Type()
)
agCurCfgHttpsServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgHttpsServerPort.setStatus("current")


class _AgNewCfgHttpsServerPort_Type(Integer32):
    """Custom type agNewCfgHttpsServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgHttpsServerPort_Type.__name__ = "Integer32"
_AgNewCfgHttpsServerPort_Object = MibScalar
agNewCfgHttpsServerPort = _AgNewCfgHttpsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 50),
    _AgNewCfgHttpsServerPort_Type()
)
agNewCfgHttpsServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgHttpsServerPort.setStatus("current")


class _AgCurDaylightSavings_Type(Integer32):
    """Custom type agCurDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420)
        )
    )
    namedValues = NamedValues(
        *(("africa-Algeria", 1),
          ("africa-Angola", 2),
          ("africa-Benin", 3),
          ("africa-Botswana", 4),
          ("africa-Burkina-Faso", 5),
          ("africa-Burundi", 6),
          ("africa-Cameroon", 7),
          ("africa-Central-African-Rep", 8),
          ("africa-Chad", 9),
          ("africa-Congo-EastDemRepCongo", 11),
          ("africa-Congo-Rep", 12),
          ("africa-Congo-WestDemRepCongo", 10),
          ("africa-Cote-dIvoire", 13),
          ("africa-Djibouti", 14),
          ("africa-Egypt", 15),
          ("africa-Equatorial-Guinea", 16),
          ("africa-Eritrea", 17),
          ("africa-Ethiopia", 18),
          ("africa-Gabon", 19),
          ("africa-Gambia", 20),
          ("africa-Ghana", 21),
          ("africa-Guinea", 22),
          ("africa-Guinea-Bissau", 23),
          ("africa-Kenya", 24),
          ("africa-Lesotho", 25),
          ("africa-Liberia", 26),
          ("africa-Libya", 27),
          ("africa-Malawi", 28),
          ("africa-Mali-NorthEastMali", 30),
          ("africa-Mali-SouthWestMali", 29),
          ("africa-Mauritania", 31),
          ("africa-Morocco", 32),
          ("africa-Mozambique", 33),
          ("africa-Namibia", 34),
          ("africa-Niger", 35),
          ("africa-Nigeria", 36),
          ("africa-Rwanda", 37),
          ("africa-SaoTome-And-Principe", 38),
          ("africa-Senegal", 39),
          ("africa-SierraLeone", 40),
          ("africa-Somalia", 41),
          ("africa-SouthAfrica", 42),
          ("africa-Spain-CanaryIslands", 45),
          ("africa-Spain-CeutaMelilla", 44),
          ("africa-Spain-Mainland", 43),
          ("africa-Sudan", 46),
          ("africa-Swaziland", 47),
          ("africa-Tanzania", 48),
          ("africa-Togo", 49),
          ("africa-Tunisia", 50),
          ("africa-Uganda", 51),
          ("africa-Western-Sahara", 52),
          ("africa-Zambia", 53),
          ("africa-Zimbabwe", 54),
          ("americas-Anguilla", 55),
          ("americas-Antigua-Barbuda", 56),
          ("americas-Argentina-Catamarca", 60),
          ("americas-Argentina-EArgentina", 57),
          ("americas-Argentina-Jujuy", 59),
          ("americas-Argentina-Mendoza", 61),
          ("americas-Argentina-MostLocations", 58),
          ("americas-Aruba", 62),
          ("americas-Bahamas", 63),
          ("americas-Barbados", 64),
          ("americas-Belize", 65),
          ("americas-Bolivia", 66),
          ("americas-Brazil-Acre", 79),
          ("americas-Brazil-AlagoasSergipe", 72),
          ("americas-Brazil-AmapaEPara", 68),
          ("americas-Brazil-AtlanticIslands", 67),
          ("americas-Brazil-EAmazonas", 77),
          ("americas-Brazil-MatoGrossoDoSul", 74),
          ("americas-Brazil-NEBrazil", 69),
          ("americas-Brazil-Pernambuco", 70),
          ("americas-Brazil-Roraima", 76),
          ("americas-Brazil-SSEBrazil", 73),
          ("americas-Brazil-Tocantins", 71),
          ("americas-Brazil-WAmazonas", 78),
          ("americas-Brazil-WParaRondonia", 75),
          ("americas-Canada-AtlanTime-ELabrador", 82),
          ("americas-Canada-AtlanTime-NovaScotia", 81),
          ("americas-Canada-CenStdTime-SaskatchewanMidwest", 92),
          ("americas-Canada-CenStdTime-SaskatchewanMostlocation", 91),
          ("americas-Canada-CenTime-ManitobaWestOntario", 88),
          ("americas-Canada-CenTime-RainyRiver", 89),
          ("americas-Canada-CenTime-WestNunavut", 90),
          ("americas-Canada-EastStdTime-CenNunavut", 87),
          ("americas-Canada-EastStdTime-EastNunavut", 86),
          ("americas-Canada-EastStdTime-PangnirtungNunavut", 85),
          ("americas-Canada-EastTime-OntarioMostlocation", 83),
          ("americas-Canada-EastTime-ThunderBay", 84),
          ("americas-Canada-MountStdTime-DawsonCreekFortSaintJohnBritishColumbia", 96),
          ("americas-Canada-MountTime-AlbertaEastBritishColumbia", 93),
          ("americas-Canada-MountTime-CentralNorthwestTerritories", 94),
          ("americas-Canada-MountTime-WestNorthwestTerritories", 95),
          ("americas-Canada-NewfoundlandIsland", 80),
          ("americas-Canada-PacificTime-NorthYukon", 99),
          ("americas-Canada-PacificTime-SouthYukon", 98),
          ("americas-Canada-PacificTime-WestBritishColumbia", 97),
          ("americas-CaymanIslands", 100),
          ("americas-Chile-EasterIsland", 102),
          ("americas-Chile-MostLocation", 101),
          ("americas-Colombia", 103),
          ("americas-CostaRica", 104),
          ("americas-Cuba", 105),
          ("americas-Dominica", 106),
          ("americas-DominicanRepublic", 107),
          ("americas-Ecuador", 108),
          ("americas-ElSalvado", 109),
          ("americas-FrenchGuiana", 110),
          ("americas-Greenland-EastCoastNorthScoresbysund", 112),
          ("americas-Greenland-MostLocation", 111),
          ("americas-Greenland-ScoresbysundIttoqqortoormiit", 113),
          ("americas-Greenland-ThulePituffik", 114),
          ("americas-Grenada", 115),
          ("americas-Guadeloupe", 116),
          ("americas-Guatemala", 117),
          ("americas-Guyana", 118),
          ("americas-Haiti", 119),
          ("americas-Honduras", 120),
          ("americas-Jamaica", 121),
          ("americas-Martinique", 122),
          ("americas-Mexico-CentTime-CampecheYucatan", 125),
          ("americas-Mexico-CentTime-CoahuilaDurangoNuevoLeonTamaulipas", 126),
          ("americas-Mexico-CentTime-Mostlocations", 123),
          ("americas-Mexico-CentTime-QuintanaRoo", 124),
          ("americas-Mexico-MountStdTime-Sonora", 129),
          ("americas-Mexico-MountTime-Chihuahua", 128),
          ("americas-Mexico-MountTime-SBajaNayaritSinaloa", 127),
          ("americas-Mexico-PacificTime", 130),
          ("americas-Montserrat", 131),
          ("americas-NetherlandsAntilles", 132),
          ("americas-Nicaragua", 133),
          ("americas-Panama", 134),
          ("americas-Paraguay", 135),
          ("americas-Peru", 136),
          ("americas-PuertoRico", 137),
          ("americas-StKittsAndNevis", 138),
          ("americas-StLucia", 139),
          ("americas-StPierreAndMiquelon", 140),
          ("americas-StVincent", 141),
          ("americas-Suriname", 142),
          ("americas-TrinidadAndTobago", 143),
          ("americas-TurksAndCaicosIs", 144),
          ("americas-USA-AlaskaTime", 161),
          ("americas-USA-AlaskaTime-AlaskaPanhandle", 162),
          ("americas-USA-AlaskaTime-AlaskaPanhandleNeck", 163),
          ("americas-USA-AlaskaTime-WestAlaska", 164),
          ("americas-USA-AleutianIslands", 165),
          ("americas-USA-CentTime", 153),
          ("americas-USA-CentTime-MichiganWisconsinborder", 154),
          ("americas-USA-CentTime-NorthDakotaOliverCounty", 155),
          ("americas-USA-EastStdTime-IndianaCrawfordCounty", 150),
          ("americas-USA-EastStdTime-IndianaMostLocations", 149),
          ("americas-USA-EastStdTime-IndianaStarkeCounty", 151),
          ("americas-USA-EastStdTime-IndianaSwitzerlandCounty", 152),
          ("americas-USA-EastTime", 145),
          ("americas-USA-EastTime-KentuckyLouisvilleArea", 147),
          ("americas-USA-EastTime-KentuckyWayneCounty", 148),
          ("americas-USA-EastTime-MichiganMostLocation", 146),
          ("americas-USA-Hawaii", 166),
          ("americas-USA-MountStdTime-Arizona", 159),
          ("americas-USA-MountTime", 156),
          ("americas-USA-MountTime-Navajo", 158),
          ("americas-USA-MountTime-SouthIdahoAndEastOregon", 157),
          ("americas-USA-PacificTime", 160),
          ("americas-Uruguay", 167),
          ("americas-Venezuela", 168),
          ("americas-VirginIslands-UK", 169),
          ("americas-VirginIslands-US", 170),
          ("antarctica-Amundsen-ScottStationSouthPole", 172),
          ("antarctica-CaseyStationBaileyPeninsula", 176),
          ("antarctica-DavisStationVestfoldHills", 175),
          ("antarctica-Dumont-dUrvilleBaseTerreAdelie", 178),
          ("antarctica-MawsonStationHolmeBay", 174),
          ("antarctica-McMurdoStationRossIsland", 171),
          ("antarctica-PalmerStationAnversIsland", 173),
          ("antarctica-SyowaStationEOngulI", 179),
          ("antarctica-VostokStationSMagneticPole", 177),
          ("arcticOcean-JanMayen", 181),
          ("arcticOcean-Svalbard", 180),
          ("asia-Afghanistan", 182),
          ("asia-Armenia", 183),
          ("asia-Azerbaijan", 184),
          ("asia-Bahrain", 185),
          ("asia-Bangladesh", 186),
          ("asia-Bhutan", 187),
          ("asia-Brunei", 188),
          ("asia-Cambodia", 189),
          ("asia-China-CentralChinaGansuGuizhouSichuanYunnan", 192),
          ("asia-China-EastChinaBeijingGuangdongShanghai", 190),
          ("asia-China-Heilongjiang", 191),
          ("asia-China-SouthwestXinjiangUyghur", 194),
          ("asia-China-TibetmostofXinjiangUyghur", 193),
          ("asia-Cyprus", 195),
          ("asia-EastTimor", 196),
          ("asia-Georgia", 197),
          ("asia-HongKong", 198),
          ("asia-India", 199),
          ("asia-Indonesia-EastSouthBorneoCelebesBaliNusaTengarraWestTimor", 202),
          ("asia-Indonesia-IrianJayaAndMoluccas", 203),
          ("asia-Indonesia-JavaAndSumatra", 200),
          ("asia-Indonesia-WestCentralBorneo", 201),
          ("asia-Iran", 204),
          ("asia-Iraq", 205),
          ("asia-Israel", 206),
          ("asia-Japan", 207),
          ("asia-Jordan", 208),
          ("asia-Kazakhstan-Aqtobe", 211),
          ("asia-Kazakhstan-AtyrauMangghystau", 212),
          ("asia-Kazakhstan-MostLocations", 209),
          ("asia-Kazakhstan-QyzylordaKyzylorda", 210),
          ("asia-Kazakhstan-WestKazakhstan", 213),
          ("asia-Korea-North", 214),
          ("asia-Korea-South", 215),
          ("asia-Kuwait", 216),
          ("asia-Kyrgyzstan", 217),
          ("asia-Laos", 218),
          ("asia-Lebanon", 219),
          ("asia-Macau", 220),
          ("asia-Malaysia-PeninsularMalaysia", 221),
          ("asia-Malaysia-SabahSarawak", 222),
          ("asia-Mongolia-BayanOlgiyGoviAltaiHovdUvsZavkhan", 224),
          ("asia-Mongolia-DornodSukhbaatar", 225),
          ("asia-Mongolia-MostLocations", 223),
          ("asia-Myanmar", 226),
          ("asia-Nepal", 227),
          ("asia-Oman", 228),
          ("asia-Pakistan", 229),
          ("asia-Palestine", 230),
          ("asia-Philippines", 231),
          ("asia-Qatar", 232),
          ("asia-Russia-Moscow-01Kaliningrad", 233),
          ("asia-Russia-Moscow00WestRussia", 234),
          ("asia-Russia-Moscow01CaspianSea", 235),
          ("asia-Russia-Moscow02Urals", 236),
          ("asia-Russia-Moscow03Novosibirsk", 238),
          ("asia-Russia-Moscow03WestSiberia", 237),
          ("asia-Russia-Moscow04YeniseiRiver", 239),
          ("asia-Russia-Moscow05LakeBaikal", 240),
          ("asia-Russia-Moscow06LenaRiver", 241),
          ("asia-Russia-Moscow07AmurRiver", 242),
          ("asia-Russia-Moscow07SakhalinIsland", 243),
          ("asia-Russia-Moscow08Magadan", 244),
          ("asia-Russia-Moscow09Kamchatka", 245),
          ("asia-Russia-Moscow10BeringSea", 246),
          ("asia-SaudiArabia", 247),
          ("asia-Singapore", 248),
          ("asia-SriLanka", 249),
          ("asia-Syria", 250),
          ("asia-Taiwan", 251),
          ("asia-Tajikistan", 252),
          ("asia-Thailand", 253),
          ("asia-Turkmenistan", 254),
          ("asia-UnitedArabEmirates", 255),
          ("asia-Uzbekistan-EastUzbekistan", 257),
          ("asia-Uzbekistan-WestUzbekistan", 256),
          ("asia-Vietnam", 258),
          ("asia-Yemen", 259),
          ("atlanticOcean-Bermuda", 260),
          ("atlanticOcean-CapeVerde", 261),
          ("atlanticOcean-FaeroeIslands", 262),
          ("atlanticOcean-FalklandIslands", 263),
          ("atlanticOcean-Iceland", 264),
          ("atlanticOcean-Portugal-Azores", 267),
          ("atlanticOcean-Portugal-MadeiraIslands", 266),
          ("atlanticOcean-Portugal-Mainland", 265),
          ("atlanticOcean-SouthGeorgia-SouthSandwichIslands", 268),
          ("atlanticOcean-Spain-CanaryIslands", 271),
          ("atlanticOcean-Spain-CeutaMelilla", 270),
          ("atlanticOcean-Spain-Mainland", 269),
          ("atlanticOcean-StHelena", 272),
          ("atlanticOcean-Svalbard-JanMayen", 273),
          ("australia-LordHoweIsland", 274),
          ("australia-NewSouthWales-MostLocations", 277),
          ("australia-NewSouthWales-Yancowinna", 278),
          ("australia-NorthernTerritory", 282),
          ("australia-Queensland-HolidayIslands", 280),
          ("australia-Queensland-MostLocations", 279),
          ("australia-SouthAustralia", 281),
          ("australia-Tasmania", 275),
          ("australia-Victoria", 276),
          ("australia-WesternAustralia", 283),
          ("europe-Albania", 284),
          ("europe-Andorra", 285),
          ("europe-Austria", 286),
          ("europe-Belarus", 287),
          ("europe-Belgium", 288),
          ("europe-BosniaHerzegovina", 289),
          ("europe-Britain-UKGreatBritain", 290),
          ("europe-Britain-UKNorthernIreland", 291),
          ("europe-Bulgaria", 292),
          ("europe-Croatia", 293),
          ("europe-CzechRepublic", 294),
          ("europe-Denmark", 295),
          ("europe-Estonia", 296),
          ("europe-Finland", 297),
          ("europe-France", 298),
          ("europe-Germany", 299),
          ("europe-Gibraltar", 300),
          ("europe-Greece", 301),
          ("europe-Hungary", 302),
          ("europe-Ireland", 303),
          ("europe-Italy", 304),
          ("europe-Latvia", 305),
          ("europe-Liechtenstein", 306),
          ("europe-Lithuania", 307),
          ("europe-Luxembourg", 308),
          ("europe-Macedonia", 309),
          ("europe-Malta", 310),
          ("europe-Moldova", 311),
          ("europe-Monaco", 312),
          ("europe-Netherlands", 313),
          ("europe-Norway", 314),
          ("europe-Poland", 315),
          ("europe-Portugal-Azores", 318),
          ("europe-Portugal-MadeiraIslands", 317),
          ("europe-Portugal-Mainland", 316),
          ("europe-Romania", 319),
          ("europe-Russia-Moscow-01Kaliningrad", 320),
          ("europe-Russia-Moscow00WestRussia", 321),
          ("europe-Russia-Moscow01CaspianSea", 322),
          ("europe-Russia-Moscow02Urals", 323),
          ("europe-Russia-Moscow03Novosibirsk", 325),
          ("europe-Russia-Moscow03WestSiberia", 324),
          ("europe-Russia-Moscow04YeniseiRiver", 326),
          ("europe-Russia-Moscow05LakeBaikal", 327),
          ("europe-Russia-Moscow06LenaRiver", 328),
          ("europe-Russia-Moscow07AmurRiver", 329),
          ("europe-Russia-Moscow07SakhalinIsland", 330),
          ("europe-Russia-Moscow08Magadan", 331),
          ("europe-Russia-Moscow09Kamchatka", 332),
          ("europe-Russia-Moscow10BeringSea", 333),
          ("europe-SanMarino", 334),
          ("europe-Slovakia", 335),
          ("europe-Slovenia", 336),
          ("europe-Spain-CanaryIslands", 339),
          ("europe-Spain-CeutaAndMelilla", 338),
          ("europe-Spain-Mainland", 337),
          ("europe-Sweden", 340),
          ("europe-Switzerland", 341),
          ("europe-Turkey", 342),
          ("europe-Ukraine-CentralCrimea", 346),
          ("europe-Ukraine-MostLocations", 343),
          ("europe-Ukraine-Ruthenia", 344),
          ("europe-Ukraine-Zaporozhye-ELugansk", 345),
          ("europe-VaticanCity", 347),
          ("europe-Yugoslavia", 348),
          ("indianOcean-BritishIndianOceanTerritory", 349),
          ("indianOcean-ChristmasIsland", 350),
          ("indianOcean-CocosOrKeelingIslands", 351),
          ("indianOcean-Comoros", 352),
          ("indianOcean-FrenchSouthernAndAntarcticLands", 353),
          ("indianOcean-Madagascar", 354),
          ("indianOcean-Maldives", 355),
          ("indianOcean-Mauritius", 356),
          ("indianOcean-Mayotte", 357),
          ("indianOcean-Reunion", 358),
          ("indianOcean-Seychelles", 359),
          ("none", 0),
          ("pacificOcean-Chile-EasterIslandSalayGomez", 361),
          ("pacificOcean-Chile-MostLocations", 360),
          ("pacificOcean-CookIslands", 362),
          ("pacificOcean-Ecuador", 363),
          ("pacificOcean-Fiji", 364),
          ("pacificOcean-FrenchPolynesia-GambierIslands", 367),
          ("pacificOcean-FrenchPolynesia-MarquesasIslands", 366),
          ("pacificOcean-FrenchPolynesia-SocietyIslands", 365),
          ("pacificOcean-Guam", 368),
          ("pacificOcean-Kiribati-GilbertIslands", 369),
          ("pacificOcean-Kiribati-LineIslands", 371),
          ("pacificOcean-Kiribati-PhoenixIslands", 370),
          ("pacificOcean-MarshallIslands-Kwajalein", 373),
          ("pacificOcean-MarshallIslands-MostLocations", 372),
          ("pacificOcean-Micronesia-Kosrae", 377),
          ("pacificOcean-Micronesia-PonapeOrPohnpei", 376),
          ("pacificOcean-Micronesia-TrukOrChuuk", 375),
          ("pacificOcean-Micronesia-Yap", 374),
          ("pacificOcean-Nauru", 378),
          ("pacificOcean-NewCaledonia", 379),
          ("pacificOcean-NewZealand-ChathamIslands", 381),
          ("pacificOcean-NewZealand-MostLocations", 380),
          ("pacificOcean-Niue", 382),
          ("pacificOcean-NorfolkIsland", 383),
          ("pacificOcean-NorthernMarianaIslands", 384),
          ("pacificOcean-Palau", 385),
          ("pacificOcean-PapuaNewGuinea", 386),
          ("pacificOcean-Pitcairn", 387),
          ("pacificOcean-SamoaAmerican", 388),
          ("pacificOcean-SamoaWestern", 389),
          ("pacificOcean-SolomonIslands", 390),
          ("pacificOcean-Tokelau", 391),
          ("pacificOcean-Tonga", 392),
          ("pacificOcean-Tuvalu", 393),
          ("pacificOcean-USMinorOutlyingIslands-JohnstonAtoll", 416),
          ("pacificOcean-USMinorOutlyingIslands-MidwayIslands", 417),
          ("pacificOcean-USMinorOutlyingIslands-WakeIsland", 418),
          ("pacificOcean-Vanuatu", 419),
          ("pacificOcean-WallisAndFutuna", 420),
          ("pacificOceanUSA-AlaskaTime", 410),
          ("pacificOceanUSA-AlaskaTime-AlaskaPanhandle", 411),
          ("pacificOceanUSA-AlaskaTime-AlaskaPanhandleNeck", 412),
          ("pacificOceanUSA-AlaskaTime-WestAlaska", 413),
          ("pacificOceanUSA-AleutianIslands", 414),
          ("pacificOceanUSA-CentTime", 402),
          ("pacificOceanUSA-CentTime-MichiganWisconsinborder", 403),
          ("pacificOceanUSA-CentTime-NorthDakotaOliverCounty", 404),
          ("pacificOceanUSA-EastStdTime-IndianaCrawfordCounty", 399),
          ("pacificOceanUSA-EastStdTime-IndianaMostLocations", 398),
          ("pacificOceanUSA-EastStdTime-IndianaStarkeCounty", 400),
          ("pacificOceanUSA-EastStdTime-IndianaSwitzerlandCounty", 401),
          ("pacificOceanUSA-EastTime", 394),
          ("pacificOceanUSA-EastTime-KentuckyLouisvilleArea", 396),
          ("pacificOceanUSA-EastTime-KentuckyWayneCounty", 397),
          ("pacificOceanUSA-EastTime-MichiganMostLocations", 395),
          ("pacificOceanUSA-Hawaii", 415),
          ("pacificOceanUSA-MountStdTime-Arizona", 408),
          ("pacificOceanUSA-MountTime", 405),
          ("pacificOceanUSA-MountTime-Navajo", 407),
          ("pacificOceanUSA-MountTime-SouthIdahoAndEastOregon", 406),
          ("pacificOceanUSA-PacificTime", 409))
    )


_AgCurDaylightSavings_Type.__name__ = "Integer32"
_AgCurDaylightSavings_Object = MibScalar
agCurDaylightSavings = _AgCurDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 51),
    _AgCurDaylightSavings_Type()
)
agCurDaylightSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurDaylightSavings.setStatus("current")


class _AgNewDaylightSavings_Type(Integer32):
    """Custom type agNewDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420)
        )
    )
    namedValues = NamedValues(
        *(("africa-Algeria", 1),
          ("africa-Angola", 2),
          ("africa-Benin", 3),
          ("africa-Botswana", 4),
          ("africa-Burkina-Faso", 5),
          ("africa-Burundi", 6),
          ("africa-Cameroon", 7),
          ("africa-Central-African-Rep", 8),
          ("africa-Chad", 9),
          ("africa-Congo-EastDemRepCongo", 11),
          ("africa-Congo-Rep", 12),
          ("africa-Congo-WestDemRepCongo", 10),
          ("africa-Cote-dIvoire", 13),
          ("africa-Djibouti", 14),
          ("africa-Egypt", 15),
          ("africa-Equatorial-Guinea", 16),
          ("africa-Eritrea", 17),
          ("africa-Ethiopia", 18),
          ("africa-Gabon", 19),
          ("africa-Gambia", 20),
          ("africa-Ghana", 21),
          ("africa-Guinea", 22),
          ("africa-Guinea-Bissau", 23),
          ("africa-Kenya", 24),
          ("africa-Lesotho", 25),
          ("africa-Liberia", 26),
          ("africa-Libya", 27),
          ("africa-Malawi", 28),
          ("africa-Mali-NorthEastMali", 30),
          ("africa-Mali-SouthWestMali", 29),
          ("africa-Mauritania", 31),
          ("africa-Morocco", 32),
          ("africa-Mozambique", 33),
          ("africa-Namibia", 34),
          ("africa-Niger", 35),
          ("africa-Nigeria", 36),
          ("africa-Rwanda", 37),
          ("africa-SaoTome-And-Principe", 38),
          ("africa-Senegal", 39),
          ("africa-SierraLeone", 40),
          ("africa-Somalia", 41),
          ("africa-SouthAfrica", 42),
          ("africa-Spain-CanaryIslands", 45),
          ("africa-Spain-CeutaMelilla", 44),
          ("africa-Spain-Mainland", 43),
          ("africa-Sudan", 46),
          ("africa-Swaziland", 47),
          ("africa-Tanzania", 48),
          ("africa-Togo", 49),
          ("africa-Tunisia", 50),
          ("africa-Uganda", 51),
          ("africa-Western-Sahara", 52),
          ("africa-Zambia", 53),
          ("africa-Zimbabwe", 54),
          ("americas-Anguilla", 55),
          ("americas-Antigua-Barbuda", 56),
          ("americas-Argentina-Catamarca", 60),
          ("americas-Argentina-EArgentina", 57),
          ("americas-Argentina-Jujuy", 59),
          ("americas-Argentina-Mendoza", 61),
          ("americas-Argentina-MostLocations", 58),
          ("americas-Aruba", 62),
          ("americas-Bahamas", 63),
          ("americas-Barbados", 64),
          ("americas-Belize", 65),
          ("americas-Bolivia", 66),
          ("americas-Brazil-Acre", 79),
          ("americas-Brazil-AlagoasSergipe", 72),
          ("americas-Brazil-AmapaEPara", 68),
          ("americas-Brazil-AtlanticIslands", 67),
          ("americas-Brazil-EAmazonas", 77),
          ("americas-Brazil-MatoGrossoDoSul", 74),
          ("americas-Brazil-NEBrazil", 69),
          ("americas-Brazil-Pernambuco", 70),
          ("americas-Brazil-Roraima", 76),
          ("americas-Brazil-SSEBrazil", 73),
          ("americas-Brazil-Tocantins", 71),
          ("americas-Brazil-WAmazonas", 78),
          ("americas-Brazil-WParaRondonia", 75),
          ("americas-Canada-AtlanTime-ELabrador", 82),
          ("americas-Canada-AtlanTime-NovaScotia", 81),
          ("americas-Canada-CenStdTime-SaskatchewanMidwest", 92),
          ("americas-Canada-CenStdTime-SaskatchewanMostlocation", 91),
          ("americas-Canada-CenTime-ManitobaWestOntario", 88),
          ("americas-Canada-CenTime-RainyRiver", 89),
          ("americas-Canada-CenTime-WestNunavut", 90),
          ("americas-Canada-EastStdTime-CenNunavut", 87),
          ("americas-Canada-EastStdTime-EastNunavut", 86),
          ("americas-Canada-EastStdTime-PangnirtungNunavut", 85),
          ("americas-Canada-EastTime-OntarioMostlocation", 83),
          ("americas-Canada-EastTime-ThunderBay", 84),
          ("americas-Canada-MountStdTime-DawsonCreekFortSaintJohnBritishColumbia", 96),
          ("americas-Canada-MountTime-AlbertaEastBritishColumbia", 93),
          ("americas-Canada-MountTime-CentralNorthwestTerritories", 94),
          ("americas-Canada-MountTime-WestNorthwestTerritories", 95),
          ("americas-Canada-NewfoundlandIsland", 80),
          ("americas-Canada-PacificTime-NorthYukon", 99),
          ("americas-Canada-PacificTime-SouthYukon", 98),
          ("americas-Canada-PacificTime-WestBritishColumbia", 97),
          ("americas-CaymanIslands", 100),
          ("americas-Chile-EasterIsland", 102),
          ("americas-Chile-MostLocation", 101),
          ("americas-Colombia", 103),
          ("americas-CostaRica", 104),
          ("americas-Cuba", 105),
          ("americas-Dominica", 106),
          ("americas-DominicanRepublic", 107),
          ("americas-Ecuador", 108),
          ("americas-ElSalvado", 109),
          ("americas-FrenchGuiana", 110),
          ("americas-Greenland-EastCoastNorthScoresbysund", 112),
          ("americas-Greenland-MostLocation", 111),
          ("americas-Greenland-ScoresbysundIttoqqortoormiit", 113),
          ("americas-Greenland-ThulePituffik", 114),
          ("americas-Grenada", 115),
          ("americas-Guadeloupe", 116),
          ("americas-Guatemala", 117),
          ("americas-Guyana", 118),
          ("americas-Haiti", 119),
          ("americas-Honduras", 120),
          ("americas-Jamaica", 121),
          ("americas-Martinique", 122),
          ("americas-Mexico-CentTime-CampecheYucatan", 125),
          ("americas-Mexico-CentTime-CoahuilaDurangoNuevoLeonTamaulipas", 126),
          ("americas-Mexico-CentTime-Mostlocations", 123),
          ("americas-Mexico-CentTime-QuintanaRoo", 124),
          ("americas-Mexico-MountStdTime-Sonora", 129),
          ("americas-Mexico-MountTime-Chihuahua", 128),
          ("americas-Mexico-MountTime-SBajaNayaritSinaloa", 127),
          ("americas-Mexico-PacificTime", 130),
          ("americas-Montserrat", 131),
          ("americas-NetherlandsAntilles", 132),
          ("americas-Nicaragua", 133),
          ("americas-Panama", 134),
          ("americas-Paraguay", 135),
          ("americas-Peru", 136),
          ("americas-PuertoRico", 137),
          ("americas-StKittsAndNevis", 138),
          ("americas-StLucia", 139),
          ("americas-StPierreAndMiquelon", 140),
          ("americas-StVincent", 141),
          ("americas-Suriname", 142),
          ("americas-TrinidadAndTobago", 143),
          ("americas-TurksAndCaicosIs", 144),
          ("americas-USA-AlaskaTime", 161),
          ("americas-USA-AlaskaTime-AlaskaPanhandle", 162),
          ("americas-USA-AlaskaTime-AlaskaPanhandleNeck", 163),
          ("americas-USA-AlaskaTime-WestAlaska", 164),
          ("americas-USA-AleutianIslands", 165),
          ("americas-USA-CentTime", 153),
          ("americas-USA-CentTime-MichiganWisconsinborder", 154),
          ("americas-USA-CentTime-NorthDakotaOliverCounty", 155),
          ("americas-USA-EastStdTime-IndianaCrawfordCounty", 150),
          ("americas-USA-EastStdTime-IndianaMostLocations", 149),
          ("americas-USA-EastStdTime-IndianaStarkeCounty", 151),
          ("americas-USA-EastStdTime-IndianaSwitzerlandCounty", 152),
          ("americas-USA-EastTime", 145),
          ("americas-USA-EastTime-KentuckyLouisvilleArea", 147),
          ("americas-USA-EastTime-KentuckyWayneCounty", 148),
          ("americas-USA-EastTime-MichiganMostLocation", 146),
          ("americas-USA-Hawaii", 166),
          ("americas-USA-MountStdTime-Arizona", 159),
          ("americas-USA-MountTime", 156),
          ("americas-USA-MountTime-Navajo", 158),
          ("americas-USA-MountTime-SouthIdahoAndEastOregon", 157),
          ("americas-USA-PacificTime", 160),
          ("americas-Uruguay", 167),
          ("americas-Venezuela", 168),
          ("americas-VirginIslands-UK", 169),
          ("americas-VirginIslands-US", 170),
          ("antarctica-Amundsen-ScottStationSouthPole", 172),
          ("antarctica-CaseyStationBaileyPeninsula", 176),
          ("antarctica-DavisStationVestfoldHills", 175),
          ("antarctica-Dumont-dUrvilleBaseTerreAdelie", 178),
          ("antarctica-MawsonStationHolmeBay", 174),
          ("antarctica-McMurdoStationRossIsland", 171),
          ("antarctica-PalmerStationAnversIsland", 173),
          ("antarctica-SyowaStationEOngulI", 179),
          ("antarctica-VostokStationSMagneticPole", 177),
          ("arcticOcean-JanMayen", 181),
          ("arcticOcean-Svalbard", 180),
          ("asia-Afghanistan", 182),
          ("asia-Armenia", 183),
          ("asia-Azerbaijan", 184),
          ("asia-Bahrain", 185),
          ("asia-Bangladesh", 186),
          ("asia-Bhutan", 187),
          ("asia-Brunei", 188),
          ("asia-Cambodia", 189),
          ("asia-China-CentralChinaGansuGuizhouSichuanYunnan", 192),
          ("asia-China-EastChinaBeijingGuangdongShanghai", 190),
          ("asia-China-Heilongjiang", 191),
          ("asia-China-SouthwestXinjiangUyghur", 194),
          ("asia-China-TibetmostofXinjiangUyghur", 193),
          ("asia-Cyprus", 195),
          ("asia-EastTimor", 196),
          ("asia-Georgia", 197),
          ("asia-HongKong", 198),
          ("asia-India", 199),
          ("asia-Indonesia-EastSouthBorneoCelebesBaliNusaTengarraWestTimor", 202),
          ("asia-Indonesia-IrianJayaAndMoluccas", 203),
          ("asia-Indonesia-JavaAndSumatra", 200),
          ("asia-Indonesia-WestCentralBorneo", 201),
          ("asia-Iran", 204),
          ("asia-Iraq", 205),
          ("asia-Israel", 206),
          ("asia-Japan", 207),
          ("asia-Jordan", 208),
          ("asia-Kazakhstan-Aqtobe", 211),
          ("asia-Kazakhstan-AtyrauMangghystau", 212),
          ("asia-Kazakhstan-MostLocations", 209),
          ("asia-Kazakhstan-QyzylordaKyzylorda", 210),
          ("asia-Kazakhstan-WestKazakhstan", 213),
          ("asia-Korea-North", 214),
          ("asia-Korea-South", 215),
          ("asia-Kuwait", 216),
          ("asia-Kyrgyzstan", 217),
          ("asia-Laos", 218),
          ("asia-Lebanon", 219),
          ("asia-Macau", 220),
          ("asia-Malaysia-PeninsularMalaysia", 221),
          ("asia-Malaysia-SabahSarawak", 222),
          ("asia-Mongolia-BayanOlgiyGoviAltaiHovdUvsZavkhan", 224),
          ("asia-Mongolia-DornodSukhbaatar", 225),
          ("asia-Mongolia-MostLocations", 223),
          ("asia-Myanmar", 226),
          ("asia-Nepal", 227),
          ("asia-Oman", 228),
          ("asia-Pakistan", 229),
          ("asia-Palestine", 230),
          ("asia-Philippines", 231),
          ("asia-Qatar", 232),
          ("asia-Russia-Moscow-01Kaliningrad", 233),
          ("asia-Russia-Moscow00WestRussia", 234),
          ("asia-Russia-Moscow01CaspianSea", 235),
          ("asia-Russia-Moscow02Urals", 236),
          ("asia-Russia-Moscow03Novosibirsk", 238),
          ("asia-Russia-Moscow03WestSiberia", 237),
          ("asia-Russia-Moscow04YeniseiRiver", 239),
          ("asia-Russia-Moscow05LakeBaikal", 240),
          ("asia-Russia-Moscow06LenaRiver", 241),
          ("asia-Russia-Moscow07AmurRiver", 242),
          ("asia-Russia-Moscow07SakhalinIsland", 243),
          ("asia-Russia-Moscow08Magadan", 244),
          ("asia-Russia-Moscow09Kamchatka", 245),
          ("asia-Russia-Moscow10BeringSea", 246),
          ("asia-SaudiArabia", 247),
          ("asia-Singapore", 248),
          ("asia-SriLanka", 249),
          ("asia-Syria", 250),
          ("asia-Taiwan", 251),
          ("asia-Tajikistan", 252),
          ("asia-Thailand", 253),
          ("asia-Turkmenistan", 254),
          ("asia-UnitedArabEmirates", 255),
          ("asia-Uzbekistan-EastUzbekistan", 257),
          ("asia-Uzbekistan-WestUzbekistan", 256),
          ("asia-Vietnam", 258),
          ("asia-Yemen", 259),
          ("atlanticOcean-Bermuda", 260),
          ("atlanticOcean-CapeVerde", 261),
          ("atlanticOcean-FaeroeIslands", 262),
          ("atlanticOcean-FalklandIslands", 263),
          ("atlanticOcean-Iceland", 264),
          ("atlanticOcean-Portugal-Azores", 267),
          ("atlanticOcean-Portugal-MadeiraIslands", 266),
          ("atlanticOcean-Portugal-Mainland", 265),
          ("atlanticOcean-SouthGeorgia-SouthSandwichIslands", 268),
          ("atlanticOcean-Spain-CanaryIslands", 271),
          ("atlanticOcean-Spain-CeutaMelilla", 270),
          ("atlanticOcean-Spain-Mainland", 269),
          ("atlanticOcean-StHelena", 272),
          ("atlanticOcean-Svalbard-JanMayen", 273),
          ("australia-LordHoweIsland", 274),
          ("australia-NewSouthWales-MostLocations", 277),
          ("australia-NewSouthWales-Yancowinna", 278),
          ("australia-NorthernTerritory", 282),
          ("australia-Queensland-HolidayIslands", 280),
          ("australia-Queensland-MostLocations", 279),
          ("australia-SouthAustralia", 281),
          ("australia-Tasmania", 275),
          ("australia-Victoria", 276),
          ("australia-WesternAustralia", 283),
          ("europe-Albania", 284),
          ("europe-Andorra", 285),
          ("europe-Austria", 286),
          ("europe-Belarus", 287),
          ("europe-Belgium", 288),
          ("europe-BosniaHerzegovina", 289),
          ("europe-Britain-UKGreatBritain", 290),
          ("europe-Britain-UKNorthernIreland", 291),
          ("europe-Bulgaria", 292),
          ("europe-Croatia", 293),
          ("europe-CzechRepublic", 294),
          ("europe-Denmark", 295),
          ("europe-Estonia", 296),
          ("europe-Finland", 297),
          ("europe-France", 298),
          ("europe-Germany", 299),
          ("europe-Gibraltar", 300),
          ("europe-Greece", 301),
          ("europe-Hungary", 302),
          ("europe-Ireland", 303),
          ("europe-Italy", 304),
          ("europe-Latvia", 305),
          ("europe-Liechtenstein", 306),
          ("europe-Lithuania", 307),
          ("europe-Luxembourg", 308),
          ("europe-Macedonia", 309),
          ("europe-Malta", 310),
          ("europe-Moldova", 311),
          ("europe-Monaco", 312),
          ("europe-Netherlands", 313),
          ("europe-Norway", 314),
          ("europe-Poland", 315),
          ("europe-Portugal-Azores", 318),
          ("europe-Portugal-MadeiraIslands", 317),
          ("europe-Portugal-Mainland", 316),
          ("europe-Romania", 319),
          ("europe-Russia-Moscow-01Kaliningrad", 320),
          ("europe-Russia-Moscow00WestRussia", 321),
          ("europe-Russia-Moscow01CaspianSea", 322),
          ("europe-Russia-Moscow02Urals", 323),
          ("europe-Russia-Moscow03Novosibirsk", 325),
          ("europe-Russia-Moscow03WestSiberia", 324),
          ("europe-Russia-Moscow04YeniseiRiver", 326),
          ("europe-Russia-Moscow05LakeBaikal", 327),
          ("europe-Russia-Moscow06LenaRiver", 328),
          ("europe-Russia-Moscow07AmurRiver", 329),
          ("europe-Russia-Moscow07SakhalinIsland", 330),
          ("europe-Russia-Moscow08Magadan", 331),
          ("europe-Russia-Moscow09Kamchatka", 332),
          ("europe-Russia-Moscow10BeringSea", 333),
          ("europe-SanMarino", 334),
          ("europe-Slovakia", 335),
          ("europe-Slovenia", 336),
          ("europe-Spain-CanaryIslands", 339),
          ("europe-Spain-CeutaAndMelilla", 338),
          ("europe-Spain-Mainland", 337),
          ("europe-Sweden", 340),
          ("europe-Switzerland", 341),
          ("europe-Turkey", 342),
          ("europe-Ukraine-CentralCrimea", 346),
          ("europe-Ukraine-MostLocations", 343),
          ("europe-Ukraine-Ruthenia", 344),
          ("europe-Ukraine-Zaporozhye-ELugansk", 345),
          ("europe-VaticanCity", 347),
          ("europe-Yugoslavia", 348),
          ("indianOcean-BritishIndianOceanTerritory", 349),
          ("indianOcean-ChristmasIsland", 350),
          ("indianOcean-CocosOrKeelingIslands", 351),
          ("indianOcean-Comoros", 352),
          ("indianOcean-FrenchSouthernAndAntarcticLands", 353),
          ("indianOcean-Madagascar", 354),
          ("indianOcean-Maldives", 355),
          ("indianOcean-Mauritius", 356),
          ("indianOcean-Mayotte", 357),
          ("indianOcean-Reunion", 358),
          ("indianOcean-Seychelles", 359),
          ("none", 0),
          ("pacificOcean-Chile-EasterIslandSalayGomez", 361),
          ("pacificOcean-Chile-MostLocations", 360),
          ("pacificOcean-CookIslands", 362),
          ("pacificOcean-Ecuador", 363),
          ("pacificOcean-Fiji", 364),
          ("pacificOcean-FrenchPolynesia-GambierIslands", 367),
          ("pacificOcean-FrenchPolynesia-MarquesasIslands", 366),
          ("pacificOcean-FrenchPolynesia-SocietyIslands", 365),
          ("pacificOcean-Guam", 368),
          ("pacificOcean-Kiribati-GilbertIslands", 369),
          ("pacificOcean-Kiribati-LineIslands", 371),
          ("pacificOcean-Kiribati-PhoenixIslands", 370),
          ("pacificOcean-MarshallIslands-Kwajalein", 373),
          ("pacificOcean-MarshallIslands-MostLocations", 372),
          ("pacificOcean-Micronesia-Kosrae", 377),
          ("pacificOcean-Micronesia-PonapeOrPohnpei", 376),
          ("pacificOcean-Micronesia-TrukOrChuuk", 375),
          ("pacificOcean-Micronesia-Yap", 374),
          ("pacificOcean-Nauru", 378),
          ("pacificOcean-NewCaledonia", 379),
          ("pacificOcean-NewZealand-ChathamIslands", 381),
          ("pacificOcean-NewZealand-MostLocations", 380),
          ("pacificOcean-Niue", 382),
          ("pacificOcean-NorfolkIsland", 383),
          ("pacificOcean-NorthernMarianaIslands", 384),
          ("pacificOcean-Palau", 385),
          ("pacificOcean-PapuaNewGuinea", 386),
          ("pacificOcean-Pitcairn", 387),
          ("pacificOcean-SamoaAmerican", 388),
          ("pacificOcean-SamoaWestern", 389),
          ("pacificOcean-SolomonIslands", 390),
          ("pacificOcean-Tokelau", 391),
          ("pacificOcean-Tonga", 392),
          ("pacificOcean-Tuvalu", 393),
          ("pacificOcean-USMinorOutlyingIslands-JohnstonAtoll", 416),
          ("pacificOcean-USMinorOutlyingIslands-MidwayIslands", 417),
          ("pacificOcean-USMinorOutlyingIslands-WakeIsland", 418),
          ("pacificOcean-Vanuatu", 419),
          ("pacificOceanUSA-AlaskaTime", 410),
          ("pacificOceanUSA-AlaskaTime-AlaskaPanhandle", 411),
          ("pacificOceanUSA-AlaskaTime-AlaskaPanhandleNeck", 412),
          ("pacificOceanUSA-AlaskaTime-WestAlaska", 413),
          ("pacificOceanUSA-AleutianIslands", 414),
          ("pacificOceanUSA-CentTime", 402),
          ("pacificOceanUSA-CentTime-MichiganWisconsinborder", 403),
          ("pacificOceanUSA-CentTime-NorthDakotaOliverCounty", 404),
          ("pacificOceanUSA-EastStdTime-IndianaCrawfordCounty", 399),
          ("pacificOceanUSA-EastStdTime-IndianaMostLocations", 398),
          ("pacificOceanUSA-EastStdTime-IndianaStarkeCounty", 400),
          ("pacificOceanUSA-EastStdTime-IndianaSwitzerlandCounty", 401),
          ("pacificOceanUSA-EastTime", 394),
          ("pacificOceanUSA-EastTime-KentuckyLouisvilleArea", 396),
          ("pacificOceanUSA-EastTime-KentuckyWayneCounty", 397),
          ("pacificOceanUSA-EastTime-MichiganMostLocations", 395),
          ("pacificOceanUSA-Hawaii", 415),
          ("pacificOceanUSA-MountStdTime-Arizona", 408),
          ("pacificOceanUSA-MountTime", 405),
          ("pacificOceanUSA-MountTime-Navajo", 407),
          ("pacificOceanUSA-MountTime-SouthIdahoAndEastOregon", 406),
          ("pacificOceanUSA-PacificTime", 409),
          ("pacificOceanWallisAndFutuna", 420))
    )


_AgNewDaylightSavings_Type.__name__ = "Integer32"
_AgNewDaylightSavings_Object = MibScalar
agNewDaylightSavings = _AgNewDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 52),
    _AgNewDaylightSavings_Type()
)
agNewDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewDaylightSavings.setStatus("current")
_AgCurCfgIdleCLITimeout_Type = Integer32
_AgCurCfgIdleCLITimeout_Object = MibScalar
agCurCfgIdleCLITimeout = _AgCurCfgIdleCLITimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 53),
    _AgCurCfgIdleCLITimeout_Type()
)
agCurCfgIdleCLITimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgIdleCLITimeout.setStatus("current")
_AgNewCfgIdleCLITimeout_Type = Integer32
_AgNewCfgIdleCLITimeout_Object = MibScalar
agNewCfgIdleCLITimeout = _AgNewCfgIdleCLITimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 54),
    _AgNewCfgIdleCLITimeout_Type()
)
agNewCfgIdleCLITimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgIdleCLITimeout.setStatus("current")


class _AgCurCfgUfdTrap_Type(Integer32):
    """Custom type agCurCfgUfdTrap based on Integer32"""
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


_AgCurCfgUfdTrap_Type.__name__ = "Integer32"
_AgCurCfgUfdTrap_Object = MibScalar
agCurCfgUfdTrap = _AgCurCfgUfdTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 55),
    _AgCurCfgUfdTrap_Type()
)
agCurCfgUfdTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgUfdTrap.setStatus("current")


class _AgNewCfgUfdTrap_Type(Integer32):
    """Custom type agNewCfgUfdTrap based on Integer32"""
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


_AgNewCfgUfdTrap_Type.__name__ = "Integer32"
_AgNewCfgUfdTrap_Object = MibScalar
agNewCfgUfdTrap = _AgNewCfgUfdTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 56),
    _AgNewCfgUfdTrap_Type()
)
agNewCfgUfdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgUfdTrap.setStatus("current")


class _AgCurBootNxtCliMode_Type(Integer32):
    """Custom type agCurBootNxtCliMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aoscli", 1),
          ("iscli", 2))
    )


_AgCurBootNxtCliMode_Type.__name__ = "Integer32"
_AgCurBootNxtCliMode_Object = MibScalar
agCurBootNxtCliMode = _AgCurBootNxtCliMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 64),
    _AgCurBootNxtCliMode_Type()
)
agCurBootNxtCliMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurBootNxtCliMode.setStatus("current")


class _AgNewBootNxtCliMode_Type(Integer32):
    """Custom type agNewBootNxtCliMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aoscli", 1),
          ("iscli", 2))
    )


_AgNewBootNxtCliMode_Type.__name__ = "Integer32"
_AgNewBootNxtCliMode_Object = MibScalar
agNewBootNxtCliMode = _AgNewBootNxtCliMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 65),
    _AgNewBootNxtCliMode_Type()
)
agNewBootNxtCliMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewBootNxtCliMode.setStatus("current")


class _AgCurCfgReminders_Type(Integer32):
    """Custom type agCurCfgReminders based on Integer32"""
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


_AgCurCfgReminders_Type.__name__ = "Integer32"
_AgCurCfgReminders_Object = MibScalar
agCurCfgReminders = _AgCurCfgReminders_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 70),
    _AgCurCfgReminders_Type()
)
agCurCfgReminders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgReminders.setStatus("current")


class _AgNewCfgReminders_Type(Integer32):
    """Custom type agNewCfgReminders based on Integer32"""
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


_AgNewCfgReminders_Type.__name__ = "Integer32"
_AgNewCfgReminders_Object = MibScalar
agNewCfgReminders = _AgNewCfgReminders_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 1, 71),
    _AgNewCfgReminders_Type()
)
agNewCfgReminders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgReminders.setStatus("current")
_AgPortConfig_ObjectIdentity = ObjectIdentity
agPortConfig = _AgPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2)
)
_AgPortTableMaxEnt_Type = Integer32
_AgPortTableMaxEnt_Object = MibScalar
agPortTableMaxEnt = _AgPortTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 1),
    _AgPortTableMaxEnt_Type()
)
agPortTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortTableMaxEnt.setStatus("current")
_AgPortCurCfgTable_Object = MibTable
agPortCurCfgTable = _AgPortCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    agPortCurCfgTable.setStatus("current")
_AgPortCurCfgTableEntry_Object = MibTableRow
agPortCurCfgTableEntry = _AgPortCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1)
)
agPortCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agPortCurCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortCurCfgTableEntry.setStatus("current")
_AgPortCurCfgIndx_Type = Integer32
_AgPortCurCfgIndx_Object = MibTableColumn
agPortCurCfgIndx = _AgPortCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 1),
    _AgPortCurCfgIndx_Type()
)
agPortCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgIndx.setStatus("current")


class _AgPortCurCfgState_Type(Integer32):
    """Custom type agPortCurCfgState based on Integer32"""
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


_AgPortCurCfgState_Type.__name__ = "Integer32"
_AgPortCurCfgState_Object = MibTableColumn
agPortCurCfgState = _AgPortCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 2),
    _AgPortCurCfgState_Type()
)
agPortCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgState.setStatus("current")


class _AgPortCurCfgVlanTag_Type(Integer32):
    """Custom type agPortCurCfgVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 2),
          ("untagged", 3))
    )


_AgPortCurCfgVlanTag_Type.__name__ = "Integer32"
_AgPortCurCfgVlanTag_Object = MibTableColumn
agPortCurCfgVlanTag = _AgPortCurCfgVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 3),
    _AgPortCurCfgVlanTag_Type()
)
agPortCurCfgVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgVlanTag.setStatus("current")


class _AgPortCurCfgStp_Type(Integer32):
    """Custom type agPortCurCfgStp based on Integer32"""
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


_AgPortCurCfgStp_Type.__name__ = "Integer32"
_AgPortCurCfgStp_Object = MibTableColumn
agPortCurCfgStp = _AgPortCurCfgStp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 4),
    _AgPortCurCfgStp_Type()
)
agPortCurCfgStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgStp.setStatus("current")


class _AgPortCurCfgRmon_Type(Integer32):
    """Custom type agPortCurCfgRmon based on Integer32"""
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


_AgPortCurCfgRmon_Type.__name__ = "Integer32"
_AgPortCurCfgRmon_Object = MibTableColumn
agPortCurCfgRmon = _AgPortCurCfgRmon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 5),
    _AgPortCurCfgRmon_Type()
)
agPortCurCfgRmon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgRmon.setStatus("current")


class _AgPortCurCfgPVID_Type(Integer32):
    """Custom type agPortCurCfgPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AgPortCurCfgPVID_Type.__name__ = "Integer32"
_AgPortCurCfgPVID_Object = MibTableColumn
agPortCurCfgPVID = _AgPortCurCfgPVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 6),
    _AgPortCurCfgPVID_Type()
)
agPortCurCfgPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPVID.setStatus("current")


class _AgPortCurCfgGigEthAutoNeg_Type(Integer32):
    """Custom type agPortCurCfgGigEthAutoNeg based on Integer32"""
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


_AgPortCurCfgGigEthAutoNeg_Type.__name__ = "Integer32"
_AgPortCurCfgGigEthAutoNeg_Object = MibTableColumn
agPortCurCfgGigEthAutoNeg = _AgPortCurCfgGigEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 11),
    _AgPortCurCfgGigEthAutoNeg_Type()
)
agPortCurCfgGigEthAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthAutoNeg.setStatus("current")


class _AgPortCurCfgGigEthSpeed_Type(Integer32):
    """Custom type agPortCurCfgGigEthSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("any", 4),
          ("mbs10", 2),
          ("mbs100", 3),
          ("mbs1000", 5))
    )


_AgPortCurCfgGigEthSpeed_Type.__name__ = "Integer32"
_AgPortCurCfgGigEthSpeed_Object = MibTableColumn
agPortCurCfgGigEthSpeed = _AgPortCurCfgGigEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 12),
    _AgPortCurCfgGigEthSpeed_Type()
)
agPortCurCfgGigEthSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthSpeed.setStatus("current")


class _AgPortCurCfgGigEthMode_Type(Integer32):
    """Custom type agPortCurCfgGigEthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("full-or-half-duplex", 4),
          ("half-duplex", 3))
    )


_AgPortCurCfgGigEthMode_Type.__name__ = "Integer32"
_AgPortCurCfgGigEthMode_Object = MibTableColumn
agPortCurCfgGigEthMode = _AgPortCurCfgGigEthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 13),
    _AgPortCurCfgGigEthMode_Type()
)
agPortCurCfgGigEthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthMode.setStatus("current")


class _AgPortCurCfgGigEthFctl_Type(Integer32):
    """Custom type agPortCurCfgGigEthFctl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("none", 5),
          ("receive", 3),
          ("transmit", 2))
    )


_AgPortCurCfgGigEthFctl_Type.__name__ = "Integer32"
_AgPortCurCfgGigEthFctl_Object = MibTableColumn
agPortCurCfgGigEthFctl = _AgPortCurCfgGigEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 14),
    _AgPortCurCfgGigEthFctl_Type()
)
agPortCurCfgGigEthFctl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthFctl.setStatus("current")


class _AgPortCurCfgPortName_Type(DisplayString):
    """Custom type agPortCurCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgPortCurCfgPortName_Type.__name__ = "DisplayString"
_AgPortCurCfgPortName_Object = MibTableColumn
agPortCurCfgPortName = _AgPortCurCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 15),
    _AgPortCurCfgPortName_Type()
)
agPortCurCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPortName.setStatus("current")


class _AgPortCurCfgLinkTrap_Type(Integer32):
    """Custom type agPortCurCfgLinkTrap based on Integer32"""
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


_AgPortCurCfgLinkTrap_Type.__name__ = "Integer32"
_AgPortCurCfgLinkTrap_Object = MibTableColumn
agPortCurCfgLinkTrap = _AgPortCurCfgLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 18),
    _AgPortCurCfgLinkTrap_Type()
)
agPortCurCfgLinkTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgLinkTrap.setStatus("current")


class _AgPortCurCfgTagPVID_Type(Integer32):
    """Custom type agPortCurCfgTagPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 2),
          ("untagged", 3))
    )


_AgPortCurCfgTagPVID_Type.__name__ = "Integer32"
_AgPortCurCfgTagPVID_Object = MibTableColumn
agPortCurCfgTagPVID = _AgPortCurCfgTagPVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 19),
    _AgPortCurCfgTagPVID_Type()
)
agPortCurCfgTagPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgTagPVID.setStatus("current")


class _AgPortCurCfgMulticastThreshold_Type(Integer32):
    """Custom type agPortCurCfgMulticastThreshold based on Integer32"""
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


_AgPortCurCfgMulticastThreshold_Type.__name__ = "Integer32"
_AgPortCurCfgMulticastThreshold_Object = MibTableColumn
agPortCurCfgMulticastThreshold = _AgPortCurCfgMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 20),
    _AgPortCurCfgMulticastThreshold_Type()
)
agPortCurCfgMulticastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgMulticastThreshold.setStatus("current")


class _AgPortCurCfgMulticastThresholdRate_Type(Integer32):
    """Custom type agPortCurCfgMulticastThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_AgPortCurCfgMulticastThresholdRate_Type.__name__ = "Integer32"
_AgPortCurCfgMulticastThresholdRate_Object = MibTableColumn
agPortCurCfgMulticastThresholdRate = _AgPortCurCfgMulticastThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 21),
    _AgPortCurCfgMulticastThresholdRate_Type()
)
agPortCurCfgMulticastThresholdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgMulticastThresholdRate.setStatus("current")


class _AgPortCurCfgBroadcastThreshold_Type(Integer32):
    """Custom type agPortCurCfgBroadcastThreshold based on Integer32"""
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


_AgPortCurCfgBroadcastThreshold_Type.__name__ = "Integer32"
_AgPortCurCfgBroadcastThreshold_Object = MibTableColumn
agPortCurCfgBroadcastThreshold = _AgPortCurCfgBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 22),
    _AgPortCurCfgBroadcastThreshold_Type()
)
agPortCurCfgBroadcastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgBroadcastThreshold.setStatus("current")


class _AgPortCurCfgBroadcastThresholdRate_Type(Integer32):
    """Custom type agPortCurCfgBroadcastThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_AgPortCurCfgBroadcastThresholdRate_Type.__name__ = "Integer32"
_AgPortCurCfgBroadcastThresholdRate_Object = MibTableColumn
agPortCurCfgBroadcastThresholdRate = _AgPortCurCfgBroadcastThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 23),
    _AgPortCurCfgBroadcastThresholdRate_Type()
)
agPortCurCfgBroadcastThresholdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgBroadcastThresholdRate.setStatus("current")


class _AgPortCurCfgDLFThreshold_Type(Integer32):
    """Custom type agPortCurCfgDLFThreshold based on Integer32"""
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


_AgPortCurCfgDLFThreshold_Type.__name__ = "Integer32"
_AgPortCurCfgDLFThreshold_Object = MibTableColumn
agPortCurCfgDLFThreshold = _AgPortCurCfgDLFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 24),
    _AgPortCurCfgDLFThreshold_Type()
)
agPortCurCfgDLFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgDLFThreshold.setStatus("current")


class _AgPortCurCfgDLFThresholdRate_Type(Integer32):
    """Custom type agPortCurCfgDLFThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_AgPortCurCfgDLFThresholdRate_Type.__name__ = "Integer32"
_AgPortCurCfgDLFThresholdRate_Object = MibTableColumn
agPortCurCfgDLFThresholdRate = _AgPortCurCfgDLFThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 1, 25),
    _AgPortCurCfgDLFThresholdRate_Type()
)
agPortCurCfgDLFThresholdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgDLFThresholdRate.setStatus("current")
_AgPortFiberCurCfgTable_Object = MibTable
agPortFiberCurCfgTable = _AgPortFiberCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    agPortFiberCurCfgTable.setStatus("current")
_AgPortFiberCurCfgTableEntry_Object = MibTableRow
agPortFiberCurCfgTableEntry = _AgPortFiberCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 2, 1)
)
agPortFiberCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agPortFiberCurCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortFiberCurCfgTableEntry.setStatus("current")
_AgPortFiberCurCfgIndx_Type = Integer32
_AgPortFiberCurCfgIndx_Object = MibTableColumn
agPortFiberCurCfgIndx = _AgPortFiberCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 2, 1, 1),
    _AgPortFiberCurCfgIndx_Type()
)
agPortFiberCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortFiberCurCfgIndx.setStatus("current")


class _AgPortFiberCurCfgTxCtrl_Type(Integer32):
    """Custom type agPortFiberCurCfgTxCtrl based on Integer32"""
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


_AgPortFiberCurCfgTxCtrl_Type.__name__ = "Integer32"
_AgPortFiberCurCfgTxCtrl_Object = MibTableColumn
agPortFiberCurCfgTxCtrl = _AgPortFiberCurCfgTxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 2, 1, 2),
    _AgPortFiberCurCfgTxCtrl_Type()
)
agPortFiberCurCfgTxCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortFiberCurCfgTxCtrl.setStatus("current")


class _AgPortFiberCurCfgTxPulse_Type(Integer32):
    """Custom type agPortFiberCurCfgTxPulse based on Integer32"""
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


_AgPortFiberCurCfgTxPulse_Type.__name__ = "Integer32"
_AgPortFiberCurCfgTxPulse_Object = MibTableColumn
agPortFiberCurCfgTxPulse = _AgPortFiberCurCfgTxPulse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 2, 1, 3),
    _AgPortFiberCurCfgTxPulse_Type()
)
agPortFiberCurCfgTxPulse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortFiberCurCfgTxPulse.setStatus("current")


class _AgPortFiberCurCfgTxUp_Type(Integer32):
    """Custom type agPortFiberCurCfgTxUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgPortFiberCurCfgTxUp_Type.__name__ = "Integer32"
_AgPortFiberCurCfgTxUp_Object = MibTableColumn
agPortFiberCurCfgTxUp = _AgPortFiberCurCfgTxUp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 2, 1, 4),
    _AgPortFiberCurCfgTxUp_Type()
)
agPortFiberCurCfgTxUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortFiberCurCfgTxUp.setStatus("current")


class _AgPortFiberCurCfgTxDn_Type(Integer32):
    """Custom type agPortFiberCurCfgTxDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgPortFiberCurCfgTxDn_Type.__name__ = "Integer32"
_AgPortFiberCurCfgTxDn_Object = MibTableColumn
agPortFiberCurCfgTxDn = _AgPortFiberCurCfgTxDn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 2, 2, 1, 5),
    _AgPortFiberCurCfgTxDn_Type()
)
agPortFiberCurCfgTxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortFiberCurCfgTxDn.setStatus("current")
_AgPortNewCfgTable_Object = MibTable
agPortNewCfgTable = _AgPortNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    agPortNewCfgTable.setStatus("current")
_AgPortNewCfgTableEntry_Object = MibTableRow
agPortNewCfgTableEntry = _AgPortNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1)
)
agPortNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agPortNewCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortNewCfgTableEntry.setStatus("current")
_AgPortNewCfgIndx_Type = Integer32
_AgPortNewCfgIndx_Object = MibTableColumn
agPortNewCfgIndx = _AgPortNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 1),
    _AgPortNewCfgIndx_Type()
)
agPortNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortNewCfgIndx.setStatus("current")


class _AgPortNewCfgState_Type(Integer32):
    """Custom type agPortNewCfgState based on Integer32"""
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


_AgPortNewCfgState_Type.__name__ = "Integer32"
_AgPortNewCfgState_Object = MibTableColumn
agPortNewCfgState = _AgPortNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 2),
    _AgPortNewCfgState_Type()
)
agPortNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgState.setStatus("current")


class _AgPortNewCfgVlanTag_Type(Integer32):
    """Custom type agPortNewCfgVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 2),
          ("untagged", 3))
    )


_AgPortNewCfgVlanTag_Type.__name__ = "Integer32"
_AgPortNewCfgVlanTag_Object = MibTableColumn
agPortNewCfgVlanTag = _AgPortNewCfgVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 3),
    _AgPortNewCfgVlanTag_Type()
)
agPortNewCfgVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgVlanTag.setStatus("current")


class _AgPortNewCfgStp_Type(Integer32):
    """Custom type agPortNewCfgStp based on Integer32"""
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


_AgPortNewCfgStp_Type.__name__ = "Integer32"
_AgPortNewCfgStp_Object = MibTableColumn
agPortNewCfgStp = _AgPortNewCfgStp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 4),
    _AgPortNewCfgStp_Type()
)
agPortNewCfgStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgStp.setStatus("current")


class _AgPortNewCfgRmon_Type(Integer32):
    """Custom type agPortNewCfgRmon based on Integer32"""
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


_AgPortNewCfgRmon_Type.__name__ = "Integer32"
_AgPortNewCfgRmon_Object = MibTableColumn
agPortNewCfgRmon = _AgPortNewCfgRmon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 5),
    _AgPortNewCfgRmon_Type()
)
agPortNewCfgRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgRmon.setStatus("current")


class _AgPortNewCfgPVID_Type(Integer32):
    """Custom type agPortNewCfgPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AgPortNewCfgPVID_Type.__name__ = "Integer32"
_AgPortNewCfgPVID_Object = MibTableColumn
agPortNewCfgPVID = _AgPortNewCfgPVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 6),
    _AgPortNewCfgPVID_Type()
)
agPortNewCfgPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPVID.setStatus("current")


class _AgPortNewCfgGigEthAutoNeg_Type(Integer32):
    """Custom type agPortNewCfgGigEthAutoNeg based on Integer32"""
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


_AgPortNewCfgGigEthAutoNeg_Type.__name__ = "Integer32"
_AgPortNewCfgGigEthAutoNeg_Object = MibTableColumn
agPortNewCfgGigEthAutoNeg = _AgPortNewCfgGigEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 11),
    _AgPortNewCfgGigEthAutoNeg_Type()
)
agPortNewCfgGigEthAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthAutoNeg.setStatus("current")


class _AgPortNewCfgGigEthSpeed_Type(Integer32):
    """Custom type agPortNewCfgGigEthSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("any", 4),
          ("mbs10", 2),
          ("mbs100", 3),
          ("mbs1000", 5))
    )


_AgPortNewCfgGigEthSpeed_Type.__name__ = "Integer32"
_AgPortNewCfgGigEthSpeed_Object = MibTableColumn
agPortNewCfgGigEthSpeed = _AgPortNewCfgGigEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 12),
    _AgPortNewCfgGigEthSpeed_Type()
)
agPortNewCfgGigEthSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthSpeed.setStatus("current")


class _AgPortNewCfgGigEthMode_Type(Integer32):
    """Custom type agPortNewCfgGigEthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("full-or-half-duplex", 4),
          ("half-duplex", 3))
    )


_AgPortNewCfgGigEthMode_Type.__name__ = "Integer32"
_AgPortNewCfgGigEthMode_Object = MibTableColumn
agPortNewCfgGigEthMode = _AgPortNewCfgGigEthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 13),
    _AgPortNewCfgGigEthMode_Type()
)
agPortNewCfgGigEthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthMode.setStatus("current")


class _AgPortNewCfgGigEthFctl_Type(Integer32):
    """Custom type agPortNewCfgGigEthFctl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("none", 5),
          ("receive", 3),
          ("transmit", 2))
    )


_AgPortNewCfgGigEthFctl_Type.__name__ = "Integer32"
_AgPortNewCfgGigEthFctl_Object = MibTableColumn
agPortNewCfgGigEthFctl = _AgPortNewCfgGigEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 14),
    _AgPortNewCfgGigEthFctl_Type()
)
agPortNewCfgGigEthFctl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthFctl.setStatus("current")


class _AgPortNewCfgPortName_Type(DisplayString):
    """Custom type agPortNewCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgPortNewCfgPortName_Type.__name__ = "DisplayString"
_AgPortNewCfgPortName_Object = MibTableColumn
agPortNewCfgPortName = _AgPortNewCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 15),
    _AgPortNewCfgPortName_Type()
)
agPortNewCfgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPortName.setStatus("current")


class _AgPortNewCfgLinkTrap_Type(Integer32):
    """Custom type agPortNewCfgLinkTrap based on Integer32"""
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


_AgPortNewCfgLinkTrap_Type.__name__ = "Integer32"
_AgPortNewCfgLinkTrap_Object = MibTableColumn
agPortNewCfgLinkTrap = _AgPortNewCfgLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 18),
    _AgPortNewCfgLinkTrap_Type()
)
agPortNewCfgLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgLinkTrap.setStatus("current")


class _AgPortNewCfgTagPVID_Type(Integer32):
    """Custom type agPortNewCfgTagPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 2),
          ("untagged", 3))
    )


_AgPortNewCfgTagPVID_Type.__name__ = "Integer32"
_AgPortNewCfgTagPVID_Object = MibTableColumn
agPortNewCfgTagPVID = _AgPortNewCfgTagPVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 19),
    _AgPortNewCfgTagPVID_Type()
)
agPortNewCfgTagPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgTagPVID.setStatus("current")


class _AgPortNewCfgMulticastThreshold_Type(Integer32):
    """Custom type agPortNewCfgMulticastThreshold based on Integer32"""
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


_AgPortNewCfgMulticastThreshold_Type.__name__ = "Integer32"
_AgPortNewCfgMulticastThreshold_Object = MibTableColumn
agPortNewCfgMulticastThreshold = _AgPortNewCfgMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 20),
    _AgPortNewCfgMulticastThreshold_Type()
)
agPortNewCfgMulticastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgMulticastThreshold.setStatus("current")


class _AgPortNewCfgMulticastThresholdRate_Type(Integer32):
    """Custom type agPortNewCfgMulticastThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_AgPortNewCfgMulticastThresholdRate_Type.__name__ = "Integer32"
_AgPortNewCfgMulticastThresholdRate_Object = MibTableColumn
agPortNewCfgMulticastThresholdRate = _AgPortNewCfgMulticastThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 21),
    _AgPortNewCfgMulticastThresholdRate_Type()
)
agPortNewCfgMulticastThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgMulticastThresholdRate.setStatus("current")


class _AgPortNewCfgBroadcastThreshold_Type(Integer32):
    """Custom type agPortNewCfgBroadcastThreshold based on Integer32"""
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


_AgPortNewCfgBroadcastThreshold_Type.__name__ = "Integer32"
_AgPortNewCfgBroadcastThreshold_Object = MibTableColumn
agPortNewCfgBroadcastThreshold = _AgPortNewCfgBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 22),
    _AgPortNewCfgBroadcastThreshold_Type()
)
agPortNewCfgBroadcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgBroadcastThreshold.setStatus("current")


class _AgPortNewCfgBroadcastThresholdRate_Type(Integer32):
    """Custom type agPortNewCfgBroadcastThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_AgPortNewCfgBroadcastThresholdRate_Type.__name__ = "Integer32"
_AgPortNewCfgBroadcastThresholdRate_Object = MibTableColumn
agPortNewCfgBroadcastThresholdRate = _AgPortNewCfgBroadcastThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 23),
    _AgPortNewCfgBroadcastThresholdRate_Type()
)
agPortNewCfgBroadcastThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgBroadcastThresholdRate.setStatus("current")


class _AgPortNewCfgDLFThreshold_Type(Integer32):
    """Custom type agPortNewCfgDLFThreshold based on Integer32"""
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


_AgPortNewCfgDLFThreshold_Type.__name__ = "Integer32"
_AgPortNewCfgDLFThreshold_Object = MibTableColumn
agPortNewCfgDLFThreshold = _AgPortNewCfgDLFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 24),
    _AgPortNewCfgDLFThreshold_Type()
)
agPortNewCfgDLFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgDLFThreshold.setStatus("current")


class _AgPortNewCfgDLFThresholdRate_Type(Integer32):
    """Custom type agPortNewCfgDLFThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_AgPortNewCfgDLFThresholdRate_Type.__name__ = "Integer32"
_AgPortNewCfgDLFThresholdRate_Object = MibTableColumn
agPortNewCfgDLFThresholdRate = _AgPortNewCfgDLFThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 1, 25),
    _AgPortNewCfgDLFThresholdRate_Type()
)
agPortNewCfgDLFThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgDLFThresholdRate.setStatus("current")
_AgPortFiberNewCfgTable_Object = MibTable
agPortFiberNewCfgTable = _AgPortFiberNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    agPortFiberNewCfgTable.setStatus("current")
_AgPortFiberNewCfgTableEntry_Object = MibTableRow
agPortFiberNewCfgTableEntry = _AgPortFiberNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 2, 1)
)
agPortFiberNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agPortFiberNewCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortFiberNewCfgTableEntry.setStatus("current")
_AgPortFiberNewCfgIndx_Type = Integer32
_AgPortFiberNewCfgIndx_Object = MibTableColumn
agPortFiberNewCfgIndx = _AgPortFiberNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 2, 1, 1),
    _AgPortFiberNewCfgIndx_Type()
)
agPortFiberNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortFiberNewCfgIndx.setStatus("current")


class _AgPortFiberNewCfgTxCtrl_Type(Integer32):
    """Custom type agPortFiberNewCfgTxCtrl based on Integer32"""
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


_AgPortFiberNewCfgTxCtrl_Type.__name__ = "Integer32"
_AgPortFiberNewCfgTxCtrl_Object = MibTableColumn
agPortFiberNewCfgTxCtrl = _AgPortFiberNewCfgTxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 2, 1, 2),
    _AgPortFiberNewCfgTxCtrl_Type()
)
agPortFiberNewCfgTxCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortFiberNewCfgTxCtrl.setStatus("current")


class _AgPortFiberNewCfgTxPulse_Type(Integer32):
    """Custom type agPortFiberNewCfgTxPulse based on Integer32"""
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


_AgPortFiberNewCfgTxPulse_Type.__name__ = "Integer32"
_AgPortFiberNewCfgTxPulse_Object = MibTableColumn
agPortFiberNewCfgTxPulse = _AgPortFiberNewCfgTxPulse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 2, 1, 3),
    _AgPortFiberNewCfgTxPulse_Type()
)
agPortFiberNewCfgTxPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortFiberNewCfgTxPulse.setStatus("current")


class _AgPortFiberNewCfgTxUp_Type(Integer32):
    """Custom type agPortFiberNewCfgTxUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgPortFiberNewCfgTxUp_Type.__name__ = "Integer32"
_AgPortFiberNewCfgTxUp_Object = MibTableColumn
agPortFiberNewCfgTxUp = _AgPortFiberNewCfgTxUp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 2, 1, 4),
    _AgPortFiberNewCfgTxUp_Type()
)
agPortFiberNewCfgTxUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortFiberNewCfgTxUp.setStatus("current")


class _AgPortFiberNewCfgTxDn_Type(Integer32):
    """Custom type agPortFiberNewCfgTxDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgPortFiberNewCfgTxDn_Type.__name__ = "Integer32"
_AgPortFiberNewCfgTxDn_Object = MibTableColumn
agPortFiberNewCfgTxDn = _AgPortFiberNewCfgTxDn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 2, 3, 2, 1, 5),
    _AgPortFiberNewCfgTxDn_Type()
)
agPortFiberNewCfgTxDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortFiberNewCfgTxDn.setStatus("current")
_AgRadiusConfig_ObjectIdentity = ObjectIdentity
agRadiusConfig = _AgRadiusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3)
)
_RadCurCfgPrimaryIpAddr_Type = IpAddress
_RadCurCfgPrimaryIpAddr_Object = MibScalar
radCurCfgPrimaryIpAddr = _RadCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 1),
    _RadCurCfgPrimaryIpAddr_Type()
)
radCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgPrimaryIpAddr.setStatus("current")
_RadNewCfgPrimaryIpAddr_Type = IpAddress
_RadNewCfgPrimaryIpAddr_Object = MibScalar
radNewCfgPrimaryIpAddr = _RadNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 2),
    _RadNewCfgPrimaryIpAddr_Type()
)
radNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgPrimaryIpAddr.setStatus("current")
_RadCurCfgSecondaryIpAddr_Type = IpAddress
_RadCurCfgSecondaryIpAddr_Object = MibScalar
radCurCfgSecondaryIpAddr = _RadCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 3),
    _RadCurCfgSecondaryIpAddr_Type()
)
radCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgSecondaryIpAddr.setStatus("current")
_RadNewCfgSecondaryIpAddr_Type = IpAddress
_RadNewCfgSecondaryIpAddr_Object = MibScalar
radNewCfgSecondaryIpAddr = _RadNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 4),
    _RadNewCfgSecondaryIpAddr_Type()
)
radNewCfgSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgSecondaryIpAddr.setStatus("current")


class _RadCurCfgPort_Type(Integer32):
    """Custom type radCurCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 3000),
    )


_RadCurCfgPort_Type.__name__ = "Integer32"
_RadCurCfgPort_Object = MibScalar
radCurCfgPort = _RadCurCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 5),
    _RadCurCfgPort_Type()
)
radCurCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgPort.setStatus("current")


class _RadNewCfgPort_Type(Integer32):
    """Custom type radNewCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 3000),
    )


_RadNewCfgPort_Type.__name__ = "Integer32"
_RadNewCfgPort_Object = MibScalar
radNewCfgPort = _RadNewCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 6),
    _RadNewCfgPort_Type()
)
radNewCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgPort.setStatus("current")


class _RadCurCfgTimeout_Type(Integer32):
    """Custom type radCurCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadCurCfgTimeout_Type.__name__ = "Integer32"
_RadCurCfgTimeout_Object = MibScalar
radCurCfgTimeout = _RadCurCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 7),
    _RadCurCfgTimeout_Type()
)
radCurCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgTimeout.setStatus("current")


class _RadNewCfgTimeout_Type(Integer32):
    """Custom type radNewCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadNewCfgTimeout_Type.__name__ = "Integer32"
_RadNewCfgTimeout_Object = MibScalar
radNewCfgTimeout = _RadNewCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 8),
    _RadNewCfgTimeout_Type()
)
radNewCfgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgTimeout.setStatus("current")


class _RadCurCfgRetries_Type(Integer32):
    """Custom type radCurCfgRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RadCurCfgRetries_Type.__name__ = "Integer32"
_RadCurCfgRetries_Object = MibScalar
radCurCfgRetries = _RadCurCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 9),
    _RadCurCfgRetries_Type()
)
radCurCfgRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgRetries.setStatus("current")


class _RadNewCfgRetries_Type(Integer32):
    """Custom type radNewCfgRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RadNewCfgRetries_Type.__name__ = "Integer32"
_RadNewCfgRetries_Object = MibScalar
radNewCfgRetries = _RadNewCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 10),
    _RadNewCfgRetries_Type()
)
radNewCfgRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgRetries.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 11),
    _RadCurCfgState_Type()
)
radCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 12),
    _RadNewCfgState_Type()
)
radNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgState.setStatus("current")


class _RadCurCfgAuthenString_Type(DisplayString):
    """Custom type radCurCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RadCurCfgAuthenString_Type.__name__ = "DisplayString"
_RadCurCfgAuthenString_Object = MibScalar
radCurCfgAuthenString = _RadCurCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 13),
    _RadCurCfgAuthenString_Type()
)
radCurCfgAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgAuthenString.setStatus("current")


class _RadNewCfgAuthenString_Type(DisplayString):
    """Custom type radNewCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RadNewCfgAuthenString_Type.__name__ = "DisplayString"
_RadNewCfgAuthenString_Object = MibScalar
radNewCfgAuthenString = _RadNewCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 14),
    _RadNewCfgAuthenString_Type()
)
radNewCfgAuthenString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgAuthenString.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 15),
    _RadCurCfgTelnet_Type()
)
radCurCfgTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgTelnet.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 16),
    _RadNewCfgTelnet_Type()
)
radNewCfgTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgTelnet.setStatus("current")


class _RadCurCfgAuthenSecondString_Type(DisplayString):
    """Custom type radCurCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RadCurCfgAuthenSecondString_Type.__name__ = "DisplayString"
_RadCurCfgAuthenSecondString_Object = MibScalar
radCurCfgAuthenSecondString = _RadCurCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 17),
    _RadCurCfgAuthenSecondString_Type()
)
radCurCfgAuthenSecondString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgAuthenSecondString.setStatus("current")


class _RadNewCfgAuthenSecondString_Type(DisplayString):
    """Custom type radNewCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RadNewCfgAuthenSecondString_Type.__name__ = "DisplayString"
_RadNewCfgAuthenSecondString_Object = MibScalar
radNewCfgAuthenSecondString = _RadNewCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 18),
    _RadNewCfgAuthenSecondString_Type()
)
radNewCfgAuthenSecondString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgAuthenSecondString.setStatus("current")


class _RadCurCfgSecBd_Type(Integer32):
    """Custom type radCurCfgSecBd based on Integer32"""
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


_RadCurCfgSecBd_Type.__name__ = "Integer32"
_RadCurCfgSecBd_Object = MibScalar
radCurCfgSecBd = _RadCurCfgSecBd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 19),
    _RadCurCfgSecBd_Type()
)
radCurCfgSecBd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgSecBd.setStatus("current")


class _RadNewCfgSecBd_Type(Integer32):
    """Custom type radNewCfgSecBd based on Integer32"""
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


_RadNewCfgSecBd_Type.__name__ = "Integer32"
_RadNewCfgSecBd_Object = MibScalar
radNewCfgSecBd = _RadNewCfgSecBd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 3, 20),
    _RadNewCfgSecBd_Type()
)
radNewCfgSecBd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgSecBd.setStatus("current")
_AgNTP_ObjectIdentity = ObjectIdentity
agNTP = _AgNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4)
)
_AgCurCfgNTPServer_Type = IpAddress
_AgCurCfgNTPServer_Object = MibScalar
agCurCfgNTPServer = _AgCurCfgNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 1),
    _AgCurCfgNTPServer_Type()
)
agCurCfgNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPServer.setStatus("current")
_AgNewCfgNTPServer_Type = IpAddress
_AgNewCfgNTPServer_Object = MibScalar
agNewCfgNTPServer = _AgNewCfgNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 2),
    _AgNewCfgNTPServer_Type()
)
agNewCfgNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPServer.setStatus("current")


class _AgCurCfgNTPResyncInterval_Type(Integer32):
    """Custom type agCurCfgNTPResyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44640),
    )


_AgCurCfgNTPResyncInterval_Type.__name__ = "Integer32"
_AgCurCfgNTPResyncInterval_Object = MibScalar
agCurCfgNTPResyncInterval = _AgCurCfgNTPResyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 3),
    _AgCurCfgNTPResyncInterval_Type()
)
agCurCfgNTPResyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPResyncInterval.setStatus("current")


class _AgNewCfgNTPResyncInterval_Type(Integer32):
    """Custom type agNewCfgNTPResyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44640),
    )


_AgNewCfgNTPResyncInterval_Type.__name__ = "Integer32"
_AgNewCfgNTPResyncInterval_Object = MibScalar
agNewCfgNTPResyncInterval = _AgNewCfgNTPResyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 4),
    _AgNewCfgNTPResyncInterval_Type()
)
agNewCfgNTPResyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPResyncInterval.setStatus("current")


class _AgCurCfgNTPTzoneHHMM_Type(DisplayString):
    """Custom type agCurCfgNTPTzoneHHMM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AgCurCfgNTPTzoneHHMM_Type.__name__ = "DisplayString"
_AgCurCfgNTPTzoneHHMM_Object = MibScalar
agCurCfgNTPTzoneHHMM = _AgCurCfgNTPTzoneHHMM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 5),
    _AgCurCfgNTPTzoneHHMM_Type()
)
agCurCfgNTPTzoneHHMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPTzoneHHMM.setStatus("current")


class _AgNewCfgNTPTzoneHHMM_Type(DisplayString):
    """Custom type agNewCfgNTPTzoneHHMM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AgNewCfgNTPTzoneHHMM_Type.__name__ = "DisplayString"
_AgNewCfgNTPTzoneHHMM_Object = MibScalar
agNewCfgNTPTzoneHHMM = _AgNewCfgNTPTzoneHHMM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 6),
    _AgNewCfgNTPTzoneHHMM_Type()
)
agNewCfgNTPTzoneHHMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPTzoneHHMM.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 7),
    _AgCurCfgNTPDlight_Type()
)
agCurCfgNTPDlight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPDlight.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 8),
    _AgNewCfgNTPDlight_Type()
)
agNewCfgNTPDlight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPDlight.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 9),
    _AgCurCfgNTPService_Type()
)
agCurCfgNTPService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPService.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 10),
    _AgNewCfgNTPService_Type()
)
agNewCfgNTPService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPService.setStatus("current")
_AgCurCfgNTPSecServer_Type = IpAddress
_AgCurCfgNTPSecServer_Object = MibScalar
agCurCfgNTPSecServer = _AgCurCfgNTPSecServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 11),
    _AgCurCfgNTPSecServer_Type()
)
agCurCfgNTPSecServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPSecServer.setStatus("current")
_AgNewCfgNTPSecServer_Type = IpAddress
_AgNewCfgNTPSecServer_Object = MibScalar
agNewCfgNTPSecServer = _AgNewCfgNTPSecServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 4, 12),
    _AgNewCfgNTPSecServer_Type()
)
agNewCfgNTPSecServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPSecServer.setStatus("current")
_AgSyslog_ObjectIdentity = ObjectIdentity
agSyslog = _AgSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5)
)
_AgCurCfgSyslogHost_Type = IpAddress
_AgCurCfgSyslogHost_Object = MibScalar
agCurCfgSyslogHost = _AgCurCfgSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 1),
    _AgCurCfgSyslogHost_Type()
)
agCurCfgSyslogHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogHost.setStatus("current")
_AgNewCfgSyslogHost_Type = IpAddress
_AgNewCfgSyslogHost_Object = MibScalar
agNewCfgSyslogHost = _AgNewCfgSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 2),
    _AgNewCfgSyslogHost_Type()
)
agNewCfgSyslogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogHost.setStatus("current")
_AgCurCfgSyslog2Host_Type = IpAddress
_AgCurCfgSyslog2Host_Object = MibScalar
agCurCfgSyslog2Host = _AgCurCfgSyslog2Host_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 3),
    _AgCurCfgSyslog2Host_Type()
)
agCurCfgSyslog2Host.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslog2Host.setStatus("current")
_AgNewCfgSyslog2Host_Type = IpAddress
_AgNewCfgSyslog2Host_Object = MibScalar
agNewCfgSyslog2Host = _AgNewCfgSyslog2Host_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 4),
    _AgNewCfgSyslog2Host_Type()
)
agNewCfgSyslog2Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslog2Host.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 5),
    _AgCurCfgSyslogFac_Type()
)
agCurCfgSyslogFac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogFac.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 6),
    _AgNewCfgSyslogFac_Type()
)
agNewCfgSyslogFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogFac.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 7),
    _AgCurCfgSyslog2Fac_Type()
)
agCurCfgSyslog2Fac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslog2Fac.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 8),
    _AgNewCfgSyslog2Fac_Type()
)
agNewCfgSyslog2Fac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslog2Fac.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 9),
    _AgClrSyslogMsgs_Type()
)
agClrSyslogMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agClrSyslogMsgs.setStatus("current")
_AgSyslogMsgTableMaxSize_Type = Integer32
_AgSyslogMsgTableMaxSize_Object = MibScalar
agSyslogMsgTableMaxSize = _AgSyslogMsgTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 10),
    _AgSyslogMsgTableMaxSize_Type()
)
agSyslogMsgTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSyslogMsgTableMaxSize.setStatus("current")
_AgSyslogMsgTable_Object = MibTable
agSyslogMsgTable = _AgSyslogMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 11)
)
if mibBuilder.loadTexts:
    agSyslogMsgTable.setStatus("current")
_AgSyslogMsgTableEntry_Object = MibTableRow
agSyslogMsgTableEntry = _AgSyslogMsgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 11, 1)
)
agSyslogMsgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agSyslogMsgIndex"),
)
if mibBuilder.loadTexts:
    agSyslogMsgTableEntry.setStatus("current")
_AgSyslogMsgIndex_Type = Integer32
_AgSyslogMsgIndex_Object = MibTableColumn
agSyslogMsgIndex = _AgSyslogMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 11, 1, 1),
    _AgSyslogMsgIndex_Type()
)
agSyslogMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSyslogMsgIndex.setStatus("current")


class _AgSyslogMessage_Type(DisplayString):
    """Custom type agSyslogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgSyslogMessage_Type.__name__ = "DisplayString"
_AgSyslogMessage_Object = MibTableColumn
agSyslogMessage = _AgSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 11, 1, 2),
    _AgSyslogMessage_Type()
)
agSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSyslogMessage.setStatus("current")
_AgLog_ObjectIdentity = ObjectIdentity
agLog = _AgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12)
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 1),
    _AgNewCfgSyslogTrapConsole_Type()
)
agNewCfgSyslogTrapConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapConsole.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 2),
    _AgCurCfgSyslogTrapConsole_Type()
)
agCurCfgSyslogTrapConsole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapConsole.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 3),
    _AgNewCfgSyslogTrapSystem_Type()
)
agNewCfgSyslogTrapSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSystem.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 4),
    _AgCurCfgSyslogTrapSystem_Type()
)
agCurCfgSyslogTrapSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSystem.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 5),
    _AgNewCfgSyslogTrapMgmt_Type()
)
agNewCfgSyslogTrapMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapMgmt.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 6),
    _AgCurCfgSyslogTrapMgmt_Type()
)
agCurCfgSyslogTrapMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapMgmt.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 7),
    _AgNewCfgSyslogTrapCli_Type()
)
agNewCfgSyslogTrapCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapCli.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 8),
    _AgCurCfgSyslogTrapCli_Type()
)
agCurCfgSyslogTrapCli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapCli.setStatus("current")


class _AgNewCfgSyslogTrapStg_Type(Integer32):
    """Custom type agNewCfgSyslogTrapStg based on Integer32"""
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


_AgNewCfgSyslogTrapStg_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapStg_Object = MibScalar
agNewCfgSyslogTrapStg = _AgNewCfgSyslogTrapStg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 9),
    _AgNewCfgSyslogTrapStg_Type()
)
agNewCfgSyslogTrapStg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapStg.setStatus("current")


class _AgCurCfgSyslogTrapStg_Type(Integer32):
    """Custom type agCurCfgSyslogTrapStg based on Integer32"""
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


_AgCurCfgSyslogTrapStg_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapStg_Object = MibScalar
agCurCfgSyslogTrapStg = _AgCurCfgSyslogTrapStg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 10),
    _AgCurCfgSyslogTrapStg_Type()
)
agCurCfgSyslogTrapStg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapStg.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 11),
    _AgNewCfgSyslogTrapVlan_Type()
)
agNewCfgSyslogTrapVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapVlan.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 12),
    _AgCurCfgSyslogTrapVlan_Type()
)
agCurCfgSyslogTrapVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapVlan.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 19),
    _AgNewCfgSyslogTrapSsh_Type()
)
agNewCfgSyslogTrapSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSsh.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 20),
    _AgCurCfgSyslogTrapSsh_Type()
)
agCurCfgSyslogTrapSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSsh.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 21),
    _AgNewCfgSyslogTrapVrrp_Type()
)
agNewCfgSyslogTrapVrrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapVrrp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 22),
    _AgCurCfgSyslogTrapVrrp_Type()
)
agCurCfgSyslogTrapVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapVrrp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 25),
    _AgNewCfgSyslogTrapNtp_Type()
)
agNewCfgSyslogTrapNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapNtp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 26),
    _AgCurCfgSyslogTrapNtp_Type()
)
agCurCfgSyslogTrapNtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapNtp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 31),
    _AgNewCfgSyslogTrapIp_Type()
)
agNewCfgSyslogTrapIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapIp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 32),
    _AgCurCfgSyslogTrapIp_Type()
)
agCurCfgSyslogTrapIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapIp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 35),
    _AgNewCfgSyslogTrapWeb_Type()
)
agNewCfgSyslogTrapWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapWeb.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 36),
    _AgCurCfgSyslogTrapWeb_Type()
)
agCurCfgSyslogTrapWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapWeb.setStatus("current")


class _AgNewCfgSyslogTrapOspf_Type(Integer32):
    """Custom type agNewCfgSyslogTrapOspf based on Integer32"""
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


_AgNewCfgSyslogTrapOspf_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapOspf_Object = MibScalar
agNewCfgSyslogTrapOspf = _AgNewCfgSyslogTrapOspf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 41),
    _AgNewCfgSyslogTrapOspf_Type()
)
agNewCfgSyslogTrapOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapOspf.setStatus("current")


class _AgCurCfgSyslogTrapOspf_Type(Integer32):
    """Custom type agCurCfgSyslogTrapOspf based on Integer32"""
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


_AgCurCfgSyslogTrapOspf_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapOspf_Object = MibScalar
agCurCfgSyslogTrapOspf = _AgCurCfgSyslogTrapOspf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 42),
    _AgCurCfgSyslogTrapOspf_Type()
)
agCurCfgSyslogTrapOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapOspf.setStatus("current")


class _AgNewCfgSyslogTrapRmon_Type(Integer32):
    """Custom type agNewCfgSyslogTrapRmon based on Integer32"""
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


_AgNewCfgSyslogTrapRmon_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapRmon_Object = MibScalar
agNewCfgSyslogTrapRmon = _AgNewCfgSyslogTrapRmon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 45),
    _AgNewCfgSyslogTrapRmon_Type()
)
agNewCfgSyslogTrapRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapRmon.setStatus("current")


class _AgCurCfgSyslogTrapRmon_Type(Integer32):
    """Custom type agCurCfgSyslogTrapRmon based on Integer32"""
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


_AgCurCfgSyslogTrapRmon_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapRmon_Object = MibScalar
agCurCfgSyslogTrapRmon = _AgCurCfgSyslogTrapRmon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 46),
    _AgCurCfgSyslogTrapRmon_Type()
)
agCurCfgSyslogTrapRmon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapRmon.setStatus("current")


class _AgNewCfgSyslogTrapUfd_Type(Integer32):
    """Custom type agNewCfgSyslogTrapUfd based on Integer32"""
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


_AgNewCfgSyslogTrapUfd_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapUfd_Object = MibScalar
agNewCfgSyslogTrapUfd = _AgNewCfgSyslogTrapUfd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 47),
    _AgNewCfgSyslogTrapUfd_Type()
)
agNewCfgSyslogTrapUfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapUfd.setStatus("current")


class _AgCurCfgSyslogTrapUfd_Type(Integer32):
    """Custom type agCurCfgSyslogTrapUfd based on Integer32"""
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


_AgCurCfgSyslogTrapUfd_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapUfd_Object = MibScalar
agCurCfgSyslogTrapUfd = _AgCurCfgSyslogTrapUfd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 48),
    _AgCurCfgSyslogTrapUfd_Type()
)
agCurCfgSyslogTrapUfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapUfd.setStatus("current")


class _AgNewCfgSyslogTrapCfg_Type(Integer32):
    """Custom type agNewCfgSyslogTrapCfg based on Integer32"""
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


_AgNewCfgSyslogTrapCfg_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapCfg_Object = MibScalar
agNewCfgSyslogTrapCfg = _AgNewCfgSyslogTrapCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 49),
    _AgNewCfgSyslogTrapCfg_Type()
)
agNewCfgSyslogTrapCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapCfg.setStatus("current")


class _AgCurCfgSyslogTrapCfg_Type(Integer32):
    """Custom type agCurCfgSyslogTrapCfg based on Integer32"""
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


_AgCurCfgSyslogTrapCfg_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapCfg_Object = MibScalar
agCurCfgSyslogTrapCfg = _AgCurCfgSyslogTrapCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 50),
    _AgCurCfgSyslogTrapCfg_Type()
)
agCurCfgSyslogTrapCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapCfg.setStatus("current")


class _AgNewCfgSyslogTrap8021x_Type(Integer32):
    """Custom type agNewCfgSyslogTrap8021x based on Integer32"""
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


_AgNewCfgSyslogTrap8021x_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrap8021x_Object = MibScalar
agNewCfgSyslogTrap8021x = _AgNewCfgSyslogTrap8021x_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 51),
    _AgNewCfgSyslogTrap8021x_Type()
)
agNewCfgSyslogTrap8021x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrap8021x.setStatus("current")


class _AgCurCfgSyslogTrap8021x_Type(Integer32):
    """Custom type agCurCfgSyslogTrap8021x based on Integer32"""
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


_AgCurCfgSyslogTrap8021x_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrap8021x_Object = MibScalar
agCurCfgSyslogTrap8021x = _AgCurCfgSyslogTrap8021x_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 52),
    _AgCurCfgSyslogTrap8021x_Type()
)
agCurCfgSyslogTrap8021x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrap8021x.setStatus("current")


class _AgNewCfgSyslogTrapHotlinks_Type(Integer32):
    """Custom type agNewCfgSyslogTrapHotlinks based on Integer32"""
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


_AgNewCfgSyslogTrapHotlinks_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapHotlinks_Object = MibScalar
agNewCfgSyslogTrapHotlinks = _AgNewCfgSyslogTrapHotlinks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 53),
    _AgNewCfgSyslogTrapHotlinks_Type()
)
agNewCfgSyslogTrapHotlinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapHotlinks.setStatus("current")


class _AgCurCfgSyslogTrapHotlinks_Type(Integer32):
    """Custom type agCurCfgSyslogTrapHotlinks based on Integer32"""
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


_AgCurCfgSyslogTrapHotlinks_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapHotlinks_Object = MibScalar
agCurCfgSyslogTrapHotlinks = _AgCurCfgSyslogTrapHotlinks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 12, 54),
    _AgCurCfgSyslogTrapHotlinks_Type()
)
agCurCfgSyslogTrapHotlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapHotlinks.setStatus("current")


class _AgCurCfgSyslogSev_Type(Integer32):
    """Custom type agCurCfgSyslogSev based on Integer32"""
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
        *(("alert1", 2),
          ("crit2", 3),
          ("debug7", 8),
          ("emerg0", 1),
          ("err3", 4),
          ("info6", 7),
          ("notice5", 6),
          ("warning4", 5))
    )


_AgCurCfgSyslogSev_Type.__name__ = "Integer32"
_AgCurCfgSyslogSev_Object = MibScalar
agCurCfgSyslogSev = _AgCurCfgSyslogSev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 13),
    _AgCurCfgSyslogSev_Type()
)
agCurCfgSyslogSev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogSev.setStatus("current")


class _AgNewCfgSyslogSev_Type(Integer32):
    """Custom type agNewCfgSyslogSev based on Integer32"""
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
        *(("alert1", 2),
          ("crit2", 3),
          ("debug7", 8),
          ("emerg0", 1),
          ("err3", 4),
          ("info6", 7),
          ("notice5", 6),
          ("warning4", 5))
    )


_AgNewCfgSyslogSev_Type.__name__ = "Integer32"
_AgNewCfgSyslogSev_Object = MibScalar
agNewCfgSyslogSev = _AgNewCfgSyslogSev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 14),
    _AgNewCfgSyslogSev_Type()
)
agNewCfgSyslogSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogSev.setStatus("current")


class _AgCurCfgSyslog2Sev_Type(Integer32):
    """Custom type agCurCfgSyslog2Sev based on Integer32"""
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
        *(("alert1", 2),
          ("crit2", 3),
          ("debug7", 8),
          ("emerg0", 1),
          ("err3", 4),
          ("info6", 7),
          ("notice5", 6),
          ("warning4", 5))
    )


_AgCurCfgSyslog2Sev_Type.__name__ = "Integer32"
_AgCurCfgSyslog2Sev_Object = MibScalar
agCurCfgSyslog2Sev = _AgCurCfgSyslog2Sev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 15),
    _AgCurCfgSyslog2Sev_Type()
)
agCurCfgSyslog2Sev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslog2Sev.setStatus("current")


class _AgNewCfgSyslog2Sev_Type(Integer32):
    """Custom type agNewCfgSyslog2Sev based on Integer32"""
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
        *(("alert1", 2),
          ("crit2", 3),
          ("debug7", 8),
          ("emerg0", 1),
          ("err3", 4),
          ("info6", 7),
          ("notice5", 6),
          ("warning4", 5))
    )


_AgNewCfgSyslog2Sev_Type.__name__ = "Integer32"
_AgNewCfgSyslog2Sev_Object = MibScalar
agNewCfgSyslog2Sev = _AgNewCfgSyslog2Sev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 5, 16),
    _AgNewCfgSyslog2Sev_Type()
)
agNewCfgSyslog2Sev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslog2Sev.setStatus("current")
_AgTrapHost_ObjectIdentity = ObjectIdentity
agTrapHost = _AgTrapHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6)
)
_AgTrapHostTableMaxEnt_Type = Integer32
_AgTrapHostTableMaxEnt_Object = MibScalar
agTrapHostTableMaxEnt = _AgTrapHostTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 1),
    _AgTrapHostTableMaxEnt_Type()
)
agTrapHostTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTrapHostTableMaxEnt.setStatus("current")
_AgCurCfgTrapHostTable_Object = MibTable
agCurCfgTrapHostTable = _AgCurCfgTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    agCurCfgTrapHostTable.setStatus("current")
_AgCurCfgTrapHostEntry_Object = MibTableRow
agCurCfgTrapHostEntry = _AgCurCfgTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 2, 1)
)
agCurCfgTrapHostEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agCurCfgTrapHostIndx"),
)
if mibBuilder.loadTexts:
    agCurCfgTrapHostEntry.setStatus("current")
_AgCurCfgTrapHostIndx_Type = Integer32
_AgCurCfgTrapHostIndx_Object = MibTableColumn
agCurCfgTrapHostIndx = _AgCurCfgTrapHostIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 2, 1, 1),
    _AgCurCfgTrapHostIndx_Type()
)
agCurCfgTrapHostIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostIndx.setStatus("current")
_AgCurCfgTrapHostIpAddr_Type = IpAddress
_AgCurCfgTrapHostIpAddr_Object = MibTableColumn
agCurCfgTrapHostIpAddr = _AgCurCfgTrapHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 2, 1, 2),
    _AgCurCfgTrapHostIpAddr_Type()
)
agCurCfgTrapHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostIpAddr.setStatus("current")


class _AgCurCfgTrapHostCommString_Type(DisplayString):
    """Custom type agCurCfgTrapHostCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgCurCfgTrapHostCommString_Type.__name__ = "DisplayString"
_AgCurCfgTrapHostCommString_Object = MibTableColumn
agCurCfgTrapHostCommString = _AgCurCfgTrapHostCommString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 2, 1, 3),
    _AgCurCfgTrapHostCommString_Type()
)
agCurCfgTrapHostCommString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostCommString.setStatus("current")
_AgNewCfgTrapHostTable_Object = MibTable
agNewCfgTrapHostTable = _AgNewCfgTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    agNewCfgTrapHostTable.setStatus("current")
_AgNewCfgTrapHostEntry_Object = MibTableRow
agNewCfgTrapHostEntry = _AgNewCfgTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 3, 1)
)
agNewCfgTrapHostEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agNewCfgTrapHostIndx"),
)
if mibBuilder.loadTexts:
    agNewCfgTrapHostEntry.setStatus("current")
_AgNewCfgTrapHostIndx_Type = Integer32
_AgNewCfgTrapHostIndx_Object = MibTableColumn
agNewCfgTrapHostIndx = _AgNewCfgTrapHostIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 3, 1, 1),
    _AgNewCfgTrapHostIndx_Type()
)
agNewCfgTrapHostIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgTrapHostIndx.setStatus("current")
_AgNewCfgTrapHostIpAddr_Type = IpAddress
_AgNewCfgTrapHostIpAddr_Object = MibTableColumn
agNewCfgTrapHostIpAddr = _AgNewCfgTrapHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 3, 1, 2),
    _AgNewCfgTrapHostIpAddr_Type()
)
agNewCfgTrapHostIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTrapHostIpAddr.setStatus("current")


class _AgNewCfgTrapHostCommString_Type(DisplayString):
    """Custom type agNewCfgTrapHostCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgNewCfgTrapHostCommString_Type.__name__ = "DisplayString"
_AgNewCfgTrapHostCommString_Object = MibTableColumn
agNewCfgTrapHostCommString = _AgNewCfgTrapHostCommString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 6, 3, 1, 3),
    _AgNewCfgTrapHostCommString_Type()
)
agNewCfgTrapHostCommString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTrapHostCommString.setStatus("current")
_AgTftp_ObjectIdentity = ObjectIdentity
agTftp = _AgTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7)
)


class _AgTftpServer_Type(DisplayString):
    """Custom type agTftpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgTftpServer_Type.__name__ = "DisplayString"
_AgTftpServer_Object = MibScalar
agTftpServer = _AgTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 1),
    _AgTftpServer_Type()
)
agTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpServer.setStatus("current")


class _AgTftpImage_Type(Integer32):
    """Custom type agTftpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("boot", 4),
          ("image1", 2),
          ("image2", 3))
    )


_AgTftpImage_Type.__name__ = "Integer32"
_AgTftpImage_Object = MibScalar
agTftpImage = _AgTftpImage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 2),
    _AgTftpImage_Type()
)
agTftpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpImage.setStatus("current")


class _AgTftpImageFileName_Type(DisplayString):
    """Custom type agTftpImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpImageFileName_Type.__name__ = "DisplayString"
_AgTftpImageFileName_Object = MibScalar
agTftpImageFileName = _AgTftpImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 3),
    _AgTftpImageFileName_Type()
)
agTftpImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpImageFileName.setStatus("current")


class _AgTftpCfgFileName_Type(DisplayString):
    """Custom type agTftpCfgFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpCfgFileName_Type.__name__ = "DisplayString"
_AgTftpCfgFileName_Object = MibScalar
agTftpCfgFileName = _AgTftpCfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 4),
    _AgTftpCfgFileName_Type()
)
agTftpCfgFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpCfgFileName.setStatus("current")


class _AgTftpDumpFileName_Type(DisplayString):
    """Custom type agTftpDumpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpDumpFileName_Type.__name__ = "DisplayString"
_AgTftpDumpFileName_Object = MibScalar
agTftpDumpFileName = _AgTftpDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 5),
    _AgTftpDumpFileName_Type()
)
agTftpDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpDumpFileName.setStatus("current")


class _AgTftpAction_Type(Integer32):
    """Custom type agTftpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cfg-get", 3),
          ("cfg-put", 4),
          ("dump-put", 5),
          ("img-get", 2),
          ("img-put", 7),
          ("other", 1),
          ("tsdump-put", 8))
    )


_AgTftpAction_Type.__name__ = "Integer32"
_AgTftpAction_Object = MibScalar
agTftpAction = _AgTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 6),
    _AgTftpAction_Type()
)
agTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpAction.setStatus("current")


class _AgTftpLastActionStatus_Type(DisplayString):
    """Custom type agTftpLastActionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpLastActionStatus_Type.__name__ = "DisplayString"
_AgTftpLastActionStatus_Object = MibScalar
agTftpLastActionStatus = _AgTftpLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 7),
    _AgTftpLastActionStatus_Type()
)
agTftpLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTftpLastActionStatus.setStatus("current")


class _AgTftpUserName_Type(DisplayString):
    """Custom type agTftpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpUserName_Type.__name__ = "DisplayString"
_AgTftpUserName_Object = MibScalar
agTftpUserName = _AgTftpUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 9),
    _AgTftpUserName_Type()
)
agTftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpUserName.setStatus("current")


class _AgTftpPassword_Type(DisplayString):
    """Custom type agTftpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpPassword_Type.__name__ = "DisplayString"
_AgTftpPassword_Object = MibScalar
agTftpPassword = _AgTftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 10),
    _AgTftpPassword_Type()
)
agTftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpPassword.setStatus("current")


class _AgTftpTSDumpFileName_Type(DisplayString):
    """Custom type agTftpTSDumpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpTSDumpFileName_Type.__name__ = "DisplayString"
_AgTftpTSDumpFileName_Object = MibScalar
agTftpTSDumpFileName = _AgTftpTSDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 7, 11),
    _AgTftpTSDumpFileName_Type()
)
agTftpTSDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpTSDumpFileName.setStatus("current")
_AgApply_ObjectIdentity = ObjectIdentity
agApply = _AgApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8)
)


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8, 1),
    _AgApplyPending_Type()
)
agApplyPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyPending.setStatus("current")


class _AgApplyConfig_Type(Integer32):
    """Custom type agApplyConfig based on Integer32"""
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
        *(("apply", 1),
          ("complete", 4),
          ("failed", 5),
          ("idle", 2),
          ("inprogress", 3))
    )


_AgApplyConfig_Type.__name__ = "Integer32"
_AgApplyConfig_Object = MibScalar
agApplyConfig = _AgApplyConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8, 2),
    _AgApplyConfig_Type()
)
agApplyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agApplyConfig.setStatus("current")
_AgApplyTableSize_Type = Integer32
_AgApplyTableSize_Object = MibScalar
agApplyTableSize = _AgApplyTableSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8, 4),
    _AgApplyTableSize_Type()
)
agApplyTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyTableSize.setStatus("current")
_AgApplyTable_Object = MibTable
agApplyTable = _AgApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    agApplyTable.setStatus("current")
_AgApplyTableEntry_Object = MibTableRow
agApplyTableEntry = _AgApplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8, 5, 1)
)
agApplyTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agApplyIndex"),
)
if mibBuilder.loadTexts:
    agApplyTableEntry.setStatus("current")
_AgApplyIndex_Type = Integer32
_AgApplyIndex_Object = MibTableColumn
agApplyIndex = _AgApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8, 5, 1, 1),
    _AgApplyIndex_Type()
)
agApplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyIndex.setStatus("current")
_AgApplyString_Type = OctetString
_AgApplyString_Object = MibTableColumn
agApplyString = _AgApplyString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 8, 5, 1, 2),
    _AgApplyString_Type()
)
agApplyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyString.setStatus("current")
_AgTacacsConfig_ObjectIdentity = ObjectIdentity
agTacacsConfig = _AgTacacsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10)
)
_TacCurCfgPrimaryIpAddr_Type = IpAddress
_TacCurCfgPrimaryIpAddr_Object = MibScalar
tacCurCfgPrimaryIpAddr = _TacCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 1),
    _TacCurCfgPrimaryIpAddr_Type()
)
tacCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgPrimaryIpAddr.setStatus("current")
_TacNewCfgPrimaryIpAddr_Type = IpAddress
_TacNewCfgPrimaryIpAddr_Object = MibScalar
tacNewCfgPrimaryIpAddr = _TacNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 2),
    _TacNewCfgPrimaryIpAddr_Type()
)
tacNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgPrimaryIpAddr.setStatus("current")
_TacCurCfgSecondaryIpAddr_Type = IpAddress
_TacCurCfgSecondaryIpAddr_Object = MibScalar
tacCurCfgSecondaryIpAddr = _TacCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 3),
    _TacCurCfgSecondaryIpAddr_Type()
)
tacCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgSecondaryIpAddr.setStatus("current")
_TacNewCfgSecondaryIpAddr_Type = IpAddress
_TacNewCfgSecondaryIpAddr_Object = MibScalar
tacNewCfgSecondaryIpAddr = _TacNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 4),
    _TacNewCfgSecondaryIpAddr_Type()
)
tacNewCfgSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgSecondaryIpAddr.setStatus("current")


class _TacCurCfgPort_Type(Integer32):
    """Custom type tacCurCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_TacCurCfgPort_Type.__name__ = "Integer32"
_TacCurCfgPort_Object = MibScalar
tacCurCfgPort = _TacCurCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 5),
    _TacCurCfgPort_Type()
)
tacCurCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgPort.setStatus("current")


class _TacNewCfgPort_Type(Integer32):
    """Custom type tacNewCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_TacNewCfgPort_Type.__name__ = "Integer32"
_TacNewCfgPort_Object = MibScalar
tacNewCfgPort = _TacNewCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 6),
    _TacNewCfgPort_Type()
)
tacNewCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgPort.setStatus("current")


class _TacCurCfgTimeout_Type(Integer32):
    """Custom type tacCurCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_TacCurCfgTimeout_Type.__name__ = "Integer32"
_TacCurCfgTimeout_Object = MibScalar
tacCurCfgTimeout = _TacCurCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 7),
    _TacCurCfgTimeout_Type()
)
tacCurCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgTimeout.setStatus("current")


class _TacNewCfgTimeout_Type(Integer32):
    """Custom type tacNewCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_TacNewCfgTimeout_Type.__name__ = "Integer32"
_TacNewCfgTimeout_Object = MibScalar
tacNewCfgTimeout = _TacNewCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 8),
    _TacNewCfgTimeout_Type()
)
tacNewCfgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgTimeout.setStatus("current")


class _TacCurCfgRetries_Type(Integer32):
    """Custom type tacCurCfgRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TacCurCfgRetries_Type.__name__ = "Integer32"
_TacCurCfgRetries_Object = MibScalar
tacCurCfgRetries = _TacCurCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 9),
    _TacCurCfgRetries_Type()
)
tacCurCfgRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgRetries.setStatus("current")


class _TacNewCfgRetries_Type(Integer32):
    """Custom type tacNewCfgRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TacNewCfgRetries_Type.__name__ = "Integer32"
_TacNewCfgRetries_Object = MibScalar
tacNewCfgRetries = _TacNewCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 10),
    _TacNewCfgRetries_Type()
)
tacNewCfgRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgRetries.setStatus("current")


class _TacCurCfgState_Type(Integer32):
    """Custom type tacCurCfgState based on Integer32"""
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


_TacCurCfgState_Type.__name__ = "Integer32"
_TacCurCfgState_Object = MibScalar
tacCurCfgState = _TacCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 11),
    _TacCurCfgState_Type()
)
tacCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgState.setStatus("current")


class _TacNewCfgState_Type(Integer32):
    """Custom type tacNewCfgState based on Integer32"""
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


_TacNewCfgState_Type.__name__ = "Integer32"
_TacNewCfgState_Object = MibScalar
tacNewCfgState = _TacNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 12),
    _TacNewCfgState_Type()
)
tacNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgState.setStatus("current")


class _TacCurCfgAuthenString_Type(DisplayString):
    """Custom type tacCurCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TacCurCfgAuthenString_Type.__name__ = "DisplayString"
_TacCurCfgAuthenString_Object = MibScalar
tacCurCfgAuthenString = _TacCurCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 13),
    _TacCurCfgAuthenString_Type()
)
tacCurCfgAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgAuthenString.setStatus("current")


class _TacNewCfgAuthenString_Type(DisplayString):
    """Custom type tacNewCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TacNewCfgAuthenString_Type.__name__ = "DisplayString"
_TacNewCfgAuthenString_Object = MibScalar
tacNewCfgAuthenString = _TacNewCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 14),
    _TacNewCfgAuthenString_Type()
)
tacNewCfgAuthenString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgAuthenString.setStatus("current")


class _TacCurCfgTelnet_Type(Integer32):
    """Custom type tacCurCfgTelnet based on Integer32"""
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


_TacCurCfgTelnet_Type.__name__ = "Integer32"
_TacCurCfgTelnet_Object = MibScalar
tacCurCfgTelnet = _TacCurCfgTelnet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 15),
    _TacCurCfgTelnet_Type()
)
tacCurCfgTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgTelnet.setStatus("current")


class _TacNewCfgTelnet_Type(Integer32):
    """Custom type tacNewCfgTelnet based on Integer32"""
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


_TacNewCfgTelnet_Type.__name__ = "Integer32"
_TacNewCfgTelnet_Object = MibScalar
tacNewCfgTelnet = _TacNewCfgTelnet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 16),
    _TacNewCfgTelnet_Type()
)
tacNewCfgTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgTelnet.setStatus("current")


class _TacCurCfgAuthenSecondString_Type(DisplayString):
    """Custom type tacCurCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TacCurCfgAuthenSecondString_Type.__name__ = "DisplayString"
_TacCurCfgAuthenSecondString_Object = MibScalar
tacCurCfgAuthenSecondString = _TacCurCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 17),
    _TacCurCfgAuthenSecondString_Type()
)
tacCurCfgAuthenSecondString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgAuthenSecondString.setStatus("current")


class _TacNewCfgAuthenSecondString_Type(DisplayString):
    """Custom type tacNewCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TacNewCfgAuthenSecondString_Type.__name__ = "DisplayString"
_TacNewCfgAuthenSecondString_Object = MibScalar
tacNewCfgAuthenSecondString = _TacNewCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 18),
    _TacNewCfgAuthenSecondString_Type()
)
tacNewCfgAuthenSecondString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgAuthenSecondString.setStatus("current")


class _TacCurCfgSecBd_Type(Integer32):
    """Custom type tacCurCfgSecBd based on Integer32"""
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


_TacCurCfgSecBd_Type.__name__ = "Integer32"
_TacCurCfgSecBd_Object = MibScalar
tacCurCfgSecBd = _TacCurCfgSecBd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 23),
    _TacCurCfgSecBd_Type()
)
tacCurCfgSecBd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgSecBd.setStatus("current")


class _TacNewCfgSecBd_Type(Integer32):
    """Custom type tacNewCfgSecBd based on Integer32"""
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


_TacNewCfgSecBd_Type.__name__ = "Integer32"
_TacNewCfgSecBd_Object = MibScalar
tacNewCfgSecBd = _TacNewCfgSecBd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 24),
    _TacNewCfgSecBd_Type()
)
tacNewCfgSecBd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgSecBd.setStatus("current")


class _TacCurCfgCmap_Type(Integer32):
    """Custom type tacCurCfgCmap based on Integer32"""
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


_TacCurCfgCmap_Type.__name__ = "Integer32"
_TacCurCfgCmap_Object = MibScalar
tacCurCfgCmap = _TacCurCfgCmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 25),
    _TacCurCfgCmap_Type()
)
tacCurCfgCmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgCmap.setStatus("current")


class _TacNewCfgCmap_Type(Integer32):
    """Custom type tacNewCfgCmap based on Integer32"""
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


_TacNewCfgCmap_Type.__name__ = "Integer32"
_TacNewCfgCmap_Object = MibScalar
tacNewCfgCmap = _TacNewCfgCmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 26),
    _TacNewCfgCmap_Type()
)
tacNewCfgCmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgCmap.setStatus("current")
_AgTacacsUserMapCurCfgTable_Object = MibTable
agTacacsUserMapCurCfgTable = _AgTacacsUserMapCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 31)
)
if mibBuilder.loadTexts:
    agTacacsUserMapCurCfgTable.setStatus("current")
_AgTacacsUserMapCurCfgTableEntry_Object = MibTableRow
agTacacsUserMapCurCfgTableEntry = _AgTacacsUserMapCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 31, 1)
)
agTacacsUserMapCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agTacacsUserMapCurCfgUId"),
)
if mibBuilder.loadTexts:
    agTacacsUserMapCurCfgTableEntry.setStatus("current")
_AgTacacsUserMapCurCfgUId_Type = Integer32
_AgTacacsUserMapCurCfgUId_Object = MibTableColumn
agTacacsUserMapCurCfgUId = _AgTacacsUserMapCurCfgUId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 31, 1, 1),
    _AgTacacsUserMapCurCfgUId_Type()
)
agTacacsUserMapCurCfgUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTacacsUserMapCurCfgUId.setStatus("current")


class _AgTacacsUserMapCurCfgMapping_Type(Integer32):
    """Custom type agTacacsUserMapCurCfgMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin", 3),
          ("invalid", 0),
          ("oper", 2),
          ("user", 1))
    )


_AgTacacsUserMapCurCfgMapping_Type.__name__ = "Integer32"
_AgTacacsUserMapCurCfgMapping_Object = MibTableColumn
agTacacsUserMapCurCfgMapping = _AgTacacsUserMapCurCfgMapping_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 31, 1, 2),
    _AgTacacsUserMapCurCfgMapping_Type()
)
agTacacsUserMapCurCfgMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTacacsUserMapCurCfgMapping.setStatus("current")
_AgTacacsUserMapNewCfgTable_Object = MibTable
agTacacsUserMapNewCfgTable = _AgTacacsUserMapNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 32)
)
if mibBuilder.loadTexts:
    agTacacsUserMapNewCfgTable.setStatus("current")
_AgTacacsUserMapNewCfgTableEntry_Object = MibTableRow
agTacacsUserMapNewCfgTableEntry = _AgTacacsUserMapNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 32, 1)
)
agTacacsUserMapNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agTacacsUserMapNewCfgUId"),
)
if mibBuilder.loadTexts:
    agTacacsUserMapNewCfgTableEntry.setStatus("current")
_AgTacacsUserMapNewCfgUId_Type = Integer32
_AgTacacsUserMapNewCfgUId_Object = MibTableColumn
agTacacsUserMapNewCfgUId = _AgTacacsUserMapNewCfgUId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 32, 1, 1),
    _AgTacacsUserMapNewCfgUId_Type()
)
agTacacsUserMapNewCfgUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTacacsUserMapNewCfgUId.setStatus("current")


class _AgTacacsUserMapNewCfgMapping_Type(Integer32):
    """Custom type agTacacsUserMapNewCfgMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin", 3),
          ("invalid", 0),
          ("oper", 2),
          ("user", 1))
    )


_AgTacacsUserMapNewCfgMapping_Type.__name__ = "Integer32"
_AgTacacsUserMapNewCfgMapping_Object = MibTableColumn
agTacacsUserMapNewCfgMapping = _AgTacacsUserMapNewCfgMapping_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 10, 32, 1, 2),
    _AgTacacsUserMapNewCfgMapping_Type()
)
agTacacsUserMapNewCfgMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agTacacsUserMapNewCfgMapping.setStatus("current")
_AgMgmtNetConfig_ObjectIdentity = ObjectIdentity
agMgmtNetConfig = _AgMgmtNetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11)
)
_AgMgmtNetTableMaxSize_Type = Integer32
_AgMgmtNetTableMaxSize_Object = MibScalar
agMgmtNetTableMaxSize = _AgMgmtNetTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 1),
    _AgMgmtNetTableMaxSize_Type()
)
agMgmtNetTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtNetTableMaxSize.setStatus("current")
_AgCurCfgMgmtNetTable_Object = MibTable
agCurCfgMgmtNetTable = _AgCurCfgMgmtNetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    agCurCfgMgmtNetTable.setStatus("current")
_AgCurCfgMgmtNetEntry_Object = MibTableRow
agCurCfgMgmtNetEntry = _AgCurCfgMgmtNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 2, 1)
)
agCurCfgMgmtNetEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agCurCfgMgmtNetIndex"),
)
if mibBuilder.loadTexts:
    agCurCfgMgmtNetEntry.setStatus("current")
_AgCurCfgMgmtNetIndex_Type = Integer32
_AgCurCfgMgmtNetIndex_Object = MibTableColumn
agCurCfgMgmtNetIndex = _AgCurCfgMgmtNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 2, 1, 1),
    _AgCurCfgMgmtNetIndex_Type()
)
agCurCfgMgmtNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtNetIndex.setStatus("current")
_AgCurCfgMgmtNetSubnet_Type = IpAddress
_AgCurCfgMgmtNetSubnet_Object = MibTableColumn
agCurCfgMgmtNetSubnet = _AgCurCfgMgmtNetSubnet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 2, 1, 2),
    _AgCurCfgMgmtNetSubnet_Type()
)
agCurCfgMgmtNetSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtNetSubnet.setStatus("current")
_AgCurCfgMgmtNetMask_Type = IpAddress
_AgCurCfgMgmtNetMask_Object = MibTableColumn
agCurCfgMgmtNetMask = _AgCurCfgMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 2, 1, 3),
    _AgCurCfgMgmtNetMask_Type()
)
agCurCfgMgmtNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtNetMask.setStatus("current")
_AgNewCfgMgmtNetTable_Object = MibTable
agNewCfgMgmtNetTable = _AgNewCfgMgmtNetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    agNewCfgMgmtNetTable.setStatus("current")
_AgNewCfgMgmtNetEntry_Object = MibTableRow
agNewCfgMgmtNetEntry = _AgNewCfgMgmtNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 3, 1)
)
agNewCfgMgmtNetEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agNewCfgMgmtNetIndex"),
)
if mibBuilder.loadTexts:
    agNewCfgMgmtNetEntry.setStatus("current")
_AgNewCfgMgmtNetIndex_Type = Integer32
_AgNewCfgMgmtNetIndex_Object = MibTableColumn
agNewCfgMgmtNetIndex = _AgNewCfgMgmtNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 3, 1, 1),
    _AgNewCfgMgmtNetIndex_Type()
)
agNewCfgMgmtNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetIndex.setStatus("current")
_AgNewCfgMgmtNetSubnet_Type = IpAddress
_AgNewCfgMgmtNetSubnet_Object = MibTableColumn
agNewCfgMgmtNetSubnet = _AgNewCfgMgmtNetSubnet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 3, 1, 2),
    _AgNewCfgMgmtNetSubnet_Type()
)
agNewCfgMgmtNetSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetSubnet.setStatus("current")
_AgNewCfgMgmtNetMask_Type = IpAddress
_AgNewCfgMgmtNetMask_Object = MibTableColumn
agNewCfgMgmtNetMask = _AgNewCfgMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 3, 1, 3),
    _AgNewCfgMgmtNetMask_Type()
)
agNewCfgMgmtNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetMask.setStatus("current")


class _AgNewCfgMgmtNetDelete_Type(Integer32):
    """Custom type agNewCfgMgmtNetDelete based on Integer32"""
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


_AgNewCfgMgmtNetDelete_Type.__name__ = "Integer32"
_AgNewCfgMgmtNetDelete_Object = MibTableColumn
agNewCfgMgmtNetDelete = _AgNewCfgMgmtNetDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 11, 3, 1, 4),
    _AgNewCfgMgmtNetDelete_Type()
)
agNewCfgMgmtNetDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetDelete.setStatus("current")
_AgAccess_ObjectIdentity = ObjectIdentity
agAccess = _AgAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12)
)
_AgAccessUserMaxUserID_Type = Integer32
_AgAccessUserMaxUserID_Object = MibScalar
agAccessUserMaxUserID = _AgAccessUserMaxUserID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 1),
    _AgAccessUserMaxUserID_Type()
)
agAccessUserMaxUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAccessUserMaxUserID.setStatus("current")
_AgAccessUserCurCfgTable_Object = MibTable
agAccessUserCurCfgTable = _AgAccessUserCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    agAccessUserCurCfgTable.setStatus("current")
_AgAccessUserCurCfgTableEntry_Object = MibTableRow
agAccessUserCurCfgTableEntry = _AgAccessUserCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 2, 1)
)
agAccessUserCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agAccessUserCurCfgUId"),
)
if mibBuilder.loadTexts:
    agAccessUserCurCfgTableEntry.setStatus("current")
_AgAccessUserCurCfgUId_Type = Integer32
_AgAccessUserCurCfgUId_Object = MibTableColumn
agAccessUserCurCfgUId = _AgAccessUserCurCfgUId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 2, 1, 1),
    _AgAccessUserCurCfgUId_Type()
)
agAccessUserCurCfgUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAccessUserCurCfgUId.setStatus("current")


class _AgAccessUserCurCos_Type(Integer32):
    """Custom type agAccessUserCurCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("admin", 6),
          ("oper", 3),
          ("user", 0))
    )


_AgAccessUserCurCos_Type.__name__ = "Integer32"
_AgAccessUserCurCos_Object = MibTableColumn
agAccessUserCurCos = _AgAccessUserCurCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 2, 1, 2),
    _AgAccessUserCurCos_Type()
)
agAccessUserCurCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAccessUserCurCos.setStatus("current")


class _AgAccessUserCurCfgName_Type(DisplayString):
    """Custom type agAccessUserCurCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AgAccessUserCurCfgName_Type.__name__ = "DisplayString"
_AgAccessUserCurCfgName_Object = MibTableColumn
agAccessUserCurCfgName = _AgAccessUserCurCfgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 2, 1, 3),
    _AgAccessUserCurCfgName_Type()
)
agAccessUserCurCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAccessUserCurCfgName.setStatus("current")


class _AgAccessUserCurCfgPswd_Type(DisplayString):
    """Custom type agAccessUserCurCfgPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgAccessUserCurCfgPswd_Type.__name__ = "DisplayString"
_AgAccessUserCurCfgPswd_Object = MibTableColumn
agAccessUserCurCfgPswd = _AgAccessUserCurCfgPswd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 2, 1, 4),
    _AgAccessUserCurCfgPswd_Type()
)
agAccessUserCurCfgPswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAccessUserCurCfgPswd.setStatus("current")


class _AgAccessUserCurCfgState_Type(Integer32):
    """Custom type agAccessUserCurCfgState based on Integer32"""
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


_AgAccessUserCurCfgState_Type.__name__ = "Integer32"
_AgAccessUserCurCfgState_Object = MibTableColumn
agAccessUserCurCfgState = _AgAccessUserCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 2, 1, 5),
    _AgAccessUserCurCfgState_Type()
)
agAccessUserCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAccessUserCurCfgState.setStatus("current")
_AgAccessUserNewCfgTable_Object = MibTable
agAccessUserNewCfgTable = _AgAccessUserNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3)
)
if mibBuilder.loadTexts:
    agAccessUserNewCfgTable.setStatus("current")
_AgAccessUserNewCfgTableEntry_Object = MibTableRow
agAccessUserNewCfgTableEntry = _AgAccessUserNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3, 1)
)
agAccessUserNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agAccessUserNewCfgUId"),
)
if mibBuilder.loadTexts:
    agAccessUserNewCfgTableEntry.setStatus("current")
_AgAccessUserNewCfgUId_Type = Integer32
_AgAccessUserNewCfgUId_Object = MibTableColumn
agAccessUserNewCfgUId = _AgAccessUserNewCfgUId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3, 1, 1),
    _AgAccessUserNewCfgUId_Type()
)
agAccessUserNewCfgUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAccessUserNewCfgUId.setStatus("current")


class _AgAccessUserNewCos_Type(Integer32):
    """Custom type agAccessUserNewCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("admin", 6),
          ("oper", 3),
          ("user", 0))
    )


_AgAccessUserNewCos_Type.__name__ = "Integer32"
_AgAccessUserNewCos_Object = MibTableColumn
agAccessUserNewCos = _AgAccessUserNewCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3, 1, 2),
    _AgAccessUserNewCos_Type()
)
agAccessUserNewCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agAccessUserNewCos.setStatus("current")


class _AgAccessUserNewCfgName_Type(DisplayString):
    """Custom type agAccessUserNewCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AgAccessUserNewCfgName_Type.__name__ = "DisplayString"
_AgAccessUserNewCfgName_Object = MibTableColumn
agAccessUserNewCfgName = _AgAccessUserNewCfgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3, 1, 3),
    _AgAccessUserNewCfgName_Type()
)
agAccessUserNewCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agAccessUserNewCfgName.setStatus("current")


class _AgAccessUserNewCfgPswd_Type(DisplayString):
    """Custom type agAccessUserNewCfgPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgAccessUserNewCfgPswd_Type.__name__ = "DisplayString"
_AgAccessUserNewCfgPswd_Object = MibTableColumn
agAccessUserNewCfgPswd = _AgAccessUserNewCfgPswd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3, 1, 4),
    _AgAccessUserNewCfgPswd_Type()
)
agAccessUserNewCfgPswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agAccessUserNewCfgPswd.setStatus("current")


class _AgAccessUserNewCfgState_Type(Integer32):
    """Custom type agAccessUserNewCfgState based on Integer32"""
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


_AgAccessUserNewCfgState_Type.__name__ = "Integer32"
_AgAccessUserNewCfgState_Object = MibTableColumn
agAccessUserNewCfgState = _AgAccessUserNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3, 1, 5),
    _AgAccessUserNewCfgState_Type()
)
agAccessUserNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agAccessUserNewCfgState.setStatus("current")


class _AgAccessUserNewCfgDelete_Type(Integer32):
    """Custom type agAccessUserNewCfgDelete based on Integer32"""
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


_AgAccessUserNewCfgDelete_Type.__name__ = "Integer32"
_AgAccessUserNewCfgDelete_Object = MibTableColumn
agAccessUserNewCfgDelete = _AgAccessUserNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 1, 12, 3, 1, 6),
    _AgAccessUserNewCfgDelete_Type()
)
agAccessUserNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agAccessUserNewCfgDelete.setStatus("current")
_AgentStats_ObjectIdentity = ObjectIdentity
agentStats = _AgentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2)
)
_PktStats_ObjectIdentity = ObjectIdentity
pktStats = _PktStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1)
)
_PktStatsAllocs_Type = Counter32
_PktStatsAllocs_Object = MibScalar
pktStatsAllocs = _PktStatsAllocs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 1),
    _PktStatsAllocs_Type()
)
pktStatsAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsAllocs.setStatus("current")
_PktStatsFrees_Type = Counter32
_PktStatsFrees_Object = MibScalar
pktStatsFrees = _PktStatsFrees_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 2),
    _PktStatsFrees_Type()
)
pktStatsFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsFrees.setStatus("current")
_PktStatsAllocFails_Type = Counter32
_PktStatsAllocFails_Object = MibScalar
pktStatsAllocFails = _PktStatsAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 3),
    _PktStatsAllocFails_Type()
)
pktStatsAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsAllocFails.setStatus("current")
_PktStatsMediums_Type = Gauge32
_PktStatsMediums_Object = MibScalar
pktStatsMediums = _PktStatsMediums_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 4),
    _PktStatsMediums_Type()
)
pktStatsMediums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsMediums.setStatus("current")
_PktStatsJumbos_Type = Gauge32
_PktStatsJumbos_Object = MibScalar
pktStatsJumbos = _PktStatsJumbos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 5),
    _PktStatsJumbos_Type()
)
pktStatsJumbos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsJumbos.setStatus("current")
_PktStatsSmalls_Type = Gauge32
_PktStatsSmalls_Object = MibScalar
pktStatsSmalls = _PktStatsSmalls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 6),
    _PktStatsSmalls_Type()
)
pktStatsSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsSmalls.setStatus("current")
_PktStatsMediumsHiWatermark_Type = Counter32
_PktStatsMediumsHiWatermark_Object = MibScalar
pktStatsMediumsHiWatermark = _PktStatsMediumsHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 7),
    _PktStatsMediumsHiWatermark_Type()
)
pktStatsMediumsHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsMediumsHiWatermark.setStatus("current")
_PktStatsJumbosHiWatermark_Type = Counter32
_PktStatsJumbosHiWatermark_Object = MibScalar
pktStatsJumbosHiWatermark = _PktStatsJumbosHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 8),
    _PktStatsJumbosHiWatermark_Type()
)
pktStatsJumbosHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsJumbosHiWatermark.setStatus("current")
_PktStatsSmallsHiWatermark_Type = Counter32
_PktStatsSmallsHiWatermark_Object = MibScalar
pktStatsSmallsHiWatermark = _PktStatsSmallsHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 1, 9),
    _PktStatsSmallsHiWatermark_Type()
)
pktStatsSmallsHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsSmallsHiWatermark.setStatus("current")
_MpCpuStats_ObjectIdentity = ObjectIdentity
mpCpuStats = _MpCpuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 2)
)
_MpCpuStatsUtil1Second_Type = Integer32
_MpCpuStatsUtil1Second_Object = MibScalar
mpCpuStatsUtil1Second = _MpCpuStatsUtil1Second_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 2, 1),
    _MpCpuStatsUtil1Second_Type()
)
mpCpuStatsUtil1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuStatsUtil1Second.setStatus("current")
_MpCpuStatsUtil4Seconds_Type = Integer32
_MpCpuStatsUtil4Seconds_Object = MibScalar
mpCpuStatsUtil4Seconds = _MpCpuStatsUtil4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 2, 2),
    _MpCpuStatsUtil4Seconds_Type()
)
mpCpuStatsUtil4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuStatsUtil4Seconds.setStatus("current")
_MpCpuStatsUtil64Seconds_Type = Integer32
_MpCpuStatsUtil64Seconds_Object = MibScalar
mpCpuStatsUtil64Seconds = _MpCpuStatsUtil64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 2, 3),
    _MpCpuStatsUtil64Seconds_Type()
)
mpCpuStatsUtil64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuStatsUtil64Seconds.setStatus("current")
_PortStats_ObjectIdentity = ObjectIdentity
portStats = _PortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3)
)
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("current")
_PortStatsTableEntry_Object = MibTableRow
portStatsTableEntry = _PortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1)
)
portStatsTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "portStatsIndx"),
)
if mibBuilder.loadTexts:
    portStatsTableEntry.setStatus("current")
_PortStatsIndx_Type = Integer32
_PortStatsIndx_Object = MibTableColumn
portStatsIndx = _PortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 1),
    _PortStatsIndx_Type()
)
portStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsIndx.setStatus("current")
_PortStatsPhyIfInOctets_Type = Counter32
_PortStatsPhyIfInOctets_Object = MibTableColumn
portStatsPhyIfInOctets = _PortStatsPhyIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 2),
    _PortStatsPhyIfInOctets_Type()
)
portStatsPhyIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInOctets.setStatus("current")
_PortStatsPhyIfInUcastPkts_Type = Counter32
_PortStatsPhyIfInUcastPkts_Object = MibTableColumn
portStatsPhyIfInUcastPkts = _PortStatsPhyIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 3),
    _PortStatsPhyIfInUcastPkts_Type()
)
portStatsPhyIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInUcastPkts.setStatus("current")
_PortStatsPhyIfInNUcastPkts_Type = Counter32
_PortStatsPhyIfInNUcastPkts_Object = MibTableColumn
portStatsPhyIfInNUcastPkts = _PortStatsPhyIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 4),
    _PortStatsPhyIfInNUcastPkts_Type()
)
portStatsPhyIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInNUcastPkts.setStatus("current")
_PortStatsPhyIfInDiscards_Type = Counter32
_PortStatsPhyIfInDiscards_Object = MibTableColumn
portStatsPhyIfInDiscards = _PortStatsPhyIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 5),
    _PortStatsPhyIfInDiscards_Type()
)
portStatsPhyIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInDiscards.setStatus("current")
_PortStatsPhyIfInErrors_Type = Counter32
_PortStatsPhyIfInErrors_Object = MibTableColumn
portStatsPhyIfInErrors = _PortStatsPhyIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 6),
    _PortStatsPhyIfInErrors_Type()
)
portStatsPhyIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInErrors.setStatus("current")
_PortStatsPhyIfInUnknownProtos_Type = Counter32
_PortStatsPhyIfInUnknownProtos_Object = MibTableColumn
portStatsPhyIfInUnknownProtos = _PortStatsPhyIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 7),
    _PortStatsPhyIfInUnknownProtos_Type()
)
portStatsPhyIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInUnknownProtos.setStatus("current")
_PortStatsPhyIfOutOctets_Type = Counter32
_PortStatsPhyIfOutOctets_Object = MibTableColumn
portStatsPhyIfOutOctets = _PortStatsPhyIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 8),
    _PortStatsPhyIfOutOctets_Type()
)
portStatsPhyIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutOctets.setStatus("current")
_PortStatsPhyIfOutUcastPkts_Type = Counter32
_PortStatsPhyIfOutUcastPkts_Object = MibTableColumn
portStatsPhyIfOutUcastPkts = _PortStatsPhyIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 9),
    _PortStatsPhyIfOutUcastPkts_Type()
)
portStatsPhyIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutUcastPkts.setStatus("current")
_PortStatsPhyIfOutNUcastPkts_Type = Counter32
_PortStatsPhyIfOutNUcastPkts_Object = MibTableColumn
portStatsPhyIfOutNUcastPkts = _PortStatsPhyIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 10),
    _PortStatsPhyIfOutNUcastPkts_Type()
)
portStatsPhyIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutNUcastPkts.setStatus("current")
_PortStatsPhyIfOutDiscards_Type = Counter32
_PortStatsPhyIfOutDiscards_Object = MibTableColumn
portStatsPhyIfOutDiscards = _PortStatsPhyIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 11),
    _PortStatsPhyIfOutDiscards_Type()
)
portStatsPhyIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutDiscards.setStatus("current")
_PortStatsPhyIfOutErrors_Type = Counter32
_PortStatsPhyIfOutErrors_Object = MibTableColumn
portStatsPhyIfOutErrors = _PortStatsPhyIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 12),
    _PortStatsPhyIfOutErrors_Type()
)
portStatsPhyIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutErrors.setStatus("current")
_PortStatsPhyIfOutQLen_Type = Gauge32
_PortStatsPhyIfOutQLen_Object = MibTableColumn
portStatsPhyIfOutQLen = _PortStatsPhyIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 13),
    _PortStatsPhyIfOutQLen_Type()
)
portStatsPhyIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutQLen.setStatus("current")
_PortStatsPhyIfInBroadcastPkts_Type = Counter32
_PortStatsPhyIfInBroadcastPkts_Object = MibTableColumn
portStatsPhyIfInBroadcastPkts = _PortStatsPhyIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 14),
    _PortStatsPhyIfInBroadcastPkts_Type()
)
portStatsPhyIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInBroadcastPkts.setStatus("current")
_PortStatsPhyIfOutBroadcastPkts_Type = Counter32
_PortStatsPhyIfOutBroadcastPkts_Object = MibTableColumn
portStatsPhyIfOutBroadcastPkts = _PortStatsPhyIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 15),
    _PortStatsPhyIfOutBroadcastPkts_Type()
)
portStatsPhyIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutBroadcastPkts.setStatus("current")


class _PortStatsClear_Type(Integer32):
    """Custom type portStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_PortStatsClear_Type.__name__ = "Integer32"
_PortStatsClear_Object = MibTableColumn
portStatsClear = _PortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 16),
    _PortStatsClear_Type()
)
portStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStatsClear.setStatus("current")
_PortStatsPhyIfInMulticastPkts_Type = Counter32
_PortStatsPhyIfInMulticastPkts_Object = MibTableColumn
portStatsPhyIfInMulticastPkts = _PortStatsPhyIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 17),
    _PortStatsPhyIfInMulticastPkts_Type()
)
portStatsPhyIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInMulticastPkts.setStatus("current")
_PortStatsPhyIfOutMulticastPkts_Type = Counter32
_PortStatsPhyIfOutMulticastPkts_Object = MibTableColumn
portStatsPhyIfOutMulticastPkts = _PortStatsPhyIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 1, 1, 18),
    _PortStatsPhyIfOutMulticastPkts_Type()
)
portStatsPhyIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutMulticastPkts.setStatus("current")
_Dot1xPortStatsTable_Object = MibTable
dot1xPortStatsTable = _Dot1xPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dot1xPortStatsTable.setStatus("current")
_Dot1xPortStatsTableEntry_Object = MibTableRow
dot1xPortStatsTableEntry = _Dot1xPortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1)
)
dot1xPortStatsTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "dot1xPortStatsIndx"),
)
if mibBuilder.loadTexts:
    dot1xPortStatsTableEntry.setStatus("current")
_Dot1xPortStatsIndx_Type = Integer32
_Dot1xPortStatsIndx_Object = MibTableColumn
dot1xPortStatsIndx = _Dot1xPortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 1),
    _Dot1xPortStatsIndx_Type()
)
dot1xPortStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xPortStatsIndx.setStatus("current")
_EapolFramesRx_Type = Integer32
_EapolFramesRx_Object = MibTableColumn
eapolFramesRx = _EapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 2),
    _EapolFramesRx_Type()
)
eapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolFramesRx.setStatus("current")
_EapolFramesTx_Type = Integer32
_EapolFramesTx_Object = MibTableColumn
eapolFramesTx = _EapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 3),
    _EapolFramesTx_Type()
)
eapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolFramesTx.setStatus("current")
_EapolStartFramesRx_Type = Integer32
_EapolStartFramesRx_Object = MibTableColumn
eapolStartFramesRx = _EapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 4),
    _EapolStartFramesRx_Type()
)
eapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolStartFramesRx.setStatus("current")
_EapolLogoffFramesRx_Type = Integer32
_EapolLogoffFramesRx_Object = MibTableColumn
eapolLogoffFramesRx = _EapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 5),
    _EapolLogoffFramesRx_Type()
)
eapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolLogoffFramesRx.setStatus("current")
_EapolRespIdFramesRx_Type = Integer32
_EapolRespIdFramesRx_Object = MibTableColumn
eapolRespIdFramesRx = _EapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 6),
    _EapolRespIdFramesRx_Type()
)
eapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolRespIdFramesRx.setStatus("current")
_EapolRespFramesRx_Type = Integer32
_EapolRespFramesRx_Object = MibTableColumn
eapolRespFramesRx = _EapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 7),
    _EapolRespFramesRx_Type()
)
eapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolRespFramesRx.setStatus("current")
_EapolReqIdFramesTx_Type = Integer32
_EapolReqIdFramesTx_Object = MibTableColumn
eapolReqIdFramesTx = _EapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 8),
    _EapolReqIdFramesTx_Type()
)
eapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolReqIdFramesTx.setStatus("current")
_EapolReqFramesTx_Type = Integer32
_EapolReqFramesTx_Object = MibTableColumn
eapolReqFramesTx = _EapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 9),
    _EapolReqFramesTx_Type()
)
eapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapolReqFramesTx.setStatus("current")
_InvalidEapolFramesRx_Type = Integer32
_InvalidEapolFramesRx_Object = MibTableColumn
invalidEapolFramesRx = _InvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 10),
    _InvalidEapolFramesRx_Type()
)
invalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invalidEapolFramesRx.setStatus("current")
_EapLengthErrorFramesRx_Type = Integer32
_EapLengthErrorFramesRx_Object = MibTableColumn
eapLengthErrorFramesRx = _EapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 11),
    _EapLengthErrorFramesRx_Type()
)
eapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapLengthErrorFramesRx.setStatus("current")
_AuthEntersConnecting_Type = Integer32
_AuthEntersConnecting_Object = MibTableColumn
authEntersConnecting = _AuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 12),
    _AuthEntersConnecting_Type()
)
authEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authEntersConnecting.setStatus("current")
_AuthEapLogoffsWhileConnecting_Type = Integer32
_AuthEapLogoffsWhileConnecting_Object = MibTableColumn
authEapLogoffsWhileConnecting = _AuthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 13),
    _AuthEapLogoffsWhileConnecting_Type()
)
authEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authEapLogoffsWhileConnecting.setStatus("current")
_AuthEntersAuthenticating_Type = Integer32
_AuthEntersAuthenticating_Object = MibTableColumn
authEntersAuthenticating = _AuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 14),
    _AuthEntersAuthenticating_Type()
)
authEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authEntersAuthenticating.setStatus("current")
_AuthSuccessesWhileAuthenticating_Type = Integer32
_AuthSuccessesWhileAuthenticating_Object = MibTableColumn
authSuccessesWhileAuthenticating = _AuthSuccessesWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 15),
    _AuthSuccessesWhileAuthenticating_Type()
)
authSuccessesWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSuccessesWhileAuthenticating.setStatus("current")
_AuthTimeoutsWhileAuthenticating_Type = Integer32
_AuthTimeoutsWhileAuthenticating_Object = MibTableColumn
authTimeoutsWhileAuthenticating = _AuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 16),
    _AuthTimeoutsWhileAuthenticating_Type()
)
authTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authTimeoutsWhileAuthenticating.setStatus("current")
_AuthFailWhileAuthenticating_Type = Integer32
_AuthFailWhileAuthenticating_Object = MibTableColumn
authFailWhileAuthenticating = _AuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 17),
    _AuthFailWhileAuthenticating_Type()
)
authFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authFailWhileAuthenticating.setStatus("current")
_AuthReauthsWhileAuthenticating_Type = Integer32
_AuthReauthsWhileAuthenticating_Object = MibTableColumn
authReauthsWhileAuthenticating = _AuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 18),
    _AuthReauthsWhileAuthenticating_Type()
)
authReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authReauthsWhileAuthenticating.setStatus("current")
_AuthEapStartsWhileAuthenticating_Type = Integer32
_AuthEapStartsWhileAuthenticating_Object = MibTableColumn
authEapStartsWhileAuthenticating = _AuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 19),
    _AuthEapStartsWhileAuthenticating_Type()
)
authEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authEapStartsWhileAuthenticating.setStatus("current")
_AuthEapLogoffWhileAuthenticating_Type = Integer32
_AuthEapLogoffWhileAuthenticating_Object = MibTableColumn
authEapLogoffWhileAuthenticating = _AuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 20),
    _AuthEapLogoffWhileAuthenticating_Type()
)
authEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authEapLogoffWhileAuthenticating.setStatus("current")
_AuthReauthsWhileAuthenticated_Type = Integer32
_AuthReauthsWhileAuthenticated_Object = MibTableColumn
authReauthsWhileAuthenticated = _AuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 21),
    _AuthReauthsWhileAuthenticated_Type()
)
authReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authReauthsWhileAuthenticated.setStatus("current")
_AuthEapStartsWhileAuthenticated_Type = Integer32
_AuthEapStartsWhileAuthenticated_Object = MibTableColumn
authEapStartsWhileAuthenticated = _AuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 22),
    _AuthEapStartsWhileAuthenticated_Type()
)
authEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authEapStartsWhileAuthenticated.setStatus("current")
_AuthEapLogoffWhileAuthenticated_Type = Integer32
_AuthEapLogoffWhileAuthenticated_Object = MibTableColumn
authEapLogoffWhileAuthenticated = _AuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 23),
    _AuthEapLogoffWhileAuthenticated_Type()
)
authEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authEapLogoffWhileAuthenticated.setStatus("current")
_BackendResponses_Type = Integer32
_BackendResponses_Object = MibTableColumn
backendResponses = _BackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 24),
    _BackendResponses_Type()
)
backendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backendResponses.setStatus("current")
_BackendAccessChallenges_Type = Integer32
_BackendAccessChallenges_Object = MibTableColumn
backendAccessChallenges = _BackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 25),
    _BackendAccessChallenges_Type()
)
backendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backendAccessChallenges.setStatus("current")
_BackendOtherRequestsToSupplicant_Type = Integer32
_BackendOtherRequestsToSupplicant_Object = MibTableColumn
backendOtherRequestsToSupplicant = _BackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 26),
    _BackendOtherRequestsToSupplicant_Type()
)
backendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backendOtherRequestsToSupplicant.setStatus("current")
_BackendNonNakResponsesFromSupplicant_Type = Integer32
_BackendNonNakResponsesFromSupplicant_Object = MibTableColumn
backendNonNakResponsesFromSupplicant = _BackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 27),
    _BackendNonNakResponsesFromSupplicant_Type()
)
backendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backendNonNakResponsesFromSupplicant.setStatus("current")
_BackendAuthSuccesses_Type = Integer32
_BackendAuthSuccesses_Object = MibTableColumn
backendAuthSuccesses = _BackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 28),
    _BackendAuthSuccesses_Type()
)
backendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backendAuthSuccesses.setStatus("current")
_BackendAuthFails_Type = Integer32
_BackendAuthFails_Object = MibTableColumn
backendAuthFails = _BackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 29),
    _BackendAuthFails_Type()
)
backendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backendAuthFails.setStatus("current")
_LastEapolFrameVersion_Type = Integer32
_LastEapolFrameVersion_Object = MibTableColumn
lastEapolFrameVersion = _LastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 30),
    _LastEapolFrameVersion_Type()
)
lastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastEapolFrameVersion.setStatus("current")
_LastEapolFrameSource_Type = MacAddress
_LastEapolFrameSource_Object = MibTableColumn
lastEapolFrameSource = _LastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 3, 2, 1, 31),
    _LastEapolFrameSource_Type()
)
lastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastEapolFrameSource.setStatus("current")
_SpStats_ObjectIdentity = ObjectIdentity
spStats = _SpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 4)
)
_MgmtStats_ObjectIdentity = ObjectIdentity
mgmtStats = _MgmtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 5)
)
_NtpStats_ObjectIdentity = ObjectIdentity
ntpStats = _NtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9)
)
_NtpPrimaryServerReqSent_Type = Integer32
_NtpPrimaryServerReqSent_Object = MibScalar
ntpPrimaryServerReqSent = _NtpPrimaryServerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 1),
    _NtpPrimaryServerReqSent_Type()
)
ntpPrimaryServerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPrimaryServerReqSent.setStatus("current")
_NtpPrimaryServerRespRcvd_Type = Integer32
_NtpPrimaryServerRespRcvd_Object = MibScalar
ntpPrimaryServerRespRcvd = _NtpPrimaryServerRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 2),
    _NtpPrimaryServerRespRcvd_Type()
)
ntpPrimaryServerRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPrimaryServerRespRcvd.setStatus("current")
_NtpPrimaryServerUpdates_Type = Integer32
_NtpPrimaryServerUpdates_Object = MibScalar
ntpPrimaryServerUpdates = _NtpPrimaryServerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 3),
    _NtpPrimaryServerUpdates_Type()
)
ntpPrimaryServerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPrimaryServerUpdates.setStatus("current")
_NtpSecondaryServerReqSent_Type = Integer32
_NtpSecondaryServerReqSent_Object = MibScalar
ntpSecondaryServerReqSent = _NtpSecondaryServerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 4),
    _NtpSecondaryServerReqSent_Type()
)
ntpSecondaryServerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSecondaryServerReqSent.setStatus("current")
_NtpSecondaryServerRespRcvd_Type = Integer32
_NtpSecondaryServerRespRcvd_Object = MibScalar
ntpSecondaryServerRespRcvd = _NtpSecondaryServerRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 5),
    _NtpSecondaryServerRespRcvd_Type()
)
ntpSecondaryServerRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSecondaryServerRespRcvd.setStatus("current")
_NtpSecondaryServerUpdates_Type = Integer32
_NtpSecondaryServerUpdates_Object = MibScalar
ntpSecondaryServerUpdates = _NtpSecondaryServerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 6),
    _NtpSecondaryServerUpdates_Type()
)
ntpSecondaryServerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSecondaryServerUpdates.setStatus("current")


class _NtpLastUpdateServer_Type(Integer32):
    """Custom type ntpLastUpdateServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_NtpLastUpdateServer_Type.__name__ = "Integer32"
_NtpLastUpdateServer_Object = MibScalar
ntpLastUpdateServer = _NtpLastUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 7),
    _NtpLastUpdateServer_Type()
)
ntpLastUpdateServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLastUpdateServer.setStatus("current")


class _NtpLastUpdateTime_Type(DisplayString):
    """Custom type ntpLastUpdateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NtpLastUpdateTime_Type.__name__ = "DisplayString"
_NtpLastUpdateTime_Object = MibScalar
ntpLastUpdateTime = _NtpLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 8),
    _NtpLastUpdateTime_Type()
)
ntpLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLastUpdateTime.setStatus("current")


class _NtpClearStats_Type(Integer32):
    """Custom type ntpClearStats based on Integer32"""
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


_NtpClearStats_Type.__name__ = "Integer32"
_NtpClearStats_Object = MibScalar
ntpClearStats = _NtpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 9),
    _NtpClearStats_Type()
)
ntpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClearStats.setStatus("current")


class _NtpSystemCurrentTime_Type(DisplayString):
    """Custom type ntpSystemCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NtpSystemCurrentTime_Type.__name__ = "DisplayString"
_NtpSystemCurrentTime_Object = MibScalar
ntpSystemCurrentTime = _NtpSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 9, 10),
    _NtpSystemCurrentTime_Type()
)
ntpSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSystemCurrentTime.setStatus("current")
_AclPortStats_ObjectIdentity = ObjectIdentity
aclPortStats = _AclPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 10)
)
_AclPortStatsTable_Object = MibTable
aclPortStatsTable = _AclPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    aclPortStatsTable.setStatus("current")
_AclPortStatsTableEntry_Object = MibTableRow
aclPortStatsTableEntry = _AclPortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 10, 1, 1)
)
aclPortStatsTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "aclPortStatsIndx"),
)
if mibBuilder.loadTexts:
    aclPortStatsTableEntry.setStatus("current")
_AclPortStatsIndx_Type = Integer32
_AclPortStatsIndx_Object = MibTableColumn
aclPortStatsIndx = _AclPortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 10, 1, 1, 1),
    _AclPortStatsIndx_Type()
)
aclPortStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPortStatsIndx.setStatus("current")
_AclPortStatsHits_Type = Counter32
_AclPortStatsHits_Object = MibTableColumn
aclPortStatsHits = _AclPortStatsHits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 10, 1, 1, 2),
    _AclPortStatsHits_Type()
)
aclPortStatsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPortStatsHits.setStatus("current")


class _AclPortClearStats_Type(Integer32):
    """Custom type aclPortClearStats based on Integer32"""
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


_AclPortClearStats_Type.__name__ = "Integer32"
_AclPortClearStats_Object = MibTableColumn
aclPortClearStats = _AclPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 10, 1, 1, 3),
    _AclPortClearStats_Type()
)
aclPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortClearStats.setStatus("current")
_AclMeterPortStats_ObjectIdentity = ObjectIdentity
aclMeterPortStats = _AclMeterPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 11)
)
_AclMeterPortStatsTable_Object = MibTable
aclMeterPortStatsTable = _AclMeterPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    aclMeterPortStatsTable.setStatus("current")
_AclMeterPortStatsTableEntry_Object = MibTableRow
aclMeterPortStatsTableEntry = _AclMeterPortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 11, 1, 1)
)
aclMeterPortStatsTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "aclMeterPortStatsIndx"),
)
if mibBuilder.loadTexts:
    aclMeterPortStatsTableEntry.setStatus("current")
_AclMeterPortStatsIndx_Type = Integer32
_AclMeterPortStatsIndx_Object = MibTableColumn
aclMeterPortStatsIndx = _AclMeterPortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 11, 1, 1, 1),
    _AclMeterPortStatsIndx_Type()
)
aclMeterPortStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMeterPortStatsIndx.setStatus("current")
_AclMeterPortStatsHits_Type = Counter32
_AclMeterPortStatsHits_Object = MibTableColumn
aclMeterPortStatsHits = _AclMeterPortStatsHits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 11, 1, 1, 2),
    _AclMeterPortStatsHits_Type()
)
aclMeterPortStatsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMeterPortStatsHits.setStatus("current")


class _AclMeterPortClearStats_Type(Integer32):
    """Custom type aclMeterPortClearStats based on Integer32"""
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


_AclMeterPortClearStats_Type.__name__ = "Integer32"
_AclMeterPortClearStats_Object = MibTableColumn
aclMeterPortClearStats = _AclMeterPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 2, 11, 1, 1, 3),
    _AclMeterPortClearStats_Type()
)
aclMeterPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMeterPortClearStats.setStatus("current")
_AgentInfo_ObjectIdentity = ObjectIdentity
agentInfo = _AgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 1)
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 1, 1),
    _HwPartNumber_Type()
)
hwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPartNumber.setStatus("current")


class _HwRevision_Type(DisplayString):
    """Custom type hwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRevision_Type.__name__ = "DisplayString"
_HwRevision_Object = MibScalar
hwRevision = _HwRevision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 1, 2),
    _HwRevision_Type()
)
hwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRevision.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 1, 3),
    _HwPowerSupplyStatus_Type()
)
hwPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPowerSupplyStatus.setStatus("current")
_HwSensor1Temp_Type = Integer32
_HwSensor1Temp_Object = MibScalar
hwSensor1Temp = _HwSensor1Temp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 1, 4),
    _HwSensor1Temp_Type()
)
hwSensor1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensor1Temp.setStatus("current")


class _HwInsertedCubeType_Type(Integer32):
    """Custom type hwInsertedCubeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copperCube", 2),
          ("fiberCube", 1),
          ("none", 3))
    )


_HwInsertedCubeType_Type.__name__ = "Integer32"
_HwInsertedCubeType_Object = MibScalar
hwInsertedCubeType = _HwInsertedCubeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 1, 5),
    _HwInsertedCubeType_Type()
)
hwInsertedCubeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInsertedCubeType.setStatus("current")
_PortInfo_ObjectIdentity = ObjectIdentity
portInfo = _PortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2)
)
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("current")
_PortInfoTableEntry_Object = MibTableRow
portInfoTableEntry = _PortInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1)
)
portInfoTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "portInfoIndx"),
)
if mibBuilder.loadTexts:
    portInfoTableEntry.setStatus("current")
_PortInfoIndx_Type = Integer32
_PortInfoIndx_Object = MibTableColumn
portInfoIndx = _PortInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 1),
    _PortInfoIndx_Type()
)
portInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoIndx.setStatus("current")


class _PortInfoSpeed_Type(Integer32):
    """Custom type portInfoSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("any", 5),
          ("mbs10", 2),
          ("mbs100", 3),
          ("mbs1000", 4))
    )


_PortInfoSpeed_Type.__name__ = "Integer32"
_PortInfoSpeed_Object = MibTableColumn
portInfoSpeed = _PortInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 2),
    _PortInfoSpeed_Type()
)
portInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSpeed.setStatus("current")


class _PortInfoMode_Type(Integer32):
    """Custom type portInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 3))
    )


_PortInfoMode_Type.__name__ = "Integer32"
_PortInfoMode_Object = MibTableColumn
portInfoMode = _PortInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 3),
    _PortInfoMode_Type()
)
portInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoMode.setStatus("current")


class _PortInfoFlowCtrl_Type(Integer32):
    """Custom type portInfoFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("none", 5),
          ("receive", 3),
          ("transmit", 2))
    )


_PortInfoFlowCtrl_Type.__name__ = "Integer32"
_PortInfoFlowCtrl_Object = MibTableColumn
portInfoFlowCtrl = _PortInfoFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 4),
    _PortInfoFlowCtrl_Type()
)
portInfoFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoFlowCtrl.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 5),
    _PortInfoLink_Type()
)
portInfoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoLink.setStatus("current")


class _PortInfoPhyIfDescr_Type(DisplayString):
    """Custom type portInfoPhyIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortInfoPhyIfDescr_Type.__name__ = "DisplayString"
_PortInfoPhyIfDescr_Object = MibTableColumn
portInfoPhyIfDescr = _PortInfoPhyIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 6),
    _PortInfoPhyIfDescr_Type()
)
portInfoPhyIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfDescr.setStatus("current")


class _PortInfoPhyIfType_Type(Integer32):
    """Custom type portInfoPhyIfType based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("basicISDN", 20),
          ("ddn-x25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("frame-relay", 32),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("nsip", 27),
          ("other", 1),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("softwareLoopback", 24),
          ("starLan", 11),
          ("ultra", 29))
    )


_PortInfoPhyIfType_Type.__name__ = "Integer32"
_PortInfoPhyIfType_Object = MibTableColumn
portInfoPhyIfType = _PortInfoPhyIfType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 7),
    _PortInfoPhyIfType_Type()
)
portInfoPhyIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfType.setStatus("current")
_PortInfoPhyIfMtu_Type = Integer32
_PortInfoPhyIfMtu_Object = MibTableColumn
portInfoPhyIfMtu = _PortInfoPhyIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 8),
    _PortInfoPhyIfMtu_Type()
)
portInfoPhyIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfMtu.setStatus("current")
_PortInfoPhyIfPhysAddress_Type = PhysAddress
_PortInfoPhyIfPhysAddress_Object = MibTableColumn
portInfoPhyIfPhysAddress = _PortInfoPhyIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 9),
    _PortInfoPhyIfPhysAddress_Type()
)
portInfoPhyIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfPhysAddress.setStatus("current")


class _PortInfoPhyIfOperStatus_Type(Integer32):
    """Custom type portInfoPhyIfOperStatus based on Integer32"""
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


_PortInfoPhyIfOperStatus_Type.__name__ = "Integer32"
_PortInfoPhyIfOperStatus_Object = MibTableColumn
portInfoPhyIfOperStatus = _PortInfoPhyIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 10),
    _PortInfoPhyIfOperStatus_Type()
)
portInfoPhyIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfOperStatus.setStatus("current")
_PortInfoPhyIfLastChange_Type = TimeTicks
_PortInfoPhyIfLastChange_Object = MibTableColumn
portInfoPhyIfLastChange = _PortInfoPhyIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 2, 1, 1, 11),
    _PortInfoPhyIfLastChange_Type()
)
portInfoPhyIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfLastChange.setStatus("current")
_SwKeyInfo_ObjectIdentity = ObjectIdentity
swKeyInfo = _SwKeyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 3)
)
_AgDiff_ObjectIdentity = ObjectIdentity
agDiff = _AgDiff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 4)
)


class _AgDiffState_Type(Integer32):
    """Custom type agDiffState based on Integer32"""
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
        *(("complete", 5),
          ("diff", 1),
          ("flashdiff", 2),
          ("idle", 3),
          ("inprogress", 4))
    )


_AgDiffState_Type.__name__ = "Integer32"
_AgDiffState_Object = MibScalar
agDiffState = _AgDiffState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 4, 2),
    _AgDiffState_Type()
)
agDiffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agDiffState.setStatus("current")
_AgDiffTableSize_Type = Integer32
_AgDiffTableSize_Object = MibScalar
agDiffTableSize = _AgDiffTableSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 4, 3),
    _AgDiffTableSize_Type()
)
agDiffTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDiffTableSize.setStatus("current")
_AgDiffTable_Object = MibTable
agDiffTable = _AgDiffTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    agDiffTable.setStatus("current")
_AgDiffTableEntry_Object = MibTableRow
agDiffTableEntry = _AgDiffTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 4, 4, 1)
)
agDiffTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agDiffIndex"),
)
if mibBuilder.loadTexts:
    agDiffTableEntry.setStatus("current")
_AgDiffIndex_Type = Integer32
_AgDiffIndex_Object = MibTableColumn
agDiffIndex = _AgDiffIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 4, 4, 1, 1),
    _AgDiffIndex_Type()
)
agDiffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDiffIndex.setStatus("current")
_AgDiffString_Type = OctetString
_AgDiffString_Object = MibTableColumn
agDiffString = _AgDiffString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 4, 4, 1, 2),
    _AgDiffString_Type()
)
agDiffString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDiffString.setStatus("current")
_AgCfgDump_ObjectIdentity = ObjectIdentity
agCfgDump = _AgCfgDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 5)
)


class _AgCfgDumpState_Type(Integer32):
    """Custom type agCfgDumpState based on Integer32"""
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
        *(("complete", 4),
          ("dump", 1),
          ("idle", 2),
          ("inprogress", 3))
    )


_AgCfgDumpState_Type.__name__ = "Integer32"
_AgCfgDumpState_Object = MibScalar
agCfgDumpState = _AgCfgDumpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 5, 2),
    _AgCfgDumpState_Type()
)
agCfgDumpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agCfgDumpState.setStatus("current")
_AgCfgDumpTableSize_Type = Integer32
_AgCfgDumpTableSize_Object = MibScalar
agCfgDumpTableSize = _AgCfgDumpTableSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 5, 3),
    _AgCfgDumpTableSize_Type()
)
agCfgDumpTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgDumpTableSize.setStatus("current")
_AgCfgDumpTable_Object = MibTable
agCfgDumpTable = _AgCfgDumpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    agCfgDumpTable.setStatus("current")
_AgCfgDumpTableEntry_Object = MibTableRow
agCfgDumpTableEntry = _AgCfgDumpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 5, 4, 1)
)
agCfgDumpTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "agCfgDumpIndex"),
)
if mibBuilder.loadTexts:
    agCfgDumpTableEntry.setStatus("current")
_AgCfgDumpIndex_Type = Integer32
_AgCfgDumpIndex_Object = MibTableColumn
agCfgDumpIndex = _AgCfgDumpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 5, 4, 1, 1),
    _AgCfgDumpIndex_Type()
)
agCfgDumpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgDumpIndex.setStatus("current")
_AgCfgDumpString_Type = OctetString
_AgCfgDumpString_Object = MibTableColumn
agCfgDumpString = _AgCfgDumpString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 5, 4, 1, 2),
    _AgCfgDumpString_Type()
)
agCfgDumpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgDumpString.setStatus("current")
_MgmtInfo_ObjectIdentity = ObjectIdentity
mgmtInfo = _MgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 6)
)
_GeaportInfo_ObjectIdentity = ObjectIdentity
geaportInfo = _GeaportInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 7)
)
_GeaportInfoTable_Object = MibTable
geaportInfoTable = _GeaportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    geaportInfoTable.setStatus("current")
_GeaportInfoTableEntry_Object = MibTableRow
geaportInfoTableEntry = _GeaportInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 7, 1, 1)
)
geaportInfoTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "geaportInfoLogicalIndex"),
)
if mibBuilder.loadTexts:
    geaportInfoTableEntry.setStatus("current")
_GeaportInfoLogicalIndex_Type = Integer32
_GeaportInfoLogicalIndex_Object = MibTableColumn
geaportInfoLogicalIndex = _GeaportInfoLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 7, 1, 1, 1),
    _GeaportInfoLogicalIndex_Type()
)
geaportInfoLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaportInfoLogicalIndex.setStatus("current")
_GeaportInfoPort_Type = Integer32
_GeaportInfoPort_Object = MibTableColumn
geaportInfoPort = _GeaportInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 7, 1, 1, 2),
    _GeaportInfoPort_Type()
)
geaportInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaportInfoPort.setStatus("current")
_GeaportInfoUnit_Type = Integer32
_GeaportInfoUnit_Object = MibTableColumn
geaportInfoUnit = _GeaportInfoUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 7, 1, 1, 3),
    _GeaportInfoUnit_Type()
)
geaportInfoUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaportInfoUnit.setStatus("current")
_UfdInfo_ObjectIdentity = ObjectIdentity
ufdInfo = _UfdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8)
)


class _UfdInfoState_Type(Integer32):
    """Custom type ufdInfoState based on Integer32"""
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


_UfdInfoState_Type.__name__ = "Integer32"
_UfdInfoState_Object = MibScalar
ufdInfoState = _UfdInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8, 1),
    _UfdInfoState_Type()
)
ufdInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdInfoState.setStatus("current")


class _UfdInfoLtMStatus_Type(Integer32):
    """Custom type ufdInfoLtMStatus based on Integer32"""
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
        *(("blocked", 4),
          ("down", 2),
          ("forwarding", 3),
          ("up", 1))
    )


_UfdInfoLtMStatus_Type.__name__ = "Integer32"
_UfdInfoLtMStatus_Object = MibScalar
ufdInfoLtMStatus = _UfdInfoLtMStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8, 2),
    _UfdInfoLtMStatus_Type()
)
ufdInfoLtMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdInfoLtMStatus.setStatus("current")
_UfdInfoLtMPorts_Type = OctetString
_UfdInfoLtMPorts_Object = MibScalar
ufdInfoLtMPorts = _UfdInfoLtMPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8, 3),
    _UfdInfoLtMPorts_Type()
)
ufdInfoLtMPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdInfoLtMPorts.setStatus("current")
_UfdInfoLtMTrunks_Type = OctetString
_UfdInfoLtMTrunks_Object = MibScalar
ufdInfoLtMTrunks = _UfdInfoLtMTrunks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8, 4),
    _UfdInfoLtMTrunks_Type()
)
ufdInfoLtMTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdInfoLtMTrunks.setStatus("current")


class _UfdInfoLtDStatus_Type(Integer32):
    """Custom type ufdInfoLtDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoDisabled", 2),
          ("up", 1))
    )


_UfdInfoLtDStatus_Type.__name__ = "Integer32"
_UfdInfoLtDStatus_Object = MibScalar
ufdInfoLtDStatus = _UfdInfoLtDStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8, 5),
    _UfdInfoLtDStatus_Type()
)
ufdInfoLtDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdInfoLtDStatus.setStatus("current")
_UfdInfoLtDPorts_Type = OctetString
_UfdInfoLtDPorts_Object = MibScalar
ufdInfoLtDPorts = _UfdInfoLtDPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8, 6),
    _UfdInfoLtDPorts_Type()
)
ufdInfoLtDPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdInfoLtDPorts.setStatus("current")
_UfdInfoLtDTrunks_Type = Integer32
_UfdInfoLtDTrunks_Object = MibScalar
ufdInfoLtDTrunks = _UfdInfoLtDTrunks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 3, 8, 7),
    _UfdInfoLtDTrunks_Type()
)
ufdInfoLtDTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdInfoLtDTrunks.setStatus("current")
_AgentOper_ObjectIdentity = ObjectIdentity
agentOper = _AgentOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4)
)
_AgPortOperTable_Object = MibTable
agPortOperTable = _AgPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    agPortOperTable.setStatus("current")
_AgPortOperTableEntry_Object = MibTableRow
agPortOperTableEntry = _AgPortOperTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 1)
)
agPortOperTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "portOperIdx"),
)
if mibBuilder.loadTexts:
    agPortOperTableEntry.setStatus("current")
_PortOperIdx_Type = Integer32
_PortOperIdx_Object = MibTableColumn
portOperIdx = _PortOperIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 1, 1),
    _PortOperIdx_Type()
)
portOperIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperIdx.setStatus("current")


class _PortOperState_Type(Integer32):
    """Custom type portOperState based on Integer32"""
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


_PortOperState_Type.__name__ = "Integer32"
_PortOperState_Object = MibTableColumn
portOperState = _PortOperState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 1, 2),
    _PortOperState_Type()
)
portOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOperState.setStatus("current")


class _PortOperRmon_Type(Integer32):
    """Custom type portOperRmon based on Integer32"""
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


_PortOperRmon_Type.__name__ = "Integer32"
_PortOperRmon_Object = MibTableColumn
portOperRmon = _PortOperRmon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 1, 3),
    _PortOperRmon_Type()
)
portOperRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOperRmon.setStatus("current")
_PortOperDot1xTable_Object = MibTable
portOperDot1xTable = _PortOperDot1xTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    portOperDot1xTable.setStatus("current")
_PortOperDot1xTableEntry_Object = MibTableRow
portOperDot1xTableEntry = _PortOperDot1xTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 2, 1)
)
portOperDot1xTableEntry.setIndexNames(
    (0, "BLADETYPE2-SWITCH-MIB", "portOperDot1xIndx"),
)
if mibBuilder.loadTexts:
    portOperDot1xTableEntry.setStatus("current")
_PortOperDot1xIndx_Type = Integer32
_PortOperDot1xIndx_Object = MibTableColumn
portOperDot1xIndx = _PortOperDot1xIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 2, 1, 1),
    _PortOperDot1xIndx_Type()
)
portOperDot1xIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperDot1xIndx.setStatus("current")


class _PortOperDot1xReset_Type(Integer32):
    """Custom type portOperDot1xReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortOperDot1xReset_Type.__name__ = "Integer32"
_PortOperDot1xReset_Object = MibTableColumn
portOperDot1xReset = _PortOperDot1xReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 2, 1, 2),
    _PortOperDot1xReset_Type()
)
portOperDot1xReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOperDot1xReset.setStatus("current")


class _PortOperDot1xReauth_Type(Integer32):
    """Custom type portOperDot1xReauth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortOperDot1xReauth_Type.__name__ = "Integer32"
_PortOperDot1xReauth_Object = MibTableColumn
portOperDot1xReauth = _PortOperDot1xReauth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 1, 2, 1, 3),
    _PortOperDot1xReauth_Type()
)
portOperDot1xReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOperDot1xReauth.setStatus("current")
_AgNTPOper_ObjectIdentity = ObjectIdentity
agNTPOper = _AgNTPOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 2)
)


class _NtpOperSendReq_Type(Integer32):
    """Custom type ntpOperSendReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NtpOperSendReq_Type.__name__ = "Integer32"
_NtpOperSendReq_Object = MibScalar
ntpOperSendReq = _NtpOperSendReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 1, 4, 2, 1),
    _NtpOperSendReq_Type()
)
ntpOperSendReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpOperSendReq.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADETYPE2-SWITCH-MIB",
    **{"agent": agent,
       "agentConfig": agentConfig,
       "agSystem": agSystem,
       "agApplyConfiguration": agApplyConfiguration,
       "agSavePending": agSavePending,
       "agSaveConfiguration": agSaveConfiguration,
       "agRevert": agRevert,
       "agRevertApply": agRevertApply,
       "agReset": agReset,
       "agConfigForNxtReset": agConfigForNxtReset,
       "agImageForNxtReset": agImageForNxtReset,
       "agSoftwareVersion": agSoftwareVersion,
       "agBootVer": agBootVer,
       "agImage1Ver": agImage1Ver,
       "agImage2Ver": agImage2Ver,
       "agRtcDate": agRtcDate,
       "agRtcTime": agRtcTime,
       "agLastSetErrorReason": agLastSetErrorReason,
       "agCurCfgHttpServerPort": agCurCfgHttpServerPort,
       "agNewCfgHttpServerPort": agNewCfgHttpServerPort,
       "agCurCfgLoginBanner": agCurCfgLoginBanner,
       "agNewCfgLoginBanner": agNewCfgLoginBanner,
       "agCurCfgConsole": agCurCfgConsole,
       "agNewCfgConsole": agNewCfgConsole,
       "agCurCfgBootp": agCurCfgBootp,
       "agNewCfgBootp": agNewCfgBootp,
       "agSlotNumber": agSlotNumber,
       "agCurCfgSnmpTimeout": agCurCfgSnmpTimeout,
       "agNewCfgSnmpTimeout": agNewCfgSnmpTimeout,
       "agCurCfgTelnetServerPort": agCurCfgTelnetServerPort,
       "agNewCfgTelnetServerPort": agNewCfgTelnetServerPort,
       "agClearFlashDump": agClearFlashDump,
       "agRackId": agRackId,
       "agChassis": agChassis,
       "agCurCfgTftpServerPort": agCurCfgTftpServerPort,
       "agNewCfgTftpServerPort": agNewCfgTftpServerPort,
       "agCurCfgHttpsServerPort": agCurCfgHttpsServerPort,
       "agNewCfgHttpsServerPort": agNewCfgHttpsServerPort,
       "agCurDaylightSavings": agCurDaylightSavings,
       "agNewDaylightSavings": agNewDaylightSavings,
       "agCurCfgIdleCLITimeout": agCurCfgIdleCLITimeout,
       "agNewCfgIdleCLITimeout": agNewCfgIdleCLITimeout,
       "agCurCfgUfdTrap": agCurCfgUfdTrap,
       "agNewCfgUfdTrap": agNewCfgUfdTrap,
       "agCurBootNxtCliMode": agCurBootNxtCliMode,
       "agNewBootNxtCliMode": agNewBootNxtCliMode,
       "agCurCfgReminders": agCurCfgReminders,
       "agNewCfgReminders": agNewCfgReminders,
       "agPortConfig": agPortConfig,
       "agPortTableMaxEnt": agPortTableMaxEnt,
       "agPortCurCfgTable": agPortCurCfgTable,
       "agPortCurCfgTableEntry": agPortCurCfgTableEntry,
       "agPortCurCfgIndx": agPortCurCfgIndx,
       "agPortCurCfgState": agPortCurCfgState,
       "agPortCurCfgVlanTag": agPortCurCfgVlanTag,
       "agPortCurCfgStp": agPortCurCfgStp,
       "agPortCurCfgRmon": agPortCurCfgRmon,
       "agPortCurCfgPVID": agPortCurCfgPVID,
       "agPortCurCfgGigEthAutoNeg": agPortCurCfgGigEthAutoNeg,
       "agPortCurCfgGigEthSpeed": agPortCurCfgGigEthSpeed,
       "agPortCurCfgGigEthMode": agPortCurCfgGigEthMode,
       "agPortCurCfgGigEthFctl": agPortCurCfgGigEthFctl,
       "agPortCurCfgPortName": agPortCurCfgPortName,
       "agPortCurCfgLinkTrap": agPortCurCfgLinkTrap,
       "agPortCurCfgTagPVID": agPortCurCfgTagPVID,
       "agPortCurCfgMulticastThreshold": agPortCurCfgMulticastThreshold,
       "agPortCurCfgMulticastThresholdRate": agPortCurCfgMulticastThresholdRate,
       "agPortCurCfgBroadcastThreshold": agPortCurCfgBroadcastThreshold,
       "agPortCurCfgBroadcastThresholdRate": agPortCurCfgBroadcastThresholdRate,
       "agPortCurCfgDLFThreshold": agPortCurCfgDLFThreshold,
       "agPortCurCfgDLFThresholdRate": agPortCurCfgDLFThresholdRate,
       "agPortFiberCurCfgTable": agPortFiberCurCfgTable,
       "agPortFiberCurCfgTableEntry": agPortFiberCurCfgTableEntry,
       "agPortFiberCurCfgIndx": agPortFiberCurCfgIndx,
       "agPortFiberCurCfgTxCtrl": agPortFiberCurCfgTxCtrl,
       "agPortFiberCurCfgTxPulse": agPortFiberCurCfgTxPulse,
       "agPortFiberCurCfgTxUp": agPortFiberCurCfgTxUp,
       "agPortFiberCurCfgTxDn": agPortFiberCurCfgTxDn,
       "agPortNewCfgTable": agPortNewCfgTable,
       "agPortNewCfgTableEntry": agPortNewCfgTableEntry,
       "agPortNewCfgIndx": agPortNewCfgIndx,
       "agPortNewCfgState": agPortNewCfgState,
       "agPortNewCfgVlanTag": agPortNewCfgVlanTag,
       "agPortNewCfgStp": agPortNewCfgStp,
       "agPortNewCfgRmon": agPortNewCfgRmon,
       "agPortNewCfgPVID": agPortNewCfgPVID,
       "agPortNewCfgGigEthAutoNeg": agPortNewCfgGigEthAutoNeg,
       "agPortNewCfgGigEthSpeed": agPortNewCfgGigEthSpeed,
       "agPortNewCfgGigEthMode": agPortNewCfgGigEthMode,
       "agPortNewCfgGigEthFctl": agPortNewCfgGigEthFctl,
       "agPortNewCfgPortName": agPortNewCfgPortName,
       "agPortNewCfgLinkTrap": agPortNewCfgLinkTrap,
       "agPortNewCfgTagPVID": agPortNewCfgTagPVID,
       "agPortNewCfgMulticastThreshold": agPortNewCfgMulticastThreshold,
       "agPortNewCfgMulticastThresholdRate": agPortNewCfgMulticastThresholdRate,
       "agPortNewCfgBroadcastThreshold": agPortNewCfgBroadcastThreshold,
       "agPortNewCfgBroadcastThresholdRate": agPortNewCfgBroadcastThresholdRate,
       "agPortNewCfgDLFThreshold": agPortNewCfgDLFThreshold,
       "agPortNewCfgDLFThresholdRate": agPortNewCfgDLFThresholdRate,
       "agPortFiberNewCfgTable": agPortFiberNewCfgTable,
       "agPortFiberNewCfgTableEntry": agPortFiberNewCfgTableEntry,
       "agPortFiberNewCfgIndx": agPortFiberNewCfgIndx,
       "agPortFiberNewCfgTxCtrl": agPortFiberNewCfgTxCtrl,
       "agPortFiberNewCfgTxPulse": agPortFiberNewCfgTxPulse,
       "agPortFiberNewCfgTxUp": agPortFiberNewCfgTxUp,
       "agPortFiberNewCfgTxDn": agPortFiberNewCfgTxDn,
       "agRadiusConfig": agRadiusConfig,
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
       "radNewCfgTelnet": radNewCfgTelnet,
       "radCurCfgAuthenSecondString": radCurCfgAuthenSecondString,
       "radNewCfgAuthenSecondString": radNewCfgAuthenSecondString,
       "radCurCfgSecBd": radCurCfgSecBd,
       "radNewCfgSecBd": radNewCfgSecBd,
       "agNTP": agNTP,
       "agCurCfgNTPServer": agCurCfgNTPServer,
       "agNewCfgNTPServer": agNewCfgNTPServer,
       "agCurCfgNTPResyncInterval": agCurCfgNTPResyncInterval,
       "agNewCfgNTPResyncInterval": agNewCfgNTPResyncInterval,
       "agCurCfgNTPTzoneHHMM": agCurCfgNTPTzoneHHMM,
       "agNewCfgNTPTzoneHHMM": agNewCfgNTPTzoneHHMM,
       "agCurCfgNTPDlight": agCurCfgNTPDlight,
       "agNewCfgNTPDlight": agNewCfgNTPDlight,
       "agCurCfgNTPService": agCurCfgNTPService,
       "agNewCfgNTPService": agNewCfgNTPService,
       "agCurCfgNTPSecServer": agCurCfgNTPSecServer,
       "agNewCfgNTPSecServer": agNewCfgNTPSecServer,
       "agSyslog": agSyslog,
       "agCurCfgSyslogHost": agCurCfgSyslogHost,
       "agNewCfgSyslogHost": agNewCfgSyslogHost,
       "agCurCfgSyslog2Host": agCurCfgSyslog2Host,
       "agNewCfgSyslog2Host": agNewCfgSyslog2Host,
       "agCurCfgSyslogFac": agCurCfgSyslogFac,
       "agNewCfgSyslogFac": agNewCfgSyslogFac,
       "agCurCfgSyslog2Fac": agCurCfgSyslog2Fac,
       "agNewCfgSyslog2Fac": agNewCfgSyslog2Fac,
       "agClrSyslogMsgs": agClrSyslogMsgs,
       "agSyslogMsgTableMaxSize": agSyslogMsgTableMaxSize,
       "agSyslogMsgTable": agSyslogMsgTable,
       "agSyslogMsgTableEntry": agSyslogMsgTableEntry,
       "agSyslogMsgIndex": agSyslogMsgIndex,
       "agSyslogMessage": agSyslogMessage,
       "agLog": agLog,
       "agNewCfgSyslogTrapConsole": agNewCfgSyslogTrapConsole,
       "agCurCfgSyslogTrapConsole": agCurCfgSyslogTrapConsole,
       "agNewCfgSyslogTrapSystem": agNewCfgSyslogTrapSystem,
       "agCurCfgSyslogTrapSystem": agCurCfgSyslogTrapSystem,
       "agNewCfgSyslogTrapMgmt": agNewCfgSyslogTrapMgmt,
       "agCurCfgSyslogTrapMgmt": agCurCfgSyslogTrapMgmt,
       "agNewCfgSyslogTrapCli": agNewCfgSyslogTrapCli,
       "agCurCfgSyslogTrapCli": agCurCfgSyslogTrapCli,
       "agNewCfgSyslogTrapStg": agNewCfgSyslogTrapStg,
       "agCurCfgSyslogTrapStg": agCurCfgSyslogTrapStg,
       "agNewCfgSyslogTrapVlan": agNewCfgSyslogTrapVlan,
       "agCurCfgSyslogTrapVlan": agCurCfgSyslogTrapVlan,
       "agNewCfgSyslogTrapSsh": agNewCfgSyslogTrapSsh,
       "agCurCfgSyslogTrapSsh": agCurCfgSyslogTrapSsh,
       "agNewCfgSyslogTrapVrrp": agNewCfgSyslogTrapVrrp,
       "agCurCfgSyslogTrapVrrp": agCurCfgSyslogTrapVrrp,
       "agNewCfgSyslogTrapNtp": agNewCfgSyslogTrapNtp,
       "agCurCfgSyslogTrapNtp": agCurCfgSyslogTrapNtp,
       "agNewCfgSyslogTrapIp": agNewCfgSyslogTrapIp,
       "agCurCfgSyslogTrapIp": agCurCfgSyslogTrapIp,
       "agNewCfgSyslogTrapWeb": agNewCfgSyslogTrapWeb,
       "agCurCfgSyslogTrapWeb": agCurCfgSyslogTrapWeb,
       "agNewCfgSyslogTrapOspf": agNewCfgSyslogTrapOspf,
       "agCurCfgSyslogTrapOspf": agCurCfgSyslogTrapOspf,
       "agNewCfgSyslogTrapRmon": agNewCfgSyslogTrapRmon,
       "agCurCfgSyslogTrapRmon": agCurCfgSyslogTrapRmon,
       "agNewCfgSyslogTrapUfd": agNewCfgSyslogTrapUfd,
       "agCurCfgSyslogTrapUfd": agCurCfgSyslogTrapUfd,
       "agNewCfgSyslogTrapCfg": agNewCfgSyslogTrapCfg,
       "agCurCfgSyslogTrapCfg": agCurCfgSyslogTrapCfg,
       "agNewCfgSyslogTrap8021x": agNewCfgSyslogTrap8021x,
       "agCurCfgSyslogTrap8021x": agCurCfgSyslogTrap8021x,
       "agNewCfgSyslogTrapHotlinks": agNewCfgSyslogTrapHotlinks,
       "agCurCfgSyslogTrapHotlinks": agCurCfgSyslogTrapHotlinks,
       "agCurCfgSyslogSev": agCurCfgSyslogSev,
       "agNewCfgSyslogSev": agNewCfgSyslogSev,
       "agCurCfgSyslog2Sev": agCurCfgSyslog2Sev,
       "agNewCfgSyslog2Sev": agNewCfgSyslog2Sev,
       "agTrapHost": agTrapHost,
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
       "agTftp": agTftp,
       "agTftpServer": agTftpServer,
       "agTftpImage": agTftpImage,
       "agTftpImageFileName": agTftpImageFileName,
       "agTftpCfgFileName": agTftpCfgFileName,
       "agTftpDumpFileName": agTftpDumpFileName,
       "agTftpAction": agTftpAction,
       "agTftpLastActionStatus": agTftpLastActionStatus,
       "agTftpUserName": agTftpUserName,
       "agTftpPassword": agTftpPassword,
       "agTftpTSDumpFileName": agTftpTSDumpFileName,
       "agApply": agApply,
       "agApplyPending": agApplyPending,
       "agApplyConfig": agApplyConfig,
       "agApplyTableSize": agApplyTableSize,
       "agApplyTable": agApplyTable,
       "agApplyTableEntry": agApplyTableEntry,
       "agApplyIndex": agApplyIndex,
       "agApplyString": agApplyString,
       "agTacacsConfig": agTacacsConfig,
       "tacCurCfgPrimaryIpAddr": tacCurCfgPrimaryIpAddr,
       "tacNewCfgPrimaryIpAddr": tacNewCfgPrimaryIpAddr,
       "tacCurCfgSecondaryIpAddr": tacCurCfgSecondaryIpAddr,
       "tacNewCfgSecondaryIpAddr": tacNewCfgSecondaryIpAddr,
       "tacCurCfgPort": tacCurCfgPort,
       "tacNewCfgPort": tacNewCfgPort,
       "tacCurCfgTimeout": tacCurCfgTimeout,
       "tacNewCfgTimeout": tacNewCfgTimeout,
       "tacCurCfgRetries": tacCurCfgRetries,
       "tacNewCfgRetries": tacNewCfgRetries,
       "tacCurCfgState": tacCurCfgState,
       "tacNewCfgState": tacNewCfgState,
       "tacCurCfgAuthenString": tacCurCfgAuthenString,
       "tacNewCfgAuthenString": tacNewCfgAuthenString,
       "tacCurCfgTelnet": tacCurCfgTelnet,
       "tacNewCfgTelnet": tacNewCfgTelnet,
       "tacCurCfgAuthenSecondString": tacCurCfgAuthenSecondString,
       "tacNewCfgAuthenSecondString": tacNewCfgAuthenSecondString,
       "tacCurCfgSecBd": tacCurCfgSecBd,
       "tacNewCfgSecBd": tacNewCfgSecBd,
       "tacCurCfgCmap": tacCurCfgCmap,
       "tacNewCfgCmap": tacNewCfgCmap,
       "agTacacsUserMapCurCfgTable": agTacacsUserMapCurCfgTable,
       "agTacacsUserMapCurCfgTableEntry": agTacacsUserMapCurCfgTableEntry,
       "agTacacsUserMapCurCfgUId": agTacacsUserMapCurCfgUId,
       "agTacacsUserMapCurCfgMapping": agTacacsUserMapCurCfgMapping,
       "agTacacsUserMapNewCfgTable": agTacacsUserMapNewCfgTable,
       "agTacacsUserMapNewCfgTableEntry": agTacacsUserMapNewCfgTableEntry,
       "agTacacsUserMapNewCfgUId": agTacacsUserMapNewCfgUId,
       "agTacacsUserMapNewCfgMapping": agTacacsUserMapNewCfgMapping,
       "agMgmtNetConfig": agMgmtNetConfig,
       "agMgmtNetTableMaxSize": agMgmtNetTableMaxSize,
       "agCurCfgMgmtNetTable": agCurCfgMgmtNetTable,
       "agCurCfgMgmtNetEntry": agCurCfgMgmtNetEntry,
       "agCurCfgMgmtNetIndex": agCurCfgMgmtNetIndex,
       "agCurCfgMgmtNetSubnet": agCurCfgMgmtNetSubnet,
       "agCurCfgMgmtNetMask": agCurCfgMgmtNetMask,
       "agNewCfgMgmtNetTable": agNewCfgMgmtNetTable,
       "agNewCfgMgmtNetEntry": agNewCfgMgmtNetEntry,
       "agNewCfgMgmtNetIndex": agNewCfgMgmtNetIndex,
       "agNewCfgMgmtNetSubnet": agNewCfgMgmtNetSubnet,
       "agNewCfgMgmtNetMask": agNewCfgMgmtNetMask,
       "agNewCfgMgmtNetDelete": agNewCfgMgmtNetDelete,
       "agAccess": agAccess,
       "agAccessUserMaxUserID": agAccessUserMaxUserID,
       "agAccessUserCurCfgTable": agAccessUserCurCfgTable,
       "agAccessUserCurCfgTableEntry": agAccessUserCurCfgTableEntry,
       "agAccessUserCurCfgUId": agAccessUserCurCfgUId,
       "agAccessUserCurCos": agAccessUserCurCos,
       "agAccessUserCurCfgName": agAccessUserCurCfgName,
       "agAccessUserCurCfgPswd": agAccessUserCurCfgPswd,
       "agAccessUserCurCfgState": agAccessUserCurCfgState,
       "agAccessUserNewCfgTable": agAccessUserNewCfgTable,
       "agAccessUserNewCfgTableEntry": agAccessUserNewCfgTableEntry,
       "agAccessUserNewCfgUId": agAccessUserNewCfgUId,
       "agAccessUserNewCos": agAccessUserNewCos,
       "agAccessUserNewCfgName": agAccessUserNewCfgName,
       "agAccessUserNewCfgPswd": agAccessUserNewCfgPswd,
       "agAccessUserNewCfgState": agAccessUserNewCfgState,
       "agAccessUserNewCfgDelete": agAccessUserNewCfgDelete,
       "agentStats": agentStats,
       "pktStats": pktStats,
       "pktStatsAllocs": pktStatsAllocs,
       "pktStatsFrees": pktStatsFrees,
       "pktStatsAllocFails": pktStatsAllocFails,
       "pktStatsMediums": pktStatsMediums,
       "pktStatsJumbos": pktStatsJumbos,
       "pktStatsSmalls": pktStatsSmalls,
       "pktStatsMediumsHiWatermark": pktStatsMediumsHiWatermark,
       "pktStatsJumbosHiWatermark": pktStatsJumbosHiWatermark,
       "pktStatsSmallsHiWatermark": pktStatsSmallsHiWatermark,
       "mpCpuStats": mpCpuStats,
       "mpCpuStatsUtil1Second": mpCpuStatsUtil1Second,
       "mpCpuStatsUtil4Seconds": mpCpuStatsUtil4Seconds,
       "mpCpuStatsUtil64Seconds": mpCpuStatsUtil64Seconds,
       "portStats": portStats,
       "portStatsTable": portStatsTable,
       "portStatsTableEntry": portStatsTableEntry,
       "portStatsIndx": portStatsIndx,
       "portStatsPhyIfInOctets": portStatsPhyIfInOctets,
       "portStatsPhyIfInUcastPkts": portStatsPhyIfInUcastPkts,
       "portStatsPhyIfInNUcastPkts": portStatsPhyIfInNUcastPkts,
       "portStatsPhyIfInDiscards": portStatsPhyIfInDiscards,
       "portStatsPhyIfInErrors": portStatsPhyIfInErrors,
       "portStatsPhyIfInUnknownProtos": portStatsPhyIfInUnknownProtos,
       "portStatsPhyIfOutOctets": portStatsPhyIfOutOctets,
       "portStatsPhyIfOutUcastPkts": portStatsPhyIfOutUcastPkts,
       "portStatsPhyIfOutNUcastPkts": portStatsPhyIfOutNUcastPkts,
       "portStatsPhyIfOutDiscards": portStatsPhyIfOutDiscards,
       "portStatsPhyIfOutErrors": portStatsPhyIfOutErrors,
       "portStatsPhyIfOutQLen": portStatsPhyIfOutQLen,
       "portStatsPhyIfInBroadcastPkts": portStatsPhyIfInBroadcastPkts,
       "portStatsPhyIfOutBroadcastPkts": portStatsPhyIfOutBroadcastPkts,
       "portStatsClear": portStatsClear,
       "portStatsPhyIfInMulticastPkts": portStatsPhyIfInMulticastPkts,
       "portStatsPhyIfOutMulticastPkts": portStatsPhyIfOutMulticastPkts,
       "dot1xPortStatsTable": dot1xPortStatsTable,
       "dot1xPortStatsTableEntry": dot1xPortStatsTableEntry,
       "dot1xPortStatsIndx": dot1xPortStatsIndx,
       "eapolFramesRx": eapolFramesRx,
       "eapolFramesTx": eapolFramesTx,
       "eapolStartFramesRx": eapolStartFramesRx,
       "eapolLogoffFramesRx": eapolLogoffFramesRx,
       "eapolRespIdFramesRx": eapolRespIdFramesRx,
       "eapolRespFramesRx": eapolRespFramesRx,
       "eapolReqIdFramesTx": eapolReqIdFramesTx,
       "eapolReqFramesTx": eapolReqFramesTx,
       "invalidEapolFramesRx": invalidEapolFramesRx,
       "eapLengthErrorFramesRx": eapLengthErrorFramesRx,
       "authEntersConnecting": authEntersConnecting,
       "authEapLogoffsWhileConnecting": authEapLogoffsWhileConnecting,
       "authEntersAuthenticating": authEntersAuthenticating,
       "authSuccessesWhileAuthenticating": authSuccessesWhileAuthenticating,
       "authTimeoutsWhileAuthenticating": authTimeoutsWhileAuthenticating,
       "authFailWhileAuthenticating": authFailWhileAuthenticating,
       "authReauthsWhileAuthenticating": authReauthsWhileAuthenticating,
       "authEapStartsWhileAuthenticating": authEapStartsWhileAuthenticating,
       "authEapLogoffWhileAuthenticating": authEapLogoffWhileAuthenticating,
       "authReauthsWhileAuthenticated": authReauthsWhileAuthenticated,
       "authEapStartsWhileAuthenticated": authEapStartsWhileAuthenticated,
       "authEapLogoffWhileAuthenticated": authEapLogoffWhileAuthenticated,
       "backendResponses": backendResponses,
       "backendAccessChallenges": backendAccessChallenges,
       "backendOtherRequestsToSupplicant": backendOtherRequestsToSupplicant,
       "backendNonNakResponsesFromSupplicant": backendNonNakResponsesFromSupplicant,
       "backendAuthSuccesses": backendAuthSuccesses,
       "backendAuthFails": backendAuthFails,
       "lastEapolFrameVersion": lastEapolFrameVersion,
       "lastEapolFrameSource": lastEapolFrameSource,
       "spStats": spStats,
       "mgmtStats": mgmtStats,
       "ntpStats": ntpStats,
       "ntpPrimaryServerReqSent": ntpPrimaryServerReqSent,
       "ntpPrimaryServerRespRcvd": ntpPrimaryServerRespRcvd,
       "ntpPrimaryServerUpdates": ntpPrimaryServerUpdates,
       "ntpSecondaryServerReqSent": ntpSecondaryServerReqSent,
       "ntpSecondaryServerRespRcvd": ntpSecondaryServerRespRcvd,
       "ntpSecondaryServerUpdates": ntpSecondaryServerUpdates,
       "ntpLastUpdateServer": ntpLastUpdateServer,
       "ntpLastUpdateTime": ntpLastUpdateTime,
       "ntpClearStats": ntpClearStats,
       "ntpSystemCurrentTime": ntpSystemCurrentTime,
       "aclPortStats": aclPortStats,
       "aclPortStatsTable": aclPortStatsTable,
       "aclPortStatsTableEntry": aclPortStatsTableEntry,
       "aclPortStatsIndx": aclPortStatsIndx,
       "aclPortStatsHits": aclPortStatsHits,
       "aclPortClearStats": aclPortClearStats,
       "aclMeterPortStats": aclMeterPortStats,
       "aclMeterPortStatsTable": aclMeterPortStatsTable,
       "aclMeterPortStatsTableEntry": aclMeterPortStatsTableEntry,
       "aclMeterPortStatsIndx": aclMeterPortStatsIndx,
       "aclMeterPortStatsHits": aclMeterPortStatsHits,
       "aclMeterPortClearStats": aclMeterPortClearStats,
       "agentInfo": agentInfo,
       "hardware": hardware,
       "hwPartNumber": hwPartNumber,
       "hwRevision": hwRevision,
       "hwPowerSupplyStatus": hwPowerSupplyStatus,
       "hwSensor1Temp": hwSensor1Temp,
       "hwInsertedCubeType": hwInsertedCubeType,
       "portInfo": portInfo,
       "portInfoTable": portInfoTable,
       "portInfoTableEntry": portInfoTableEntry,
       "portInfoIndx": portInfoIndx,
       "portInfoSpeed": portInfoSpeed,
       "portInfoMode": portInfoMode,
       "portInfoFlowCtrl": portInfoFlowCtrl,
       "portInfoLink": portInfoLink,
       "portInfoPhyIfDescr": portInfoPhyIfDescr,
       "portInfoPhyIfType": portInfoPhyIfType,
       "portInfoPhyIfMtu": portInfoPhyIfMtu,
       "portInfoPhyIfPhysAddress": portInfoPhyIfPhysAddress,
       "portInfoPhyIfOperStatus": portInfoPhyIfOperStatus,
       "portInfoPhyIfLastChange": portInfoPhyIfLastChange,
       "swKeyInfo": swKeyInfo,
       "agDiff": agDiff,
       "agDiffState": agDiffState,
       "agDiffTableSize": agDiffTableSize,
       "agDiffTable": agDiffTable,
       "agDiffTableEntry": agDiffTableEntry,
       "agDiffIndex": agDiffIndex,
       "agDiffString": agDiffString,
       "agCfgDump": agCfgDump,
       "agCfgDumpState": agCfgDumpState,
       "agCfgDumpTableSize": agCfgDumpTableSize,
       "agCfgDumpTable": agCfgDumpTable,
       "agCfgDumpTableEntry": agCfgDumpTableEntry,
       "agCfgDumpIndex": agCfgDumpIndex,
       "agCfgDumpString": agCfgDumpString,
       "mgmtInfo": mgmtInfo,
       "geaportInfo": geaportInfo,
       "geaportInfoTable": geaportInfoTable,
       "geaportInfoTableEntry": geaportInfoTableEntry,
       "geaportInfoLogicalIndex": geaportInfoLogicalIndex,
       "geaportInfoPort": geaportInfoPort,
       "geaportInfoUnit": geaportInfoUnit,
       "ufdInfo": ufdInfo,
       "ufdInfoState": ufdInfoState,
       "ufdInfoLtMStatus": ufdInfoLtMStatus,
       "ufdInfoLtMPorts": ufdInfoLtMPorts,
       "ufdInfoLtMTrunks": ufdInfoLtMTrunks,
       "ufdInfoLtDStatus": ufdInfoLtDStatus,
       "ufdInfoLtDPorts": ufdInfoLtDPorts,
       "ufdInfoLtDTrunks": ufdInfoLtDTrunks,
       "agentOper": agentOper,
       "agPortOperTable": agPortOperTable,
       "agPortOperTableEntry": agPortOperTableEntry,
       "portOperIdx": portOperIdx,
       "portOperState": portOperState,
       "portOperRmon": portOperRmon,
       "portOperDot1xTable": portOperDot1xTable,
       "portOperDot1xTableEntry": portOperDot1xTableEntry,
       "portOperDot1xIndx": portOperDot1xIndx,
       "portOperDot1xReset": portOperDot1xReset,
       "portOperDot1xReauth": portOperDot1xReauth,
       "agNTPOper": agNTPOper,
       "ntpOperSendReq": ntpOperSendReq}
)
