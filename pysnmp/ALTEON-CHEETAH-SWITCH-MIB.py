# SNMP MIB module (ALTEON-CHEETAH-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-CHEETAH-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:52 2024
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

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1)
)
agent.setRevisions(
        ("2004-09-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentConfig_ObjectIdentity = ObjectIdentity
agentConfig = _AgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1)
)
_AgSystem_ObjectIdentity = ObjectIdentity
agSystem = _AgSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 6),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_AgReset_Type.__name__ = "Integer32"
_AgReset_Object = MibScalar
agReset = _AgReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 20),
    _AgNewCfgLoginBanner_Type()
)
agNewCfgLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgLoginBanner.setStatus("current")


class _AgCurCfgSmtpHost_Type(DisplayString):
    """Custom type agCurCfgSmtpHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AgCurCfgSmtpHost_Type.__name__ = "DisplayString"
_AgCurCfgSmtpHost_Object = MibScalar
agCurCfgSmtpHost = _AgCurCfgSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 21),
    _AgCurCfgSmtpHost_Type()
)
agCurCfgSmtpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSmtpHost.setStatus("current")


class _AgNewCfgSmtpHost_Type(DisplayString):
    """Custom type agNewCfgSmtpHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AgNewCfgSmtpHost_Type.__name__ = "DisplayString"
_AgNewCfgSmtpHost_Object = MibScalar
agNewCfgSmtpHost = _AgNewCfgSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 22),
    _AgNewCfgSmtpHost_Type()
)
agNewCfgSmtpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSmtpHost.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 29),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 30),
    _AgNewCfgBootp_Type()
)
agNewCfgBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgBootp.setStatus("current")


class _AgCurCfgSnmpTimeout_Type(Integer32):
    """Custom type agCurCfgSnmpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgCurCfgSnmpTimeout_Type.__name__ = "Integer32"
_AgCurCfgSnmpTimeout_Object = MibScalar
agCurCfgSnmpTimeout = _AgCurCfgSnmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 32),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 33),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 34),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 35),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 36),
    _AgClearFlashDump_Type()
)
agClearFlashDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agClearFlashDump.setStatus("current")


class _AgCurCfgNortelMultipleStgMode_Type(Integer32):
    """Custom type agCurCfgNortelMultipleStgMode based on Integer32"""
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


_AgCurCfgNortelMultipleStgMode_Type.__name__ = "Integer32"
_AgCurCfgNortelMultipleStgMode_Object = MibScalar
agCurCfgNortelMultipleStgMode = _AgCurCfgNortelMultipleStgMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 37),
    _AgCurCfgNortelMultipleStgMode_Type()
)
agCurCfgNortelMultipleStgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNortelMultipleStgMode.setStatus("current")


class _AgNewCfgNortelMultipleStgMode_Type(Integer32):
    """Custom type agNewCfgNortelMultipleStgMode based on Integer32"""
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


_AgNewCfgNortelMultipleStgMode_Type.__name__ = "Integer32"
_AgNewCfgNortelMultipleStgMode_Object = MibScalar
agNewCfgNortelMultipleStgMode = _AgNewCfgNortelMultipleStgMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 38),
    _AgNewCfgNortelMultipleStgMode_Type()
)
agNewCfgNortelMultipleStgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNortelMultipleStgMode.setStatus("current")
_AgCurCfgTrapSrcIf_Type = Integer32
_AgCurCfgTrapSrcIf_Object = MibScalar
agCurCfgTrapSrcIf = _AgCurCfgTrapSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 39),
    _AgCurCfgTrapSrcIf_Type()
)
agCurCfgTrapSrcIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapSrcIf.setStatus("current")
_AgNewCfgTrapSrcIf_Type = Integer32
_AgNewCfgTrapSrcIf_Object = MibScalar
agNewCfgTrapSrcIf = _AgNewCfgTrapSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 40),
    _AgNewCfgTrapSrcIf_Type()
)
agNewCfgTrapSrcIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTrapSrcIf.setStatus("current")


class _AgCurCfgARPMaxRate_Type(Integer32):
    """Custom type agCurCfgARPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgCurCfgARPMaxRate_Type.__name__ = "Integer32"
_AgCurCfgARPMaxRate_Object = MibScalar
agCurCfgARPMaxRate = _AgCurCfgARPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 41),
    _AgCurCfgARPMaxRate_Type()
)
agCurCfgARPMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgARPMaxRate.setStatus("current")


class _AgNewCfgARPMaxRate_Type(Integer32):
    """Custom type agNewCfgARPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgNewCfgARPMaxRate_Type.__name__ = "Integer32"
_AgNewCfgARPMaxRate_Object = MibScalar
agNewCfgARPMaxRate = _AgNewCfgARPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 42),
    _AgNewCfgARPMaxRate_Type()
)
agNewCfgARPMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgARPMaxRate.setStatus("current")


class _AgCurCfgICMPMaxRate_Type(Integer32):
    """Custom type agCurCfgICMPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgCurCfgICMPMaxRate_Type.__name__ = "Integer32"
_AgCurCfgICMPMaxRate_Object = MibScalar
agCurCfgICMPMaxRate = _AgCurCfgICMPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 43),
    _AgCurCfgICMPMaxRate_Type()
)
agCurCfgICMPMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgICMPMaxRate.setStatus("current")


class _AgNewCfgICMPMaxRate_Type(Integer32):
    """Custom type agNewCfgICMPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgNewCfgICMPMaxRate_Type.__name__ = "Integer32"
_AgNewCfgICMPMaxRate_Object = MibScalar
agNewCfgICMPMaxRate = _AgNewCfgICMPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 44),
    _AgNewCfgICMPMaxRate_Type()
)
agNewCfgICMPMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgICMPMaxRate.setStatus("current")


class _AgCurCfgTCPMaxRate_Type(Integer32):
    """Custom type agCurCfgTCPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgCurCfgTCPMaxRate_Type.__name__ = "Integer32"
_AgCurCfgTCPMaxRate_Object = MibScalar
agCurCfgTCPMaxRate = _AgCurCfgTCPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 45),
    _AgCurCfgTCPMaxRate_Type()
)
agCurCfgTCPMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTCPMaxRate.setStatus("current")


class _AgNewCfgTCPMaxRate_Type(Integer32):
    """Custom type agNewCfgTCPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgNewCfgTCPMaxRate_Type.__name__ = "Integer32"
_AgNewCfgTCPMaxRate_Object = MibScalar
agNewCfgTCPMaxRate = _AgNewCfgTCPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 46),
    _AgNewCfgTCPMaxRate_Type()
)
agNewCfgTCPMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTCPMaxRate.setStatus("current")


class _AgCurCfgUDPMaxRate_Type(Integer32):
    """Custom type agCurCfgUDPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgCurCfgUDPMaxRate_Type.__name__ = "Integer32"
_AgCurCfgUDPMaxRate_Object = MibScalar
agCurCfgUDPMaxRate = _AgCurCfgUDPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 47),
    _AgCurCfgUDPMaxRate_Type()
)
agCurCfgUDPMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgUDPMaxRate.setStatus("current")


class _AgNewCfgUDPMaxRate_Type(Integer32):
    """Custom type agNewCfgUDPMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgNewCfgUDPMaxRate_Type.__name__ = "Integer32"
_AgNewCfgUDPMaxRate_Object = MibScalar
agNewCfgUDPMaxRate = _AgNewCfgUDPMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 48),
    _AgNewCfgUDPMaxRate_Type()
)
agNewCfgUDPMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgUDPMaxRate.setStatus("current")


class _AgCurCfgHttpsServerPort_Type(Integer32):
    """Custom type agCurCfgHttpsServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgCurCfgHttpsServerPort_Type.__name__ = "Integer32"
_AgCurCfgHttpsServerPort_Object = MibScalar
agCurCfgHttpsServerPort = _AgCurCfgHttpsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 49),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 50),
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
          ("americas-Canada-MountStdTime-DawsonCrkStJohnBritColumbia", 96),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 55),
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
          ("americas-Canada-MountStdTime-DawsonCrkStJohnBritColumbia", 96),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 56),
    _AgNewDaylightSavings_Type()
)
agNewDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewDaylightSavings.setStatus("current")


class _AgCurCfgIdleCLITimeout_Type(Integer32):
    """Custom type agCurCfgIdleCLITimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10080),
    )


_AgCurCfgIdleCLITimeout_Type.__name__ = "Integer32"
_AgCurCfgIdleCLITimeout_Object = MibScalar
agCurCfgIdleCLITimeout = _AgCurCfgIdleCLITimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 57),
    _AgCurCfgIdleCLITimeout_Type()
)
agCurCfgIdleCLITimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgIdleCLITimeout.setStatus("current")


class _AgNewCfgIdleCLITimeout_Type(Integer32):
    """Custom type agNewCfgIdleCLITimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10080),
    )


_AgNewCfgIdleCLITimeout_Type.__name__ = "Integer32"
_AgNewCfgIdleCLITimeout_Object = MibScalar
agNewCfgIdleCLITimeout = _AgNewCfgIdleCLITimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 58),
    _AgNewCfgIdleCLITimeout_Type()
)
agNewCfgIdleCLITimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgIdleCLITimeout.setStatus("current")


class _AgCurCfgXMLCfgServerPort_Type(Integer32):
    """Custom type agCurCfgXMLCfgServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgCurCfgXMLCfgServerPort_Type.__name__ = "Integer32"
_AgCurCfgXMLCfgServerPort_Object = MibScalar
agCurCfgXMLCfgServerPort = _AgCurCfgXMLCfgServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 59),
    _AgCurCfgXMLCfgServerPort_Type()
)
agCurCfgXMLCfgServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgXMLCfgServerPort.setStatus("current")


class _AgNewCfgXMLCfgServerPort_Type(Integer32):
    """Custom type agNewCfgXMLCfgServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgXMLCfgServerPort_Type.__name__ = "Integer32"
_AgNewCfgXMLCfgServerPort_Object = MibScalar
agNewCfgXMLCfgServerPort = _AgNewCfgXMLCfgServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 60),
    _AgNewCfgXMLCfgServerPort_Type()
)
agNewCfgXMLCfgServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgXMLCfgServerPort.setStatus("current")


class _AgSymantecGlobalState_Type(Integer32):
    """Custom type agSymantecGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AgSymantecGlobalState_Type.__name__ = "Integer32"
_AgSymantecGlobalState_Object = MibScalar
agSymantecGlobalState = _AgSymantecGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 1, 61),
    _AgSymantecGlobalState_Type()
)
agSymantecGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSymantecGlobalState.setStatus("current")
_AgPortConfig_ObjectIdentity = ObjectIdentity
agPortConfig = _AgPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2)
)
_AgPortTableMaxEnt_Type = Integer32
_AgPortTableMaxEnt_Object = MibScalar
agPortTableMaxEnt = _AgPortTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 1),
    _AgPortTableMaxEnt_Type()
)
agPortTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortTableMaxEnt.setStatus("current")
_AgPortCurCfgTable_Object = MibTable
agPortCurCfgTable = _AgPortCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    agPortCurCfgTable.setStatus("current")
_AgPortCurCfgTableEntry_Object = MibTableRow
agPortCurCfgTableEntry = _AgPortCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1)
)
agPortCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agPortCurCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortCurCfgTableEntry.setStatus("current")
_AgPortCurCfgIndx_Type = Integer32
_AgPortCurCfgIndx_Object = MibTableColumn
agPortCurCfgIndx = _AgPortCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 3),
    _AgPortCurCfgVlanTag_Type()
)
agPortCurCfgVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgVlanTag.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 5),
    _AgPortCurCfgRmon_Type()
)
agPortCurCfgRmon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgRmon.setStatus("current")
_AgPortCurCfgPVID_Type = Integer32
_AgPortCurCfgPVID_Object = MibTableColumn
agPortCurCfgPVID = _AgPortCurCfgPVID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 6),
    _AgPortCurCfgPVID_Type()
)
agPortCurCfgPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPVID.setStatus("current")


class _AgPortCurCfgFastEthAutoNeg_Type(Integer32):
    """Custom type agPortCurCfgFastEthAutoNeg based on Integer32"""
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


_AgPortCurCfgFastEthAutoNeg_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthAutoNeg_Object = MibTableColumn
agPortCurCfgFastEthAutoNeg = _AgPortCurCfgFastEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 7),
    _AgPortCurCfgFastEthAutoNeg_Type()
)
agPortCurCfgFastEthAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthAutoNeg.setStatus("current")


class _AgPortCurCfgFastEthSpeed_Type(Integer32):
    """Custom type agPortCurCfgFastEthSpeed based on Integer32"""
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


_AgPortCurCfgFastEthSpeed_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthSpeed_Object = MibTableColumn
agPortCurCfgFastEthSpeed = _AgPortCurCfgFastEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 8),
    _AgPortCurCfgFastEthSpeed_Type()
)
agPortCurCfgFastEthSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthSpeed.setStatus("current")


class _AgPortCurCfgFastEthMode_Type(Integer32):
    """Custom type agPortCurCfgFastEthMode based on Integer32"""
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


_AgPortCurCfgFastEthMode_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthMode_Object = MibTableColumn
agPortCurCfgFastEthMode = _AgPortCurCfgFastEthMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 9),
    _AgPortCurCfgFastEthMode_Type()
)
agPortCurCfgFastEthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthMode.setStatus("current")


class _AgPortCurCfgFastEthFctl_Type(Integer32):
    """Custom type agPortCurCfgFastEthFctl based on Integer32"""
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


_AgPortCurCfgFastEthFctl_Type.__name__ = "Integer32"
_AgPortCurCfgFastEthFctl_Object = MibTableColumn
agPortCurCfgFastEthFctl = _AgPortCurCfgFastEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 10),
    _AgPortCurCfgFastEthFctl_Type()
)
agPortCurCfgFastEthFctl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgFastEthFctl.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 11),
    _AgPortCurCfgGigEthAutoNeg_Type()
)
agPortCurCfgGigEthAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthAutoNeg.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 12),
    _AgPortCurCfgGigEthFctl_Type()
)
agPortCurCfgGigEthFctl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthFctl.setStatus("current")


class _AgPortCurCfgPortName_Type(DisplayString):
    """Custom type agPortCurCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgPortCurCfgPortName_Type.__name__ = "DisplayString"
_AgPortCurCfgPortName_Object = MibTableColumn
agPortCurCfgPortName = _AgPortCurCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 13),
    _AgPortCurCfgPortName_Type()
)
agPortCurCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPortName.setStatus("current")
_AgPortCurCfgBwmContract_Type = Integer32
_AgPortCurCfgBwmContract_Object = MibTableColumn
agPortCurCfgBwmContract = _AgPortCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 14),
    _AgPortCurCfgBwmContract_Type()
)
agPortCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgBwmContract.setStatus("current")


class _AgPortCurCfgDiscardNonIPs_Type(Integer32):
    """Custom type agPortCurCfgDiscardNonIPs based on Integer32"""
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


_AgPortCurCfgDiscardNonIPs_Type.__name__ = "Integer32"
_AgPortCurCfgDiscardNonIPs_Object = MibTableColumn
agPortCurCfgDiscardNonIPs = _AgPortCurCfgDiscardNonIPs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 15),
    _AgPortCurCfgDiscardNonIPs_Type()
)
agPortCurCfgDiscardNonIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgDiscardNonIPs.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 16),
    _AgPortCurCfgLinkTrap_Type()
)
agPortCurCfgLinkTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgLinkTrap.setStatus("current")


class _AgPortCurCfgPreferred_Type(Integer32):
    """Custom type agPortCurCfgPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("sfp", 2))
    )


_AgPortCurCfgPreferred_Type.__name__ = "Integer32"
_AgPortCurCfgPreferred_Object = MibTableColumn
agPortCurCfgPreferred = _AgPortCurCfgPreferred_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 17),
    _AgPortCurCfgPreferred_Type()
)
agPortCurCfgPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPreferred.setStatus("current")


class _AgPortCurCfgBackup_Type(Integer32):
    """Custom type agPortCurCfgBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("copper", 3),
          ("none", 2),
          ("sfp", 4))
    )


_AgPortCurCfgBackup_Type.__name__ = "Integer32"
_AgPortCurCfgBackup_Object = MibTableColumn
agPortCurCfgBackup = _AgPortCurCfgBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 18),
    _AgPortCurCfgBackup_Type()
)
agPortCurCfgBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgBackup.setStatus("current")


class _AgPortCurCfgEgressBW_Type(DisplayString):
    """Custom type agPortCurCfgEgressBW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AgPortCurCfgEgressBW_Type.__name__ = "DisplayString"
_AgPortCurCfgEgressBW_Object = MibTableColumn
agPortCurCfgEgressBW = _AgPortCurCfgEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 19),
    _AgPortCurCfgEgressBW_Type()
)
agPortCurCfgEgressBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgEgressBW.setStatus("current")
_AgPortCurCfgNonIPBwmContract_Type = Integer32
_AgPortCurCfgNonIPBwmContract_Object = MibTableColumn
agPortCurCfgNonIPBwmContract = _AgPortCurCfgNonIPBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 20),
    _AgPortCurCfgNonIPBwmContract_Type()
)
agPortCurCfgNonIPBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgNonIPBwmContract.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 22),
    _AgPortCurCfgGigEthMode_Type()
)
agPortCurCfgGigEthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgGigEthMode.setStatus("current")


class _AgPortCurCfgPortAlias_Type(DisplayString):
    """Custom type agPortCurCfgPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AgPortCurCfgPortAlias_Type.__name__ = "DisplayString"
_AgPortCurCfgPortAlias_Object = MibTableColumn
agPortCurCfgPortAlias = _AgPortCurCfgPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 2, 1, 24),
    _AgPortCurCfgPortAlias_Type()
)
agPortCurCfgPortAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgPortAlias.setStatus("current")
_AgPortNewCfgTable_Object = MibTable
agPortNewCfgTable = _AgPortNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    agPortNewCfgTable.setStatus("current")
_AgPortNewCfgTableEntry_Object = MibTableRow
agPortNewCfgTableEntry = _AgPortNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1)
)
agPortNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agPortNewCfgIndx"),
)
if mibBuilder.loadTexts:
    agPortNewCfgTableEntry.setStatus("current")
_AgPortNewCfgIndx_Type = Integer32
_AgPortNewCfgIndx_Object = MibTableColumn
agPortNewCfgIndx = _AgPortNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 3),
    _AgPortNewCfgVlanTag_Type()
)
agPortNewCfgVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgVlanTag.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 5),
    _AgPortNewCfgRmon_Type()
)
agPortNewCfgRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgRmon.setStatus("current")
_AgPortNewCfgPVID_Type = Integer32
_AgPortNewCfgPVID_Object = MibTableColumn
agPortNewCfgPVID = _AgPortNewCfgPVID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 6),
    _AgPortNewCfgPVID_Type()
)
agPortNewCfgPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPVID.setStatus("current")


class _AgPortNewCfgFastEthAutoNeg_Type(Integer32):
    """Custom type agPortNewCfgFastEthAutoNeg based on Integer32"""
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


_AgPortNewCfgFastEthAutoNeg_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthAutoNeg_Object = MibTableColumn
agPortNewCfgFastEthAutoNeg = _AgPortNewCfgFastEthAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 7),
    _AgPortNewCfgFastEthAutoNeg_Type()
)
agPortNewCfgFastEthAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthAutoNeg.setStatus("current")


class _AgPortNewCfgFastEthSpeed_Type(Integer32):
    """Custom type agPortNewCfgFastEthSpeed based on Integer32"""
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


_AgPortNewCfgFastEthSpeed_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthSpeed_Object = MibTableColumn
agPortNewCfgFastEthSpeed = _AgPortNewCfgFastEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 8),
    _AgPortNewCfgFastEthSpeed_Type()
)
agPortNewCfgFastEthSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthSpeed.setStatus("current")


class _AgPortNewCfgFastEthMode_Type(Integer32):
    """Custom type agPortNewCfgFastEthMode based on Integer32"""
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


_AgPortNewCfgFastEthMode_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthMode_Object = MibTableColumn
agPortNewCfgFastEthMode = _AgPortNewCfgFastEthMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 9),
    _AgPortNewCfgFastEthMode_Type()
)
agPortNewCfgFastEthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthMode.setStatus("current")


class _AgPortNewCfgFastEthFctl_Type(Integer32):
    """Custom type agPortNewCfgFastEthFctl based on Integer32"""
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


_AgPortNewCfgFastEthFctl_Type.__name__ = "Integer32"
_AgPortNewCfgFastEthFctl_Object = MibTableColumn
agPortNewCfgFastEthFctl = _AgPortNewCfgFastEthFctl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 10),
    _AgPortNewCfgFastEthFctl_Type()
)
agPortNewCfgFastEthFctl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgFastEthFctl.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 11),
    _AgPortNewCfgGigEthAutoNeg_Type()
)
agPortNewCfgGigEthAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthAutoNeg.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 12),
    _AgPortNewCfgGigEthFctl_Type()
)
agPortNewCfgGigEthFctl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthFctl.setStatus("current")


class _AgPortNewCfgPortName_Type(DisplayString):
    """Custom type agPortNewCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgPortNewCfgPortName_Type.__name__ = "DisplayString"
_AgPortNewCfgPortName_Object = MibTableColumn
agPortNewCfgPortName = _AgPortNewCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 13),
    _AgPortNewCfgPortName_Type()
)
agPortNewCfgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPortName.setStatus("current")
_AgPortNewCfgBwmContract_Type = Integer32
_AgPortNewCfgBwmContract_Object = MibTableColumn
agPortNewCfgBwmContract = _AgPortNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 14),
    _AgPortNewCfgBwmContract_Type()
)
agPortNewCfgBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgBwmContract.setStatus("current")


class _AgPortNewCfgDiscardNonIPs_Type(Integer32):
    """Custom type agPortNewCfgDiscardNonIPs based on Integer32"""
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


_AgPortNewCfgDiscardNonIPs_Type.__name__ = "Integer32"
_AgPortNewCfgDiscardNonIPs_Object = MibTableColumn
agPortNewCfgDiscardNonIPs = _AgPortNewCfgDiscardNonIPs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 15),
    _AgPortNewCfgDiscardNonIPs_Type()
)
agPortNewCfgDiscardNonIPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgDiscardNonIPs.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 16),
    _AgPortNewCfgLinkTrap_Type()
)
agPortNewCfgLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgLinkTrap.setStatus("current")


class _AgPortNewCfgPreferred_Type(Integer32):
    """Custom type agPortNewCfgPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("sfp", 2))
    )


_AgPortNewCfgPreferred_Type.__name__ = "Integer32"
_AgPortNewCfgPreferred_Object = MibTableColumn
agPortNewCfgPreferred = _AgPortNewCfgPreferred_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 17),
    _AgPortNewCfgPreferred_Type()
)
agPortNewCfgPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPreferred.setStatus("current")


class _AgPortNewCfgBackup_Type(Integer32):
    """Custom type agPortNewCfgBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("none", 1),
          ("sfp", 3))
    )


_AgPortNewCfgBackup_Type.__name__ = "Integer32"
_AgPortNewCfgBackup_Object = MibTableColumn
agPortNewCfgBackup = _AgPortNewCfgBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 18),
    _AgPortNewCfgBackup_Type()
)
agPortNewCfgBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgBackup.setStatus("current")


class _AgPortNewCfgEgressBW_Type(DisplayString):
    """Custom type agPortNewCfgEgressBW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AgPortNewCfgEgressBW_Type.__name__ = "DisplayString"
_AgPortNewCfgEgressBW_Object = MibTableColumn
agPortNewCfgEgressBW = _AgPortNewCfgEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 19),
    _AgPortNewCfgEgressBW_Type()
)
agPortNewCfgEgressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgEgressBW.setStatus("current")
_AgPortNewCfgNonIPBwmContract_Type = Integer32
_AgPortNewCfgNonIPBwmContract_Object = MibTableColumn
agPortNewCfgNonIPBwmContract = _AgPortNewCfgNonIPBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 20),
    _AgPortNewCfgNonIPBwmContract_Type()
)
agPortNewCfgNonIPBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgNonIPBwmContract.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 22),
    _AgPortNewCfgGigEthMode_Type()
)
agPortNewCfgGigEthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgGigEthMode.setStatus("current")


class _AgPortNewCfgPortAlias_Type(DisplayString):
    """Custom type agPortNewCfgPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AgPortNewCfgPortAlias_Type.__name__ = "DisplayString"
_AgPortNewCfgPortAlias_Object = MibTableColumn
agPortNewCfgPortAlias = _AgPortNewCfgPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 2, 3, 1, 24),
    _AgPortNewCfgPortAlias_Type()
)
agPortNewCfgPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPortAlias.setStatus("current")
_AgRadiusConfig_ObjectIdentity = ObjectIdentity
agRadiusConfig = _AgRadiusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3)
)
_RadCurCfgPrimaryIpAddr_Type = IpAddress
_RadCurCfgPrimaryIpAddr_Object = MibScalar
radCurCfgPrimaryIpAddr = _RadCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 1),
    _RadCurCfgPrimaryIpAddr_Type()
)
radCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgPrimaryIpAddr.setStatus("current")
_RadNewCfgPrimaryIpAddr_Type = IpAddress
_RadNewCfgPrimaryIpAddr_Object = MibScalar
radNewCfgPrimaryIpAddr = _RadNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 2),
    _RadNewCfgPrimaryIpAddr_Type()
)
radNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgPrimaryIpAddr.setStatus("current")
_RadCurCfgSecondaryIpAddr_Type = IpAddress
_RadCurCfgSecondaryIpAddr_Object = MibScalar
radCurCfgSecondaryIpAddr = _RadCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 3),
    _RadCurCfgSecondaryIpAddr_Type()
)
radCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgSecondaryIpAddr.setStatus("current")
_RadNewCfgSecondaryIpAddr_Type = IpAddress
_RadNewCfgSecondaryIpAddr_Object = MibScalar
radNewCfgSecondaryIpAddr = _RadNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 12),
    _RadNewCfgState_Type()
)
radNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgState.setStatus("current")


class _RadCurCfgAuthenString_Type(DisplayString):
    """Custom type radCurCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadCurCfgAuthenString_Type.__name__ = "DisplayString"
_RadCurCfgAuthenString_Object = MibScalar
radCurCfgAuthenString = _RadCurCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 13),
    _RadCurCfgAuthenString_Type()
)
radCurCfgAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgAuthenString.setStatus("current")


class _RadNewCfgAuthenString_Type(DisplayString):
    """Custom type radNewCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadNewCfgAuthenString_Type.__name__ = "DisplayString"
_RadNewCfgAuthenString_Object = MibScalar
radNewCfgAuthenString = _RadNewCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 16),
    _RadNewCfgTelnet_Type()
)
radNewCfgTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgTelnet.setStatus("current")


class _RadCurCfgAuthenSecondString_Type(DisplayString):
    """Custom type radCurCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadCurCfgAuthenSecondString_Type.__name__ = "DisplayString"
_RadCurCfgAuthenSecondString_Object = MibScalar
radCurCfgAuthenSecondString = _RadCurCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 17),
    _RadCurCfgAuthenSecondString_Type()
)
radCurCfgAuthenSecondString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radCurCfgAuthenSecondString.setStatus("current")


class _RadNewCfgAuthenSecondString_Type(DisplayString):
    """Custom type radNewCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadNewCfgAuthenSecondString_Type.__name__ = "DisplayString"
_RadNewCfgAuthenSecondString_Object = MibScalar
radNewCfgAuthenSecondString = _RadNewCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 3, 18),
    _RadNewCfgAuthenSecondString_Type()
)
radNewCfgAuthenSecondString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radNewCfgAuthenSecondString.setStatus("current")
_AgNTP_ObjectIdentity = ObjectIdentity
agNTP = _AgNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4)
)
_AgCurCfgNTPServer_Type = IpAddress
_AgCurCfgNTPServer_Object = MibScalar
agCurCfgNTPServer = _AgCurCfgNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 1),
    _AgCurCfgNTPServer_Type()
)
agCurCfgNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPServer.setStatus("current")
_AgNewCfgNTPServer_Type = IpAddress
_AgNewCfgNTPServer_Object = MibScalar
agNewCfgNTPServer = _AgNewCfgNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 10),
    _AgNewCfgNTPService_Type()
)
agNewCfgNTPService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPService.setStatus("current")
_AgCurCfgNTPSecServer_Type = IpAddress
_AgCurCfgNTPSecServer_Object = MibScalar
agCurCfgNTPSecServer = _AgCurCfgNTPSecServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 11),
    _AgCurCfgNTPSecServer_Type()
)
agCurCfgNTPSecServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgNTPSecServer.setStatus("current")
_AgNewCfgNTPSecServer_Type = IpAddress
_AgNewCfgNTPSecServer_Object = MibScalar
agNewCfgNTPSecServer = _AgNewCfgNTPSecServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 4, 12),
    _AgNewCfgNTPSecServer_Type()
)
agNewCfgNTPSecServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgNTPSecServer.setStatus("current")
_AgSyslog_ObjectIdentity = ObjectIdentity
agSyslog = _AgSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5)
)
_AgCurCfgSyslogHost_Type = IpAddress
_AgCurCfgSyslogHost_Object = MibScalar
agCurCfgSyslogHost = _AgCurCfgSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 1),
    _AgCurCfgSyslogHost_Type()
)
agCurCfgSyslogHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogHost.setStatus("current")
_AgNewCfgSyslogHost_Type = IpAddress
_AgNewCfgSyslogHost_Object = MibScalar
agNewCfgSyslogHost = _AgNewCfgSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 2),
    _AgNewCfgSyslogHost_Type()
)
agNewCfgSyslogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogHost.setStatus("current")
_AgCurCfgSyslog2Host_Type = IpAddress
_AgCurCfgSyslog2Host_Object = MibScalar
agCurCfgSyslog2Host = _AgCurCfgSyslog2Host_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 3),
    _AgCurCfgSyslog2Host_Type()
)
agCurCfgSyslog2Host.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslog2Host.setStatus("current")
_AgNewCfgSyslog2Host_Type = IpAddress
_AgNewCfgSyslog2Host_Object = MibScalar
agNewCfgSyslog2Host = _AgNewCfgSyslog2Host_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 9),
    _AgClrSyslogMsgs_Type()
)
agClrSyslogMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agClrSyslogMsgs.setStatus("current")
_AgSyslogMsgTableMaxSize_Type = Integer32
_AgSyslogMsgTableMaxSize_Object = MibScalar
agSyslogMsgTableMaxSize = _AgSyslogMsgTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 10),
    _AgSyslogMsgTableMaxSize_Type()
)
agSyslogMsgTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSyslogMsgTableMaxSize.setStatus("current")
_AgSyslogMsgTable_Object = MibTable
agSyslogMsgTable = _AgSyslogMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 11)
)
if mibBuilder.loadTexts:
    agSyslogMsgTable.setStatus("current")
_AgSyslogMsgTableEntry_Object = MibTableRow
agSyslogMsgTableEntry = _AgSyslogMsgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 11, 1)
)
agSyslogMsgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agSyslogMsgIndex"),
)
if mibBuilder.loadTexts:
    agSyslogMsgTableEntry.setStatus("current")
_AgSyslogMsgIndex_Type = Integer32
_AgSyslogMsgIndex_Object = MibTableColumn
agSyslogMsgIndex = _AgSyslogMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 11, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 11, 1, 2),
    _AgSyslogMessage_Type()
)
agSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSyslogMessage.setStatus("current")
_AgLog_ObjectIdentity = ObjectIdentity
agLog = _AgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 8),
    _AgCurCfgSyslogTrapCli_Type()
)
agCurCfgSyslogTrapCli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapCli.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 9),
    _AgNewCfgSyslogTrapStp_Type()
)
agNewCfgSyslogTrapStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapStp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 10),
    _AgCurCfgSyslogTrapStp_Type()
)
agCurCfgSyslogTrapStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapStp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 12),
    _AgCurCfgSyslogTrapVlan_Type()
)
agCurCfgSyslogTrapVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapVlan.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 13),
    _AgNewCfgSyslogTrapSlb_Type()
)
agNewCfgSyslogTrapSlb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSlb.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 14),
    _AgCurCfgSyslogTrapSlb_Type()
)
agCurCfgSyslogTrapSlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSlb.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 15),
    _AgNewCfgSyslogTrapGslb_Type()
)
agNewCfgSyslogTrapGslb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapGslb.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 16),
    _AgCurCfgSyslogTrapGslb_Type()
)
agCurCfgSyslogTrapGslb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapGslb.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 17),
    _AgNewCfgSyslogTrapFilter_Type()
)
agNewCfgSyslogTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapFilter.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 18),
    _AgCurCfgSyslogTrapFilter_Type()
)
agCurCfgSyslogTrapFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapFilter.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 19),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 20),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 21),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 22),
    _AgCurCfgSyslogTrapVrrp_Type()
)
agCurCfgSyslogTrapVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapVrrp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 23),
    _AgNewCfgSyslogTrapBgp_Type()
)
agNewCfgSyslogTrapBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapBgp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 24),
    _AgCurCfgSyslogTrapBgp_Type()
)
agCurCfgSyslogTrapBgp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapBgp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 25),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 26),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 31),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 32),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 35),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 36),
    _AgCurCfgSyslogTrapWeb_Type()
)
agCurCfgSyslogTrapWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapWeb.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 37),
    _AgNewCfgSyslogTrapSynAtk_Type()
)
agNewCfgSyslogTrapSynAtk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSynAtk.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 38),
    _AgCurCfgSyslogTrapSynAtk_Type()
)
agCurCfgSyslogTrapSynAtk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSynAtk.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 39),
    _AgNewCfgSyslogTrapTcpLim_Type()
)
agNewCfgSyslogTrapTcpLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapTcpLim.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 40),
    _AgCurCfgSyslogTrapTcpLim_Type()
)
agCurCfgSyslogTrapTcpLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapTcpLim.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 41),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 42),
    _AgCurCfgSyslogTrapOspf_Type()
)
agCurCfgSyslogTrapOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapOspf.setStatus("current")


class _AgNewCfgSyslogTrapSecurity_Type(Integer32):
    """Custom type agNewCfgSyslogTrapSecurity based on Integer32"""
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


_AgNewCfgSyslogTrapSecurity_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapSecurity_Object = MibScalar
agNewCfgSyslogTrapSecurity = _AgNewCfgSyslogTrapSecurity_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 43),
    _AgNewCfgSyslogTrapSecurity_Type()
)
agNewCfgSyslogTrapSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSecurity.setStatus("current")


class _AgCurCfgSyslogTrapSecurity_Type(Integer32):
    """Custom type agCurCfgSyslogTrapSecurity based on Integer32"""
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


_AgCurCfgSyslogTrapSecurity_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapSecurity_Object = MibScalar
agCurCfgSyslogTrapSecurity = _AgCurCfgSyslogTrapSecurity_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 44),
    _AgCurCfgSyslogTrapSecurity_Type()
)
agCurCfgSyslogTrapSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSecurity.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 45),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 46),
    _AgCurCfgSyslogTrapRmon_Type()
)
agCurCfgSyslogTrapRmon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapRmon.setStatus("current")


class _AgNewCfgSyslogTrapSlbAtk_Type(Integer32):
    """Custom type agNewCfgSyslogTrapSlbAtk based on Integer32"""
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


_AgNewCfgSyslogTrapSlbAtk_Type.__name__ = "Integer32"
_AgNewCfgSyslogTrapSlbAtk_Object = MibScalar
agNewCfgSyslogTrapSlbAtk = _AgNewCfgSyslogTrapSlbAtk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 47),
    _AgNewCfgSyslogTrapSlbAtk_Type()
)
agNewCfgSyslogTrapSlbAtk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslogTrapSlbAtk.setStatus("current")


class _AgCurCfgSyslogTrapSlbAtk_Type(Integer32):
    """Custom type agCurCfgSyslogTrapSlbAtk based on Integer32"""
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


_AgCurCfgSyslogTrapSlbAtk_Type.__name__ = "Integer32"
_AgCurCfgSyslogTrapSlbAtk_Object = MibScalar
agCurCfgSyslogTrapSlbAtk = _AgCurCfgSyslogTrapSlbAtk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 12, 48),
    _AgCurCfgSyslogTrapSlbAtk_Type()
)
agCurCfgSyslogTrapSlbAtk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSyslogTrapSlbAtk.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 13),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 5, 16),
    _AgNewCfgSyslog2Sev_Type()
)
agNewCfgSyslog2Sev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSyslog2Sev.setStatus("current")
_AgTrapHost_ObjectIdentity = ObjectIdentity
agTrapHost = _AgTrapHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6)
)
_AgTrapHostTableMaxEnt_Type = Integer32
_AgTrapHostTableMaxEnt_Object = MibScalar
agTrapHostTableMaxEnt = _AgTrapHostTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 1),
    _AgTrapHostTableMaxEnt_Type()
)
agTrapHostTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTrapHostTableMaxEnt.setStatus("current")
_AgCurCfgTrapHostTable_Object = MibTable
agCurCfgTrapHostTable = _AgCurCfgTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    agCurCfgTrapHostTable.setStatus("current")
_AgCurCfgTrapHostEntry_Object = MibTableRow
agCurCfgTrapHostEntry = _AgCurCfgTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 2, 1)
)
agCurCfgTrapHostEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agCurCfgTrapHostIndx"),
)
if mibBuilder.loadTexts:
    agCurCfgTrapHostEntry.setStatus("current")
_AgCurCfgTrapHostIndx_Type = Integer32
_AgCurCfgTrapHostIndx_Object = MibTableColumn
agCurCfgTrapHostIndx = _AgCurCfgTrapHostIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 2, 1, 1),
    _AgCurCfgTrapHostIndx_Type()
)
agCurCfgTrapHostIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostIndx.setStatus("current")
_AgCurCfgTrapHostIpAddr_Type = IpAddress
_AgCurCfgTrapHostIpAddr_Object = MibTableColumn
agCurCfgTrapHostIpAddr = _AgCurCfgTrapHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 2, 1, 3),
    _AgCurCfgTrapHostCommString_Type()
)
agCurCfgTrapHostCommString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgTrapHostCommString.setStatus("current")
_AgNewCfgTrapHostTable_Object = MibTable
agNewCfgTrapHostTable = _AgNewCfgTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    agNewCfgTrapHostTable.setStatus("current")
_AgNewCfgTrapHostEntry_Object = MibTableRow
agNewCfgTrapHostEntry = _AgNewCfgTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 3, 1)
)
agNewCfgTrapHostEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agNewCfgTrapHostIndx"),
)
if mibBuilder.loadTexts:
    agNewCfgTrapHostEntry.setStatus("current")
_AgNewCfgTrapHostIndx_Type = Integer32
_AgNewCfgTrapHostIndx_Object = MibTableColumn
agNewCfgTrapHostIndx = _AgNewCfgTrapHostIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 3, 1, 1),
    _AgNewCfgTrapHostIndx_Type()
)
agNewCfgTrapHostIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgTrapHostIndx.setStatus("current")
_AgNewCfgTrapHostIpAddr_Type = IpAddress
_AgNewCfgTrapHostIpAddr_Object = MibTableColumn
agNewCfgTrapHostIpAddr = _AgNewCfgTrapHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 6, 3, 1, 3),
    _AgNewCfgTrapHostCommString_Type()
)
agNewCfgTrapHostCommString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTrapHostCommString.setStatus("current")
_AgTftp_ObjectIdentity = ObjectIdentity
agTftp = _AgTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7)
)


class _AgTftpServer_Type(DisplayString):
    """Custom type agTftpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpServer_Type.__name__ = "DisplayString"
_AgTftpServer_Object = MibScalar
agTftpServer = _AgTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 5),
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
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bkpdump-put", 6),
          ("bogon-get", 9),
          ("cfg-get", 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 7),
    _AgTftpLastActionStatus_Type()
)
agTftpLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTftpLastActionStatus.setStatus("current")


class _AgTftpPort_Type(Integer32):
    """Custom type agTftpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgTftpPort_Type.__name__ = "Integer32"
_AgTftpPort_Object = MibScalar
agTftpPort = _AgTftpPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 8),
    _AgTftpPort_Type()
)
agTftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpPort.setStatus("current")


class _AgTftpUserName_Type(DisplayString):
    """Custom type agTftpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpUserName_Type.__name__ = "DisplayString"
_AgTftpUserName_Object = MibScalar
agTftpUserName = _AgTftpUserName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 7, 11),
    _AgTftpTSDumpFileName_Type()
)
agTftpTSDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpTSDumpFileName.setStatus("current")
_AgApply_ObjectIdentity = ObjectIdentity
agApply = _AgApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8, 2),
    _AgApplyConfig_Type()
)
agApplyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agApplyConfig.setStatus("current")
_AgApplyTableSize_Type = Integer32
_AgApplyTableSize_Object = MibScalar
agApplyTableSize = _AgApplyTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8, 4),
    _AgApplyTableSize_Type()
)
agApplyTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyTableSize.setStatus("current")
_AgApplyTable_Object = MibTable
agApplyTable = _AgApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    agApplyTable.setStatus("current")
_AgApplyTableEntry_Object = MibTableRow
agApplyTableEntry = _AgApplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8, 5, 1)
)
agApplyTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agApplyIndex"),
)
if mibBuilder.loadTexts:
    agApplyTableEntry.setStatus("current")
_AgApplyIndex_Type = Integer32
_AgApplyIndex_Object = MibTableColumn
agApplyIndex = _AgApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8, 5, 1, 1),
    _AgApplyIndex_Type()
)
agApplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyIndex.setStatus("current")
_AgApplyString_Type = OctetString
_AgApplyString_Object = MibTableColumn
agApplyString = _AgApplyString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 8, 5, 1, 2),
    _AgApplyString_Type()
)
agApplyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agApplyString.setStatus("current")
_AgMgmt_ObjectIdentity = ObjectIdentity
agMgmt = _AgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9)
)
_AgMgmtCurCfgIpAddr_Type = IpAddress
_AgMgmtCurCfgIpAddr_Object = MibScalar
agMgmtCurCfgIpAddr = _AgMgmtCurCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 1),
    _AgMgmtCurCfgIpAddr_Type()
)
agMgmtCurCfgIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgIpAddr.setStatus("current")
_AgMgmtNewCfgIpAddr_Type = IpAddress
_AgMgmtNewCfgIpAddr_Object = MibScalar
agMgmtNewCfgIpAddr = _AgMgmtNewCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 2),
    _AgMgmtNewCfgIpAddr_Type()
)
agMgmtNewCfgIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgIpAddr.setStatus("current")
_AgMgmtCurCfgMask_Type = IpAddress
_AgMgmtCurCfgMask_Object = MibScalar
agMgmtCurCfgMask = _AgMgmtCurCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 3),
    _AgMgmtCurCfgMask_Type()
)
agMgmtCurCfgMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgMask.setStatus("current")
_AgMgmtNewCfgMask_Type = IpAddress
_AgMgmtNewCfgMask_Object = MibScalar
agMgmtNewCfgMask = _AgMgmtNewCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 4),
    _AgMgmtNewCfgMask_Type()
)
agMgmtNewCfgMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgMask.setStatus("current")
_AgMgmtCurCfgGateway_Type = IpAddress
_AgMgmtCurCfgGateway_Object = MibScalar
agMgmtCurCfgGateway = _AgMgmtCurCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 7),
    _AgMgmtCurCfgGateway_Type()
)
agMgmtCurCfgGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgGateway.setStatus("current")
_AgMgmtNewCfgGateway_Type = IpAddress
_AgMgmtNewCfgGateway_Object = MibScalar
agMgmtNewCfgGateway = _AgMgmtNewCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 8),
    _AgMgmtNewCfgGateway_Type()
)
agMgmtNewCfgGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgGateway.setStatus("current")


class _AgMgmtCurCfgState_Type(Integer32):
    """Custom type agMgmtCurCfgState based on Integer32"""
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


_AgMgmtCurCfgState_Type.__name__ = "Integer32"
_AgMgmtCurCfgState_Object = MibScalar
agMgmtCurCfgState = _AgMgmtCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 9),
    _AgMgmtCurCfgState_Type()
)
agMgmtCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgState.setStatus("current")


class _AgMgmtNewCfgState_Type(Integer32):
    """Custom type agMgmtNewCfgState based on Integer32"""
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


_AgMgmtNewCfgState_Type.__name__ = "Integer32"
_AgMgmtNewCfgState_Object = MibScalar
agMgmtNewCfgState = _AgMgmtNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 10),
    _AgMgmtNewCfgState_Type()
)
agMgmtNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgState.setStatus("current")


class _AgMgmtCurCfgNtp_Type(Integer32):
    """Custom type agMgmtCurCfgNtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgNtp_Type.__name__ = "Integer32"
_AgMgmtCurCfgNtp_Object = MibScalar
agMgmtCurCfgNtp = _AgMgmtCurCfgNtp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 11),
    _AgMgmtCurCfgNtp_Type()
)
agMgmtCurCfgNtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgNtp.setStatus("current")


class _AgMgmtNewCfgNtp_Type(Integer32):
    """Custom type agMgmtNewCfgNtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgNtp_Type.__name__ = "Integer32"
_AgMgmtNewCfgNtp_Object = MibScalar
agMgmtNewCfgNtp = _AgMgmtNewCfgNtp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 12),
    _AgMgmtNewCfgNtp_Type()
)
agMgmtNewCfgNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgNtp.setStatus("current")


class _AgMgmtCurCfgRadius_Type(Integer32):
    """Custom type agMgmtCurCfgRadius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgRadius_Type.__name__ = "Integer32"
_AgMgmtCurCfgRadius_Object = MibScalar
agMgmtCurCfgRadius = _AgMgmtCurCfgRadius_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 13),
    _AgMgmtCurCfgRadius_Type()
)
agMgmtCurCfgRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgRadius.setStatus("current")


class _AgMgmtNewCfgRadius_Type(Integer32):
    """Custom type agMgmtNewCfgRadius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgRadius_Type.__name__ = "Integer32"
_AgMgmtNewCfgRadius_Object = MibScalar
agMgmtNewCfgRadius = _AgMgmtNewCfgRadius_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 14),
    _AgMgmtNewCfgRadius_Type()
)
agMgmtNewCfgRadius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgRadius.setStatus("current")


class _AgMgmtCurCfgSmtp_Type(Integer32):
    """Custom type agMgmtCurCfgSmtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgSmtp_Type.__name__ = "Integer32"
_AgMgmtCurCfgSmtp_Object = MibScalar
agMgmtCurCfgSmtp = _AgMgmtCurCfgSmtp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 15),
    _AgMgmtCurCfgSmtp_Type()
)
agMgmtCurCfgSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgSmtp.setStatus("current")


class _AgMgmtNewCfgSmtp_Type(Integer32):
    """Custom type agMgmtNewCfgSmtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgSmtp_Type.__name__ = "Integer32"
_AgMgmtNewCfgSmtp_Object = MibScalar
agMgmtNewCfgSmtp = _AgMgmtNewCfgSmtp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 16),
    _AgMgmtNewCfgSmtp_Type()
)
agMgmtNewCfgSmtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgSmtp.setStatus("current")


class _AgMgmtCurCfgSnmp_Type(Integer32):
    """Custom type agMgmtCurCfgSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgSnmp_Type.__name__ = "Integer32"
_AgMgmtCurCfgSnmp_Object = MibScalar
agMgmtCurCfgSnmp = _AgMgmtCurCfgSnmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 17),
    _AgMgmtCurCfgSnmp_Type()
)
agMgmtCurCfgSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgSnmp.setStatus("current")


class _AgMgmtNewCfgSnmp_Type(Integer32):
    """Custom type agMgmtNewCfgSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgSnmp_Type.__name__ = "Integer32"
_AgMgmtNewCfgSnmp_Object = MibScalar
agMgmtNewCfgSnmp = _AgMgmtNewCfgSnmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 18),
    _AgMgmtNewCfgSnmp_Type()
)
agMgmtNewCfgSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgSnmp.setStatus("current")


class _AgMgmtCurCfgSyslog_Type(Integer32):
    """Custom type agMgmtCurCfgSyslog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgSyslog_Type.__name__ = "Integer32"
_AgMgmtCurCfgSyslog_Object = MibScalar
agMgmtCurCfgSyslog = _AgMgmtCurCfgSyslog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 19),
    _AgMgmtCurCfgSyslog_Type()
)
agMgmtCurCfgSyslog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgSyslog.setStatus("current")


class _AgMgmtNewCfgSyslog_Type(Integer32):
    """Custom type agMgmtNewCfgSyslog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgSyslog_Type.__name__ = "Integer32"
_AgMgmtNewCfgSyslog_Object = MibScalar
agMgmtNewCfgSyslog = _AgMgmtNewCfgSyslog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 20),
    _AgMgmtNewCfgSyslog_Type()
)
agMgmtNewCfgSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgSyslog.setStatus("current")


class _AgMgmtCurCfgTftp_Type(Integer32):
    """Custom type agMgmtCurCfgTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgTftp_Type.__name__ = "Integer32"
_AgMgmtCurCfgTftp_Object = MibScalar
agMgmtCurCfgTftp = _AgMgmtCurCfgTftp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 21),
    _AgMgmtCurCfgTftp_Type()
)
agMgmtCurCfgTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgTftp.setStatus("current")


class _AgMgmtNewCfgTftp_Type(Integer32):
    """Custom type agMgmtNewCfgTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgTftp_Type.__name__ = "Integer32"
_AgMgmtNewCfgTftp_Object = MibScalar
agMgmtNewCfgTftp = _AgMgmtNewCfgTftp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 22),
    _AgMgmtNewCfgTftp_Type()
)
agMgmtNewCfgTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgTftp.setStatus("current")
_AgMgmtPort_ObjectIdentity = ObjectIdentity
agMgmtPort = _AgMgmtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 23)
)


class _AgMgmtPortCurCfgSpeed_Type(Integer32):
    """Custom type agMgmtPortCurCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("mbs10", 1),
          ("mbs100", 2))
    )


_AgMgmtPortCurCfgSpeed_Type.__name__ = "Integer32"
_AgMgmtPortCurCfgSpeed_Object = MibScalar
agMgmtPortCurCfgSpeed = _AgMgmtPortCurCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 23, 1),
    _AgMgmtPortCurCfgSpeed_Type()
)
agMgmtPortCurCfgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtPortCurCfgSpeed.setStatus("current")


class _AgMgmtPortNewCfgSpeed_Type(Integer32):
    """Custom type agMgmtPortNewCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("mbs10", 1),
          ("mbs100", 2))
    )


_AgMgmtPortNewCfgSpeed_Type.__name__ = "Integer32"
_AgMgmtPortNewCfgSpeed_Object = MibScalar
agMgmtPortNewCfgSpeed = _AgMgmtPortNewCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 23, 2),
    _AgMgmtPortNewCfgSpeed_Type()
)
agMgmtPortNewCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtPortNewCfgSpeed.setStatus("current")


class _AgMgmtPortCurCfgMode_Type(Integer32):
    """Custom type agMgmtPortCurCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("full", 1),
          ("half", 2))
    )


_AgMgmtPortCurCfgMode_Type.__name__ = "Integer32"
_AgMgmtPortCurCfgMode_Object = MibScalar
agMgmtPortCurCfgMode = _AgMgmtPortCurCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 23, 3),
    _AgMgmtPortCurCfgMode_Type()
)
agMgmtPortCurCfgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtPortCurCfgMode.setStatus("current")


class _AgMgmtPortNewCfgMode_Type(Integer32):
    """Custom type agMgmtPortNewCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("full", 1),
          ("half", 2))
    )


_AgMgmtPortNewCfgMode_Type.__name__ = "Integer32"
_AgMgmtPortNewCfgMode_Object = MibScalar
agMgmtPortNewCfgMode = _AgMgmtPortNewCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 23, 4),
    _AgMgmtPortNewCfgMode_Type()
)
agMgmtPortNewCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtPortNewCfgMode.setStatus("current")


class _AgMgmtPortCurCfgAuto_Type(Integer32):
    """Custom type agMgmtPortCurCfgAuto based on Integer32"""
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


_AgMgmtPortCurCfgAuto_Type.__name__ = "Integer32"
_AgMgmtPortCurCfgAuto_Object = MibScalar
agMgmtPortCurCfgAuto = _AgMgmtPortCurCfgAuto_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 23, 5),
    _AgMgmtPortCurCfgAuto_Type()
)
agMgmtPortCurCfgAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtPortCurCfgAuto.setStatus("current")


class _AgMgmtPortNewCfgAuto_Type(Integer32):
    """Custom type agMgmtPortNewCfgAuto based on Integer32"""
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


_AgMgmtPortNewCfgAuto_Type.__name__ = "Integer32"
_AgMgmtPortNewCfgAuto_Object = MibScalar
agMgmtPortNewCfgAuto = _AgMgmtPortNewCfgAuto_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 23, 6),
    _AgMgmtPortNewCfgAuto_Type()
)
agMgmtPortNewCfgAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtPortNewCfgAuto.setStatus("current")


class _AgMgmtCurCfgDns_Type(Integer32):
    """Custom type agMgmtCurCfgDns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgDns_Type.__name__ = "Integer32"
_AgMgmtCurCfgDns_Object = MibScalar
agMgmtCurCfgDns = _AgMgmtCurCfgDns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 24),
    _AgMgmtCurCfgDns_Type()
)
agMgmtCurCfgDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgDns.setStatus("current")


class _AgMgmtNewCfgDns_Type(Integer32):
    """Custom type agMgmtNewCfgDns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgDns_Type.__name__ = "Integer32"
_AgMgmtNewCfgDns_Object = MibScalar
agMgmtNewCfgDns = _AgMgmtNewCfgDns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 25),
    _AgMgmtNewCfgDns_Type()
)
agMgmtNewCfgDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgDns.setStatus("current")


class _AgMgmtCurCfgTacacs_Type(Integer32):
    """Custom type agMgmtCurCfgTacacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgTacacs_Type.__name__ = "Integer32"
_AgMgmtCurCfgTacacs_Object = MibScalar
agMgmtCurCfgTacacs = _AgMgmtCurCfgTacacs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 26),
    _AgMgmtCurCfgTacacs_Type()
)
agMgmtCurCfgTacacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgTacacs.setStatus("current")


class _AgMgmtNewCfgTacacs_Type(Integer32):
    """Custom type agMgmtNewCfgTacacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgTacacs_Type.__name__ = "Integer32"
_AgMgmtNewCfgTacacs_Object = MibScalar
agMgmtNewCfgTacacs = _AgMgmtNewCfgTacacs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 27),
    _AgMgmtNewCfgTacacs_Type()
)
agMgmtNewCfgTacacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgTacacs.setStatus("current")


class _AgMgmtCurCfgIntr_Type(Integer32):
    """Custom type agMgmtCurCfgIntr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AgMgmtCurCfgIntr_Type.__name__ = "Integer32"
_AgMgmtCurCfgIntr_Object = MibScalar
agMgmtCurCfgIntr = _AgMgmtCurCfgIntr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 28),
    _AgMgmtCurCfgIntr_Type()
)
agMgmtCurCfgIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgIntr.setStatus("current")


class _AgMgmtNewCfgIntr_Type(Integer32):
    """Custom type agMgmtNewCfgIntr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AgMgmtNewCfgIntr_Type.__name__ = "Integer32"
_AgMgmtNewCfgIntr_Object = MibScalar
agMgmtNewCfgIntr = _AgMgmtNewCfgIntr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 29),
    _AgMgmtNewCfgIntr_Type()
)
agMgmtNewCfgIntr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgIntr.setStatus("current")


class _AgMgmtCurCfgRetry_Type(Integer32):
    """Custom type agMgmtCurCfgRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AgMgmtCurCfgRetry_Type.__name__ = "Integer32"
_AgMgmtCurCfgRetry_Object = MibScalar
agMgmtCurCfgRetry = _AgMgmtCurCfgRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 30),
    _AgMgmtCurCfgRetry_Type()
)
agMgmtCurCfgRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgRetry.setStatus("current")


class _AgMgmtNewCfgRetry_Type(Integer32):
    """Custom type agMgmtNewCfgRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AgMgmtNewCfgRetry_Type.__name__ = "Integer32"
_AgMgmtNewCfgRetry_Object = MibScalar
agMgmtNewCfgRetry = _AgMgmtNewCfgRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 31),
    _AgMgmtNewCfgRetry_Type()
)
agMgmtNewCfgRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgRetry.setStatus("current")


class _AgMgmtCurCfgSonmp_Type(Integer32):
    """Custom type agMgmtCurCfgSonmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgSonmp_Type.__name__ = "Integer32"
_AgMgmtCurCfgSonmp_Object = MibScalar
agMgmtCurCfgSonmp = _AgMgmtCurCfgSonmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 32),
    _AgMgmtCurCfgSonmp_Type()
)
agMgmtCurCfgSonmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgSonmp.setStatus("current")


class _AgMgmtNewCfgSonmp_Type(Integer32):
    """Custom type agMgmtNewCfgSonmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgSonmp_Type.__name__ = "Integer32"
_AgMgmtNewCfgSonmp_Object = MibScalar
agMgmtNewCfgSonmp = _AgMgmtNewCfgSonmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 33),
    _AgMgmtNewCfgSonmp_Type()
)
agMgmtNewCfgSonmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgSonmp.setStatus("current")


class _AgMgmtCurCfgWlm_Type(Integer32):
    """Custom type agMgmtCurCfgWlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgWlm_Type.__name__ = "Integer32"
_AgMgmtCurCfgWlm_Object = MibScalar
agMgmtCurCfgWlm = _AgMgmtCurCfgWlm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 34),
    _AgMgmtCurCfgWlm_Type()
)
agMgmtCurCfgWlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgWlm.setStatus("current")


class _AgMgmtNewCfgWlm_Type(Integer32):
    """Custom type agMgmtNewCfgWlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgWlm_Type.__name__ = "Integer32"
_AgMgmtNewCfgWlm_Object = MibScalar
agMgmtNewCfgWlm = _AgMgmtNewCfgWlm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 35),
    _AgMgmtNewCfgWlm_Type()
)
agMgmtNewCfgWlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgWlm.setStatus("current")


class _AgMgmtCurCfgReport_Type(Integer32):
    """Custom type agMgmtCurCfgReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtCurCfgReport_Type.__name__ = "Integer32"
_AgMgmtCurCfgReport_Object = MibScalar
agMgmtCurCfgReport = _AgMgmtCurCfgReport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 36),
    _AgMgmtCurCfgReport_Type()
)
agMgmtCurCfgReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtCurCfgReport.setStatus("current")


class _AgMgmtNewCfgReport_Type(Integer32):
    """Custom type agMgmtNewCfgReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mgmt", 2))
    )


_AgMgmtNewCfgReport_Type.__name__ = "Integer32"
_AgMgmtNewCfgReport_Object = MibScalar
agMgmtNewCfgReport = _AgMgmtNewCfgReport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 9, 37),
    _AgMgmtNewCfgReport_Type()
)
agMgmtNewCfgReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agMgmtNewCfgReport.setStatus("current")
_AgSslproc_ObjectIdentity = ObjectIdentity
agSslproc = _AgSslproc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10)
)
_AgSslprocCurCfgIpAddr_Type = IpAddress
_AgSslprocCurCfgIpAddr_Object = MibScalar
agSslprocCurCfgIpAddr = _AgSslprocCurCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 1),
    _AgSslprocCurCfgIpAddr_Type()
)
agSslprocCurCfgIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSslprocCurCfgIpAddr.setStatus("current")
_AgSslprocNewCfgIpAddr_Type = IpAddress
_AgSslprocNewCfgIpAddr_Object = MibScalar
agSslprocNewCfgIpAddr = _AgSslprocNewCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 2),
    _AgSslprocNewCfgIpAddr_Type()
)
agSslprocNewCfgIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSslprocNewCfgIpAddr.setStatus("current")


class _AgSslprocCurCfgPort_Type(Integer32):
    """Custom type agSslprocCurCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgSslprocCurCfgPort_Type.__name__ = "Integer32"
_AgSslprocCurCfgPort_Object = MibScalar
agSslprocCurCfgPort = _AgSslprocCurCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 3),
    _AgSslprocCurCfgPort_Type()
)
agSslprocCurCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSslprocCurCfgPort.setStatus("current")


class _AgSslprocNewCfgPort_Type(Integer32):
    """Custom type agSslprocNewCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgSslprocNewCfgPort_Type.__name__ = "Integer32"
_AgSslprocNewCfgPort_Object = MibScalar
agSslprocNewCfgPort = _AgSslprocNewCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 4),
    _AgSslprocNewCfgPort_Type()
)
agSslprocNewCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSslprocNewCfgPort.setStatus("current")


class _AgSslprocCurCfgRts_Type(Integer32):
    """Custom type agSslprocCurCfgRts based on Integer32"""
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


_AgSslprocCurCfgRts_Type.__name__ = "Integer32"
_AgSslprocCurCfgRts_Object = MibScalar
agSslprocCurCfgRts = _AgSslprocCurCfgRts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 5),
    _AgSslprocCurCfgRts_Type()
)
agSslprocCurCfgRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSslprocCurCfgRts.setStatus("current")


class _AgSslprocNewCfgRts_Type(Integer32):
    """Custom type agSslprocNewCfgRts based on Integer32"""
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


_AgSslprocNewCfgRts_Type.__name__ = "Integer32"
_AgSslprocNewCfgRts_Object = MibScalar
agSslprocNewCfgRts = _AgSslprocNewCfgRts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 6),
    _AgSslprocNewCfgRts_Type()
)
agSslprocNewCfgRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSslprocNewCfgRts.setStatus("current")


class _AgSslprocCurCfgFilt_Type(Integer32):
    """Custom type agSslprocCurCfgFilt based on Integer32"""
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


_AgSslprocCurCfgFilt_Type.__name__ = "Integer32"
_AgSslprocCurCfgFilt_Object = MibScalar
agSslprocCurCfgFilt = _AgSslprocCurCfgFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 7),
    _AgSslprocCurCfgFilt_Type()
)
agSslprocCurCfgFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSslprocCurCfgFilt.setStatus("current")


class _AgSslprocNewCfgFilt_Type(Integer32):
    """Custom type agSslprocNewCfgFilt based on Integer32"""
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


_AgSslprocNewCfgFilt_Type.__name__ = "Integer32"
_AgSslprocNewCfgFilt_Object = MibScalar
agSslprocNewCfgFilt = _AgSslprocNewCfgFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 10, 8),
    _AgSslprocNewCfgFilt_Type()
)
agSslprocNewCfgFilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSslprocNewCfgFilt.setStatus("current")
_AgTacacsConfig_ObjectIdentity = ObjectIdentity
agTacacsConfig = _AgTacacsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11)
)
_TacCurCfgPrimaryIpAddr_Type = IpAddress
_TacCurCfgPrimaryIpAddr_Object = MibScalar
tacCurCfgPrimaryIpAddr = _TacCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 1),
    _TacCurCfgPrimaryIpAddr_Type()
)
tacCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgPrimaryIpAddr.setStatus("current")
_TacNewCfgPrimaryIpAddr_Type = IpAddress
_TacNewCfgPrimaryIpAddr_Object = MibScalar
tacNewCfgPrimaryIpAddr = _TacNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 2),
    _TacNewCfgPrimaryIpAddr_Type()
)
tacNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgPrimaryIpAddr.setStatus("current")
_TacCurCfgSecondaryIpAddr_Type = IpAddress
_TacCurCfgSecondaryIpAddr_Object = MibScalar
tacCurCfgSecondaryIpAddr = _TacCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 3),
    _TacCurCfgSecondaryIpAddr_Type()
)
tacCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgSecondaryIpAddr.setStatus("current")
_TacNewCfgSecondaryIpAddr_Type = IpAddress
_TacNewCfgSecondaryIpAddr_Object = MibScalar
tacNewCfgSecondaryIpAddr = _TacNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 12),
    _TacNewCfgState_Type()
)
tacNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgState.setStatus("current")


class _TacCurCfgAuthenString_Type(DisplayString):
    """Custom type tacCurCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TacCurCfgAuthenString_Type.__name__ = "DisplayString"
_TacCurCfgAuthenString_Object = MibScalar
tacCurCfgAuthenString = _TacCurCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 13),
    _TacCurCfgAuthenString_Type()
)
tacCurCfgAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgAuthenString.setStatus("current")


class _TacNewCfgAuthenString_Type(DisplayString):
    """Custom type tacNewCfgAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TacNewCfgAuthenString_Type.__name__ = "DisplayString"
_TacNewCfgAuthenString_Object = MibScalar
tacNewCfgAuthenString = _TacNewCfgAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 16),
    _TacNewCfgTelnet_Type()
)
tacNewCfgTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgTelnet.setStatus("current")


class _TacCurCfgAuthenSecondString_Type(DisplayString):
    """Custom type tacCurCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TacCurCfgAuthenSecondString_Type.__name__ = "DisplayString"
_TacCurCfgAuthenSecondString_Object = MibScalar
tacCurCfgAuthenSecondString = _TacCurCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 17),
    _TacCurCfgAuthenSecondString_Type()
)
tacCurCfgAuthenSecondString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacCurCfgAuthenSecondString.setStatus("current")


class _TacNewCfgAuthenSecondString_Type(DisplayString):
    """Custom type tacNewCfgAuthenSecondString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TacNewCfgAuthenSecondString_Type.__name__ = "DisplayString"
_TacNewCfgAuthenSecondString_Object = MibScalar
tacNewCfgAuthenSecondString = _TacNewCfgAuthenSecondString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 18),
    _TacNewCfgAuthenSecondString_Type()
)
tacNewCfgAuthenSecondString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgAuthenSecondString.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 25),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 11, 26),
    _TacNewCfgCmap_Type()
)
tacNewCfgCmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacNewCfgCmap.setStatus("current")
_AgMgmtNetConfig_ObjectIdentity = ObjectIdentity
agMgmtNetConfig = _AgMgmtNetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12)
)
_AgMgmtNetTableMaxSize_Type = Integer32
_AgMgmtNetTableMaxSize_Object = MibScalar
agMgmtNetTableMaxSize = _AgMgmtNetTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 1),
    _AgMgmtNetTableMaxSize_Type()
)
agMgmtNetTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMgmtNetTableMaxSize.setStatus("current")
_AgCurCfgMgmtNetTable_Object = MibTable
agCurCfgMgmtNetTable = _AgCurCfgMgmtNetTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    agCurCfgMgmtNetTable.setStatus("current")
_AgCurCfgMgmtNetEntry_Object = MibTableRow
agCurCfgMgmtNetEntry = _AgCurCfgMgmtNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 2, 1)
)
agCurCfgMgmtNetEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agCurCfgMgmtNetIndex"),
)
if mibBuilder.loadTexts:
    agCurCfgMgmtNetEntry.setStatus("current")
_AgCurCfgMgmtNetIndex_Type = Integer32
_AgCurCfgMgmtNetIndex_Object = MibTableColumn
agCurCfgMgmtNetIndex = _AgCurCfgMgmtNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 2, 1, 1),
    _AgCurCfgMgmtNetIndex_Type()
)
agCurCfgMgmtNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtNetIndex.setStatus("current")
_AgCurCfgMgmtNetSubnet_Type = IpAddress
_AgCurCfgMgmtNetSubnet_Object = MibTableColumn
agCurCfgMgmtNetSubnet = _AgCurCfgMgmtNetSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 2, 1, 2),
    _AgCurCfgMgmtNetSubnet_Type()
)
agCurCfgMgmtNetSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtNetSubnet.setStatus("current")
_AgCurCfgMgmtNetMask_Type = IpAddress
_AgCurCfgMgmtNetMask_Object = MibTableColumn
agCurCfgMgmtNetMask = _AgCurCfgMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 2, 1, 3),
    _AgCurCfgMgmtNetMask_Type()
)
agCurCfgMgmtNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgMgmtNetMask.setStatus("current")
_AgNewCfgMgmtNetTable_Object = MibTable
agNewCfgMgmtNetTable = _AgNewCfgMgmtNetTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 3)
)
if mibBuilder.loadTexts:
    agNewCfgMgmtNetTable.setStatus("current")
_AgNewCfgMgmtNetEntry_Object = MibTableRow
agNewCfgMgmtNetEntry = _AgNewCfgMgmtNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 3, 1)
)
agNewCfgMgmtNetEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agNewCfgMgmtNetIndex"),
)
if mibBuilder.loadTexts:
    agNewCfgMgmtNetEntry.setStatus("current")
_AgNewCfgMgmtNetIndex_Type = Integer32
_AgNewCfgMgmtNetIndex_Object = MibTableColumn
agNewCfgMgmtNetIndex = _AgNewCfgMgmtNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 3, 1, 1),
    _AgNewCfgMgmtNetIndex_Type()
)
agNewCfgMgmtNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetIndex.setStatus("current")
_AgNewCfgMgmtNetSubnet_Type = IpAddress
_AgNewCfgMgmtNetSubnet_Object = MibTableColumn
agNewCfgMgmtNetSubnet = _AgNewCfgMgmtNetSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 3, 1, 2),
    _AgNewCfgMgmtNetSubnet_Type()
)
agNewCfgMgmtNetSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetSubnet.setStatus("current")
_AgNewCfgMgmtNetMask_Type = IpAddress
_AgNewCfgMgmtNetMask_Object = MibTableColumn
agNewCfgMgmtNetMask = _AgNewCfgMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 12, 3, 1, 4),
    _AgNewCfgMgmtNetDelete_Type()
)
agNewCfgMgmtNetDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgMgmtNetDelete.setStatus("current")
_AgBoot_ObjectIdentity = ObjectIdentity
agBoot = _AgBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 13)
)


class _AgCfgBootWeekday_Type(Integer32):
    """Custom type agCfgBootWeekday based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_AgCfgBootWeekday_Type.__name__ = "Integer32"
_AgCfgBootWeekday_Object = MibScalar
agCfgBootWeekday = _AgCfgBootWeekday_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 13, 1),
    _AgCfgBootWeekday_Type()
)
agCfgBootWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agCfgBootWeekday.setStatus("current")


class _AgCfgBootHour_Type(Integer32):
    """Custom type agCfgBootHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgCfgBootHour_Type.__name__ = "Integer32"
_AgCfgBootHour_Object = MibScalar
agCfgBootHour = _AgCfgBootHour_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 13, 2),
    _AgCfgBootHour_Type()
)
agCfgBootHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agCfgBootHour.setStatus("current")


class _AgCfgBootMin_Type(Integer32):
    """Custom type agCfgBootMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgCfgBootMin_Type.__name__ = "Integer32"
_AgCfgBootMin_Object = MibScalar
agCfgBootMin = _AgCfgBootMin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 13, 3),
    _AgCfgBootMin_Type()
)
agCfgBootMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agCfgBootMin.setStatus("current")


class _AgCfgBootReset_Type(Integer32):
    """Custom type agCfgBootReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("none", 1))
    )


_AgCfgBootReset_Type.__name__ = "Integer32"
_AgCfgBootReset_Object = MibScalar
agCfgBootReset = _AgCfgBootReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 13, 4),
    _AgCfgBootReset_Type()
)
agCfgBootReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agCfgBootReset.setStatus("current")


class _AgCfgBootNxtResetTime_Type(DisplayString):
    """Custom type agCfgBootNxtResetTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgCfgBootNxtResetTime_Type.__name__ = "DisplayString"
_AgCfgBootNxtResetTime_Object = MibScalar
agCfgBootNxtResetTime = _AgCfgBootNxtResetTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 13, 5),
    _AgCfgBootNxtResetTime_Type()
)
agCfgBootNxtResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgBootNxtResetTime.setStatus("current")
_AgSecurity_ObjectIdentity = ObjectIdentity
agSecurity = _AgSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14)
)
_AgPgroup_ObjectIdentity = ObjectIdentity
agPgroup = _AgPgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1)
)
_AgPgrpMatchTableMaxSize_Type = Integer32
_AgPgrpMatchTableMaxSize_Object = MibScalar
agPgrpMatchTableMaxSize = _AgPgrpMatchTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 1),
    _AgPgrpMatchTableMaxSize_Type()
)
agPgrpMatchTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPgrpMatchTableMaxSize.setStatus("current")
_AgCurCfgPgrpMatchTable_Object = MibTable
agCurCfgPgrpMatchTable = _AgCurCfgPgrpMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    agCurCfgPgrpMatchTable.setStatus("current")
_AgCurCfgPgrpMatchEntry_Object = MibTableRow
agCurCfgPgrpMatchEntry = _AgCurCfgPgrpMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 2, 1)
)
agCurCfgPgrpMatchEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agCurCfgPgrpMatchIndex"),
)
if mibBuilder.loadTexts:
    agCurCfgPgrpMatchEntry.setStatus("current")
_AgCurCfgPgrpMatchIndex_Type = Integer32
_AgCurCfgPgrpMatchIndex_Object = MibTableColumn
agCurCfgPgrpMatchIndex = _AgCurCfgPgrpMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 2, 1, 1),
    _AgCurCfgPgrpMatchIndex_Type()
)
agCurCfgPgrpMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgPgrpMatchIndex.setStatus("current")


class _AgCurCfgPgrpName_Type(DisplayString):
    """Custom type agCurCfgPgrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgCurCfgPgrpName_Type.__name__ = "DisplayString"
_AgCurCfgPgrpName_Object = MibTableColumn
agCurCfgPgrpName = _AgCurCfgPgrpName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 2, 1, 2),
    _AgCurCfgPgrpName_Type()
)
agCurCfgPgrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgPgrpName.setStatus("current")
_AgCurCfgPgrpMatchBmap_Type = OctetString
_AgCurCfgPgrpMatchBmap_Object = MibTableColumn
agCurCfgPgrpMatchBmap = _AgCurCfgPgrpMatchBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 2, 1, 3),
    _AgCurCfgPgrpMatchBmap_Type()
)
agCurCfgPgrpMatchBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgPgrpMatchBmap.setStatus("current")
_AgNewCfgPgrpMatchTable_Object = MibTable
agNewCfgPgrpMatchTable = _AgNewCfgPgrpMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    agNewCfgPgrpMatchTable.setStatus("current")
_AgNewCfgPgrpMatchEntry_Object = MibTableRow
agNewCfgPgrpMatchEntry = _AgNewCfgPgrpMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3, 1)
)
agNewCfgPgrpMatchEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agNewCfgPgrpMatchIndex"),
)
if mibBuilder.loadTexts:
    agNewCfgPgrpMatchEntry.setStatus("current")
_AgNewCfgPgrpMatchIndex_Type = Integer32
_AgNewCfgPgrpMatchIndex_Object = MibTableColumn
agNewCfgPgrpMatchIndex = _AgNewCfgPgrpMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3, 1, 1),
    _AgNewCfgPgrpMatchIndex_Type()
)
agNewCfgPgrpMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgPgrpMatchIndex.setStatus("current")


class _AgNewCfgPgrpName_Type(DisplayString):
    """Custom type agNewCfgPgrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgNewCfgPgrpName_Type.__name__ = "DisplayString"
_AgNewCfgPgrpName_Object = MibTableColumn
agNewCfgPgrpName = _AgNewCfgPgrpName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3, 1, 2),
    _AgNewCfgPgrpName_Type()
)
agNewCfgPgrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgPgrpName.setStatus("current")
_AgNewCfgPgrpMatchAdd_Type = Integer32
_AgNewCfgPgrpMatchAdd_Object = MibTableColumn
agNewCfgPgrpMatchAdd = _AgNewCfgPgrpMatchAdd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3, 1, 3),
    _AgNewCfgPgrpMatchAdd_Type()
)
agNewCfgPgrpMatchAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgPgrpMatchAdd.setStatus("current")
_AgNewCfgPgrpMatchRem_Type = Integer32
_AgNewCfgPgrpMatchRem_Object = MibTableColumn
agNewCfgPgrpMatchRem = _AgNewCfgPgrpMatchRem_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3, 1, 4),
    _AgNewCfgPgrpMatchRem_Type()
)
agNewCfgPgrpMatchRem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgPgrpMatchRem.setStatus("current")
_AgNewCfgPgrpMatchBmap_Type = OctetString
_AgNewCfgPgrpMatchBmap_Object = MibTableColumn
agNewCfgPgrpMatchBmap = _AgNewCfgPgrpMatchBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3, 1, 5),
    _AgNewCfgPgrpMatchBmap_Type()
)
agNewCfgPgrpMatchBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgPgrpMatchBmap.setStatus("current")


class _AgNewCfgPgrpDelete_Type(Integer32):
    """Custom type agNewCfgPgrpDelete based on Integer32"""
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


_AgNewCfgPgrpDelete_Type.__name__ = "Integer32"
_AgNewCfgPgrpDelete_Object = MibTableColumn
agNewCfgPgrpDelete = _AgNewCfgPgrpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 1, 3, 1, 6),
    _AgNewCfgPgrpDelete_Type()
)
agNewCfgPgrpDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agNewCfgPgrpDelete.setStatus("current")
_AgCfgSecurityPortTable_Object = MibTable
agCfgSecurityPortTable = _AgCfgSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    agCfgSecurityPortTable.setStatus("current")
_AgCfgSecurityPortTableEntry_Object = MibTableRow
agCfgSecurityPortTableEntry = _AgCfgSecurityPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1)
)
agCfgSecurityPortTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agCfgSecurityPortIndx"),
)
if mibBuilder.loadTexts:
    agCfgSecurityPortTableEntry.setStatus("current")
_AgCfgSecurityPortIndx_Type = Integer32
_AgCfgSecurityPortIndx_Object = MibTableColumn
agCfgSecurityPortIndx = _AgCfgSecurityPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 1),
    _AgCfgSecurityPortIndx_Type()
)
agCfgSecurityPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgSecurityPortIndx.setStatus("current")


class _AgCurCfgSecurityDosState_Type(Integer32):
    """Custom type agCurCfgSecurityDosState based on Integer32"""
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


_AgCurCfgSecurityDosState_Type.__name__ = "Integer32"
_AgCurCfgSecurityDosState_Object = MibTableColumn
agCurCfgSecurityDosState = _AgCurCfgSecurityDosState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 2),
    _AgCurCfgSecurityDosState_Type()
)
agCurCfgSecurityDosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSecurityDosState.setStatus("current")


class _AgNewCfgSecurityDosState_Type(Integer32):
    """Custom type agNewCfgSecurityDosState based on Integer32"""
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


_AgNewCfgSecurityDosState_Type.__name__ = "Integer32"
_AgNewCfgSecurityDosState_Object = MibTableColumn
agNewCfgSecurityDosState = _AgNewCfgSecurityDosState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 3),
    _AgNewCfgSecurityDosState_Type()
)
agNewCfgSecurityDosState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecurityDosState.setStatus("current")


class _AgCurCfgSecurityIpAclState_Type(Integer32):
    """Custom type agCurCfgSecurityIpAclState based on Integer32"""
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


_AgCurCfgSecurityIpAclState_Type.__name__ = "Integer32"
_AgCurCfgSecurityIpAclState_Object = MibTableColumn
agCurCfgSecurityIpAclState = _AgCurCfgSecurityIpAclState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 4),
    _AgCurCfgSecurityIpAclState_Type()
)
agCurCfgSecurityIpAclState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSecurityIpAclState.setStatus("current")


class _AgNewCfgSecurityIpAclState_Type(Integer32):
    """Custom type agNewCfgSecurityIpAclState based on Integer32"""
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


_AgNewCfgSecurityIpAclState_Type.__name__ = "Integer32"
_AgNewCfgSecurityIpAclState_Object = MibTableColumn
agNewCfgSecurityIpAclState = _AgNewCfgSecurityIpAclState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 5),
    _AgNewCfgSecurityIpAclState_Type()
)
agNewCfgSecurityIpAclState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecurityIpAclState.setStatus("current")


class _AgCurCfgSecurityUbState_Type(Integer32):
    """Custom type agCurCfgSecurityUbState based on Integer32"""
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


_AgCurCfgSecurityUbState_Type.__name__ = "Integer32"
_AgCurCfgSecurityUbState_Object = MibTableColumn
agCurCfgSecurityUbState = _AgCurCfgSecurityUbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 6),
    _AgCurCfgSecurityUbState_Type()
)
agCurCfgSecurityUbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSecurityUbState.setStatus("current")


class _AgNewCfgSecurityUbState_Type(Integer32):
    """Custom type agNewCfgSecurityUbState based on Integer32"""
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


_AgNewCfgSecurityUbState_Type.__name__ = "Integer32"
_AgNewCfgSecurityUbState_Object = MibTableColumn
agNewCfgSecurityUbState = _AgNewCfgSecurityUbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 7),
    _AgNewCfgSecurityUbState_Type()
)
agNewCfgSecurityUbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecurityUbState.setStatus("current")


class _AgCurCfgSecurityBogonState_Type(Integer32):
    """Custom type agCurCfgSecurityBogonState based on Integer32"""
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


_AgCurCfgSecurityBogonState_Type.__name__ = "Integer32"
_AgCurCfgSecurityBogonState_Object = MibTableColumn
agCurCfgSecurityBogonState = _AgCurCfgSecurityBogonState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 8),
    _AgCurCfgSecurityBogonState_Type()
)
agCurCfgSecurityBogonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSecurityBogonState.setStatus("current")


class _AgNewCfgSecurityBogonState_Type(Integer32):
    """Custom type agNewCfgSecurityBogonState based on Integer32"""
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


_AgNewCfgSecurityBogonState_Type.__name__ = "Integer32"
_AgNewCfgSecurityBogonState_Object = MibTableColumn
agNewCfgSecurityBogonState = _AgNewCfgSecurityBogonState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 9),
    _AgNewCfgSecurityBogonState_Type()
)
agNewCfgSecurityBogonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecurityBogonState.setStatus("current")
_AgCurCfgSecurityAttacksBmap_Type = OctetString
_AgCurCfgSecurityAttacksBmap_Object = MibTableColumn
agCurCfgSecurityAttacksBmap = _AgCurCfgSecurityAttacksBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 10),
    _AgCurCfgSecurityAttacksBmap_Type()
)
agCurCfgSecurityAttacksBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSecurityAttacksBmap.setStatus("current")
_AgNewCfgSecurityAttacksBmap_Type = OctetString
_AgNewCfgSecurityAttacksBmap_Object = MibTableColumn
agNewCfgSecurityAttacksBmap = _AgNewCfgSecurityAttacksBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 11),
    _AgNewCfgSecurityAttacksBmap_Type()
)
agNewCfgSecurityAttacksBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgSecurityAttacksBmap.setStatus("current")


class _AgNewCfgSecurityAddAttack_Type(Integer32):
    """Custom type agNewCfgSecurityAddAttack based on Integer32"""
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
              56)
        )
    )
    namedValues = NamedValues(
        *(("ackzero", 34),
          ("arplen", 50),
          ("arpnbcast", 51),
          ("arpnucast", 52),
          ("arpspoof", 53),
          ("blat", 20),
          ("broadcast", 3),
          ("dnsport", 32),
          ("finscan", 24),
          ("flagabnormal", 28),
          ("fragboundary", 12),
          ("fragdata", 11),
          ("fragdontoff", 14),
          ("fraggle", 38),
          ("fraglast", 13),
          ("fragmoredont", 10),
          ("fragoff", 16),
          ("fragopt", 15),
          ("fragoversize", 17),
          ("ftpport", 31),
          ("fullxmasscan", 23),
          ("garp", 54),
          ("icmpdata", 44),
          ("icmplen", 42),
          ("icmpoff", 45),
          ("icmptype", 46),
          ("igmpfrag", 48),
          ("igmplen", 47),
          ("igmptype", 49),
          ("ip6len", 55),
          ("ip6version", 56),
          ("iplen", 1),
          ("ipoptlen", 9),
          ("ipprot", 8),
          ("ipreserved", 6),
          ("ipttl", 7),
          ("ipversion", 2),
          ("land", 5),
          ("loopback", 4),
          ("nullscan", 22),
          ("pepsi", 39),
          ("rc8", 40),
          ("seqzero", 33),
          ("smurf", 43),
          ("snmpnull", 41),
          ("syndata", 29),
          ("synfinscan", 27),
          ("synfrag", 30),
          ("tcplen", 18),
          ("tcpoptlen", 35),
          ("tcpportzero", 19),
          ("tcpreserved", 21),
          ("udplen", 36),
          ("udpportzero", 37),
          ("vecnascan", 25),
          ("xmassscan", 26))
    )


_AgNewCfgSecurityAddAttack_Type.__name__ = "Integer32"
_AgNewCfgSecurityAddAttack_Object = MibTableColumn
agNewCfgSecurityAddAttack = _AgNewCfgSecurityAddAttack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 12),
    _AgNewCfgSecurityAddAttack_Type()
)
agNewCfgSecurityAddAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecurityAddAttack.setStatus("current")


class _AgNewCfgSecurityRemAttack_Type(Integer32):
    """Custom type agNewCfgSecurityRemAttack based on Integer32"""
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
              56)
        )
    )
    namedValues = NamedValues(
        *(("ackzero", 34),
          ("arplen", 50),
          ("arpnbcast", 51),
          ("arpnucast", 52),
          ("arpspoof", 53),
          ("blat", 20),
          ("broadcast", 3),
          ("dnsport", 32),
          ("finscan", 24),
          ("flagabnormal", 28),
          ("fragboundary", 12),
          ("fragdata", 11),
          ("fragdontoff", 14),
          ("fraggle", 38),
          ("fraglast", 13),
          ("fragmoredont", 10),
          ("fragoff", 16),
          ("fragopt", 15),
          ("fragoversize", 17),
          ("ftpport", 31),
          ("fullxmasscan", 23),
          ("garp", 54),
          ("icmpdata", 44),
          ("icmplen", 42),
          ("icmpoff", 45),
          ("icmptype", 46),
          ("igmpfrag", 48),
          ("igmplen", 47),
          ("igmptype", 49),
          ("ip6len", 55),
          ("ip6version", 56),
          ("iplen", 1),
          ("ipoptlen", 9),
          ("ipprot", 8),
          ("ipreserved", 6),
          ("ipttl", 7),
          ("ipversion", 2),
          ("land", 5),
          ("loopback", 4),
          ("nullscan", 22),
          ("pepsi", 39),
          ("rc8", 40),
          ("seqzero", 33),
          ("smurf", 43),
          ("snmpnull", 41),
          ("syndata", 29),
          ("synfinscan", 27),
          ("synfrag", 30),
          ("tcplen", 18),
          ("tcpoptlen", 35),
          ("tcpportzero", 19),
          ("tcpreserved", 21),
          ("udplen", 36),
          ("udpportzero", 37),
          ("vecnascan", 25),
          ("xmassscan", 26))
    )


_AgNewCfgSecurityRemAttack_Type.__name__ = "Integer32"
_AgNewCfgSecurityRemAttack_Object = MibTableColumn
agNewCfgSecurityRemAttack = _AgNewCfgSecurityRemAttack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 13),
    _AgNewCfgSecurityRemAttack_Type()
)
agNewCfgSecurityRemAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecurityRemAttack.setStatus("current")


class _AgNewCfgSecurityDoSAttacks_Type(Integer32):
    """Custom type agNewCfgSecurityDoSAttacks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addall", 2),
          ("ok", 1),
          ("remall", 3))
    )


_AgNewCfgSecurityDoSAttacks_Type.__name__ = "Integer32"
_AgNewCfgSecurityDoSAttacks_Object = MibTableColumn
agNewCfgSecurityDoSAttacks = _AgNewCfgSecurityDoSAttacks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 14),
    _AgNewCfgSecurityDoSAttacks_Type()
)
agNewCfgSecurityDoSAttacks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecurityDoSAttacks.setStatus("current")


class _AgCurCfgSecuritySymantecState_Type(Integer32):
    """Custom type agCurCfgSecuritySymantecState based on Integer32"""
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


_AgCurCfgSecuritySymantecState_Type.__name__ = "Integer32"
_AgCurCfgSecuritySymantecState_Object = MibTableColumn
agCurCfgSecuritySymantecState = _AgCurCfgSecuritySymantecState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 15),
    _AgCurCfgSecuritySymantecState_Type()
)
agCurCfgSecuritySymantecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSecuritySymantecState.setStatus("current")


class _AgNewCfgSecuritySymantecState_Type(Integer32):
    """Custom type agNewCfgSecuritySymantecState based on Integer32"""
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


_AgNewCfgSecuritySymantecState_Type.__name__ = "Integer32"
_AgNewCfgSecuritySymantecState_Object = MibTableColumn
agNewCfgSecuritySymantecState = _AgNewCfgSecuritySymantecState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 2, 1, 16),
    _AgNewCfgSecuritySymantecState_Type()
)
agNewCfgSecuritySymantecState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSecuritySymantecState.setStatus("current")
_IpAclCfg_ObjectIdentity = ObjectIdentity
ipAclCfg = _IpAclCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3)
)
_IpAclTableMaxSize_Type = Integer32
_IpAclTableMaxSize_Object = MibScalar
ipAclTableMaxSize = _IpAclTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 1),
    _IpAclTableMaxSize_Type()
)
ipAclTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclTableMaxSize.setStatus("current")
_IpAclCurCfgTable_Object = MibTable
ipAclCurCfgTable = _IpAclCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 2)
)
if mibBuilder.loadTexts:
    ipAclCurCfgTable.setStatus("current")
_IpAclCurCfgEntry_Object = MibTableRow
ipAclCurCfgEntry = _IpAclCurCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 2, 1)
)
ipAclCurCfgEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "ipAclCurCfgIndx"),
)
if mibBuilder.loadTexts:
    ipAclCurCfgEntry.setStatus("current")
_IpAclCurCfgIndx_Type = Integer32
_IpAclCurCfgIndx_Object = MibTableColumn
ipAclCurCfgIndx = _IpAclCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 2, 1, 1),
    _IpAclCurCfgIndx_Type()
)
ipAclCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclCurCfgIndx.setStatus("current")
_IpAclCurCfgIp_Type = IpAddress
_IpAclCurCfgIp_Object = MibTableColumn
ipAclCurCfgIp = _IpAclCurCfgIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 2, 1, 2),
    _IpAclCurCfgIp_Type()
)
ipAclCurCfgIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclCurCfgIp.setStatus("current")
_IpAclCurCfgMask_Type = IpAddress
_IpAclCurCfgMask_Object = MibTableColumn
ipAclCurCfgMask = _IpAclCurCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 2, 1, 3),
    _IpAclCurCfgMask_Type()
)
ipAclCurCfgMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclCurCfgMask.setStatus("current")
_IpAclNewCfgTable_Object = MibTable
ipAclNewCfgTable = _IpAclNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 3)
)
if mibBuilder.loadTexts:
    ipAclNewCfgTable.setStatus("current")
_IpAclNewCfgEntry_Object = MibTableRow
ipAclNewCfgEntry = _IpAclNewCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 3, 1)
)
ipAclNewCfgEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "ipAclNewCfgIndx"),
)
if mibBuilder.loadTexts:
    ipAclNewCfgEntry.setStatus("current")
_IpAclNewCfgIndx_Type = Integer32
_IpAclNewCfgIndx_Object = MibTableColumn
ipAclNewCfgIndx = _IpAclNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 3, 1, 1),
    _IpAclNewCfgIndx_Type()
)
ipAclNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclNewCfgIndx.setStatus("current")
_IpAclNewCfgIp_Type = IpAddress
_IpAclNewCfgIp_Object = MibTableColumn
ipAclNewCfgIp = _IpAclNewCfgIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 3, 1, 2),
    _IpAclNewCfgIp_Type()
)
ipAclNewCfgIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAclNewCfgIp.setStatus("current")


class _IpAclNewCfgAction_Type(Integer32):
    """Custom type ipAclNewCfgAction based on Integer32"""
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


_IpAclNewCfgAction_Type.__name__ = "Integer32"
_IpAclNewCfgAction_Object = MibTableColumn
ipAclNewCfgAction = _IpAclNewCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 3, 1, 3),
    _IpAclNewCfgAction_Type()
)
ipAclNewCfgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAclNewCfgAction.setStatus("current")
_IpAclNewCfgMask_Type = IpAddress
_IpAclNewCfgMask_Object = MibTableColumn
ipAclNewCfgMask = _IpAclNewCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 3, 3, 1, 4),
    _IpAclNewCfgMask_Type()
)
ipAclNewCfgMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAclNewCfgMask.setStatus("current")
_UdpBlastCfg_ObjectIdentity = ObjectIdentity
udpBlastCfg = _UdpBlastCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4)
)
_UdpBlastudpPortTableMaxSize_Type = Integer32
_UdpBlastudpPortTableMaxSize_Object = MibScalar
udpBlastudpPortTableMaxSize = _UdpBlastudpPortTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 1),
    _UdpBlastudpPortTableMaxSize_Type()
)
udpBlastudpPortTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastudpPortTableMaxSize.setStatus("current")


class _UdpBlastCurCfgudpPortPacketLimit_Type(Integer32):
    """Custom type udpBlastCurCfgudpPortPacketLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000000),
    )


_UdpBlastCurCfgudpPortPacketLimit_Type.__name__ = "Integer32"
_UdpBlastCurCfgudpPortPacketLimit_Object = MibScalar
udpBlastCurCfgudpPortPacketLimit = _UdpBlastCurCfgudpPortPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 2),
    _UdpBlastCurCfgudpPortPacketLimit_Type()
)
udpBlastCurCfgudpPortPacketLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastCurCfgudpPortPacketLimit.setStatus("current")
_UdpBlastCurCfgudpPortTable_Object = MibTable
udpBlastCurCfgudpPortTable = _UdpBlastCurCfgudpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 3)
)
if mibBuilder.loadTexts:
    udpBlastCurCfgudpPortTable.setStatus("current")
_UdpBlastCurCfgudpPortEntry_Object = MibTableRow
udpBlastCurCfgudpPortEntry = _UdpBlastCurCfgudpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 3, 1)
)
udpBlastCurCfgudpPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "udpBlastCurCfgudpPortLowIndx"),
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "udpBlastCurCfgudpPortHighIndx"),
)
if mibBuilder.loadTexts:
    udpBlastCurCfgudpPortEntry.setStatus("current")


class _UdpBlastCurCfgudpPortLowIndx_Type(Integer32):
    """Custom type udpBlastCurCfgudpPortLowIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UdpBlastCurCfgudpPortLowIndx_Type.__name__ = "Integer32"
_UdpBlastCurCfgudpPortLowIndx_Object = MibTableColumn
udpBlastCurCfgudpPortLowIndx = _UdpBlastCurCfgudpPortLowIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 3, 1, 1),
    _UdpBlastCurCfgudpPortLowIndx_Type()
)
udpBlastCurCfgudpPortLowIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastCurCfgudpPortLowIndx.setStatus("current")


class _UdpBlastCurCfgudpPortHighIndx_Type(Integer32):
    """Custom type udpBlastCurCfgudpPortHighIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UdpBlastCurCfgudpPortHighIndx_Type.__name__ = "Integer32"
_UdpBlastCurCfgudpPortHighIndx_Object = MibTableColumn
udpBlastCurCfgudpPortHighIndx = _UdpBlastCurCfgudpPortHighIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 3, 1, 2),
    _UdpBlastCurCfgudpPortHighIndx_Type()
)
udpBlastCurCfgudpPortHighIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastCurCfgudpPortHighIndx.setStatus("current")


class _UdpBlastCurCfgudpPortEntryPacketLimit_Type(Integer32):
    """Custom type udpBlastCurCfgudpPortEntryPacketLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000000),
    )


_UdpBlastCurCfgudpPortEntryPacketLimit_Type.__name__ = "Integer32"
_UdpBlastCurCfgudpPortEntryPacketLimit_Object = MibTableColumn
udpBlastCurCfgudpPortEntryPacketLimit = _UdpBlastCurCfgudpPortEntryPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 3, 1, 3),
    _UdpBlastCurCfgudpPortEntryPacketLimit_Type()
)
udpBlastCurCfgudpPortEntryPacketLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastCurCfgudpPortEntryPacketLimit.setStatus("current")


class _UdpBlastNewCfgudpPortPacketLimit_Type(Integer32):
    """Custom type udpBlastNewCfgudpPortPacketLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000000),
    )


_UdpBlastNewCfgudpPortPacketLimit_Type.__name__ = "Integer32"
_UdpBlastNewCfgudpPortPacketLimit_Object = MibScalar
udpBlastNewCfgudpPortPacketLimit = _UdpBlastNewCfgudpPortPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 4),
    _UdpBlastNewCfgudpPortPacketLimit_Type()
)
udpBlastNewCfgudpPortPacketLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpBlastNewCfgudpPortPacketLimit.setStatus("current")
_UdpBlastNewCfgudpPortTable_Object = MibTable
udpBlastNewCfgudpPortTable = _UdpBlastNewCfgudpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 5)
)
if mibBuilder.loadTexts:
    udpBlastNewCfgudpPortTable.setStatus("current")
_UdpBlastNewCfgudpPortEntry_Object = MibTableRow
udpBlastNewCfgudpPortEntry = _UdpBlastNewCfgudpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 5, 1)
)
udpBlastNewCfgudpPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "udpBlastNewCfgudpPortLowIndx"),
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "udpBlastNewCfgudpPortHighIndx"),
)
if mibBuilder.loadTexts:
    udpBlastNewCfgudpPortEntry.setStatus("current")


class _UdpBlastNewCfgudpPortLowIndx_Type(Integer32):
    """Custom type udpBlastNewCfgudpPortLowIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UdpBlastNewCfgudpPortLowIndx_Type.__name__ = "Integer32"
_UdpBlastNewCfgudpPortLowIndx_Object = MibTableColumn
udpBlastNewCfgudpPortLowIndx = _UdpBlastNewCfgudpPortLowIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 5, 1, 1),
    _UdpBlastNewCfgudpPortLowIndx_Type()
)
udpBlastNewCfgudpPortLowIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastNewCfgudpPortLowIndx.setStatus("current")


class _UdpBlastNewCfgudpPortHighIndx_Type(Integer32):
    """Custom type udpBlastNewCfgudpPortHighIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UdpBlastNewCfgudpPortHighIndx_Type.__name__ = "Integer32"
_UdpBlastNewCfgudpPortHighIndx_Object = MibTableColumn
udpBlastNewCfgudpPortHighIndx = _UdpBlastNewCfgudpPortHighIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 5, 1, 2),
    _UdpBlastNewCfgudpPortHighIndx_Type()
)
udpBlastNewCfgudpPortHighIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastNewCfgudpPortHighIndx.setStatus("current")


class _UdpBlastNewCfgudpPortEntryDelete_Type(Integer32):
    """Custom type udpBlastNewCfgudpPortEntryDelete based on Integer32"""
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


_UdpBlastNewCfgudpPortEntryDelete_Type.__name__ = "Integer32"
_UdpBlastNewCfgudpPortEntryDelete_Object = MibTableColumn
udpBlastNewCfgudpPortEntryDelete = _UdpBlastNewCfgudpPortEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 5, 1, 3),
    _UdpBlastNewCfgudpPortEntryDelete_Type()
)
udpBlastNewCfgudpPortEntryDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    udpBlastNewCfgudpPortEntryDelete.setStatus("current")


class _UdpBlastNewCfgudpPortEntryPacketLimit_Type(Integer32):
    """Custom type udpBlastNewCfgudpPortEntryPacketLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000000),
    )


_UdpBlastNewCfgudpPortEntryPacketLimit_Type.__name__ = "Integer32"
_UdpBlastNewCfgudpPortEntryPacketLimit_Object = MibTableColumn
udpBlastNewCfgudpPortEntryPacketLimit = _UdpBlastNewCfgudpPortEntryPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 4, 5, 1, 4),
    _UdpBlastNewCfgudpPortEntryPacketLimit_Type()
)
udpBlastNewCfgudpPortEntryPacketLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    udpBlastNewCfgudpPortEntryPacketLimit.setStatus("current")
_SecGeneralCfg_ObjectIdentity = ObjectIdentity
secGeneralCfg = _SecGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5)
)


class _SecCurCfgSecurityLogThreshold_Type(Integer32):
    """Custom type secCurCfgSecurityLogThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_SecCurCfgSecurityLogThreshold_Type.__name__ = "Integer32"
_SecCurCfgSecurityLogThreshold_Object = MibScalar
secCurCfgSecurityLogThreshold = _SecCurCfgSecurityLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 1),
    _SecCurCfgSecurityLogThreshold_Type()
)
secCurCfgSecurityLogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secCurCfgSecurityLogThreshold.setStatus("current")


class _SecNewCfgSecurityLogThreshold_Type(Integer32):
    """Custom type secNewCfgSecurityLogThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_SecNewCfgSecurityLogThreshold_Type.__name__ = "Integer32"
_SecNewCfgSecurityLogThreshold_Object = MibScalar
secNewCfgSecurityLogThreshold = _SecNewCfgSecurityLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 2),
    _SecNewCfgSecurityLogThreshold_Type()
)
secNewCfgSecurityLogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secNewCfgSecurityLogThreshold.setStatus("current")


class _SecCurCfgPacketDepth_Type(Integer32):
    """Custom type secCurCfgPacketDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SecCurCfgPacketDepth_Type.__name__ = "Integer32"
_SecCurCfgPacketDepth_Object = MibScalar
secCurCfgPacketDepth = _SecCurCfgPacketDepth_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 5),
    _SecCurCfgPacketDepth_Type()
)
secCurCfgPacketDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secCurCfgPacketDepth.setStatus("current")


class _SecNewCfgPacketDepth_Type(Integer32):
    """Custom type secNewCfgPacketDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SecNewCfgPacketDepth_Type.__name__ = "Integer32"
_SecNewCfgPacketDepth_Object = MibScalar
secNewCfgPacketDepth = _SecNewCfgPacketDepth_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 6),
    _SecNewCfgPacketDepth_Type()
)
secNewCfgPacketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secNewCfgPacketDepth.setStatus("current")
_SecCurCfgIpAclSyslogThreshold_Type = Integer32
_SecCurCfgIpAclSyslogThreshold_Object = MibScalar
secCurCfgIpAclSyslogThreshold = _SecCurCfgIpAclSyslogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 7),
    _SecCurCfgIpAclSyslogThreshold_Type()
)
secCurCfgIpAclSyslogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secCurCfgIpAclSyslogThreshold.setStatus("current")
_SecNewCfgIpAclSyslogThreshold_Type = Integer32
_SecNewCfgIpAclSyslogThreshold_Object = MibScalar
secNewCfgIpAclSyslogThreshold = _SecNewCfgIpAclSyslogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 8),
    _SecNewCfgIpAclSyslogThreshold_Type()
)
secNewCfgIpAclSyslogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secNewCfgIpAclSyslogThreshold.setStatus("current")
_SecCurCfgIpAclSyslogTime_Type = Integer32
_SecCurCfgIpAclSyslogTime_Object = MibScalar
secCurCfgIpAclSyslogTime = _SecCurCfgIpAclSyslogTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 9),
    _SecCurCfgIpAclSyslogTime_Type()
)
secCurCfgIpAclSyslogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secCurCfgIpAclSyslogTime.setStatus("current")
_SecNewCfgIpAclSyslogTime_Type = Integer32
_SecNewCfgIpAclSyslogTime_Object = MibScalar
secNewCfgIpAclSyslogTime = _SecNewCfgIpAclSyslogTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 5, 10),
    _SecNewCfgIpAclSyslogTime_Type()
)
secNewCfgIpAclSyslogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secNewCfgIpAclSyslogTime.setStatus("current")
_DosAttackPrevCfg_ObjectIdentity = ObjectIdentity
dosAttackPrevCfg = _DosAttackPrevCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6)
)


class _DosCurCfgIPTTL_Type(Integer32):
    """Custom type dosCurCfgIPTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DosCurCfgIPTTL_Type.__name__ = "Integer32"
_DosCurCfgIPTTL_Object = MibScalar
dosCurCfgIPTTL = _DosCurCfgIPTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 1),
    _DosCurCfgIPTTL_Type()
)
dosCurCfgIPTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosCurCfgIPTTL.setStatus("current")


class _DosNewCfgIPTTL_Type(Integer32):
    """Custom type dosNewCfgIPTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DosNewCfgIPTTL_Type.__name__ = "Integer32"
_DosNewCfgIPTTL_Object = MibScalar
dosNewCfgIPTTL = _DosNewCfgIPTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 2),
    _DosNewCfgIPTTL_Type()
)
dosNewCfgIPTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosNewCfgIPTTL.setStatus("current")


class _DosCurCfgIPProt_Type(Integer32):
    """Custom type dosCurCfgIPProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DosCurCfgIPProt_Type.__name__ = "Integer32"
_DosCurCfgIPProt_Object = MibScalar
dosCurCfgIPProt = _DosCurCfgIPProt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 3),
    _DosCurCfgIPProt_Type()
)
dosCurCfgIPProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosCurCfgIPProt.setStatus("current")


class _DosNewCfgIPProt_Type(Integer32):
    """Custom type dosNewCfgIPProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DosNewCfgIPProt_Type.__name__ = "Integer32"
_DosNewCfgIPProt_Object = MibScalar
dosNewCfgIPProt = _DosNewCfgIPProt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 4),
    _DosNewCfgIPProt_Type()
)
dosNewCfgIPProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosNewCfgIPProt.setStatus("current")


class _DosCurCfgFragdata_Type(Integer32):
    """Custom type dosCurCfgFragdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 248),
    )


_DosCurCfgFragdata_Type.__name__ = "Integer32"
_DosCurCfgFragdata_Object = MibScalar
dosCurCfgFragdata = _DosCurCfgFragdata_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 5),
    _DosCurCfgFragdata_Type()
)
dosCurCfgFragdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosCurCfgFragdata.setStatus("current")


class _DosNewCfgFragdata_Type(Integer32):
    """Custom type dosNewCfgFragdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 248),
    )


_DosNewCfgFragdata_Type.__name__ = "Integer32"
_DosNewCfgFragdata_Object = MibScalar
dosNewCfgFragdata = _DosNewCfgFragdata_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 6),
    _DosNewCfgFragdata_Type()
)
dosNewCfgFragdata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosNewCfgFragdata.setStatus("current")


class _DosCurCfgFragoff_Type(Integer32):
    """Custom type dosCurCfgFragoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 248),
    )


_DosCurCfgFragoff_Type.__name__ = "Integer32"
_DosCurCfgFragoff_Object = MibScalar
dosCurCfgFragoff = _DosCurCfgFragoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 7),
    _DosCurCfgFragoff_Type()
)
dosCurCfgFragoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosCurCfgFragoff.setStatus("current")


class _DosNewCfgFragoff_Type(Integer32):
    """Custom type dosNewCfgFragoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 248),
    )


_DosNewCfgFragoff_Type.__name__ = "Integer32"
_DosNewCfgFragoff_Object = MibScalar
dosNewCfgFragoff = _DosNewCfgFragoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 8),
    _DosNewCfgFragoff_Type()
)
dosNewCfgFragoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosNewCfgFragoff.setStatus("current")


class _DosCurCfgSYNdata_Type(Integer32):
    """Custom type dosCurCfgSYNdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DosCurCfgSYNdata_Type.__name__ = "Integer32"
_DosCurCfgSYNdata_Object = MibScalar
dosCurCfgSYNdata = _DosCurCfgSYNdata_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 9),
    _DosCurCfgSYNdata_Type()
)
dosCurCfgSYNdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosCurCfgSYNdata.setStatus("current")


class _DosNewCfgSYNdata_Type(Integer32):
    """Custom type dosNewCfgSYNdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DosNewCfgSYNdata_Type.__name__ = "Integer32"
_DosNewCfgSYNdata_Object = MibScalar
dosNewCfgSYNdata = _DosNewCfgSYNdata_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 10),
    _DosNewCfgSYNdata_Type()
)
dosNewCfgSYNdata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosNewCfgSYNdata.setStatus("current")


class _DosCurCfgICMPdata_Type(Integer32):
    """Custom type dosCurCfgICMPdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9026),
    )


_DosCurCfgICMPdata_Type.__name__ = "Integer32"
_DosCurCfgICMPdata_Object = MibScalar
dosCurCfgICMPdata = _DosCurCfgICMPdata_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 11),
    _DosCurCfgICMPdata_Type()
)
dosCurCfgICMPdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosCurCfgICMPdata.setStatus("current")


class _DosNewCfgICMPdata_Type(Integer32):
    """Custom type dosNewCfgICMPdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9026),
    )


_DosNewCfgICMPdata_Type.__name__ = "Integer32"
_DosNewCfgICMPdata_Object = MibScalar
dosNewCfgICMPdata = _DosNewCfgICMPdata_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 12),
    _DosNewCfgICMPdata_Type()
)
dosNewCfgICMPdata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosNewCfgICMPdata.setStatus("current")


class _DosCurCfgICMPoff_Type(Integer32):
    """Custom type dosCurCfgICMPoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8190),
    )


_DosCurCfgICMPoff_Type.__name__ = "Integer32"
_DosCurCfgICMPoff_Object = MibScalar
dosCurCfgICMPoff = _DosCurCfgICMPoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 13),
    _DosCurCfgICMPoff_Type()
)
dosCurCfgICMPoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosCurCfgICMPoff.setStatus("current")


class _DosNewCfgICMPoff_Type(Integer32):
    """Custom type dosNewCfgICMPoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8190),
    )


_DosNewCfgICMPoff_Type.__name__ = "Integer32"
_DosNewCfgICMPoff_Object = MibScalar
dosNewCfgICMPoff = _DosNewCfgICMPoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 6, 14),
    _DosNewCfgICMPoff_Type()
)
dosNewCfgICMPoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosNewCfgICMPoff.setStatus("current")
_IpDstAclCfg_ObjectIdentity = ObjectIdentity
ipDstAclCfg = _IpDstAclCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7)
)
_IpDstAclTableMaxSize_Type = Integer32
_IpDstAclTableMaxSize_Object = MibScalar
ipDstAclTableMaxSize = _IpDstAclTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 1),
    _IpDstAclTableMaxSize_Type()
)
ipDstAclTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDstAclTableMaxSize.setStatus("current")
_IpDstAclCurCfgTable_Object = MibTable
ipDstAclCurCfgTable = _IpDstAclCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 2)
)
if mibBuilder.loadTexts:
    ipDstAclCurCfgTable.setStatus("current")
_IpDstAclCurCfgEntry_Object = MibTableRow
ipDstAclCurCfgEntry = _IpDstAclCurCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 2, 1)
)
ipDstAclCurCfgEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "ipDstAclCurCfgIndx"),
)
if mibBuilder.loadTexts:
    ipDstAclCurCfgEntry.setStatus("current")
_IpDstAclCurCfgIndx_Type = Integer32
_IpDstAclCurCfgIndx_Object = MibTableColumn
ipDstAclCurCfgIndx = _IpDstAclCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 2, 1, 1),
    _IpDstAclCurCfgIndx_Type()
)
ipDstAclCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDstAclCurCfgIndx.setStatus("current")
_IpDstAclCurCfgIp_Type = IpAddress
_IpDstAclCurCfgIp_Object = MibTableColumn
ipDstAclCurCfgIp = _IpDstAclCurCfgIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 2, 1, 2),
    _IpDstAclCurCfgIp_Type()
)
ipDstAclCurCfgIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDstAclCurCfgIp.setStatus("current")
_IpDstAclCurCfgMask_Type = IpAddress
_IpDstAclCurCfgMask_Object = MibTableColumn
ipDstAclCurCfgMask = _IpDstAclCurCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 2, 1, 3),
    _IpDstAclCurCfgMask_Type()
)
ipDstAclCurCfgMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDstAclCurCfgMask.setStatus("current")
_IpDstAclNewCfgTable_Object = MibTable
ipDstAclNewCfgTable = _IpDstAclNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 3)
)
if mibBuilder.loadTexts:
    ipDstAclNewCfgTable.setStatus("current")
_IpDstAclNewCfgEntry_Object = MibTableRow
ipDstAclNewCfgEntry = _IpDstAclNewCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 3, 1)
)
ipDstAclNewCfgEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "ipDstAclNewCfgIndx"),
)
if mibBuilder.loadTexts:
    ipDstAclNewCfgEntry.setStatus("current")
_IpDstAclNewCfgIndx_Type = Integer32
_IpDstAclNewCfgIndx_Object = MibTableColumn
ipDstAclNewCfgIndx = _IpDstAclNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 3, 1, 1),
    _IpDstAclNewCfgIndx_Type()
)
ipDstAclNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDstAclNewCfgIndx.setStatus("current")
_IpDstAclNewCfgIp_Type = IpAddress
_IpDstAclNewCfgIp_Object = MibTableColumn
ipDstAclNewCfgIp = _IpDstAclNewCfgIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 3, 1, 2),
    _IpDstAclNewCfgIp_Type()
)
ipDstAclNewCfgIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipDstAclNewCfgIp.setStatus("current")


class _IpDstAclNewCfgAction_Type(Integer32):
    """Custom type ipDstAclNewCfgAction based on Integer32"""
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


_IpDstAclNewCfgAction_Type.__name__ = "Integer32"
_IpDstAclNewCfgAction_Object = MibTableColumn
ipDstAclNewCfgAction = _IpDstAclNewCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 3, 1, 3),
    _IpDstAclNewCfgAction_Type()
)
ipDstAclNewCfgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipDstAclNewCfgAction.setStatus("current")
_IpDstAclNewCfgMask_Type = IpAddress
_IpDstAclNewCfgMask_Object = MibTableColumn
ipDstAclNewCfgMask = _IpDstAclNewCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 7, 3, 1, 4),
    _IpDstAclNewCfgMask_Type()
)
ipDstAclNewCfgMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipDstAclNewCfgMask.setStatus("current")
_SymantecCfg_ObjectIdentity = ObjectIdentity
symantecCfg = _SymantecCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8)
)
_SymSigBwmMappingTableMaxSize_Type = Integer32
_SymSigBwmMappingTableMaxSize_Object = MibScalar
symSigBwmMappingTableMaxSize = _SymSigBwmMappingTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 1),
    _SymSigBwmMappingTableMaxSize_Type()
)
symSigBwmMappingTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symSigBwmMappingTableMaxSize.setStatus("current")
_SymCurCfgSigBwmMappingTable_Object = MibTable
symCurCfgSigBwmMappingTable = _SymCurCfgSigBwmMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 2)
)
if mibBuilder.loadTexts:
    symCurCfgSigBwmMappingTable.setStatus("current")
_SymCurCfgSigBwmMappingTableEntry_Object = MibTableRow
symCurCfgSigBwmMappingTableEntry = _SymCurCfgSigBwmMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 2, 1)
)
symCurCfgSigBwmMappingTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symCurCfgTblIndex"),
)
if mibBuilder.loadTexts:
    symCurCfgSigBwmMappingTableEntry.setStatus("current")
_SymCurCfgTblIndex_Type = Integer32
_SymCurCfgTblIndex_Object = MibTableColumn
symCurCfgTblIndex = _SymCurCfgTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 2, 1, 1),
    _SymCurCfgTblIndex_Type()
)
symCurCfgTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symCurCfgTblIndex.setStatus("current")
_SymCurCfgSignatureID_Type = Integer32
_SymCurCfgSignatureID_Object = MibTableColumn
symCurCfgSignatureID = _SymCurCfgSignatureID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 2, 1, 2),
    _SymCurCfgSignatureID_Type()
)
symCurCfgSignatureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symCurCfgSignatureID.setStatus("current")
_SymCurCfgInContractID_Type = Integer32
_SymCurCfgInContractID_Object = MibTableColumn
symCurCfgInContractID = _SymCurCfgInContractID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 2, 1, 3),
    _SymCurCfgInContractID_Type()
)
symCurCfgInContractID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symCurCfgInContractID.setStatus("current")
_SymCurCfgOutContractID_Type = Integer32
_SymCurCfgOutContractID_Object = MibTableColumn
symCurCfgOutContractID = _SymCurCfgOutContractID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 2, 1, 4),
    _SymCurCfgOutContractID_Type()
)
symCurCfgOutContractID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symCurCfgOutContractID.setStatus("current")
_SymNewCfgSigBwmMappingTable_Object = MibTable
symNewCfgSigBwmMappingTable = _SymNewCfgSigBwmMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 3)
)
if mibBuilder.loadTexts:
    symNewCfgSigBwmMappingTable.setStatus("current")
_SymNewCfgSigBwmMappingTableEntry_Object = MibTableRow
symNewCfgSigBwmMappingTableEntry = _SymNewCfgSigBwmMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 3, 1)
)
symNewCfgSigBwmMappingTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symNewCfgTblIndex"),
)
if mibBuilder.loadTexts:
    symNewCfgSigBwmMappingTableEntry.setStatus("current")
_SymNewCfgTblIndex_Type = Integer32
_SymNewCfgTblIndex_Object = MibTableColumn
symNewCfgTblIndex = _SymNewCfgTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 3, 1, 1),
    _SymNewCfgTblIndex_Type()
)
symNewCfgTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symNewCfgTblIndex.setStatus("current")
_SymNewCfgSignatureID_Type = Integer32
_SymNewCfgSignatureID_Object = MibTableColumn
symNewCfgSignatureID = _SymNewCfgSignatureID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 3, 1, 2),
    _SymNewCfgSignatureID_Type()
)
symNewCfgSignatureID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    symNewCfgSignatureID.setStatus("current")
_SymNewCfgInContractID_Type = Integer32
_SymNewCfgInContractID_Object = MibTableColumn
symNewCfgInContractID = _SymNewCfgInContractID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 3, 1, 3),
    _SymNewCfgInContractID_Type()
)
symNewCfgInContractID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    symNewCfgInContractID.setStatus("current")
_SymNewCfgOutContractID_Type = Integer32
_SymNewCfgOutContractID_Object = MibTableColumn
symNewCfgOutContractID = _SymNewCfgOutContractID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 3, 1, 4),
    _SymNewCfgOutContractID_Type()
)
symNewCfgOutContractID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    symNewCfgOutContractID.setStatus("current")


class _SymNewCfgDeleteEntry_Type(Integer32):
    """Custom type symNewCfgDeleteEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("others", 1))
    )


_SymNewCfgDeleteEntry_Type.__name__ = "Integer32"
_SymNewCfgDeleteEntry_Object = MibTableColumn
symNewCfgDeleteEntry = _SymNewCfgDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 3, 1, 5),
    _SymNewCfgDeleteEntry_Type()
)
symNewCfgDeleteEntry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    symNewCfgDeleteEntry.setStatus("current")


class _SymNewCfgDefaultAction_Type(Integer32):
    """Custom type symNewCfgDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_SymNewCfgDefaultAction_Type.__name__ = "Integer32"
_SymNewCfgDefaultAction_Object = MibScalar
symNewCfgDefaultAction = _SymNewCfgDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 4),
    _SymNewCfgDefaultAction_Type()
)
symNewCfgDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    symNewCfgDefaultAction.setStatus("current")


class _SymCurCfgDefaultAction_Type(Integer32):
    """Custom type symCurCfgDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_SymCurCfgDefaultAction_Type.__name__ = "Integer32"
_SymCurCfgDefaultAction_Object = MibScalar
symCurCfgDefaultAction = _SymCurCfgDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 5),
    _SymCurCfgDefaultAction_Type()
)
symCurCfgDefaultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symCurCfgDefaultAction.setStatus("current")
_SymSigFileVersionSeqNumber_Type = Integer32
_SymSigFileVersionSeqNumber_Object = MibScalar
symSigFileVersionSeqNumber = _SymSigFileVersionSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 14, 8, 6),
    _SymSigFileVersionSeqNumber_Type()
)
symSigFileVersionSeqNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    symSigFileVersionSeqNumber.setStatus("current")
_AgSonmp_ObjectIdentity = ObjectIdentity
agSonmp = _AgSonmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 15)
)
_AgCurCfgSonmpSrcIf_Type = Integer32
_AgCurCfgSonmpSrcIf_Object = MibScalar
agCurCfgSonmpSrcIf = _AgCurCfgSonmpSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 15, 1),
    _AgCurCfgSonmpSrcIf_Type()
)
agCurCfgSonmpSrcIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgSonmpSrcIf.setStatus("current")
_AgNewCfgSonmpSrcIf_Type = Integer32
_AgNewCfgSonmpSrcIf_Object = MibScalar
agNewCfgSonmpSrcIf = _AgNewCfgSonmpSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 15, 2),
    _AgNewCfgSonmpSrcIf_Type()
)
agNewCfgSonmpSrcIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgSonmpSrcIf.setStatus("current")
_AgPortAccessCfg_ObjectIdentity = ObjectIdentity
agPortAccessCfg = _AgPortAccessCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16)
)
_AgPortAccessTableMaxSize_Type = Integer32
_AgPortAccessTableMaxSize_Object = MibScalar
agPortAccessTableMaxSize = _AgPortAccessTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 1),
    _AgPortAccessTableMaxSize_Type()
)
agPortAccessTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortAccessTableMaxSize.setStatus("current")
_AgCurCfgPortAccessTable_Object = MibTable
agCurCfgPortAccessTable = _AgCurCfgPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 2)
)
if mibBuilder.loadTexts:
    agCurCfgPortAccessTable.setStatus("current")
_AgCurCfgPortAccessEntry_Object = MibTableRow
agCurCfgPortAccessEntry = _AgCurCfgPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 2, 1)
)
agCurCfgPortAccessEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agCurCfgPortAccessIndex"),
)
if mibBuilder.loadTexts:
    agCurCfgPortAccessEntry.setStatus("current")
_AgCurCfgPortAccessIndex_Type = Integer32
_AgCurCfgPortAccessIndex_Object = MibTableColumn
agCurCfgPortAccessIndex = _AgCurCfgPortAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 2, 1, 1),
    _AgCurCfgPortAccessIndex_Type()
)
agCurCfgPortAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgPortAccessIndex.setStatus("current")


class _AgCurCfgPortAccessState_Type(Integer32):
    """Custom type agCurCfgPortAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 0))
    )


_AgCurCfgPortAccessState_Type.__name__ = "Integer32"
_AgCurCfgPortAccessState_Object = MibTableColumn
agCurCfgPortAccessState = _AgCurCfgPortAccessState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 2, 1, 2),
    _AgCurCfgPortAccessState_Type()
)
agCurCfgPortAccessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCurCfgPortAccessState.setStatus("current")
_AgNewCfgPortAccessTable_Object = MibTable
agNewCfgPortAccessTable = _AgNewCfgPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 3)
)
if mibBuilder.loadTexts:
    agNewCfgPortAccessTable.setStatus("current")
_AgNewCfgPortAccessEntry_Object = MibTableRow
agNewCfgPortAccessEntry = _AgNewCfgPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 3, 1)
)
agNewCfgPortAccessEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agNewCfgPortAccessIndex"),
)
if mibBuilder.loadTexts:
    agNewCfgPortAccessEntry.setStatus("current")
_AgNewCfgPortAccessIndex_Type = Integer32
_AgNewCfgPortAccessIndex_Object = MibTableColumn
agNewCfgPortAccessIndex = _AgNewCfgPortAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 3, 1, 1),
    _AgNewCfgPortAccessIndex_Type()
)
agNewCfgPortAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agNewCfgPortAccessIndex.setStatus("current")


class _AgNewCfgPortAccessState_Type(Integer32):
    """Custom type agNewCfgPortAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 0))
    )


_AgNewCfgPortAccessState_Type.__name__ = "Integer32"
_AgNewCfgPortAccessState_Object = MibTableColumn
agNewCfgPortAccessState = _AgNewCfgPortAccessState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 16, 3, 1, 2),
    _AgNewCfgPortAccessState_Type()
)
agNewCfgPortAccessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgPortAccessState.setStatus("current")
_AgSave_ObjectIdentity = ObjectIdentity
agSave = _AgSave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 17)
)


class _AgSaveConfig_Type(Integer32):
    """Custom type agSaveConfig based on Integer32"""
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
        *(("complete", 4),
          ("failed", 5),
          ("idle", 2),
          ("inprogress", 3),
          ("save", 1),
          ("saveNoBackup", 6))
    )


_AgSaveConfig_Type.__name__ = "Integer32"
_AgSaveConfig_Object = MibScalar
agSaveConfig = _AgSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 17, 1),
    _AgSaveConfig_Type()
)
agSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSaveConfig.setStatus("current")
_AgSaveTableSize_Type = Integer32
_AgSaveTableSize_Object = MibScalar
agSaveTableSize = _AgSaveTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 17, 2),
    _AgSaveTableSize_Type()
)
agSaveTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSaveTableSize.setStatus("current")
_AgSaveTable_Object = MibTable
agSaveTable = _AgSaveTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 17, 3)
)
if mibBuilder.loadTexts:
    agSaveTable.setStatus("current")
_AgSaveTableEntry_Object = MibTableRow
agSaveTableEntry = _AgSaveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 17, 3, 1)
)
agSaveTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agSaveIndex"),
)
if mibBuilder.loadTexts:
    agSaveTableEntry.setStatus("current")
_AgSaveIndex_Type = Integer32
_AgSaveIndex_Object = MibTableColumn
agSaveIndex = _AgSaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 17, 3, 1, 1),
    _AgSaveIndex_Type()
)
agSaveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSaveIndex.setStatus("current")
_AgSaveString_Type = OctetString
_AgSaveString_Object = MibTableColumn
agSaveString = _AgSaveString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 17, 3, 1, 2),
    _AgSaveString_Type()
)
agSaveString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSaveString.setStatus("current")
_AgFileTransfer_ObjectIdentity = ObjectIdentity
agFileTransfer = _AgFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18)
)
_AgFileSize_Type = Integer32
_AgFileSize_Object = MibScalar
agFileSize = _AgFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 1),
    _AgFileSize_Type()
)
agFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agFileSize.setStatus("current")


class _AgFileTransferState_Type(Integer32):
    """Custom type agFileTransferState based on Integer32"""
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
        *(("complete", 5),
          ("endoftransfer", 7),
          ("error", 6),
          ("idle", 1),
          ("inprogress", 3),
          ("missingrows", 4),
          ("transfer", 2))
    )


_AgFileTransferState_Type.__name__ = "Integer32"
_AgFileTransferState_Object = MibScalar
agFileTransferState = _AgFileTransferState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 2),
    _AgFileTransferState_Type()
)
agFileTransferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agFileTransferState.setStatus("current")


class _AgFileTableMissingRows_Type(OctetString):
    """Custom type agFileTableMissingRows based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AgFileTableMissingRows_Type.__name__ = "OctetString"
_AgFileTableMissingRows_Object = MibScalar
agFileTableMissingRows = _AgFileTableMissingRows_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 3),
    _AgFileTableMissingRows_Type()
)
agFileTableMissingRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agFileTableMissingRows.setStatus("current")


class _AgFileType_Type(Integer32):
    """Custom type agFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bogon", 1),
          ("symantecSignature", 2))
    )


_AgFileType_Type.__name__ = "Integer32"
_AgFileType_Object = MibScalar
agFileType = _AgFileType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 4),
    _AgFileType_Type()
)
agFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agFileType.setStatus("current")
_AgFileTableSize_Type = Integer32
_AgFileTableSize_Object = MibScalar
agFileTableSize = _AgFileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 5),
    _AgFileTableSize_Type()
)
agFileTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agFileTableSize.setStatus("current")
_AgFileTable_Object = MibTable
agFileTable = _AgFileTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 6)
)
if mibBuilder.loadTexts:
    agFileTable.setStatus("current")
_AgFileTableEntry_Object = MibTableRow
agFileTableEntry = _AgFileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 6, 1)
)
agFileTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agFileIndex"),
)
if mibBuilder.loadTexts:
    agFileTableEntry.setStatus("current")
_AgFileIndex_Type = Integer32
_AgFileIndex_Object = MibTableColumn
agFileIndex = _AgFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 6, 1, 1),
    _AgFileIndex_Type()
)
agFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agFileIndex.setStatus("current")


class _AgFileString_Type(OctetString):
    """Custom type agFileString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AgFileString_Type.__name__ = "OctetString"
_AgFileString_Object = MibTableColumn
agFileString = _AgFileString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 6, 1, 2),
    _AgFileString_Type()
)
agFileString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agFileString.setStatus("current")
_AgFileErrorTableSize_Type = Integer32
_AgFileErrorTableSize_Object = MibScalar
agFileErrorTableSize = _AgFileErrorTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 7),
    _AgFileErrorTableSize_Type()
)
agFileErrorTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agFileErrorTableSize.setStatus("current")
_AgFileErrorTable_Object = MibTable
agFileErrorTable = _AgFileErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 8)
)
if mibBuilder.loadTexts:
    agFileErrorTable.setStatus("current")
_AgFileErrorTableEntry_Object = MibTableRow
agFileErrorTableEntry = _AgFileErrorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 8, 1)
)
agFileErrorTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agFileErrorIndex"),
)
if mibBuilder.loadTexts:
    agFileErrorTableEntry.setStatus("current")
_AgFileErrorIndex_Type = Integer32
_AgFileErrorIndex_Object = MibTableColumn
agFileErrorIndex = _AgFileErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 8, 1, 1),
    _AgFileErrorIndex_Type()
)
agFileErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agFileErrorIndex.setStatus("current")
_AgFileErrorString_Type = DisplayString
_AgFileErrorString_Object = MibTableColumn
agFileErrorString = _AgFileErrorString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 1, 18, 8, 1, 2),
    _AgFileErrorString_Type()
)
agFileErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agFileErrorString.setStatus("current")
_AgentStats_ObjectIdentity = ObjectIdentity
agentStats = _AgentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2)
)
_PktStats_ObjectIdentity = ObjectIdentity
pktStats = _PktStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1)
)
_PktStatsAllocs_Type = Counter32
_PktStatsAllocs_Object = MibScalar
pktStatsAllocs = _PktStatsAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 1),
    _PktStatsAllocs_Type()
)
pktStatsAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsAllocs.setStatus("current")
_PktStatsFrees_Type = Counter32
_PktStatsFrees_Object = MibScalar
pktStatsFrees = _PktStatsFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 2),
    _PktStatsFrees_Type()
)
pktStatsFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsFrees.setStatus("current")
_PktStatsAllocFails_Type = Counter32
_PktStatsAllocFails_Object = MibScalar
pktStatsAllocFails = _PktStatsAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 3),
    _PktStatsAllocFails_Type()
)
pktStatsAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsAllocFails.setStatus("current")
_PktStatsMediums_Type = Gauge32
_PktStatsMediums_Object = MibScalar
pktStatsMediums = _PktStatsMediums_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 4),
    _PktStatsMediums_Type()
)
pktStatsMediums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsMediums.setStatus("current")
_PktStatsJumbos_Type = Gauge32
_PktStatsJumbos_Object = MibScalar
pktStatsJumbos = _PktStatsJumbos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 5),
    _PktStatsJumbos_Type()
)
pktStatsJumbos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsJumbos.setStatus("current")
_PktStatsSmalls_Type = Gauge32
_PktStatsSmalls_Object = MibScalar
pktStatsSmalls = _PktStatsSmalls_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 6),
    _PktStatsSmalls_Type()
)
pktStatsSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsSmalls.setStatus("current")
_PktStatsMediumsHiWatermark_Type = Counter32
_PktStatsMediumsHiWatermark_Object = MibScalar
pktStatsMediumsHiWatermark = _PktStatsMediumsHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 7),
    _PktStatsMediumsHiWatermark_Type()
)
pktStatsMediumsHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsMediumsHiWatermark.setStatus("current")
_PktStatsJumbosHiWatermark_Type = Counter32
_PktStatsJumbosHiWatermark_Object = MibScalar
pktStatsJumbosHiWatermark = _PktStatsJumbosHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 8),
    _PktStatsJumbosHiWatermark_Type()
)
pktStatsJumbosHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsJumbosHiWatermark.setStatus("current")
_PktStatsSmallsHiWatermark_Type = Counter32
_PktStatsSmallsHiWatermark_Object = MibScalar
pktStatsSmallsHiWatermark = _PktStatsSmallsHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 9),
    _PktStatsSmallsHiWatermark_Type()
)
pktStatsSmallsHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsSmallsHiWatermark.setStatus("current")
_PktStatsDiscards_Type = Counter32
_PktStatsDiscards_Object = MibScalar
pktStatsDiscards = _PktStatsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 1, 10),
    _PktStatsDiscards_Type()
)
pktStatsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStatsDiscards.setStatus("current")
_MpCpuStats_ObjectIdentity = ObjectIdentity
mpCpuStats = _MpCpuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 2)
)
_MpCpuStatsUtil1Second_Type = Integer32
_MpCpuStatsUtil1Second_Object = MibScalar
mpCpuStatsUtil1Second = _MpCpuStatsUtil1Second_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 2, 1),
    _MpCpuStatsUtil1Second_Type()
)
mpCpuStatsUtil1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuStatsUtil1Second.setStatus("current")
_MpCpuStatsUtil4Seconds_Type = Integer32
_MpCpuStatsUtil4Seconds_Object = MibScalar
mpCpuStatsUtil4Seconds = _MpCpuStatsUtil4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 2, 2),
    _MpCpuStatsUtil4Seconds_Type()
)
mpCpuStatsUtil4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuStatsUtil4Seconds.setStatus("current")
_MpCpuStatsUtil64Seconds_Type = Integer32
_MpCpuStatsUtil64Seconds_Object = MibScalar
mpCpuStatsUtil64Seconds = _MpCpuStatsUtil64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 2, 3),
    _MpCpuStatsUtil64Seconds_Type()
)
mpCpuStatsUtil64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCpuStatsUtil64Seconds.setStatus("current")
_PortStats_ObjectIdentity = ObjectIdentity
portStats = _PortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3)
)
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("current")
_PortStatsTableEntry_Object = MibTableRow
portStatsTableEntry = _PortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1)
)
portStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "portStatsIndx"),
)
if mibBuilder.loadTexts:
    portStatsTableEntry.setStatus("current")
_PortStatsIndx_Type = Integer32
_PortStatsIndx_Object = MibTableColumn
portStatsIndx = _PortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 1),
    _PortStatsIndx_Type()
)
portStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsIndx.setStatus("current")
_PortStatsPhyIfInOctets_Type = Counter32
_PortStatsPhyIfInOctets_Object = MibTableColumn
portStatsPhyIfInOctets = _PortStatsPhyIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 2),
    _PortStatsPhyIfInOctets_Type()
)
portStatsPhyIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInOctets.setStatus("current")
_PortStatsPhyIfInUcastPkts_Type = Counter32
_PortStatsPhyIfInUcastPkts_Object = MibTableColumn
portStatsPhyIfInUcastPkts = _PortStatsPhyIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 3),
    _PortStatsPhyIfInUcastPkts_Type()
)
portStatsPhyIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInUcastPkts.setStatus("current")
_PortStatsPhyIfInNUcastPkts_Type = Counter32
_PortStatsPhyIfInNUcastPkts_Object = MibTableColumn
portStatsPhyIfInNUcastPkts = _PortStatsPhyIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 4),
    _PortStatsPhyIfInNUcastPkts_Type()
)
portStatsPhyIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInNUcastPkts.setStatus("current")
_PortStatsPhyIfInDiscards_Type = Counter32
_PortStatsPhyIfInDiscards_Object = MibTableColumn
portStatsPhyIfInDiscards = _PortStatsPhyIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 5),
    _PortStatsPhyIfInDiscards_Type()
)
portStatsPhyIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInDiscards.setStatus("current")
_PortStatsPhyIfInErrors_Type = Counter32
_PortStatsPhyIfInErrors_Object = MibTableColumn
portStatsPhyIfInErrors = _PortStatsPhyIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 6),
    _PortStatsPhyIfInErrors_Type()
)
portStatsPhyIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInErrors.setStatus("current")
_PortStatsPhyIfInUnknownProtos_Type = Counter32
_PortStatsPhyIfInUnknownProtos_Object = MibTableColumn
portStatsPhyIfInUnknownProtos = _PortStatsPhyIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 7),
    _PortStatsPhyIfInUnknownProtos_Type()
)
portStatsPhyIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInUnknownProtos.setStatus("current")
_PortStatsPhyIfOutOctets_Type = Counter32
_PortStatsPhyIfOutOctets_Object = MibTableColumn
portStatsPhyIfOutOctets = _PortStatsPhyIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 8),
    _PortStatsPhyIfOutOctets_Type()
)
portStatsPhyIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutOctets.setStatus("current")
_PortStatsPhyIfOutUcastPkts_Type = Counter32
_PortStatsPhyIfOutUcastPkts_Object = MibTableColumn
portStatsPhyIfOutUcastPkts = _PortStatsPhyIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 9),
    _PortStatsPhyIfOutUcastPkts_Type()
)
portStatsPhyIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutUcastPkts.setStatus("current")
_PortStatsPhyIfOutNUcastPkts_Type = Counter32
_PortStatsPhyIfOutNUcastPkts_Object = MibTableColumn
portStatsPhyIfOutNUcastPkts = _PortStatsPhyIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 10),
    _PortStatsPhyIfOutNUcastPkts_Type()
)
portStatsPhyIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutNUcastPkts.setStatus("current")
_PortStatsPhyIfOutDiscards_Type = Counter32
_PortStatsPhyIfOutDiscards_Object = MibTableColumn
portStatsPhyIfOutDiscards = _PortStatsPhyIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 11),
    _PortStatsPhyIfOutDiscards_Type()
)
portStatsPhyIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutDiscards.setStatus("current")
_PortStatsPhyIfOutErrors_Type = Counter32
_PortStatsPhyIfOutErrors_Object = MibTableColumn
portStatsPhyIfOutErrors = _PortStatsPhyIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 12),
    _PortStatsPhyIfOutErrors_Type()
)
portStatsPhyIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutErrors.setStatus("current")
_PortStatsPhyIfOutQLen_Type = Gauge32
_PortStatsPhyIfOutQLen_Object = MibTableColumn
portStatsPhyIfOutQLen = _PortStatsPhyIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 13),
    _PortStatsPhyIfOutQLen_Type()
)
portStatsPhyIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutQLen.setStatus("current")
_PortStatsPhyIfInBroadcastPkts_Type = Counter32
_PortStatsPhyIfInBroadcastPkts_Object = MibTableColumn
portStatsPhyIfInBroadcastPkts = _PortStatsPhyIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 14),
    _PortStatsPhyIfInBroadcastPkts_Type()
)
portStatsPhyIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInBroadcastPkts.setStatus("current")
_PortStatsPhyIfOutBroadcastPkts_Type = Counter32
_PortStatsPhyIfOutBroadcastPkts_Object = MibTableColumn
portStatsPhyIfOutBroadcastPkts = _PortStatsPhyIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 15),
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
        *(("clear", 2),
          ("ok", 1))
    )


_PortStatsClear_Type.__name__ = "Integer32"
_PortStatsClear_Object = MibTableColumn
portStatsClear = _PortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 16),
    _PortStatsClear_Type()
)
portStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStatsClear.setStatus("current")
_PortStatsPhyIfInMcastPkts_Type = Counter32
_PortStatsPhyIfInMcastPkts_Object = MibTableColumn
portStatsPhyIfInMcastPkts = _PortStatsPhyIfInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 17),
    _PortStatsPhyIfInMcastPkts_Type()
)
portStatsPhyIfInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInMcastPkts.setStatus("current")
_PortStatsPhyIfOutMcastPkts_Type = Counter32
_PortStatsPhyIfOutMcastPkts_Object = MibTableColumn
portStatsPhyIfOutMcastPkts = _PortStatsPhyIfOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 3, 1, 1, 18),
    _PortStatsPhyIfOutMcastPkts_Type()
)
portStatsPhyIfOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutMcastPkts.setStatus("current")
_SpStats_ObjectIdentity = ObjectIdentity
spStats = _SpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4)
)
_SpStatsCpuUtilTable_Object = MibTable
spStatsCpuUtilTable = _SpStatsCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    spStatsCpuUtilTable.setStatus("current")
_SpStatsCpuUtilTableEntry_Object = MibTableRow
spStatsCpuUtilTableEntry = _SpStatsCpuUtilTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 1, 1)
)
spStatsCpuUtilTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "spStatsCpuUtilSpIndex"),
)
if mibBuilder.loadTexts:
    spStatsCpuUtilTableEntry.setStatus("current")
_SpStatsCpuUtilSpIndex_Type = Integer32
_SpStatsCpuUtilSpIndex_Object = MibTableColumn
spStatsCpuUtilSpIndex = _SpStatsCpuUtilSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 1, 1, 1),
    _SpStatsCpuUtilSpIndex_Type()
)
spStatsCpuUtilSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spStatsCpuUtilSpIndex.setStatus("current")
_SpStatsCpuUtil1Second_Type = Integer32
_SpStatsCpuUtil1Second_Object = MibTableColumn
spStatsCpuUtil1Second = _SpStatsCpuUtil1Second_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 1, 1, 2),
    _SpStatsCpuUtil1Second_Type()
)
spStatsCpuUtil1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spStatsCpuUtil1Second.setStatus("current")
_SpStatsCpuUtil4Seconds_Type = Integer32
_SpStatsCpuUtil4Seconds_Object = MibTableColumn
spStatsCpuUtil4Seconds = _SpStatsCpuUtil4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 1, 1, 3),
    _SpStatsCpuUtil4Seconds_Type()
)
spStatsCpuUtil4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spStatsCpuUtil4Seconds.setStatus("current")
_SpStatsCpuUtil64Seconds_Type = Integer32
_SpStatsCpuUtil64Seconds_Object = MibTableColumn
spStatsCpuUtil64Seconds = _SpStatsCpuUtil64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 1, 1, 4),
    _SpStatsCpuUtil64Seconds_Type()
)
spStatsCpuUtil64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spStatsCpuUtil64Seconds.setStatus("current")
_SpMaintStatsTable_Object = MibTable
spMaintStatsTable = _SpMaintStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    spMaintStatsTable.setStatus("current")
_SpMaintStatsTableEntry_Object = MibTableRow
spMaintStatsTableEntry = _SpMaintStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1)
)
spMaintStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "spMaintStatsSpIndex"),
)
if mibBuilder.loadTexts:
    spMaintStatsTableEntry.setStatus("current")
_SpMaintStatsSpIndex_Type = Integer32
_SpMaintStatsSpIndex_Object = MibTableColumn
spMaintStatsSpIndex = _SpMaintStatsSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 1),
    _SpMaintStatsSpIndex_Type()
)
spMaintStatsSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSpIndex.setStatus("current")
_SpMaintStatsPfdbFreeEmpty_Type = Counter32
_SpMaintStatsPfdbFreeEmpty_Object = MibTableColumn
spMaintStatsPfdbFreeEmpty = _SpMaintStatsPfdbFreeEmpty_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 2),
    _SpMaintStatsPfdbFreeEmpty_Type()
)
spMaintStatsPfdbFreeEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsPfdbFreeEmpty.setStatus("current")
_SpMaintStatsResolveErrNoddw_Type = Counter32
_SpMaintStatsResolveErrNoddw_Object = MibTableColumn
spMaintStatsResolveErrNoddw = _SpMaintStatsResolveErrNoddw_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 3),
    _SpMaintStatsResolveErrNoddw_Type()
)
spMaintStatsResolveErrNoddw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsResolveErrNoddw.setStatus("current")
_SpMaintStatsLearnErrNoddw_Type = Counter32
_SpMaintStatsLearnErrNoddw_Object = MibTableColumn
spMaintStatsLearnErrNoddw = _SpMaintStatsLearnErrNoddw_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 4),
    _SpMaintStatsLearnErrNoddw_Type()
)
spMaintStatsLearnErrNoddw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsLearnErrNoddw.setStatus("current")
_SpMaintStatsAgeMPNoddw_Type = Counter32
_SpMaintStatsAgeMPNoddw_Object = MibTableColumn
spMaintStatsAgeMPNoddw = _SpMaintStatsAgeMPNoddw_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 5),
    _SpMaintStatsAgeMPNoddw_Type()
)
spMaintStatsAgeMPNoddw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsAgeMPNoddw.setStatus("current")
_SpMaintStatsDeleteMiss_Type = Counter32
_SpMaintStatsDeleteMiss_Object = MibTableColumn
spMaintStatsDeleteMiss = _SpMaintStatsDeleteMiss_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 6),
    _SpMaintStatsDeleteMiss_Type()
)
spMaintStatsDeleteMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsDeleteMiss.setStatus("current")
_SpMaintStatsRecvLetErrorsMP_Type = Counter32
_SpMaintStatsRecvLetErrorsMP_Object = MibTableColumn
spMaintStatsRecvLetErrorsMP = _SpMaintStatsRecvLetErrorsMP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 7),
    _SpMaintStatsRecvLetErrorsMP_Type()
)
spMaintStatsRecvLetErrorsMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetErrorsMP.setStatus("current")
_SpMaintStatsRecvLetErrorsSP1_Type = Counter32
_SpMaintStatsRecvLetErrorsSP1_Object = MibTableColumn
spMaintStatsRecvLetErrorsSP1 = _SpMaintStatsRecvLetErrorsSP1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 8),
    _SpMaintStatsRecvLetErrorsSP1_Type()
)
spMaintStatsRecvLetErrorsSP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetErrorsSP1.setStatus("current")
_SpMaintStatsRecvLetErrorsSP2_Type = Counter32
_SpMaintStatsRecvLetErrorsSP2_Object = MibTableColumn
spMaintStatsRecvLetErrorsSP2 = _SpMaintStatsRecvLetErrorsSP2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 9),
    _SpMaintStatsRecvLetErrorsSP2_Type()
)
spMaintStatsRecvLetErrorsSP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetErrorsSP2.setStatus("current")
_SpMaintStatsRecvLetErrorsSP3_Type = Counter32
_SpMaintStatsRecvLetErrorsSP3_Object = MibTableColumn
spMaintStatsRecvLetErrorsSP3 = _SpMaintStatsRecvLetErrorsSP3_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 10),
    _SpMaintStatsRecvLetErrorsSP3_Type()
)
spMaintStatsRecvLetErrorsSP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetErrorsSP3.setStatus("current")
_SpMaintStatsRecvLetErrorsSP4_Type = Counter32
_SpMaintStatsRecvLetErrorsSP4_Object = MibTableColumn
spMaintStatsRecvLetErrorsSP4 = _SpMaintStatsRecvLetErrorsSP4_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 11),
    _SpMaintStatsRecvLetErrorsSP4_Type()
)
spMaintStatsRecvLetErrorsSP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetErrorsSP4.setStatus("current")
_SpMaintStatsSendLetFailsMP_Type = Counter32
_SpMaintStatsSendLetFailsMP_Object = MibTableColumn
spMaintStatsSendLetFailsMP = _SpMaintStatsSendLetFailsMP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 12),
    _SpMaintStatsSendLetFailsMP_Type()
)
spMaintStatsSendLetFailsMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetFailsMP.setStatus("current")
_SpMaintStatsSendLetFailsSP1_Type = Counter32
_SpMaintStatsSendLetFailsSP1_Object = MibTableColumn
spMaintStatsSendLetFailsSP1 = _SpMaintStatsSendLetFailsSP1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 13),
    _SpMaintStatsSendLetFailsSP1_Type()
)
spMaintStatsSendLetFailsSP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetFailsSP1.setStatus("current")
_SpMaintStatsSendLetFailsSP2_Type = Counter32
_SpMaintStatsSendLetFailsSP2_Object = MibTableColumn
spMaintStatsSendLetFailsSP2 = _SpMaintStatsSendLetFailsSP2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 14),
    _SpMaintStatsSendLetFailsSP2_Type()
)
spMaintStatsSendLetFailsSP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetFailsSP2.setStatus("current")
_SpMaintStatsSendLetFailsSP3_Type = Counter32
_SpMaintStatsSendLetFailsSP3_Object = MibTableColumn
spMaintStatsSendLetFailsSP3 = _SpMaintStatsSendLetFailsSP3_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 15),
    _SpMaintStatsSendLetFailsSP3_Type()
)
spMaintStatsSendLetFailsSP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetFailsSP3.setStatus("current")
_SpMaintStatsSendLetFailsSP4_Type = Counter32
_SpMaintStatsSendLetFailsSP4_Object = MibTableColumn
spMaintStatsSendLetFailsSP4 = _SpMaintStatsSendLetFailsSP4_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 16),
    _SpMaintStatsSendLetFailsSP4_Type()
)
spMaintStatsSendLetFailsSP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetFailsSP4.setStatus("current")
_SpMaintStatsRecvLetSuccessMP_Type = Counter32
_SpMaintStatsRecvLetSuccessMP_Object = MibTableColumn
spMaintStatsRecvLetSuccessMP = _SpMaintStatsRecvLetSuccessMP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 17),
    _SpMaintStatsRecvLetSuccessMP_Type()
)
spMaintStatsRecvLetSuccessMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetSuccessMP.setStatus("current")
_SpMaintStatsRecvLetSuccessSP1_Type = Counter32
_SpMaintStatsRecvLetSuccessSP1_Object = MibTableColumn
spMaintStatsRecvLetSuccessSP1 = _SpMaintStatsRecvLetSuccessSP1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 18),
    _SpMaintStatsRecvLetSuccessSP1_Type()
)
spMaintStatsRecvLetSuccessSP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetSuccessSP1.setStatus("current")
_SpMaintStatsRecvLetSuccessSP2_Type = Counter32
_SpMaintStatsRecvLetSuccessSP2_Object = MibTableColumn
spMaintStatsRecvLetSuccessSP2 = _SpMaintStatsRecvLetSuccessSP2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 19),
    _SpMaintStatsRecvLetSuccessSP2_Type()
)
spMaintStatsRecvLetSuccessSP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetSuccessSP2.setStatus("current")
_SpMaintStatsRecvLetSuccessSP3_Type = Counter32
_SpMaintStatsRecvLetSuccessSP3_Object = MibTableColumn
spMaintStatsRecvLetSuccessSP3 = _SpMaintStatsRecvLetSuccessSP3_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 20),
    _SpMaintStatsRecvLetSuccessSP3_Type()
)
spMaintStatsRecvLetSuccessSP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetSuccessSP3.setStatus("current")
_SpMaintStatsRecvLetSuccessSP4_Type = Counter32
_SpMaintStatsRecvLetSuccessSP4_Object = MibTableColumn
spMaintStatsRecvLetSuccessSP4 = _SpMaintStatsRecvLetSuccessSP4_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 21),
    _SpMaintStatsRecvLetSuccessSP4_Type()
)
spMaintStatsRecvLetSuccessSP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRecvLetSuccessSP4.setStatus("current")
_SpMaintStatsSendLetSuccessMP_Type = Counter32
_SpMaintStatsSendLetSuccessMP_Object = MibTableColumn
spMaintStatsSendLetSuccessMP = _SpMaintStatsSendLetSuccessMP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 22),
    _SpMaintStatsSendLetSuccessMP_Type()
)
spMaintStatsSendLetSuccessMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetSuccessMP.setStatus("current")
_SpMaintStatsSendLetSuccessSP1_Type = Counter32
_SpMaintStatsSendLetSuccessSP1_Object = MibTableColumn
spMaintStatsSendLetSuccessSP1 = _SpMaintStatsSendLetSuccessSP1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 23),
    _SpMaintStatsSendLetSuccessSP1_Type()
)
spMaintStatsSendLetSuccessSP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetSuccessSP1.setStatus("current")
_SpMaintStatsSendLetSuccessSP2_Type = Counter32
_SpMaintStatsSendLetSuccessSP2_Object = MibTableColumn
spMaintStatsSendLetSuccessSP2 = _SpMaintStatsSendLetSuccessSP2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 24),
    _SpMaintStatsSendLetSuccessSP2_Type()
)
spMaintStatsSendLetSuccessSP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetSuccessSP2.setStatus("current")
_SpMaintStatsSendLetSuccessSP3_Type = Counter32
_SpMaintStatsSendLetSuccessSP3_Object = MibTableColumn
spMaintStatsSendLetSuccessSP3 = _SpMaintStatsSendLetSuccessSP3_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 25),
    _SpMaintStatsSendLetSuccessSP3_Type()
)
spMaintStatsSendLetSuccessSP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetSuccessSP3.setStatus("current")
_SpMaintStatsSendLetSuccessSP4_Type = Counter32
_SpMaintStatsSendLetSuccessSP4_Object = MibTableColumn
spMaintStatsSendLetSuccessSP4 = _SpMaintStatsSendLetSuccessSP4_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 26),
    _SpMaintStatsSendLetSuccessSP4_Type()
)
spMaintStatsSendLetSuccessSP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsSendLetSuccessSP4.setStatus("current")
_SpMaintStatsRateLimitArpDrops_Type = Counter32
_SpMaintStatsRateLimitArpDrops_Object = MibTableColumn
spMaintStatsRateLimitArpDrops = _SpMaintStatsRateLimitArpDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 27),
    _SpMaintStatsRateLimitArpDrops_Type()
)
spMaintStatsRateLimitArpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRateLimitArpDrops.setStatus("current")
_SpMaintStatsRateLimitIcmpDrops_Type = Counter32
_SpMaintStatsRateLimitIcmpDrops_Object = MibTableColumn
spMaintStatsRateLimitIcmpDrops = _SpMaintStatsRateLimitIcmpDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 28),
    _SpMaintStatsRateLimitIcmpDrops_Type()
)
spMaintStatsRateLimitIcmpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRateLimitIcmpDrops.setStatus("current")
_SpMaintStatsRateLimitTcpDrops_Type = Counter32
_SpMaintStatsRateLimitTcpDrops_Object = MibTableColumn
spMaintStatsRateLimitTcpDrops = _SpMaintStatsRateLimitTcpDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 29),
    _SpMaintStatsRateLimitTcpDrops_Type()
)
spMaintStatsRateLimitTcpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRateLimitTcpDrops.setStatus("current")
_SpMaintStatsRateLimitUdpDrops_Type = Counter32
_SpMaintStatsRateLimitUdpDrops_Object = MibTableColumn
spMaintStatsRateLimitUdpDrops = _SpMaintStatsRateLimitUdpDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 2, 1, 30),
    _SpMaintStatsRateLimitUdpDrops_Type()
)
spMaintStatsRateLimitUdpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMaintStatsRateLimitUdpDrops.setStatus("current")
_SpMemStatsTable_Object = MibTable
spMemStatsTable = _SpMemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    spMemStatsTable.setStatus("current")
_SpMemStatsTableEntry_Object = MibTableRow
spMemStatsTableEntry = _SpMemStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1)
)
spMemStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "spMemStatsIndex"),
)
if mibBuilder.loadTexts:
    spMemStatsTableEntry.setStatus("current")
_SpMemStatsIndex_Type = Integer32
_SpMemStatsIndex_Object = MibTableColumn
spMemStatsIndex = _SpMemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1, 1),
    _SpMemStatsIndex_Type()
)
spMemStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemStatsIndex.setStatus("current")
_SpMemStatsTotal_Type = Integer32
_SpMemStatsTotal_Object = MibTableColumn
spMemStatsTotal = _SpMemStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1, 2),
    _SpMemStatsTotal_Type()
)
spMemStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemStatsTotal.setStatus("current")
_SpMemStatsCurr_Type = Integer32
_SpMemStatsCurr_Object = MibTableColumn
spMemStatsCurr = _SpMemStatsCurr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1, 3),
    _SpMemStatsCurr_Type()
)
spMemStatsCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemStatsCurr.setStatus("current")
_SpMemStatsAllocs_Type = Counter32
_SpMemStatsAllocs_Object = MibTableColumn
spMemStatsAllocs = _SpMemStatsAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1, 4),
    _SpMemStatsAllocs_Type()
)
spMemStatsAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemStatsAllocs.setStatus("current")
_SpMemStatsFrees_Type = Counter32
_SpMemStatsFrees_Object = MibTableColumn
spMemStatsFrees = _SpMemStatsFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1, 5),
    _SpMemStatsFrees_Type()
)
spMemStatsFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemStatsFrees.setStatus("current")
_SpMemStatsAllocsFailures_Type = Counter32
_SpMemStatsAllocsFailures_Object = MibTableColumn
spMemStatsAllocsFailures = _SpMemStatsAllocsFailures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1, 6),
    _SpMemStatsAllocsFailures_Type()
)
spMemStatsAllocsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemStatsAllocsFailures.setStatus("current")
_SpMemStatsHiWat_Type = Integer32
_SpMemStatsHiWat_Object = MibTableColumn
spMemStatsHiWat = _SpMemStatsHiWat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 4, 3, 1, 7),
    _SpMemStatsHiWat_Type()
)
spMemStatsHiWat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemStatsHiWat.setStatus("current")
_MgmtStats_ObjectIdentity = ObjectIdentity
mgmtStats = _MgmtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5)
)
_MgmtStatsRxpackets_Type = Counter32
_MgmtStatsRxpackets_Object = MibScalar
mgmtStatsRxpackets = _MgmtStatsRxpackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 1),
    _MgmtStatsRxpackets_Type()
)
mgmtStatsRxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsRxpackets.setStatus("current")
_MgmtStatsRxErrors_Type = Counter32
_MgmtStatsRxErrors_Object = MibScalar
mgmtStatsRxErrors = _MgmtStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 2),
    _MgmtStatsRxErrors_Type()
)
mgmtStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsRxErrors.setStatus("current")
_MgmtStatsRxDropped_Type = Counter32
_MgmtStatsRxDropped_Object = MibScalar
mgmtStatsRxDropped = _MgmtStatsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 3),
    _MgmtStatsRxDropped_Type()
)
mgmtStatsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsRxDropped.setStatus("current")
_MgmtStatsRxOverruns_Type = Counter32
_MgmtStatsRxOverruns_Object = MibScalar
mgmtStatsRxOverruns = _MgmtStatsRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 4),
    _MgmtStatsRxOverruns_Type()
)
mgmtStatsRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsRxOverruns.setStatus("current")
_MgmtStatsRxFrame_Type = Counter32
_MgmtStatsRxFrame_Object = MibScalar
mgmtStatsRxFrame = _MgmtStatsRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 5),
    _MgmtStatsRxFrame_Type()
)
mgmtStatsRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsRxFrame.setStatus("current")
_MgmtStatsTxpackets_Type = Counter32
_MgmtStatsTxpackets_Object = MibScalar
mgmtStatsTxpackets = _MgmtStatsTxpackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 6),
    _MgmtStatsTxpackets_Type()
)
mgmtStatsTxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxpackets.setStatus("current")
_MgmtStatsTxErrors_Type = Counter32
_MgmtStatsTxErrors_Object = MibScalar
mgmtStatsTxErrors = _MgmtStatsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 7),
    _MgmtStatsTxErrors_Type()
)
mgmtStatsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxErrors.setStatus("current")
_MgmtStatsTxDropped_Type = Counter32
_MgmtStatsTxDropped_Object = MibScalar
mgmtStatsTxDropped = _MgmtStatsTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 8),
    _MgmtStatsTxDropped_Type()
)
mgmtStatsTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxDropped.setStatus("current")
_MgmtStatsTxOverruns_Type = Counter32
_MgmtStatsTxOverruns_Object = MibScalar
mgmtStatsTxOverruns = _MgmtStatsTxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 9),
    _MgmtStatsTxOverruns_Type()
)
mgmtStatsTxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxOverruns.setStatus("current")
_MgmtStatsTxCarrier_Type = Counter32
_MgmtStatsTxCarrier_Object = MibScalar
mgmtStatsTxCarrier = _MgmtStatsTxCarrier_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 10),
    _MgmtStatsTxCarrier_Type()
)
mgmtStatsTxCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxCarrier.setStatus("current")
_MgmtStatsTxCollisions_Type = Counter32
_MgmtStatsTxCollisions_Object = MibScalar
mgmtStatsTxCollisions = _MgmtStatsTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 11),
    _MgmtStatsTxCollisions_Type()
)
mgmtStatsTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxCollisions.setStatus("current")
_MgmtStatsTxQueueLen_Type = Counter32
_MgmtStatsTxQueueLen_Object = MibScalar
mgmtStatsTxQueueLen = _MgmtStatsTxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 12),
    _MgmtStatsTxQueueLen_Type()
)
mgmtStatsTxQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxQueueLen.setStatus("current")
_MgmtStatsRxBytes_Type = Counter32
_MgmtStatsRxBytes_Object = MibScalar
mgmtStatsRxBytes = _MgmtStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 13),
    _MgmtStatsRxBytes_Type()
)
mgmtStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsRxBytes.setStatus("current")
_MgmtStatsRxMulticast_Type = Counter32
_MgmtStatsRxMulticast_Object = MibScalar
mgmtStatsRxMulticast = _MgmtStatsRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 14),
    _MgmtStatsRxMulticast_Type()
)
mgmtStatsRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsRxMulticast.setStatus("current")
_MgmtStatsTxBytes_Type = Counter32
_MgmtStatsTxBytes_Object = MibScalar
mgmtStatsTxBytes = _MgmtStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 5, 15),
    _MgmtStatsTxBytes_Type()
)
mgmtStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtStatsTxBytes.setStatus("current")
_SecurityStats_ObjectIdentity = ObjectIdentity
securityStats = _SecurityStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6)
)
_AgDosPortStatsTable_Object = MibTable
agDosPortStatsTable = _AgDosPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    agDosPortStatsTable.setStatus("current")
_AgDosPortStatsTableEntry_Object = MibTableRow
agDosPortStatsTableEntry = _AgDosPortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1)
)
agDosPortStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agDosPortStatsIndx"),
)
if mibBuilder.loadTexts:
    agDosPortStatsTableEntry.setStatus("current")
_AgDosPortStatsIndx_Type = Integer32
_AgDosPortStatsIndx_Object = MibTableColumn
agDosPortStatsIndx = _AgDosPortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 1),
    _AgDosPortStatsIndx_Type()
)
agDosPortStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIndx.setStatus("current")
_AgDosPortStatsIPLen_Type = Counter32
_AgDosPortStatsIPLen_Object = MibTableColumn
agDosPortStatsIPLen = _AgDosPortStatsIPLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 10),
    _AgDosPortStatsIPLen_Type()
)
agDosPortStatsIPLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIPLen.setStatus("current")
_AgDosPortStatsIPVersion_Type = Counter32
_AgDosPortStatsIPVersion_Object = MibTableColumn
agDosPortStatsIPVersion = _AgDosPortStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 11),
    _AgDosPortStatsIPVersion_Type()
)
agDosPortStatsIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIPVersion.setStatus("current")
_AgDosPortStatsBroadcast_Type = Counter32
_AgDosPortStatsBroadcast_Object = MibTableColumn
agDosPortStatsBroadcast = _AgDosPortStatsBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 12),
    _AgDosPortStatsBroadcast_Type()
)
agDosPortStatsBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsBroadcast.setStatus("current")
_AgDosPortStatsLoopback_Type = Counter32
_AgDosPortStatsLoopback_Object = MibTableColumn
agDosPortStatsLoopback = _AgDosPortStatsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 13),
    _AgDosPortStatsLoopback_Type()
)
agDosPortStatsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsLoopback.setStatus("current")
_AgDosPortStatsLand_Type = Counter32
_AgDosPortStatsLand_Object = MibTableColumn
agDosPortStatsLand = _AgDosPortStatsLand_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 14),
    _AgDosPortStatsLand_Type()
)
agDosPortStatsLand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsLand.setStatus("current")
_AgDosPortStatsIPReserved_Type = Counter32
_AgDosPortStatsIPReserved_Object = MibTableColumn
agDosPortStatsIPReserved = _AgDosPortStatsIPReserved_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 15),
    _AgDosPortStatsIPReserved_Type()
)
agDosPortStatsIPReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIPReserved.setStatus("current")
_AgDosPortStatsIPTTL_Type = Counter32
_AgDosPortStatsIPTTL_Object = MibTableColumn
agDosPortStatsIPTTL = _AgDosPortStatsIPTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 16),
    _AgDosPortStatsIPTTL_Type()
)
agDosPortStatsIPTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIPTTL.setStatus("current")
_AgDosPortStatsIPProt_Type = Counter32
_AgDosPortStatsIPProt_Object = MibTableColumn
agDosPortStatsIPProt = _AgDosPortStatsIPProt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 17),
    _AgDosPortStatsIPProt_Type()
)
agDosPortStatsIPProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIPProt.setStatus("current")
_AgDosPortStatsIPOptLen_Type = Counter32
_AgDosPortStatsIPOptLen_Object = MibTableColumn
agDosPortStatsIPOptLen = _AgDosPortStatsIPOptLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 18),
    _AgDosPortStatsIPOptLen_Type()
)
agDosPortStatsIPOptLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIPOptLen.setStatus("current")
_AgDosPortStatsFragMoreDont_Type = Counter32
_AgDosPortStatsFragMoreDont_Object = MibTableColumn
agDosPortStatsFragMoreDont = _AgDosPortStatsFragMoreDont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 19),
    _AgDosPortStatsFragMoreDont_Type()
)
agDosPortStatsFragMoreDont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragMoreDont.setStatus("current")
_AgDosPortStatsFragData_Type = Counter32
_AgDosPortStatsFragData_Object = MibTableColumn
agDosPortStatsFragData = _AgDosPortStatsFragData_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 20),
    _AgDosPortStatsFragData_Type()
)
agDosPortStatsFragData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragData.setStatus("current")
_AgDosPortStatsFragBoundary_Type = Counter32
_AgDosPortStatsFragBoundary_Object = MibTableColumn
agDosPortStatsFragBoundary = _AgDosPortStatsFragBoundary_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 21),
    _AgDosPortStatsFragBoundary_Type()
)
agDosPortStatsFragBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragBoundary.setStatus("current")
_AgDosPortStatsFragLast_Type = Counter32
_AgDosPortStatsFragLast_Object = MibTableColumn
agDosPortStatsFragLast = _AgDosPortStatsFragLast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 22),
    _AgDosPortStatsFragLast_Type()
)
agDosPortStatsFragLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragLast.setStatus("current")
_AgDosPortStatsFragDontOff_Type = Counter32
_AgDosPortStatsFragDontOff_Object = MibTableColumn
agDosPortStatsFragDontOff = _AgDosPortStatsFragDontOff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 23),
    _AgDosPortStatsFragDontOff_Type()
)
agDosPortStatsFragDontOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragDontOff.setStatus("current")
_AgDosPortStatsFragOpt_Type = Counter32
_AgDosPortStatsFragOpt_Object = MibTableColumn
agDosPortStatsFragOpt = _AgDosPortStatsFragOpt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 24),
    _AgDosPortStatsFragOpt_Type()
)
agDosPortStatsFragOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragOpt.setStatus("current")
_AgDosPortStatsFragOff_Type = Counter32
_AgDosPortStatsFragOff_Object = MibTableColumn
agDosPortStatsFragOff = _AgDosPortStatsFragOff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 25),
    _AgDosPortStatsFragOff_Type()
)
agDosPortStatsFragOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragOff.setStatus("current")
_AgDosPortStatsFragOversize_Type = Counter32
_AgDosPortStatsFragOversize_Object = MibTableColumn
agDosPortStatsFragOversize = _AgDosPortStatsFragOversize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 26),
    _AgDosPortStatsFragOversize_Type()
)
agDosPortStatsFragOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFragOversize.setStatus("current")
_AgDosPortStatsTCPLen_Type = Counter32
_AgDosPortStatsTCPLen_Object = MibTableColumn
agDosPortStatsTCPLen = _AgDosPortStatsTCPLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 27),
    _AgDosPortStatsTCPLen_Type()
)
agDosPortStatsTCPLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsTCPLen.setStatus("current")
_AgDosPortStatsTCPPortZero_Type = Counter32
_AgDosPortStatsTCPPortZero_Object = MibTableColumn
agDosPortStatsTCPPortZero = _AgDosPortStatsTCPPortZero_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 28),
    _AgDosPortStatsTCPPortZero_Type()
)
agDosPortStatsTCPPortZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsTCPPortZero.setStatus("current")
_AgDosPortStatsBlatAttack_Type = Counter32
_AgDosPortStatsBlatAttack_Object = MibTableColumn
agDosPortStatsBlatAttack = _AgDosPortStatsBlatAttack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 29),
    _AgDosPortStatsBlatAttack_Type()
)
agDosPortStatsBlatAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsBlatAttack.setStatus("current")
_AgDosPortStatsTCPReserved_Type = Counter32
_AgDosPortStatsTCPReserved_Object = MibTableColumn
agDosPortStatsTCPReserved = _AgDosPortStatsTCPReserved_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 30),
    _AgDosPortStatsTCPReserved_Type()
)
agDosPortStatsTCPReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsTCPReserved.setStatus("current")
_AgDosPortStatsNullScanAttack_Type = Counter32
_AgDosPortStatsNullScanAttack_Object = MibTableColumn
agDosPortStatsNullScanAttack = _AgDosPortStatsNullScanAttack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 31),
    _AgDosPortStatsNullScanAttack_Type()
)
agDosPortStatsNullScanAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsNullScanAttack.setStatus("current")
_AgDosPortStatsFullXmasScan_Type = Counter32
_AgDosPortStatsFullXmasScan_Object = MibTableColumn
agDosPortStatsFullXmasScan = _AgDosPortStatsFullXmasScan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 32),
    _AgDosPortStatsFullXmasScan_Type()
)
agDosPortStatsFullXmasScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFullXmasScan.setStatus("current")
_AgDosPortStatsFinScan_Type = Counter32
_AgDosPortStatsFinScan_Object = MibTableColumn
agDosPortStatsFinScan = _AgDosPortStatsFinScan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 33),
    _AgDosPortStatsFinScan_Type()
)
agDosPortStatsFinScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFinScan.setStatus("current")
_AgDosPortStatsVecnaScan_Type = Counter32
_AgDosPortStatsVecnaScan_Object = MibTableColumn
agDosPortStatsVecnaScan = _AgDosPortStatsVecnaScan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 34),
    _AgDosPortStatsVecnaScan_Type()
)
agDosPortStatsVecnaScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsVecnaScan.setStatus("current")
_AgDosPortStatsXmasScanAttack_Type = Counter32
_AgDosPortStatsXmasScanAttack_Object = MibTableColumn
agDosPortStatsXmasScanAttack = _AgDosPortStatsXmasScanAttack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 35),
    _AgDosPortStatsXmasScanAttack_Type()
)
agDosPortStatsXmasScanAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsXmasScanAttack.setStatus("current")
_AgDosPortStatsSynFinScan_Type = Counter32
_AgDosPortStatsSynFinScan_Object = MibTableColumn
agDosPortStatsSynFinScan = _AgDosPortStatsSynFinScan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 36),
    _AgDosPortStatsSynFinScan_Type()
)
agDosPortStatsSynFinScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsSynFinScan.setStatus("current")
_AgDosPortStatsFlagAbnormal_Type = Counter32
_AgDosPortStatsFlagAbnormal_Object = MibTableColumn
agDosPortStatsFlagAbnormal = _AgDosPortStatsFlagAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 37),
    _AgDosPortStatsFlagAbnormal_Type()
)
agDosPortStatsFlagAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFlagAbnormal.setStatus("current")
_AgDosPortStatsSYNData_Type = Counter32
_AgDosPortStatsSYNData_Object = MibTableColumn
agDosPortStatsSYNData = _AgDosPortStatsSYNData_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 38),
    _AgDosPortStatsSYNData_Type()
)
agDosPortStatsSYNData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsSYNData.setStatus("current")
_AgDosPortStatsSYNFrag_Type = Counter32
_AgDosPortStatsSYNFrag_Object = MibTableColumn
agDosPortStatsSYNFrag = _AgDosPortStatsSYNFrag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 39),
    _AgDosPortStatsSYNFrag_Type()
)
agDosPortStatsSYNFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsSYNFrag.setStatus("current")
_AgDosPortStatsFTPPort_Type = Counter32
_AgDosPortStatsFTPPort_Object = MibTableColumn
agDosPortStatsFTPPort = _AgDosPortStatsFTPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 40),
    _AgDosPortStatsFTPPort_Type()
)
agDosPortStatsFTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFTPPort.setStatus("current")
_AgDosPortStatsDNSPort_Type = Counter32
_AgDosPortStatsDNSPort_Object = MibTableColumn
agDosPortStatsDNSPort = _AgDosPortStatsDNSPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 41),
    _AgDosPortStatsDNSPort_Type()
)
agDosPortStatsDNSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsDNSPort.setStatus("current")
_AgDosPortStatsSeqZero_Type = Counter32
_AgDosPortStatsSeqZero_Object = MibTableColumn
agDosPortStatsSeqZero = _AgDosPortStatsSeqZero_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 42),
    _AgDosPortStatsSeqZero_Type()
)
agDosPortStatsSeqZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsSeqZero.setStatus("current")
_AgDosPortStatsAckZero_Type = Counter32
_AgDosPortStatsAckZero_Object = MibTableColumn
agDosPortStatsAckZero = _AgDosPortStatsAckZero_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 43),
    _AgDosPortStatsAckZero_Type()
)
agDosPortStatsAckZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsAckZero.setStatus("current")
_AgDosPortStatsTCPOptLen_Type = Counter32
_AgDosPortStatsTCPOptLen_Object = MibTableColumn
agDosPortStatsTCPOptLen = _AgDosPortStatsTCPOptLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 44),
    _AgDosPortStatsTCPOptLen_Type()
)
agDosPortStatsTCPOptLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsTCPOptLen.setStatus("current")
_AgDosPortStatsUDPLen_Type = Counter32
_AgDosPortStatsUDPLen_Object = MibTableColumn
agDosPortStatsUDPLen = _AgDosPortStatsUDPLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 45),
    _AgDosPortStatsUDPLen_Type()
)
agDosPortStatsUDPLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsUDPLen.setStatus("current")
_AgDosPortStatsUDPPortZero_Type = Counter32
_AgDosPortStatsUDPPortZero_Object = MibTableColumn
agDosPortStatsUDPPortZero = _AgDosPortStatsUDPPortZero_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 46),
    _AgDosPortStatsUDPPortZero_Type()
)
agDosPortStatsUDPPortZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsUDPPortZero.setStatus("current")
_AgDosPortStatsFraggleAttack_Type = Counter32
_AgDosPortStatsFraggleAttack_Object = MibTableColumn
agDosPortStatsFraggleAttack = _AgDosPortStatsFraggleAttack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 47),
    _AgDosPortStatsFraggleAttack_Type()
)
agDosPortStatsFraggleAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsFraggleAttack.setStatus("current")
_AgDosPortStatsPepsi_Type = Counter32
_AgDosPortStatsPepsi_Object = MibTableColumn
agDosPortStatsPepsi = _AgDosPortStatsPepsi_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 48),
    _AgDosPortStatsPepsi_Type()
)
agDosPortStatsPepsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsPepsi.setStatus("current")
_AgDosPortStatsRc8_Type = Counter32
_AgDosPortStatsRc8_Object = MibTableColumn
agDosPortStatsRc8 = _AgDosPortStatsRc8_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 49),
    _AgDosPortStatsRc8_Type()
)
agDosPortStatsRc8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsRc8.setStatus("current")
_AgDosPortStatsSNMPNull_Type = Counter32
_AgDosPortStatsSNMPNull_Object = MibTableColumn
agDosPortStatsSNMPNull = _AgDosPortStatsSNMPNull_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 50),
    _AgDosPortStatsSNMPNull_Type()
)
agDosPortStatsSNMPNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsSNMPNull.setStatus("current")
_AgDosPortStatsICMPLen_Type = Counter32
_AgDosPortStatsICMPLen_Object = MibTableColumn
agDosPortStatsICMPLen = _AgDosPortStatsICMPLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 51),
    _AgDosPortStatsICMPLen_Type()
)
agDosPortStatsICMPLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsICMPLen.setStatus("current")
_AgDosPortStatsSmurfAttack_Type = Counter32
_AgDosPortStatsSmurfAttack_Object = MibTableColumn
agDosPortStatsSmurfAttack = _AgDosPortStatsSmurfAttack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 52),
    _AgDosPortStatsSmurfAttack_Type()
)
agDosPortStatsSmurfAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsSmurfAttack.setStatus("current")
_AgDosPortStatsICMPData_Type = Counter32
_AgDosPortStatsICMPData_Object = MibTableColumn
agDosPortStatsICMPData = _AgDosPortStatsICMPData_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 53),
    _AgDosPortStatsICMPData_Type()
)
agDosPortStatsICMPData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsICMPData.setStatus("current")
_AgDosPortStatsICMPOff_Type = Counter32
_AgDosPortStatsICMPOff_Object = MibTableColumn
agDosPortStatsICMPOff = _AgDosPortStatsICMPOff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 54),
    _AgDosPortStatsICMPOff_Type()
)
agDosPortStatsICMPOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsICMPOff.setStatus("current")
_AgDosPortStatsICMPType_Type = Counter32
_AgDosPortStatsICMPType_Object = MibTableColumn
agDosPortStatsICMPType = _AgDosPortStatsICMPType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 55),
    _AgDosPortStatsICMPType_Type()
)
agDosPortStatsICMPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsICMPType.setStatus("current")
_AgDosPortStatsIGMPLen_Type = Counter32
_AgDosPortStatsIGMPLen_Object = MibTableColumn
agDosPortStatsIGMPLen = _AgDosPortStatsIGMPLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 56),
    _AgDosPortStatsIGMPLen_Type()
)
agDosPortStatsIGMPLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIGMPLen.setStatus("current")
_AgDosPortStatsIGMPFrag_Type = Counter32
_AgDosPortStatsIGMPFrag_Object = MibTableColumn
agDosPortStatsIGMPFrag = _AgDosPortStatsIGMPFrag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 57),
    _AgDosPortStatsIGMPFrag_Type()
)
agDosPortStatsIGMPFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIGMPFrag.setStatus("current")
_AgDosPortStatsIGMPType_Type = Counter32
_AgDosPortStatsIGMPType_Object = MibTableColumn
agDosPortStatsIGMPType = _AgDosPortStatsIGMPType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 58),
    _AgDosPortStatsIGMPType_Type()
)
agDosPortStatsIGMPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIGMPType.setStatus("current")
_AgDosPortStatsARPLen_Type = Counter32
_AgDosPortStatsARPLen_Object = MibTableColumn
agDosPortStatsARPLen = _AgDosPortStatsARPLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 59),
    _AgDosPortStatsARPLen_Type()
)
agDosPortStatsARPLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsARPLen.setStatus("current")
_AgDosPortStatsARPNbCast_Type = Counter32
_AgDosPortStatsARPNbCast_Object = MibTableColumn
agDosPortStatsARPNbCast = _AgDosPortStatsARPNbCast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 60),
    _AgDosPortStatsARPNbCast_Type()
)
agDosPortStatsARPNbCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsARPNbCast.setStatus("current")
_AgDosPortStatsARPNuCast_Type = Counter32
_AgDosPortStatsARPNuCast_Object = MibTableColumn
agDosPortStatsARPNuCast = _AgDosPortStatsARPNuCast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 61),
    _AgDosPortStatsARPNuCast_Type()
)
agDosPortStatsARPNuCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsARPNuCast.setStatus("current")
_AgDosPortStatsARPSpoof_Type = Counter32
_AgDosPortStatsARPSpoof_Object = MibTableColumn
agDosPortStatsARPSpoof = _AgDosPortStatsARPSpoof_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 62),
    _AgDosPortStatsARPSpoof_Type()
)
agDosPortStatsARPSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsARPSpoof.setStatus("current")
_AgDosPortStatsGARP_Type = Counter32
_AgDosPortStatsGARP_Object = MibTableColumn
agDosPortStatsGARP = _AgDosPortStatsGARP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 63),
    _AgDosPortStatsGARP_Type()
)
agDosPortStatsGARP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsGARP.setStatus("current")
_AgDosPortStatsIP6Len_Type = Counter32
_AgDosPortStatsIP6Len_Object = MibTableColumn
agDosPortStatsIP6Len = _AgDosPortStatsIP6Len_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 64),
    _AgDosPortStatsIP6Len_Type()
)
agDosPortStatsIP6Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIP6Len.setStatus("current")
_AgDosPortStatsIP6Version_Type = Counter32
_AgDosPortStatsIP6Version_Object = MibTableColumn
agDosPortStatsIP6Version = _AgDosPortStatsIP6Version_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 1, 1, 65),
    _AgDosPortStatsIP6Version_Type()
)
agDosPortStatsIP6Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDosPortStatsIP6Version.setStatus("current")
_AgSecurityPgrpStatsTable_Object = MibTable
agSecurityPgrpStatsTable = _AgSecurityPgrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    agSecurityPgrpStatsTable.setStatus("current")
_AgSecurityPgrpStatsTableEntry_Object = MibTableRow
agSecurityPgrpStatsTableEntry = _AgSecurityPgrpStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 2, 1)
)
agSecurityPgrpStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agSecurityPgrpStatsIndx"),
)
if mibBuilder.loadTexts:
    agSecurityPgrpStatsTableEntry.setStatus("current")
_AgSecurityPgrpStatsIndx_Type = Integer32
_AgSecurityPgrpStatsIndx_Object = MibTableColumn
agSecurityPgrpStatsIndx = _AgSecurityPgrpStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 2, 1, 1),
    _AgSecurityPgrpStatsIndx_Type()
)
agSecurityPgrpStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityPgrpStatsIndx.setStatus("current")
_AgSecurityPgrpStatsName_Type = DisplayString
_AgSecurityPgrpStatsName_Object = MibTableColumn
agSecurityPgrpStatsName = _AgSecurityPgrpStatsName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 2, 1, 2),
    _AgSecurityPgrpStatsName_Type()
)
agSecurityPgrpStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityPgrpStatsName.setStatus("current")
_AgSecurityPgrpStatsHits_Type = Counter32
_AgSecurityPgrpStatsHits_Object = MibTableColumn
agSecurityPgrpStatsHits = _AgSecurityPgrpStatsHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 2, 1, 3),
    _AgSecurityPgrpStatsHits_Type()
)
agSecurityPgrpStatsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityPgrpStatsHits.setStatus("current")
_AgSecurityUbStatsTable_Object = MibTable
agSecurityUbStatsTable = _AgSecurityUbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    agSecurityUbStatsTable.setStatus("current")
_AgSecurityUbStatsTableEntry_Object = MibTableRow
agSecurityUbStatsTableEntry = _AgSecurityUbStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 3, 1)
)
agSecurityUbStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agSecurityUbStatsIndx"),
)
if mibBuilder.loadTexts:
    agSecurityUbStatsTableEntry.setStatus("current")
_AgSecurityUbStatsIndx_Type = Integer32
_AgSecurityUbStatsIndx_Object = MibTableColumn
agSecurityUbStatsIndx = _AgSecurityUbStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 3, 1, 1),
    _AgSecurityUbStatsIndx_Type()
)
agSecurityUbStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityUbStatsIndx.setStatus("current")
_AgSecurityUbStatsPort_Type = Integer32
_AgSecurityUbStatsPort_Object = MibTableColumn
agSecurityUbStatsPort = _AgSecurityUbStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 3, 1, 2),
    _AgSecurityUbStatsPort_Type()
)
agSecurityUbStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityUbStatsPort.setStatus("current")
_AgSecurityUbStatsBlockedPacket_Type = Counter32
_AgSecurityUbStatsBlockedPacket_Object = MibTableColumn
agSecurityUbStatsBlockedPacket = _AgSecurityUbStatsBlockedPacket_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 3, 1, 3),
    _AgSecurityUbStatsBlockedPacket_Type()
)
agSecurityUbStatsBlockedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityUbStatsBlockedPacket.setStatus("current")
_AgSecurityUbStatsPacketRate_Type = Counter32
_AgSecurityUbStatsPacketRate_Object = MibTableColumn
agSecurityUbStatsPacketRate = _AgSecurityUbStatsPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 3, 1, 4),
    _AgSecurityUbStatsPacketRate_Type()
)
agSecurityUbStatsPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityUbStatsPacketRate.setStatus("current")
_AgSecurityIpAclStatsTable_Object = MibTable
agSecurityIpAclStatsTable = _AgSecurityIpAclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    agSecurityIpAclStatsTable.setStatus("current")
_AgSecurityIpAclStatsTableEntry_Object = MibTableRow
agSecurityIpAclStatsTableEntry = _AgSecurityIpAclStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 4, 1)
)
agSecurityIpAclStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agSecurityIpAclStatsIndx"),
)
if mibBuilder.loadTexts:
    agSecurityIpAclStatsTableEntry.setStatus("current")
_AgSecurityIpAclStatsIndx_Type = Integer32
_AgSecurityIpAclStatsIndx_Object = MibTableColumn
agSecurityIpAclStatsIndx = _AgSecurityIpAclStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 4, 1, 1),
    _AgSecurityIpAclStatsIndx_Type()
)
agSecurityIpAclStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityIpAclStatsIndx.setStatus("current")
_AgSecurityIpAclStatsAddress_Type = IpAddress
_AgSecurityIpAclStatsAddress_Object = MibTableColumn
agSecurityIpAclStatsAddress = _AgSecurityIpAclStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 4, 1, 2),
    _AgSecurityIpAclStatsAddress_Type()
)
agSecurityIpAclStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityIpAclStatsAddress.setStatus("current")
_AgSecurityIpAclStatsBlockedPacket_Type = Counter32
_AgSecurityIpAclStatsBlockedPacket_Object = MibTableColumn
agSecurityIpAclStatsBlockedPacket = _AgSecurityIpAclStatsBlockedPacket_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 4, 1, 3),
    _AgSecurityIpAclStatsBlockedPacket_Type()
)
agSecurityIpAclStatsBlockedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityIpAclStatsBlockedPacket.setStatus("current")
_AgSecurityIpDstAclStatsTable_Object = MibTable
agSecurityIpDstAclStatsTable = _AgSecurityIpDstAclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    agSecurityIpDstAclStatsTable.setStatus("current")
_AgSecurityIpDstAclStatsTableEntry_Object = MibTableRow
agSecurityIpDstAclStatsTableEntry = _AgSecurityIpDstAclStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 5, 1)
)
agSecurityIpDstAclStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agSecurityIpDstAclStatsIndx"),
)
if mibBuilder.loadTexts:
    agSecurityIpDstAclStatsTableEntry.setStatus("current")
_AgSecurityIpDstAclStatsIndx_Type = Integer32
_AgSecurityIpDstAclStatsIndx_Object = MibTableColumn
agSecurityIpDstAclStatsIndx = _AgSecurityIpDstAclStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 5, 1, 1),
    _AgSecurityIpDstAclStatsIndx_Type()
)
agSecurityIpDstAclStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityIpDstAclStatsIndx.setStatus("current")
_AgSecurityIpDstAclStatsAddress_Type = IpAddress
_AgSecurityIpDstAclStatsAddress_Object = MibTableColumn
agSecurityIpDstAclStatsAddress = _AgSecurityIpDstAclStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 5, 1, 2),
    _AgSecurityIpDstAclStatsAddress_Type()
)
agSecurityIpDstAclStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityIpDstAclStatsAddress.setStatus("current")
_AgSecurityIpDstAclStatsBlockedPacket_Type = Counter32
_AgSecurityIpDstAclStatsBlockedPacket_Object = MibTableColumn
agSecurityIpDstAclStatsBlockedPacket = _AgSecurityIpDstAclStatsBlockedPacket_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 5, 1, 3),
    _AgSecurityIpDstAclStatsBlockedPacket_Type()
)
agSecurityIpDstAclStatsBlockedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecurityIpDstAclStatsBlockedPacket.setStatus("current")
_SymantecStats_ObjectIdentity = ObjectIdentity
symantecStats = _SymantecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6)
)
_SymStatsTotalHits_Type = Counter32
_SymStatsTotalHits_Object = MibScalar
symStatsTotalHits = _SymStatsTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 1),
    _SymStatsTotalHits_Type()
)
symStatsTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsTotalHits.setStatus("current")


class _SymStatsClear_Type(Integer32):
    """Custom type symStatsClear based on Integer32"""
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


_SymStatsClear_Type.__name__ = "Integer32"
_SymStatsClear_Object = MibScalar
symStatsClear = _SymStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 2),
    _SymStatsClear_Type()
)
symStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    symStatsClear.setStatus("current")
_SymStatsSourceIp_Type = IpAddress
_SymStatsSourceIp_Object = MibScalar
symStatsSourceIp = _SymStatsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 3),
    _SymStatsSourceIp_Type()
)
symStatsSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsSourceIp.setStatus("current")
_SymStatsSourcePort_Type = Integer32
_SymStatsSourcePort_Object = MibScalar
symStatsSourcePort = _SymStatsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 4),
    _SymStatsSourcePort_Type()
)
symStatsSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsSourcePort.setStatus("current")
_SymStatsDestIp_Type = IpAddress
_SymStatsDestIp_Object = MibScalar
symStatsDestIp = _SymStatsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 5),
    _SymStatsDestIp_Type()
)
symStatsDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsDestIp.setStatus("current")
_SymStatsDestPort_Type = Integer32
_SymStatsDestPort_Object = MibScalar
symStatsDestPort = _SymStatsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 6),
    _SymStatsDestPort_Type()
)
symStatsDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsDestPort.setStatus("current")


class _SymStatsProtocol_Type(DisplayString):
    """Custom type symStatsProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SymStatsProtocol_Type.__name__ = "DisplayString"
_SymStatsProtocol_Object = MibScalar
symStatsProtocol = _SymStatsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 7),
    _SymStatsProtocol_Type()
)
symStatsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsProtocol.setStatus("current")
_SymStatsLastHitId_Type = Integer32
_SymStatsLastHitId_Object = MibScalar
symStatsLastHitId = _SymStatsLastHitId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 8),
    _SymStatsLastHitId_Type()
)
symStatsLastHitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsLastHitId.setStatus("current")
_SymStatsConfiguredHitsMax_Type = Integer32
_SymStatsConfiguredHitsMax_Object = MibScalar
symStatsConfiguredHitsMax = _SymStatsConfiguredHitsMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 9),
    _SymStatsConfiguredHitsMax_Type()
)
symStatsConfiguredHitsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsMax.setStatus("current")
_SymStatsConfiguredHitsTable_Object = MibTable
symStatsConfiguredHitsTable = _SymStatsConfiguredHitsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10)
)
if mibBuilder.loadTexts:
    symStatsConfiguredHitsTable.setStatus("current")
_SymStatsConfiguredHitsTableEntry_Object = MibTableRow
symStatsConfiguredHitsTableEntry = _SymStatsConfiguredHitsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10, 1)
)
symStatsConfiguredHitsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symStatsConfiguredHitsTblIndex"),
)
if mibBuilder.loadTexts:
    symStatsConfiguredHitsTableEntry.setStatus("current")
_SymStatsConfiguredHitsTblIndex_Type = Integer32
_SymStatsConfiguredHitsTblIndex_Object = MibTableColumn
symStatsConfiguredHitsTblIndex = _SymStatsConfiguredHitsTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10, 1, 1),
    _SymStatsConfiguredHitsTblIndex_Type()
)
symStatsConfiguredHitsTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsTblIndex.setStatus("current")
_SymStatsConfiguredHitsSigId_Type = Integer32
_SymStatsConfiguredHitsSigId_Object = MibTableColumn
symStatsConfiguredHitsSigId = _SymStatsConfiguredHitsSigId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10, 1, 2),
    _SymStatsConfiguredHitsSigId_Type()
)
symStatsConfiguredHitsSigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsSigId.setStatus("current")
_SymStatsConfiguredHitsTotalSpHCount_Type = Counter32
_SymStatsConfiguredHitsTotalSpHCount_Object = MibTableColumn
symStatsConfiguredHitsTotalSpHCount = _SymStatsConfiguredHitsTotalSpHCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10, 1, 3),
    _SymStatsConfiguredHitsTotalSpHCount_Type()
)
symStatsConfiguredHitsTotalSpHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsTotalSpHCount.setStatus("current")
_SymStatsConfiguredHitsInCont_Type = Counter32
_SymStatsConfiguredHitsInCont_Object = MibTableColumn
symStatsConfiguredHitsInCont = _SymStatsConfiguredHitsInCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10, 1, 4),
    _SymStatsConfiguredHitsInCont_Type()
)
symStatsConfiguredHitsInCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsInCont.setStatus("current")
_SymStatsConfiguredHitsOutCont_Type = Counter32
_SymStatsConfiguredHitsOutCont_Object = MibTableColumn
symStatsConfiguredHitsOutCont = _SymStatsConfiguredHitsOutCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10, 1, 5),
    _SymStatsConfiguredHitsOutCont_Type()
)
symStatsConfiguredHitsOutCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsOutCont.setStatus("current")


class _SymStatsConfiguredHitsLastHitTime_Type(DisplayString):
    """Custom type symStatsConfiguredHitsLastHitTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SymStatsConfiguredHitsLastHitTime_Type.__name__ = "DisplayString"
_SymStatsConfiguredHitsLastHitTime_Object = MibTableColumn
symStatsConfiguredHitsLastHitTime = _SymStatsConfiguredHitsLastHitTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 10, 1, 6),
    _SymStatsConfiguredHitsLastHitTime_Type()
)
symStatsConfiguredHitsLastHitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsLastHitTime.setStatus("current")
_SymStatsConfiguredHitsCountOnSpTable_Object = MibTable
symStatsConfiguredHitsCountOnSpTable = _SymStatsConfiguredHitsCountOnSpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 11)
)
if mibBuilder.loadTexts:
    symStatsConfiguredHitsCountOnSpTable.setStatus("current")
_SymStatsConfiguredHitsCountOnSpTableEntry_Object = MibTableRow
symStatsConfiguredHitsCountOnSpTableEntry = _SymStatsConfiguredHitsCountOnSpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 11, 1)
)
symStatsConfiguredHitsCountOnSpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symStatsConfiguredHitsCountOnSpTblIndex"),
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symStatsConfiguredHitsCountOnSpTblSpIndex"),
)
if mibBuilder.loadTexts:
    symStatsConfiguredHitsCountOnSpTableEntry.setStatus("current")
_SymStatsConfiguredHitsCountOnSpTblIndex_Type = Integer32
_SymStatsConfiguredHitsCountOnSpTblIndex_Object = MibTableColumn
symStatsConfiguredHitsCountOnSpTblIndex = _SymStatsConfiguredHitsCountOnSpTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 11, 1, 1),
    _SymStatsConfiguredHitsCountOnSpTblIndex_Type()
)
symStatsConfiguredHitsCountOnSpTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsCountOnSpTblIndex.setStatus("current")
_SymStatsConfiguredHitsCountOnSpTblSpIndex_Type = Integer32
_SymStatsConfiguredHitsCountOnSpTblSpIndex_Object = MibTableColumn
symStatsConfiguredHitsCountOnSpTblSpIndex = _SymStatsConfiguredHitsCountOnSpTblSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 11, 1, 2),
    _SymStatsConfiguredHitsCountOnSpTblSpIndex_Type()
)
symStatsConfiguredHitsCountOnSpTblSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsCountOnSpTblSpIndex.setStatus("current")
_SymStatsConfiguredHitsCountOnSpTblHitCount_Type = Counter32
_SymStatsConfiguredHitsCountOnSpTblHitCount_Object = MibTableColumn
symStatsConfiguredHitsCountOnSpTblHitCount = _SymStatsConfiguredHitsCountOnSpTblHitCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 11, 1, 3),
    _SymStatsConfiguredHitsCountOnSpTblHitCount_Type()
)
symStatsConfiguredHitsCountOnSpTblHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsConfiguredHitsCountOnSpTblHitCount.setStatus("current")
_SymStatsUnconfiguredHitsMax_Type = Integer32
_SymStatsUnconfiguredHitsMax_Object = MibScalar
symStatsUnconfiguredHitsMax = _SymStatsUnconfiguredHitsMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 12),
    _SymStatsUnconfiguredHitsMax_Type()
)
symStatsUnconfiguredHitsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsMax.setStatus("current")
_SymStatsUnconfiguredHitsTable_Object = MibTable
symStatsUnconfiguredHitsTable = _SymStatsUnconfiguredHitsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 13)
)
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsTable.setStatus("current")
_SymStatsUnconfiguredHitsTableEntry_Object = MibTableRow
symStatsUnconfiguredHitsTableEntry = _SymStatsUnconfiguredHitsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 13, 1)
)
symStatsUnconfiguredHitsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symStatsUnconfiguredHitsTblIndex"),
)
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsTableEntry.setStatus("current")
_SymStatsUnconfiguredHitsTblIndex_Type = Integer32
_SymStatsUnconfiguredHitsTblIndex_Object = MibTableColumn
symStatsUnconfiguredHitsTblIndex = _SymStatsUnconfiguredHitsTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 13, 1, 1),
    _SymStatsUnconfiguredHitsTblIndex_Type()
)
symStatsUnconfiguredHitsTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsTblIndex.setStatus("current")
_SymStatsUnconfiguredHitsSigId_Type = Integer32
_SymStatsUnconfiguredHitsSigId_Object = MibTableColumn
symStatsUnconfiguredHitsSigId = _SymStatsUnconfiguredHitsSigId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 13, 1, 2),
    _SymStatsUnconfiguredHitsSigId_Type()
)
symStatsUnconfiguredHitsSigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsSigId.setStatus("current")
_SymStatsUnconfiguredHitsTotalSpHCount_Type = Counter32
_SymStatsUnconfiguredHitsTotalSpHCount_Object = MibTableColumn
symStatsUnconfiguredHitsTotalSpHCount = _SymStatsUnconfiguredHitsTotalSpHCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 13, 1, 3),
    _SymStatsUnconfiguredHitsTotalSpHCount_Type()
)
symStatsUnconfiguredHitsTotalSpHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsTotalSpHCount.setStatus("current")


class _SymStatsUnconfiguredHitsLastHitTime_Type(DisplayString):
    """Custom type symStatsUnconfiguredHitsLastHitTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SymStatsUnconfiguredHitsLastHitTime_Type.__name__ = "DisplayString"
_SymStatsUnconfiguredHitsLastHitTime_Object = MibTableColumn
symStatsUnconfiguredHitsLastHitTime = _SymStatsUnconfiguredHitsLastHitTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 13, 1, 4),
    _SymStatsUnconfiguredHitsLastHitTime_Type()
)
symStatsUnconfiguredHitsLastHitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsLastHitTime.setStatus("current")
_SymStatsUnconfiguredHitsCountOnSpTable_Object = MibTable
symStatsUnconfiguredHitsCountOnSpTable = _SymStatsUnconfiguredHitsCountOnSpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 14)
)
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsCountOnSpTable.setStatus("current")
_SymStatsUnconfiguredHitsCountOnSpTableEntry_Object = MibTableRow
symStatsUnconfiguredHitsCountOnSpTableEntry = _SymStatsUnconfiguredHitsCountOnSpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 14, 1)
)
symStatsUnconfiguredHitsCountOnSpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symStatsUnconfiguredHitsCountOnSpTblIndex"),
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symStatsUnconfiguredHitsCountOnSpTblSpIndex"),
)
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsCountOnSpTableEntry.setStatus("current")
_SymStatsUnconfiguredHitsCountOnSpTblIndex_Type = Integer32
_SymStatsUnconfiguredHitsCountOnSpTblIndex_Object = MibTableColumn
symStatsUnconfiguredHitsCountOnSpTblIndex = _SymStatsUnconfiguredHitsCountOnSpTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 14, 1, 1),
    _SymStatsUnconfiguredHitsCountOnSpTblIndex_Type()
)
symStatsUnconfiguredHitsCountOnSpTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsCountOnSpTblIndex.setStatus("current")
_SymStatsUnconfiguredHitsCountOnSpTblSpIndex_Type = Integer32
_SymStatsUnconfiguredHitsCountOnSpTblSpIndex_Object = MibTableColumn
symStatsUnconfiguredHitsCountOnSpTblSpIndex = _SymStatsUnconfiguredHitsCountOnSpTblSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 14, 1, 2),
    _SymStatsUnconfiguredHitsCountOnSpTblSpIndex_Type()
)
symStatsUnconfiguredHitsCountOnSpTblSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsCountOnSpTblSpIndex.setStatus("current")
_SymStatsUnconfiguredHitsCountOnSpTblHitCount_Type = Counter32
_SymStatsUnconfiguredHitsCountOnSpTblHitCount_Object = MibTableColumn
symStatsUnconfiguredHitsCountOnSpTblHitCount = _SymStatsUnconfiguredHitsCountOnSpTblHitCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 6, 6, 14, 1, 3),
    _SymStatsUnconfiguredHitsCountOnSpTblHitCount_Type()
)
symStatsUnconfiguredHitsCountOnSpTblHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symStatsUnconfiguredHitsCountOnSpTblHitCount.setStatus("current")
_AgClearStats_ObjectIdentity = ObjectIdentity
agClearStats = _AgClearStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 7)
)


class _SnmpClearStats_Type(Integer32):
    """Custom type snmpClearStats based on Integer32"""
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


_SnmpClearStats_Type.__name__ = "Integer32"
_SnmpClearStats_Object = MibScalar
snmpClearStats = _SnmpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 7, 1),
    _SnmpClearStats_Type()
)
snmpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpClearStats.setStatus("current")
_MpMemStats_ObjectIdentity = ObjectIdentity
mpMemStats = _MpMemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 8)
)
_MpMemStatsTotal_Type = Integer32
_MpMemStatsTotal_Object = MibScalar
mpMemStatsTotal = _MpMemStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 8, 1),
    _MpMemStatsTotal_Type()
)
mpMemStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpMemStatsTotal.setStatus("current")
_MpMemStatsUsed_Type = Integer32
_MpMemStatsUsed_Object = MibScalar
mpMemStatsUsed = _MpMemStatsUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 8, 2),
    _MpMemStatsUsed_Type()
)
mpMemStatsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpMemStatsUsed.setStatus("current")
_MpMemStatsFree_Type = Integer32
_MpMemStatsFree_Object = MibScalar
mpMemStatsFree = _MpMemStatsFree_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 8, 3),
    _MpMemStatsFree_Type()
)
mpMemStatsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpMemStatsFree.setStatus("current")
_MpMemStatsLowFree_Type = Integer32
_MpMemStatsLowFree_Object = MibScalar
mpMemStatsLowFree = _MpMemStatsLowFree_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 8, 4),
    _MpMemStatsLowFree_Type()
)
mpMemStatsLowFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpMemStatsLowFree.setStatus("current")
_NtpStats_ObjectIdentity = ObjectIdentity
ntpStats = _NtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9)
)
_NtpPrimaryServerReqSent_Type = Integer32
_NtpPrimaryServerReqSent_Object = MibScalar
ntpPrimaryServerReqSent = _NtpPrimaryServerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 1),
    _NtpPrimaryServerReqSent_Type()
)
ntpPrimaryServerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPrimaryServerReqSent.setStatus("current")
_NtpPrimaryServerRespRcvd_Type = Integer32
_NtpPrimaryServerRespRcvd_Object = MibScalar
ntpPrimaryServerRespRcvd = _NtpPrimaryServerRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 2),
    _NtpPrimaryServerRespRcvd_Type()
)
ntpPrimaryServerRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPrimaryServerRespRcvd.setStatus("current")
_NtpPrimaryServerUpdates_Type = Integer32
_NtpPrimaryServerUpdates_Object = MibScalar
ntpPrimaryServerUpdates = _NtpPrimaryServerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 3),
    _NtpPrimaryServerUpdates_Type()
)
ntpPrimaryServerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPrimaryServerUpdates.setStatus("current")
_NtpSecondaryServerReqSent_Type = Integer32
_NtpSecondaryServerReqSent_Object = MibScalar
ntpSecondaryServerReqSent = _NtpSecondaryServerReqSent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 4),
    _NtpSecondaryServerReqSent_Type()
)
ntpSecondaryServerReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSecondaryServerReqSent.setStatus("current")
_NtpSecondaryServerRespRcvd_Type = Integer32
_NtpSecondaryServerRespRcvd_Object = MibScalar
ntpSecondaryServerRespRcvd = _NtpSecondaryServerRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 5),
    _NtpSecondaryServerRespRcvd_Type()
)
ntpSecondaryServerRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSecondaryServerRespRcvd.setStatus("current")
_NtpSecondaryServerUpdates_Type = Integer32
_NtpSecondaryServerUpdates_Object = MibScalar
ntpSecondaryServerUpdates = _NtpSecondaryServerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 9, 10),
    _NtpSystemCurrentTime_Type()
)
ntpSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSystemCurrentTime.setStatus("current")
_PortMirrorStats_ObjectIdentity = ObjectIdentity
portMirrorStats = _PortMirrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11)
)
_PortMirrorStatsTable_Object = MibTable
portMirrorStatsTable = _PortMirrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    portMirrorStatsTable.setStatus("current")
_PortMirrorStatsTableEntry_Object = MibTableRow
portMirrorStatsTableEntry = _PortMirrorStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11, 1, 1)
)
portMirrorStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "portMirrorStatsIndx"),
)
if mibBuilder.loadTexts:
    portMirrorStatsTableEntry.setStatus("current")
_PortMirrorStatsIndx_Type = Integer32
_PortMirrorStatsIndx_Object = MibTableColumn
portMirrorStatsIndx = _PortMirrorStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11, 1, 1, 1),
    _PortMirrorStatsIndx_Type()
)
portMirrorStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMirrorStatsIndx.setStatus("current")
_PortMirrorStatsIngress_Type = Counter32
_PortMirrorStatsIngress_Object = MibTableColumn
portMirrorStatsIngress = _PortMirrorStatsIngress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11, 1, 1, 2),
    _PortMirrorStatsIngress_Type()
)
portMirrorStatsIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMirrorStatsIngress.setStatus("current")
_PortMirrorStatsEgress_Type = Counter32
_PortMirrorStatsEgress_Object = MibTableColumn
portMirrorStatsEgress = _PortMirrorStatsEgress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11, 1, 1, 3),
    _PortMirrorStatsEgress_Type()
)
portMirrorStatsEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMirrorStatsEgress.setStatus("current")
_PortMirrorClear_ObjectIdentity = ObjectIdentity
portMirrorClear = _PortMirrorClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11, 2)
)


class _PortMirrorStatsClear_Type(Integer32):
    """Custom type portMirrorStatsClear based on Integer32"""
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


_PortMirrorStatsClear_Type.__name__ = "Integer32"
_PortMirrorStatsClear_Object = MibScalar
portMirrorStatsClear = _PortMirrorStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 2, 11, 2, 1),
    _PortMirrorStatsClear_Type()
)
portMirrorStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMirrorStatsClear.setStatus("current")
_AgentInfo_ObjectIdentity = ObjectIdentity
agentInfo = _AgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 2),
    _HwRevision_Type()
)
hwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRevision.setStatus("current")


class _HwTemperatureStatus_Type(Integer32):
    """Custom type hwTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exceed", 2),
          ("ok", 1))
    )


_HwTemperatureStatus_Type.__name__ = "Integer32"
_HwTemperatureStatus_Object = MibScalar
hwTemperatureStatus = _HwTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 3),
    _HwTemperatureStatus_Type()
)
hwTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemperatureStatus.setStatus("current")


class _HwFanStatus_Type(Integer32):
    """Custom type hwFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_HwFanStatus_Type.__name__ = "Integer32"
_HwFanStatus_Object = MibScalar
hwFanStatus = _HwFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 4),
    _HwFanStatus_Type()
)
hwFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFanStatus.setStatus("current")


class _HwOrderNumber_Type(DisplayString):
    """Custom type hwOrderNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwOrderNumber_Type.__name__ = "DisplayString"
_HwOrderNumber_Object = MibScalar
hwOrderNumber = _HwOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 5),
    _HwOrderNumber_Type()
)
hwOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOrderNumber.setStatus("current")


class _HwMainBoardNumber_Type(DisplayString):
    """Custom type hwMainBoardNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwMainBoardNumber_Type.__name__ = "DisplayString"
_HwMainBoardNumber_Object = MibScalar
hwMainBoardNumber = _HwMainBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 6),
    _HwMainBoardNumber_Type()
)
hwMainBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMainBoardNumber.setStatus("current")


class _HwMainBoardRevision_Type(DisplayString):
    """Custom type hwMainBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwMainBoardRevision_Type.__name__ = "DisplayString"
_HwMainBoardRevision_Object = MibScalar
hwMainBoardRevision = _HwMainBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 7),
    _HwMainBoardRevision_Type()
)
hwMainBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMainBoardRevision.setStatus("current")


class _HwEthernetBoardNumber_Type(DisplayString):
    """Custom type hwEthernetBoardNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwEthernetBoardNumber_Type.__name__ = "DisplayString"
_HwEthernetBoardNumber_Object = MibScalar
hwEthernetBoardNumber = _HwEthernetBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 8),
    _HwEthernetBoardNumber_Type()
)
hwEthernetBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetBoardNumber.setStatus("current")


class _HwEthernetBoardRevision_Type(DisplayString):
    """Custom type hwEthernetBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwEthernetBoardRevision_Type.__name__ = "DisplayString"
_HwEthernetBoardRevision_Object = MibScalar
hwEthernetBoardRevision = _HwEthernetBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 9),
    _HwEthernetBoardRevision_Type()
)
hwEthernetBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetBoardRevision.setStatus("current")


class _HwChassisSerialNumber_Type(DisplayString):
    """Custom type hwChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwChassisSerialNumber_Type.__name__ = "DisplayString"
_HwChassisSerialNumber_Object = MibScalar
hwChassisSerialNumber = _HwChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 10),
    _HwChassisSerialNumber_Type()
)
hwChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChassisSerialNumber.setStatus("current")


class _HwChassisRevision_Type(DisplayString):
    """Custom type hwChassisRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwChassisRevision_Type.__name__ = "DisplayString"
_HwChassisRevision_Object = MibScalar
hwChassisRevision = _HwChassisRevision_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 11),
    _HwChassisRevision_Type()
)
hwChassisRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChassisRevision.setStatus("current")


class _HwPower_Type(Integer32):
    """Custom type hwPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_HwPower_Type.__name__ = "Integer32"
_HwPower_Object = MibScalar
hwPower = _HwPower_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 1, 24),
    _HwPower_Type()
)
hwPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPower.setStatus("current")
_PortInfo_ObjectIdentity = ObjectIdentity
portInfo = _PortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2)
)
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("current")
_PortInfoTableEntry_Object = MibTableRow
portInfoTableEntry = _PortInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1)
)
portInfoTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "portInfoIndx"),
)
if mibBuilder.loadTexts:
    portInfoTableEntry.setStatus("current")
_PortInfoIndx_Type = Integer32
_PortInfoIndx_Object = MibTableColumn
portInfoIndx = _PortInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 7),
    _PortInfoPhyIfType_Type()
)
portInfoPhyIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfType.setStatus("current")
_PortInfoPhyIfMtu_Type = Integer32
_PortInfoPhyIfMtu_Object = MibTableColumn
portInfoPhyIfMtu = _PortInfoPhyIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 8),
    _PortInfoPhyIfMtu_Type()
)
portInfoPhyIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfMtu.setStatus("current")
_PortInfoPhyIfPhysAddress_Type = PhysAddress
_PortInfoPhyIfPhysAddress_Object = MibTableColumn
portInfoPhyIfPhysAddress = _PortInfoPhyIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 10),
    _PortInfoPhyIfOperStatus_Type()
)
portInfoPhyIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfOperStatus.setStatus("current")
_PortInfoPhyIfLastChange_Type = TimeTicks
_PortInfoPhyIfLastChange_Object = MibTableColumn
portInfoPhyIfLastChange = _PortInfoPhyIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 11),
    _PortInfoPhyIfLastChange_Type()
)
portInfoPhyIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfLastChange.setStatus("current")


class _PortInfoPhyConnType_Type(Integer32):
    """Custom type portInfoPhyConnType based on Integer32"""
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
        *(("feCopper", 1),
          ("geCopper", 2),
          ("geSFP", 3),
          ("unknown", 4))
    )


_PortInfoPhyConnType_Type.__name__ = "Integer32"
_PortInfoPhyConnType_Object = MibTableColumn
portInfoPhyConnType = _PortInfoPhyConnType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 12),
    _PortInfoPhyConnType_Type()
)
portInfoPhyConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyConnType.setStatus("current")


class _PortInfoPreferred_Type(Integer32):
    """Custom type portInfoPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("invalid", 1),
          ("sfp", 3))
    )


_PortInfoPreferred_Type.__name__ = "Integer32"
_PortInfoPreferred_Object = MibTableColumn
portInfoPreferred = _PortInfoPreferred_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 13),
    _PortInfoPreferred_Type()
)
portInfoPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPreferred.setStatus("current")


class _PortInfoBackup_Type(Integer32):
    """Custom type portInfoBackup based on Integer32"""
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
        *(("copper", 3),
          ("invalid", 1),
          ("none", 2),
          ("sfp", 4))
    )


_PortInfoBackup_Type.__name__ = "Integer32"
_PortInfoBackup_Object = MibTableColumn
portInfoBackup = _PortInfoBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 14),
    _PortInfoBackup_Type()
)
portInfoBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoBackup.setStatus("current")


class _PortInfoSFPName_Type(DisplayString):
    """Custom type portInfoSFPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortInfoSFPName_Type.__name__ = "DisplayString"
_PortInfoSFPName_Object = MibTableColumn
portInfoSFPName = _PortInfoSFPName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 15),
    _PortInfoSFPName_Type()
)
portInfoSFPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSFPName.setStatus("current")


class _PortInfoSFPType_Type(Integer32):
    """Custom type portInfoSFPType based on Integer32"""
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
        *(("invalid", 1),
          ("sfpTypeCX", 4),
          ("sfpTypeCopper", 5),
          ("sfpTypeLX", 3),
          ("sfpTypeSX", 2))
    )


_PortInfoSFPType_Type.__name__ = "Integer32"
_PortInfoSFPType_Object = MibTableColumn
portInfoSFPType = _PortInfoSFPType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 2, 1, 1, 17),
    _PortInfoSFPType_Type()
)
portInfoSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSFPType.setStatus("current")
_SwKeyInfo_ObjectIdentity = ObjectIdentity
swKeyInfo = _SwKeyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3)
)
_AgEnabledSwFeatures_Type = DisplayString
_AgEnabledSwFeatures_Object = MibScalar
agEnabledSwFeatures = _AgEnabledSwFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 1),
    _AgEnabledSwFeatures_Type()
)
agEnabledSwFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledSwFeatures.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 2),
    _AgEnabledGslbKey_Type()
)
agEnabledGslbKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledGslbKey.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 3),
    _AgEnabledBwmKey_Type()
)
agEnabledBwmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledBwmKey.setStatus("current")


class _AgEnabledSecurityKey_Type(Integer32):
    """Custom type agEnabledSecurityKey based on Integer32"""
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


_AgEnabledSecurityKey_Type.__name__ = "Integer32"
_AgEnabledSecurityKey_Object = MibScalar
agEnabledSecurityKey = _AgEnabledSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 4),
    _AgEnabledSecurityKey_Type()
)
agEnabledSecurityKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledSecurityKey.setStatus("current")


class _AgEnabledLinklbKey_Type(Integer32):
    """Custom type agEnabledLinklbKey based on Integer32"""
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


_AgEnabledLinklbKey_Type.__name__ = "Integer32"
_AgEnabledLinklbKey_Object = MibScalar
agEnabledLinklbKey = _AgEnabledLinklbKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 6),
    _AgEnabledLinklbKey_Type()
)
agEnabledLinklbKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnabledLinklbKey.setStatus("current")


class _AgSymantecSwKeyInfo_Type(Integer32):
    """Custom type agSymantecSwKeyInfo based on Integer32"""
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
          ("enabled", 1),
          ("expired", 3))
    )


_AgSymantecSwKeyInfo_Type.__name__ = "Integer32"
_AgSymantecSwKeyInfo_Object = MibScalar
agSymantecSwKeyInfo = _AgSymantecSwKeyInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 7),
    _AgSymantecSwKeyInfo_Type()
)
agSymantecSwKeyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSymantecSwKeyInfo.setStatus("current")
_AgSymantecSwKeyRemainingDays_Type = Integer32
_AgSymantecSwKeyRemainingDays_Object = MibScalar
agSymantecSwKeyRemainingDays = _AgSymantecSwKeyRemainingDays_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 8),
    _AgSymantecSwKeyRemainingDays_Type()
)
agSymantecSwKeyRemainingDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSymantecSwKeyRemainingDays.setStatus("current")


class _AgSymLicenseSwKeyRenewalPending_Type(Integer32):
    """Custom type agSymLicenseSwKeyRenewalPending based on Integer32"""
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


_AgSymLicenseSwKeyRenewalPending_Type.__name__ = "Integer32"
_AgSymLicenseSwKeyRenewalPending_Object = MibScalar
agSymLicenseSwKeyRenewalPending = _AgSymLicenseSwKeyRenewalPending_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 3, 9),
    _AgSymLicenseSwKeyRenewalPending_Type()
)
agSymLicenseSwKeyRenewalPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSymLicenseSwKeyRenewalPending.setStatus("current")
_AgDiff_ObjectIdentity = ObjectIdentity
agDiff = _AgDiff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 4)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 4, 2),
    _AgDiffState_Type()
)
agDiffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agDiffState.setStatus("current")
_AgDiffTableSize_Type = Integer32
_AgDiffTableSize_Object = MibScalar
agDiffTableSize = _AgDiffTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 4, 3),
    _AgDiffTableSize_Type()
)
agDiffTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDiffTableSize.setStatus("current")
_AgDiffTable_Object = MibTable
agDiffTable = _AgDiffTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    agDiffTable.setStatus("current")
_AgDiffTableEntry_Object = MibTableRow
agDiffTableEntry = _AgDiffTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 4, 4, 1)
)
agDiffTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agDiffIndex"),
)
if mibBuilder.loadTexts:
    agDiffTableEntry.setStatus("current")
_AgDiffIndex_Type = Integer32
_AgDiffIndex_Object = MibTableColumn
agDiffIndex = _AgDiffIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 4, 4, 1, 1),
    _AgDiffIndex_Type()
)
agDiffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDiffIndex.setStatus("current")
_AgDiffString_Type = OctetString
_AgDiffString_Object = MibTableColumn
agDiffString = _AgDiffString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 4, 4, 1, 2),
    _AgDiffString_Type()
)
agDiffString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDiffString.setStatus("current")
_AgCfgDump_ObjectIdentity = ObjectIdentity
agCfgDump = _AgCfgDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 5)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 5, 2),
    _AgCfgDumpState_Type()
)
agCfgDumpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agCfgDumpState.setStatus("current")
_AgCfgDumpTableSize_Type = Integer32
_AgCfgDumpTableSize_Object = MibScalar
agCfgDumpTableSize = _AgCfgDumpTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 5, 3),
    _AgCfgDumpTableSize_Type()
)
agCfgDumpTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgDumpTableSize.setStatus("current")
_AgCfgDumpTable_Object = MibTable
agCfgDumpTable = _AgCfgDumpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    agCfgDumpTable.setStatus("current")
_AgCfgDumpTableEntry_Object = MibTableRow
agCfgDumpTableEntry = _AgCfgDumpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 5, 4, 1)
)
agCfgDumpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "agCfgDumpIndex"),
)
if mibBuilder.loadTexts:
    agCfgDumpTableEntry.setStatus("current")
_AgCfgDumpIndex_Type = Integer32
_AgCfgDumpIndex_Object = MibTableColumn
agCfgDumpIndex = _AgCfgDumpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 5, 4, 1, 1),
    _AgCfgDumpIndex_Type()
)
agCfgDumpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgDumpIndex.setStatus("current")
_AgCfgDumpString_Type = OctetString
_AgCfgDumpString_Object = MibTableColumn
agCfgDumpString = _AgCfgDumpString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 5, 4, 1, 2),
    _AgCfgDumpString_Type()
)
agCfgDumpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agCfgDumpString.setStatus("current")
_MgmtInfo_ObjectIdentity = ObjectIdentity
mgmtInfo = _MgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 6)
)


class _MgmtPortInfoSpeed_Type(Integer32):
    """Custom type mgmtPortInfoSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("mbs10", 1),
          ("mbs100", 2))
    )


_MgmtPortInfoSpeed_Type.__name__ = "Integer32"
_MgmtPortInfoSpeed_Object = MibScalar
mgmtPortInfoSpeed = _MgmtPortInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 6, 1),
    _MgmtPortInfoSpeed_Type()
)
mgmtPortInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortInfoSpeed.setStatus("current")


class _MgmtPortInfoMode_Type(Integer32):
    """Custom type mgmtPortInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("full-duplex", 1),
          ("half-duplex", 2))
    )


_MgmtPortInfoMode_Type.__name__ = "Integer32"
_MgmtPortInfoMode_Object = MibScalar
mgmtPortInfoMode = _MgmtPortInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 6, 2),
    _MgmtPortInfoMode_Type()
)
mgmtPortInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortInfoMode.setStatus("current")


class _MgmtPortInfoLink_Type(Integer32):
    """Custom type mgmtPortInfoLink based on Integer32"""
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
          ("down", 2),
          ("up", 1))
    )


_MgmtPortInfoLink_Type.__name__ = "Integer32"
_MgmtPortInfoLink_Object = MibScalar
mgmtPortInfoLink = _MgmtPortInfoLink_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 6, 3),
    _MgmtPortInfoLink_Type()
)
mgmtPortInfoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortInfoLink.setStatus("current")
_SecurityInfo_ObjectIdentity = ObjectIdentity
securityInfo = _SecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7)
)
_IpAclBogonInfo_ObjectIdentity = ObjectIdentity
ipAclBogonInfo = _IpAclBogonInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 1)
)
_IpAclBogonInfoTableMaxSize_Type = Integer32
_IpAclBogonInfoTableMaxSize_Object = MibScalar
ipAclBogonInfoTableMaxSize = _IpAclBogonInfoTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 1, 1),
    _IpAclBogonInfoTableMaxSize_Type()
)
ipAclBogonInfoTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclBogonInfoTableMaxSize.setStatus("current")
_IpAclBogonInfoTable_Object = MibTable
ipAclBogonInfoTable = _IpAclBogonInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ipAclBogonInfoTable.setStatus("current")
_IpAclBogonInfoTableEntry_Object = MibTableRow
ipAclBogonInfoTableEntry = _IpAclBogonInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 1, 2, 1)
)
ipAclBogonInfoTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "ipAclBogonInfoIndex"),
)
if mibBuilder.loadTexts:
    ipAclBogonInfoTableEntry.setStatus("current")
_IpAclBogonInfoIndex_Type = Integer32
_IpAclBogonInfoIndex_Object = MibTableColumn
ipAclBogonInfoIndex = _IpAclBogonInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 1, 2, 1, 1),
    _IpAclBogonInfoIndex_Type()
)
ipAclBogonInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclBogonInfoIndex.setStatus("current")
_IpAclBogonInfoIp_Type = IpAddress
_IpAclBogonInfoIp_Object = MibTableColumn
ipAclBogonInfoIp = _IpAclBogonInfoIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 1, 2, 1, 2),
    _IpAclBogonInfoIp_Type()
)
ipAclBogonInfoIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclBogonInfoIp.setStatus("current")
_IpAclBogonInfoMask_Type = IpAddress
_IpAclBogonInfoMask_Object = MibTableColumn
ipAclBogonInfoMask = _IpAclBogonInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 1, 2, 1, 3),
    _IpAclBogonInfoMask_Type()
)
ipAclBogonInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclBogonInfoMask.setStatus("current")
_SymantecInfo_ObjectIdentity = ObjectIdentity
symantecInfo = _SymantecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2)
)


class _SymIpsEngineVersion_Type(DisplayString):
    """Custom type symIpsEngineVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SymIpsEngineVersion_Type.__name__ = "DisplayString"
_SymIpsEngineVersion_Object = MibScalar
symIpsEngineVersion = _SymIpsEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 1),
    _SymIpsEngineVersion_Type()
)
symIpsEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symIpsEngineVersion.setStatus("current")
_SymMatchInfoSpTable_Object = MibTable
symMatchInfoSpTable = _SymMatchInfoSpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    symMatchInfoSpTable.setStatus("current")
_SymMatchInfoSpTableEntry_Object = MibTableRow
symMatchInfoSpTableEntry = _SymMatchInfoSpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1)
)
symMatchInfoSpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symMatchInfoSpTableIndex"),
)
if mibBuilder.loadTexts:
    symMatchInfoSpTableEntry.setStatus("current")
_SymMatchInfoSpTableIndex_Type = Integer32
_SymMatchInfoSpTableIndex_Object = MibTableColumn
symMatchInfoSpTableIndex = _SymMatchInfoSpTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1, 1),
    _SymMatchInfoSpTableIndex_Type()
)
symMatchInfoSpTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpTableIndex.setStatus("current")
_SymMatchInfoSpClientIp_Type = IpAddress
_SymMatchInfoSpClientIp_Object = MibTableColumn
symMatchInfoSpClientIp = _SymMatchInfoSpClientIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1, 2),
    _SymMatchInfoSpClientIp_Type()
)
symMatchInfoSpClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpClientIp.setStatus("current")
_SymMatchInfoSpServerIp_Type = IpAddress
_SymMatchInfoSpServerIp_Object = MibTableColumn
symMatchInfoSpServerIp = _SymMatchInfoSpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1, 3),
    _SymMatchInfoSpServerIp_Type()
)
symMatchInfoSpServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpServerIp.setStatus("current")
_SymMatchInfoSpClientPort_Type = Integer32
_SymMatchInfoSpClientPort_Object = MibTableColumn
symMatchInfoSpClientPort = _SymMatchInfoSpClientPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1, 4),
    _SymMatchInfoSpClientPort_Type()
)
symMatchInfoSpClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpClientPort.setStatus("current")
_SymMatchInfoSpServerPort_Type = Integer32
_SymMatchInfoSpServerPort_Object = MibTableColumn
symMatchInfoSpServerPort = _SymMatchInfoSpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1, 5),
    _SymMatchInfoSpServerPort_Type()
)
symMatchInfoSpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpServerPort.setStatus("current")


class _SymMatchInfoSpProtocol_Type(DisplayString):
    """Custom type symMatchInfoSpProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SymMatchInfoSpProtocol_Type.__name__ = "DisplayString"
_SymMatchInfoSpProtocol_Object = MibTableColumn
symMatchInfoSpProtocol = _SymMatchInfoSpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1, 6),
    _SymMatchInfoSpProtocol_Type()
)
symMatchInfoSpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpProtocol.setStatus("current")
_SymMatchInfoSpNumOfMatches_Type = Integer32
_SymMatchInfoSpNumOfMatches_Object = MibTableColumn
symMatchInfoSpNumOfMatches = _SymMatchInfoSpNumOfMatches_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 2, 1, 7),
    _SymMatchInfoSpNumOfMatches_Type()
)
symMatchInfoSpNumOfMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpNumOfMatches.setStatus("current")
_SymMatchInfoSpSigActTable_Object = MibTable
symMatchInfoSpSigActTable = _SymMatchInfoSpSigActTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 3)
)
if mibBuilder.loadTexts:
    symMatchInfoSpSigActTable.setStatus("current")
_SymMatchInfoSpSigActTableEntry_Object = MibTableRow
symMatchInfoSpSigActTableEntry = _SymMatchInfoSpSigActTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 3, 1)
)
symMatchInfoSpSigActTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symMatchInfoSpSigActTblSpIndex"),
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "symMatchInfoSpSigActTblIndex"),
)
if mibBuilder.loadTexts:
    symMatchInfoSpSigActTableEntry.setStatus("current")
_SymMatchInfoSpSigActTblSpIndex_Type = Integer32
_SymMatchInfoSpSigActTblSpIndex_Object = MibTableColumn
symMatchInfoSpSigActTblSpIndex = _SymMatchInfoSpSigActTblSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 3, 1, 1),
    _SymMatchInfoSpSigActTblSpIndex_Type()
)
symMatchInfoSpSigActTblSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpSigActTblSpIndex.setStatus("current")
_SymMatchInfoSpSigActTblIndex_Type = Integer32
_SymMatchInfoSpSigActTblIndex_Object = MibTableColumn
symMatchInfoSpSigActTblIndex = _SymMatchInfoSpSigActTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 3, 1, 2),
    _SymMatchInfoSpSigActTblIndex_Type()
)
symMatchInfoSpSigActTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpSigActTblIndex.setStatus("current")
_SymMatchInfoSpSigActTblSigId_Type = Integer32
_SymMatchInfoSpSigActTblSigId_Object = MibTableColumn
symMatchInfoSpSigActTblSigId = _SymMatchInfoSpSigActTblSigId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 3, 1, 3),
    _SymMatchInfoSpSigActTblSigId_Type()
)
symMatchInfoSpSigActTblSigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpSigActTblSigId.setStatus("current")


class _SymMatchInfoSpSigActTblAction_Type(DisplayString):
    """Custom type symMatchInfoSpSigActTblAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SymMatchInfoSpSigActTblAction_Type.__name__ = "DisplayString"
_SymMatchInfoSpSigActTblAction_Object = MibTableColumn
symMatchInfoSpSigActTblAction = _SymMatchInfoSpSigActTblAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 7, 2, 3, 1, 4),
    _SymMatchInfoSpSigActTblAction_Type()
)
symMatchInfoSpSigActTblAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symMatchInfoSpSigActTblAction.setStatus("current")
_CapacityInfo_ObjectIdentity = ObjectIdentity
capacityInfo = _CapacityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9)
)
_SwitchCapL2Info_ObjectIdentity = ObjectIdentity
switchCapL2Info = _SwitchCapL2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1)
)
_SwitchCapFDBMaxEnt_Type = Integer32
_SwitchCapFDBMaxEnt_Object = MibScalar
switchCapFDBMaxEnt = _SwitchCapFDBMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 1),
    _SwitchCapFDBMaxEnt_Type()
)
switchCapFDBMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapFDBMaxEnt.setStatus("current")
_SwitchCapFDBCurrEnt_Type = Integer32
_SwitchCapFDBCurrEnt_Object = MibScalar
switchCapFDBCurrEnt = _SwitchCapFDBCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 2),
    _SwitchCapFDBCurrEnt_Type()
)
switchCapFDBCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapFDBCurrEnt.setStatus("current")
_SwitchCapFDBPerSPMaxEnt_Type = Integer32
_SwitchCapFDBPerSPMaxEnt_Object = MibScalar
switchCapFDBPerSPMaxEnt = _SwitchCapFDBPerSPMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 3),
    _SwitchCapFDBPerSPMaxEnt_Type()
)
switchCapFDBPerSPMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapFDBPerSPMaxEnt.setStatus("current")
_SwitchCapVlanMaxEnt_Type = Integer32
_SwitchCapVlanMaxEnt_Object = MibScalar
switchCapVlanMaxEnt = _SwitchCapVlanMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 4),
    _SwitchCapVlanMaxEnt_Type()
)
switchCapVlanMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVlanMaxEnt.setStatus("current")
_SwitchCapVlanCurrEnt_Type = DisplayString
_SwitchCapVlanCurrEnt_Object = MibScalar
switchCapVlanCurrEnt = _SwitchCapVlanCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 5),
    _SwitchCapVlanCurrEnt_Type()
)
switchCapVlanCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVlanCurrEnt.setStatus("current")
_SwitchCapStaticTrunkGrpsMaxEnt_Type = Integer32
_SwitchCapStaticTrunkGrpsMaxEnt_Object = MibScalar
switchCapStaticTrunkGrpsMaxEnt = _SwitchCapStaticTrunkGrpsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 6),
    _SwitchCapStaticTrunkGrpsMaxEnt_Type()
)
switchCapStaticTrunkGrpsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapStaticTrunkGrpsMaxEnt.setStatus("current")
_SwitchCapStaticTrunkGrpsCurrEnt_Type = DisplayString
_SwitchCapStaticTrunkGrpsCurrEnt_Object = MibScalar
switchCapStaticTrunkGrpsCurrEnt = _SwitchCapStaticTrunkGrpsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 7),
    _SwitchCapStaticTrunkGrpsCurrEnt_Type()
)
switchCapStaticTrunkGrpsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapStaticTrunkGrpsCurrEnt.setStatus("current")
_SwitchCapLACPTrunkGRs_Type = Integer32
_SwitchCapLACPTrunkGRs_Object = MibScalar
switchCapLACPTrunkGRs = _SwitchCapLACPTrunkGRs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 8),
    _SwitchCapLACPTrunkGRs_Type()
)
switchCapLACPTrunkGRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapLACPTrunkGRs.setStatus("current")
_SwitchCapTrunksperTrunkGR_Type = Integer32
_SwitchCapTrunksperTrunkGR_Object = MibScalar
switchCapTrunksperTrunkGR = _SwitchCapTrunksperTrunkGR_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 9),
    _SwitchCapTrunksperTrunkGR_Type()
)
switchCapTrunksperTrunkGR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapTrunksperTrunkGR.setStatus("current")
_SwitchCapSTGsMaxEnt_Type = Integer32
_SwitchCapSTGsMaxEnt_Object = MibScalar
switchCapSTGsMaxEnt = _SwitchCapSTGsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 10),
    _SwitchCapSTGsMaxEnt_Type()
)
switchCapSTGsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSTGsMaxEnt.setStatus("current")
_SwitchCapSTGsCurrEnt_Type = DisplayString
_SwitchCapSTGsCurrEnt_Object = MibScalar
switchCapSTGsCurrEnt = _SwitchCapSTGsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 11),
    _SwitchCapSTGsCurrEnt_Type()
)
switchCapSTGsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSTGsCurrEnt.setStatus("current")
_SwitchCapPortTeamsMaxEnt_Type = Integer32
_SwitchCapPortTeamsMaxEnt_Object = MibScalar
switchCapPortTeamsMaxEnt = _SwitchCapPortTeamsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 12),
    _SwitchCapPortTeamsMaxEnt_Type()
)
switchCapPortTeamsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapPortTeamsMaxEnt.setStatus("current")
_SwitchCapPortTeamsCurrEnt_Type = DisplayString
_SwitchCapPortTeamsCurrEnt_Object = MibScalar
switchCapPortTeamsCurrEnt = _SwitchCapPortTeamsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 13),
    _SwitchCapPortTeamsCurrEnt_Type()
)
switchCapPortTeamsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapPortTeamsCurrEnt.setStatus("current")
_SwitchCapMonitorPorts_Type = Integer32
_SwitchCapMonitorPorts_Object = MibScalar
switchCapMonitorPorts = _SwitchCapMonitorPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 1, 14),
    _SwitchCapMonitorPorts_Type()
)
switchCapMonitorPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapMonitorPorts.setStatus("current")
_SwitchCapL3Info_ObjectIdentity = ObjectIdentity
switchCapL3Info = _SwitchCapL3Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2)
)
_SwitchCapIpIntfMaxEnt_Type = Integer32
_SwitchCapIpIntfMaxEnt_Object = MibScalar
switchCapIpIntfMaxEnt = _SwitchCapIpIntfMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 1),
    _SwitchCapIpIntfMaxEnt_Type()
)
switchCapIpIntfMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpIntfMaxEnt.setStatus("current")
_SwitchCapIpIntfCurrEnt_Type = DisplayString
_SwitchCapIpIntfCurrEnt_Object = MibScalar
switchCapIpIntfCurrEnt = _SwitchCapIpIntfCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 2),
    _SwitchCapIpIntfCurrEnt_Type()
)
switchCapIpIntfCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpIntfCurrEnt.setStatus("current")
_SwitchCapIpGWMaxEnt_Type = DisplayString
_SwitchCapIpGWMaxEnt_Object = MibScalar
switchCapIpGWMaxEnt = _SwitchCapIpGWMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 3),
    _SwitchCapIpGWMaxEnt_Type()
)
switchCapIpGWMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpGWMaxEnt.setStatus("current")
_SwitchCapIpGWCurrEnt_Type = DisplayString
_SwitchCapIpGWCurrEnt_Object = MibScalar
switchCapIpGWCurrEnt = _SwitchCapIpGWCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 4),
    _SwitchCapIpGWCurrEnt_Type()
)
switchCapIpGWCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpGWCurrEnt.setStatus("current")
_SwitchCapIpRoutesMaxEnt_Type = Integer32
_SwitchCapIpRoutesMaxEnt_Object = MibScalar
switchCapIpRoutesMaxEnt = _SwitchCapIpRoutesMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 5),
    _SwitchCapIpRoutesMaxEnt_Type()
)
switchCapIpRoutesMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpRoutesMaxEnt.setStatus("current")
_SwitchCapIpRoutesCurrEnt_Type = Integer32
_SwitchCapIpRoutesCurrEnt_Object = MibScalar
switchCapIpRoutesCurrEnt = _SwitchCapIpRoutesCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 6),
    _SwitchCapIpRoutesCurrEnt_Type()
)
switchCapIpRoutesCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpRoutesCurrEnt.setStatus("current")
_SwitchCapIpStaticRoutesMaxEnt_Type = Integer32
_SwitchCapIpStaticRoutesMaxEnt_Object = MibScalar
switchCapIpStaticRoutesMaxEnt = _SwitchCapIpStaticRoutesMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 7),
    _SwitchCapIpStaticRoutesMaxEnt_Type()
)
switchCapIpStaticRoutesMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpStaticRoutesMaxEnt.setStatus("current")
_SwitchCapIpStaticRoutesCurrEnt_Type = Integer32
_SwitchCapIpStaticRoutesCurrEnt_Object = MibScalar
switchCapIpStaticRoutesCurrEnt = _SwitchCapIpStaticRoutesCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 8),
    _SwitchCapIpStaticRoutesCurrEnt_Type()
)
switchCapIpStaticRoutesCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpStaticRoutesCurrEnt.setStatus("current")
_SwitchCapIpARPMaxEnt_Type = Integer32
_SwitchCapIpARPMaxEnt_Object = MibScalar
switchCapIpARPMaxEnt = _SwitchCapIpARPMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 9),
    _SwitchCapIpARPMaxEnt_Type()
)
switchCapIpARPMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpARPMaxEnt.setStatus("current")
_SwitchCapIpARPCurrEnt_Type = Integer32
_SwitchCapIpARPCurrEnt_Object = MibScalar
switchCapIpARPCurrEnt = _SwitchCapIpARPCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 10),
    _SwitchCapIpARPCurrEnt_Type()
)
switchCapIpARPCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpARPCurrEnt.setStatus("current")
_SwitchCapIpStaticARPMaxEnt_Type = Integer32
_SwitchCapIpStaticARPMaxEnt_Object = MibScalar
switchCapIpStaticARPMaxEnt = _SwitchCapIpStaticARPMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 11),
    _SwitchCapIpStaticARPMaxEnt_Type()
)
switchCapIpStaticARPMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpStaticARPMaxEnt.setStatus("current")
_SwitchCapIpStaticARPCurrEnt_Type = Integer32
_SwitchCapIpStaticARPCurrEnt_Object = MibScalar
switchCapIpStaticARPCurrEnt = _SwitchCapIpStaticARPCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 12),
    _SwitchCapIpStaticARPCurrEnt_Type()
)
switchCapIpStaticARPCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIpStaticARPCurrEnt.setStatus("current")
_SwitchCapLocNetsMaxEnt_Type = Integer32
_SwitchCapLocNetsMaxEnt_Object = MibScalar
switchCapLocNetsMaxEnt = _SwitchCapLocNetsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 13),
    _SwitchCapLocNetsMaxEnt_Type()
)
switchCapLocNetsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapLocNetsMaxEnt.setStatus("current")
_SwitchCapLocNetsCurrEnt_Type = Integer32
_SwitchCapLocNetsCurrEnt_Object = MibScalar
switchCapLocNetsCurrEnt = _SwitchCapLocNetsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 14),
    _SwitchCapLocNetsCurrEnt_Type()
)
switchCapLocNetsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapLocNetsCurrEnt.setStatus("current")
_SwitchCapDNSSerMaxEnt_Type = Integer32
_SwitchCapDNSSerMaxEnt_Object = MibScalar
switchCapDNSSerMaxEnt = _SwitchCapDNSSerMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 15),
    _SwitchCapDNSSerMaxEnt_Type()
)
switchCapDNSSerMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapDNSSerMaxEnt.setStatus("current")
_SwitchCapDNSSerCurrEnt_Type = Integer32
_SwitchCapDNSSerCurrEnt_Object = MibScalar
switchCapDNSSerCurrEnt = _SwitchCapDNSSerCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 16),
    _SwitchCapDNSSerCurrEnt_Type()
)
switchCapDNSSerCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapDNSSerCurrEnt.setStatus("current")
_SwitchCapBootpSerMaxEnt_Type = Integer32
_SwitchCapBootpSerMaxEnt_Object = MibScalar
switchCapBootpSerMaxEnt = _SwitchCapBootpSerMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 17),
    _SwitchCapBootpSerMaxEnt_Type()
)
switchCapBootpSerMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapBootpSerMaxEnt.setStatus("current")
_SwitchCapBootpSerCurrEnt_Type = Integer32
_SwitchCapBootpSerCurrEnt_Object = MibScalar
switchCapBootpSerCurrEnt = _SwitchCapBootpSerCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 18),
    _SwitchCapBootpSerCurrEnt_Type()
)
switchCapBootpSerCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapBootpSerCurrEnt.setStatus("current")
_SwitchCapRIPIntfMaxEnt_Type = Integer32
_SwitchCapRIPIntfMaxEnt_Object = MibScalar
switchCapRIPIntfMaxEnt = _SwitchCapRIPIntfMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 19),
    _SwitchCapRIPIntfMaxEnt_Type()
)
switchCapRIPIntfMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRIPIntfMaxEnt.setStatus("current")
_SwitchCapRIPIntfCurrEnt_Type = Integer32
_SwitchCapRIPIntfCurrEnt_Object = MibScalar
switchCapRIPIntfCurrEnt = _SwitchCapRIPIntfCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 20),
    _SwitchCapRIPIntfCurrEnt_Type()
)
switchCapRIPIntfCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRIPIntfCurrEnt.setStatus("current")
_SwitchCapOSPFIntfMaxEnt_Type = Integer32
_SwitchCapOSPFIntfMaxEnt_Object = MibScalar
switchCapOSPFIntfMaxEnt = _SwitchCapOSPFIntfMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 21),
    _SwitchCapOSPFIntfMaxEnt_Type()
)
switchCapOSPFIntfMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFIntfMaxEnt.setStatus("current")
_SwitchCapOSPFIntfCurrEnt_Type = DisplayString
_SwitchCapOSPFIntfCurrEnt_Object = MibScalar
switchCapOSPFIntfCurrEnt = _SwitchCapOSPFIntfCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 22),
    _SwitchCapOSPFIntfCurrEnt_Type()
)
switchCapOSPFIntfCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFIntfCurrEnt.setStatus("current")
_SwitchCapOSPFAreasMaxEnt_Type = Integer32
_SwitchCapOSPFAreasMaxEnt_Object = MibScalar
switchCapOSPFAreasMaxEnt = _SwitchCapOSPFAreasMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 23),
    _SwitchCapOSPFAreasMaxEnt_Type()
)
switchCapOSPFAreasMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFAreasMaxEnt.setStatus("current")
_SwitchCapOSPFAreasCurrEnt_Type = DisplayString
_SwitchCapOSPFAreasCurrEnt_Object = MibScalar
switchCapOSPFAreasCurrEnt = _SwitchCapOSPFAreasCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 24),
    _SwitchCapOSPFAreasCurrEnt_Type()
)
switchCapOSPFAreasCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFAreasCurrEnt.setStatus("current")
_SwitchCapOSPFSummaryRangesMaxEnt_Type = Integer32
_SwitchCapOSPFSummaryRangesMaxEnt_Object = MibScalar
switchCapOSPFSummaryRangesMaxEnt = _SwitchCapOSPFSummaryRangesMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 25),
    _SwitchCapOSPFSummaryRangesMaxEnt_Type()
)
switchCapOSPFSummaryRangesMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFSummaryRangesMaxEnt.setStatus("current")
_SwitchCapOSPFSummaryRangesCurrEnt_Type = DisplayString
_SwitchCapOSPFSummaryRangesCurrEnt_Object = MibScalar
switchCapOSPFSummaryRangesCurrEnt = _SwitchCapOSPFSummaryRangesCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 26),
    _SwitchCapOSPFSummaryRangesCurrEnt_Type()
)
switchCapOSPFSummaryRangesCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFSummaryRangesCurrEnt.setStatus("current")
_SwitchCapOSPFVirtLinksMaxEnt_Type = Integer32
_SwitchCapOSPFVirtLinksMaxEnt_Object = MibScalar
switchCapOSPFVirtLinksMaxEnt = _SwitchCapOSPFVirtLinksMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 27),
    _SwitchCapOSPFVirtLinksMaxEnt_Type()
)
switchCapOSPFVirtLinksMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFVirtLinksMaxEnt.setStatus("current")
_SwitchCapOSPFVirtLinksCurrEnt_Type = DisplayString
_SwitchCapOSPFVirtLinksCurrEnt_Object = MibScalar
switchCapOSPFVirtLinksCurrEnt = _SwitchCapOSPFVirtLinksCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 28),
    _SwitchCapOSPFVirtLinksCurrEnt_Type()
)
switchCapOSPFVirtLinksCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFVirtLinksCurrEnt.setStatus("current")
_SwitchCapOSPFHostsMaxEnt_Type = Integer32
_SwitchCapOSPFHostsMaxEnt_Object = MibScalar
switchCapOSPFHostsMaxEnt = _SwitchCapOSPFHostsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 29),
    _SwitchCapOSPFHostsMaxEnt_Type()
)
switchCapOSPFHostsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFHostsMaxEnt.setStatus("current")
_SwitchCapOSPFHostsCurrEnt_Type = DisplayString
_SwitchCapOSPFHostsCurrEnt_Object = MibScalar
switchCapOSPFHostsCurrEnt = _SwitchCapOSPFHostsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 30),
    _SwitchCapOSPFHostsCurrEnt_Type()
)
switchCapOSPFHostsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapOSPFHostsCurrEnt.setStatus("current")
_SwitchCapLSDBLimit_Type = Integer32
_SwitchCapLSDBLimit_Object = MibScalar
switchCapLSDBLimit = _SwitchCapLSDBLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 31),
    _SwitchCapLSDBLimit_Type()
)
switchCapLSDBLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapLSDBLimit.setStatus("current")
_SwitchCapBGPPeersMaxEnt_Type = Integer32
_SwitchCapBGPPeersMaxEnt_Object = MibScalar
switchCapBGPPeersMaxEnt = _SwitchCapBGPPeersMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 32),
    _SwitchCapBGPPeersMaxEnt_Type()
)
switchCapBGPPeersMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapBGPPeersMaxEnt.setStatus("current")
_SwitchCapBGPPeersCurrEnt_Type = DisplayString
_SwitchCapBGPPeersCurrEnt_Object = MibScalar
switchCapBGPPeersCurrEnt = _SwitchCapBGPPeersCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 33),
    _SwitchCapBGPPeersCurrEnt_Type()
)
switchCapBGPPeersCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapBGPPeersCurrEnt.setStatus("current")
_SwitchCapBGPRouteAggrsMaxEnt_Type = Integer32
_SwitchCapBGPRouteAggrsMaxEnt_Object = MibScalar
switchCapBGPRouteAggrsMaxEnt = _SwitchCapBGPRouteAggrsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 34),
    _SwitchCapBGPRouteAggrsMaxEnt_Type()
)
switchCapBGPRouteAggrsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapBGPRouteAggrsMaxEnt.setStatus("current")
_SwitchCapBGPRouteAggrsCurrEnt_Type = DisplayString
_SwitchCapBGPRouteAggrsCurrEnt_Object = MibScalar
switchCapBGPRouteAggrsCurrEnt = _SwitchCapBGPRouteAggrsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 35),
    _SwitchCapBGPRouteAggrsCurrEnt_Type()
)
switchCapBGPRouteAggrsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapBGPRouteAggrsCurrEnt.setStatus("current")
_SwitchCapRouteMapsMaxEnt_Type = Integer32
_SwitchCapRouteMapsMaxEnt_Object = MibScalar
switchCapRouteMapsMaxEnt = _SwitchCapRouteMapsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 36),
    _SwitchCapRouteMapsMaxEnt_Type()
)
switchCapRouteMapsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRouteMapsMaxEnt.setStatus("current")
_SwitchCapRouteMapsCurrEnt_Type = DisplayString
_SwitchCapRouteMapsCurrEnt_Object = MibScalar
switchCapRouteMapsCurrEnt = _SwitchCapRouteMapsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 37),
    _SwitchCapRouteMapsCurrEnt_Type()
)
switchCapRouteMapsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRouteMapsCurrEnt.setStatus("current")
_SwitchCapNwkFltsMaxEnt_Type = Integer32
_SwitchCapNwkFltsMaxEnt_Object = MibScalar
switchCapNwkFltsMaxEnt = _SwitchCapNwkFltsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 38),
    _SwitchCapNwkFltsMaxEnt_Type()
)
switchCapNwkFltsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapNwkFltsMaxEnt.setStatus("current")
_SwitchCapNwkFltsCurrEnt_Type = DisplayString
_SwitchCapNwkFltsCurrEnt_Object = MibScalar
switchCapNwkFltsCurrEnt = _SwitchCapNwkFltsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 39),
    _SwitchCapNwkFltsCurrEnt_Type()
)
switchCapNwkFltsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapNwkFltsCurrEnt.setStatus("current")
_SwitchCapASFlts_Type = Integer32
_SwitchCapASFlts_Object = MibScalar
switchCapASFlts = _SwitchCapASFlts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 40),
    _SwitchCapASFlts_Type()
)
switchCapASFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapASFlts.setStatus("current")
_SwitchCapVRRPRtrsMaxEnt_Type = Integer32
_SwitchCapVRRPRtrsMaxEnt_Object = MibScalar
switchCapVRRPRtrsMaxEnt = _SwitchCapVRRPRtrsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 41),
    _SwitchCapVRRPRtrsMaxEnt_Type()
)
switchCapVRRPRtrsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVRRPRtrsMaxEnt.setStatus("current")
_SwitchCapVRRPRtrsCurrEnt_Type = DisplayString
_SwitchCapVRRPRtrsCurrEnt_Object = MibScalar
switchCapVRRPRtrsCurrEnt = _SwitchCapVRRPRtrsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 42),
    _SwitchCapVRRPRtrsCurrEnt_Type()
)
switchCapVRRPRtrsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVRRPRtrsCurrEnt.setStatus("current")
_SwitchCapVRRPRtrGRsMaxEnt_Type = Integer32
_SwitchCapVRRPRtrGRsMaxEnt_Object = MibScalar
switchCapVRRPRtrGRsMaxEnt = _SwitchCapVRRPRtrGRsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 43),
    _SwitchCapVRRPRtrGRsMaxEnt_Type()
)
switchCapVRRPRtrGRsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVRRPRtrGRsMaxEnt.setStatus("current")
_SwitchCapVRRPRtrGRsCurrEnt_Type = DisplayString
_SwitchCapVRRPRtrGRsCurrEnt_Object = MibScalar
switchCapVRRPRtrGRsCurrEnt = _SwitchCapVRRPRtrGRsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 44),
    _SwitchCapVRRPRtrGRsCurrEnt_Type()
)
switchCapVRRPRtrGRsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVRRPRtrGRsCurrEnt.setStatus("current")
_SwitchCapVRRPIntfsMaxEnt_Type = Integer32
_SwitchCapVRRPIntfsMaxEnt_Object = MibScalar
switchCapVRRPIntfsMaxEnt = _SwitchCapVRRPIntfsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 45),
    _SwitchCapVRRPIntfsMaxEnt_Type()
)
switchCapVRRPIntfsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVRRPIntfsMaxEnt.setStatus("current")
_SwitchCapVRRPIntfsCurrEnt_Type = Integer32
_SwitchCapVRRPIntfsCurrEnt_Object = MibScalar
switchCapVRRPIntfsCurrEnt = _SwitchCapVRRPIntfsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 2, 46),
    _SwitchCapVRRPIntfsCurrEnt_Type()
)
switchCapVRRPIntfsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVRRPIntfsCurrEnt.setStatus("current")
_SwitchCapSlbInfo_ObjectIdentity = ObjectIdentity
switchCapSlbInfo = _SwitchCapSlbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3)
)
_SwitchCapRealSersMaxEnt_Type = Integer32
_SwitchCapRealSersMaxEnt_Object = MibScalar
switchCapRealSersMaxEnt = _SwitchCapRealSersMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 1),
    _SwitchCapRealSersMaxEnt_Type()
)
switchCapRealSersMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRealSersMaxEnt.setStatus("current")
_SwitchCapRealSersCurrEnt_Type = DisplayString
_SwitchCapRealSersCurrEnt_Object = MibScalar
switchCapRealSersCurrEnt = _SwitchCapRealSersCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 2),
    _SwitchCapRealSersCurrEnt_Type()
)
switchCapRealSersCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRealSersCurrEnt.setStatus("current")
_SwitchCapSerGRsMaxEnt_Type = Integer32
_SwitchCapSerGRsMaxEnt_Object = MibScalar
switchCapSerGRsMaxEnt = _SwitchCapSerGRsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 3),
    _SwitchCapSerGRsMaxEnt_Type()
)
switchCapSerGRsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSerGRsMaxEnt.setStatus("current")
_SwitchCapSerGRsCurrEnt_Type = Integer32
_SwitchCapSerGRsCurrEnt_Object = MibScalar
switchCapSerGRsCurrEnt = _SwitchCapSerGRsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 4),
    _SwitchCapSerGRsCurrEnt_Type()
)
switchCapSerGRsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSerGRsCurrEnt.setStatus("current")
_SwitchCapVirtSersMaxEnt_Type = Integer32
_SwitchCapVirtSersMaxEnt_Object = MibScalar
switchCapVirtSersMaxEnt = _SwitchCapVirtSersMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 5),
    _SwitchCapVirtSersMaxEnt_Type()
)
switchCapVirtSersMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVirtSersMaxEnt.setStatus("current")
_SwitchCapVirtSersCurrEnt_Type = DisplayString
_SwitchCapVirtSersCurrEnt_Object = MibScalar
switchCapVirtSersCurrEnt = _SwitchCapVirtSersCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 6),
    _SwitchCapVirtSersCurrEnt_Type()
)
switchCapVirtSersCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVirtSersCurrEnt.setStatus("current")
_SwitchCapVirtServicesEnt_Type = Integer32
_SwitchCapVirtServicesEnt_Object = MibScalar
switchCapVirtServicesEnt = _SwitchCapVirtServicesEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 7),
    _SwitchCapVirtServicesEnt_Type()
)
switchCapVirtServicesEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapVirtServicesEnt.setStatus("current")
_SwitchCapRealServicesEnt_Type = Integer32
_SwitchCapRealServicesEnt_Object = MibScalar
switchCapRealServicesEnt = _SwitchCapRealServicesEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 8),
    _SwitchCapRealServicesEnt_Type()
)
switchCapRealServicesEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRealServicesEnt.setStatus("current")
_SwitchCapRealIDSSer_Type = Integer32
_SwitchCapRealIDSSer_Object = MibScalar
switchCapRealIDSSer = _SwitchCapRealIDSSer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 9),
    _SwitchCapRealIDSSer_Type()
)
switchCapRealIDSSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRealIDSSer.setStatus("current")
_SwitchCapIDSSerGRs_Type = Integer32
_SwitchCapIDSSerGRs_Object = MibScalar
switchCapIDSSerGRs = _SwitchCapIDSSerGRs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 10),
    _SwitchCapIDSSerGRs_Type()
)
switchCapIDSSerGRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapIDSSerGRs.setStatus("current")
_SwitchCapGSLBDomainsMaxEnt_Type = Integer32
_SwitchCapGSLBDomainsMaxEnt_Object = MibScalar
switchCapGSLBDomainsMaxEnt = _SwitchCapGSLBDomainsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 11),
    _SwitchCapGSLBDomainsMaxEnt_Type()
)
switchCapGSLBDomainsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBDomainsMaxEnt.setStatus("current")
_SwitchCapGSLBDomainsCurrEnt_Type = DisplayString
_SwitchCapGSLBDomainsCurrEnt_Object = MibScalar
switchCapGSLBDomainsCurrEnt = _SwitchCapGSLBDomainsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 12),
    _SwitchCapGSLBDomainsCurrEnt_Type()
)
switchCapGSLBDomainsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBDomainsCurrEnt.setStatus("current")
_SwitchCapGSLBServicesMaxEnt_Type = Integer32
_SwitchCapGSLBServicesMaxEnt_Object = MibScalar
switchCapGSLBServicesMaxEnt = _SwitchCapGSLBServicesMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 13),
    _SwitchCapGSLBServicesMaxEnt_Type()
)
switchCapGSLBServicesMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBServicesMaxEnt.setStatus("current")
_SwitchCapGSLBServicesCurrEnt_Type = DisplayString
_SwitchCapGSLBServicesCurrEnt_Object = MibScalar
switchCapGSLBServicesCurrEnt = _SwitchCapGSLBServicesCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 14),
    _SwitchCapGSLBServicesCurrEnt_Type()
)
switchCapGSLBServicesCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBServicesCurrEnt.setStatus("current")
_SwitchCapGSLBLocSersMaxEnt_Type = Integer32
_SwitchCapGSLBLocSersMaxEnt_Object = MibScalar
switchCapGSLBLocSersMaxEnt = _SwitchCapGSLBLocSersMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 15),
    _SwitchCapGSLBLocSersMaxEnt_Type()
)
switchCapGSLBLocSersMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBLocSersMaxEnt.setStatus("current")
_SwitchCapGSLBLocSersCurrEnt_Type = DisplayString
_SwitchCapGSLBLocSersCurrEnt_Object = MibScalar
switchCapGSLBLocSersCurrEnt = _SwitchCapGSLBLocSersCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 16),
    _SwitchCapGSLBLocSersCurrEnt_Type()
)
switchCapGSLBLocSersCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBLocSersCurrEnt.setStatus("current")
_SwitchCapGSLBRemSersMaxEnt_Type = Integer32
_SwitchCapGSLBRemSersMaxEnt_Object = MibScalar
switchCapGSLBRemSersMaxEnt = _SwitchCapGSLBRemSersMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 17),
    _SwitchCapGSLBRemSersMaxEnt_Type()
)
switchCapGSLBRemSersMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBRemSersMaxEnt.setStatus("current")
_SwitchCapGSLBRemSersCurrEnt_Type = DisplayString
_SwitchCapGSLBRemSersCurrEnt_Object = MibScalar
switchCapGSLBRemSersCurrEnt = _SwitchCapGSLBRemSersCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 18),
    _SwitchCapGSLBRemSersCurrEnt_Type()
)
switchCapGSLBRemSersCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBRemSersCurrEnt.setStatus("current")
_SwitchCapGSLBRemSitesMaxEnt_Type = Integer32
_SwitchCapGSLBRemSitesMaxEnt_Object = MibScalar
switchCapGSLBRemSitesMaxEnt = _SwitchCapGSLBRemSitesMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 19),
    _SwitchCapGSLBRemSitesMaxEnt_Type()
)
switchCapGSLBRemSitesMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBRemSitesMaxEnt.setStatus("current")
_SwitchCapGSLBRemSitesCurrEnt_Type = DisplayString
_SwitchCapGSLBRemSitesCurrEnt_Object = MibScalar
switchCapGSLBRemSitesCurrEnt = _SwitchCapGSLBRemSitesCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 20),
    _SwitchCapGSLBRemSitesCurrEnt_Type()
)
switchCapGSLBRemSitesCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBRemSitesCurrEnt.setStatus("current")
_SwitchCapGSLBFailoversPerRemSiteMaxEnt_Type = Integer32
_SwitchCapGSLBFailoversPerRemSiteMaxEnt_Object = MibScalar
switchCapGSLBFailoversPerRemSiteMaxEnt = _SwitchCapGSLBFailoversPerRemSiteMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 21),
    _SwitchCapGSLBFailoversPerRemSiteMaxEnt_Type()
)
switchCapGSLBFailoversPerRemSiteMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBFailoversPerRemSiteMaxEnt.setStatus("current")
_SwitchCapGSLBFailoversPerRemSiteCurrEnt_Type = DisplayString
_SwitchCapGSLBFailoversPerRemSiteCurrEnt_Object = MibScalar
switchCapGSLBFailoversPerRemSiteCurrEnt = _SwitchCapGSLBFailoversPerRemSiteCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 22),
    _SwitchCapGSLBFailoversPerRemSiteCurrEnt_Type()
)
switchCapGSLBFailoversPerRemSiteCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBFailoversPerRemSiteCurrEnt.setStatus("current")
_SwitchCapGSLBNetworksMaxEnt_Type = Integer32
_SwitchCapGSLBNetworksMaxEnt_Object = MibScalar
switchCapGSLBNetworksMaxEnt = _SwitchCapGSLBNetworksMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 23),
    _SwitchCapGSLBNetworksMaxEnt_Type()
)
switchCapGSLBNetworksMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBNetworksMaxEnt.setStatus("current")
_SwitchCapGSLBNetworksCurrEnt_Type = DisplayString
_SwitchCapGSLBNetworksCurrEnt_Object = MibScalar
switchCapGSLBNetworksCurrEnt = _SwitchCapGSLBNetworksCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 24),
    _SwitchCapGSLBNetworksCurrEnt_Type()
)
switchCapGSLBNetworksCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBNetworksCurrEnt.setStatus("current")
_SwitchCapGSLBGeographicalRegionsMaxEnt_Type = Integer32
_SwitchCapGSLBGeographicalRegionsMaxEnt_Object = MibScalar
switchCapGSLBGeographicalRegionsMaxEnt = _SwitchCapGSLBGeographicalRegionsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 25),
    _SwitchCapGSLBGeographicalRegionsMaxEnt_Type()
)
switchCapGSLBGeographicalRegionsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBGeographicalRegionsMaxEnt.setStatus("current")
_SwitchCapGSLBGeographicalRegionsCurrEnt_Type = DisplayString
_SwitchCapGSLBGeographicalRegionsCurrEnt_Object = MibScalar
switchCapGSLBGeographicalRegionsCurrEnt = _SwitchCapGSLBGeographicalRegionsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 26),
    _SwitchCapGSLBGeographicalRegionsCurrEnt_Type()
)
switchCapGSLBGeographicalRegionsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBGeographicalRegionsCurrEnt.setStatus("current")
_SwitchCapGSLBRulesMaxEnt_Type = Integer32
_SwitchCapGSLBRulesMaxEnt_Object = MibScalar
switchCapGSLBRulesMaxEnt = _SwitchCapGSLBRulesMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 27),
    _SwitchCapGSLBRulesMaxEnt_Type()
)
switchCapGSLBRulesMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBRulesMaxEnt.setStatus("current")
_SwitchCapGSLBRulesCurrEnt_Type = DisplayString
_SwitchCapGSLBRulesCurrEnt_Object = MibScalar
switchCapGSLBRulesCurrEnt = _SwitchCapGSLBRulesCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 28),
    _SwitchCapGSLBRulesCurrEnt_Type()
)
switchCapGSLBRulesCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBRulesCurrEnt.setStatus("current")
_SwitchCapGSLBMetricsPerRuleMaxEnt_Type = Integer32
_SwitchCapGSLBMetricsPerRuleMaxEnt_Object = MibScalar
switchCapGSLBMetricsPerRuleMaxEnt = _SwitchCapGSLBMetricsPerRuleMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 29),
    _SwitchCapGSLBMetricsPerRuleMaxEnt_Type()
)
switchCapGSLBMetricsPerRuleMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBMetricsPerRuleMaxEnt.setStatus("current")
_SwitchCapGSLBMetricPerRuleCurrEnt_Type = DisplayString
_SwitchCapGSLBMetricPerRuleCurrEnt_Object = MibScalar
switchCapGSLBMetricPerRuleCurrEnt = _SwitchCapGSLBMetricPerRuleCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 30),
    _SwitchCapGSLBMetricPerRuleCurrEnt_Type()
)
switchCapGSLBMetricPerRuleCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBMetricPerRuleCurrEnt.setStatus("current")
_SwitchCapGSLBDNSPersCacheMaxEnt_Type = Integer32
_SwitchCapGSLBDNSPersCacheMaxEnt_Object = MibScalar
switchCapGSLBDNSPersCacheMaxEnt = _SwitchCapGSLBDNSPersCacheMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 31),
    _SwitchCapGSLBDNSPersCacheMaxEnt_Type()
)
switchCapGSLBDNSPersCacheMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBDNSPersCacheMaxEnt.setStatus("current")
_SwitchCapGSLBDNSPersCacheCurrEnt_Type = DisplayString
_SwitchCapGSLBDNSPersCacheCurrEnt_Object = MibScalar
switchCapGSLBDNSPersCacheCurrEnt = _SwitchCapGSLBDNSPersCacheCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 32),
    _SwitchCapGSLBDNSPersCacheCurrEnt_Type()
)
switchCapGSLBDNSPersCacheCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapGSLBDNSPersCacheCurrEnt.setStatus("current")
_SwitchCapFltsMaxEnt_Type = Integer32
_SwitchCapFltsMaxEnt_Object = MibScalar
switchCapFltsMaxEnt = _SwitchCapFltsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 33),
    _SwitchCapFltsMaxEnt_Type()
)
switchCapFltsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapFltsMaxEnt.setStatus("current")
_SwitchCapFltsCurrEnt_Type = DisplayString
_SwitchCapFltsCurrEnt_Object = MibScalar
switchCapFltsCurrEnt = _SwitchCapFltsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 34),
    _SwitchCapFltsCurrEnt_Type()
)
switchCapFltsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapFltsCurrEnt.setStatus("current")
_SwitchCapPIPsMaxEnt_Type = Integer32
_SwitchCapPIPsMaxEnt_Object = MibScalar
switchCapPIPsMaxEnt = _SwitchCapPIPsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 35),
    _SwitchCapPIPsMaxEnt_Type()
)
switchCapPIPsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapPIPsMaxEnt.setStatus("current")
_SwitchCapPIPsCurrEnt_Type = Integer32
_SwitchCapPIPsCurrEnt_Object = MibScalar
switchCapPIPsCurrEnt = _SwitchCapPIPsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 36),
    _SwitchCapPIPsCurrEnt_Type()
)
switchCapPIPsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapPIPsCurrEnt.setStatus("current")
_SwitchCapScriptHealthChecksMaxEnt_Type = Integer32
_SwitchCapScriptHealthChecksMaxEnt_Object = MibScalar
switchCapScriptHealthChecksMaxEnt = _SwitchCapScriptHealthChecksMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 37),
    _SwitchCapScriptHealthChecksMaxEnt_Type()
)
switchCapScriptHealthChecksMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapScriptHealthChecksMaxEnt.setStatus("current")
_SwitchCapScriptHealthChecksCurrEnt_Type = Integer32
_SwitchCapScriptHealthChecksCurrEnt_Object = MibScalar
switchCapScriptHealthChecksCurrEnt = _SwitchCapScriptHealthChecksCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 38),
    _SwitchCapScriptHealthChecksCurrEnt_Type()
)
switchCapScriptHealthChecksCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapScriptHealthChecksCurrEnt.setStatus("current")
_SwitchCapSNMPHealthChecksMaxEnt_Type = Integer32
_SwitchCapSNMPHealthChecksMaxEnt_Object = MibScalar
switchCapSNMPHealthChecksMaxEnt = _SwitchCapSNMPHealthChecksMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 39),
    _SwitchCapSNMPHealthChecksMaxEnt_Type()
)
switchCapSNMPHealthChecksMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSNMPHealthChecksMaxEnt.setStatus("current")
_SwitchCapSNMPHealthChecksCurrEnt_Type = Integer32
_SwitchCapSNMPHealthChecksCurrEnt_Object = MibScalar
switchCapSNMPHealthChecksCurrEnt = _SwitchCapSNMPHealthChecksCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 40),
    _SwitchCapSNMPHealthChecksCurrEnt_Type()
)
switchCapSNMPHealthChecksCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSNMPHealthChecksCurrEnt.setStatus("current")
_SwitchCapRulesforURLParsingMaxEnt_Type = Integer32
_SwitchCapRulesforURLParsingMaxEnt_Object = MibScalar
switchCapRulesforURLParsingMaxEnt = _SwitchCapRulesforURLParsingMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 41),
    _SwitchCapRulesforURLParsingMaxEnt_Type()
)
switchCapRulesforURLParsingMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRulesforURLParsingMaxEnt.setStatus("current")
_SwitchCapRulesforURLParsingCurrEnt_Type = Integer32
_SwitchCapRulesforURLParsingCurrEnt_Object = MibScalar
switchCapRulesforURLParsingCurrEnt = _SwitchCapRulesforURLParsingCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 42),
    _SwitchCapRulesforURLParsingCurrEnt_Type()
)
switchCapRulesforURLParsingCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapRulesforURLParsingCurrEnt.setStatus("current")
_SwitchCapSLBSessionsMaxEnt_Type = Integer32
_SwitchCapSLBSessionsMaxEnt_Object = MibScalar
switchCapSLBSessionsMaxEnt = _SwitchCapSLBSessionsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 43),
    _SwitchCapSLBSessionsMaxEnt_Type()
)
switchCapSLBSessionsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSLBSessionsMaxEnt.setStatus("current")
_SwitchCapSLBSessionsCurrEnt_Type = Integer32
_SwitchCapSLBSessionsCurrEnt_Object = MibScalar
switchCapSLBSessionsCurrEnt = _SwitchCapSLBSessionsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 44),
    _SwitchCapSLBSessionsCurrEnt_Type()
)
switchCapSLBSessionsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSLBSessionsCurrEnt.setStatus("current")
_SwitchCapNumofRportstoVport_Type = Integer32
_SwitchCapNumofRportstoVport_Object = MibScalar
switchCapNumofRportstoVport = _SwitchCapNumofRportstoVport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 45),
    _SwitchCapNumofRportstoVport_Type()
)
switchCapNumofRportstoVport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapNumofRportstoVport.setStatus("current")
_SwitchCapDomianRecordsMaxEnt_Type = Integer32
_SwitchCapDomianRecordsMaxEnt_Object = MibScalar
switchCapDomianRecordsMaxEnt = _SwitchCapDomianRecordsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 46),
    _SwitchCapDomianRecordsMaxEnt_Type()
)
switchCapDomianRecordsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapDomianRecordsMaxEnt.setStatus("current")
_SwitchCapDomainRecordsCurrEnt_Type = DisplayString
_SwitchCapDomainRecordsCurrEnt_Object = MibScalar
switchCapDomainRecordsCurrEnt = _SwitchCapDomainRecordsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 47),
    _SwitchCapDomainRecordsCurrEnt_Type()
)
switchCapDomainRecordsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapDomainRecordsCurrEnt.setStatus("current")
_SwitchCapMappingPerDomainrecord_Type = Integer32
_SwitchCapMappingPerDomainrecord_Object = MibScalar
switchCapMappingPerDomainrecord = _SwitchCapMappingPerDomainrecord_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 3, 48),
    _SwitchCapMappingPerDomainrecord_Type()
)
switchCapMappingPerDomainrecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapMappingPerDomainrecord.setStatus("current")
_SwitchCapSlbPortInfo_ObjectIdentity = ObjectIdentity
switchCapSlbPortInfo = _SwitchCapSlbPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4)
)
_SwitchCapSlbPortInfoTable_Object = MibTable
switchCapSlbPortInfoTable = _SwitchCapSlbPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4, 1)
)
if mibBuilder.loadTexts:
    switchCapSlbPortInfoTable.setStatus("current")
_SwitchCapSlbPortInfoTableEntry_Object = MibTableRow
switchCapSlbPortInfoTableEntry = _SwitchCapSlbPortInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4, 1, 1)
)
switchCapSlbPortInfoTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "switchCapSlbPortInfoIndx"),
)
if mibBuilder.loadTexts:
    switchCapSlbPortInfoTableEntry.setStatus("current")
_SwitchCapSlbPortInfoIndx_Type = Integer32
_SwitchCapSlbPortInfoIndx_Object = MibTableColumn
switchCapSlbPortInfoIndx = _SwitchCapSlbPortInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4, 1, 1, 1),
    _SwitchCapSlbPortInfoIndx_Type()
)
switchCapSlbPortInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSlbPortInfoIndx.setStatus("current")


class _SwitchCapSlbPortClientState_Type(Integer32):
    """Custom type switchCapSlbPortClientState based on Integer32"""
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


_SwitchCapSlbPortClientState_Type.__name__ = "Integer32"
_SwitchCapSlbPortClientState_Object = MibTableColumn
switchCapSlbPortClientState = _SwitchCapSlbPortClientState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4, 1, 1, 2),
    _SwitchCapSlbPortClientState_Type()
)
switchCapSlbPortClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSlbPortClientState.setStatus("current")


class _SwitchCapSlbPortSerState_Type(Integer32):
    """Custom type switchCapSlbPortSerState based on Integer32"""
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


_SwitchCapSlbPortSerState_Type.__name__ = "Integer32"
_SwitchCapSlbPortSerState_Object = MibTableColumn
switchCapSlbPortSerState = _SwitchCapSlbPortSerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4, 1, 1, 3),
    _SwitchCapSlbPortSerState_Type()
)
switchCapSlbPortSerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSlbPortSerState.setStatus("current")
_SwitchCapSlbPortFltState_Type = DisplayString
_SwitchCapSlbPortFltState_Object = MibTableColumn
switchCapSlbPortFltState = _SwitchCapSlbPortFltState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4, 1, 1, 4),
    _SwitchCapSlbPortFltState_Type()
)
switchCapSlbPortFltState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSlbPortFltState.setStatus("current")


class _SwitchCapSlbPortRTSState_Type(Integer32):
    """Custom type switchCapSlbPortRTSState based on Integer32"""
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


_SwitchCapSlbPortRTSState_Type.__name__ = "Integer32"
_SwitchCapSlbPortRTSState_Object = MibTableColumn
switchCapSlbPortRTSState = _SwitchCapSlbPortRTSState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 4, 1, 1, 5),
    _SwitchCapSlbPortRTSState_Type()
)
switchCapSlbPortRTSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCapSlbPortRTSState.setStatus("current")
_SwitchCapBwmInfo_ObjectIdentity = ObjectIdentity
switchCapBwmInfo = _SwitchCapBwmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5)
)
_BwmPoliciesMaxEnt_Type = Integer32
_BwmPoliciesMaxEnt_Object = MibScalar
bwmPoliciesMaxEnt = _BwmPoliciesMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 1),
    _BwmPoliciesMaxEnt_Type()
)
bwmPoliciesMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmPoliciesMaxEnt.setStatus("current")
_BwmPoliciesCurrEnt_Type = Integer32
_BwmPoliciesCurrEnt_Object = MibScalar
bwmPoliciesCurrEnt = _BwmPoliciesCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 2),
    _BwmPoliciesCurrEnt_Type()
)
bwmPoliciesCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmPoliciesCurrEnt.setStatus("current")
_BwmContsMaxEnt_Type = Integer32
_BwmContsMaxEnt_Object = MibScalar
bwmContsMaxEnt = _BwmContsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 3),
    _BwmContsMaxEnt_Type()
)
bwmContsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContsMaxEnt.setStatus("current")
_BwmContsCurrEnt_Type = DisplayString
_BwmContsCurrEnt_Object = MibScalar
bwmContsCurrEnt = _BwmContsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 4),
    _BwmContsCurrEnt_Type()
)
bwmContsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContsCurrEnt.setStatus("current")
_BwmGRsMaxEnt_Type = Integer32
_BwmGRsMaxEnt_Object = MibScalar
bwmGRsMaxEnt = _BwmGRsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 5),
    _BwmGRsMaxEnt_Type()
)
bwmGRsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmGRsMaxEnt.setStatus("current")
_BwmGRsCurrEnt_Type = Integer32
_BwmGRsCurrEnt_Object = MibScalar
bwmGRsCurrEnt = _BwmGRsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 6),
    _BwmGRsCurrEnt_Type()
)
bwmGRsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmGRsCurrEnt.setStatus("current")
_BwmContsPerGRs_Type = Integer32
_BwmContsPerGRs_Object = MibScalar
bwmContsPerGRs = _BwmContsPerGRs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 7),
    _BwmContsPerGRs_Type()
)
bwmContsPerGRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContsPerGRs.setStatus("current")
_BwmTimePoliciesPerCont_Type = Integer32
_BwmTimePoliciesPerCont_Object = MibScalar
bwmTimePoliciesPerCont = _BwmTimePoliciesPerCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 5, 8),
    _BwmTimePoliciesPerCont_Type()
)
bwmTimePoliciesPerCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmTimePoliciesPerCont.setStatus("current")
_SwitchCapSecInfo_ObjectIdentity = ObjectIdentity
switchCapSecInfo = _SwitchCapSecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6)
)
_ConfigSrcIPACLsMaxEnt_Type = Integer32
_ConfigSrcIPACLsMaxEnt_Object = MibScalar
configSrcIPACLsMaxEnt = _ConfigSrcIPACLsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 1),
    _ConfigSrcIPACLsMaxEnt_Type()
)
configSrcIPACLsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configSrcIPACLsMaxEnt.setStatus("current")
_ConfigSrcIPACLsCurrEnt_Type = Integer32
_ConfigSrcIPACLsCurrEnt_Object = MibScalar
configSrcIPACLsCurrEnt = _ConfigSrcIPACLsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 2),
    _ConfigSrcIPACLsCurrEnt_Type()
)
configSrcIPACLsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configSrcIPACLsCurrEnt.setStatus("current")
_BogonSrcIPACLsMaxEnt_Type = Integer32
_BogonSrcIPACLsMaxEnt_Object = MibScalar
bogonSrcIPACLsMaxEnt = _BogonSrcIPACLsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 3),
    _BogonSrcIPACLsMaxEnt_Type()
)
bogonSrcIPACLsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bogonSrcIPACLsMaxEnt.setStatus("current")
_BogonSrcIPACLsCurrEnt_Type = Integer32
_BogonSrcIPACLsCurrEnt_Object = MibScalar
bogonSrcIPACLsCurrEnt = _BogonSrcIPACLsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 4),
    _BogonSrcIPACLsCurrEnt_Type()
)
bogonSrcIPACLsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bogonSrcIPACLsCurrEnt.setStatus("current")
_OperSrcIPACLsMaxEnt_Type = Integer32
_OperSrcIPACLsMaxEnt_Object = MibScalar
operSrcIPACLsMaxEnt = _OperSrcIPACLsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 5),
    _OperSrcIPACLsMaxEnt_Type()
)
operSrcIPACLsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operSrcIPACLsMaxEnt.setStatus("current")
_OperSrcIPACLsCurrEnt_Type = Integer32
_OperSrcIPACLsCurrEnt_Object = MibScalar
operSrcIPACLsCurrEnt = _OperSrcIPACLsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 6),
    _OperSrcIPACLsCurrEnt_Type()
)
operSrcIPACLsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operSrcIPACLsCurrEnt.setStatus("current")
_TotalSrcIPACLsMaxEnt_Type = Integer32
_TotalSrcIPACLsMaxEnt_Object = MibScalar
totalSrcIPACLsMaxEnt = _TotalSrcIPACLsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 7),
    _TotalSrcIPACLsMaxEnt_Type()
)
totalSrcIPACLsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSrcIPACLsMaxEnt.setStatus("current")
_TotalSrcIPACLsCurrEnt_Type = Integer32
_TotalSrcIPACLsCurrEnt_Object = MibScalar
totalSrcIPACLsCurrEnt = _TotalSrcIPACLsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 8),
    _TotalSrcIPACLsCurrEnt_Type()
)
totalSrcIPACLsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSrcIPACLsCurrEnt.setStatus("current")
_ConfigDstIPACLsMaxEnt_Type = Integer32
_ConfigDstIPACLsMaxEnt_Object = MibScalar
configDstIPACLsMaxEnt = _ConfigDstIPACLsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 9),
    _ConfigDstIPACLsMaxEnt_Type()
)
configDstIPACLsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDstIPACLsMaxEnt.setStatus("current")
_ConfigDstIPACLsCurrEnt_Type = Integer32
_ConfigDstIPACLsCurrEnt_Object = MibScalar
configDstIPACLsCurrEnt = _ConfigDstIPACLsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 10),
    _ConfigDstIPACLsCurrEnt_Type()
)
configDstIPACLsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDstIPACLsCurrEnt.setStatus("current")
_OperDstIPACLsMaxEnt_Type = Integer32
_OperDstIPACLsMaxEnt_Object = MibScalar
operDstIPACLsMaxEnt = _OperDstIPACLsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 11),
    _OperDstIPACLsMaxEnt_Type()
)
operDstIPACLsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operDstIPACLsMaxEnt.setStatus("current")
_OperDstIPACLsCurrEnt_Type = Integer32
_OperDstIPACLsCurrEnt_Object = MibScalar
operDstIPACLsCurrEnt = _OperDstIPACLsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 12),
    _OperDstIPACLsCurrEnt_Type()
)
operDstIPACLsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operDstIPACLsCurrEnt.setStatus("current")
_TotalDstIPACLsMaxEnt_Type = Integer32
_TotalDstIPACLsMaxEnt_Object = MibScalar
totalDstIPACLsMaxEnt = _TotalDstIPACLsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 13),
    _TotalDstIPACLsMaxEnt_Type()
)
totalDstIPACLsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDstIPACLsMaxEnt.setStatus("current")
_TotalDstIPACLsCurrEnt_Type = Integer32
_TotalDstIPACLsCurrEnt_Object = MibScalar
totalDstIPACLsCurrEnt = _TotalDstIPACLsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 14),
    _TotalDstIPACLsCurrEnt_Type()
)
totalDstIPACLsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDstIPACLsCurrEnt.setStatus("current")
_IpDosAtkPrevention_Type = Integer32
_IpDosAtkPrevention_Object = MibScalar
ipDosAtkPrevention = _IpDosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 15),
    _IpDosAtkPrevention_Type()
)
ipDosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDosAtkPrevention.setStatus("current")
_TcpDosAtkPrevention_Type = Integer32
_TcpDosAtkPrevention_Object = MibScalar
tcpDosAtkPrevention = _TcpDosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 16),
    _TcpDosAtkPrevention_Type()
)
tcpDosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpDosAtkPrevention.setStatus("current")
_UdpDosAtkPrevention_Type = Integer32
_UdpDosAtkPrevention_Object = MibScalar
udpDosAtkPrevention = _UdpDosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 17),
    _UdpDosAtkPrevention_Type()
)
udpDosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpDosAtkPrevention.setStatus("current")
_IcmpDosAtkPrevention_Type = Integer32
_IcmpDosAtkPrevention_Object = MibScalar
icmpDosAtkPrevention = _IcmpDosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 18),
    _IcmpDosAtkPrevention_Type()
)
icmpDosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpDosAtkPrevention.setStatus("current")
_IgmpDosAtkPrevention_Type = Integer32
_IgmpDosAtkPrevention_Object = MibScalar
igmpDosAtkPrevention = _IgmpDosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 19),
    _IgmpDosAtkPrevention_Type()
)
igmpDosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpDosAtkPrevention.setStatus("current")
_ArpDosAtkPrevention_Type = Integer32
_ArpDosAtkPrevention_Object = MibScalar
arpDosAtkPrevention = _ArpDosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 20),
    _ArpDosAtkPrevention_Type()
)
arpDosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpDosAtkPrevention.setStatus("current")
_Ipv6DosAtkPrevention_Type = Integer32
_Ipv6DosAtkPrevention_Object = MibScalar
ipv6DosAtkPrevention = _Ipv6DosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 21),
    _Ipv6DosAtkPrevention_Type()
)
ipv6DosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DosAtkPrevention.setStatus("current")
_TotalDosAtkPrevention_Type = Integer32
_TotalDosAtkPrevention_Object = MibScalar
totalDosAtkPrevention = _TotalDosAtkPrevention_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 22),
    _TotalDosAtkPrevention_Type()
)
totalDosAtkPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDosAtkPrevention.setStatus("current")
_UdpBlastProtection_Type = Integer32
_UdpBlastProtection_Object = MibScalar
udpBlastProtection = _UdpBlastProtection_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 6, 23),
    _UdpBlastProtection_Type()
)
udpBlastProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBlastProtection.setStatus("current")
_SwitchCapGeneralInfo_ObjectIdentity = ObjectIdentity
switchCapGeneralInfo = _SwitchCapGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7)
)
_SyslogHostMaxEnt_Type = Integer32
_SyslogHostMaxEnt_Object = MibScalar
syslogHostMaxEnt = _SyslogHostMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 1),
    _SyslogHostMaxEnt_Type()
)
syslogHostMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogHostMaxEnt.setStatus("current")
_SyslogHostCurrEnt_Type = Integer32
_SyslogHostCurrEnt_Object = MibScalar
syslogHostCurrEnt = _SyslogHostCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 2),
    _SyslogHostCurrEnt_Type()
)
syslogHostCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogHostCurrEnt.setStatus("current")
_RadiusSerMaxEnt_Type = Integer32
_RadiusSerMaxEnt_Object = MibScalar
radiusSerMaxEnt = _RadiusSerMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 3),
    _RadiusSerMaxEnt_Type()
)
radiusSerMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSerMaxEnt.setStatus("current")
_RadiusSerCurrEnt_Type = Integer32
_RadiusSerCurrEnt_Object = MibScalar
radiusSerCurrEnt = _RadiusSerCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 4),
    _RadiusSerCurrEnt_Type()
)
radiusSerCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSerCurrEnt.setStatus("current")
_TacacsSerMaxEnt_Type = Integer32
_TacacsSerMaxEnt_Object = MibScalar
tacacsSerMaxEnt = _TacacsSerMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 5),
    _TacacsSerMaxEnt_Type()
)
tacacsSerMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacsSerMaxEnt.setStatus("current")
_TacacsSerCurrEnt_Type = Integer32
_TacacsSerCurrEnt_Object = MibScalar
tacacsSerCurrEnt = _TacacsSerCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 6),
    _TacacsSerCurrEnt_Type()
)
tacacsSerCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacsSerCurrEnt.setStatus("current")
_NtpSerMaxEnt_Type = Integer32
_NtpSerMaxEnt_Object = MibScalar
ntpSerMaxEnt = _NtpSerMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 7),
    _NtpSerMaxEnt_Type()
)
ntpSerMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSerMaxEnt.setStatus("current")
_NtpSerCurrEnt_Type = Integer32
_NtpSerCurrEnt_Object = MibScalar
ntpSerCurrEnt = _NtpSerCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 8),
    _NtpSerCurrEnt_Type()
)
ntpSerCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSerCurrEnt.setStatus("current")
_SmtpHostsMaxEnt_Type = Integer32
_SmtpHostsMaxEnt_Object = MibScalar
smtpHostsMaxEnt = _SmtpHostsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 9),
    _SmtpHostsMaxEnt_Type()
)
smtpHostsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpHostsMaxEnt.setStatus("current")
_SmtpHostsCurrEnt_Type = Integer32
_SmtpHostsCurrEnt_Object = MibScalar
smtpHostsCurrEnt = _SmtpHostsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 10),
    _SmtpHostsCurrEnt_Type()
)
smtpHostsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpHostsCurrEnt.setStatus("current")
_MgmtNetworksMaxEnt_Type = Integer32
_MgmtNetworksMaxEnt_Object = MibScalar
mgmtNetworksMaxEnt = _MgmtNetworksMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 11),
    _MgmtNetworksMaxEnt_Type()
)
mgmtNetworksMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtNetworksMaxEnt.setStatus("current")
_MgmtNetworksCurrEnt_Type = Integer32
_MgmtNetworksCurrEnt_Object = MibScalar
mgmtNetworksCurrEnt = _MgmtNetworksCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 12),
    _MgmtNetworksCurrEnt_Type()
)
mgmtNetworksCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtNetworksCurrEnt.setStatus("current")
_EndUsers_Type = Integer32
_EndUsers_Object = MibScalar
endUsers = _EndUsers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 13),
    _EndUsers_Type()
)
endUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endUsers.setStatus("current")
_PanicDumps_Type = Integer32
_PanicDumps_Object = MibScalar
panicDumps = _PanicDumps_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 14),
    _PanicDumps_Type()
)
panicDumps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panicDumps.setStatus("current")
_MpMemory_Type = DisplayString
_MpMemory_Object = MibScalar
mpMemory = _MpMemory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 15),
    _MpMemory_Type()
)
mpMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpMemory.setStatus("current")
_SpMemory_Type = DisplayString
_SpMemory_Object = MibScalar
spMemory = _SpMemory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 16),
    _SpMemory_Type()
)
spMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spMemory.setStatus("current")
_Snmpv3UsersMaxEnt_Type = Integer32
_Snmpv3UsersMaxEnt_Object = MibScalar
snmpv3UsersMaxEnt = _Snmpv3UsersMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 17),
    _Snmpv3UsersMaxEnt_Type()
)
snmpv3UsersMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3UsersMaxEnt.setStatus("current")
_Snmpv3UsersCurrEnt_Type = Integer32
_Snmpv3UsersCurrEnt_Object = MibScalar
snmpv3UsersCurrEnt = _Snmpv3UsersCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 18),
    _Snmpv3UsersCurrEnt_Type()
)
snmpv3UsersCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3UsersCurrEnt.setStatus("current")
_Snmpv3ViewsMaxEnt_Type = Integer32
_Snmpv3ViewsMaxEnt_Object = MibScalar
snmpv3ViewsMaxEnt = _Snmpv3ViewsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 19),
    _Snmpv3ViewsMaxEnt_Type()
)
snmpv3ViewsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3ViewsMaxEnt.setStatus("current")
_Snmpv3ViewsCurrEnt_Type = Integer32
_Snmpv3ViewsCurrEnt_Object = MibScalar
snmpv3ViewsCurrEnt = _Snmpv3ViewsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 20),
    _Snmpv3ViewsCurrEnt_Type()
)
snmpv3ViewsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3ViewsCurrEnt.setStatus("current")
_Snmpv3AccessGRsMaxEnt_Type = Integer32
_Snmpv3AccessGRsMaxEnt_Object = MibScalar
snmpv3AccessGRsMaxEnt = _Snmpv3AccessGRsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 21),
    _Snmpv3AccessGRsMaxEnt_Type()
)
snmpv3AccessGRsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3AccessGRsMaxEnt.setStatus("current")
_Snmpv3AccessGRsCurrEnt_Type = Integer32
_Snmpv3AccessGRsCurrEnt_Object = MibScalar
snmpv3AccessGRsCurrEnt = _Snmpv3AccessGRsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 22),
    _Snmpv3AccessGRsCurrEnt_Type()
)
snmpv3AccessGRsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3AccessGRsCurrEnt.setStatus("current")
_Snmpv3TargetAddrMaxEnt_Type = Integer32
_Snmpv3TargetAddrMaxEnt_Object = MibScalar
snmpv3TargetAddrMaxEnt = _Snmpv3TargetAddrMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 23),
    _Snmpv3TargetAddrMaxEnt_Type()
)
snmpv3TargetAddrMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3TargetAddrMaxEnt.setStatus("current")
_Snmpv3TargetAddrCurrEnt_Type = Integer32
_Snmpv3TargetAddrCurrEnt_Object = MibScalar
snmpv3TargetAddrCurrEnt = _Snmpv3TargetAddrCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 24),
    _Snmpv3TargetAddrCurrEnt_Type()
)
snmpv3TargetAddrCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3TargetAddrCurrEnt.setStatus("current")
_Snmpv3TargetParamsMaxEnt_Type = Integer32
_Snmpv3TargetParamsMaxEnt_Object = MibScalar
snmpv3TargetParamsMaxEnt = _Snmpv3TargetParamsMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 25),
    _Snmpv3TargetParamsMaxEnt_Type()
)
snmpv3TargetParamsMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3TargetParamsMaxEnt.setStatus("current")
_Snmpv3TargetParamsCurrEnt_Type = Integer32
_Snmpv3TargetParamsCurrEnt_Object = MibScalar
snmpv3TargetParamsCurrEnt = _Snmpv3TargetParamsCurrEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 3, 9, 7, 26),
    _Snmpv3TargetParamsCurrEnt_Type()
)
snmpv3TargetParamsCurrEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3TargetParamsCurrEnt.setStatus("current")
_AgentOper_ObjectIdentity = ObjectIdentity
agentOper = _AgentOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4)
)
_AgPortOperTable_Object = MibTable
agPortOperTable = _AgPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    agPortOperTable.setStatus("current")
_AgPortOperTableEntry_Object = MibTableRow
agPortOperTableEntry = _AgPortOperTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4, 1, 1)
)
agPortOperTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-SWITCH-MIB", "portOperIdx"),
)
if mibBuilder.loadTexts:
    agPortOperTableEntry.setStatus("current")
_PortOperIdx_Type = Integer32
_PortOperIdx_Object = MibTableColumn
portOperIdx = _PortOperIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4, 1, 1, 3),
    _PortOperRmon_Type()
)
portOperRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOperRmon.setStatus("current")
_AgNTPOper_ObjectIdentity = ObjectIdentity
agNTPOper = _AgNTPOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4, 2)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 1, 4, 2, 1),
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
    "ALTEON-CHEETAH-SWITCH-MIB",
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
       "agCurCfgSmtpHost": agCurCfgSmtpHost,
       "agNewCfgSmtpHost": agNewCfgSmtpHost,
       "agCurCfgConsole": agCurCfgConsole,
       "agNewCfgConsole": agNewCfgConsole,
       "agCurCfgBootp": agCurCfgBootp,
       "agNewCfgBootp": agNewCfgBootp,
       "agCurCfgSnmpTimeout": agCurCfgSnmpTimeout,
       "agNewCfgSnmpTimeout": agNewCfgSnmpTimeout,
       "agCurCfgTelnetServerPort": agCurCfgTelnetServerPort,
       "agNewCfgTelnetServerPort": agNewCfgTelnetServerPort,
       "agClearFlashDump": agClearFlashDump,
       "agCurCfgNortelMultipleStgMode": agCurCfgNortelMultipleStgMode,
       "agNewCfgNortelMultipleStgMode": agNewCfgNortelMultipleStgMode,
       "agCurCfgTrapSrcIf": agCurCfgTrapSrcIf,
       "agNewCfgTrapSrcIf": agNewCfgTrapSrcIf,
       "agCurCfgARPMaxRate": agCurCfgARPMaxRate,
       "agNewCfgARPMaxRate": agNewCfgARPMaxRate,
       "agCurCfgICMPMaxRate": agCurCfgICMPMaxRate,
       "agNewCfgICMPMaxRate": agNewCfgICMPMaxRate,
       "agCurCfgTCPMaxRate": agCurCfgTCPMaxRate,
       "agNewCfgTCPMaxRate": agNewCfgTCPMaxRate,
       "agCurCfgUDPMaxRate": agCurCfgUDPMaxRate,
       "agNewCfgUDPMaxRate": agNewCfgUDPMaxRate,
       "agCurCfgHttpsServerPort": agCurCfgHttpsServerPort,
       "agNewCfgHttpsServerPort": agNewCfgHttpsServerPort,
       "agCurDaylightSavings": agCurDaylightSavings,
       "agNewDaylightSavings": agNewDaylightSavings,
       "agCurCfgIdleCLITimeout": agCurCfgIdleCLITimeout,
       "agNewCfgIdleCLITimeout": agNewCfgIdleCLITimeout,
       "agCurCfgXMLCfgServerPort": agCurCfgXMLCfgServerPort,
       "agNewCfgXMLCfgServerPort": agNewCfgXMLCfgServerPort,
       "agSymantecGlobalState": agSymantecGlobalState,
       "agPortConfig": agPortConfig,
       "agPortTableMaxEnt": agPortTableMaxEnt,
       "agPortCurCfgTable": agPortCurCfgTable,
       "agPortCurCfgTableEntry": agPortCurCfgTableEntry,
       "agPortCurCfgIndx": agPortCurCfgIndx,
       "agPortCurCfgState": agPortCurCfgState,
       "agPortCurCfgVlanTag": agPortCurCfgVlanTag,
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
       "agPortCurCfgLinkTrap": agPortCurCfgLinkTrap,
       "agPortCurCfgPreferred": agPortCurCfgPreferred,
       "agPortCurCfgBackup": agPortCurCfgBackup,
       "agPortCurCfgEgressBW": agPortCurCfgEgressBW,
       "agPortCurCfgNonIPBwmContract": agPortCurCfgNonIPBwmContract,
       "agPortCurCfgGigEthSpeed": agPortCurCfgGigEthSpeed,
       "agPortCurCfgGigEthMode": agPortCurCfgGigEthMode,
       "agPortCurCfgPortAlias": agPortCurCfgPortAlias,
       "agPortNewCfgTable": agPortNewCfgTable,
       "agPortNewCfgTableEntry": agPortNewCfgTableEntry,
       "agPortNewCfgIndx": agPortNewCfgIndx,
       "agPortNewCfgState": agPortNewCfgState,
       "agPortNewCfgVlanTag": agPortNewCfgVlanTag,
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
       "agPortNewCfgLinkTrap": agPortNewCfgLinkTrap,
       "agPortNewCfgPreferred": agPortNewCfgPreferred,
       "agPortNewCfgBackup": agPortNewCfgBackup,
       "agPortNewCfgEgressBW": agPortNewCfgEgressBW,
       "agPortNewCfgNonIPBwmContract": agPortNewCfgNonIPBwmContract,
       "agPortNewCfgGigEthSpeed": agPortNewCfgGigEthSpeed,
       "agPortNewCfgGigEthMode": agPortNewCfgGigEthMode,
       "agPortNewCfgPortAlias": agPortNewCfgPortAlias,
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
       "agNewCfgSyslogTrapIp": agNewCfgSyslogTrapIp,
       "agCurCfgSyslogTrapIp": agCurCfgSyslogTrapIp,
       "agNewCfgSyslogTrapWeb": agNewCfgSyslogTrapWeb,
       "agCurCfgSyslogTrapWeb": agCurCfgSyslogTrapWeb,
       "agNewCfgSyslogTrapSynAtk": agNewCfgSyslogTrapSynAtk,
       "agCurCfgSyslogTrapSynAtk": agCurCfgSyslogTrapSynAtk,
       "agNewCfgSyslogTrapTcpLim": agNewCfgSyslogTrapTcpLim,
       "agCurCfgSyslogTrapTcpLim": agCurCfgSyslogTrapTcpLim,
       "agNewCfgSyslogTrapOspf": agNewCfgSyslogTrapOspf,
       "agCurCfgSyslogTrapOspf": agCurCfgSyslogTrapOspf,
       "agNewCfgSyslogTrapSecurity": agNewCfgSyslogTrapSecurity,
       "agCurCfgSyslogTrapSecurity": agCurCfgSyslogTrapSecurity,
       "agNewCfgSyslogTrapRmon": agNewCfgSyslogTrapRmon,
       "agCurCfgSyslogTrapRmon": agCurCfgSyslogTrapRmon,
       "agNewCfgSyslogTrapSlbAtk": agNewCfgSyslogTrapSlbAtk,
       "agCurCfgSyslogTrapSlbAtk": agCurCfgSyslogTrapSlbAtk,
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
       "agTftpPort": agTftpPort,
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
       "agMgmt": agMgmt,
       "agMgmtCurCfgIpAddr": agMgmtCurCfgIpAddr,
       "agMgmtNewCfgIpAddr": agMgmtNewCfgIpAddr,
       "agMgmtCurCfgMask": agMgmtCurCfgMask,
       "agMgmtNewCfgMask": agMgmtNewCfgMask,
       "agMgmtCurCfgGateway": agMgmtCurCfgGateway,
       "agMgmtNewCfgGateway": agMgmtNewCfgGateway,
       "agMgmtCurCfgState": agMgmtCurCfgState,
       "agMgmtNewCfgState": agMgmtNewCfgState,
       "agMgmtCurCfgNtp": agMgmtCurCfgNtp,
       "agMgmtNewCfgNtp": agMgmtNewCfgNtp,
       "agMgmtCurCfgRadius": agMgmtCurCfgRadius,
       "agMgmtNewCfgRadius": agMgmtNewCfgRadius,
       "agMgmtCurCfgSmtp": agMgmtCurCfgSmtp,
       "agMgmtNewCfgSmtp": agMgmtNewCfgSmtp,
       "agMgmtCurCfgSnmp": agMgmtCurCfgSnmp,
       "agMgmtNewCfgSnmp": agMgmtNewCfgSnmp,
       "agMgmtCurCfgSyslog": agMgmtCurCfgSyslog,
       "agMgmtNewCfgSyslog": agMgmtNewCfgSyslog,
       "agMgmtCurCfgTftp": agMgmtCurCfgTftp,
       "agMgmtNewCfgTftp": agMgmtNewCfgTftp,
       "agMgmtPort": agMgmtPort,
       "agMgmtPortCurCfgSpeed": agMgmtPortCurCfgSpeed,
       "agMgmtPortNewCfgSpeed": agMgmtPortNewCfgSpeed,
       "agMgmtPortCurCfgMode": agMgmtPortCurCfgMode,
       "agMgmtPortNewCfgMode": agMgmtPortNewCfgMode,
       "agMgmtPortCurCfgAuto": agMgmtPortCurCfgAuto,
       "agMgmtPortNewCfgAuto": agMgmtPortNewCfgAuto,
       "agMgmtCurCfgDns": agMgmtCurCfgDns,
       "agMgmtNewCfgDns": agMgmtNewCfgDns,
       "agMgmtCurCfgTacacs": agMgmtCurCfgTacacs,
       "agMgmtNewCfgTacacs": agMgmtNewCfgTacacs,
       "agMgmtCurCfgIntr": agMgmtCurCfgIntr,
       "agMgmtNewCfgIntr": agMgmtNewCfgIntr,
       "agMgmtCurCfgRetry": agMgmtCurCfgRetry,
       "agMgmtNewCfgRetry": agMgmtNewCfgRetry,
       "agMgmtCurCfgSonmp": agMgmtCurCfgSonmp,
       "agMgmtNewCfgSonmp": agMgmtNewCfgSonmp,
       "agMgmtCurCfgWlm": agMgmtCurCfgWlm,
       "agMgmtNewCfgWlm": agMgmtNewCfgWlm,
       "agMgmtCurCfgReport": agMgmtCurCfgReport,
       "agMgmtNewCfgReport": agMgmtNewCfgReport,
       "agSslproc": agSslproc,
       "agSslprocCurCfgIpAddr": agSslprocCurCfgIpAddr,
       "agSslprocNewCfgIpAddr": agSslprocNewCfgIpAddr,
       "agSslprocCurCfgPort": agSslprocCurCfgPort,
       "agSslprocNewCfgPort": agSslprocNewCfgPort,
       "agSslprocCurCfgRts": agSslprocCurCfgRts,
       "agSslprocNewCfgRts": agSslprocNewCfgRts,
       "agSslprocCurCfgFilt": agSslprocCurCfgFilt,
       "agSslprocNewCfgFilt": agSslprocNewCfgFilt,
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
       "tacCurCfgCmap": tacCurCfgCmap,
       "tacNewCfgCmap": tacNewCfgCmap,
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
       "agBoot": agBoot,
       "agCfgBootWeekday": agCfgBootWeekday,
       "agCfgBootHour": agCfgBootHour,
       "agCfgBootMin": agCfgBootMin,
       "agCfgBootReset": agCfgBootReset,
       "agCfgBootNxtResetTime": agCfgBootNxtResetTime,
       "agSecurity": agSecurity,
       "agPgroup": agPgroup,
       "agPgrpMatchTableMaxSize": agPgrpMatchTableMaxSize,
       "agCurCfgPgrpMatchTable": agCurCfgPgrpMatchTable,
       "agCurCfgPgrpMatchEntry": agCurCfgPgrpMatchEntry,
       "agCurCfgPgrpMatchIndex": agCurCfgPgrpMatchIndex,
       "agCurCfgPgrpName": agCurCfgPgrpName,
       "agCurCfgPgrpMatchBmap": agCurCfgPgrpMatchBmap,
       "agNewCfgPgrpMatchTable": agNewCfgPgrpMatchTable,
       "agNewCfgPgrpMatchEntry": agNewCfgPgrpMatchEntry,
       "agNewCfgPgrpMatchIndex": agNewCfgPgrpMatchIndex,
       "agNewCfgPgrpName": agNewCfgPgrpName,
       "agNewCfgPgrpMatchAdd": agNewCfgPgrpMatchAdd,
       "agNewCfgPgrpMatchRem": agNewCfgPgrpMatchRem,
       "agNewCfgPgrpMatchBmap": agNewCfgPgrpMatchBmap,
       "agNewCfgPgrpDelete": agNewCfgPgrpDelete,
       "agCfgSecurityPortTable": agCfgSecurityPortTable,
       "agCfgSecurityPortTableEntry": agCfgSecurityPortTableEntry,
       "agCfgSecurityPortIndx": agCfgSecurityPortIndx,
       "agCurCfgSecurityDosState": agCurCfgSecurityDosState,
       "agNewCfgSecurityDosState": agNewCfgSecurityDosState,
       "agCurCfgSecurityIpAclState": agCurCfgSecurityIpAclState,
       "agNewCfgSecurityIpAclState": agNewCfgSecurityIpAclState,
       "agCurCfgSecurityUbState": agCurCfgSecurityUbState,
       "agNewCfgSecurityUbState": agNewCfgSecurityUbState,
       "agCurCfgSecurityBogonState": agCurCfgSecurityBogonState,
       "agNewCfgSecurityBogonState": agNewCfgSecurityBogonState,
       "agCurCfgSecurityAttacksBmap": agCurCfgSecurityAttacksBmap,
       "agNewCfgSecurityAttacksBmap": agNewCfgSecurityAttacksBmap,
       "agNewCfgSecurityAddAttack": agNewCfgSecurityAddAttack,
       "agNewCfgSecurityRemAttack": agNewCfgSecurityRemAttack,
       "agNewCfgSecurityDoSAttacks": agNewCfgSecurityDoSAttacks,
       "agCurCfgSecuritySymantecState": agCurCfgSecuritySymantecState,
       "agNewCfgSecuritySymantecState": agNewCfgSecuritySymantecState,
       "ipAclCfg": ipAclCfg,
       "ipAclTableMaxSize": ipAclTableMaxSize,
       "ipAclCurCfgTable": ipAclCurCfgTable,
       "ipAclCurCfgEntry": ipAclCurCfgEntry,
       "ipAclCurCfgIndx": ipAclCurCfgIndx,
       "ipAclCurCfgIp": ipAclCurCfgIp,
       "ipAclCurCfgMask": ipAclCurCfgMask,
       "ipAclNewCfgTable": ipAclNewCfgTable,
       "ipAclNewCfgEntry": ipAclNewCfgEntry,
       "ipAclNewCfgIndx": ipAclNewCfgIndx,
       "ipAclNewCfgIp": ipAclNewCfgIp,
       "ipAclNewCfgAction": ipAclNewCfgAction,
       "ipAclNewCfgMask": ipAclNewCfgMask,
       "udpBlastCfg": udpBlastCfg,
       "udpBlastudpPortTableMaxSize": udpBlastudpPortTableMaxSize,
       "udpBlastCurCfgudpPortPacketLimit": udpBlastCurCfgudpPortPacketLimit,
       "udpBlastCurCfgudpPortTable": udpBlastCurCfgudpPortTable,
       "udpBlastCurCfgudpPortEntry": udpBlastCurCfgudpPortEntry,
       "udpBlastCurCfgudpPortLowIndx": udpBlastCurCfgudpPortLowIndx,
       "udpBlastCurCfgudpPortHighIndx": udpBlastCurCfgudpPortHighIndx,
       "udpBlastCurCfgudpPortEntryPacketLimit": udpBlastCurCfgudpPortEntryPacketLimit,
       "udpBlastNewCfgudpPortPacketLimit": udpBlastNewCfgudpPortPacketLimit,
       "udpBlastNewCfgudpPortTable": udpBlastNewCfgudpPortTable,
       "udpBlastNewCfgudpPortEntry": udpBlastNewCfgudpPortEntry,
       "udpBlastNewCfgudpPortLowIndx": udpBlastNewCfgudpPortLowIndx,
       "udpBlastNewCfgudpPortHighIndx": udpBlastNewCfgudpPortHighIndx,
       "udpBlastNewCfgudpPortEntryDelete": udpBlastNewCfgudpPortEntryDelete,
       "udpBlastNewCfgudpPortEntryPacketLimit": udpBlastNewCfgudpPortEntryPacketLimit,
       "secGeneralCfg": secGeneralCfg,
       "secCurCfgSecurityLogThreshold": secCurCfgSecurityLogThreshold,
       "secNewCfgSecurityLogThreshold": secNewCfgSecurityLogThreshold,
       "secCurCfgPacketDepth": secCurCfgPacketDepth,
       "secNewCfgPacketDepth": secNewCfgPacketDepth,
       "secCurCfgIpAclSyslogThreshold": secCurCfgIpAclSyslogThreshold,
       "secNewCfgIpAclSyslogThreshold": secNewCfgIpAclSyslogThreshold,
       "secCurCfgIpAclSyslogTime": secCurCfgIpAclSyslogTime,
       "secNewCfgIpAclSyslogTime": secNewCfgIpAclSyslogTime,
       "dosAttackPrevCfg": dosAttackPrevCfg,
       "dosCurCfgIPTTL": dosCurCfgIPTTL,
       "dosNewCfgIPTTL": dosNewCfgIPTTL,
       "dosCurCfgIPProt": dosCurCfgIPProt,
       "dosNewCfgIPProt": dosNewCfgIPProt,
       "dosCurCfgFragdata": dosCurCfgFragdata,
       "dosNewCfgFragdata": dosNewCfgFragdata,
       "dosCurCfgFragoff": dosCurCfgFragoff,
       "dosNewCfgFragoff": dosNewCfgFragoff,
       "dosCurCfgSYNdata": dosCurCfgSYNdata,
       "dosNewCfgSYNdata": dosNewCfgSYNdata,
       "dosCurCfgICMPdata": dosCurCfgICMPdata,
       "dosNewCfgICMPdata": dosNewCfgICMPdata,
       "dosCurCfgICMPoff": dosCurCfgICMPoff,
       "dosNewCfgICMPoff": dosNewCfgICMPoff,
       "ipDstAclCfg": ipDstAclCfg,
       "ipDstAclTableMaxSize": ipDstAclTableMaxSize,
       "ipDstAclCurCfgTable": ipDstAclCurCfgTable,
       "ipDstAclCurCfgEntry": ipDstAclCurCfgEntry,
       "ipDstAclCurCfgIndx": ipDstAclCurCfgIndx,
       "ipDstAclCurCfgIp": ipDstAclCurCfgIp,
       "ipDstAclCurCfgMask": ipDstAclCurCfgMask,
       "ipDstAclNewCfgTable": ipDstAclNewCfgTable,
       "ipDstAclNewCfgEntry": ipDstAclNewCfgEntry,
       "ipDstAclNewCfgIndx": ipDstAclNewCfgIndx,
       "ipDstAclNewCfgIp": ipDstAclNewCfgIp,
       "ipDstAclNewCfgAction": ipDstAclNewCfgAction,
       "ipDstAclNewCfgMask": ipDstAclNewCfgMask,
       "symantecCfg": symantecCfg,
       "symSigBwmMappingTableMaxSize": symSigBwmMappingTableMaxSize,
       "symCurCfgSigBwmMappingTable": symCurCfgSigBwmMappingTable,
       "symCurCfgSigBwmMappingTableEntry": symCurCfgSigBwmMappingTableEntry,
       "symCurCfgTblIndex": symCurCfgTblIndex,
       "symCurCfgSignatureID": symCurCfgSignatureID,
       "symCurCfgInContractID": symCurCfgInContractID,
       "symCurCfgOutContractID": symCurCfgOutContractID,
       "symNewCfgSigBwmMappingTable": symNewCfgSigBwmMappingTable,
       "symNewCfgSigBwmMappingTableEntry": symNewCfgSigBwmMappingTableEntry,
       "symNewCfgTblIndex": symNewCfgTblIndex,
       "symNewCfgSignatureID": symNewCfgSignatureID,
       "symNewCfgInContractID": symNewCfgInContractID,
       "symNewCfgOutContractID": symNewCfgOutContractID,
       "symNewCfgDeleteEntry": symNewCfgDeleteEntry,
       "symNewCfgDefaultAction": symNewCfgDefaultAction,
       "symCurCfgDefaultAction": symCurCfgDefaultAction,
       "symSigFileVersionSeqNumber": symSigFileVersionSeqNumber,
       "agSonmp": agSonmp,
       "agCurCfgSonmpSrcIf": agCurCfgSonmpSrcIf,
       "agNewCfgSonmpSrcIf": agNewCfgSonmpSrcIf,
       "agPortAccessCfg": agPortAccessCfg,
       "agPortAccessTableMaxSize": agPortAccessTableMaxSize,
       "agCurCfgPortAccessTable": agCurCfgPortAccessTable,
       "agCurCfgPortAccessEntry": agCurCfgPortAccessEntry,
       "agCurCfgPortAccessIndex": agCurCfgPortAccessIndex,
       "agCurCfgPortAccessState": agCurCfgPortAccessState,
       "agNewCfgPortAccessTable": agNewCfgPortAccessTable,
       "agNewCfgPortAccessEntry": agNewCfgPortAccessEntry,
       "agNewCfgPortAccessIndex": agNewCfgPortAccessIndex,
       "agNewCfgPortAccessState": agNewCfgPortAccessState,
       "agSave": agSave,
       "agSaveConfig": agSaveConfig,
       "agSaveTableSize": agSaveTableSize,
       "agSaveTable": agSaveTable,
       "agSaveTableEntry": agSaveTableEntry,
       "agSaveIndex": agSaveIndex,
       "agSaveString": agSaveString,
       "agFileTransfer": agFileTransfer,
       "agFileSize": agFileSize,
       "agFileTransferState": agFileTransferState,
       "agFileTableMissingRows": agFileTableMissingRows,
       "agFileType": agFileType,
       "agFileTableSize": agFileTableSize,
       "agFileTable": agFileTable,
       "agFileTableEntry": agFileTableEntry,
       "agFileIndex": agFileIndex,
       "agFileString": agFileString,
       "agFileErrorTableSize": agFileErrorTableSize,
       "agFileErrorTable": agFileErrorTable,
       "agFileErrorTableEntry": agFileErrorTableEntry,
       "agFileErrorIndex": agFileErrorIndex,
       "agFileErrorString": agFileErrorString,
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
       "pktStatsDiscards": pktStatsDiscards,
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
       "portStatsPhyIfInMcastPkts": portStatsPhyIfInMcastPkts,
       "portStatsPhyIfOutMcastPkts": portStatsPhyIfOutMcastPkts,
       "spStats": spStats,
       "spStatsCpuUtilTable": spStatsCpuUtilTable,
       "spStatsCpuUtilTableEntry": spStatsCpuUtilTableEntry,
       "spStatsCpuUtilSpIndex": spStatsCpuUtilSpIndex,
       "spStatsCpuUtil1Second": spStatsCpuUtil1Second,
       "spStatsCpuUtil4Seconds": spStatsCpuUtil4Seconds,
       "spStatsCpuUtil64Seconds": spStatsCpuUtil64Seconds,
       "spMaintStatsTable": spMaintStatsTable,
       "spMaintStatsTableEntry": spMaintStatsTableEntry,
       "spMaintStatsSpIndex": spMaintStatsSpIndex,
       "spMaintStatsPfdbFreeEmpty": spMaintStatsPfdbFreeEmpty,
       "spMaintStatsResolveErrNoddw": spMaintStatsResolveErrNoddw,
       "spMaintStatsLearnErrNoddw": spMaintStatsLearnErrNoddw,
       "spMaintStatsAgeMPNoddw": spMaintStatsAgeMPNoddw,
       "spMaintStatsDeleteMiss": spMaintStatsDeleteMiss,
       "spMaintStatsRecvLetErrorsMP": spMaintStatsRecvLetErrorsMP,
       "spMaintStatsRecvLetErrorsSP1": spMaintStatsRecvLetErrorsSP1,
       "spMaintStatsRecvLetErrorsSP2": spMaintStatsRecvLetErrorsSP2,
       "spMaintStatsRecvLetErrorsSP3": spMaintStatsRecvLetErrorsSP3,
       "spMaintStatsRecvLetErrorsSP4": spMaintStatsRecvLetErrorsSP4,
       "spMaintStatsSendLetFailsMP": spMaintStatsSendLetFailsMP,
       "spMaintStatsSendLetFailsSP1": spMaintStatsSendLetFailsSP1,
       "spMaintStatsSendLetFailsSP2": spMaintStatsSendLetFailsSP2,
       "spMaintStatsSendLetFailsSP3": spMaintStatsSendLetFailsSP3,
       "spMaintStatsSendLetFailsSP4": spMaintStatsSendLetFailsSP4,
       "spMaintStatsRecvLetSuccessMP": spMaintStatsRecvLetSuccessMP,
       "spMaintStatsRecvLetSuccessSP1": spMaintStatsRecvLetSuccessSP1,
       "spMaintStatsRecvLetSuccessSP2": spMaintStatsRecvLetSuccessSP2,
       "spMaintStatsRecvLetSuccessSP3": spMaintStatsRecvLetSuccessSP3,
       "spMaintStatsRecvLetSuccessSP4": spMaintStatsRecvLetSuccessSP4,
       "spMaintStatsSendLetSuccessMP": spMaintStatsSendLetSuccessMP,
       "spMaintStatsSendLetSuccessSP1": spMaintStatsSendLetSuccessSP1,
       "spMaintStatsSendLetSuccessSP2": spMaintStatsSendLetSuccessSP2,
       "spMaintStatsSendLetSuccessSP3": spMaintStatsSendLetSuccessSP3,
       "spMaintStatsSendLetSuccessSP4": spMaintStatsSendLetSuccessSP4,
       "spMaintStatsRateLimitArpDrops": spMaintStatsRateLimitArpDrops,
       "spMaintStatsRateLimitIcmpDrops": spMaintStatsRateLimitIcmpDrops,
       "spMaintStatsRateLimitTcpDrops": spMaintStatsRateLimitTcpDrops,
       "spMaintStatsRateLimitUdpDrops": spMaintStatsRateLimitUdpDrops,
       "spMemStatsTable": spMemStatsTable,
       "spMemStatsTableEntry": spMemStatsTableEntry,
       "spMemStatsIndex": spMemStatsIndex,
       "spMemStatsTotal": spMemStatsTotal,
       "spMemStatsCurr": spMemStatsCurr,
       "spMemStatsAllocs": spMemStatsAllocs,
       "spMemStatsFrees": spMemStatsFrees,
       "spMemStatsAllocsFailures": spMemStatsAllocsFailures,
       "spMemStatsHiWat": spMemStatsHiWat,
       "mgmtStats": mgmtStats,
       "mgmtStatsRxpackets": mgmtStatsRxpackets,
       "mgmtStatsRxErrors": mgmtStatsRxErrors,
       "mgmtStatsRxDropped": mgmtStatsRxDropped,
       "mgmtStatsRxOverruns": mgmtStatsRxOverruns,
       "mgmtStatsRxFrame": mgmtStatsRxFrame,
       "mgmtStatsTxpackets": mgmtStatsTxpackets,
       "mgmtStatsTxErrors": mgmtStatsTxErrors,
       "mgmtStatsTxDropped": mgmtStatsTxDropped,
       "mgmtStatsTxOverruns": mgmtStatsTxOverruns,
       "mgmtStatsTxCarrier": mgmtStatsTxCarrier,
       "mgmtStatsTxCollisions": mgmtStatsTxCollisions,
       "mgmtStatsTxQueueLen": mgmtStatsTxQueueLen,
       "mgmtStatsRxBytes": mgmtStatsRxBytes,
       "mgmtStatsRxMulticast": mgmtStatsRxMulticast,
       "mgmtStatsTxBytes": mgmtStatsTxBytes,
       "securityStats": securityStats,
       "agDosPortStatsTable": agDosPortStatsTable,
       "agDosPortStatsTableEntry": agDosPortStatsTableEntry,
       "agDosPortStatsIndx": agDosPortStatsIndx,
       "agDosPortStatsIPLen": agDosPortStatsIPLen,
       "agDosPortStatsIPVersion": agDosPortStatsIPVersion,
       "agDosPortStatsBroadcast": agDosPortStatsBroadcast,
       "agDosPortStatsLoopback": agDosPortStatsLoopback,
       "agDosPortStatsLand": agDosPortStatsLand,
       "agDosPortStatsIPReserved": agDosPortStatsIPReserved,
       "agDosPortStatsIPTTL": agDosPortStatsIPTTL,
       "agDosPortStatsIPProt": agDosPortStatsIPProt,
       "agDosPortStatsIPOptLen": agDosPortStatsIPOptLen,
       "agDosPortStatsFragMoreDont": agDosPortStatsFragMoreDont,
       "agDosPortStatsFragData": agDosPortStatsFragData,
       "agDosPortStatsFragBoundary": agDosPortStatsFragBoundary,
       "agDosPortStatsFragLast": agDosPortStatsFragLast,
       "agDosPortStatsFragDontOff": agDosPortStatsFragDontOff,
       "agDosPortStatsFragOpt": agDosPortStatsFragOpt,
       "agDosPortStatsFragOff": agDosPortStatsFragOff,
       "agDosPortStatsFragOversize": agDosPortStatsFragOversize,
       "agDosPortStatsTCPLen": agDosPortStatsTCPLen,
       "agDosPortStatsTCPPortZero": agDosPortStatsTCPPortZero,
       "agDosPortStatsBlatAttack": agDosPortStatsBlatAttack,
       "agDosPortStatsTCPReserved": agDosPortStatsTCPReserved,
       "agDosPortStatsNullScanAttack": agDosPortStatsNullScanAttack,
       "agDosPortStatsFullXmasScan": agDosPortStatsFullXmasScan,
       "agDosPortStatsFinScan": agDosPortStatsFinScan,
       "agDosPortStatsVecnaScan": agDosPortStatsVecnaScan,
       "agDosPortStatsXmasScanAttack": agDosPortStatsXmasScanAttack,
       "agDosPortStatsSynFinScan": agDosPortStatsSynFinScan,
       "agDosPortStatsFlagAbnormal": agDosPortStatsFlagAbnormal,
       "agDosPortStatsSYNData": agDosPortStatsSYNData,
       "agDosPortStatsSYNFrag": agDosPortStatsSYNFrag,
       "agDosPortStatsFTPPort": agDosPortStatsFTPPort,
       "agDosPortStatsDNSPort": agDosPortStatsDNSPort,
       "agDosPortStatsSeqZero": agDosPortStatsSeqZero,
       "agDosPortStatsAckZero": agDosPortStatsAckZero,
       "agDosPortStatsTCPOptLen": agDosPortStatsTCPOptLen,
       "agDosPortStatsUDPLen": agDosPortStatsUDPLen,
       "agDosPortStatsUDPPortZero": agDosPortStatsUDPPortZero,
       "agDosPortStatsFraggleAttack": agDosPortStatsFraggleAttack,
       "agDosPortStatsPepsi": agDosPortStatsPepsi,
       "agDosPortStatsRc8": agDosPortStatsRc8,
       "agDosPortStatsSNMPNull": agDosPortStatsSNMPNull,
       "agDosPortStatsICMPLen": agDosPortStatsICMPLen,
       "agDosPortStatsSmurfAttack": agDosPortStatsSmurfAttack,
       "agDosPortStatsICMPData": agDosPortStatsICMPData,
       "agDosPortStatsICMPOff": agDosPortStatsICMPOff,
       "agDosPortStatsICMPType": agDosPortStatsICMPType,
       "agDosPortStatsIGMPLen": agDosPortStatsIGMPLen,
       "agDosPortStatsIGMPFrag": agDosPortStatsIGMPFrag,
       "agDosPortStatsIGMPType": agDosPortStatsIGMPType,
       "agDosPortStatsARPLen": agDosPortStatsARPLen,
       "agDosPortStatsARPNbCast": agDosPortStatsARPNbCast,
       "agDosPortStatsARPNuCast": agDosPortStatsARPNuCast,
       "agDosPortStatsARPSpoof": agDosPortStatsARPSpoof,
       "agDosPortStatsGARP": agDosPortStatsGARP,
       "agDosPortStatsIP6Len": agDosPortStatsIP6Len,
       "agDosPortStatsIP6Version": agDosPortStatsIP6Version,
       "agSecurityPgrpStatsTable": agSecurityPgrpStatsTable,
       "agSecurityPgrpStatsTableEntry": agSecurityPgrpStatsTableEntry,
       "agSecurityPgrpStatsIndx": agSecurityPgrpStatsIndx,
       "agSecurityPgrpStatsName": agSecurityPgrpStatsName,
       "agSecurityPgrpStatsHits": agSecurityPgrpStatsHits,
       "agSecurityUbStatsTable": agSecurityUbStatsTable,
       "agSecurityUbStatsTableEntry": agSecurityUbStatsTableEntry,
       "agSecurityUbStatsIndx": agSecurityUbStatsIndx,
       "agSecurityUbStatsPort": agSecurityUbStatsPort,
       "agSecurityUbStatsBlockedPacket": agSecurityUbStatsBlockedPacket,
       "agSecurityUbStatsPacketRate": agSecurityUbStatsPacketRate,
       "agSecurityIpAclStatsTable": agSecurityIpAclStatsTable,
       "agSecurityIpAclStatsTableEntry": agSecurityIpAclStatsTableEntry,
       "agSecurityIpAclStatsIndx": agSecurityIpAclStatsIndx,
       "agSecurityIpAclStatsAddress": agSecurityIpAclStatsAddress,
       "agSecurityIpAclStatsBlockedPacket": agSecurityIpAclStatsBlockedPacket,
       "agSecurityIpDstAclStatsTable": agSecurityIpDstAclStatsTable,
       "agSecurityIpDstAclStatsTableEntry": agSecurityIpDstAclStatsTableEntry,
       "agSecurityIpDstAclStatsIndx": agSecurityIpDstAclStatsIndx,
       "agSecurityIpDstAclStatsAddress": agSecurityIpDstAclStatsAddress,
       "agSecurityIpDstAclStatsBlockedPacket": agSecurityIpDstAclStatsBlockedPacket,
       "symantecStats": symantecStats,
       "symStatsTotalHits": symStatsTotalHits,
       "symStatsClear": symStatsClear,
       "symStatsSourceIp": symStatsSourceIp,
       "symStatsSourcePort": symStatsSourcePort,
       "symStatsDestIp": symStatsDestIp,
       "symStatsDestPort": symStatsDestPort,
       "symStatsProtocol": symStatsProtocol,
       "symStatsLastHitId": symStatsLastHitId,
       "symStatsConfiguredHitsMax": symStatsConfiguredHitsMax,
       "symStatsConfiguredHitsTable": symStatsConfiguredHitsTable,
       "symStatsConfiguredHitsTableEntry": symStatsConfiguredHitsTableEntry,
       "symStatsConfiguredHitsTblIndex": symStatsConfiguredHitsTblIndex,
       "symStatsConfiguredHitsSigId": symStatsConfiguredHitsSigId,
       "symStatsConfiguredHitsTotalSpHCount": symStatsConfiguredHitsTotalSpHCount,
       "symStatsConfiguredHitsInCont": symStatsConfiguredHitsInCont,
       "symStatsConfiguredHitsOutCont": symStatsConfiguredHitsOutCont,
       "symStatsConfiguredHitsLastHitTime": symStatsConfiguredHitsLastHitTime,
       "symStatsConfiguredHitsCountOnSpTable": symStatsConfiguredHitsCountOnSpTable,
       "symStatsConfiguredHitsCountOnSpTableEntry": symStatsConfiguredHitsCountOnSpTableEntry,
       "symStatsConfiguredHitsCountOnSpTblIndex": symStatsConfiguredHitsCountOnSpTblIndex,
       "symStatsConfiguredHitsCountOnSpTblSpIndex": symStatsConfiguredHitsCountOnSpTblSpIndex,
       "symStatsConfiguredHitsCountOnSpTblHitCount": symStatsConfiguredHitsCountOnSpTblHitCount,
       "symStatsUnconfiguredHitsMax": symStatsUnconfiguredHitsMax,
       "symStatsUnconfiguredHitsTable": symStatsUnconfiguredHitsTable,
       "symStatsUnconfiguredHitsTableEntry": symStatsUnconfiguredHitsTableEntry,
       "symStatsUnconfiguredHitsTblIndex": symStatsUnconfiguredHitsTblIndex,
       "symStatsUnconfiguredHitsSigId": symStatsUnconfiguredHitsSigId,
       "symStatsUnconfiguredHitsTotalSpHCount": symStatsUnconfiguredHitsTotalSpHCount,
       "symStatsUnconfiguredHitsLastHitTime": symStatsUnconfiguredHitsLastHitTime,
       "symStatsUnconfiguredHitsCountOnSpTable": symStatsUnconfiguredHitsCountOnSpTable,
       "symStatsUnconfiguredHitsCountOnSpTableEntry": symStatsUnconfiguredHitsCountOnSpTableEntry,
       "symStatsUnconfiguredHitsCountOnSpTblIndex": symStatsUnconfiguredHitsCountOnSpTblIndex,
       "symStatsUnconfiguredHitsCountOnSpTblSpIndex": symStatsUnconfiguredHitsCountOnSpTblSpIndex,
       "symStatsUnconfiguredHitsCountOnSpTblHitCount": symStatsUnconfiguredHitsCountOnSpTblHitCount,
       "agClearStats": agClearStats,
       "snmpClearStats": snmpClearStats,
       "mpMemStats": mpMemStats,
       "mpMemStatsTotal": mpMemStatsTotal,
       "mpMemStatsUsed": mpMemStatsUsed,
       "mpMemStatsFree": mpMemStatsFree,
       "mpMemStatsLowFree": mpMemStatsLowFree,
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
       "portMirrorStats": portMirrorStats,
       "portMirrorStatsTable": portMirrorStatsTable,
       "portMirrorStatsTableEntry": portMirrorStatsTableEntry,
       "portMirrorStatsIndx": portMirrorStatsIndx,
       "portMirrorStatsIngress": portMirrorStatsIngress,
       "portMirrorStatsEgress": portMirrorStatsEgress,
       "portMirrorClear": portMirrorClear,
       "portMirrorStatsClear": portMirrorStatsClear,
       "agentInfo": agentInfo,
       "hardware": hardware,
       "hwPartNumber": hwPartNumber,
       "hwRevision": hwRevision,
       "hwTemperatureStatus": hwTemperatureStatus,
       "hwFanStatus": hwFanStatus,
       "hwOrderNumber": hwOrderNumber,
       "hwMainBoardNumber": hwMainBoardNumber,
       "hwMainBoardRevision": hwMainBoardRevision,
       "hwEthernetBoardNumber": hwEthernetBoardNumber,
       "hwEthernetBoardRevision": hwEthernetBoardRevision,
       "hwChassisSerialNumber": hwChassisSerialNumber,
       "hwChassisRevision": hwChassisRevision,
       "hwPower": hwPower,
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
       "portInfoPhyConnType": portInfoPhyConnType,
       "portInfoPreferred": portInfoPreferred,
       "portInfoBackup": portInfoBackup,
       "portInfoSFPName": portInfoSFPName,
       "portInfoSFPType": portInfoSFPType,
       "swKeyInfo": swKeyInfo,
       "agEnabledSwFeatures": agEnabledSwFeatures,
       "agEnabledGslbKey": agEnabledGslbKey,
       "agEnabledBwmKey": agEnabledBwmKey,
       "agEnabledSecurityKey": agEnabledSecurityKey,
       "agEnabledLinklbKey": agEnabledLinklbKey,
       "agSymantecSwKeyInfo": agSymantecSwKeyInfo,
       "agSymantecSwKeyRemainingDays": agSymantecSwKeyRemainingDays,
       "agSymLicenseSwKeyRenewalPending": agSymLicenseSwKeyRenewalPending,
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
       "mgmtPortInfoSpeed": mgmtPortInfoSpeed,
       "mgmtPortInfoMode": mgmtPortInfoMode,
       "mgmtPortInfoLink": mgmtPortInfoLink,
       "securityInfo": securityInfo,
       "ipAclBogonInfo": ipAclBogonInfo,
       "ipAclBogonInfoTableMaxSize": ipAclBogonInfoTableMaxSize,
       "ipAclBogonInfoTable": ipAclBogonInfoTable,
       "ipAclBogonInfoTableEntry": ipAclBogonInfoTableEntry,
       "ipAclBogonInfoIndex": ipAclBogonInfoIndex,
       "ipAclBogonInfoIp": ipAclBogonInfoIp,
       "ipAclBogonInfoMask": ipAclBogonInfoMask,
       "symantecInfo": symantecInfo,
       "symIpsEngineVersion": symIpsEngineVersion,
       "symMatchInfoSpTable": symMatchInfoSpTable,
       "symMatchInfoSpTableEntry": symMatchInfoSpTableEntry,
       "symMatchInfoSpTableIndex": symMatchInfoSpTableIndex,
       "symMatchInfoSpClientIp": symMatchInfoSpClientIp,
       "symMatchInfoSpServerIp": symMatchInfoSpServerIp,
       "symMatchInfoSpClientPort": symMatchInfoSpClientPort,
       "symMatchInfoSpServerPort": symMatchInfoSpServerPort,
       "symMatchInfoSpProtocol": symMatchInfoSpProtocol,
       "symMatchInfoSpNumOfMatches": symMatchInfoSpNumOfMatches,
       "symMatchInfoSpSigActTable": symMatchInfoSpSigActTable,
       "symMatchInfoSpSigActTableEntry": symMatchInfoSpSigActTableEntry,
       "symMatchInfoSpSigActTblSpIndex": symMatchInfoSpSigActTblSpIndex,
       "symMatchInfoSpSigActTblIndex": symMatchInfoSpSigActTblIndex,
       "symMatchInfoSpSigActTblSigId": symMatchInfoSpSigActTblSigId,
       "symMatchInfoSpSigActTblAction": symMatchInfoSpSigActTblAction,
       "capacityInfo": capacityInfo,
       "switchCapL2Info": switchCapL2Info,
       "switchCapFDBMaxEnt": switchCapFDBMaxEnt,
       "switchCapFDBCurrEnt": switchCapFDBCurrEnt,
       "switchCapFDBPerSPMaxEnt": switchCapFDBPerSPMaxEnt,
       "switchCapVlanMaxEnt": switchCapVlanMaxEnt,
       "switchCapVlanCurrEnt": switchCapVlanCurrEnt,
       "switchCapStaticTrunkGrpsMaxEnt": switchCapStaticTrunkGrpsMaxEnt,
       "switchCapStaticTrunkGrpsCurrEnt": switchCapStaticTrunkGrpsCurrEnt,
       "switchCapLACPTrunkGRs": switchCapLACPTrunkGRs,
       "switchCapTrunksperTrunkGR": switchCapTrunksperTrunkGR,
       "switchCapSTGsMaxEnt": switchCapSTGsMaxEnt,
       "switchCapSTGsCurrEnt": switchCapSTGsCurrEnt,
       "switchCapPortTeamsMaxEnt": switchCapPortTeamsMaxEnt,
       "switchCapPortTeamsCurrEnt": switchCapPortTeamsCurrEnt,
       "switchCapMonitorPorts": switchCapMonitorPorts,
       "switchCapL3Info": switchCapL3Info,
       "switchCapIpIntfMaxEnt": switchCapIpIntfMaxEnt,
       "switchCapIpIntfCurrEnt": switchCapIpIntfCurrEnt,
       "switchCapIpGWMaxEnt": switchCapIpGWMaxEnt,
       "switchCapIpGWCurrEnt": switchCapIpGWCurrEnt,
       "switchCapIpRoutesMaxEnt": switchCapIpRoutesMaxEnt,
       "switchCapIpRoutesCurrEnt": switchCapIpRoutesCurrEnt,
       "switchCapIpStaticRoutesMaxEnt": switchCapIpStaticRoutesMaxEnt,
       "switchCapIpStaticRoutesCurrEnt": switchCapIpStaticRoutesCurrEnt,
       "switchCapIpARPMaxEnt": switchCapIpARPMaxEnt,
       "switchCapIpARPCurrEnt": switchCapIpARPCurrEnt,
       "switchCapIpStaticARPMaxEnt": switchCapIpStaticARPMaxEnt,
       "switchCapIpStaticARPCurrEnt": switchCapIpStaticARPCurrEnt,
       "switchCapLocNetsMaxEnt": switchCapLocNetsMaxEnt,
       "switchCapLocNetsCurrEnt": switchCapLocNetsCurrEnt,
       "switchCapDNSSerMaxEnt": switchCapDNSSerMaxEnt,
       "switchCapDNSSerCurrEnt": switchCapDNSSerCurrEnt,
       "switchCapBootpSerMaxEnt": switchCapBootpSerMaxEnt,
       "switchCapBootpSerCurrEnt": switchCapBootpSerCurrEnt,
       "switchCapRIPIntfMaxEnt": switchCapRIPIntfMaxEnt,
       "switchCapRIPIntfCurrEnt": switchCapRIPIntfCurrEnt,
       "switchCapOSPFIntfMaxEnt": switchCapOSPFIntfMaxEnt,
       "switchCapOSPFIntfCurrEnt": switchCapOSPFIntfCurrEnt,
       "switchCapOSPFAreasMaxEnt": switchCapOSPFAreasMaxEnt,
       "switchCapOSPFAreasCurrEnt": switchCapOSPFAreasCurrEnt,
       "switchCapOSPFSummaryRangesMaxEnt": switchCapOSPFSummaryRangesMaxEnt,
       "switchCapOSPFSummaryRangesCurrEnt": switchCapOSPFSummaryRangesCurrEnt,
       "switchCapOSPFVirtLinksMaxEnt": switchCapOSPFVirtLinksMaxEnt,
       "switchCapOSPFVirtLinksCurrEnt": switchCapOSPFVirtLinksCurrEnt,
       "switchCapOSPFHostsMaxEnt": switchCapOSPFHostsMaxEnt,
       "switchCapOSPFHostsCurrEnt": switchCapOSPFHostsCurrEnt,
       "switchCapLSDBLimit": switchCapLSDBLimit,
       "switchCapBGPPeersMaxEnt": switchCapBGPPeersMaxEnt,
       "switchCapBGPPeersCurrEnt": switchCapBGPPeersCurrEnt,
       "switchCapBGPRouteAggrsMaxEnt": switchCapBGPRouteAggrsMaxEnt,
       "switchCapBGPRouteAggrsCurrEnt": switchCapBGPRouteAggrsCurrEnt,
       "switchCapRouteMapsMaxEnt": switchCapRouteMapsMaxEnt,
       "switchCapRouteMapsCurrEnt": switchCapRouteMapsCurrEnt,
       "switchCapNwkFltsMaxEnt": switchCapNwkFltsMaxEnt,
       "switchCapNwkFltsCurrEnt": switchCapNwkFltsCurrEnt,
       "switchCapASFlts": switchCapASFlts,
       "switchCapVRRPRtrsMaxEnt": switchCapVRRPRtrsMaxEnt,
       "switchCapVRRPRtrsCurrEnt": switchCapVRRPRtrsCurrEnt,
       "switchCapVRRPRtrGRsMaxEnt": switchCapVRRPRtrGRsMaxEnt,
       "switchCapVRRPRtrGRsCurrEnt": switchCapVRRPRtrGRsCurrEnt,
       "switchCapVRRPIntfsMaxEnt": switchCapVRRPIntfsMaxEnt,
       "switchCapVRRPIntfsCurrEnt": switchCapVRRPIntfsCurrEnt,
       "switchCapSlbInfo": switchCapSlbInfo,
       "switchCapRealSersMaxEnt": switchCapRealSersMaxEnt,
       "switchCapRealSersCurrEnt": switchCapRealSersCurrEnt,
       "switchCapSerGRsMaxEnt": switchCapSerGRsMaxEnt,
       "switchCapSerGRsCurrEnt": switchCapSerGRsCurrEnt,
       "switchCapVirtSersMaxEnt": switchCapVirtSersMaxEnt,
       "switchCapVirtSersCurrEnt": switchCapVirtSersCurrEnt,
       "switchCapVirtServicesEnt": switchCapVirtServicesEnt,
       "switchCapRealServicesEnt": switchCapRealServicesEnt,
       "switchCapRealIDSSer": switchCapRealIDSSer,
       "switchCapIDSSerGRs": switchCapIDSSerGRs,
       "switchCapGSLBDomainsMaxEnt": switchCapGSLBDomainsMaxEnt,
       "switchCapGSLBDomainsCurrEnt": switchCapGSLBDomainsCurrEnt,
       "switchCapGSLBServicesMaxEnt": switchCapGSLBServicesMaxEnt,
       "switchCapGSLBServicesCurrEnt": switchCapGSLBServicesCurrEnt,
       "switchCapGSLBLocSersMaxEnt": switchCapGSLBLocSersMaxEnt,
       "switchCapGSLBLocSersCurrEnt": switchCapGSLBLocSersCurrEnt,
       "switchCapGSLBRemSersMaxEnt": switchCapGSLBRemSersMaxEnt,
       "switchCapGSLBRemSersCurrEnt": switchCapGSLBRemSersCurrEnt,
       "switchCapGSLBRemSitesMaxEnt": switchCapGSLBRemSitesMaxEnt,
       "switchCapGSLBRemSitesCurrEnt": switchCapGSLBRemSitesCurrEnt,
       "switchCapGSLBFailoversPerRemSiteMaxEnt": switchCapGSLBFailoversPerRemSiteMaxEnt,
       "switchCapGSLBFailoversPerRemSiteCurrEnt": switchCapGSLBFailoversPerRemSiteCurrEnt,
       "switchCapGSLBNetworksMaxEnt": switchCapGSLBNetworksMaxEnt,
       "switchCapGSLBNetworksCurrEnt": switchCapGSLBNetworksCurrEnt,
       "switchCapGSLBGeographicalRegionsMaxEnt": switchCapGSLBGeographicalRegionsMaxEnt,
       "switchCapGSLBGeographicalRegionsCurrEnt": switchCapGSLBGeographicalRegionsCurrEnt,
       "switchCapGSLBRulesMaxEnt": switchCapGSLBRulesMaxEnt,
       "switchCapGSLBRulesCurrEnt": switchCapGSLBRulesCurrEnt,
       "switchCapGSLBMetricsPerRuleMaxEnt": switchCapGSLBMetricsPerRuleMaxEnt,
       "switchCapGSLBMetricPerRuleCurrEnt": switchCapGSLBMetricPerRuleCurrEnt,
       "switchCapGSLBDNSPersCacheMaxEnt": switchCapGSLBDNSPersCacheMaxEnt,
       "switchCapGSLBDNSPersCacheCurrEnt": switchCapGSLBDNSPersCacheCurrEnt,
       "switchCapFltsMaxEnt": switchCapFltsMaxEnt,
       "switchCapFltsCurrEnt": switchCapFltsCurrEnt,
       "switchCapPIPsMaxEnt": switchCapPIPsMaxEnt,
       "switchCapPIPsCurrEnt": switchCapPIPsCurrEnt,
       "switchCapScriptHealthChecksMaxEnt": switchCapScriptHealthChecksMaxEnt,
       "switchCapScriptHealthChecksCurrEnt": switchCapScriptHealthChecksCurrEnt,
       "switchCapSNMPHealthChecksMaxEnt": switchCapSNMPHealthChecksMaxEnt,
       "switchCapSNMPHealthChecksCurrEnt": switchCapSNMPHealthChecksCurrEnt,
       "switchCapRulesforURLParsingMaxEnt": switchCapRulesforURLParsingMaxEnt,
       "switchCapRulesforURLParsingCurrEnt": switchCapRulesforURLParsingCurrEnt,
       "switchCapSLBSessionsMaxEnt": switchCapSLBSessionsMaxEnt,
       "switchCapSLBSessionsCurrEnt": switchCapSLBSessionsCurrEnt,
       "switchCapNumofRportstoVport": switchCapNumofRportstoVport,
       "switchCapDomianRecordsMaxEnt": switchCapDomianRecordsMaxEnt,
       "switchCapDomainRecordsCurrEnt": switchCapDomainRecordsCurrEnt,
       "switchCapMappingPerDomainrecord": switchCapMappingPerDomainrecord,
       "switchCapSlbPortInfo": switchCapSlbPortInfo,
       "switchCapSlbPortInfoTable": switchCapSlbPortInfoTable,
       "switchCapSlbPortInfoTableEntry": switchCapSlbPortInfoTableEntry,
       "switchCapSlbPortInfoIndx": switchCapSlbPortInfoIndx,
       "switchCapSlbPortClientState": switchCapSlbPortClientState,
       "switchCapSlbPortSerState": switchCapSlbPortSerState,
       "switchCapSlbPortFltState": switchCapSlbPortFltState,
       "switchCapSlbPortRTSState": switchCapSlbPortRTSState,
       "switchCapBwmInfo": switchCapBwmInfo,
       "bwmPoliciesMaxEnt": bwmPoliciesMaxEnt,
       "bwmPoliciesCurrEnt": bwmPoliciesCurrEnt,
       "bwmContsMaxEnt": bwmContsMaxEnt,
       "bwmContsCurrEnt": bwmContsCurrEnt,
       "bwmGRsMaxEnt": bwmGRsMaxEnt,
       "bwmGRsCurrEnt": bwmGRsCurrEnt,
       "bwmContsPerGRs": bwmContsPerGRs,
       "bwmTimePoliciesPerCont": bwmTimePoliciesPerCont,
       "switchCapSecInfo": switchCapSecInfo,
       "configSrcIPACLsMaxEnt": configSrcIPACLsMaxEnt,
       "configSrcIPACLsCurrEnt": configSrcIPACLsCurrEnt,
       "bogonSrcIPACLsMaxEnt": bogonSrcIPACLsMaxEnt,
       "bogonSrcIPACLsCurrEnt": bogonSrcIPACLsCurrEnt,
       "operSrcIPACLsMaxEnt": operSrcIPACLsMaxEnt,
       "operSrcIPACLsCurrEnt": operSrcIPACLsCurrEnt,
       "totalSrcIPACLsMaxEnt": totalSrcIPACLsMaxEnt,
       "totalSrcIPACLsCurrEnt": totalSrcIPACLsCurrEnt,
       "configDstIPACLsMaxEnt": configDstIPACLsMaxEnt,
       "configDstIPACLsCurrEnt": configDstIPACLsCurrEnt,
       "operDstIPACLsMaxEnt": operDstIPACLsMaxEnt,
       "operDstIPACLsCurrEnt": operDstIPACLsCurrEnt,
       "totalDstIPACLsMaxEnt": totalDstIPACLsMaxEnt,
       "totalDstIPACLsCurrEnt": totalDstIPACLsCurrEnt,
       "ipDosAtkPrevention": ipDosAtkPrevention,
       "tcpDosAtkPrevention": tcpDosAtkPrevention,
       "udpDosAtkPrevention": udpDosAtkPrevention,
       "icmpDosAtkPrevention": icmpDosAtkPrevention,
       "igmpDosAtkPrevention": igmpDosAtkPrevention,
       "arpDosAtkPrevention": arpDosAtkPrevention,
       "ipv6DosAtkPrevention": ipv6DosAtkPrevention,
       "totalDosAtkPrevention": totalDosAtkPrevention,
       "udpBlastProtection": udpBlastProtection,
       "switchCapGeneralInfo": switchCapGeneralInfo,
       "syslogHostMaxEnt": syslogHostMaxEnt,
       "syslogHostCurrEnt": syslogHostCurrEnt,
       "radiusSerMaxEnt": radiusSerMaxEnt,
       "radiusSerCurrEnt": radiusSerCurrEnt,
       "tacacsSerMaxEnt": tacacsSerMaxEnt,
       "tacacsSerCurrEnt": tacacsSerCurrEnt,
       "ntpSerMaxEnt": ntpSerMaxEnt,
       "ntpSerCurrEnt": ntpSerCurrEnt,
       "smtpHostsMaxEnt": smtpHostsMaxEnt,
       "smtpHostsCurrEnt": smtpHostsCurrEnt,
       "mgmtNetworksMaxEnt": mgmtNetworksMaxEnt,
       "mgmtNetworksCurrEnt": mgmtNetworksCurrEnt,
       "endUsers": endUsers,
       "panicDumps": panicDumps,
       "mpMemory": mpMemory,
       "spMemory": spMemory,
       "snmpv3UsersMaxEnt": snmpv3UsersMaxEnt,
       "snmpv3UsersCurrEnt": snmpv3UsersCurrEnt,
       "snmpv3ViewsMaxEnt": snmpv3ViewsMaxEnt,
       "snmpv3ViewsCurrEnt": snmpv3ViewsCurrEnt,
       "snmpv3AccessGRsMaxEnt": snmpv3AccessGRsMaxEnt,
       "snmpv3AccessGRsCurrEnt": snmpv3AccessGRsCurrEnt,
       "snmpv3TargetAddrMaxEnt": snmpv3TargetAddrMaxEnt,
       "snmpv3TargetAddrCurrEnt": snmpv3TargetAddrCurrEnt,
       "snmpv3TargetParamsMaxEnt": snmpv3TargetParamsMaxEnt,
       "snmpv3TargetParamsCurrEnt": snmpv3TargetParamsCurrEnt,
       "agentOper": agentOper,
       "agPortOperTable": agPortOperTable,
       "agPortOperTableEntry": agPortOperTableEntry,
       "portOperIdx": portOperIdx,
       "portOperState": portOperState,
       "portOperRmon": portOperRmon,
       "agNTPOper": agNTPOper,
       "ntpOperSendReq": ntpOperSendReq}
)
