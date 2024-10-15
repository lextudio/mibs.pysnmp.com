# SNMP MIB module (BIANCA-BRICK-SERIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-SERIAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:45 2024
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



class Date(Integer32):
    """Custom type Date based on Integer32"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Serial_ObjectIdentity = ObjectIdentity
serial = _Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 25)
)
_SerialIfTable_Object = MibTable
serialIfTable = _SerialIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1)
)
if mibBuilder.loadTexts:
    serialIfTable.setStatus("mandatory")
_SerialIfEntry_Object = MibTableRow
serialIfEntry = _SerialIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1)
)
serialIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-SERIAL-MIB", "serialIfIndex"),
)
if mibBuilder.loadTexts:
    serialIfEntry.setStatus("mandatory")
_SerialIfIndex_Type = Integer32
_SerialIfIndex_Object = MibTableColumn
serialIfIndex = _SerialIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 1),
    _SerialIfIndex_Type()
)
serialIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfIndex.setStatus("mandatory")


class _SerialIfType_Type(Integer32):
    """Custom type serialIfType based on Integer32"""
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
        *(("none", 1),
          ("v35", 3),
          ("v36", 4),
          ("x21", 2),
          ("x21bis", 5))
    )


_SerialIfType_Type.__name__ = "Integer32"
_SerialIfType_Object = MibTableColumn
serialIfType = _SerialIfType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 2),
    _SerialIfType_Type()
)
serialIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIfType.setStatus("mandatory")


class _SerialIfConnector_Type(Integer32):
    """Custom type serialIfConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_SerialIfConnector_Type.__name__ = "Integer32"
_SerialIfConnector_Object = MibTableColumn
serialIfConnector = _SerialIfConnector_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 3),
    _SerialIfConnector_Type()
)
serialIfConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIfConnector.setStatus("mandatory")


class _SerialIfLeads_Type(Integer32):
    """Custom type serialIfLeads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SerialIfLeads_Type.__name__ = "Integer32"
_SerialIfLeads_Object = MibTableColumn
serialIfLeads = _SerialIfLeads_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 4),
    _SerialIfLeads_Type()
)
serialIfLeads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIfLeads.setStatus("mandatory")


class _SerialIfClock_Type(Integer32):
    """Custom type serialIfClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("extern", 2),
          ("intern", 3))
    )


_SerialIfClock_Type.__name__ = "Integer32"
_SerialIfClock_Object = MibTableColumn
serialIfClock = _SerialIfClock_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 5),
    _SerialIfClock_Type()
)
serialIfClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIfClock.setStatus("mandatory")
_SerialIfSpeed_Type = Integer32
_SerialIfSpeed_Object = MibTableColumn
serialIfSpeed = _SerialIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 8),
    _SerialIfSpeed_Type()
)
serialIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIfSpeed.setStatus("mandatory")


class _SerialIfL2Mode_Type(Integer32):
    """Custom type serialIfL2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("dce", 2),
          ("dte", 1))
    )


_SerialIfL2Mode_Type.__name__ = "Integer32"
_SerialIfL2Mode_Object = MibTableColumn
serialIfL2Mode = _SerialIfL2Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 10),
    _SerialIfL2Mode_Type()
)
serialIfL2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIfL2Mode.setStatus("mandatory")


class _SerialIfL1State_Type(Integer32):
    """Custom type serialIfL1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dn", 1),
          ("up", 2))
    )


_SerialIfL1State_Type.__name__ = "Integer32"
_SerialIfL1State_Object = MibTableColumn
serialIfL1State = _SerialIfL1State_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 15),
    _SerialIfL1State_Type()
)
serialIfL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfL1State.setStatus("mandatory")
_SerialIfSpeedReal_Type = Integer32
_SerialIfSpeedReal_Object = MibTableColumn
serialIfSpeedReal = _SerialIfSpeedReal_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 16),
    _SerialIfSpeedReal_Type()
)
serialIfSpeedReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfSpeedReal.setStatus("mandatory")
_SerialIfRxPackets_Type = Counter32
_SerialIfRxPackets_Object = MibTableColumn
serialIfRxPackets = _SerialIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 20),
    _SerialIfRxPackets_Type()
)
serialIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfRxPackets.setStatus("mandatory")
_SerialIfRxOctets_Type = Counter32
_SerialIfRxOctets_Object = MibTableColumn
serialIfRxOctets = _SerialIfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 21),
    _SerialIfRxOctets_Type()
)
serialIfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfRxOctets.setStatus("mandatory")
_SerialIfTxPackets_Type = Counter32
_SerialIfTxPackets_Object = MibTableColumn
serialIfTxPackets = _SerialIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 22),
    _SerialIfTxPackets_Type()
)
serialIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfTxPackets.setStatus("mandatory")
_SerialIfTxOctets_Type = Counter32
_SerialIfTxOctets_Object = MibTableColumn
serialIfTxOctets = _SerialIfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 23),
    _SerialIfTxOctets_Type()
)
serialIfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfTxOctets.setStatus("mandatory")
_SerialIfRxResets_Type = Counter32
_SerialIfRxResets_Object = MibTableColumn
serialIfRxResets = _SerialIfRxResets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 24),
    _SerialIfRxResets_Type()
)
serialIfRxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfRxResets.setStatus("mandatory")
_SerialIfRxAborts_Type = Counter32
_SerialIfRxAborts_Object = MibTableColumn
serialIfRxAborts = _SerialIfRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 25),
    _SerialIfRxAborts_Type()
)
serialIfRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfRxAborts.setStatus("mandatory")
_SerialIfRxOverruns_Type = Counter32
_SerialIfRxOverruns_Object = MibTableColumn
serialIfRxOverruns = _SerialIfRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 26),
    _SerialIfRxOverruns_Type()
)
serialIfRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfRxOverruns.setStatus("mandatory")
_SerialIfRxCRCErrors_Type = Counter32
_SerialIfRxCRCErrors_Object = MibTableColumn
serialIfRxCRCErrors = _SerialIfRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 27),
    _SerialIfRxCRCErrors_Type()
)
serialIfRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfRxCRCErrors.setStatus("mandatory")
_SerialIfRxGiantFrames_Type = Counter32
_SerialIfRxGiantFrames_Object = MibTableColumn
serialIfRxGiantFrames = _SerialIfRxGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 28),
    _SerialIfRxGiantFrames_Type()
)
serialIfRxGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfRxGiantFrames.setStatus("mandatory")
_SerialIfTxResets_Type = Counter32
_SerialIfTxResets_Object = MibTableColumn
serialIfTxResets = _SerialIfTxResets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 29),
    _SerialIfTxResets_Type()
)
serialIfTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfTxResets.setStatus("mandatory")
_SerialIfTxAborts_Type = Counter32
_SerialIfTxAborts_Object = MibTableColumn
serialIfTxAborts = _SerialIfTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 30),
    _SerialIfTxAborts_Type()
)
serialIfTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfTxAborts.setStatus("mandatory")
_SerialIfTxUnderruns_Type = Counter32
_SerialIfTxUnderruns_Object = MibTableColumn
serialIfTxUnderruns = _SerialIfTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 31),
    _SerialIfTxUnderruns_Type()
)
serialIfTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfTxUnderruns.setStatus("mandatory")
_SerialIfTxGiantFrames_Type = Counter32
_SerialIfTxGiantFrames_Object = MibTableColumn
serialIfTxGiantFrames = _SerialIfTxGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 25, 1, 1, 32),
    _SerialIfTxGiantFrames_Type()
)
serialIfTxGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialIfTxGiantFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-SERIAL-MIB",
    **{"Date": Date,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "serial": serial,
       "serialIfTable": serialIfTable,
       "serialIfEntry": serialIfEntry,
       "serialIfIndex": serialIfIndex,
       "serialIfType": serialIfType,
       "serialIfConnector": serialIfConnector,
       "serialIfLeads": serialIfLeads,
       "serialIfClock": serialIfClock,
       "serialIfSpeed": serialIfSpeed,
       "serialIfL2Mode": serialIfL2Mode,
       "serialIfL1State": serialIfL1State,
       "serialIfSpeedReal": serialIfSpeedReal,
       "serialIfRxPackets": serialIfRxPackets,
       "serialIfRxOctets": serialIfRxOctets,
       "serialIfTxPackets": serialIfTxPackets,
       "serialIfTxOctets": serialIfTxOctets,
       "serialIfRxResets": serialIfRxResets,
       "serialIfRxAborts": serialIfRxAborts,
       "serialIfRxOverruns": serialIfRxOverruns,
       "serialIfRxCRCErrors": serialIfRxCRCErrors,
       "serialIfRxGiantFrames": serialIfRxGiantFrames,
       "serialIfTxResets": serialIfTxResets,
       "serialIfTxAborts": serialIfTxAborts,
       "serialIfTxUnderruns": serialIfTxUnderruns,
       "serialIfTxGiantFrames": serialIfTxGiantFrames}
)
