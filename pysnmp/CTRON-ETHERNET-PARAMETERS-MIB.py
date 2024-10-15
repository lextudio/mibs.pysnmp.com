# SNMP MIB module (CTRON-ETHERNET-PARAMETERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ETHERNET-PARAMETERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:50 2024
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

(ctIfPortIfNumber,
 ctIfPortPortNumber) = mibBuilder.importSymbols(
    "CTIF-EXT-MIB",
    "ctIfPortIfNumber",
    "ctIfPortPortNumber")

(ctEthernetCtlParameters,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctEthernetCtlParameters")

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

_CtAutoNegCtl_ObjectIdentity = ObjectIdentity
ctAutoNegCtl = _CtAutoNegCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1)
)
_CtAutoNegCtlTable_Object = MibTable
ctAutoNegCtlTable = _CtAutoNegCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ctAutoNegCtlTable.setStatus("mandatory")
_CtAutoNegCtlEntry_Object = MibTableRow
ctAutoNegCtlEntry = _CtAutoNegCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1)
)
ctAutoNegCtlEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctIfPortIfNumber"),
    (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"),
)
if mibBuilder.loadTexts:
    ctAutoNegCtlEntry.setStatus("mandatory")


class _CtAutoNegAdminStatus_Type(Integer32):
    """Custom type ctAutoNegAdminStatus based on Integer32"""
    defaultValue = 1

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


_CtAutoNegAdminStatus_Type.__name__ = "Integer32"
_CtAutoNegAdminStatus_Object = MibTableColumn
ctAutoNegAdminStatus = _CtAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 1),
    _CtAutoNegAdminStatus_Type()
)
ctAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAutoNegAdminStatus.setStatus("mandatory")


class _CtAutoNegRemoteSignalling_Type(Integer32):
    """Custom type ctAutoNegRemoteSignalling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notdetected", 2))
    )


_CtAutoNegRemoteSignalling_Type.__name__ = "Integer32"
_CtAutoNegRemoteSignalling_Object = MibTableColumn
ctAutoNegRemoteSignalling = _CtAutoNegRemoteSignalling_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 2),
    _CtAutoNegRemoteSignalling_Type()
)
ctAutoNegRemoteSignalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAutoNegRemoteSignalling.setStatus("mandatory")


class _CtAutoNegAutoConfig_Type(Integer32):
    """Custom type ctAutoNegAutoConfig based on Integer32"""
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
        *(("complete", 3),
          ("configuring", 2),
          ("disabled", 4),
          ("other", 1),
          ("paralleldetectfailed", 5))
    )


_CtAutoNegAutoConfig_Type.__name__ = "Integer32"
_CtAutoNegAutoConfig_Object = MibTableColumn
ctAutoNegAutoConfig = _CtAutoNegAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 3),
    _CtAutoNegAutoConfig_Type()
)
ctAutoNegAutoConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAutoNegAutoConfig.setStatus("mandatory")
_CtAutoNegLocalTechnologyAbility_Type = Integer32
_CtAutoNegLocalTechnologyAbility_Object = MibTableColumn
ctAutoNegLocalTechnologyAbility = _CtAutoNegLocalTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 4),
    _CtAutoNegLocalTechnologyAbility_Type()
)
ctAutoNegLocalTechnologyAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAutoNegLocalTechnologyAbility.setStatus("mandatory")
_CtAutoNegAdvertisedTechnologyAbility_Type = Integer32
_CtAutoNegAdvertisedTechnologyAbility_Object = MibTableColumn
ctAutoNegAdvertisedTechnologyAbility = _CtAutoNegAdvertisedTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 5),
    _CtAutoNegAdvertisedTechnologyAbility_Type()
)
ctAutoNegAdvertisedTechnologyAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAutoNegAdvertisedTechnologyAbility.setStatus("mandatory")
_CtAutoNegReceivedTechnologyAbility_Type = Integer32
_CtAutoNegReceivedTechnologyAbility_Object = MibTableColumn
ctAutoNegReceivedTechnologyAbility = _CtAutoNegReceivedTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 6),
    _CtAutoNegReceivedTechnologyAbility_Type()
)
ctAutoNegReceivedTechnologyAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAutoNegReceivedTechnologyAbility.setStatus("mandatory")
_CtFlowControl_ObjectIdentity = ObjectIdentity
ctFlowControl = _CtFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2)
)
_CtFlowCtlTable_Object = MibTable
ctFlowCtlTable = _CtFlowCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctFlowCtlTable.setStatus("mandatory")
_CtFlowCtlEntry_Object = MibTableRow
ctFlowCtlEntry = _CtFlowCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1)
)
ctFlowCtlEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctIfPortIfNumber"),
    (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"),
)
if mibBuilder.loadTexts:
    ctFlowCtlEntry.setStatus("mandatory")


class _CtFlowCtlHalfDuplexAdminStatus_Type(Integer32):
    """Custom type ctFlowCtlHalfDuplexAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtFlowCtlHalfDuplexAdminStatus_Type.__name__ = "Integer32"
_CtFlowCtlHalfDuplexAdminStatus_Object = MibTableColumn
ctFlowCtlHalfDuplexAdminStatus = _CtFlowCtlHalfDuplexAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 1),
    _CtFlowCtlHalfDuplexAdminStatus_Type()
)
ctFlowCtlHalfDuplexAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFlowCtlHalfDuplexAdminStatus.setStatus("mandatory")


class _CtFlowCtlHalfDuplexOperStatus_Type(Integer32):
    """Custom type ctFlowCtlHalfDuplexOperStatus based on Integer32"""
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
          ("notsupported", 3))
    )


_CtFlowCtlHalfDuplexOperStatus_Type.__name__ = "Integer32"
_CtFlowCtlHalfDuplexOperStatus_Object = MibTableColumn
ctFlowCtlHalfDuplexOperStatus = _CtFlowCtlHalfDuplexOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 2),
    _CtFlowCtlHalfDuplexOperStatus_Type()
)
ctFlowCtlHalfDuplexOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFlowCtlHalfDuplexOperStatus.setStatus("mandatory")
_CtEtherSupportedPauseModes_Type = Integer32
_CtEtherSupportedPauseModes_Object = MibTableColumn
ctEtherSupportedPauseModes = _CtEtherSupportedPauseModes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 3),
    _CtEtherSupportedPauseModes_Type()
)
ctEtherSupportedPauseModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEtherSupportedPauseModes.setStatus("mandatory")


class _CtFlowCtlPauseAdminStatus_Type(Integer32):
    """Custom type ctFlowCtlPauseAdminStatus based on Integer32"""
    defaultValue = 5

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
        *(("asymmetricRx", 2),
          ("asymmetricTx", 3),
          ("autonegotiate", 5),
          ("disabled", 4),
          ("symmetric", 1))
    )


_CtFlowCtlPauseAdminStatus_Type.__name__ = "Integer32"
_CtFlowCtlPauseAdminStatus_Object = MibTableColumn
ctFlowCtlPauseAdminStatus = _CtFlowCtlPauseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 4),
    _CtFlowCtlPauseAdminStatus_Type()
)
ctFlowCtlPauseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFlowCtlPauseAdminStatus.setStatus("mandatory")


class _CtFlowCtlPauseOperStatus_Type(Integer32):
    """Custom type ctFlowCtlPauseOperStatus based on Integer32"""
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
        *(("asymmetricRx", 2),
          ("asymmetricTx", 3),
          ("disabled", 4),
          ("notsupported", 6),
          ("symmetric", 1),
          ("unknown", 5))
    )


_CtFlowCtlPauseOperStatus_Type.__name__ = "Integer32"
_CtFlowCtlPauseOperStatus_Object = MibTableColumn
ctFlowCtlPauseOperStatus = _CtFlowCtlPauseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 5),
    _CtFlowCtlPauseOperStatus_Type()
)
ctFlowCtlPauseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFlowCtlPauseOperStatus.setStatus("mandatory")


class _CtFlowCtlPauseTimer_Type(Integer32):
    """Custom type ctFlowCtlPauseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtFlowCtlPauseTimer_Type.__name__ = "Integer32"
_CtFlowCtlPauseTimer_Object = MibTableColumn
ctFlowCtlPauseTimer = _CtFlowCtlPauseTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 6),
    _CtFlowCtlPauseTimer_Type()
)
ctFlowCtlPauseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFlowCtlPauseTimer.setStatus("mandatory")
_CtFlowCtlRxPauseFrames_Type = Counter32
_CtFlowCtlRxPauseFrames_Object = MibTableColumn
ctFlowCtlRxPauseFrames = _CtFlowCtlRxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 7),
    _CtFlowCtlRxPauseFrames_Type()
)
ctFlowCtlRxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFlowCtlRxPauseFrames.setStatus("mandatory")
_CtFlowCtlTxPauseFrames_Type = Counter32
_CtFlowCtlTxPauseFrames_Object = MibTableColumn
ctFlowCtlTxPauseFrames = _CtFlowCtlTxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 8),
    _CtFlowCtlTxPauseFrames_Type()
)
ctFlowCtlTxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFlowCtlTxPauseFrames.setStatus("mandatory")
_CtEtherManualConfig_ObjectIdentity = ObjectIdentity
ctEtherManualConfig = _CtEtherManualConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3)
)
_CtEtherManualConfigTable_Object = MibTable
ctEtherManualConfigTable = _CtEtherManualConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ctEtherManualConfigTable.setStatus("mandatory")
_CtEtherManualConfigEntry_Object = MibTableRow
ctEtherManualConfigEntry = _CtEtherManualConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1)
)
ctEtherManualConfigEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctIfPortIfNumber"),
    (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"),
)
if mibBuilder.loadTexts:
    ctEtherManualConfigEntry.setStatus("mandatory")
_CtEtherSupportedSpeed_Type = Integer32
_CtEtherSupportedSpeed_Object = MibTableColumn
ctEtherSupportedSpeed = _CtEtherSupportedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 1),
    _CtEtherSupportedSpeed_Type()
)
ctEtherSupportedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEtherSupportedSpeed.setStatus("mandatory")


class _CtEtherSpeedAdminStatus_Type(Integer32):
    """Custom type ctEtherSpeedAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gigabit", 4),
          ("hundredmegabit", 3),
          ("tenmegabit", 2))
    )


_CtEtherSpeedAdminStatus_Type.__name__ = "Integer32"
_CtEtherSpeedAdminStatus_Object = MibTableColumn
ctEtherSpeedAdminStatus = _CtEtherSpeedAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 2),
    _CtEtherSpeedAdminStatus_Type()
)
ctEtherSpeedAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEtherSpeedAdminStatus.setStatus("mandatory")


class _CtEtherSpeedOperStatus_Type(Integer32):
    """Custom type ctEtherSpeedOperStatus based on Integer32"""
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
        *(("gigabit", 4),
          ("hundredmegabit", 3),
          ("tenmegabit", 2),
          ("unknown", 1))
    )


_CtEtherSpeedOperStatus_Type.__name__ = "Integer32"
_CtEtherSpeedOperStatus_Object = MibTableColumn
ctEtherSpeedOperStatus = _CtEtherSpeedOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 3),
    _CtEtherSpeedOperStatus_Type()
)
ctEtherSpeedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEtherSpeedOperStatus.setStatus("mandatory")


class _CtEtherSupportedDuplex_Type(Integer32):
    """Custom type ctEtherSupportedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 2),
          ("halfandfullduplex", 3),
          ("halfduplex", 1))
    )


_CtEtherSupportedDuplex_Type.__name__ = "Integer32"
_CtEtherSupportedDuplex_Object = MibTableColumn
ctEtherSupportedDuplex = _CtEtherSupportedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 4),
    _CtEtherSupportedDuplex_Type()
)
ctEtherSupportedDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEtherSupportedDuplex.setStatus("mandatory")


class _CtEtherDuplexAdminStatus_Type(Integer32):
    """Custom type ctEtherDuplexAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 3),
          ("halfduplex", 2))
    )


_CtEtherDuplexAdminStatus_Type.__name__ = "Integer32"
_CtEtherDuplexAdminStatus_Object = MibTableColumn
ctEtherDuplexAdminStatus = _CtEtherDuplexAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 5),
    _CtEtherDuplexAdminStatus_Type()
)
ctEtherDuplexAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEtherDuplexAdminStatus.setStatus("mandatory")


class _CtEtherDuplexOperStatus_Type(Integer32):
    """Custom type ctEtherDuplexOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 3),
          ("halfduplex", 2),
          ("unknown", 1))
    )


_CtEtherDuplexOperStatus_Type.__name__ = "Integer32"
_CtEtherDuplexOperStatus_Object = MibTableColumn
ctEtherDuplexOperStatus = _CtEtherDuplexOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 6),
    _CtEtherDuplexOperStatus_Type()
)
ctEtherDuplexOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEtherDuplexOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ETHERNET-PARAMETERS-MIB",
    **{"ctAutoNegCtl": ctAutoNegCtl,
       "ctAutoNegCtlTable": ctAutoNegCtlTable,
       "ctAutoNegCtlEntry": ctAutoNegCtlEntry,
       "ctAutoNegAdminStatus": ctAutoNegAdminStatus,
       "ctAutoNegRemoteSignalling": ctAutoNegRemoteSignalling,
       "ctAutoNegAutoConfig": ctAutoNegAutoConfig,
       "ctAutoNegLocalTechnologyAbility": ctAutoNegLocalTechnologyAbility,
       "ctAutoNegAdvertisedTechnologyAbility": ctAutoNegAdvertisedTechnologyAbility,
       "ctAutoNegReceivedTechnologyAbility": ctAutoNegReceivedTechnologyAbility,
       "ctFlowControl": ctFlowControl,
       "ctFlowCtlTable": ctFlowCtlTable,
       "ctFlowCtlEntry": ctFlowCtlEntry,
       "ctFlowCtlHalfDuplexAdminStatus": ctFlowCtlHalfDuplexAdminStatus,
       "ctFlowCtlHalfDuplexOperStatus": ctFlowCtlHalfDuplexOperStatus,
       "ctEtherSupportedPauseModes": ctEtherSupportedPauseModes,
       "ctFlowCtlPauseAdminStatus": ctFlowCtlPauseAdminStatus,
       "ctFlowCtlPauseOperStatus": ctFlowCtlPauseOperStatus,
       "ctFlowCtlPauseTimer": ctFlowCtlPauseTimer,
       "ctFlowCtlRxPauseFrames": ctFlowCtlRxPauseFrames,
       "ctFlowCtlTxPauseFrames": ctFlowCtlTxPauseFrames,
       "ctEtherManualConfig": ctEtherManualConfig,
       "ctEtherManualConfigTable": ctEtherManualConfigTable,
       "ctEtherManualConfigEntry": ctEtherManualConfigEntry,
       "ctEtherSupportedSpeed": ctEtherSupportedSpeed,
       "ctEtherSpeedAdminStatus": ctEtherSpeedAdminStatus,
       "ctEtherSpeedOperStatus": ctEtherSpeedOperStatus,
       "ctEtherSupportedDuplex": ctEtherSupportedDuplex,
       "ctEtherDuplexAdminStatus": ctEtherDuplexAdminStatus,
       "ctEtherDuplexOperStatus": ctEtherDuplexOperStatus}
)
