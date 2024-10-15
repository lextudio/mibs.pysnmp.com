# SNMP MIB module (PBC-CMTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PBC-CMTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:59 2024
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

(docsDevEvId,
 docsDevEvLevel,
 docsDevEvText) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvId",
    "docsDevEvLevel",
    "docsDevEvText")

(docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIndex) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pacificBroadband,
 pbcCaps,
 pbcManagement,
 pbcModuleRegs) = mibBuilder.importSymbols(
    "PBC-ENT-MIB",
    "pacificBroadband",
    "pbcCaps",
    "pbcManagement",
    "pbcModuleRegs")

(pbcCardIfPortIndex,) = mibBuilder.importSymbols(
    "PBC-GENERIC-MIB",
    "pbcCardIfPortIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

pbcCmtsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class TenthdB(Integer32, TextualConvention):
    status = "current"


class OneHundredthdBmVPerHz(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PbcCmts_ObjectIdentity = ObjectIdentity
pbcCmts = _PbcCmts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2)
)
_PbcCmtsIfMibExtendedObjects_ObjectIdentity = ObjectIdentity
pbcCmtsIfMibExtendedObjects = _PbcCmtsIfMibExtendedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1)
)
_PbcGeneral_ObjectIdentity = ObjectIdentity
pbcGeneral = _PbcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 1)
)
_PbcDownStreamMgmt_ObjectIdentity = ObjectIdentity
pbcDownStreamMgmt = _PbcDownStreamMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 2)
)
_PbcCmtsIfDownstreamNumEntries_Type = Unsigned32
_PbcCmtsIfDownstreamNumEntries_Object = MibScalar
pbcCmtsIfDownstreamNumEntries = _PbcCmtsIfDownstreamNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 2, 1),
    _PbcCmtsIfDownstreamNumEntries_Type()
)
pbcCmtsIfDownstreamNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfDownstreamNumEntries.setStatus("current")
_PbcCmtsIfDownstreamChannelTable_Object = MibTable
pbcCmtsIfDownstreamChannelTable = _PbcCmtsIfDownstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pbcCmtsIfDownstreamChannelTable.setStatus("current")
_PbcCmtsIfDownstreamChannelEntry_Object = MibTableRow
pbcCmtsIfDownstreamChannelEntry = _PbcCmtsIfDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 2, 2, 1)
)
pbcCmtsIfDownstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pbcCmtsIfDownstreamChannelEntry.setStatus("current")


class _PbcCmtsIfDownstreamIfTxPower_Type(Integer32):
    """Custom type pbcCmtsIfDownstreamIfTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dBmV32", 1),
          ("dBmV38", 2))
    )


_PbcCmtsIfDownstreamIfTxPower_Type.__name__ = "Integer32"
_PbcCmtsIfDownstreamIfTxPower_Object = MibTableColumn
pbcCmtsIfDownstreamIfTxPower = _PbcCmtsIfDownstreamIfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 2, 2, 1, 1),
    _PbcCmtsIfDownstreamIfTxPower_Type()
)
pbcCmtsIfDownstreamIfTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfDownstreamIfTxPower.setStatus("current")
_PbcUpStreamMgmt_ObjectIdentity = ObjectIdentity
pbcUpStreamMgmt = _PbcUpStreamMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3)
)
_PbcCmtsIfUpstreamNumEntries_Type = Unsigned32
_PbcCmtsIfUpstreamNumEntries_Object = MibScalar
pbcCmtsIfUpstreamNumEntries = _PbcCmtsIfUpstreamNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 1),
    _PbcCmtsIfUpstreamNumEntries_Type()
)
pbcCmtsIfUpstreamNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamNumEntries.setStatus("current")
_PbcCmtsIfUpstreamChannelTable_Object = MibTable
pbcCmtsIfUpstreamChannelTable = _PbcCmtsIfUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamChannelTable.setStatus("current")
_PbcCmtsIfUpstreamChannelEntry_Object = MibTableRow
pbcCmtsIfUpstreamChannelEntry = _PbcCmtsIfUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1)
)
pbcCmtsIfUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamChannelEntry.setStatus("current")
_PbcCmtsIfUpstreamPort_Type = Integer32
_PbcCmtsIfUpstreamPort_Object = MibTableColumn
pbcCmtsIfUpstreamPort = _PbcCmtsIfUpstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 1),
    _PbcCmtsIfUpstreamPort_Type()
)
pbcCmtsIfUpstreamPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamPort.setStatus("current")


class _PbcCmtsIfUpstreamOperMode_Type(Integer32):
    """Custom type pbcCmtsIfUpstreamOperMode based on Integer32"""
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
        *(("available", 1),
          ("inUse", 3),
          ("scanning", 4),
          ("standby", 2),
          ("unlicensed", 5))
    )


_PbcCmtsIfUpstreamOperMode_Type.__name__ = "Integer32"
_PbcCmtsIfUpstreamOperMode_Object = MibTableColumn
pbcCmtsIfUpstreamOperMode = _PbcCmtsIfUpstreamOperMode_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 2),
    _PbcCmtsIfUpstreamOperMode_Type()
)
pbcCmtsIfUpstreamOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamOperMode.setStatus("current")


class _PbcCmtsIfUpstreamCmdRcvdPwr_Type(TenthdBmV):
    """Custom type pbcCmtsIfUpstreamCmdRcvdPwr based on TenthdBmV"""
    defaultValue = 0


_PbcCmtsIfUpstreamCmdRcvdPwr_Object = MibTableColumn
pbcCmtsIfUpstreamCmdRcvdPwr = _PbcCmtsIfUpstreamCmdRcvdPwr_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 3),
    _PbcCmtsIfUpstreamCmdRcvdPwr_Type()
)
pbcCmtsIfUpstreamCmdRcvdPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmdRcvdPwr.setStatus("current")
_PbcCmtsIfUpstreamPowerLevel_Type = TenthdBmV
_PbcCmtsIfUpstreamPowerLevel_Object = MibTableColumn
pbcCmtsIfUpstreamPowerLevel = _PbcCmtsIfUpstreamPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 4),
    _PbcCmtsIfUpstreamPowerLevel_Type()
)
pbcCmtsIfUpstreamPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamPowerLevel.setStatus("current")
_PbcCmtsIfUpstreamMER_Type = TenthdB
_PbcCmtsIfUpstreamMER_Object = MibTableColumn
pbcCmtsIfUpstreamMER = _PbcCmtsIfUpstreamMER_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 5),
    _PbcCmtsIfUpstreamMER_Type()
)
pbcCmtsIfUpstreamMER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamMER.setStatus("current")
_PbcCmtsIfUpstreamHcsErrors_Type = Counter32
_PbcCmtsIfUpstreamHcsErrors_Object = MibTableColumn
pbcCmtsIfUpstreamHcsErrors = _PbcCmtsIfUpstreamHcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 6),
    _PbcCmtsIfUpstreamHcsErrors_Type()
)
pbcCmtsIfUpstreamHcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamHcsErrors.setStatus("current")
_PbcCmtsIfUpstreamCrcErrors_Type = Counter32
_PbcCmtsIfUpstreamCrcErrors_Object = MibTableColumn
pbcCmtsIfUpstreamCrcErrors = _PbcCmtsIfUpstreamCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 7),
    _PbcCmtsIfUpstreamCrcErrors_Type()
)
pbcCmtsIfUpstreamCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCrcErrors.setStatus("current")


class _PbcCmtsIfUpstreamCER_Type(Gauge32):
    """Custom type pbcCmtsIfUpstreamCER based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PbcCmtsIfUpstreamCER_Type.__name__ = "Gauge32"
_PbcCmtsIfUpstreamCER_Object = MibTableColumn
pbcCmtsIfUpstreamCER = _PbcCmtsIfUpstreamCER_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 8),
    _PbcCmtsIfUpstreamCER_Type()
)
pbcCmtsIfUpstreamCER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCER.setStatus("current")
_PbcCmtsIfUpstreamCmTotal_Type = Unsigned32
_PbcCmtsIfUpstreamCmTotal_Object = MibTableColumn
pbcCmtsIfUpstreamCmTotal = _PbcCmtsIfUpstreamCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 9),
    _PbcCmtsIfUpstreamCmTotal_Type()
)
pbcCmtsIfUpstreamCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmTotal.setStatus("current")
_PbcCmtsIfUpstreamCmRangeAborted_Type = Unsigned32
_PbcCmtsIfUpstreamCmRangeAborted_Object = MibTableColumn
pbcCmtsIfUpstreamCmRangeAborted = _PbcCmtsIfUpstreamCmRangeAborted_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 10),
    _PbcCmtsIfUpstreamCmRangeAborted_Type()
)
pbcCmtsIfUpstreamCmRangeAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmRangeAborted.setStatus("current")
_PbcCmtsIfUpstreamCmRanging_Type = Unsigned32
_PbcCmtsIfUpstreamCmRanging_Object = MibTableColumn
pbcCmtsIfUpstreamCmRanging = _PbcCmtsIfUpstreamCmRanging_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 11),
    _PbcCmtsIfUpstreamCmRanging_Type()
)
pbcCmtsIfUpstreamCmRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmRanging.setStatus("current")
_PbcCmtsIfUpstreamCmRangingComplete_Type = Unsigned32
_PbcCmtsIfUpstreamCmRangingComplete_Object = MibTableColumn
pbcCmtsIfUpstreamCmRangingComplete = _PbcCmtsIfUpstreamCmRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 12),
    _PbcCmtsIfUpstreamCmRangingComplete_Type()
)
pbcCmtsIfUpstreamCmRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmRangingComplete.setStatus("current")
_PbcCmtsIfUpstreamCmIpComplete_Type = Unsigned32
_PbcCmtsIfUpstreamCmIpComplete_Object = MibTableColumn
pbcCmtsIfUpstreamCmIpComplete = _PbcCmtsIfUpstreamCmIpComplete_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 13),
    _PbcCmtsIfUpstreamCmIpComplete_Type()
)
pbcCmtsIfUpstreamCmIpComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmIpComplete.setStatus("current")
_PbcCmtsIfUpstreamCmRegistered_Type = Unsigned32
_PbcCmtsIfUpstreamCmRegistered_Object = MibTableColumn
pbcCmtsIfUpstreamCmRegistered = _PbcCmtsIfUpstreamCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 14),
    _PbcCmtsIfUpstreamCmRegistered_Type()
)
pbcCmtsIfUpstreamCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmRegistered.setStatus("current")
_PbcCmtsIfUpstreamCmRogue_Type = Unsigned32
_PbcCmtsIfUpstreamCmRogue_Object = MibTableColumn
pbcCmtsIfUpstreamCmRogue = _PbcCmtsIfUpstreamCmRogue_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 3, 2, 1, 15),
    _PbcCmtsIfUpstreamCmRogue_Type()
)
pbcCmtsIfUpstreamCmRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfUpstreamCmRogue.setStatus("current")
_PbcMacMgmt_ObjectIdentity = ObjectIdentity
pbcMacMgmt = _PbcMacMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4)
)
_PbcCmtsIfMacTable_Object = MibTable
pbcCmtsIfMacTable = _PbcCmtsIfMacTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pbcCmtsIfMacTable.setStatus("current")
_PbcCmtsIfMacEntry_Object = MibTableRow
pbcCmtsIfMacEntry = _PbcCmtsIfMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1)
)
pbcCmtsIfMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pbcCmtsIfMacEntry.setStatus("current")
_PbcCmtsIfMacCmTotal_Type = Unsigned32
_PbcCmtsIfMacCmTotal_Object = MibTableColumn
pbcCmtsIfMacCmTotal = _PbcCmtsIfMacCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1, 1),
    _PbcCmtsIfMacCmTotal_Type()
)
pbcCmtsIfMacCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfMacCmTotal.setStatus("current")
_PbcCmtsIfMacCmRangeAborted_Type = Unsigned32
_PbcCmtsIfMacCmRangeAborted_Object = MibTableColumn
pbcCmtsIfMacCmRangeAborted = _PbcCmtsIfMacCmRangeAborted_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1, 2),
    _PbcCmtsIfMacCmRangeAborted_Type()
)
pbcCmtsIfMacCmRangeAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfMacCmRangeAborted.setStatus("current")
_PbcCmtsIfMacCmRanging_Type = Unsigned32
_PbcCmtsIfMacCmRanging_Object = MibTableColumn
pbcCmtsIfMacCmRanging = _PbcCmtsIfMacCmRanging_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1, 3),
    _PbcCmtsIfMacCmRanging_Type()
)
pbcCmtsIfMacCmRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfMacCmRanging.setStatus("current")
_PbcCmtsIfMacCmRangingComplete_Type = Unsigned32
_PbcCmtsIfMacCmRangingComplete_Object = MibTableColumn
pbcCmtsIfMacCmRangingComplete = _PbcCmtsIfMacCmRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1, 4),
    _PbcCmtsIfMacCmRangingComplete_Type()
)
pbcCmtsIfMacCmRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfMacCmRangingComplete.setStatus("current")
_PbcCmtsIfMacCmIpComplete_Type = Unsigned32
_PbcCmtsIfMacCmIpComplete_Object = MibTableColumn
pbcCmtsIfMacCmIpComplete = _PbcCmtsIfMacCmIpComplete_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1, 5),
    _PbcCmtsIfMacCmIpComplete_Type()
)
pbcCmtsIfMacCmIpComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfMacCmIpComplete.setStatus("current")
_PbcCmtsIfMacCmRegistered_Type = Unsigned32
_PbcCmtsIfMacCmRegistered_Object = MibTableColumn
pbcCmtsIfMacCmRegistered = _PbcCmtsIfMacCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1, 6),
    _PbcCmtsIfMacCmRegistered_Type()
)
pbcCmtsIfMacCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfMacCmRegistered.setStatus("current")
_PbcCmtsIfMacCmRogue_Type = Unsigned32
_PbcCmtsIfMacCmRogue_Object = MibTableColumn
pbcCmtsIfMacCmRogue = _PbcCmtsIfMacCmRogue_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 4, 1, 1, 7),
    _PbcCmtsIfMacCmRogue_Type()
)
pbcCmtsIfMacCmRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsIfMacCmRogue.setStatus("current")
_PbcCmtsCmMgmt_ObjectIdentity = ObjectIdentity
pbcCmtsCmMgmt = _PbcCmtsCmMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5)
)
_PbcCmtsCmStatusTable_Object = MibTable
pbcCmtsCmStatusTable = _PbcCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pbcCmtsCmStatusTable.setStatus("current")
_PbcCmtsCmStatusEntry_Object = MibTableRow
pbcCmtsCmStatusEntry = _PbcCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    pbcCmtsCmStatusEntry.setStatus("current")
_PbcCmtsCmStatusFirstOnline_Type = DateAndTime
_PbcCmtsCmStatusFirstOnline_Object = MibTableColumn
pbcCmtsCmStatusFirstOnline = _PbcCmtsCmStatusFirstOnline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 1),
    _PbcCmtsCmStatusFirstOnline_Type()
)
pbcCmtsCmStatusFirstOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusFirstOnline.setStatus("current")
_PbcCmtsCmStatusLastOnline_Type = DateAndTime
_PbcCmtsCmStatusLastOnline_Object = MibTableColumn
pbcCmtsCmStatusLastOnline = _PbcCmtsCmStatusLastOnline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 2),
    _PbcCmtsCmStatusLastOnline_Type()
)
pbcCmtsCmStatusLastOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusLastOnline.setStatus("current")
_PbcCmtsCmStatusTimesOnline_Type = Counter32
_PbcCmtsCmStatusTimesOnline_Object = MibTableColumn
pbcCmtsCmStatusTimesOnline = _PbcCmtsCmStatusTimesOnline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 3),
    _PbcCmtsCmStatusTimesOnline_Type()
)
pbcCmtsCmStatusTimesOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusTimesOnline.setStatus("current")


class _PbcCmtsCmStatusPercentOnline_Type(Unsigned32):
    """Custom type pbcCmtsCmStatusPercentOnline based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PbcCmtsCmStatusPercentOnline_Type.__name__ = "Unsigned32"
_PbcCmtsCmStatusPercentOnline_Object = MibTableColumn
pbcCmtsCmStatusPercentOnline = _PbcCmtsCmStatusPercentOnline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 4),
    _PbcCmtsCmStatusPercentOnline_Type()
)
pbcCmtsCmStatusPercentOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusPercentOnline.setStatus("current")
_PbcCmtsCmStatusMinOnline_Type = TimeInterval
_PbcCmtsCmStatusMinOnline_Object = MibTableColumn
pbcCmtsCmStatusMinOnline = _PbcCmtsCmStatusMinOnline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 5),
    _PbcCmtsCmStatusMinOnline_Type()
)
pbcCmtsCmStatusMinOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusMinOnline.setStatus("current")
_PbcCmtsCmStatusMaxOnline_Type = TimeInterval
_PbcCmtsCmStatusMaxOnline_Object = MibTableColumn
pbcCmtsCmStatusMaxOnline = _PbcCmtsCmStatusMaxOnline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 6),
    _PbcCmtsCmStatusMaxOnline_Type()
)
pbcCmtsCmStatusMaxOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusMaxOnline.setStatus("current")
_PbcCmtsCmStatusAvgOnline_Type = TimeInterval
_PbcCmtsCmStatusAvgOnline_Object = MibTableColumn
pbcCmtsCmStatusAvgOnline = _PbcCmtsCmStatusAvgOnline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 7),
    _PbcCmtsCmStatusAvgOnline_Type()
)
pbcCmtsCmStatusAvgOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusAvgOnline.setStatus("current")
_PbcCmtsCmStatusMinOffline_Type = TimeInterval
_PbcCmtsCmStatusMinOffline_Object = MibTableColumn
pbcCmtsCmStatusMinOffline = _PbcCmtsCmStatusMinOffline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 8),
    _PbcCmtsCmStatusMinOffline_Type()
)
pbcCmtsCmStatusMinOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusMinOffline.setStatus("current")
_PbcCmtsCmStatusMaxOffline_Type = TimeInterval
_PbcCmtsCmStatusMaxOffline_Object = MibTableColumn
pbcCmtsCmStatusMaxOffline = _PbcCmtsCmStatusMaxOffline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 9),
    _PbcCmtsCmStatusMaxOffline_Type()
)
pbcCmtsCmStatusMaxOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusMaxOffline.setStatus("current")
_PbcCmtsCmStatusAvgOffline_Type = TimeInterval
_PbcCmtsCmStatusAvgOffline_Object = MibTableColumn
pbcCmtsCmStatusAvgOffline = _PbcCmtsCmStatusAvgOffline_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 1, 1, 10),
    _PbcCmtsCmStatusAvgOffline_Type()
)
pbcCmtsCmStatusAvgOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsCmStatusAvgOffline.setStatus("current")
_PbcCmtsRogueCmTable_Object = MibTable
pbcCmtsRogueCmTable = _PbcCmtsRogueCmTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    pbcCmtsRogueCmTable.setStatus("current")
_PbcCmtsRogueCmEntry_Object = MibTableRow
pbcCmtsRogueCmEntry = _PbcCmtsRogueCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2, 1)
)
pbcCmtsRogueCmEntry.setIndexNames(
    (0, "PBC-CMTS-MIB", "pbcCmtsRogueCmMacAddress"),
)
if mibBuilder.loadTexts:
    pbcCmtsRogueCmEntry.setStatus("current")
_PbcCmtsRogueCmMacAddress_Type = MacAddress
_PbcCmtsRogueCmMacAddress_Object = MibTableColumn
pbcCmtsRogueCmMacAddress = _PbcCmtsRogueCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2, 1, 1),
    _PbcCmtsRogueCmMacAddress_Type()
)
pbcCmtsRogueCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsRogueCmMacAddress.setStatus("current")
_PbcCmtsRogueCmIpAddress_Type = IpAddress
_PbcCmtsRogueCmIpAddress_Object = MibTableColumn
pbcCmtsRogueCmIpAddress = _PbcCmtsRogueCmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2, 1, 2),
    _PbcCmtsRogueCmIpAddress_Type()
)
pbcCmtsRogueCmIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsRogueCmIpAddress.setStatus("current")
_PbcCmtsRogueCmPtr_Type = Integer32
_PbcCmtsRogueCmPtr_Object = MibTableColumn
pbcCmtsRogueCmPtr = _PbcCmtsRogueCmPtr_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2, 1, 3),
    _PbcCmtsRogueCmPtr_Type()
)
pbcCmtsRogueCmPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsRogueCmPtr.setStatus("current")


class _PbcCmtsRogueCmType_Type(Integer32):
    """Custom type pbcCmtsRogueCmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 3),
          ("rigged", 2),
          ("unProvisioned", 1))
    )


_PbcCmtsRogueCmType_Type.__name__ = "Integer32"
_PbcCmtsRogueCmType_Object = MibTableColumn
pbcCmtsRogueCmType = _PbcCmtsRogueCmType_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2, 1, 4),
    _PbcCmtsRogueCmType_Type()
)
pbcCmtsRogueCmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsRogueCmType.setStatus("current")
_PbcCmtsRogueCmFirstActive_Type = DateAndTime
_PbcCmtsRogueCmFirstActive_Object = MibTableColumn
pbcCmtsRogueCmFirstActive = _PbcCmtsRogueCmFirstActive_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2, 1, 5),
    _PbcCmtsRogueCmFirstActive_Type()
)
pbcCmtsRogueCmFirstActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsRogueCmFirstActive.setStatus("current")
_PbcCmtsRogueCmLastActive_Type = DateAndTime
_PbcCmtsRogueCmLastActive_Object = MibTableColumn
pbcCmtsRogueCmLastActive = _PbcCmtsRogueCmLastActive_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 1, 5, 2, 1, 6),
    _PbcCmtsRogueCmLastActive_Type()
)
pbcCmtsRogueCmLastActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsRogueCmLastActive.setStatus("current")
_PbcCmtsCableSpectrumManagement_ObjectIdentity = ObjectIdentity
pbcCmtsCableSpectrumManagement = _PbcCmtsCableSpectrumManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2)
)
_PbcCmtsSpectrumAnalysisMgmt_ObjectIdentity = ObjectIdentity
pbcCmtsSpectrumAnalysisMgmt = _PbcCmtsSpectrumAnalysisMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2)
)
_PbcCmtsSpectrumAnalysisObjects_ObjectIdentity = ObjectIdentity
pbcCmtsSpectrumAnalysisObjects = _PbcCmtsSpectrumAnalysisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1)
)
_PbcSpectrumAnalysisRFInputTable_Object = MibTable
pbcSpectrumAnalysisRFInputTable = _PbcSpectrumAnalysisRFInputTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisRFInputTable.setStatus("current")
_PbcSpectrumAnalysisRFInputEntry_Object = MibTableRow
pbcSpectrumAnalysisRFInputEntry = _PbcSpectrumAnalysisRFInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1)
)
pbcSpectrumAnalysisRFInputEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"),
)
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisRFInputEntry.setStatus("current")


class _PbcSpectrumAnalysisEnable_Type(TruthValue):
    """Custom type pbcSpectrumAnalysisEnable based on TruthValue"""


_PbcSpectrumAnalysisEnable_Object = MibTableColumn
pbcSpectrumAnalysisEnable = _PbcSpectrumAnalysisEnable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 1),
    _PbcSpectrumAnalysisEnable_Type()
)
pbcSpectrumAnalysisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisEnable.setStatus("current")


class _PbcSpectrumAnalysisCmdStatus_Type(Integer32):
    """Custom type pbcSpectrumAnalysisCmdStatus based on Integer32"""
    defaultValue = 1

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
        *(("available", 1),
          ("complete", 3),
          ("generalFailure", 4),
          ("noResources", 5),
          ("scanInProgress", 2))
    )


_PbcSpectrumAnalysisCmdStatus_Type.__name__ = "Integer32"
_PbcSpectrumAnalysisCmdStatus_Object = MibTableColumn
pbcSpectrumAnalysisCmdStatus = _PbcSpectrumAnalysisCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 2),
    _PbcSpectrumAnalysisCmdStatus_Type()
)
pbcSpectrumAnalysisCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisCmdStatus.setStatus("current")


class _PbcSpectrumAnalysisIntegrationLen_Type(Unsigned32):
    """Custom type pbcSpectrumAnalysisIntegrationLen based on Unsigned32"""
    defaultValue = 1


_PbcSpectrumAnalysisIntegrationLen_Object = MibTableColumn
pbcSpectrumAnalysisIntegrationLen = _PbcSpectrumAnalysisIntegrationLen_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 3),
    _PbcSpectrumAnalysisIntegrationLen_Type()
)
pbcSpectrumAnalysisIntegrationLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisIntegrationLen.setStatus("current")


class _PbcSpectrumAnalysisFreqStep_Type(Integer32):
    """Custom type pbcSpectrumAnalysisFreqStep based on Integer32"""
    defaultValue = 4

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
        *(("kHz160", 4),
          ("kHz20", 1),
          ("kHz40", 2),
          ("kHz80", 3))
    )


_PbcSpectrumAnalysisFreqStep_Type.__name__ = "Integer32"
_PbcSpectrumAnalysisFreqStep_Object = MibTableColumn
pbcSpectrumAnalysisFreqStep = _PbcSpectrumAnalysisFreqStep_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 4),
    _PbcSpectrumAnalysisFreqStep_Type()
)
pbcSpectrumAnalysisFreqStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisFreqStep.setStatus("current")


class _PbcSpectrumAnalysisFreqMin_Type(Unsigned32):
    """Custom type pbcSpectrumAnalysisFreqMin based on Unsigned32"""
    defaultValue = 5000000


_PbcSpectrumAnalysisFreqMin_Object = MibTableColumn
pbcSpectrumAnalysisFreqMin = _PbcSpectrumAnalysisFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 5),
    _PbcSpectrumAnalysisFreqMin_Type()
)
pbcSpectrumAnalysisFreqMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisFreqMin.setStatus("current")


class _PbcSpectrumAnalysisFreqMax_Type(Unsigned32):
    """Custom type pbcSpectrumAnalysisFreqMax based on Unsigned32"""
    defaultValue = 42000000


_PbcSpectrumAnalysisFreqMax_Object = MibTableColumn
pbcSpectrumAnalysisFreqMax = _PbcSpectrumAnalysisFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 6),
    _PbcSpectrumAnalysisFreqMax_Type()
)
pbcSpectrumAnalysisFreqMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisFreqMax.setStatus("current")


class _PbcSpectrumAnalysisArraySize_Type(Unsigned32):
    """Custom type pbcSpectrumAnalysisArraySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_PbcSpectrumAnalysisArraySize_Type.__name__ = "Unsigned32"
_PbcSpectrumAnalysisArraySize_Object = MibTableColumn
pbcSpectrumAnalysisArraySize = _PbcSpectrumAnalysisArraySize_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 7),
    _PbcSpectrumAnalysisArraySize_Type()
)
pbcSpectrumAnalysisArraySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArraySize.setStatus("current")


class _PbcSpectrumAnalysisActiveArray_Type(Unsigned32):
    """Custom type pbcSpectrumAnalysisActiveArray based on Unsigned32"""
    defaultValue = 0


_PbcSpectrumAnalysisActiveArray_Object = MibTableColumn
pbcSpectrumAnalysisActiveArray = _PbcSpectrumAnalysisActiveArray_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 1, 1, 8),
    _PbcSpectrumAnalysisActiveArray_Type()
)
pbcSpectrumAnalysisActiveArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisActiveArray.setStatus("current")
_PbcSpectrumAnalysisArrayIndexTable_Object = MibTable
pbcSpectrumAnalysisArrayIndexTable = _PbcSpectrumAnalysisArrayIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayIndexTable.setStatus("current")
_PbcSpectrumAnalysisArrayIndexEntry_Object = MibTableRow
pbcSpectrumAnalysisArrayIndexEntry = _PbcSpectrumAnalysisArrayIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 2, 1)
)
pbcSpectrumAnalysisArrayIndexEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"),
    (0, "PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayIndex"),
)
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayIndexEntry.setStatus("current")
_PbcSpectrumAnalysisArrayIndex_Type = Unsigned32
_PbcSpectrumAnalysisArrayIndex_Object = MibTableColumn
pbcSpectrumAnalysisArrayIndex = _PbcSpectrumAnalysisArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 2, 1, 1),
    _PbcSpectrumAnalysisArrayIndex_Type()
)
pbcSpectrumAnalysisArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayIndex.setStatus("current")


class _PbcSpectrumAnalysisArrayStatus_Type(Integer32):
    """Custom type pbcSpectrumAnalysisArrayStatus based on Integer32"""
    defaultValue = 1

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
        *(("abort", 4),
          ("available", 1),
          ("scanComplete", 3),
          ("scanning", 2))
    )


_PbcSpectrumAnalysisArrayStatus_Type.__name__ = "Integer32"
_PbcSpectrumAnalysisArrayStatus_Object = MibTableColumn
pbcSpectrumAnalysisArrayStatus = _PbcSpectrumAnalysisArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 2, 1, 2),
    _PbcSpectrumAnalysisArrayStatus_Type()
)
pbcSpectrumAnalysisArrayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayStatus.setStatus("current")
_PbcSpectrumAnalysisArrayScanStart_Type = DateAndTime
_PbcSpectrumAnalysisArrayScanStart_Object = MibTableColumn
pbcSpectrumAnalysisArrayScanStart = _PbcSpectrumAnalysisArrayScanStart_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 2, 1, 3),
    _PbcSpectrumAnalysisArrayScanStart_Type()
)
pbcSpectrumAnalysisArrayScanStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayScanStart.setStatus("current")
_PbcSpectrumAnalysisArrayScanStop_Type = DateAndTime
_PbcSpectrumAnalysisArrayScanStop_Object = MibTableColumn
pbcSpectrumAnalysisArrayScanStop = _PbcSpectrumAnalysisArrayScanStop_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 2, 1, 4),
    _PbcSpectrumAnalysisArrayScanStop_Type()
)
pbcSpectrumAnalysisArrayScanStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayScanStop.setStatus("current")
_PbcSpectrumAnalysisDataTable_Object = MibTable
pbcSpectrumAnalysisDataTable = _PbcSpectrumAnalysisDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisDataTable.setStatus("current")
_PbcSpectrumAnalysisDataEntry_Object = MibTableRow
pbcSpectrumAnalysisDataEntry = _PbcSpectrumAnalysisDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 3, 1)
)
pbcSpectrumAnalysisDataEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"),
    (0, "PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayIndex"),
    (0, "PBC-CMTS-MIB", "pbcSpectrumAnalysisFrequency"),
)
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisDataEntry.setStatus("current")
_PbcSpectrumAnalysisFrequency_Type = Unsigned32
_PbcSpectrumAnalysisFrequency_Object = MibTableColumn
pbcSpectrumAnalysisFrequency = _PbcSpectrumAnalysisFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 3, 1, 1),
    _PbcSpectrumAnalysisFrequency_Type()
)
pbcSpectrumAnalysisFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisFrequency.setStatus("current")
_PbcSpectrumAnalysisPower_Type = OneHundredthdBmVPerHz
_PbcSpectrumAnalysisPower_Object = MibTableColumn
pbcSpectrumAnalysisPower = _PbcSpectrumAnalysisPower_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 1, 3, 1, 2),
    _PbcSpectrumAnalysisPower_Type()
)
pbcSpectrumAnalysisPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisPower.setStatus("current")
_PbcCmtsSpectrumAnalysisNotificationEnables_ObjectIdentity = ObjectIdentity
pbcCmtsSpectrumAnalysisNotificationEnables = _PbcCmtsSpectrumAnalysisNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 2)
)
_PbcCmtsSpectrumAnalysisNotificationTable_Object = MibTable
pbcCmtsSpectrumAnalysisNotificationTable = _PbcCmtsSpectrumAnalysisNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pbcCmtsSpectrumAnalysisNotificationTable.setStatus("current")
_PbcCmtsSpectrumAnalysisNotificationEntry_Object = MibTableRow
pbcCmtsSpectrumAnalysisNotificationEntry = _PbcCmtsSpectrumAnalysisNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 2, 1, 1)
)
pbcCmtsSpectrumAnalysisNotificationEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"),
)
if mibBuilder.loadTexts:
    pbcCmtsSpectrumAnalysisNotificationEntry.setStatus("current")


class _PbcCmtsSpectrumAnalysisEnableSweepNotification_Type(TruthValue):
    """Custom type pbcCmtsSpectrumAnalysisEnableSweepNotification based on TruthValue"""


_PbcCmtsSpectrumAnalysisEnableSweepNotification_Object = MibTableColumn
pbcCmtsSpectrumAnalysisEnableSweepNotification = _PbcCmtsSpectrumAnalysisEnableSweepNotification_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 2, 1, 1, 1),
    _PbcCmtsSpectrumAnalysisEnableSweepNotification_Type()
)
pbcCmtsSpectrumAnalysisEnableSweepNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsSpectrumAnalysisEnableSweepNotification.setStatus("current")
_PbcSweepNotificationRecipient_Type = IpAddress
_PbcSweepNotificationRecipient_Object = MibTableColumn
pbcSweepNotificationRecipient = _PbcSweepNotificationRecipient_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 2, 1, 1, 2),
    _PbcSweepNotificationRecipient_Type()
)
pbcSweepNotificationRecipient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSweepNotificationRecipient.setStatus("current")


class _PbcSweepNotificationRecipientPort_Type(Integer32):
    """Custom type pbcSweepNotificationRecipientPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PbcSweepNotificationRecipientPort_Type.__name__ = "Integer32"
_PbcSweepNotificationRecipientPort_Object = MibTableColumn
pbcSweepNotificationRecipientPort = _PbcSweepNotificationRecipientPort_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 2, 1, 1, 3),
    _PbcSweepNotificationRecipientPort_Type()
)
pbcSweepNotificationRecipientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcSweepNotificationRecipientPort.setStatus("current")


class _PbcCmtsSpectrumAnalysisNotificationType_Type(Integer32):
    """Custom type pbcCmtsSpectrumAnalysisNotificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv2c", 1),
          ("snmpv3", 2))
    )


_PbcCmtsSpectrumAnalysisNotificationType_Type.__name__ = "Integer32"
_PbcCmtsSpectrumAnalysisNotificationType_Object = MibTableColumn
pbcCmtsSpectrumAnalysisNotificationType = _PbcCmtsSpectrumAnalysisNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 2, 1, 1, 4),
    _PbcCmtsSpectrumAnalysisNotificationType_Type()
)
pbcCmtsSpectrumAnalysisNotificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsSpectrumAnalysisNotificationType.setStatus("current")
_PbcCmtsSpectrumAnalysisNotificationPrefix_ObjectIdentity = ObjectIdentity
pbcCmtsSpectrumAnalysisNotificationPrefix = _PbcCmtsSpectrumAnalysisNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 3)
)
_PbcCmtsSpectrumAnalysisNotifications_ObjectIdentity = ObjectIdentity
pbcCmtsSpectrumAnalysisNotifications = _PbcCmtsSpectrumAnalysisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 3, 1)
)
_PbcCardIfPortIndexID_Type = Integer32
_PbcCardIfPortIndexID_Object = MibScalar
pbcCardIfPortIndexID = _PbcCardIfPortIndexID_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 3, 1, 2),
    _PbcCardIfPortIndexID_Type()
)
pbcCardIfPortIndexID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pbcCardIfPortIndexID.setStatus("current")
_PbcSpectrumAnalysisArrayIndexID_Type = Integer32
_PbcSpectrumAnalysisArrayIndexID_Object = MibScalar
pbcSpectrumAnalysisArrayIndexID = _PbcSpectrumAnalysisArrayIndexID_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 3, 1, 3),
    _PbcSpectrumAnalysisArrayIndexID_Type()
)
pbcSpectrumAnalysisArrayIndexID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayIndexID.setStatus("current")
_PbcSpectrumAnalysisArrayStatusID_Type = Integer32
_PbcSpectrumAnalysisArrayStatusID_Object = MibScalar
pbcSpectrumAnalysisArrayStatusID = _PbcSpectrumAnalysisArrayStatusID_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 3, 1, 4),
    _PbcSpectrumAnalysisArrayStatusID_Type()
)
pbcSpectrumAnalysisArrayStatusID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pbcSpectrumAnalysisArrayStatusID.setStatus("current")
_PbcCmtsNotificationManagement_ObjectIdentity = ObjectIdentity
pbcCmtsNotificationManagement = _PbcCmtsNotificationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3)
)


class _PbcCmtsEventsEnable_Type(TruthValue):
    """Custom type pbcCmtsEventsEnable based on TruthValue"""


_PbcCmtsEventsEnable_Object = MibScalar
pbcCmtsEventsEnable = _PbcCmtsEventsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 1),
    _PbcCmtsEventsEnable_Type()
)
pbcCmtsEventsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsEventsEnable.setStatus("current")


class _PbcCmtsNotificationsControl_Type(Bits):
    """Custom type pbcCmtsNotificationsControl based on Bits"""
    namedValues = NamedValues(
        *(("access", 3),
          ("chassis", 1),
          ("cmStateChange", 9),
          ("config", 4),
          ("dataPath", 5),
          ("debug", 8),
          ("envMon", 0),
          ("flapList", 7),
          ("rfInterface", 6),
          ("software", 2))
    )

_PbcCmtsNotificationsControl_Type.__name__ = "Bits"
_PbcCmtsNotificationsControl_Object = MibScalar
pbcCmtsNotificationsControl = _PbcCmtsNotificationsControl_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 2),
    _PbcCmtsNotificationsControl_Type()
)
pbcCmtsNotificationsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsNotificationsControl.setStatus("current")
_PbcCmtsSystemNotifications_ObjectIdentity = ObjectIdentity
pbcCmtsSystemNotifications = _PbcCmtsSystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3)
)


class _PbcCmtsModemEventsEnable_Type(Bits):
    """Custom type pbcCmtsModemEventsEnable based on Bits"""
    namedValues = NamedValues(
        *(("deRanging", 0),
          ("registration", 1))
    )

_PbcCmtsModemEventsEnable_Type.__name__ = "Bits"
_PbcCmtsModemEventsEnable_Object = MibScalar
pbcCmtsModemEventsEnable = _PbcCmtsModemEventsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 4),
    _PbcCmtsModemEventsEnable_Type()
)
pbcCmtsModemEventsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsModemEventsEnable.setStatus("current")
_PbcCmtsConformance_ObjectIdentity = ObjectIdentity
pbcCmtsConformance = _PbcCmtsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4)
)
_PbcCmtsGroups_ObjectIdentity = ObjectIdentity
pbcCmtsGroups = _PbcCmtsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 1)
)
_PbcCmtsCompliances_ObjectIdentity = ObjectIdentity
pbcCmtsCompliances = _PbcCmtsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 2)
)
_PbcFlapListManagement_ObjectIdentity = ObjectIdentity
pbcFlapListManagement = _PbcFlapListManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5)
)
_PbcFlapListObjects_ObjectIdentity = ObjectIdentity
pbcFlapListObjects = _PbcFlapListObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1)
)


class _PbcCmtsFlapListAgeMinutes_Type(Unsigned32):
    """Custom type pbcCmtsFlapListAgeMinutes based on Unsigned32"""
    defaultValue = 1440

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_PbcCmtsFlapListAgeMinutes_Type.__name__ = "Unsigned32"
_PbcCmtsFlapListAgeMinutes_Object = MibScalar
pbcCmtsFlapListAgeMinutes = _PbcCmtsFlapListAgeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 1),
    _PbcCmtsFlapListAgeMinutes_Type()
)
pbcCmtsFlapListAgeMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListAgeMinutes.setStatus("current")


class _PbcCmtsFlapListIMRetryInterval_Type(Unsigned32):
    """Custom type pbcCmtsFlapListIMRetryInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_PbcCmtsFlapListIMRetryInterval_Type.__name__ = "Unsigned32"
_PbcCmtsFlapListIMRetryInterval_Object = MibScalar
pbcCmtsFlapListIMRetryInterval = _PbcCmtsFlapListIMRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 2),
    _PbcCmtsFlapListIMRetryInterval_Type()
)
pbcCmtsFlapListIMRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListIMRetryInterval.setStatus("current")


class _PbcCmtsFlapListCERThreshold_Type(Unsigned32):
    """Custom type pbcCmtsFlapListCERThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_PbcCmtsFlapListCERThreshold_Type.__name__ = "Unsigned32"
_PbcCmtsFlapListCERThreshold_Object = MibScalar
pbcCmtsFlapListCERThreshold = _PbcCmtsFlapListCERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 3),
    _PbcCmtsFlapListCERThreshold_Type()
)
pbcCmtsFlapListCERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListCERThreshold.setStatus("current")


class _PbcCmtsFlapListMERThreshold_Type(TenthdB):
    """Custom type pbcCmtsFlapListMERThreshold based on TenthdB"""
    defaultValue = 180

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcCmtsFlapListMERThreshold_Type.__name__ = "TenthdB"
_PbcCmtsFlapListMERThreshold_Object = MibScalar
pbcCmtsFlapListMERThreshold = _PbcCmtsFlapListMERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 4),
    _PbcCmtsFlapListMERThreshold_Type()
)
pbcCmtsFlapListMERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListMERThreshold.setStatus("current")


class _PbcCmtsFlapListQPSKSNRThreshold_Type(TenthdB):
    """Custom type pbcCmtsFlapListQPSKSNRThreshold based on TenthdB"""
    defaultValue = 180

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcCmtsFlapListQPSKSNRThreshold_Type.__name__ = "TenthdB"
_PbcCmtsFlapListQPSKSNRThreshold_Object = MibScalar
pbcCmtsFlapListQPSKSNRThreshold = _PbcCmtsFlapListQPSKSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 5),
    _PbcCmtsFlapListQPSKSNRThreshold_Type()
)
pbcCmtsFlapListQPSKSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListQPSKSNRThreshold.setStatus("current")


class _PbcCmtsFlapListQAM16SNRThreshold_Type(TenthdB):
    """Custom type pbcCmtsFlapListQAM16SNRThreshold based on TenthdB"""
    defaultValue = 180

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcCmtsFlapListQAM16SNRThreshold_Type.__name__ = "TenthdB"
_PbcCmtsFlapListQAM16SNRThreshold_Object = MibScalar
pbcCmtsFlapListQAM16SNRThreshold = _PbcCmtsFlapListQAM16SNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 6),
    _PbcCmtsFlapListQAM16SNRThreshold_Type()
)
pbcCmtsFlapListQAM16SNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListQAM16SNRThreshold.setStatus("current")


class _PbcCmtsFlapListPowerAdjustThreshold_Type(TenthdB):
    """Custom type pbcCmtsFlapListPowerAdjustThreshold based on TenthdB"""
    defaultValue = 30

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcCmtsFlapListPowerAdjustThreshold_Type.__name__ = "TenthdB"
_PbcCmtsFlapListPowerAdjustThreshold_Object = MibScalar
pbcCmtsFlapListPowerAdjustThreshold = _PbcCmtsFlapListPowerAdjustThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 7),
    _PbcCmtsFlapListPowerAdjustThreshold_Type()
)
pbcCmtsFlapListPowerAdjustThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListPowerAdjustThreshold.setStatus("current")


class _PbcCmtsFlapListSMMissThreshold_Type(Unsigned32):
    """Custom type pbcCmtsFlapListSMMissThreshold based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PbcCmtsFlapListSMMissThreshold_Type.__name__ = "Unsigned32"
_PbcCmtsFlapListSMMissThreshold_Object = MibScalar
pbcCmtsFlapListSMMissThreshold = _PbcCmtsFlapListSMMissThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 8),
    _PbcCmtsFlapListSMMissThreshold_Type()
)
pbcCmtsFlapListSMMissThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListSMMissThreshold.setStatus("current")


class _PbcCmtsFlapListFreqThreshold_Type(Unsigned32):
    """Custom type pbcCmtsFlapListFreqThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_PbcCmtsFlapListFreqThreshold_Type.__name__ = "Unsigned32"
_PbcCmtsFlapListFreqThreshold_Object = MibScalar
pbcCmtsFlapListFreqThreshold = _PbcCmtsFlapListFreqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 9),
    _PbcCmtsFlapListFreqThreshold_Type()
)
pbcCmtsFlapListFreqThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListFreqThreshold.setStatus("current")


class _PbcCmtsFlapListSize_Type(Unsigned32):
    """Custom type pbcCmtsFlapListSize based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_PbcCmtsFlapListSize_Type.__name__ = "Unsigned32"
_PbcCmtsFlapListSize_Object = MibScalar
pbcCmtsFlapListSize = _PbcCmtsFlapListSize_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 10),
    _PbcCmtsFlapListSize_Type()
)
pbcCmtsFlapListSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListSize.setStatus("current")
_PbcUsFlapListControlTable_Object = MibTable
pbcUsFlapListControlTable = _PbcUsFlapListControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11)
)
if mibBuilder.loadTexts:
    pbcUsFlapListControlTable.setStatus("current")
_PbcUsFlapListControlEntry_Object = MibTableRow
pbcUsFlapListControlEntry = _PbcUsFlapListControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1)
)
pbcUsFlapListControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pbcUsFlapListControlEntry.setStatus("current")


class _PbcUsFlapListControlIMRetryInterval_Type(Unsigned32):
    """Custom type pbcUsFlapListControlIMRetryInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_PbcUsFlapListControlIMRetryInterval_Type.__name__ = "Unsigned32"
_PbcUsFlapListControlIMRetryInterval_Object = MibTableColumn
pbcUsFlapListControlIMRetryInterval = _PbcUsFlapListControlIMRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 1),
    _PbcUsFlapListControlIMRetryInterval_Type()
)
pbcUsFlapListControlIMRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlIMRetryInterval.setStatus("current")


class _PbcUsFlapListControlCERThreshold_Type(Unsigned32):
    """Custom type pbcUsFlapListControlCERThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_PbcUsFlapListControlCERThreshold_Type.__name__ = "Unsigned32"
_PbcUsFlapListControlCERThreshold_Object = MibTableColumn
pbcUsFlapListControlCERThreshold = _PbcUsFlapListControlCERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 2),
    _PbcUsFlapListControlCERThreshold_Type()
)
pbcUsFlapListControlCERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlCERThreshold.setStatus("current")


class _PbcUsFlapListControlMERThreshold_Type(TenthdB):
    """Custom type pbcUsFlapListControlMERThreshold based on TenthdB"""
    defaultValue = 180

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcUsFlapListControlMERThreshold_Type.__name__ = "TenthdB"
_PbcUsFlapListControlMERThreshold_Object = MibTableColumn
pbcUsFlapListControlMERThreshold = _PbcUsFlapListControlMERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 3),
    _PbcUsFlapListControlMERThreshold_Type()
)
pbcUsFlapListControlMERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlMERThreshold.setStatus("current")


class _PbcUsFlapListControlQPSKSNRThreshold_Type(TenthdB):
    """Custom type pbcUsFlapListControlQPSKSNRThreshold based on TenthdB"""
    defaultValue = 180

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcUsFlapListControlQPSKSNRThreshold_Type.__name__ = "TenthdB"
_PbcUsFlapListControlQPSKSNRThreshold_Object = MibTableColumn
pbcUsFlapListControlQPSKSNRThreshold = _PbcUsFlapListControlQPSKSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 4),
    _PbcUsFlapListControlQPSKSNRThreshold_Type()
)
pbcUsFlapListControlQPSKSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlQPSKSNRThreshold.setStatus("current")


class _PbcUsFlapListControlQAM16SNRThreshold_Type(TenthdB):
    """Custom type pbcUsFlapListControlQAM16SNRThreshold based on TenthdB"""
    defaultValue = 180

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcUsFlapListControlQAM16SNRThreshold_Type.__name__ = "TenthdB"
_PbcUsFlapListControlQAM16SNRThreshold_Object = MibTableColumn
pbcUsFlapListControlQAM16SNRThreshold = _PbcUsFlapListControlQAM16SNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 5),
    _PbcUsFlapListControlQAM16SNRThreshold_Type()
)
pbcUsFlapListControlQAM16SNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlQAM16SNRThreshold.setStatus("current")


class _PbcUsFlapListControlPowerAdjustThreshold_Type(TenthdB):
    """Custom type pbcUsFlapListControlPowerAdjustThreshold based on TenthdB"""
    defaultValue = 30

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PbcUsFlapListControlPowerAdjustThreshold_Type.__name__ = "TenthdB"
_PbcUsFlapListControlPowerAdjustThreshold_Object = MibTableColumn
pbcUsFlapListControlPowerAdjustThreshold = _PbcUsFlapListControlPowerAdjustThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 6),
    _PbcUsFlapListControlPowerAdjustThreshold_Type()
)
pbcUsFlapListControlPowerAdjustThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlPowerAdjustThreshold.setStatus("current")


class _PbcUsFlapListControlSMMissThreshold_Type(Unsigned32):
    """Custom type pbcUsFlapListControlSMMissThreshold based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PbcUsFlapListControlSMMissThreshold_Type.__name__ = "Unsigned32"
_PbcUsFlapListControlSMMissThreshold_Object = MibTableColumn
pbcUsFlapListControlSMMissThreshold = _PbcUsFlapListControlSMMissThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 7),
    _PbcUsFlapListControlSMMissThreshold_Type()
)
pbcUsFlapListControlSMMissThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlSMMissThreshold.setStatus("current")


class _PbcUsFlapListControlFreqThreshold_Type(Unsigned32):
    """Custom type pbcUsFlapListControlFreqThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_PbcUsFlapListControlFreqThreshold_Type.__name__ = "Unsigned32"
_PbcUsFlapListControlFreqThreshold_Object = MibTableColumn
pbcUsFlapListControlFreqThreshold = _PbcUsFlapListControlFreqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 11, 1, 8),
    _PbcUsFlapListControlFreqThreshold_Type()
)
pbcUsFlapListControlFreqThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcUsFlapListControlFreqThreshold.setStatus("current")
_PbcCmtsFlapListTable_Object = MibTable
pbcCmtsFlapListTable = _PbcCmtsFlapListTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12)
)
if mibBuilder.loadTexts:
    pbcCmtsFlapListTable.setStatus("current")
_PbcCmtsFlapListEntry_Object = MibTableRow
pbcCmtsFlapListEntry = _PbcCmtsFlapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12, 1)
)
pbcCmtsFlapListEntry.setIndexNames(
    (0, "PBC-CMTS-MIB", "pbcCmtsFlapListMacAddr"),
)
if mibBuilder.loadTexts:
    pbcCmtsFlapListEntry.setStatus("current")
_PbcCmtsFlapListMacAddr_Type = MacAddress
_PbcCmtsFlapListMacAddr_Object = MibTableColumn
pbcCmtsFlapListMacAddr = _PbcCmtsFlapListMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12, 1, 1),
    _PbcCmtsFlapListMacAddr_Type()
)
pbcCmtsFlapListMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsFlapListMacAddr.setStatus("current")
_PbcCmtsFlapListUpstreamIfIndex_Type = InterfaceIndex
_PbcCmtsFlapListUpstreamIfIndex_Object = MibTableColumn
pbcCmtsFlapListUpstreamIfIndex = _PbcCmtsFlapListUpstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12, 1, 2),
    _PbcCmtsFlapListUpstreamIfIndex_Type()
)
pbcCmtsFlapListUpstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsFlapListUpstreamIfIndex.setStatus("current")
_PbcCmtsFlapListDownstreamIfIndex_Type = InterfaceIndex
_PbcCmtsFlapListDownstreamIfIndex_Object = MibTableColumn
pbcCmtsFlapListDownstreamIfIndex = _PbcCmtsFlapListDownstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12, 1, 3),
    _PbcCmtsFlapListDownstreamIfIndex_Type()
)
pbcCmtsFlapListDownstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsFlapListDownstreamIfIndex.setStatus("current")
_PbcCmtsFlapListFlapCount_Type = Counter32
_PbcCmtsFlapListFlapCount_Object = MibTableColumn
pbcCmtsFlapListFlapCount = _PbcCmtsFlapListFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12, 1, 4),
    _PbcCmtsFlapListFlapCount_Type()
)
pbcCmtsFlapListFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsFlapListFlapCount.setStatus("current")


class _PbcCmtsFlapListFlapCause_Type(Integer32):
    """Custom type pbcCmtsFlapListFlapCause based on Integer32"""
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
        *(("cer", 2),
          ("freqDrift", 8),
          ("imRetry", 1),
          ("mer", 3),
          ("powerAdjust", 6),
          ("smMiss", 7),
          ("snrQam16", 5),
          ("snrQpsk", 4))
    )


_PbcCmtsFlapListFlapCause_Type.__name__ = "Integer32"
_PbcCmtsFlapListFlapCause_Object = MibTableColumn
pbcCmtsFlapListFlapCause = _PbcCmtsFlapListFlapCause_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12, 1, 5),
    _PbcCmtsFlapListFlapCause_Type()
)
pbcCmtsFlapListFlapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsFlapListFlapCause.setStatus("current")
_PbcCmtsFlapListFreqDrift_Type = Unsigned32
_PbcCmtsFlapListFreqDrift_Object = MibTableColumn
pbcCmtsFlapListFreqDrift = _PbcCmtsFlapListFreqDrift_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 12, 1, 6),
    _PbcCmtsFlapListFreqDrift_Type()
)
pbcCmtsFlapListFreqDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcCmtsFlapListFreqDrift.setStatus("current")
_PbcCmtsFlapListEventsEnable_Type = TruthValue
_PbcCmtsFlapListEventsEnable_Object = MibScalar
pbcCmtsFlapListEventsEnable = _PbcCmtsFlapListEventsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 5, 1, 13),
    _PbcCmtsFlapListEventsEnable_Type()
)
pbcCmtsFlapListEventsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcCmtsFlapListEventsEnable.setStatus("current")
_PbcG10CMTS_ObjectIdentity = ObjectIdentity
pbcG10CMTS = _PbcG10CMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 1001)
)
_PbcG1CMTS_ObjectIdentity = ObjectIdentity
pbcG1CMTS = _PbcG1CMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 1002)
)
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("PBC-CMTS-MIB",
     "pbcCmtsCmStatusEntry")
)
pbcCmtsCmStatusEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups

pbcCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 1, 1)
)
pbcCmtsGroup.setObjects(
      *(("PBC-CMTS-MIB", "pbcCmtsIfDownstreamNumEntries"),
        ("PBC-CMTS-MIB", "pbcCmtsIfDownstreamIfTxPower"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamNumEntries"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamPort"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamOperMode"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmdRcvdPwr"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamPowerLevel"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamHcsErrors"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCrcErrors"),
        ("PBC-CMTS-MIB", "pbcCmtsIfMacCmTotal"),
        ("PBC-CMTS-MIB", "pbcCmtsIfMacCmRangeAborted"),
        ("PBC-CMTS-MIB", "pbcCmtsIfMacCmRanging"),
        ("PBC-CMTS-MIB", "pbcCmtsIfMacCmRangingComplete"),
        ("PBC-CMTS-MIB", "pbcCmtsIfMacCmIpComplete"),
        ("PBC-CMTS-MIB", "pbcCmtsIfMacCmRegistered"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmTotal"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmRangeAborted"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmRanging"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmRangingComplete"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmIpComplete"),
        ("PBC-CMTS-MIB", "pbcCmtsRogueCmMacAddress"),
        ("PBC-CMTS-MIB", "pbcCmtsRogueCmIpAddress"),
        ("PBC-CMTS-MIB", "pbcCmtsRogueCmPtr"),
        ("PBC-CMTS-MIB", "pbcCmtsRogueCmType"),
        ("PBC-CMTS-MIB", "pbcCmtsRogueCmFirstActive"),
        ("PBC-CMTS-MIB", "pbcCmtsRogueCmLastActive"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusFirstOnline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusLastOnline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusTimesOnline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusPercentOnline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusMinOnline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusMaxOnline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusAvgOnline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusMinOffline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusMaxOffline"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStatusAvgOffline"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmRogue"),
        ("PBC-CMTS-MIB", "pbcCmtsIfMacCmRogue"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCER"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamMER"),
        ("PBC-CMTS-MIB", "pbcCmtsIfUpstreamCmRegistered"))
)
if mibBuilder.loadTexts:
    pbcCmtsGroup.setStatus("current")

pbcCableSpectrumManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 1, 2)
)
pbcCableSpectrumManagementGroup.setObjects(
      *(("PBC-CMTS-MIB", "pbcSpectrumAnalysisEnable"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisCmdStatus"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisIntegrationLen"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisFreqStep"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisFreqMin"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisFreqMax"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArraySize"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisActiveArray"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayIndex"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayStatus"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisFrequency"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisPower"),
        ("PBC-CMTS-MIB", "pbcCmtsSpectrumAnalysisEnableSweepNotification"),
        ("PBC-CMTS-MIB", "pbcSweepNotificationRecipient"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayScanStart"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayScanStop"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayIndexID"),
        ("PBC-CMTS-MIB", "pbcCardIfPortIndexID"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayStatusID"),
        ("PBC-CMTS-MIB", "pbcCmtsSpectrumAnalysisNotificationType"),
        ("PBC-CMTS-MIB", "pbcSweepNotificationRecipientPort"))
)
if mibBuilder.loadTexts:
    pbcCableSpectrumManagementGroup.setStatus("current")

pbcCmtsNotificationManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 1, 3)
)
pbcCmtsNotificationManagementGroup.setObjects(
      *(("PBC-CMTS-MIB", "pbcCmtsModemEventsEnable"),
        ("PBC-CMTS-MIB", "pbcCmtsNotificationsControl"),
        ("PBC-CMTS-MIB", "pbcCmtsEventsEnable"))
)
if mibBuilder.loadTexts:
    pbcCmtsNotificationManagementGroup.setStatus("current")

pbcFlapListManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 1, 5)
)
pbcFlapListManagementGroup.setObjects(
      *(("PBC-CMTS-MIB", "pbcCmtsFlapListAgeMinutes"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListIMRetryInterval"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListCERThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListMERThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListQPSKSNRThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListQAM16SNRThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListPowerAdjustThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListSMMissThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListFreqThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListSize"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlIMRetryInterval"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlCERThreshold"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlMERThreshold"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlQPSKSNRThreshold"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlQAM16SNRThreshold"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlPowerAdjustThreshold"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlSMMissThreshold"),
        ("PBC-CMTS-MIB", "pbcUsFlapListControlFreqThreshold"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListMacAddr"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListUpstreamIfIndex"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListDownstreamIfIndex"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListFlapCount"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListFlapCause"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListFreqDrift"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListEventsEnable"))
)
if mibBuilder.loadTexts:
    pbcFlapListManagementGroup.setStatus("current")


# Notification objects

pbcCmtsSpectrumAnalysisSweepComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 2, 2, 3, 1, 1)
)
pbcCmtsSpectrumAnalysisSweepComplete.setObjects(
      *(("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayIndexID"),
        ("PBC-CMTS-MIB", "pbcCardIfPortIndexID"),
        ("PBC-CMTS-MIB", "pbcSpectrumAnalysisArrayStatusID"))
)
if mibBuilder.loadTexts:
    pbcCmtsSpectrumAnalysisSweepComplete.setStatus(
        "current"
    )

pbcCmtsEnvMonNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 1)
)
pbcCmtsEnvMonNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsEnvMonNotification.setStatus(
        "current"
    )

pbcCmtsChassisNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 2)
)
pbcCmtsChassisNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsChassisNotification.setStatus(
        "current"
    )

pbcCmtsSoftwareNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 3)
)
pbcCmtsSoftwareNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsSoftwareNotification.setStatus(
        "current"
    )

pbcCmtsAccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 4)
)
pbcCmtsAccessNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsAccessNotification.setStatus(
        "current"
    )

pbcCmtsConfigNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 5)
)
pbcCmtsConfigNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsConfigNotification.setStatus(
        "current"
    )

pbcCmtsDataPathNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 6)
)
pbcCmtsDataPathNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsDataPathNotification.setStatus(
        "current"
    )

pbcCmtsRfInterfaceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 7)
)
pbcCmtsRfInterfaceNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsRfInterfaceNotification.setStatus(
        "current"
    )

pbcCmtsFlapListNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 8)
)
pbcCmtsFlapListNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsFlapListNotification.setStatus(
        "current"
    )

pbcCmtsDebugNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 9)
)
pbcCmtsDebugNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsDebugNotification.setStatus(
        "current"
    )

pbcCmtsCmStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 3, 3, 10)
)
pbcCmtsCmStateChangeNotification.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    pbcCmtsCmStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups

pbcCmtsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 1, 4)
)
pbcCmtsNotificationGroup.setObjects(
      *(("PBC-CMTS-MIB", "pbcCmtsEnvMonNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsSpectrumAnalysisSweepComplete"),
        ("PBC-CMTS-MIB", "pbcCmtsChassisNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsSoftwareNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsAccessNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsCmStateChangeNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsRfInterfaceNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsFlapListNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsDataPathNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsConfigNotification"),
        ("PBC-CMTS-MIB", "pbcCmtsDebugNotification"))
)
if mibBuilder.loadTexts:
    pbcCmtsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pbcCmtsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5987, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    pbcCmtsBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PBC-CMTS-MIB",
    **{"TenthdBmV": TenthdBmV,
       "TenthdB": TenthdB,
       "OneHundredthdBmVPerHz": OneHundredthdBmVPerHz,
       "pbcCmtsMib": pbcCmtsMib,
       "pbcCmts": pbcCmts,
       "pbcCmtsIfMibExtendedObjects": pbcCmtsIfMibExtendedObjects,
       "pbcGeneral": pbcGeneral,
       "pbcDownStreamMgmt": pbcDownStreamMgmt,
       "pbcCmtsIfDownstreamNumEntries": pbcCmtsIfDownstreamNumEntries,
       "pbcCmtsIfDownstreamChannelTable": pbcCmtsIfDownstreamChannelTable,
       "pbcCmtsIfDownstreamChannelEntry": pbcCmtsIfDownstreamChannelEntry,
       "pbcCmtsIfDownstreamIfTxPower": pbcCmtsIfDownstreamIfTxPower,
       "pbcUpStreamMgmt": pbcUpStreamMgmt,
       "pbcCmtsIfUpstreamNumEntries": pbcCmtsIfUpstreamNumEntries,
       "pbcCmtsIfUpstreamChannelTable": pbcCmtsIfUpstreamChannelTable,
       "pbcCmtsIfUpstreamChannelEntry": pbcCmtsIfUpstreamChannelEntry,
       "pbcCmtsIfUpstreamPort": pbcCmtsIfUpstreamPort,
       "pbcCmtsIfUpstreamOperMode": pbcCmtsIfUpstreamOperMode,
       "pbcCmtsIfUpstreamCmdRcvdPwr": pbcCmtsIfUpstreamCmdRcvdPwr,
       "pbcCmtsIfUpstreamPowerLevel": pbcCmtsIfUpstreamPowerLevel,
       "pbcCmtsIfUpstreamMER": pbcCmtsIfUpstreamMER,
       "pbcCmtsIfUpstreamHcsErrors": pbcCmtsIfUpstreamHcsErrors,
       "pbcCmtsIfUpstreamCrcErrors": pbcCmtsIfUpstreamCrcErrors,
       "pbcCmtsIfUpstreamCER": pbcCmtsIfUpstreamCER,
       "pbcCmtsIfUpstreamCmTotal": pbcCmtsIfUpstreamCmTotal,
       "pbcCmtsIfUpstreamCmRangeAborted": pbcCmtsIfUpstreamCmRangeAborted,
       "pbcCmtsIfUpstreamCmRanging": pbcCmtsIfUpstreamCmRanging,
       "pbcCmtsIfUpstreamCmRangingComplete": pbcCmtsIfUpstreamCmRangingComplete,
       "pbcCmtsIfUpstreamCmIpComplete": pbcCmtsIfUpstreamCmIpComplete,
       "pbcCmtsIfUpstreamCmRegistered": pbcCmtsIfUpstreamCmRegistered,
       "pbcCmtsIfUpstreamCmRogue": pbcCmtsIfUpstreamCmRogue,
       "pbcMacMgmt": pbcMacMgmt,
       "pbcCmtsIfMacTable": pbcCmtsIfMacTable,
       "pbcCmtsIfMacEntry": pbcCmtsIfMacEntry,
       "pbcCmtsIfMacCmTotal": pbcCmtsIfMacCmTotal,
       "pbcCmtsIfMacCmRangeAborted": pbcCmtsIfMacCmRangeAborted,
       "pbcCmtsIfMacCmRanging": pbcCmtsIfMacCmRanging,
       "pbcCmtsIfMacCmRangingComplete": pbcCmtsIfMacCmRangingComplete,
       "pbcCmtsIfMacCmIpComplete": pbcCmtsIfMacCmIpComplete,
       "pbcCmtsIfMacCmRegistered": pbcCmtsIfMacCmRegistered,
       "pbcCmtsIfMacCmRogue": pbcCmtsIfMacCmRogue,
       "pbcCmtsCmMgmt": pbcCmtsCmMgmt,
       "pbcCmtsCmStatusTable": pbcCmtsCmStatusTable,
       "pbcCmtsCmStatusEntry": pbcCmtsCmStatusEntry,
       "pbcCmtsCmStatusFirstOnline": pbcCmtsCmStatusFirstOnline,
       "pbcCmtsCmStatusLastOnline": pbcCmtsCmStatusLastOnline,
       "pbcCmtsCmStatusTimesOnline": pbcCmtsCmStatusTimesOnline,
       "pbcCmtsCmStatusPercentOnline": pbcCmtsCmStatusPercentOnline,
       "pbcCmtsCmStatusMinOnline": pbcCmtsCmStatusMinOnline,
       "pbcCmtsCmStatusMaxOnline": pbcCmtsCmStatusMaxOnline,
       "pbcCmtsCmStatusAvgOnline": pbcCmtsCmStatusAvgOnline,
       "pbcCmtsCmStatusMinOffline": pbcCmtsCmStatusMinOffline,
       "pbcCmtsCmStatusMaxOffline": pbcCmtsCmStatusMaxOffline,
       "pbcCmtsCmStatusAvgOffline": pbcCmtsCmStatusAvgOffline,
       "pbcCmtsRogueCmTable": pbcCmtsRogueCmTable,
       "pbcCmtsRogueCmEntry": pbcCmtsRogueCmEntry,
       "pbcCmtsRogueCmMacAddress": pbcCmtsRogueCmMacAddress,
       "pbcCmtsRogueCmIpAddress": pbcCmtsRogueCmIpAddress,
       "pbcCmtsRogueCmPtr": pbcCmtsRogueCmPtr,
       "pbcCmtsRogueCmType": pbcCmtsRogueCmType,
       "pbcCmtsRogueCmFirstActive": pbcCmtsRogueCmFirstActive,
       "pbcCmtsRogueCmLastActive": pbcCmtsRogueCmLastActive,
       "pbcCmtsCableSpectrumManagement": pbcCmtsCableSpectrumManagement,
       "pbcCmtsSpectrumAnalysisMgmt": pbcCmtsSpectrumAnalysisMgmt,
       "pbcCmtsSpectrumAnalysisObjects": pbcCmtsSpectrumAnalysisObjects,
       "pbcSpectrumAnalysisRFInputTable": pbcSpectrumAnalysisRFInputTable,
       "pbcSpectrumAnalysisRFInputEntry": pbcSpectrumAnalysisRFInputEntry,
       "pbcSpectrumAnalysisEnable": pbcSpectrumAnalysisEnable,
       "pbcSpectrumAnalysisCmdStatus": pbcSpectrumAnalysisCmdStatus,
       "pbcSpectrumAnalysisIntegrationLen": pbcSpectrumAnalysisIntegrationLen,
       "pbcSpectrumAnalysisFreqStep": pbcSpectrumAnalysisFreqStep,
       "pbcSpectrumAnalysisFreqMin": pbcSpectrumAnalysisFreqMin,
       "pbcSpectrumAnalysisFreqMax": pbcSpectrumAnalysisFreqMax,
       "pbcSpectrumAnalysisArraySize": pbcSpectrumAnalysisArraySize,
       "pbcSpectrumAnalysisActiveArray": pbcSpectrumAnalysisActiveArray,
       "pbcSpectrumAnalysisArrayIndexTable": pbcSpectrumAnalysisArrayIndexTable,
       "pbcSpectrumAnalysisArrayIndexEntry": pbcSpectrumAnalysisArrayIndexEntry,
       "pbcSpectrumAnalysisArrayIndex": pbcSpectrumAnalysisArrayIndex,
       "pbcSpectrumAnalysisArrayStatus": pbcSpectrumAnalysisArrayStatus,
       "pbcSpectrumAnalysisArrayScanStart": pbcSpectrumAnalysisArrayScanStart,
       "pbcSpectrumAnalysisArrayScanStop": pbcSpectrumAnalysisArrayScanStop,
       "pbcSpectrumAnalysisDataTable": pbcSpectrumAnalysisDataTable,
       "pbcSpectrumAnalysisDataEntry": pbcSpectrumAnalysisDataEntry,
       "pbcSpectrumAnalysisFrequency": pbcSpectrumAnalysisFrequency,
       "pbcSpectrumAnalysisPower": pbcSpectrumAnalysisPower,
       "pbcCmtsSpectrumAnalysisNotificationEnables": pbcCmtsSpectrumAnalysisNotificationEnables,
       "pbcCmtsSpectrumAnalysisNotificationTable": pbcCmtsSpectrumAnalysisNotificationTable,
       "pbcCmtsSpectrumAnalysisNotificationEntry": pbcCmtsSpectrumAnalysisNotificationEntry,
       "pbcCmtsSpectrumAnalysisEnableSweepNotification": pbcCmtsSpectrumAnalysisEnableSweepNotification,
       "pbcSweepNotificationRecipient": pbcSweepNotificationRecipient,
       "pbcSweepNotificationRecipientPort": pbcSweepNotificationRecipientPort,
       "pbcCmtsSpectrumAnalysisNotificationType": pbcCmtsSpectrumAnalysisNotificationType,
       "pbcCmtsSpectrumAnalysisNotificationPrefix": pbcCmtsSpectrumAnalysisNotificationPrefix,
       "pbcCmtsSpectrumAnalysisNotifications": pbcCmtsSpectrumAnalysisNotifications,
       "pbcCmtsSpectrumAnalysisSweepComplete": pbcCmtsSpectrumAnalysisSweepComplete,
       "pbcCardIfPortIndexID": pbcCardIfPortIndexID,
       "pbcSpectrumAnalysisArrayIndexID": pbcSpectrumAnalysisArrayIndexID,
       "pbcSpectrumAnalysisArrayStatusID": pbcSpectrumAnalysisArrayStatusID,
       "pbcCmtsNotificationManagement": pbcCmtsNotificationManagement,
       "pbcCmtsEventsEnable": pbcCmtsEventsEnable,
       "pbcCmtsNotificationsControl": pbcCmtsNotificationsControl,
       "pbcCmtsSystemNotifications": pbcCmtsSystemNotifications,
       "pbcCmtsEnvMonNotification": pbcCmtsEnvMonNotification,
       "pbcCmtsChassisNotification": pbcCmtsChassisNotification,
       "pbcCmtsSoftwareNotification": pbcCmtsSoftwareNotification,
       "pbcCmtsAccessNotification": pbcCmtsAccessNotification,
       "pbcCmtsConfigNotification": pbcCmtsConfigNotification,
       "pbcCmtsDataPathNotification": pbcCmtsDataPathNotification,
       "pbcCmtsRfInterfaceNotification": pbcCmtsRfInterfaceNotification,
       "pbcCmtsFlapListNotification": pbcCmtsFlapListNotification,
       "pbcCmtsDebugNotification": pbcCmtsDebugNotification,
       "pbcCmtsCmStateChangeNotification": pbcCmtsCmStateChangeNotification,
       "pbcCmtsModemEventsEnable": pbcCmtsModemEventsEnable,
       "pbcCmtsConformance": pbcCmtsConformance,
       "pbcCmtsGroups": pbcCmtsGroups,
       "pbcCmtsGroup": pbcCmtsGroup,
       "pbcCableSpectrumManagementGroup": pbcCableSpectrumManagementGroup,
       "pbcCmtsNotificationManagementGroup": pbcCmtsNotificationManagementGroup,
       "pbcCmtsNotificationGroup": pbcCmtsNotificationGroup,
       "pbcFlapListManagementGroup": pbcFlapListManagementGroup,
       "pbcCmtsCompliances": pbcCmtsCompliances,
       "pbcCmtsBasicCompliance": pbcCmtsBasicCompliance,
       "pbcFlapListManagement": pbcFlapListManagement,
       "pbcFlapListObjects": pbcFlapListObjects,
       "pbcCmtsFlapListAgeMinutes": pbcCmtsFlapListAgeMinutes,
       "pbcCmtsFlapListIMRetryInterval": pbcCmtsFlapListIMRetryInterval,
       "pbcCmtsFlapListCERThreshold": pbcCmtsFlapListCERThreshold,
       "pbcCmtsFlapListMERThreshold": pbcCmtsFlapListMERThreshold,
       "pbcCmtsFlapListQPSKSNRThreshold": pbcCmtsFlapListQPSKSNRThreshold,
       "pbcCmtsFlapListQAM16SNRThreshold": pbcCmtsFlapListQAM16SNRThreshold,
       "pbcCmtsFlapListPowerAdjustThreshold": pbcCmtsFlapListPowerAdjustThreshold,
       "pbcCmtsFlapListSMMissThreshold": pbcCmtsFlapListSMMissThreshold,
       "pbcCmtsFlapListFreqThreshold": pbcCmtsFlapListFreqThreshold,
       "pbcCmtsFlapListSize": pbcCmtsFlapListSize,
       "pbcUsFlapListControlTable": pbcUsFlapListControlTable,
       "pbcUsFlapListControlEntry": pbcUsFlapListControlEntry,
       "pbcUsFlapListControlIMRetryInterval": pbcUsFlapListControlIMRetryInterval,
       "pbcUsFlapListControlCERThreshold": pbcUsFlapListControlCERThreshold,
       "pbcUsFlapListControlMERThreshold": pbcUsFlapListControlMERThreshold,
       "pbcUsFlapListControlQPSKSNRThreshold": pbcUsFlapListControlQPSKSNRThreshold,
       "pbcUsFlapListControlQAM16SNRThreshold": pbcUsFlapListControlQAM16SNRThreshold,
       "pbcUsFlapListControlPowerAdjustThreshold": pbcUsFlapListControlPowerAdjustThreshold,
       "pbcUsFlapListControlSMMissThreshold": pbcUsFlapListControlSMMissThreshold,
       "pbcUsFlapListControlFreqThreshold": pbcUsFlapListControlFreqThreshold,
       "pbcCmtsFlapListTable": pbcCmtsFlapListTable,
       "pbcCmtsFlapListEntry": pbcCmtsFlapListEntry,
       "pbcCmtsFlapListMacAddr": pbcCmtsFlapListMacAddr,
       "pbcCmtsFlapListUpstreamIfIndex": pbcCmtsFlapListUpstreamIfIndex,
       "pbcCmtsFlapListDownstreamIfIndex": pbcCmtsFlapListDownstreamIfIndex,
       "pbcCmtsFlapListFlapCount": pbcCmtsFlapListFlapCount,
       "pbcCmtsFlapListFlapCause": pbcCmtsFlapListFlapCause,
       "pbcCmtsFlapListFreqDrift": pbcCmtsFlapListFreqDrift,
       "pbcCmtsFlapListEventsEnable": pbcCmtsFlapListEventsEnable,
       "pbcG10CMTS": pbcG10CMTS,
       "pbcG1CMTS": pbcG1CMTS}
)
