# SNMP MIB module (ALTEON-TS-PHYSICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-TS-PHYSICAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:02 2024
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

(agent,
 information,
 operCmds,
 stats) = mibBuilder.importSymbols(
    "ALTEON-TIGON-SWITCH-MIB",
    "agent",
    "information",
    "operCmds",
    "stats")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

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
    (0, "ALTEON-TS-PHYSICAL-MIB", "agPortCurCfgIndx"),
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3))
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
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3),
          ("none", 4))
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 7),
    _AgPortCurCfgRmon_Type()
)
agPortCurCfgRmon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgRmon.setStatus("mandatory")


class _AgPortCurCfgPVID_Type(Integer32):
    """Custom type agPortCurCfgPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgPortCurCfgPVID_Type.__name__ = "Integer32"
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
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mbs10", 2),
          ("mbs100", 3),
          ("mbs10or100", 4))
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
        ValueSizeConstraint(0, 63),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 17),
    _AgPortCurCfgDiscardNonIPs_Type()
)
agPortCurCfgDiscardNonIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgDiscardNonIPs.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 2, 1, 18),
    _AgPortCurCfgLinkTrap_Type()
)
agPortCurCfgLinkTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortCurCfgLinkTrap.setStatus("mandatory")
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
    (0, "ALTEON-TS-PHYSICAL-MIB", "agPortNewCfgIndx"),
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3))
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
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet", 2),
          ("gigabit-ethernet", 3),
          ("none", 4))
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 7),
    _AgPortNewCfgRmon_Type()
)
agPortNewCfgRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgRmon.setStatus("mandatory")


class _AgPortNewCfgPVID_Type(Integer32):
    """Custom type agPortNewCfgPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgPortNewCfgPVID_Type.__name__ = "Integer32"
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
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mbs10", 2),
          ("mbs100", 3),
          ("mbs10or100", 4))
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
        ValueSizeConstraint(0, 63),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 17),
    _AgPortNewCfgDiscardNonIPs_Type()
)
agPortNewCfgDiscardNonIPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgDiscardNonIPs.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 2, 3, 3, 1, 18),
    _AgPortNewCfgLinkTrap_Type()
)
agPortNewCfgLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgLinkTrap.setStatus("mandatory")
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
    (0, "ALTEON-TS-PHYSICAL-MIB", "vlanCurCfgVlanId"),
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
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
_VlanCurCfgStg_Type = Integer32
_VlanCurCfgStg_Object = MibTableColumn
vlanCurCfgStg = _VlanCurCfgStg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 2, 1, 7),
    _VlanCurCfgStg_Type()
)
vlanCurCfgStg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgStg.setStatus("mandatory")
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
    (0, "ALTEON-TS-PHYSICAL-MIB", "vlanNewCfgVlanId"),
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
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
_VlanNewCfgStg_Type = Integer32
_VlanNewCfgStg_Object = MibTableColumn
vlanNewCfgStg = _VlanNewCfgStg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 4, 3, 1, 10),
    _VlanNewCfgStg_Type()
)
vlanNewCfgStg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgStg.setStatus("mandatory")
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
    pmCurCfgMonitoringPort.setStatus("obsolete")
_PmNewCfgMonitoringPort_Type = Integer32
_PmNewCfgMonitoringPort_Object = MibScalar
pmNewCfgMonitoringPort = _PmNewCfgMonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 2),
    _PmNewCfgMonitoringPort_Type()
)
pmNewCfgMonitoringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgMonitoringPort.setStatus("obsolete")
_PmCurCfgMirroredPort_Type = Integer32
_PmCurCfgMirroredPort_Object = MibScalar
pmCurCfgMirroredPort = _PmCurCfgMirroredPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 3),
    _PmCurCfgMirroredPort_Type()
)
pmCurCfgMirroredPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgMirroredPort.setStatus("obsolete")
_PmNewCfgMirroredPort_Type = Integer32
_PmNewCfgMirroredPort_Object = MibScalar
pmNewCfgMirroredPort = _PmNewCfgMirroredPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 4),
    _PmNewCfgMirroredPort_Type()
)
pmNewCfgMirroredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgMirroredPort.setStatus("obsolete")


class _PmCurCfgMonitoredTraffic_Type(Integer32):
    """Custom type pmCurCfgMonitoredTraffic based on Integer32"""
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
        *(("both", 5),
          ("none", 2),
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
    pmCurCfgMonitoredTraffic.setStatus("obsolete")


class _PmNewCfgMonitoredTraffic_Type(Integer32):
    """Custom type pmNewCfgMonitoredTraffic based on Integer32"""
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
        *(("both", 5),
          ("none", 2),
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
    pmNewCfgMonitoredTraffic.setStatus("obsolete")


class _PmCurCfgState_Type(Integer32):
    """Custom type pmCurCfgState based on Integer32"""
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


_PmCurCfgState_Type.__name__ = "Integer32"
_PmCurCfgState_Object = MibScalar
pmCurCfgState = _PmCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 7),
    _PmCurCfgState_Type()
)
pmCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgState.setStatus("obsolete")


class _PmNewCfgState_Type(Integer32):
    """Custom type pmNewCfgState based on Integer32"""
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


_PmNewCfgState_Type.__name__ = "Integer32"
_PmNewCfgState_Object = MibScalar
pmNewCfgState = _PmNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 8),
    _PmNewCfgState_Type()
)
pmNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgState.setStatus("obsolete")


class _PmCurCfgTimeout_Type(Integer32):
    """Custom type pmCurCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmCurCfgTimeout_Type.__name__ = "Integer32"
_PmCurCfgTimeout_Object = MibScalar
pmCurCfgTimeout = _PmCurCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 9),
    _PmCurCfgTimeout_Type()
)
pmCurCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgTimeout.setStatus("obsolete")


class _PmNewCfgTimeout_Type(Integer32):
    """Custom type pmNewCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmNewCfgTimeout_Type.__name__ = "Integer32"
_PmNewCfgTimeout_Object = MibScalar
pmNewCfgTimeout = _PmNewCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 6, 10),
    _PmNewCfgTimeout_Type()
)
pmNewCfgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgTimeout.setStatus("obsolete")
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
    (0, "ALTEON-TS-PHYSICAL-MIB", "trunkGroupCurCfgIndex"),
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
    (0, "ALTEON-TS-PHYSICAL-MIB", "trunkGroupNewCfgIndex"),
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
_PortCpuStats_ObjectIdentity = ObjectIdentity
portCpuStats = _PortCpuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17)
)
_PortCpuStatsUtilTable_Object = MibTable
portCpuStatsUtilTable = _PortCpuStatsUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1)
)
if mibBuilder.loadTexts:
    portCpuStatsUtilTable.setStatus("mandatory")
_PortCpuStatsUtilTableEntry_Object = MibTableRow
portCpuStatsUtilTableEntry = _PortCpuStatsUtilTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1)
)
portCpuStatsUtilTableEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "portCpuStatsUtilIndx"),
)
if mibBuilder.loadTexts:
    portCpuStatsUtilTableEntry.setStatus("mandatory")


class _PortCpuStatsUtilIndx_Type(Integer32):
    """Custom type portCpuStatsUtilIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortCpuStatsUtilIndx_Type.__name__ = "Integer32"
_PortCpuStatsUtilIndx_Object = MibTableColumn
portCpuStatsUtilIndx = _PortCpuStatsUtilIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1, 1),
    _PortCpuStatsUtilIndx_Type()
)
portCpuStatsUtilIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpuStatsUtilIndx.setStatus("mandatory")
_PortCpuAStatsUtil1Second_Type = Integer32
_PortCpuAStatsUtil1Second_Object = MibTableColumn
portCpuAStatsUtil1Second = _PortCpuAStatsUtil1Second_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1, 2),
    _PortCpuAStatsUtil1Second_Type()
)
portCpuAStatsUtil1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpuAStatsUtil1Second.setStatus("mandatory")
_PortCpuBStatsUtil1Second_Type = Integer32
_PortCpuBStatsUtil1Second_Object = MibTableColumn
portCpuBStatsUtil1Second = _PortCpuBStatsUtil1Second_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1, 3),
    _PortCpuBStatsUtil1Second_Type()
)
portCpuBStatsUtil1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpuBStatsUtil1Second.setStatus("mandatory")
_PortCpuAStatsUtil4Seconds_Type = Integer32
_PortCpuAStatsUtil4Seconds_Object = MibTableColumn
portCpuAStatsUtil4Seconds = _PortCpuAStatsUtil4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1, 4),
    _PortCpuAStatsUtil4Seconds_Type()
)
portCpuAStatsUtil4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpuAStatsUtil4Seconds.setStatus("mandatory")
_PortCpuBStatsUtil4Seconds_Type = Integer32
_PortCpuBStatsUtil4Seconds_Object = MibTableColumn
portCpuBStatsUtil4Seconds = _PortCpuBStatsUtil4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1, 5),
    _PortCpuBStatsUtil4Seconds_Type()
)
portCpuBStatsUtil4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpuBStatsUtil4Seconds.setStatus("mandatory")
_PortCpuAStatsUtil64Seconds_Type = Integer32
_PortCpuAStatsUtil64Seconds_Object = MibTableColumn
portCpuAStatsUtil64Seconds = _PortCpuAStatsUtil64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1, 6),
    _PortCpuAStatsUtil64Seconds_Type()
)
portCpuAStatsUtil64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpuAStatsUtil64Seconds.setStatus("mandatory")
_PortCpuBStatsUtil64Seconds_Type = Integer32
_PortCpuBStatsUtil64Seconds_Object = MibTableColumn
portCpuBStatsUtil64Seconds = _PortCpuBStatsUtil64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 17, 1, 1, 7),
    _PortCpuBStatsUtil64Seconds_Type()
)
portCpuBStatsUtil64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpuBStatsUtil64Seconds.setStatus("mandatory")
_Port_stats_ObjectIdentity = ObjectIdentity
port_stats = _Port_stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26)
)
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("mandatory")
_PortStatsTableEntry_Object = MibTableRow
portStatsTableEntry = _PortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1)
)
portStatsTableEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "portStatsIndx"),
)
if mibBuilder.loadTexts:
    portStatsTableEntry.setStatus("mandatory")


class _PortStatsIndx_Type(Integer32):
    """Custom type portStatsIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortStatsIndx_Type.__name__ = "Integer32"
_PortStatsIndx_Object = MibTableColumn
portStatsIndx = _PortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 1),
    _PortStatsIndx_Type()
)
portStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsIndx.setStatus("mandatory")
_PortStatsPhyIfInOctets_Type = Counter32
_PortStatsPhyIfInOctets_Object = MibTableColumn
portStatsPhyIfInOctets = _PortStatsPhyIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 2),
    _PortStatsPhyIfInOctets_Type()
)
portStatsPhyIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInOctets.setStatus("mandatory")
_PortStatsPhyIfInUcastPkts_Type = Counter32
_PortStatsPhyIfInUcastPkts_Object = MibTableColumn
portStatsPhyIfInUcastPkts = _PortStatsPhyIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 3),
    _PortStatsPhyIfInUcastPkts_Type()
)
portStatsPhyIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInUcastPkts.setStatus("mandatory")
_PortStatsPhyIfInNUcastPkts_Type = Counter32
_PortStatsPhyIfInNUcastPkts_Object = MibTableColumn
portStatsPhyIfInNUcastPkts = _PortStatsPhyIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 4),
    _PortStatsPhyIfInNUcastPkts_Type()
)
portStatsPhyIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInNUcastPkts.setStatus("mandatory")
_PortStatsPhyIfInDiscards_Type = Counter32
_PortStatsPhyIfInDiscards_Object = MibTableColumn
portStatsPhyIfInDiscards = _PortStatsPhyIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 5),
    _PortStatsPhyIfInDiscards_Type()
)
portStatsPhyIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInDiscards.setStatus("mandatory")
_PortStatsPhyIfInErrors_Type = Counter32
_PortStatsPhyIfInErrors_Object = MibTableColumn
portStatsPhyIfInErrors = _PortStatsPhyIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 6),
    _PortStatsPhyIfInErrors_Type()
)
portStatsPhyIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInErrors.setStatus("mandatory")
_PortStatsPhyIfInUnknownProtos_Type = Counter32
_PortStatsPhyIfInUnknownProtos_Object = MibTableColumn
portStatsPhyIfInUnknownProtos = _PortStatsPhyIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 7),
    _PortStatsPhyIfInUnknownProtos_Type()
)
portStatsPhyIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInUnknownProtos.setStatus("mandatory")
_PortStatsPhyIfOutOctets_Type = Counter32
_PortStatsPhyIfOutOctets_Object = MibTableColumn
portStatsPhyIfOutOctets = _PortStatsPhyIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 8),
    _PortStatsPhyIfOutOctets_Type()
)
portStatsPhyIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutOctets.setStatus("mandatory")
_PortStatsPhyIfOutUcastPkts_Type = Counter32
_PortStatsPhyIfOutUcastPkts_Object = MibTableColumn
portStatsPhyIfOutUcastPkts = _PortStatsPhyIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 9),
    _PortStatsPhyIfOutUcastPkts_Type()
)
portStatsPhyIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutUcastPkts.setStatus("mandatory")
_PortStatsPhyIfOutNUcastPkts_Type = Counter32
_PortStatsPhyIfOutNUcastPkts_Object = MibTableColumn
portStatsPhyIfOutNUcastPkts = _PortStatsPhyIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 10),
    _PortStatsPhyIfOutNUcastPkts_Type()
)
portStatsPhyIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutNUcastPkts.setStatus("mandatory")
_PortStatsPhyIfOutDiscards_Type = Counter32
_PortStatsPhyIfOutDiscards_Object = MibTableColumn
portStatsPhyIfOutDiscards = _PortStatsPhyIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 11),
    _PortStatsPhyIfOutDiscards_Type()
)
portStatsPhyIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutDiscards.setStatus("mandatory")
_PortStatsPhyIfOutErrors_Type = Counter32
_PortStatsPhyIfOutErrors_Object = MibTableColumn
portStatsPhyIfOutErrors = _PortStatsPhyIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 12),
    _PortStatsPhyIfOutErrors_Type()
)
portStatsPhyIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutErrors.setStatus("mandatory")
_PortStatsPhyIfOutQLen_Type = Gauge32
_PortStatsPhyIfOutQLen_Object = MibTableColumn
portStatsPhyIfOutQLen = _PortStatsPhyIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 13),
    _PortStatsPhyIfOutQLen_Type()
)
portStatsPhyIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutQLen.setStatus("mandatory")
_PortStatsPhyIfInBroadcastPkts_Type = Counter32
_PortStatsPhyIfInBroadcastPkts_Object = MibTableColumn
portStatsPhyIfInBroadcastPkts = _PortStatsPhyIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 14),
    _PortStatsPhyIfInBroadcastPkts_Type()
)
portStatsPhyIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfInBroadcastPkts.setStatus("mandatory")
_PortStatsPhyIfOutBroadcastPkts_Type = Counter32
_PortStatsPhyIfOutBroadcastPkts_Object = MibTableColumn
portStatsPhyIfOutBroadcastPkts = _PortStatsPhyIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 26, 1, 1, 15),
    _PortStatsPhyIfOutBroadcastPkts_Type()
)
portStatsPhyIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPhyIfOutBroadcastPkts.setStatus("mandatory")
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
    (0, "ALTEON-TS-PHYSICAL-MIB", "portInfoIndx"),
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


class _PortInfoPhyIfDescr_Type(DisplayString):
    """Custom type portInfoPhyIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortInfoPhyIfDescr_Type.__name__ = "DisplayString"
_PortInfoPhyIfDescr_Object = MibTableColumn
portInfoPhyIfDescr = _PortInfoPhyIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 6),
    _PortInfoPhyIfDescr_Type()
)
portInfoPhyIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfDescr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 7),
    _PortInfoPhyIfType_Type()
)
portInfoPhyIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfType.setStatus("mandatory")
_PortInfoPhyIfMtu_Type = Integer32
_PortInfoPhyIfMtu_Object = MibTableColumn
portInfoPhyIfMtu = _PortInfoPhyIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 8),
    _PortInfoPhyIfMtu_Type()
)
portInfoPhyIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfMtu.setStatus("mandatory")
_PortInfoPhyIfPhysAddress_Type = PhysAddress
_PortInfoPhyIfPhysAddress_Object = MibTableColumn
portInfoPhyIfPhysAddress = _PortInfoPhyIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 9),
    _PortInfoPhyIfPhysAddress_Type()
)
portInfoPhyIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfPhysAddress.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 10),
    _PortInfoPhyIfOperStatus_Type()
)
portInfoPhyIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfOperStatus.setStatus("mandatory")
_PortInfoPhyIfLastChange_Type = TimeTicks
_PortInfoPhyIfLastChange_Object = MibTableColumn
portInfoPhyIfLastChange = _PortInfoPhyIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 1, 1, 1, 11),
    _PortInfoPhyIfLastChange_Type()
)
portInfoPhyIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoPhyIfLastChange.setStatus("mandatory")
_MirrOper_ObjectIdentity = ObjectIdentity
mirrOper = _MirrOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 3)
)
_MirrOperMonitoringPort_Type = Integer32
_MirrOperMonitoringPort_Object = MibScalar
mirrOperMonitoringPort = _MirrOperMonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 3, 1),
    _MirrOperMonitoringPort_Type()
)
mirrOperMonitoringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrOperMonitoringPort.setStatus("mandatory")
_MirrOperMirroredPort_Type = Integer32
_MirrOperMirroredPort_Object = MibScalar
mirrOperMirroredPort = _MirrOperMirroredPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 3, 2),
    _MirrOperMirroredPort_Type()
)
mirrOperMirroredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrOperMirroredPort.setStatus("mandatory")


class _MirrOperType_Type(Integer32):
    """Custom type mirrOperType based on Integer32"""
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
        *(("both", 4),
          ("in", 2),
          ("none", 1),
          ("out", 3))
    )


_MirrOperType_Type.__name__ = "Integer32"
_MirrOperType_Object = MibScalar
mirrOperType = _MirrOperType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 3, 3),
    _MirrOperType_Type()
)
mirrOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrOperType.setStatus("mandatory")


class _MirrOperTimeout_Type(Integer32):
    """Custom type mirrOperTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_MirrOperTimeout_Type.__name__ = "Integer32"
_MirrOperTimeout_Object = MibScalar
mirrOperTimeout = _MirrOperTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 3, 4),
    _MirrOperTimeout_Type()
)
mirrOperTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrOperTimeout.setStatus("mandatory")


class _MirrOperState_Type(Integer32):
    """Custom type mirrOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MirrOperState_Type.__name__ = "Integer32"
_MirrOperState_Object = MibScalar
mirrOperState = _MirrOperState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 3, 5),
    _MirrOperState_Type()
)
mirrOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrOperState.setStatus("mandatory")
_Mirroring_ObjectIdentity = ObjectIdentity
mirroring = _Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18)
)
_MirrPortMirr_ObjectIdentity = ObjectIdentity
mirrPortMirr = _MirrPortMirr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1)
)


class _PmCurCfgPortMirrState_Type(Integer32):
    """Custom type pmCurCfgPortMirrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PmCurCfgPortMirrState_Type.__name__ = "Integer32"
_PmCurCfgPortMirrState_Object = MibScalar
pmCurCfgPortMirrState = _PmCurCfgPortMirrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 1),
    _PmCurCfgPortMirrState_Type()
)
pmCurCfgPortMirrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPortMirrState.setStatus("mandatory")


class _PmNewCfgPortMirrState_Type(Integer32):
    """Custom type pmNewCfgPortMirrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PmNewCfgPortMirrState_Type.__name__ = "Integer32"
_PmNewCfgPortMirrState_Object = MibScalar
pmNewCfgPortMirrState = _PmNewCfgPortMirrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 2),
    _PmNewCfgPortMirrState_Type()
)
pmNewCfgPortMirrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgPortMirrState.setStatus("mandatory")
_PmCurCfgPortMonitorTable_Object = MibTable
pmCurCfgPortMonitorTable = _PmCurCfgPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 3)
)
if mibBuilder.loadTexts:
    pmCurCfgPortMonitorTable.setStatus("mandatory")
_PmCurCfgPortMonitorEntry_Object = MibTableRow
pmCurCfgPortMonitorEntry = _PmCurCfgPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 3, 1)
)
pmCurCfgPortMonitorEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmCurCfgPmirrMoniPortIndex"),
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmCurCfgPmirrMirrPortIndex"),
)
if mibBuilder.loadTexts:
    pmCurCfgPortMonitorEntry.setStatus("mandatory")
_PmCurCfgPmirrMoniPortIndex_Type = Integer32
_PmCurCfgPmirrMoniPortIndex_Object = MibTableColumn
pmCurCfgPmirrMoniPortIndex = _PmCurCfgPmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 3, 1, 1),
    _PmCurCfgPmirrMoniPortIndex_Type()
)
pmCurCfgPmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrMoniPortIndex.setStatus("mandatory")
_PmCurCfgPmirrMirrPortIndex_Type = Integer32
_PmCurCfgPmirrMirrPortIndex_Object = MibTableColumn
pmCurCfgPmirrMirrPortIndex = _PmCurCfgPmirrMirrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 3, 1, 2),
    _PmCurCfgPmirrMirrPortIndex_Type()
)
pmCurCfgPmirrMirrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrMirrPortIndex.setStatus("mandatory")


class _PmCurCfgPmirrDirection_Type(Integer32):
    """Custom type pmCurCfgPmirrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("out", 2))
    )


_PmCurCfgPmirrDirection_Type.__name__ = "Integer32"
_PmCurCfgPmirrDirection_Object = MibTableColumn
pmCurCfgPmirrDirection = _PmCurCfgPmirrDirection_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 3, 1, 3),
    _PmCurCfgPmirrDirection_Type()
)
pmCurCfgPmirrDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrDirection.setStatus("mandatory")
_PmNewCfgPortMonitorTable_Object = MibTable
pmNewCfgPortMonitorTable = _PmNewCfgPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 4)
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorTable.setStatus("mandatory")
_PmNewCfgPortMonitorEntry_Object = MibTableRow
pmNewCfgPortMonitorEntry = _PmNewCfgPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 4, 1)
)
pmNewCfgPortMonitorEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmNewCfgPmirrMoniPortIndex"),
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmNewCfgPmirrMirrPortIndex"),
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorEntry.setStatus("mandatory")
_PmNewCfgPmirrMoniPortIndex_Type = Integer32
_PmNewCfgPmirrMoniPortIndex_Object = MibTableColumn
pmNewCfgPmirrMoniPortIndex = _PmNewCfgPmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 4, 1, 1),
    _PmNewCfgPmirrMoniPortIndex_Type()
)
pmNewCfgPmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgPmirrMoniPortIndex.setStatus("mandatory")
_PmNewCfgPmirrMirrPortIndex_Type = Integer32
_PmNewCfgPmirrMirrPortIndex_Object = MibTableColumn
pmNewCfgPmirrMirrPortIndex = _PmNewCfgPmirrMirrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 4, 1, 2),
    _PmNewCfgPmirrMirrPortIndex_Type()
)
pmNewCfgPmirrMirrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgPmirrMirrPortIndex.setStatus("mandatory")


class _PmNewCfgPmirrDirection_Type(Integer32):
    """Custom type pmNewCfgPmirrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("out", 2))
    )


_PmNewCfgPmirrDirection_Type.__name__ = "Integer32"
_PmNewCfgPmirrDirection_Object = MibTableColumn
pmNewCfgPmirrDirection = _PmNewCfgPmirrDirection_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 4, 1, 3),
    _PmNewCfgPmirrDirection_Type()
)
pmNewCfgPmirrDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgPmirrDirection.setStatus("mandatory")


class _PmNewCfgPmirrDelete_Type(Integer32):
    """Custom type pmNewCfgPmirrDelete based on Integer32"""
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


_PmNewCfgPmirrDelete_Type.__name__ = "Integer32"
_PmNewCfgPmirrDelete_Object = MibTableColumn
pmNewCfgPmirrDelete = _PmNewCfgPmirrDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 1, 4, 1, 4),
    _PmNewCfgPmirrDelete_Type()
)
pmNewCfgPmirrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgPmirrDelete.setStatus("mandatory")
_MirrVlanMirr_ObjectIdentity = ObjectIdentity
mirrVlanMirr = _MirrVlanMirr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2)
)


class _PmCurCfgVlanMirrState_Type(Integer32):
    """Custom type pmCurCfgVlanMirrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PmCurCfgVlanMirrState_Type.__name__ = "Integer32"
_PmCurCfgVlanMirrState_Object = MibScalar
pmCurCfgVlanMirrState = _PmCurCfgVlanMirrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 1),
    _PmCurCfgVlanMirrState_Type()
)
pmCurCfgVlanMirrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgVlanMirrState.setStatus("mandatory")


class _PmNewCfgVlanMirrState_Type(Integer32):
    """Custom type pmNewCfgVlanMirrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PmNewCfgVlanMirrState_Type.__name__ = "Integer32"
_PmNewCfgVlanMirrState_Object = MibScalar
pmNewCfgVlanMirrState = _PmNewCfgVlanMirrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 2),
    _PmNewCfgVlanMirrState_Type()
)
pmNewCfgVlanMirrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgVlanMirrState.setStatus("mandatory")
_PmCurCfgVlanMonitorTable_Object = MibTable
pmCurCfgVlanMonitorTable = _PmCurCfgVlanMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 3)
)
if mibBuilder.loadTexts:
    pmCurCfgVlanMonitorTable.setStatus("mandatory")
_PmCurCfgVlanMonitorEntry_Object = MibTableRow
pmCurCfgVlanMonitorEntry = _PmCurCfgVlanMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 3, 1)
)
pmCurCfgVlanMonitorEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmCurCfgVmirrMoniPortIndex"),
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmCurCfgVmirrMirrVlanIndex"),
)
if mibBuilder.loadTexts:
    pmCurCfgVlanMonitorEntry.setStatus("mandatory")
_PmCurCfgVmirrMoniPortIndex_Type = Integer32
_PmCurCfgVmirrMoniPortIndex_Object = MibTableColumn
pmCurCfgVmirrMoniPortIndex = _PmCurCfgVmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 3, 1, 1),
    _PmCurCfgVmirrMoniPortIndex_Type()
)
pmCurCfgVmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgVmirrMoniPortIndex.setStatus("mandatory")
_PmCurCfgVmirrMirrVlanIndex_Type = Integer32
_PmCurCfgVmirrMirrVlanIndex_Object = MibTableColumn
pmCurCfgVmirrMirrVlanIndex = _PmCurCfgVmirrMirrVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 3, 1, 2),
    _PmCurCfgVmirrMirrVlanIndex_Type()
)
pmCurCfgVmirrMirrVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgVmirrMirrVlanIndex.setStatus("mandatory")


class _PmCurCfgVmirrDirection_Type(Integer32):
    """Custom type pmCurCfgVmirrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("out", 2))
    )


_PmCurCfgVmirrDirection_Type.__name__ = "Integer32"
_PmCurCfgVmirrDirection_Object = MibTableColumn
pmCurCfgVmirrDirection = _PmCurCfgVmirrDirection_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 3, 1, 3),
    _PmCurCfgVmirrDirection_Type()
)
pmCurCfgVmirrDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgVmirrDirection.setStatus("mandatory")
_PmNewCfgVlanMonitorTable_Object = MibTable
pmNewCfgVlanMonitorTable = _PmNewCfgVlanMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 4)
)
if mibBuilder.loadTexts:
    pmNewCfgVlanMonitorTable.setStatus("mandatory")
_PmNewCfgVlanMonitorEntry_Object = MibTableRow
pmNewCfgVlanMonitorEntry = _PmNewCfgVlanMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 4, 1)
)
pmNewCfgVlanMonitorEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmNewCfgVmirrMoniPortIndex"),
    (0, "ALTEON-TS-PHYSICAL-MIB", "pmNewCfgVmirrMirrVlanIndex"),
)
if mibBuilder.loadTexts:
    pmNewCfgVlanMonitorEntry.setStatus("mandatory")
_PmNewCfgVmirrMoniPortIndex_Type = Integer32
_PmNewCfgVmirrMoniPortIndex_Object = MibTableColumn
pmNewCfgVmirrMoniPortIndex = _PmNewCfgVmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 4, 1, 1),
    _PmNewCfgVmirrMoniPortIndex_Type()
)
pmNewCfgVmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgVmirrMoniPortIndex.setStatus("mandatory")
_PmNewCfgVmirrMirrVlanIndex_Type = Integer32
_PmNewCfgVmirrMirrVlanIndex_Object = MibTableColumn
pmNewCfgVmirrMirrVlanIndex = _PmNewCfgVmirrMirrVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 4, 1, 2),
    _PmNewCfgVmirrMirrVlanIndex_Type()
)
pmNewCfgVmirrMirrVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgVmirrMirrVlanIndex.setStatus("mandatory")


class _PmNewCfgVmirrDirection_Type(Integer32):
    """Custom type pmNewCfgVmirrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("out", 2))
    )


_PmNewCfgVmirrDirection_Type.__name__ = "Integer32"
_PmNewCfgVmirrDirection_Object = MibTableColumn
pmNewCfgVmirrDirection = _PmNewCfgVmirrDirection_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 4, 1, 3),
    _PmNewCfgVmirrDirection_Type()
)
pmNewCfgVmirrDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgVmirrDirection.setStatus("mandatory")


class _PmNewCfgVmirrDelete_Type(Integer32):
    """Custom type pmNewCfgVmirrDelete based on Integer32"""
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


_PmNewCfgVmirrDelete_Type.__name__ = "Integer32"
_PmNewCfgVmirrDelete_Object = MibTableColumn
pmNewCfgVmirrDelete = _PmNewCfgVmirrDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 18, 2, 4, 1, 4),
    _PmNewCfgVmirrDelete_Type()
)
pmNewCfgVmirrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgVmirrDelete.setStatus("mandatory")
_SpannTreeGrpCfg_ObjectIdentity = ObjectIdentity
spannTreeGrpCfg = _SpannTreeGrpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19)
)
_StgCurCfgTable_Object = MibTable
stgCurCfgTable = _StgCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 1)
)
if mibBuilder.loadTexts:
    stgCurCfgTable.setStatus("mandatory")
_StgCurCfgTableEntry_Object = MibTableRow
stgCurCfgTableEntry = _StgCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 1, 1)
)
stgCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "stgCurCfgIndex"),
)
if mibBuilder.loadTexts:
    stgCurCfgTableEntry.setStatus("mandatory")


class _StgCurCfgIndex_Type(Integer32):
    """Custom type stgCurCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_StgCurCfgIndex_Type.__name__ = "Integer32"
_StgCurCfgIndex_Object = MibTableColumn
stgCurCfgIndex = _StgCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 1, 1, 1),
    _StgCurCfgIndex_Type()
)
stgCurCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgIndex.setStatus("mandatory")


class _StgCurCfgState_Type(Integer32):
    """Custom type stgCurCfgState based on Integer32"""
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


_StgCurCfgState_Type.__name__ = "Integer32"
_StgCurCfgState_Object = MibTableColumn
stgCurCfgState = _StgCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 1, 1, 2),
    _StgCurCfgState_Type()
)
stgCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgState.setStatus("mandatory")


class _StgCurCfgVlanBmap1_Type(OctetString):
    """Custom type stgCurCfgVlanBmap1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgCurCfgVlanBmap1_Type.__name__ = "OctetString"
_StgCurCfgVlanBmap1_Object = MibTableColumn
stgCurCfgVlanBmap1 = _StgCurCfgVlanBmap1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 1, 1, 3),
    _StgCurCfgVlanBmap1_Type()
)
stgCurCfgVlanBmap1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgVlanBmap1.setStatus("mandatory")


class _StgCurCfgVlanBmap2_Type(OctetString):
    """Custom type stgCurCfgVlanBmap2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgCurCfgVlanBmap2_Type.__name__ = "OctetString"
_StgCurCfgVlanBmap2_Object = MibTableColumn
stgCurCfgVlanBmap2 = _StgCurCfgVlanBmap2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 1, 1, 4),
    _StgCurCfgVlanBmap2_Type()
)
stgCurCfgVlanBmap2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgVlanBmap2.setStatus("mandatory")
_StgNewCfgTable_Object = MibTable
stgNewCfgTable = _StgNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2)
)
if mibBuilder.loadTexts:
    stgNewCfgTable.setStatus("mandatory")
_StgNewCfgTableEntry_Object = MibTableRow
stgNewCfgTableEntry = _StgNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1)
)
stgNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "stgNewCfgIndex"),
)
if mibBuilder.loadTexts:
    stgNewCfgTableEntry.setStatus("mandatory")


class _StgNewCfgIndex_Type(Integer32):
    """Custom type stgNewCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_StgNewCfgIndex_Type.__name__ = "Integer32"
_StgNewCfgIndex_Object = MibTableColumn
stgNewCfgIndex = _StgNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1, 1),
    _StgNewCfgIndex_Type()
)
stgNewCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgIndex.setStatus("mandatory")


class _StgNewCfgState_Type(Integer32):
    """Custom type stgNewCfgState based on Integer32"""
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


_StgNewCfgState_Type.__name__ = "Integer32"
_StgNewCfgState_Object = MibTableColumn
stgNewCfgState = _StgNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1, 2),
    _StgNewCfgState_Type()
)
stgNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgState.setStatus("mandatory")


class _StgNewCfgDefaultCfg_Type(Integer32):
    """Custom type stgNewCfgDefaultCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("default-config", 1)
    )


_StgNewCfgDefaultCfg_Type.__name__ = "Integer32"
_StgNewCfgDefaultCfg_Object = MibTableColumn
stgNewCfgDefaultCfg = _StgNewCfgDefaultCfg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1, 3),
    _StgNewCfgDefaultCfg_Type()
)
stgNewCfgDefaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgDefaultCfg.setStatus("mandatory")
_StgNewCfgAddVlan_Type = Integer32
_StgNewCfgAddVlan_Object = MibTableColumn
stgNewCfgAddVlan = _StgNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1, 4),
    _StgNewCfgAddVlan_Type()
)
stgNewCfgAddVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgAddVlan.setStatus("mandatory")
_StgNewCfgRemoveVlan_Type = Integer32
_StgNewCfgRemoveVlan_Object = MibTableColumn
stgNewCfgRemoveVlan = _StgNewCfgRemoveVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1, 5),
    _StgNewCfgRemoveVlan_Type()
)
stgNewCfgRemoveVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgRemoveVlan.setStatus("mandatory")


class _StgNewCfgVlanBmap1_Type(OctetString):
    """Custom type stgNewCfgVlanBmap1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgNewCfgVlanBmap1_Type.__name__ = "OctetString"
_StgNewCfgVlanBmap1_Object = MibTableColumn
stgNewCfgVlanBmap1 = _StgNewCfgVlanBmap1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1, 6),
    _StgNewCfgVlanBmap1_Type()
)
stgNewCfgVlanBmap1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgVlanBmap1.setStatus("mandatory")


class _StgNewCfgVlanBmap2_Type(OctetString):
    """Custom type stgNewCfgVlanBmap2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgNewCfgVlanBmap2_Type.__name__ = "OctetString"
_StgNewCfgVlanBmap2_Object = MibTableColumn
stgNewCfgVlanBmap2 = _StgNewCfgVlanBmap2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 2, 1, 7),
    _StgNewCfgVlanBmap2_Type()
)
stgNewCfgVlanBmap2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgVlanBmap2.setStatus("mandatory")
_StgCurCfgPortTable_Object = MibTable
stgCurCfgPortTable = _StgCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 3)
)
if mibBuilder.loadTexts:
    stgCurCfgPortTable.setStatus("mandatory")
_StgCurCfgPortTableEntry_Object = MibTableRow
stgCurCfgPortTableEntry = _StgCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 3, 1)
)
stgCurCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "stgCurCfgStgIndex"),
    (0, "ALTEON-TS-PHYSICAL-MIB", "stgCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    stgCurCfgPortTableEntry.setStatus("mandatory")
_StgCurCfgStgIndex_Type = Integer32
_StgCurCfgStgIndex_Object = MibTableColumn
stgCurCfgStgIndex = _StgCurCfgStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 3, 1, 1),
    _StgCurCfgStgIndex_Type()
)
stgCurCfgStgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgStgIndex.setStatus("mandatory")
_StgCurCfgPortIndex_Type = Integer32
_StgCurCfgPortIndex_Object = MibTableColumn
stgCurCfgPortIndex = _StgCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 3, 1, 2),
    _StgCurCfgPortIndex_Type()
)
stgCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortIndex.setStatus("mandatory")


class _StgCurCfgPortState_Type(Integer32):
    """Custom type stgCurCfgPortState based on Integer32"""
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


_StgCurCfgPortState_Type.__name__ = "Integer32"
_StgCurCfgPortState_Object = MibTableColumn
stgCurCfgPortState = _StgCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 3, 1, 3),
    _StgCurCfgPortState_Type()
)
stgCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortState.setStatus("mandatory")
_StgNewCfgPortTable_Object = MibTable
stgNewCfgPortTable = _StgNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 4)
)
if mibBuilder.loadTexts:
    stgNewCfgPortTable.setStatus("mandatory")
_StgNewCfgPortTableEntry_Object = MibTableRow
stgNewCfgPortTableEntry = _StgNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 4, 1)
)
stgNewCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-TS-PHYSICAL-MIB", "stgNewCfgStgIndex"),
    (0, "ALTEON-TS-PHYSICAL-MIB", "stgNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    stgNewCfgPortTableEntry.setStatus("mandatory")
_StgNewCfgStgIndex_Type = Integer32
_StgNewCfgStgIndex_Object = MibTableColumn
stgNewCfgStgIndex = _StgNewCfgStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 4, 1, 1),
    _StgNewCfgStgIndex_Type()
)
stgNewCfgStgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgStgIndex.setStatus("mandatory")
_StgNewCfgPortIndex_Type = Integer32
_StgNewCfgPortIndex_Object = MibTableColumn
stgNewCfgPortIndex = _StgNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 4, 1, 2),
    _StgNewCfgPortIndex_Type()
)
stgNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgPortIndex.setStatus("mandatory")


class _StgNewCfgPortState_Type(Integer32):
    """Custom type stgNewCfgPortState based on Integer32"""
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


_StgNewCfgPortState_Type.__name__ = "Integer32"
_StgNewCfgPortState_Object = MibTableColumn
stgNewCfgPortState = _StgNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 19, 4, 1, 3),
    _StgNewCfgPortState_Type()
)
stgNewCfgPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgPortState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-TS-PHYSICAL-MIB",
    **{"agPortConfig": agPortConfig,
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
       "agPortCurCfgLinkTrap": agPortCurCfgLinkTrap,
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
       "agPortNewCfgLinkTrap": agPortNewCfgLinkTrap,
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
       "vlanCurCfgStg": vlanCurCfgStg,
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
       "vlanNewCfgStg": vlanNewCfgStg,
       "portmirroring": portmirroring,
       "pmCurCfgMonitoringPort": pmCurCfgMonitoringPort,
       "pmNewCfgMonitoringPort": pmNewCfgMonitoringPort,
       "pmCurCfgMirroredPort": pmCurCfgMirroredPort,
       "pmNewCfgMirroredPort": pmNewCfgMirroredPort,
       "pmCurCfgMonitoredTraffic": pmCurCfgMonitoredTraffic,
       "pmNewCfgMonitoredTraffic": pmNewCfgMonitoredTraffic,
       "pmCurCfgState": pmCurCfgState,
       "pmNewCfgState": pmNewCfgState,
       "pmCurCfgTimeout": pmCurCfgTimeout,
       "pmNewCfgTimeout": pmNewCfgTimeout,
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
       "portCpuStats": portCpuStats,
       "portCpuStatsUtilTable": portCpuStatsUtilTable,
       "portCpuStatsUtilTableEntry": portCpuStatsUtilTableEntry,
       "portCpuStatsUtilIndx": portCpuStatsUtilIndx,
       "portCpuAStatsUtil1Second": portCpuAStatsUtil1Second,
       "portCpuBStatsUtil1Second": portCpuBStatsUtil1Second,
       "portCpuAStatsUtil4Seconds": portCpuAStatsUtil4Seconds,
       "portCpuBStatsUtil4Seconds": portCpuBStatsUtil4Seconds,
       "portCpuAStatsUtil64Seconds": portCpuAStatsUtil64Seconds,
       "portCpuBStatsUtil64Seconds": portCpuBStatsUtil64Seconds,
       "port-stats": port_stats,
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
       "port-info": port_info,
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
       "mirrOper": mirrOper,
       "mirrOperMonitoringPort": mirrOperMonitoringPort,
       "mirrOperMirroredPort": mirrOperMirroredPort,
       "mirrOperType": mirrOperType,
       "mirrOperTimeout": mirrOperTimeout,
       "mirrOperState": mirrOperState,
       "mirroring": mirroring,
       "mirrPortMirr": mirrPortMirr,
       "pmCurCfgPortMirrState": pmCurCfgPortMirrState,
       "pmNewCfgPortMirrState": pmNewCfgPortMirrState,
       "pmCurCfgPortMonitorTable": pmCurCfgPortMonitorTable,
       "pmCurCfgPortMonitorEntry": pmCurCfgPortMonitorEntry,
       "pmCurCfgPmirrMoniPortIndex": pmCurCfgPmirrMoniPortIndex,
       "pmCurCfgPmirrMirrPortIndex": pmCurCfgPmirrMirrPortIndex,
       "pmCurCfgPmirrDirection": pmCurCfgPmirrDirection,
       "pmNewCfgPortMonitorTable": pmNewCfgPortMonitorTable,
       "pmNewCfgPortMonitorEntry": pmNewCfgPortMonitorEntry,
       "pmNewCfgPmirrMoniPortIndex": pmNewCfgPmirrMoniPortIndex,
       "pmNewCfgPmirrMirrPortIndex": pmNewCfgPmirrMirrPortIndex,
       "pmNewCfgPmirrDirection": pmNewCfgPmirrDirection,
       "pmNewCfgPmirrDelete": pmNewCfgPmirrDelete,
       "mirrVlanMirr": mirrVlanMirr,
       "pmCurCfgVlanMirrState": pmCurCfgVlanMirrState,
       "pmNewCfgVlanMirrState": pmNewCfgVlanMirrState,
       "pmCurCfgVlanMonitorTable": pmCurCfgVlanMonitorTable,
       "pmCurCfgVlanMonitorEntry": pmCurCfgVlanMonitorEntry,
       "pmCurCfgVmirrMoniPortIndex": pmCurCfgVmirrMoniPortIndex,
       "pmCurCfgVmirrMirrVlanIndex": pmCurCfgVmirrMirrVlanIndex,
       "pmCurCfgVmirrDirection": pmCurCfgVmirrDirection,
       "pmNewCfgVlanMonitorTable": pmNewCfgVlanMonitorTable,
       "pmNewCfgVlanMonitorEntry": pmNewCfgVlanMonitorEntry,
       "pmNewCfgVmirrMoniPortIndex": pmNewCfgVmirrMoniPortIndex,
       "pmNewCfgVmirrMirrVlanIndex": pmNewCfgVmirrMirrVlanIndex,
       "pmNewCfgVmirrDirection": pmNewCfgVmirrDirection,
       "pmNewCfgVmirrDelete": pmNewCfgVmirrDelete,
       "spannTreeGrpCfg": spannTreeGrpCfg,
       "stgCurCfgTable": stgCurCfgTable,
       "stgCurCfgTableEntry": stgCurCfgTableEntry,
       "stgCurCfgIndex": stgCurCfgIndex,
       "stgCurCfgState": stgCurCfgState,
       "stgCurCfgVlanBmap1": stgCurCfgVlanBmap1,
       "stgCurCfgVlanBmap2": stgCurCfgVlanBmap2,
       "stgNewCfgTable": stgNewCfgTable,
       "stgNewCfgTableEntry": stgNewCfgTableEntry,
       "stgNewCfgIndex": stgNewCfgIndex,
       "stgNewCfgState": stgNewCfgState,
       "stgNewCfgDefaultCfg": stgNewCfgDefaultCfg,
       "stgNewCfgAddVlan": stgNewCfgAddVlan,
       "stgNewCfgRemoveVlan": stgNewCfgRemoveVlan,
       "stgNewCfgVlanBmap1": stgNewCfgVlanBmap1,
       "stgNewCfgVlanBmap2": stgNewCfgVlanBmap2,
       "stgCurCfgPortTable": stgCurCfgPortTable,
       "stgCurCfgPortTableEntry": stgCurCfgPortTableEntry,
       "stgCurCfgStgIndex": stgCurCfgStgIndex,
       "stgCurCfgPortIndex": stgCurCfgPortIndex,
       "stgCurCfgPortState": stgCurCfgPortState,
       "stgNewCfgPortTable": stgNewCfgPortTable,
       "stgNewCfgPortTableEntry": stgNewCfgPortTableEntry,
       "stgNewCfgStgIndex": stgNewCfgStgIndex,
       "stgNewCfgPortIndex": stgNewCfgPortIndex,
       "stgNewCfgPortState": stgNewCfgPortState}
)
