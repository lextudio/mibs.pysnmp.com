# SNMP MIB module (MODULES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MODULES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:37 2024
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

_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12)
)
_EthAg_ObjectIdentity = ObjectIdentity
ethAg = _EthAg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 1)
)
_EthAgTable_Object = MibTable
ethAgTable = _EthAgTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ethAgTable.setStatus("mandatory")
_EthAgEntry_Object = MibTableRow
ethAgEntry = _EthAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1, 1)
)
ethAgEntry.setIndexNames(
    (0, "MODULES-MIB", "ethAgId"),
)
if mibBuilder.loadTexts:
    ethAgEntry.setStatus("mandatory")


class _EthAgId_Type(Integer32):
    """Custom type ethAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthAgId_Type.__name__ = "Integer32"
_EthAgId_Object = MibTableColumn
ethAgId = _EthAgId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1, 1, 1),
    _EthAgId_Type()
)
ethAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethAgId.setStatus("mandatory")
_EthAgPerfBusSelection_Type = Integer32
_EthAgPerfBusSelection_Object = MibTableColumn
ethAgPerfBusSelection = _EthAgPerfBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1, 1, 2),
    _EthAgPerfBusSelection_Type()
)
ethAgPerfBusSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAgPerfBusSelection.setStatus("mandatory")
_EthGroup_ObjectIdentity = ObjectIdentity
ethGroup = _EthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 2)
)
_EthGroupTable_Object = MibTable
ethGroupTable = _EthGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ethGroupTable.setStatus("mandatory")
_EthGroupEntry_Object = MibTableRow
ethGroupEntry = _EthGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1)
)
ethGroupEntry.setIndexNames(
    (0, "MODULES-MIB", "ethGroupId"),
)
if mibBuilder.loadTexts:
    ethGroupEntry.setStatus("mandatory")


class _EthGroupId_Type(Integer32):
    """Custom type ethGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthGroupId_Type.__name__ = "Integer32"
_EthGroupId_Object = MibTableColumn
ethGroupId = _EthGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 1),
    _EthGroupId_Type()
)
ethGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupId.setStatus("mandatory")


class _EthGroupFIFO_Type(Integer32):
    """Custom type ethGroupFIFO based on Integer32"""
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


_EthGroupFIFO_Type.__name__ = "Integer32"
_EthGroupFIFO_Object = MibTableColumn
ethGroupFIFO = _EthGroupFIFO_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 2),
    _EthGroupFIFO_Type()
)
ethGroupFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupFIFO.setStatus("mandatory")


class _EthGroup10BTPlus_Type(Integer32):
    """Custom type ethGroup10BTPlus based on Integer32"""
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


_EthGroup10BTPlus_Type.__name__ = "Integer32"
_EthGroup10BTPlus_Object = MibTableColumn
ethGroup10BTPlus = _EthGroup10BTPlus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 3),
    _EthGroup10BTPlus_Type()
)
ethGroup10BTPlus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroup10BTPlus.setStatus("mandatory")


class _EthGroupIntPortsRedundancy_Type(Integer32):
    """Custom type ethGroupIntPortsRedundancy based on Integer32"""
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


_EthGroupIntPortsRedundancy_Type.__name__ = "Integer32"
_EthGroupIntPortsRedundancy_Object = MibTableColumn
ethGroupIntPortsRedundancy = _EthGroupIntPortsRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 4),
    _EthGroupIntPortsRedundancy_Type()
)
ethGroupIntPortsRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupIntPortsRedundancy.setStatus("mandatory")


class _EthGroupBackboneMode_Type(Integer32):
    """Custom type ethGroupBackboneMode based on Integer32"""
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


_EthGroupBackboneMode_Type.__name__ = "Integer32"
_EthGroupBackboneMode_Object = MibTableColumn
ethGroupBackboneMode = _EthGroupBackboneMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 5),
    _EthGroupBackboneMode_Type()
)
ethGroupBackboneMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupBackboneMode.setStatus("mandatory")


class _EthGroupFOIRLPlusMode_Type(Integer32):
    """Custom type ethGroupFOIRLPlusMode based on Integer32"""
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


_EthGroupFOIRLPlusMode_Type.__name__ = "Integer32"
_EthGroupFOIRLPlusMode_Object = MibTableColumn
ethGroupFOIRLPlusMode = _EthGroupFOIRLPlusMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 6),
    _EthGroupFOIRLPlusMode_Type()
)
ethGroupFOIRLPlusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupFOIRLPlusMode.setStatus("mandatory")


class _EthGroupWrongPortSelection_Type(Integer32):
    """Custom type ethGroupWrongPortSelection based on Integer32"""
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


_EthGroupWrongPortSelection_Type.__name__ = "Integer32"
_EthGroupWrongPortSelection_Object = MibTableColumn
ethGroupWrongPortSelection = _EthGroupWrongPortSelection_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 7),
    _EthGroupWrongPortSelection_Type()
)
ethGroupWrongPortSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupWrongPortSelection.setStatus("mandatory")


class _EthGroupBackupBus_Type(Integer32):
    """Custom type ethGroupBackupBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EthGroupBackupBus_Type.__name__ = "Integer32"
_EthGroupBackupBus_Object = MibTableColumn
ethGroupBackupBus = _EthGroupBackupBus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 8),
    _EthGroupBackupBus_Type()
)
ethGroupBackupBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupBackupBus.setStatus("mandatory")


class _EthGroupSingleBusMode_Type(Integer32):
    """Custom type ethGroupSingleBusMode based on Integer32"""
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


_EthGroupSingleBusMode_Type.__name__ = "Integer32"
_EthGroupSingleBusMode_Object = MibTableColumn
ethGroupSingleBusMode = _EthGroupSingleBusMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 9),
    _EthGroupSingleBusMode_Type()
)
ethGroupSingleBusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupSingleBusMode.setStatus("mandatory")
_EthGroupSpecificOID_Type = ObjectIdentifier
_EthGroupSpecificOID_Object = MibTableColumn
ethGroupSpecificOID = _EthGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 10),
    _EthGroupSpecificOID_Type()
)
ethGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupSpecificOID.setStatus("mandatory")


class _EthGroup10FBPlus_Type(Integer32):
    """Custom type ethGroup10FBPlus based on Integer32"""
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


_EthGroup10FBPlus_Type.__name__ = "Integer32"
_EthGroup10FBPlus_Object = MibTableColumn
ethGroup10FBPlus = _EthGroup10FBPlus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 11),
    _EthGroup10FBPlus_Type()
)
ethGroup10FBPlus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroup10FBPlus.setStatus("mandatory")


class _EthGroupMasterClock_Type(Integer32):
    """Custom type ethGroupMasterClock based on Integer32"""
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


_EthGroupMasterClock_Type.__name__ = "Integer32"
_EthGroupMasterClock_Object = MibTableColumn
ethGroupMasterClock = _EthGroupMasterClock_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 12),
    _EthGroupMasterClock_Type()
)
ethGroupMasterClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupMasterClock.setStatus("mandatory")


class _EthGroupIdleTrx_Type(Integer32):
    """Custom type ethGroupIdleTrx based on Integer32"""
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


_EthGroupIdleTrx_Type.__name__ = "Integer32"
_EthGroupIdleTrx_Object = MibTableColumn
ethGroupIdleTrx = _EthGroupIdleTrx_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 13),
    _EthGroupIdleTrx_Type()
)
ethGroupIdleTrx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupIdleTrx.setStatus("mandatory")
_EthGroupTotalFrames_Type = Counter32
_EthGroupTotalFrames_Object = MibTableColumn
ethGroupTotalFrames = _EthGroupTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 15),
    _EthGroupTotalFrames_Type()
)
ethGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupTotalFrames.setStatus("mandatory")
_EthGroupTotalOctets_Type = Counter32
_EthGroupTotalOctets_Object = MibTableColumn
ethGroupTotalOctets = _EthGroupTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 16),
    _EthGroupTotalOctets_Type()
)
ethGroupTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupTotalOctets.setStatus("mandatory")
_EthGroupTotalErrors_Type = Counter32
_EthGroupTotalErrors_Object = MibTableColumn
ethGroupTotalErrors = _EthGroupTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 17),
    _EthGroupTotalErrors_Type()
)
ethGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupTotalErrors.setStatus("mandatory")


class _EthGroupBridgeMode_Type(Integer32):
    """Custom type ethGroupBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              9,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bus1To10BTPort", 9),
          ("bus1ToAUIPort", 5),
          ("bus1Tobus2", 3),
          ("bus2To10BTPort", 10),
          ("bus2ToAUIPort", 6),
          ("portAUITo10BTPort", 12))
    )


_EthGroupBridgeMode_Type.__name__ = "Integer32"
_EthGroupBridgeMode_Object = MibTableColumn
ethGroupBridgeMode = _EthGroupBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 18),
    _EthGroupBridgeMode_Type()
)
ethGroupBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupBridgeMode.setStatus("mandatory")
_EthGroupBroadcastPkts_Type = Counter32
_EthGroupBroadcastPkts_Object = MibTableColumn
ethGroupBroadcastPkts = _EthGroupBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 19),
    _EthGroupBroadcastPkts_Type()
)
ethGroupBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupBroadcastPkts.setStatus("mandatory")
_EthGroupMulticastPkts_Type = Counter32
_EthGroupMulticastPkts_Object = MibTableColumn
ethGroupMulticastPkts = _EthGroupMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 20),
    _EthGroupMulticastPkts_Type()
)
ethGroupMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupMulticastPkts.setStatus("mandatory")
_EthPort_ObjectIdentity = ObjectIdentity
ethPort = _EthPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 3)
)
_EthPortTable_Object = MibTable
ethPortTable = _EthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ethPortTable.setStatus("mandatory")
_EthPortEntry_Object = MibTableRow
ethPortEntry = _EthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1)
)
ethPortEntry.setIndexNames(
    (0, "MODULES-MIB", "ethPortGroupId"),
    (0, "MODULES-MIB", "ethPortId"),
)
if mibBuilder.loadTexts:
    ethPortEntry.setStatus("mandatory")
_EthPortGroupId_Type = Integer32
_EthPortGroupId_Object = MibTableColumn
ethPortGroupId = _EthPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 1),
    _EthPortGroupId_Type()
)
ethPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortGroupId.setStatus("mandatory")
_EthPortId_Type = Integer32
_EthPortId_Object = MibTableColumn
ethPortId = _EthPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 2),
    _EthPortId_Type()
)
ethPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortId.setStatus("mandatory")


class _EthPortFunctionalStatus_Type(Integer32):
    """Custom type ethPortFunctionalStatus based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("illSeq", 6),
          ("localJabber", 3),
          ("lockLost", 11),
          ("notSupported", 255),
          ("ok", 1),
          ("partitionOrLocalJabber", 8),
          ("remoteFault", 10),
          ("remoteFaultOrLockLost", 9),
          ("remoteJabber", 5),
          ("rld", 2),
          ("shortCirc", 7),
          ("tld", 4))
    )


_EthPortFunctionalStatus_Type.__name__ = "Integer32"
_EthPortFunctionalStatus_Object = MibTableColumn
ethPortFunctionalStatus = _EthPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 3),
    _EthPortFunctionalStatus_Type()
)
ethPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFunctionalStatus.setStatus("mandatory")


class _EthPortManPart_Type(Integer32):
    """Custom type ethPortManPart based on Integer32"""
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


_EthPortManPart_Type.__name__ = "Integer32"
_EthPortManPart_Object = MibTableColumn
ethPortManPart = _EthPortManPart_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 4),
    _EthPortManPart_Type()
)
ethPortManPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortManPart.setStatus("mandatory")


class _EthPortJabber_Type(Integer32):
    """Custom type ethPortJabber based on Integer32"""
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


_EthPortJabber_Type.__name__ = "Integer32"
_EthPortJabber_Object = MibTableColumn
ethPortJabber = _EthPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 5),
    _EthPortJabber_Type()
)
ethPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortJabber.setStatus("mandatory")


class _EthPortNoAUILoop_Type(Integer32):
    """Custom type ethPortNoAUILoop based on Integer32"""
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


_EthPortNoAUILoop_Type.__name__ = "Integer32"
_EthPortNoAUILoop_Object = MibTableColumn
ethPortNoAUILoop = _EthPortNoAUILoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 6),
    _EthPortNoAUILoop_Type()
)
ethPortNoAUILoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortNoAUILoop.setStatus("mandatory")


class _EthPortMJLP_Type(Integer32):
    """Custom type ethPortMJLP based on Integer32"""
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


_EthPortMJLP_Type.__name__ = "Integer32"
_EthPortMJLP_Object = MibTableColumn
ethPortMJLP = _EthPortMJLP_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 7),
    _EthPortMJLP_Type()
)
ethPortMJLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortMJLP.setStatus("mandatory")


class _EthPortFIFO_Type(Integer32):
    """Custom type ethPortFIFO based on Integer32"""
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


_EthPortFIFO_Type.__name__ = "Integer32"
_EthPortFIFO_Object = MibTableColumn
ethPortFIFO = _EthPortFIFO_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 8),
    _EthPortFIFO_Type()
)
ethPortFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFIFO.setStatus("mandatory")


class _EthPortAutoPartitionState_Type(Integer32):
    """Custom type ethPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoPartition", 1),
          ("notAutoPartition", 2),
          ("notSupported", 255))
    )


_EthPortAutoPartitionState_Type.__name__ = "Integer32"
_EthPortAutoPartitionState_Object = MibTableColumn
ethPortAutoPartitionState = _EthPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 9),
    _EthPortAutoPartitionState_Type()
)
ethPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortAutoPartitionState.setStatus("mandatory")


class _EthPortSQETest_Type(Integer32):
    """Custom type ethPortSQETest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 255))
    )


_EthPortSQETest_Type.__name__ = "Integer32"
_EthPortSQETest_Object = MibTableColumn
ethPortSQETest = _EthPortSQETest_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 10),
    _EthPortSQETest_Type()
)
ethPortSQETest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortSQETest.setStatus("mandatory")
_EthPortLastSourceAddr_Type = OctetString
_EthPortLastSourceAddr_Object = MibTableColumn
ethPortLastSourceAddr = _EthPortLastSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 11),
    _EthPortLastSourceAddr_Type()
)
ethPortLastSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortLastSourceAddr.setStatus("mandatory")


class _EthPortUserStatus_Type(Integer32):
    """Custom type ethPortUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("multiUser", 2),
          ("notSupported", 255),
          ("singleUser", 1))
    )


_EthPortUserStatus_Type.__name__ = "Integer32"
_EthPortUserStatus_Object = MibTableColumn
ethPortUserStatus = _EthPortUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 12),
    _EthPortUserStatus_Type()
)
ethPortUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortUserStatus.setStatus("mandatory")
_EthPortMainBusSelection_Type = Integer32
_EthPortMainBusSelection_Object = MibTableColumn
ethPortMainBusSelection = _EthPortMainBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 13),
    _EthPortMainBusSelection_Type()
)
ethPortMainBusSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortMainBusSelection.setStatus("mandatory")
_EthPortTraffic_Type = Counter32
_EthPortTraffic_Object = MibTableColumn
ethPortTraffic = _EthPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 14),
    _EthPortTraffic_Type()
)
ethPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortTraffic.setStatus("mandatory")
_EthPortFramesReceivedOK_Type = Counter32
_EthPortFramesReceivedOK_Object = MibTableColumn
ethPortFramesReceivedOK = _EthPortFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 15),
    _EthPortFramesReceivedOK_Type()
)
ethPortFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFramesReceivedOK.setStatus("mandatory")
_EthPortRunts_Type = Counter32
_EthPortRunts_Object = MibTableColumn
ethPortRunts = _EthPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 16),
    _EthPortRunts_Type()
)
ethPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortRunts.setStatus("mandatory")
_EthPortPacketErrors_Type = Counter32
_EthPortPacketErrors_Object = MibTableColumn
ethPortPacketErrors = _EthPortPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 17),
    _EthPortPacketErrors_Type()
)
ethPortPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPacketErrors.setStatus("mandatory")
_EthPortSpecificOID_Type = ObjectIdentifier
_EthPortSpecificOID_Object = MibTableColumn
ethPortSpecificOID = _EthPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 18),
    _EthPortSpecificOID_Type()
)
ethPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortSpecificOID.setStatus("mandatory")
_EthPortCollisions_Type = Counter32
_EthPortCollisions_Object = MibTableColumn
ethPortCollisions = _EthPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 19),
    _EthPortCollisions_Type()
)
ethPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortCollisions.setStatus("mandatory")
_EthPortPartitions_Type = Counter32
_EthPortPartitions_Object = MibTableColumn
ethPortPartitions = _EthPortPartitions_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 20),
    _EthPortPartitions_Type()
)
ethPortPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPartitions.setStatus("mandatory")
_EthPortPygmys_Type = Counter32
_EthPortPygmys_Object = MibTableColumn
ethPortPygmys = _EthPortPygmys_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 21),
    _EthPortPygmys_Type()
)
ethPortPygmys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPygmys.setStatus("mandatory")
_EthPortJabberCounter_Type = Counter32
_EthPortJabberCounter_Object = MibTableColumn
ethPortJabberCounter = _EthPortJabberCounter_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 22),
    _EthPortJabberCounter_Type()
)
ethPortJabberCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortJabberCounter.setStatus("mandatory")


class _EthPortCoupling_Type(Integer32):
    """Custom type ethPortCoupling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("dc", 1),
          ("notSupported", 255))
    )


_EthPortCoupling_Type.__name__ = "Integer32"
_EthPortCoupling_Object = MibTableColumn
ethPortCoupling = _EthPortCoupling_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 23),
    _EthPortCoupling_Type()
)
ethPortCoupling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortCoupling.setStatus("mandatory")


class _EthPortPolarity_Type(Integer32):
    """Custom type ethPortPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_EthPortPolarity_Type.__name__ = "Integer32"
_EthPortPolarity_Object = MibTableColumn
ethPortPolarity = _EthPortPolarity_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 24),
    _EthPortPolarity_Type()
)
ethPortPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPolarity.setStatus("mandatory")
_EthPortReadableFrames_Type = Counter32
_EthPortReadableFrames_Object = MibTableColumn
ethPortReadableFrames = _EthPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 25),
    _EthPortReadableFrames_Type()
)
ethPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortReadableFrames.setStatus("mandatory")
_EthPortReadableOctets_Type = Counter32
_EthPortReadableOctets_Object = MibTableColumn
ethPortReadableOctets = _EthPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 26),
    _EthPortReadableOctets_Type()
)
ethPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortReadableOctets.setStatus("mandatory")
_EthPortFCSErrors_Type = Counter32
_EthPortFCSErrors_Object = MibTableColumn
ethPortFCSErrors = _EthPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 27),
    _EthPortFCSErrors_Type()
)
ethPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFCSErrors.setStatus("mandatory")
_EthPortAlignmentErrors_Type = Counter32
_EthPortAlignmentErrors_Object = MibTableColumn
ethPortAlignmentErrors = _EthPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 28),
    _EthPortAlignmentErrors_Type()
)
ethPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortAlignmentErrors.setStatus("mandatory")
_EthPortFramesTooLong_Type = Counter32
_EthPortFramesTooLong_Object = MibTableColumn
ethPortFramesTooLong = _EthPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 29),
    _EthPortFramesTooLong_Type()
)
ethPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFramesTooLong.setStatus("mandatory")
_EthPortLateEvents_Type = Counter32
_EthPortLateEvents_Object = MibTableColumn
ethPortLateEvents = _EthPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 30),
    _EthPortLateEvents_Type()
)
ethPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortLateEvents.setStatus("mandatory")
_EthPortVeryLongEvents_Type = Counter32
_EthPortVeryLongEvents_Object = MibTableColumn
ethPortVeryLongEvents = _EthPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 31),
    _EthPortVeryLongEvents_Type()
)
ethPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortVeryLongEvents.setStatus("mandatory")
_EthPortDataRateMismatches_Type = Counter32
_EthPortDataRateMismatches_Object = MibTableColumn
ethPortDataRateMismatches = _EthPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 32),
    _EthPortDataRateMismatches_Type()
)
ethPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortDataRateMismatches.setStatus("mandatory")
_EthPortTotalErrors_Type = Counter32
_EthPortTotalErrors_Object = MibTableColumn
ethPortTotalErrors = _EthPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 33),
    _EthPortTotalErrors_Type()
)
ethPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortTotalErrors.setStatus("mandatory")
_EthPortSourceAddrChanges_Type = Counter32
_EthPortSourceAddrChanges_Object = MibTableColumn
ethPortSourceAddrChanges = _EthPortSourceAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 34),
    _EthPortSourceAddrChanges_Type()
)
ethPortSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortSourceAddrChanges.setStatus("mandatory")


class _EthPortOperStatus_Type(Integer32):
    """Custom type ethPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notSupported", 255),
          ("operational", 1))
    )


_EthPortOperStatus_Type.__name__ = "Integer32"
_EthPortOperStatus_Object = MibTableColumn
ethPortOperStatus = _EthPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 35),
    _EthPortOperStatus_Type()
)
ethPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortOperStatus.setStatus("mandatory")
_EthPortBroadcastPkts_Type = Counter32
_EthPortBroadcastPkts_Object = MibTableColumn
ethPortBroadcastPkts = _EthPortBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 36),
    _EthPortBroadcastPkts_Type()
)
ethPortBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortBroadcastPkts.setStatus("mandatory")
_EthPortMulticastPkts_Type = Counter32
_EthPortMulticastPkts_Object = MibTableColumn
ethPortMulticastPkts = _EthPortMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 37),
    _EthPortMulticastPkts_Type()
)
ethPortMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortMulticastPkts.setStatus("mandatory")
_EthIntPort_ObjectIdentity = ObjectIdentity
ethIntPort = _EthIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 4)
)
_EthIntPortTable_Object = MibTable
ethIntPortTable = _EthIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1)
)
if mibBuilder.loadTexts:
    ethIntPortTable.setStatus("mandatory")
_EthIntPortEntry_Object = MibTableRow
ethIntPortEntry = _EthIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1)
)
ethIntPortEntry.setIndexNames(
    (0, "MODULES-MIB", "ethIntPortGroupId"),
    (0, "MODULES-MIB", "ethIntPortId"),
)
if mibBuilder.loadTexts:
    ethIntPortEntry.setStatus("mandatory")


class _EthIntPortGroupId_Type(Integer32):
    """Custom type ethIntPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthIntPortGroupId_Type.__name__ = "Integer32"
_EthIntPortGroupId_Object = MibTableColumn
ethIntPortGroupId = _EthIntPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 1),
    _EthIntPortGroupId_Type()
)
ethIntPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortGroupId.setStatus("mandatory")


class _EthIntPortId_Type(Integer32):
    """Custom type ethIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthIntPortId_Type.__name__ = "Integer32"
_EthIntPortId_Object = MibTableColumn
ethIntPortId = _EthIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 2),
    _EthIntPortId_Type()
)
ethIntPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortId.setStatus("mandatory")


class _EthIntPortPartition_Type(Integer32):
    """Custom type ethIntPortPartition based on Integer32"""
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


_EthIntPortPartition_Type.__name__ = "Integer32"
_EthIntPortPartition_Object = MibTableColumn
ethIntPortPartition = _EthIntPortPartition_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 3),
    _EthIntPortPartition_Type()
)
ethIntPortPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortPartition.setStatus("mandatory")


class _EthIntPortJabber_Type(Integer32):
    """Custom type ethIntPortJabber based on Integer32"""
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


_EthIntPortJabber_Type.__name__ = "Integer32"
_EthIntPortJabber_Object = MibTableColumn
ethIntPortJabber = _EthIntPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 4),
    _EthIntPortJabber_Type()
)
ethIntPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortJabber.setStatus("deprecated")


class _EthIntPortBackedUp_Type(Integer32):
    """Custom type ethIntPortBackedUp based on Integer32"""
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


_EthIntPortBackedUp_Type.__name__ = "Integer32"
_EthIntPortBackedUp_Object = MibTableColumn
ethIntPortBackedUp = _EthIntPortBackedUp_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 5),
    _EthIntPortBackedUp_Type()
)
ethIntPortBackedUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIntPortBackedUp.setStatus("mandatory")
_EthBus_ObjectIdentity = ObjectIdentity
ethBus = _EthBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 5)
)
_EthBusPerfTable_Object = MibTable
ethBusPerfTable = _EthBusPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1)
)
if mibBuilder.loadTexts:
    ethBusPerfTable.setStatus("mandatory")
_EthBusPerfEntry_Object = MibTableRow
ethBusPerfEntry = _EthBusPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1)
)
ethBusPerfEntry.setIndexNames(
    (0, "MODULES-MIB", "ethBusPerfAgId"),
    (0, "MODULES-MIB", "ethBusPerfId"),
)
if mibBuilder.loadTexts:
    ethBusPerfEntry.setStatus("mandatory")


class _EthBusPerfAgId_Type(Integer32):
    """Custom type ethBusPerfAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusPerfAgId_Type.__name__ = "Integer32"
_EthBusPerfAgId_Object = MibTableColumn
ethBusPerfAgId = _EthBusPerfAgId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 1),
    _EthBusPerfAgId_Type()
)
ethBusPerfAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPerfAgId.setStatus("mandatory")


class _EthBusPerfId_Type(Integer32):
    """Custom type ethBusPerfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusPerfId_Type.__name__ = "Integer32"
_EthBusPerfId_Object = MibTableColumn
ethBusPerfId = _EthBusPerfId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 2),
    _EthBusPerfId_Type()
)
ethBusPerfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPerfId.setStatus("mandatory")
_EthBusTrafficBuffer_Type = OctetString
_EthBusTrafficBuffer_Object = MibTableColumn
ethBusTrafficBuffer = _EthBusTrafficBuffer_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 3),
    _EthBusTrafficBuffer_Type()
)
ethBusTrafficBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTrafficBuffer.setStatus("deprecated")
_EthBusTrafficThresh_Type = Integer32
_EthBusTrafficThresh_Object = MibTableColumn
ethBusTrafficThresh = _EthBusTrafficThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 4),
    _EthBusTrafficThresh_Type()
)
ethBusTrafficThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBusTrafficThresh.setStatus("mandatory")
_EthBusPeakTraffic_Type = Integer32
_EthBusPeakTraffic_Object = MibTableColumn
ethBusPeakTraffic = _EthBusPeakTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 5),
    _EthBusPeakTraffic_Type()
)
ethBusPeakTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBusPeakTraffic.setStatus("mandatory")
_EthBusTotalCollisions_Type = Counter32
_EthBusTotalCollisions_Object = MibTableColumn
ethBusTotalCollisions = _EthBusTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 6),
    _EthBusTotalCollisions_Type()
)
ethBusTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalCollisions.setStatus("mandatory")
_EthBusTotalPackets_Type = Counter32
_EthBusTotalPackets_Object = MibTableColumn
ethBusTotalPackets = _EthBusTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 7),
    _EthBusTotalPackets_Type()
)
ethBusTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalPackets.setStatus("mandatory")
_EthBusTotalErrors_Type = Counter32
_EthBusTotalErrors_Object = MibTableColumn
ethBusTotalErrors = _EthBusTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 8),
    _EthBusTotalErrors_Type()
)
ethBusTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalErrors.setStatus("mandatory")
_EthBusTraffic_Type = Integer32
_EthBusTraffic_Object = MibTableColumn
ethBusTraffic = _EthBusTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 9),
    _EthBusTraffic_Type()
)
ethBusTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTraffic.setStatus("mandatory")
_EthBusUtilization_Type = Integer32
_EthBusUtilization_Object = MibTableColumn
ethBusUtilization = _EthBusUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 10),
    _EthBusUtilization_Type()
)
ethBusUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusUtilization.setStatus("mandatory")
_EthBusPeakUtilization_Type = Integer32
_EthBusPeakUtilization_Object = MibTableColumn
ethBusPeakUtilization = _EthBusPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 11),
    _EthBusPeakUtilization_Type()
)
ethBusPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPeakUtilization.setStatus("mandatory")


class _EthBusThresholdStatus_Type(OctetString):
    """Custom type ethBusThresholdStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EthBusThresholdStatus_Type.__name__ = "OctetString"
_EthBusThresholdStatus_Object = MibTableColumn
ethBusThresholdStatus = _EthBusThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 12),
    _EthBusThresholdStatus_Type()
)
ethBusThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusThresholdStatus.setStatus("mandatory")
_EthBusClockTable_Object = MibTable
ethBusClockTable = _EthBusClockTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2)
)
if mibBuilder.loadTexts:
    ethBusClockTable.setStatus("mandatory")
_EthBusClockEntry_Object = MibTableRow
ethBusClockEntry = _EthBusClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1)
)
ethBusClockEntry.setIndexNames(
    (0, "MODULES-MIB", "ethBusClockBusId"),
    (0, "MODULES-MIB", "ethBusClockId"),
)
if mibBuilder.loadTexts:
    ethBusClockEntry.setStatus("mandatory")


class _EthBusClockBusId_Type(Integer32):
    """Custom type ethBusClockBusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusClockBusId_Type.__name__ = "Integer32"
_EthBusClockBusId_Object = MibTableColumn
ethBusClockBusId = _EthBusClockBusId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1, 1),
    _EthBusClockBusId_Type()
)
ethBusClockBusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusClockBusId.setStatus("mandatory")


class _EthBusClockId_Type(Integer32):
    """Custom type ethBusClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusClockId_Type.__name__ = "Integer32"
_EthBusClockId_Object = MibTableColumn
ethBusClockId = _EthBusClockId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1, 2),
    _EthBusClockId_Type()
)
ethBusClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusClockId.setStatus("mandatory")


class _EthBusClockTestResult_Type(Integer32):
    """Custom type ethBusClockTestResult based on Integer32"""
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
        *(("busFailure", 3),
          ("clockFailure", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_EthBusClockTestResult_Type.__name__ = "Integer32"
_EthBusClockTestResult_Object = MibTableColumn
ethBusClockTestResult = _EthBusClockTestResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1, 3),
    _EthBusClockTestResult_Type()
)
ethBusClockTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusClockTestResult.setStatus("mandatory")
_Feth_ObjectIdentity = ObjectIdentity
feth = _Feth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 6)
)
_FethPort_ObjectIdentity = ObjectIdentity
fethPort = _FethPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1)
)
_FethPortTable_Object = MibTable
fethPortTable = _FethPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fethPortTable.setStatus("mandatory")
_FethPortEntry_Object = MibTableRow
fethPortEntry = _FethPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1)
)
fethPortEntry.setIndexNames(
    (0, "MODULES-MIB", "fethPortGroupId"),
    (0, "MODULES-MIB", "fethPortId"),
)
if mibBuilder.loadTexts:
    fethPortEntry.setStatus("mandatory")
_FethPortGroupId_Type = Integer32
_FethPortGroupId_Object = MibTableColumn
fethPortGroupId = _FethPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 1),
    _FethPortGroupId_Type()
)
fethPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortGroupId.setStatus("mandatory")
_FethPortId_Type = Integer32
_FethPortId_Object = MibTableColumn
fethPortId = _FethPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 2),
    _FethPortId_Type()
)
fethPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortId.setStatus("mandatory")


class _FethPortFunctionalStatus_Type(Integer32):
    """Custom type fethPortFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              10,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("ok", 1),
          ("partition", 8),
          ("remoteFault", 10),
          ("rld", 2),
          ("rxJabber", 3),
          ("wrongSpeed", 12))
    )


_FethPortFunctionalStatus_Type.__name__ = "Integer32"
_FethPortFunctionalStatus_Object = MibTableColumn
fethPortFunctionalStatus = _FethPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 3),
    _FethPortFunctionalStatus_Type()
)
fethPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortFunctionalStatus.setStatus("mandatory")


class _FethPortFIFO_Type(Integer32):
    """Custom type fethPortFIFO based on Integer32"""
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


_FethPortFIFO_Type.__name__ = "Integer32"
_FethPortFIFO_Object = MibTableColumn
fethPortFIFO = _FethPortFIFO_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 4),
    _FethPortFIFO_Type()
)
fethPortFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortFIFO.setStatus("mandatory")


class _FethPortOperStatus_Type(Integer32):
    """Custom type fethPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notSupported", 255),
          ("operational", 1))
    )


_FethPortOperStatus_Type.__name__ = "Integer32"
_FethPortOperStatus_Object = MibTableColumn
fethPortOperStatus = _FethPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 5),
    _FethPortOperStatus_Type()
)
fethPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortOperStatus.setStatus("mandatory")


class _FethPortAutoPartitionState_Type(Integer32):
    """Custom type fethPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoPartition", 1),
          ("notAutoPartition", 2),
          ("notSupported", 255))
    )


_FethPortAutoPartitionState_Type.__name__ = "Integer32"
_FethPortAutoPartitionState_Object = MibTableColumn
fethPortAutoPartitionState = _FethPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 6),
    _FethPortAutoPartitionState_Type()
)
fethPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortAutoPartitionState.setStatus("mandatory")
_FethPortFramesReceived_Type = Counter32
_FethPortFramesReceived_Object = MibTableColumn
fethPortFramesReceived = _FethPortFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 7),
    _FethPortFramesReceived_Type()
)
fethPortFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortFramesReceived.setStatus("mandatory")
_FethPortFramesTransmitted_Type = Counter32
_FethPortFramesTransmitted_Object = MibTableColumn
fethPortFramesTransmitted = _FethPortFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 8),
    _FethPortFramesTransmitted_Type()
)
fethPortFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortFramesTransmitted.setStatus("mandatory")
_FethPortTotalErrors_Type = Counter32
_FethPortTotalErrors_Object = MibTableColumn
fethPortTotalErrors = _FethPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 9),
    _FethPortTotalErrors_Type()
)
fethPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortTotalErrors.setStatus("mandatory")
_FethPortFramesTransmittedOK_Type = Counter32
_FethPortFramesTransmittedOK_Object = MibTableColumn
fethPortFramesTransmittedOK = _FethPortFramesTransmittedOK_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 10),
    _FethPortFramesTransmittedOK_Type()
)
fethPortFramesTransmittedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortFramesTransmittedOK.setStatus("mandatory")
_FethPortCollisionFrames_Type = Counter32
_FethPortCollisionFrames_Object = MibTableColumn
fethPortCollisionFrames = _FethPortCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 11),
    _FethPortCollisionFrames_Type()
)
fethPortCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortCollisionFrames.setStatus("mandatory")
_FethPortAlignmentErrors_Type = Counter32
_FethPortAlignmentErrors_Object = MibTableColumn
fethPortAlignmentErrors = _FethPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 12),
    _FethPortAlignmentErrors_Type()
)
fethPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortAlignmentErrors.setStatus("mandatory")
_FethPortRxErrors_Type = Counter32
_FethPortRxErrors_Object = MibTableColumn
fethPortRxErrors = _FethPortRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 13),
    _FethPortRxErrors_Type()
)
fethPortRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortRxErrors.setStatus("mandatory")
_FethPortReadableFrames_Type = Counter32
_FethPortReadableFrames_Object = MibTableColumn
fethPortReadableFrames = _FethPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 14),
    _FethPortReadableFrames_Type()
)
fethPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortReadableFrames.setStatus("mandatory")
_FethPortUpper32ReadableOctets_Type = Counter32
_FethPortUpper32ReadableOctets_Object = MibTableColumn
fethPortUpper32ReadableOctets = _FethPortUpper32ReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 15),
    _FethPortUpper32ReadableOctets_Type()
)
fethPortUpper32ReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortUpper32ReadableOctets.setStatus("mandatory")
_FethPortLower32ReadableOctets_Type = Counter32
_FethPortLower32ReadableOctets_Object = MibTableColumn
fethPortLower32ReadableOctets = _FethPortLower32ReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 16),
    _FethPortLower32ReadableOctets_Type()
)
fethPortLower32ReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortLower32ReadableOctets.setStatus("mandatory")
_FethPortFCSErrors_Type = Counter32
_FethPortFCSErrors_Object = MibTableColumn
fethPortFCSErrors = _FethPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 17),
    _FethPortFCSErrors_Type()
)
fethPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortFCSErrors.setStatus("mandatory")
_FethPortFrameTooLongs_Type = Counter32
_FethPortFrameTooLongs_Object = MibTableColumn
fethPortFrameTooLongs = _FethPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 18),
    _FethPortFrameTooLongs_Type()
)
fethPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortFrameTooLongs.setStatus("mandatory")
_FethPortShortEvents_Type = Counter32
_FethPortShortEvents_Object = MibTableColumn
fethPortShortEvents = _FethPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 19),
    _FethPortShortEvents_Type()
)
fethPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortShortEvents.setStatus("mandatory")
_FethPortRunts_Type = Counter32
_FethPortRunts_Object = MibTableColumn
fethPortRunts = _FethPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 20),
    _FethPortRunts_Type()
)
fethPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortRunts.setStatus("mandatory")
_FethPortLateEvents_Type = Counter32
_FethPortLateEvents_Object = MibTableColumn
fethPortLateEvents = _FethPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 21),
    _FethPortLateEvents_Type()
)
fethPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortLateEvents.setStatus("mandatory")
_FethPortVeryLongEvents_Type = Counter32
_FethPortVeryLongEvents_Object = MibTableColumn
fethPortVeryLongEvents = _FethPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 22),
    _FethPortVeryLongEvents_Type()
)
fethPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortVeryLongEvents.setStatus("mandatory")
_FethPortDataRateMismatches_Type = Counter32
_FethPortDataRateMismatches_Object = MibTableColumn
fethPortDataRateMismatches = _FethPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 23),
    _FethPortDataRateMismatches_Type()
)
fethPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortDataRateMismatches.setStatus("mandatory")
_FethPortAutoPartitions_Type = Counter32
_FethPortAutoPartitions_Object = MibTableColumn
fethPortAutoPartitions = _FethPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 24),
    _FethPortAutoPartitions_Type()
)
fethPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortAutoPartitions.setStatus("mandatory")
_FethPortSymbolErrors_Type = Counter32
_FethPortSymbolErrors_Object = MibTableColumn
fethPortSymbolErrors = _FethPortSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 25),
    _FethPortSymbolErrors_Type()
)
fethPortSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortSymbolErrors.setStatus("mandatory")


class _FethPortLastSourceAddress_Type(OctetString):
    """Custom type fethPortLastSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_FethPortLastSourceAddress_Type.__name__ = "OctetString"
_FethPortLastSourceAddress_Object = MibTableColumn
fethPortLastSourceAddress = _FethPortLastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 26),
    _FethPortLastSourceAddress_Type()
)
fethPortLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortLastSourceAddress.setStatus("deprecated")
_FethPortSourceAddrChanges_Type = Counter32
_FethPortSourceAddrChanges_Object = MibTableColumn
fethPortSourceAddrChanges = _FethPortSourceAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 27),
    _FethPortSourceAddrChanges_Type()
)
fethPortSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortSourceAddrChanges.setStatus("mandatory")


class _FethPortMode_Type(Integer32):
    """Custom type fethPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("fullDuplexAndFlowControl", 3),
          ("fullDuplexAndFlowControlAndISL", 5),
          ("fullDuplexAndISL", 4),
          ("halfDuplex", 1),
          ("notSupported", 255))
    )


_FethPortMode_Type.__name__ = "Integer32"
_FethPortMode_Object = MibTableColumn
fethPortMode = _FethPortMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 28),
    _FethPortMode_Type()
)
fethPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fethPortMode.setStatus("mandatory")


class _FethPortLinkRedundancyMode_Type(Integer32):
    """Custom type fethPortLinkRedundancyMode based on Integer32"""
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


_FethPortLinkRedundancyMode_Type.__name__ = "Integer32"
_FethPortLinkRedundancyMode_Object = MibTableColumn
fethPortLinkRedundancyMode = _FethPortLinkRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 29),
    _FethPortLinkRedundancyMode_Type()
)
fethPortLinkRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fethPortLinkRedundancyMode.setStatus("mandatory")


class _FethPortLinkRedundancyStatus_Type(Integer32):
    """Custom type fethPortLinkRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("firstLinkActive", 1),
          ("notSupported", 255),
          ("secondLinkActive", 2))
    )


_FethPortLinkRedundancyStatus_Type.__name__ = "Integer32"
_FethPortLinkRedundancyStatus_Object = MibTableColumn
fethPortLinkRedundancyStatus = _FethPortLinkRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 30),
    _FethPortLinkRedundancyStatus_Type()
)
fethPortLinkRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortLinkRedundancyStatus.setStatus("mandatory")


class _FethPortDormantLinkFunctionalStatus_Type(Integer32):
    """Custom type fethPortDormantLinkFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("ok", 1),
          ("remoteFault", 10),
          ("rld", 2))
    )


_FethPortDormantLinkFunctionalStatus_Type.__name__ = "Integer32"
_FethPortDormantLinkFunctionalStatus_Object = MibTableColumn
fethPortDormantLinkFunctionalStatus = _FethPortDormantLinkFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 31),
    _FethPortDormantLinkFunctionalStatus_Type()
)
fethPortDormantLinkFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortDormantLinkFunctionalStatus.setStatus("mandatory")
_FethPortUpper32TransmittedOctets_Type = Counter32
_FethPortUpper32TransmittedOctets_Object = MibTableColumn
fethPortUpper32TransmittedOctets = _FethPortUpper32TransmittedOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 32),
    _FethPortUpper32TransmittedOctets_Type()
)
fethPortUpper32TransmittedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortUpper32TransmittedOctets.setStatus("mandatory")
_FethPortLower32TransmittedOctets_Type = Counter32
_FethPortLower32TransmittedOctets_Object = MibTableColumn
fethPortLower32TransmittedOctets = _FethPortLower32TransmittedOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 33),
    _FethPortLower32TransmittedOctets_Type()
)
fethPortLower32TransmittedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortLower32TransmittedOctets.setStatus("mandatory")
_FethPortBroadcastReceivedFrames_Type = Counter32
_FethPortBroadcastReceivedFrames_Object = MibTableColumn
fethPortBroadcastReceivedFrames = _FethPortBroadcastReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 34),
    _FethPortBroadcastReceivedFrames_Type()
)
fethPortBroadcastReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortBroadcastReceivedFrames.setStatus("mandatory")
_FethPortMulticastReceivedFrames_Type = Counter32
_FethPortMulticastReceivedFrames_Object = MibTableColumn
fethPortMulticastReceivedFrames = _FethPortMulticastReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 35),
    _FethPortMulticastReceivedFrames_Type()
)
fethPortMulticastReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethPortMulticastReceivedFrames.setStatus("mandatory")


class _FethPortEnablePHY_Type(Integer32):
    """Custom type fethPortEnablePHY based on Integer32"""
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
        *(("enPHY1", 1),
          ("enPHY2", 2),
          ("notSupported", 255))
    )


_FethPortEnablePHY_Type.__name__ = "Integer32"
_FethPortEnablePHY_Object = MibTableColumn
fethPortEnablePHY = _FethPortEnablePHY_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 1, 1, 1, 36),
    _FethPortEnablePHY_Type()
)
fethPortEnablePHY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fethPortEnablePHY.setStatus("mandatory")
_FethGroup_ObjectIdentity = ObjectIdentity
fethGroup = _FethGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2)
)
_FethGroupTable_Object = MibTable
fethGroupTable = _FethGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1)
)
if mibBuilder.loadTexts:
    fethGroupTable.setStatus("mandatory")
_FethGroupEntry_Object = MibTableRow
fethGroupEntry = _FethGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1)
)
fethGroupEntry.setIndexNames(
    (0, "MODULES-MIB", "fethGroupId"),
)
if mibBuilder.loadTexts:
    fethGroupEntry.setStatus("mandatory")


class _FethGroupId_Type(Integer32):
    """Custom type fethGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FethGroupId_Type.__name__ = "Integer32"
_FethGroupId_Object = MibTableColumn
fethGroupId = _FethGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 1),
    _FethGroupId_Type()
)
fethGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethGroupId.setStatus("mandatory")


class _FethGroupOperStatus_Type(Integer32):
    """Custom type fethGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_FethGroupOperStatus_Type.__name__ = "Integer32"
_FethGroupOperStatus_Object = MibTableColumn
fethGroupOperStatus = _FethGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 2),
    _FethGroupOperStatus_Type()
)
fethGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethGroupOperStatus.setStatus("mandatory")
_FethGroupUtilization_Type = Integer32
_FethGroupUtilization_Object = MibTableColumn
fethGroupUtilization = _FethGroupUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 3),
    _FethGroupUtilization_Type()
)
fethGroupUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethGroupUtilization.setStatus("mandatory")
_FethGroupTotalFrames_Type = Counter32
_FethGroupTotalFrames_Object = MibTableColumn
fethGroupTotalFrames = _FethGroupTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 4),
    _FethGroupTotalFrames_Type()
)
fethGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethGroupTotalFrames.setStatus("mandatory")
_FethGroupUpper32TotalOctets_Type = Counter32
_FethGroupUpper32TotalOctets_Object = MibTableColumn
fethGroupUpper32TotalOctets = _FethGroupUpper32TotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 5),
    _FethGroupUpper32TotalOctets_Type()
)
fethGroupUpper32TotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethGroupUpper32TotalOctets.setStatus("mandatory")
_FethGroupLower32TotalOctets_Type = Counter32
_FethGroupLower32TotalOctets_Object = MibTableColumn
fethGroupLower32TotalOctets = _FethGroupLower32TotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 6),
    _FethGroupLower32TotalOctets_Type()
)
fethGroupLower32TotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethGroupLower32TotalOctets.setStatus("mandatory")
_FethGroupTotalErrors_Type = Counter32
_FethGroupTotalErrors_Object = MibTableColumn
fethGroupTotalErrors = _FethGroupTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 7),
    _FethGroupTotalErrors_Type()
)
fethGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fethGroupTotalErrors.setStatus("mandatory")


class _FethGroupFefiEnable_Type(Integer32):
    """Custom type fethGroupFefiEnable based on Integer32"""
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


_FethGroupFefiEnable_Type.__name__ = "Integer32"
_FethGroupFefiEnable_Object = MibTableColumn
fethGroupFefiEnable = _FethGroupFefiEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 6, 2, 1, 1, 8),
    _FethGroupFefiEnable_Type()
)
fethGroupFefiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fethGroupFefiEnable.setStatus("mandatory")
_Tok_ObjectIdentity = ObjectIdentity
tok = _Tok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13)
)
_TokRing_ObjectIdentity = ObjectIdentity
tokRing = _TokRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 1)
)
_TokRingTable_Object = MibTable
tokRingTable = _TokRingTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tokRingTable.setStatus("mandatory")
_TokRingEntry_Object = MibTableRow
tokRingEntry = _TokRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1)
)
tokRingEntry.setIndexNames(
    (0, "MODULES-MIB", "tokRingAgId"),
    (0, "MODULES-MIB", "tokRingId"),
)
if mibBuilder.loadTexts:
    tokRingEntry.setStatus("mandatory")


class _TokRingAgId_Type(Integer32):
    """Custom type tokRingAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingAgId_Type.__name__ = "Integer32"
_TokRingAgId_Object = MibTableColumn
tokRingAgId = _TokRingAgId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 1),
    _TokRingAgId_Type()
)
tokRingAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingAgId.setStatus("mandatory")


class _TokRingId_Type(Integer32):
    """Custom type tokRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingId_Type.__name__ = "Integer32"
_TokRingId_Object = MibTableColumn
tokRingId = _TokRingId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 2),
    _TokRingId_Type()
)
tokRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingId.setStatus("mandatory")


class _TokRingLeftSlot_Type(Integer32):
    """Custom type tokRingLeftSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingLeftSlot_Type.__name__ = "Integer32"
_TokRingLeftSlot_Object = MibTableColumn
tokRingLeftSlot = _TokRingLeftSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 3),
    _TokRingLeftSlot_Type()
)
tokRingLeftSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingLeftSlot.setStatus("mandatory")


class _TokRingRightSlot_Type(Integer32):
    """Custom type tokRingRightSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingRightSlot_Type.__name__ = "Integer32"
_TokRingRightSlot_Object = MibTableColumn
tokRingRightSlot = _TokRingRightSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 4),
    _TokRingRightSlot_Type()
)
tokRingRightSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingRightSlot.setStatus("mandatory")
_TokRingTrafficBuffer_Type = OctetString
_TokRingTrafficBuffer_Object = MibTableColumn
tokRingTrafficBuffer = _TokRingTrafficBuffer_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 5),
    _TokRingTrafficBuffer_Type()
)
tokRingTrafficBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingTrafficBuffer.setStatus("deprecated")
_TokRingTrafficThresh_Type = Integer32
_TokRingTrafficThresh_Object = MibTableColumn
tokRingTrafficThresh = _TokRingTrafficThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 6),
    _TokRingTrafficThresh_Type()
)
tokRingTrafficThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingTrafficThresh.setStatus("mandatory")
_TokRingPeakTraffic_Type = Integer32
_TokRingPeakTraffic_Object = MibTableColumn
tokRingPeakTraffic = _TokRingPeakTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 7),
    _TokRingPeakTraffic_Type()
)
tokRingPeakTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingPeakTraffic.setStatus("mandatory")
_TokRingNumberOfStations_Type = Integer32
_TokRingNumberOfStations_Object = MibTableColumn
tokRingNumberOfStations = _TokRingNumberOfStations_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 8),
    _TokRingNumberOfStations_Type()
)
tokRingNumberOfStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingNumberOfStations.setStatus("mandatory")
_TokRingConfiguration_Type = OctetString
_TokRingConfiguration_Object = MibTableColumn
tokRingConfiguration = _TokRingConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 9),
    _TokRingConfiguration_Type()
)
tokRingConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingConfiguration.setStatus("mandatory")


class _TokRingBeaconing_Type(Integer32):
    """Custom type tokRingBeaconing based on Integer32"""
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


_TokRingBeaconing_Type.__name__ = "Integer32"
_TokRingBeaconing_Object = MibTableColumn
tokRingBeaconing = _TokRingBeaconing_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 10),
    _TokRingBeaconing_Type()
)
tokRingBeaconing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingBeaconing.setStatus("mandatory")
_TokRingBeaconingStation_Type = OctetString
_TokRingBeaconingStation_Object = MibTableColumn
tokRingBeaconingStation = _TokRingBeaconingStation_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 11),
    _TokRingBeaconingStation_Type()
)
tokRingBeaconingStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingBeaconingStation.setStatus("mandatory")


class _TokRingStationsMatch_Type(Integer32):
    """Custom type tokRingStationsMatch based on Integer32"""
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
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1),
          ("partial", 3))
    )


_TokRingStationsMatch_Type.__name__ = "Integer32"
_TokRingStationsMatch_Object = MibTableColumn
tokRingStationsMatch = _TokRingStationsMatch_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 12),
    _TokRingStationsMatch_Type()
)
tokRingStationsMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationsMatch.setStatus("mandatory")
_TokRingTraffic_Type = Integer32
_TokRingTraffic_Object = MibTableColumn
tokRingTraffic = _TokRingTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 13),
    _TokRingTraffic_Type()
)
tokRingTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingTraffic.setStatus("mandatory")


class _TokRingSecurityMethod_Type(Integer32):
    """Custom type tokRingSecurityMethod based on Integer32"""
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
        *(("disabled", 3),
          ("notSupported", 255),
          ("perPort", 1),
          ("perRing", 2))
    )


_TokRingSecurityMethod_Type.__name__ = "Integer32"
_TokRingSecurityMethod_Object = MibTableColumn
tokRingSecurityMethod = _TokRingSecurityMethod_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 14),
    _TokRingSecurityMethod_Type()
)
tokRingSecurityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingSecurityMethod.setStatus("mandatory")


class _TokRingSecurityPolicy_Type(OctetString):
    """Custom type tokRingSecurityPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TokRingSecurityPolicy_Type.__name__ = "OctetString"
_TokRingSecurityPolicy_Object = MibTableColumn
tokRingSecurityPolicy = _TokRingSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 15),
    _TokRingSecurityPolicy_Type()
)
tokRingSecurityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingSecurityPolicy.setStatus("mandatory")
_TokRingSecureAddr_Type = OctetString
_TokRingSecureAddr_Object = MibTableColumn
tokRingSecureAddr = _TokRingSecureAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 16),
    _TokRingSecureAddr_Type()
)
tokRingSecureAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingSecureAddr.setStatus("mandatory")
_TokRingLastViolation_Type = OctetString
_TokRingLastViolation_Object = MibTableColumn
tokRingLastViolation = _TokRingLastViolation_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 17),
    _TokRingLastViolation_Type()
)
tokRingLastViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingLastViolation.setStatus("mandatory")
_TokRingUtilization_Type = Integer32
_TokRingUtilization_Object = MibTableColumn
tokRingUtilization = _TokRingUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 18),
    _TokRingUtilization_Type()
)
tokRingUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingUtilization.setStatus("mandatory")
_TokRingPeakUtilization_Type = Integer32
_TokRingPeakUtilization_Object = MibTableColumn
tokRingPeakUtilization = _TokRingPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 19),
    _TokRingPeakUtilization_Type()
)
tokRingPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingPeakUtilization.setStatus("mandatory")


class _TokRingBeaconingResolution_Type(Integer32):
    """Custom type tokRingBeaconingResolution based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_TokRingBeaconingResolution_Type.__name__ = "Integer32"
_TokRingBeaconingResolution_Object = MibTableColumn
tokRingBeaconingResolution = _TokRingBeaconingResolution_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 20),
    _TokRingBeaconingResolution_Type()
)
tokRingBeaconingResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingBeaconingResolution.setStatus("mandatory")


class _TokRingThresholdStatus_Type(OctetString):
    """Custom type tokRingThresholdStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TokRingThresholdStatus_Type.__name__ = "OctetString"
_TokRingThresholdStatus_Object = MibTableColumn
tokRingThresholdStatus = _TokRingThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 21),
    _TokRingThresholdStatus_Type()
)
tokRingThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingThresholdStatus.setStatus("mandatory")


class _TokRingActiveMonitor_Type(OctetString):
    """Custom type tokRingActiveMonitor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TokRingActiveMonitor_Type.__name__ = "OctetString"
_TokRingActiveMonitor_Object = MibTableColumn
tokRingActiveMonitor = _TokRingActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 22),
    _TokRingActiveMonitor_Type()
)
tokRingActiveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingActiveMonitor.setStatus("mandatory")
_TokGroup_ObjectIdentity = ObjectIdentity
tokGroup = _TokGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 2)
)
_TokGroupTable_Object = MibTable
tokGroupTable = _TokGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1)
)
if mibBuilder.loadTexts:
    tokGroupTable.setStatus("mandatory")
_TokGroupEntry_Object = MibTableRow
tokGroupEntry = _TokGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1)
)
tokGroupEntry.setIndexNames(
    (0, "MODULES-MIB", "tokGroupId"),
)
if mibBuilder.loadTexts:
    tokGroupEntry.setStatus("mandatory")


class _TokGroupId_Type(Integer32):
    """Custom type tokGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokGroupId_Type.__name__ = "Integer32"
_TokGroupId_Object = MibTableColumn
tokGroupId = _TokGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 1),
    _TokGroupId_Type()
)
tokGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupId.setStatus("mandatory")


class _TokGroupAutoRightLoop_Type(Integer32):
    """Custom type tokGroupAutoRightLoop based on Integer32"""
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


_TokGroupAutoRightLoop_Type.__name__ = "Integer32"
_TokGroupAutoRightLoop_Object = MibTableColumn
tokGroupAutoRightLoop = _TokGroupAutoRightLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 2),
    _TokGroupAutoRightLoop_Type()
)
tokGroupAutoRightLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoRightLoop.setStatus("mandatory")


class _TokGroupAutoLeftLoop_Type(Integer32):
    """Custom type tokGroupAutoLeftLoop based on Integer32"""
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


_TokGroupAutoLeftLoop_Type.__name__ = "Integer32"
_TokGroupAutoLeftLoop_Object = MibTableColumn
tokGroupAutoLeftLoop = _TokGroupAutoLeftLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 3),
    _TokGroupAutoLeftLoop_Type()
)
tokGroupAutoLeftLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoLeftLoop.setStatus("mandatory")


class _TokGroupManRightLoop_Type(Integer32):
    """Custom type tokGroupManRightLoop based on Integer32"""
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


_TokGroupManRightLoop_Type.__name__ = "Integer32"
_TokGroupManRightLoop_Object = MibTableColumn
tokGroupManRightLoop = _TokGroupManRightLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 4),
    _TokGroupManRightLoop_Type()
)
tokGroupManRightLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManRightLoop.setStatus("mandatory")


class _TokGroupManLeftLoop_Type(Integer32):
    """Custom type tokGroupManLeftLoop based on Integer32"""
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


_TokGroupManLeftLoop_Type.__name__ = "Integer32"
_TokGroupManLeftLoop_Object = MibTableColumn
tokGroupManLeftLoop = _TokGroupManLeftLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 5),
    _TokGroupManLeftLoop_Type()
)
tokGroupManLeftLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManLeftLoop.setStatus("mandatory")


class _TokGroupRightNeighbor_Type(Integer32):
    """Custom type tokGroupRightNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_TokGroupRightNeighbor_Type.__name__ = "Integer32"
_TokGroupRightNeighbor_Object = MibTableColumn
tokGroupRightNeighbor = _TokGroupRightNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 6),
    _TokGroupRightNeighbor_Type()
)
tokGroupRightNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRightNeighbor.setStatus("mandatory")


class _TokGroupLeftNeighbor_Type(Integer32):
    """Custom type tokGroupLeftNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_TokGroupLeftNeighbor_Type.__name__ = "Integer32"
_TokGroupLeftNeighbor_Object = MibTableColumn
tokGroupLeftNeighbor = _TokGroupLeftNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 7),
    _TokGroupLeftNeighbor_Type()
)
tokGroupLeftNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupLeftNeighbor.setStatus("mandatory")


class _TokGroupIOMode_Type(Integer32):
    """Custom type tokGroupIOMode based on Integer32"""
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
              10,
              11,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dualRingIn", 2),
          ("dualRingOut", 3),
          ("illegalMode", 4),
          ("intRepeater", 6),
          ("lobe", 5),
          ("notSupported", 255),
          ("single", 1),
          ("star", 7),
          ("starAndIntRepeater", 12),
          ("starAndRI", 10),
          ("starAndRingOut", 8),
          ("starAndSingle", 11))
    )


_TokGroupIOMode_Type.__name__ = "Integer32"
_TokGroupIOMode_Object = MibTableColumn
tokGroupIOMode = _TokGroupIOMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 8),
    _TokGroupIOMode_Type()
)
tokGroupIOMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupIOMode.setStatus("mandatory")


class _TokGroupBridgeMode_Type(Integer32):
    """Custom type tokGroupBridgeMode based on Integer32"""
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
        *(("modeA", 1),
          ("modeB", 2),
          ("modeC", 3),
          ("notSupported", 255))
    )


_TokGroupBridgeMode_Type.__name__ = "Integer32"
_TokGroupBridgeMode_Object = MibTableColumn
tokGroupBridgeMode = _TokGroupBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 9),
    _TokGroupBridgeMode_Type()
)
tokGroupBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupBridgeMode.setStatus("mandatory")


class _TokGroupManLinkLoop_Type(Integer32):
    """Custom type tokGroupManLinkLoop based on Integer32"""
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


_TokGroupManLinkLoop_Type.__name__ = "Integer32"
_TokGroupManLinkLoop_Object = MibTableColumn
tokGroupManLinkLoop = _TokGroupManLinkLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 10),
    _TokGroupManLinkLoop_Type()
)
tokGroupManLinkLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManLinkLoop.setStatus("mandatory")


class _TokGroupManBusLoop_Type(Integer32):
    """Custom type tokGroupManBusLoop based on Integer32"""
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


_TokGroupManBusLoop_Type.__name__ = "Integer32"
_TokGroupManBusLoop_Object = MibTableColumn
tokGroupManBusLoop = _TokGroupManBusLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 11),
    _TokGroupManBusLoop_Type()
)
tokGroupManBusLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManBusLoop.setStatus("mandatory")


class _TokGroupAutoLinkLoop_Type(Integer32):
    """Custom type tokGroupAutoLinkLoop based on Integer32"""
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


_TokGroupAutoLinkLoop_Type.__name__ = "Integer32"
_TokGroupAutoLinkLoop_Object = MibTableColumn
tokGroupAutoLinkLoop = _TokGroupAutoLinkLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 12),
    _TokGroupAutoLinkLoop_Type()
)
tokGroupAutoLinkLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoLinkLoop.setStatus("mandatory")


class _TokGroupAutoBusLoop_Type(Integer32):
    """Custom type tokGroupAutoBusLoop based on Integer32"""
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


_TokGroupAutoBusLoop_Type.__name__ = "Integer32"
_TokGroupAutoBusLoop_Object = MibTableColumn
tokGroupAutoBusLoop = _TokGroupAutoBusLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 13),
    _TokGroupAutoBusLoop_Type()
)
tokGroupAutoBusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoBusLoop.setStatus("mandatory")
_TokGroupSpecificOID_Type = ObjectIdentifier
_TokGroupSpecificOID_Object = MibTableColumn
tokGroupSpecificOID = _TokGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 14),
    _TokGroupSpecificOID_Type()
)
tokGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupSpecificOID.setStatus("mandatory")


class _TokGroupStarSpeedDetect_Type(Integer32):
    """Custom type tokGroupStarSpeedDetect based on Integer32"""
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


_TokGroupStarSpeedDetect_Type.__name__ = "Integer32"
_TokGroupStarSpeedDetect_Object = MibTableColumn
tokGroupStarSpeedDetect = _TokGroupStarSpeedDetect_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 15),
    _TokGroupStarSpeedDetect_Type()
)
tokGroupStarSpeedDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupStarSpeedDetect.setStatus("mandatory")


class _TokGroupLobeSpeedDetect_Type(Integer32):
    """Custom type tokGroupLobeSpeedDetect based on Integer32"""
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


_TokGroupLobeSpeedDetect_Type.__name__ = "Integer32"
_TokGroupLobeSpeedDetect_Object = MibTableColumn
tokGroupLobeSpeedDetect = _TokGroupLobeSpeedDetect_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 16),
    _TokGroupLobeSpeedDetect_Type()
)
tokGroupLobeSpeedDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupLobeSpeedDetect.setStatus("mandatory")


class _TokGroupLSTBeaconing_Type(Integer32):
    """Custom type tokGroupLSTBeaconing based on Integer32"""
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


_TokGroupLSTBeaconing_Type.__name__ = "Integer32"
_TokGroupLSTBeaconing_Object = MibTableColumn
tokGroupLSTBeaconing = _TokGroupLSTBeaconing_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 17),
    _TokGroupLSTBeaconing_Type()
)
tokGroupLSTBeaconing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupLSTBeaconing.setStatus("mandatory")


class _TokGroupLSTBeaconThresh_Type(Integer32):
    """Custom type tokGroupLSTBeaconThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokGroupLSTBeaconThresh_Type.__name__ = "Integer32"
_TokGroupLSTBeaconThresh_Object = MibTableColumn
tokGroupLSTBeaconThresh = _TokGroupLSTBeaconThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 18),
    _TokGroupLSTBeaconThresh_Type()
)
tokGroupLSTBeaconThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupLSTBeaconThresh.setStatus("mandatory")
_TokGroupRingTable_Object = MibTable
tokGroupRingTable = _TokGroupRingTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2)
)
if mibBuilder.loadTexts:
    tokGroupRingTable.setStatus("mandatory")
_TokGroupRingEntry_Object = MibTableRow
tokGroupRingEntry = _TokGroupRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1)
)
tokGroupRingEntry.setIndexNames(
    (0, "MODULES-MIB", "tokGroupRingGroupId"),
    (0, "MODULES-MIB", "tokGroupRingId"),
)
if mibBuilder.loadTexts:
    tokGroupRingEntry.setStatus("mandatory")


class _TokGroupRingGroupId_Type(Integer32):
    """Custom type tokGroupRingGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokGroupRingGroupId_Type.__name__ = "Integer32"
_TokGroupRingGroupId_Object = MibTableColumn
tokGroupRingGroupId = _TokGroupRingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 1),
    _TokGroupRingGroupId_Type()
)
tokGroupRingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRingGroupId.setStatus("mandatory")


class _TokGroupRingId_Type(Integer32):
    """Custom type tokGroupRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokGroupRingId_Type.__name__ = "Integer32"
_TokGroupRingId_Object = MibTableColumn
tokGroupRingId = _TokGroupRingId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 2),
    _TokGroupRingId_Type()
)
tokGroupRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRingId.setStatus("mandatory")


class _TokGroupRingSpeed_Type(Integer32):
    """Custom type tokGroupRingSpeed based on Integer32"""
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
        *(("fourMegabit", 3),
          ("oneMegabit", 2),
          ("sixteenMegabit", 4),
          ("sixteenMgbEarly", 5),
          ("unknown", 1))
    )


_TokGroupRingSpeed_Type.__name__ = "Integer32"
_TokGroupRingSpeed_Object = MibTableColumn
tokGroupRingSpeed = _TokGroupRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 3),
    _TokGroupRingSpeed_Type()
)
tokGroupRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupRingSpeed.setStatus("mandatory")


class _TokGroupRingInserted_Type(Integer32):
    """Custom type tokGroupRingInserted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 2),
          ("notInserted", 1),
          ("notSupported", 255))
    )


_TokGroupRingInserted_Type.__name__ = "Integer32"
_TokGroupRingInserted_Object = MibTableColumn
tokGroupRingInserted = _TokGroupRingInserted_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 4),
    _TokGroupRingInserted_Type()
)
tokGroupRingInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRingInserted.setStatus("mandatory")


class _TokGroupRingStatus_Type(Integer32):
    """Custom type tokGroupRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notSupported", 255),
          ("up", 1))
    )


_TokGroupRingStatus_Type.__name__ = "Integer32"
_TokGroupRingStatus_Object = MibTableColumn
tokGroupRingStatus = _TokGroupRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 5),
    _TokGroupRingStatus_Type()
)
tokGroupRingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupRingStatus.setStatus("mandatory")
_TokPort_ObjectIdentity = ObjectIdentity
tokPort = _TokPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 3)
)
_TokPortTable_Object = MibTable
tokPortTable = _TokPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1)
)
if mibBuilder.loadTexts:
    tokPortTable.setStatus("mandatory")
_TokPortEntry_Object = MibTableRow
tokPortEntry = _TokPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1)
)
tokPortEntry.setIndexNames(
    (0, "MODULES-MIB", "tokPortGroupId"),
    (0, "MODULES-MIB", "tokPortId"),
)
if mibBuilder.loadTexts:
    tokPortEntry.setStatus("mandatory")


class _TokPortGroupId_Type(Integer32):
    """Custom type tokPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokPortGroupId_Type.__name__ = "Integer32"
_TokPortGroupId_Object = MibTableColumn
tokPortGroupId = _TokPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 1),
    _TokPortGroupId_Type()
)
tokPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortGroupId.setStatus("mandatory")


class _TokPortId_Type(Integer32):
    """Custom type tokPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokPortId_Type.__name__ = "Integer32"
_TokPortId_Object = MibTableColumn
tokPortId = _TokPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 2),
    _TokPortId_Type()
)
tokPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortId.setStatus("mandatory")


class _TokPortBypass_Type(Integer32):
    """Custom type tokPortBypass based on Integer32"""
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


_TokPortBypass_Type.__name__ = "Integer32"
_TokPortBypass_Object = MibTableColumn
tokPortBypass = _TokPortBypass_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 3),
    _TokPortBypass_Type()
)
tokPortBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokPortBypass.setStatus("mandatory")


class _TokPortConnected_Type(Integer32):
    """Custom type tokPortConnected based on Integer32"""
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
          ("notConnected", 2),
          ("notSupported", 255))
    )


_TokPortConnected_Type.__name__ = "Integer32"
_TokPortConnected_Object = MibTableColumn
tokPortConnected = _TokPortConnected_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 4),
    _TokPortConnected_Type()
)
tokPortConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortConnected.setStatus("mandatory")


class _TokPortTCP_Type(Integer32):
    """Custom type tokPortTCP based on Integer32"""
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


_TokPortTCP_Type.__name__ = "Integer32"
_TokPortTCP_Object = MibTableColumn
tokPortTCP = _TokPortTCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 5),
    _TokPortTCP_Type()
)
tokPortTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokPortTCP.setStatus("mandatory")


class _TokPortCableFault_Type(Integer32):
    """Custom type tokPortCableFault based on Integer32"""
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


_TokPortCableFault_Type.__name__ = "Integer32"
_TokPortCableFault_Object = MibTableColumn
tokPortCableFault = _TokPortCableFault_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 6),
    _TokPortCableFault_Type()
)
tokPortCableFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortCableFault.setStatus("mandatory")


class _TokPortFunctionalStatus_Type(Integer32):
    """Custom type tokPortFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("ok", 1),
          ("rld", 2),
          ("tld", 4))
    )


_TokPortFunctionalStatus_Type.__name__ = "Integer32"
_TokPortFunctionalStatus_Object = MibTableColumn
tokPortFunctionalStatus = _TokPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 7),
    _TokPortFunctionalStatus_Type()
)
tokPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortFunctionalStatus.setStatus("mandatory")
_TokPortLastSourceAddr_Type = OctetString
_TokPortLastSourceAddr_Object = MibTableColumn
tokPortLastSourceAddr = _TokPortLastSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 8),
    _TokPortLastSourceAddr_Type()
)
tokPortLastSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortLastSourceAddr.setStatus("mandatory")
_TokPortSpecificOID_Type = ObjectIdentifier
_TokPortSpecificOID_Object = MibTableColumn
tokPortSpecificOID = _TokPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 9),
    _TokPortSpecificOID_Type()
)
tokPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortSpecificOID.setStatus("mandatory")


class _TokPortRingSpeedError_Type(Integer32):
    """Custom type tokPortRingSpeedError based on Integer32"""
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


_TokPortRingSpeedError_Type.__name__ = "Integer32"
_TokPortRingSpeedError_Object = MibTableColumn
tokPortRingSpeedError = _TokPortRingSpeedError_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 10),
    _TokPortRingSpeedError_Type()
)
tokPortRingSpeedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortRingSpeedError.setStatus("mandatory")


class _TokPortSpeedDetect_Type(Integer32):
    """Custom type tokPortSpeedDetect based on Integer32"""
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


_TokPortSpeedDetect_Type.__name__ = "Integer32"
_TokPortSpeedDetect_Object = MibTableColumn
tokPortSpeedDetect = _TokPortSpeedDetect_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 11),
    _TokPortSpeedDetect_Type()
)
tokPortSpeedDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokPortSpeedDetect.setStatus("mandatory")
_TokPortRingId_Type = Integer32
_TokPortRingId_Object = MibTableColumn
tokPortRingId = _TokPortRingId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 12),
    _TokPortRingId_Type()
)
tokPortRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortRingId.setStatus("mandatory")


class _TokPortMapping_Type(Integer32):
    """Custom type tokPortMapping based on Integer32"""
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


_TokPortMapping_Type.__name__ = "Integer32"
_TokPortMapping_Object = MibTableColumn
tokPortMapping = _TokPortMapping_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 13),
    _TokPortMapping_Type()
)
tokPortMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokPortMapping.setStatus("mandatory")
_TokRingStation_ObjectIdentity = ObjectIdentity
tokRingStation = _TokRingStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 4)
)
_TokRingStationTable_Object = MibTable
tokRingStationTable = _TokRingStationTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1)
)
if mibBuilder.loadTexts:
    tokRingStationTable.setStatus("mandatory")
_TokRingStationEntry_Object = MibTableRow
tokRingStationEntry = _TokRingStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1)
)
tokRingStationEntry.setIndexNames(
    (0, "MODULES-MIB", "tokRingId"),
    (0, "MODULES-MIB", "tokRingStationMAC"),
)
if mibBuilder.loadTexts:
    tokRingStationEntry.setStatus("mandatory")


class _TokRingStationRingId_Type(Integer32):
    """Custom type tokRingStationRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingStationRingId_Type.__name__ = "Integer32"
_TokRingStationRingId_Object = MibTableColumn
tokRingStationRingId = _TokRingStationRingId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 1),
    _TokRingStationRingId_Type()
)
tokRingStationRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationRingId.setStatus("mandatory")
_TokRingStationMAC_Type = OctetString
_TokRingStationMAC_Object = MibTableColumn
tokRingStationMAC = _TokRingStationMAC_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 2),
    _TokRingStationMAC_Type()
)
tokRingStationMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationMAC.setStatus("mandatory")
_TokRingStationLineErrors_Type = Counter32
_TokRingStationLineErrors_Object = MibTableColumn
tokRingStationLineErrors = _TokRingStationLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 3),
    _TokRingStationLineErrors_Type()
)
tokRingStationLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationLineErrors.setStatus("mandatory")
_TokRingStationInternalErrors_Type = Counter32
_TokRingStationInternalErrors_Object = MibTableColumn
tokRingStationInternalErrors = _TokRingStationInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 4),
    _TokRingStationInternalErrors_Type()
)
tokRingStationInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationInternalErrors.setStatus("mandatory")
_TokRingStationBurstErrors_Type = Counter32
_TokRingStationBurstErrors_Object = MibTableColumn
tokRingStationBurstErrors = _TokRingStationBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 5),
    _TokRingStationBurstErrors_Type()
)
tokRingStationBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationBurstErrors.setStatus("mandatory")
_TokRingStationACErrors_Type = Counter32
_TokRingStationACErrors_Object = MibTableColumn
tokRingStationACErrors = _TokRingStationACErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 6),
    _TokRingStationACErrors_Type()
)
tokRingStationACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationACErrors.setStatus("mandatory")
_TokRingStationAbortsTrans_Type = Counter32
_TokRingStationAbortsTrans_Object = MibTableColumn
tokRingStationAbortsTrans = _TokRingStationAbortsTrans_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 7),
    _TokRingStationAbortsTrans_Type()
)
tokRingStationAbortsTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationAbortsTrans.setStatus("mandatory")
_TokRingStationLostFrames_Type = Counter32
_TokRingStationLostFrames_Object = MibTableColumn
tokRingStationLostFrames = _TokRingStationLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 8),
    _TokRingStationLostFrames_Type()
)
tokRingStationLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationLostFrames.setStatus("mandatory")
_TokRingStationReceiveCongErrors_Type = Counter32
_TokRingStationReceiveCongErrors_Object = MibTableColumn
tokRingStationReceiveCongErrors = _TokRingStationReceiveCongErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 9),
    _TokRingStationReceiveCongErrors_Type()
)
tokRingStationReceiveCongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationReceiveCongErrors.setStatus("mandatory")
_TokRingStationFramesCopied_Type = Counter32
_TokRingStationFramesCopied_Object = MibTableColumn
tokRingStationFramesCopied = _TokRingStationFramesCopied_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 10),
    _TokRingStationFramesCopied_Type()
)
tokRingStationFramesCopied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationFramesCopied.setStatus("mandatory")
_TokRingStationFrequencyErrors_Type = Counter32
_TokRingStationFrequencyErrors_Object = MibTableColumn
tokRingStationFrequencyErrors = _TokRingStationFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 11),
    _TokRingStationFrequencyErrors_Type()
)
tokRingStationFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationFrequencyErrors.setStatus("mandatory")
_TokRingStationTokenErrors_Type = Counter32
_TokRingStationTokenErrors_Object = MibTableColumn
tokRingStationTokenErrors = _TokRingStationTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 12),
    _TokRingStationTokenErrors_Type()
)
tokRingStationTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationTokenErrors.setStatus("mandatory")
_TokRingStationTotalErrors_Type = Counter32
_TokRingStationTotalErrors_Object = MibTableColumn
tokRingStationTotalErrors = _TokRingStationTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 13),
    _TokRingStationTotalErrors_Type()
)
tokRingStationTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationTotalErrors.setStatus("mandatory")


class _TokRingStationFunctionalType_Type(Integer32):
    """Custom type tokRingStationFunctionalType based on Integer32"""
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
        *(("activeMonitor", 8),
          ("agent", 2),
          ("bridge", 3),
          ("lanManager", 7),
          ("netbios", 4),
          ("other", 9),
          ("ringErrorMonitor", 6),
          ("ringParameterServer", 5),
          ("ringStation", 1))
    )


_TokRingStationFunctionalType_Type.__name__ = "Integer32"
_TokRingStationFunctionalType_Object = MibTableColumn
tokRingStationFunctionalType = _TokRingStationFunctionalType_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 4, 1, 1, 14),
    _TokRingStationFunctionalType_Type()
)
tokRingStationFunctionalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationFunctionalType.setStatus("mandatory")
_TokIntPort_ObjectIdentity = ObjectIdentity
tokIntPort = _TokIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 5)
)
_TokIntPortTable_Object = MibTable
tokIntPortTable = _TokIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1)
)
if mibBuilder.loadTexts:
    tokIntPortTable.setStatus("mandatory")
_TokIntPortEntry_Object = MibTableRow
tokIntPortEntry = _TokIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1)
)
tokIntPortEntry.setIndexNames(
    (0, "MODULES-MIB", "tokIntPortGroupId"),
    (0, "MODULES-MIB", "tokIntPortId"),
)
if mibBuilder.loadTexts:
    tokIntPortEntry.setStatus("mandatory")


class _TokIntPortGroupId_Type(Integer32):
    """Custom type tokIntPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokIntPortGroupId_Type.__name__ = "Integer32"
_TokIntPortGroupId_Object = MibTableColumn
tokIntPortGroupId = _TokIntPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 1),
    _TokIntPortGroupId_Type()
)
tokIntPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokIntPortGroupId.setStatus("mandatory")


class _TokIntPortId_Type(Integer32):
    """Custom type tokIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokIntPortId_Type.__name__ = "Integer32"
_TokIntPortId_Object = MibTableColumn
tokIntPortId = _TokIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 2),
    _TokIntPortId_Type()
)
tokIntPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokIntPortId.setStatus("mandatory")


class _TokIntPortLeftNeighbor_Type(Integer32):
    """Custom type tokIntPortLeftNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 3),
          ("exist", 1),
          ("notExist", 2))
    )


_TokIntPortLeftNeighbor_Type.__name__ = "Integer32"
_TokIntPortLeftNeighbor_Object = MibTableColumn
tokIntPortLeftNeighbor = _TokIntPortLeftNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 3),
    _TokIntPortLeftNeighbor_Type()
)
tokIntPortLeftNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokIntPortLeftNeighbor.setStatus("mandatory")


class _TokIntPortRightNeighbor_Type(Integer32):
    """Custom type tokIntPortRightNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 3),
          ("exist", 1),
          ("notExist", 2))
    )


_TokIntPortRightNeighbor_Type.__name__ = "Integer32"
_TokIntPortRightNeighbor_Object = MibTableColumn
tokIntPortRightNeighbor = _TokIntPortRightNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 4),
    _TokIntPortRightNeighbor_Type()
)
tokIntPortRightNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokIntPortRightNeighbor.setStatus("mandatory")


class _TokIntPortManLeftLoop_Type(Integer32):
    """Custom type tokIntPortManLeftLoop based on Integer32"""
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


_TokIntPortManLeftLoop_Type.__name__ = "Integer32"
_TokIntPortManLeftLoop_Object = MibTableColumn
tokIntPortManLeftLoop = _TokIntPortManLeftLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 5),
    _TokIntPortManLeftLoop_Type()
)
tokIntPortManLeftLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokIntPortManLeftLoop.setStatus("mandatory")


class _TokIntPortManRightLoop_Type(Integer32):
    """Custom type tokIntPortManRightLoop based on Integer32"""
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


_TokIntPortManRightLoop_Type.__name__ = "Integer32"
_TokIntPortManRightLoop_Object = MibTableColumn
tokIntPortManRightLoop = _TokIntPortManRightLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 6),
    _TokIntPortManRightLoop_Type()
)
tokIntPortManRightLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokIntPortManRightLoop.setStatus("mandatory")


class _TokIntPortAutoLeftLoop_Type(Integer32):
    """Custom type tokIntPortAutoLeftLoop based on Integer32"""
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


_TokIntPortAutoLeftLoop_Type.__name__ = "Integer32"
_TokIntPortAutoLeftLoop_Object = MibTableColumn
tokIntPortAutoLeftLoop = _TokIntPortAutoLeftLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 7),
    _TokIntPortAutoLeftLoop_Type()
)
tokIntPortAutoLeftLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokIntPortAutoLeftLoop.setStatus("mandatory")


class _TokIntPortAutoRightLoop_Type(Integer32):
    """Custom type tokIntPortAutoRightLoop based on Integer32"""
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


_TokIntPortAutoRightLoop_Type.__name__ = "Integer32"
_TokIntPortAutoRightLoop_Object = MibTableColumn
tokIntPortAutoRightLoop = _TokIntPortAutoRightLoop_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 5, 1, 1, 8),
    _TokIntPortAutoRightLoop_Type()
)
tokIntPortAutoRightLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokIntPortAutoRightLoop.setStatus("mandatory")
_Ts_ObjectIdentity = ObjectIdentity
ts = _Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 14)
)
_TsGroup_ObjectIdentity = ObjectIdentity
tsGroup = _TsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 14, 1)
)
_TsGroupTable_Object = MibTable
tsGroupTable = _TsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1)
)
if mibBuilder.loadTexts:
    tsGroupTable.setStatus("mandatory")
_TsGroupEntry_Object = MibTableRow
tsGroupEntry = _TsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1)
)
tsGroupEntry.setIndexNames(
    (0, "MODULES-MIB", "tsGroupId"),
)
if mibBuilder.loadTexts:
    tsGroupEntry.setStatus("mandatory")


class _TsGroupId_Type(Integer32):
    """Custom type tsGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TsGroupId_Type.__name__ = "Integer32"
_TsGroupId_Object = MibTableColumn
tsGroupId = _TsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1, 1),
    _TsGroupId_Type()
)
tsGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsGroupId.setStatus("mandatory")


class _TsGroupLATStatus_Type(Integer32):
    """Custom type tsGroupLATStatus based on Integer32"""
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


_TsGroupLATStatus_Type.__name__ = "Integer32"
_TsGroupLATStatus_Object = MibTableColumn
tsGroupLATStatus = _TsGroupLATStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1, 2),
    _TsGroupLATStatus_Type()
)
tsGroupLATStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsGroupLATStatus.setStatus("mandatory")


class _TsGroupOperationMode_Type(Integer32):
    """Custom type tsGroupOperationMode based on Integer32"""
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
        *(("diagnostics", 1),
          ("diagnosticsFailure", 2),
          ("loading", 3),
          ("loadingFailure", 4),
          ("operational", 5))
    )


_TsGroupOperationMode_Type.__name__ = "Integer32"
_TsGroupOperationMode_Object = MibTableColumn
tsGroupOperationMode = _TsGroupOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1, 3),
    _TsGroupOperationMode_Type()
)
tsGroupOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsGroupOperationMode.setStatus("mandatory")
_Ltalk_ObjectIdentity = ObjectIdentity
ltalk = _Ltalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 15)
)
_LtalkPort_ObjectIdentity = ObjectIdentity
ltalkPort = _LtalkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 15, 1)
)
_LtalkPortTable_Object = MibTable
ltalkPortTable = _LtalkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1)
)
if mibBuilder.loadTexts:
    ltalkPortTable.setStatus("mandatory")
_LtalkPortEntry_Object = MibTableRow
ltalkPortEntry = _LtalkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1)
)
ltalkPortEntry.setIndexNames(
    (0, "MODULES-MIB", "ltalkPortGroupId"),
    (0, "MODULES-MIB", "ltalkPortId"),
)
if mibBuilder.loadTexts:
    ltalkPortEntry.setStatus("mandatory")


class _LtalkPortGroupId_Type(Integer32):
    """Custom type ltalkPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LtalkPortGroupId_Type.__name__ = "Integer32"
_LtalkPortGroupId_Object = MibTableColumn
ltalkPortGroupId = _LtalkPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 1),
    _LtalkPortGroupId_Type()
)
ltalkPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortGroupId.setStatus("mandatory")


class _LtalkPortId_Type(Integer32):
    """Custom type ltalkPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LtalkPortId_Type.__name__ = "Integer32"
_LtalkPortId_Object = MibTableColumn
ltalkPortId = _LtalkPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 2),
    _LtalkPortId_Type()
)
ltalkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortId.setStatus("mandatory")


class _LtalkPortTest_Type(Integer32):
    """Custom type ltalkPortTest based on Integer32"""
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


_LtalkPortTest_Type.__name__ = "Integer32"
_LtalkPortTest_Object = MibTableColumn
ltalkPortTest = _LtalkPortTest_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 3),
    _LtalkPortTest_Type()
)
ltalkPortTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltalkPortTest.setStatus("mandatory")


class _LtalkPortTestResult_Type(Integer32):
    """Custom type ltalkPortTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("ok", 1))
    )


_LtalkPortTestResult_Type.__name__ = "Integer32"
_LtalkPortTestResult_Object = MibTableColumn
ltalkPortTestResult = _LtalkPortTestResult_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 4),
    _LtalkPortTestResult_Type()
)
ltalkPortTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortTestResult.setStatus("mandatory")


class _LtalkPortJam_Type(Integer32):
    """Custom type ltalkPortJam based on Integer32"""
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


_LtalkPortJam_Type.__name__ = "Integer32"
_LtalkPortJam_Object = MibTableColumn
ltalkPortJam = _LtalkPortJam_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 5),
    _LtalkPortJam_Type()
)
ltalkPortJam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortJam.setStatus("mandatory")
_Cl_ObjectIdentity = ObjectIdentity
cl = _Cl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 16)
)
_ClGroup_ObjectIdentity = ObjectIdentity
clGroup = _ClGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 16, 1)
)
_ClGroupTable_Object = MibTable
clGroupTable = _ClGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1)
)
if mibBuilder.loadTexts:
    clGroupTable.setStatus("mandatory")
_ClGroupEntry_Object = MibTableRow
clGroupEntry = _ClGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1)
)
clGroupEntry.setIndexNames(
    (0, "MODULES-MIB", "clGroupId"),
)
if mibBuilder.loadTexts:
    clGroupEntry.setStatus("mandatory")


class _ClGroupId_Type(Integer32):
    """Custom type clGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClGroupId_Type.__name__ = "Integer32"
_ClGroupId_Object = MibTableColumn
clGroupId = _ClGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 1),
    _ClGroupId_Type()
)
clGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGroupId.setStatus("mandatory")


class _ClGroupClockRedundancy_Type(Integer32):
    """Custom type clGroupClockRedundancy based on Integer32"""
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


_ClGroupClockRedundancy_Type.__name__ = "Integer32"
_ClGroupClockRedundancy_Object = MibTableColumn
clGroupClockRedundancy = _ClGroupClockRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 2),
    _ClGroupClockRedundancy_Type()
)
clGroupClockRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupClockRedundancy.setStatus("mandatory")
_ClGroupMainClock_Type = Integer32
_ClGroupMainClock_Object = MibTableColumn
clGroupMainClock = _ClGroupMainClock_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 3),
    _ClGroupMainClock_Type()
)
clGroupMainClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupMainClock.setStatus("mandatory")


class _ClGroupTestClocks_Type(Integer32):
    """Custom type clGroupTestClocks based on Integer32"""
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


_ClGroupTestClocks_Type.__name__ = "Integer32"
_ClGroupTestClocks_Object = MibTableColumn
clGroupTestClocks = _ClGroupTestClocks_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 4),
    _ClGroupTestClocks_Type()
)
clGroupTestClocks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupTestClocks.setStatus("mandatory")
_ClPort_ObjectIdentity = ObjectIdentity
clPort = _ClPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 16, 2)
)
_ClPortTable_Object = MibTable
clPortTable = _ClPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1)
)
if mibBuilder.loadTexts:
    clPortTable.setStatus("mandatory")
_ClPortEntry_Object = MibTableRow
clPortEntry = _ClPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1)
)
clPortEntry.setIndexNames(
    (0, "MODULES-MIB", "clPortGroupId"),
    (0, "MODULES-MIB", "clPortId"),
)
if mibBuilder.loadTexts:
    clPortEntry.setStatus("mandatory")


class _ClPortGroupId_Type(Integer32):
    """Custom type clPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClPortGroupId_Type.__name__ = "Integer32"
_ClPortGroupId_Object = MibTableColumn
clPortGroupId = _ClPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1, 1),
    _ClPortGroupId_Type()
)
clPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortGroupId.setStatus("mandatory")


class _ClPortId_Type(Integer32):
    """Custom type clPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClPortId_Type.__name__ = "Integer32"
_ClPortId_Object = MibTableColumn
clPortId = _ClPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1, 2),
    _ClPortId_Type()
)
clPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortId.setStatus("mandatory")


class _ClPortFunctionalStatus_Type(Integer32):
    """Custom type clPortFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("ok", 1))
    )


_ClPortFunctionalStatus_Type.__name__ = "Integer32"
_ClPortFunctionalStatus_Object = MibTableColumn
clPortFunctionalStatus = _ClPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1, 3),
    _ClPortFunctionalStatus_Type()
)
clPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortFunctionalStatus.setStatus("mandatory")
_BRouter_ObjectIdentity = ObjectIdentity
bRouter = _BRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 21)
)
_Iwb_ObjectIdentity = ObjectIdentity
iwb = _Iwb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 21, 1)
)
_Iwr_ObjectIdentity = ObjectIdentity
iwr = _Iwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 21, 2)
)
_IwrGroupTable_Object = MibTable
iwrGroupTable = _IwrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1)
)
if mibBuilder.loadTexts:
    iwrGroupTable.setStatus("mandatory")
_IwrGroupEntry_Object = MibTableRow
iwrGroupEntry = _IwrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1)
)
iwrGroupEntry.setIndexNames(
    (0, "MODULES-MIB", "iwrGroupId"),
)
if mibBuilder.loadTexts:
    iwrGroupEntry.setStatus("mandatory")
_IwrGroupId_Type = Integer32
_IwrGroupId_Object = MibTableColumn
iwrGroupId = _IwrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1, 1),
    _IwrGroupId_Type()
)
iwrGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrGroupId.setStatus("mandatory")


class _IwrOperState_Type(Integer32):
    """Custom type iwrOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 2),
          ("fail", 3),
          ("run", 1))
    )


_IwrOperState_Type.__name__ = "Integer32"
_IwrOperState_Object = MibTableColumn
iwrOperState = _IwrOperState_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1, 2),
    _IwrOperState_Type()
)
iwrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrOperState.setStatus("mandatory")


class _IwrPMState_Type(Integer32):
    """Custom type iwrPMState based on Integer32"""
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


_IwrPMState_Type.__name__ = "Integer32"
_IwrPMState_Object = MibTableColumn
iwrPMState = _IwrPMState_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1, 3),
    _IwrPMState_Type()
)
iwrPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrPMState.setStatus("mandatory")


class _IwrIOMState_Type(Integer32):
    """Custom type iwrIOMState based on Integer32"""
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


_IwrIOMState_Type.__name__ = "Integer32"
_IwrIOMState_Object = MibTableColumn
iwrIOMState = _IwrIOMState_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1, 4),
    _IwrIOMState_Type()
)
iwrIOMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrIOMState.setStatus("mandatory")


class _IwrEthernetMode_Type(Integer32):
    """Custom type iwrEthernetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bus4", 1),
          ("ex10bt", 2),
          ("notSupported", 255))
    )


_IwrEthernetMode_Type.__name__ = "Integer32"
_IwrEthernetMode_Object = MibTableColumn
iwrEthernetMode = _IwrEthernetMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1, 5),
    _IwrEthernetMode_Type()
)
iwrEthernetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwrEthernetMode.setStatus("mandatory")


class _IwrPrimaryFDDIInsert_Type(Integer32):
    """Custom type iwrPrimaryFDDIInsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 2),
          ("inserted", 1),
          ("notSupported", 255))
    )


_IwrPrimaryFDDIInsert_Type.__name__ = "Integer32"
_IwrPrimaryFDDIInsert_Object = MibTableColumn
iwrPrimaryFDDIInsert = _IwrPrimaryFDDIInsert_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1, 6),
    _IwrPrimaryFDDIInsert_Type()
)
iwrPrimaryFDDIInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrPrimaryFDDIInsert.setStatus("mandatory")


class _IwrSecondaryFDDIInsert_Type(Integer32):
    """Custom type iwrSecondaryFDDIInsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 2),
          ("inserted", 1),
          ("notSupported", 255))
    )


_IwrSecondaryFDDIInsert_Type.__name__ = "Integer32"
_IwrSecondaryFDDIInsert_Object = MibTableColumn
iwrSecondaryFDDIInsert = _IwrSecondaryFDDIInsert_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 1, 1, 7),
    _IwrSecondaryFDDIInsert_Type()
)
iwrSecondaryFDDIInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrSecondaryFDDIInsert.setStatus("mandatory")
_IwrWANTable_Object = MibTable
iwrWANTable = _IwrWANTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 2)
)
if mibBuilder.loadTexts:
    iwrWANTable.setStatus("mandatory")
_IwrWANEntry_Object = MibTableRow
iwrWANEntry = _IwrWANEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 2, 1)
)
iwrWANEntry.setIndexNames(
    (0, "MODULES-MIB", "iwrWANGroupId"),
    (0, "MODULES-MIB", "iwrWANPortId"),
)
if mibBuilder.loadTexts:
    iwrWANEntry.setStatus("mandatory")
_IwrWANGroupId_Type = Integer32
_IwrWANGroupId_Object = MibTableColumn
iwrWANGroupId = _IwrWANGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 2, 1, 1),
    _IwrWANGroupId_Type()
)
iwrWANGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANGroupId.setStatus("mandatory")
_IwrWANPortId_Type = Integer32
_IwrWANPortId_Object = MibTableColumn
iwrWANPortId = _IwrWANPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 2, 1, 2),
    _IwrWANPortId_Type()
)
iwrWANPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANPortId.setStatus("mandatory")


class _IwrWANConnection_Type(Integer32):
    """Custom type iwrWANConnection based on Integer32"""
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


_IwrWANConnection_Type.__name__ = "Integer32"
_IwrWANConnection_Object = MibTableColumn
iwrWANConnection = _IwrWANConnection_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 2, 1, 3),
    _IwrWANConnection_Type()
)
iwrWANConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANConnection.setStatus("mandatory")


class _IwrWANPortCableType_Type(Integer32):
    """Custom type iwrWANPortCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 2),
          ("v35", 3),
          ("x21", 1))
    )


_IwrWANPortCableType_Type.__name__ = "Integer32"
_IwrWANPortCableType_Object = MibTableColumn
iwrWANPortCableType = _IwrWANPortCableType_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 2, 1, 4),
    _IwrWANPortCableType_Type()
)
iwrWANPortCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANPortCableType.setStatus("mandatory")
_IwrInterfaceAddrTable_Object = MibTable
iwrInterfaceAddrTable = _IwrInterfaceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 3)
)
if mibBuilder.loadTexts:
    iwrInterfaceAddrTable.setStatus("mandatory")
_IwrInterfaceEntry_Object = MibTableRow
iwrInterfaceEntry = _IwrInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 3, 1)
)
iwrInterfaceEntry.setIndexNames(
    (0, "MODULES-MIB", "iwrInterfaceGroupId"),
    (0, "MODULES-MIB", "iwrInterfaceId"),
)
if mibBuilder.loadTexts:
    iwrInterfaceEntry.setStatus("mandatory")
_IwrInterfaceGroupId_Type = Integer32
_IwrInterfaceGroupId_Object = MibTableColumn
iwrInterfaceGroupId = _IwrInterfaceGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 3, 1, 1),
    _IwrInterfaceGroupId_Type()
)
iwrInterfaceGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrInterfaceGroupId.setStatus("mandatory")
_IwrInterfaceId_Type = Integer32
_IwrInterfaceId_Object = MibTableColumn
iwrInterfaceId = _IwrInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 3, 1, 2),
    _IwrInterfaceId_Type()
)
iwrInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrInterfaceId.setStatus("mandatory")
_IwrInterfaceAddr_Type = IpAddress
_IwrInterfaceAddr_Object = MibTableColumn
iwrInterfaceAddr = _IwrInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 3, 1, 3),
    _IwrInterfaceAddr_Type()
)
iwrInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrInterfaceAddr.setStatus("mandatory")
_IwrInterfaceMask_Type = IpAddress
_IwrInterfaceMask_Object = MibTableColumn
iwrInterfaceMask = _IwrInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 3, 1, 4),
    _IwrInterfaceMask_Type()
)
iwrInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrInterfaceMask.setStatus("mandatory")
_IwrInterfaceMacAddress_Type = OctetString
_IwrInterfaceMacAddress_Object = MibTableColumn
iwrInterfaceMacAddress = _IwrInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 2, 3, 1, 5),
    _IwrInterfaceMacAddress_Type()
)
iwrInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrInterfaceMacAddress.setStatus("mandatory")
_Itr_ObjectIdentity = ObjectIdentity
itr = _Itr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 21, 3)
)
_ItrGroupTable_Object = MibTable
itrGroupTable = _ItrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 1)
)
if mibBuilder.loadTexts:
    itrGroupTable.setStatus("mandatory")
_ItrGroupEntry_Object = MibTableRow
itrGroupEntry = _ItrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 1, 1)
)
itrGroupEntry.setIndexNames(
    (0, "MODULES-MIB", "itrGroupId"),
)
if mibBuilder.loadTexts:
    itrGroupEntry.setStatus("mandatory")
_ItrGroupId_Type = Integer32
_ItrGroupId_Object = MibTableColumn
itrGroupId = _ItrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 1, 1, 1),
    _ItrGroupId_Type()
)
itrGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrGroupId.setStatus("mandatory")
_ItrMainSWVersion_Type = DisplayString
_ItrMainSWVersion_Object = MibTableColumn
itrMainSWVersion = _ItrMainSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 1, 1, 2),
    _ItrMainSWVersion_Type()
)
itrMainSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrMainSWVersion.setStatus("mandatory")


class _ItrConfigState_Type(Integer32):
    """Custom type itrConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("notSupported", 255),
          ("remote", 2))
    )


_ItrConfigState_Type.__name__ = "Integer32"
_ItrConfigState_Object = MibTableColumn
itrConfigState = _ItrConfigState_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 1, 1, 3),
    _ItrConfigState_Type()
)
itrConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrConfigState.setStatus("mandatory")


class _ItrModuleState_Type(Integer32):
    """Custom type itrModuleState based on Integer32"""
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
        *(("load", 2),
          ("notSupported", 255),
          ("oper", 1),
          ("setup", 3))
    )


_ItrModuleState_Type.__name__ = "Integer32"
_ItrModuleState_Object = MibTableColumn
itrModuleState = _ItrModuleState_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 1, 1, 4),
    _ItrModuleState_Type()
)
itrModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrModuleState.setStatus("mandatory")
_ItrLinkTable_Object = MibTable
itrLinkTable = _ItrLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2)
)
if mibBuilder.loadTexts:
    itrLinkTable.setStatus("mandatory")
_ItrLinkEntry_Object = MibTableRow
itrLinkEntry = _ItrLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1)
)
itrLinkEntry.setIndexNames(
    (0, "MODULES-MIB", "itrLinkGroupId"),
    (0, "MODULES-MIB", "itrLinkPortId"),
)
if mibBuilder.loadTexts:
    itrLinkEntry.setStatus("mandatory")
_ItrLinkGroupId_Type = Integer32
_ItrLinkGroupId_Object = MibTableColumn
itrLinkGroupId = _ItrLinkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 1),
    _ItrLinkGroupId_Type()
)
itrLinkGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkGroupId.setStatus("mandatory")
_ItrLinkPortId_Type = Integer32
_ItrLinkPortId_Object = MibTableColumn
itrLinkPortId = _ItrLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 2),
    _ItrLinkPortId_Type()
)
itrLinkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkPortId.setStatus("mandatory")


class _ItrLinkIf_Type(Integer32):
    """Custom type itrLinkIf based on Integer32"""
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
        *(("dte-dce", 4),
          ("v11", 1),
          ("v24", 2),
          ("v35", 3))
    )


_ItrLinkIf_Type.__name__ = "Integer32"
_ItrLinkIf_Object = MibTableColumn
itrLinkIf = _ItrLinkIf_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 3),
    _ItrLinkIf_Type()
)
itrLinkIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkIf.setStatus("mandatory")


class _ItrLinkMode_Type(Integer32):
    """Custom type itrLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("sync", 1))
    )


_ItrLinkMode_Type.__name__ = "Integer32"
_ItrLinkMode_Object = MibTableColumn
itrLinkMode = _ItrLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 4),
    _ItrLinkMode_Type()
)
itrLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkMode.setStatus("mandatory")


class _ItrLinkAsyncRate_Type(Integer32):
    """Custom type itrLinkAsyncRate based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("r115200", 10),
          ("r14400", 4),
          ("r19200", 5),
          ("r2400", 1),
          ("r38400", 6),
          ("r4800", 2),
          ("r56000", 7),
          ("r57600", 8),
          ("r64000", 9),
          ("r9600", 3),
          ("unknown", 255))
    )


_ItrLinkAsyncRate_Type.__name__ = "Integer32"
_ItrLinkAsyncRate_Object = MibTableColumn
itrLinkAsyncRate = _ItrLinkAsyncRate_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 5),
    _ItrLinkAsyncRate_Type()
)
itrLinkAsyncRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkAsyncRate.setStatus("mandatory")


class _ItrLinkSyncRate_Type(Integer32):
    """Custom type itrLinkSyncRate based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("r1024000", 18),
          ("r112000", 12),
          ("r1200", 1),
          ("r128000", 13),
          ("r14400", 5),
          ("r1544000", 19),
          ("r19200", 6),
          ("r2048000", 20),
          ("r2400", 2),
          ("r256000", 14),
          ("r38400", 7),
          ("r384000", 15),
          ("r4800", 3),
          ("r48000", 8),
          ("r512000", 16),
          ("r56000", 9),
          ("r57600", 10),
          ("r64000", 11),
          ("r786000", 17),
          ("r9600", 4),
          ("unknown", 255))
    )


_ItrLinkSyncRate_Type.__name__ = "Integer32"
_ItrLinkSyncRate_Object = MibTableColumn
itrLinkSyncRate = _ItrLinkSyncRate_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 6),
    _ItrLinkSyncRate_Type()
)
itrLinkSyncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkSyncRate.setStatus("mandatory")


class _ItrLinkParity_Type(Integer32):
    """Custom type itrLinkParity based on Integer32"""
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


_ItrLinkParity_Type.__name__ = "Integer32"
_ItrLinkParity_Object = MibTableColumn
itrLinkParity = _ItrLinkParity_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 7),
    _ItrLinkParity_Type()
)
itrLinkParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkParity.setStatus("deprecated")


class _ItrLinkParityEvenOdd_Type(Integer32):
    """Custom type itrLinkParityEvenOdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("notSupported", 255),
          ("odd", 2))
    )


_ItrLinkParityEvenOdd_Type.__name__ = "Integer32"
_ItrLinkParityEvenOdd_Object = MibTableColumn
itrLinkParityEvenOdd = _ItrLinkParityEvenOdd_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 8),
    _ItrLinkParityEvenOdd_Type()
)
itrLinkParityEvenOdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkParityEvenOdd.setStatus("deprecated")


class _ItrLinkStopBit_Type(Integer32):
    """Custom type itrLinkStopBit based on Integer32"""
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
        *(("none", 3),
          ("notSupported", 255),
          ("one", 1),
          ("two", 2))
    )


_ItrLinkStopBit_Type.__name__ = "Integer32"
_ItrLinkStopBit_Object = MibTableColumn
itrLinkStopBit = _ItrLinkStopBit_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 9),
    _ItrLinkStopBit_Type()
)
itrLinkStopBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkStopBit.setStatus("mandatory")


class _ItrLinkRemoteLANConn_Type(Integer32):
    """Custom type itrLinkRemoteLANConn based on Integer32"""
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
          ("disconnected", 2),
          ("notSupported", 255))
    )


_ItrLinkRemoteLANConn_Type.__name__ = "Integer32"
_ItrLinkRemoteLANConn_Object = MibTableColumn
itrLinkRemoteLANConn = _ItrLinkRemoteLANConn_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 10),
    _ItrLinkRemoteLANConn_Type()
)
itrLinkRemoteLANConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkRemoteLANConn.setStatus("mandatory")


class _ItrLinkFunctionalStatus_Type(Integer32):
    """Custom type itrLinkFunctionalStatus based on Integer32"""
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
        *(("disable", 4),
          ("fail", 2),
          ("noRxClk", 3),
          ("ok", 1))
    )


_ItrLinkFunctionalStatus_Type.__name__ = "Integer32"
_ItrLinkFunctionalStatus_Object = MibTableColumn
itrLinkFunctionalStatus = _ItrLinkFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 11),
    _ItrLinkFunctionalStatus_Type()
)
itrLinkFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkFunctionalStatus.setStatus("mandatory")


class _ItrLinkAdminStatus_Type(Integer32):
    """Custom type itrLinkAdminStatus based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 1),
          ("enabledOnDemand", 2),
          ("notSupported", 255))
    )


_ItrLinkAdminStatus_Type.__name__ = "Integer32"
_ItrLinkAdminStatus_Object = MibTableColumn
itrLinkAdminStatus = _ItrLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 12),
    _ItrLinkAdminStatus_Type()
)
itrLinkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkAdminStatus.setStatus("mandatory")


class _ItrLinkReset_Type(Integer32):
    """Custom type itrLinkReset based on Integer32"""
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


_ItrLinkReset_Type.__name__ = "Integer32"
_ItrLinkReset_Object = MibTableColumn
itrLinkReset = _ItrLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 13),
    _ItrLinkReset_Type()
)
itrLinkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkReset.setStatus("mandatory")


class _ItrLinkConnectionStatus_Type(Integer32):
    """Custom type itrLinkConnectionStatus based on Integer32"""
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
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1),
          ("trying", 3))
    )


_ItrLinkConnectionStatus_Type.__name__ = "Integer32"
_ItrLinkConnectionStatus_Object = MibTableColumn
itrLinkConnectionStatus = _ItrLinkConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 14),
    _ItrLinkConnectionStatus_Type()
)
itrLinkConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkConnectionStatus.setStatus("mandatory")


class _ItrLinkDataBits_Type(Integer32):
    """Custom type itrLinkDataBits based on Integer32"""
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
        *(("eight", 2),
          ("none", 3),
          ("notSupported", 255),
          ("seven", 1))
    )


_ItrLinkDataBits_Type.__name__ = "Integer32"
_ItrLinkDataBits_Object = MibTableColumn
itrLinkDataBits = _ItrLinkDataBits_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 15),
    _ItrLinkDataBits_Type()
)
itrLinkDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkDataBits.setStatus("mandatory")


class _ItrLinkControlSignalsMode_Type(Integer32):
    """Custom type itrLinkControlSignalsMode based on Integer32"""
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


_ItrLinkControlSignalsMode_Type.__name__ = "Integer32"
_ItrLinkControlSignalsMode_Object = MibTableColumn
itrLinkControlSignalsMode = _ItrLinkControlSignalsMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 16),
    _ItrLinkControlSignalsMode_Type()
)
itrLinkControlSignalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkControlSignalsMode.setStatus("mandatory")


class _ItrLinkParityType_Type(Integer32):
    """Custom type itrLinkParityType based on Integer32"""
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
        *(("even", 2),
          ("noParity", 1),
          ("none", 4),
          ("notSupported", 255),
          ("odd", 3))
    )


_ItrLinkParityType_Type.__name__ = "Integer32"
_ItrLinkParityType_Object = MibTableColumn
itrLinkParityType = _ItrLinkParityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 21, 3, 2, 1, 17),
    _ItrLinkParityType_Type()
)
itrLinkParityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkParityType.setStatus("mandatory")
_LntFddiGroup_ObjectIdentity = ObjectIdentity
lntFddiGroup = _LntFddiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 25)
)
_LntFddiPort_ObjectIdentity = ObjectIdentity
lntFddiPort = _LntFddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 25, 1)
)
_LntFddiPortTable_Object = MibTable
lntFddiPortTable = _LntFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1)
)
if mibBuilder.loadTexts:
    lntFddiPortTable.setStatus("mandatory")
_LntFddiPortEntry_Object = MibTableRow
lntFddiPortEntry = _LntFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1)
)
lntFddiPortEntry.setIndexNames(
    (0, "MODULES-MIB", "lntFddiPortGroupId"),
    (0, "MODULES-MIB", "lntFddiPortId"),
)
if mibBuilder.loadTexts:
    lntFddiPortEntry.setStatus("mandatory")


class _LntFddiPortGroupId_Type(Integer32):
    """Custom type lntFddiPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LntFddiPortGroupId_Type.__name__ = "Integer32"
_LntFddiPortGroupId_Object = MibTableColumn
lntFddiPortGroupId = _LntFddiPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 1),
    _LntFddiPortGroupId_Type()
)
lntFddiPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortGroupId.setStatus("mandatory")


class _LntFddiPortId_Type(Integer32):
    """Custom type lntFddiPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LntFddiPortId_Type.__name__ = "Integer32"
_LntFddiPortId_Object = MibTableColumn
lntFddiPortId = _LntFddiPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 2),
    _LntFddiPortId_Type()
)
lntFddiPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortId.setStatus("mandatory")


class _LntFddiPortMACCurrentPath_Type(Integer32):
    """Custom type lntFddiPortMACCurrentPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_LntFddiPortMACCurrentPath_Type.__name__ = "Integer32"
_LntFddiPortMACCurrentPath_Object = MibTableColumn
lntFddiPortMACCurrentPath = _LntFddiPortMACCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 3),
    _LntFddiPortMACCurrentPath_Type()
)
lntFddiPortMACCurrentPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lntFddiPortMACCurrentPath.setStatus("mandatory")


class _LntFddiPortOpticalSwitchExist_Type(Integer32):
    """Custom type lntFddiPortOpticalSwitchExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("not-exist", 2))
    )


_LntFddiPortOpticalSwitchExist_Type.__name__ = "Integer32"
_LntFddiPortOpticalSwitchExist_Object = MibTableColumn
lntFddiPortOpticalSwitchExist = _LntFddiPortOpticalSwitchExist_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 4),
    _LntFddiPortOpticalSwitchExist_Type()
)
lntFddiPortOpticalSwitchExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortOpticalSwitchExist.setStatus("mandatory")


class _LntFddiPortRingConfiguration_Type(Integer32):
    """Custom type lntFddiPortRingConfiguration based on Integer32"""
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
        *(("dualHomingA", 6),
          ("dualHomingB", 7),
          ("isolate", 5),
          ("thru", 1),
          ("wrap-a", 2),
          ("wrap-b", 3),
          ("wrap-s", 4))
    )


_LntFddiPortRingConfiguration_Type.__name__ = "Integer32"
_LntFddiPortRingConfiguration_Object = MibTableColumn
lntFddiPortRingConfiguration = _LntFddiPortRingConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 5),
    _LntFddiPortRingConfiguration_Type()
)
lntFddiPortRingConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortRingConfiguration.setStatus("mandatory")


class _LntFddiPortLineStatusA_Type(Integer32):
    """Custom type lntFddiPortLineStatusA based on Integer32"""
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
        *(("als", 1),
          ("hls", 4),
          ("ils", 2),
          ("mls", 3),
          ("nls", 6),
          ("qls", 5),
          ("sils", 7))
    )


_LntFddiPortLineStatusA_Type.__name__ = "Integer32"
_LntFddiPortLineStatusA_Object = MibTableColumn
lntFddiPortLineStatusA = _LntFddiPortLineStatusA_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 6),
    _LntFddiPortLineStatusA_Type()
)
lntFddiPortLineStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortLineStatusA.setStatus("mandatory")


class _LntFddiPortLineStatusB_Type(Integer32):
    """Custom type lntFddiPortLineStatusB based on Integer32"""
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
        *(("als", 1),
          ("hls", 4),
          ("ils", 2),
          ("mls", 3),
          ("nls", 6),
          ("qls", 5),
          ("sils", 7))
    )


_LntFddiPortLineStatusB_Type.__name__ = "Integer32"
_LntFddiPortLineStatusB_Object = MibTableColumn
lntFddiPortLineStatusB = _LntFddiPortLineStatusB_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 7),
    _LntFddiPortLineStatusB_Type()
)
lntFddiPortLineStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortLineStatusB.setStatus("mandatory")
_LntFddiPortRxTotalPackets_Type = Counter32
_LntFddiPortRxTotalPackets_Object = MibTableColumn
lntFddiPortRxTotalPackets = _LntFddiPortRxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 8),
    _LntFddiPortRxTotalPackets_Type()
)
lntFddiPortRxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortRxTotalPackets.setStatus("mandatory")
_LntFddiPortRxTotalOctets_Type = Counter32
_LntFddiPortRxTotalOctets_Object = MibTableColumn
lntFddiPortRxTotalOctets = _LntFddiPortRxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 9),
    _LntFddiPortRxTotalOctets_Type()
)
lntFddiPortRxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortRxTotalOctets.setStatus("mandatory")
_LntFddiPortTxTotalPackets_Type = Counter32
_LntFddiPortTxTotalPackets_Object = MibTableColumn
lntFddiPortTxTotalPackets = _LntFddiPortTxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 10),
    _LntFddiPortTxTotalPackets_Type()
)
lntFddiPortTxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortTxTotalPackets.setStatus("mandatory")
_LntFddiPortTxTotalOctets_Type = Counter32
_LntFddiPortTxTotalOctets_Object = MibTableColumn
lntFddiPortTxTotalOctets = _LntFddiPortTxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 11),
    _LntFddiPortTxTotalOctets_Type()
)
lntFddiPortTxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lntFddiPortTxTotalOctets.setStatus("mandatory")


class _LntFddiPortIPXtoFDDIMatching_Type(Integer32):
    """Custom type lntFddiPortIPXtoFDDIMatching based on Integer32"""
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
        *(("fddi-raw", 4),
          ("llc", 1),
          ("notSupported", 255),
          ("snap", 2),
          ("tunneled", 3))
    )


_LntFddiPortIPXtoFDDIMatching_Type.__name__ = "Integer32"
_LntFddiPortIPXtoFDDIMatching_Object = MibTableColumn
lntFddiPortIPXtoFDDIMatching = _LntFddiPortIPXtoFDDIMatching_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 12),
    _LntFddiPortIPXtoFDDIMatching_Type()
)
lntFddiPortIPXtoFDDIMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lntFddiPortIPXtoFDDIMatching.setStatus("mandatory")


class _LntFddiPortFDDItoIPXMatching_Type(Integer32):
    """Custom type lntFddiPortFDDItoIPXMatching based on Integer32"""
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
        *(("eth-2", 3),
          ("eth-raw", 4),
          ("llc", 1),
          ("notSupported", 255),
          ("snap", 2))
    )


_LntFddiPortFDDItoIPXMatching_Type.__name__ = "Integer32"
_LntFddiPortFDDItoIPXMatching_Object = MibTableColumn
lntFddiPortFDDItoIPXMatching = _LntFddiPortFDDItoIPXMatching_Object(
    (1, 3, 6, 1, 4, 1, 81, 25, 1, 1, 1, 13),
    _LntFddiPortFDDItoIPXMatching_Type()
)
lntFddiPortFDDItoIPXMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lntFddiPortFDDItoIPXMatching.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MODULES-MIB",
    **{"eth": eth,
       "ethAg": ethAg,
       "ethAgTable": ethAgTable,
       "ethAgEntry": ethAgEntry,
       "ethAgId": ethAgId,
       "ethAgPerfBusSelection": ethAgPerfBusSelection,
       "ethGroup": ethGroup,
       "ethGroupTable": ethGroupTable,
       "ethGroupEntry": ethGroupEntry,
       "ethGroupId": ethGroupId,
       "ethGroupFIFO": ethGroupFIFO,
       "ethGroup10BTPlus": ethGroup10BTPlus,
       "ethGroupIntPortsRedundancy": ethGroupIntPortsRedundancy,
       "ethGroupBackboneMode": ethGroupBackboneMode,
       "ethGroupFOIRLPlusMode": ethGroupFOIRLPlusMode,
       "ethGroupWrongPortSelection": ethGroupWrongPortSelection,
       "ethGroupBackupBus": ethGroupBackupBus,
       "ethGroupSingleBusMode": ethGroupSingleBusMode,
       "ethGroupSpecificOID": ethGroupSpecificOID,
       "ethGroup10FBPlus": ethGroup10FBPlus,
       "ethGroupMasterClock": ethGroupMasterClock,
       "ethGroupIdleTrx": ethGroupIdleTrx,
       "ethGroupTotalFrames": ethGroupTotalFrames,
       "ethGroupTotalOctets": ethGroupTotalOctets,
       "ethGroupTotalErrors": ethGroupTotalErrors,
       "ethGroupBridgeMode": ethGroupBridgeMode,
       "ethGroupBroadcastPkts": ethGroupBroadcastPkts,
       "ethGroupMulticastPkts": ethGroupMulticastPkts,
       "ethPort": ethPort,
       "ethPortTable": ethPortTable,
       "ethPortEntry": ethPortEntry,
       "ethPortGroupId": ethPortGroupId,
       "ethPortId": ethPortId,
       "ethPortFunctionalStatus": ethPortFunctionalStatus,
       "ethPortManPart": ethPortManPart,
       "ethPortJabber": ethPortJabber,
       "ethPortNoAUILoop": ethPortNoAUILoop,
       "ethPortMJLP": ethPortMJLP,
       "ethPortFIFO": ethPortFIFO,
       "ethPortAutoPartitionState": ethPortAutoPartitionState,
       "ethPortSQETest": ethPortSQETest,
       "ethPortLastSourceAddr": ethPortLastSourceAddr,
       "ethPortUserStatus": ethPortUserStatus,
       "ethPortMainBusSelection": ethPortMainBusSelection,
       "ethPortTraffic": ethPortTraffic,
       "ethPortFramesReceivedOK": ethPortFramesReceivedOK,
       "ethPortRunts": ethPortRunts,
       "ethPortPacketErrors": ethPortPacketErrors,
       "ethPortSpecificOID": ethPortSpecificOID,
       "ethPortCollisions": ethPortCollisions,
       "ethPortPartitions": ethPortPartitions,
       "ethPortPygmys": ethPortPygmys,
       "ethPortJabberCounter": ethPortJabberCounter,
       "ethPortCoupling": ethPortCoupling,
       "ethPortPolarity": ethPortPolarity,
       "ethPortReadableFrames": ethPortReadableFrames,
       "ethPortReadableOctets": ethPortReadableOctets,
       "ethPortFCSErrors": ethPortFCSErrors,
       "ethPortAlignmentErrors": ethPortAlignmentErrors,
       "ethPortFramesTooLong": ethPortFramesTooLong,
       "ethPortLateEvents": ethPortLateEvents,
       "ethPortVeryLongEvents": ethPortVeryLongEvents,
       "ethPortDataRateMismatches": ethPortDataRateMismatches,
       "ethPortTotalErrors": ethPortTotalErrors,
       "ethPortSourceAddrChanges": ethPortSourceAddrChanges,
       "ethPortOperStatus": ethPortOperStatus,
       "ethPortBroadcastPkts": ethPortBroadcastPkts,
       "ethPortMulticastPkts": ethPortMulticastPkts,
       "ethIntPort": ethIntPort,
       "ethIntPortTable": ethIntPortTable,
       "ethIntPortEntry": ethIntPortEntry,
       "ethIntPortGroupId": ethIntPortGroupId,
       "ethIntPortId": ethIntPortId,
       "ethIntPortPartition": ethIntPortPartition,
       "ethIntPortJabber": ethIntPortJabber,
       "ethIntPortBackedUp": ethIntPortBackedUp,
       "ethBus": ethBus,
       "ethBusPerfTable": ethBusPerfTable,
       "ethBusPerfEntry": ethBusPerfEntry,
       "ethBusPerfAgId": ethBusPerfAgId,
       "ethBusPerfId": ethBusPerfId,
       "ethBusTrafficBuffer": ethBusTrafficBuffer,
       "ethBusTrafficThresh": ethBusTrafficThresh,
       "ethBusPeakTraffic": ethBusPeakTraffic,
       "ethBusTotalCollisions": ethBusTotalCollisions,
       "ethBusTotalPackets": ethBusTotalPackets,
       "ethBusTotalErrors": ethBusTotalErrors,
       "ethBusTraffic": ethBusTraffic,
       "ethBusUtilization": ethBusUtilization,
       "ethBusPeakUtilization": ethBusPeakUtilization,
       "ethBusThresholdStatus": ethBusThresholdStatus,
       "ethBusClockTable": ethBusClockTable,
       "ethBusClockEntry": ethBusClockEntry,
       "ethBusClockBusId": ethBusClockBusId,
       "ethBusClockId": ethBusClockId,
       "ethBusClockTestResult": ethBusClockTestResult,
       "feth": feth,
       "fethPort": fethPort,
       "fethPortTable": fethPortTable,
       "fethPortEntry": fethPortEntry,
       "fethPortGroupId": fethPortGroupId,
       "fethPortId": fethPortId,
       "fethPortFunctionalStatus": fethPortFunctionalStatus,
       "fethPortFIFO": fethPortFIFO,
       "fethPortOperStatus": fethPortOperStatus,
       "fethPortAutoPartitionState": fethPortAutoPartitionState,
       "fethPortFramesReceived": fethPortFramesReceived,
       "fethPortFramesTransmitted": fethPortFramesTransmitted,
       "fethPortTotalErrors": fethPortTotalErrors,
       "fethPortFramesTransmittedOK": fethPortFramesTransmittedOK,
       "fethPortCollisionFrames": fethPortCollisionFrames,
       "fethPortAlignmentErrors": fethPortAlignmentErrors,
       "fethPortRxErrors": fethPortRxErrors,
       "fethPortReadableFrames": fethPortReadableFrames,
       "fethPortUpper32ReadableOctets": fethPortUpper32ReadableOctets,
       "fethPortLower32ReadableOctets": fethPortLower32ReadableOctets,
       "fethPortFCSErrors": fethPortFCSErrors,
       "fethPortFrameTooLongs": fethPortFrameTooLongs,
       "fethPortShortEvents": fethPortShortEvents,
       "fethPortRunts": fethPortRunts,
       "fethPortLateEvents": fethPortLateEvents,
       "fethPortVeryLongEvents": fethPortVeryLongEvents,
       "fethPortDataRateMismatches": fethPortDataRateMismatches,
       "fethPortAutoPartitions": fethPortAutoPartitions,
       "fethPortSymbolErrors": fethPortSymbolErrors,
       "fethPortLastSourceAddress": fethPortLastSourceAddress,
       "fethPortSourceAddrChanges": fethPortSourceAddrChanges,
       "fethPortMode": fethPortMode,
       "fethPortLinkRedundancyMode": fethPortLinkRedundancyMode,
       "fethPortLinkRedundancyStatus": fethPortLinkRedundancyStatus,
       "fethPortDormantLinkFunctionalStatus": fethPortDormantLinkFunctionalStatus,
       "fethPortUpper32TransmittedOctets": fethPortUpper32TransmittedOctets,
       "fethPortLower32TransmittedOctets": fethPortLower32TransmittedOctets,
       "fethPortBroadcastReceivedFrames": fethPortBroadcastReceivedFrames,
       "fethPortMulticastReceivedFrames": fethPortMulticastReceivedFrames,
       "fethPortEnablePHY": fethPortEnablePHY,
       "fethGroup": fethGroup,
       "fethGroupTable": fethGroupTable,
       "fethGroupEntry": fethGroupEntry,
       "fethGroupId": fethGroupId,
       "fethGroupOperStatus": fethGroupOperStatus,
       "fethGroupUtilization": fethGroupUtilization,
       "fethGroupTotalFrames": fethGroupTotalFrames,
       "fethGroupUpper32TotalOctets": fethGroupUpper32TotalOctets,
       "fethGroupLower32TotalOctets": fethGroupLower32TotalOctets,
       "fethGroupTotalErrors": fethGroupTotalErrors,
       "fethGroupFefiEnable": fethGroupFefiEnable,
       "tok": tok,
       "tokRing": tokRing,
       "tokRingTable": tokRingTable,
       "tokRingEntry": tokRingEntry,
       "tokRingAgId": tokRingAgId,
       "tokRingId": tokRingId,
       "tokRingLeftSlot": tokRingLeftSlot,
       "tokRingRightSlot": tokRingRightSlot,
       "tokRingTrafficBuffer": tokRingTrafficBuffer,
       "tokRingTrafficThresh": tokRingTrafficThresh,
       "tokRingPeakTraffic": tokRingPeakTraffic,
       "tokRingNumberOfStations": tokRingNumberOfStations,
       "tokRingConfiguration": tokRingConfiguration,
       "tokRingBeaconing": tokRingBeaconing,
       "tokRingBeaconingStation": tokRingBeaconingStation,
       "tokRingStationsMatch": tokRingStationsMatch,
       "tokRingTraffic": tokRingTraffic,
       "tokRingSecurityMethod": tokRingSecurityMethod,
       "tokRingSecurityPolicy": tokRingSecurityPolicy,
       "tokRingSecureAddr": tokRingSecureAddr,
       "tokRingLastViolation": tokRingLastViolation,
       "tokRingUtilization": tokRingUtilization,
       "tokRingPeakUtilization": tokRingPeakUtilization,
       "tokRingBeaconingResolution": tokRingBeaconingResolution,
       "tokRingThresholdStatus": tokRingThresholdStatus,
       "tokRingActiveMonitor": tokRingActiveMonitor,
       "tokGroup": tokGroup,
       "tokGroupTable": tokGroupTable,
       "tokGroupEntry": tokGroupEntry,
       "tokGroupId": tokGroupId,
       "tokGroupAutoRightLoop": tokGroupAutoRightLoop,
       "tokGroupAutoLeftLoop": tokGroupAutoLeftLoop,
       "tokGroupManRightLoop": tokGroupManRightLoop,
       "tokGroupManLeftLoop": tokGroupManLeftLoop,
       "tokGroupRightNeighbor": tokGroupRightNeighbor,
       "tokGroupLeftNeighbor": tokGroupLeftNeighbor,
       "tokGroupIOMode": tokGroupIOMode,
       "tokGroupBridgeMode": tokGroupBridgeMode,
       "tokGroupManLinkLoop": tokGroupManLinkLoop,
       "tokGroupManBusLoop": tokGroupManBusLoop,
       "tokGroupAutoLinkLoop": tokGroupAutoLinkLoop,
       "tokGroupAutoBusLoop": tokGroupAutoBusLoop,
       "tokGroupSpecificOID": tokGroupSpecificOID,
       "tokGroupStarSpeedDetect": tokGroupStarSpeedDetect,
       "tokGroupLobeSpeedDetect": tokGroupLobeSpeedDetect,
       "tokGroupLSTBeaconing": tokGroupLSTBeaconing,
       "tokGroupLSTBeaconThresh": tokGroupLSTBeaconThresh,
       "tokGroupRingTable": tokGroupRingTable,
       "tokGroupRingEntry": tokGroupRingEntry,
       "tokGroupRingGroupId": tokGroupRingGroupId,
       "tokGroupRingId": tokGroupRingId,
       "tokGroupRingSpeed": tokGroupRingSpeed,
       "tokGroupRingInserted": tokGroupRingInserted,
       "tokGroupRingStatus": tokGroupRingStatus,
       "tokPort": tokPort,
       "tokPortTable": tokPortTable,
       "tokPortEntry": tokPortEntry,
       "tokPortGroupId": tokPortGroupId,
       "tokPortId": tokPortId,
       "tokPortBypass": tokPortBypass,
       "tokPortConnected": tokPortConnected,
       "tokPortTCP": tokPortTCP,
       "tokPortCableFault": tokPortCableFault,
       "tokPortFunctionalStatus": tokPortFunctionalStatus,
       "tokPortLastSourceAddr": tokPortLastSourceAddr,
       "tokPortSpecificOID": tokPortSpecificOID,
       "tokPortRingSpeedError": tokPortRingSpeedError,
       "tokPortSpeedDetect": tokPortSpeedDetect,
       "tokPortRingId": tokPortRingId,
       "tokPortMapping": tokPortMapping,
       "tokRingStation": tokRingStation,
       "tokRingStationTable": tokRingStationTable,
       "tokRingStationEntry": tokRingStationEntry,
       "tokRingStationRingId": tokRingStationRingId,
       "tokRingStationMAC": tokRingStationMAC,
       "tokRingStationLineErrors": tokRingStationLineErrors,
       "tokRingStationInternalErrors": tokRingStationInternalErrors,
       "tokRingStationBurstErrors": tokRingStationBurstErrors,
       "tokRingStationACErrors": tokRingStationACErrors,
       "tokRingStationAbortsTrans": tokRingStationAbortsTrans,
       "tokRingStationLostFrames": tokRingStationLostFrames,
       "tokRingStationReceiveCongErrors": tokRingStationReceiveCongErrors,
       "tokRingStationFramesCopied": tokRingStationFramesCopied,
       "tokRingStationFrequencyErrors": tokRingStationFrequencyErrors,
       "tokRingStationTokenErrors": tokRingStationTokenErrors,
       "tokRingStationTotalErrors": tokRingStationTotalErrors,
       "tokRingStationFunctionalType": tokRingStationFunctionalType,
       "tokIntPort": tokIntPort,
       "tokIntPortTable": tokIntPortTable,
       "tokIntPortEntry": tokIntPortEntry,
       "tokIntPortGroupId": tokIntPortGroupId,
       "tokIntPortId": tokIntPortId,
       "tokIntPortLeftNeighbor": tokIntPortLeftNeighbor,
       "tokIntPortRightNeighbor": tokIntPortRightNeighbor,
       "tokIntPortManLeftLoop": tokIntPortManLeftLoop,
       "tokIntPortManRightLoop": tokIntPortManRightLoop,
       "tokIntPortAutoLeftLoop": tokIntPortAutoLeftLoop,
       "tokIntPortAutoRightLoop": tokIntPortAutoRightLoop,
       "ts": ts,
       "tsGroup": tsGroup,
       "tsGroupTable": tsGroupTable,
       "tsGroupEntry": tsGroupEntry,
       "tsGroupId": tsGroupId,
       "tsGroupLATStatus": tsGroupLATStatus,
       "tsGroupOperationMode": tsGroupOperationMode,
       "ltalk": ltalk,
       "ltalkPort": ltalkPort,
       "ltalkPortTable": ltalkPortTable,
       "ltalkPortEntry": ltalkPortEntry,
       "ltalkPortGroupId": ltalkPortGroupId,
       "ltalkPortId": ltalkPortId,
       "ltalkPortTest": ltalkPortTest,
       "ltalkPortTestResult": ltalkPortTestResult,
       "ltalkPortJam": ltalkPortJam,
       "cl": cl,
       "clGroup": clGroup,
       "clGroupTable": clGroupTable,
       "clGroupEntry": clGroupEntry,
       "clGroupId": clGroupId,
       "clGroupClockRedundancy": clGroupClockRedundancy,
       "clGroupMainClock": clGroupMainClock,
       "clGroupTestClocks": clGroupTestClocks,
       "clPort": clPort,
       "clPortTable": clPortTable,
       "clPortEntry": clPortEntry,
       "clPortGroupId": clPortGroupId,
       "clPortId": clPortId,
       "clPortFunctionalStatus": clPortFunctionalStatus,
       "bRouter": bRouter,
       "iwb": iwb,
       "iwr": iwr,
       "iwrGroupTable": iwrGroupTable,
       "iwrGroupEntry": iwrGroupEntry,
       "iwrGroupId": iwrGroupId,
       "iwrOperState": iwrOperState,
       "iwrPMState": iwrPMState,
       "iwrIOMState": iwrIOMState,
       "iwrEthernetMode": iwrEthernetMode,
       "iwrPrimaryFDDIInsert": iwrPrimaryFDDIInsert,
       "iwrSecondaryFDDIInsert": iwrSecondaryFDDIInsert,
       "iwrWANTable": iwrWANTable,
       "iwrWANEntry": iwrWANEntry,
       "iwrWANGroupId": iwrWANGroupId,
       "iwrWANPortId": iwrWANPortId,
       "iwrWANConnection": iwrWANConnection,
       "iwrWANPortCableType": iwrWANPortCableType,
       "iwrInterfaceAddrTable": iwrInterfaceAddrTable,
       "iwrInterfaceEntry": iwrInterfaceEntry,
       "iwrInterfaceGroupId": iwrInterfaceGroupId,
       "iwrInterfaceId": iwrInterfaceId,
       "iwrInterfaceAddr": iwrInterfaceAddr,
       "iwrInterfaceMask": iwrInterfaceMask,
       "iwrInterfaceMacAddress": iwrInterfaceMacAddress,
       "itr": itr,
       "itrGroupTable": itrGroupTable,
       "itrGroupEntry": itrGroupEntry,
       "itrGroupId": itrGroupId,
       "itrMainSWVersion": itrMainSWVersion,
       "itrConfigState": itrConfigState,
       "itrModuleState": itrModuleState,
       "itrLinkTable": itrLinkTable,
       "itrLinkEntry": itrLinkEntry,
       "itrLinkGroupId": itrLinkGroupId,
       "itrLinkPortId": itrLinkPortId,
       "itrLinkIf": itrLinkIf,
       "itrLinkMode": itrLinkMode,
       "itrLinkAsyncRate": itrLinkAsyncRate,
       "itrLinkSyncRate": itrLinkSyncRate,
       "itrLinkParity": itrLinkParity,
       "itrLinkParityEvenOdd": itrLinkParityEvenOdd,
       "itrLinkStopBit": itrLinkStopBit,
       "itrLinkRemoteLANConn": itrLinkRemoteLANConn,
       "itrLinkFunctionalStatus": itrLinkFunctionalStatus,
       "itrLinkAdminStatus": itrLinkAdminStatus,
       "itrLinkReset": itrLinkReset,
       "itrLinkConnectionStatus": itrLinkConnectionStatus,
       "itrLinkDataBits": itrLinkDataBits,
       "itrLinkControlSignalsMode": itrLinkControlSignalsMode,
       "itrLinkParityType": itrLinkParityType,
       "lntFddiGroup": lntFddiGroup,
       "lntFddiPort": lntFddiPort,
       "lntFddiPortTable": lntFddiPortTable,
       "lntFddiPortEntry": lntFddiPortEntry,
       "lntFddiPortGroupId": lntFddiPortGroupId,
       "lntFddiPortId": lntFddiPortId,
       "lntFddiPortMACCurrentPath": lntFddiPortMACCurrentPath,
       "lntFddiPortOpticalSwitchExist": lntFddiPortOpticalSwitchExist,
       "lntFddiPortRingConfiguration": lntFddiPortRingConfiguration,
       "lntFddiPortLineStatusA": lntFddiPortLineStatusA,
       "lntFddiPortLineStatusB": lntFddiPortLineStatusB,
       "lntFddiPortRxTotalPackets": lntFddiPortRxTotalPackets,
       "lntFddiPortRxTotalOctets": lntFddiPortRxTotalOctets,
       "lntFddiPortTxTotalPackets": lntFddiPortTxTotalPackets,
       "lntFddiPortTxTotalOctets": lntFddiPortTxTotalOctets,
       "lntFddiPortIPXtoFDDIMatching": lntFddiPortIPXtoFDDIMatching,
       "lntFddiPortFDDItoIPXMatching": lntFddiPortFDDItoIPXMatching}
)
